# Atlas / Ontology Vocabulary

The ontology vocabulary gives semantic meaning to the raw UI graph stored in Atlas.

Where the **graph model** describes *structure* (states, transitions) and the **core schema** describes *shape* (fields, IDs), the ontology describes *meaning*:

- What kind of UI pattern a state or element represents.
- What role an element plays within its state.
- What intent a transition fulfills.

This allows consumers to ask questions like:

- “Which action in this state actually *saves*?”  
- “Where are the primary actions?”  
- “Which transitions are destructive?”

---

## Layers of Semantics

Atlas uses three main layers of semantics:

1. **Patterns** – UI-level patterns or components.
2. **Roles** – roles of individual elements within those patterns.
3. **Intents** – abstract actions the user is trying to perform.

These can be attached to:

- States (e.g., “this state is a modal dialog”).
- Elements (e.g., “this button is primary and destructive”).
- Transitions (e.g., “this action implements ExportToPDF”).

---

## 1. Patterns

Patterns describe recurring UI structures. Examples:

- `Modal` – overlays or dialogs requiring explicit dismissal.
- `SidePanel` – sidebars with controls or navigation.
- `Toolbar` – horizontal or vertical bar containing actions.
- `MenuBar` – top-level menu strip.
- `ContextMenu` – right-click or long-press menu.
- `ToastNotification` – transient notification, usually non-blocking.
- `WizardStep` – step within a multi-step wizard.

Patterns can be used to annotate:

- States (e.g., “this state is a modal dialog”).
- Groups of elements (e.g., “these elements form a toolbar”).

Example (conceptual):

```jsonc
{
  "type": "state",
  "id": "state_export_dialog",
  "context_id": "ctx_example",
  "fingerprints": { "structure": "hash_export" },
  "interactive_elements": ["el_btn_ok", "el_btn_cancel"],
  "metadata": {
    "pattern": "Modal"
  }
}
