---
type: source
category: "Media, voice & content"
source_url: https://supadata.ai/
companion_urls:
  - https://github.com/supadata-ai/mcp
raw_files:
  - ../../raw/web/supadata.ai.md
  - ../../raw/github/supadata-ai-mcp.md
tags:
  - video-transcript-api
  - youtube-transcript
  - social-media-metadata
  - web-scraping-api
  - mcp-server
  - structured-data-extraction
  - rag
related:
  - meetclaras.com
  - firecrawl.dev
  - coleam00-cole-medin-knowledge-base
product: supadata
detail_level: standard
created: 2026-07-30
updated: 2026-07-30
---

Supadata is a "web media to text" REST API for developers that turns YouTube, TikTok, Instagram, X (Twitter), and Facebook videos into transcripts, metadata, and AI-extracted structured data, alongside general-purpose web scrape/map/crawl endpoints — plus an official MCP server (`supadata-ai/mcp`, 61 stars, MIT, TypeScript) that exposes the same nine tools to Claude, Cursor, and other MCP clients. It occupies a narrower, more developer-facing niche than [[meetclaras.com]]'s end-user YouTube knowledge-extraction product, and overlaps [[firecrawl.dev]] on the web scrape/map/crawl surface while adding video/social-platform transcript and metadata extraction that Firecrawl doesn't cover.

_All claims below are sourced from ../../raw/web/supadata.ai.md unless otherwise noted._

## What it does

Supadata exposes video transcript extraction (YouTube, TikTok, Instagram, X, Facebook, and public file URLs), social-media metadata retrieval (titles, descriptions, tags, thumbnails, engagement metrics), AI-powered structured/schema-based data extraction from video content, and general web scrape/map/crawl endpoints — all through one REST API at `https://api.supadata.ai/v1`, authenticated via an `x-api-key` header. The Transcript endpoint "fetches existing transcript or fall back to AI to create one," returning either plain text or timestamped segments, with automatic async job handling (HTTP 202 + polling) for videos longer than 20 minutes.

## Key features

- **Universal transcript extraction** across five platforms plus raw file URLs (MP4, WEBM, MP3, FLAC, MPEG, M4A, OGG, WAV up to 1 GB), with `native`/`generate`/`auto` modes and multi-language support via ISO 639-1 codes
- **AI-powered structured extraction** — custom prompt or JSON-schema-based data extraction from video content, not just raw transcript text
- **Web scrape/map/crawl** — single-page scraping, site-wide URL discovery, and multi-page crawl jobs, returned as Markdown/HTML/JSON
- **YouTube-specific endpoints** for channel, playlist, channel-videos, playlist-videos, and batch processing
- **MCP server** (`supadata-ai/mcp`) exposing all nine tools directly to MCP-compatible agent clients (../../raw/github/supadata-ai-mcp.md)

## Architecture

The MCP server wraps the REST API's tools 1:1 — `supadata_transcript`, `supadata_check_transcript_status`, `supadata_metadata`, `supadata_extract`, `supadata_check_extract_status`, `supadata_scrape`, `supadata_map`, `supadata_crawl`, and `supadata_check_crawl_status` — registered via `@modelcontextprotocol/sdk` on stdio transport with Zod-validated inputs, built on top of the official `@supadata/js` JavaScript SDK. (../../raw/github/supadata-ai-mcp.md)

Long-running operations (large-video transcription, AI extraction, multi-page crawls) are modeled as asynchronous jobs: an initial call returns a `jobId`, and a companion "check status" tool/endpoint polls for `queued`/`active`/`completed`/`failed` states, with results expiring after 1 hour. This same async pattern is used consistently across transcript, extract, and crawl operations rather than being a one-off for any single endpoint. (../../raw/github/supadata-ai-mcp.md)

## Installation

```bash
# MCP server — see the integration guide for Claude, ChatGPT, Cursor, Windsurf, VS Code
# https://docs.supadata.ai/integrations/mcp
# Requires SUPADATA_API_KEY environment variable

# From source
npm install
npm run build
npm run start
```

REST API access requires only an API key generated automatically at sign-up (`dash.supadata.ai`); the JS (`@supadata/js`) and Python SDKs wrap the same endpoints for direct code integration outside of MCP. (../../raw/github/supadata-ai-mcp.md)

## Example usage

```bash
# Direct REST call
curl 'https://api.supadata.ai/v1/transcript?url=[video_url]' \
  -H 'x-api-key: {your_api_key}'

# Via the MCP server's transcript tool
supadata_transcript --url "https://youtube.com/watch?v=example" --lang "en"

# Web scrape via MCP
supadata_scrape --url "https://example.com" --lang "en"
```

(../../raw/github/supadata-ai-mcp.md)

## When to use

Supadata fits agent and pipeline builders who need programmatic transcript/metadata extraction across multiple video and social platforms in one API — RAG ingestion, content repurposing, brand monitoring, and sentiment analysis are named use cases — especially where an MCP-native integration is wanted alongside a plain REST/SDK path. For teams whose needs are purely YouTube-and-human-facing (interactive Q&A over a transcript, not programmatic pipeline access), [[meetclaras.com]] is a closer fit; for teams that only need general-purpose web scrape/crawl without the video/social-metadata layer, [[firecrawl.dev]] is a more focused alternative.

## Maintenance status

The MCP server has 61 stars, MIT license, TypeScript, and no published GitHub release (versioned via `package.json`/`CHANGELOG.md` instead); last pushed 2026-06-09. (../../raw/github/supadata-ai-mcp.md) The wider product ships a separate JS and Python SDK, no-code integrations (Zapier, Make, n8n, Active Pieces), and a public changelog/status page at `feedback.supadata.ai` / `status.supadata.ai`.

## Ecosystem

Supadata lists AppsFlyer, Bosch, HelloFresh, Huel, and OpenAI as users. Beyond the official MCP server, it integrates with Zapier, Make, n8n, and Active Pieces, and is also listed on RapidAPI under separate YouTube-transcript and web-scraping listings. Six credit-based pricing tiers run from a 100-credit free plan up to a 1,000,000-credit "Supa" plan ($897/mo), plus custom Enterprise pricing.

## Documentation

Full API reference lives at `docs.supadata.ai` (Mintlify-hosted), covering Universal Services (Transcript, Metadata), Web Scraping (Scrape, Map, Crawl), YouTube-specific endpoints (Channel, Playlist, Channel Videos, Playlist Videos, Batch), and a documented error taxonomy (invalid request, unauthorized, not found, limit exceeded, upgrade required, transcript unavailable, internal error). The docs site publishes its own `llms.txt`/`llms-full.txt` for agent-driven discovery.
