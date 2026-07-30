---
type: source
category: "MCP servers & integrations"
source_url: https://serpapi.com/
tags:
  - google-search-api
  - serp-api
  - web-search-api
  - mcp-integration
  - search-api
  - zero-trace-mode
  - legal-shield
  - ai-grounding
related:
  - brave-search
  - anysearch.com
  - serper.dev
product: serpapi
detail_level: standard
created: 2026-07-30
updated: 2026-07-30
---

SerpApi is a real-time JSON API for structured search-engine results, covering over 100 named endpoints across Google (dozens of verticals: search, images, maps, shopping, scholar, patents, trends, flights, and more), Bing, Baidu, Amazon, DuckDuckGo, Yandex, Yahoo!, YouTube, and a dozen other engines/platforms, plus an in-house "Search Index" LLM-first web index still in preview. It is a larger, more enterprise-oriented, GEO-priced competitor to [[serper.dev]] and [[brave-search]] in this wiki's search-API-for-agents cluster, distinguished by full-browser CAPTCHA-solving execution, a U.S. Legal Shield (up to $2M coverage) for lawful scraping, and SOC 2/SOC 3/ISO 27001 certification.

_All claims below are sourced from ../../raw/web/serpapi.com.md unless otherwise noted._

## What it does

SerpApi exposes over 100 distinct search endpoints as a single REST API (`GET https://serpapi.com/search?engine=<name>&...`), each returning structured JSON mirroring the corresponding search-engine vertical. The flagship Google Search API alone supports device targeting, geographic/location parameters (`location`, `uule`, `lat`/`lon`/`radius`), localization (`google_domain`, `gl`, `hl`, `cr`, `lr`), and search-type filters (`tbm` for images/local/video/news/shopping), returning organic results, knowledge graph data, local results, related searches, and pagination. Beyond Google, it covers Bing, Baidu, Amazon, Apple App Store/Maps, DuckDuckGo, eBay, Facebook, Instagram, Naver, OpenTable, The Home Depot, Tripadvisor, Walmart, Yahoo!, Yandex, Yelp, and YouTube — each with its own dedicated endpoint(s) documented at `serpapi.com/<engine>-api.md`.

## Key features

- **Real-time execution in full browsers with CAPTCHA solving**, rather than a static crawled index
- **Search Index** — SerpApi's own LLM-first web index (`engine=search_index`, currently in preview), purpose-built for "AI grounding, benchmarking, and search automation" with a `mode=deep` option that runs "parallel sub-query fan-out" to decompose a query into multiple aspects for more diverse results
- **Global geolocated routing** via proxy servers for location-accurate results
- **U.S. Legal Shield** — up to $2 million in coverage for lawful search-data scraping (Production plan and above)
- **ZeroTrace Mode** — prevents search parameters, files, and metadata from being stored (Enterprise-only on the Search Index endpoint; broader ZeroTrace also mentioned on the main pricing page)
- **Compliance** — SOC 2 Type II, SOC 3, and ISO 27001 certified; 99.95% SLA with refund penalty

## Architecture and concepts

SerpApi's core architecture is a single REST endpoint (`serpapi.com/search`) parameterized by `engine=<name>` to select among 100+ supported search verticals, rather than one endpoint per engine — the per-engine ".md" docs pages each describe that engine's parameter subset and response shape on top of the shared request/response envelope. The `llms.txt` catalog (captured verbatim in the raw file) is itself the clearest map of this structure: every engine, pricing page, integration guide, and use-case page is enumerated with a one-line description, which is unusually complete for a commercial SaaS API.

## Main APIs

- **Google Search API** (`engine=google`) — the flagship endpoint; full parameter set for location, localization, device, and search-type filtering (see What it does)
- **Search Index** (`engine=search_index`) — SerpApi's own LLM-first index; supports `no_cache`, `async` (submit now, retrieve later via a Searches Archive API), `zero_trace`, and `json_restrictor` (payload-size reduction by filtering output fields)
- **Client libraries** — official SDKs for Ruby, Python, JavaScript, Golang, PHP, Java, Rust, .NET, Swift, C++, plus a CLI, each in its own GitHub repository (`serpapi-python`, `serpapi-javascript`, etc.)
- **MCP integration** (`serpapi-mcp`) — lets "any MCP-compatible AI agent (Claude, ChatGPT, Cursor, etc.) use SerpApi as a web search tool"

## When to use

SerpApi fits teams that need broad engine coverage beyond Google alone (Amazon, Walmart, Yelp, Tripadvisor, YouTube, and more, in one account) or need the U.S. Legal Shield / enterprise compliance posture (SOC 2/SOC 3/ISO 27001) for regulated scraping use cases — background checks, price monitoring, IP/copyright checking are named use cases on the site. For teams that only need Google-flavored web/news/shopping search at the lowest price point, [[serper.dev]] is cheaper and simpler; for teams prioritizing an independent (non-reseller) crawler with a maintained MCP server and Zero Data Retention as a default rather than an add-on, [[brave-search]] is the closer fit.

## Ecosystem

SerpApi integrates via first-party libraries in Ruby, Python, JavaScript, Golang, PHP, Java, Rust, .NET, Swift, C++, a CLI, and an MCP server (`serpapi-mcp`), each in its own GitHub repository. The only `github.com` link discoverable on the public site is `serpapi/public-roadmap` (129 stars) — a public issue-tracker/roadmap board, not the product's source — so no companion GitHub repo was ingested here; see the raw file's Notes section for the discovery/rejection reasoning. Client base includes Nvidia, Shopify, Perplexity, Adobe, Samsung, KPMG, and others.
