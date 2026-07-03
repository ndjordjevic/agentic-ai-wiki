# coleam00/claude-memory-compiler

## Metadata
- Stars: 1225
- Primary language: Python
- Default branch: main
- Latest release: none
- License: (not specified in repo metadata)
- Homepage: (none)
- Fetched: 2026-07-03
- Final URL: https://github.com/coleam00/claude-memory-compiler

## Description
Give Claude Code a memory that evolves with your codebase. Hooks automatically capture sessions, the Claude Agent SDK extracts key decisions and lessons, and an LLM compiler organizes everything into structured, cross-referenced knowledge articles - inspired by Karpathy's LLM Knowledge Base architecture.

## README
# LLM Personal Knowledge Base

**Your AI conversations compile themselves into a searchable knowledge base.**

Adapted from [Karpathy's LLM Knowledge Base](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) architecture, but instead of clipping web articles, the raw data is your own conversations with Claude Code. When a session ends (or auto-compacts mid-session), Claude Code hooks capture the conversation transcript and spawn a background process that uses the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk) to extract the important stuff - decisions, lessons learned, patterns, gotchas - and appends it to a daily log. You then compile those daily logs into structured, cross-referenced knowledge articles organized by concept. Retrieval uses a simple index file instead of RAG - no vector database, no embeddings, just markdown.

Anthropic has clarified that personal use of the Claude Agent SDK is covered under your existing Claude subscription (Max, Team, or Enterprise) - no separate API credits needed. Unlike OpenClaw, which requires API billing for its memory flush, this runs on your subscription.

## Quick Start

Tell your AI coding agent:

> "Clone https://github.com/coleam00/claude-memory-compiler into this project. Set up the Claude Code hooks so my conversations automatically get captured into daily logs, compiled into a knowledge base, and injected back into future sessions. Read the AGENTS.md for the full technical reference on how everything works."

The agent will:
1. Clone the repo and run `uv sync` to install dependencies
2. Copy `.claude/settings.json` into your project (or merge the hooks into your existing settings)
3. The hooks activate automatically next time you open Claude Code

From there, your conversations start accumulating. After 6 PM local time, the next session flush automatically triggers compilation of that day's logs into knowledge articles. You can also run `uv run python scripts/compile.py` manually at any time.

## How It Works

```
Conversation -> SessionEnd/PreCompact hooks -> flush.py extracts knowledge
    -> daily/YYYY-MM-DD.md -> compile.py -> knowledge/concepts/, connections/, qa/
        -> SessionStart hook injects index into next session -> cycle repeats
```

- **Hooks** capture conversations automatically (session end + pre-compaction safety net)
- **flush.py** calls the Claude Agent SDK to decide what's worth saving, and after 6 PM triggers end-of-day compilation automatically
- **compile.py** turns daily logs into organized concept articles with cross-references (triggered automatically or run manually)
- **query.py** answers questions using index-guided retrieval (no RAG needed at personal scale)
- **lint.py** runs 7 health checks (broken links, orphans, contradictions, staleness)

## Key Commands

```bash
uv run python scripts/compile.py                    # compile new daily logs
uv run python scripts/query.py "question"            # ask the knowledge base
uv run python scripts/query.py "question" --file-back # ask + save answer back
uv run python scripts/lint.py                        # run health checks
uv run python scripts/lint.py --structural-only      # free structural checks only
```

## Why No RAG?

Karpathy's insight: at personal scale (50-500 articles), the LLM reading a structured `index.md` outperforms vector similarity. The LLM understands what you're really asking; cosine similarity just finds similar words. RAG becomes necessary at ~2,000+ articles when the index exceeds the context window.

## Technical Reference

See **[AGENTS.md](AGENTS.md)** for the complete technical reference: article formats, hook architecture, script internals, cross-platform details, costs, and customization options. AGENTS.md is designed to give an AI agent everything it needs to understand, modify, or rebuild the system.

## Docs

### AGENTS.md (schema and technical reference)

Key architecture layers:
- `daily/` — immutable conversation logs (append-only source material)
- `knowledge/` — LLM-owned compiled articles (`index.md`, `log.md`, `concepts/`, `connections/`, `qa/`)
- `AGENTS.md` — compiler specification for the LLM

Compiler analogy:
```
daily/          = source code    (your conversations - the raw material)
LLM             = compiler       (extracts and organizes knowledge)
knowledge/      = executable     (structured, queryable knowledge base)
lint            = test suite     (health checks for consistency)
queries         = runtime        (using the knowledge)
```

Hook system (`.claude/settings.json`):
- **SessionStart** → `session-start.py` injects `knowledge/index.md` + recent daily log (max 20k chars, no API calls)
- **SessionEnd** → `session-end.py` copies JSONL transcript, spawns detached `flush.py`
- **PreCompact** → `pre-compact.py` same as SessionEnd; safety net before auto-compaction (Claude Code bug #13668 guard for empty transcript_path)

`flush.py` background process:
1. Sets `CLAUDE_INVOKED_BY=memory_flush` (recursion guard)
2. Reads pre-extracted conversation context from temp `.md` file
3. Skips empty context or duplicate flush within 60 seconds
4. Calls Claude Agent SDK (`query()` with `allowed_tools=[]`, `max_turns=2`)
5. Appends structured bullets or `FLUSH_OK` to `daily/YYYY-MM-DD.md`
6. After 6 PM local (`COMPILE_AFTER_HOUR = 18`), if daily log hash changed, spawns detached `compile.py`

`compile.py`:
- Uses Claude Agent SDK async streaming `query()` with tools Read/Write/Edit/Glob/Grep, `permission_mode="acceptEdits"`, `max_turns=30`
- Incremental via SHA-256 hashes in `state.json`
- Cost: ~$0.45-0.65 per daily log

`query.py`:
- Loads entire KB (index + all articles) — index-guided, no RAG
- `--file-back` creates `knowledge/qa/` article (compounding loop)

`lint.py` — seven checks:
1. Broken links
2. Orphan pages
3. Orphan sources (uncompiled daily logs)
4. Stale articles
5. Missing backlinks
6. Sparse articles (<200 words)
7. Contradictions (LLM judgment; `--structural-only` skips)

Article types:
- `knowledge/concepts/` — atomic knowledge
- `knowledge/connections/` — cross-cutting links between 2+ concepts
- `knowledge/qa/` — filed query answers

Dependencies (`pyproject.toml`):
- `claude-agent-sdk>=0.1.29`
- `python-dotenv>=1.0.0`
- `tzdata>=2024.1`
- Python 3.12+, managed by uv
- No API key — uses Claude Code credentials at `~/.claude/.credentials.json`

Costs (from AGENTS.md):
| Operation | Cost |
|-----------|------|
| Compile one daily log | $0.45-0.65 |
| Query (no file-back) | ~$0.15-0.25 |
| Query (with file-back) | ~$0.25-0.40 |
| Full lint (with contradictions) | ~$0.15-0.25 |
| Structural lint only | $0.00 |
| Memory flush (per session) | ~$0.02-0.05 |

Scaling note: at ~2,000+ articles, add hybrid RAG; Karpathy recommends `qmd` by Tobi Lutke.

Obsidian integration: pure markdown with `[[wikilinks]]` — point vault at `knowledge/`.

### pyproject.toml

```toml
[project]
name = "llm-personal-kb"
version = "0.1.0"
description = "Personal knowledge base compiled from AI conversations - inspired by Karpathy's LLM KB architecture"
requires-python = ">=3.12"
dependencies = [
    "claude-agent-sdk>=0.1.29",
    "python-dotenv>=1.0.0",
    "tzdata>=2024.1",
]
```

### .claude/settings.json

```json
{
  "hooks": {
    "SessionStart": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/session-start.py", "timeout": 15 }] }],
    "PreCompact": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/pre-compact.py", "timeout": 10 }] }],
    "SessionEnd": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/session-end.py", "timeout": 10 }] }]
  }
}
```

## Top-level structure

| Path | Type | Notes |
|---|---|---|
| `.claude/` | dir | `settings.json` — hook configuration |
| `hooks/` | dir | `session-start.py`, `session-end.py`, `pre-compact.py` — Claude Code lifecycle hooks |
| `scripts/` | dir | `compile.py`, `query.py`, `lint.py`, `flush.py`, `config.py`, `utils.py` — CLI tools |
| `AGENTS.md` | file | Full schema + technical reference for AI agents |
| `README.md` | file | Quick start and overview |
| `pyproject.toml` | file | Python dependencies (uv) |
| `uv.lock` | file | Locked dependency versions |
| `.gitignore` | file | Excludes runtime state, temp files, caches |

Runtime directories (created on use, gitignored): `daily/`, `knowledge/`, `reports/`, `scripts/state.json`, `scripts/last-flush.json`
