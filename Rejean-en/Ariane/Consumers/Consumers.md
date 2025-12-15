# Consumers

Ariane is designed as a data source.

Theseus explores applications and Atlas stores UI graphs; **consumers** are any external systems that query Atlas to understand how to operate software.

This page describes the main categories of consumers and the typical ways they interact with Ariane’s data.

---

## Types of Consumers

Examples of potential consumers include:

- **AI agents**
  - Use Atlas to plan and execute multi-step actions inside existing software.
  - Translate user goals (“export this document as PDF”) into concrete UI paths.

- **Automation tools**
  - Use Atlas to generate or validate scripts that manipulate applications via their UI.
  - Prefer declarative workflows (“do ExportToPDF”) over brittle, hard-coded sequences.

- **Analysis and diagnostics tools**
  - Analyze UI graphs to understand complexity, reachability, and safety.
  - Identify patterns such as deeply nested workflows or risky actions near common states.

- **Future overlay-style clients (optional)**
  - Use Atlas as a backend to highlight next actions on screen.
  - Not part of the core Ariane scope, but a natural downstream consumer.

---

## Core Usage Pattern

Most consumers follow a similar high-level pattern:

1. **Identify the current state**
   - Obtain a fingerprint (or partial description) of the live UI.
   - Query Atlas to find matching `state_id` candidates.

2. **Determine possible actions**
   - Fetch outgoing transitions from that state.
   - Inspect associated elements, patterns, and intents.

3. **Plan a path**
   - Given a goal (expressed in terms of intents or state conditions), search for a path:
     - `current_state` → ... → `goal_state`.

4. **Execute or explain**
   - Instruct the user or an automation layer to perform the required steps.
   - Optionally adapt or replan if the observed state diverges from expectations.

The exact details depend on the consumer, but the underlying operations are:

- State recognition.
- Transition lookup.
- Pathfinding constrained by intents and safety.

---

## State Recognition

To interact meaningfully, a consumer first needs to know “where it is” in the UI.

Typical steps:

1. Observe the current UI via its own mechanisms (e.g., screen capture + OCR, direct access to accessibility APIs).
2. Compute or approximate fingerprints compatible with those used in Atlas:
   - Structural analogs (if tree access is available).
   - Visual/perceptual hashes (if screenshots are available).
   - Semantic hints from labels/text.
3. Query Atlas:
   - “Given these fingerprints/hints, which state(s) are most similar?”

Atlas responds with:

- Candidate `state_id` values.
- Confidence scores or similarity metrics (if provided by the implementation).
- References to interactive elements.

Consumers can then decide whether they have a strong enough state match to proceed.

---

## Transition and Intent Lookup

Once a state is identified, consumers can ask:

- “What can be done from here?”  
- “Which actions correspond to a desired intent?”

Typical queries:

- **List all outgoing transitions**:
  - For a given `state_id`, return all transitions and target states.

- **Filter by intent**:
  - For a given `state_id` and `intent` (e.g., `Save`, `ExportToPDF`), return transitions whose `intent` matches.

- **Inspect elements**:
  - For each transition, get the associated element:
    - Role, label, bounds.
    - Pattern (e.g., primaryAction, destructiveAction).

This allows consumers to reason about:

- Which actions are relevant.
- How they are labeled and where they are located in the UI.
- Which actions may be risky (e.g., destructive).

---

## Path Planning

Consumers can use Atlas as a planning substrate.

Example problem:

> From the current state `S`, find a sequence of actions leading to a state where `ExportToPDF` has been carried out.

Conceptually:

1. Treat the UI graph in Atlas as a search space.
2. Use algorithms such as:
   - BFS or Dijkstra-style search for shortest path by steps.
   - Heuristic search if some transitions are cheaper or safer.
3. Optionally constrain paths by:
   - Maximum depth or number of steps.
   - Safety constraints (avoid destructive intents).
   - Intermediate constraints (must pass through or avoid certain states).

Output to the consumer:

- A sequence of transitions:
  - `t1: click element X`
  - `t2: open menu Y`
  - `t3: select option Z`
- Along with:
  - Target coordinates or locators for each step (from element data).
  - Semantic explanation of each step based on intents and patterns.

---

## Safety and Constraints

Consumers may impose their own safety rules on top of Atlas:

- Exclude transitions with certain intents (e.g., `DeleteItem`, `FormatDisk`) unless explicitly allowed.
- Limit maximum path lengths to reduce complexity and risk.
- Prefer transitions annotated as:
  - `primaryAction` over obscure alternatives.
  - High-confidence over low-confidence mappings.

Atlas provides the raw data (roles, patterns, intents); consumers choose how strictly to interpret and enforce it.

---

## Future Overlay-Style Clients (Non-Core)

One possible consumer type is an overlay or heads-up display that:

- Queries Atlas in real time.
- Draws hints or highlights on top of the running application.
- Shows step-by-step guidance to the user.

From Ariane’s perspective, such a client:

- Is just another consumer of the UI graph.
- Uses state recognition and transition lookup in the same way as any other tool.
- May perform additional rendering and interaction interception locally.

This concept is not part of the core specification for Ariane, but documenting it here clarifies how the data model can support such use cases.

See: [Consumers/Future-Overlay-Client](Consumers-Future-Overlay-Client.md)

---

## Related Pages

- [Consumers/AI-Agent-Integration](Consumers-AI-Agent-Integration.md) – more focused view on AI agents using Ariane.  
- [Atlas](Atlas.md) – storage and semantic layer that consumers query.  
- [Atlas/Graph-Model](Atlas-Graph-Model.md) – structural view of states and transitions.  
- [Atlas/Core-Schema](Atlas-Core-Schema.md) – fields available to consumers.  
- [Background-UI-as-Data](Background-UI-as-Data.md) – motivation for exposing UIs as data.
