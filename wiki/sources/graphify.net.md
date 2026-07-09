---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://graphify.net/
companion_urls:
  - https://github.com/safishamsi/graphify
raw_files:
  - ../../raw/web/graphify.net.md
  - ../../raw/github/safishamsi-graphify.md
tags:
  - knowledge-graph
  - code-understanding
  - tree-sitter
  - ast-extraction
  - leiden-community-detection
  - ai-coding-assistant
  - claude-code-skill
  - token-reduction
related:
  - skills.sh
  - anthropics-skills
  - HKUDS-RAG-Anything
product: graphify
detail_level: standard
created: 2026-06-09
updated: 2026-07-01
---

Graphify is an open-source knowledge graph skill for AI coding assistants that turns an entire codebase — source code, documentation, research papers, and diagrams — into a queryable graph, replacing naive file-search with structured traversal and delivering a reported 71.5× token reduction on a 52-file corpus (~1.7k tokens vs ~123k raw). Built on Tree-sitter AST extraction, NetworkX, and Leiden community detection, it requires no embeddings, no vector store, and no server, and integrates natively with over 24 AI coding platforms including Claude Code, Codex, Cursor, Gemini CLI, and GitHub Copilot CLI. With 63,000+ GitHub stars and YC S26 backing, Graphify is one of the most widely adopted graph-based context layers in the AI coding assistant ecosystem.

_All claims below are sourced from ../../raw/web/graphify.net.md unless otherwise noted._

## What it does

Running `/graphify .` in any AI coding assistant produces three outputs: an interactive HTML graph (`graphify-out/graph.html`) navigable in any browser, a `GRAPH_REPORT.md` audit highlighting god nodes, surprising cross-file connections, and suggested questions, and a persistent `graph.json` that can be queried at any time without re-reading source files. The graph ingests code, Markdown, PDFs, images, videos, and external URLs (papers, tweets), and tags every relationship as `EXTRACTED` (explicit, confidence 1.0), `INFERRED` (reasoned, with a score), or `AMBIGUOUS` (flagged for human review).

## Key features

- **71.5× token reduction** — average cost on a 52-file mixed corpus drops from ~123k raw tokens to ~1.7k via structured graph traversal.
- **Multi-modal extraction** — code (28 tree-sitter grammars), Markdown/HTML/YAML, PDFs, images, video/audio transcription, and live PostgreSQL schema introspection.
- **Provenance tagging** — every edge carries a confidence label (`EXTRACTED`, `INFERRED`, `AMBIGUOUS`) so AI assistants know what was found vs guessed.
- **Leiden community detection** — clusters the graph using graph topology alone (no embeddings), via the `graspologic` library; `semantically_similar_to` edges from the LLM pass co-exist with structural edges for conceptual affinity. (../../raw/github/safishamsi-graphify.md)
- **God nodes** — identifies the highest-degree nodes (most-connected concepts) as the structural load-bearing points of the codebase.
- **Incremental updates** — SHA256 cache; re-extract only changed files with `--update`; auto-rebuild via git post-commit hook.
- **MCP server** — exposes graph over MCP stdio or HTTP for structured tool access (`query_graph`, `get_node`, `get_neighbors`, `shortest_path`, PR tools).
- **PR dashboard** — `graphify prs` shows CI state, review status, worktree mapping, merge-order conflict risk, and AI triage ranking.

## Architecture

Graphify is a Claude Code skill backed by a Python library. The skill orchestrates the library; the library can be used standalone via `graphify extract`. (../../raw/github/safishamsi-graphify.md)

The extraction pipeline is a strict linear stage sequence: (../../raw/github/safishamsi-graphify.md)
```
detect()  →  extract()  →  build_graph()  →  cluster()  →  analyze()  →  report()  →  export()
```

Each stage is a single function in its own module, communicating through plain Python dicts and NetworkX graphs — no shared state, no side effects outside `graphify-out/`. Key modules: `detect.py` (file collection), `extract.py` (tree-sitter AST + LLM semantic pass), `build.py` (NetworkX graph assembly), `cluster.py` (Leiden clustering), `analyze.py` (god nodes, surprises, questions), `report.py` (GRAPH_REPORT.md rendering), `export.py` (HTML, JSON, Obsidian, SVG, GraphML, Neo4j Cypher). (../../raw/github/safishamsi-graphify.md)

Code extraction is always local (tree-sitter, no API calls); docs/PDFs/images/videos are sent to the configured AI model API for semantic extraction. Source code never leaves the machine during the AST pass. (../../raw/github/safishamsi-graphify.md)

## Installation

```bash
uv tool install graphifyy    # recommended — puts graphify on PATH
graphify install              # register skill with AI assistant
graphify claude install       # CLAUDE.md + PreToolUse hook (project-scoped)
```

The PyPI package name is `graphifyy` (double-y); the CLI is `graphify`. Requires Python 3.10+. (../../raw/github/safishamsi-graphify.md)

Platform-specific optional extras: `pdf`, `office`, `video`, `mcp`, `neo4j`, `leiden` (Python < 3.13), `sql`, `postgres`, `terraform`, `ollama`, `openai`, `gemini`, `anthropic`, `bedrock`, `azure`, `all`. (../../raw/github/safishamsi-graphify.md)

## Example usage

```bash
/graphify .                           # build graph for current folder
/graphify ./docs --update             # re-extract only changed files
/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"
/graphify add https://arxiv.org/abs/1706.03762   # ingest a paper
graphify export callflow-html          # Mermaid architecture HTML
graphify hook install                  # auto-rebuild on git commit
graphify prs                           # PR dashboard
python -m graphify.serve graphify-out/graph.json  # MCP stdio server
```

Always-on integration writes platform-native config so the graph is consulted before every file-search or code-read operation: (../../raw/github/safishamsi-graphify.md)
```bash
graphify claude install     # CLAUDE.md + PreToolUse hook (Claude Code)
graphify codex install      # AGENTS.md + .codex/hooks.json hook (Codex)
graphify cursor install     # .cursor/rules/graphify.mdc (Cursor)
graphify gemini install     # GEMINI.md + BeforeTool hook (Gemini CLI)
```

## When to use

Graphify is most valuable when an AI coding assistant is spending many tokens re-reading source files to answer structural or cross-file questions. It is particularly effective for: large repositories where raw file content exceeds context windows; onboarding to unfamiliar codebases; dependency and impact analysis; architecture documentation generation; and CI workflows where headless `graphify extract` can pre-build the graph without IDE involvement.

## Maintenance status

63,681 stars; 6,504 forks; YC S26 backed; latest release v0.8.36 (2026-06-08); actively maintained on the `v8` branch with frequent releases. MIT license. (../../raw/github/safishamsi-graphify.md)

Built-on product: [Penpax](https://graphifylabs.ai) applies the same graph approach to the user's entire working life (meetings, browser history, emails, files, code) as an always-on, fully on-device layer. (../../raw/github/safishamsi-graphify.md)

## Ecosystem

Graphify integrates with 24+ AI coding platforms. It competes positionally with Sourcegraph (enterprise code search, no graph model), Code2Vec (vector embeddings, no structure), and Neo4j (graph database, but requires a separate extractor). Unlike those tools, Graphify is both the extractor and the graph, runs fully locally, and is purpose-built for AI assistant context injection.

The MCP server (`graphify[mcp]`) allows any MCP-capable client to query the graph. The `global` graph feature merges graphs across multiple repos into `~/.graphify/global.json` for cross-project queries. Team-friendly: `graphify-out/` can be committed to git; a built-in git merge driver auto-union-merges `graph.json` on concurrent commits.

Companion GitHub repo: [safishamsi/graphify](https://github.com/safishamsi/graphify) (63k+ stars, Python, MIT, default branch `v8`).
