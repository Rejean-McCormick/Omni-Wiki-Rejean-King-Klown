# RAG Memory System

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft uses **Retrieval Augmented Generation (RAG)** as an explicit long-term memory layer to maintain continuity across large stories.

RAG is not the Story Bible (intent).  
RAG is not the Matrix (runtime state).  
RAG is **evidence**: previously written text and relevant notes that can be retrieved and injected into the current Part’s prompt.

---

## 1) Why RAG Exists

LLMs have limited context windows. Without memory, long projects drift:
- character traits change
- facts get contradicted
- timeline breaks
- names/places mutate

RAG solves this by:
- indexing written prose and notes as searchable chunks
- retrieving only the top relevant snippets for the active Part
- injecting them as bounded “evidence” during drafting and review

---

## 2) What RAG Stores

Recommended indexed sources:
- Part manuscripts (`data/manuscripts/*.md`)
- Editor notes (optional)
- stable reference notes (optional, if you want them searchable)

RAG SHOULD store per-chunk metadata:
- `project_id`
- `part_id` (if applicable)
- `chapter_id` (if applicable)
- `source_path`
- `timestamp`
- optional tags (character names, location IDs)

RAG MUST NOT be treated as canonical intent. If RAG conflicts with Story Bible, Story Bible wins.

See: **[Story Bible](Story-Bible-Creative-Intent.md)**

---

## 3) Storage Location (Per Project)

Recommended location:
- `projects/<project_id>/data/memory_db/`

This ensures multi-project isolation and avoids cross-story contamination.

See: **[Multi-Project Management](Multi-Project-Management.md)**

---

## 4) Ingestion (Write Path)

Ingestion typically occurs during **SCAN**.

Flow:
1. Scanner detects changed manuscript files.
2. File is chunked into semantic segments (paragraphs or sections).
3. Each chunk is embedded (vectorized).
4. Vectors + metadata are stored in the project’s vector database.

Deterministic pipeline: **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

### 4.1 Chunking recommendations
- chunk by paragraph boundaries when possible
- target 150–500 tokens per chunk (implementation-dependent)
- include stable headers in metadata rather than duplicating them in every chunk

### 4.2 Deduplication recommendations
- hash chunk text + source to avoid re-inserting identical chunks
- update metadata timestamps on re-ingest

---

## 5) Retrieval (Read Path)

Retrieval occurs during **prompt hydration** for a Part.

Flow:
1. Orchestrator builds a query set from:
   - the Part contract fields (goal/obstacle/turn/outcome)
   - high-signal beats (Plot/Conflict)
   - explicit continuity questions (if present)
2. Vector search returns top-k relevant chunks.
3. Orchestrator formats them as “evidence” and injects them into the prompt.

Prompt hydration: **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

### 5.1 Bounded retrieval (required)
To prevent prompt bloat:
- `top_k` MUST be bounded (e.g., 5–10)
- total evidence tokens MUST be bounded
- prefer fewer, higher-confidence chunks over many weak chunks

### 5.2 Evidence formatting (recommended)
Format each retrieved chunk with:
- source + part ID
- a short excerpt
- optional “why retrieved” hint

Example:

```text
[RAG] Source: P014.md (CH05 / P014)
- "Mara always keeps her left hand gloved..."
````

---

## 6) RAG in Drafting vs Reviewing

### 6.1 Narrator (Draft/Revise)

Use RAG to:

* preserve continuity facts
* recall prior scene outcomes
* maintain consistent voice and details

### 6.2 Editor (Review)

Use RAG to:

* verify consistency (“does this contradict earlier text?”)
* confirm details (names, timeline, injuries, locations)

Editor should treat RAG as evidence, not instructions.

---

## 7) Interfaces and Tools (Recommended)

Expose RAG through a small tool surface, e.g.:

* `memory.query(text, top_k=...)`
* optional: `memory.query_filters(part_id=..., chapter_id=...)`

Recommended role rules:

* Narrator can request retrieval through orchestrator hydration, but does not directly call DB.
* Editor may call a controlled `check_memory` tool for spot checks.

---

## 8) Failure Modes and Guards

* **Hallucinated “memories”**: mitigate by only injecting retrieved text excerpts.
* **Cross-project bleed**: mitigate with per-project DB path + required `project_id` filter.
* **Contradicting intent**: Story Bible overrides RAG; Editor should flag conflicts.
* **Prompt overflow**: enforce strict token budgets for evidence.

---

## 9) Related Pages

* **[Architecture Overview](Architecture-Overview.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**
* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
* **[Story Bible](Story-Bible-Creative-Intent.md)**
* **[Central Matrix](Central-Matrix-Runtime-State.md)**

