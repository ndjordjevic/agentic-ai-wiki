---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/supabase/agent-skills
tags:
  - supabase
  - agent-skills
  - postgres-best-practices
  - skills-cli
  - claude-code-plugin
  - well-known-discovery
  - rls
related:
  - supabase.com
  - supabase-cli
  - addyosmani-agent-skills
  - stripe-best-practices
product: supabase-agent-skills
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

supabase/agent-skills is Supabase's official Agent Skills pack for developers using AI agents with Supabase. It ships two skills—comprehensive Supabase product coverage and Postgres performance best practices—in the [Agent Skills](https://agentskills.io/) format, compatible with 18+ agents including Claude Code, GitHub Copilot, Cursor, and Cline.

_All claims below are sourced from ../../raw/github/supabase-agent-skills.md unless otherwise noted._

## What it does

Once installed, skills activate when relevant tasks are detected. The `supabase` skill covers Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues; client libraries and SSR (`supabase-js`, `@supabase/ssr`) in Next.js, React, SvelteKit, Astro, Remix; auth troubleshooting (sessions, JWT, cookies, `getSession`/`getUser`/`getClaims`, RLS); Supabase CLI and MCP; schema/migrations, security audits, and Postgres extensions (`pg_graphql`, `pg_cron`, `pg_vector`). The `supabase-postgres-best-practices` skill supplies impact-prioritized guidelines across eight categories (query performance, connection management, schema design, concurrency & locking, security & RLS, data access patterns, monitoring & diagnostics, advanced features) for SQL, indexes, pooling/scaling, and RLS reviews.

## Installation

Detailed install docs: [Supabase AI Skills](https://supabase.com/docs/guides/getting-started/ai-skills).

**All skills:**

```bash
npx skills add supabase/agent-skills
```

**Single skill:**

```bash
npx skills add supabase/agent-skills --skill supabase
npx skills add supabase/agent-skills --skill supabase-postgres-best-practices
```

**Claude Code plugins:**

```bash
claude plugin marketplace add supabase/agent-skills
claude plugin install supabase@supabase-agent-skills
claude plugin install postgres-best-practices@supabase-agent-skills
```

## Key features

- **`supabase`** — full-product Supabase development skill (DB, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues, clients/SSR, CLI/MCP, migrations, RLS, extensions).
- **`supabase-postgres-best-practices`** — Postgres optimization references in eight impact-ranked categories; critical focus on query performance, connection management, and security/RLS.
- **Agent Skills Open Standard** — each skill is a folder with required `SKILL.md` (frontmatter: name, description, metadata) and optional `references/` for deeper docs.
- **`.well-known` discovery** — each release uploads `dist/index.json` (schema v0.2.0) with skill tarballs; consumed by supabase.com at `https://supabase.com/.well-known/agent-skills/`. Built by `scripts/build-release.ts` via Release Please on every semver release; planned drop-in swap to `agentskills/build-for-well-known` GitHub Action when published to Marketplace.

## Architecture

Skills live under `skills/supabase` and `skills/supabase-postgres-best-practices`. Packaging/release: TypeScript primary language, pnpm, `release-please-config.json`, `.release-please-manifest.json`, `scripts/build-release.ts`, Vitest (`test/`, `vitest.config.ts`). Claude marketplace metadata in `.claude-plugin/marketplace.json`; also `.mcp.json`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`. Homepage/docs: https://supabase.com/docs/guides/getting-started/ai-skills.

## Example usage

After install, natural-language prompts that should route into the skills:

```text
Optimize this Postgres query
Review my schema for performance issues
Help me set up Supabase Auth with Next.js
Help me add proper indexes to this table
```

```bash
npx skills add supabase/agent-skills
npx skills add supabase/agent-skills --skill supabase-postgres-best-practices
```

## Maintenance status

2,957 stars, 257 forks, TypeScript primary language, default branch `main`, last pushed 2026-10-02. Latest release v0.1.9 (2026-09-28). MIT License. Semver releases driven by Release Please with `.well-known` artifact upload.

## When to use

Use when agents implement or debug Supabase apps (Auth/SSR/RLS, migrations, CLI/MCP) or need vendor Postgres performance guidance ranked by impact. Prefer the `supabase` skill for product-wide work and `supabase-postgres-best-practices` for SQL/schema/index/RLS/pooling reviews. Pair with [[supabase-cli]] and platform docs on [[supabase.com]] rather than treating skills as a substitute for those tools.

## Ecosystem

Official Supabase surface alongside [[supabase.com]] (docs/platform, including AI skills guide and `.well-known` hosting) and [[supabase-cli]]. Methodologically related to broader skill packs such as [[addyosmani-agent-skills]], but scoped to Supabase + Postgres rather than full-SDLC engineering. Install via skills CLI or Claude Code marketplace plugins; discovery also via supabase.com `.well-known/agent-skills/`.
