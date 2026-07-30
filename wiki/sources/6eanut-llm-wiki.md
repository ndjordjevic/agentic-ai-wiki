---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/6eanut/llm-wiki
tags: [llm-wiki, karpathy-pattern, claude-code, skills, knowledge-base, agent-memory]
related: [anthropics-skills, shareai-lab-learn-claude-code, forrestchang-andrej-karpathy-skills, skills.sh, runcabinet.com, hilash-cabinet, nadimtuhin-claude-token-optimizer, teng-lin-notebooklm-py, kepano-obsidian-skills, langchain-ai-openwiki, deepwiki.com, he-yufeng-RepoWiki, bb-boy680-open-zread, coleam00-helpline, coleam00-claude-memory-compiler, agricidaniel-claude-obsidian, coleam00-cole-medin-knowledge-base]
product: llm-wiki
detail_level: standard
created: 2026-05-13
updated: 2026-07-30
---

# 6eanut/llm-wiki

_All claims below are sourced from ../../raw/github/6eanut-llm-wiki.md unless otherwise noted._

`6eanut/llm-wiki` is a Claude Code skill that implements Andrej Karpathy's LLM Wiki pattern as a fully automated, maintainable knowledge base. It compiles knowledge once and keeps it current — rather than re-deriving answers from raw sources on every query — and ships it as an installable Claude Code skill with slash commands, session hooks, and bash utility scripts. The project is positioned at the intersection of [[anthropics-skills]]'s plugin ecosystem, [[shareai-lab-learn-claude-code]]'s harness engineering philosophy, and the Karpathy-wiki operationalization already seen in [[runcabinet.com]].

## What it does

`llm-wiki` builds and maintains a persistent, interlinked markdown wiki from user-supplied source documents. Users drop files (markdown, text) into `.raw/`, run `/wiki-ingest`, and Claude Code analyses the source, extracts concepts, and generates typed wiki pages with bidirectional `[[wikilinks]]`. Subsequent questions are answered by reading `wiki/.llm-wiki/index.md` first, then 3–5 relevant pages, giving O(1) lookup without re-reading source documents every turn.

## Installation

```bash
# One-command quickstart (installs skill + initializes wiki + optional demo data)
git clone https://github.com/6eanut/llm-wiki
cd llm-wiki
./quickstart.sh              # basic
./quickstart.sh --with-hooks # with SessionStart/Stop lifecycle hooks (recommended)

# Manual setup
./llm-wiki/install.sh --force
~/.claude/skills/llm-wiki/scripts/setup-project.sh ./wiki --with-hooks
```

The `--with-hooks` flag enables two session lifecycle hooks: `session-start.sh` injects live wiki stats (page count, recent changes, pending reviews) at the start of each Claude Code session; `session-stop.sh` writes a hot-cache that bridges context into the next session.

## Key features

- **Proactive wiki rule** — `CLAUDE.md` / `WIKI.md` template instructs Claude to read `index.md` before answering any factual question. No explicit `/wiki-query` invocation needed for routine questions.
- **Two-phase ingest** — Phase 1 writes a reviewable analysis (`inbox/{sha256}-analysis.md`); Phase 2 generates wiki pages. The human has a checkpoint between analysis and generation.
- **SHA-256 incremental caching** — `.done` sentinel files prevent re-ingestion of unchanged sources. Safe to re-drop files.
- **Auto-generated index** — `wiki/.llm-wiki/index.md` regenerated on every change; never hand-edited. Enables the O(1) lookup pattern.
- **Hot-cache for session continuity** — context from the previous session is bridged forward via `cache/hot-cache.md` to avoid repeating orientation work.
- **Bilingual support** — CJK character ratio determines `zh` / `en` / `bilingual` page language; `aliases` field enables cross-language wikilink resolution.
- **Review queue** — `review.json` tracks pending and resolved review items processed by `/wiki-review`.

## Architecture

Three-layer architecture separates concerns:

```
.raw/ (sources)    →    wiki/ (pages)    →    skill (schema + workflows)
  (immutable)            (LLM-generated)       (conventions)
```

**LLM is the runtime** — all content work (extraction, cross-referencing, contradiction detection, synthesis) is done by Claude. Bash is used only for correctness-critical deterministic operations: SHA-256 hashing, index freshness checks, orphan detection, frontmatter validation, and broken-link detection.

**Key architectural decisions:**

| Decision | Rationale |
|---|---|
| CLAUDE.md for rules | Always-loaded; tells Claude when to use the wiki without a tool call |
| SessionStart hook | Dynamic stats injected per session; keeps context current |
| Markdown workflow files | `workflows/*.md` are executable instructions, not just documentation |
| Two-phase ingest | Human checkpoint prevents runaway page generation |
| SHA-256 sentinel files | Idempotent re-runs; no cleanup needed after crashes |

## Example usage

```
# After setup, start Claude Code and ingest a source
/wiki-ingest .raw/greek-olympians.md

# Ask any question — Claude reads the wiki automatically (no /wiki-query needed)
"What is the relationship between Zeus and Athena?"

# Explicit wiki operations
/wiki                 # dashboard: stats, recent activity, pending reviews
/wiki-query <question>
/wiki-lint [--quick|--full]
/wiki-save            # persist current answer as a synthesis page
/wiki-graph           # D3.js knowledge graph visualization
/wiki-review          # process review queue
```

## Skill file map

```
llm-wiki/
├── SKILL.md               Skill manifest + proactive usage rules
├── WIKI.md                CLAUDE.md template for the user's project
├── WIKI_SCHEMA.md         Page type definitions & conventions
├── install.sh             Global installation (one-time)
├── commands/              6 slash commands (wiki-ingest, wiki-query, wiki-lint,
│                          wiki-save, wiki-graph, wiki-review)
├── workflows/             Deep procedure files (ingest, query, lint, save-synthesis,
│                          graph, review)
├── scripts/               Deterministic bash utilities (init-wiki, hash-files,
│                          check-stale, find-orphans, validate-frontmatter,
│                          find-broken-links, setup-project)
├── templates/             Page templates (article, concept, person, synthesis)
└── hooks/                 session-start.sh, session-stop.sh
```

## Maintenance status

- 35 stars, 7 forks as of 2026-05-13
- Actively maintained; last pushed 2026-05-13
- MIT license
- CI badge present (GitHub Actions); no releases yet
