---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/every-app/open-seo
tags:
  - seo
  - open-seo
  - mcp-server
  - agent-skills
  - dataforseo
  - self-hosted
  - rank-tracking
  - keyword-research
related:
  - AgriciDaniel-jev-seo
  - firecrawl.dev
  - tavily.com
product: open-seo
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

every-app/open-seo (OpenSEO) is an open-source, pay-as-you-go alternative to Semrush/Ahrefs aimed at humans and AI agents: keyword research, rank tracking, competitor insights, backlinks, site audits, and AI visibility, with a first-class MCP server and Agent Skills so tools like Claude Code, Codex, OpenClaw, and Hermes can drive SEO workflows directly.

_All claims below are sourced from ../../raw/github/every-app-open-seo.md unless otherwise noted._

## What it does

OpenSEO packages focused SEO workflows (not a bloated suite) behind a modern UI and agent surfaces. Data comes from a bring-your-own [DataForSEO](https://dataforseo.com/) API key—self-hosters pay DataForSEO directly; the hosted service at [openseo.so](https://openseo.so) adds ~28% on top of those requests. Hosted use starts free with an optional $10/month subscription; self-host paths include Docker (Compose-friendly) and a one-command Cloudflare deploy (free Cloudflare plan). Advanced setups support Cloudflare Access or Docker without app sign-in behind Tailscale/private network. Accounts are email/password: first visitor becomes admin; MCP clients reuse the same accounts.

## Installation

**Hosted:** use [openseo.so](https://openseo.so).

**Self-host Docker** — see `docs/SELF_HOSTING_DOCKER.md` (prebuilt image; Coolify/Portainer/Dokploy compatible).

**Self-host Cloudflare** — see `docs/SELF_HOSTING_CLOUDFLARE.md`.

**Agent Skills** (example contrib skill):

```sh
npx skills add every-app/open-seo --skill simple-issue-description
```

MCP and skills setup docs are linked from the README (`openseo.so/docs/mcp`, `openseo.so/docs/skills/setup`, plus ChatGPT and Codex guides).

## Key features

- Main workflows: keyword research, rank tracking, competitor insights, backlinks, site audits, AI visibility.
- MCP server for agents (Claude Code, OpenClaw, Hermes, ChatGPT, Codex, Cursor).
- Pre-built Agent Skills plus ability to author custom skills on the MCP.
- No mandatory SaaS subscription when self-hosting—BYO DataForSEO key.
- Plugin packaging under `.claude-plugin/`, `.cursor-plugin/`, and `plugins/openseo`.

## Architecture

TypeScript monorepo (`pnpm` workspace) with `src/`, `web/`, Drizzle migrations, Vite configs (including MCP widgets and Cloudflare/worker bundles), `compose.yaml` for Docker, and Wrangler configs for Cloudflare. Agent/plugin manifests live in `.agents/`, `.claude/`, `.claude-plugin/`, `.cursor-plugin/`, and `plugins/`. Docs cover DataForSEO keys, Google Maps/Analytics/Search Console hooks, and local Postgres development.

## Example usage

```sh
# Install a documented Agent Skill from the repo
npx skills add every-app/open-seo --skill simple-issue-description

# Then point an MCP-capable agent at your OpenSEO instance
# (see openseo.so/docs/mcp for client-specific config)
```

## Maintenance status

25,694 stars, 3,511 forks, TypeScript, default branch `main`, latest release v0.1.21 (2026-10-30), MIT license, homepage https://openseo.so, pushed 2026-10-30.

## Ecosystem

Positions itself against Semrush/Ahrefs with agent-native MCP/skills. Adjacent SEO-for-agents work in this wiki includes [[AgriciDaniel-jev-seo]]; web-data layers such as [[firecrawl.dev]] and [[tavily.com]] solve different retrieval problems but often sit in the same agent stack.
