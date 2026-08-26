---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/xhluca/session-migrate
tags: [session-portability, native-transcript-format, harness-migration, content-free-manifest, catalog-search, lossless-conversion, python-cli]
related:
  - max-sixty-worktrunk
  - tmuxai.dev
  - pi.dev
product: session-migrate
detail_level: standard
created: 2026-08-26
updated: 2026-08-26
---

session-migrate (`smigrate`) is a Python CLI (53 stars, MIT, v0.8.0) that moves a native coding-agent conversation — the whole resumable session, not just its text — between Claude Code, Codex, Pi, Oh My Pi, OpenCode, GitHub Copilot CLI, Antigravity CLI, Cursor Agent, Mistral Vibe, Muse Code, Qwen Code, and Kimi Code. It matters for this wiki as the missing piece in the multi-harness workflow other tools here assume is possible: switching agents mid-task without starting the conversation over.

_All claims below are sourced from ../../raw/github/xhluca-session-migrate.md unless otherwise noted._

## What it does

`smigrate transfer SESSION_ID --from claude --to codex --cwd "$PWD"` reads a session in its native storage format, projects it into a small ordered "portable event timeline," and writes a new, independent, resumable session in the target agent's own native format (e.g. `codex resume NEW_SESSION_UUID` immediately works). It also ships `inspect` (structural metadata without printing message text), `convert` (write a standalone artifact + manifest without installing anywhere), `import` (convert and install into a target's home directory, collision-checked, `--dry-run` supported), and a private local `catalog` that indexes session titles/IDs across all configured agent homes so a session can be found by fuzzy title search (`catalog search "oauth refresh"`) instead of by UUID. All 12 formats are both readable and writable, giving 144 ordered routes including same-format "portable rewrite."

## Key features

- **Content-free manifests** — every `convert`/`import`/`transfer` emits a JSON summary (`dropped_events`, `warnings`, hashes, record counts) with no message, tool, or media bodies, so operators can audit what was lost without re-exposing the transcript.
- **Bounded, identity-checked readers** — JSON/JSONL sources (Claude, Codex, Pi, OMP, Copilot, Vibe, Muse, Qwen, Kimi) cap total bytes, record count, JSON nesting, and media size, and validate file identity before/after reading so an actively-appending or truncated session fails safely instead of corrupting output.
- **SQLite/protobuf clean-room readers** — Antigravity and Cursor are read via a consistent SQLite backup (including WAL) plus independently-written, bounded protobuf decoders; unsupported native constructs become reason-specific opaque events rather than being silently dropped.
- **No-clobber native installation** — new files are mode `0600`, new state dirs `0700`; existing permissions are never changed and the source session is never modified or overwritten.
- **Exact version pinning** — writers are pinned to specific host agent builds/releases; a source or target declaring a different version is flagged (`unvalidated_source_version` / `unvalidated_target_version`) rather than silently proceeding.
- **`--title` catalog lookup** — `transfer --title "parser refactor" --from claude --to copilot` resolves an ambiguous human title through the local catalog instead of requiring the raw session UUID.

## Architecture

The pipeline is native source → bounded parse/identity check → ordered portable event timeline (kinds: message, tool call, tool result, thinking, compaction, context, opaque; roles: user, assistant, system, tool) → target-specific projection with loss accounting → validated native target + manifest. `formats/*.py` holds one bounded reader/writer per agent (`claude.py`, `codex.py`, `pi.py`, `omp.py`, `opencode.py`, `copilot.py`, `antigravity.py`, `cursor.py`, `vibe.py`, `muse.py`, `qwen.py`, `kimi.py`); `model.py` defines the neutral `Session`/`Event` types; `inspection.py` does content-free format detection; `discovery.py` performs exact native-ID lookup without trusting mutable indexes; `catalog.py` is the private multi-root SQLite metadata index; `conversion.py` dispatches, rewrites, validates, and installs; `cli.py` exposes the commands and JSON/error contracts. OpenCode is treated as a **virtual** source: the catalog reads only its native `opencode.db` metadata, and a selected session is exported through the exact pinned official `opencode export` CLI rather than the migrator ever touching OpenCode's SQLite directly. Same-format migration (e.g. Claude → Claude) deliberately still runs the full reader→model→writer pipeline and allocates a new target identity — it is a portable rewrite, not a byte-copy, and does not keep the two sessions in sync.

## Installation

```bash
curl -LsSf https://session-migrate.github.io/install.sh | sh
# or
uv tool install session-migrate
# or
pipx install session-migrate
```

Requires Python 3.11+ and Linux. The full command is `session-migrate`; `smigrate` is the shorthand. `uv tool upgrade session-migrate` upgrades an existing install.

## Example usage

```bash
# Inspect a transcript's structure without printing its content
smigrate inspect ~/.claude/projects/-work/SESSION.jsonl

# Move a Claude session into Codex and resume it from the same directory
smigrate transfer SESSION_UUID --from claude --to codex --cwd "$PWD"
codex resume NEW_SESSION_UUID

# Find an older session by title instead of UUID, then migrate it
smigrate catalog refresh
smigrate catalog search "oauth refresh" --format claude
smigrate transfer --title "oauth refresh" --from claude --to pi
```

A coding agent can also be handed the procedure directly: `Follow https://session-migrate.github.io/llms.txt to migrate a session from [SOURCE] to [TARGET]. Session: [UUID OR TITLE]` — sandbox-tested with both Claude Code and Codex.

## When to use

Reach for session-migrate when a long-running, tool-heavy conversation needs to continue in a different coding agent — evaluating a new harness mid-task, working around a source agent's limitation, or standardizing session storage across a team that uses several CLIs. It is not a substitute for the agents' own resume mechanisms and does not synchronize two live sessions; each migration produces one new, independent target session. Cursor support is explicitly experimental (text-only, pinned to one exact Linux build) and should not be relied on for tool-call or image fidelity.

## Maintenance status

53 stars, 4 forks, MIT license, default branch `main`, latest release v0.8.0 (2026-08-25), pushed as recently as 2026-08-26. Primary language Python. Homepage: session-migrate.github.io. Contribution requires sanitized native-shaped fixtures and a real native-resume oracle for any new format adapter — vendor code, binaries, or real transcripts are explicitly disallowed for the clean-room Antigravity/Cursor work.

## Ecosystem

session-migrate's data-and-credential boundary is notable: it never reads login stores, cookies, API keys, MCP connections, or workspace files, and performs no redaction or secret scanning — a secret already embedded in a migrated message or tool result is copied verbatim into the target. It complements this wiki's other terminal/session tooling — [[max-sixty-worktrunk]] and [[tmuxai.dev]] manage *where* an agent session runs (parallel worktrees, tmux panes), while session-migrate manages *which agent* a given session's history can resume inside, including [[pi.dev]] as one of its twelve supported targets. Antigravity and Cursor's reverse-engineered formats are published as separate companion research repos (`xhluca/antigravity-session-interoperability`, `xhluca/cursor-session-interoperability`).
