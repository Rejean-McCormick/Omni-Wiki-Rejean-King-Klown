
# Dashboard TUI Reference

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> The dashboard pattern is also downstream of Mojomast’s original “mission control” approach for observing swarm activity.  
> SwarmCraft’s deterministic layering is derived from the meta-structure of **Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

The SwarmCraft Dashboard is a **Terminal UI (TUI)** that observes and steers the engine while keeping UI and execution decoupled.

Key principle:
- **Engine runs the AI work**
- **Dashboard renders state and sends control signals**

This prevents UI freezes and supports restart-safe operation.

---

## 1) What the Dashboard Watches

The dashboard should primarily read:
- `data/matrix.json` (runtime state)
- `data/story_bible/outline.json` (structure reference, optional)
- logs (engine logs, tool logs)
- token usage metrics (if tracked)

The dashboard must never be the source of truth; it is a view/controller.

Matrix reference: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 2) Recommended Layout (3-Column Mission Control)

A recommended high-level layout:

### 2.1 Context Panel (Left)
Shows “what the engine is currently focused on”:
- active project (project_id)
- active chapter + part (from `matrix.active_task`)
- cast in scope (optional, derived from outline or tags)
- location in scope (optional)
- active tool (what the engine is doing right now)

### 2.2 Action Panel (Center)
Shows “what is happening”:
- prose stream (latest generated text excerpt)
- system log tail (planner decisions, tool calls, warnings/errors)
- current step indicator (SCAN / PLAN / EXECUTE)

### 2.3 Progress Panel (Right)
Shows “how the project is doing”:
- parts table (status, locks, word counts)
- chapter rollups (optional)
- integrity signals (missing files, schema drift)
- cost/tokens counters

---

## 3) Core Widgets (Recommended)

### 3.1 Active Task Card
Displays:
- `target_type` (should be `part`)
- `target_id` (Part ID)
- action (`DRAFT`, `REVISE`, `REVIEW`)
- reason (planner rationale)
- elapsed time

### 3.2 Matrix Table
Backed by `matrix.parts`:
- Part ID
- Chapter ID
- Status (`EMPTY`, `DRAFTING`, `REVIEW_READY`, `REVISION_NEEDED`, `LOCKED`)
- Locked indicator
- Word count
- Last modified

### 3.3 Integrity / Alerts
Derived from scan validation:
- missing manuscripts
- outline/template mismatch (thread keys)
- orphan manuscripts
- locked conflicts

### 3.4 Token / Cost Tracker (Optional)
If token tracking is enabled:
- tokens in / out per step
- per-session totals
- optional cost estimate

---

## 4) Control Surface (Director Override)

The dashboard may write control signals to a project-scoped control file, e.g.:

- `projects/<project_id>/data/control.json`

Typical fields (recommended):

```json
{
  "run_state": "RUNNING",
  "architect_override": {
    "force_target_part_id": null,
    "force_action": null,
    "note": null
  }
}
````

### 4.1 Run states

* `RUNNING`
* `PAUSED`
* `STOPPED`

### 4.2 Override behaviors (Recommended)

Overrides should be applied at PLAN-time:

* force focus on a specific part
* force a specific action (review vs revise)
* inject a short director note that becomes part of the plan rationale

The deterministic loop remains intact:

* overrides influence selection, not execution ordering

Pipeline: **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 5) Multi-Project UX

If multiple projects exist, dashboard SHOULD display:

* active project id
* quick switch mechanism (implementation dependent)
* project health summary

Multi-project: **[Multi-Project Management](Multi-Project-Management.md)**

---

## 6) Failure and Recovery UX

The dashboard should handle:

* engine crash (dashboard stays up)
* engine restart (dashboard reconnects to state files)
* partial writes (prefer atomic writes in engine)

Recommended indicators:

* “Engine heartbeat” or “last update timestamp” from Matrix
* last SCAN time
* last EXECUTE time

Matrix includes timestamps: **[Central Matrix](Central-Matrix-Runtime-State.md)**

---

## 7) What the Dashboard Should Not Do

* It should not run LLM calls.
* It should not mutate manuscripts directly.
* It should not edit Story Bible files directly unless explicitly a dedicated editor UI (separate feature).

All modifications should go through the engine tools layer.

---

## 8) Related Pages

* **[Central Matrix](Central-Matrix-Runtime-State.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**
* **[Story Bible](Story-Bible-Creative-Intent.md)**
* **[Multi-Project Management](Multi-Project-Management.md)**

