# Houseofmvps/codesight

## Metadata
- Stars: 1230
- Primary language: TypeScript
- Default branch: main
- Latest release: (none published)
- License: MIT License
- Homepage: https://github.com/Houseofmvps/codesight
- Fetched: 2026-07-16
- Final URL: https://github.com/Houseofmvps/codesight

## Description
Universal AI context generator. Saves thousands of tokens per conversation in Claude Code, Cursor, Copilot, Codex, and more.

## README

<div align="center">

### Your AI assistant wastes thousands of tokens every conversation just figuring out your project. codesight fixes that in one command.

**4,000+ downloads and counting.**

**Zero dependencies. AST precision. 30+ framework detectors. 14 ORM parsers. 14 MCP tools. One `npx` call.**

**Works with TypeScript, JavaScript, Python, Go, Ruby, Elixir, Java, Kotlin, Rust, PHP, Dart, Swift, C#, and BrightScript/BrighterScript (Roku).** TypeScript projects get full AST precision. Everything else uses battle-tested regex detection across the same 30+ frameworks.

**Built by [Kailesk Khumar](https://www.linkedin.com/in/kailesk-khumar), founder of [HouseofMVPs](https://houseofmvps.com) and [Kailxlabs](https://www.kailxlabs.co)**

*Also: [ultraship](https://github.com/Houseofmvps/ultraship) (39 expert skills for Claude Code) · [claude-rank](https://github.com/Houseofmvps/claude-rank) (SEO/GEO/AEO plugin for Claude Code)*

</div>

```
0 dependencies · Node.js >= 18 · 145 tests · 14 MCP tools · MIT · tested on 25+ OSS projects across 14 languages
```

## Works With

**Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Windsurf, Cline, Aider**, and anything that reads markdown.

## Install

```bash
npx codesight
```

That's it. Run it in any project root. No config, no setup, no API keys.

```bash
npx codesight --wiki                       # Generate wiki knowledge base (.codesight/wiki/)
npx codesight --init                       # Generate CLAUDE.md, .cursorrules, codex.md, AGENTS.md
npx codesight --open                       # Open interactive HTML report in browser
npx codesight --mcp                        # Start as MCP server (14 tools) for Claude Code / Cursor
npx codesight --blast src/lib/db.ts        # Show blast radius for a file
npx codesight --profile claude-code        # Generate optimized config for a specific AI tool
npx codesight --benchmark                  # Show detailed token savings breakdown
npx codesight --native-ast                 # Opt-in: AST plugins for more languages (see docs/wasm-plugins.md)
npx codesight --mode knowledge             # Map knowledge base (.md notes → KNOWLEDGE.md)
npx codesight --mode knowledge ~/vault     # Map Obsidian vault, ADRs, meeting notes, retros
```

## Wiki Knowledge Base (v1.6.2)

Inspired by [Karpathy's LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — but compiled from AST, not an LLM. Zero API calls. 200ms.

```bash
npx codesight --wiki
```

Generates `.codesight/wiki/` — a persistent knowledge base of your codebase that survives across every session:

```
.codesight/wiki/
  index.md      — catalog of all articles (~200 tokens) — read this at session start
  overview.md   — architecture, subsystems, high-impact files (~500 tokens)
  auth.md       — auth routes, middleware, session flow
  payments.md   — payment routes, webhook handling, billing flow
  database.md   — all models, fields, relations, high-impact DB files
  users.md      — user management routes and related models
  ui.md         — UI components with props
  log.md        — append-only record of every wiki operation
```

**Why this cuts token usage further:**

Instead of loading the full 5K token context map every conversation, your AI reads one targeted article:

| Question              | Without wiki                 | With wiki                   |
|-----------------------|------------------------------|-----------------------------|
| "How does auth work?" | ~12K tokens (reads 8+ files) | ~300 tokens (`auth.md`)     |
| "What models exist?"  | ~5K tokens (CODESIGHT.md)    | ~400 tokens (`database.md`) |
| New session start     | ~5K tokens (full reload)     | ~200 tokens (`index.md`)    |

**Persistent across sessions.** The wiki lives in `.codesight/wiki/`, committed to git. Every new Claude Code, Cursor, or Codex session starts with full codebase knowledge from the first message.

**Auto-regenerates.** Use `--watch` to keep the wiki current as you code. Use `--hook` to regenerate on every commit.

**3 new MCP tools** for wiki access:

| Tool                         | What it does                                                      |
|------------------------------|---------------------------------------------------------------------|
| `codesight_get_wiki_index`   | Get the wiki catalog (~200 tokens) at session start               |
| `codesight_get_wiki_article` | Read one article by name: `auth`, `database`, `payments`, etc.    |
| `codesight_lint_wiki`        | Health check: orphan articles, missing cross-links, stale content |

The key difference from general-purpose wiki tools: codesight already knows your routes, schema, blast radius, and middleware from AST — no LLM needed to extract code structure. The wiki is a narrative layer on top of data your codebase already contains.

## Knowledge Mode (v1.9.3)

Not just code — your decisions, meeting notes, ADRs, and retrospectives carry as much context as the codebase itself. `--mode knowledge` maps them the same way codesight maps code.

```bash
npx codesight --mode knowledge              # Scan current directory for .md files
npx codesight --mode knowledge ~/vault      # Scan an Obsidian vault
npx codesight --mode knowledge ./docs       # Scan a project docs folder
```

Outputs `.codesight/KNOWLEDGE.md` — a compact AI context primer with Key Decisions, Open Questions, and a Note Index (Decision Records, Meeting Notes, Retrospectives, Specs & PRDs, Research).

**What it detects automatically:**

| Note type        | Signals                                                                  |
|------------------|--------------------------------------------------------------------------|
| Decision records | ADR format (`## Decision`), "decided to", "going with", "chose X over Y" |
| Meeting notes    | `Attendees:`, `Action items:`, filename: `standup`, `sync`, `1on1`       |
| Retrospectives   | "What went well", "Stop doing", filename: `retro`, `retrospective`       |
| Specs / PRDs     | `## Goals`, `## Requirements`, filename: `prd`, `spec`, `roadmap`        |
| Research         | filename: `research`, `analysis`, `benchmark`, `comparison`              |
| Session logs     | filename: `session`, `daily`, `weekly`                                   |

**Supports:** Obsidian vaults (YAML frontmatter, `[[backlinks]]`, `#tags`), Notion exports, ADR tooling (`adr-tools`, `Log4brains`, raw markdown), any folder of markdown files.

## Benchmarks (Real Projects)

Every number comes from running codesight on real production codebases — small SaaS projects (v1.6.2) and large open-source platforms with 4K–10K+ files (v1.6.4).

### Three-Level Token Reduction

| Project    | Manual exploration | codesight scan       | codesight --wiki (targeted) | **Total reduction** |
|------------|--------------------|----------------------|-----------------------------|---------------------|
| **SaaS A** | 46,020 tokens      | 3,936 tokens (11.7x) | ~550 tokens                 | **83.7x**           |
| **SaaS B** | 26,130 tokens      | 3,629 tokens (7.2x)  | ~440 tokens                 | **59.4x**           |
| **SaaS C** | 47,450 tokens      | 4,162 tokens (11.4x) | ~360 tokens                 | **131.8x**          |

**Average combined reduction: 91x.**

**Layer 1 — codesight scan** eliminates manual file exploration (glob/grep/read across 40-138 files) by reading one pre-compiled map. **Layer 2 — `--wiki`** eliminates loading the full map for every question by reading a 200-token index plus one relevant article per question.

### Multi-Language OSS Benchmark (v1.6.7)

Tested against real open-source codebases spanning every supported language and framework (Next.js+tRPC+Prisma, NestJS, Hono, Remix, SvelteKit, Nuxt, Express, Rails, Laravel, Django, Flask, FastAPI, Phoenix, Gin, Echo, Fiber, Actix, Axum, ASP.NET Core, Spring Boot, SwiftUI, Vapor, Flutter). Reported savings range roughly 7x–41x depending on stack; zero false positives across all tests.

### Detection Accuracy

| Project    | Route Recall | Schema Recall | False Positives | Detection Method                          |
|------------|--------------|---------------|-----------------|-------------------------------------------|
| **SaaS A** | 38/43 (88%)  | 12/12 (100%)  | 0               | Schema: AST (Drizzle), Routes: AST (Hono) |
| **SaaS B** | 17/17 (100%) | 8/8 (100%)    | 0               | Full AST (Hono + Drizzle + React)         |
| **SaaS C** | 56/59 (~95%) | 0/0 (correct) | 0               | AST (FastAPI + MongoDB)                   |

### Blast Radius Accuracy

Tested on a production SaaS: changing the database module correctly identified 5 affected files across API/auth/server layers, all routes touching the database, 12 affected models, at BFS depth 3 hops through the import graph.

## How It Works

codesight runs 8 parallel detectors (Routes, Schema, Components, Dep Graph, Middleware, Config, Libraries, Contracts), then writes the results as structured markdown designed to be read by an AI in a single file load.

## What It Generates

```
.codesight/
  CODESIGHT.md     Combined context map (one file, full project understanding)
  routes.md        Every API route with method, path, params, and what it touches
  schema.md        Every database model with fields, types, keys, and relations
  components.md    Every UI component with its props
  libs.md          Every library export with function signatures
  config.md        Every env var (required vs default), config files, key deps
  middleware.md    Auth, rate limiting, CORS, validation, logging, error handlers
  graph.md         Which files import what and which break the most things if changed
  cicd.md          GitHub Actions / CircleCI pipelines (when present)
  githooks.md      lefthook / husky / raw .git/hooks (when present)
  skills.md        .claude/commands + .claude/skills (when present)
  report.html      Interactive visual dashboard (with --html or --open)
```

The last three come from **built-in plugins** that scan dotfile directories (`.github/`, `.husky/`, `.claude/`) the main pass skips. They run automatically and stay silent on projects without those files.

## AST Precision

When TypeScript is installed in the project being scanned, codesight uses the actual TypeScript compiler API to parse code structurally instead of regex guessing (follows `router.use()` chains, combines NestJS decorators, parses tRPC nesting, extracts Drizzle field types, gets React props from interfaces, detects middleware in route chains, filters non-route calls). No configuration needed — kicks in automatically if TypeScript is in `node_modules`; falls back to regex otherwise.

**AST-supported frameworks:** Express, Hono, Fastify, Koa, Elysia, NestJS, tRPC, Drizzle, TypeORM, React.

### Native-AST WASM plugins (opt-in)

By default codesight uses built-in extractors (AST for TypeScript, regex for everything else). `--native-ast` opts in to **WebAssembly plugins** for full-AST precision on non-TypeScript source files:

```bash
npx codesight --native-ast                 # use every discovered plugin (additive)
npx codesight --native-ast=rust,go         # only these languages (authoritative for their files)
npx codesight --native-ast=none            # force off (overrides config)
npx codesight --native-ast-strict          # like --native-ast, but fail if a named plugin is missing
npx codesight --plugin-dir ./wasm          # extra directory to search for plugins
```

Dispatch is **language-driven**: each plugin self-describes (via a `describe()` export) the file extensions it handles, so any language works, not just built-in ones. codesight ships no plugins itself — prebuilt reference plugins (Rust/`syn`, Python/`ruff`, Go/`go/parser`) are published as checksummed GitHub release assets, dropped into `~/.codesight/plugins/` (or `--plugin-dir`), then enabled with `--native-ast`. Full contract: `docs/wasm-plugins.md`.

## Built-in plugins

| Plugin     | Reads                                  | Output                                                 |
|------------|-----------------------------------------|--------------------------------------------------------|
| `cicd`     | `.github/workflows/`, `.circleci/`     | Pipeline triggers, jobs, secrets, deploy targets       |
| `githooks` | lefthook / husky config, `.git/hooks/` | Which commands run on which git lifecycle              |
| `skills`   | `.claude/commands/`, `.claude/skills/` | Available slash commands / agent skills + descriptions |

Opt out per project via `codesight.config.js` → `disableDetectors: [...]`.

**Terraform is opt-in**, not auto-loaded (it reaches outside the scanned directory to sibling `../infrastructure` repos):

```js
// codesight.config.js
import {createTerraformPlugin} from "codesight/plugins/terraform";
export default {plugins: [createTerraformPlugin({infraPath: "../infra"})]};
```

## Routes / Schema / Dependency Graph / Blast Radius / Environment Audit

- **Routes:** methods, URL parameters, what each route touches (auth, database, cache, payments, AI, email, queues), handler location. 30+ frameworks auto-detected.
- **Schema:** models, fields, types, primary/foreign keys, unique constraints, relations — parsed directly from ORM definitions via AST.
- **Dependency Graph:** most-imported files flagged as highest blast radius.
- **Blast Radius:** `npx codesight --blast src/lib/db.ts` — BFS through the import graph finds all transitively affected files, routes, and models. Also queryable via MCP before making changes.
- **Environment Audit:** every env var, flagged required vs has-default, with the exact file where referenced.

## Token Benchmark

```bash
npx codesight --benchmark
```

Breaks down savings per detector type (routes ~400 tokens each, schema models ~300, components ~250, library exports ~200, env vars ~100, files scanned ~80), times a 1.3x revisit multiplier. A developer manually verified Claude Code spends 40-70K tokens exploring the same projects codesight summarizes in 3-5K tokens.

## Roku / BrightScript / SceneGraph

codesight treats Roku channels as first-class projects, anchored on the `manifest` file at the channel root. Supports both the standard single-channel layout and a multi-channel monorepo layout (detected via `roku-deploy` in deps + a `common/` directory with ≥2 sibling per-channel directories, each with their own `manifest`).

Mappings: Routes → Screens (Scene XML `<children>` elements, `VIEW`/`MODAL`); Schema → SceneGraph component `<interface>` fields; Components → `<component>` XML; Libraries → `.brs`/`.bs` files; Middleware → `observeField`/`m.global.AddField`; Dependencies → `<script uri="pkg:/...">` / BrighterScript `import`; Events → observed fields, Rudderstack; Config → manifest key/value lines as `manifest.<name>` pseudo env-vars.

Custom navigation helpers (`ShowScreen`, `pushScreen`, etc.) configurable via `rokuScreenHelpers` in codesight config.

## Supported Stacks

- **Routes:** Hono, Express, Fastify, Next.js (App + Pages), Koa, NestJS, tRPC, Elysia, AdonisJS, SvelteKit, Remix, Nuxt, FastAPI, Flask, Django, Go (net/http, Gin, Fiber, Echo, Chi), Rails, Phoenix, Spring Boot, Ktor, Actix, Axum, Laravel, ASP.NET Core, Vapor, Flutter (go_router), Roku SceneGraph, raw http.createServer
- **Events:** BullMQ, Celery, Kafka, Redis pub/sub, Socket.io, EventEmitter, SceneGraph observers, Rudderstack
- **Schema:** Drizzle, Prisma, TypeORM, Mongoose, Sequelize, SQLAlchemy, Django ORM, ActiveRecord, Ecto, Eloquent, Entity Framework, Exposed, Room, SceneGraph `<interface>` (14 ORMs)
- **Components:** React, Vue, Svelte, Flutter widgets, SwiftUI views (auto-filters shadcn/ui and Radix primitives), Roku SceneGraph components
- **Libraries:** TypeScript, JavaScript, Python, Go, Dart, Swift, C#, PHP, BrightScript, BrighterScript
- **Middleware:** Auth, rate limiting, CORS, validation, logging, error handlers, SceneGraph observers + `m.global` fields
- **Monorepos:** pnpm, npm, yarn workspaces + mixed-language workspaces
- **Languages:** TypeScript, JavaScript, Python, Go, Ruby, Elixir, Java, Kotlin, Rust, PHP, Dart, Swift, C#, BrightScript/BrighterScript

## AI Config Generation

```bash
npx codesight --init
```

Generates ready-to-use instruction files for major AI coding tools at once: `CLAUDE.md` (Claude Code), `.cursorrules` (Cursor), `.github/copilot-instructions.md` (GitHub Copilot), `codex.md` (OpenAI Codex CLI), `AGENTS.md` (OpenAI Codex agents). Each is pre-filled with the project's stack, architecture, high-impact files, and required env vars.

## MCP Server (14 Tools)

```bash
npx codesight --mcp
```

Runs as a Model Context Protocol server; Claude Code and Cursor call it directly to get project context on demand.

```json
{
  "mcpServers": {
    "codesight": {
      "command": "npx",
      "args": ["codesight", "--mcp"]
    }
  }
}
```

**OpenAI Codex CLI** (`~/.codex/config.toml`):
```toml
[mcp_servers.codesight]
command = "npx"
args = ["codesight", "--mcp"]
startup_timeout_sec = 60
```
`npx` resolving the package on first run can exceed the default 30s timeout — set `startup_timeout_sec = 60` or install globally and use `command = "codesight"`.

| Tool                         | What it does                                                                              |
|------------------------------|---------------------------------------------------------------------------------------------|
| `codesight_get_wiki_index`   | Wiki catalog (~200 tokens) — read at session start                                        |
| `codesight_get_wiki_article` | Read one wiki article by name: `auth`, `database`, `payments`, etc.                       |
| `codesight_lint_wiki`        | Health check: orphan articles, missing cross-links                                        |
| `codesight_scan`             | Full project scan (~3K-5K tokens)                                                         |
| `codesight_get_summary`      | Compact overview (~500 tokens)                                                            |
| `codesight_get_routes`       | Routes filtered by prefix, tag, or method                                                 |
| `codesight_get_schema`       | Schema filtered by model name                                                             |
| `codesight_get_blast_radius` | Impact analysis before changing a file                                                    |
| `codesight_get_env`          | Environment variables (filter: required only)                                             |
| `codesight_get_hot_files`    | Most imported files with configurable limit                                               |
| `codesight_get_events`       | Background events: BullMQ queues, Celery tasks, Kafka topics, Redis pub/sub, EventEmitter |
| `codesight_get_coverage`     | Test coverage map: which routes and models have test files                                |
| `codesight_get_knowledge`    | Knowledge map from `--mode knowledge`: decisions, open questions, themes, note index      |
| `codesight_refresh`          | Force re-scan (results are cached per session)                                            |

Session caching means the first call scans, subsequent calls return instantly.

## AI Tool Profiles

```bash
npx codesight --profile claude-code
npx codesight --profile cursor
npx codesight --profile codex
npx codesight --profile copilot
npx codesight --profile windsurf
```

Generates an optimized config file for a specific AI tool, pre-filled with project summary, stack info, high-impact files, required env vars, and tool-specific usage instructions.

## Visual Report

```bash
npx codesight --open
```

Interactive HTML dashboard: routes table with method badges/tags, schema cards, dependency hot files with impact bars, env var audit, token savings breakdown.

## GitHub Action

```yaml
name: codesight
on: [ push ]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install -g codesight && codesight
      - uses: actions/upload-artifact@v4
        with:
          name: codesight
          path: .codesight/
```

## Watch Mode and Git Hook

`npx codesight --watch` re-scans automatically on source/config file changes (`.ts`, `.js`, `.py`, `.go`, `.prisma`, `.env`, etc.), ignoring `node_modules` and build output. `npx codesight --hook` installs a git hook to regenerate context on every commit.

## All Options

```bash
npx codesight                              # Scan current directory
npx codesight ./my-project                 # Scan specific directory
npx codesight --wiki                       # Generate wiki knowledge base
npx codesight --init                       # Generate AI config files
npx codesight --open                       # Open visual HTML report
npx codesight --html                       # Generate HTML report without opening
npx codesight --mcp                        # Start MCP server (14 tools)
npx codesight --blast src/lib/db.ts        # Show blast radius for a file
npx codesight --profile claude-code        # Optimized config for specific tool
npx codesight --watch                      # Watch mode (add --wiki to auto-regenerate wiki)
npx codesight --wiki --watch               # Watch + auto-regenerate wiki on changes
npx codesight --hook                       # Install git pre-commit hook (includes wiki)
npx codesight --benchmark                  # Detailed token savings breakdown
npx codesight --json                       # Output as JSON
npx codesight --mode knowledge             # Map .md knowledge base → KNOWLEDGE.md
npx codesight --mode knowledge ~/vault     # Map Obsidian vault or any .md folder
npx codesight --max-tokens 50000           # Trim output to fit token budget
npx codesight --since HEAD~5               # Show routes from last 5 commits only
npx codesight -o .ai-context               # Custom output directory
npx codesight -d 5                         # Limit directory depth
```

## How It Compares

|                      | codesight                                            | File concatenation tools | AST-based tools (e.g. code-review-graph) |
|----------------------|--------------------------------------------------------|---------------------------|-------------------------------------------|
| **Parsing**          | AST (TypeScript compiler) + regex fallback           | None                     | Tree-sitter + SQLite                     |
| **Token reduction**  | 7x-12x base scan; 60-131x with targeted wiki queries | 1x (dumps everything)    | 8x reported                              |
| **Route detection**  | 30+ frameworks, auto-detected                        | None                     | Limited                                  |
| **Schema parsing**   | 14 ORMs with field types and relations               | None                     | Varies                                   |
| **Blast radius**     | BFS through import graph                             | None                     | Yes                                      |
| **AI tool profiles** | 5 tools (Claude, Cursor, Codex, Copilot, Windsurf)   | None                     | Auto-detect                              |
| **MCP tools**        | 14 specialized tools with session caching            | None                     | 22 tools                                 |
| **Setup**            | `npx codesight` (zero deps, zero config)             | Copy/paste               | `pip install` + optional deps            |
| **Dependencies**     | Zero (borrows TS from your project)                  | Varies                   | Tree-sitter, SQLite, NetworkX, etc.      |
| **Language**         | TypeScript (zero runtime deps)                       | Varies                   | Python                                   |
| **Scan time**        | 185-290ms (small), 0.9-2.8s (10K files)              | Varies                   | Under 2s reported                        |

codesight is purpose-built for giving an AI assistant enough context to be useful without wasting tokens on file exploration — structured extraction (routes, schema, components, dependencies) rather than general-purpose code graph analysis.

## Contributing

```bash
git clone https://github.com/Houseofmvps/codesight.git
cd codesight
pnpm install
pnpm dev              # Run locally
pnpm build            # Compile TypeScript
pnpm test             # Run 145 tests
```

PRs welcome. Open an issue first for large changes.

## License

MIT

## Docs

### docs/wasm-plugins.md (excerpt — full WASM plugin ABI contract)

`codesight` implements support for optional, user-supplied WebAssembly plugins that can provide AST-grade route/schema/import extraction. Currently, codesight does not ship any language-specific plugins itself; it exclusively includes support for parsing user-specified languages via user-supplied plugins. When no plugin is present (the default), `codesight` uses its built-in extractors and behaves exactly as it otherwise would.

Contents: Mental model, Discovery & naming, Enabling native parsing, The WASM ABI, Extraction kinds, JSON output shapes, Fallback & strict semantics, Plugin skeleton, Building & testing locally, Releases, Versioning.

**Mental model:** for each source file, codesight calls the matching per-kind export (`parseRoutes` / `parseSchemas`) with the file's source; the plugin returns a UTF8-encoded JSON array describing what it found. codesight maps that JSON into its domain types, stamps contextual fields it already knows (file path, framework label, route tags), tags the result `confidence: "native"`, and merges it into the scan. Contextual fields a plugin emits (`file`, `framework`, `tags`, `from`, `confidence`) are ignored — codesight always overrides them. The module is instantiated once per scan and its `parse*` functions are called many times (a long-lived "reactor", not a per-file process); compile a library, not a command.

**Discovery & naming:** plugin binaries must match `codesight-<lang>-ast.wasm` (`<lang>` ∈ `[a-z0-9_-]+`; `-ast` capability namespace reserved). The module is fully self-describing via its `describe()` export, which declares the authoritative `languageId` and file `extensions` it parses — the `<lang>` in the filename is only a discovery key/fallback id. Built-in language ids (`rust`/`go`/`python`) get a default extension map (`.rs`/`.go`/`.py`) when `describe()` is omitted; any other language must declare `extensions` to be routed.

## Top-level structure

- `.codesight/` — codesight's own self-scan output (dogfooding)
- `.github/` — CI workflows (not fetched in detail)
- `assets/` — README images (token-comparison, how-it-works, detectors, ast-precision, blast-radius, mcp-server diagrams)
- `docs/` — `wasm-plugins.md` (WASM plugin ABI contract, the only docs file)
- `eval/` — `README.md` + `fixtures/` (benchmark/eval fixtures backing the README's accuracy tables)
- `plugins/ast/` — first-party AST plugin implementations
- `reference/ast-plugin/` — reference AST plugin implementation for the WASM contract
- `src/` — main TypeScript source:
  - `ast/` — TypeScript AST parsing layer
  - `detectors/` — the 8 parallel detectors (routes, schema, components, dep graph, middleware, config, libraries, contracts) across 30+ frameworks
  - `generators/` — output generators (CODESIGHT.md, wiki, AI tool profiles, HTML report)
  - `monorepo/` — workspace detection (pnpm/npm/yarn, mixed-language)
  - `plugins/ast/` — plugin loading/dispatch glue
  - `wasm/` — WASM plugin host runtime
  - `config.ts`, `core.ts`, `eval.ts`, `formatter.ts`, `index.ts`, `mcp-server.ts`, `scanner.ts`, `telemetry.ts`, `types.ts` — top-level module files
- `tests/` — 145 tests
- `package.json`, `pnpm-lock.yaml`, `tsconfig.json` — project config
- `CITATION.cff`, `LICENSE` — MIT license, citation metadata
