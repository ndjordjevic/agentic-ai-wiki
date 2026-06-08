---
type: source
source_url: https://github.com/anthropics/skills
tags:
  - agent-skills
  - skill-creator
  - claude-skills
  - mcp-builder
  - document-processing
  - skill-ecosystem
  - anthropic
  - plugin-marketplace
related:
  - skills.sh
  - shareai-lab-learn-claude-code
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - github-spec-kit
  - forrestchang-andrej-karpathy-skills
  - anombyte93-prd-taskmaster
  - nidhinjs-prompt-master
  - anthropic.com
  - anthropic.com-messages
  - obra-superpowers
  - browse.sh
  - bmad-code-org-bmad-method
  - buildermethods-agent-os
  - othmanadi-planning-with-files
  - openai-codex-plugin-cc
  - garrytan-gstack
  - voltagent-awesome-agent-skills
product: skills
detail_level: standard
created: 2026-05-11
updated: 2026-06-08
---

Anthropic's official `skills` repository is the canonical reference implementation of the Agent Skills pattern for Claude — a collection of 17 self-contained SKILL.md-based modules spanning document processing, creative design, developer tooling, enterprise communications, and a meta skill-creator that teaches Claude to build and evaluate new skills. With 132,000+ stars, it is the highest-starred skills repository in the ecosystem and serves as the primary example library for anyone learning to write skills for Claude Code, Claude.ai, or the Claude API.

_All claims below are sourced from ../../raw/github/anthropics-skills.md unless otherwise noted._

## What it does

The repository ships two distinct tiers of skills. The first tier — **document skills** (`xlsx`, `docx`, `pptx`, `pdf`) — are the production skills that power Claude's native document capabilities in Claude.ai; they are source-available (not open source) but published so developers can study complex, production-grade skill patterns. The second tier — **example skills** — are Apache 2.0-licensed demonstrations covering algorithmic art, brand guidelines, canvas design, frontend design, internal communications, MCP server generation, skill creation and evaluation, Slack GIF creation, theme generation, web artifact building, and web application testing.

## Skills

| Skill | Bundle | License | Description |
|---|---|---|---|
| `algorithmic-art` | example | Apache 2.0 | Create generative art using p5.js with seeded randomness, flow fields, and particle systems. |
| `brand-guidelines` | example | Apache 2.0 | Apply Anthropic's brand colors and typography to any artifact for consistent visual styling. |
| `canvas-design` | example | Apache 2.0 | Design static visual art (posters, artwork) and export as .png or .pdf. |
| `claude-api` | claude-api | Apache 2.0 | Build, debug, and optimize Claude API / Anthropic SDK apps; handles model migrations and prompt caching. |
| `doc-coauthoring` | example | Apache 2.0 | Structured co-authoring workflow for documentation, proposals, and technical specs. |
| `docx` | document | source-available | Create, read, edit, and manipulate Word (.docx) files with full formatting (headings, tables, TOC, letterheads). |
| `frontend-design` | example | Apache 2.0 | Build production-grade, distinctively styled frontends (React, HTML/CSS, landing pages, dashboards). |
| `internal-comms` | example | Apache 2.0 | Write internal communications (status reports, newsletters, incident reports) in company format. |
| `mcp-builder` | example | Apache 2.0 | Guide for building high-quality MCP servers in Python (FastMCP) or TypeScript (MCP SDK). |
| `pdf` | document | source-available | Full PDF operations: create, read, split, merge, fill forms, OCR, encrypt, and extract images. |
| `pptx` | document | source-available | Create, read, edit, and convert PowerPoint (.pptx) presentations and slide decks. |
| `skill-creator` | example | Apache 2.0 | Meta-skill for creating, evaluating, and iterating on new skills, with eval tooling and a description optimizer. |
| `slack-gif-creator` | example | Apache 2.0 | Generate Slack-optimized animated GIFs with proper size constraints and validation. |
| `theme-factory` | example | Apache 2.0 | Apply 10 pre-set or on-the-fly themes (colors/fonts) to any artifact — slides, docs, HTML pages. |
| `web-artifacts-builder` | example | Apache 2.0 | Build complex multi-component HTML artifacts using React, Tailwind CSS, and shadcn/ui. |
| `webapp-testing` | example | Apache 2.0 | Test local web apps with Playwright: verify UI, capture screenshots, view browser logs. |
| `xlsx` | document | source-available | Create, read, edit, and convert spreadsheets (.xlsx, .csv, .tsv) with formula, chart, and data-cleaning support. |

## Key features

- **Self-contained skill format** — every skill is a folder containing a `SKILL.md` with YAML frontmatter (`name:`, `description:`) and freeform markdown instructions; no build step or runtime dependency required beyond the agent that loads it.
- **Plugin marketplace integration** — `.claude-plugin/marketplace.json` groups skills into named plugin bundles (`document-skills`, `example-skills`, `claude-api`) installable in Claude Code via `/plugin install <name>@anthropic-agent-skills`.
- **skill-creator meta-skill** — a fully featured skill for building, evaluating, and iterating on other skills, complete with `eval-viewer/generate_review.py`, `agents/` subagents, benchmark scripts, and a description optimizer for improving trigger accuracy.
- **mcp-builder skill** — a skill for generating MCP (Model Context Protocol) server scaffolding, bridging the skills and MCP ecosystems.
- **Template and spec** — `template/SKILL.md` provides the minimal two-field starting point; `spec/` links to the canonical Agent Skills specification at agentskills.io/specification.
- **Multi-surface availability** — skills are usable in Claude Code (plugin install), Claude.ai (paid plans, custom skill upload), and the Claude API (Skills API).

## Architecture

Skills follow the SKILL.md file format: a YAML frontmatter block with `name` and `description`, followed by markdown instructions the agent executes at load time. The repository structures skills as individual subdirectories under `skills/`, each optionally containing supporting assets, scripts, agents, or references — the `skill-creator` skill being the most complex example with five subdirectories and evaluation tooling.

The Claude Code plugin system uses `.claude-plugin/marketplace.json` to declare named plugin bundles that map to skill subdirectory paths. The command `/plugin marketplace add anthropics/skills` registers the repo, after which individual bundles are installed with `/plugin install <bundle>@anthropic-agent-skills`. This registry pattern is compatible with the `npx skills` CLI from the `vercel-labs/skills` infrastructure (the distribution layer covered in [[skills.sh]]).

## Installation

**Claude Code (plugin marketplace):**
```bash
# Register the marketplace
/plugin marketplace add anthropics/skills

# Install document skills (xlsx, docx, pptx, pdf)
/plugin install document-skills@anthropic-agent-skills

# Install example skills (art, design, comms, testing, mcp-builder, skill-creator, etc.)
/plugin install example-skills@anthropic-agent-skills
```

**Via npx skills CLI:**
```bash
npx skills add anthropics/skills
npx skills add anthropics/skills --skill skill-creator
```

**Claude.ai:** example skills are pre-loaded for paid plan users; custom skills can be uploaded via the Claude.ai interface.

**Claude API:** use the Skills API Quickstart at docs.claude.com to attach skills to API requests.

## Example usage

Once `example-skills` is installed, simply mention the skill in a prompt:

```
Use the PDF skill to extract the form fields from path/to/some-file.pdf
```

For the skill-creator skill:
```
Use the skill-creator to build a new skill that formats release notes from a git log
```

A minimal custom SKILL.md:
```markdown
---
name: release-notes
description: Format git log output into structured release notes with sections for features, fixes, and breaking changes.
---

# Release Notes Formatter
Given a git log, produce a structured release notes document...
```

## When to use

Use this repository when you need production-quality SKILL.md examples to study or fork, when you want to extend Claude Code with Anthropic's official document-processing capabilities, or when you are building new skills and want to use the `skill-creator` skill to generate, evaluate, and iterate on them. It is the authoritative starting point for anyone building on the Agent Skills standard — consult this alongside [[skills.sh]] for the broader ecosystem of community-published skills.

## Maintenance status

132,032 stars, 15,545 forks, Python primary language, last pushed 2026-05-09. No versioned releases — updates ship directly to the `main` branch. No top-level open-source license; individual skills carry Apache 2.0 (example skills) or source-available terms (document skills) per `THIRD_PARTY_NOTICES.md`. Actively maintained by Anthropic; the repo is referenced in official Claude documentation and the Anthropic engineering blog.

## Ecosystem

The repository sits at the intersection of two ecosystems: the Agent Skills standard (agentskills.io) and the Claude platform (Claude Code, Claude.ai, Claude API). It is cross-listed in the official skills registry at [[skills.sh]], which shows `anthropics/skills` as an official publisher with 289 skills indexed. The `mcp-builder` skill connects to the Model Context Protocol ecosystem. The `skill-creator` pattern — capturing a workflow as a SKILL.md with supporting evaluation tooling — is the same on-demand loading pattern described in session 5 of [[shareai-lab-learn-claude-code]].
