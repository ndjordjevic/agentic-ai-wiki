---
type: source
category: "Design & UI generation"
source_url: https://www.usehallmark.com/
companion_urls:
  - https://github.com/Nutlope/hallmark
raw_files:
  - ../../raw/web/usehallmark.com.md
  - ../../raw/github/Nutlope-hallmark.md
tags:
  - anti-ai-slop
  - design-skill
  - hallmark
  - theme-catalog
  - sloplint
  - agent-skills
  - coding-agents
related:
  - Nutlope-hallmark
  - Nutlope-inspo
  - Nutlope-variate
  - leonxlnx-taste-skill
  - open-design.ai
  - ui-skills.com
  - dmmulroy-anti-slop
product: usehallmark.com
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Hallmark (usehallmark.com) is the product site for Together AI's design skill that targets AI-generated UI slop — install with one line (`npx skills add nutlope/hallmark -g`) into Claude Code, Codex, or OpenCode, then build or redesign pages that pass Hallmark's own browser linter. The site markets **50 themes** and a before/after demo (Opus alone vs Hallmark). Companion open-source repo: [[Nutlope-hallmark]]. (../../raw/github/Nutlope-hallmark.md)

_All claims below are sourced from ../../raw/web/usehallmark.com.md unless otherwise noted._

## What it does

Hallmark sits between a one-line brief and shipped HTML: it asks for real material (photos, numbers, screenshots), deals themes that fit the prompt (or a custom branch), lays out a unique page structure, then runs `sloplint` in a real browser and a fresh-eyes review. The marketing site frames the product as "design taste for coding agents" and shows side-by-side issue counts from Hallmark's linter (Without vs With).

## Key features

- **One-line install** — `npx skills add nutlope/hallmark -g` (or `--agent claude-code|codex|opencode`).
- **Build / redesign verbs** — `/hallmark …` builds; `/hallmark redesign ./site` keeps content/links/forms and rebuilds look (Claude Code); Codex uses `$hallmark`.
- **Fifty themes** — editorial, modern minimal, atmospheric, playful categories (Refract, Cobalt, Furrow, Midnight, Riso, …).
- **Self-check** — browser linter catches tracked capitals, low-contrast text on photos, adjacent filled buttons, photo-vs-gradient mistakes.
- **Optional design system** — reads tokens / `design.md` before designing; can screenshot a live app URL or folder.
- **Open photo library** — Wikimedia Commons images, credited; no API key required (image key optional).

## Architecture

Public marketing site on Vercel (404 responses show `fra1` edge). Skill packages land in `~/.claude/skills/hallmark` or `~/.agents/skills/hallmark` depending on agent. Deep mechanism (macrostructures, slop-test gates, theme machinery) lives in the GitHub skill repo. (../../raw/github/Nutlope-hallmark.md)

## Installation

```bash
npx skills add nutlope/hallmark -g
# agent-scoped examples from the site:
npx skills add nutlope/hallmark -g --agent claude-code
npx skills add nutlope/hallmark -g --agent codex
npx skills add nutlope/hallmark -g --agent opencode
```

## Example usage

```text
/hallmark a site for Five Mile Gin, a small distillery that forages its botanicals
/hallmark redesign ./site
```

Codex: `$hallmark` / `$hallmark redesign`. OpenCode discovers the installed skill copies automatically.

## When to use

Use Hallmark when coding agents keep emitting generic hero → features → CTA pages and you want structural variety plus automated slop checks. Prefer [[Nutlope-inspo]] when the need is live production-site references over MCP, or [[open-design.ai]] for a full local design studio.

## Maintenance status

Site live as of 2026-10-28; companion [[Nutlope-hallmark]] is the starred open-source skill (Together AI). Theme count on the site (50) may exceed older README figures — treat the site as the marketing surface of truth for current theme marketing. (../../raw/github/Nutlope-hallmark.md)

## Ecosystem

Same Nutlope/Together design line as [[Nutlope-inspo]] and [[Nutlope-variate]]; overlaps anti-slop / taste skills ([[leonxlnx-taste-skill]], [[dmmulroy-anti-slop]]) and DESIGN.md workflows ([[open-design.ai]], [[ui-skills.com]]).
