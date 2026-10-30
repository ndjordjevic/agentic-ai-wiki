---
type: source
category: "MCP servers & integrations"
source_url: https://www.tavily.com/
companion_urls:
  - https://github.com/tavily-ai/tavily-python
raw_files:
  - ../../raw/web/tavily.com.md
  - ../../raw/github/tavily-ai-tavily-python.md
tags:
  - web-search-api
  - content-extraction
  - site-crawl-map
  - cited-research-agent
  - remote-mcp-server
  - keyless-access
  - agent-grounding
related:
  - brave-search
  - serper.dev
  - serpapi.com
  - anysearch.com
  - firecrawl.dev
  - massive.com
  - firecrawl-anydoc
  - apify-apify-mcp-server
  - every-app-open-seo
product: tavily
detail_level: standard
created: 2026-10-15
updated: 2026-10-30
---

Tavily ("Tavily by Nebius") sells itself as "the web access layer for AI agents": one API for real-time web **Search**, **Extract**, **Crawl**, **Map**, and **Research** that returns clean, ranked, chunked, LLM-ready content instead of raw HTML or bare links. It is offered as a REST API, Python/JS SDKs, a remote MCP server, a `tvly` CLI with Agent Skills, and a keyless free tier. It is one of the most widely integrated agent search providers. LangChain calls it its recommended search tool, and it ships first-party integrations for CrewAI, LlamaIndex, Mastra, Vercel AI SDK, Pydantic AI, Agno, Google ADK, OpenAI/Anthropic tool-calling, n8n, Zapier, and many more. That reach makes it a default grounding layer in the agent-framework landscape this wiki covers.

_All claims below are sourced from ../../raw/web/tavily.com.md unless otherwise noted._

## What it does

Tavily replaces the "search, then scrape, filter and trim to fit the context window" pipeline with a single call. Search pulls from up to 20 sites per call, then uses proprietary AI to score, filter and rank the most relevant sources and content. It can add a short generated answer. Agents choose a capability by task:

| Capability | Use it when |
|---|---|
| **Search** | Sources are unknown or current context is needed (default start) |
| **Extract** | The URL is known or picked from Search |
| **Map** | You need a site's URL structure before crawling |
| **Crawl** | Many pages on one site must be read (graph traversal + extraction) |
| **Research** | The output should be a cited synthesis: a report, comparison, or decision-ready answer |

Requests pass through security layers that block PII leakage, prompt injection, and malicious sources. For example, an email address in a query returns "Query blocked, PII detected". The landing page claims 300M+ monthly requests, 3M+ developers, a 180 ms p50 on `/search`, a 99.99% uptime SLA, and SOC 2 / ISO 27001 / GDPR / zero-data-retention (ZDR) compliance. It also cites a #1 ranking on Tavily's own published Company Search benchmark.

## Key features

- **Search depths:** `ultra-fast` (one NLP summary per URL), `fast`, `basic` (1 credit), and `advanced` (2 credits). `chunks_per_source` returns ~500–800-character relevant snippets. Topics are `general`, `news`, and `finance`. Filters include time range, dates, include/exclude domains, country, and exact match.
- **Agent-grade defaults** from the docs: `search_depth="advanced"`, `chunks_per_source=3`, `max_results=5` (10 for broad research). Prefer Search → Extract for grounded answers, and avoid `include_answer` except as a seed.
- **Research endpoint:** an asynchronous research task with `model=mini|pro`, citation formats, streaming, and status polling. It costs 4–110 credits (mini) or 15–250 credits (pro) per request.
- **Keyless access:** Search and Extract work with no account via the header `X-Tavily-Access-Mode: keyless`, or via the no-key remote MCP. Responses are identical to keyed ones, but rate-limited. **x402** lets an agent pay per Advanced Search in USDC on Base, with no key or account.
- **Agent-readable docs:** every page is served as `.md`, alongside `llms.txt`, `llms-full.txt`, an `agents.md` setup guide, and a docs MCP server at `https://docs.tavily.com/mcp`.
- **Feedback API (beta):** agents can score their own search calls per result to improve ranking.
- **Enterprise:** bulk key generation and deactivation, organization usage reporting, per-request logs, and partner availability on Amazon Bedrock AgentCore, Azure AI Foundry, Databricks, IBM watsonx Orchestrate, and the Snowflake Marketplace.

## Architecture

The docs give three connection paths, chosen by where Tavily must run. **SDK/API** is for production apps and agent runtimes. **MCP** gives governed, shared access across a team's agent clients through the remote server at `https://mcp.tavily.com/mcp/`, which supports OAuth 2.0 or an API key, plus a `DEFAULT_PARAMETERS` header. The open-source `tavily-ai/tavily-mcp` package can also run locally. **CLI + Skills** (`tvly`) covers a single developer's local coding session, and installing the CLI also installs Agent Skills for Claude Code, Cursor, and Codex.

The Python SDK provides a sync `TavilyClient` and an async `AsyncTavilyClient`, with methods `search`, `get_search_context` (a RAG context string), `qna_search`, `extract` (up to 20 URLs), `crawl`, `map`, `research`/`get_research` (with streaming), and `feedback`. Called with no API key, it runs in keyless mode for Search and Extract only, and raises `TavilyKeylessLimitError` with `retry_after_seconds` when it hits the cap. Enterprises can inject a pre-configured `requests.Session` or `httpx.AsyncClient` to route traffic through their own API gateway. Optional `project_id`, `session_id`, `human_id`, and `client_name` values are sent as `X-*` headers for attribution, and `human_id` is hashed server-side (../../raw/github/tavily-ai-tavily-python.md).

## Installation

```bash
pip install tavily-python          # Python SDK (PyPI 0.8.5)
npm i @tavily/core                 # JavaScript SDK
pip install tavily-cli && tvly login    # CLI + Agent Skills
claude mcp add tavily-remote-mcp --transport http https://mcp.tavily.com/mcp/
```

A free API key from `app.tavily.com` gives 1,000 credits a month with no credit card required (../../raw/github/tavily-ai-tavily-python.md).

## Example usage

```python
from tavily import TavilyClient

client = TavilyClient(api_key="tvly-YOUR_API_KEY")   # or TavilyClient() for keyless
response = client.search("your query", search_depth="advanced",
                         chunks_per_source=3, max_results=5)
pages = client.extract(urls=["https://example.com"])
report = client.research(input="Research the latest developments in AI", model="pro")
result = client.get_research(report["request_id"])
```

```bash
tvly search "latest AI news"
tvly crawl "https://docs.example.com" --depth 2
tvly research "compare React vs Svelte for production apps"
curl -X POST https://api.tavily.com/search -H "X-Tavily-Access-Mode: keyless" \
  -H "Content-Type: application/json" -d '{"query": "latest AI news"}'
```

(../../raw/github/tavily-ai-tavily-python.md)

## When to use

Use Tavily when an agent needs fresh, citable web context in a form that fits the context window and is ready to use: RAG grounding, research and comparison agents, company intelligence, news monitoring, or crawl-to-RAG knowledge bases. Pick Research over Search when you want a finished multi-source answer with citations rather than raw sources to process yourself. Keyless mode and the remote MCP make it easy to try inside Claude Code or Cursor. Production use needs a paid plan or pay-as-you-go: 100 requests per minute on development keys and 1,000 on production keys, with Crawl capped at 100 and Research at 20.

## Maintenance status

The Python SDK `tavily-ai/tavily-python` has 1,424 stars and 192 forks. It is MIT-licensed, its default branch is `master`, and it was last pushed 2026-10-06. It has no GitHub releases; versions ship to PyPI, currently `tavily-python` 0.8.5. Crawl is still described as invite-only in the README, even though the docs list it as a standard endpoint (../../raw/github/tavily-ai-tavily-python.md). Pricing runs from Free (1,000 credits/month) through Project ($30 for 4k credits) and Growth ($500 for 100k credits), then pay-as-you-go at $0.008 per credit, and Enterprise. Tavily raised a $25M Series A in 2025 and has since joined Nebius.

## Ecosystem

Other official repos include `tavily-js`, `tavily-mcp`, `tavily-cli`, and `tavily-ai/skills` (Agent Skills). Tavily lists more than 35 integrations: frameworks (LangChain, LlamaIndex, CrewAI, Mastra, Haystack, Pydantic AI, Agno, Google ADK, Vercel AI SDK), no-code tools (n8n, Zapier, Make, Dify, Flowise, Langflow), agents (Devin, Hermes Agent, OpenCode, OpenClaw, Grok Build, Microsoft 365 Copilot), and MCP gateways (Arcade.dev, TrueFoundry, Scalekit, Composio). It also appears as a listed server on [[smithery.ai]]. In this wiki it sits alongside the other search APIs for agents, [[brave-search]], [[serper.dev]], [[serpapi.com]], and [[anysearch.com]]. Tavily differs from them by returning ranked content chunks and offering Crawl, Map, and Research rather than SERP listings alone. It overlaps with [[firecrawl.dev]] on extraction and crawling.

## Documentation

The docs at `docs.tavily.com` (Mintlify) are organized as Getting Started, API Reference (Search, Extract, Crawl, Map, Research, Feedback, Usage, Logs, plus an OpenAPI spec), Enterprise API, SDKs (Python and JS), Best Practices, Ecosystem (MCP, CLI, Agent Skills, x402), Integrations, Partnerships, Examples (an Agent Toolkit for production research agents, quick tutorials, use cases, a cookbook), and a Changelog.
