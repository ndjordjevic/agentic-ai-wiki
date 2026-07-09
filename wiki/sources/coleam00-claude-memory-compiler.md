---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/coleam00/claude-memory-compiler
tags:
  - personal-knowledge-base
  - karpathy-llm-kb
  - claude-code-hooks
  - claude-agent-sdk
  - index-guided-retrieval
  - conversation-memory
  - no-rag
  - session-compaction
related:
  - 6eanut-llm-wiki
  - hilash-cabinet
  - forrestchang-andrej-karpathy-skills
  - langchain-ai-openwiki
  - gitlawb-openclaude
  - coleam00-helpline
  - coleam00-archon
  - supermemory.ai
  - kepano-obsidian-skills
  - shareai-lab-learn-claude-code
product: claude-memory-compiler
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`coleam00/claude-memory-compiler` (1.2k+ stars, Python) turns your own Claude Code conversations into a self-maintaining personal knowledge base — adapted from Andrej Karpathy's LLM Knowledge Base pattern but sourcing raw material from session transcripts instead of clipped web articles. Claude Code hooks capture conversations on session end and before auto-compaction; a background `flush.py` uses the Claude Agent SDK to extract decisions and lessons into daily logs; `compile.py` compiles those logs into cross-referenced `knowledge/` articles; and `session-start.py` injects the index back into every new session. Retrieval is index-guided markdown lookup — no vector DB, no embeddings — at personal scale (50–500 articles).

_All claims below are sourced from ../../raw/github/coleam00-claude-memory-compiler.md unless otherwise noted._

## What it does

The project implements a full **conversation → memory → retrieval** loop for Claude Code projects. Instead of manually curating notes or relying on context-window summarization alone, the system treats daily conversation logs as immutable source code, an LLM compiler (`compile.py` via Claude Agent SDK) as the build step, and structured `knowledge/` articles as the executable output. `query.py` answers questions by reading `knowledge/index.md` first, then 3–10 relevant articles — the same index-first retrieval insight Karpathy advocates and that [[6eanut-llm-wiki]] implements for external documents. Unlike [[gitlawb-openclaude]]'s memory flush (which requires separate API billing), personal Claude Agent SDK use here runs on an existing Claude Max/Team/Enterprise subscription.

## Installation

Tell a coding agent (or follow manually):

```bash
git clone https://github.com/coleam00/claude-memory-compiler
cd claude-memory-compiler
uv sync
# Copy or merge .claude/settings.json hooks into your project
```

Hooks activate on the next Claude Code session. Conversations accumulate in `daily/`; after 6 PM local time the next flush auto-triggers compilation, or run `uv run python scripts/compile.py` manually.

## Key features

- **Automatic capture** — `SessionEnd` and `PreCompact` hooks copy JSONL transcripts and spawn detached `flush.py`; PreCompact is critical for long sessions that auto-compact multiple times before close.
- **LLM-curated extraction** — `flush.py` calls Claude Agent SDK with `allowed_tools=[]` so the model decides what's worth saving (structured bullets or `FLUSH_OK`), not a fixed template.
- **Three article types** — `knowledge/concepts/` (atomic facts), `connections/` (cross-cutting synthesis), `qa/` (filed answers from `--file-back` queries).
- **Index-guided retrieval** — no RAG at personal scale; `query.py` loads index + articles and synthesizes with `[[wikilinks]]`.
- **Seven lint checks** — broken links, orphans, stale sources, missing backlinks, sparse articles, and LLM-judged contradictions (`--structural-only` is free).
- **End-of-day auto-compile** — after 6 PM, changed daily logs trigger detached `compile.py` via hash comparison in `state.json`.
- **Obsidian-compatible** — pure markdown wikilinks; works with [[kepano-obsidian-skills]] vault conventions.

## Architecture

Three-layer compiler model:

```
daily/ (immutable logs)  →  LLM compiler (compile.py / flush.py)  →  knowledge/ (articles + index.md)
```

**Hook layer** (`hooks/`):
- `session-start.py` — pure local I/O; injects up to 20k chars of index + recent daily log via `additionalContext` JSON (no API call).
- `session-end.py` / `pre-compact.py` — copy transcript to temp file, spawn detached `flush.py`; recursion guard via `CLAUDE_INVOKED_BY`; 60-second dedup per session.

**Script layer** (`scripts/`):
- `flush.py` — background memory extraction; sets `CLAUDE_INVOKED_BY=memory_flush`; appends to `daily/YYYY-MM-DD.md`.
- `compile.py` — async Agent SDK with Read/Write/Edit/Glob/Grep tools, `max_turns=30`, incremental SHA-256 tracking.
- `query.py` — full KB in context; optional `--file-back` compounds knowledge into `qa/`.
- `lint.py` — structural + optional LLM contradiction check; reports to `reports/`.

**State** — `state.json` (ingestion hashes, costs) and `last-flush.json` (dedup) are gitignored and regenerated.

Scaling threshold: ~2,000+ articles when index exceeds context window — then add hybrid RAG (Karpathy cites `qmd`).

## Example usage

```bash
uv run python scripts/compile.py                    # compile new/changed daily logs
uv run python scripts/compile.py --all              # force full recompile
uv run python scripts/query.py "What auth patterns do I use?"
uv run python scripts/query.py "What's my error handling strategy?" --file-back
uv run python scripts/lint.py                       # all checks
uv run python scripts/lint.py --structural-only     # free structural only
```

## Maintenance status

1,225 stars, 310 forks, Python, default branch `main`, no tagged releases, last pushed 2026-04-06. Authored by Cole Medin ([[coleam00-helpline]], [[coleam00-archon]], [[coleam00-harness-engineering-demo]]) as a drop-in personal-memory layer complementary to repo-documentation tools like [[langchain-ai-openwiki]] and skill-based wikis like [[6eanut-llm-wiki]]. Estimated per-operation costs documented in AGENTS.md: ~$0.02–0.05 per session flush, ~$0.45–0.65 per daily compile.
