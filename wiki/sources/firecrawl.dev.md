---
type: source
source_url: https://www.firecrawl.dev/
companion_urls:
  - https://github.com/firecrawl/firecrawl
raw_files:
  - ../../raw/web/firecrawl.dev.md
  - ../../raw/github/firecrawl-firecrawl.md
tags:
  - web-scraping
  - llm-ready-markdown
  - crawl-api
  - mcp-integration
  - agent-skills
  - structured-extraction
  - browser-rendering
related:
  - browserbase.com
  - browser-use.com
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - supabase.com
  - render.com
  - crafterq.ai
product: firecrawl.dev
detail_level: standard
created: 2026-07-06
updated: 2026-07-08
---

Firecrawl is a web data API platform (145K+ GitHub stars, one of the largest open-source repos on GitHub) that turns the live web into clean, LLM-ready data through one API family: Search, Scrape, Crawl, Map, Parse, and Interact. It targets the same "AI needs reliable web access" problem as [[browserbase.com]] and [[browser-use.com]], but positions itself specifically as a **data** API rather than a full browser-automation platform — the core promise is markdown/JSON output with minimal token overhead, not driving a persistent interactive session.

_All claims below are sourced from ../../raw/web/firecrawl.dev.md unless otherwise noted._

## What it does

Firecrawl exposes six endpoints under one API key: **Search** (live web queries that return full page content, not just links/snippets), **Scrape** (a single URL to clean Markdown/HTML/JSON/screenshot), **Crawl** (depth-first traversal of a site with depth/limit/path controls, respecting `robots.txt` for the `FirecrawlAgent` directive), **Map** (fast site-structure discovery), **Parse** (document extraction from PDFs, DOCX, and other file types), and **Interact** (a managed real browser for multi-step flows — login, click, fill — behind auth walls or pagination). The workflow is framed as Find → Extract → Clean → Use: Search/Map find pages, Scrape/Crawl/Parse extract and clean content, and Interact is reserved for cases a plain scrape can't reach.

## Key features

- JavaScript rendering with "smart wait" — automatically waits for dynamic content to finish loading before extracting, covering 96% of the web including JS-heavy pages
- Both a cached web index (fast) and live scrape/crawl (fresh) depending on the query
- Structured data extraction via JSON schemas, in addition to Markdown/HTML/screenshot output formats
- Token-efficient output: strips navs, footers, and ads, claiming ~93% fewer input tokens per page vs. a raw fetch (example cited: 38,381 tokens raw vs. much less cleaned for a blog page)
- New `/monitor` capability — an always-on search that pings an agent the moment new matching content appears on the web
- Official SDKs for Python, Node.js, Go, Rust, Java, and Elixir, plus a CLI (`firecrawl-cli`) (../../raw/github/firecrawl-firecrawl.md)
- Official MCP server for Claude, Cursor, Windsurf, and other MCP clients; agent Skills packages for Claude Code and Codex that automate setup (400,000+ MCP server installs reported)

## Architecture and concepts

The monorepo (`firecrawl/firecrawl`) is organized as `apps/api` (the core service) plus one directory per SDK (`python-sdk`, `js-sdk`, `go-sdk`, `java-sdk`, `rust-sdk`, `php-sdk`, `dot-net-sdk`, `elixir-sdk`, `ruby-sdk`), supporting services (`playwright-service-ts` for rendering, `go-html-to-md-service` for markdown conversion, `nuq-postgres`, `redis`), and agent-facing packages (`firecrawl-cli`, `firecrawl-cli-skills`, `firecrawl-skills`, `firecrawl-workflows`). (../../raw/github/firecrawl-firecrawl.md) The hosted product runs on "Fire-engine," Firecrawl's proprietary infrastructure for proxy rotation, rendering, and reliability, which the open-source repo does not fully replicate — `SELF_HOST.md` documents the self-hosted path via `docker-compose.yaml` for teams that want to run the OSS core themselves. (../../raw/github/firecrawl-firecrawl.md) Credits are the shared billing unit across endpoints: Scrape/Crawl/Map/Monitor cost 1 credit/page, Search costs 2 credits per 10 results, and Interact costs 2 credits per browser-minute — one credit is not uniformly "one page."

## Main APIs

- `POST /scrape` — single URL → Markdown/HTML/JSON/screenshot
- `POST /crawl`, plus `GET /crawl/{id}` (status), `GET /crawl/{id}/errors`, `DELETE /crawl/{id}` (cancel), `GET /crawl/active` — asynchronous site crawl lifecycle (../../raw/github/firecrawl-firecrawl.md)
- `POST /map` — fast link/structure discovery for a domain
- Search endpoint — full-page-content search results, not link-only
- Interact/browser session endpoints — `browser-create`, `browser-execute` (Playwright or agent-browser code in-session), `browser-list`, `browser-delete` for standalone driven sessions (../../raw/github/firecrawl-firecrawl.md)
- `GET /activity`, `GET /credit-usage`, `GET /credit-usage-historical` — account/usage introspection endpoints (../../raw/github/firecrawl-firecrawl.md)

## When to use

Reach for Firecrawl when an agent or pipeline needs **clean, structured web content** at scale — RAG ingestion, deep-research agents, lead enrichment, competitive intelligence, content generation, or price monitoring — and the target pages are mostly readable via scrape/crawl rather than requiring sustained interactive browser control. Prefer [[browserbase.com]] or [[browser-use.com]] instead when the task is fundamentally an interactive session (multi-step logins, CAPTCHA-heavy flows, long-lived stateful automation) rather than "fetch and clean this content"; Firecrawl's Interact endpoint covers occasional interaction needs but is explicitly not designed for long-running persistent sessions. The free tier (1,000 credits/month) is enough for light use; Hobby/Standard/Growth/Scale plans scale up rate limits and credit allotments for production pipelines.

## Maintenance status

Actively maintained; AGPL-3.0 licensed, primary language TypeScript. (../../raw/github/firecrawl-firecrawl.md)
- Stars: 145,284; forks: 8,362 (../../raw/github/firecrawl-firecrawl.md)
- Latest release: v2.11.0 (2026-06-19) (../../raw/github/firecrawl-firecrawl.md)
- Reports 1.25M+ developers, 150,000+ companies, 5B+ requests served; SDKs see 2.5M+ weekly npm/PyPI downloads
- Notable users cited: Shopify, Canva, Apple, DoorDash, Lovable

## Ecosystem

- **MCP Server** connects Firecrawl to Claude, Cursor, Windsurf, and other MCP-compatible clients for search/scrape/interact from within an agent session — comparable in role to [[microsoft-playwright-mcp]] but backed by Firecrawl's scrape/crawl infrastructure instead of raw Playwright control
- **agent-onboarding SKILL.md** (`firecrawl.dev/agent-onboarding/SKILL.md`) lets an AI agent fetch setup instructions and mint an API key directly, following the same "agent onboards itself via a fetchable skill file" pattern seen elsewhere in this wiki (e.g. [[vercel-labs-agent-browser]])
- `examples/` in the monorepo is a large collection of community/official example apps (research agents, crawlers, extractors, RAG pipelines) built on the SDKs (../../raw/github/firecrawl-firecrawl.md)
- Competes/overlaps with [[browserbase.com]] (Search & Fetch APIs plus full browser fleet) and [[browser-use.com]] (LLM-driven browser agent); Firecrawl differentiates on being scrape/crawl-first with token-efficient markdown as the primary deliverable rather than an interactive agent loop

## Documentation

Docs live at `docs.firecrawl.dev` (Mintlify-hosted, with `llms.txt`/`llms-full.txt` catalogs). Top-level sections include `introduction`, `ai-onboarding`, `features/{scrape,crawl,search,map}`, `api-reference/*` (per-endpoint reference), `sdks/{python,node,go,java,ruby,rust,dotnet,php,elixir,cli}`, and `mcp-server`.
