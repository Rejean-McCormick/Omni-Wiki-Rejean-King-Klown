# Hybrid Mapping and Human-Guided Assistants

This page describes how Ariane supports a **hybrid approach**:

- Theseus performs **automated exploration** where possible.
- Human operators perform actions in real software where automation is not safe, reliable, or allowed.
- Both kinds of observations are stored in **Atlas** as the same kind of graph (states and transitions), with metadata indicating how they were obtained.

The goal is not full autonomy over “every interface”, but a realistic system where:

- Automation covers standards-based, accessibility-friendly UIs.
- Humans cover the hard parts.
- External tools (including AI agents) can rely on Atlas as a unified, machine-readable reference.

---

## Why a hybrid approach?

Purely automatic exploration is limited by:

- Anti-bot protections, logins, CAPTCHAs, 2FA, and secure flows.
- Custom-drawn UIs (canvas, 3D, games) without good accessibility metadata.
- High-risk operations (deletion, payments, production changes).
- Combinatorial explosion if you try to explore all possible paths.

On the other hand, purely manual documentation doesn’t give you:

- A consistent data model across apps.
- Programmatic query and pathfinding.
- A shared graph that agents and tools can consume.

The hybrid mode combines both:

- **Automation** for broad coverage of “normal” UI patterns.
- **Human-in-the-loop** for exceptional, sensitive, or complex workflows.
- A single graph in Atlas as the reference.

---

## Metadata conventions

Hybrid mapping is expressed entirely through existing Atlas records, using conventions in `metadata`.

### Source of observation

On `StateRecord.metadata` and `TransitionRecord.metadata`:

- `source = "auto"` – discovered by automated exploration.
- `source = "human"` – recorded while a human operator drove the UI.

Examples:

```json
{
  "context_id": "example-web-app-en",
  "discovered_at": "2025-03-01T10:00:00Z",
  "metadata": {
    "source": "human",
    "author": "operator-42",
    "session_id": "2025-03-01T09-59-00Z-session-1"
  },
  "state": { "...": "..." }
}
