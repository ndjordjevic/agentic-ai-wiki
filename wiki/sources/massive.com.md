---
type: source
category: "MCP servers & integrations"
source_url: https://massive.com/
tags:
  - financial-market-data
  - remote-mcp-server
  - llms-txt-docs
  - x402-payments
  - websocket-streaming
  - s3-flat-files
  - stock-options-crypto-data
related:
  - marketstack.com
  - monid.ai
  - tavily.com
product: massive
detail_level: standard
created: 2026-10-15
updated: 2026-10-15
---

Massive is a financial market data platform covering stocks, options, indices, futures, forex, and crypto. It delivers data through a REST API, WebSocket streams, and S3 flat files, and its landing page also lists SQL query access. It says it is co-located in exchange datacenters with direct fiber cross-connects, offering tick-level trades and quotes, aggregate bars, and 20+ years of history depending on plan. For this wiki, what matters is how deliberately agent-first its distribution has become. It runs a hosted OAuth remote MCP server designed around a few composable tools rather than one tool per endpoint, publishes `llms.txt` indexes at every level of its docs tree, and lets agents with no account buy US stock data per request over x402. That makes it a reference example of "make your API agent-consumable" design for a domain data provider.

_All claims below are sourced from ../../raw/web/massive.com.md unless otherwise noted._

## What it does

Massive sells institutional-grade, exchange-direct market data. It describes the data as "clean, normalized … without survivorship bias", sold on simple monthly plans per asset class. There are three access methods:

- **REST API** (`api.massive.com`), for historical and real-time on-demand queries. Stocks alone covers tickers, aggregate bars (OHLC), snapshots, trades and quotes, technical indicators, corporate actions, fundamentals (including float), news, and SEC filings. Options (OPRA), futures (CME venues), indices, forex, crypto, and alternative data such as European consumer spending from Fable Data have their own sections.
- **WebSocket** for live streams of trades, quotes, per-second and per-minute aggregates, and Fair Market Value. Endpoints are `wss://socket.massive.com/<market>` for real-time data and `wss://delayed.massive.com/<market>` for delayed data.
- **Flat Files**, daily bulk CSVs (trades, quotes, minute and day aggregates) on an S3-compatible endpoint at `https://files.massive.com`, readable with `aws s3`, `rclone`, `mc`, or boto3.

The landing page claims trillions of rows, petabytes of raw data, and millions of messages per second.

## Key features

- **Hosted remote MCP server** at `https://mcp.massive.com/`. It uses OAuth sign-in with nothing to install, and has setup guides for Claude Code, Claude Desktop, Cursor (one-click install), ChatGPT, Grok, Codex, GitHub Copilot, and Gemini CLI. Access mirrors your plan, so for example Options data without an Options plan returns an access-denied error. Each session gets 64 MB of working storage and up to 10 concurrent workspaces.
- **Context-efficient tool design.** Instead of exposing dozens of endpoints as tools, the server offers a few composable tools: natural-language endpoint search, on-demand parameter docs, and execution of any REST call. It indexes `llms.txt` at startup, so it stays current as endpoints are added.
- **Self-hosted MCP** (`massive-com/mcp_massive`, installed via `uv` or `pip`). It adds a local data workspace with in-memory DataFrames, SQL over results, and built-in financial functions such as Greeks, returns, and technical indicators.
- **LLM-friendly docs.** Every page is available as `.md`, has "Copy for LLM" and "View as Markdown" buttons, and `llms.txt` indexes exist at root, section, and category level (e.g. `/docs/rest/stocks/tickers/llms.txt`). The root `llms.txt` even tells agents how to handle API keys: read them from `MASSIVE_API_KEY`, and never ask the user to paste a key into chat.
- **x402 pay-per-request.** On `agent.massive.com`, agents pay in USDC on Base, with no account or API key. Coverage is US stocks only: end-of-day bars and aggregates, current-session snapshots, SMA/EMA/RSI/MACD, reference data, news, and SEC filings (10-K sections, 8-K disclosures, 13-F, Forms 3/4), with intraday values based on Fair Market Value. Settlement goes through Coinbase Developer Platform's facilitator, and routes are listed on Agentic.Market and the x402 Bazaar. Only successful requests are charged.
- **Official clients** for Python, JavaScript, Go, and Kotlin/JVM (`massive-com/client-*`), which handle auth, retries, pagination, and parsing.

## Architecture and concepts

The AI Tools quickstart lays out an integration ladder:

| Approach | Best for | Context efficiency | Setup effort |
|---|---|---|---|
| MCP server | most agentic workflows and complex analysis | excellent | low |
| `llms.txt` + Markdown | documentation-aware agents | very good | none |
| Direct REST + function calling | custom orchestration, full control | good | medium |
| Skills / instructions | team conventions, compliance rules | excellent | low |
| x402 pay-per-request | agents with no Massive account | good | medium |

It recommends starting with MCP plus `llms.txt`, then adding Skills that encode team rules on top. Examples include using adjusted versus unadjusted prices, handling corporate actions and market hours, and preferred return or volatility formulas. MCP does not carry streaming, so WebSocket remains the path for live feeds. REST responses share one JSON envelope (`status`, `count`, `results`, `request_id`), so one endpoint teaches the pattern for all.

## Main APIs

- REST examples: `GET /v3/reference/tickers`, `GET /v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from}/{to}`, `GET /v2/snapshot/locale/us/markets/stocks/tickers`, `GET /v3/snapshot` (unified multi-asset snapshot), `GET /v3/trades/{ticker}`, `GET /v3/reference/dividends`.
- MCP in Claude Code: `claude mcp add --transport http massive https://mcp.massive.com/`, then `/mcp` → massive → Authenticate in the browser. A free Basic account is enough to start.
- Agent onboarding prompt from the landing page: *"I want to work with financial market data. Read massive.com/docs/llms.txt to see what Massive covers, then help me get started."*
- x402: ask the agent to fetch `https://agentic.market/SKILL.md`. This Coinbase-maintained skill sets up an agent wallet, finds the route, and pays per request. Agents can request missing routes for free via `POST https://agent.massive.com/feedback`.

## When to use

Use Massive when an agent or app needs reliable, exchange-sourced market data: trading tools, research agents, backtesting, dashboards, screening options chains, or SEC-filing analysis. Use the hosted MCP for interactive agent work inside Claude Code or Cursor, REST with the official clients for production code, WebSocket for real-time feeds, and Flat Files for bulk history. x402 suits autonomous agents with no account that only need US stock data at end-of-day or snapshot recency. Real-time, tick-level, or non-stock data requires an API key and plan.

## Ecosystem

Massive integrates with every major agent client through its remote MCP server, and its x402 offering ties into Coinbase's agent-payments stack (Agentic.Market, the x402 Bazaar, and Coinbase's payments MCP). The landing page names NYSE, Nasdaq, and Cboe as the exchanges it connects to directly. Within this wiki it is the deeper, agent-native counterpart to [[marketstack.com]], a simpler REST market-data API. It shares the pay-per-request x402 model with [[tavily.com]], and complements [[monid.ai]], a metered gateway that brokers many data APIs to agents.
