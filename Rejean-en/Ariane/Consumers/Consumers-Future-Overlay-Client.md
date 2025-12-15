# Consumers / Future Overlay Client (Concept)

This page describes a **possible** overlay-style client as a downstream consumer of Ariane.

It is intentionally non-normative: Ariane’s core scope is limited to exploration (Theseus) and storage/semantics (Atlas). An overlay client is one way to use that data, not a requirement of the project.

---

## Concept

A future overlay client would:

- Run alongside existing applications.
- Recognize the current UI state.
- Query Atlas for recommended next actions.
- Render hints directly on top of the application (e.g., highlights, arrows, step counters).

From Ariane’s perspective, this client is simply:

> A consumer that performs real-time state recognition and uses Atlas for next-step suggestions and path planning.

All rendering, input interception, and user interaction are handled by the client itself.

---

## Responsibilities of the Overlay Client

An overlay-style client (if built) would handle:

1. **Local observation**
   - Capture UI structure via accessibility APIs or screen capture + detection.
   - Compute or approximate fingerprints compatible with Atlas.

2. **State recognition via Atlas**
   - Query Atlas: “Which state does this UI most closely match?”
   - Use returned `state_id`, elements, and semantics.

3. **Guidance retrieval**
   - Given a goal (intent) or a predefined workflow:
     - Use Atlas to find the next transition(s) and target elements.
   - Retrieve element roles, labels, bounds, and intents.

4. **Visual overlay**
   - Draw highlights or markers at the coordinates of target elements.
   - Optionally dim the rest of the UI, show step counters, etc.

5. **Interaction handling (optional)**
   - Optionally intercept clicks or keystrokes to:
     - Enforce a guided path.
     - Confirm that the user followed the suggested step.

None of these behaviors are mandated or implemented by Ariane itself; they are purely client-side responsibilities.

---

## Interaction with Atlas

From a data standpoint, the overlay client behaves like any other agent:

- Uses Atlas for:
  - State recognition (matching fingerprints).
  - Transition lookup (outgoing edges).
  - Intent-based planning (goal-directed pathfinding).

- Uses its own UI representation for:
  - Rendering.
  - Input handling.
  - Error detection and recovery.

Ariane remains unaware of how the data is rendered or presented to users.

---

## Privacy and Local Processing (Recommended)

While not enforced by Ariane, a reasonable overlay design would:

- Perform all screen capture and accessibility access locally.
- Send only:
  - Structural/hashed fingerprints.
  - Context identifiers (app, version, platform).
- Avoid sending raw screenshots, text content, or user data to remote services when not necessary.

These are design recommendations for any future overlay consumer, not requirements of the core spec.

---

## Non-Goals for Ariane

To keep the scope clear:

- Ariane does **not** define any UI framework or library for drawing overlays.
- Ariane does **not** require any particular client to exist.
- Ariane does **not** specify UX rules for guided walkthroughs.

The only requirement is that any consumer—overlay or otherwise—must be able to:

- Recognize states.
- Query transitions and intents.
- Use the graph in a way that respects its semantics.

---

## Related Pages

- [Consumers](Consumers.md) – overview of consumer types, including overlay as one example.  
- [Consumers/AI-Agent-Integration](Consumers-AI-Agent-Integration.md) – how agents use Atlas for planning and guidance.  
- [Atlas](Atlas.md) – data and semantics that overlay clients would query.  
- [Theseus](Theseus.md) – how the underlying UI graphs are discovered in the first place.
