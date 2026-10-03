---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/dzhng/jevgrep
tags:
  - semantic-code-search
  - coding-agent-cli
  - tree-sitter-parsing
  - jev-model
  - agent-skill
  - swe-bench-eval
  - repository-retrieval
product: jevgrep
detail_level: standard
created: 2026-10-03
updated: 2026-10-03
related:
  - zilliztech-claude-context
---

Jevgrep (`jg`) is a TypeScript CLI that lets a coding agent ask a natural-language question about a repository and get back relevant files, reading leads, and verbatim source excerpts in one stdout response, using a model called Jev to judge relevance across folders, files, and declarations instead of plain pattern matching. It targets the "where do I start" cost of unfamiliar multi-file tasks: the agent still owns research, implementation, and testing, but `jg` removes the exploratory grep/read loop that normally precedes it.

_All claims below are sourced from ../../raw/github/dzhng-jevgrep.md unless otherwise noted._

## What it does
`jg "<question>" [path]` hierarchically traverses a repository using directory metadata and content previews rather than uploading the whole tree, keeps every file that passes a relevance bar (no fixed top-N cutoff), and reports incomplete discovery when a navigation byte budget is reached so the caller can narrow the search root. Output order is a compact file summary first, then verbatim selected source with line references, then detailed declaration and call locations — evidence for the agent to act on, not a generated answer or a completeness guarantee. `jg files [root]` previews which files a search would read (grouped by top-level directory) with no provider key or network call, and `--exclude` takes gitignore-style patterns to skip paths for one search.

## Installation
```sh
npm install -g @dzhng/jevgrep
jg auth
jg skill
```
Requires Node.js 22+ on macOS, Linux, or Windows, and a key for Vercel AI Gateway, TypeSafe, OpenRouter, OpenCode Zen, or a custom TypeSafe-compatible endpoint (provider selection requires 0.3.0+). No separate Python, Bun, or ripgrep install is needed. `jg auth --provider custom --base-url <url> --model <id> --stdin` configures a self-hosted TypeSafe-compatible gateway (must be `https://`, with `http://localhost`/`127.0.0.1` allowed for a local proxy); the saved endpoint/model becomes part of the cache identity so custom answers stay separate from preset providers. `jg doctor` verifies the saved key with synthetic input and reports the provider/endpoint host without ever printing the key.

## Key features
- **Agent skill install, separate from the CLI.** `jg skill` detects installed coding agents (Claude Code, Codex, OpenCode, others) and installs a bundled skill (`skills/jevgrep/SKILL.md`) that teaches the agent how to invoke `jg` and interpret its output; installing the CLI alone does not teach an agent to use it. The installer delegates to the [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI and can be run directly via `npx skills add dzhng/jevgrep --skill jevgrep`.
- **Multi-language declaration parsing.** Python, Go, and Rust use packaged Tree-sitter WASM grammars in a shared cancellable worker (avoiding a Python runtime dependency); TypeScript/JavaScript use the TypeScript compiler's own parser; other text falls back to bounded source chunks. Syntax-error trees and bare-CR Python also fall back to text.
- **Relationship-aware retrieval.** A relationship pass can recover implementations of the same class contract across platforms/files; source relevance and scope are judged separately, and contextual follow-up can retract earlier selections when later evidence rejects them — but a failed judgment never erases prior evidence.
- **Local filtering, no local report files.** Default filesystem filtering respects ignore files and excludes hidden, dependency/build, binary, and obvious credential files (not a security guarantee — choose a root deliberately). Evaluation answers are cached locally; output goes to stdout only.

## Architecture and concepts
Retrieval is owned by `packages/core/src/retrieve.ts`: hierarchical traversal decides where to explore from directory metadata and content previews under a navigation byte budget, with a bounded early source pass reusing the same relevance judgments in later selection. Unread descendants and failed classifications are reported as unknown rather than silently dropped — "completion" means the planned search finished, not that every relevant byte was found. Source selection and presentation are kept separate so declaration units, comments, structural class headers, and bounded local-call context can preserve meaning without requiring whole-file output. The core (`packages/core/src/`) also owns source eligibility, evaluation, and cache identity; native state and question objects pass through the Vercel AI SDK, with source text just a field inside those objects — so provider selection changes transport/auth only, not retrieval semantics.

## Main APIs
- `jg "<question>" [path]` — the primary search command.
- `jg files [root]` — dry-run file-count preview, same filtering flags as search, no provider call.
- `jg auth [--provider <name>] [--base-url <url>] [--model <id>] [--stdin]` — configure and save provider credentials.
- `jg doctor` — validate the saved provider/endpoint with synthetic input.
- `jg skill` — install the bundled agent skill into detected coding-agent projects.
- `jg --help` — cache controls, search overrides, incomplete-result behavior.

## When to use
Reach for `jg` when you know the *behavior* you need (e.g. "where is authentication checked before a request reaches a handler?") but not which file holds it, across repositories unfamiliar to the agent. When you already know an exact symbol or path, a direct read or `rg` search is usually sufficient — the project frames itself as a complement to, not a replacement for, grep-style tools. The maintainers report their ten-task SWE-bench comparison matched baseline task success (8/10 solved both ways) while reducing measured Sol-only agent cost by ~30% (and ~26-28% total cost including Jev cost in later reruns); these are single-run cost/quality observations, not a guaranteed speed improvement or universal savings claim.

## Ecosystem
Jevgrep is published to npm as `@dzhng/jevgrep` and built as a Bun/Turborepo monorepo (`apps/cli` for the CLI package, `packages/core` for the retrieval engine, `packages/typescript-config` for shared tooling). It depends on the separate [vercel-labs/skills](https://github.com/vercel-labs/skills) installer for agent-skill distribution and on a "Jev" relevance model served through Vercel AI Gateway or compatible providers. Evaluation harness and dated cost/quality result reports live under `evals/`, and design/decision records (including the project's own implementation history) live under `specs/`. The repository's `AGENTS.md` documents an "iteration speed first" verification policy — narrowest check first, full test run only once a spec's implementation is finished — reflecting the same cost-conscious philosophy the tool applies to agent context-gathering.

Maintenance status: MIT-licensed, actively released (v0.8.0, 2026-10-01, Windows support), 2,092 stars and 136 forks at time of fetch.
