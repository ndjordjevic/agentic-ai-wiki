---
type: source
category: "Design & UI generation"
source_url: https://github.com/jakubkrehel/skills
tags:
  - agent-skills
  - interface-design
  - accessibility
  - typography
  - color-systems
  - ui-review
  - claude-code-plugin
  - skills-sh
related:
  - emilkowalski-skills
  - skills.sh
  - leonxlnx-taste-skill
  - Owl-Listener-designer-skills
  - elayadesign-ai-design-skills
  - codeswithroh-tastemaker
  - ConardLi-garden-skills
  - MengTo-Skills
  - ibelick-ui-skills
product: skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

jakubkrehel/skills (8,750 stars, MIT) is Jakub Krehel's Agent Skills pack for building and reviewing interfaces — accessibility, layout, writing, typography, color, and UI polish — drawn from his writing on jakub.kr and the Interfaces magazine (interfaces.dev). Installable via `npx skills` / [[skills.sh]] and as a Claude Code plugin (`interfaces@interfaces`), it pairs broad review skills (`better-interface`, `interface-review`) with focused craft skills and user-invoked exploration tools (break, variant, state-machine, teardown).

_All claims below are sourced from ../../raw/github/jakubkrehel-skills.md unless otherwise noted._

## What it does

Fourteen skills under `skills/`:

- **Review / improve** — `better-interface` (ranked multi-axis report), `better-ui`, `better-typography`, `better-colors`, `better-accessibility` (WCAG 2.2), `better-layout`, `better-writing`, `interface-review` (branch/PR/uncommitted UI regressions; user-invoked).
- **Build / explore** — `build-design` (Figma or design image → UI using project tokens), `explain-interface` (URL or screenshot teardown; user-invoked), `break` (worst-case scenarios on a temporary page), `state-machine` (every component state with switcher), `variant` (multiple variants to iterate), `teardown` (technical illustration → SVG/PNG/PDF).

## Installation

```bash
npx skills add jakubkrehel/skills

# Claude Code plugin
/plugin marketplace add jakubkrehel/skills
/plugin install interfaces@interfaces
```

Also listed on skills.sh (`skills.sh/jakubkrehel/skills`). Repo includes `AGENTS.md`, `CLAUDE.md`, `.claude-plugin/`, and `opencode.json`.

## Key features

- **Multi-axis interface review** — one ranked report across a11y, layout, writing, type, color, and polish.
- **WCAG 2.2 accessibility skill** — keyboard/focus, ARIA, names, forms, announcements, motion, zoom.
- **Change-scoped review** — `interface-review` targets what a branch/PR actually introduced.
- **Exploration utilities** — break / variant / state-machine for stress-testing and picking directions.
- **Design-to-code** — `build-design` from Figma or image against existing tokens/components.

## Architecture

Self-contained skill folders under `skills/`, plus agent instruction files and Claude plugin marketplace packaging for the `interfaces` plugin. Homepage: https://jakub.kr/skills.

## Example usage

```bash
npx skills add jakubkrehel/skills
# ask: "run better-interface on this screen" or "interface-review on my uncommitted changes"
```

## Maintenance status

8,750 GitHub stars, 332 forks, MIT licensed, default branch `main`, most recent push 2026-10-25, no tagged releases. Primary language Markdown. Active skills.sh-listed pack with Claude plugin install path.
