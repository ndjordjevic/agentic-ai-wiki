---
type: source
category: "Browser & web automation"
source_url: https://alexandria.firecrawl.dev
companion_urls:
  - https://github.com/firecrawl/skills
raw_files:
  - ../../raw/web/alexandria.firecrawl.dev.md
  - ../../raw/github/firecrawl-skills.md
tags:
  - structured-data-providers
  - firecrawl-alexandria
  - agent-data-apis
  - mcp-integration
  - credit-metered-tools
  - find-inspect-call
  - government-research-indexes
related:
  - firecrawl.dev
  - monid.ai
  - tavily.com
  - serpapi.com
  - skills.sh
  - firecrawl-anydoc
  - apify-apify-mcp-server
product: alexandria.firecrawl.dev
detail_level: standard
created: 2026-11-14
updated: 2026-11-14
studied: true

---

Alexandria by Firecrawl is a library of licensed data providers and specialized indexes that AI agents call through the same Firecrawl surfaces they already use — ChatGPT/Codex plugin, Claude connector, MCP server, CLI, API/SDKs — returning typed, sourced records (company, people, jobs, SEC filings, public records, research papers, and more) in one call instead of scraping HTML about the same facts.

_All claims below are sourced from ../../raw/web/alexandria.firecrawl.dev.md unless otherwise noted._

## What it does

Alexandria sits beside Firecrawl's Search/Scrape/Crawl stack: when an official source already publishes the answer, an agent discovers a **provider** tool, inspects its contract (inputs, sample response, credit price), then executes it via `scrape` with an `alexandria: { provider, capability, options }` body and no URL. Discovery is free; execution is charged at each tool's listed credit price. Keyless Firecrawl access does **not** include Alexandria providers — a signed-in account or API key on a team with Alexandria enabled is required. Firecrawl's own **Government Index** (~30M US government pages) and **Research Index** (40M+ paper abstracts) tools are free within plan rate limits.

## Key features

- **Provider + tool model** — a provider supplies data (page at `/<provider>`); a tool is one callable capability named by `provider` + `capability`. Firecrawl also publishes composite tools that chain several providers into one job.
- **Category catalog** — dozens of topic shelves with live provider counts (e.g. public records 226, company 125, retail 83, people 41, jobs 19, finance 47); each category has agent-readable Markdown under `/agents/categories/<category>`.
- **Find → inspect → call** — free semantic discovery (`search` with `sources: ["alexandria"]` or `find_tools`), free contract inspection, then billed execution; optional feedback within 20 minutes refunds 1 credit (capped per site/team/day).
- **Agent surfaces** — same tools via plugin/connector, hosted MCP (`mcp.firecrawl.dev/v2/mcp` or OAuth), local `firecrawl-mcp`, CLI (`firecrawl search` / `find-tools` / `scrape`), and Python/Node SDKs; Agent runs can auto-pick providers when `exchange: { enabled: true }`.
- **Terms gate** — some providers return `THIRD_PARTY_DATA_TERMS_REQUIRED` with `requiresAction.url`; agents must hand that URL to a human admin and never accept terms themselves.
- **Companion skills catalog** — `firecrawl/skills` (156★, ISC) distributes `firecrawl-alexandria` and related core/build/workflow skills via `npx skills add firecrawl/skills`. (../../raw/github/firecrawl-skills.md)

## Architecture

Alexandria is not a separate product API host: every request goes to `https://api.firecrawl.dev/v2` with a Firecrawl Bearer key. Search returns ranked tools alongside optional web results; Find Tools browses/paginates the catalogue; Scrape executes one (or a batch of up to 10) Alexandria calls. Domain matching can attach tools to a website during search/scrape. Credits are shared with the rest of Firecrawl (1 credit ≈ 1 basic scrape page elsewhere); tool prices are listed on each provider page and via `find_tools` with `includeCosts: true`.

The GitHub companion `firecrawl/skills` is a CI-synced distribution catalog (not the skill source of truth): core skills including `firecrawl-alexandria` mirror from `firecrawl/cli`, build skills from `firecrawl/firecrawl`, workflows from `firecrawl/firecrawl-workflows`. (../../raw/github/firecrawl-skills.md)

## Installation

```bash
# CLI + skills (includes firecrawl-alexandria)
npx -y firecrawl-cli@latest init --all --browser
# or skills catalog only
npx skills add firecrawl/skills
# MCP (OAuth or API key)
# https://mcp.firecrawl.dev/v2/mcp-oauth
```

Paste the AGENTS.md/CLAUDE.md block from the What-is-Alexandria page so coding agents check Alexandria before scraping structured data. (../../raw/github/firecrawl-skills.md)

## Example usage

```bash
firecrawl search alexandria 'open federal cybersecurity contracts'
firecrawl list sam-gov opportunities/search --pretty
firecrawl scrape sam-gov/opportunities/search \
  --options '{"query":"cybersecurity","statuses":["active"],"page_size":20}' \
  --json -o .firecrawl/sam-gov.json
```

Via MCP: `firecrawl_search` with `sources: ["alexandria"]` → `firecrawl_find_tools` → `firecrawl_scrape` with an `alexandria` body and no `url`. (../../raw/github/firecrawl-skills.md)

## When to use

Prefer a provider tool when the task needs the same fields across many entities, exact figures/timestamps, provenance, or many records. Use ordinary Firecrawl web search/scrape when a page already answers the question. Alexandria is the structured-data counterpart to [[firecrawl.dev]]'s HTML extraction path, and a Firecrawl-native peer to aggregator gateways like [[monid.ai]].

## Maintenance status

Companion catalog `firecrawl/skills`: 156 stars, ISC, default branch `main`, last push 2026-11-11; no GitHub releases. Alexandria itself launched with Firecrawl's $75M Series B (Sep 2026) and has been expanding providers/indexes (Government Index, Research Index, SEC filings, life sciences, people enrichment, etc.). (../../raw/github/firecrawl-skills.md)

## Ecosystem

Works wherever Firecrawl does: ChatGPT/Codex plugin, Claude connector, Claude Code, Cursor, any MCP client, LangChain/LangGraph/LlamaIndex/OpenAI Agents SDK integrations listed on Firecrawl docs, and automation tools (Dify, n8n, Make, Zapier). Skills install through [[skills.sh]]-style `npx skills add`. Benchmarks and rankings pages publish provider quality/speed/cost from live agent calls; Firecrawl cites a 21% higher answer-quality score vs built-in web tools across 845 internal tasks.
