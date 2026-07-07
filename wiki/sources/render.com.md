---
type: source
source_url: https://render.com/
tags:
  - cloud-platform
  - paas
  - deployment
  - workflows
  - mcp
  - agent-hosting
  - postgres
  - infrastructure-as-code
related:
  - vercel.com
  - trigger.dev
  - supabase.com
  - skills.sh
  - firecrawl.dev
  - litellm.ai
  - pydantic.dev
  - streamlit.io
product: render
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

Render is a unified cloud platform ("the cloud for builders") for deploying and scaling web apps, APIs, data pipelines, and AI agents with minimal ops. Connect a Git repo, pick a service type, and Render handles builds, networking, TLS, scaling, previews, rollbacks, and observability. For agentic workloads it adds **Render Workflows** (durable task orchestration as code), first-class **coding-agent integrations** (official Agent Skills, hosted MCP server, Jules PR auto-fix), and managed **Postgres** and **Key Value** datastores on a private network — positioning as a full-stack Heroku/Railway alternative that explicitly markets agent deployment alongside traditional PaaS use cases.

_All claims below are sourced from ../../raw/web/render.com.md unless otherwise noted._

## What it does

Render hosts your code as one or more **services** in containerized instances across regions (Oregon, Ohio, Virginia, Frankfurt, Singapore). The core workflow is: select a service type → connect GitHub/GitLab/Bitbucket (or Docker image) → Render builds and deploys on every push.

Service types cover the full application stack:

- **Web services** — dynamic apps and API servers at a public `onrender.com` URL (Express, Django, FastAPI, Rails, etc.)
- **Static sites** — frontends over a global CDN (React, Next.js static export, Hugo, etc.)
- **Private services** — internal-only apps reachable over Render's private network
- **Background workers** — continuous queue consumers (Celery, Sidekiq)
- **Cron jobs** — scheduled scripts that run and exit
- **Workflows** — long-running, composable tasks for agents, ETL, and on-demand background jobs (public beta)
- **Render Postgres** — managed PostgreSQL with PITR, read replicas, HA, connection pooling
- **Render Key Value** — Redis-compatible in-memory store (Valkey on new instances) for caches and job queues

The platform emphasizes zero-ops production paths: autoscaling, preview environments for every PR, zero-downtime deploys, Blueprints (IaC via `render.yaml`), Terraform provider, integrated logs/metrics, and compliance certifications (SOC 2 Type 2, HIPAA, ISO 27001, GDPR).

## Key features

**Deployment and runtime**

- Git-connected auto-deploys with instant rollback and maintenance mode
- Native language runtimes plus Docker deploys (Dockerfile or prebuilt images)
- Load-based autoscaling for traffic bursts
- Full-stack **preview environments** — disposable copies of entire Blueprint-defined stacks per PR (Pro+)
- **Service previews** — standalone preview instances for individual services
- Persistent disks, WebSockets, edge caching, managed TLS (including wildcards)
- Private networking between services in the same region without VPC setup

**Render Workflows (agent/background orchestration)**

- Define tasks as TypeScript or Python functions with `@renderinc/sdk/workflows` or `render_sdk`
- Managed queuing, on-demand instance spin-up, automatic retries, runs up to 24 hours
- Task chaining for agent patterns (gather context → execute skills → compose response)
- Trigger from web apps, agents, CI/CD, CLI, API, or Dashboard
- Alternative to DIY Celery/BullMQ + worker fleet — Render unifies submission, queue, and provisioning

**Agent and coding-tool integrations**

- **Render MCP Server** at `https://mcp.render.com/mcp` — create services, query Postgres, pull logs/metrics from Cursor, Codex, Claude Code, Jules, Windsurf
- **Official Agent Skills** (`render-deploy`, `render-debug`, `render-monitor`) installable via `render skills install` or from `render-oss/skills`
- **Jules integration** — auto-analyzes failed PR preview builds and pushes fixes
- **LLM-friendly docs** — `.md` suffix URLs, `llms.txt` / `llms-full.txt`, `Accept: text/markdown`, experimental docs MCP at `mcp.inkeep.com/render/mcp`
- Dedicated docs page: "Using Render with Coding Agents"

**Security and compliance**

- Built-in DDoS protection, encryption at rest, audit logs, RBAC
- HIPAA on Render for regulated workloads
- Isolated environments prevent non-prod from reaching production services

## Architecture and concepts

Render's mental model is **services + datastores on a private network**, orchestrated via Dashboard, CLI, REST API, Blueprints, or MCP:

1. **Compute layer** — instance types set RAM/CPU per service; web services bind to `PORT` (default 10000) on `0.0.0.0`; workflows spin ephemeral instances per task run
2. **Data layer** — Postgres for relational/vector workloads; Key Value for queues and caches; optional persistent disks on web/private/worker services
3. **Networking** — public URLs for web/static; private hostnames for internal traffic; custom domains; outbound IP controls
4. **IaC** — `render.yaml` Blueprints define multi-service architectures; preview environments clone the Blueprint stack per PR
5. **Observability** — dashboard logs/metrics; webhooks; streaming to external OTel/logging providers

For multi-service apps, Render documents explicit architecture patterns (web + worker + Postgres + Key Value) with private-network communication — no Kubernetes required.

## Main APIs

**REST API** — programmatic management of services, deploys, databases, and metrics (`api-docs.render.com`).

**Render CLI** — `render` commands for deploys, logs, scaling, skills install, workflow triggers.

**Workflows SDK**

- TypeScript: `@renderinc/sdk` — `render.workflows.startTask('my-workflow/taskName', [args])`
- Python: `render_sdk` — sync and async task triggers
- REST: `POST https://api.render.com/v1/task-runs` with Bearer API key

**MCP** — hosted server at `https://mcp.render.com/mcp` with tools for workspace selection, service CRUD (limited types), deploy history, log/metric queries, read-only SQL on Postgres.

**Blueprints** — declarative `render.yaml` for services, databases, env groups, preview config (`previews.generation`, `previewPlan`, `previewValue`, `initialDeployHook`).

## When to use

Render fits when you want a **unified PaaS** for full-stack apps and agent backends without managing Kubernetes or stitching together separate hosting, database, queue, and preview-infrastructure vendors. Strong cases:

- Deploying **AI agents and workflows** with managed orchestration (Render Workflows) instead of self-managed Celery/Redis workers
- **Full-stack preview environments** that mirror production Blueprint architecture on every PR
- Teams migrating from **Heroku or Railway** with comparable DX and explicit migration guides
- **HIPAA-compliant** agent or healthcare apps needing managed compliance primitives
- **Coding-agent-driven deploys** via MCP, official skills, or Jules auto-fix on preview failures

Compare [[vercel.com]] when edge/serverless and AI SDK/Gateway/Sandbox are the primary needs; [[trigger.dev]] for framework-native durable background jobs outside a full PaaS; [[supabase.com]] when Postgres+Auth+Realtime as a backend platform is the core requirement rather than general compute hosting.

## Ecosystem

- **100+ quickstart templates** — FastAPI, Django, Next.js, n8n, OpenClaw, LangChain+MongoDB chatbot, Open WebUI, Temporal, and more
- **Migration paths** — Heroku, Railway, Replit guides; migration credits program
- **Comparisons** — explicit docs vs Heroku, Vercel, Railway, Fly.io
- **Open-source agent tooling** — `render-oss/render-mcp-server`, `render-oss/skills`, example repos under `render-examples/`
- **Third-party integrations** — Datadog, OIDC for AWS, Formspree, QuotaGuard static IPs
- Articles cover agent hosting, LangChain deployment, MCP server guides, durable workflow platforms, and multi-agent deployment without AWS complexity
