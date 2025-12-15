# Theseus / Exploration Engine

The Exploration Engine controls how Theseus moves through an application:

- Which elements to interact with.
- In what order to explore them.
- When to stop.
- How to avoid unsafe or unproductive actions.

Its goal is to build a useful UI graph with bounded effort, while minimizing risk.

---

## Inputs and Outputs

**Inputs:**

- Current **state** (UI tree + state ID).
- List of **interactive elements** for that state.
- Exploration configuration:
  - Depth limits.
  - Action filters.
  - Safety constraints.

**Outputs:**

- A sequence of **actions** taken.
- Newly discovered **states** and **transitions**.
- Metadata about exploration coverage (visited states, pruned paths, errors).

---

## Core Loop

Conceptually, the Exploration Engine runs a loop like this:

1. Identify the current state (using state identification).
2. If the state is new:
   - Record it.
   - Enumerate candidate actions.
3. Pick a safe, unexplored action.
4. Execute the action via the driver.
5. Observe the resulting UI and compute the next state.
6. Record a transition from the previous state to the new state.
7. Repeat until no further actions are available within constraints.

---

## Traversal Strategy

The engine treats the UI as an implicit graph it is progressively revealing.

### Depth-First Exploration

A simple and useful default is **depth-first search (DFS)**:

- Choose an unexplored action from the current state.
- Follow it until:
  - A new state is discovered, or
  - A known state is reached (loop).
- Backtrack when:
  - All actions from a state have been explored or pruned.
  - Depth limits are reached.

Benefits:

- Easy to implement.
- Naturally builds complete *paths* (useful for downstream consumers).

Other traversal modes (e.g., breadth-first, heuristic-guided search) can be added, but DFS is a good baseline.

---

## Loop Detection and State History

To avoid infinite loops and redundant work:

- The engine keeps a **visited set** of state IDs.
- Each state has a record of:
  - Which actions have already been taken.
  - Which outgoing transitions have been observed.

If an action leads to a state that is already known:

- A new **edge** (transition) is recorded.
- The engine may still explore alternate actions from the current state, but it avoids revisiting the same transition repeatedly.

This ensures the exploration converges even if the application allows cycling between screens.

---

## Action Selection and Prioritization

Not all actions are equally important. The engine can prioritize:

- **Top-level navigation** (menus, tabs, primary buttons).
- **Dialogs and modals** (things that lead to new interaction surfaces).
- **Configuration sections** (tabs/panels inside settings).
- **Highly visible controls** (buttons in prominent positions).

Examples of filters:

- Ignore elements that:
  - Are off-screen or not visible.
  - Are known to be irrelevant (e.g., specific controls in debugging overlays, when detectable).
- Deprioritize:
  - Elements that appear identical or near-duplicate within the same region.
  - Controls that seem purely decorative.

Exact heuristics can be tuned per application or platform.

---

## Safety and Risk Management

Some actions are potentially destructive (e.g., delete, reset, format, uninstall). The engine should avoid them by default unless running in a controlled sandbox.

Safety mechanisms include:

- **Keyword-based filters**  
  - Skip actions whose labels or descriptions match high-risk patterns (e.g., “Delete”, “Erase”, “Format”, “Reset”, “Uninstall”), especially when combined with red styling or warning icons.

- **Scope constraints**  
  - Do not navigate into obviously hazardous subsystems (e.g., system-level disk tools) unless explicitly allowed.

- **Confirmation detection**  
  - If an action opens a destructive confirmation dialog, treat this as a discovered state without proceeding further.

- **Configurable risk profiles**  
  - Allow running in:
    - “Safe mode” – conservative, avoids any destructive-looking action.
    - “Sandbox mode” – more permissive, for controlled environments such as test VMs.

The Exploration Engine should treat safety as a first-class concern.

---

## Handling Non-Standard UIs

Some UIs do not expose sufficient accessibility information to support tree-based exploration.

In these cases, the engine may enable **fallback modes** via the driver:

1. **Vision-based candidate detection**
   - Capture a screenshot.
   - Detect potential interactive regions (buttons, inputs, menus) using vision heuristics.
   - Use OCR to infer text labels where possible.

2. **Coordinate-based interaction**
   - Treat candidate regions as elements.
   - Perform actions by clicking/tapping at their coordinates.

Trade-offs:

- Less reliable than accessibility-based exploration.
- Harder to map precisely back into structured UI trees.
- Best used for narrow, targeted exploration in controlled conditions.

---

## Exploration Limits

To keep exploration tractable, the engine uses explicit limits:

- **Depth limit**  
  - Maximum length of a path from the starting state.

- **State limit**  
  - Maximum number of distinct states to discover in a single run.

- **Action limit per state**  
  - Maximum number of actions to attempt from any given state.

When a limit is reached, the engine:

- Stops further exploration.
- Outputs the partial graph discovered so far.

These limits can be configured depending on:

- Target application complexity.
- Time/resources available.
- Desired coverage.

---

## Error Handling and Recovery

During exploration, actions can fail in various ways:

- Element disappears before activation.
- App becomes unresponsive.
- OS denies access to certain windows.

The engine should:

- Record errors as annotations on transitions or states.
- Attempt to recover by:
  - Returning to a known stable state (e.g., main window).
  - Restarting the application if necessary (under driver control).
- Avoid infinite retry loops.

Failures are data too: they indicate unreachable paths or restricted states.

---

## Output for Atlas

The Exploration Engine provides Atlas with:

- **States**  
  - IDs, fingerprints, and interactive elements.

- **Transitions**  
  - Source state, target state, action metadata, and any semantic hints.

- **Coverage metadata**  
  - Which states were fully explored, partially explored, or unreachable.
  - Any errors or safety-related skips.

Atlas then persists this information and makes it available to consumers.

---

## Related Pages

- [Theseus](Theseus.md) – overview of the exploration engine.  
- [Theseus/State-Identification](Theseus-State-Identification.md) – how states are fingerprinted and recognized.  
- [Atlas](Atlas.md) – how the discovered graph is stored and exposed to external systems.  
- [Consumers/AI-Agent-Integration](Consumers-AI-Agent-Integration.md) – how agents use the resulting graph during guidance.
