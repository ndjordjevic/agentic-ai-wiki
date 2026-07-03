# coleam00/helpline

## Metadata
- Stars: 100
- Primary language: Python
- Default branch: main
- Latest release: none
- License: null
- Homepage: 
- Fetched: 2026-07-03
- Final URL: https://github.com/coleam00/helpline

## Description
Demonstration codebase for building the AI Layer (CLAUDE.md hierarchy, hooks, skills, LSP, MCP, plugin) — companion repo for the 'How Claude Code works in large codebases' video.

## README
# Helpline

Helpline is a B2B helpdesk and customer-support platform — an internal monorepo
where five services (`api`, `auth`, `billing`, `notifications`, `search`) talk
over HTTP and share two internal packages (`core`, `db`). It's the kind of
mid-sized, multi-service codebase where an AI coding agent either pays for
itself or quietly makes a mess: shared packages that everything imports, money
rules that must never silently regress, a request gateway with its own
conventions, and tests scattered across services.

## Quick start

**What this repo actually is.** Helpline is a *demonstration codebase*, built
for the YouTube video **"The AI Layer: How to Make Claude Code Work in Large
Codebases."** It is a deliberately realistic — but compact — complex codebase,
used to show *concretely* how to build an **AI Layer** — our name for the
harness of configuration and tooling that Anthropic's article describes in
[*How Claude Code works in large codebases*](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start).
(The article describes the harness and its components; "AI Layer" is our term
for it, not Anthropic's.)
That article is the *what* and the *why*, and it is excellent — but it stays
high-level. Helpline is the *how*: every component from the article, built and
validated on a real codebase. The rest of this repo is written as if Helpline
were a live product, because that is exactly how you should treat your own
codebase when you give it an AI Layer.

**Run it:**

```bash
git clone https://github.com/coleam00/helpline.git
cd helpline
uv sync --extra dev
uv run pytest                 # the application's own test suite
```

**See the AI Layer:** read **[`AI-LAYER.md`](AI-LAYER.md)** — it maps every
component to the article and to where it lives in this repo. Then run the
validator, which proves every piece works end to end:

```bash
uv run --extra dev python tooling/validate/validate_all.py   # 13/13
```

## The AI Layer, concretely

Every codebase you ship with an AI agent has three parts: **code**, **tests**,
and — the new one — the **AI Layer**: the configuration, context, and reusable
workflows that make an agent productive in *your* codebase. Helpline builds
every component the article names:

| Component (from the article) | Built here | Where |
|-------------------------------|------------|-------|
| **CLAUDE.md hierarchy** | lean root `CLAUDE.md` + one per service/package, loaded additively | `CLAUDE.md`, `*/CLAUDE.md` |
| **Hooks** | a `SessionStart` orientation hook + a self-improving `Stop` hook that reflects on the session and proposes concrete `CLAUDE.md` edits | `.claude/hooks/` |
| **Skills** | `billing-money-rules`, `api-add-route`, `scoped-tests` — glob-scoped with the `paths:` field, progressive disclosure into `references/` | `.claude/skills/` |
| **Subagent** | a genuinely read-only `explorer` (no write tools) that maps a subsystem and reports back | `.claude/agents/explorer.md` |
| **LSP** | pyright + `pyright-langserver` for symbol-level navigation | `docs/lsp-setup.md` |
| **MCP** | `codebase-search` — AST-based `where_is` / `find_references` / `outline` | `tooling/mcp/` |
| **Plugin** | `helpline-ai-layer` — bundles the portable pieces for one-command install | `tooling/helpline-ai-layer/` |

The git history is the before/after, on purpose: **commit 1** is Helpline with
*no* AI Layer; **commit 2** adds *the entire layer*.

## Take this to your own codebase

Helpline is not just something to read — it is something to *reuse*. There are
two ways, and both matter more than the codebase itself.

### 1. Install the plugin — the fastest path

The portable, repo-agnostic pieces of the AI Layer are bundled as a Claude Code
plugin at `tooling/helpline-ai-layer/`. From your own project:

```
/plugin marketplace add /path/to/helpline/tooling
/plugin install helpline-ai-layer@helpline-tooling
```

That one install gives *your* repo:

- the **self-improving Stop hook** — reflects on each session and proposes
  `CLAUDE.md` updates, so your layer never silently rots;
- the **read-only `explorer` subagent** — maps a subsystem without burning your
  main session's context;
- the **`codebase-search` MCP** — AST-based structured search;
- a generic **`scoped-tests`** skill.

These are deliberately layout-agnostic: the hooks follow *your* `CLAUDE.md`
hierarchy, and the MCP discovers *your* source by walking the repo. Nothing is
tied to Helpline's directory names.

### 2. Point your coding agent at this repo

You don't have to copy anything by hand. Clone Helpline, open it alongside your
project, and tell your agent something like:

> Read `AI-LAYER.md` and the `.claude/` folder in the Helpline repo. It is a
> worked example of the AI Layer from Anthropic's large-codebases article.
> Build a comparable AI Layer for *this* codebase — a CLAUDE.md hierarchy,
> hooks, skills, an MCP, a subagent — adapted to our structure and conventions.

`AI-LAYER.md` exists for exactly this. It is an agent-readable map from each
article concept to the artifact that implements it, plus the proof that it
works. The repo is a reference implementation your agent can learn the *pattern*
from — not boilerplate to clone blindly.

### What travels, and what you rebuild

| Generalizable — works in any repo | Repo-specific — rebuild for yours |
|-----------------------------------|------------------------------------|
| the `Stop` / `SessionStart` hooks (CLAUDE.md-hierarchy based) | the `CLAUDE.md` files (your conventions) |
| the `explorer` subagent | `billing-money-rules`, `api-add-route` (your domain skills) |
| the `codebase-search` MCP | — |
| the generic `scoped-tests` skill | — |

The repo-specific pieces aren't reusable *content* — but they are reusable
*templates*. Copy the shape, change the substance.

## Layout

```
services/
  api/            HTTP gateway — routes, request handling
  auth/           authentication — tokens, password hashing
  billing/        subscriptions + invoicing
  notifications/  outbound email + templating
  search/         ticket search indexing + queries
packages/
  core/           shared domain models + error types
  db/             database connection + repositories
infra/            docker-compose for local dev
scripts/          one-off operational scripts
tests/            cross-service integration tests
tooling/          the AI Layer's MCP server, the plugin, and the validators
```

Each service owns its own area. `packages/core` and `packages/db` are imported
by every service — change them carefully.

## Dev

```bash
uv sync --extra dev      # install
uv run pytest            # full test suite
uv run pyright           # type-check
```

## Docs

### AI-LAYER.md
# Helpline AI Layer — Article Alignment & Video Map

This repo is a worked, **fully validated** example of Anthropic's article
*"How Claude Code works in large codebases: best practices and where to start."*
Helpline shipped with **no AI Layer**; every piece below was built on top of it
and tested end to end (`VALIDATION.md` — 13/13).

Article thesis: **the harness — the ecosystem built around the model —
determines how Claude Code performs more than the model alone.**

> *"AI Layer" is our name for that harness. Anthropic's article describes the
> harness and its components; it does not use the phrase "AI Layer."*

---

## The extension points — article → artifact → proof

| Extension point | What the article says | Built here | Proof |
|---|---|---|---|
| **CLAUDE.md files** | Loaded first; lean root, subdirectory files load additively as Claude walks the tree | `CLAUDE.md` (lean root) + 7 subdirectory files in each service/package | `validate_all.py` → "CLAUDE.md hierarchy" |
| **Hooks** | Best use is *self-improving* setup, not just prevention. "A start hook can load team-specific context dynamically." "A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh." | `SessionStart` hook loads dynamic orientation (active areas + recent commits). `Stop` hook = a deterministic trigger (`propose_claude_md.py`) that spawns a background reflector (`reflect_claude_md.py`); the reflector calls headless `claude -p` to reflect on the session diff and write concrete proposed `CLAUDE.md` edits — with a deterministic fallback if `claude` is unavailable | `validate_all.py` → "Hook — Stop": both files compile, recursion guard holds, a real end-to-end reflection writes `.claude/claude-md-review.md` |
| **Skills** | On-demand expertise, progressive disclosure, scoped to specific paths | `billing-money-rules`, `api-add-route` (both with `references/`), `scoped-tests` — each scoped with the `paths:` glob frontmatter field, so a skill auto-loads only when the agent works in its part of the repo | `validate_all.py` → "Skills": frontmatter + `paths:` scoping |
| **Plugins** | Bundle skills/hooks/MCP into installable packages, distribute via a marketplace | `tooling/helpline-ai-layer/` plugin + `tooling/.claude-plugin/marketplace.json`; bundles only the repo-agnostic pieces (generic `scoped-tests`, hooks, explorer, MCP) | "Plugin" check — 8 files, all JSON valid |
| **LSP** | Symbol-level precision instead of text-pattern false positives | pyright + `pyright-langserver`, configured in `[tool.pyright]` | `check_lsp.py` — real `initialize` handshake, 16 capabilities |
| **MCP servers** | Expose structured search as a callable tool | `codebase-search` server — `where_is`, `find_references`, `outline`, all **AST-based** (parses every module; never substring-matches), wired via `.mcp.json` | `check_mcp.py` — real handshake + all three tools called |
| **Subagents** | Split exploration from editing — read-only mapper, separate context window | `.claude/agents/explorer.md` — **genuinely read-only** (`tools: Read, Grep, Glob` — no Write/Edit), returns findings as its report to the parent | "Subagent" check asserts no write tools are granted |

---

## The 3 configuration patterns

### Pattern 1 — Make the codebase navigable at scale
- **Lean, layered CLAUDE.md** — root holds only repo-wide truths; each service
  and package carries its own conventions.
- **Initialized in subdirectories**, not just the root — Claude walks up the
  tree, so local context is never lost.
- **`CODEBASE_MAP.md`** — find where a feature lives before exploring.
- **`.claudeignore`** — generated files, caches, `uv.lock` excluded.
- **Scoped test commands** — every service `CLAUDE.md` and the `scoped-tests`
  skill say "run *your* service's tests, not the full suite."
- **LSP** — symbol search instead of grep false-positives.

### Pattern 2 — Actively maintain CLAUDE.md as models evolve
- The **`Stop` hook** is the proactive half, split in two so the turn never
  blocks on a model call: `propose_claude_md.py` cheaply detects which areas
  changed and spawns `reflect_claude_md.py` in the background; the reflector
  asks headless `claude -p` to reflect on the session's diff and draft concrete
  `CLAUDE.md` edits into `.claude/claude-md-review.md`. The AI Layer proposes
  its own updates instead of rotting silently. A recursion guard stops the
  nested `claude` from re-triggering the hook; a deterministic fallback flags
  the touched areas if `claude` is unavailable.
- **Review cadence:** a full `CLAUDE.md` / skills / hooks review every **3–6
  months**, and after any major model release. Rules written for an older
  model's limits (e.g. "refactor one file at a time") become a drag once newer
  models can do coordinated cross-file edits — delete them when that happens.

### Pattern 3 — Assign ownership
- The **Platform Team** owns `tooling/` and `.claude/` — one DRI for
  configuration, the plugin marketplace, and `CLAUDE.md` conventions.
- The **plugin is the distribution mechanism**: a new repo or new engineer runs
  one install and gets the team's baseline layer on day one, instead of
  bottoms-up fragmentation.

---

## Getting started — the article's 4 phases

| Phase | Article | In this repo |
|---|---|---|
| Foundation | CLAUDE.md hierarchy, ignore rules, LSP | `CLAUDE.md` ×8, `.claudeignore`, pyright |
| Infrastructure | skills, MCP, plugin distribution | 3 skills, `codebase-search` MCP, `helpline-ai-layer` plugin |
| Governance | review requirements, DRI, approvals | *Partial by nature* — version-controlled `.claude/settings.json` permissions is the one concrete artifact; the DRI, approved-skills list, and review process are organizational and live outside any single repo (Pattern 3 documents the intent) |
| Scale | expand skills/plugins, iterate CLAUDE.md, periodic review | the `Stop` hook + the 3–6 month cadence above |

---

## Validation

Everything above is verified by `tooling/validate/validate_all.py` →
`VALIDATION.md` (**13/13**). Re-run any time:

```bash
uv run --extra dev python tooling/validate/validate_all.py
```

### CLAUDE.md (root)
# Helpline

B2B helpdesk platform. Monorepo: 5 services + 2 shared packages. Python 3.11+, `uv`.

This root file is intentionally lean — it holds only what's true everywhere.
Each service and package has its own `CLAUDE.md` with local conventions;
Claude loads them automatically as it moves into that directory.

## Where things live

See `CODEBASE_MAP.md` for the full tree. Top level:

- `services/` — `api`, `auth`, `billing`, `notifications`, `search`
- `packages/` — `core` (domain models + errors), `db` (connection + repos)

## Critical gotchas (repo-wide)

- **`packages/core` and `packages/db` are imported by every service.** A change
  there ripples everywhere — run the full suite, not a scoped one, for those.
- **Run tests scoped to what you changed.** `uv run pytest services/auth` after
  an auth change. The full suite is only for `core`/`db` changes. See each
  service's `CLAUDE.md` for its exact command.
- **Imports are flat.** `core.*`, `db.*`, and each service name (`api`, `auth`,
  …) are importable directly — `packages/` and `services/` are on the path.
- **The DB connection is a process-wide in-memory stub.** `get_connection()`
  returns one shared instance. Tests that mutate tables must clean up after
  themselves or state leaks across tests.
- **Navigate by symbol, not by grep.** pyright runs as the language server —
  to find where something is defined or used, prefer LSP go-to-definition and
  find-references over text search. In a codebase this size grep returns false
  matches (comments, substrings, unrelated names); the LSP is exact. Setup and
  verification: `docs/lsp-setup.md`.

## Commands

```bash
uv sync --extra dev      # install
uv run pytest -q         # full suite
npx pyright              # type-check
```

### CODEBASE_MAP.md
# Helpline — Codebase Map

A lightweight map of the repo so an agent can find where a feature lives
*before* it starts reading files. Layered: top-level groups first, then the
modules inside each. Keep this current when you add or move a service.

## Top level

| Path | What it is |
|------|------------|
| `services/` | The five runnable services. Each is independently testable. |
| `packages/` | Shared libraries imported by services. Changes here are repo-wide. |
| `tests/` | Cross-service integration tests. Per-service tests live beside the service. |
| `infra/` | Local-dev infrastructure (`docker-compose.yml`: Postgres + Redis). |
| `scripts/` | One-off operational scripts (`seed_data.py`). |

## services/

| Service | Entry points | Responsibility |
|---------|--------------|----------------|
| `api` | `routes.py` (route table), `app.py` (dispatch) | HTTP gateway. Validate → call service/repo → shape response. |
| `auth` | `tokens.py`, `passwords.py` | Session tokens (HMAC) + password hashing (PBKDF2). |
| `billing` | `subscriptions.py`, `invoices.py` | Plans, seat limits, invoice generation. Money in cents. |
| `notifications` | `email.py`, `templates.py` | Outbound email; all copy via named templates. |
| `search` | `indexer.py`, `query.py` | In-memory inverted index over tickets; AND queries. |

## packages/

| Package | Entry points | Responsibility |
|---------|--------------|----------------|
| `core` | `models.py`, `errors.py` | Domain dataclasses + the error hierarchy (HTTP contract). |
| `db` | `connection.py`, `repositories.py` | Connection stub + typed repositories. Services use repos only. |

## Finding a feature

- **A route / endpoint** → `services/api/routes.py`, then the handler module.
- **Pricing or seat rules** → `services/billing/subscriptions.py`.
- **A domain model field** → `packages/core/models.py`.
- **How data is read/written** → `packages/db/repositories.py`.

### VALIDATION.md
# Helpline AI Layer — Validation Report

_Generated 2026-05-20T07:48:49 by `tooling/validate/validate_all.py`._

**13/13 checks passed.**

| Check | Result | Detail |
|-------|--------|--------|
| App — test suite | ✅ PASS | pytest: 9 passed in 0.18s |
| App — type check | ✅ PASS | pyright: 0 errors, 0 warnings, 0 informations |
| App — runtime smoke | ✅ PASS | app smoke: seeded 1 user, 2 tickets |
| CLAUDE.md hierarchy | ✅ PASS | 8 CLAUDE.md files present |
| Hook — SessionStart | ✅ PASS | SessionStart hook ran and emitted orientation context |
| Hook — Stop (self-improving) | ✅ PASS | trigger + reflector compile, recursion guard holds, end-to-end reflection wrote claude-md-review.md (LLM reflection) |
| Skills (path-scoped) | ✅ PASS | 3 skills valid (frontmatter + paths-scoped + progressive disclosure) |
| Subagent (explorer) | ✅ PASS | explorer subagent is genuinely read-only (tools: ['Glob', 'Grep', 'Read']) |
| LSP (pyright handshake) | ✅ PASS | PASS: pyright language server initialized (16 capabilities) |
| LSP navigation (go-to-definition) | ✅ PASS | PASS: LSP go-to-definition resolved 'monthly_total_cents' to the real definition — subscriptions.py:30 |
| MCP server (handshake + calls) | ✅ PASS | PASS: MCP server 'helpline-codebase-search' — handshake ok, tools ['where_is', 'find_references', 'outline']; where_is + find_references + outline returned real AST results |
| Plugin (bundle + marketplace) | ✅ PASS | plugin: 8 bundled files present, all JSON valid |
| .claudeignore + settings.json | ✅ PASS | .claudeignore present, settings.json valid (incl. hooks block) |

Re-run any time with `uv run --extra dev python tooling/validate/validate_all.py`.

### docs/lsp-setup.md
# LSP setup — pyright

The article calls out Language Server Protocol integration as the way to give
Claude **symbol-level** precision — "go to definition" and "find all
references" — instead of text-pattern matching that produces thousands of false
grep hits.

## What's wired

- **pyright** is a dev dependency (`pyproject.toml` → `[project.optional-dependencies].dev`).
- The type-check config lives in `pyproject.toml` → `[tool.pyright]`:
  `extraPaths` makes the flat `core.*` / `db.*` / service imports resolve, and
  `venvPath`/`venv` point pyright at `.venv` so installed packages resolve.
- The language server binary is `pyright-langserver` (ships with the `pyright`
  package). Claude Code speaks LSP to it over stdio.
- The **navigation rule** lives in the root `CLAUDE.md` gotchas — *navigate by
  symbol, not by grep*. Installing the server isn't enough; that rule is what
  makes the agent actually reach for go-to-definition over text search.

## Verify it

```bash
uv sync --extra dev
uv run pyright                                          # type-check, expect 0 errors
uv run python tooling/validate/check_lsp.py             # real LSP initialize handshake
uv run python tooling/validate/check_lsp_navigation.py  # real go-to-definition + grep contrast
```

- `check_lsp.py` spawns `pyright-langserver --stdio`, sends an `initialize`
  request with proper `Content-Length` framing, and confirms the server
  returns its capabilities — proof the LSP path works end to end.
- `check_lsp_navigation.py` goes further: it asks pyright to resolve a real
  symbol to its definition via `textDocument/definition` and confirms the
  answer is the *correct* file — then contrasts it with a plain grep, which
  returns every textual mention. This is the proof the navigation rule
  actually helps, not just that the server is installed.

## Top-level structure
- `.claude/` — **AI Layer config**: hooks, skills, agents (explorer subagent), settings
- `.claudeignore` — excludes generated files, caches, `uv.lock` from agent context
- `.mcp.json` — wires `codebase-search` MCP server
- `AI-LAYER.md` — agent-readable map from Anthropic article concepts to artifacts + validation proof
- `CLAUDE.md` — lean root agent instructions (8 total across repo)
- `CODEBASE_MAP.md` — feature-location map for agents
- `VALIDATION.md` — 13/13 AI Layer validation report
- `docs/` — LSP setup guide (`lsp-setup.md`)
- `services/` — five runnable microservices (`api`, `auth`, `billing`, `notifications`, `search`)
- `packages/` — shared `core` (models/errors) and `db` (connection/repos) imported by all services
- `infra/` — docker-compose for local Postgres + Redis
- `scripts/` — operational scripts (`seed_data.py`)
- `tests/` — cross-service integration tests
- `tooling/` — AI Layer MCP server, `helpline-ai-layer` plugin, validators (`validate_all.py`)
- `pyproject.toml`, `uv.lock` — Python 3.11+ monorepo via `uv`
