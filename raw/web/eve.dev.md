# eve.dev

## Fetch log
- Inbox URL: https://eve.dev/
- Final URL: https://eve.dev/
- Fetched: 2026-07-21
- Pages: 7
- Mode: standard

## Landing page — https://eve.dev/
Title: eve

URL Source: https://eve.dev/

Markdown Content:
[](https://vercel.com/oss)

*   [](https://eve.dev/)
*   [Docs](https://eve.dev/en/docs)
*   [Integrations](https://eve.dev/en/integrations)
*   [Templates](https://eve.dev/en/templates)
*   [GitHub](https://github.com/vercel/eve/)

Search…⌘K Ask AI Ask AI[](https://github.com/vercel/eve)

[Docs](https://eve.dev/en/docs)[Integrations](https://eve.dev/en/integrations)[Templates](https://eve.dev/en/templates)[GitHub](https://github.com/vercel/eve/)[GitHub](https://github.com/vercel/eve)

# The framework for building agents

Like Next.js for agents. Build durable agents with one folder.

## Your agent/is a directory

An instructions.md file is all you need to run an agent. Skills, tools, channels, and the rest are optional building blocks you add as it grows.

## Works natively with Next.js

Wrap your config with withEve() and the agent mounts into your existing app. Same dev server, same deploy.

## Built on open-source SDKs, yours to self-host

Swap any backend and self-host the whole runtime, with zero managed-infrastructure dependencies.

## Everything you need for production agents

- Durable Execution — workflows survive crashes and restarts; every step is checkpointed.
- Sandboxed Compute — isolated execution for code and shell.
- Multi-Channel Delivery — one agent codebase can serve web chat, Slack, API, cron, and CLI surfaces.
- Human-in-the-Loop — approval and pause/resume flows.

## Docs — https://eve.dev/docs
Title: Introduction

URL Source: https://eve.dev/docs

Markdown Content:
How an eve agent is laid out as files, what runs when a message arrives, and the building blocks you add as it grows.

eve is a framework for building durable agents as ordinary files in a TypeScript project.

A small eve app looks like this:

```text
my-agent/
├── package.json
└── agent/
    ├── agent.ts
    ├── instructions.md
    ├── tools/
    ├── skills/
    └── channels/
```

Filesystem-first model:
- instructions in `instructions.md`
- model/runtime config in `agent.ts`
- typed tools in `tools/`
- skills in `skills/`
- channels in `channels/`

Durability highlights:
- stream progress
- call tools/subagents
- pause for approval or human input
- resume after input
- keep durable state across turns

## Introduction — https://eve.dev/docs/introduction
Title: Introduction

URL Source: https://eve.dev/docs/introduction

Markdown Content:
How an eve agent is laid out as files, what runs when a message arrives, and the building blocks you add as it grows.

eve is a framework for building durable agents as ordinary files in a TypeScript project.

As an agent grows, concerns map to predictable authored paths:
- `connections/` for external MCP/OpenAPI tools
- `hooks/` for lifecycle and stream reactions
- `sandbox/` for controlled file/command execution
- `subagents/` for specialist delegation
- `schedules/` for recurring work
- `lib/` for shared code

## Getting Started — https://eve.dev/docs/getting-started
Title: Getting Started

URL Source: https://eve.dev/docs/getting-started

Markdown Content:
Install eve, scaffold your first agent, give it a tool, and run it locally.

Prerequisites:
- Node 24+
- npm
- model credential (`AI_GATEWAY_API_KEY`, `VERCEL_OIDC_TOKEN`, or provider-specific key such as `ANTHROPIC_API_KEY`)

Quick start:
```bash
npx eve@latest init my-agent
```

Manual path:
```bash
npm install eve@latest ai zod
npx eve dev
```

HTTP session lifecycle examples:
- `POST /eve/v1/session` to start a durable session
- `GET /eve/v1/session/<id>/stream` to stream NDJSON events
- `POST /eve/v1/session/<id>` with `continuationToken` to continue

## MCP Connections — https://eve.dev/docs/connections/mcp
Title: MCP Connections

URL Source: https://eve.dev/docs/connections/mcp

Markdown Content:
Connect an eve agent to a remote MCP server, authorize it with Vercel Connect or static credentials, and control which tools the model can discover.

Key patterns:
- define a connection in `agent/connections/<name>.ts` with `defineMcpClientConnection`
- auth via `connect(...)` (Vercel Connect OAuth) or static `auth.getToken`
- optional `headers` for non-bearer schemes
- scope tool surfaces with `tools.allow` / `tools.block`
- gate risky tools using approval policies (`once`, `always`, or custom approval fn)

## Evals Overview — https://eve.dev/docs/evals/overview
Title: Overview

URL Source: https://eve.dev/docs/evals/overview

Markdown Content:
Define repeatable scored checks for an eve agent with `defineEval` and run them with `eve eval`.

Highlights:
- eval files under `evals/*.eval.ts`
- `defineEvalConfig` for shared defaults (judge model, reporters, concurrency, timeouts)
- deterministic fixture models via `mockModel`
- run-level and value-level assertions (`t.succeeded`, `t.calledTool`, `t.check`, `t.judge.*`)
- `eve eval` for local or remote targets

## Channels Overview — https://eve.dev/docs/channels/overview
Title: Overview

URL Source: https://eve.dev/docs/channels/overview

Markdown Content:
How users reach your agent: the channel contract, the base eve HTTP channel, and authoring custom channels.

Channel responsibilities:
- normalize platform input into a user message
- own continuation tokens for that surface
- define delivery behavior for responses

eve channel notes:
- base HTTP channel is enabled by default
- channels are authored in `agent/channels/`
- built-in and first-class channel support includes web/HTTP, Slack, Discord, Teams, Telegram, Twilio, GitHub, and Linear
