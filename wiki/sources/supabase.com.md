---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://supabase.com/
companion_urls:
  - https://github.com/supabase/supabase
raw_files:
  - ../../raw/web/supabase.com.md
  - ../../raw/github/supabase-supabase.md
tags:
  - postgres-backend
  - pgvector
  - row-level-security
  - edge-functions
  - supabase-cli
  - firebase-alternative
  - agent-backend
  - mcp-integration
related:
  - firecrawl.dev
  - lovable.dev
  - bolt.new
  - must-have-clis-2026
  - trigger.dev
  - langchain.com
  - vercel.com
  - render.com
  - neon.com
product: supabase
detail_level: standard
created: 2026-07-07
updated: 2026-07-08
---

Supabase is the open-source Postgres development platform (105K+ GitHub stars) that packages a dedicated Postgres database, Auth, auto-generated REST/GraphQL APIs, Storage, Realtime, Edge Functions, and a pgvector-powered AI toolkit into one integrated backend — marketed as a Firebase alternative you can self-host or run locally via the Supabase CLI. It matters for this wiki because it is the default managed backend behind many agentic app builders ([[lovable.dev]], [[bolt.new]]) and a common persistence layer for RAG pipelines, agent memory, and vector search — with first-class AI-tooling docs (MCP, skills, plugins) and case studies like [[firecrawl.dev]] migrating from Pinecone to Supabase Vector.

_All claims below are sourced from ../../raw/web/supabase.com.md unless otherwise noted._

## What it does

Supabase gives every project a full, portable Postgres instance plus a suite of integrated services: user authentication (20+ social providers, email/password, OTP, magic links, SSO), S3-compatible file storage with CDN, WebSocket-based Realtime (database changes, presence, broadcast), globally distributed Edge Functions (TypeScript/Deno), and pgvector-based vector search. From your schema it auto-generates REST APIs (PostgREST) and GraphQL (pg_graphql) with no backend code required. The platform is available hosted (16+ regions, SOC2 Type 2) or self-hosted / local via Docker and the CLI.

## Key features

- **Dedicated Postgres** per project with Table Editor, SQL Editor, 40+ extensions (pgvector, PostGIS, pg_cron), Database Branching, Read Replicas, and Database Webhooks
- **Auth + RLS** — JWT-based sessions with authorization policies written in SQL at the database level, not application middleware
- **AI & Vectors** — semantic, keyword, and hybrid search over pgvector; integrations with OpenAI, Hugging Face, LangChain, LlamaIndex; embedding generation in Edge Functions
- **Edge Functions** — Deno/TypeScript serverless at the edge for webhooks, LLM orchestration, image generation, and third-party integrations
- **Supabase CLI** — `supabase start` spins up the full local stack; `supabase db push` applies version-controlled migrations to production (../../raw/github/supabase-supabase.md)
- **AI developer tooling** — docs for building with AI tools, MCP server integration, and agent-oriented workflows
- **Client SDKs** — official libraries for JavaScript/TypeScript, Python, Flutter, Swift, Kotlin, plus community ports (../../raw/github/supabase-supabase.md)

## Architecture

Supabase composes proven open-source components behind a Kong API gateway: Postgres as the core datastore, PostgREST for REST, GoTrue for JWT auth, Realtime (Elixir) for WebSocket change feeds, Storage API for S3-backed files, pg_graphql for GraphQL, and postgres-meta for database management. Client libraries are modular — each feature (PostgREST, GoTrue, Realtime, Storage, Functions) has standalone implementations per language, bundled into the main Supabase client. (../../raw/github/supabase-supabase.md) The hosted platform adds dashboard UI, branching, observability, and managed infrastructure; the same stack runs locally via Docker for dev/CI parity.

## Installation

```bash
# CLI (macOS)
brew install supabase/tap/supabase

# Local project setup
supabase init
supabase start   # full stack at http://localhost:54323
```

For hosted projects, sign up at supabase.com/dashboard and connect via `@supabase/supabase-js` with project URL and anon key. (../../raw/github/supabase-supabase.md)

## Example usage

```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_ANON_KEY
)

// Query with RLS-scoped auth token automatically attached
const { data } = await supabase.from('todos').select('*')
```

Edge Function webhook handler pattern: deploy a TypeScript handler via `supabase functions deploy`, validate JWT at the gateway, call Postgres or external APIs (Stripe, OpenAI), return JSON — with local parity via `supabase functions serve`. (../../raw/github/supabase-supabase.md)

## When to use

Reach for Supabase when you need a batteries-included Postgres backend for web, mobile, or AI apps — especially if you want Auth, Storage, Realtime, and vector search in one platform without stitching together separate services. It fits agentic workflows as: (1) a **persistence + RAG layer** (pgvector tables alongside transactional data, hybrid search), (2) a **local-first dev backend** via CLI for agent-built apps ([[must-have-clis-2026]]), (3) the **managed runtime** behind vibe-coding builders ([[lovable.dev]], [[bolt.new]]), and (4) an **Edge Functions target** for webhooks, scheduled jobs (pg_cron), and lightweight LLM orchestration. Prefer a dedicated vector DB only when you need specialized scale/features beyond pgvector; prefer a serverless-Postgres-only provider if you only need the database without the full platform.

## Maintenance status

Actively maintained; Apache 2.0 licensed monorepo, primary language TypeScript. (../../raw/github/supabase-supabase.md)
- Stars: 105,839; forks: 13,010 (../../raw/github/supabase-supabase.md)
- Latest release: v1.26.05 (2026-05-07) (../../raw/github/supabase-supabase.md)
- Last push: 2026-07-07
- SOC2 Type 2, HIPAA, ISO 27001 certified (hosted platform)

## Ecosystem

- **MCP server** — Supabase MCP lets AI agents inspect schema, write migrations, and manage projects from Claude Code/Cursor (documented under AI Tools in docs)
- **LangChain / LlamaIndex** — first-class vector-store integrations for RAG pipelines; overlaps conceptually with [[langchain.com]] vector tooling but keeps vectors in Postgres
- **Builder integrations** — [[lovable.dev]] Lovable Cloud, [[bolt.new]] database option, [[trigger.dev]] task integrations
- **CLI in agent stacks** — profiled in [[must-have-clis-2026]] as the standard for local Postgres + Auth + Storage development
- **Vector migration target** — [[firecrawl.dev]] case study cites switching from Pinecone to Supabase Vector for simpler ops and comparable performance
- **Self-hosting** — full Docker-based self-host path; local dev uses the same open-source components as production

## Documentation

Docs at `supabase.com/docs` with `llms.txt`, `llms-full.txt`, and per-SDK reference catalogs (`llms/js.txt`, `llms/python.txt`, `llms/cli.txt`, etc.). Top-level guides: Getting Started, Auth, Database, Storage, Realtime, Edge Functions, AI & Vectors, Local Development & CLI, Self-Hosting, Deployment & Branching, Security, Cron, Queues, Integrations, AI Tools.
