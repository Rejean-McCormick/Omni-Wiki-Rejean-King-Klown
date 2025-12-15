# Deterministic Pipeline (SCAN-PLAN-EXECUTE)

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft runs a strict, repeatable control loop that transforms explicit project state into prose:

**SCAN → PLAN → EXECUTE**

This loop is designed to be:
- deterministic (same state → same next decision at the orchestration layer)
- restart-safe (crashes recover by re-scanning truth from disk)
- observable (each step is logged; state files are inspectable)

---

## 0) Glossary

- **Part**: the atomic unit of drafting/revision. Chapters are rollups over Parts.
- **Matrix**: runtime state (`data/matrix.json`).
- **Story Bible**: creative intent (`data/story_bible/`).
- **Scaffold**: templates + outline (parts mapping + thread beats + contracts).

---

## 1) Cycle Overview

### 1.1 SCAN
Recompute reality from disk and refresh runtime state.

Outputs:
- refreshed `data/matrix.json`
- optional RAG ingestion updates (per project)

### 1.2 PLAN
Select one target Part and one action.

Outputs:
- `matrix.active_task` populated with `{ target_id, action, reason }`
- optional “narrow queries” requested for continuity

### 1.3 EXECUTE
Run one persona on one Part, then persist results via tools.

Outputs:
- updated manuscript file for the Part, or review notes
- updated matrix bookkeeping
- return to SCAN

---

## 2) SCAN (Normative)

### 2.1 Inputs
SCAN reads:
- `data/story_bible/outline.json` (Parts ordering + locks)
- `data/story_bible/templates/<template_id>.json` (thread set + cadence)
- manuscripts under `data/manuscripts/` (or configured root)
- existing `data/matrix.json`
- `data/memory_db/` (if RAG enabled)

### 2.2 Responsibilities
SCAN MUST:
1. Enumerate expected **Parts** from `outline.json`.
2. Verify presence of each Part’s manuscript file.
3. Compute per-part metrics:
   - word count
   - last modified time
   - status
4. Respect locks:
   - never downgrade a `LOCKED` part
   - never infer unlocks automatically
5. Validate integrity:
   - missing parts
   - missing beats keys (fill with empty strings in UI projection)
   - schema mismatch between template threads and outline beats
6. Optionally ingest changed prose into RAG memory.
7. Atomically write the updated `data/matrix.json`.

### 2.3 Status derivation (Recommended)
A scanner SHOULD classify a Part as:

- `EMPTY`: file missing or below minimum threshold
- `DRAFTING`: draft exists but incomplete
- `REVIEW_READY`: draft is complete enough for Editor pass
- `REVISION_NEEDED`: flagged by Editor or override
- `LOCKED`: protected from further automated edits

Matrix semantics: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 3) PLAN (Normative)

### 3.1 Inputs
PLAN reads:
- current `data/matrix.json`
- `outline.json` for ordering + locks
- operator overrides (control surface), if present

### 3.2 Selection policy (Recommended default)
Absent overrides, the Architect SHOULD prioritize:
1. Any Part with `REVISION_NEEDED`
2. The earliest Part with `EMPTY`
3. The earliest Part with `DRAFTING`
4. Optional: any Part failing integrity checks (continuity, constraints, missing sections)

### 3.3 Hard constraints
PLAN MUST NOT select:
- Matrix `LOCKED` Parts
- Parts whose Outline locks prohibit changes (mapping depends on implementation: beats vs contract vs manuscript)

### 3.4 Plan output shape
The plan MUST specify:
- `target_type: "part"`
- `target_id: "<part_id>"`
- `action: "DRAFT" | "REVISE" | "REVIEW"`
- optional: `priority`, `reason`, `requested_memory_queries[]`

The orchestrator persists the plan into `matrix.active_task`.

---

## 4) EXECUTE (Normative)

EXECUTE performs exactly one scoped operation on exactly one Part.

### 4.1 Prompt hydration (Part slice)
Before invoking a persona, the orchestrator MUST hydrate a **Part slice**:
- the target Part’s thread beats (cells)
- the Part contract (goal/obstacle/turn/outcome)
- minimal continuity:
  - previous Part outcome summary (or last approved beat summary)
  - chapter-level goal/summary (if defined in outline)
  - relevant character/lore snippets (only what’s needed)
- project-level style constraints

Details: **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

### 4.2 Narrator execution (DRAFT / REVISE)
If action is `DRAFT` or `REVISE`:
- the Narrator produces prose for exactly one Part
- prose is written to `data/manuscripts/<part_id>.md` (recommended)
- the orchestrator updates Matrix bookkeeping and returns to SCAN

### 4.3 Editor execution (REVIEW)
If action is `REVIEW`:
- the Editor checks the manuscript against:
  - Part beats + contract
  - continuity constraints (optionally via RAG)
  - style constraints
- output is either:
  - approve (advance to `REVIEW_READY` / candidate for locking), or
  - revision request (set `REVISION_NEEDED` with structured notes)

### 4.4 Tool safety
All modifications MUST go through the guarded tool layer (file ops + state updates).
No persona may mutate project files directly.

---

## 5) Atomicity, Concurrency, and Restart Safety

### 5.1 Atomic step rule
One loop iteration = one atomic action:
- one SCAN refresh
- one PLAN decision
- one EXECUTE action on one Part

### 5.2 No concurrent writers
Only one worker persona may write at a time for the active project.

### 5.3 Crash recovery
On restart:
- SCAN re-derives truth from disk
- Matrix is reconciled (locks respected)
- execution resumes without reliance on chat history

---

## 6) Observability and Control

- Dashboard observes `matrix.json`, logs, and metrics without blocking the engine.
- Control signals/overrides may affect PLAN (target selection) without breaking the deterministic loop.

Dashboard: **[Dashboard TUI Reference](Dashboard-TUI-Reference.md)**

---

## 7) Related Pages

- **[Architecture Overview](Architecture-Overview.md)**
- **[Central Matrix](Central-Matrix-Runtime-State.md)**
- **[Story Bible](Story-Bible-Creative-Intent.md)**
- **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
- **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
