---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://github.com/gastownhall/beads
tags:
  - agent-task-tracking
  - distributed-issue-tracker
  - dolt-powered
  - persistent-agent-memory
  - dependency-graph
  - multi-agent-workflow
  - agent-integrations
related:
  - gsd-build-get-shit-done
  - coleam00-archon
product: beads
detail_level: standard
created: 2026-05-18
updated: 2026-05-18
---

Beads (`bd`) is a distributed, graph-based issue tracker designed as a persistent memory upgrade for AI coding agents. With 23,795 stars and an MIT license, it solves a core problem of long-horizon agent work: coding agents forget context across sessions and resort to lossy markdown task lists. Beads replaces markdown plans with a dependency-aware Dolt-powered SQL database, giving agents a structured, versioned, conflict-free task graph that persists across sessions, branches, and even across multiple concurrent agents. The project includes native integration recipes for Claude Code, GitHub Copilot CLI, Codex, Gemini CLI, [[factory.ai]], and more.

_All claims below are sourced from ../../raw/github/gastownhall-beads.md unless otherwise noted._

## What it does

Beads provides a CLI tool (`bd`) that coding agents use in place of ad-hoc markdown TODO files. Agents call `bd ready` to find unblocked tasks, `bd update <id> --claim` to atomically reserve a task, `bd create` to record new work, and `bd close` to mark completion. `bd prime` injects the full workflow context and stored project memories into the agent's active session at startup — acting as the agent's persistent knowledge layer. `bd remember "insight"` stores findings that `bd prime` will surface in future sessions.

The underlying storage is [Dolt](https://github.com/dolthub/dolt) — a version-controlled SQL database — either embedded in-process (default, single-writer) or connected to an external `dolt sql-server` (multi-writer). Every write is automatically committed to Dolt history, providing a complete audit trail. Teams sync across machines via `bd dolt push` / `bd dolt pull` to Dolt remotes (DoltHub, S3, GCS, filesystem).

## Key features

- **Hash-based IDs:** IDs like `bd-a1b2` are derived from random UUIDs, eliminating sequential-ID collisions when multiple agents create tasks concurrently on different branches.
- **Dependency graph:** `bd dep add <child> <parent>` models blocking, parent-child (epic/subtask), related, and discovered-from relationships. `bd ready` surfaces only tasks with no open blockers.
- **Hierarchical epics:** IDs scale as `bd-a3f8` → `bd-a3f8.1` → `bd-a3f8.1.1` for structured work breakdown.
- **Compaction:** Semantic "memory decay" summarizes old closed tasks, preserving context-window budget over long projects.
- **Molecules and wisps:** Molecules are template workflows that spawn ephemeral local-only wisp issues for execution steps; wisps are squashed into a permanent digest when done and never sync to remotes.
- **Messaging:** A `message` issue type with threading (`--thread`) and mail delegation for inter-agent communication.
- **Stealth and contributor modes:** `bd init --stealth` keeps beads local without committing to the main repo; `bd init --contributor` routes planning issues to a separate repo, keeping forks clean.
- **Git-free operation:** `BEADS_DIR` bypasses git repo discovery, enabling use in non-git VCS, monorepos, CI/CD, and ephemeral evaluation environments.

## Architecture

The architecture has two synchronized layers: a **CLI layer** (`cmd/bd/` Cobra commands, all supporting `--json`) and a **Dolt database** (`.beads/dolt/` or `.beads/embeddeddolt/`). Every write is an immediate Dolt commit; reads run directly against the local database via SQL.

Hash-based collision prevention is the key design that enables distributed operation: IDs are derived from random UUIDs, starting at 4 chars and growing progressively. Merge logic compares content hashes — same hash means skip, different hash means update, no match means create — so all agents converge to the same state without central coordination.

The data model covers Issues, Dependencies, Labels, Comments, and Events. Storage is backed by `internal/storage/dolt/`; the RPC protocol at `internal/rpc/protocol.go` handles server-mode multi-writer access. Molecules (template workflows) create local-only wisps that are hard-deleted on squash, keeping sync history clean.

## Installation

```bash
brew install beads           # macOS / Linux (recommended)
npm install -g @beads/bd     # Node.js users
curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash
```

After install, in any project:

```bash
bd init          # creates .beads/ database and writes AGENTS.md
bd setup claude  # installs SessionStart/PreCompact hooks for Claude Code
bd setup copilot # installs Copilot CLI plugin + .github/copilot-instructions.md
bd setup codex   # installs Beads skill + AGENTS.md guidance for Codex
```

## Example usage

```bash
# Agent workflow bootstrap
bd prime                          # inject workflow context at session start

# Task discovery and claiming
bd ready                          # list tasks with no open blockers
bd update bd-a1b2 --claim         # atomically mark in_progress + set assignee

# Task creation and linking
bd create "Implement OAuth" -p 1  # create a P1 task
bd dep add bd-f14c bd-a1b2        # f14c blocks a1b2

# Persistent memory
bd remember "Use snake_case for all DB column names"

# Close and review
bd close bd-a1b2 "Implemented and tested"
bd show bd-a1b2                   # view task details and audit trail
```

For Git-free use, set `BEADS_DIR` and add `--stealth` to `bd init` to disable all git integration.

## Maintenance status

23,795 stars, 1,576 forks, MIT license, latest release v1.0.4 (2026-05-10). Written in Go. Actively maintained with a recent push on 2026-05-18. Extensive documentation (60+ files in `docs/`), community tools directory, and integration recipes for 10+ AI coding environments. Docs hosted at https://gastownhall.github.io/beads/.

## Ecosystem

Beads integrates with Claude Code (SessionStart/PreCompact hooks via `bd setup claude`), GitHub Copilot CLI (native plugin via `bd setup copilot`), Gemini CLI, [[factory.ai]], Codex, Cursor, Windsurf, Aider, and more via the recipe system. The `full` profile writes the complete command reference into agent instruction files; the `minimal` profile writes a pointer to `bd prime` for hook-enabled agents. Community-built UIs, extensions, and native apps are listed in `docs/COMMUNITY_TOOLS.md`. Dolt remotes (DoltHub, S3, GCS) handle sync without a dedicated server. An MCP/npm package (`@beads/bd`) and PyPI package (`beads-mcp`) extend reach to Python and Node.js environments.
