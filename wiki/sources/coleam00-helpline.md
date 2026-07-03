---
type: source
source_url: https://github.com/coleam00/helpline
tags:
  - ai-layer
  - claude-code-harness
  - claude-md-hierarchy
  - self-improving-hooks
  - path-scoped-skills
  - ast-codebase-search-mcp
  - pyright-lsp
  - large-codebase-patterns
related:
  - how-claude-code-works-in-large-codebases
  - coleam00-harness-engineering-demo
  - shareai-lab-learn-claude-code
  - anthropics-skills
  - obra-superpowers
  - zilliztech-claude-context
  - coleam00-archon
  - langchain-ai-openwiki
  - 6eanut-llm-wiki
product: helpline
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

Helpline (100 ★, Python) is Cole Medin's **worked reference implementation** of Anthropic's "How Claude Code works in large codebases" article — a deliberately realistic five-service Python monorepo (helpdesk SaaS) whose real purpose is demonstrating the **AI Layer**: the harness of CLAUDE.md files, hooks, skills, LSP, MCP, subagents, and a distributable plugin that makes coding agents productive at scale. Git history is intentionally split: commit 1 is the app with no layer; commit 2 adds the entire validated harness (13/13 checks). The portable pieces ship as the `helpline-ai-layer` Claude Code plugin for one-command install into any repo.

_All claims below are sourced from ../../raw/github/coleam00-helpline.md unless otherwise noted._

## What it does

Helpline wraps a compact but realistic multi-service codebase — HTTP gateway (`api`), auth, billing (money-in-cents rules), notifications, and search over shared `core`/`db` packages — inside a fully instrumented agent harness. `AI-LAYER.md` maps every Anthropic article extension point to a concrete artifact and validation proof. The repo is written as if Helpline were a live product so teams can copy the *pattern* (not blind boilerplate): lean layered `CLAUDE.md` files, a `CODEBASE_MAP.md` for feature location, `.claudeignore` for noise exclusion, path-scoped domain skills, and end-to-end validators in `tooling/validate/validate_all.py`.

## Installation

**Run the demo app:**

```bash
git clone https://github.com/coleam00/helpline.git
cd helpline
uv sync --extra dev
uv run pytest
```

**Validate the AI Layer (13/13):**

```bash
uv run --extra dev python tooling/validate/validate_all.py
```

**Install portable pieces into your own repo via plugin:**

```
/plugin marketplace add /path/to/helpline/tooling
/plugin install helpline-ai-layer@helpline-tooling
```

This bundles the self-improving Stop hook, read-only `explorer` subagent, AST-based `codebase-search` MCP, and generic `scoped-tests` skill — all layout-agnostic.

## Key features

- **CLAUDE.md hierarchy** — lean root + seven subdirectory files (one per service/package); Claude loads them additively as it walks the tree.
- **Self-improving hooks** — `SessionStart` injects orientation (active areas + recent commits); `Stop` spawns a background reflector (`reflect_claude_md.py`) that calls headless `claude -p` to propose concrete `CLAUDE.md` edits into `.claude/claude-md-review.md`, with recursion guard and deterministic fallback.
- **Path-scoped skills** — `billing-money-rules`, `api-add-route` (with `references/` progressive disclosure), and `scoped-tests`; each uses `paths:` glob frontmatter so skills auto-load only in their directory.
- **Read-only explorer subagent** — `.claude/agents/explorer.md` grants only `Read`, `Grep`, `Glob` (no write tools); maps subsystems in a separate context window.
- **AST-based MCP** — `codebase-search` server exposes `where_is`, `find_references`, `outline` via Python AST parsing (never substring grep); wired in `.mcp.json`.
- **LSP integration** — pyright + `pyright-langserver` with `[tool.pyright]` config; root `CLAUDE.md` enforces "navigate by symbol, not by grep."
- **Distributable plugin** — `tooling/helpline-ai-layer/` bundles repo-agnostic pieces with marketplace manifest for team-wide baseline installs.

## Architecture

The application layer is a Python 3.11+ monorepo managed by `uv`:

- `services/api` — HTTP gateway (`routes.py` route table, `app.py` dispatch)
- `services/auth` — HMAC session tokens + PBKDF2 password hashing
- `services/billing` — subscriptions, seat limits, invoices (money stored in cents)
- `services/notifications` — outbound email via named templates
- `services/search` — in-memory inverted index with AND queries
- `packages/core` — domain dataclasses + error hierarchy (HTTP contract)
- `packages/db` — process-wide in-memory connection stub + typed repositories

The AI Layer lives in `.claude/` (hooks, skills, agents, settings), `tooling/mcp/` (MCP server), `tooling/helpline-ai-layer/` (plugin bundle), and `tooling/validate/` (13 automated checks including real LSP handshake, MCP tool calls, and end-to-end Stop-hook reflection). Three configuration patterns from the article are documented in `AI-LAYER.md`: (1) navigability at scale, (2) proactive CLAUDE.md maintenance with 3–6 month review cadence, (3) platform-team ownership via plugin distribution.

## Example usage

Point your coding agent at Helpline alongside your project:

> Read `AI-LAYER.md` and the `.claude/` folder in the Helpline repo. It is a worked example of the AI Layer from Anthropic's large-codebases article. Build a comparable AI Layer for *this* codebase — a CLAUDE.md hierarchy, hooks, skills, an MCP, a subagent — adapted to our structure and conventions.

Or install only the portable plugin and keep Helpline-specific domain skills (`billing-money-rules`, `api-add-route`) as templates to rebuild for your domain.

## Maintenance status

100 stars, 31 forks, Python primary language, default branch `main`, last pushed 2026-05-20. No releases published. Companion to Cole Medin's YouTube video "The AI Layer: How to Make Claude Code Work in Large Codebases" (May 20, 2026). Directly implements the Anthropic article ingested as [[how-claude-code-works-in-large-codebases]]. Sibling demos from the same author include [[coleam00-harness-engineering-demo]] (PIV loop harness) and [[coleam00-archon]] (YAML workflow engine).
