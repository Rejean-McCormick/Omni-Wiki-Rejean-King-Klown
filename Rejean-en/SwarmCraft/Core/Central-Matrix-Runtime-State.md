# Story Bible (Creative Intent)

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

The **Story Bible** is SwarmCraft’s home for **creative intent**: the canonical narrative plan, constraints, and reference material that guide drafting and revision.

It is designed to be:
- **explicit** (no hidden “chat history” requirements)
- **versionable** (text/JSON files under source control)
- **sliceable** (only the relevant subset is injected into prompts)
- **human-editable** (writers can edit directly or through UI)

The Story Bible is distinct from:
- **Matrix** (runtime progress state): **[Central Matrix](Central-Matrix-Runtime-State.md)**
- **RAG memory** (retrieved continuity evidence): **[RAG Memory System](RAG-Memory-System.md)**

---

## 1) Location and Project Isolation

**Recommended per-project location:**
- `projects/<project_id>/data/story_bible/`

Single-project setups MAY use:
- `data/story_bible/`

The Story Bible is project-scoped. Each project has its own Bible and must not share it implicitly.

See: **[Multi-Project Management](Multi-Project-Management.md)**

---

## 2) What Lives in the Story Bible

SwarmCraft treats the Story Bible as the canonical source for:

### 2.1 Canonical references
- Characters (bios, arcs, secrets, voice constraints)
- Locations (maps, rules, sensory signatures)
- Lore (history, factions, magic/tech rules)
- Style rules (tone, POV, reading level, taboo list)
- Constraints (hard rules the Editor enforces)

These may be stored in Markdown or JSON, depending on preference and tooling.

### 2.2 The Story Scaffold (New)
The scaffold is part of the Story Bible because it is **creative intent**, not runtime state:

- **Templates:** `templates/<template_id>.json`  
  Defines threads (Plot, Character Development, etc.), cadence expectations, and default parts/chapter.

- **Outline:** `outline.json`  
  Defines chapters → parts mapping, per-part thread beats, and per-part “contract”.

Scaffold entry point:
- **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**

---

## 3) Recommended Folder Layout

Example:

```text
projects/<project_id>/data/story_bible/
├── README.md
├── outline.json
├── templates/
│   ├── children.picturebook.json
│   ├── novel.default.json
│   └── screenplay.default.json
├── characters/
│   ├── king_klown.md
│   └── ...
├── locations/
│   ├── cosmic_council_hall.md
│   └── ...
├── lore/
│   ├── world_rules.md
│   └── ...
├── constraints/
│   ├── hard_rules.md
│   └── style_guide.md
└── glossaries/
    └── terms.md
````

This is a recommendation, not a constraint—projects may reorganize, but the engine must be able to find `outline.json` and the selected `templates/<template_id>.json`.

---

## 4) Bible vs Matrix vs Memory (Key Separation)

### Story Bible (Intent)

* “What the story *should be*.”
* Edited by humans and the Wizard.
* Used as authoritative instruction.

### Matrix (Runtime)

* “What the system has *done* and what is next.”
* Derived from disk and updated by tools.
* Tracks statuses and active tasks.

See: **[Central Matrix](Central-Matrix-Runtime-State.md)**

### RAG Memory (Evidence)

* “What has been *written before*.”
* Queried to prevent continuity drift.
* Does not define intent; it provides recall.

See: **[RAG Memory System](RAG-Memory-System.md)**

---

## 5) How the Bible Is Used in Prompts (Slice-by-Slice)

SwarmCraft never dumps the whole Story Bible into the LLM.

Instead, the orchestrator hydrates prompts by selecting only:

* the target Part’s beats + contract from the Outline
* the minimal character/location/lore references required for that Part
* applicable constraints (style/voice/safety rules)

This reduces repetition, keeps cost stable, and prevents “prompt sprawl.”

See: **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

---

## 6) Editing Workflows

The Story Bible supports three editing modes:

1. **Wizard-generated scaffold**
   A guided LLM workflow creates the first template selection + outline draft.

2. **Grid editing (human-friendly)**
   Outline beats are displayed as a grid (threads × parts), with optional CSV round-trip.

3. **Direct file edits**
   Writers can edit Markdown/JSON files directly, then SCAN reconciles changes.

Grid + CSV:

* **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**

---

## 7) Integrity Rules (Recommended)

The scanner/orchestrator SHOULD validate:

* the chosen template thread list matches the outline beats keys
* every Part referenced in outline has a stable `part_id`
* locks are honored (beats/contract/manuscript)
* no orphan manuscripts exist without a Part mapping (or they are flagged)

---

## 8) Related Pages

* **[Story Scaffold](Story-Scaffold-Templates-Outline-Parts.md)**
* **[Schema Templates](Schema-Templates.md)**
* **[Schema Outline](Schema-Outline.md)**
* **[Outline Grid CSV Round-Trip](Outline-Grid-CSV-Round-Trip.md)**
* **[Central Matrix](Central-Matrix-Runtime-State.md)**
* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**

