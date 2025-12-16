##  SenTient (Semantic Entity Intelligent Transformation)

**Version:** 1.0.0-RC2
**Status:** Production Ready (Hybrid Architecture)

---

## 1.  Executive Summary and Core Philosophy

**SenTient** is a next-generation Entity Reconciliation and Relation Extraction engine designed to bridge the gap between messy, unstructured text and structured Knowledge Graphs (Wikidata/Wikibase).

The core philosophy is a **Hybrid Orchestration System** that combines three distinct technological lineages into a single "Funnel" pipeline to achieve high performance and accuracy:

* **Speed (Layer 1):** The FST-based rapid tagging of **OpenTapioca** (Solr).
* **Semantics (Layer 2):** The context-aware NLP of **Falcon 2.0** (Python/SBERT/Elastic).
* **Structure (Layer 3):** The robust data modeling and state management of **OpenRefine** (Java Core + DuckDB).

### Key Architectural Features
* **Performance Target:** High Precision ($>0.85$) and High Recall ($>0.80$) while maintaining a sub-second response time for user interactivity.
* **Hybrid Memory Architecture:** The Java Core uses a split-state strategy, keeping lightweight status flags and Row IDs in **Hot RAM** for instant faceting, while offloading heavy AI payloads (vectors, candidates, scores) to a **DuckDB Sidecar** (Cold Data). This approach supports datasets exceeding 5GB.
* **Decoupled Frontend:** The UI (React/Vite on Port `3000`) is decoupled from the Java Core (Jetty on Port `3333`) and communicates via a REST-like Command Pattern API.

---

## 2.  The Three-Layer Funnel and Processing Pipeline

The system operates on a "Funnel" logic: broad and fast at the top, narrow and precise at the bottom. The unit of work is the **SmartCell** object, which acts as the immutable contract across all layers.

### 2.1. Layer 1: Ingestion & Fast Tagging (The Sieve)
* **Component:** `index_solr` + `core_java (Clustering)`.
* **Role:** High-speed identification of "Surface Forms" using string matching and pre-calculated popularity.
* **Latency Budget:** Must be **< 50ms per batch**.
* **Process Flow:**
    1.  **Normalization & Fingerprinting:** Java performs client-side deduplication using the **Key Collision Fingerprint** algorithm (tokenize, clean, sort, join) to minimize Solr API calls.
    2.  **FST Tagger:** The normalized text is passed to the **Solr TaggerHandler**, which uses a memory-mapped **Finite State Transducer (FST)** containing $\approx 14M$ Wikidata items. Lookup time is $O(k)$.
    3.  **Authority Filter:** Candidates with low `popularity_score` ($< 100$) or those matching stop words are immediately pruned.

### 2.2. Layer 2: The Semantic Linguist (Falcon 2.0)
* **Component:** `nlp_falcon` (Python 3.9+, Flask, SBERT).
* **Role:** Contextual disambiguation (solving the "Paris Problem") and semantic analysis.
* **Latency Budget:** $\approx 200ms$ per entity batch (Target).
* **Process Flow:**
    1.  **Preprocessing:** **Falcon Optimization** uses stopword pruning (`falcon_extended_en.txt`) and N-Gram generation to clean the signal.
    2.  **Property Extraction (Edge Detector):** Queries the `sentient_properties_v1` ElasticSearch index to infer the most likely **Wikidata Property (Predicate)**, boosting or penalizing entity candidates accordingly.
    3.  **Vector Scoring:** Encodes the 5-word context window into a 768-dimensional vector using **SBERT** (`all-MiniLM-L6-v2`). It then calculates **Cosine Similarity** ($S_{\text{Context}}$) between the input vector and candidate description vectors fetched from the `sentient_entities_fallback` Elastic index.

### 2.3. Layer 3: The Core Orchestrator (Final Adjudication)
* **Component:** `core_java` (Java 17, Jetty 10, Butterfly Framework).
* **Role:** Final Adjudication, Asynchronous Process Management, and State Serialization.
* **Process Flow:**
    1.  **Async Management:** Frontend triggers a **Command** (`ReconcileCommand`), which launches a non-blocking `LongRunningProcess` managed by the `ProcessManager` (utilizing a `ThreadPoolExecutorAdapter`). The Frontend polls for progress.
    2.  **Consensus Scoring:** Upon receiving Layer 2 scores, the Core performs **Score Normalization** (using a Sigmoid function with $k=2.0$, $m=3.0$) on Solr's raw $\log_{score}$ to map it to a [0, 1] range. It then applies the final weighted formula:
        $$\text{Score}_{\text{Sentry}} = (S_{\text{Normalized}} \times 0.4) + (S_{\text{Falcon}} \times 0.3) + (S_{\text{Levenshtein}} \times 0.3) \text{}$$
    3.  **Data Offload:** The orchestrator calls `DuckDBStore.insertBatch()` to persist heavy vectors to disk and flags the in-memory **Cell** as `RECONCILED` (lightweight state).
    4.  **History & Serialization:** Every data modification is a **Transaction** implementing the `AbstractOperation` Command Pattern, ensuring that state can be restored by re-applying the History log upon server crash.

---

## 3.  QA, Validation & Benchmarking

The QA Strategy relies on three pillars to statistically prove system improvement over time.

### 3.1. The Scrutinizers (Runtime Validation)
Scrutinizers are "Linting Rules for Data" located in `config/qa/scrutinizer_rules.yaml`. They run in the Java Core *before* export.
* **Integrity Scrutinizers:** Block export if data is logically corrupt (e.g., `MATCHED` cell has a null QID).
* **Constraint Scrutinizers:** Check for Wikidata alignment violations (e.g., Single Value Constraint) and show a `WARNING`.
* **Consensus Scrutinizers:** Check for statistical anomalies in scores (e.g., "Paris Hilton Rule": high popularity but low context score).

### 3.2. Golden Standard Datasets
Accuracy is measured against ground truth using industry-standard datasets:
* **LC-QuAD 2.0:** Validating complex relation extraction.
* **SimpleQuestions:** Validating simple entity spotting speed (Target Latency $< 50ms$/query).
* **WebQSP:** Testing disambiguation of ambiguous surface forms.

### 3.3. Benchmarking & Deployment Guardrail
The `evaluate_falcon_api.py` script runs the full pipeline.

| Metric | Target (v1.0) | Acceptable Range |
| :--- | :--- | :--- |
| **Precision** | 0.85 | $> 0.80$ |
| **Recall** | 0.82 | $> 0.75$ |
| **F-Score** | 0.83 | $> 0.78$ |
| **Latency (p95)** | 200ms | $< 500ms$ |

**Deployment Rule:** If Precision drops by $> 2\%$ after a model update (e.g., SBERT or Solr FST index), the deployment is **rejected**.

---

## 4.  Data Dictionary: The SmartCell Protocol

The **SmartCell** is the immutable data contract defined in `schemas/data/smart_cell.json`.

| Logical Field | JSON Type | Java Type | Python Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `raw_value` | `String` | `String` | `str` | Original user input (never modified) |
| `status` | `Enum (String)` | `Recon.Judgment` | `str` | Current lifecycle state (`NEW`, `PENDING`, `MATCHED`, etc.) |
| `consensus_score` | `Float` | `float` (transient) | `float` | Final calculated confidence (0.0 to 1.0) |
| `match` | `Candidate` Obj | `ReconCandidate` | `dict` | The single winning entity (if reconciled) |
| `vector` | `Array<Float>` | `double[]` | `np.ndarray` | SBERT embedding payload |

### Telemetry (`features`)
The `Candidate` object contains a `features` object used for UI visualization and debugging. The Frontend renders a stacked bar chart based on these weights:
* `tapioca_popularity` (Solr Log-Likelihood).
* `falcon_context` (Cosine Similarity from SBERT).
* `levenshtein_distance` (Normalized string distance from Java Core).

---

## 5.  Wiring & Configuration Strategy

### Network Topology (Port Map)
All services are bound strictly to `127.0.0.1` for security.

| Service | Port | Protocol | Timeout |
| :--- | :--- | :--- | :--- |
| **Java Core (Orchestrator)** | `3333` | HTTP/1.1 | - |
| **Falcon (Python)** | `5005` | HTTP/1.1 | 120s (Throttled) |
| **Solr (Tapioca)** | `8983` | HTTP/2 | 500ms (Strict) |
| **ElasticSearch** | `9200` | HTTP/TCP | - |

### File System Layout
The central configuration files are located in `config/orchestration/environment.json` and other files within the `config/` directory.

