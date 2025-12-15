# Architecture Overview

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft is a **deterministic, data-driven story engine**. It transforms explicit project state into prose using a strict control loop and a layered architecture that separates:

- **Brain** (LLM personas and prompt behaviors)
- **Logic** (orchestration, tools, validation)
- **Memory** (project state files + RAG index)

---

## 1) The Three-Layer Model (Brain / Logic / Memory)

### Brain (LLM Personas)
Stateless services that generate or evaluate content. They never own canonical state.

Typical personas:
- **Architect**: plans next actions and targets
- **Narrator**: drafts/revises prose for one Part
- **Editor**: validates prose against scaffold + continuity

Location (typical):
- `ai_services/`

### Logic (Deterministic Engine)
The orchestrated runtime that:
- selects what to do next
- hydrates prompts slice-by-slice
- executes file operations through guarded tools
- enforces the update cycle

Core modules (typical):
- `core/orchestrator.py`
- `core/agent_tools.py`
- `core/project_manager.py`
- `core/scanner.py` (or equivalent)

### Memory (Explicit Project State)
All durable “truth” lives in versionable state and indexes:

- **Matrix** (runtime state): `data/matrix.json`
- **Story Bible** (creative intent): `data/story_bible/`
- **RAG memory DB** (long-term continuity): `data/memory_db/` (per project)

---

## 2) The Deterministic Control Loop

SwarmCraft runs a strict cycle:

**SCAN → PLAN → EXECUTE**

- **SCAN**  
  Reads filesystem + state, updates Matrix metrics/status, ingests new prose into RAG memory.
- **PLAN**  
  Architect selects the next target **Part** and action (draft/revise/review), based on Matrix status + control signals.
- **EXECUTE**  
  Narrator/Editor runs for exactly one Part. All mutations occur via tools, then the system returns to SCAN.

Details: **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 3) Core Data Objects

### 3.1 Matrix (Runtime State)
`data/matrix.json` is the machine-readable view of “what exists and what’s next.”

It tracks:
- per-part manuscript path
- status (`EMPTY`, `DRAFTING`, `REVIEW_READY`, `REVISION_NEEDED`, `LOCKED`)
- active task target (always a **Part**)
- word counts, timestamps, metrics

Details: **[Central Matrix](Central-Matrix-Runtime-State.md)**

### 3.2 Story Bible (Creative Intent)
The Story Bible stores the canonical creative plan:
- characters, lore, constraints, style rules
- **templates** and **outline** (the Story Scaffold)

Details: **[Story Bible](Story-Bible-Creative-Intent.md)**

### 3.3 Story Scaffold (Templates + Outline + Parts)
The scaffold is the structured narrative “grid” that humans and the Wizard can edit:

- **Templates** define:
  - thread set (Plot, Character Development, etc.)
  - cadence rules (how often threads must be filled)
  - default parts-per-chapter (and allowed bounds)

- **Outline** defines:
  - chapters → parts mapping
  - per-part thread beats (grid cells)
  - per-part contract (goal / obstacle / turn / outcome)
  - locks (protect manual edits)

Details:
- **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
- **[Schema: Templates](Schema: Templates.md)**
- **[Schema: Outline](Schema: Outline.md)**
- **[Outline Grid & CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**

---

## 4) Units of Work: Parts, Not Chapters

A **Part** is the atomic unit SwarmCraft drafts and revises.

- A chapter may contain **1–6 parts** depending on template and user choice.
- Parts enable:
  - small, stable prompt slices
  - targeted regeneration (one beat / one part)
  - better continuity control
  - clearer status tracking

Part orchestration: **[Orchestration: Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

---

## 5) Multi-Project Isolation

SwarmCraft supports multiple isolated projects (universes):

- each project has its own:
  - `matrix.json`
  - `story_bible/`
  - `memory_db/`

Details: **[Multi-Project Management](Multi-Project-Management.md)**

---

## 6) RAG Memory for Long-Form Continuity

The memory system ingests written prose and enables semantic retrieval:
- prevents character/world drift
- reduces plot holes
- avoids bloating prompts with “story so far”

Details: **[RAG Memory System](RAG-Memory-System.md)**

---

## 7) Control Surfaces

SwarmCraft is designed to be observable and steerable:

- **TUI Dashboard**: real-time view of tasks, logs, and state  
  Details: **[Dashboard  Reference](Dashboard-TUI-Reference.md)**

- **Control file** (implementation-specific): pause/resume/override planning without coupling UI to engine.

---

## 8) Provider Integration (Grok)

SwarmCraft uses a provider adapter to keep the engine model-agnostic:
- normalizes tool calling and responses
- centralizes API settings and error handling
- enables “Powered by Grok” without hardwiring provider logic everywhere

Details: **[Provider Adapter: Grok](Provider-Adapter-Grok.md)**

---

## 9) Where to Go Next

- **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**
- **[Central Matrix](Central-Matrix-Runtime-State.md)**
- **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
- **[Orchestration: Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
