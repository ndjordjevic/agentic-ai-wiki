---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/AgriciDaniel/claude-obsidian
tags:
  - claude-obsidian
  - obsidian-pkm
  - karpathy-llm-wiki
  - claude-code-plugin
  - agent-skills
  - compound-vault
  - methodology-modes
  - hybrid-retrieval
  - second-brain
related:
  - 6eanut-llm-wiki
  - kepano-obsidian-skills
  - forrestchang-andrej-karpathy-skills
  - anthropics-skills
  - shareai-lab-learn-claude-code
  - runcabinet.com
  - hilash-cabinet
  - reseek.net
  - zilliztech-claude-context
  - chopratejas-headroom
product: claude-obsidian
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

_All claims below are sourced from ../../raw/github/agricidaniel-claude-obsidian.md unless otherwise noted._

`AgriciDaniel/claude-obsidian` (8,984+ stars, MIT, v1.9.2) is the most mature open-source implementation of Andrej Karpathy's LLM Wiki pattern as an Obsidian vault + Claude Code plugin. Unlike chat-over-notes plugins, it is a **knowledge engine**: Claude ingests sources into typed wiki pages (`sources/`, `entities/`, `concepts/`), maintains cross-references and contradiction callouts, answers from the vault with page citations, lints health, and compounds context across sessions via a hot cache. It ships **15 Agent Skills** (`/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/autoresearch`, `/save`, `/think`, `/canvas`, etc.), first-class PKM methodology modes (LYT/PARA/Zettelkasten/Generic), and the v1.7 "Compound Vault" refoundation (Obsidian CLI transport, hybrid BM25+cosine retrieval, multi-writer advisory locks). It hard-prefers [[kepano-obsidian-skills]] as substrate for Obsidian primitives and sits in the same Karpathy-wiki niche as [[6eanut-llm-wiki]] and [[runcabinet.com]] — but with deeper Obsidian integration, autonomous research, and production-scale community adoption.

## What it does

claude-obsidian turns an Obsidian vault into a self-organizing second brain. Users drop sources (PDFs, markdown, URLs, transcripts) into `.raw/`; Claude reads them, extracts entities and concepts, updates bidirectional wikilinks, and files everything into a structured vault. Queries follow a two-layer lookup: `wiki/hot.md` (recent ~500-word session cache) first, then `wiki/index.md` (master catalog), then drill into specific pages — answers cite wiki pages, not training data. `/wiki-lint` runs an 8-category health check (orphans, dead links, stale claims, missing cross-references). Session-end hooks refresh the hot cache so the next Claude Code session starts with full recent context.

The plugin distinguishes itself from Smart Connections and Copilot-style chat plugins by **creating and maintaining** notes autonomously: contradiction flagging via `[!contradiction]` callouts, batch parallel ingest, methodology-aware filing, autonomous 3-round web research (`/autoresearch`), and multi-writer safety via per-file advisory locks (v1.7+).

## Installation

**Option 1 — Clone as vault (recommended):**

```bash
git clone https://github.com/AgriciDaniel/claude-obsidian
cd claude-obsidian
bash bin/setup-vault.sh
```

Open the folder in Obsidian, then open Claude Code in the same folder and type `/wiki`.

**Option 2 — Claude Code plugin:**

```bash
claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Option 3 — Existing vault:** copy `WIKI.md` into vault root; Claude scaffolds `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`, and `wiki/overview.md` on first `/wiki`.

**Requirements:** Claude Code (latest), Obsidian v1.9.10+ (Bases dashboard; v1.6+ works with Dataview fallback), Python 3.10+ (retrieval pipeline and tests), Bash/zsh, Git.

## Key features

- **15 cohering skills** — `wiki`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `wiki-retrieve`, `wiki-cli`, `wiki-mode`, `wiki-fold`, `autoresearch`, `save`, `think`, `canvas`, `defuddle`, `obsidian-markdown`, `obsidian-bases` — each invocable as a slash command or natural-language trigger.
- **Compound Vault (v1.7)** — Obsidian 1.12 CLI as default transport with MCP/filesystem fallback chain; hybrid retrieval (contextual prefix + BM25 + cosine rerank per Anthropic's contextual retrieval research); per-file advisory locking via `scripts/wiki-lock.sh`.
- **Methodology modes (v1.8)** — LYT, PARA, Zettelkasten, or Generic; `scripts/wiki-mode.py route` determines filing paths for `wiki-ingest`, `save`, and `autoresearch` without auto-migrating existing files.
- **Thinking framework (v1.9)** — `/think` skill runs a 10-principle thinking loop as an invocable skill.
- **DragonScale Memory (optional)** — `bin/setup-dragonscale.sh` adds log folds, deterministic page addresses, semantic tiling lint, and boundary-first autoresearch topic selection.
- **Multi-agent / multi-host** — Agent Skills compatible (experimental on Codex, Cursor, Windsurf, Gemini CLI, Goose); production-verified on Claude Code.
- **Seed vault** — ships pre-seeded concepts (LLM Wiki Pattern, Hot Cache, Compounding Knowledge), entities (Andrej Karpathy), and Bases/Dataview dashboards.
- **Local-first retrieval** — `/wiki-retrieve` API egress gated behind `--allow-egress`; default path is fully local (BM25 + optional ollama rerank).

## Architecture

Three-layer Karpathy wiki pattern inside an Obsidian vault:

```
.raw/ (immutable sources)  →  wiki/ (LLM-maintained pages)  →  skills/ (workflows + conventions)
```

**Query path (default):** `Read(hot.md)` → `Read(index.md)` → `Read(N relevant pages)` → synthesize with citations.

**Query path (opt-in `/wiki-retrieve`):** chunk on paragraph boundaries → contextual prefix per chunk → BM25 top-20 → cosine rerank (ollama `nomic-embed-text`) → top-5 page-address dedupe.

**Transport stack (v1.7+, auto-detected):** Obsidian CLI → MCP-obsidian (REST API) → mcpvault (filesystem BM25) → direct Read/Write (floor). `scripts/detect-transport.sh` writes `.vault-meta/transport.json`.

**Concurrency:** parallel ingest sub-agents acquire per-file locks before writes; stale locks self-reap after 60 seconds.

**Substrate alignment:** `obsidian-markdown`, `obsidian-bases`, and `canvas` skills hard-prefer [[kepano-obsidian-skills]] when installed; local copies remain as fallbacks.

**Vault page types:** `wiki/sources/` (ingested documents), `wiki/entities/` (people, orgs, products), `wiki/concepts/` (abstract ideas), `wiki/meta/` (dashboard, graph assets).

## Example usage

```bash
# After setup
/wiki                          # scaffold or continue vault setup
ingest my-article.pdf          # create 8–15 cross-referenced wiki pages
what do you know about X?      # query with page citations
lint the wiki                  # 8-category health check
/autoresearch quantum computing # 3-round autonomous research loop
/save session-notes            # file current conversation as wiki note
/think                         # 10-principle thinking loop
```

**Methodology mode setup:**

```bash
bash bin/setup-mode.sh           # interactive
bash bin/setup-mode.sh --mode para   # non-interactive
```

**Opt-in retrieval pipeline:**

```bash
bash bin/setup-retrieve.sh
```

## Maintenance status

| Signal | Value |
|---|---|
| Stars | 8,984+ |
| Latest release | v1.9.2 (2026-05-28) — Compound Vault, Methodology Modes, Thinking Framework |
| License | MIT |
| Primary language | Python |
| Default branch | `main` |
| CI | `make test` + SKILL.md frontmatter validation + plugin manifest JSON on every PR |
| Community | AI Marketing Hub (2,800+ free), AI Marketing Hub Pro (early-access mirror) |

Active development through v1.9.x; roadmap items include GUI ergonomics (v2.5+) and derivative outputs (v2.0). Companion projects: `claude-canvas` (visual layer), `claude-ads`, `claude-seo`, `best-practices` (engineering kernel). Competes in the Obsidian+AI space against chat plugins; in the Karpathy-wiki space against [[6eanut-llm-wiki]] (lighter Claude Code skill) and [[hilash-cabinet]]/[[runcabinet.com]] (Cabinet pattern).
