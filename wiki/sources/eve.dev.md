---
type: source
category: "Agent frameworks & SDKs"
source_url: https://eve.dev/
companion_urls:
  - https://github.com/vercel/eve
raw_files:
  - ../../raw/web/eve.dev.md
  - ../../raw/github/vercel-eve.md
tags:
  - eve-framework
  - filesystem-first-agents
  - durable-sessions
  - mcp-connections
  - multi-channel-agents
  - eval-driven-development
  - vercel-ai
related:
  - adk.dev
  - pydantic-pydantic-ai
  - coleam00-eve-analyst
product: eve
detail_level: standard
created: 2026-07-21
updated: 2026-07-21
---

`eve.dev` documents **eve**, Vercel’s filesystem-first framework for durable agents: agents are authored as ordinary folders (`instructions`, `tools`, `skills`, `channels`, `connections`, `subagents`, `schedules`) and run through a built-in durable execution harness with pause/resume, streaming, and multi-channel delivery. Paired with its companion repo, it provides both product-level framing and concrete implementation/runtime semantics.

_All claims below are sourced from ../../raw/web/eve.dev.md unless otherwise noted._

## What it does

eve positions agent development as a directory-native workflow instead of a monolithic orchestration config. Core capabilities are discovered by path, then composed into one runtime that can serve HTTP sessions, connect to platform channels, call tools and subagents, and persist/continue long-running work. The docs emphasize durability, human-in-the-loop control, and operational portability across web/app/CLI surfaces.

## Key features

From the docs and landing surface, key primitives include filesystem-derived capability discovery, default durable session APIs, built-in channel model, MCP/OpenAPI connection integrations, and first-class eval tooling. The companion repository reinforces this with an actively maintained TypeScript monorepo and versioned CLI/framework release train (`eve@0.26.1`, `main` branch, Apache-2.0). (../../raw/github/vercel-eve.md)

## Architecture

The implementation surface is split between authored agent files and framework internals: agent projects declare behavior in `agent/*`, while the framework/runtime/CLI live in `packages/eve` inside a pnpm+turborepo monorepo with supporting docs apps, fixtures, e2e suites, and invariant guards. The AGENTS guidance also codifies repository design principles (small composable modules, file-path-derived naming, and runtime ownership in `eve` package). (../../raw/github/vercel-eve.md)

## Installation

Quick start:

```bash
npx eve@latest init my-agent
```

Manual bootstrap:

```bash
npm install eve@latest ai zod
npx eve dev
```

The canonical docs require Node 24+ and describe both direct-provider and AI Gateway credential paths. (../../raw/github/vercel-eve.md)

## Example usage

```bash
curl -X POST http://127.0.0.1:2000/eve/v1/session \
  -H 'content-type: application/json' \
  -d '{"message":"What is the weather in Brooklyn?"}'
curl http://127.0.0.1:2000/eve/v1/session/<sessionId>/stream
```

This models the core session lifecycle: create, stream NDJSON events, then continue with a `continuationToken`. (../../raw/github/vercel-eve.md)

## When to use

Use eve when you want a codebase-native framework for production agent apps that need durability, auditability, explicit capability boundaries, and transport flexibility (HTTP, web chat, Slack/Discord/Teams/etc.). It is especially strong when teams want convention-based structure instead of bespoke orchestration glue.

## Maintenance status

Companion repo health: 3,916 stars, 367 forks, last push 2026-07-21, latest release `eve@0.26.1` (2026-07-20), default branch `main`, Apache License 2.0. (../../raw/github/vercel-eve.md)

## Ecosystem

eve’s docs frame channels, MCP/OpenAPI connections, eval/reporting flows, and generated client/server surfaces as one integrated platform; the landing page also points to templates and integrations, and the repo includes a `skills/` directory and docs for channel-specific and connection-specific operational patterns. The framework is tightly aligned with Vercel tooling while remaining self-hostable.

## Documentation

The docs set is broad and structured (`getting-started`, `instructions`, `tools`, `skills`, `subagents`, `sandbox`, `channels`, `connections`, `evals`, `reference`, `tutorial`) and includes both conceptual models (execution/durability/security) and operational workflows (auth, route protection, channel wiring, eval runners).
