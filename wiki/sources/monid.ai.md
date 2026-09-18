---
type: source
category: "MCP servers & integrations"
source_url: https://monid.ai/
tags: [tool-gateway, mcp-server, agent-tools, pay-per-call, runtime-tool-discovery, data-apis, web-search, provider-failover]
related: [openrouter.ai, serpapi.com, serper.dev, firecrawl.dev]
product: monid
detail_level: standard
created: 2026-09-01
updated: 2026-09-01
---

Monid is a gateway for the tool and data calls an AI agent makes at runtime — it brands itself "the OpenRouter for agent tools." Where OpenRouter routes LLM inference across model providers behind one key and one balance, Monid does the analogous job one layer down: it brokers 1,000+ endpoints (the site also cites 1,700+ tools across 55+ providers) for web search, scraping, browser automation, people/company enrichment, contact verification, social-platform data, financial and on-chain data, maps, real estate, e-commerce pricing, jobs, SEO, news, voice/SMS, and generative media. An agent describes what it needs in natural language, Monid picks the endpoint, runs the call, normalizes the response to JSON, and meters it against one prepaid balance. It matters to this wiki as infrastructure that lets agents avoid per-vendor signup, keys, and schemas, and instead discover tools dynamically instead of hardcoding providers.

_All claims below are sourced from ../../raw/web/monid.ai.md unless otherwise noted._

## What it does

Monid sits between an agent and the many paid data providers it might need, exposing all of them through one base URL, one API key, and one balance. Instead of integrating each provider (Exa, Apollo, People Data Labs, Firecrawl, Browserbase, Ahrefs, etc.) one by one, an agent points at Monid, describes its need, and gets back normalized JSON from whichever provider fits, with pooled rate limits and automatic failover when a provider throttles. Billing is prepaid and pay-per-call — no subscription, no monthly minimum, no per-provider signup; every account starts with free credit ($1 is cited), and most calls cost a fraction of a cent (roughly $0.0013 per call cited on the landing page). Monid is positioned as complementary to OpenRouter rather than a competitor: OpenRouter meters tokens and answers "which model runs this turn," Monid meters tool calls and answers "which endpoint serves this call," and running both together is the intended setup.

## Key features

- **Runtime tool discovery** — agents search the catalog with natural-language queries rather than pre-loading every endpoint into context; discovery ranks candidates by fit and cost. New providers and endpoints are added continuously, so the catalog is meant to be queried live, not hardcoded.
- **Four setup surfaces** — a remote MCP server, an agent Skill (`SKILL.md` manifest), a CLI, and a REST API; setup is "one line" on any of them.
- **One balance, one invoice** — a single prepaid wallet covers all providers; estimated cost is held against the balance while a run is in flight, then settled to the actual amount on completion.
- **Pooled rate limits and failover** across providers within a category.
- **Broad catalog** — web search and grounded answers, page/whole-site scraping, browser automation, social data across Western and Chinese platforms (Douyin, Xiaohongshu, Weibo, Zhihu, Bilibili, Kuaishou, WeChat, Toutiao, and more), people/company enrichment, email/phone/address verification, maps and local reviews, real estate, e-commerce pricing, jobs and compensation, SEO and backlinks, financial/derivatives/prediction-market data, on-chain and DeFi, news, voice/SMS/agentic calls, demographics and weather, and generative AI for image, video, music, speech, and 3D.
- **x402 crypto payment** — an alternative to the prepaid workspace balance, paying per run with a USDC wallet via the x402 protocol.
- **Provider marketplace** — API providers can apply to list their endpoints; Monid handles routing, metering, and revenue share.

## Architecture and concepts

The core interaction model is a four-step loop: **discover** (natural-language search over endpoints, e.g. "twitter posts"), **inspect** (review the input schema, output structure, and current price before running — `monid inspect` is the source of truth for price, not the docs), **run** (execute the endpoint), and **poll** (retrieve results for long-running runs). Pricing is charged as per-call fees (fixed per execution) and/or per-result fees (variable by returned items, sometimes with a base fee), varying by units such as resolution or duration for media endpoints. Endpoints are grouped into the capability categories listed above; providers named per category include Exa and BlockRun (search), Apify and Firecrawl (scraping), Browserbase (browser automation), Apollo / People Data Labs / Akta (enrichment), Strale (verification), Ahrefs (SEO), QuickNode and DefiLlama (on-chain), ElevenLabs / MiniMax / Suzanne (generative and voice), and others. Authentication differs by surface: the MCP server uses OAuth login; the Skill/CLI/API path uses an API key generated in the dashboard and shown only once.

## Main APIs

REST endpoints (documented at `https://monid.ai/docs/api/overview`): `discover`, `inspect`, `run`, `runs/list`, `runs/get`, `runs/stop`, `wallet/balance`, `wallet/activities`, plus `auth/whoami` and `auth/workspaces`. The CLI mirrors these: `monid discover`, `monid inspect`, `monid run`, `monid runs list|get|stop`, and `monid keys list|add|activate|remove` for local credential management. The remote MCP server is at `https://mcp.monid.ai/v1` (Streamable HTTP); it is added to Claude Code with `claude mcp add --transport http monid https://mcp.monid.ai/v1` and authorized via `/mcp`, and connects to Claude.ai, ChatGPT, Codex, Cursor, OpenCode, and OpenClaw through each client's connector/plugin settings. MCP clients also expose a `monid_balance` tool returning `balance` and `held`.

## When to use

Use Monid when an agent needs external paid data and you would rather not sign up for, key, and bill each provider separately — you want one balance and one invoice, runtime tool selection instead of a hardcoded vendor, and failover when a provider throttles. It is especially attractive at low volume, where running providers directly means paying monthly subscriptions or per-seat plans regardless of usage across several separate vendors. Use a single provider's API directly when you only ever call that one vendor and never need routing or failover. Use an action platform such as Composio or Zapier when you need to *write* into SaaS apps rather than read data. Use a dedicated browser agent when a site has no API and you must click through a UI. Use OpenRouter (not Monid) to route the model call itself.

## Ecosystem

Monid is the tool-layer counterpart to [[openrouter.ai]], explicitly modeled on it and intended to run alongside it. Its catalog aggregates providers this wiki covers individually — search APIs like [[serpapi.com]] and [[serper.dev]], and the scraping/crawl layer represented by [[firecrawl.dev]] — behind one metered balance, so it sits upstream of them as an aggregator rather than a competitor. It ships a remote MCP server, placing it in the same integration surface as other agent-facing gateways, and supports x402 wallet payments for pay-per-run crypto billing. Community and support run through X (@MonidHQ), a Discord, and email; providers can apply to list APIs in the catalog via a public form.
