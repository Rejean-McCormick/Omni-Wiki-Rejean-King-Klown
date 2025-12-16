# Abstract Wiki Architect

**Abstract Wiki Architect** is a family-based, data-driven NLG toolkit for **Abstract Wikipedia** and **Wikifunctions**.

Instead of writing one renderer per language (“300 scripts for 300 languages”), this project organises NLG as:

- ~15 shared **family engines** (per language family, in Python),
- hundreds of per-language **configuration cards** (grammar matrices + language cards, in JSON),
- a library of **cross-linguistic constructions** (sentence patterns),
- a **lexicon subsystem** (with bridges to Wikidata / Abstract Wikipedia-style lexemes),
- a small, well-defined inventory of **semantic frames**,
- and a **QA factory** for large, language-specific test suites.

The goal is to provide a **professional, testable architecture** for rule-based NLG across many languages, aligned with the ideas behind Abstract Wikipedia and Wikifunctions, but usable independently.

---

## 1. Abstract Wikipedia and Wikifunctions: motivation

Abstract Wikipedia and Wikifunctions aim to:

- represent knowledge in a language-independent way, and  
- render it into many natural languages via functions and language-specific resources.

To do that at scale, you need more than “one script per language”. You need:

- **shared logic per language family** (Romance, Slavic, Bantu, Japonic, …),
- **per-language configurations** (morphology rules, determiners, orthographic details),
- a small inventory of **constructions** (“X is a Y”, “X has Y”, “There is a Y in X”, …),
- **lexica** with the right features for NLG (gender, animacy, noun class, etc.),
- **semantic frames** that are language-agnostic but close to AW’s data,
- and basic **discourse logic** (topics, pronouns, short multi-sentence descriptions).

This repository is a way to:

- make those layers concrete in code,
- explore how lexicon + morphology + constructions + semantics + discourse can be kept separate but interoperable,
- create a reference architecture that can talk to Abstract Wikipedia / Wikifunctions concepts.

It is not an official Wikimedia component, but it is designed with that ecosystem in mind.

---

## 2. Integration into Konnaxion

[Konnaxion](https://github.com/Rejean-McCormick/Konnaxion) is a broader **socio-technical platform** project, focused on:

- roles, responsibilities, and governance structures,
- processes and coordination flows,
- long-term questions around infrastructure, knowledge, and legitimacy.

Konnaxion **is not an AI product** and does not expose AI features to end users. AI is used on the **builder side**: to design, generate, and refactor entire files, modules, and documentation. The running system is conventional software.

The intended relationship between Abstract Wiki Architect and Konnaxion is:

1. **Shared semantic structures**

   - Use similar semantic frames to Abstract Wikipedia (entities, roles, events, biographical frames, membership frames, etc.) for Konnaxion’s knowledge objects.
   - Keep the semantic layer close to what Abstract Wikipedia / Wikifunctions adopt, so ideas – and possibly data – can move between them.

2. **Renderer for multi-lingual narratives**

   - Use Abstract Wiki Architect as a rendering layer for:
     - short descriptions of roles, mandates, and decisions,
     - summaries of processes and events,
     - biographies and contextual information about actors in a socio-technical system.
   - Reuse the same constructions that already express “X is a Polish physicist” to express things like “X is a mediator for Y” or “X coordinates process Z”.

3. **Clear separation of concerns**

   - Within Konnaxion, Abstract Wiki Architect is a **library/subsystem**, not the whole platform.
   - Konnaxion focuses on governance and coordination; Abstract Wiki Architect focuses on transforming structured data into multi-lingual text.

4. **Alignment with Wikimedia**

   - Where Abstract Wikipedia / Wikifunctions stabilise on certain semantic patterns or APIs, Konnaxion can reuse them instead of reinventing them.
   - This repo is a place where that alignment can be tested and iterated in code.

In short: **Abstract Wiki Architect is the NLG / language layer; Konnaxion is the larger socio-technical platform that may reuse it.**

---

## 3. What the tool does (architecture overview)

Very roughly, the architecture is:

> **Engines (families)** + **Configs (languages)** + **Constructions (sentence patterns)**  
> + **Lexica** + **Frames (semantics)** + **Discourse** + **Router/API**

### 3.1 Engines and morphology

- `engines/` – family-level engines (Romance, Slavic, Agglutinative, Germanic, Bantu, Semitic, Indo-Aryan, Iranic, Japonic, Koreanic, etc.).
  - Each engine knows how its family works (gender systems, cases, agreement, noun classes, etc.).
  - Engines do not hard-code language-specific endings; they consult configuration and lexicon.

- `morphology/` – family-specific morphology modules:
  - use grammar matrices in `data/morphology_configs/` (e.g. `romance_grammar_matrix.json`, `slavic_matrix.json`, …),
  - use per-language configs (e.g. `data/romance/it.json`, `data/slavic/ru.json`),
  - use lemma features from the lexicon,
  - expose a small, clear API to constructions (e.g. inflect NP, choose article, inflect verb, join tokens).

### 3.2 Constructions (sentence patterns)

Under `constructions/`:

- `copula_equative_simple` – “X is a Y”
- `copula_equative_classification` – “X is a Polish physicist”
- `copula_attributive_np`, `copula_attributive_adj`
- `copula_existential` – “There is a Y in X”
- `copula_locative`
- `possession_have` – “X has Y”
- `intransitive_event`, `transitive_event`, `ditransitive_event`, `passive_event`
- `relative_clause_subject_gap`
- `coordination_clauses`
- `comparative_superlative`
- `causative_event`
- `topic_comment_copular`
- `apposition_np`
- …

Constructions are **family-agnostic**:

- they decide roles (SUBJ, PRED, LOC, OBJ, etc.),
- they call morphology + lexicon to realise noun phrases and verbs,
- they can take discourse information into account (topic vs focus, givenness) when available.

### 3.3 Frames, semantics, and discourse

#### 3.3.1 Semantic frames

Under `semantics/` and `docs/FRAMES_*.md`:

- **Core value types**:
  - `Entity`, `Location`, `TimeSpan`, `Event`, quantities, etc.
- **Frame families**:
  - **Entity frames** (`FRAMES_ENTITY.md`): persons, organisations, places, works, products, laws, projects, etc.
  - **Event frames** (`FRAMES_EVENT.md`): single events / episodes with participants, time, and location.
  - **Relational frames** (`FRAMES_RELATIONAL.md`): statement-level facts (definitions, attributes, measurements, memberships, roles, part–whole, comparisons, etc.).
  - **Narrative / aggregate frames** (`FRAMES_NARRATIVE.md`): timelines, careers, developments, receptions, comparisons, lists.
  - **Meta frames** (`FRAMES_META.md`): article / section structure and sources.

`semantics/normalization.py` and `semantics/aw_bridge.py` map “loose” inputs (dicts, CSV rows, Z-objects) into typed frames that the engines and constructions can consume.

A key example is the biography frame:

```python
from semantics.types import Entity, BioFrame

marie = Entity(
    id="Q7186",
    name="Marie Curie",
    gender="female",
    human=True,
)

frame = BioFrame(
    main_entity=marie,
    primary_profession_lemmas=["physicist"],
    nationality_lemmas=["polish"],
)
````

This `BioFrame` can be passed to the internal router or the public NLG API.

#### 3.3.2 Discourse and information structure

Under `discourse/`:

* `DiscourseState` tracks mentioned entities, current topic, and simple salience.
* `info_structure.py` assigns topic vs focus labels to frames and arguments.
* `referring_expression.py` chooses between full name, short name, pronoun, or zero subject.
* `planner.py` orders several frames into short multi-sentence descriptions.

This is what allows outputs like:

> “Marie Curie is a Polish physicist. She discovered radium.”

instead of:

> “Marie Curie is a Polish physicist. Marie Curie discovered radium.”

and makes it possible to build topic–comment variants for languages where that matters.

### 3.4 Lexicon subsystem

Under `lexicon/`:

* types (`Lexeme`, `Form`, etc.),
* loaders and indices,
* normalisation helpers (for lemma lookup),
* bridges to Wikidata / Abstract Wikipedia-style lexemes.

Lexicon data in `data/lexicon/` (e.g. `en_lexicon.json`, `fr_lexicon.json`, `it_lexicon.json`, `ru_lexicon.json`, `ja_lexicon.json`, …) typically contains:

* lemma and POS (`NOUN`, `ADJ`, `VERB`, …),
* features (gender, number, noun class, etc.),
* flags (`human`, `nationality`, …),
* cross-links (feminine/masculine, plural/singular),
* optional IDs (Wikidata Q-IDs, Lexeme IDs),
* language-specific details needed by morphology.

Supporting tools include:

* building / updating lexica from Wikidata,
* schema validation and smoke tests,
* coverage reports relative to QA test suites,
* simple lexicon statistics per language.

### 3.5 Router, profiles, and API

* `language_profiles/` – per-language profiles (family, default constructions, key settings).
* `router.py` – internal entry point:

  * given a **language code** and either:

    * higher-level arguments (name, profession, nationality, etc.), or
    * explicit semantic frames,
  * loads the language profile and lexicon,
  * selects the appropriate family engine and constructions,
  * returns a surface string.

Examples:

* `render_bio(...)` for biography-like sentences,
* `render_from_semantics(frame, lang_code=...)` for semantic-frame inputs.

On top of this, a small **public NLG API** (`docs/FRONTEND_API.md`) exposes:

```python
from nlg.api import generate_bio, generate
from semantics.types import Entity, BioFrame

bio = BioFrame(
    main_entity=Entity(name="Douglas Adams", gender="male", human=True),
    primary_profession_lemmas=["writer"],
    nationality_lemmas=["british"],
)

result = generate_bio(lang="en", bio=bio)
print(result.text)       # "Douglas Adams was a British writer."
print(result.sentences)  # ["Douglas Adams was a British writer."]

result2 = generate(lang="fr", frame=bio)
print(result2.text)
```

The API returns a `GenerationResult` (final text, sentence list, debug info), and hides router / engine / lexicon details from callers.

---

## 4. QA and test-driven development

The toolkit is built around **test suites** and **regression checks**:

* CSV-based test suites (`qa_tools/generated_datasets/test_suite_*.csv`):

  * each row describes a case (e.g. name, profession, nationality, gender, language),
  * includes one or more expected outputs (gold sentences),
  * are suitable for editing by native speakers and non-coders.

* Test suite generator:

  * `qa_tools/test_suite_generator.py` produces language-specific CSV templates.

* Test runner:

  * `qa/test_runner.py` loads frames from CSV rows, calls the renderer, and compares actual vs expected outputs,
  * prints per-language pass/fail stats and mismatch reports.

* Lexicon QA:

  * coverage reports (which lemmas in the test suites are missing from the lexicon),
  * schema validation and smoke tests,
  * optional regression tests over lemma inventories.

The intent is to make it easy to:

* add a new language,
* grow coverage with native-speaker feedback,
* detect regressions when changing engines, morphology configs, or lexicon data.

---

## 5. Hosting and HTTP exposure

Beyond the Python API, the stack can be exposed as a web service:

* a FastAPI backend (Architect API),
* a Next.js frontend UI (Architect frontend),
* mounted under an existing domain via Nginx (for example, under `/abstract_wiki_architect/`).

The HTTP API simply wraps the same frame-based `generate(...)` / `generate_bio(...)` calls and returns JSON, making it easier to integrate with other systems (including potential Wikifunctions prototypes or Konnaxion).

Details are in `docs/hosting.md`.

---

## 6. How it is built (development approach)

The project emphasises **architecture and file-level organisation**:

* clear decomposition into modules (engines, morphology, constructions, lexicon, semantics, discourse),
* language-agnostic frame model at the interface to Abstract Wikipedia / Wikifunctions,
* explicit data-driven configuration (JSON matrices, language cards, lexicon files),
* readable, idiomatic Python with descriptive names and simple control flow.

AI is used on the **builder side**:

* to draft, refactor, and reorganise entire modules and documentation,
* to help populate test suites and lexicon entries under human supervision.

Automated tests and QA suites provide stability as the architecture evolves.

The aim is a codebase that is:

* detailed enough to be realistic,
* structured enough to be a reference,
* adaptable enough to connect with Abstract Wikipedia, Wikifunctions, and Konnaxion.

---

## 7. Links

* **Repository:**
  [https://github.com/Rejean-McCormick/abstract-wiki-architect](https://github.com/Rejean-McCormick/abstract-wiki-architect)

* **Meta-Wiki (Abstract Wikipedia tools page):**
  [https://meta.wikimedia.org/wiki/Abstract_Wikipedia/Tools/abstract-wiki-architect](https://meta.wikimedia.org/wiki/Abstract_Wikipedia/Tools/abstract-wiki-architect)

* **Konnaxion (platform reusing these ideas):**
  [https://github.com/Rejean-McCormick/Konnaxion](https://github.com/Rejean-McCormick/Konnaxion)
  [https://github.com/Rejean-McCormick/Konnaxion/wiki](https://github.com/Rejean-McCormick/Konnaxion/wiki)

