---
type: source
source_url: https://reseek.net/
tags:
  - personal-knowledge-management
  - second-brain
  - semantic-search
  - mcp-server
  - ocr
  - ai-chat
  - bookmark-manager
  - knowledge-capture
related:
  - runcabinet.com
  - meetclaras.com
  - supermemory.ai
  - HKUDS-RAG-Anything
  - zaro.ai
product: reseek
detail_level: standard
created: 2026-05-13
updated: 2026-07-01
---

Reseek is a SaaS personal knowledge management platform — a cloud-hosted "second brain" — that lets users save any digital content (links, notes, images, PDFs, YouTube videos, Twitter/X posts) into a single searchable library. It applies OCR, automatic tagging, semantic AI search, and AI chat on top of everything saved, and exposes the library to external tools and AI agents through a REST API and an MCP Server.

_All claims below are sourced from ../../raw/web/reseek.net.md unless otherwise noted._

## What it does

Reseek captures heterogeneous digital content — web links (title, description, preview image, author, publish date auto-filled), plain text and markdown notes, images (OCR extracts embedded text), PDFs (page-by-page text extraction with page count and word count), YouTube videos (title, description, thumbnail, chapters, hashtags), and Twitter/X posts (post text, engagement counts, attached image OCR) — and stores everything in a unified, semantically searchable library. Users can filter by content type, date range, and tags; switch between grid and list views; and chat with their saved content via an AI assistant that surfaces connections and summaries across the whole library.

## Key features

- **Multi-format capture** — saves links, notes, images, PDFs, YouTube, and Twitter/X posts; metadata auto-filled from each source type
- **OCR** — extracts text from images, screenshots, receipts, and images attached to X posts, making visual content fully searchable
- **PDF processing** — page-by-page text extraction; file metadata (page count, word count) stored alongside content
- **Automatic tagging** — AI-generated tags applied at save time; users can override or add their own
- **Semantic search** — natural-language queries understood by meaning, not keyword match; smart highlighting shows why a result was surfaced
- **AI chat** — interactive Q&A across the entire library; surfaces forgotten content and cross-item connections
- **Smart filtering** — filter by content type, date range, custom criteria; grid and list views; ranking by relevance
- **PWA** — installable on macOS, Windows, Linux, iPhone, iPadOS, and Android; home-screen and desktop launcher support
- **API** — REST API with personal access tokens for programmatic save, search, and fetch
- **MCP Server** — Model Context Protocol tools (`search-library`, `get-library-item`, `save-note`, `save-link`) for AI agents and external clients

## Architecture and concepts

Reseek is a cloud SaaS product (no self-hosted option mentioned). The library is the central data model: every saved item is a typed document (link, note, image, PDF, YouTube, X post) with extracted text, metadata, and AI-generated tags. Semantic search is powered by an embedding model that indexes extracted text and metadata for meaning-based retrieval. The AI chat layer sits atop the same index, answering questions by retrieving and synthesizing relevant items.

The MCP Server exposes a user-scoped API using authenticated personal access tokens — the same credential system as the REST API — making Reseek usable as a structured knowledge backend for LLM clients (Claude, OpenAI-compatible agents, custom MCP hosts). The four MCP tools cover read (`search-library`, `get-library-item`) and write (`save-note`, `save-link`) operations.

The PWA layer wraps the web app in an installable shell with no separate native codebase.

## Main APIs

- **REST API** — personal access token authentication; supports programmatic item save, library search, and item fetch; suitable for automations, scripts, and integrations
- **MCP Server** — four tools available to MCP-compatible AI clients:
  - `search-library` — semantic search across all saved items
  - `get-library-item` — fetch a specific saved item by ID
  - `save-note` — create a new text or markdown note
  - `save-link` — save a URL and trigger auto-metadata fetch

## When to use

Reseek fits workflows where a knowledge worker or AI agent needs a centralized, AI-queryable store of mixed-format content — web research, video summaries, image captures, and documents — without building a custom retrieval system. The MCP Server makes it directly pluggable into LLM workflows: an agent can save research items during a session and retrieve them semantically in a later session. Compared to [[runcabinet.com]] (self-hosted, developer-oriented, markdown-on-disk), Reseek is a hosted SaaS product aimed at individuals and knowledge workers who prefer managed infrastructure and a consumer-grade UI. Compared to [[meetclaras.com]], which is YouTube-specific, Reseek is multi-format and includes an API/MCP layer for programmatic access.

## Ecosystem

Reseek targets researchers, business professionals, lifelong learners, entrepreneurs, content creators, and digital minimalists. Pricing is $9/month or $99/year with all features (AI search, chat, OCR, PDF processing, automatic tagging) included in both plans. No open-source repository was found. The MCP Server and API position it as a knowledge-layer component in agentic AI stacks rather than a pure consumer note-taking app.
