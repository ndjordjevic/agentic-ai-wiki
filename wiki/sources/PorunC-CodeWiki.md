---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/PorunC/CodeWiki
tags:
  - ast-analysis
  - graphrag
  - mcp-server
  - codewiki
  - source-grounded-wiki
  - litellm
related:
  - deepwiki.com
  - AIDotNet-OpenDeepWiki
  - langchain-ai-openwiki
  - he-yufeng-RepoWiki
product: codewiki
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`PorunC/CodeWiki` is a Python knowledge platform that combines **AST-based code graphs**, **GraphRAG retrieval**, DeepWiki-style wiki generation, and LiteLLM-powered Q&A — exposed through a FastAPI + React web UI, CLI, HTTP API, and **MCP server**. Unlike [[deepwiki.com]]'s hosted indexer, CodeWiki runs locally (`pip install codewiki && codewiki serve`) and includes a **Lite Mode** that builds a no-LLM graph index (`.codewiki/codewiki-lite.sqlite3`) optimized for fast symbol search, call traces, and agent MCP tools without calling an external model.

_All claims below are sourced from ../../raw/github/PorunC-CodeWiki.md unless otherwise noted._

## What it does

CodeWiki registers repositories (local path or Git URL), analyzes them into deterministic graphs (imports, definitions, calls, routes, inheritance), optionally builds GraphRAG chunk indexes with embeddings, generates source-cited wiki catalogs and pages with diagrams, and answers questions grounded in retrieved code evidence. A bundled Codex skill lets Codex CLI plan, write, validate, and export wiki pages from local CodeWiki evidence without invoking CodeWiki's own LLM wiki generator.

## Installation

```bash
pip install codewiki
codewiki serve
# open http://127.0.0.1:8000
```

Docker: `docker compose up --build`.

## Key features

- **Multi-language AST** — Python, TypeScript/TSX, JavaScript/JSX, Java, Go, Rust, C, C++, C#.
- **GraphRAG Q&A** — `codewiki ask --repo my-repo "How does the main workflow fit together?"`
- **DeepWiki-style wikis** — `codewiki wiki catalog .` / `wiki pages .` with citations, translations, incremental updates, browser export.
- **MCP server** — `codewiki mcp` plus `codewiki lite agents install` for Codex/Claude Code config.
- **Lite Mode** — project-local graph index without LLM for agent context and impact analysis.
- **Storage** — SQLite default; PostgreSQL + optional pgvector for production search.

## Architecture

Single-user platform: FastAPI backend, React frontend (packaged in PyPI wheel), LiteLLM for model routing, SQLite/PostgreSQL persistence. CLI covers `repos add`, `analyze`, `graphrag build`, `wiki catalog/pages`, `skill install codex`, `ask`, `mcp`.

## Example usage

```bash
codewiki repos add . --name my-repo
codewiki analyze .
codewiki graphrag build . --embeddings
codewiki wiki pages .
codewiki ask --repo my-repo "Where is authentication handled?"
codewiki mcp
```

## Maintenance status

163 stars, MIT, PyPI `codewiki` v0.6.3, active through 2026-06. Smaller community than [[AsyncFuncAI-deepwiki-open]] or [[AIDotNet-OpenDeepWiki]], but distinctive for **AST + GraphRAG + MCP** in one local tool — good when agents need symbol-level grounding, not just generated prose wikis.
