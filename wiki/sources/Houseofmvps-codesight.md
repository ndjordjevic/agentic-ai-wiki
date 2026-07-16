---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/Houseofmvps/codesight
tags:
  - context-map-generator
  - ast-precision
  - claude-md-generation
  - mcp-server
  - blast-radius
  - token-savings
  - karpathy-wiki-pattern
  - roku-brightscript
related:
  - nadimtuhin-claude-token-optimizer
  - langchain-ai-openwiki
  - he-yufeng-RepoWiki
  - PorunC-CodeWiki
product: codesight
detail_level: standard
created: 2026-07-16
updated: 2026-07-16
---

`codesight` is a zero-dependency `npx` CLI that scans a codebase and compiles a structured context map (`CODESIGHT.md` plus `routes.md`, `schema.md`, `components.md`, `graph.md`, and more) for AI coding assistants, using the TypeScript compiler API for AST-precision on TypeScript projects and regex fallback across 30+ frameworks and 13 other languages. Its `--wiki` mode generates a persistent, Karpathy-pattern knowledge base (`.codesight/wiki/index.md` + per-topic articles) purely from AST/regex extraction rather than an LLM pass — a deterministic, zero-API-call counterpart to LLM-driven wiki generators like [[langchain-ai-openwiki]], [[he-yufeng-RepoWiki]], and [[PorunC-CodeWiki]].

_All claims below are sourced from ../../raw/github/Houseofmvps-codesight.md unless otherwise noted._

## What it does

Run `npx codesight` in any project root and it produces `.codesight/CODESIGHT.md` — a single-file, combined context map covering routes, schema, components, library exports, config/env vars, middleware, the import dependency graph, and (via built-in plugins) CI/CD pipelines, git hooks, and Claude Code skills/commands. The goal is replacing an AI assistant's manual file exploration (glob/grep/read across dozens of files) with one pre-compiled read.

## Installation

```bash
npx codesight
```

No config, setup, or API keys required. Node.js >= 18.

## Key features

- **8 parallel detectors:** routes, schema, components, dependency graph, middleware, config, libraries, contracts — run across 30+ web frameworks (Hono, Express, NestJS, tRPC, FastAPI, Django, Rails, Phoenix, Gin, Spring Boot, Laravel, ASP.NET Core, and more) and 14 ORMs (Drizzle, Prisma, TypeORM, SQLAlchemy, ActiveRecord, Ecto, Entity Framework, etc.).
- **`--wiki`:** generates `.codesight/wiki/` — index + overview + per-topic articles (`auth.md`, `payments.md`, `database.md`, etc.), designed so an agent reads a ~200-token index plus one ~300-token targeted article instead of the full context map every session. Reported combined reduction across three benchmarked SaaS projects: 59x–132x (average ~91x) versus manual exploration.
- **`--mode knowledge`:** maps non-code knowledge (Obsidian vaults, ADRs, meeting notes, retrospectives) into `.codesight/KNOWLEDGE.md` — decision records, open questions, and a categorized note index — as a companion to the code-facing `CODESIGHT.md`.
- **`--blast <file>`:** BFS through the import graph to compute blast radius — every transitively affected file, route, and model for a proposed change, also exposed as an MCP tool so an agent can query it before editing.
- **`--init`:** generates `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`, `codex.md`, and `AGENTS.md` in one pass, each pre-filled with stack, architecture, high-impact files, and required env vars.
- **`--native-ast`:** opt-in WebAssembly plugin system for full-AST precision on non-TypeScript languages (Rust, Go, Python reference plugins ship as separate GitHub release assets); dispatch is language-driven via each plugin's self-describing `describe()` export, so any language can be supported without a built-in detector.
- **Roku/BrightScript support:** treats Roku channels as first-class projects, anchored on the `manifest` file, with both single-channel and multi-channel monorepo layout detection, and its own concept mapping (screens as routes, SceneGraph `<interface>` fields as schema).

## Architecture and concepts

Detection layers, in priority order: AST (TypeScript compiler API, when TypeScript is present) → optional native WASM plugins for other languages (`--native-ast`) → regex fallback for everything else. The WASM plugin contract (`docs/wasm-plugins.md`) specifies plugins as long-lived "reactor" modules — instantiated once per scan, called per-file via `parseRoutes`/`parseSchemas` exports returning UTF8 JSON, with codesight itself stamping contextual fields (file path, framework label, `confidence: "native"`) rather than trusting plugin-supplied context.

Three built-in plugins (`cicd`, `githooks`, `skills`) scan dotfile directories (`.github/`, `.husky/`, `.claude/`) that the main pass skips, staying silent when those files are absent; a separate opt-in Terraform plugin reaches into sibling infrastructure repos when explicitly configured.

## Main APIs

CLI flags are the primary interface: `--wiki`, `--init`, `--open` (HTML dashboard), `--mcp` (starts as an MCP server with 14 tools), `--blast <file>`, `--profile <tool>` (per-tool optimized config for Claude Code/Cursor/Codex/Copilot/Windsurf), `--benchmark`, `--watch`/`--hook` (auto-regenerate on file change or git commit), `--mode knowledge`, `--native-ast[=langs]`, `--max-tokens`, `--since <ref>`.

The MCP server exposes 14 tools with session-level scan caching, including `codesight_get_wiki_index`/`_get_wiki_article`/`_lint_wiki` for wiki access, `codesight_get_blast_radius`, `codesight_get_routes`/`_get_schema`/`_get_env`/`_get_hot_files`/`_get_events`/`_get_coverage`, and `codesight_get_knowledge` for the knowledge-mode map.

## When to use

Fits any project where an AI coding assistant repeatedly re-explores the same codebase structure across sessions — particularly larger or multi-workspace repos where manual glob/grep exploration is expensive. The `--wiki` mode specifically targets the recurring-session case (vs. one-off scans), and `--mode knowledge` extends the same "compile once, look up cheaply" idea to a team's non-code decision history. Zero dependencies and zero API calls make it low-friction to add to CI (a bundled GitHub Action re-scans on every push).

## Ecosystem

Works with Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Windsurf, Cline, and Aider. Positions itself against plain file-concatenation tools (no structure, 1x token reduction) and other AST-based code-graph tools like code-review-graph (Tree-sitter + SQLite, Python, ~8x reported) — codesight's differentiator is zero runtime dependencies plus the layered wiki/targeted-query mode on top of the base scan. From the same author/org: `ultraship` (39 expert Claude Code skills) and `claude-rank` (SEO/GEO/AEO plugin for Claude Code).

## Maintenance status

1,230 GitHub stars, 111 forks, MIT license, no formal GitHub releases published as of 2026-07-16 (versioned via README references like v1.6.2/v1.9.3). 145 tests, actively pushed (last push 2026-07-08).
