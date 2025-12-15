# Outline Grid CSV Round-Trip

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft supports a **human-friendly grid editor** for the outline and a **CSV round-trip** workflow.

Goal:
- Humans can edit the scaffold like a spreadsheet.
- The system can import/export without losing structure.
- Stable Part IDs preserve meaning across edits.

This page specifies how `outline.json` maps to a grid and how CSV import/export should behave.

---

## 1) Grid Model

### 1.1 What the grid shows
- **Columns**: Parts (ordered by chapter then part order)
- **Rows**: Threads (from the active template)
- **Cells**: A thread beat for that Part

Source of truth:
- Threads come from `templates/<template_id>.json`  
  See: **[Schema Templates](Schema-Templates.md)**
- Beats come from `outline.json`  
  See: **[Schema Outline](Schema-Outline.md)**

### 1.2 What is NOT in the grid (by default)
- Part contract fields (goal/obstacle/turn/outcome)  
  These may be shown in a separate panel, side sheet, or a second table export format.
- Manuscripts (prose) are not in the outline grid.

---

## 2) Canonical Mapping: Outline → Grid

Given:
- `threads = template.threads[]`
- ordered parts = `for each chapter in chapters[]: chapter.part_ids[]`

Cell mapping:

```

cell(thread, part_id) = outline.parts[part_id].beats[thread] (string or empty)

````

If the key is missing, treat it as empty when projecting:
- missing beat keys MUST NOT break UI or export
- export should emit an empty string for missing cells

---

## 3) CSV Export Format (Beats Grid)

### 3.1 Shape
- First column: thread name
- Remaining columns: `Part 1`, `Part 2`, … in display order
- Optional second header row: stable `part_id` values (recommended)

The beats-only CSV is a projection of the grid (threads × parts).

### 3.2 Recommended headers (two-row header)
Row 1 (human labels):
- column 1: empty or `Thread`
- columns 2..N: `Part 1`, `Part 2`, … (or chapter-aware labels)

Row 2 (machine IDs):
- column 1: `part_id`
- columns 2..N: `P001`, `P002`, …

This allows the CSV to remain stable even if “Part 3” is moved into a different chapter.

### 3.3 Example
```csv
,Part 1,Part 2,Part 3
part_id,P001,P002,P003
Plot,"The World in Turmoil...","The Revelation...","A Seed of Hope..."
Character Development,"King Klown feels helpless...","Insight sparks vision...","Cautious optimism..."
Conflict,"Global crisis escalates...","Self-doubt...","Opposition begins..."
````

---

## 4) CSV Import Rules (Beats Grid)

### 4.1 Primary key: part_id row

Import SHOULD use the `part_id` row as the canonical mapping.

* If present, `part_id` row MUST be used.
* If absent, importer MAY fall back to positional mapping (less safe).

### 4.2 Thread name matching

Rows are matched by thread name (first column).

* Exact match is recommended.
* Whitespace trimming is recommended.
* Unknown thread names:

  * either reject with validation error, or
  * store in `outline.parts[*].beats` only if the system supports custom threads (not recommended by default)

### 4.3 Lock compliance (required)

Importer MUST respect outline locks:

* If `outline.parts[part_id].locks.beats == true`, that part’s beats MUST NOT be modified by CSV import.

Recommended behavior:

* import produces a report:

  * updated cells count
  * skipped due to locks
  * unknown threads
  * unknown part_ids

---

## 5) Handling Template Changes (Thread Set Changes)

If the user changes template (or template version):

* The grid row set changes (threads list changes)
* The system SHOULD provide a migration layer:

  * missing threads: create empty beats
  * removed threads: preserve in outline as “orphaned” beats only if explicitly enabled, otherwise drop with confirmation

Recommended: do not silently delete beats.

---

## 6) Parts/Chapter Changes (Column Reflow)

If the user changes `parts_per_chapter`:

* Part IDs must remain stable.
* The UI may re-group columns under different chapters.
* CSV export order may change, but the `part_id` row remains stable.

Rule:

* do not rename existing part IDs when reflowing chapters
* generate new part IDs only when new parts are created

---

## 7) Optional: Contract CSV Export

Beats CSV is intentionally simple. If you want contract editing in CSV, use a second file:

`outline_contract.csv` (recommended)

Shape:

```csv
part_id,chapter_id,title,goal,obstacle,turn,outcome
P001,CH01,Part 1,"...","...","...","..."
```

Contract import MUST respect `locks.contract`.

---

## 8) Relationship to Writing and Orchestration

The grid is a scaffold. The engine uses it slice-by-slice:

* during PLAN to detect missing beats (cadence)
* during EXECUTE to inject only the active Part slice
* during REVIEW to validate manuscript coverage of beats + contract

See:

* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 9) Related Pages

* **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
* **[Schema Templates](Schema-Templates.md)**
* **[Schema Outline](Schema-Outline.md)**
* **[Central Matrix](Central-Matrix-Runtime-State.md)**


