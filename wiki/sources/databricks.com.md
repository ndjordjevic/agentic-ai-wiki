---
type: source
category: "Agent frameworks & SDKs"
source_url: https://www.databricks.com/
tags:
  - data-intelligence-platform
  - agent-bricks
  - durable-agent-server
  - unity-gateway
  - managed-agent-memory
  - lakebase
  - mlflow-tracing
  - enterprise-agents
related:
  - gemini-enterprise-agent-platform
  - omnigent-ai-omnigent
  - neon.com
  - litellm.ai
product: databricks
detail_level: standard
created: 2026-10-15
updated: 2026-10-15
---

Databricks is the "Data and AI company" behind Apache Spark, Delta Lake, MLflow, and Unity Catalog. It sells a multi-cloud lakehouse platform on AWS, Azure, and GCP that covers data engineering (Lakeflow), warehousing (Databricks SQL), BI (AI/BI, Genie), ML/GenAI, governance (Unity Catalog), operational Postgres (Lakebase, built on the acquired Neon), and app hosting (Databricks Apps). The 2026 site leads with "One database for AI, apps and agents". For this wiki, the relevant part is the agent developer stack documented on the Developer Hub. **Agent Bricks** hosts custom agents written in any framework (LangGraph, the OpenAI Agents SDK, or anything else) on a managed **agent runtime** with `DurableAgentServer`, which provides streaming, background runs, and crash recovery. It adds **managed memory and session stores** backed by Lakebase, a **Databricks Sandbox** for agent-written code, MLflow tracing and evaluation, and **Unity Gateway**, which governs model, MCP, and skill traffic. Databricks also runs a managed **Omnigent** coding-agent meta-harness and ships official Agent Skills for coding agents. It is an enterprise agent platform in the same category as Google's Gemini Enterprise Agent Platform, AWS Bedrock AgentCore, and Azure AI Foundry, with the difference that it is anchored to the customer's governed lakehouse data.

_All claims below are sourced from ../../raw/web/databricks.com.md unless otherwise noted._

## What it does

- **Unified data + AI platform.** Databricks runs analytical and operational workloads on one open, governed foundation. Data stays in customer-owned S3, ADLS, or GCS in open formats (Parquet, Delta, and Iceberg via UniForm). The company claims more than 20,000 customers, over 60% of the Fortune 500 on the landing page (over 70% in `llms.txt`), and five Gartner Magic Quadrant "Leader" placements.
- **Agent development platform (Agent Bricks).** You write the agent in code with any framework or harness and any model. Agent Bricks supplies the production infrastructure: hosting, durable execution, memory, tools, model access, tracing, and governance.
- **Governed AI traffic (Unity Gateway, formerly Unity AI Gateway).** A single control plane that routes model and MCP requests and enforces rate limits, budgets, guardrails, service policies, and usage tracking across agents, tools, models, and MCPs.
- **Operational database for agents (Lakebase).** Managed serverless Postgres built on Neon that syncs with the lakehouse without custom ETL. It also backs agent memory, sessions, and runtime state.
- **Analytics agents (Genie).** Natural-language analytics over governed data. Genie spaces, now called "Genie Agents", can be wired into apps and used as agent tools.
- **Free Edition.** Serverless SQL, notebooks, MLflow, AI/BI, and Genie at no cost, with no credit card required.

## Key features

- **Agent Bricks CLI (`agentbricks`, experimental):** `init` scaffolds an agent from a LangGraph or OpenAI Agents SDK template, or brings an existing agent. `tools add` attaches MCP servers, Genie Agents, Unity Catalog functions, and sandboxes. `dev` runs the agent locally with traces. `deploy` provisions the stores, tools, and MLflow experiment declared in `agent.toml`, grants access, and deploys the agent as the Databricks app `agent-bricks-<name>`, with 1–5 instances routed by an `X-Routing-Key` header.
- **`DurableAgentServer`** (from `databricks_agentkit` in the `databricks-agentbricks` package, Python 3.10+): a FastAPI app with a single `@app.invoke` async handler. The same handler serves sync, SSE-streaming, and background requests. Invocations are idempotent by client-supplied UUID (reusing an ID for a different request returns `409`), and invocations that share a `session_id` run serially. Clients can reconnect to an event stream after a dropped connection.
- **Crash recovery:** register `@app.recover` and the server starts a replacement attempt within seconds once a run's heartbeats stop. Recovery covers interrupted workers only, not handler errors. Retries are uncapped, so the handler should check `context.attempt`. The LangGraph template resumes from its checkpoint, and the OpenAI Agents SDK template replays the request in the same session.
- **Managed memory and sessions (Beta, Lakebase-backed):** session stores keep append-only conversation items keyed by `actor_id` and `session_id`. Memory stores keep durable facts at filesystem-like paths (for example `/preferences/contact.md`), and recall uses **BM25 full-text search, not vector similarity**. `memory_tools(actor)` adapters for LangGraph and the OpenAI Agents SDK give the model `remember` and `recall` tools with the actor bound in code.
- **Unity Gateway:** an OpenAI-compatible endpoint (`/ai-gateway/mlflow/v1`) for Unity Catalog model services such as `system.ai.claude-sonnet-4-5`, plus BYOK external providers (OpenAI, Anthropic, Bedrock). It adds per-user and per-service rate limits (HTTP 429), budgets that alert or block, per-request usage logs in `system.ai_gateway.usage`, MCP service registration and governance, and governed `SKILL.md` "skills" stored as Unity Catalog securables.
- **Coding-agent governance:** the `ug` CLI (`uv tool install git+https://github.com/databricks/unity-gateway`, then `ug claude`, `ug codex`, and so on) routes Claude Code, Codex, Cursor, and Gemini CLI through Unity Gateway so they share one invoice, one dashboard, and one set of rate limits.
- **Omnigent on Databricks (Beta):** a managed server for the open-source Omnigent meta-harness, giving Codex, Claude Code, Cursor, Pi, and 10+ other harnesses one shared web, desktop, and mobile UI. Sessions are shareable and run on a Databricks Sandbox or on a registered laptop or VM, with model access through Unity Gateway.
- **Official Agent Skills:** `databricks aitools install` detects installed coding agents. It installs a `databricks` plugin for Claude Code, Codex CLI, and GitHub Copilot, and links raw skill files from `~/.databricks/aitools/skills/` for Cursor, OpenCode, and Antigravity. The skills are published in `databricks/databricks-agent-skills` and follow the agentskills.io standard. A DevHub Docs MCP Server gives coding agents read access to the docs.

## Architecture and concepts

**Agent compute stack (three layers).** The bottom layer is the framework or harness that runs the agent loop: LangGraph, the OpenAI Agents SDK, any other framework, or Omnigent as a meta-harness. That loop is wrapped by an agent server (`DurableAgentServer`, or a custom server via `agentbricks init --server custom`), which exposes `POST /api/invocations`, `GET /api/invocations/<id>`, and `GET /api/invocations/<id>/events?after=<id>`. The server runs on the **agent runtime**, which is managed compute on Databricks Apps. While a run is in progress, the server writes status, heartbeats, events, and the result to a **Runtime Store**. That store is in-process under `agentbricks dev` and persisted in Lakebase after `deploy`, and it is separate from the agent's own memory and session stores. Agents built on MLflow `AgentServer` or `LongRunningAgentServer`, or deployed to Model Serving, are now legacy.

**Request flow.** A client (app, user, or agent) calls the agent. The agent calls models, MCP servers, and skills through Unity Gateway, reads and writes history and memory, runs generated code in Databricks Sandbox, and records each step with MLflow Tracing. Those traces feed MLflow evaluation and production monitoring, which inform the next version. The documented lifecycle runs: scaffold, then write the loop, add context and tools, debug locally from traces, evaluate, deploy, and monitor and improve.

**Identity.** A deployed agent runs as its app's **service principal**. MCP services, sandboxes, Genie One, and Genie Agent tools run **on behalf of the requesting user** by default (`auth = "user"`), Unity Catalog functions always run as the service principal, and custom code can act as the user by declaring `[auth.user]` in `agent.toml` and calling `context.request_auth.client_for("user")`. User credentials are held in memory only for the active attempt, so request-user invocations cannot be crash-recovered. Memory `actor_id` partitions data but is **not** access control: set it from verified identity in trusted code, and use one store per tenant for strict isolation.

**Three agent surfaces.** Use **Agent Bricks** for a standalone production agent that other apps and services call over HTTP. Use the **AppKit `agents` plugin** (`@databricks/appkit/beta`) for lightweight agents that live inside one app: each agent is declared in `server/agents/<id>/agent.ts` with `createAgent`, backed by `DatabricksAdapter.fromModelServing` or `fromAiGateway`, and streamed with the `useAgentChat` React hook, which emits OpenAI Responses-API events. Use **Omnigent** while building with coding agents. Omnigent does not host the agents you build; those are deployed to the agent runtime.

## Main APIs

- **Python (AgentKit):** `DurableAgentServer`, `InvocationContext` (`invocation_id`, `session_id`, `attempt`, `is_recovery`, `emit`, `request_auth`), `AgentKitClient(WorkspaceClient())` with `.session_stores` and `.memory_stores` (`add`, `append_items`, `list_items`, `search`, `grant_permission`), and framework adapters `databricks_agentkit.langgraph` (`checkpointer`, `memory_tools`, `thread_config`) and `databricks_agentkit.openai` (`memory_tools`, `session_store`).
- **REST:** `/api/2.0/agents/session-stores`, `/api/2.0/agents/memory-stores`, and the agent invocation API above. Unity Gateway's OpenAI-compatible endpoint requires the `ai-gateway` user API scope.
- **CLIs:** `agentbricks` (`init`, `tools add`, `dev`, `deploy`, `deployments list|get|logs|stop|start|delete`, `memory bind`, `sessions bind`, `endpoint invoke`), `databricks serving-endpoints list|get|query|create`, `databricks aitools install|list|update|uninstall`, and `ug`.
- **TypeScript (AppKit):** `createAgent`, `DatabricksAdapter.fromModelServing` / `fromAiGateway`, `runAgent` for server-side calls, and `useAgentChat`.

## When to use

- You already keep governed enterprise data in a Databricks lakehouse and want production agents that read it under Unity Catalog permissions, with on-behalf-of-user tool calls.
- You want to keep your own agent framework (LangGraph, the OpenAI Agents SDK) but need managed durable hosting, crash recovery, session and memory stores, sandboxed code execution, and tracing and evaluation, without assembling those pieces yourself.
- You need centralized governance of LLM, MCP, and coding-agent traffic: one gateway with budgets, rate limits, usage tables, and BYOK providers. LiteLLM is a self-hosted alternative for this.
- It is probably not the right fit for small, standalone agent projects with no Databricks footprint. Several pieces are still Beta or experimental: Agent Bricks CLI, memory and sessions, Sandbox, and Omnigent.

## Ecosystem

- **Open-source foundations** (all Apache 2.0): Apache Spark (ASF), and Delta Lake, MLflow, and Unity Catalog OSS (LF AI & Data). Databricks contributes to Apache Iceberg but did not create it; it acquired Tabular, the company founded by Iceberg's creators, in 2024.
- **Acquisitions:** Neon, acquired in 2025, is the engine behind Lakebase.
- **Developer Hub templates:** AI chat app, RAG chat with Lakebase pgvector, Lakebase agent memory, Genie multi-agent selector, agentic support console, and "Onboard Your Coding Agent" (skills, Docs MCP, and an `AGENTS.md` bootstrap).
- **LLM manifests:** a routing `llms.txt` points to separate manifests for Docs (the product source of truth), the Developer Hub, Community, Answers, Neon, and `llms-full.txt`. It also includes explicit disambiguation notes aimed at AI systems.
- **Model catalog:** Databricks-hosted foundation models are prefixed `databricks-` (for example `databricks-claude-sonnet-4-6`). There are also `system.ai.*` model services and external models via provider services.
