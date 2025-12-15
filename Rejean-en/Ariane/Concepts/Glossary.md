# Glossary

This glossary defines key terms used throughout the Ariane documentation.

---

## A

**Action**  
An interaction performed on the UI, such as clicking a button, selecting a menu item, pressing a key, or setting a value in an input. In Atlas, actions are attached to transitions.

**AI Agent**  
An autonomous or semi-autonomous system that interprets user goals, plans steps, and interacts with software. In the context of Ariane, agents are consumers of the UI graph stored in Atlas.

**App Context**  
See **Context**.

**Atlas**  
The storage and semantic layer of Ariane. Atlas stores UI graphs (states and transitions), enforces a core schema, and attaches semantic information (patterns, roles, intents) to nodes and edges.

---

## C

**Context**  
An object that scopes a UI graph to a specific environment: application identifier, version, platform, and locale. All states and transitions in Atlas are tied to a context.

**Consumer**  
Any external system that queries Atlas to understand and operate software. Includes AI agents, automation tools, analysis tools, and (optionally) future overlay-style clients.

---

## D

**Destructive Action**  
An action that irreversibly modifies or deletes data (e.g., “Delete”, “Format”, “Erase”). Typically given a specific semantic pattern (e.g., `destructiveAction`) and intent (e.g., `DeleteItem`).

**Driver**  
A platform-specific adapter used by Theseus to interact with real software. Drivers provide access to the UI tree, identify interactive elements, and execute abstract actions on those elements.

---

## E

**Element (Interactive Element)**  
A control within a UI state that can be acted upon (button, link, menu item, text field, checkbox, etc.). In Atlas, elements have roles, labels, bounds, locators, and optional semantic annotations.

**Exploration Engine**  
The part of Theseus that decides which actions to take during exploration: chooses elements to interact with, manages traversal, avoids loops, and applies safety constraints.

**ExportToPDF (Intent example)**  
A sample semantic intent representing the goal of exporting content to a PDF file. Different applications may implement this intent via different UI sequences.

---

## F

**Fingerprint**  
A set of identifiers computed from an observed UI tree (and optionally a screenshot/text) to recognize and distinguish states. Typically includes:
- Structural component (hash of tree structure).
- Visual/perceptual component (hash of appearance).
- Optional semantic component (hash of textual content).

---

## G

**Graph (UI Graph)**  
The representation of an application’s UI as a directed graph, where nodes are states and edges are transitions. Stored in Atlas.

**Graph Model**  
The abstract definition of how states and transitions form a graph (directed, possibly cyclic, labeled edges, etc.), independent of storage implementation.

---

## I

**Intent**  
An abstract description of what an action does (e.g., `Save`, `OpenFile`, `ExportToPDF`, `DeleteItem`). Intents are semantic labels used on elements and transitions so consumers can plan in terms of goals, not raw UI labels.

**Interactive Element**  
See **Element**.

---

## L

**Locator**  
A platform-specific reference that allows a driver or consumer to locate an element in the live UI (e.g., accessibility path, DOM selector). Stored with elements in Atlas.

---

## O

**Ontology**  
The vocabulary of patterns, roles, and intents used by Ariane to describe the meaning of states, elements, and transitions (e.g., `Modal`, `primaryAction`, `Save`, `ExportToPDF`).

**Overlay Client (Future Concept)**  
A possible, non-core consumer that uses Atlas to draw guidance on top of existing applications (highlights, arrows, step counters). Not part of Ariane’s core specification.

---

## P

**Pattern (UI Pattern)**  
A semantic classification of UI structures or roles, such as:
- `Modal` – blocking dialog.
- `primaryAction` – main action in a state.
- `destructiveAction` – action that deletes data.
Patterns are usually attached via semantic fields on states or elements.

**Path**  
A sequence of transitions through the UI graph, typically representing a workflow (e.g., from home screen to export completion).

**Procedural Knowledge**  
Knowledge about *how to perform actions* or workflows (e.g., “how to export a document as PDF in App X”), as opposed to facts or static data. Ariane aims to represent procedural knowledge as UI graph data.

---

## S

**Safety Constraints**  
Rules used by Theseus or consumers to avoid risky actions during exploration or execution. Examples: skipping destructive actions, limiting path length, or requiring explicit authorization for certain intents.

**Semantic Hash**  
A fingerprint component derived from the textual content of the UI (labels, titles, etc.), used to distinguish states that are structurally similar but semantically different.

**Semantics**  
In Ariane, semantic information attached to states, elements, or transitions, typically in terms of patterns, roles, and intents.

**State**  
A node in the UI graph representing a specific UI configuration (screen, dialog, view). Each state has an ID, fingerprints, and a set of interactive elements.

**State Identification**  
The process of deciding whether a newly observed UI corresponds to a known state or a new one, using fingerprints and similarity thresholds.

---

## T

**Theseus**  
The exploration engine of Ariane. Theseus drives applications through their UIs (via drivers), discovers states and transitions, and emits structured data for Atlas.

**Transition**  
A directed edge in the UI graph from a source state to a target state, representing an action (click, keypress, value change, etc.). Each transition includes action metadata and optionally an intent.

---

## U

**UI as Data**  
The core idea of Ariane: represent user interfaces as machine-readable graphs (states and transitions), rather than just pixels or prose descriptions.

**UI Tree (Accessibility / DOM Tree)**  
The hierarchical structure of UI elements exposed by accessibility APIs or the DOM. Used by drivers and Theseus to identify elements, compute fingerprints, and derive states.

---

## V

**Variant (State Variant)**  
A state that is a variation of another state (e.g., due to A/B testing, layout changes, feature flags) but represents the same conceptual place in the application. Variants may be linked explicitly in Atlas via metadata.

**Visual Hash (Perceptual Hash)**  
A fingerprint component derived from a screenshot or rendered view of the UI, intended to capture visual similarity despite small changes in color or layout.

---

## Related Pages

- [Background-UI-as-Data](Background-UI-as-Data.md) – conceptual motivation and knowledge domains.  
- [Theseus](Theseus.md) – exploration engine and drivers.  
- [Atlas](Atlas.md) – storage and semantic model.  
- [Consumers](Consumers.md) – how external systems use Ariane’s data.
