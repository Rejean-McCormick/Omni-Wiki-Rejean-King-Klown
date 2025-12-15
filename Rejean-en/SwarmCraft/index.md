# SwarmCraft: Deterministic Story Engine

> **Architectural Lineage:**
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in `mojomast/swarmussy`. Its deterministic layering is derived from the meta-structure of the **Abstract Wiki Architect**.

## **POWERED BY GROK**

**SwarmCraft** is a deterministic, data-driven story engine designed to transform explicit project state into prose using a strict control loop. Unlike chat-based swarms, it separates **Brain** (LLM personas), **Logic** (orchestration), and **Memory** (explicit state) to ensure long-form narrative coherence.

---

## 1. Core Architecture

The system operates on a **"Three-Layer Model"** to prevent hallucinations and state drift:

* **Brain (Personas):** Stateless services (Architect, Narrator, Editor) that never own canonical state.
* **Logic (Engine):** The runtime that handles the `SCAN → PLAN → EXECUTE` loop and tool execution.
* **Memory (State):** All truth lives in the **Matrix** (runtime status), **Story Bible** (creative intent), and **RAG DB** (long-term continuity).

### The Deterministic Pipeline

SwarmCraft replaces emergent coordination with a strict cycle:

1. **SCAN:** Recompute reality from disk.
2. **PLAN:** Select the next atomic **Part** to draft or revise.
3. **EXECUTE:** Run one persona on that Part, then exit.

---

## 2. Documentation Modules

### Core Logic & Orchestration

* [**Architecture Overview**](Core/Architecture-Overview.md) – High-level diagram of the Brain/Logic/Memory separation.
* [**Deterministic Pipeline**](Core/Deterministic-Pipeline-Scan-Plan-Execute.md) – Detailed breakdown of the SCAN-PLAN-EXECUTE control loop.
* [**Prompt Hydration**](Runtime/Orchestration-Slice-By-Slice-Prompt-Hydration.md) – How the engine prevents "prompt sprawl" by injecting only the active Part slice.
* [**Provider Adapter: Grok**](Runtime/Provider-Adapter-Grok.md) – The normalization layer that keeps the engine model-agnostic.

### State & Schema (The Truth)

* [**Central Matrix**](Core/Central-Matrix-Runtime-State.md) – The machine-readable runtime state (`matrix.json`).
* [**Story Bible (Intent)**](Scaffold/Story-Bible-Creative-Intent.md) – Where characters, lore, and constraints live.
* [**Story Scaffold**](Scaffold/Story-Scaffold-Templates-Outline-Parts.md) – The grid system combining Templates and Outlines.
* [**Schema: Templates**](Scaffold/Schema-Templates.md) – Defining thread sets and pacing rules.
* [**Schema: Outline**](Scaffold/Schema-Outline.md) – Defining chapters, parts, and beat contracts.

### Operations & Usage

* [**Dashboard TUI**](Runtime/Dashboard-TUI-Reference.md) – The "Mission Control" interface for observing the engine.
* [**Multi-Project Management**](Runtime/Multi-Project-Management.md) – Running isolated universes in a single runtime.
* [**Outline Grid & CSV**](Scaffold/Outline-Grid-CSV-Round-Trip.md) – Round-tripping the story structure via spreadsheets.
* [**RAG Memory System**](Runtime/RAG-Memory-System.md) – Long-term retrieval for narrative continuity.

---

## 3. Key Concepts

### Parts, Not Chapters
The atomic unit of work is the **Part**. Chapters are simply rollups of 1–6 Parts. This allows for small, stable prompt slices and targeted regeneration.

### Slice-by-Slice Hydration
The engine never dumps the whole Story Bible into the LLM. It hydrates prompts with **only** the active Part's beats, contract, and relevant RAG evidence.

### Credits & Lineage
* **Upstream Foundation:** Mojomast/swarmussy (Multi-agent patterns, TUI concepts).
* **Meta-Structure:** Abstract Wiki Architect (State separation).
* **Full Credits:** [**Read the Credits & Lineage Page**](Meta/Credits-And-Lineage.md).