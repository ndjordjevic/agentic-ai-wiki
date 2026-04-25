# coleam00/claude-memory-compiler

## Metadata
- Stars: 895
- Primary language: Python
- Default branch: main
- Latest release: (none)
- License: (none)
- Homepage: (none)
- Fetched: 2026-04-25
- Final URL: https://github.com/coleam00/claude-memory-compiler

## Description
Give Claude Code a memory that evolves with your codebase. Hooks automatically capture sessions, the Claude Agent SDK extracts key decisions and lessons, and an LLM compiler organizes everything into structured, cross-referenced knowledge articles - inspired by Karpathy's LLM Knowledge Base architecture.

## README

# LLM Personal Knowledge Base

**Your AI conversations compile themselves into a searchable knowledge base.**

Adapted from [Karpathy's LLM Knowledge Base](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) architecture, but instead of clipping web articles, the raw data is your own conversations with Claude Code. When a session ends (or auto-compacts mid-session), Claude Code hooks capture the conversation transcript and spawn a background process that uses the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk) to extract the important stuff - decisions, lessons learned, patterns, gotchas - and appends it to a daily log. You then compile those daily logs into structured, cross-referenced knowledge articles organized by concept. Retrieval uses a simple index file instead of RAG - no vector database, no embeddings, just markdown.

Anthropic has clarified that personal use of the Claude Agent SDK is covered under your existing Claude subscription (Max, Team, or Enterprise) - no separate API credits needed. Unlike OpenClaw, which requires API billing for its memory flush, this runs on your subscription.

### Quick Start

Tell your AI coding agent:

> "Clone https://github.com/coleam00/claude-memory-compiler into this project. Set up the Claude Code hooks so my conversations automatically get captured into daily logs, compiled into a knowledge base, and injected back into future sessions. Read the AGENTS.md for the full technical reference on how everything works."

The agent will:
1. Clone the repo and run `uv sync` to install dependencies
2. Copy `.claude/settings.json` into your project (or merge the hooks into your existing settings)
3. The hooks activate automatically next time you open Claude Code

From there, your conversations start accumulating. After 6 PM local time, the next session flush automatically triggers compilation of that day's logs into knowledge articles. You can also run `uv run python scripts/compile.py` manually at any time.

### How It Works

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

### Key Commands

```bash
uv run python scripts/compile.py                    # compile new daily logs
uv run python scripts/query.py "question"            # ask the knowledge base
uv run python scripts/query.py "question" --file-back # ask + save answer back
uv run python scripts/lint.py                        # run health checks
uv run python scripts/lint.py --structural-only      # free structural checks only
```

### Why No RAG?

Karpathy's insight: at personal scale (50-500 articles), the LLM reading a structured `index.md` outperforms vector similarity. The LLM understands what you're really asking; cosine similarity just finds similar words. RAG becomes necessary at ~2,000+ articles when the index exceeds the context window.

### Technical Reference

See **AGENTS.md** for the complete technical reference: article formats, hook architecture, script internals, cross-platform details, costs, and customization options. AGENTS.md is designed to give an AI agent everything it needs to understand, modify, or rebuild the system.

## AGENTS.md

# AGENTS.md - Personal Knowledge Base Schema

> Adapted from Andrej Karpathy's LLM Knowledge Base architecture.
> Instead of ingesting external articles, this system compiles knowledge from your own AI conversations.

### The Compiler Analogy

```
daily/          = source code    (your conversations - the raw material)
LLM             = compiler       (extracts and organizes knowledge)
knowledge/      = executable     (structured, queryable knowledge base)
lint            = test suite     (health checks for consistency)
queries         = runtime        (using the knowledge)
```

You don't manually organize your knowledge. You have conversations, and the LLM handles the synthesis, cross-referencing, and maintenance.

### Architecture

**Layer 1: `daily/` - Conversation Logs (Immutable Source)**

Daily logs capture what happened in your AI coding sessions. These are the "raw sources" - append-only, never edited after the fact.

Each file follows this format:
```markdown
# Daily Log: YYYY-MM-DD

## Sessions

### Session (HH:MM) - Brief Title

**Context:** What the user was working on.
**Key Exchanges:** ...
**Decisions Made:** ...
**Lessons Learned:** ...
**Action Items:** ...
```

**Layer 2: `knowledge/` - Compiled Knowledge (LLM-Owned)**

The LLM owns this directory entirely. Humans read it but rarely edit it directly.

```
knowledge/
├── index.md              # Master catalog - every article with one-line summary
├── log.md                # Append-only chronological build log
├── concepts/             # Atomic knowledge articles
├── connections/          # Cross-cutting insights linking 2+ concepts
└── qa/                   # Filed query answers (compounding knowledge)
```

**Layer 3: AGENTS.md** — the schema that tells the LLM how to compile and maintain the knowledge base.

### Article Formats

**Concept articles** (`knowledge/concepts/`): one article per atomic piece of knowledge — facts, patterns, decisions, preferences, lessons. Frontmatter: `title`, `aliases`, `tags`, `sources`, `created`, `updated`. Body: 2-4 sentence core explanation, key points (bullets), details (paragraphs), related concepts (wikilinks), sources.

**Connection articles** (`knowledge/connections/`): cross-cutting synthesis linking 2+ concepts. Created when a conversation reveals a non-obvious relationship. Frontmatter: `connects`, `sources`.

**Q&A articles** (`knowledge/qa/`): filed answers from queries. Frontmatter: `question`, `consulted`, `filed`.

### Core Operations

**Compile (daily/ → knowledge/):**
1. Read daily log
2. Read `knowledge/index.md` to understand current state
3. For each piece of knowledge: update existing concept article or create new one
4. If non-obvious connection between 2+ concepts: create `connections/` article
5. Update `knowledge/index.md` and append to `knowledge/log.md`
- A single daily log may touch 3-10 knowledge articles
- Prefer updating over creating near-duplicates

**Query:**
1. Read `knowledge/index.md`
2. Identify 3-10 relevant articles, read them in full
3. Synthesize answer with `[[wikilink]]` citations
4. If `--file-back`: create `knowledge/qa/` article and update index + log
- At personal KB scale (50-500 articles), index-guided LLM outperforms RAG

**Lint (7 checks):**
1. Broken links — `[[wikilinks]]` to non-existent articles
2. Orphan pages — zero inbound links
3. Orphan sources — daily logs not yet compiled
4. Stale articles — source daily log changed since compilation
5. Contradictions — conflicting claims (LLM judgment)
6. Missing backlinks — A links to B but B doesn't link back
7. Sparse articles — below 200 words

### Hook System

Three hooks configured in `.claude/settings.json`:

**`SessionStart`** → `hooks/session-start.py`
- Pure local I/O, no API calls, runs under 1 second
- Reads `knowledge/index.md` + most recent daily log
- Outputs JSON to stdout with `additionalContext` field
- Max context: 20,000 characters

**`SessionEnd`** → `hooks/session-end.py`
- Reads hook input from stdin (JSON with `session_id`, `transcript_path`, `cwd`)
- Copies raw JSONL transcript to temp file
- Spawns `flush.py` as fully detached background process
- Recursion guard: exits if `CLAUDE_INVOKED_BY` env var set

**`PreCompact`** → `hooks/pre-compact.py`
- Same architecture as session-end.py
- Fires before auto-compaction of context window
- Guards against empty `transcript_path` (known Claude Code bug #13668)
- Critical for long sessions: captures context before summarization discards it

**Background flush process (`flush.py`):**
- Detached: `CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS` (Windows) / `start_new_session=True` (Mac/Linux)
- Sets `CLAUDE_INVOKED_BY=memory_flush` (prevents recursive hook firing)
- Skips if empty or same session flushed within 60 seconds (deduplication)
- Calls Claude Agent SDK (`query()`, `allowed_tools=[]`, `max_turns=2`)
- Appends structured bullet points (or `FLUSH_OK`) to `daily/YYYY-MM-DD.md`
- **End-of-day auto-compilation:** after 6 PM local time, if today's log changed (SHA-256 vs `state.json`), spawns `compile.py` as another detached background process

**`.claude/settings.json`:**
```json
{
  "hooks": {
    "SessionStart": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/session-start.py", "timeout": 15 }] }],
    "PreCompact": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/pre-compact.py", "timeout": 10 }] }],
    "SessionEnd": [{ "matcher": "", "hooks": [{ "type": "command", "command": "uv run python hooks/session-end.py", "timeout": 10 }] }]
  }
}
```

### JSONL Transcript Format

```python
entry = json.loads(line)
msg = entry.get("message", {})
role = msg.get("role", "")     # "user" or "assistant"
content = msg.get("content", "")  # string or list of content blocks
```

Content can be a string or a list of `{"type": "text", "text": "..."}` blocks.

### compile.py (The Compiler)

Uses Claude Agent SDK async streaming `query()`:
```python
async for message in query(
    prompt=compile_prompt,
    options=ClaudeAgentOptions(
        cwd=str(ROOT_DIR),
        system_prompt={"type": "preset", "preset": "claude_code"},
        allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"],
        permission_mode="acceptEdits",
        max_turns=30,
    ),
):
```
- Incremental: tracks SHA-256 hashes in `state.json`, skips unchanged files
- Cost: ~$0.45-0.65 per daily log

CLI:
```bash
uv run python scripts/compile.py              # compile new/changed only
uv run python scripts/compile.py --all        # force recompile everything
uv run python scripts/compile.py --file daily/2026-04-01.md
uv run python scripts/compile.py --dry-run
```

### query.py (Index-Guided Retrieval)

Loads entire knowledge base into context (index + all articles). No RAG. CLI:
```bash
uv run python scripts/query.py "question"
uv run python scripts/query.py "question" --file-back
```

### lint.py (Health Checks)

Structural checks (free) + contradictions (LLM, ~$0.15-0.25). Reports saved to `reports/lint-YYYY-MM-DD.md`.

### State Tracking

- `scripts/state.json` — daily log SHA-256 hashes, compilation timestamps, costs, total_cost, query_count, last_lint
- `scripts/last-flush.json` — flush deduplication (session_id + timestamp). Both gitignored.

### Costs

| Operation | Cost |
|-----------|------|
| Compile one daily log | $0.45-0.65 |
| Query (no file-back) | ~$0.15-0.25 |
| Query (with file-back) | ~$0.25-0.40 |
| Full lint (with contradictions) | ~$0.15-0.25 |
| Structural lint only | $0.00 |
| Memory flush (per session) | ~$0.02-0.05 |

### Customization

- Add article types by creating new directories in `knowledge/` (e.g. `people/`, `projects/`, `tools/`) and defining formats in AGENTS.md
- Obsidian integration: point a vault at `knowledge/` for graph view, backlinks, search
- Scaling beyond 2,000+ articles: add hybrid RAG (keyword + semantic) as retrieval layer

## Top-level structure

| Path | Type | Notes |
|---|---|---|
| `.claude/settings.json` | file | Hook configuration (SessionStart, SessionEnd, PreCompact) |
| `AGENTS.md` | file | Full technical schema and agent instructions |
| `README.md` | file | Quick start + overview |
| `pyproject.toml` | file | Python dependencies (claude-agent-sdk, python-dotenv, tzdata) |
| `hooks/` | dir | session-start.py, session-end.py, pre-compact.py |
| `scripts/` | dir | compile.py, query.py, lint.py, flush.py, config.py, utils.py |
| `uv.lock` | file | Dependency lock (boilerplate) |
