---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://neon.com/
companion_urls:
  - https://github.com/neondatabase/neon
raw_files:
  - ../../raw/web/neon.com.md
  - ../../raw/github/neondatabase-neon.md
tags:
  - serverless-postgres
  - database-branching
  - autoscaling
  - scale-to-zero
  - agent-backend
  - mcp-integration
  - neon-auth
  - pgvector
related:
  - supabase.com
  - render.com
  - vercel.com
  - langchain.com
  - trigger.dev
product: neon
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Neon is a serverless Postgres backend platform (22.5K+ GitHub stars, Apache 2.0, Databricks-owned since May 2025) designed explicitly for apps and agents — separating compute and storage to deliver autoscaling, git-like database branching, scale-to-zero, instant point-in-time restore, and fleet APIs that spin up databases in ~120ms. Beyond core Postgres it bundles managed Neon Auth (Better Auth, users in `neon_auth` schema), Data API (Supabase-compatible REST), early-access Functions, Object Storage, and AI Gateway — all agent-ready via `npx neon@latest init`, MCP server (`mcp.neon.tech`), Agent Skills, and editor plugins for Cursor, Claude Code, Codex, and GitHub Copilot. It competes as the agent-native Postgres layer behind codegen platforms — compare integrated backends [[supabase.com]], PaaS hosts [[render.com]]/[[vercel.com]], and AI framework persistence patterns [[langchain.com]].

_All claims below are sourced from ../../raw/web/neon.com.md unless otherwise noted._

## What it does

Neon provides serverless PostgreSQL with a lakebase architecture: ephemeral compute nodes run standard Postgres while a durable storage layer (safekeepers for WAL quorum, pageserver for page materialization, object storage for immutable history) handles correctness and branching. The platform targets both traditional app backends and agent/codegen platforms that need thousands of per-user or per-preview databases that pause when idle. One-command setup (`npx neon@latest init`) connects AI assistants via MCP and installs agent skills; the Neon API (`console.neon.tech/api/v2/`) provisions projects, branches, databases, and endpoints programmatically.

## Key features

- **Serverless Postgres** — autoscaling compute (0.25–8 CU range), scale-to-zero after 5 minutes idle, instant restore within configurable history window (6h free / up to 30 days on Scale)
- **Copy-on-write branching** — git-like database branches for dev, CI/CD, preview environments, and agent database versioning/checkpoints; schema-only and TTL branches supported
- **Neon Auth** — managed Better Auth (v1.4.18) with users/sessions in Postgres, OAuth, magic links, RLS-compatible; auth state branches with data (up to 60K MAU free)
- **Data API** — PostgREST-style HTTPS REST interface, Supabase drop-in compatible
- **AI & agent tooling** — MCP server with project/branch/schema/query/auth tools; Agent Skills; Cursor/Claude Code/Codex/Copilot plugins; pgvector and LangChain/LlamaIndex guides
- **Fleet APIs** — programmatic database creation in milliseconds for agent platforms deploying per-user databases (../../raw/github/neondatabase-neon.md)
- **Enterprise features without platform fees** — HIPAA, SOC2, PrivateLink, OTel metrics export, 99.95% SLA on Scale

## Architecture

Neon's lakebase design splits OLTP into compute (stateless Postgres on RAM/NVMe) and storage (safekeepers → pageserver → object storage). WAL quorum via Paxos defines commit correctness; pages are reconstructed on demand, never read from object storage on the hot query path. This enables copy-on-write branching, instant restores, and scale-to-zero as metadata operations rather than data copies. The open-source implementation (`neondatabase/neon`, Rust) comprises compute nodes, pageserver, safekeeper, proxy, and a local control plane (`cargo neon`). (../../raw/github/neondatabase-neon.md)

## Installation

```bash
# AI-guided project setup (MCP + skills + API key)
npx neon@latest init

# CLI install
npm i -g neonctl
neonctl auth

# Local development from source
git clone --recursive https://github.com/neondatabase/neon.git
cd neon && make -j$(nproc) -s
cargo neon init && cargo neon start
```

(../../raw/github/neondatabase-neon.md)

## Example usage

```bash
# Create a branch via API
export NEON_API_KEY="your-api-key"
curl -X POST "https://console.neon.tech/api/v2/projects/$PROJECT_ID/branches" \
  -H "Authorization: Bearer $NEON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"branch": {"name": "dev-branch"}}'

# MCP quick setup
npx neon@latest init
# Then in your AI editor: "Get started with Neon"
```

Provision databases for agent fleets via `POST https://api.neon.tech/v2/projects/:id/database` (connection string in ~120ms per marketing claims).

## When to use

Choose Neon when you need serverless Postgres with branching for preview/CI workflows, per-tenant or per-agent database fleets that scale to zero, or tight AI-editor integration (MCP + skills) for schema management without leaving your IDE. Strong fit for codegen platforms deploying user-generated app backends. Less ideal if you need a full Firebase-style suite (realtime, storage, edge functions in one OSS stack) — [[supabase.com]] covers more surface area; or if you want self-hosted everything without a managed control plane.

## Maintenance status

Open-source core actively maintained (22,501 stars, Rust, Apache 2.0, default branch `main`, latest release `release-proxy-8853`). Acquired by Databricks (May 2025); marketing positions Neon as "Postgres backends for apps and agents" within the Databricks ecosystem. Hosted service at neon.com with Free/Launch/Scale plans and no platform fees. (../../raw/github/neondatabase-neon.md)

## Ecosystem

Integrates with 30+ frameworks (Next.js, Drizzle, Prisma, Django, etc.), Vercel (managed integration with per-preview branches), GitHub Actions for branching CI, LangChain/LlamaIndex/Semantic Kernel for RAG, Inngest for agentic workflows, and Datadog/OTel for observability. Early-access services (Functions, Storage, AI Gateway) extend the platform beyond Postgres. Docs available as markdown (`*.md` URLs) and `llms.txt` for agent consumption.

## Documentation

Comprehensive docs at neon.com/docs with sections for Introduction, Connect, CLI, AI & Agents, Auth, Functions, Storage, AI Gateway, Data API, Branching, Manage, Guides, Import, Workflows, Reference, PostgreSQL, Security, and Extensions. Agent-focused entry points: `with-an-agent.md`, `neon-mcp-server.md`, `agent-skills.md`, and per-editor plugin guides.
