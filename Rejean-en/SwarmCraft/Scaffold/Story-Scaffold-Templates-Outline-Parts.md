# Story Scaffold (Templates-Outline-Parts)

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

The **Story Scaffold** is SwarmCraft’s structured planning layer used to generate and maintain narrative coherence. It is designed as a **human-editable grid** and a **machine-usable schema**.

It combines:
- **Templates**: what threads exist and how they should be paced
- **Outline**: chapters → parts mapping + per-part beats + part contracts
- **Parts**: the atomic unit the engine drafts/revises

The Scaffold lives inside the Story Bible:
- `data/story_bible/templates/<template_id>.json`
- `data/story_bible/outline.json`

See: **[Story Bible](Story-Bible-Creative-Intent.md)**

---

## 1) Why Parts Exist

SwarmCraft drafts and revises **one Part at a time**.

A Part is the atomic unit because it enables:
- stable, small prompt slices
- targeted regeneration (one slice)
- better continuity control
- precise status tracking in Matrix

Chapters are **rollups** over Parts.

Related:
- **[Central Matrix](Central-Matrix-Runtime-State.md)**
- **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 2) Threads (Narrative Lanes)

A template defines the thread set used to structure the story, e.g.:

- Plot
- Character Development
- Philosophy
- Conflict
- Themes
- World-Building
- Emotion
- Symbolism and Imagery
- Structure
- Relationships

Threads are not the final prose. They are **scaffolding lanes** the engine uses to plan and draft.

---

## 3) Templates: Thread Set + Cadence + Default Parts/Chapter

A **template** defines:
- the thread list (rows in the grid)
- cadence rules (which threads are required per part/chapter, and at what frequency)
- default and allowed ranges for parts/chapter
- optional genre voice constraints

Schema: **[Schema Templates](Schema-Templates.md)**

---

## 4) Outline: Chapters → Parts + Per-Part Beats + Part Contract

The **outline** is the canonical story plan for a project.

It defines:
- chapters and their ordered parts
- for each part:
  - beats per thread (grid cells)
  - a “part contract” (goal / obstacle / turn / outcome)
  - optional locks (protect manual edits)

Schema: **[Schema Outline](Schema-Outline.md)**

---

## 5) Grid View (Human Editing)

The UI projects the outline into a grid:

- Columns = Parts (`P001`, `P002`, …)
- Rows = Threads (Plot, Character Dev, etc.)
- Cells = the beat for that thread in that part

This is designed to be:
- quick to scan
- easy to edit manually
- compatible with CSV round-trip when needed

Round-trip spec: **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**

---

## 6) How the Scaffold Drives Writing

During execution, SwarmCraft hydrates prompts with **only the active Part slice**:

- that Part’s thread beats
- that Part’s contract
- minimal continuity (previous part outcome, relevant character/lore snippets)
- style constraints

This prevents the system from “re-summarizing the whole story” every time.

Details: **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

---

## 7) Parts/Chapter: User-Configurable Splitting

Templates provide defaults, but the user can override:

- **Children / picture book:** typically `1 part = 1 chapter`
- **Novel:** often `3 parts/chapter` (default example)
- **Complex long-form:** up to `6 parts/chapter` where needed

Important constraint:
- parts must have stable IDs; changing parts/chapter should preserve existing part IDs wherever possible, or explicitly create new parts with new IDs.

---

## 8) Orchestration Expectations (Recommended)

The engine SHOULD:
- treat empty cells as “no beat required” unless cadence says otherwise
- enforce cadence at plan-time (PLAN chooses what needs filling)
- use Editor to verify manuscript covers the contract + beats
- lock parts once stable to avoid regressions

---

## 9) How This Relates to Matrix

- **Outline** is creative intent.
- **Matrix** is runtime progress.

Matrix stores:
- status per Part (EMPTY/DRAFTING/REVIEW_READY/REVISION_NEEDED/LOCKED)
- manuscript paths and metrics
- active_task target

Matrix page: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 10) Related Pages

- **[Story Bible](Story-Bible-Creative-Intent.md)**
- **[Schema Templates](Schema-Templates.md)**
- **[Schema Outline](Schema-Outline.md)**
- **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**
- **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
- **[Central Matrix](Central-Matrix-Runtime-State.md)**
