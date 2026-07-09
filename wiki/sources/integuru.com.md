---
type: source
category: "MCP servers & integrations"
source_url: https://www.integuru.com/
companion_urls:
  - https://github.com/Integuru-AI/Integuru
raw_files:
  - ../../raw/web/integuru.com.md
  - ../../raw/github/Integuru-AI-Integuru.md
tags:
  - api-generation
  - unofficial-api
  - reverse-engineering
  - agent-tools
  - direct-http
  - integration-platform
  - y-combinator
  - managed-integrations
related:
  - firecrawl.dev
  - browser-use.com
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - browserbase.com
  - webhook.site
  - brave-search
  - vellum.ai
product: integuru
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Integuru (YC-backed, 10M+ API calls/month) is a platform that generates fast, production-ready APIs for websites and web systems that lack usable public APIs — by reverse-engineering the private HTTP endpoints a platform's own frontend calls, then exposing them as documented, direct-HTTP integrations. It explicitly positions against browser automation and traditional RPA: no browsers, sub-3-second latency, 99.9%+ reliability, and 24/7 on-call maintenance on Production plans. The open-source companion repo `Integuru-AI/Integuru` (4.6K stars, AGPL-3.0) is the earliest public v0 agent; the current hosted product lives at integuru.com with CLI (`npm install -g integuru`) and web UI at app.integuru.com.

_All claims below are sourced from ../../raw/web/integuru.com.md unless otherwise noted._

## What it does

Integuru turns any authenticated web platform into a callable API. Operators provide a target URL and account credentials, describe the integration in natural language, and receive production-ready endpoints with full request/response schemas — typically within 20 minutes. The platform handles complex auth (session cookies, email/phone 2FA), edge-case branching logic across account states, and ongoing maintenance when target platforms change. Two delivery models: **self-serve** (Free/Developer/Production tiers where teams generate and run integrations directly) and **Full Managed Service** (Integuru builds each requested platform/feature for free sandbox trial, then maintains production integrations end to end with 24/7 on-call support).

## Key features

- **Direct HTTP, no browser** — integrations call backend JSON endpoints, not rendered HTML; contrasts with RPA/Puppeteer/Playwright approaches that break on UI changes (../../raw/github/Integuru-AI-Integuru.md)
- **Edge case coverage** — handles branching logic, states, and paths from real-world usage rather than only happy-path flows
- **Complete API schemas** — documented request/response formats for every field
- **Auth auto-healing** (Production) — re-authenticates on session expiry; supports session cookies, 2FA, OAuth-style flows
- **48+ published integrations** across healthcare (ModMed, DrChrono, eClinicalWorks), fintech, logistics, property management, restaurants, and more — with a public catalogue at `/integrations` and many more available on request
- **Industry verticals** — dedicated pages for AI agents, healthcare (HIPAA-compliant, BAA at no extra cost), fintech (200+ financial platforms), logistics, legal, government, real estate, and enterprise AI transformation
- **CLI-first access** — `npm install -g integuru` with web app at app.integuru.com; llms.txt and machine-readable site content for agent discovery

## Architecture

The hosted product reverse-engineers a target platform's network traffic to map endpoint dependency graphs and generate stable HTTP clients — the same conceptual approach as the open-source v0 agent, which takes a HAR file + cookies + natural-language prompt and outputs runnable Python that traverses a request dependency graph. (../../raw/github/Integuru-AI-Integuru.md) v0 workflow: `create_har.py` captures browser network requests → agent identifies the target action's request URL → maps dynamic parameters to upstream requests → builds dependency graph → generates code traversing from leaf nodes to the master request. The current SaaS product automates capture, auth handling, schema documentation, monitoring, and maintenance — v0 README notes the newest version is at integuru.com, not the repo.

## Installation

```bash
npm install -g integuru
```

Or use the web app at https://app.integuru.com. For the open-source v0 agent: Poetry install, set `OPENAI_API_KEY`, run `create_har.py` to capture HAR + cookies, then `poetry run integuru --prompt "..." --model gpt-4o`. (../../raw/github/Integuru-AI-Integuru.md)

## Example usage

Self-serve: connect a platform URL, authenticate, describe the desired read/write workflow in natural language, receive documented API endpoints. Managed: send a queue of platforms and features to Integuru; each integration is built for free sandbox trial within days, then maintained in production. Published integration example: ModMed healthcare — 21 actions across patient records, appointments, and clinical workflows via direct HTTP.

## When to use

When a platform has a rich web UI but no usable public API — incomplete official APIs, months-long partnership approval, or gated access — and the integration is production-critical (customer-facing product features, not one-off scraping). Explicitly **not** for mass-scraping public data or antibot-heavy scraping targets. Strong fit for AI agent tool access (sub-3-second tool calls vs 30s–5min browser automation), healthcare AI companies integrating with EHRs beyond FHIR limits, fintech startups connecting to banking/payroll portals, and logistics teams reaching carrier portals that EDI cannot cover.

## Maintenance status

YC-backed (Taiki, Inc.). 10M+ API calls/month across customer base. Production tier from $300/month with 24/7 on-call maintenance and auth auto-healing; Developer $30/month with manual maintenance; Free tier with 100 calls/month and assisted build-out. Companion repo 4,631 stars, AGPL-3.0, last pushed 2026-06-24 — v0 snapshot; active product development on hosted platform. (../../raw/github/Integuru-AI-Integuru.md)

## Ecosystem

Customers include Perspectives, Halo, Charta, Truss, Cartage, Roverpass, Knowtex, Wybit, Brickwise, Penciled, Andy AI, Paraspot, Opacity, Tivara, Multiplier, and Wedge. Competes architecturally with browser-automation stacks [[browser-use.com]], [[microsoft-playwright-mcp]], [[vercel-labs-agent-browser]], and [[browserbase.com]] — Integuru's pitch is that agents operating through the browser layer are too slow and brittle for production tool calls. Adjacent but different from [[firecrawl.dev]] (LLM-ready web *content* extraction at the HTML layer) and [[brave-search]] (search API). The v0 open-source agent shares the reverse-engineering philosophy but the hosted product adds auth auto-healing, schema docs, and managed maintenance that DIY HAR-based workflows lack.
