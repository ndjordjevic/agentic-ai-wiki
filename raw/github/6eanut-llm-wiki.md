# 6eanut/llm-wiki

## Metadata
- Stars: 35
- Primary language: Shell
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: —
- Fetched: 2026-05-13
- Final URL: https://github.com/6eanut/llm-wiki

## Description
Claude Code skill for building persistent, interlinked knowledge bases from source documents. Knowledge is compiled once and kept current — never re-derived per query. Based on Karpathy's LLM Wiki pattern.

## README
# LLM Wiki — Compounding Knowledge Base for Claude Code

A **Claude Code skill** that builds and maintains a persistent, interlinked wiki from your source documents. Based on Andrej Karpathy's LLM Wiki pattern.

Knowledge is compiled once and kept current, not re-derived on every query.

---

## Quick Start

### One Command

```bash
git clone https://github.com/6eanut/llm-wiki
cd llm-wiki
./quickstart.sh
```

The script installs the skill, initializes the wiki, and drops in demo source files (Greek mythology — optional, use `--no-demo` to skip).

After setup, start Claude Code and run:

```
/wiki-ingest .raw/greek-olympians.md
```

Then ask anything about the content — Claude checks the wiki automatically.

### With Session Hooks (Recommended)

```bash
./quickstart.sh --with-hooks
```

This enables:
- **Dynamic wiki stats at startup** — page count, recent changes, pending reviews injected at the start of every session
- **Hot-cache for session continuity** — context from your last session is bridged forward so you don't lose state between sessions

### Manual Setup

```bash
./llm-wiki/install.sh --force                                            # 1. Install skill
~/.claude/skills/llm-wiki/scripts/setup-project.sh ./wiki --with-hooks  # 2. Init wiki
# 3. Drop source files in .raw/ and run /wiki-ingest
```

---

## Architecture

### How Proactive Wiki Works

```
Session starts
    ↓
Claude reads CLAUDE.md → "Check the wiki before answering"
    ↓
SessionStart hook runs → wiki stats, topics, pending items
    ↓
Slash commands auto-discovered from ~/.claude/commands/
    ↓
Skill auto-registered as "wiki" from ~/.claude/skills/llm-wiki/
    ↓
User asks any question
    ↓
Claude reads index.md → finds relevant pages → answers with citations
```

### Key Architectural Decisions

| Decision | Rationale |
|----------|-----------|
| **CLAUDE.md for rules** | Always-loaded, no tool call needed. Tells Claude WHEN to use the wiki. |
| **SessionStart hook for state** | Dynamic wiki stats injected each session. |
| **LLM is the runtime** | All content work done by Claude. No external language runtime needed. |
| **Bash for determinism only** | SHA-256 hashing, file listing, grep — correctness-critical operations only. |
| **Markdown workflow files** | Each command has a `workflows/*.md` procedure. Documentation = executable instructions. |
| **Two-phase ingest** | Phase 1 (analysis) writes a reviewable analysis before Phase 2 (generation) creates pages. |
| **Auto-generated index** | `index.md` regenerated on every change. Enables O(1) lookup of relevant pages. |
| **SHA-256 incremental caching** | `.done` sentinel files prevent re-ingestion. Safe to re-drop sources. |

### Three-Layer Data Architecture

```
.raw/ (sources)    →    wiki/ (pages)    →    skill (schema + workflows)
  (immutable)            (LLM-generated)       (conventions)
```

---

## Wiki Directory Structure

```
wiki/
├── .llm-wiki/
│   ├── schema.md                   Copy of WIKI_SCHEMA.md
│   ├── config.md                   User preferences
│   ├── index.md                    ★ AUTO-GENERATED — never edit by hand ★
│   ├── review.json                 {pending: [...], resolved: [...]}
│   ├── cache/
│   │   ├── hot-cache.md            Multi-session context bridge
│   │   ├── source-manifest.json    SHA-256 → source metadata
│   │   ├── state-hash.txt          Detects external modifications
│   │   └── ingests/{sha256}.done   Sentinel files (idempotent ingestion)
│   └── inbox/{sha256}-analysis.md  Phase 1 ingest analyses
├── transformer.md                  Concept page
├── 2026-04-28-weekly-notes.md      Article page
├── alan-turing.md                  Person page
└── synth-2026-04-28-riscv.md       Synthesis page
```

---

## Page Types

### `concept` — Define a term, idea, methodology, tool
### `article` — Notes, blog drafts, imported documents
### `person` — Author, researcher, notable individual
### `synthesis` — Saved query answer (the compounding mechanism)

---

## Bilingual Support

- **Auto-detection**: CJK character ratio determines `zh` / `en` / `bilingual`
- **Page titles**: `"English / 中文"` format for bilingual pages
- **Cross-language wikilinks**: `aliases` field provides translations
- **Query matching**: Prefers same-language pages, falls back across languages

---

## Compared to RAG

| | Typical RAG | LLM Wiki |
|---|-----|----------|
| Knowledge state | Re-derived per query | Persisted, compounding |
| Cross-references | None | Bidirectional [[wikilinks]] |
| Contradictions | Undetected | Flagged with callout blocks |
| Confidence | Opaque | Explicit per-page ratings |
| Audit trail | None | `based_on` provenance chain |
| Query cost | Every query reads source chunks | Index-first: only 3-5 pages read |
| Proactive | No — must be invoked | Yes — CLAUDE.md + hook drives behavior |

---

## Credits
- **Pattern**: Andrej Karpathy
- **Implementation**: Built with Claude Code

## License
MIT

## Top-level structure

| Name | Type | Notes |
|---|---|---|
| `.editorconfig` | file | Editor formatting config |
| `.githooks/` | dir | Git hook scripts |
| `.github/` | dir | CI/CD workflows (CI badge in README) |
| `.gitignore` | file | Standard ignores |
| `.markdownlint-cli2.jsonc` | file | Markdown linting configuration |
| `.raw/` | dir | Demo source files (Greek mythology sample) |
| `CHANGELOG.md` | file | Version history |
| `CODE_OF_CONDUCT.md` | file | Community standards |
| `CONTRIBUTING.md` | file | Contribution guide |
| `FAQ.md` | file | Frequently asked questions |
| `LICENSE` | file | MIT license |
| `README.md` | file | Main documentation |
| `SECURITY.md` | file | Security policy |
| `SUPPORT.md` | file | Support info |
| `llm-wiki.md` | file | Skill manifest / CLAUDE.md template copy |
| `llm-wiki/` | dir | ★ Main skill directory (see below) |
| `package.json` | file | Node.js package (CI tooling / markdownlint) |
| `quickstart.sh` | file | One-command setup script |
| `scripts/` | dir | ci-local.sh — local CI runner |
| `uninstall.sh` | file | Removes installed skill |

## Docs

### llm-wiki/ (skill directory)

```
llm-wiki/
├── SKILL.md                         Skill manifest with proactive usage rules
├── WIKI.md                          CLAUDE.md template (copied to project root)
├── WIKI_SCHEMA.md                   Page type definitions & conventions
├── install.sh                       Global installation (one-time)
├── commands/                        Auto-discovered slash commands
│   ├── wiki-ingest.md               /wiki-ingest
│   ├── wiki-query.md                /wiki-query
│   ├── wiki-lint.md                 /wiki-lint
│   ├── wiki-save.md                 /wiki-save
│   ├── wiki-graph.md                /wiki-graph
│   └── wiki-review.md               /wiki-review
├── templates/                       Page templates (article, concept, person, synthesis)
├── scripts/                         Deterministic bash operations
│   ├── _utils.sh                    Shared utility functions
│   ├── setup-project.sh             One-stop project setup
│   ├── init-wiki.sh                 Bootstrap new wiki directory
│   ├── hash-files.sh                SHA-256 hash source files
│   ├── check-stale.sh               Index freshness check
│   ├── find-orphans.sh              Pages with zero incoming links
│   ├── validate-frontmatter.sh      Required field validation
│   └── find-broken-links.sh         Dead wikilink detection
├── workflows/                       Deep workflow procedures
│   ├── ingest.md                    Two-phase source ingestion
│   ├── query.md                     Index-first knowledge retrieval
│   ├── lint.md                      Structural + semantic health check
│   ├── save-synthesis.md            Persist answers as synthesis pages
│   ├── graph.md                     D3.js knowledge graph generation
│   └── review.md                    Review queue processing
└── hooks/                           Session lifecycle
    ├── session-start.sh             Wiki stats + PROACTIVE WIKI RULE
    └── session-stop.sh              Write hot-cache for next session
```

### SKILL.md (excerpt)

The skill manifest defines proactive usage rules:
- Before answering any factual question: read `.llm-wiki/index.md` first
- When wiki lacks knowledge: surface the gap and suggest adding sources
- After modifying wiki pages: always regenerate the index
- Use `Skill("llm-wiki")` only for deep operations (ingest, full lint, graph, review); lightweight queries need no skill invocation
