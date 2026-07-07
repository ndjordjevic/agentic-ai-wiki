---
type: source
source_url: https://trigger.dev/
companion_urls:
  - https://github.com/triggerdotdev/trigger.dev
raw_files:
  - ../../raw/web/trigger.dev.md
  - ../../raw/github/triggerdotdev-trigger.dev.md
tags:
  - background-jobs
  - durable-execution
  - ai-agents
  - typescript
  - checkpoint-resume
  - human-in-the-loop
  - realtime-streaming
  - mcp-server
related:
  - abacus.ai
  - n8n.io
  - zapier.com
  - langchain.com-langgraph
  - crewai.com
  - postiz.com
  - marketstack.com
  - adk.dev
  - google-adk-go
  - microsoft-agent-framework
  - app.sauna.ai
  - supabase.com
product: trigger
detail_level: standard
created: 2026-07-03
updated: 2026-07-07
---

Trigger.dev is an Apache 2.0 open-source platform (15.5k+ GitHub stars, v4.5.0 GA July 2026) for building AI agents and durable TypeScript workflows without workflow DSLs or determinism constraints. Developers write plain `async/await` tasks in their existing codebase, deploy with `npx trigger.dev deploy`, and get checkpoint-resume durability (CRIU snapshots), no timeouts, elastic scaling, queues, automatic retries, human-in-the-loop waitpoints, realtime run/LLM streaming to React hooks, OpenTelemetry observability, and an MCP server for coding agents — on Trigger.dev Cloud or self-hosted via Docker/Kubernetes.

_All claims below are sourced from ../../raw/web/trigger.dev.md unless otherwise noted._

## What it does

Trigger.dev offloads long-running background work — AI agent loops, multi-step LLM pipelines, media processing, scheduled cron, multi-tenant SaaS jobs — from request/response servers into a managed execution layer. Tasks are exported functions in a `trigger/` folder in the developer's repo; the app triggers them via the SDK and receives a run handle immediately while work continues in the background.

Unlike deterministic workflow engines (Temporal, Restate, DBOS), Trigger.dev requires no special DSL or replay-safe code — any npm package and normal TypeScript patterns work. Unlike serverless functions (Lambda, Vercel), tasks have no execution timeout and paused/waiting time consumes no compute or billing on Cloud.

## Key features

- **Durable tasks in plain TypeScript:** `task({ id, run })` with automatic retries, idempotency keys, `triggerAndWait` for subtasks, and `wait.for()` / waitpoint tokens for delays and external events.
- **AI agents (v4.5 GA):** `chat.agent()` with tool calling, `needsApproval` for human-in-the-loop, `streamText` integration, and patterns for autonomous agents, prompt chaining, routing, parallelization, orchestration, and evaluator-optimizer flows.
- **Checkpoint-resume:** CRIU snapshots capture full process state during waits; resources release while paused; resume is exact — successful prior work is not re-run on retry. (../../raw/github/triggerdotdev-trigger.dev.md)
- **Realtime:** `useRealtimeRun` for run status/metadata in React UIs; `useRealtimeStream` + `streams.define()` for LLM token streaming — no WebSockets or polling required.
- **Build extensions:** One-line config for Prisma, FFmpeg, Puppeteer, Playwright, Python (`requirements.txt`), apt-get system packages, esbuild plugins, and custom Docker layers.
- **MCP server:** `npx trigger.dev install-mcp` wires Claude Code, Cursor, Windsurf, VS Code, Codex CLI, and 10+ other clients to search docs, trigger tasks, deploy, and query runs/TRQL metrics.
- **Multi-environment:** DEV, STAGING, PREVIEW (branch-isolated), and PROD with atomic versioning so in-flight runs are unaffected by deploys.

## Architecture

Trigger.dev implements a serverless-style architecture without timeouts: deploy builds task code via esbuild into a Docker image; the orchestrator schedules runs onto elastic worker pools with configurable Machines (vCPU/RAM). The Checkpoint-Resume System uses CRIU to snapshot task state when waiting on subtasks (`triggerAndWait`), timed waits (`wait.for`), or waitpoint tokens (`wait.forToken`); checkpoints compress to disk and restore on event-driven resumption. (../../raw/github/triggerdotdev-trigger.dev.md)

Durable execution combines checkpointing with idempotency keys on subtasks — retries replay only from the failed step, using cached results for completed subtasks. OpenTelemetry powers the trace view in the dashboard with auto-correlated parent/child logs; custom instrumentations (Prisma, AWS SDK) plug in via `trigger.config.ts`. (../../raw/github/triggerdotdev-trigger.dev.md)

The monorepo (`apps/`, `packages/`, `hosting/`, `docs/`) ships the same codebase for Cloud and self-hosted deployments. Realtime run updates use Electric SQL (PostgreSQL sync); streams use a separate transport layer. (../../raw/github/triggerdotdev-trigger.dev.md)

## Installation

```shell
npx trigger.dev@latest login
npx trigger.dev@latest init
npx trigger.dev@latest dev    # local task execution against cloud scheduler
npx trigger.dev@latest deploy # build + deploy to Cloud or self-hosted profile
```

Self-hosted: Docker Compose or Kubernetes Helm chart per `hosting/` docs. MCP: `npx trigger.dev@latest install-mcp --client cursor` (or `--yolo` for all clients). (../../raw/github/triggerdotdev-trigger.dev.md)

## Example usage

**Define and trigger a task:**

```ts
import { task } from "@trigger.dev/sdk";

export const helloWorld = task({
  id: "hello-world",
  run: async (payload: { message: string }) => {
    console.log(payload.message);
  },
});
```

```ts
import { tasks } from "@trigger.dev/sdk";
import type { helloWorld } from "./trigger/hello";

const handle = await tasks.trigger<typeof helloWorld>("hello-world", { message: "Hi" });
```

**Human-in-the-loop waitpoint:**

```ts
import { wait } from "@trigger.dev/sdk";

const token = await wait.createToken({ timeout: "10m" });
// Pass token.id + token.publicAccessToken to frontend for approval UI
const result = await wait.forToken<{ status: "approved" | "rejected" }>(token.id);
```

**MCP from a coding agent:** `"Trigger my foobar task with a sample payload"` or `"Deploy my project to staging"` after `install-mcp`. (../../raw/github/triggerdotdev-trigger.dev.md)

## When to use

Choose Trigger.dev when you need **code-first**, **TypeScript-native** durable execution for AI agents or long background jobs and want to avoid operating Redis/BullMQ queues, Temporal worker clusters, or splitting work into serverless-sized chunks. Strong fit for: streaming AI UIs with HITL approvals, FFmpeg/browser/Python-heavy tasks via build extensions, per-tenant SaaS concurrency, and teams already using MCP-aware coding agents who want deploy/trigger/monitor from the IDE.

Less ideal when you need visual workflow builders ([[n8n.io]]), no-code automation ([[zapier.com]]), or a Python-first agent framework ([[crewai.com]], [[adk.dev]]) — though Trigger.dev tasks can call any of those as external services.

## Maintenance status

- **Stars:** 15,545 | **License:** Apache 2.0 | **Latest release:** v4.5.0 (2026-07-02) | **Default branch:** main
- **Cloud pricing:** Free ($5 credit), Hobby $10/mo, Pro $50/mo — compute-seconds + per-run fee; paused time not billed
- **Compliance:** SOC 2 Type II, GDPR; HIPAA BAA on Enterprise
- Actively maintained monorepo with `AGENTS.md`/`CLAUDE.md` for contributor agents; large adopter base (Cal.com, Midday, Magic Patterns, Resend, Unkey). (../../raw/github/triggerdotdev-trigger.dev.md)

## Ecosystem

- **Integrations:** Vercel, GitHub, Resend, Supabase, Stripe, OpenAI/Vercel AI SDK, Deepgram, Firecrawl, Browserbase, Sentry — plus 30+ example task templates.
- **Comparisons published:** vs Temporal (no DSL/determinism), vs BullMQ (no Redis ops), vs n8n (code-first vs visual).
- **Agent tooling:** MCP server + Skills for AI coding assistants; complements harness frameworks ([[langchain.com-langgraph]], [[microsoft-agent-framework]]) as the **execution/runtime layer** agents offload durable work to.
- **Self-host:** Same Apache 2.0 stack as Cloud — Docker Compose or Kubernetes; active Discord community.

## Documentation

Docs at `trigger.dev/docs` with `llms.txt` catalog. Key areas: quick start, how-it-works (checkpoint-resume), AI agents guide, Realtime (hooks + streams), waitpoints/HITL, build extensions, self-hosting, Management API, MCP, and production examples (FFmpeg, Puppeteer, OpenAI, Fal.ai, etc.).
