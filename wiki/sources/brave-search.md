---
type: source
category: "MCP servers & integrations"
source_url: https://brave.com/search/api/
companion_urls:
  - https://github.com/brave/brave-search-mcp-server
raw_files:
  - ../../raw/web/brave-search.md
  - ../../raw/github/brave-brave-search-mcp-server.md
tags:
  - web-search-api
  - mcp-server
  - llm-grounding
  - rag
  - search-api
  - brave-search
  - ai-agents
  - real-time-search
related:
  - anysearch.com
  - integuru.com
  - serper.dev
product: brave
detail_level: standard
created: 2026-06-09
updated: 2026-07-30
---

Brave Search API is a privacy-first, commercially licensed web search API that gives AI agents and chatbots access to the world's largest independent Web index — 30+ billion pages refreshed 100 million times daily — through specialized endpoints for web, images, videos, news, LLM context, and AI-powered summarization. It is the only major search API built on a fully independent crawler (not a reseller of Bing or Google data), with a SOC 2 Type II attestation, Zero Data Retention option for enterprise, and a native MCP server (`brave/brave-search-mcp-server`, 1,166 stars, TypeScript, STDIO + HTTP) that integrates directly into Claude Desktop, VS Code, and any MCP-compatible agent runtime.

_All claims below are sourced from ../../raw/web/brave-search.md unless otherwise noted._

## What it does

Brave Search API exposes real-time web intelligence through seven endpoints:

- **Web Search** — paginated results (max 20 per page) with freshness filters (`pd`/`pw`/`pm`/`py`), geographic targeting, and Search Goggles for custom re-ranking
- **LLM Context** — pre-extracted, AI-optimized web content with configurable token/snippet budgets, designed for direct injection into agent prompts and RAG pipelines
- **News Search** — freshness-controlled news results, defaulting to last 24 hours
- **Image / Video Search** — media-specific endpoints with metadata
- **Local Search** — business/POI lookup requiring Pro plan; falls back to web search on free tier
- **Place Search** — geographic POI lookup by lat/long, location string, or radius
- **Summarizer** — AI-generated summaries returned via a two-step key flow (web search with `summary: true`, then summarizer call)

## Key features

- **Independent index**: not a Bing or Google reseller; crawler covers 30B+ pages updated 100M times/day
- **Search Goggles**: declarative re-ranking rules allowing custom result boosting/demotion (for example, filter SEO-spam for unbiased tech reviews)
- **Extra snippets**: up to 5 additional text excerpts per result (Search plan and above)
- **Rich data enrichments**: weather, sports, stocks, currency, crypto, calculations via `enable_rich_callback=1` callback pattern
- **SOC 2 Type II** and **Zero Data Retention** for enterprise; HIPAA-ready architecture
- **Pricing**: Search at $5/1K requests ($5 monthly free credits); Answers at $4/1K + $5/M tokens; Enterprise custom

## Architecture

The MCP server (`brave/brave-search-mcp-server`) wraps the HTTP REST API in seven MCP tools, making all endpoints accessible to any MCP-compatible agent host without custom HTTP client code. (../../raw/github/brave-brave-search-mcp-server.md)

STDIO is the default transport as of v2.x, following standard MCP conventions; HTTP transport remains available via `BRAVE_MCP_TRANSPORT=http`. The server supports a space-separated tool whitelist (`BRAVE_MCP_ENABLED_TOOLS`) and blacklist (`BRAVE_MCP_DISABLED_TOOLS`) so operators can expose only the endpoints their agent needs. (../../raw/github/brave-brave-search-mcp-server.md)

The LLM Context endpoint (`brave_llm_context`) is the recommended integration point for agentic/RAG use cases: it bundles web fetching, content extraction, and token budgeting into a single call, returning structured context rather than raw HTML or link lists. Parameters control max URLs (1-50), max tokens (1024-32768), max snippets (1-256), and a `context_threshold_mode` that trades recall vs. precision. (../../raw/github/brave-brave-search-mcp-server.md)

## Installation

```bash
# NPX (STDIO, Claude Desktop)
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}

# Docker
{
  "mcpServers": {
    "brave-search": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "BRAVE_API_KEY", "docker.io/mcp/brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}
```

API key obtained from https://api-dashboard.search.brave.com/app/keys after choosing a plan. (../../raw/github/brave-brave-search-mcp-server.md)

## Example usage

```typescript
// brave_llm_context — grounding an agent with real-time web content
{
  tool: "brave_llm_context",
  params: {
    query: "latest SEC filings for NVIDIA 2026",
    count: 10,
    maximum_number_of_urls: 5,
    maximum_number_of_tokens: 8192,
    context_threshold_mode: "balanced",
    freshness: "pw"  // last 7 days
  }
}

// brave_web_search with Goggles re-ranking
{
  tool: "brave_web_search",
  params: {
    query: "best TypeScript testing frameworks",
    goggles: ["https://raw.githubusercontent.com/.../no-seo-spam.goggle"],
    extra_snippets: true,
    count: 10
  }
}
```

(../../raw/github/brave-brave-search-mcp-server.md)

## When to use

Brave Search API is the right choice when:

- Agents need real-time web grounding that cannot be served by a training cutoff — regulatory monitoring, competitor tracking, news-sensitive tasks
- Privacy or compliance constraints rule out Bing/Google APIs (Zero Data Retention, SOC 2, HIPAA)
- Quality-critical results require custom re-ranking without building a crawler (Goggles)
- The agent runtime already supports MCP and the team wants zero-HTTP-client integration
- Agentic pipelines need LLM-ready extracted content (not raw HTML) to minimize prompt token cost

For human-readable search results with pagination, use the Web Search endpoint. For AI pipelines requiring structured text context, use the LLM Context endpoint.

## Maintenance status

Stars: 1,166 | Latest release: v2.0.83 (2026-06-01) | License: MIT | Language: TypeScript | Node.js 22.x+ required (../../raw/github/brave-brave-search-mcp-server.md)

The MCP server is actively maintained by Brave Software; v2.x changed the default transport to STDIO and removed base64 image encoding in favor of URL-based references. Amazon Bedrock AgentCore is officially supported (`BRAVE_MCP_STATELESS=true`). (../../raw/github/brave-brave-search-mcp-server.md)

## Ecosystem

Brave Search API integrates with 24+ tools and platforms: LangChain, CrewAI, LlamaIndex, Dify (development frameworks); Cline, Cursor, Windsurf, Zed, Avante.nvim (code editors); Flowise, Microsoft Power Platform, Postman (low-code/no-code); BoltAI, MindMac (chat apps); Blaxel, Docker Hub, AWS Marketplace (infrastructure); DeerFlow, Quivr (RAG and research frameworks).

The MCP server is listed on MCP.so, PulseMCP, and Kiro. How-to guides cover integrations with OpenClaw, Claude Desktop, Dify, n8n, Open WebUI, and more.

## Documentation

Developer dashboard and REST API docs: https://api-dashboard.search.brave.com/app/documentation/web-search/get-started
