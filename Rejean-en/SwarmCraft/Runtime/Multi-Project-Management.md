# Multi-Project Management

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft supports multiple isolated projects (“universes”) in the same repository/runtime.

A **project** is an isolated unit that contains:
- its own Story Bible (templates + outline + references)
- its own Central Matrix (runtime state)
- its own RAG Memory DB
- its own manuscripts and logs (recommended)

This prevents cross-story contamination and enables switching between worlds without restarting the whole engine.

---

## 1) Project Root Structure (Recommended)

SwarmCraft SHOULD use a `projects/` root:

```text
root/
└── projects/
    ├── .last_project
    │
    ├── project_alpha/
    │   └── data/
    │       ├── matrix.json
    │       ├── story_bible/
    │       │   ├── outline.json
    │       │   └── templates/
    │       ├── memory_db/
    │       └── manuscripts/
    │
    └── project_beta/
        └── data/
            ├── matrix.json
            ├── story_bible/
            ├── memory_db/
            └── manuscripts/
````

Notes:

* `projects/<project_id>/data/` is the canonical project data root.
* Manuscripts under `data/manuscripts/` is recommended to keep everything portable.

---

## 2) Project Identity

Each project is identified by its folder name:

* `project_id = "project_alpha"`

The project ID should be:

* stable (do not rename casually)
* filesystem-safe (ASCII, no spaces recommended)

---

## 3) What Isolated Means (Normative)

For correctness, projects MUST NOT share:

* `matrix.json` (runtime state)
* `story_bible/` (creative intent)
* `memory_db/` (RAG vectors)

If your implementation uses global caches, they MUST be keyed by `project_id`.

---

## 4) Switching Projects

A project manager component (implementation detail) typically supports:

* list available projects
* set active project
* remember last active project

### 4.1 `.last_project` (Recommended)

A simple pointer file:

* `projects/.last_project`

Contents:

```text
project_alpha
```

On startup:

* if an explicit project is not chosen, engine loads `.last_project`
* if missing, engine may prompt or choose a default (implementation choice)

---

## 5) Per-Project Lifecycle

### 5.1 Create a project (Recommended behavior)

Creating a project should:

1. Create `projects/<project_id>/data/`
2. Create an initial Story Bible structure:

   * `story_bible/templates/`
   * `story_bible/outline.json` (blank scaffold)
3. Initialize `matrix.json` (empty/initial state)
4. Initialize `memory_db/` (empty DB folder)
5. Optionally create `manuscripts/` folder

### 5.2 Delete a project (Recommended behavior)

Deletion should be explicit and guarded.
Recommended to require a confirmation flag.

---

## 6) How Multi-Project Interacts with the Pipeline

In the deterministic loop, the orchestrator operates against exactly one active project:

* SCAN reads/writes `projects/<id>/data/*`
* PLAN selects the next Part within that project
* EXECUTE writes manuscripts and updates Matrix within that project
* RAG ingestion/retrieval is scoped to that project’s `memory_db/`

Pipeline: **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 7) Dashboard Considerations

The dashboard should clearly display:

* active project ID
* active part/chapter target
* per-project token usage (session + optional totals)
* health/integrity signals for that project only

Dashboard: **[Dashboard TUI Reference](Dashboard-TUI-Reference.md)**

---

## 8) Related Pages

* **[Central Matrix](Central-Matrix-Runtime-State.md)**
* **[Story Bible](Story-Bible-Creative-Intent.md)**
* **[RAG Memory System](RAG-Memory-System.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**


