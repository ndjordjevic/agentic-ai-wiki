# coleam00/agent-control-plane

## Metadata
- Stars: 25
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-06-30
- Final URL: https://github.com/coleam00/agent-control-plane

## Description
A control plane for long-running agent loops: agents prompting agents on Pi, run history in Neon, a React dashboard, deployable with Retool.

## README

# Agent Control Plane

> Long-running agent loops you can actually watch. Give it a goal; agents prompt agents until it's done; every run is recorded so you can see what they did while you stepped away.

A control plane for long-running agent loops, built on **Pi** (a provider-independent coding agent) with run history in **Neon** (serverless Postgres) and a **React** dashboard. You give it a goal; it runs a loop until the goal is met, recording every run so you can see what your agents did, not just what they are doing right now. Because it drives Pi rather than any one model API, the same loop runs on Claude, GPT, Gemini, Kimi, or a local model.

## How it works

Two loop modes:

- **orchestrated (default): agents prompting agents.** Each round an LLM **orchestrator** agent inspects progress (with read-only tools) and decides either that the goal is done or what the next task(s) are. It writes the prompts that **worker** agents then execute (with full tools). Independent tasks fan out and run in parallel. The orchestrator makes the continue/done call, not a regex.
- **ralph: the classic single-agent loop.** A fixed prompt re-runs one worker agent each round; a sentinel in its output (`LOOP_STATUS: DONE`) ends the loop.

State lives on disk (a `PROGRESS.md` per loop) and in Neon, never in a model's context, so every round starts with a fresh context. The human gate is the resume action: a loop that hits its iteration cap parks in `awaiting_approval` until you approve more rounds.

Every run (orchestrator or worker) lands in Neon with its role, output, tokens, status, and a link to the orchestrator decision that spawned it. The dashboard shows the live loop plus the full history.

```
orchestrated round:                         Neon                      React dashboard -> Retool
orchestrator agent decides  ──┐      loops / runs / run_events         live: orchestrator decision
   ├─ done -> stop            │  ->  (role: orchestrator|worker,   ->  + the workers it spawned;
   └─ tasks -> worker agents ─┘      parent_run_id, reasoning,         full run history; the human
      (fan out in parallel)          output, tokens, status)           resume gate
```

## Models and providers

The control plane never talks to a model directly. It drives **Pi**, and Pi resolves the model and provider from its own auth. So the whole loop (orchestrator and workers) runs on whatever Pi supports: Claude, GPT, Gemini, Kimi, or a local model. Switching is two steps and zero code changes.

**1. Authenticate Pi for the provider you want** (once). Either a subscription login (run `pi`, then `/login`) or an API key in your environment:

| Provider | Env var |
|----------|---------|
| Anthropic / Claude | `ANTHROPIC_API_KEY` |
| OpenAI | `OPENAI_API_KEY` |
| Google Gemini | `GEMINI_API_KEY` |
| Kimi (Moonshot) | `KIMI_API_KEY` |

Pi also supports DeepSeek, Mistral, Groq, xAI, OpenRouter, Azure OpenAI, Amazon Bedrock, Vertex AI, and local runtimes (Ollama, vLLM, LM Studio).

**2. Set `PI_MODEL`** in `backend/.env`:

```bash
PI_MODEL=anthropic/claude-sonnet-4     # Claude
PI_MODEL=openai/gpt-4o                  # OpenAI
PI_MODEL=kimi-coding/kimi-for-coding    # Kimi (the default)
PI_MODEL=ollama/llama3.1:8b             # a local model
```

## Project layout

| Path | What |
|------|------|
| `backend/` | Bun + TypeScript. Drives the Pi loop, persists to Neon, serves the JSON API (Hono). |
| `backend/src/pi.ts` | Spawns `pi --mode json --print` and parses its event stream. |
| `backend/src/loop.ts` | The loop driver: orchestrated (orchestrator + workers) and ralph modes, the decision parser, fan-out, and the human resume gate. |
| `backend/src/db.ts` | Neon access + the `loops` / `runs` / `run_events` schema. |
| `backend/migrations/` | `001_init.sql` (base schema) + `002_orchestrator.sql` (mode, role, parent_run_id, reasoning). |
| `backend/src/itest.ts` | Integration suite (`bun run itest`, needs the server in `ACP_FAKE_PI=1` mode). |
| `frontend/` | Vite + React + TS dashboard (mode selector, orchestrator/worker view). The artifact you deploy with Retool. |

## Prerequisites

- Bun (backend runtime)
- Pi installed and on PATH, authed for your provider
- A Neon project (serverless Postgres). Copy its pooled connection string.

## Setup

```bash
cp .env.example .env
# edit .env: paste DATABASE_URL (Neon), set PI_MODEL

cd backend
bun install
bun run migrate     # create the tables in Neon
bun run smoke       # end-to-end: Neon connection + one real Pi run
bun run dev         # API on http://localhost:8787
```

```bash
cd frontend
bun install
bun run dev         # dashboard on http://localhost:5173
```

Start a loop:
```bash
curl -s localhost:8787/api/loops -X POST \
  -H 'content-type: application/json' \
  -d '{"goal":"Build a small CLI todo app in Python with pytest tests","maxIterations":5,"mode":"orchestrated"}'
```

## API

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/health` | liveness + active model |
| GET | `/api/loops` | all loops |
| GET | `/api/loops/:id` | one loop + its runs |
| POST | `/api/loops` | start a loop `{goal, maxIterations, mode?}` |
| POST | `/api/loops/:id/resume` | human gate: continue past iteration cap |
| POST | `/api/loops/:id/pause` | pause after current run |
| POST | `/api/loops/:id/stop` | stop the loop |
| GET | `/api/runs` | full run history |
| GET | `/api/runs/:id` | one run + its streamed events |

## Deploying with Retool

The dashboard is a standard React app deployable with Retool:

1. Zip the `frontend/` source (Retool's React importer takes source, not a build).
2. In Retool: **Create > App > Chat tab > Import React code**, select the zip.
3. Add a Retool **Postgres resource** pointed at the same `DATABASE_URL` (reads straight from Neon via managed connector).
4. Wire the **resume** action behind a confirm dialog and a manager-only permission; enable Retool's audit log for the trail.

The Bun/TS backend is not imported into Retool; Retool talks to Neon directly for reads, and to the backend's gated endpoints for actions.

## Top-level structure

```
.env.example          — environment variable template
.gitignore
LICENSE               — MIT
README.md
backend/              — Bun + TypeScript API server
  migrations/         — SQL migrations (001_init.sql, 002_orchestrator.sql)
  src/
    config.ts         — configuration
    db.ts             — Neon access + loops/runs/run_events schema
    itest.ts          — integration test suite (ACP_FAKE_PI=1)
    loop.ts           — loop driver: orchestrated + ralph modes, fan-out, human gate
    migrate.ts        — migration runner
    pi.ts             — Pi subprocess interface (--mode json --print event stream)
    server.ts         — Hono API server
    smoke.ts          — smoke test (Neon connection + one real Pi run)
    util.ts / util.test.ts
  package.json        — Bun scripts: dev, migrate, smoke, test, itest
  tsconfig.json
frontend/             — Vite + React + TypeScript dashboard
  src/                — React components (mode selector, orchestrator/worker view)
  index.html
  vite.config.ts
  package.json
  tsconfig.json
```
