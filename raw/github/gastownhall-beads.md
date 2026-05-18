# gastownhall/beads

## Metadata
- Stars: 23,795
- Primary language: Go
- Default branch: main
- Latest release: v1.0.4 (2026-05-10)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-05-18
- Final URL: https://github.com/gastownhall/beads

## Description
Beads - A memory upgrade for your coding agent

## README

# bd - Beads

**Distributed graph issue tracker for AI agents, powered by [Dolt](https://github.com/dolthub/dolt).**

**Platforms:** macOS, Linux, Windows, FreeBSD

**Docs:** https://gastownhall.github.io/beads/

Beads provides a persistent, structured memory for coding agents. It replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context.

### ⚡ Quick Start

```bash
# Install beads CLI (system-wide - don't clone this repo into your project)
curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash

# Initialize in YOUR project
cd your-project
bd init

# Optional: install richer instructions for your agent
bd setup codex    # Codex CLI - creates/updates AGENTS.md
bd setup claude   # Claude Code - installs hooks/settings
bd setup factory  # Factory.ai Droid - creates/updates AGENTS.md
```

`bd init` creates or updates `AGENTS.md` by default so agents can discover the beads workflow. It skips agent files only when you pass `--skip-agents` or `--stealth`, or when you configure a custom agent file. Use `bd setup --list` to see supported integrations.

### 🛠 Features

* **Dolt-Powered:** Version-controlled SQL database with cell-level merge, native branching, and built-in sync via Dolt remotes.
* **Agent-Optimized:** JSON output, dependency tracking, and auto-ready task detection.
* **Zero Conflict:** Hash-based IDs (`bd-a1b2`) prevent merge collisions in multi-agent/multi-branch workflows.
* **Compaction:** Semantic "memory decay" summarizes old closed tasks to save context window.
* **Messaging:** Message issue type with threading (`--thread`), ephemeral lifecycle, and mail delegation.
* **Graph Links:** `relates_to`, `duplicates`, `supersedes`, and `replies_to` for knowledge graphs.

### 📖 Essential Commands

| Command | Action |
| --- | --- |
| `bd ready` | List tasks with no open blockers. |
| `bd create "Title" -p 0` | Create a P0 task. |
| `bd update <id> --claim` | Atomically claim a task (sets assignee + in_progress). |
| `bd dep add <child> <parent>` | Link tasks (blocks, related, parent-child). |
| `bd show <id>` | View task details and audit trail. |
| `bd prime` | Print agent workflow context and persistent memories. |
| `bd remember "insight"` | Store project memory that `bd prime` injects later. |

### 🔗 Hierarchy & Workflow

Beads supports hierarchical IDs for epics:
* `bd-a3f8` (Epic)
* `bd-a3f8.1` (Task)
* `bd-a3f8.1.1` (Sub-task)

**Stealth Mode:** Run `bd init --stealth` to use Beads locally without committing files to the main repo.

**Contributor vs Maintainer:** Contributors can run `bd init --contributor` to route planning issues to a separate repo. Maintainers are auto-detected via SSH URLs or HTTPS with credentials.

### 📦 Installation

```bash
brew install beads           # macOS / Linux (recommended)
npm install -g @beads/bd     # Node.js users
```

Other methods: install script | go install | from source | Windows | Arch AUR

### 💾 Storage Modes

**Embedded Mode (default):** Dolt runs in-process — no external server needed. Data lives in `.beads/embeddeddolt/`. Single-writer only (file locking enforced). Recommended for most users.

**Server Mode:** Connects to an external `dolt sql-server`. Data lives in `.beads/dolt/`. Supports multiple concurrent writers.

| Flag | Env Var | Default |
|------|---------|---------|
| `--server-host` | `BEADS_DOLT_SERVER_HOST` | `127.0.0.1` |
| `--server-port` | `BEADS_DOLT_SERVER_PORT` | `3307` |
| `--server-socket` | `BEADS_DOLT_SERVER_SOCKET` | (none; uses TCP) |
| `--server-user` | `BEADS_DOLT_SERVER_USER` | `root` |

**Unix domain sockets:** Use `--server-socket` to connect via a Unix socket — useful in sandboxed environments (e.g., Claude Code) where file-level access control is simpler than network allowlists.

### 🚀 Git-Free Usage

```bash
export BEADS_DIR=/path/to/your/project/.beads
bd init --quiet --stealth
bd create "Fix auth bug" -p 1 -t bug
bd ready --json
bd update bd-a1b2 --claim
bd prime
bd close bd-a1b2 "Fixed"
```

Useful for non-git VCS (Sapling, Jujutsu), monorepos, CI/CD, and evaluation/testing.

## Docs

### docs/ARCHITECTURE.md

bd's core design enables a distributed, Dolt-powered issue tracker. The architecture has two synchronized layers:

**CLI Layer:** `bd create`, `list`, `update`, `close`, `ready`, `show`, `dep`, `sync`, and more. All commands support `--json` for programmatic use.

**Dolt Database:** Version-controlled SQL database with cell-level merge. Issues, dependencies, labels, comments, events. Automatic Dolt commits on every write. Native push/pull to Dolt remotes.

**Why Dolt?** Millisecond queries with full SQL support. Native version control — every write is automatically committed to Dolt history (complete audit trail). Cell-level merge resolves conflicts automatically. Native push/pull to Dolt remotes (DoltHub, S3, GCS) with no special sync server.

**Hash-Based Collision Prevention:** Sequential IDs cause collisions when multiple agents create issues concurrently. Beads uses hash-based IDs derived from random UUIDs (`bd-a1b2`, `bd-f14c`) ensuring uniqueness across branches. IDs start at 4 chars and grow progressively as the database grows. Content hashing: same ID + different content = update; same ID + same content = skip.

**Data Types:**

| Type | Description | Key Fields |
|------|-------------|------------|
| Issue | Work item | ID, Title, Description, Status, Priority, Type |
| Dependency | Relationship | FromID, ToID, Type (blocks/related/parent-child/discovered-from) |
| Label | Tag | Name, Color, Description |
| Comment | Discussion | IssueID, Author, Content, Timestamp |
| Event | Audit trail | IssueID, Type, Data, Timestamp |

**Dependency Types:**

| Type | Semantic | Affects `bd ready`? |
|------|----------|---------------------|
| `blocks` | Issue X must close before Y starts | Yes |
| `parent-child` | Hierarchical (epic/subtask) | Yes (children blocked if parent blocked) |
| `related` | Soft link for reference | No |
| `discovered-from` | Found during work on parent | No |

**Status Flow:** `open → in_progress → closed` (reopen supported)

**Issue Types:** `bug`, `feature`, `task`, `epic`, `chore`, `message`, `merge-request`, `molecule`, `gate`, `agent`, `role`, `convoy`

**Molecules and Wisps:** Molecules are template work items that define structured workflows. When spawned, they create wisps — ephemeral child issues tracking execution steps. Wisps are intentionally local-only (never synced) and hard-deleted when squashed into a permanent digest issue.

**Directory Structure:**
```
.beads/
├── dolt/             # Dolt database, sql-server.pid, sql-server.log (gitignored)
├── metadata.json     # Backend config (local, gitignored)
└── config.yaml       # Project config (optional)
```

**Key Code Paths:**
| Area | Files |
|------|-------|
| CLI entry | `cmd/bd/main.go` |
| Storage interface | `internal/storage/storage.go` |
| Dolt implementation | `internal/storage/dolt/` |
| RPC protocol | `internal/rpc/protocol.go`, `server_*.go` |
| Export logic | `cmd/bd/export.go` |
| Backup restore | `cmd/bd/backup_restore.go` |
| Issue bootstrap/migration | `cmd/bd/init.go` |

### docs/SETUP.md (excerpt)

The `bd setup` command uses a recipe-based architecture to configure beads with AI coding tools. Built-in recipes:

| Recipe | Path | Integration Type |
|--------|------|-----------------|
| `cursor` | `.cursor/rules/beads.mdc` | Rules file |
| `claude` | `~/.claude/settings.json` + `CLAUDE.md` | SessionStart/PreCompact hooks + minimal section |
| `copilot` | `.copilot-plugin/plugin.json` + `.github/copilot-instructions.md` | native Copilot plugin hooks + repository instructions |
| `gemini` | `~/.gemini/settings.json` + `GEMINI.md` | SessionStart/PreCompress hooks + minimal section |
| `factory` | `AGENTS.md` | Marked section |
| `codex` | `.agents/skills/beads/SKILL.md` + `AGENTS.md` | Beads agent skill + generated skill guidance |
| `mux` | `AGENTS.md` | Marked section |
| `aider` | `.aider.conf.yml` + `.aider/` | Multi-file config |

**Profiles:**
- `full` — used by Factory, Codex, Mux, OpenCode: complete command reference in instruction files
- `minimal` — used by Claude Code, GitHub Copilot CLI, Gemini CLI: pointer to `bd prime` only

`bd prime` is the single source of truth for operational workflow commands; hook-enabled agents (Claude, Copilot, Gemini) use it as the primary integration surface.

### AGENTS.md (excerpt)

This file references AGENT_INSTRUCTIONS.md for full instructions. Key sections: Issue Tracking, Development Guidelines, Project Scope, Visual Design System, Contributor Protection, Maintainer PR Guidelines.

**Storage Boundary:** Beads talks to storage through a driver interface (`dolthub/driver` for Dolt). Do not add beads-side flocks, engine introspection, storage-specific retry or crash-recovery logic, or public SDK return types that leak driver internals.

**Agent Warning:** DO NOT use `bd edit` — it opens an interactive editor ($EDITOR). Use `bd update` with flags instead.

## Top-level structure

```
beads.go                  # CLI entry point
beads_cgo.go / beads_nocgo.go  # CGO/non-CGO build variants
cmd/                      # Cobra command implementations (bd create, list, update, close, etc.)
internal/                 # Core logic: storage, types, rpc, recipes
docs/                     # Extensive documentation (60+ files)
  ARCHITECTURE.md         # Data model, sync mechanism, component overview
  SETUP.md                # Agent/IDE integration recipe system
  INSTALLING.md           # Full installation guide
  DOLT.md                 # Dolt backend details
  SYNC_CONCEPTS.md        # Sync architecture
  FAQ.md                  # Common questions
  ADVANCED.md             # Advanced features
  COMMUNITY_TOOLS.md      # Community-built UIs, extensions, integrations
  CLI_REFERENCE.md        # Full CLI reference
examples/                 # Integration examples (bash-agent, python-agent, multi-phase-development, etc.)
scripts/                  # Install scripts and utilities
.claude/                  # Claude Code integration files
.agent/                   # Agent instruction files
.claude-plugin/           # Claude plugin configuration
integrations/             # Third-party integration configs
AGENTS.md                 # Agent instructions (compatibility file; see AGENT_INSTRUCTIONS.md)
AGENT_INSTRUCTIONS.md     # Full agent workflow instructions
CLAUDE.md                 # Claude Code-specific instructions
CHANGELOG.md              # Version history
CONTRIBUTING.md           # Contribution guidelines
```
