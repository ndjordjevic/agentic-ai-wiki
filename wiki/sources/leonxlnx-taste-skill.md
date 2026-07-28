---
type: source
category: "Design & UI generation"
source_url: https://github.com/Leonxlnx/taste-skill
tags:
  - agent-skill
  - anti-slop
  - frontend-design
  - gsap-motion
  - design-dials
  - image-generation
  - design-md
  - skill-family
related:
  - stitch.withgoogle.com
  - voltagent-awesome-design-md
  - open-design.ai
  - oso95-scroll-world
  - skills.sh
  - Nutlope-hallmark
product: taste-skill
detail_level: standard
created: 2026-07-14
updated: 2026-07-28
---

Taste Skill (63,152 stars, MIT) is a family of thirteen portable Agent Skills — ten implementation skills that output frontend code and three image-generation skills that output design reference boards — aimed at a specific, named failure mode: AI-built interfaces that default to generic, "boilerplate-looking" layouts. Rather than one skill, it's a menu of stylistic variants (soft, minimalist, brutalist, Stitch-compatible) plus workflow skills (redesign audit, image-to-code, full-output enforcement), with the flagship `taste-skill` (v2, install name `design-taste-frontend`) exposing three 1-10 tunable dials — layout variance, motion intensity, visual density — instead of a single fixed aesthetic.

_All claims below are sourced from ../../raw/github/leonxlnx-taste-skill.md unless otherwise noted._

## What it does

Each skill targets one job. The default `taste-skill` (v2, experimental, install name `design-taste-frontend`) reads the design brief, infers the design language, and tunes three dials — DESIGN_VARIANCE (centered/clean vs. asymmetric/modern), MOTION_INTENSITY (hover vs. scroll/magnetic), VISUAL_DENSITY (spacious vs. dense dashboard) — while enforcing a design-system map, a hard em-dash ban, canonical GSAP animation code skeletons, and a strict pre-flight check. Variant skills narrow to a fixed aesthetic once a direction is chosen: `soft-skill` (calm, premium, spring motion), `minimalist-skill` (Notion/Linear-style editorial UI), `brutalist-skill` (Swiss type, sharp contrast, experimental layout), and `stitch-skill` (Google Stitch-compatible rules including optional `DESIGN.md` export). Workflow skills cover adjacent needs: `gpt-tasteskill` (a stricter GPT/Codex-oriented variant with higher layout variance and stronger GSAP direction), `redesign-skill` (audits an existing UI before fixing layout/spacing/hierarchy/styling), `image-to-code-skill` (generate reference images → analyze → implement, an explicit three-step pipeline), and `output-skill` (forces complete output with no placeholder comments, for agents that truncate). Three separate image-generation skills — `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit` — produce comps, mobile flows, or brand-identity boards only (no code), meant to be generated first (e.g. with ChatGPT Images) then handed to a coding agent for implementation.

## Installation

The `npx skills add` CLI (vercel-labs/agent-skills) scans the repo's `skills/` folder, so both code and image-generation skills install the same way:
```bash
npx skills add https://github.com/Leonxlnx/taste-skill                                    # everything
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"    # one skill by install name
```
The `--skill` value is the `name:` field inside each `SKILL.md`'s frontmatter, not the folder name (e.g. folder `taste-skill` installs as `design-taste-frontend`). Any `SKILL.md` can also be copied directly into a project or pasted into a ChatGPT/Codex conversation. Upgrading from v1 to v2 is a re-run of the same install command with the same install name (`design-taste-frontend`), replacing the SKILL.md in place; projects that depend on exact v1 behavior can pin explicitly with `--skill "design-taste-frontend-v1"`. (../../raw/github/leonxlnx-taste-skill.md)

## Key features

- **Tunable dials on the default skill** — DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY, each a 1-10 knob set as numbers at the top of the skill file, letting one skill span a spectrum of outputs rather than encoding one fixed look.
- **Anti-slop enforcement mechanics** — canonical GSAP code skeletons, a hard em-dash ban, and a strict pre-flight check are called out specifically as the mechanisms that push output away from generic AI-frontend patterns.
- **Redesign-audit protocol** — `redesign-skill` explicitly separates "audit the existing UI" from "fix it," rather than jumping straight to changes on an established codebase.
- **Image-first pipeline as a first-class workflow** — `image-to-code-skill` and the three imagegen skills formalize "generate references, then implement" as a distinct path from "generate code directly," with an explicit prompt convention (`follow the skill: generate images, then analyze, then code`).
- **Stitch interoperability** — `stitch-skill` targets rule-compatibility with Google Stitch, including an optional `DESIGN.md` export, the same token format distributed at scale by [[voltagent-awesome-design-md]] and [[open-design.ai]].
- **Framework-agnostic by design** — rules target design intent (layout, typography, motion, spacing) rather than a specific framework's API, so the same skill applies across React, Vue, Svelte, and other stacks.

## Architecture

The repo is organized as thirteen independent skill folders under `skills/`, each self-contained and separately installable — `taste-skill/`, `taste-skill-v1/`, `gpt-tasteskill/`, `image-to-code-skill/`, `redesign-skill/`, `soft-skill/`, `output-skill/`, `minimalist-skill/`, `brutalist-skill/`, `stitch-skill/`, `imagegen-frontend-web/`, `imagegen-frontend-mobile/`, `brandkit/` — plus a `skills/llms.txt` catalog. A `.claude-plugin/` manifest handles Claude Code marketplace distribution, but the primary distribution path is the cross-host `npx skills add` CLI, which discovers every skill folder the same way regardless of host (Codex, Cursor, Claude Code, or manual copy-paste). `research/` holds the background writing that shaped the skill rules, and `CHANGELOG.md` documents the full v1→v2 rationale for the default skill. (../../raw/github/leonxlnx-taste-skill.md)

## Example usage

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
# then, in a prompt to the coding agent:
# "follow the skill: generate images, then analyze, then code"
```
For a fixed aesthetic once a direction is chosen: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "industrial-brutalist-ui"` or `--skill "high-end-visual-design"`. (../../raw/github/leonxlnx-taste-skill.md)

## Maintenance status

63,152 GitHub stars, 4,462 forks, MIT licensed, default branch `main`, most recent push 2026-07-04, no tagged releases. Sponsored by animations.dev (Emil Kowalski) and the Vercel Open Source Program. Active default-skill iteration is explicitly ongoing — the README labels v2 "experimental" and states it is "actively iterating toward v2.0.0 stable." (../../raw/github/leonxlnx-taste-skill.md)

## Ecosystem

Sits in the same DESIGN.md/design-token distribution space as [[voltagent-awesome-design-md]] and [[open-design.ai]] via `stitch-skill`'s Stitch-compatible export, and shares [[stitch.withgoogle.com]]'s underlying premise that AI-generated UI needs an explicit taste layer on top of raw generation. Distinguished from [[oso95-scroll-world]] (which generates a specific artifact — scroll-scrubbed landing video) by being a general-purpose frontend-quality overlay applicable to any UI-generation task, and installable the same multi-host way as other [[skills.sh]]-distributed skill families.
