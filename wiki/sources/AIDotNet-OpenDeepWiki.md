---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/AIDotNet/OpenDeepWiki
tags:
  - self-hosted
  - deepwiki-clone
  - mcp-server
  - graphrag
  - docker
  - dotnet
related:
  - deepwiki.com
  - AsyncFuncAI-deepwiki-open
  - PorunC-CodeWiki
  - langchain-ai-openwiki
product: opendeepwiki
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`AIDotNet/OpenDeepWiki` (~3.4k stars, MIT) is a full-stack, self-hosted platform that mirrors [[deepwiki.com]]'s product shape: import repos (Git URL, ZIP, or **local directory**), auto-generate structured wikis with mind maps and optional Graphify artifacts, publish SEO-friendly public doc routes, and expose the same knowledge via built-in chat, embed APIs, and **repository-scoped MCP endpoints**. Built on ASP.NET Core (.NET 10) + Next.js 16 with SQLite/PostgreSQL — heavier than [[he-yufeng-RepoWiki]] but closest to a complete private DeepWiki replacement with admin console, multi-user RBAC, and incremental background workers.

_All claims below are sourced from ../../raw/github/AIDotNet-OpenDeepWiki.md unless otherwise noted._

## What it does

OpenDeepWiki ingests codebases, runs AI-orchestrated documentation pipelines (catalog planning, page generation, optional translation), and serves results at routes like `/{owner}/{repo}`, `/{owner}/{repo}/mindmap`, and `/{owner}/{repo}/graphify`. Admins configure LLM providers, API keys, GitHub App imports, skills, and MCP providers from a web console. Chat integrations support Feishu, QQ, WeChat, and Slack webhooks.

## Installation

```bash
git clone https://github.com/AIDotNet/OpenDeepWiki.git
cd OpenDeepWiki
# edit compose.yaml: JWT_SECRET_KEY, CHAT_API_KEY, WIKI_CATALOG_*, WIKI_CONTENT_*
docker compose up -d --build
# Web UI: http://localhost:3000  |  API health: http://localhost:8080/health
```

## Key features

- **Multiple ingest sources** — Git URLs, ZIP uploads, approved local directories.
- **Rich artifact types** — README summaries, wiki catalogs, multi-language translations, Mermaid mind maps, Graphify visualizations.
- **MCP + chat + embed** — repository-scoped MCP endpoints reuse the same index as the public site and admin chat assistant.
- **Enterprise admin** — users, roles, departments, API keys, scheduled incremental updates, background workers.
- **Flexible DB** — SQLite default; PostgreSQL supported for production.

## Architecture

| Layer | Stack |
| --- | --- |
| Backend | ASP.NET Core, MiniApis, `Microsoft.Agents.AI`, LibGit2Sharp repo processing |
| Frontend | Next.js 16, React 19 App Router |
| Database | SQLite or PostgreSQL via EF Core providers |
| Deploy | Docker Compose, Makefile, optional Sealos |

Prompt assets live under `src/OpenDeepWiki/prompts`; workers handle translation, mind maps, Graphify, and incremental sync.

## Example usage

After Docker startup, log into admin (`admin@routin.ai` on fresh DB per README), add a repository source, trigger wiki generation, then browse public routes or connect an MCP client to the repo-scoped endpoint documented in the project docs.

## Maintenance status

3,382 stars, 432 forks, MIT, C# + TypeScript, v2.0.3 release, very active (pushed 2026-07-03). Hosted demo at opendeep.wiki. Strongest choice when you need **private self-hosted DeepWiki + MCP + multi-user admin** in one box; more operational surface than [[AsyncFuncAI-deepwiki-open]] or [[he-yufeng-RepoWiki]].
