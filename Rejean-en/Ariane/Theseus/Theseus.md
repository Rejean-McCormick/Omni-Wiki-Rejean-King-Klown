# Theseus

Theseus is Ariane’s exploration engine.

It inspects real software, discovers which UI states exist, and records how user actions move between them. The result is a graph of states and transitions suitable for storage in Atlas and consumption by external systems.

Theseus itself does not make decisions for users. Its job is to observe, explore, and describe.

---

## Responsibilities

Theseus is responsible for:

- **State discovery**  
  Detecting distinct UI configurations (screens, dialogs, menus, etc.).

- **Transition discovery**  
  Observing how user actions (clicks, keypresses, gestures) move the UI from one state to another.

- **State identification**  
  Assigning stable identifiers to states, so they can be recognized again even if minor visual details change.

- **Graph construction**  
  Emitting a consistent set of nodes (states) and edges (transitions) that can be stored in Atlas.

---

## High-Level Architecture

Theseus is structured around a clear separation between platform-agnostic logic and platform-specific drivers.

```text
+---------------------------------------------------------------+
|                        THESEUS CORE                           |
|                                                               |
|   [State Manager]  <-->  [Exploration Engine]  <-->  [Output] |
+----------------------------^----------------------------------+
                             |
                     +-------+--------+
                     | Abstraction    |
                     | Layer          |
                     +-------+--------+
                             |
      +----------------------+------------------------+
      |                      |                        |
[Web Driver]          [Desktop Driver]         [Mobile Driver]
(browser, DOM)        (UIA/AT-SPI, etc.)      (accessibility APIs)
