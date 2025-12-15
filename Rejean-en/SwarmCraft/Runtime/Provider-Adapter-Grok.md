# Provider Adapter Grok

> **Architectural Lineage (Credits):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full details: **[Credits & Lineage](Credits-And-Lineage.md)**

## **POWERED BY GROK** 

SwarmCraft is powered by **Grok** through a dedicated **provider adapter** layer.

Goal:
- keep the engine **provider-agnostic**
- centralize API config, retries, and error handling
- normalize responses into a stable internal interface for personas and tools

This page documents the expected behavior of the Grok adapter, without tying the rest of the codebase to Grok-specific response shapes.

---

## 1) Responsibilities of the Provider Adapter

The Grok adapter MUST:
1. Build requests from SwarmCraft’s internal prompt format.
2. Send requests to Grok with correct auth + model settings.
3. Normalize responses into:
   - `text` output
   - optional structured tool calls
   - token usage and latency metrics (if provided)
4. Apply robust retry/backoff rules.
5. Emit consistent errors for the orchestrator to handle deterministically.

The adapter SHOULD:
- support multiple Grok models/profiles
- support streaming responses (optional)
- redact secrets in logs

---

## 2) Internal Provider Interface (Recommended)

SwarmCraft should call providers through a stable interface like:

```python
class LLMProvider:
    def generate(self, messages, tools=None, tool_choice=None, **opts) -> ProviderResult:
        ...
````

Where `ProviderResult` is normalized:

```json
{
  "text": "string",
  "tool_calls": [
    {
      "name": "write_file",
      "arguments": { "path": "...", "content": "..." }
    }
  ],
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "total_tokens": 0
  },
  "meta": {
    "model": "grok-...",
    "latency_ms": 0
  }
}
```

This allows the orchestrator to remain unchanged if you later add other providers.

---

## 3) Configuration (Recommended)

### 3.1 Environment variables

Recommended keys (names may vary by implementation):

* `GROK_API_KEY`
* `GROK_MODEL` (default model id)
* `GROK_BASE_URL` (optional, if not default)

### 3.2 Project-level overrides

Optional per-project settings file, e.g.:

* `projects/<project_id>/data/settings.json`

Recommended fields:

```json
{
  "llm": {
    "provider": "grok",
    "model": "grok-...",
    "temperature": 0.7,
    "max_tokens": 2000
  }
}
```

---

## 4) Tool Calling and Safety

SwarmCraft personas must not write files directly. They request tool calls.

The Grok adapter MUST support:

* passing tool schemas (function definitions)
* receiving tool calls (structured)
* returning them to the tool executor layer

Tool execution remains in SwarmCraft (not in Grok):

* the engine validates and runs tools
* tool results can be appended to the conversation as tool messages (implementation detail)

This preserves deterministic safety rules:

* path sandboxing
* atomic writes
* audit logs

---

## 5) Retries and Error Handling (Recommended)

### 5.1 Retry classes

Adapter SHOULD retry on:

* transient network failures
* 5xx server errors
* timeouts

Adapter SHOULD NOT retry blindly on:

* auth failures (401/403)
* invalid request payload (4xx)
* tool schema mismatch errors (fix required)

### 5.2 Backoff

Use exponential backoff with jitter.

### 5.3 Deterministic surfacing

Adapter errors MUST be normalized into stable error codes so the orchestrator can:

* mark task as failed
* re-plan
* pause if needed

Example normalized error:

```json
{
  "error": {
    "code": "PROVIDER_TIMEOUT",
    "message": "Request timed out after 60s",
    "retryable": true
  }
}
```

---

## 6) Token and Cost Tracking (Optional)

If Grok provides usage metadata, the adapter SHOULD emit it in `ProviderResult.usage`.

If usage is not provided, SwarmCraft MAY estimate tokens separately, but should mark them as estimates.

Token tracking integrates with dashboard/cost panels:

* **[Dashboard TUI Reference](Dashboard-TUI-Reference.md)**

---

## 7) How Grok Fits the Deterministic Pipeline

The provider is invoked only during **EXECUTE** (and optional planning calls if you LLM-assist planning).

The pipeline remains:

* SCAN: no provider calls required
* PLAN: deterministic selection (optionally assisted)
* EXECUTE: provider call(s) for one Part, one action

Pipeline: **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**

---

## 8) Related Pages

* **[Architecture Overview](Architecture-Overview.md)**
* **[Deterministic Pipeline](Deterministic-Pipeline-Scan-Plan-Execute.md)**
* **[Orchestration Slice-by-Slice Prompt Hydration](Orchestration-Slice-By-Slice-Prompt-Hydration.md)**
* **[Dashboard TUI Reference](Dashboard-TUI-Reference.md)**


