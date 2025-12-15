# Atlas

Atlas is Ariane’s storage and semantic layer.

It stores the UI graphs produced by Theseus in a structured, queryable form and enriches them with semantic information about elements, actions, and intents.

In short:

- Theseus **discovers** states and transitions.
- Atlas **persists** them and adds meaning.
- External systems **query** Atlas to understand how to operate software.

---

## Responsibilities

Atlas is responsible for:

- **Graph storage**  
  Persisting UI states (nodes) and transitions (edges) for many applications and versions.

- **Schema enforcement**  
  Ensuring that all stored data follows a consistent, formal structure (context, states, transitions, elements).

- **Semantic enrichment**  
  Attaching roles, patterns, and intents to UI elements and transitions (e.g., “this button implements Save”).

- **Versioning and variants**  
  Distinguishing between different app versions and A/B variants, while keeping them queryable.

- **Access interfaces**  
  Providing suitable APIs or query endpoints so that consumers (agents, tools) can retrieve the data they need.

---

## Conceptual Model

At a high level, Atlas models each application as a graph:

- **Nodes:** UI states  
- **Edges:** transitions (actions that move from one state to another)

Each graph is scoped by a **context**, such as:

- Application identity.
- Version or build.
- Platform and environment.
- Locale.

The same conceptual “screen” in different versions or locales may be represented by different states, potentially linked via variant metadata.

---

## Core Entities

Atlas organizes data around a few core entity types:

1. **Context**
   - Describes the environment for a given UI map:
     - Application identifier.
     - Version/build.
     - Platform (desktop, web, mobile, etc.).
     - Locale and other metadata.

2. **State**
   - Represents a specific UI configuration:
     - `state_id` – stable identifier.
     - Fingerprints (structural, visual, optional semantic).
     - Screenshot reference (optional).
     - List of interactive elements (buttons, inputs, menus, etc.).

3. **Interactive Element**
   - Represents an actionable control within a state:
     - Role (button, input, menu item, etc.).
     - Label or accessible name.
     - Bounding box or coordinates.
     - Platform-specific locator/path.
     - Optional semantic tags.

4. **Transition**
   - Represents a directed edge from one state to another:
     - `source_state_id` and `target_state_id`.
     - Action metadata (activate, set value, etc.).
     - Optional semantic intent (e.g., “ExportToPDF”).

These entities are defined in more detail in the core schema.

See: [Atlas/Core-Schema](Atlas-Core-Schema.md)

---

## Semantics and Ontology

Beyond raw structure, Atlas includes a vocabulary for describing:

- UI patterns (modals, menus, toasts).
- Control roles (primary button, destructive action, navigation tab).
- Intents (Save, Open, Export, Publish, etc.).

This **ontology** allows consumers to:

- Treat analogous actions across different applications as instances of the same concept.
- Search by intent instead of raw labels (“find all actions that save a document”).
- Reason about UI patterns (“find all confirmation dialogs with destructive actions”).

See: [Atlas/Ontology-Vocabulary](Atlas-Ontology-Vocabulary.md)

---

## Graph Model

The UI graph in Atlas is:

- **Directed** – transitions have a direction (from source state to target state).
- **Potentially cyclic** – applications often allow returning to previous states.
- **Labeled** – edges are labeled with actions and, optionally, intents.

Common queries include:

- Given a **state**, list outgoing transitions and their target states.
- Given a **state** and an **intent**, find all transitions that match the intent.
- Given a **start state** and **goal condition**, find a path (sequence of actions).

See: [Atlas/Graph-Model](Atlas-Graph-Model.md)

---

## Versioning and Variants

Applications evolve over time, and even a single version can exhibit multiple UI variants (e.g., A/B experiments).

Atlas supports this by:

- Associating each graph with a **context** that includes version and environment information.
- Allowing states to be linked as **variants** of a conceptual state when they represent different realizations of the same place in the UI.
- Enabling consumers to:
  - Query by specific version.
  - Or query across versions/variants when appropriate.

These relationships can be encoded via explicit links within the graph or via higher-level metadata.

---

## Access Patterns

Atlas is designed primarily for read-heavy use by external systems.

Typical access patterns:

- **State recognition**
  - Input: fingerprint(s) from a live UI.
  - Output: candidate state(s) in Atlas that match.

- **Next-step suggestion**
  - Input: current state and desired intent.
  - Output: one or more transitions (and target states) that realize that intent.

- **Route planning**
  - Input: current state, goal condition, and constraints.
  - Output: an action sequence (path through the graph).

The exact APIs and query mechanisms (e.g., graph queries, RPC, or HTTP endpoints) are implementation details.

See: [Consumers/AI-Agent-Integration](Consumers-AI-Agent-Integration.md)

---

## Data Integrity and Trust

Because data from Atlas may be used to guide user actions, its integrity matters.

At the conceptual level, Atlas supports:

- **Source attribution**
  - For each state/transition, record how and when it was discovered, and by which process.

- **Change tracking**
  - Store when a state or transition was last observed or updated.

- **Regression handling**
  - Allow new scans to coexist with older ones, rather than overwriting them blindly.

Specific mechanisms (e.g., signing or validation processes) can be added in implementation.

---

## Related Pages

- [Theseus](Theseus.md) – exploration engine that discovers states and transitions.  
- [Atlas/Graph-Model](Atlas-Graph-Model.md) – structural view of the UI graph.  
- [Atlas/Core-Schema](Atlas-Core-Schema.md) – formal definitions of context, states, elements, and transitions.  
- [Atlas/Ontology-Vocabulary](Atlas-Ontology-Vocabulary.md) – semantic categories and intents used in Atlas.  
- [Consumers](Consumers.md) – how external systems use data stored in Atlas.
