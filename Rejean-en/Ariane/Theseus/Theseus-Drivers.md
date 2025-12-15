# Theseus / Drivers

Drivers are the platform-specific adapters that allow Theseus to explore real software.

Each driver connects to a particular UI technology (web, desktop, mobile, etc.) and exposes a normalized view of the interface to the Theseus core:

- A tree of UI elements (roles, labels, hierarchy).
- A way to identify which elements are interactive.
- A way to perform abstract actions (activate, set value, focus, etc.).

The goal is that the core logic never needs to know whether it is exploring a browser, a native desktop app, or a mobile app.

---

## Driver Responsibilities

Every driver is responsible for:

1. **Tree acquisition**  
   - Retrieve the current UI/accessibility tree.
   - Provide a stable, hierarchical representation (nodes, children, attributes).

2. **Element characterization**  
   - Mark which elements are interactive (buttons, links, inputs, menu items, etc.).
   - Expose roles, labels, and metadata (e.g., enabled/disabled, checked/unchecked).

3. **Action execution**  
   - Provide operations such as:
     - `activate(elementId)` – click or trigger an action.
     - `setValue(elementId, value)` – enter text, toggle a checkbox, select an option.
     - `focus(elementId)` – move focus to an element.

4. **Context metadata**  
   - Report app identifier, version, platform, locale, and any other relevant context.

5. **Error handling**  
   - Report failures (e.g., element vanished, access denied) in a way the core can interpret.

---

## Driver Model

Conceptually, Each driver implements an interface like:

```text
Driver:
  getTree() -> UITree
  listInteractiveElements(tree) -> [UIElement]
  perform(action: AbstractAction) -> Result
  getContext() -> ContextMetadata
