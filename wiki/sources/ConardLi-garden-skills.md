---
type: source
category: "Design & UI generation"
source_url: https://github.com/ConardLi/garden-skills
tags:
  - agent-skills
  - web-design
  - motion-showreel
  - image-generation
  - knowledge-retrieval
  - presentation
  - skills-sh
  - claude-code-plugin
related:
  - emilkowalski-skills
  - skills.sh
  - leonxlnx-taste-skill
  - elayadesign-ai-design-skills
  - codeswithroh-tastemaker
  - MengTo-Skills
  - jakubkrehel-skills
  - Owl-Listener-designer-skills
product: garden-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

Garden Skills (13,323 stars, MIT) is ConardLi's curated Agent Skills collection for Claude Code, Cursor, Codex, and other coding agents — six production-oriented skills spanning code-rendered motion showreels, record-ready web video presentations, anti-cliché web design engineering, GPT Image 2 prompting, beautiful article layout, and local knowledge-base retrieval. Installable via `npx skills`, Claude Code marketplace plugins, release zips, or manual copy, with bilingual docs and pinned skill downloads.

_All claims below are sourced from ../../raw/github/ConardLi-garden-skills.md unless otherwise noted._

## What it does

Six skills live under `skills/`:

- **`motion-showreel`** — deterministic `render(t)` short films / showreels (typically 5–60s, chapters up to 20 min) with shared audio/picture timeline, 43-style library, technical acceptance gates separate from taste; ships MP4 plus editable source; tagged release `motion-showreel v0.1.0`.
- **`web-video-presentation`** — Vite + React + TypeScript 1920×1080 click-driven presentations for cinematic screen recording; 23 themes; pluggable TTS (MiniMax, OpenAI, and contracts for others).
- **`web-design-engineer`** — design-engineer workflow with five-dial Design Read, redesign modes, anti-cliché blocklist, Design Direction Advisor (six schools) + 25 anchored style recipes (Linear, Aesop, Bloomberg, Stripe Press, etc.).
- **`gpt-image-2`** — image generation / prompting skill.
- **`beautiful-article`** — turn arbitrary sources into polished articles.
- **`kb-retriever`** — local knowledge retrieval skill.

## Installation

```bash
npx skills add ConardLi/garden-skills
npx skills add ConardLi/garden-skills -s web-design-engineer
npx skills add ConardLi/garden-skills -s gpt-image-2 --global

# Claude Code marketplace
/plugin marketplace add ConardLi/garden-skills
/plugin install web-design-skills@garden-skills
/plugin install motion-showreel-skills@garden-skills
# ... presentation-skills, knowledge-base-skills, image-generation-skills, beautiful-article-skills
```

Also supports pinned `.zip` downloads from GitHub Releases, manual copy into a project, and git submodule.

## Key features

- **Multi-skill gallery** — motion, presentation, design, image gen, article, and KB retrieval under one marketplace.
- **Deterministic motion pipeline** — `motion-showreel` treats picture and sound as one timeline with technical PASS/FAIL acceptance.
- **Style recipe libraries** — 25 web-design recipes and 23 presentation themes with concrete palettes and anti-patterns.
- **Agent-agnostic install paths** — skills CLI tags, Claude plugins, release zips, manual copy.
- **i18n docs** — English, Chinese (`README.zh-CN.md`), Japanese (`README.ja-JP.md`).

## Architecture

`skills/<name>/` folders with `SKILL.md` (and per-skill README/showcase assets under `dist/`), plus website/demo trees for some skills, Claude plugin marketplace metadata, and release artifacts per skill version. Spec badge points at agentskills.io / SKILL.md format.

## Example usage

```bash
npx skills add ConardLi/garden-skills -s web-design-engineer -a claude-code
# then ask for a landing page or redesign with the skill loaded
```

## Maintenance status

13,323 GitHub stars, 1,575 forks, MIT licensed, default branch `main`, most recent push 2026-10-25. Latest release listed: `motion-showreel v0.1.0` (2026-10-11). Primary language JavaScript. Actively maintained with per-skill versioned zip downloads.
