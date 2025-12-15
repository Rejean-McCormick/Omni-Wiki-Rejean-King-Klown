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
