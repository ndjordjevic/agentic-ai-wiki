# coleam00/harness-engineering-demo

## Metadata
- Stars: 62
- Primary language: Python
- Default branch: main
- Latest release: none
- License: none
- Homepage: (none)
- Fetched: 2026-06-16
- Final URL: https://github.com/coleam00/harness-engineering-demo

## Description
(no repo description set on GitHub)

## README
# Harness Engineering Demo

Companion repo for the YouTube video **"What is Harness Engineering?"**

A minimal, real **harness** built with the primitives already inside Claude Code —
no framework required. It wraps the [Schedulr](https://github.com/coleam00/schedulr)
brownfield app with a **PIV loop** (Plan → Implement → Validate) so you can see
what "building your own harness" actually looks like in production.

> **Harness engineering** = building the context and workflows that wrap a coding
> agent — the ecosystem it operates in — so it works the way *you* work: your
> processes enforced, your standards applied, building like another engineer on
> your team instead of a clever stranger guessing at your codebase.

---

## What's in here

| Piece | What it shows |
|-------|--------------|
| `CLAUDE.md` + `.claude/context/` | Rules + on-demand context derived from the real codebase (the "AI Layer") |
| `.claude/skills/plan/SKILL.md` | PIV step 1: analyze codebase + ticket, write `plans/<feature>-plan.md` |
| `.claude/skills/implement/SKILL.md` | PIV step 2: read plan, execute tasks, run per-task validation, write `reports/<feature>-implementation-report.md` |
| `.claude/skills/validate/SKILL.md` | PIV step 3: run the full gate (ruff + mypy + pytest + tsc + vitest) |
| `.claude/skills/review/SKILL.md` | PIV step 4: delegate diff to the code-reviewer sub-agent, write `reports/<feature>-review.md` |
| `.claude/agents/code-reviewer.md` | Sub-agent that reviews diffs against CLAUDE.md rules using codebase-search MCP tools |
| `.claude/hooks/post_tool_use_lint.py` | PostToolUse hook: runs ruff (Python) or `tsc --noEmit` typecheck (TS) after every file edit |
| `.claude/hooks/stop_validate.py` | Stop hook: blocks Claude from stopping until ruff + pytest are green |
| `.claude/hooks/security_guard.py` | PreToolUse hook: denies reading/editing/writing any real `.env` and recursive directory deletion (rm -rf, rmdir, find -delete, git clean -d) |
| `.claude/settings.json` | Wires both hooks into Claude Code |
| `.mcp.json` | Registers the `codebase-search` MCP server (AST-based symbol navigation) |
| `tooling/mcp/codebase_search.py` | FastMCP server exposing `where_is`, `find_references`, `outline` over the project's Python AST |
| `tooling/pyproject.toml` | Isolated uv project declaring the `mcp` dependency for the tooling layer |
| `ralph/ralph.sh` + `ralph/ralph.py` | The Ralph loop: strings headless Claude sessions together by re-feeding a spec each iteration |
| `app/` | Schedulr brownfield app (FastAPI + Next.js) — what the harness operates on |

---

## The two halves of a harness

1. **Within a session (the AI Layer):** `CLAUDE.md`, context modules, commands, hooks — everything that shapes how Claude behaves inside one Claude Code session.
2. **Across sessions (orchestration):** plan in one session → implement+validate in another → review in a third. Handed off via markdown files in `plans/` and `reports/`. Automated with the Ralph loop.

---

## Setup

You can let the agent do this. In a fresh Claude Code session, just ask it to read this section and get the app running. Or run it yourself:

```bash
# Prerequisites: Claude Code CLI, uv (Python), npm (Node 20+)
cd app && docker compose up -d                                        # Postgres on host port 5433
cd app/backend && uv sync --extra dev && uv run alembic upgrade head  # backend deps + migrations
cd app/frontend && npm install                                        # frontend deps
```

## Running the PIV loop

The loop is two commands. Validation is not a step you run, it is enforced for you: `/implement` validates each task as it goes, and the Stop hook blocks the agent from finishing until the full gate is green. That is what makes the loop self-validating.

**0. Let the agent set up the app.** In a fresh Claude Code session at the repo root:

```
Read the README and get the app running for me: Postgres, backend deps, frontend deps, and migrations.
```

**1. Plan**

```
/plan "add your feature request here"
```

Claude reads the codebase, loads the relevant `.claude/context/` modules, and writes `plans/<feature-slug>-plan.md`.

**2. Implement**

```
/implement plans/your-plan.md
```

Claude reads the plan, executes each task with per-task validation, and writes `reports/<feature-slug>-implementation-report.md`. When it finishes, the Stop hook runs the full gate (ruff + mypy + pytest + tsc + vitest) and blocks until it is green.

> `/validate` still exists if you want to run the gate explicitly (it is the same gate the Stop hook runs), but you do not need to call it as part of the loop.

---

## Hooks

Hooks run automatically, no invocation needed. Three are wired in `.claude/settings.json`:

- **PostToolUse lint** runs ruff (or a TS typecheck) after every file edit.
- **Stop gate** blocks the agent from finishing until ruff + pytest are green. This is the hook that makes the PIV loop self-validating.
- **PreToolUse security guard** denies access to real `.env` files and recursive deletes, even under `--dangerously-skip-permissions`.

**PostToolUse (static check):** After every `Edit`/`Write`/`MultiEdit`, `.claude/hooks/post_tool_use_lint.py` runs:
- Python files under `app/backend/` run `uv run ruff check <file>`
- TS/TSX files under `app/frontend/` run `npx tsc --noEmit` (typecheck; this brownfield app has no ESLint configured, and `next lint` would prompt interactively)

Non-blocking (always exits 0), so it surfaces issues without stopping work. Binaries are resolved via `shutil.which` so it works under Windows cmd.exe too.

**Stop (validate gate):** Before Claude ends its turn, `.claude/hooks/stop_validate.py` runs ruff + pytest. If either fails it prints a JSON block decision and Claude is asked to fix the issue. It checks `stop_hook_active` in the hook JSON to avoid infinite loops.

**PreToolUse (security guard):** Before any tool runs, `.claude/hooks/security_guard.py` hard-denies two things:
- Reading, editing, or writing a real `.env` file. It covers the Read/Edit/Write/MultiEdit/NotebookEdit tools, Bash commands (cat, grep, sed, awk, xxd, base64, `python -c`, `source`/`.`, `cp`, `find -exec cat`, obfuscated globs like `.e*` and `.??v`), and Glob/Grep file targeting. Template files (`.env.example`, `.sample`, `.template`, `.dist`, `.defaults`) stay allowed so config scaffolding still works.
- Recursive directory deletion: `rm -r`/`-rf`/`-fr`/`-Rf`/`--recursive`, `rmdir`, `find -delete`, `find -exec rm`, and `git clean -d`. Single-file `rm` is still allowed.

It returns a PreToolUse `permissionDecision: deny` with a reason (exit 0) so Claude gets the explanation and adapts, and fails open on malformed input so it can never brick a session. It still fires under `--dangerously-skip-permissions`, so it holds even during unattended Ralph runs.

---

## Ralph loop

Ralph strings together headless Claude sessions, re-feeding a spec to a fresh `claude -p` process each iteration until a `DONE.txt` sentinel appears. It commits after each iteration, so every step is reversible.

```bash
python ralph/ralph.py             # in-place (sandbox / dedicated branch only)
python ralph/ralph.py --worktree  # self-isolating: Ralph makes its own worktree + branch
```

See **`ralph/example-run/`** for a complete captured run of the CSV-export spec: the spec it was given, the iteration log, the fix plan with every spec item checked off, and the code it produced. Point here for what a finished loop looks like.

**Example spec:** `ralph/PROMPT.md` instructs Claude to add CSV export (SCH-142), with 8 verifiable spec items.

```bash
# From repo root
python ralph/ralph.py             # Python driver (cross-platform)
bash ralph/ralph.sh               # Bash driver (Linux/macOS)

# Tune limits
RALPH_MAX_ITER=10 RALPH_ITER_TIMEOUT=900 python ralph/ralph.py

# Self-isolating: Ralph creates its OWN worktree + branch and runs there
python ralph/ralph.py --worktree --branch ralph/csv-export --cleanup

# Parallel agents: several isolated runs at once, each its own branch + database
python ralph/ralph.py --worktree --branch ralph/feature-a --db-isolate &
python ralph/ralph.py --worktree --branch ralph/feature-b --db-isolate &
```

See `ralph/README.md` for full documentation, the worktree mode, and the parallel/DB-isolation pattern.

**Important:** `--dangerously-skip-permissions` is used by Ralph to allow unattended file writes. Run Ralph in a sandbox or dedicated worktree, never on your main branch. The `--worktree` flag gives you that isolation automatically.

**Credit note (2026-06-15):** `claude -p` draws from a separate Agent SDK credit pool, not your interactive Claude Code subscription.

---

## Repo layout

```
harness-engineering-demo/
├── CLAUDE.md                      # Global rules (the AI Layer)
├── .mcp.json                      # Registers codebase-search MCP server
├── .claude/
│   ├── settings.json              # Hook wiring
│   ├── agents/
│   │   └── code-reviewer.md       # Sub-agent: reviews diffs against CLAUDE.md rules
│   ├── skills/
│   │   ├── plan/SKILL.md          # /plan skill (PIV step 1)
│   │   ├── implement/SKILL.md     # /implement skill (PIV step 2)
│   │   ├── validate/SKILL.md      # /validate skill (PIV step 3)
│   │   └── review/SKILL.md        # /review skill (PIV step 4 — sub-agent delegation)
│   ├── context/
│   │   ├── architecture.md        # Module map + add-resource pattern
│   │   ├── auth.md                # JWT vs legacy session
│   │   ├── codebase-search.md     # MCP tool descriptions (where_is / find_references / outline)
│   │   ├── export-pattern.md      # ExportService protocol + CSV escaping
│   │   ├── testing.md             # pytest + vitest patterns
│   │   └── timezones.md           # TimezoneAwareTime + UTC storage rules
│   └── hooks/
│       ├── post_tool_use_lint.py  # PostToolUse: lint on edit
│       ├── stop_validate.py       # Stop: validation gate
│       └── security_guard.py      # PreToolUse: block .env access + recursive deletes
├── tooling/
│   ├── pyproject.toml             # Isolated uv project for tooling deps (mcp)
│   └── mcp/
│       └── codebase_search.py     # FastMCP AST server: where_is / find_references / outline
├── plans/                         # /plan outputs land here
├── reports/                       # /implement + /review outputs land here
├── ralph/
│   ├── PROMPT.md                  # Example spec (CSV export)
│   ├── ralph.sh                   # Bash loop driver
│   ├── ralph.py                   # Python loop driver (cross-platform)
│   ├── example-run/               # A complete captured run (reference): log, fix plan, produced code
│   └── README.md                  # Ralph documentation
└── app/                           # Schedulr brownfield app
    ├── backend/                   # FastAPI + SQLAlchemy 2.0, Python 3.12, uv
    ├── frontend/                  # Next.js 15 App Router, TypeScript
    └── docker-compose.yml         # Postgres 16 (host 5433)
```

## Docs

### CLAUDE.md (repo root — the global rules file)

# Schedulr — Harness Engineering Demo

Schedulr is a B2B meeting-scheduling SaaS for sales teams. Stack: **Next.js 15 App Router + TypeScript** (frontend, `app/frontend/`) and **FastAPI + SQLAlchemy 2.0 + Alembic + Python 3.12** (backend, `app/backend/`). Postgres on host port **5433** (container 5432) via `app/docker-compose.yml`.

#### Naming Conventions

| Layer | Convention | Example |
|-------|-----------|---------|
| Python files | `snake_case` | `routes_meetings.py`, `export_service.py` |
| Python classes | `PascalCase` | `MeetingCreate`, `PDFExport` |
| Python functions/vars | `snake_case` | `list_meetings`, `viewer_tz` |
| SQLAlchemy columns | `snake_case` (exception: legacy `createdAt` on `users`) | `start_time`, `team_id` |
| TS files/components | `kebab-case` files, `PascalCase` components | `meeting-list.tsx`, `MeetingList` |
| API routes | `/api/<resource>` plural noun | `/api/meetings`, `/api/contacts` |

#### Core Code Patterns

**Pydantic schemas** (in `app/backend/app/schemas/`): one file per resource; `*Create`, `*Update`, `*Out` naming. All schema classes inherit `BaseModel`.

**SQLAlchemy 2.0 mapped columns** (`app/backend/app/models/`): use `Mapped[T]` + `mapped_column()` throughout — no legacy `Column()` calls.

**Structured errors**: raise `HTTPException(status_code=..., detail="...")` in route handlers; services raise `ValueError` for business-rule violations that routes catch.

**DB sessions**: injected via `Depends(get_db)` (`app/backend/app/database.py`); always call `db.commit()` then `db.refresh(obj)` after mutations.

**Datetime storage**: always UTC, `DateTime(timezone=True)`. Render to viewer timezone only at serialization time via `TimezoneAwareTime` (`app/backend/app/utils/timezones.py`). Never call `.strftime()` on a raw UTC datetime.

**CSV/export escaping**: any user-supplied string written to a CSV cell MUST be prefixed with `'` if it starts with `=`, `+`, `-`, or `@` to prevent formula injection. See `app/backend/app/services/export_service.py` and `.claude/context/export-pattern.md`.

#### Build & Validation Commands

| Step | Command | Working Directory |
|------|---------|------------------|
| Backend lint | `uv run ruff check app` | `app/backend` |
| Backend type check | `uv run mypy app` | `app/backend` |
| Backend tests | `uv run pytest` | `app/backend` |
| Frontend lint | _none configured — `next lint` prompts interactively (no ESLint in this brownfield app); use type check below_ | `app/frontend` |
| Frontend type check | `npx tsc --noEmit` | `app/frontend` |
| Frontend unit tests | `npm run test` | `app/frontend` |
| Frontend build | `npm run build` | `app/frontend` |

Run the full gate with `/validate` before any PR.

#### On-Demand Context

Load these modules only when the task touches the relevant area:

| Module | Load when... |
|--------|-------------|
| `.claude/context/architecture.md` | Adding a new resource, service, or route |
| `.claude/context/auth.md` | Any authentication or authorization work |
| `.claude/context/codebase-search.md` | Using the MCP tools to navigate by symbol |
| `.claude/context/export-pattern.md` | Any export feature (CSV, PDF, XLSX, etc.) |
| `.claude/context/testing.md` | Writing or modifying tests |
| `.claude/context/timezones.md` | Any datetime display, serialization, or storage |

#### Hard Rules

- Run the full validation gate (`/validate`) before opening a PR.
- Never commit secrets, `.env` files, or JWT secrets to version control. A PreToolUse hook (`.claude/hooks/security_guard.py`) hard-blocks reading/editing any `.env` (use `.env.example`) and recursive directory deletes; do not try to work around it.
- Alembic migrations must be reversible — every `upgrade()` must have a working `downgrade()`.
- Escape user-supplied fields before writing them to any CSV cell (formula-injection risk — see export-pattern context).
- New code follows the **forward** auth pattern (`auth_jwt.py`), not the legacy session token. Do not add new routes that depend on `auth_legacy.py`.

#### Symbol Navigation

Navigate by symbol using the `codebase-search` MCP server (`.mcp.json`) instead of grep. The three tools — `find_references`, `where_is`, `outline` — parse the Python AST and return only real definitions and call sites, with no false hits from comments or strings. Use them whenever you need to:

- Verify a dependency is actually wired into a new route (`find_references("get_current_user")`)
- Locate a function before reading its file (`where_is("list_meetings")`)
- Check a service's public API before adding a method (`outline("export_service")`)

See `.claude/context/codebase-search.md` for full tool descriptions.

#### Miscellaneous / Gotchas

- Postgres runs on host port **5433** (not 5432). Connection string: `postgresql+psycopg://schedulr:schedulr@localhost:5433/schedulr`. The config falls back to this when `DATABASE_URL` is unset (`app/backend/app/config.py:14`).
- Two auth systems coexist: JWT (`app/backend/app/services/auth_jwt.py`) is the forward one; legacy session token (`app/backend/app/services/auth_legacy.py`) is still used by some routes. Prefer JWT on all new routes.
- `User.createdAt` uses camelCase as the column name — brownfield smell, do not replicate (`app/backend/app/models/user.py:24`).
- `uv.lock` is committed; always use `uv run <cmd>` to execute Python tools so the locked environment is used.
- Frontend `node_modules` are NOT committed; run `npm install` in `app/frontend/` before any frontend work.

## Top-level structure

- `.claude/` — the AI Layer: `agents/code-reviewer.md` (sub-agent), `skills/{plan,implement,validate,review}/SKILL.md` (PIV slash commands), `context/{architecture,auth,codebase-search,export-pattern,testing,timezones}.md` (on-demand context modules), `hooks/{post_tool_use_lint,stop_validate,security_guard}.py`, `settings.json` (hook wiring)
- `.gitignore`, `.mcp.json` (registers the `codebase-search` MCP server)
- `CLAUDE.md` — global rules file (full content above)
- `README.md` — project overview (full content above)
- `app/` — the Schedulr brownfield app: `backend/` (FastAPI + SQLAlchemy 2.0 + Alembic, Python 3.12, uv), `frontend/` (Next.js 15 App Router, TypeScript), `docs/`, `docker-compose.yml` (Postgres 16 on host port 5433)
- `plans/` — `/plan` skill output directory (only `.gitkeep` committed)
- `ralph/` — the Ralph loop: `ralph.py` / `ralph.sh` (drivers), `PROMPT.md` (example CSV-export spec), `example-run/` (captured reference run), `README.md`
- `reports/` — `/implement` and `/review` skill output directory
- `tooling/` — isolated uv project (`pyproject.toml`, `uv.lock`) for `tooling/mcp/codebase_search.py`, a FastMCP server exposing `where_is`, `find_references`, `outline` over the project's Python AST
