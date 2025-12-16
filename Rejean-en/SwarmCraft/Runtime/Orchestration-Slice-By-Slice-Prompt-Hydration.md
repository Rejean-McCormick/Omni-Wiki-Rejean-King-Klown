# Orchestration Slice-by-Slice Prompt Hydration

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft avoids “prompt sprawl” by hydrating prompts with **only the active slice of the story**.

**Slice-by-slice prompt hydration** means:
- the engine targets **one Part**
- it injects only the **beats + contract** for that Part
- it adds only the **minimum continuity** required to write that Part correctly
- it runs **one persona** for **one atomic action**
- it returns to SCAN

This is the core mechanism that prevents scaffold repetition from becoming prose repetition.

---

## 1) Inputs to Prompt Hydration

Hydration assembles a prompt from four categories:

1. **Part slice (required)**
   - the target Part’s thread beats (grid cells)
   - the target Part’s contract (goal/obstacle/turn/outcome)

2. **Local continuity (required, minimal)**
   - previous Part outcome (or last approved summary)
   - chapter summary / chapter objective (if available)
   - any hard constraints that apply to this moment (POV/tense/reading level)

3. **Global references (optional, clipped)**
   - character snippets relevant to the scene
   - location/lore snippets relevant to the scene

4. **Memory retrieval (optional, bounded)**
   - top-k RAG snippets relevant to this Part’s contract/beat queries

Related sources:
- Outline: **[Schema Outline](Schema-Outline.md)**
- Template threads/cadence: **[Schema Templates](Schema-Templates.md)**
- RAG: **[RAG Memory System](RAG-Memory-System.md)**

---

## 2) The Hydration Contract (Normative)

The orchestrator MUST obey these constraints:

### 2.1 One Part only
Hydration MUST be for exactly one `part_id` at a time.

### 2.2 Minimalism
Hydration MUST:
- include only beats for the target part
- exclude beats for other parts unless explicitly requested as continuity summaries

### 2.3 Bounded memory
If RAG is enabled:
- retrieval MUST be bounded (top-k, token-limited)
- retrieved snippets MUST be formatted as “evidence,” not as new intent

### 2.4 Locks respected
If `outline.parts[part_id].locks.manuscript == true`:
- orchestrator MUST NOT hydrate a drafting prompt for that part
- only review/inspection is allowed (implementation choice)

Matrix locking semantics: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 3) Recommended Prompt Structure (Persona-Agnostic)

SwarmCraft prompts are assembled in stable sections so they are debuggable and repeatable.

Recommended high-level sections:

1. **System / Persona role**
2. **Task definition**
3. **Part contract**
4. **Part beats (thread grid cells)**
5. **Local continuity summary**
6. **Relevant Story Bible excerpts (clipped)**
7. **RAG memory evidence (clipped)**
8. **Output format requirements**

---

## 4) Concrete Hydration Payload (Recommended Shape)

This is the structured payload the orchestrator can assemble before rendering a text prompt:

```json
{
  "target": {
    "chapter_id": "CH01",
    "part_id": "P001",
    "action": "DRAFT"
  },
  "contract": {
    "goal": "...",
    "obstacle": "...",
    "turn": "...",
    "outcome": "..."
  },
  "beats": {
    "Plot": "...",
    "Character Development": "...",
    "Conflict": "...",
    "Themes": "...",
    "World-Building": "...",
    "Emotion": "...",
    "Symbolism and Imagery": "...",
    "Structure": "...",
    "Relationships": "..."
  },
  "continuity": {
    "previous_part_outcome": "N/A (first part)",
    "chapter_summary": "Global crisis exposes systemic failure.",
    "must_preserve": [
      "POV: third limited",
      "Tense: past",
      "Tone: clear, cinematic"
    ]
  },
  "references": {
    "characters": [
      {"id": "king_klown", "snippet": "Core traits, current arc state..."}
    ],
    "locations": [],
    "lore": []
  },
  "rag_evidence": [
    {"source": "P000.md", "snippet": "Earlier mention of ..."},
    {"source": "king_klown.md", "snippet": "Established constraint ..."}
  ],
  "output": {
    "format": "markdown",
    "length_target_words": 900,
    "must_hit_contract": true
  }
}
````

The persona sees a rendered version of this payload, not the entire project.

---

## 5) How the Slice Prevents Repetition

Scaffold repetition is acceptable because it is planning data. Prose repetition is not.

Hydration prevents repetition by ensuring:

* the model is not repeatedly asked to re-summarize all parts
* only the current part’s obligations are active
* continuity comes in as short “must-preserve” facts and evidence, not as broad story retellings

---

## 6) Editor Hydration (Review Mode)

Editor prompts should be even narrower:

Include:

* part manuscript text (the thing being reviewed)
* contract + beats for that part
* any “must preserve” constraints
* minimal memory evidence (only if needed to verify)

Exclude:

* beats from other parts
* unrelated lore/characters

Review outputs SHOULD be structured:

* pass/fail per contract field
* pass/fail per required thread beat (cadence-driven)
* revision directives (actionable bullets)
* recommended status transition (`REVIEW_READY` or `REVISION_NEEDED`)

---

## 7) Cadence Enforcement

Cadence rules come from the template and influence both PLAN and REVIEW:

* PLAN may select parts with missing required beats (per-part cadence)
* REVIEW may fail a part if required beats are not reflected in prose (when configured)

Template cadence: **[Schema Templates](Schema-Templates.md)**

---

## 8) Implementation Notes (Recommended)

* Build the hydration payload as JSON first (for testing/logging).
* Render to text prompt deterministically from the payload.
* Log the hydrated payload with redactions (keys, tokens).
* Token-limit each section to prevent prompt overflow.

---

## 9) Related Pages

* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**
* **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
* **[Schema Templates](Schema-Templates.md)**
* **[Schema Outline](Schema-Outline.md)**
* **[Central Matrix](Central-Matrix-Runtime-State.md)**
* **[RAG Memory System](RAG-Memory-System.md)**

