---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://vercel.com
tags:
  - agentic-infrastructure
  - ai-sdk
  - ai-gateway
  - deployment-platform
  - sandbox
  - workflows
  - mcp
  - serverless
related:
  - skills.sh
  - trigger.dev
  - litellm.ai
  - langchain.com
  - supabase.com
  - browserbase.com
  - must-have-clis-2026
  - ollama-ollama
  - pydantic.dev
  - developers.openai.com
  - render.com
  - claudemarketplaces.com
  - neon.com
  - docusaurus.io
  - higgsfield.ai
  - ai-sdk.dev
product: vercel
detail_level: standard
created: 2026-07-07
updated: 2026-07-28
---

Vercel positions itself as "Agentic Infrastructure" — the AI Cloud for building, deploying, and scaling AI-powered applications and agentic workloads. The platform combines a deployment and edge-compute layer (Fluid Compute, global CDN, serverless Functions, CI/CD) with an Agent Stack (AI SDK, AI Gateway, Sandbox, Workflows, Passport, eve) and agent-native tooling (CLI, MCP server, Vercel Plugin, Agent Skills via [[skills.sh]]). Coding agents can deploy via API/CLI/MCP, run untrusted code in isolated sandboxes, orchestrate durable workflows, and route model calls through a unified gateway — all on the same infrastructure that serves Notion, Zapier, and Mintlify at scale.

_All claims below are sourced from ../../raw/web/vercel.com.md unless otherwise noted._

## What it does

Vercel is a unified cloud platform for shipping web apps, AI applications, and autonomous agents. At the infrastructure level it handles Git-connected deployments, preview environments, edge routing, observability, and security (WAF, Bot Management, BotID). For agentic AI specifically, it provides:

- **Build layer:** AI SDK (unified LLM API), AI Gateway (hundreds of models through one endpoint), MCP support (deploy MCP servers, use Vercel MCP), and eve (filesystem-first durable agent framework).
- **Run layer:** Vercel Sandbox (Firecracker microVM isolation for untrusted/agent-generated code), Workflows (durable pause/resume orchestration), Fluid Compute (optimized serverless concurrency), Functions, Queues, and Container Registry.
- **Agent operations:** Vercel Agent (autonomous error investigation and PR creation), Vercel Plugin (`npx plugins add vercel/vercel-plugin` for Claude Code/Cursor), Agent Skills distribution, CLI (`vercel deploy`, `vercel dev`, `vercel env pull`), and Passport (identity provider integration for internal agents and deployments).

The homepage frames three use-case pillars: build agents on infrastructure that "thinks like them" (durable orchestration, sandboxed environments, AI model gateway), ship apps that scale instantly (global delivery, serverless functions), and host multi-tenant platforms (tenant isolation, domain management, preview URLs).

## Key features

**Agent Stack**

- **AI SDK** — TypeScript-first library with unified provider API (`generateText`, `generateObject`, `streamObject`), tool calling, streaming, and framework support (React, Next.js, Vue, Svelte, Node.js). Switch providers by changing the model string.
- **AI Gateway** — Single endpoint for hundreds of models; budgets, usage monitoring, load balancing, fallbacks, provider allowlists, automatic caching, routing rules. Works with AI SDK v5/v6, OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, and other framework integrations.
- **Sandbox** — Isolated Firecracker microVMs for untrusted code (AI agent output, user uploads). JS SDK (`@vercel/sandbox`), Python SDK (`vercel.sandbox`), CLI. Persistent sandboxes, snapshotting, tags, drives (beta). Runtimes: node26/24/22, python3.13.
- **Workflows** — Durable JavaScript/TypeScript/Python workflows built on the open-source Workflow SDK. Resumable (pause minutes to months), crash-safe deterministic replays, built-in observability. Uses Vercel Functions + Queues + managed persistence.
- **Passport (beta)** — Secure internal agents, apps, and deployments with your identity provider.
- **eve (beta)** — Filesystem-first framework for durable backend AI agents. Defines agents under an `agent/` directory; compiles to Vercel Functions. Uses Workflows, Sandbox, AI Gateway, and Connect internally.

**Core platform**

- **Fluid Compute** — Hybrid serverless/server-like compute: optimized concurrency (multiple invocations per instance), dynamic scaling, background processing via `waitUntil`, bytecode caching, cross-AZ/region failover. Enabled by default for new projects since April 2025.
- **Deployments & CI/CD** — Git integration, preview URLs, instant rollback, rolling releases, Dockerfile/container support on Fluid compute.
- **Observability** — Logs, metrics, tracing; dedicated workflow and AI Gateway dashboards.
- **Security** — WAF, bot management, BotID, deployment protection, compliance tooling.

**Agent-native developer experience**

- **CLI** — `vercel login`, `vercel deploy`, `vercel dev` (local production parity), `vercel env pull .env.local`.
- **MCP** — Deploy MCP servers on Vercel; Vercel's own MCP server for agent access to deployment/project context.
- **Vercel Plugin** — For Claude Code and Cursor: `npx plugins add vercel/vercel-plugin`.
- **Agent Skills** — Links to [[skills.sh]] ecosystem: `npx skills add vercel-labs/agent-skills` for other coding agents.

## Architecture and concepts

Vercel's agentic architecture stacks three layers:

1. **Agent Stack (build)** — AI SDK and AI Gateway handle model abstraction and routing. MCP standardizes tool/data access for LLMs. eve composes Workflows + Sandbox + Gateway + Connect into a filesystem-defined agent runtime.
2. **Compute (run)** — Fluid Compute Functions execute request/response and background work. Sandbox provides isolated execution for code agents generate. Workflows add durable state and long-running orchestration atop Functions and Queues.
3. **Ship & govern (operate)** — Global CDN, preview deployments, observability, and Passport/security wrap production agent workloads.

The docs organize capabilities into: Build AI apps → Run agents and backends → Ship and scale → Observe and improve → Secure and govern. Framework support spans full-stack (Next.js, SvelteKit, Nuxt, TanStack Start), backends (FastAPI, Hono, Express, xmcp), and agent-specific runtimes (eve).

## Main APIs

| Surface | Purpose |
|---|---|
| AI SDK (`ai` npm package) | `generateText`, `streamText`, `generateObject`, `streamObject`, tool calling |
| AI Gateway REST/SDK | Unified model endpoint; provider/model string routing (`anthropic/claude-opus-4.8`, `openai/gpt-5.5`) |
| `@vercel/sandbox` / `vercel.sandbox` | Create sandboxes, run commands, manage files |
| Workflow SDK | `'use workflow'` / `'use step'` directives for durable functions |
| Vercel CLI | Deploy, dev, env management |
| REST API / Vercel SDK | Project, deployment, domain, and platform management |
| MCP | Deploy and consume Model Context Protocol servers |

Getting started flow: install CLI → optionally add Vercel Plugin (Claude Code/Cursor) or Agent Skills (other agents) → deploy with `vercel`.

## When to use

- You want one platform to **build, deploy, and operate** AI apps and agents without stitching together separate hosting, model routing, and sandbox vendors.
- Your coding agent needs **native deploy tooling** — CLI, MCP, plugin, and skills integrations let agents ship autonomously.
- You need **safe code execution** for agent-generated output (Sandbox) or **durable long-running agent loops** (Workflows, eve) without managing your own orchestration infrastructure.
- You want a **unified model gateway** with budgets, fallbacks, and observability instead of wiring each provider separately — compare [[litellm.ai]] and [[openrouter.ai]] for self-hosted/multi-cloud alternatives.
- You already use Next.js/React and want AI SDK + Gateway + deployment on the same stack.
- You need **multi-tenant SaaS hosting** with preview URLs, domain management, and tenant isolation (Mintlify, Zapier-style platforms).

Less ideal when you need fully self-hosted/on-prem infrastructure, deterministic workflow DSLs (compare [[trigger.dev]] for checkpoint-resume without workflow constraints, or Temporal-class engines), or deep local-only development without cloud dependency (compare [[ollama-ollama]] for local inference).

## Ecosystem

- **Skills & agents:** [[skills.sh]] (Vercel-built open skills directory and `npx skills` CLI), Vercel Plugin, Agent Skills repo (`vercel-labs/agent-skills`), Vercel Agent for autonomous debugging/PRs.
- **Frameworks:** Next.js (Vercel-created), eve, SvelteKit, Nuxt, FastAPI, xmcp (MCP server framework), Turborepo.
- **Integrations:** Supabase, Stripe, and 100+ marketplace integrations; AI SDK works with LangChain, LangGraph, CrewAI, Mastra, and other frameworks documented across this wiki ([[langchain.com]], [[pydantic.dev]], [[crewai.com]]).
- **Customers cited:** Notion (agent conversations), Zapier (100M+ monthly visits), Mintlify (20K+ companies).
- **Related infrastructure:** [[browserbase.com]] lists Vercel as a customer; [[trigger.dev]] explicitly contrasts its no-timeout background tasks with Vercel serverless limits; [[must-have-clis-2026]] highlights Vercel CLI for preview deploys and env parity.
