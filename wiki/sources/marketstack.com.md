---
type: source
source_url: https://marketstack.com/
tags:
  - stock-market-api
  - financial-data
  - rest-api
  - edgar-filings
  - intraday-data
  - end-of-day-data
  - apilayer
  - agent-tools
related:
  - browser-use.com
  - pushover.net
  - trigger.dev
product: marketstack
detail_level: standard
created: 2026-07-06
updated: 2026-07-06
---

Marketstack is an APILayer-hosted REST API for worldwide stock market data — end-of-day, intraday, real-time US quotes (IEX), 750+ market indices, splits/dividends, exchange metadata, currencies, and (on V2) SEC EDGAR filings. A free tier offers 100 requests/month with EOD data and 1-year history; paid plans from $9.99/month unlock intraday, real-time intervals down to 1 minute, commodities, and company fundamentals. For agentic AI workflows it is a straightforward external-data primitive: HTTP GET + JSON + `access_key`, suitable for wrapping as an agent tool or MCP function when agents need live or historical market context.

_All claims below are sourced from ../../raw/web/marketstack.com.md unless otherwise noted._

## What it does

Marketstack exposes global equities and indices through a RESTful JSON API on `api.marketstack.com`. Developers authenticate with an `access_key` query parameter, request one or more ticker symbols (up to 100 per call), and receive paginated OHLCV data, corporate actions, exchange metadata, or ticker search results. US intraday data comes from IEX; US EOD data is licensed from Tiingo. The service runs on APILayer cloud infrastructure, claims ~100% uptime over the trailing year, and handles millions of requests per hour. Documentation lives on `docs.apilayer.com` (the `marketstack.com/documentation` path redirects there). V2 is the current recommended API version; V1 endpoints are deprecated after June 30, 2025.

## Key features

- **End-of-day (EOD) data** — `/v1/eod` and `/v2/eod` with `symbols`, `date_from`/`date_to`, `/eod/latest`, adjusted prices (CRSP methodology), splits and dividends inline
- **Intraday & real-time** — `/intraday` for IEX US tickers; intervals `1min`–`24hour`; sub-15-minute intervals (`1min`, `5min`, `10min`) require Professional plan or higher
- **Market indices** — 750+ indices via `INDX` exchange MIC (e.g. `DJI.INDX` for Dow Jones)
- **Corporate actions** — dedicated `/splits` and `/dividends` endpoints plus per-ticker routes under `/tickers/[symbol]/`
- **Ticker & exchange discovery** — `/tickers` (search, metadata, 170k+ symbols), `/exchanges` (2700+ exchanges with MIC, timezone, country)
- **Reference data** — `/currencies` and `/timezones` endpoints
- **EDGAR filings (V2)** — six new endpoints for SEC documents (10-K, 10-Q, 8-K) announced on the landing page; available on newer pricing tiers
- **Premium tiers** — Business plan adds company ratings, statements, details, concepts, and facts; Enterprise offers custom volume
- **Developer ergonomics** — interactive docs with copy-paste examples in JavaScript (fetch/axios), Python (requests/http.client); 5 req/s rate limit; structured validation errors

## Architecture and concepts

The API follows a simple GET-over-HTTPS model: every request includes `access_key`, responses wrap data in `{ pagination, data }` envelopes, and each symbol in a multi-symbol request consumes one API quota unit. Historical EOD reaches back 30 years; intraday history is capped at the last 10,000 entries per interval. Exchange coverage is identified by MIC codes (`XNAS` for NASDAQ, `IEXG` for IEX, `INDX` for indices). Plan gating is enforced at the endpoint level — free users get EOD only; intraday requires Basic+; real-time sub-15-minute intervals require Professional+. Marketstack is one product in the broader APILayer API marketplace (currencies, weather, PDFs, etc.) but operates as a standalone subscription.

## Main APIs

| Endpoint | Purpose | Key parameters |
|---|---|---|
| `GET /v1/eod` | End-of-day OHLCV | `symbols`, `date_from`, `date_to`, `exchange`, `limit`, `offset` |
| `GET /v1/intraday` | Intraday/real-time bars | `symbols`, `interval`, `exchange`, date filters |
| `GET /v1/splits` | Stock split history | `symbols`, date range |
| `GET /v1/dividends` | Dividend history | `symbols`, date range |
| `GET /v1/tickers` | List/search tickers | `search`, `exchange`, pagination |
| `GET /v1/tickers/{symbol}/eod` | Per-ticker EOD | symbol in path |
| `GET /v1/tickers/{symbol}/intraday` | Per-ticker intraday | symbol in path |
| `GET /v1/exchanges` | Exchange metadata | `search`, pagination |
| `GET /v1/exchanges/{mic}/tickers` | Tickers on an exchange | MIC in path |
| `GET /v1/currencies` | Supported currencies | pagination |
| `GET /v2/eod` | V2 EOD (current) | same pattern as v1 |

Example request:
```
https://api.marketstack.com/v1/eod?access_key=YOUR_ACCESS_KEY&symbols=AAPL
```

## When to use

- **Financial agent tools** — when a coding or browser agent needs programmatic stock prices, historical charts, or index data (the [[browser-use.com]] docs include a stock-price tool example; Marketstack is a production API backing such patterns)
- **Alerting pipelines** — combine price checks with notification primitives like [[pushover.net]] for threshold-based human alerts
- **Scheduled workflows** — poll EOD or intraday data from job runners like [[trigger.dev]] without building market-data infrastructure
- **Research agents** — EDGAR filing endpoints (V2) support compliance and financial-research agents that need SEC documents
- **Prototyping** — the free 100-request/month tier is enough to validate an agent tool integration before upgrading

## Ecosystem

Marketstack is an APILayer product (same parent as the broader API marketplace linked from the landing page). No public GitHub companion repo was found. Docs, signup, and billing are split across `marketstack.com` (marketing/pricing) and `docs.apilayer.com` (API reference). Status monitoring at `status.marketstack.com`. V2 API reference at `docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0` covers newer endpoints including EDGAR; V1 docs remain available but are marked for deprecation.
