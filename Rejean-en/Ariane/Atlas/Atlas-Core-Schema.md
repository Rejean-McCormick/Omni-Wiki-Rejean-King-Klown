# Atlas / Core Schema

The core schema defines how UI graphs are represented in Atlas as structured data.

It specifies the main object types (context, states, elements, transitions) and the fields they must provide so that:

- Theseus can reliably write data into Atlas.
- Consumers can reliably read and interpret that data.
- Implementations can validate and evolve the data model over time.

This page is schema-oriented and storage-format-agnostic (JSON, RDF, graph DB, etc.).

---

## Overview of Object Types

Atlas organizes data into four primary object types:

1. **Context** – describes the environment in which a UI graph is valid.
2. **State** – represents a specific UI configuration.
3. **Interactive Element** – represents an actionable control within a state.
4. **Transition** – represents a directed action from one state to another.

Each object type can be extended with implementation-specific fields, but the core fields below should remain stable.

---

## 1. Context

A **Context** object scopes a UI graph to a particular application and environment.

Typical fields:

```jsonc
{
  "type": "context",
  "id": "ctx_photoshop_25_1_0_win_en-us",
  "app_id": "photoshop",
  "version": "25.1.0",
  "platform": "win32",           // e.g. win32, linux, darwin, web, android, ios
  "locale": "en-US",
  "metadata": {
    "build": "25.1.0.1234",
    "channel": "stable"
  }
}
