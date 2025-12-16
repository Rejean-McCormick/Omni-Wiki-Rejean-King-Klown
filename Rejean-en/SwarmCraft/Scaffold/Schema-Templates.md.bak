# Schema Templates

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

Templates define the **shape and pacing rules** of the Story Scaffold.

A template file lives at:

- `data/story_bible/templates/<template_id>.json`

It defines:
- thread set (grid rows)
- cadence rules (what must be filled, how often)
- default parts/chapter + allowed bounds
- optional style/genre constraints used in prompt hydration

Story scaffold overview: **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**

---

## 1) Design Goals

Templates MUST support:
- multiple genres / formats (children book, novel, screenplay, etc.)
- user-chosen parts/chapter within allowed bounds
- different thread sets per template
- enforceable cadence (required beats per part or per chapter)
- stable projection into a grid and CSV

Templates SHOULD:
- remain small and readable for humans
- avoid storing story-specific content (that belongs in `outline.json`)

---

## 2) Minimal Template Schema (Recommended)

```json
{
  "template_id": "novel.default",
  "name": "Novel (Default)",
  "version": 1,

  "threads": [
    "Plot",
    "Character Development",
    "Conflict",
    "Themes",
    "World-Building",
    "Emotion",
    "Symbolism and Imagery",
    "Structure",
    "Relationships"
  ],

  "parts_per_chapter": {
    "default": 3,
    "min": 1,
    "max": 6
  },

  "cadence": {
    "per_part_required_threads": ["Plot", "Conflict"],
    "per_chapter_required_threads": ["Character Development", "Themes"],
    "soft_threads": ["Symbolism and Imagery", "World-Building"],
    "min_non_empty_cells_per_part": 3
  },

  "prompting": {
    "target_reading_level": "adult",
    "tone": ["clear", "cinematic"],
    "pov": "third_limited",
    "tense": "past",
    "hard_constraints_refs": [
      "constraints/hard_rules.md",
      "constraints/style_guide.md"
    ]
  }
}
````

Notes:

* `threads` defines the grid rows.
* `parts_per_chapter` defines defaults and bounds; users can override within bounds.
* `cadence` defines what the planner/editor should enforce.
* `prompting` provides reusable style constraints (optional).

---

## 3) Field Semantics

### 3.1 `template_id` (required)

Stable identifier used by the project config and Story Bible.

### 3.2 `threads` (required)

Ordered list of thread names.

* Order is the default order in the grid UI.
* Thread names must match outline beat keys (see Schema Outline).

### 3.3 `parts_per_chapter` (required)

Defines allowed splitting:

* `default`: recommended parts/chapter for this format
* `min`, `max`: permitted bounds for user override

### 3.4 `cadence` (recommended)

Cadence is enforcement guidance for PLAN/REVIEW.

Recommended keys:

* `per_part_required_threads`: must be non-empty in every part (unless explicitly waived)
* `per_chapter_required_threads`: must appear at least once per chapter (rollup check)
* `soft_threads`: encouraged but optional
* `min_non_empty_cells_per_part`: guard against under-specified parts

Cadence is a rule set for scaffold completeness; it does not guarantee prose quality.

### 3.5 `prompting` (optional)

Reusable prompt constraints and references:

* reading level / audience
* tone and voice
* POV and tense
* references into Story Bible Markdown files

If present, prompt hydration can include these in every Part slice.

---

## 4) Template Variants (Examples)

### 4.1 `children.picturebook.json`

Typical guidance:

* fewer threads
* `parts_per_chapter.default = 1`
* tighter cadence (Plot + Emotion required every part)

### 4.2 `novel.default.json`

Typical guidance:

* broader thread set
* `default = 3` parts/chapter
* encourages symbolism/worldbuilding but doesn’t require every part

### 4.3 `screenplay.default.json`

Typical guidance:

* threads oriented around beats, scene function, visuals
* strict structure cadence (inciting incident, midpoint, etc.) via outline contract usage

---

## 5) Validation Rules (Recommended)

A validator SHOULD enforce:

* `threads` is non-empty and has unique strings
* `parts_per_chapter.min <= default <= max`
* cadence thread names must exist in `threads`
* version is present and numeric

---

## 6) Relationship to Outline and Grid

* Template defines the *thread rows* and pacing rules.
* Outline defines the *per-part cell content*.

Related:

* **[Schema Outline](Schema-Outline.md)**
* **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**
* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**


