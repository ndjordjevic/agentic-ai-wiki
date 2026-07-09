---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/coleam00/agent-control-plane
tags:
  - agent-loop
  - long-running-agents
  - multi-agent-orchestration
  - human-in-the-loop
  - run-history
  - bun-typescript
  - pi-agent
  - fresh-context-spawning
related:
  - pi.dev
  - coleam00-archon
  - coleam00-harness-engineering-demo
  - snarktank-ralph
  - frankbria-ralph-claude-code
  - retool.com
  - sentry.io
product: agent-control-plane
detail_level: standard
created: 2026-06-30
updated: 2026-06-30
---

Agent Control Plane is a TypeScript/Bun harness by Cole Medin that wraps Pi (the provider-independent coding agent) in a durable orchestration layer: give it a goal, it runs a loop of agents until the goal is met, persists every run to Neon (serverless Postgres), and exposes a React dashboard (deployable via Retool) so you can watch the loop live or review the full history afterward. It closes the observability gap that makes unattended long-running agent loops hard to trust — you see not just the current state but every orchestrator decision, every worker output, token counts, and costs for the entire run history.

_All claims below are sourced from ../../raw/github/coleam00-agent-control-plane.md unless otherwise noted._

## What it does

The harness provides two loop modes: **orchestrated** (the default) and **ralph**. In orchestrated mode, a dedicated LLM orchestrator agent reads the current `PROGRESS.md` state with read-only tools and either declares the goal done or writes prompts for the next batch of worker agents — which then execute with full tools. Independent tasks fan out and run in parallel; the orchestrator, not a regex sentinel, decides when to stop. In ralph mode, a fixed prompt re-runs one worker agent each round until it emits `LOOP_STATUS: DONE`, matching the classic single-agent loop pattern from the [[snarktank-ralph]] and [[frankbria-ralph-claude-code]] projects.

State is never held in a model's context: `PROGRESS.md` lives on disk, and every run is flushed to Neon before the next round begins. A loop that hits its iteration cap parks at `awaiting_approval`; a `POST /api/loops/:id/resume` call (or a button in the dashboard) is the human gate before more compute is spent.

## Installation

Prerequisites: Bun, Pi installed and authenticated for your target provider, a Neon project.

```bash
cp .env.example .env
# Set DATABASE_URL (Neon pooled connection string)
# Set PI_MODEL (e.g. anthropic/claude-sonnet-4, openai/gpt-4o, ollama/llama3.1:8b)

cd backend && bun install
bun run migrate   # creates loops / runs / run_events tables in Neon
bun run smoke     # verifies Neon connection + one real Pi run
bun run dev       # API on http://localhost:8787

cd ../frontend && bun install
bun run dev       # dashboard on http://localhost:5173
```

## Key features

- **Provider-agnostic via Pi** — delegates all model calls to [[pi.dev]], inheriting Pi's full provider roster (Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Groq, local via Ollama/vLLM/LM Studio); switching providers is a one-line `PI_MODEL=` change and zero code edits
- **Durable run history** — every run lands in Neon with role (`orchestrator`/`worker`), output, token count, `cost_usd`, status, and `parent_run_id` linking workers to the orchestrator decision that spawned them
- **Human resume gate** — loops cap at `maxIterations`; the `awaiting_approval` state surfaces in the dashboard with a resume button, enabling manager approval before additional spend
- **Two loop modes** — orchestrated fan-out (agents prompting agents) and ralph (single-agent sentinel loop); selectable per-run via the `mode` field in the POST body
- **React + Retool dashboard** — live view of the current orchestrator decision and its spawned workers; full history panel; importable as Retool source code with a Postgres connector wired to Neon for direct reads
- **Integration test suite** — `ACP_FAKE_PI=1` server mode enables fast, deterministic integration tests without real Pi invocations (`bun run itest`)

## Architecture

The backend is a Bun/TypeScript Hono HTTP server. `pi.ts` spawns `pi --mode json --print` as a subprocess and parses its NDJSON event stream, abstracting Pi's streaming output into typed run events. `loop.ts` implements the two loop modes on top of this interface: for orchestrated mode it calls the orchestrator agent, parses its structured output (next tasks or done decision), then fans out worker agent calls in parallel using `Promise.all`; for ralph mode it calls the worker agent in a simple while loop and inspects the sentinel. `db.ts` manages three Neon tables: `loops` (goal, mode, status, iteration counts), `runs` (per-agent invocations with role, tokens, cost, parent_run_id), and `run_events` (raw streaming event log per run).

State isolation between rounds is structural, not instructed: each Pi invocation starts with a fresh context containing only `PROGRESS.md` and the prompt written by the orchestrator. No accumulating chat history means no context-creep over long runs — the same pattern documented in [[snarktank-ralph]].

The frontend is a Vite + React app. Retool deployment zips the source (not a build) and imports it via Retool's React importer; Retool reads Neon directly via a Postgres resource connector for the history panel, and calls the backend's gated API endpoints for mutation actions (resume, pause, stop) so auth and audit trail stay in Retool.

## Example usage

```bash
# Start an orchestrated loop (agents prompting agents)
curl -s localhost:8787/api/loops -X POST \
  -H 'content-type: application/json' \
  -d '{"goal":"Build a CLI todo app in Python with pytest tests","maxIterations":5,"mode":"orchestrated"}'

# Check loop status + runs
curl localhost:8787/api/loops/<id>

# Resume a paused loop (human gate)
curl -s localhost:8787/api/loops/<id>/resume -X POST \
  -H 'content-type: application/json' \
  -d '{"extraIterations":3}'

# Sanity-check Pi + model before wiring in
pi --mode json --print --no-session --model anthropic/claude-sonnet-4 -p "say PI OK"
```

## Maintenance status

Early-stage — 25 stars, no releases, last pushed 2026-06-16. By Cole Medin, who also authored [[coleam00-archon]] and [[coleam00-harness-engineering-demo]]. Licensed MIT. The harness is intentionally narrow in scope (a reference implementation of the durable-loop + human-gate pattern) rather than a full framework.
