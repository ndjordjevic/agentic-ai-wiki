---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/dembrandt/dembrandt-skills
tags:
  - agent-skills
  - ux-review
  - design-system
  - claude-code-plugin
  - enterprise-ux
  - dembrandt
  - skills-sh
related:
  - dembrandt-dembrandt
  - skills.sh
  - AThevon-genjutsu
  - leonxlnx-taste-skill
  - Nutlope-hallmark
  - anthropics-skills
  - ParthJadhav-app-store-screenshots
product: dembrandt
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

dembrandt-skills (~173★, MIT) packages senior-level UX and design-system judgment as Open Agent Skills (and a Claude Code plugin) so agents apply usability/contrast/pattern guidance automatically — most skills work install-only; two that read live sites need the [[dembrandt-dembrandt]] engine + browser.

_All claims below are sourced from ../../raw/github/dembrandt-dembrandt-skills.md unless otherwise noted._

## What it does

Install ~45 skills that load on demand when you ask for UX review, component choices, accessibility contrast, etc. Claude Code plugin path also registers the dembrandt MCP server.

## Installation

```bash
npx skills add dembrandt/dembrandt-skills --all
# Claude Code:
# /plugin marketplace add dembrandt/dembrandt-skills
# /plugin install dembrandt@dembrandt
```

Run `npx dembrandt install-browser` once before live-site skills.

## Key features

- Enterprise UX heuristics packaged as Agent Skills
- On-demand loading (`--all` is cheap); `--global` option
- Claude Code marketplace plugin + MCP registration
- Two skills depend on the Dembrandt extraction engine

## Architecture

Skills-only repo consuming the separate dembrandt CLI/MCP engine for live scans. Compatible with Claude Code, Cursor, Codex, Copilot, and other Open Agent Skills hosts.

## Example usage

Ask "Review this interface for usability issues" — matching skill loads and runs the review pipeline.

## Maintenance status

~173 stars, 22 forks, MIT, `main`, homepage https://www.dembrandt.com/skills, listed on skills.sh.
