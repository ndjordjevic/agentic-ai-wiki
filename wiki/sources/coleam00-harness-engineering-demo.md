---
type: source
source_url: https://github.com/coleam00/harness-engineering-demo
tags:
  - harness-engineering
  - plan-implement-validate
  - claude-code-hooks
  - claude-code-skills
  - self-validating-loop
  - ralph-loop
  - ast-codebase-search-mcp
  - subagent-code-review
related:
  - snarktank-ralph
  - obra-superpowers
  - coleam00-archon
  - gsd-build-get-shit-done
  - buildermethods-agent-os
  - eyaltoledano-claude-task-master
  - github-spec-kit
  - zilliztech-claude-context
  - frankbria-ralph-claude-code
  - coleam00-agent-control-plane
  - the-new-sdlc-with-vibe-coding
product: harness-engineering-demo
detail_level: standard
created: 2026-06-16
updated: 2026-06-30
---

A companion repo to the YouTube video "What is Harness Engineering?" demonstrating how to build a real **harness** — the context and workflows wrapping a coding agent — using only Claude Code's built-in primitives (CLAUDE.md, skills, hooks, sub-agents, MCP), with no external framework. It wraps a brownfield SaaS app (Schedulr: FastAPI + Next.js) in a self-validating **PIV loop** (Plan → Implement → Validate) and pairs it with the Ralph loop ([[snarktank-ralph]]) for unattended multi-session runs.

_All claims below are sourced from ../../raw/github/coleam00-harness-engineering-demo.md unless otherwise noted._

## What it does

Defines "harness engineering" as building the context and workflows that wrap a coding agent so it works the way the team works — its processes enforced, its standards applied — rather than acting like a clever stranger guessing at the codebase. The repo splits a harness into two halves: **within a session** (CLAUDE.md, context modules, skills, hooks — the "AI Layer") and **across sessions** (plan in one session, implement+validate in another, review in a third, handed off via markdown files in `plans/` and `reports/`, optionally automated by the Ralph loop).

## Installation

Prerequisites: Claude Code CLI, `uv` (Python), npm (Node 20+).

```bash
cd app && docker compose up -d                                        # Postgres on host port 5433
cd app/backend && uv sync --extra dev && uv run alembic upgrade head  # backend deps + migrations
cd app/frontend && npm install                                        # frontend deps
```

A fresh Claude Code session can be asked to do this setup itself by reading the README's Setup section.

## Key features

- **PIV loop as two commands**: `/plan "<feature request>"` writes `plans/<feature-slug>-plan.md` after reading the codebase and loading relevant `.claude/context/` modules; `/implement plans/<plan>.md` executes each task with per-task validation and writes `reports/<feature-slug>-implementation-report.md`. `/validate` exists standalone but is not a manual loop step — it's enforced automatically.
- **Self-validating via hooks, not convention**: a `PostToolUse` hook (`post_tool_use_lint.py`) runs `ruff check` (Python) or `tsc --noEmit` (TypeScript) after every file edit, non-blocking. A `Stop` hook (`stop_validate.py`) runs ruff + pytest and blocks Claude from ending its turn until both are green — this is what makes the loop self-validating rather than advisory.
- **Security guard hook**: `security_guard.py` (`PreToolUse`) hard-denies reading/editing/writing any real `.env` file (across Read/Edit/Write/MultiEdit/NotebookEdit, Bash command parsing including obfuscated globs, and Glob/Grep targeting — template files like `.env.example` stay allowed) and denies recursive directory deletion (`rm -rf`, `rmdir`, `find -delete`, `git clean -d`; single-file `rm` still works). It fails open on malformed input and still fires under `--dangerously-skip-permissions`, so it holds during unattended Ralph runs too.
- **Sub-agent code review**: `/review` delegates the diff to a `code-reviewer` sub-agent (`.claude/agents/code-reviewer.md`) that checks it against CLAUDE.md rules using the codebase-search MCP tools, writing `reports/<feature-slug>-review.md`.
- **AST-based symbol navigation over grep**: an isolated `uv` project (`tooling/pyproject.toml`) runs a FastMCP server (`tooling/mcp/codebase_search.py`, registered via `.mcp.json`) exposing `where_is`, `find_references`, and `outline` — parsing the Python AST so results are real definitions/call sites with no false hits from comments or strings.
- **On-demand context modules**: `.claude/context/{architecture,auth,codebase-search,export-pattern,testing,timezones}.md` are loaded only when a task touches the relevant area, keeping CLAUDE.md itself short while still covering the codebase's auth split, CSV-export escaping pattern, and UTC/timezone storage rules.

## Architecture and concepts

The harness operates on Schedulr, a B2B meeting-scheduling SaaS: Next.js 15 App Router + TypeScript frontend (`app/frontend/`), FastAPI + SQLAlchemy 2.0 + Alembic + Python 3.12 backend (`app/backend/`), Postgres 16 on host port 5433 via `app/docker-compose.yml`. CLAUDE.md encodes the codebase's real conventions as hard rules: SQLAlchemy 2.0 `Mapped[T]`/`mapped_column()` only, `*Create`/`*Update`/`*Out` Pydantic schema naming, UTC-only datetime storage rendered to viewer timezone only at serialization (never `.strftime()` on raw UTC), CSV-cell escaping against formula injection, and a hard split between the forward JWT auth pattern and a legacy session-token pattern that new routes must not use.

## Example usage

```
/plan "add your feature request here"
/implement plans/your-plan.md
```

That's the entire loop — `/implement` validates each task as it runs, and the Stop hook blocks completion until ruff + mypy + pytest + tsc + vitest are all green, so no explicit `/validate` call is required in normal use.

For unattended, multi-iteration runs:

```bash
python ralph/ralph.py --worktree --branch ralph/csv-export --cleanup
```

Ralph (`ralph/ralph.py` / `ralph/ralph.sh`) strings together headless `claude -p` sessions, re-feeding a spec each iteration until a `DONE.txt` sentinel appears, committing after every iteration so each step is reversible. `ralph/PROMPT.md` is a worked example spec (CSV export, 8 verifiable items); `ralph/example-run/` is a complete captured run — spec, iteration log, fix plan with every item checked off, and the resulting code — useful as a reference for what a finished loop looks like. `--worktree` makes Ralph self-isolating (own worktree + branch); `--db-isolate` lets multiple Ralph runs work different features in parallel against separate databases. `claude -p` draws from a separate Agent SDK credit pool, not the interactive Claude Code subscription.

## When to use

Useful as a worked, inspectable reference for teams who want to "build their own harness" directly on Claude Code primitives instead of adopting an external agent-orchestration framework — particularly the pattern of using hooks (not prompts) to make validation non-optional, and using plain markdown handoffs (`plans/`, `reports/`) to move work across sessions and sub-agents without a database or queue.

## Maintenance status

62 stars, 22 forks as of fetch. No tagged releases; no license file. Default branch `main`; last pushed 2026-05-27.

## Ecosystem

Wraps [Schedulr](https://github.com/coleam00/schedulr) as the example brownfield app under management. Shares the headless-loop pattern with [[snarktank-ralph]] (Ralph here is the same re-feed-a-spec-until-DONE.txt design). The skills/hooks/sub-agent split overlaps conceptually with [[obra-superpowers]] (skill-driven harness behavior) and [[coleam00-archon]] (multi-agent orchestration over a project codebase). The MCP-based AST symbol navigation (`where_is`/`find_references`/`outline`) parallels [[zilliztech-claude-context]]'s approach to giving agents structured codebase lookup instead of plain grep.
