---
type: source
source_url: https://github.com/coleam00/claude-memory-compiler
tags: [persistent-memory, claude-code-hooks, claude-agent-sdk, knowledge-base, index-guided-retrieval, session-amnesia, daily-logs, compiler-pattern]
related:
  - "[[hilash-cabinet]]"
  - "[[runcabinet.com]]"
  - "[[gsd-build-get-shit-done]]"
product: claude-memory-compiler
detail_level: standard
created: 2026-04-25
updated: 2026-04-27
---

`coleam00/claude-memory-compiler` is a Python tool that gives Claude Code persistent, session-spanning memory by hooking into Claude Code's lifecycle events (SessionStart, SessionEnd, PreCompact) to automatically capture conversation transcripts, extract key decisions and lessons via the Claude Agent SDK, and compile them into a structured, cross-referenced markdown knowledge base — inspired directly by Karpathy's LLM Knowledge Base architecture.

_All claims below are sourced from ../../raw/github/coleam00-claude-memory-compiler.md unless otherwise noted._

## What It Does

Solves the statelessness problem of AI coding assistants: every Claude Code session starts with no memory of past work. The system captures each conversation, distills it into a daily log, compiles those logs into concept articles, and injects the knowledge index at the start of every future session — creating a compounding loop where each conversation makes the assistant smarter for the next one.

## Installation

```bash
# Tell your agent:
"Clone https://github.com/coleam00/claude-memory-compiler into this project.
Set up the Claude Code hooks so my conversations automatically get captured..."
```

The agent clones the repo, runs `uv sync`, and merges `.claude/settings.json` into your project config. Hooks activate on the next Claude Code session open. Requires Python 3.12+, managed via `uv`.

Dependencies: `claude-agent-sdk>=0.1.29`, `python-dotenv>=1.0.0`, `tzdata>=2024.1`. No API key needed — uses Claude Code's built-in credentials at `~/.claude/.credentials.json`. Personal use of the Claude Agent SDK is covered under Claude Max/Team/Enterprise subscriptions.

## Key Features

- **Zero-friction capture**: hooks fire automatically on session end and pre-compaction; no manual steps required
- **Index-guided retrieval (no RAG)**: at personal KB scale (50-500 articles), LLM reading a structured `index.md` outperforms vector similarity; RAG only needed at ~2,000+ articles
- **End-of-day auto-compilation**: after 6 PM local time, the next session flush automatically triggers `compile.py` if today's daily log has changed (SHA-256 hash tracking in `state.json`)
- **Compounding Q&A**: `query.py --file-back` saves answers back to the knowledge base, making future queries smarter
- **Obsidian-compatible**: pure markdown with `[[wikilinks]]`; point an Obsidian vault at `knowledge/` for graph view and backlinks
- **Structural lint (free)**: 6 of 7 health checks are purely structural (no LLM, no cost)

## Architecture

The system uses a compiler analogy:

```
daily/      = source code   (conversation logs — immutable, append-only)
LLM         = compiler      (Claude Agent SDK extracts and organizes)
knowledge/  = executable    (structured, queryable knowledge base)
lint        = test suite    (7 health checks)
queries     = runtime       (index-guided retrieval)
```

**Three layers:**

1. **`daily/`** — raw daily logs, one file per day, append-only. Each session's flush writes a structured block: context, key exchanges, decisions made, lessons learned, action items.

2. **`knowledge/`** — LLM-owned compiled output:
   - `index.md` — master catalog, primary retrieval mechanism (read first on any query)
   - `log.md` — append-only build log of every compile/query/lint
   - `concepts/` — atomic knowledge articles (one per concept)
   - `connections/` — cross-cutting insights linking 2+ concepts
   - `qa/` — filed query answers for compounding knowledge

3. **`AGENTS.md`** — the compiler specification; tells the LLM exactly how to compile, query, and lint. Designed so an AI agent can understand, modify, or rebuild the entire system from this file alone.

## Hook System

Three Claude Code hooks in `.claude/settings.json`:

| Hook | Script | Role |
|---|---|---|
| `SessionStart` | `hooks/session-start.py` | Injects `knowledge/index.md` + latest daily log into session context (local I/O only, <1s, max 20k chars) |
| `SessionEnd` | `hooks/session-end.py` | Copies JSONL transcript to temp file, spawns `flush.py` as detached background process |
| `PreCompact` | `hooks/pre-compact.py` | Same as SessionEnd; fires before auto-compaction to catch context before summarization discards it |

**Why PreCompact matters**: long sessions trigger multiple auto-compactions before session end. Without it, intermediate context is lost. Guards against empty `transcript_path` (known Claude Code bug #13668).

**Detached background flush**: `flush.py` spawns fully detached (`start_new_session=True` on Mac/Linux, `DETACHED_PROCESS` on Windows) so it survives after Claude Code's hook process exits. Recursion guard: sets `CLAUDE_INVOKED_BY=memory_flush` to prevent hooks from re-firing.

**JSONL transcript parsing**: messages nested under `message` key; content can be a plain string or a list of `{"type": "text", "text": "..."}` blocks.

## Example Usage

```bash
# After setup, everything is automatic. Manual commands:
uv run python scripts/compile.py              # compile new daily logs -> knowledge articles
uv run python scripts/compile.py --all        # force recompile everything
uv run python scripts/query.py "What auth patterns do I use?"
uv run python scripts/query.py "question" --file-back  # save answer to kb
uv run python scripts/lint.py                # all 7 health checks
uv run python scripts/lint.py --structural-only  # 6 free structural checks only
```

`compile.py` uses Claude Agent SDK with `permission_mode="acceptEdits"` and `allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"]` — Claude reads the daily log and writes knowledge files directly. Cost: ~$0.45-0.65 per daily log (increases as KB grows). Total: `~$0.02-0.05` per session for flush, occasional compile at `$0.45-0.65`.

## Maintenance Status

895 stars, 233 forks, last pushed 2026-04-06. No releases; installed directly from the repo. No license specified. Active Python project maintained by coleam00.
