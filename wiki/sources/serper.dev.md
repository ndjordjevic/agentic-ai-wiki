---
type: source
category: "MCP servers & integrations"
source_url: https://serper.dev/
tags:
  - google-search-api
  - serp-api
  - web-search-api
  - search-api
  - ai-agents
  - langchain-integration
  - credit-based-pricing
related:
  - brave-search
  - anysearch.com
product: serper
detail_level: standard
created: 2026-07-30
updated: 2026-07-30
---

Serper is a Google Search API positioned as "The World's Fastest & Cheapest," returning results in 1-2 seconds across ten search verticals with pay-as-you-go credit pricing starting at $0.30 per 1,000 queries. It is widely used as an agent-facing search tool — bundled as a built-in integration in LangChain, CrewAI, Jan AI, and Haystack — making it a cheaper, Google-backed alternative to [[brave-search]] and [[anysearch.com]] for agents that need real-time web grounding.

_All claims below are sourced from ../../raw/web/serper.dev.md unless otherwise noted._

## What it does

Serper wraps Google's search results in a REST API returning JSON for ten distinct search types: standard web search, images, news, maps/places, video, shopping, Google Scholar, patents, and autocomplete. Each response mirrors the structure of the corresponding Google vertical — organic results with titles/URLs/snippets for web search, publication dates and citation counts for Scholar, pricing/delivery/retailer data for shopping, and inventors/assignees/filing dates/technical figures for patents.

## Key features

- **Speed and price positioning** — results in 1-2 seconds, advertised as "up to 10 times cheaper than competitors such as SerpAPI and Bright Data"
- **Ten search verticals** in one API surface rather than a single web-search endpoint
- **Multilingual support** — language and region selection (e.g. `en` / US) per query
- **No-credit-card free tier** — 2,500 complimentary queries to start
- **Scale** — claims over 850,000 companies and developers as active users

## Architecture and concepts

Serper is a closed-source hosted API (no public GitHub repository was found on the site) fronting Google's search index rather than an independent crawler — distinguishing it architecturally from [[brave-search]], which runs its own index. Access is entirely through the REST API; there is no MCP server or SDK published on the marketing site itself.

## Main APIs

The site's interactive **Playground** (`serper.dev/playground`) is the primary way to explore request/response shapes, but it sits behind account login/signup — no endpoint schemas or parameter references are reachable from the public marketing page. The site states that further documentation is hosted on Medium rather than a dedicated docs subdomain or `/docs` path.

## When to use

Serper fits agent and RAG pipelines that need fast, low-cost Google search grounding across multiple verticals (web, news, shopping, scholarly, patents) without standing up a Search API integration from scratch — particularly for teams already using LangChain, CrewAI, Jan AI, or Haystack, where Serper is a drop-in tool. For teams that specifically need an independent (non-Google/Bing-reseller) index, SOC 2/Zero Data Retention compliance, or a maintained MCP server, [[brave-search]] is the closer fit.

## Ecosystem

Serper integrates with LangChain, CrewAI, Jan AI, and Haystack as a built-in search tool. The site references a Playground (login-gated interactive tester), a Dashboard (account management), a status page, and documentation hosted on Medium; no companion GitHub repository is published.
