---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/bb-boy680/open-zread
tags:
  - wiki-generator
  - zread
  - tree-sitter
  - mermaid
  - incremental-sync
  - multi-agent
related:
  - deepwiki.com
  - he-yufeng-RepoWiki
  - langchain-ai-openwiki
  - AsyncFuncAI-deepwiki-open
product: open-zread
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`bb-boy680/open-zread` is an MIT-licensed, TypeScript CLI that turns any local codebase into a structured `Wiki/` folder with Mermaid diagrams — positioned as the open-source successor to zread.ai and an alternative to [[deepwiki.com]] for **local, private** repos. It uses web-tree-sitter AST parsing (14 languages), a three-layer repo map for token-efficient analysis, parallel page agents with 32 built-in tools, symbol-level incremental cache, and diff-aware wiki sync so re-runs after code changes only regenerate affected pages.

_All claims below are sourced from ../../raw/github/bb-boy680-open-zread.md unless otherwise noted._

## What it does

Run `open-zread` in a project root: configure an LLM provider in the TUI, generate documentation into `Wiki/`, then browse via `open-zread browse` (local Vite React reader at `http://localhost:5173`) or commit the wiki to the repo. Subsequent `sync` runs tag pages `new`, `updated`, `unchanged`, or `archived` based on which source symbols changed — avoiding full regeneration cost.

## Installation

```bash
npm i -g @open-zread/cli
cd /path/to/your/repo
open-zread
```

Requires Node.js 18+; Bun 1.3+ also supported.

## Key features

- **Fully local** — code stays on your machine; only your chosen LLM endpoint receives prompts.
- **75+ LLM providers** — Anthropic, OpenAI, Google, DeepSeek, Moonshot, Qwen, Groq, etc. via unified provider abstraction.
- **Symbol-level incremental cache** — AST-hash skips unchanged symbols across runs.
- **Multi-agent page generation** — configurable parallel agents, each owning one wiki page.
- **MCP-ready runtime** — connect external MCP servers; ships skills (`commit`, `debug`, `review`, `simplify`, `test`).
- **Cost meter** — per-token pricing estimates during generation.
- **Bilingual TUI** — Chinese/English UI; independent wiki output language.

## Architecture

TypeScript CLI with in-process Agent SDK (Bash, Read, Write, Edit, Glob, Grep, WebFetch, Task, MCP, LSP, Worktree, etc.), `p-limit` parallel scheduling, web-tree-sitter for 14 languages, local web reader via Vite + React + Mermaid.

## Example usage

```bash
open-zread              # TUI: generate wiki
open-zread browse       # local web reader
open-zread config       # providers, models, concurrency
open-zread wiki         # explicit wiki entry
```

Typical cost: full generation on ~30k LOC TypeScript under ~$0.20 with DeepSeek V3; sync runs often under $0.05.

## Maintenance status

23 stars (early stage), MIT, npm `@open-zread/cli` v1.2.0, pushed 2026-06-22. Lower adoption than [[AsyncFuncAI-deepwiki-open]] but strong feature set for **incremental local wiki maintenance** — pairs well with [[he-yufeng-RepoWiki]] for teams wanting committed `Wiki/` artifacts in-repo rather than a hosted browser experience.
