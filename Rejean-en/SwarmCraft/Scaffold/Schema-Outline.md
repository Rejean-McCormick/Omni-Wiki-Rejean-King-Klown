# Schema Outline

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

`outline.json` is the canonical **story plan** for a project. It defines:

- chapter ordering
- chapter → parts mapping
- per-part thread beats (grid cells)
- per-part contract (goal / obstacle / turn / outcome)
- locks to protect manual edits

File location:
- `data/story_bible/outline.json`

Story scaffold overview: **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**

---

## 1) Design Goals

The outline MUST support:
- user-chosen parts/chapter (within template bounds)
- stable part IDs (critical for tracking and CSV round-trip)
- different template thread sets
- per-part beat editing in a grid UI
- per-part contract strictness for slice-by-slice drafting
- lock scopes (beats / contract / manuscript)

The outline SHOULD:
- be readable to humans
- be resilient to partial data (empty beats allowed)
- be forward-compatible (versioned)

---

## 2) Minimal Outline Schema (Recommended)

```json
{
  "version": 1,
  "template_id": "novel.default",

  "settings": {
    "parts_per_chapter": 3
  },

  "chapters": [
    {
      "chapter_id": "CH01",
      "title": "The World in Turmoil",
      "summary": "Global crisis exposes systemic failure.",
      "part_ids": ["P001", "P002", "P003"]
    }
  ],

  "parts": {
    "P001": {
      "chapter_id": "CH01",
      "title": "Part 1",
      "order_index": 1,

      "contract": {
        "goal": "Show the world failing in a concrete, personal way.",
        "obstacle": "Institutions deny and deflect responsibility.",
        "turn": "A specific event forces the truth into the open.",
        "outcome": "King Klown realizes the crisis is structural, not isolated."
      },

      "beats": {
        "Plot": "The World in Turmoil: global crisis exposes systemic failure.",
        "Character Development": "King Klown feels helpless and isolated.",
        "Conflict": "External disaster + internal doubt collide.",
        "Themes": "Collapse and urgent need for change.",
        "World-Building": "Introduce fractured institutions and scarcity.",
        "Emotion": "Despair and urgency.",
        "Symbolism and Imagery": "Fractured world as collective neglect.",
        "Structure": "Open with stakes and central conflict.",
        "Relationships": "King Klown is disconnected from others."
      },

      "locks": {
        "beats": false,
        "contract": false,
        "manuscript": false
      }
    }
  }
}
````

Notes:

* `chapters[]` defines the ordered reading structure.
* `parts{}` is the canonical per-part content.
* `beats` keys should match template threads.

---

## 3) Field Semantics

### 3.1 `version` (required)

Schema version for migration and validation.

### 3.2 `template_id` (required)

Must match an existing template file in:

* `templates/<template_id>.json`

Template schema: **[Schema Templates](Schema-Templates.md)**

### 3.3 `settings.parts_per_chapter` (recommended)

User override of parts/chapter within template bounds.

If omitted, the engine may use the template default.

### 3.4 `chapters[]` (required)

Ordered list of chapters.

Each chapter SHOULD contain:

* `chapter_id` (stable ID)
* `title`
* optional `summary`
* `part_ids` ordered list (critical)

### 3.5 `parts{}` (required)

Map of Part IDs to Part objects.

Each Part MUST contain:

* `chapter_id` (must match one chapter)
* `order_index` (global or chapter-local; implementation choice)
* `beats` object
* `contract` object (recommended)
* `locks` object (recommended)

---

## 4) Part Contract (Strict Slice Anchor)

The **contract** is the minimum “what must happen” spec for a Part.

Recommended fields:

* `goal`
* `obstacle`
* `turn`
* `outcome`

The orchestrator uses the contract to:

* hydrate slice prompts
* give the Editor a rubric for validation

Related:

* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

---

## 5) Beat Keys and Template Compatibility

Beat keys MUST align with the active template’s threads.

Validation SHOULD ensure:

* every `beats` key exists in `template.threads`
* missing keys are treated as empty when projecting to grid/CSV
* extra keys are flagged (or preserved if you support custom threads)

---

## 6) Locks (Manual Edit Protection)

Locks prevent automation from overwriting human edits.

Recommended lock scopes:

* `beats`: prevents automated changes to beats
* `contract`: prevents automated changes to contract
* `manuscript`: prevents automated changes to prose file

Planner rule:

* PLAN MUST NOT select a part for an action that violates locks.

Matrix mapping:

* locked parts should appear as `LOCKED` (or `locked=true`) in Matrix.

Matrix: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 7) ID Stability Rules (Critical)

* `chapter_id` and `part_id` MUST be stable once created.
* Grid and CSV round-trip depend on stable `part_id`.
* Changing parts/chapter SHOULD preserve existing part IDs where possible.
* New splits SHOULD create new part IDs instead of renaming existing parts.

---

## 8) Relationship to Grid and CSV

The outline is projected into a grid for human editing:

* rows = template threads
* columns = parts (ordered by chapters / part_ids)
* cells = outline.parts[part_id].beats[thread_name]

Round-trip rules:

* CSV export is a projection of `beats`
* CSV import updates `beats` while respecting locks

See: **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**

---

## 9) Relationship to Manuscripts and Matrix

* Outline defines intent (beats + contract).
* Manuscripts contain prose generated for each Part.
* Matrix tracks runtime status and file metrics.

See:

* **[Story Bible](Story-Bible-Creative-Intent.md)**
* **[Central Matrix](Central-Matrix-Runtime-State.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

