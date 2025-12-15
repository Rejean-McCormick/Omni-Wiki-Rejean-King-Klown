# Atlas / Graph Model

Atlas represents each application as a directed graph of UI states and transitions.

This page focuses purely on the structural model: how states and transitions form a graph, independent of storage format or ontology details.

---

## Basic Definitions

- **State**  
  A node in the graph representing a specific UI configuration (screen, dialog, view, etc.).

- **Transition**  
  A directed edge from one state to another, representing a user action that changes the UI (e.g., clicking a button, selecting a menu item, hitting a key).

- **Graph**  
  For a given application context (app ID, version, platform, locale), the set of all states and transitions discovered by Theseus.

---

## Simple Example

A small example from a generic application:

```text
[Home Screen] --(Click "New")------> [New Document Dialog]
      |
      +--(Click "Open")------------> [Open File Dialog]
      |
      +--(Click "Settings")--------> [Settings Screen]
                                         |
                                         +--(Click "Back")--> [Home Screen]
