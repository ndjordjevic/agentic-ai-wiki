---
type: source
category: "Agent frameworks & SDKs"
source_url: https://developers.openai.com/api/docs/guides/agents
companion_urls:
  - https://github.com/openai/openai-agents-js
raw_files:
  - ../../raw/web/developers.openai.com.md
  - ../../raw/github/openai-openai-agents-js.md
tags: [openai-agents-sdk, multi-agent, handoffs, guardrails, mcp, tracing, sandbox-agents, voice-agents, responses-api]
related: [abacus.ai, strandsagents.com, crewai.com, langchain.com-langgraph, adk.dev, pydantic.dev, microsoft-autogen, litellm.ai, openai-codex-plugin-cc, elevenlabs.io, vercel.com]
product: openai-agents-sdk
detail_level: standard
created: 2026-07-03
updated: 2026-07-07
---

OpenAI's Agents SDK is the vendor's code-first framework for building multi-agent applications in TypeScript or Python. It sits alongside the Responses API: use Responses when one model call plus tools and app-owned logic suffices; use the SDK when your server owns orchestration, tool execution, approvals, and conversation state. The SDK provides agents (model + instructions + tools), a runtime loop with streaming, handoffs and agents-as-tools orchestration patterns, guardrails and human-in-the-loop approvals, sessions and server-managed continuation, sandbox agents for containerized filesystem work, MCP integration, built-in tracing, and voice/realtime agent pipelines.

_All claims below are sourced from ../../raw/web/developers.openai.com.md unless otherwise noted._

## What it does

The Agents SDK targets applications that plan, call tools, collaborate across specialists, and retain enough state to finish multi-step work. Developers define `Agent` objects with name, instructions, model, and optional tools, guardrails, MCP servers, handoffs, and structured output types, then run them via `run()` (TypeScript) or `Runner.run()` (Python). The platform docs position it as one of two primary build paths on OpenAI Developers — the other being the Responses API for lighter-weight direct model + tool calls.

## Key features

- **Agent loop** — model call → tool execution → handoffs → final output; streaming uses the same loop with incremental events. (../../raw/github/openai-openai-agents-js.md)
- **Orchestration** — **handoffs** delegate conversation ownership to a specialist; **agents as tools** let a manager agent call specialists as bounded capabilities while retaining the final reply.
- **Guardrails** — input (pre-model), output (pre-response), and per-tool validation; blocking or parallel execution.
- **Human-in-the-loop** — `needsApproval` on tools pauses runs with `interruptions` and resumable `state`; approve/reject then resume the same run.
- **State strategies** — app-managed history, SDK `session` (MemorySession, SQLiteSession), OpenAI `conversationId`, or `previous_response_id` continuation.
- **Sandbox agents** (beta) — container-backed agents with filesystem, commands, git repo mounts, and workspace snapshots for long-horizon tasks. (../../raw/github/openai-openai-agents-js.md)
- **Tools** — function tools (Zod/`function_tool`), hosted OpenAI tools (web search, file search, code interpreter), MCP servers, and agents-as-tools.
- **Tracing** — server-side SDK runs include tracing; inspect model calls, tool calls, handoffs, and guardrails in the Traces dashboard.
- **Voice agents** — realtime pipeline patterns documented separately under voice agents.
- **Dual SDKs** — TypeScript (`@openai/agents`) and Python (`openai-agents`) with parallel APIs; Python SDK also documents provider-agnostic support for 100+ LLMs via adapters.

## Architecture

The runtime is an application-level turn loop: prepare input → call the current agent's model → if tool calls, execute and continue → if handoff, switch agent and continue → if final answer with no pending tool work, return `RunResult` with `finalOutput`, `lastAgent`, `interruptions`, and resumable `state`. (../../raw/github/openai-openai-agents-js.md)

**Local context vs model context** — `RunContext` passes authenticated user info, DB clients, and loggers to tools without exposing them to the model; conversation history is what the model sees.

**Orchestration ownership** — handoffs transfer control (specialist owns the next user-facing branch); agents-as-tools keep a manager synthesizing the final answer (better for summarization, classification, bounded subtasks).

**Guardrail scope** — agent-level input guardrails run only on the first agent; output guardrails only on the final agent; tool guardrails attach to individual function tools. Manager-style workflows need per-tool validation, not only agent-level guardrails.

**Sandbox architecture** — `SandboxAgent` + `Manifest` entries (e.g. `GitRepo`) + `SandboxRunConfig` with a sandbox client (`UnixLocalSandboxClient` for local filesystem) runs agents against a configured workspace. (../../raw/github/openai-openai-agents-js.md)

## Installation

```bash
# TypeScript
npm install @openai/agents zod
export OPENAI_API_KEY=sk-...

# Python
pip install openai-agents
export OPENAI_API_KEY=sk-...
```
(../../raw/github/openai-openai-agents-js.md)

## Example usage

**First agent (TypeScript):**
```typescript
import { Agent, run } from "@openai/agents";

const agent = new Agent({
  name: "History tutor",
  instructions: "You answer history questions clearly and concisely.",
  model: "gpt-5.5",
});

const result = await run(agent, "When did the Roman Empire fall?");
console.log(result.finalOutput);
```

**Handoffs triage pattern:**
```typescript
const triageAgent = Agent.create({
  name: "Homework triage",
  instructions: "Route each homework question to the right specialist.",
  handoffs: [historyTutor, mathTutor],
});
```
(../../raw/github/openai-openai-agents-js.md)

**Approval pause/resume:**
```typescript
const cancelOrder = tool({
  name: "cancel_order",
  needsApproval: true,
  // ...
});
let result = await run(agent, "Cancel order 123.");
if (result.interruptions?.length) {
  const state = result.state;
  for (const interruption of result.interruptions) state.approve(interruption);
  result = await run(agent, state);
}
```

## When to use

Choose the Agents SDK when you need typed application code, direct control over tools and MCP servers, custom storage or server-managed conversation strategies, multi-agent handoffs with traceable ownership, guardrails and approval gates before side effects, or sandbox/container execution. Prefer the Responses API alone when a single model call plus tools and your own thin orchestration layer is sufficient.

## Maintenance status

TypeScript SDK (`openai/openai-agents-js`): 3.3k+ stars, MIT, latest v0.12.0 (2026-06-24), active development (pushed 2026-07-02). Python SDK (`openai/openai-agents-python`): 27k+ stars, separate repo with parallel feature set. Official docs at `developers.openai.com/api/docs/guides/agents` with quickstart, agent definitions, running agents, orchestration, guardrails, sandbox agents, results/state, integrations, evals, and voice agents sub-guides. (../../raw/github/openai-openai-agents-js.md)

## Ecosystem

OpenAI Developers hub also documents Codex (coding agent), Apps SDK (ChatGPT MCP apps), Workspace Agents, Realtime API, ChatKit, Agent Builder (legacy), and Assistants API (legacy, migration path to Responses). The Agents SDK integrates with OpenAI hosted tools (web search, file search, MCP connectors), Skills, shell/computer-use tools, and evaluation/red-teaming guides. Python SDK optionally integrates LiteLLM/`any-llm` for non-OpenAI models — relevant alongside gateways like [[litellm.ai]] and [[openrouter.ai]]. Compare multi-agent harnesses: [[strandsagents.com]], [[crewai.com]], [[langchain.com-langgraph]], [[adk.dev]], [[pydantic.dev]], [[microsoft-autogen]].

## Documentation

The ingested docs hub (`developers.openai.com`) ships `llms.txt` catalogs for API, Codex, Apps SDK, Workspace Agents, and Commerce. The Agents SDK track recommends: Quickstart → Agent definitions → Models and providers → Running agents → Orchestration → Guardrails → Results and state → Integrations/observability. Sub-guides cover sandbox agents, voice agents, ChatKit widgets, and agent workflow evaluation.
