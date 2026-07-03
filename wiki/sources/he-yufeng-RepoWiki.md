---
type: source
source_url: https://github.com/he-yufeng/RepoWiki
tags:
  - deepwiki-alternative
  - local-repos
  - cli
  - repowiki
  - pagerank
  - litellm
related:
  - deepwiki.com
  - AsyncFuncAI-deepwiki-open
  - langchain-ai-openwiki
  - bb-boy680-open-zread
product: repowiki
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`he-yufeng/RepoWiki` is a lightweight, MIT-licensed **open-source DeepWiki alternative** that generates structured wiki documentation from **local directories or GitHub URLs** using only Python + SQLite — no Docker required. Its README explicitly positions it against [[deepwiki.com]] (SaaS-only) and [[AsyncFuncAI-deepwiki-open]] (Docker, no local-folder path): RepoWiki adds `pip install repowiki`, `repowiki scan ./my-project`, terminal Q&A via `repowiki chat`, and PageRank-based "start here" reading guides.

_All claims below are sourced from ../../raw/github/he-yufeng-RepoWiki.md unless otherwise noted._

## What it does

RepoWiki scans a codebase (respecting `.gitignore` and `.repowikiignore`, skipping `.env` and key files by default), runs a multi-pass LLM analysis pipeline (overview, modules, architecture, reading guide), and outputs Markdown, JSON, or self-contained HTML wikis with Mermaid diagrams. Optional web UI (`repowiki serve`) and grounded terminal chat use built-in TF-IDF retrieval — no embedding service required.

## Installation

```bash
pip install repowiki
export DEEPSEEK_API_KEY=<key>   # or OPENAI_API_KEY, etc.
repowiki scan ./my-project
```

Web UI: `pip install repowiki[web]` then `repowiki serve`.

## Key features

- **Local private repos** — `repowiki scan ./my-project` works on disk without publishing to GitHub.
- **CLI-first** — `scan`, `serve`, `chat`, `config` commands; no database server.
- **PageRank reading guide** — import-aware dependency graph ranks files before LLM context selection.
- **Three export formats** — Markdown directory, JSON, or standalone HTML (`--format html --open`).
- **100+ LLM providers** — via LiteLLM (`repowiki config set model deepseek` / `gpt` / `claude` / etc.).
- **30+ languages detected** — Python, JS/TS, Go, Rust, Java, and more.

## Architecture

Python package under `src/repowiki/`: `scanner.py` (language detection), `analyzer.py` (LLM passes), `graph.py` (dependency + PageRank), `wiki_builder.py`, `rag.py` (TF-IDF Q&A), `cache.py` (SQLite content-hash cache). LLM layer wraps LiteLLM async client with structured prompts.

## Example usage

```bash
repowiki scan .                    # generate wiki
repowiki scan . -f html --open     # browser view
repowiki scan . -l zh              # Chinese output
repowiki chat .                    # terminal Q&A
repowiki scan https://github.com/pallets/flask
```

## Maintenance status

207 stars, MIT, PyPI package `repowiki` v0.1.0, active development (pushed 2026-07-01). Best OSS pick when the requirement is **private local folders** with minimal ops overhead — simpler than [[AsyncFuncAI-deepwiki-open]] or [[AIDotNet-OpenDeepWiki]], more repo-focused than general wikis like [[6eanut-llm-wiki]].
