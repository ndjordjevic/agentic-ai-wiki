# AgriciDaniel/claude-obsidian

## Metadata
- Stars: 8984
- Primary language: Python
- Default branch: main
- Latest release: v1.9.2: Compound Vault, Methodology Modes, and the Thinking Framework
- License: MIT License
- Homepage: https://agricidaniel.com/blog/claude-obsidian-ai-second-brain
- Fetched: 2026-07-08
- Final URL: https://github.com/AgriciDaniel/claude-obsidian

## Description
Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy's LLM Wiki pattern.

## README

# claude-obsidian: Self-Organizing AI Second Brain for Obsidian + Claude Code

<p align="center">
  <img src="wiki/meta/claude-obsidian-gif-cover-16x9.gif" alt="claude-obsidian: persistent compounding wiki vault for Claude Code and Obsidian" width="100%" />
</p>

[![GitHub stars](https://img.shields.io/github/stars/AgriciDaniel/claude-obsidian?style=flat&color=e8734a)](https://github.com/AgriciDaniel/claude-obsidian/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/AgriciDaniel/claude-obsidian?color=blue)](https://github.com/AgriciDaniel/claude-obsidian/releases/latest)
[![CI](https://github.com/AgriciDaniel/claude-obsidian/actions/workflows/test.yml/badge.svg)](https://github.com/AgriciDaniel/claude-obsidian/actions/workflows/test.yml)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-8B5CF6)](https://code.claude.com/docs/en/discover-plugins)
[![Obsidian](https://img.shields.io/badge/Obsidian-v1.9.10%2B-7c3aed)](https://obsidian.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-blue)](https://agentskills.io)
[![Community](https://img.shields.io/badge/AI%20Marketing%20Hub-Pro%20community-purple)](https://www.skool.com/ai-marketing-hub-pro)
[![Blog Post](https://img.shields.io/badge/Deep_Dive-Blog_Post-22c55e)](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain)

Claude + Obsidian knowledge companion and self-organizing AI second brain. A running AI notetaker that builds and maintains a persistent, compounding wiki vault. Every source you add gets integrated. Every question you ask pulls from everything that has been read. Knowledge compounds like interest.

Open-source Obsidian AI plugin for AI note-taking, personal knowledge management (PKM), second-brain workflows, and a private Notion alternative. **15 Claude Code skills**, multi-agent support, multi-writer safe (v1.7+), first-class methodology modes (LYT / PARA / Zettelkasten / Generic via v1.8), and the 10-principle thinking framework (v1.9). Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

> **Two ways to get this skill.** Pick the one that fits how you work.
>
> - 🌐 **Public open-source build** (latest: `v1.9.2`, recommended): the free, MIT-licensed release on [Daniel Agrici's GitHub](https://github.com/AgriciDaniel/claude-obsidian). Open to anyone, no membership required. Ships everything: v1.7 Compound Vault, v1.8 methodology modes, and the v1.9 thinking framework plus audit hardening.
> - ⚡ **AI Marketing Hub Pro**: the same MIT-licensed core, plus earliest access to in-development features before they land here, direct collaboration, and the [Pro community](https://www.skool.com/ai-marketing-hub-pro). Pro members install from the [AI Marketing Hub](https://github.com/AI-Marketing-Hub) org mirror (swap note under Option 2 below).

> ✨ **v1.7 "Compound Vault" refoundation**: Obsidian CLI as default transport, hybrid retrieval (contextual prefix + BM25 + cosine rerank per [Anthropic's Sept 2024 research](https://www.anthropic.com/news/contextual-retrieval)), per-file advisory locking that closes a latent multi-writer corruption hole, and substrate alignment with [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills). Full guide: [docs/compound-vault-guide.md](docs/compound-vault-guide.md). Optional [DragonScale Memory](docs/dragonscale-guide.md) extension (log folds, deterministic page addresses, semantic tiling lint, boundary-first autoresearch).

---

## Contents

- [What It Does](#what-it-does)
- [Why claude-obsidian?](#why-claude-obsidian)
- [Quick Start](#quick-start)
- [Commands](#commands)
  - [`/wiki`: setup, scaffold, continue](#wiki-setup-scaffold-continue)
  - [`/autoresearch`: autonomous research loop](#autoresearch-autonomous-research-loop)
  - [`/canvas`: visual layer](#canvas-visual-layer)
  - [`/think`: 10-principle thinking loop](#think-10-principle-thinking-loop)
- [Methodology Modes (v1.8+)](#methodology-modes-v18)
- [Vault Use Cases (v1.0+)](#vault-use-cases-v10)
- [Cross-Project Knowledge Base](#cross-project-knowledge-base)
- [What Gets Created](#what-gets-created)
- [Architecture](#architecture)
- [MCP Setup (Optional)](#mcp-setup-optional)
- [Plugins](#plugins)
- [CSS Snippets](#css-snippets-auto-enabled-by-setup-vaultsh)
- [Banner Plugin](#banner-plugin)
- [File Structure](#file-structure)
- [AutoResearch Configuration](#autoresearch-programmd)
- [Seed Vault](#seed-vault)
- [Companion: claude-canvas](#companion-claude-canvas)
- [FAQ](#faq)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [Community](#community)
- [License](#license)

---

## What It Does

### [YouTube Demo](https://www.youtube.com/watch?v=a2hgayvr-H4)

<p align="center">
  <img src="wiki/meta/welcome-canvas.gif" alt="claude-obsidian welcome canvas: visual demo of the wiki vault workflow" width="96%" />
</p>

You drop sources. Claude reads them, extracts entities and concepts, updates cross-references, and files everything into a structured Obsidian vault. The wiki gets richer with every ingest.

You ask questions. Claude reads the hot cache (recent context), scans the index, drills into relevant pages, and synthesizes an answer. It cites specific wiki pages, not training data.

You lint. Claude finds orphans, dead links, stale claims, and missing cross-references. Your wiki stays healthy without manual cleanup.

At the end of every session, Claude updates a hot cache. The next session starts with full recent context, no recap needed.

<p align="center">
  <img src="wiki/meta/image-example-graph-view.png" alt="Obsidian graph view showing the claude-obsidian knowledge graph with color-coded nodes for concepts, entities, and sources" width="48%" />
  <img src="wiki/meta/image-example-wiki-map-view.png" alt="Wiki Map canvas: visual hub linking domain pages, concepts, and entities" width="48%" />
</p>

---

## Why claude-obsidian?

Most Obsidian AI plugins are chat interfaces. They answer questions about your existing notes. claude-obsidian is a knowledge engine. It creates, organizes, maintains, and evolves your notes autonomously.

| Capability | claude-obsidian | Smart Connections | Copilot |
|---|---|---|---|
| **Auto-organize notes** | ✅ Creates entities, concepts, cross-references | ❌ | ❌ |
| **Contradiction flagging** | ✅ `[!contradiction]` callouts with sources | ❌ | ❌ |
| **Session memory** | ✅ Hot cache persists between conversations | ❌ | ❌ |
| **Vault maintenance** | ✅ 8-category lint (orphans, dead links, gaps) | ❌ | ❌ |
| **Autonomous research** | ✅ 3-round web research with gap-filling | ❌ | ❌ |
| **Methodology modes** | ✅ LYT / PARA / Zettelkasten / Generic (first-class) | ❌ | ❌ |
| **Thinking framework** | ✅ 10-principle loop as invocable skill | ❌ | ❌ |
| **Multi-model support** | ✅ Claude, Gemini, Codex, Cursor, Windsurf | ❌ Claude only | ✅ Multiple |
| **Visual canvas** | ✅ Via [claude-canvas](https://github.com/AgriciDaniel/claude-canvas) | ❌ | ❌ |
| **Multi-writer safe** | ✅ Per-file advisory locks (v1.7+) | ❌ | ❌ |
| **Query with citations** | ✅ Cites specific wiki pages | ✅ Cites similar notes | ✅ Cites notes |
| **Batch ingestion** | ✅ Parallel agents for multiple sources | ❌ | ❌ |
| **Open source** | ✅ MIT | ✅ MIT | ⚠️ Freemium |

> 📖 **Deep dive:** [I Turned Obsidian Into a Self-Organizing AI Brain](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain). Full breakdown with data visualizations, market context, and workflow demos.

---

## Quick Start

> ℹ️ The commands below install the **public open-source build** from `AgriciDaniel/claude-obsidian` (recommended, no membership needed). **AI Marketing Hub Pro members** who want early access to in-development features can swap `AgriciDaniel/claude-obsidian` for `AI-Marketing-Hub/claude-obsidian` (Option 2 also swaps the plugin slug; see the note under that option).

### Option 1: Clone as vault (recommended, full setup in 2 minutes)

```bash
git clone https://github.com/AgriciDaniel/claude-obsidian
cd claude-obsidian
bash bin/setup-vault.sh
```

Open the folder in Obsidian: **Manage Vaults → Open folder as vault → select `claude-obsidian/`**.

Open Claude Code in the same folder. Type `/wiki`.

> ℹ️ `setup-vault.sh` configures `graph.json` (filter + colors), `app.json` (excludes plugin dirs), and `appearance.json` (enables CSS). Run it once before the first Obsidian open. You get the fully pre-configured graph view, color scheme, and wiki structure out of the box.

---

### Option 2: Install as Claude Code plugin

Plugin installation is a two-step process. First add the marketplace catalog, then install the plugin from it.

> ℹ️ **Which version are you installing?**
>
> - **Public (recommended, no membership):** the commands below install the free, MIT-licensed release from [`AgriciDaniel/claude-obsidian`](https://github.com/AgriciDaniel/claude-obsidian). Nothing to sign up for.
> - **AI Marketing Hub Pro member?** For early access to in-development features, swap `AgriciDaniel/claude-obsidian` for `AI-Marketing-Hub/claude-obsidian` and the plugin slug `claude-obsidian@agricidaniel-claude-obsidian` for `claude-obsidian@ai-marketing-hub-claude-obsidian`. The org mirror requires an authenticated `gh auth login` (or GitHub PAT) with access to the `AI-Marketing-Hub` org. If `/plugin marketplace add` returns a 404, your account is not in the org yet. DM in the [Skool community](https://www.skool.com/ai-marketing-hub-pro) to get added.

```bash
# Step 1: add the marketplace
claude plugin marketplace add AgriciDaniel/claude-obsidian

# Step 2: install the plugin
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

In any Claude Code session: `/wiki`. Claude walks you through vault setup.

To check it worked:

```bash
claude plugin list
```

---

### Option 3: Add to an existing vault

Copy `WIKI.md` into your vault root. Paste into Claude:

```
Read WIKI.md in this project. Then:
1. Check if Obsidian is installed. If not, install it.
2. Check if the Local REST API plugin is running on port 27124.
3. Configure the MCP server.
4. Ask me ONE question: "What is this vault for?"
Then scaffold the full wiki structure.
```

---

## Commands

| You say | Claude does |
|---------|------------|
| `/wiki` | Setup check, scaffold, or continue where you left off |
| `ingest [file]` | Read source, create 8-15 wiki pages, update index and log |
| `ingest all of these` | Batch process multiple sources, then cross-reference |
| `what do you know about X?` | Read index, drill into relevant pages, synthesize answer |
| `/save` | File the current conversation as a wiki note |
| `/save [name]` | Save with a specific title (skips the naming question) |
| `/autoresearch [topic]` | Run the autonomous research loop: search, fetch, synthesize, file |
| `/canvas` | Open or create the visual canvas, list zones and nodes |
| `/canvas add image [path]` | Add an image (URL or local path) to the canvas with auto-layout |
| `/canvas add text [content]` | Add a markdown text card to the canvas |
| `/canvas add pdf [path]` | Add a PDF document as a rendered preview node |
| `/canvas add note [page]` | Pin a wiki page as a linked card on the canvas |
| `/canvas zone [name]` | Add a new labeled zone to organize visual content |
| `/canvas from banana` | Capture recently generated images onto the canvas |
| `/think [problem]` | Apply the 10-principle thinking loop to a non-trivial problem |
| `lint the wiki` | Health check: orphans, dead links, gaps, suggestions |
| `update hot cache` | Refresh hot.md with latest context summary |

> ✨ **Want more?** [claude-canvas](https://github.com/AgriciDaniel/claude-canvas) adds 12 templates, 6 layout algorithms, AI image generation, presentations, and full canvas orchestration. Install both, they complement each other.

### `/wiki`: setup, scaffold, continue

First-run setup walks through:

1. Check Obsidian is installed
2. Check Local REST API plugin (if MCP transport desired)
3. Ask "What is this vault for?" (one question, drives the scaffold)
4. Scaffold per chosen [Methodology Mode](#methodology-modes-v18) and [Vault Use Case](#vault-use-cases-v10)
5. Seed `hot.md`, `index.md`, `log.md`, `wiki/meta/dashboard.base`
6. Suggest the first ingest

On subsequent runs, `/wiki` continues where you left off. It checks vault health, surfaces stale claims, and shows recent activity from `hot.md`.

### `/autoresearch`: autonomous research loop

Configurable program at [`skills/autoresearch/references/program.md`](skills/autoresearch/references/program.md):

- Max rounds (default 3)
- Max pages per session (default 15)
- Source preference rules (academic, official docs, news)
- Confidence scoring + domain constraints

The loop:

1. **Round 1, broad search**: decompose into 3-5 angles, run 2-3 queries per angle, fetch top 2-3 results per angle
2. **Round 2, gap fill**: targeted searches for contradictions and missing pieces
3. **Round 3, synthesis check** (optional): one more pass if major gaps remain
4. **Filing**: synthesis page + source pages + entity pages + concept pages, all cross-referenced

URL validation + content sanitization applied per the `## Web egress hygiene (v1.8.2+)` policy in [`skills/autoresearch/SKILL.md`](skills/autoresearch/SKILL.md): rejects `file://` / `javascript:` / RFC1918 hosts, strips `<script>` and wikilink-injection attempts, caps fetch bodies at 50KB.

### `/canvas`: visual layer

Add images, PDFs, notes, and AI-generated images to an Obsidian canvas. Zone management for grouping. Auto-layout positions nodes without overlap.

```
/canvas                       # open or create the canvas
/canvas add image <path>      # add an image with auto-layout
/canvas add pdf <path>        # render PDF as preview node
/canvas add note <wiki-page>  # pin a wiki page as a linked card
/canvas zone <name>           # add a labeled zone
/canvas from banana           # capture recent banana-generated images
```

JSON Canvas 1.0 spec compliant ([`skills/canvas/references/canvas-spec.md`](skills/canvas/references/canvas-spec.md)). Full orchestration (12 templates, 6 layout algorithms, presentations) in the companion [claude-canvas](https://github.com/AgriciDaniel/claude-canvas).

### `/think`: 10-principle thinking loop

Apply the OBSERVE-OBSERVE-LISTEN-THINK-CONNECT-CONNECT-FEEL-ACCEPT-CREATE-GROW framework to any non-trivial problem (architectural decisions, audits, post-mortems, ambiguous user requests).

```
/think <problem statement>
```

The framework walks Claude through 10 stages with prompts at each. Use when problem novelty + irreversibility justify the discipline. See [`skills/think/SKILL.md`](skills/think/SKILL.md) for the full framework. Every other skill has a "How to think" appendix mapping the framework to its specific work. The [v1.8.0 pre-push audit](docs/audits/v1.8.0-pre-push-audit-2026-05-18.md) used this framework as its methodology spine.

---

## Methodology Modes (v1.8+)

Four organizational philosophies, opt-in via `bash bin/setup-mode.sh`. The `wiki-mode` skill (v1.8+) reads `.vault-meta/mode.json` and routes new pages accordingly. Default is `generic` (v1.7 behavior, no opinion imposed).

| Mode | Philosophy | Filing convention |
|------|-----------|-------------------|
| **Generic** (default) | No opinion. v1.7 behavior preserved. | `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/sessions/` |
| **LYT** (Linking Your Thinking) | Notes link, folders don't. MOCs are the navigation primitive. | `wiki/mocs/<topic>-moc.md` + `wiki/notes/<atomic-note>.md` |
| **PARA** (Tiago Forte) | Organize by actionability (Projects, Areas, Resources, Archives). | `wiki/projects/`, `wiki/areas/`, `wiki/resources/`, `wiki/archives/` |
| **Zettelkasten** (Luhmann slip-box) | Atomic notes, unique IDs, dense bidirectional linking, no folders. | `wiki/<YYYYMMDDHHMMSSffffff>-<slug>.md` (flat, timestamped) |

Switching modes does NOT auto-migrate existing files. Full guide: [`docs/methodology-modes-guide.md`](docs/methodology-modes-guide.md).

---

## Vault Use Cases (v1.0+)

These describe **what** your vault is for. They compose with Methodology Modes (which describe **how** it is organized).

| Use case | When to use |
|----------|-------------|
| **A: Website** | Sitemap, content audit, SEO wiki |
| **B: GitHub** | Codebase map, architecture wiki |
| **C: Business** | Project wiki, competitive intelligence |
| **D: Personal** | Second brain, goals, journal synthesis |
| **E: Research** | Papers, concepts, thesis |
| **F: Book/Course** | Chapter tracker, course notes |

Use cases can be combined. A Business + Research vault organized in PARA is a valid composition.

---

## Cross-Project Knowledge Base

Point any Claude Code project at this vault. Add to that project's `CLAUDE.md`:

```markdown
## Wiki Knowledge Base
Path: ~/path/to/vault

When you need context not already in this project:
1. Read wiki/hot.md first (recent context cache)
2. If not enough, read wiki/index.md
3. If you need domain details, read the relevant domain sub-index
4. Only then drill into specific wiki pages

Do NOT read the wiki for general coding questions or tasks unrelated to [domain].
```

Your executive assistant, coding projects, and content workflows all draw from the same knowledge base.

---

## What Gets Created

A typical scaffold creates:

- Folder structure for your chosen use case + methodology mode
- `wiki/index.md`: master catalog
- `wiki/log.md`: append-only operation log
- `wiki/hot.md`: recent context cache
- `wiki/overview.md`: executive summary
- `wiki/meta/dashboard.base`: Bases dashboard (primary, native Obsidian)
- `wiki/meta/dashboard.md`: Legacy Dataview dashboard (optional fallback)
- `_templates/`: Obsidian Templater templates for each note type
- `.obsidian/snippets/vault-colors.css`: color-coded file explorer
- Vault `CLAUDE.md`: auto-loaded project instructions

---

## Architecture

Three diagrams explain the substantive design choices of the plugin.

### Vault flow

Sources land in `.raw/`. The `/wiki-ingest` agent reads each source, extracts entities and concepts, files them into the appropriate `wiki/` subfolder (per active methodology mode), and updates the index, log, and hot cache. Queries read hot → index → pages in that order to keep token cost low.

<p align="center">
  <img src="assets/diagrams/vault-flow.svg" alt="Architecture diagram: sources flow into the wiki-ingest agent, which produces entity, concept, and source pages. The index and hot cache are updated. The wiki-query interface reads the cache, index, and pages to synthesize cited answers." width="100%" />
</p>

### Multi-writer safety (v1.7+)

Parallel ingest sub-agents can target the same wiki page if the user batches multiple sources. `scripts/wiki-lock.sh` provides per-file advisory locks: one writer acquires, the other waits and retries on the next pass. The PostToolUse auto-commit hook checks the lock list before staging, deferring the commit while writes are in flight.

<p align="center">
  <img src="assets/diagrams/multi-writer-locking.svg" alt="Architecture diagram: two parallel writers attempt to acquire a lock on the same wiki page via wiki-lock.sh. One writer is granted, writes the page, and releases the lock. The other writer logs the skip and retries on the next pass. No corruption, no half-written pages." width="100%" />
</p>

### Hybrid retrieval (v1.7+, opt-in)

The `/wiki-retrieve` skill ships a three-tier retrieval pipeline based on [Anthropic's Sept 2024 contextual retrieval research](https://www.anthropic.com/news/contextual-retrieval). BM25 is the always-on sparse layer. The contextual-prefix tier is consent-gated (`--allow-egress`) for users who want to send page bodies to the Anthropic API for prefix generation. Cosine rerank uses a local ollama model by default. The 50-query benchmark in v1.7 measured +32 percentage points top-1 accuracy and +41 percent error reduction vs the v1.6 baseline.

<p align="center">
  <img src="assets/diagrams/hybrid-retrieval.svg" alt="Architecture diagram: user query feeds both BM25 sparse search and an optional contextual-prefix Anthropic API call. Both feed a cosine rerank via local ollama embeddings. The output is a ranked list of candidates with --explain traceability for every score." width="100%" />
</p>

> ℹ️ Provision the pipeline with `bash bin/setup-retrieve.sh`. It builds the BM25 index, prompts for egress consent, and validates the ollama connection. The pipeline degrades gracefully: if any tier is unavailable, the rest still return useful results.

---

## MCP Setup (Optional)

MCP lets Claude read and write vault notes directly without copy-paste.

**Option A (REST API based):**

1. Install the Local REST API plugin in Obsidian
2. Copy your API key
3. Run:

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-obsidian"],
  "env": {
    "OBSIDIAN_API_KEY": "your-key",
    "OBSIDIAN_HOST": "127.0.0.1",
    "OBSIDIAN_PORT": "27124",
    "NODE_TLS_REJECT_UNAUTHORIZED": "0"
  }
}' --scope user
```

**Option B (filesystem based, no plugin needed):**

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@bitbonsai/mcpvault@latest", "/path/to/your/vault"]
}' --scope user
```

> ℹ️ Both transports are auto-detected by `scripts/detect-transport.sh`. The result lands in `.vault-meta/transport.json`. To pin a manual choice, edit that file and set `"manual_override": true` (v1.8.2+ honors it).

---

## Plugins

### Core Plugins (built into Obsidian, no install needed)

| Plugin | Purpose |
|--------|---------|
| **Bases** | Powers `wiki/meta/dashboard.base`: native database views. Available since Obsidian v1.9.10 (August 2025). Replaces Dataview for the primary dashboard. |
| **Properties** | Visual frontmatter editor |
| **Backlinks**, **Outline**, **Graph view** | Standard navigation |

### Pre-installed Community Plugins (ship with this vault)

Enable in **Settings → Community Plugins → enable**:

| Plugin | Purpose | Notes |
|--------|---------|-------|
| **Calendar** | Right-sidebar calendar with word count + task dots | Pre-installed |
| **Thino** | Quick memo capture panel | Pre-installed |
| **Excalidraw** | Freehand drawing canvas, annotate images | Pre-installed* |
| **Banners** | Notion-style header image via `banner:` frontmatter | Pre-installed |

\* Excalidraw `main.js` (8MB) is downloaded automatically by `setup-vault.sh`. It is not tracked in git.

### Also install from Community Plugins (not pre-installed)

| Plugin | Purpose |
|--------|---------|
| **Templater** | Auto-fills frontmatter from `_templates/` |
| **Obsidian Git** | Auto-commits vault every 15 minutes |
| **Dataview** *(optional, legacy)* | Only needed for the legacy `wiki/meta/dashboard.md` queries. The primary dashboard now uses Bases. |

Also install the **[Obsidian Web Clipper](https://obsidian.md/clipper)** browser extension. Sends web pages to `.raw/` in one click.

---

## CSS Snippets (auto-enabled by setup-vault.sh)

Three snippets ship with the vault and are enabled automatically:

| Snippet | Effect |
|---------|--------|
| `vault-colors` | Color-codes `wiki/` folders by type in the file explorer (blue = concepts, green = sources, purple = entities) |
| `ITS-Dataview-Cards` | Turns Dataview `TABLE` queries into visual card grids: use ` ```dataviewjs ` with `.cards` class |
| `ITS-Image-Adjustments` | Fine-grained image sizing in notes: append `\|100` to any image embed |

---

## Banner Plugin

Add to any wiki page frontmatter:

```yaml
banner: "_attachments/images/your-image.png"
banner_icon: "🧠"
```

The page renders a full-width header image in Obsidian. Works great for hub pages and overviews.

---

## File Structure

```
claude-obsidian/
├── .claude-plugin/
│   ├── plugin.json              # manifest
│   └── marketplace.json         # distribution
├── skills/                       # 15 Claude Code skills (v1.9.2)
│   ├── wiki/                    # orchestrator + references
│   ├── wiki-ingest/             # source ingestion
│   ├── wiki-query/              # answer questions from the vault
│   ├── wiki-lint/               # vault health check
│   ├── wiki-cli/                # Obsidian CLI transport (v1.7+)
│   ├── wiki-retrieve/           # hybrid retrieval (v1.7+, opt-in)
│   ├── wiki-mode/               # methodology modes router (v1.8+)
│   ├── wiki-fold/               # log rollup (DragonScale opt-in)
│   ├── save/                    # /save: file conversations to wiki
│   ├── autoresearch/            # autonomous research loop
│   ├── canvas/                  # visual layer (images, PDFs, notes)
│   ├── defuddle/                # web extraction wrapper
│   ├── obsidian-bases/          # Bases schema reference
│   ├── obsidian-markdown/       # OFM syntax reference
│   └── think/                   # 10-principle thinking framework (v1.9+)
├── agents/
│   ├── verifier.md              # pre-commit audit agent (v1.7.1+)
│   ├── wiki-ingest.md           # parallel batch ingestion agent
│   └── wiki-lint.md             # health check agent
├── commands/                     # slash command entry points
├── hooks/
│   └── hooks.json               # SessionStart + Stop + PostToolUse hooks
├── scripts/                      # 12 helper scripts (transport, locking, retrieval, etc.)
├── tests/                        # 9 hermetic test suites (~1240 assertions, make test)
├── bin/                          # 5 setup scripts (setup-vault, setup-retrieve, setup-mode, etc.)
├── _templates/                   # Obsidian Templater templates
├── wiki/                         # seeded vault content (demo)
│   ├── canvases/                # welcome.canvas + main.canvas
│   ├── concepts/                # seeded: LLM Wiki Pattern, Hot Cache, Compounding Knowledge
│   ├── entities/                # seeded: Andrej Karpathy
│   ├── sources/                 # populated by your first ingest
│   └── meta/
│       ├── dashboard.base       # Bases dashboard (primary)
│       └── dashboard.md         # Legacy Dataview dashboard (optional)
├── docs/                         # guides + audits + release notes
├── .raw/                         # source documents (hidden in Obsidian)
├── .obsidian/snippets/           # vault-colors.css (3-color scheme)
├── WIKI.md                       # full schema reference
├── CLAUDE.md                     # project instructions
└── README.md                     # this file
```

---

## AutoResearch: program.md

The `/autoresearch` command is configurable. Edit [`skills/autoresearch/references/program.md`](skills/autoresearch/references/program.md) to control:

- What sources to prefer (academic, official docs, news)
- Confidence scoring rules
- Max rounds and max pages per session
- Domain-specific constraints

The default program works for general research. Override it for your domain. A medical researcher would add "prefer PubMed". A business analyst would add "focus on market data and filings".

---

## Seed Vault

This repo ships with a seeded vault. Open it in Obsidian and you will see:

- `wiki/concepts/`: LLM Wiki Pattern, Hot Cache, Compounding Knowledge
- `wiki/entities/`: Andrej Karpathy
- `wiki/sources/`: empty until your first ingest
- `wiki/meta/dashboard.base`: Bases dashboard (works in any Obsidian v1.9.10+)
- `wiki/meta/dashboard.md`: Legacy Dataview dashboard (optional fallback)

The graph view will show a connected cluster of 5 pages. This is what the wiki looks like after one ingest. Add more sources and it grows from there.

<p align="center">
  <img src="wiki/meta/wiki-graph-grow.gif" alt="Animated GIF: claude-obsidian knowledge graph growing from a few seeded pages to a dense web of cross-referenced concepts after multiple ingests" width="48%" />
  <img src="wiki/meta/workflow-loop.gif" alt="Animated GIF: claude-obsidian workflow loop showing ingest, query, lint, save, and hot-cache refresh cycle" width="48%" />
</p>

---

## Companion: claude-canvas

For the visual layer, [claude-canvas](https://github.com/AgriciDaniel/claude-canvas) adds AI-orchestrated canvas creation: knowledge graphs, presentations, flowcharts, mood boards with 12 templates and 6 layout algorithms. Auto-detects claude-obsidian vaults.

```bash
claude plugin install AgriciDaniel/claude-canvas
```

---

## FAQ

**What is the best AI second brain app?**
The best AI second brain keeps your data yours. claude-obsidian stores everything as plain Markdown files you own (no database, no lock-in, no subscription) and lets Claude read, link, and organize them into one connected knowledge graph. It is free and open source (MIT).

**How do I build a second brain with AI?**
Drop any source into the vault. Claude reads it, extracts the entities and concepts, links them to what you already have, and files it into a structured Obsidian vault. You ask questions; it answers from everything it has read and cites the pages. The knowledge base gets richer and more connected with every session.

**How do I connect Claude to Obsidian as a second brain?**
Two lines: `git clone https://github.com/AgriciDaniel/claude-obsidian`, then `cd claude-obsidian && bash bin/setup-vault.sh`. Open the folder as an Obsidian vault, open Claude Code in the same folder, and type `/wiki`. Full steps in [Quick Start](#quick-start).

**Is there a good Notion alternative for a private, AI-powered knowledge base?**
Yes. claude-obsidian is an open-source, local-first alternative: your notes are plain Markdown on your own disk instead of a hosted database, and AI organizes them for you. No vendor lock-in and no monthly fee.

**Does this auto-sync across devices?**
Not on its own. The vault is a plain folder of Markdown files. Pair with Obsidian Sync, Obsidian Git, or any file-sync tool (Syncthing, iCloud, Dropbox) for cross-device sync.

**Can multiple people edit the same vault safely?**
Yes (v1.7+). Per-file advisory locking via [`scripts/wiki-lock.sh`](scripts/wiki-lock.sh) prevents concurrent writes from corrupting pages. Parallel ingest sub-agents acquire locks before writes. Stale locks self-reap after 60 seconds.

**What is the difference between `hot.md` and `index.md`?**
`hot.md` is the recent-context cache (~500 words, refreshed each session). `index.md` is the master catalog of every page in the vault. Claude reads `hot.md` first, then `index.md`, then drills into specific pages. The two-layer design keeps token cost low for repeat queries.

**Can I use this without Claude Code?**
The skills are Agent Skills compatible (experimental support for OpenAI Codex CLI, Cursor, Windsurf, Gemini CLI, Goose). Production verification is only on Claude Code today. Cross-host install paths follow each host's conventions but skill discovery may differ.

**How do I migrate from Dataview to Bases?**
Both ship side-by-side. `wiki/meta/dashboard.base` is the primary; `wiki/meta/dashboard.md` is the legacy Dataview fallback. Pick one in Obsidian, the other is harmless. Bases requires Obsidian v1.9.10+ (August 2025).

**What is the difference between Methodology Modes (LYT/PARA/Zettelkasten) and Vault Use Cases (Website/GitHub/Business)?**
Methodology Modes (v1.8+) control **how** pages are organized: folder structure + filename conventions. Vault Use Cases (v1.0+) describe **what** the vault is for: content type. They compose. A "Business" vault using PARA methodology is a valid configuration.

**Does this send my notes to Anthropic?**
No by default. The optional `/wiki-retrieve` skill has API egress (`contextual-prefix.py`) gated behind the `--allow-egress` consent flag. Without that flag, retrieval is fully local (BM25 + optional ollama rerank). Web egress in `/autoresearch` follows the same opt-in principle.

**What is the difference between the public build and AI Marketing Hub Pro?**
Both share the same MIT-licensed core on [`AgriciDaniel/claude-obsidian`](https://github.com/AgriciDaniel/claude-obsidian), which is the recommended install for everyone. AI Marketing Hub Pro members get earliest access to in-development features before they ship here, plus direct collaboration and the community. There are no paid-only features in the core.

**What is DragonScale Memory?**
An optional opt-in extension (`bash bin/setup-dragonscale.sh`) that adds four memory mechanisms: log folds (rollup of past entries), deterministic page addresses (counter-based unique IDs), semantic tiling lint (chunk-boundary validation via ollama), and boundary-first autoresearch (research the vault's "frontier" first). Not required for normal use. Full guide: [`docs/dragonscale-guide.md`](docs/dragonscale-guide.md).

---

## Requirements

| Component | Minimum | Notes |
|-----------|---------|-------|
| Claude Code | latest | https://claude.com/claude-code |
| Obsidian | v1.9.10+ (for Bases) | https://obsidian.md. v1.6+ works with Dataview fallback. |
| Python | 3.10+ | For the optional retrieval pipeline and the test suite |
| Bash | 4.0+ (or zsh) | For setup scripts |
| Git | any | For vault auto-commits via the Obsidian Git plugin |

**Optional:**

- **ollama** (for local rerank in `/wiki-retrieve`)
- **defuddle-cli** (for clean web extraction in `/defuddle`)
- **Anthropic API key** (for `/wiki-retrieve` contextual prefix tier, opt-in via `--allow-egress`)
- **Local REST API plugin** (for the REST-API MCP transport)

---

## Uninstall

Plugin install:

```bash
claude plugin uninstall claude-obsidian@agricidaniel-claude-obsidian
claude plugin marketplace remove AgriciDaniel/claude-obsidian
```

Clone install (delete the folder):

```bash
rm -rf /path/to/claude-obsidian
```

Your vault content (under `wiki/`) is plain Markdown and survives uninstall. To clear the runtime state without uninstalling, run `make clean-test-state` from the repo root.

---

## Contributing

PRs welcome. Read these first:

- [`CONTRIBUTING.md`](CONTRIBUTING.md): workflow, six-cut self-review checklist, commit conventions, hermetic test requirements
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md): Contributor Covenant v2.1
- [`SECURITY.md`](SECURITY.md): responsible security disclosure policy
- [`CHANGELOG.md`](CHANGELOG.md): version history (latest: v1.9.2)

Issue + PR templates available under [`.github/`](.github/). CI runs `make test` + SKILL.md frontmatter validation + plugin manifest JSON validity on every PR. The pre-commit verifier agent at [`agents/verifier.md`](agents/verifier.md) applies the six-cut + agent kernel to staged diffs.

---

## Related Projects

- 🎨 [**claude-canvas**](https://github.com/AgriciDaniel/claude-canvas): visual canvas orchestration (12 templates, 6 layout algorithms, AI image generation). Companion to this plugin.
- 📊 [**claude-ads**](https://github.com/AgriciDaniel/claude-ads): multi-platform paid advertising audit (250+ checks across Google, Meta, LinkedIn, TikTok, Microsoft, Apple, Amazon Ads).
- 🔍 [**claude-seo**](https://github.com/AgriciDaniel/claude-seo): technical SEO + GEO audit suite.
- 🧠 [**best-practices**](https://github.com/AgriciDaniel/best-practices): composable engineering kernel. Source for the six-cut + agent kernel that `agents/verifier.md` enforces.

---

## Community

- 📝 [**Blog post**](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain): deep dive with competitor analysis, data charts, and workflow demos
- 💬 [**AI Marketing Hub**](https://www.skool.com/ai-marketing-hub): 2,800+ members, free community
- ⚡ [**AI Marketing Hub Pro**](https://www.skool.com/ai-marketing-hub-pro): early access to in-development features and direct collaboration
- 🎬 [**YouTube**](https://www.youtube.com/@AgriciDaniel): tutorials and demos
- 🔧 [**All open-source tools**](https://github.com/AgriciDaniel): claude-seo, claude-ads, claude-blog, and more

---

## License

MIT License. See [LICENSE](LICENSE) for full text. Free for personal and commercial use. Attribution appreciated but not required.

---

## Star History

<a href="https://star-history.com/#AgriciDaniel/claude-obsidian&Date">
  <img src="https://api.star-history.com/svg?repos=AgriciDaniel/claude-obsidian&type=Date" alt="Star history chart for AgriciDaniel/claude-obsidian on GitHub" width="640" />
</a>

---

*Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Built by [Agrici Daniel](https://agricidaniel.com/about). Compounding knowledge is the highest-leverage habit a thinking person can build.*


## Docs

### compound-vault-guide.md

# Compound Vault — v1.7 Guide

**Status:** v1.7.0 (codename "Compound Vault refoundation"), released 2026-05-17  
**Audience:** users upgrading from v1.6, new adopters, and skill authors integrating with v1.7+ primitives  
**Companion docs:** [dragonscale-guide.md](dragonscale-guide.md) (optional Memory extension), [install-guide.md](install-guide.md), [CHANGELOG.md](../CHANGELOG.md)

---

## Why "Compound Vault"

The v1.7 line introduces a system name — **Compound Vault** — that names the architecture, distinct from the plugin name (`claude-obsidian`). The plugin name stays for SEO continuity and the existing 4.1k+ stars; the system name covers the 13 cohering skills that make the architecture work.

Three-clause positioning:

> *"Compounding vault, not chat. CLI-native, not chat-window. Methodology-aware, not generic."*

- **Compounding vault** — Karpathy's LLM Wiki pattern. Knowledge accumulates across sessions; the wiki gets richer with every ingest.
- **CLI-native** — Obsidian 1.12 made the `obsidian` binary a first-class surface. v1.7 makes it the default transport and demotes MCP to fallback.
- **Methodology-aware** — partial in v1.7 (modes ship in v1.8). The framing already shapes the v1.7 scope.

Drop-in tagline candidate (for blog/marketing):

> **"Karpathy's wiki, in your Obsidian."**

---

## What changed from v1.6 (executive summary)

v1.7 ships in four workstreams (§3.1 substrate / §3.2 transport / §3.3 retrieval / §3.4 concurrency), each one independent enough to roll back if it causes trouble. None are breaking — a v1.6 vault that does nothing on upgrade continues to behave exactly as v1.6.

| Workstream | What | Why | Adopter action |
|---|---|---|---|
| §3.1 Substrate | 3 skills upgrade soft-defer → hard-prefer for `kepano/obsidian-skills` | Stop competing with the platform owner | `claude plugin marketplace add kepano/obsidian-skills` (recommended) |
| §3.2 Transport | New `wiki-cli` skill + `detect-transport.sh` + decision tree | Obsidian 1.12 CLI is the fastest, safest write path | None — auto-detected on first session |
| §3.3 Retrieval | New `wiki-retrieve` skill + contextual prefix + BM25 + cosine rerank | Anthropic Sept 2024 research: 35-67% retrieval-failure reduction | `bash bin/setup-retrieve.sh` (opt-in) |
| §3.4 Concurrency | New `wiki-lock.sh` + 4 skill guards + hook debounce | Close the latent multi-writer corruption bug | None — universally beneficial, no setup |

---

## §3.1 Substrate dependency on kepano/obsidian-skills

**What it is:** Three claude-obsidian skills (`obsidian-markdown`, `obsidian-bases`, `canvas`) overlap with skills in `kepano/obsidian-skills` (by Steph Ango, Obsidian's CEO). In v1.6 we soft-deferred ("if kepano is installed, prefer it"). In v1.7 we hard-prefer: kepano is canonical; our copies are the floor.

**Why:** Continuing to ship parallel implementations of platform-owner primitives is a structural losing fight. The kepano marketplace has 30.5k+ stars; we have 4.1k+. Adopting kepano as substrate signals alignment and frees us to invest in the *workflow* layer (ingest, query, lint, autoresearch, save, retrieve) that no one else owns.

**What changed in the codebase:**
- `skills/obsidian-markdown/SKILL.md:11` — preface rewrites to "This skill is a self-contained fallback. Prefer `kepano/obsidian-skills`."
- `skills/obsidian-bases/SKILL.md:11` — same pattern.
- `skills/canvas/SKILL.md:14` — same pattern (json-canvas spec defers to kepano; wiki-scoped workflows stay claude-obsidian's).
- `skills/defuddle/SKILL.md:11` — documented as canonical (kepano does not ship a defuddle skill).
- `.claude-plugin/marketplace.json` — `recommendedCompanions` array names `kepano/obsidian-skills` with install hint, rationale, and repo link.

**Adopter action:** Run `claude plugin marketplace add kepano/obsidian-skills`. Existing skills keep working without it (the local fallbacks remain functional).

---

## §3.2 Default transport — Obsidian CLI with fallback chain

**What it is:** A four-tier transport stack with auto-detection. New skill `wiki-cli` documents the CLI recipes. New script `scripts/detect-transport.sh` writes `.vault-meta/transport.json` so other skills can consult it.

Fallback chain (highest to lowest precedence):
1. **cli** — `obsidian-cli` binary (Obsidian 1.12+). No MCP server, no TLS, no plugin.
2. **mcp-obsidian** — REST-API-backed MCP server (Local REST API plugin required). Auto-detection deferred to v1.7.x.
3. **mcpvault** — Filesystem-backed MCP server (BM25 search; no Obsidian plugin). Auto-detection deferred.
4. **filesystem** — Direct `Read`/`Write`/`Edit` tools. Always available; the floor.

**Why:** v1.6 documented four equal transports. Skills used direct `Read`/`Write` by default. v1.7 sharpens the recommendation and makes selection a one-line lookup against `.vault-meta/transport.json`.

**Architecture:**

```
detect-transport.sh (run at session start or vault setup)
    │
    └─ writes → .vault-meta/transport.json
                {
                  "preferred": "cli" | "filesystem",
                  "fallback_chain": [...],
                  "available": { cli: {...}, filesystem: {...}, mcp_obsidian: null, mcpvault: null }
                }

skills (wiki-ingest, wiki-query, save, autoresearch, wiki-lint):
    ├─ each has a "## Transport (v1.7+)" section near the top
    ├─ reads transport.json at runtime
    └─ uses obsidian-cli if "preferred": "cli", else Read/Write
```

**Adopter action:** None — the detection runs automatically and refreshes after 7 days. To force a refresh: `bash scripts/detect-transport.sh --force`. To manually pin to an MCP transport, edit `.vault-meta/transport.json` and set `"manual_override": true` so the detection script leaves your edit alone.

**See:** [`wiki/references/transport-fallback.md`](../wiki/references/transport-fallback.md) for the full decision tree and [`skills/wiki-cli/SKILL.md`](../skills/wiki-cli/SKILL.md) for the per-operation recipes.

---

## §3.3 Hybrid retrieval pipeline — wiki-retrieve (opt-in)

**What it is:** A new opt-in skill that replaces the v1.6 static `Read(hot.md) → Read(index.md) → Read(N pages)` query path with chunk-level retrieval using BM25 + cosine rerank over contextually-prefixed chunks. Implements Anthropic's [Sept 2024 Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) pattern as agent-skill plumbing.

**Why:** Page-level granularity loses to chunk-level granularity any time the answer lives in a specific passage. Anthropic measured a 35% retrieval-failure reduction from contextual prefixes, 49% from hybrid BM25+vector, and 67% from adding a reranker. v1.7 implements the contextual + sparse + rerank stack. (A separate dense vector stage is on the v1.7.x roadmap.)

**Architecture:**

```
INGEST (one-time + incremental):

  wiki/<page>.md
       │
       ▼
  scripts/contextual-prefix.py
       │  ├─ chunks on paragraph boundaries (~500 tokens target, 200 char overlap)
       │  └─ generates 1-2 sentence prefix per chunk
       │       tier 1: ANTHROPIC_API_KEY  → Anthropic API (Haiku, prompt-cached
       │                                    when body ≥ ~16 KB / Haiku 4.5 floor)
       │       tier 2: claude on PATH    → `claude -p` subprocess
       │       tier 3: synthetic          → frontmatter title + first paragraph
       │
       ▼  .vault-meta/chunks/<address>/chunk-NNN.json

  scripts/bm25-index.py build
       └─ inverted index over chunks' contextualized_text → .vault-meta/bm25/index.json

QUERY:

  query string
       │
       ▼
  scripts/retrieve.py "<query>" --top 5
       ├─ scripts/bm25-index.py query → top-20 candidates by BM25
       ├─ scripts/rerank.py            → cosine on nomic-embed-text via ollama
       │     (no-op if ollama unreachable; BM25 order preserved)
       └─ page-address dedupe          → final top-5 with absolute_path
       │
       ▼
  caller (wiki-query / autoresearch) reads cited pages and synthesizes
```

**Feature gating:** Other skills detect wiki-retrieve via:

```bash
[ -x scripts/retrieve.py ] && [ -d .vault-meta/chunks ] && [ -f .vault-meta/bm25/index.json ]
```

If detection fails, skills fall back to the v1.6 legacy read order. The skill never breaks the base plugin.

**Cost ceiling:** ~$12 per 1,000 documents per Anthropic's published figure (Haiku + prompt caching, tier 1). Tier 2 (claude CLI) is free in dollars but slower. Tier 3 (synthetic) is free and hermetic; loses most of the contextual benefit but BM25 + rerank still work.

**Adopter action:**

```bash
bash bin/setup-retrieve.sh         # full provisioning (auto-picks prefix tier)
bash bin/setup-retrieve.sh --no-llm  # force tier 3 (zero LLM dependency)
bash bin/setup-retrieve.sh --check   # diagnostics only; no provisioning
```

After setup, `wiki-query` standard/deep modes automatically use the new pipeline. Quick mode (hot.md only) is unchanged.

**See:** [`skills/wiki-retrieve/SKILL.md`](../skills/wiki-retrieve/SKILL.md) for the full skill spec, recipe reference, and v1.7.x roadmap (BGE cross-encoder, Cohere Rerank, separate dense vector stage).

---

## §3.4 Multi-writer safety — wiki-lock (core)

**What it is:** Per-file advisory locking via `scripts/wiki-lock.sh`. Every wiki page write MUST be preceded by `wiki-lock acquire <path>` and followed by `wiki-lock release <path>`.

**Why:** v1.6 had a latent corruption bug. `skills/wiki-ingest/SKILL.md:259-264` documented "single-writer only" as a convention, but the actual page-write paths had no enforcement. Two parallel sub-agents writing to the same wiki page could silently trample each other. The Karpathy-LLM-Wiki-Stack README explicitly warned about this. v1.7 closes the hole.

**Design (age-based, not flock-style):**

`flock(2)` advisory locks release when the holding process exits. That doesn't fit our model where `acquire` and `release` are SEPARATE bash invocations from the same skill (each Bash tool call is its own short-lived process — neither's PID survives long enough to mean anything). So `wiki-lock.sh` uses:

- **Atomic noclobber-write of a lockfile** (race-safe on POSIX filesystems).
- **Epoch-based AGE staleness**: a lock older than `STALE_AFTER_SEC` (default 60) is auto-reaped. Crashed holders unblock in ≤60s without manual intervention.
- **Cross-process release allowed**: `release` is `rm -f` (no PID match required). Skill authors are trusted to release locks they acquire. The `wiki-lock clear-stale --max-age 0` command is the canonical recovery path.
- **PID in the lockfile is informational only** (helpful for `list` and debugging).

**Skill integration:**

Four skills gained "## Concurrency (v1.7+)" sections with the recipe:

```bash
if bash scripts/wiki-lock.sh acquire wiki/concepts/Foo.md; then
  # … do the write via the §Transport-selected method …
  bash scripts/wiki-lock.sh release wiki/concepts/Foo.md
else
  # rc=75 = EX_TEMPFAIL = another writer in flight. Retry once after 2s;
  # if still held, log to wiki/log.md and skip this page.
  sleep 2
  bash scripts/wiki-lock.sh acquire wiki/concepts/Foo.md && {
    # write …
    bash scripts/wiki-lock.sh release wiki/concepts/Foo.md
  } || echo "skipped wiki/concepts/Foo.md (locked)"
fi
```

**Hook integration:** `hooks/hooks.json` PostToolUse now defers `git add` if any locks are currently held. Prevents torn commits during multi-agent ingest. Falls through gracefully when `wiki-lock.sh` is absent.

**Adopter action:** None — `wiki-lock.sh` is core in v1.7 (no opt-in). Sub-agents that don't follow the acquire/release pattern are racing against any other writer (as before — but now there's a tool to fix it).

**Test coverage:** `tests/test_wiki_lock.sh` (14 hermetic assertions) and `tests/test_concurrent_write.sh` (the critical correctness gate — 10 parallel workers, no losses, no garbled lines). `make test-concurrent` and `make test-lock`.

**See:** [`scripts/wiki-lock.sh`](../scripts/wiki-lock.sh) header comments for the full semantics, and `skills/wiki-ingest/SKILL.md` §Concurrency for the canonical integration pattern.

---

## Skill inventory (v1.7)

13 skills total. New in v1.7: `wiki-cli`, `wiki-retrieve`.

| Skill | Status | Role |
|---|---|---|
| `wiki` | core | Setup / scaffold / sub-skill router |
| `wiki-ingest` | core | Source → wiki pages with cross-refs |
| `wiki-query` | core | Question answering (now uses wiki-retrieve if installed) |
| `wiki-lint` | core | Health check (orphans, dead links, addresses, tiling) |
| `wiki-fold` | DragonScale Mech 1 | Extractive log rollups |
| `wiki-cli` | **new in v1.7 (§3.2)** | Obsidian CLI transport wrapper |
| `wiki-retrieve` | **new in v1.7 (§3.3, opt-in)** | Contextual + BM25 + rerank |
| `save` | core | File conversations as wiki notes |
| `autoresearch` | core | Iterative web research → wiki |
| `canvas` | core (defers to kepano json-canvas) | Visual wiki layer |
| `defuddle` | core (canonical) | Web page cleaner |
| `obsidian-markdown` | core (defers to kepano) | Obsidian Flavored Markdown reference |
| `obsidian-bases` | core (defers to kepano) | Bases YAML reference |

---

## Scripts inventory (v1.7)

| Script | Status | Role |
|---|---|---|
| `allocate-address.sh` | DragonScale Mech 2 | Atomic c-NNNNNN allocator (flock) |
| `tiling-check.py` | DragonScale Mech 3 | Embedding-based duplicate lint (fcntl) |
| `boundary-score.py` | DragonScale Mech 4 | Frontier scoring for autoresearch |
| `detect-transport.sh` | **new in v1.7 (§3.2)** | Transport detection → transport.json |
| `contextual-prefix.py` | **new in v1.7 (§3.3)** | Chunk + 3-tier prefix generation |
| `bm25-index.py` | **new in v1.7 (§3.3)** | Sparse inverted index (flock) |
| `rerank.py` | **new in v1.7 (§3.3)** | Cosine rerank via ollama (fcntl on cache) |
| `retrieve.py` | **new in v1.7 (§3.3)** | Hybrid retrieval orchestrator |
| `wiki-lock.sh` | **new in v1.7 (§3.4)** | Per-file advisory locks (noclobber) |

---

## Tests (v1.7)

`make test` runs 7 suites. All hermetic — zero network, zero ollama, zero LLM calls.

| Target | File | Assertions | Coverage |
|---|---|---|---|
| `make test-address` | `tests/test_allocate_address.sh` | ~10 | DragonScale Mech 2 |
| `make test-tiling` | `tests/test_tiling_check.py` | ~15 | DragonScale Mech 3 |
| `make test-boundary` | `tests/test_boundary_score.py` | ~35 | DragonScale Mech 4 |
| `make test-bm25` | `tests/test_bm25_index.py` | ~30 | tokenize, BM25 monotonicity, IDF |
| `make test-retrieve` | `tests/test_retrieve.py` | 22 | cosine, rerank, end-to-end subprocess |
| `make test-lock` | `tests/test_wiki_lock.sh` | 14 | acquire, release, age-based reap |
| `make test-concurrent` | `tests/test_concurrent_write.sh` | 6 | **the critical multi-writer correctness gate** |

The "hermetic test invariant" is preserved: nothing in `make test` requires the network, ollama, or any API key. Optional pipelines (contextual prefix with Anthropic API, rerank with ollama cosine) are tested via mocks and graceful fallbacks.

---

## What v1.7 is NOT

- Not a rewrite. DragonScale Mechanisms 1-4 are preserved and unchanged.
- Not a breaking change. v1.6 vaults that don't run setup-retrieve.sh see no behavior difference (modulo the wiki-lock integration, which is universally beneficial and adds no setup).
- Not a paid plugin. License stays MIT.
- Not a GUI Obsidian-plugin shell. Deferred to v2.5+ (the Claudian/deivid11 wrapper pattern is item #7 in the May 2026 gap-analysis backlog).
- Not multi-vault federation. Deferred to v2.x.

---

## Roadmap pointers

The May 2026 gap analysis identified 20 backlog items. v1.7 ships items 1, 2, 3, 4 (the top-quartile by value/effort) plus the latent-bug fix. Next milestones (subject to user prioritization):

- **v1.8** — Methodology modes (LYT / PARA / Zettelkasten / Generic via `wiki-mode`) + periodic reviews (`wiki-review`). Closes gaps #6 + #11.
- **v1.9** — Multimodal ingest adapters (YouTube, PDF, EPUB, image OCR via `wiki-ingest-multimodal`). Closes gaps #8 + #12.
- **v2.0** — NotebookLM-class derivative outputs (audio, quiz, flashcards, study guide via `wiki-derive`). Closes gaps #5 + #9 + #14.

Full plan: `~/.claude/plans/read-in-full-the-hidden-sun.md`.

---

## See also

- [CHANGELOG.md](../CHANGELOG.md) — v1.7.0 entry
- [docs/dragonscale-guide.md](dragonscale-guide.md) — DragonScale Memory extension (Mechanisms 1-4)
- [docs/install-guide.md](install-guide.md) — installation
- [wiki/references/transport-fallback.md](../wiki/references/transport-fallback.md) — transport decision tree
- [wiki/concepts/DragonScale Memory.md](../wiki/concepts/DragonScale%20Memory.md) — spec
- Anthropic Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval
- kepano/obsidian-skills: https://github.com/kepano/obsidian-skills
- Karpathy LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f


### methodology-modes-guide.md

# Methodology Modes Guide — v1.8.0

**Status:** v1.8.0 GA (2026-05-17)
**Scope:** picks an organizational style for your vault and routes new pages accordingly.
**Origin:** closes priority gap 5 from the May 2026 compass artifact.

---

## TL;DR

Pick a mode that matches how YOU think:

| You think in... | Pick |
|---|---|
| Topic clusters + navigation by following links | **LYT** |
| Active projects vs ongoing responsibilities vs reference material | **PARA** |
| Atomic claims with unique IDs and dense linking | **Zettelkasten** |
| No methodology / want v1.7 default | **Generic** |

```bash
bash bin/setup-mode.sh           # interactive
bash bin/setup-mode.sh --mode lyt   # non-interactive
```

After picking, `wiki-ingest`, `save`, and `autoresearch` consult the mode before deciding where to file new pages. Existing files are NOT moved; the mode only affects future filing.

---

## Why methodology modes exist

The May 2026 compass artifact identified 5 priority gaps. claude-obsidian v1.7 closed 4 of them (substrate alignment, default transport, hybrid retrieval, multi-writer safety) and deferred the 5th — methodology support — to v1.8.

The audit §9 axis evaluation called methodology support a **TIE** in May 2026: nobody else in the Claude+Obsidian space ships it as a first-class skill. Ideaverse Pro 2.0 ($200 paid vault) ships LYT as an opinionated structure but it's a vault, not a skill set. PARA, Zettelkasten, and mode-aware routing are entirely unserved.

v1.8.0 closes that gap. After this release, claude-obsidian is **#1 on 5 of 7 axes** per the compass framework (compounding wiki, multi-writer safety, retrieval architecture, license openness, methodology support). The remaining 2 (GUI ergonomics, derivative outputs) require larger releases (v2.5+ for GUI, v2.0 for derive).

---

## The four modes

### Generic (default)

**Philosophy:** no methodology imposed. Same as v1.6/v1.7.

**Filing convention:**
- `wiki/sources/<slug>.md` — ingested source documents
- `wiki/entities/<Name>.md` — people, orgs, products (capitalization preserved)
- `wiki/concepts/<Name>.md` — concepts and frameworks
- `wiki/sessions/<date>-<topic>.md` — session notes from `/save`

**When to use:**
- You're migrating from v1.7 and want zero behavior change
- You don't want to commit to a methodology yet
- You have your own organizational instincts and want minimal opinion

**Pros:** zero learning curve; matches v1.7 muscle memory; flexible.
**Cons:** no opinion to lean on; can sprawl in large vaults.

---

### LYT (Linking Your Thinking — Nick Milo)

**Philosophy:** the organizational primitive is the **MOC** (Map of Content). Atomic notes flat under one folder; MOCs link into clusters of notes. You navigate by following links, not by browsing folders.

**Filing convention:**
- `wiki/mocs/<topic>-moc.md` — Map of Content for a topic cluster
- `wiki/notes/<atomic-note>.md` — all atomic notes flat (no subfolders)
- Every atomic note has at least one MOC in its frontmatter `mocs:` field
- New ingests land in `wiki/notes/`; consumer skill also updates the relevant MOC

**Templates** (under `skills/wiki-mode/templates/lyt/`):
- `moc-template.md` — MOC scaffolding with core-notes / adjacent-MOCs / open-questions sections
- `atomic-template.md` — atomic note with MOC backlinks

**When to use:**
- Mid-to-large knowledge bases (>100 notes)
- You think in conceptual clusters and knowledge graphs
- You're an LYT practitioner or want to be one

**Pros:** scales beautifully; navigation gets richer with growth; explicit knowledge structure.
**Cons:** discipline of always-update-MOCs; flat notes folder can feel chaotic without good search.

---

### PARA (Tiago Forte)

**Philosophy:** organize by **actionability**, not topic. Active work in Projects (with deadline + outcome), ongoing responsibilities in Areas (no deadline), reference material in Resources (by topic), completed/inactive work in Archives.

**Filing convention:**
- `wiki/projects/<project-name>/<note>.md` — active projects
- `wiki/projects/inbox/<note>.md` — new ingests + session notes land here for triage
- `wiki/areas/<area-name>/<note>.md` — ongoing responsibilities
- `wiki/resources/<topic>/<note>.md` — reference material
- `wiki/resources/incoming/<note>.md` — new sources land here for topical sorting
- `wiki/resources/people/<Name>.md` — entity pages
- `wiki/resources/concepts/<Name>.md` — concept pages
- `wiki/archives/<year>/<note>.md` — completed projects, sunsetted areas

**Templates** (under `skills/wiki-mode/templates/para/`):
- `project-template.md` — project with status / deadline / outcome / next-action
- `area-template.md` — area with scope / standards / review cadence
- `resource-template.md` — reference material with topic + sources

**When to use:**
- Workflow-heavy users
- Knowledge workers managing many projects
- GTD-adjacent practitioners
- Anyone who has read Tiago Forte's "Building a Second Brain"

**Pros:** explicit project lifecycle; clear separation of active vs reference; matches how knowledge workers actually operate.
**Cons:** requires periodic review to move completed projects → archives; "incoming" buckets need to be processed.

---

### Zettelkasten (Niklas Luhmann's slip-box)

**Philosophy:** atomic notes, unique IDs, dense bidirectional linking. No folders. Every note answers exactly one idea. Notes find each other by ID references.

**Filing convention:**
- `wiki/<YYYYMMDDHHMMSSffffff>-<slug>.md` — flat under wiki/, timestamped IDs (20 digits = date + microseconds, collision-resistant)
- Every note has `id:`, `parent_id:` (optional), `child_ids:` (optional) in frontmatter
- No subdirectories; the wiki/ root is the whole vault
- All organization is via `parent_id` / `child_ids` / `[[ID]]` references in note bodies

**Templates** (under `skills/wiki-mode/templates/zettel/`):
- `atomic-template.md` — atomic claim with parent/child IDs + reasoning + sources

**When to use:**
- Academics and researchers
- Long-term thinkers building permanent knowledge artifacts
- Anyone who's read "How to Take Smart Notes" by Sönke Ahrens
- High-discipline, small-filing-surface preference

**Pros:** maximum link density; encourages atomic thinking; ages well over decades.
**Cons:** steepest discipline curve; flat file list is intimidating without good search; ID-based reference is less mnemonic than name-based.

---

## How modes interact with other skills

The integration is **automatic** — once you set a mode, `wiki-ingest`, `save`, and `autoresearch` consult it on every new page. You never have to think about it.

| Skill | What it does | How mode affects it |
|---|---|---|
| `wiki-ingest` | files new source/entity/concept pages | router determines destination folder per mode |
| `save` | files session notes from the current conversation | router determines `wiki/sessions/` (generic), `wiki/notes/` + MOC update (LYT), `wiki/projects/inbox/` (PARA), or `wiki/<ID>-session-...` (Zettel) |
| `autoresearch` | files synthesis page after a research loop | router determines `wiki/concepts/` (generic), `wiki/notes/` + topic MOC (LYT), `wiki/resources/<topic>/` (PARA), or `wiki/<ID>-...` (Zettel) |

The router (`scripts/wiki-mode.py route <type> "<name>"`) is the single source of truth. Skills don't compute paths themselves; they call the router and use what it returns.

---

## Switching modes later

Switching modes is **safe but does NOT auto-migrate**:

1. Run `bash bin/setup-mode.sh` (or `--mode <new-mode>` non-interactively)
2. The new mode is written to `.vault-meta/mode.json`
3. Existing files remain in their original locations and continue to work
4. New files file per the new mode
5. (Optional manual step) Use your file manager or `git mv` to migrate existing files to the new structure

**Why no auto-migration:** the wiki contains your thinking. Auto-rewriting paths could break wikilinks, lose data, or surprise you. Manual migration forces explicit decisions about what fits the new methodology vs what stays in its current home.

**Specifically for LYT migration:** after switching to LYT, run `lint the wiki` (skill: wiki-lint) to identify orphan pages that would benefit from MOC inclusion.

---

## Mode config file

`.vault-meta/mode.json` is the active mode declaration. It's **gitignored by default** — the file is treated as host-specific runtime config. To commit your mode choice across machines / collaborators:

```bash
git add -f .vault-meta/mode.json
git commit -m "chore: declare vault mode as <mode>"
```

The file schema:

```json
{
  "schema_version": 1,
  "mode": "lyt|para|zettelkasten|generic",
  "configured_at": "2026-05-17T00:00:00Z",
  "config": {
    "lyt": {"moc_folder": "wiki/mocs/", "notes_folder": "wiki/notes/"},
    "para": {"projects_folder": "...", "areas_folder": "...", "resources_folder": "...", "archives_folder": "..."},
    "zettelkasten": {"id_format": "YYYYMMDDHHMMSSffffff", "no_folders": true, "root_folder": "wiki/"},
    "generic": {"sources_folder": "wiki/sources/", "entities_folder": "wiki/entities/", "concepts_folder": "wiki/concepts/", "sessions_folder": "wiki/sessions/"}
  }
}
```

The `config` block always includes all 4 modes. The active mode is named by `mode`. Per-mode folder paths can be overridden in your `mode.json` if you want non-default conventions.

---

## When NOT to use mode-awareness

- **Tiny vaults** (<20 notes): the overhead of organization isn't justified yet. Stick with generic.
- **Vaults you didn't choose to organize**: if you don't care about methodology, don't pick one. Generic is honest.
- **Cross-project shared vaults** (per global CLAUDE.md `/save` convention): the personal vault at `~/Documents/Obsidian Vault/` has its own organizational choices; the project's mode-router only applies to the project's own `wiki/`.

---

## Roadmap from here

v1.8.0 closes priority gap 5. The compass artifact's full picture:

| Axis (per audit §9) | v1.7.2 status | v1.8.0 status | Path to LEAD |
|---|---|---|---|
| Compounding wiki primitive | #1 | #1 | ✓ |
| Multi-writer safety | #1 | #1 | ✓ |
| Retrieval architecture (free tier) | #1 | #1 | ✓ |
| License / openness | #1 | #1 | ✓ |
| **Methodology support** | TIE | **#1** ← v1.8.0 closes | ✓ |
| Derivative outputs (audio/video/quiz) | NO | NO | v2.0 (wiki-derive) |
| GUI / install ergonomics | NO | NO | v2.5+ (Community Plugin fork) |

After v1.8.0: **#1 on 5 of 7 axes per compass framework**. The remaining 2 axes require multi-release effort:
- **v1.9** — multimodal ingest (YouTube / PDF / EPUB / image OCR)
- **v2.0** — `wiki-derive` skill: audio overviews, quiz generation, study guides, mindmap synthesis (NotebookLM parity)
- **v2.5+** — Community Plugin GUI shell (mainstream Obsidian user reach)

---

## Cross-reference

- [`skills/wiki-mode/SKILL.md`](../skills/wiki-mode/SKILL.md) — the skill itself
- [`scripts/wiki-mode.py`](../scripts/wiki-mode.py) — router + config helper
- [`bin/setup-mode.sh`](../bin/setup-mode.sh) — interactive setup
- [`tests/test_wiki_mode.py`](../tests/test_wiki_mode.py) — hermetic test suite (15 assertions)
- [`docs/compound-vault-guide.md`](compound-vault-guide.md) — v1.7 omnibus that v1.8 builds on
- v1.7.0 audit §9 axis 6: [`docs/audits/v1.7.0-audit-2026-05-17.md`](audits/v1.7.0-audit-2026-05-17.md)


### install-guide.md

# claude-obsidian: Install Guide

**Claude + Obsidian Knowledge Companion**
Version 1.9.2 · public canonical: [github.com/AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) · community early-access mirror (Pro): [AI Marketing Hub org](https://github.com/AI-Marketing-Hub)

> ℹ️ The install commands below use the **public open-source** URLs (`AgriciDaniel/claude-obsidian`), recommended for everyone and requiring no membership. [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) members who want early access to in-development features can swap every `AgriciDaniel/claude-obsidian` for `AI-Marketing-Hub/claude-obsidian` and the plugin slug `claude-obsidian@agricidaniel-claude-obsidian` for `claude-obsidian@ai-marketing-hub-claude-obsidian`.

> **Optional: DragonScale Memory extension.** If you want flat extractive log folds, deterministic page addresses, semantic tiling lint, and boundary-first autoresearch topic selection, run `bash bin/setup-dragonscale.sh` after the base install. Extra prerequisites beyond the base: `flock` (standard on Linux; available via `util-linux` on macOS) and `python3` (for the tiling and boundary helpers). Optional: `ollama` with `nomic-embed-text` pulled if you want the semantic tiling lint (Mechanism 3 only; it no-ops gracefully when ollama or the model is unavailable). The boundary-first scorer (Mechanism 4) needs only `python3`, no ollama. See [`docs/dragonscale-guide.md`](./dragonscale-guide.md) for the user-facing guide, `wiki/concepts/DragonScale Memory.md` for the full spec, and `CHANGELOG.md` for what shipped in 1.6.0.

---

## What is claude-obsidian?

claude-obsidian is a Claude Code plugin + Obsidian vault that builds and maintains a persistent, compounding knowledge base. Every source you add gets processed into cross-referenced wiki pages. Every question you ask pulls from everything that has been read. Knowledge compounds like interest.

Built on Andrej Karpathy's LLM Wiki pattern.

---

## Prerequisites

| Tool | How to get it | Notes |
|------|--------------|-------|
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` | Free tier available |
| **Obsidian** | [obsidian.md](https://obsidian.md) | Free |
| **Git** | Pre-installed on most systems | For Option 1 |

---

## Installation

### Option 1: Clone as vault (recommended)

Full setup in under 2 minutes.

```bash
git clone https://github.com/AgriciDaniel/claude-obsidian
cd claude-obsidian
bash bin/setup-vault.sh
```

Then in Obsidian: **Manage Vaults → Open folder as vault → select `claude-obsidian/`**

Open Claude Code in the same folder and type `/wiki`.

### Option 2: Install as Claude Code plugin

Plugin installation in Claude Code is a two-step process. First add the marketplace catalog, then install the plugin from it.

```bash
# Step 1: add the marketplace
claude plugin marketplace add AgriciDaniel/claude-obsidian

# Step 2: install the plugin
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

Verify the install:
```bash
claude plugin list
```

In any Claude Code session: type `/wiki` and Claude walks you through vault setup.

### Option 3: Add to an existing vault

Copy `WIKI.md` from this repo into your vault root. Then paste into Claude:

```
Read WIKI.md in this project. Then:
1. Check if Obsidian is installed. If not, install it.
2. Check if the Local REST API plugin is running on port 27124.
3. Configure the MCP server.
4. Ask me ONE question: "What is this vault for?"
Then scaffold the full wiki structure.
```

---

## First Steps

### 1. Scaffold the vault

Type `/wiki` in Claude Code. Claude will:
- Detect your vault mode (website, GitHub, business, personal, research, or book/course)
- Create the folder structure and core wiki pages
- Set up `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`, and `wiki/overview.md`

### 2. Drop your first source

Put any document into `.raw/`:
- PDFs, markdown files, transcripts, articles, URLs

Tell Claude: `ingest [filename]`

Claude reads the source and creates 8–15 cross-referenced wiki pages.

### 3. Ask questions

```
what do you know about [topic]?
```

Claude reads the hot cache, scans the index, drills into relevant pages, and gives a synthesized answer, citing specific wiki pages, not training data.

---

## Commands Reference

| Command | What Claude does |
|---------|-----------------|
| `/wiki` | Setup check, scaffold, or continue where you left off |
| `ingest [file]` | Read source, create 8–15 wiki pages, update index and log |
| `ingest all of these` | Batch process multiple sources, then cross-reference |
| `what do you know about X?` | Read index → relevant pages → synthesize answer |
| `/save` | File the current conversation as a wiki note |
| `/save [name]` | Save with a specific title |
| `/autoresearch [topic]` | Autonomous research loop: search, fetch, synthesize, file |
| `/canvas` | Open or create a visual canvas |
| `/canvas add image [path]` | Add an image to the canvas |
| `/canvas add text [content]` | Add a markdown text card |
| `/canvas add pdf [path]` | Add a PDF document |
| `/canvas add note [page]` | Pin a wiki page as a linked card |
| `lint the wiki` | Health check: orphans, dead links, gaps |
| `update hot cache` | Refresh `hot.md` with latest context summary |

---

## Plugins (pre-installed)

Enable in **Settings → Community Plugins**:

| Plugin | Purpose |
|--------|---------|
| **Calendar** | Right-sidebar calendar with word count and task dots |
| **Thino** | Quick memo capture panel |
| **Excalidraw** | Freehand drawing, image annotation |
| **Banners** | Header images via `banner:` frontmatter |

Also install from Community Plugins:

| Plugin | Purpose |
|--------|---------|
| **Dataview** | Powers the dashboard queries |
| **Templater** | Auto-fills frontmatter from templates |
| **Obsidian Git** | Auto-commits vault every 15 minutes |

---

## CSS Snippets

Three snippets are auto-enabled by `setup-vault.sh`:

| Snippet | Effect |
|---------|--------|
| `vault-colors` | Color-codes wiki folders in the file explorer |
| `ITS-Dataview-Cards` | Turns Dataview queries into visual card grids |
| `ITS-Image-Adjustments` | Fine-grained image sizing; append `\|100` to embeds |

---

## Six Wiki Modes

| Mode | Use when |
|------|---------|
| **A: Website** | Sitemap, content audit, SEO wiki |
| **B: GitHub** | Codebase map, architecture wiki |
| **C: Business** | Project wiki, competitive intelligence |
| **D: Personal** | Second brain, goals, journal synthesis |
| **E: Research** | Papers, concepts, thesis |
| **F: Book/Course** | Chapter tracker, course notes |

Modes can be combined.

---

## MCP Setup (Optional)

MCP lets Claude read and write vault notes directly without copy-paste.

**Option A: REST API**

1. Install the **Local REST API** plugin in Obsidian
2. Copy your API key
3. Run:

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-obsidian"],
  "env": {
    "OBSIDIAN_API_KEY": "your-key",
    "OBSIDIAN_HOST": "127.0.0.1",
    "OBSIDIAN_PORT": "27124",
    "NODE_TLS_REJECT_UNAUTHORIZED": "0"
  }
}' --scope user
```

**Option B: Filesystem (no plugin needed)**

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@bitbonsai/mcpvault@latest", "/path/to/your/vault"]
}' --scope user
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `/wiki` says "not found" | Make sure `claude-obsidian` plugin is enabled: `claude plugin list` |
| Graph colors reset after closing Obsidian | Open Graph view → gear → Color groups → re-add once. Permanent after that. |
| Excalidraw not loading | Run `bash bin/setup-vault.sh` to download `main.js` (8MB, not in git) |
| Dashboard shows no results | Install the **Dataview** plugin from Community Plugins |
| Hot cache not loading at session start | Check hooks: `claude hooks list`; SessionStart hook should be present |

---

## Cross-Project Power Move

Point any Claude Code project at this vault. Add to that project's `CLAUDE.md`:

```markdown
## Wiki Knowledge Base
Path: ~/path/to/claude-obsidian

When you need context not in this project:
1. Read wiki/hot.md first (recent context cache)
2. If not enough, read wiki/index.md
3. If you need domain details, read the relevant wiki page

Do NOT read the wiki for general coding questions.
```

Your executive assistant, coding projects, and content workflows all draw from the same knowledge base.

---

## Support

- **GitHub (public canonical)**: [github.com/AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)
- **Issues**: [github.com/AgriciDaniel/claude-obsidian/issues](https://github.com/AgriciDaniel/claude-obsidian/issues)
- **Community early-access (Pro)**: [AI Marketing Hub org](https://github.com/AI-Marketing-Hub) · [Skool community](https://www.skool.com/ai-marketing-hub-pro)

---

*Built by [AgriciDaniel](https://github.com/AgriciDaniel) / AI Marketing Hub*
*Based on Andrej Karpathy's LLM Wiki pattern*



## Top-level structure
- `.claude-plugin/` (dir) — config/hidden
- `.cursor/` (dir) — config/hidden
- `.github/` (dir) — config/hidden
- `.gitignore` (file) — config/hidden
- `.obsidian/` (dir) — config/hidden
- `.raw/` (dir) — config/hidden
- `.vault-meta/` (dir) — config/hidden
- `.windsurf/` (dir) — config/hidden
- `AGENTS.md` (file) — agent instruction files
- `ATTRIBUTION.md` (file)
- `CHANGELOG.md` (file)
- `CITATION.cff` (file)
- `CLAUDE.md` (file) — agent instruction files
- `CODEOWNERS` (file)
- `CODE_OF_CONDUCT.md` (file)
- `CONTRIBUTING.md` (file)
- `GEMINI.md` (file) — agent instruction files
- `LICENSE` (file)
- `Makefile` (file)
- `PRIVACY.md` (file)
- `README.md` (file)
- `SECURITY.md` (file)
- `WIKI.md` (file) — agent instruction files
- `_templates/` (dir)
- `agents/` (dir) — core plugin/skill infrastructure
- `assets/` (dir)
- `bin/` (dir) — core plugin/skill infrastructure
- `commands/` (dir) — core plugin/skill infrastructure
- `docs/` (dir) — guides (compound vault, methodology modes, install, dragonscale)
- `hooks/` (dir) — core plugin/skill infrastructure
- `scripts/` (dir) — core plugin/skill infrastructure
- `skills/` (dir) — core plugin/skill infrastructure
- `tests/` (dir) — hermetic test suite (make test)
- `wiki/` (dir) — seeded vault wiki (concepts, entities, sources, meta)

### skills/ (15 skills)
autoresearch, canvas, defuddle, obsidian-bases, obsidian-markdown, save, think, wiki-cli, wiki-fold, wiki-ingest, wiki-lint, wiki-mode, wiki-query, wiki-retrieve, wiki

### Key scripts (bin/ and scripts/)
- `bin/setup-vault.sh` — one-time vault configuration (graph colors, app.json, CSS snippets)
- `bin/setup-mode.sh` — methodology mode selection (LYT/PARA/Zettelkasten/Generic)
- `bin/setup-retrieve.sh` — opt-in hybrid retrieval pipeline setup
- `bin/setup-dragonscale.sh` — optional DragonScale Memory extension
- `scripts/detect-transport.sh` — writes `.vault-meta/transport.json` (CLI/MCP/filesystem fallback chain)
- `scripts/wiki-lock.sh` — per-file advisory locking for multi-writer safety
- `scripts/contextual-prefix.py`, `scripts/bm25-index.py`, `scripts/retrieve.py`, `scripts/rerank.py` — wiki-retrieve pipeline
- `scripts/wiki-mode.py` — methodology-aware page routing

### Vault layout (wiki/)
- `wiki/index.md` — master catalog of every page
- `wiki/hot.md` — recent-context cache (~500 words, refreshed each session)
- `wiki/overview.md` — cross-source synthesis
- `wiki/log.md` — append-only ingest/refresh log
- `wiki/sources/`, `wiki/entities/`, `wiki/concepts/` — typed page folders
- `wiki/meta/` — dashboard (Bases + legacy Dataview), graph assets
