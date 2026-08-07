---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://markitdown.tech/
tags: []
related: []
product: markitdown
detail_level: standard
created: 2026-08-07
updated: 2026-08-07
---

# markitdown.tech

markitdown.tech is an online document-to-Markdown converter, inspired by and built on top of Microsoft's open-source `MarkItDown` library, designed specifically for AI workflows. It converts PDF, DOCX, XLSX, PPTX, HTML, images, audio, CSV, JSON, XML, and TXT files into clean, structured Markdown — the format that LLMs, RAG pipelines, vector databases, and knowledge bases ingest most reliably. The site also offers a Model Context Protocol (MCP) server integration (`/markitdown-mcp`) and a dedicated Claude Desktop workflow (`/markitdown-claude`), making it a drop-in enrichment step for agent pipelines that need documents converted before processing.

_All claims below are sourced from ../../raw/web/markitdown.tech.md unless otherwise noted._

## What it does

markitdown.tech provides a self-hosted conversion service (using Microsoft's MIT-licensed MarkItDown library under the hood) behind a web UI and an MCP server interface. Users upload a supported file and receive well-structured Markdown that preserves headings, tables, lists, links, and inline formatting — making it suitable for direct injection into LLM prompts or as a preprocessing stage for RAG chunking and search indexing.

The MCP server variant (`markitdown-mcp`) exposes a single tool contract: a client (e.g. Claude Desktop, an agent host) discovers the tool, sends a URI-based conversion request, and receives Markdown back. This narrow surface area reduces integration friction across teams and environments compared to per-application local-parser scripts.

## Key features

- **Broad format support:** PDF, Word (DOCX), Excel (XLSX), PowerPoint (PPTX), HTML, CSV, JSON, XML, TXT, images, audio, and public URLs.
- **Structure-preserving conversion:** headings, tables, lists, links, and inline formatting are faithfully retained — important for RAG chunking fidelity.
- **MCP server integration:** conforms to the Model Context Protocol so Claude Desktop, Cursor, and other MCP hosts can call it as a native tool.
- **Claude integration guide:** step-by-step workflow for paste-to-Claude or fully automated MCP-based conversion.
- **Batch processing (Pro):** up to 30 files per batch, 100MB file size limit, unlimited saved results.
- **Free tier:** basic conversions available without signup; source is deleted after conversion.
- **Multi-language UI:** English, Japanese, German, Portuguese localizations.

## When to use

- Preprocessing documents before feeding them into RAG pipelines or LLM prompts.
- Feeding PDFs, Word docs, or spreadsheets into Claude, Cursor, or other agents via the MCP server.
- Converting structured data (CSV, JSON, Excel) to Markdown tables for knowledge-base ingestion.
- Building Git-based documentation workflows where Markdown is the canonical edit format.

## Ecosystem

markitdown.tech is a third-party web service wrapping the official Microsoft `MarkItDown` open-source library (MIT). It is not affiliated with Microsoft. The underlying library is modular and extensible; this service self-hosts it. As a document-preprocessing layer it complements [[firecrawl.dev]] (web scrape/crawl to Markdown) and [[supadata.ai]] (video/social transcript to text), filling the local-file-to-Markdown gap those services don't cover.
