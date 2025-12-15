# Background: UI as Data

Most digital knowledge today is captured as either text (“facts”) or structured records (“entities and relationships”).  
But knowing *how to use* tools – the concrete sequences of clicks and inputs inside software – is still largely undocumented in a form machines can use.

Ariane exists to address this gap by treating user interfaces themselves as data.

---

## Knowledge Domains

You can roughly separate knowledge into three domains:

| Domain        | Description                               | Typical Infrastructure       | Coverage today |
|---------------|-------------------------------------------|------------------------------|----------------|
| Declarative   | Facts, concepts, history.                 | Text documents, encyclopedias, wikis. | High           |
| Structured    | Entities, attributes, and relationships.  | Databases, knowledge graphs. | High           |
| Procedural    | “How-to”, workflows, tool usage.          | Manuals, tutorials, videos.  | Low            |

Declarative and structured knowledge have mature infrastructure: search engines, wikis, databases, and knowledge graphs.

Procedural knowledge, by contrast, is mostly embedded in:

- Long-form tutorials and how-to articles.
- Video walkthroughs and screen recordings.
- Informal community posts, comments, and Q&A.

These artifacts are optimized for humans to read or watch, not for machines to reason over.

---

## The Procedural Knowledge Gap

Procedural knowledge has a few persistent problems:

- **Opaque to machines**  
  Manuals, videos, and blog posts rarely encode *exact* UI steps in a standardized way. Machines can’t reliably extract “Click X, then Y, then set Z to 3”.

- **Brittle and quickly outdated**  
  A minor UI redesign or new version can silently invalidate an entire tutorial.

- **Fragmented across tools and versions**  
  The same “intent” (e.g., “export to PDF”) looks very different across apps and releases.

As long as procedural knowledge remains tied to prose and pixels, AI systems have to infer “how to do things” from context or trial-and-error. That’s expensive, fragile, and often unsafe.

---

## UI as a Graph

Ariane takes a different view: treat software as a navigable graph.

At a high level:

- A **state** is a specific UI configuration (screen, dialog, menu layout, etc.).
- A **transition** is a user action that moves from one state to another (click, keypress, gesture, etc.).

This yields a simple but powerful structure:

- Nodes = UI states.
- Edges = transitions labeled with actions and semantic intents.

Once interfaces are represented this way, “how to do X” is just a pathfinding problem:

- “From current state `S`, find a path to a state where intent `ExportToPDF` is satisfied.”

---

## Why Represent UIs as Data?

Representing UIs as data (rather than just screens and documentation) unlocks several properties:

- **Machine-readable**  
  Agents can query, traverse, and compare workflows instead of guessing from pixels.

- **Versioned**  
  Different app versions can have distinct graphs, while preserving history and compatibility.

- **Cross-application reasoning**  
  Different tools that implement the same concept (“Save”, “New project”, “Publish”) can be aligned via shared semantic intents, even if their UI layouts differ.

- **Static analysis of workflows**  
  It becomes possible to analyze shortest paths, complexity, reachability, and safety properties (“is there a destructive action only one step away from a common state?”).

---

## Ariane’s Role

Ariane focuses on two things:

1. **Exploration and extraction (Theseus)**  
   - Systematically explore software.
   - Identify UI states and transitions.
   - Construct a consistent graph from those observations.

2. **Storage and semantics (Atlas)**  
   - Store the resulting UI graph with a formal schema.
   - Attach semantic meaning (intents, roles, patterns) to elements and transitions.

The result is a reusable, machine-readable description of how to operate software.

Ariane does **not** prescribe *how* agents must guide users. It only provides a structured map that external systems can consult when planning or explaining actions.

---

## Relationship to Other Knowledge Infrastructure

Ariane is designed to sit alongside, not replace, existing knowledge systems:

- Declarative knowledge remains in documentation, wikis, and reference material.
- Structured knowledge remains in databases and knowledge graphs.
- **Procedural knowledge** is where Ariane operates:
  - It answers: “Given this software and this goal, what sequence of actions achieves it?”

In practice, an agent might:

1. Use declarative and structured sources to understand what the user wants.
2. Use Ariane to decide *how* to carry out the task inside specific software.

---

## Next

- [Theseus](Theseus.md) – how Ariane explores and discovers UI states and transitions.  
- [Atlas](Atlas.md) – how those states and transitions are stored and described.  
- [Consumers](Consumers.md) – how external systems use the resulting data.
