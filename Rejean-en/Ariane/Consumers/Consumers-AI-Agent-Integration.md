# Consumers / AI Agent Integration

AI agents are a primary type of consumer for Ariane.

They use the UI graphs stored in Atlas as a reference for planning and executing actions inside existing software, turning high-level user goals into concrete sequences of UI operations.

This page describes how an AI agent can integrate with Ariane conceptually.

---

## High-Level Flow

From an agent’s point of view, the interaction with Ariane typically follows this loop:

1. **Understand the user’s goal.**
2. **Identify the current UI state.**
3. **Query Atlas for available actions and intents.**
4. **Plan a sequence of transitions toward the goal.**
5. **Execute (or instruct) the steps in the live UI.**
6. **Observe the resulting state and adjust if necessary.**

Ariane supports steps 2–4 by providing structured, semantic information about the UI.

---

## 1. Goal Representation

An agent starts with a goal, often expressed in natural language:

- “Export this document as PDF.”
- “Change the default font to Arial.”
- “Turn on dark mode.”

Internally, the agent should map this to:

- One or more **intents** known to Ariane (e.g., `ExportToPDF`, `ChangeDefaultFont`, `EnableDarkMode`).
- Optional constraints or preferences (e.g., “use the simplest path”, “avoid destructive steps”).

Ariane does not perform this mapping itself; it exposes a vocabulary of intents that the agent can align to.

See: [Atlas/Ontology-Vocabulary](Atlas-Ontology-Vocabulary.md)

---

## 2. State Recognition Against Atlas

To act correctly, the agent must know which state in Atlas corresponds to the user’s current screen.

A typical process:

1. **Observe the live UI** via:
   - Direct access to accessibility APIs, or
   - Screen capture + OCR + element detection.

2. **Compute or approximate fingerprints** compatible with Atlas:
   - Structural representation (if a tree is accessible).
   - Visual/perceptual hash (if screenshots are available).
   - Semantic hints from labels and titles.

3. **Query Atlas**:
   - “Given these fingerprint components and context (app, version, platform), what is the closest `state_id`?”

Atlas returns:

- Candidate `state_id`(s).
- Similarity or confidence scores (implementation-dependent).
- References to interactive elements and their semantics.

The agent then:

- Selects the most plausible state.
- Optionally confirms via additional checks (e.g., checking that key labels match expectations).

---

## 3. Inspecting Available Actions

Once the agent has a `state_id`, it can ask:

1. **What actions are available?**
   - Query Atlas for all outgoing transitions from this state.
   - Retrieve each transition’s:
     - Action type.
     - Target element.
     - Target state.
     - Optional intent.

2. **How are actions presented in the UI?**
   - For each associated element, retrieve:
     - Role (button, menu item, etc.).
     - Label text.
     - Bounds/coordinates.
     - Patterns (primaryAction, destructiveAction, etc.).

The agent now knows, for this state:

- Which UI elements exist.
- What they do structurally.
- What they likely mean semantically.

---

## 4. Planning with Intents

Given a goal intent (e.g., `ExportToPDF`), the agent can treat the UI graph as a planning space.

### Local Decision

In many cases, the next step is local:

- If any outgoing transition from the current state has `intent == goalIntent`, choose that transition.

Example:

```text
current_state: state_home
goal_intent: ExportToPDF

Atlas returns:
- transition: trans_home_to_export_dialog
  - intent: Export
