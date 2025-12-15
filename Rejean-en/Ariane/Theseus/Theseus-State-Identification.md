# Theseus / State Identification

State identification is how Theseus decides whether the current UI is:

- A **new state** it has never seen before, or
- A **known state** it has already mapped.

To build a stable UI graph, Theseus needs state identifiers that:

- Are stable under small cosmetic changes.
- Change when the structure or functionality meaningfully changes.
- Can be computed across different platforms and drivers.

---

## What Is a State?

For Ariane, a **state** is:

> A specific configuration of the user interface that is relevant for interaction and navigation.

Examples:

- Main window of an application.
- A dialog (e.g., “Save as”, “Preferences”).
- A subview or screen (e.g., “Export”, “Settings”, “New project”).

A state is represented by:

- The structure of the UI tree.
- The set and arrangement of interactive elements.
- Optionally, an associated screenshot or visual representation.

---

## Fingerprints

Each observed UI tree is converted into a **fingerprint**. Fingerprints are used to derive:

- A **state ID** – a compact identifier used in the graph.
- A notion of **similarity** – to decide whether two observations represent the same state or a variant.

A typical fingerprint is composed of:

1. **Structural hash**  
   - Encodes the shape and roles of the UI tree:
     - Node types (button, input, menu item, etc.).
     - Hierarchical relationships.
   - Insensitive to purely visual changes (e.g., colors, fonts).

2. **Visual hash (perceptual)**  
   - Encodes the appearance of the screen (e.g., pHash of a screenshot).
   - Robust to small visual differences but changes when layout/content changes visibly.

3. **Optional semantic hash**  
   - Encodes textual content (labels, titles) using OCR or accessibility text.
   - Useful when structure is similar but text differences matter.

---

## Example: Fingerprint Computation (Conceptual)

Pseudo-code, omitting implementation details:

```python
def compute_fingerprint(ui_tree, screenshot=None, text_tokens=None):
    structure_id = hash_tree_structure(ui_tree)
    visual_id = perceptual_hash(screenshot) if screenshot is not None else None
    semantic_id = hash_text_tokens(text_tokens) if text_tokens is not None else None

    return {
        "structure": structure_id,
        "visual": visual_id,
        "semantic": semantic_id,
    }

def compute_state_id(fingerprint):
    parts = [
        fingerprint["structure"],
        fingerprint.get("visual") or "",
        fingerprint.get("semantic") or "",
    ]
    return hash_concatenate(parts)
