---
type: source
category: "Design & UI generation"
source_url: https://github.com/MengTo/Skills
tags:
  - agent-skills
  - web-design
  - threejs
  - gsap
  - illustration
  - game-dev
  - aura-build
  - prompt-assets
related:
  - emilkowalski-skills
  - ConardLi-garden-skills
  - elayadesign-ai-design-skills
  - skills.sh
  - leonxlnx-taste-skill
  - Owl-Listener-designer-skills
  - jakubkrehel-skills
  - codeswithroh-tastemaker
product: mengto-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

MengTo/Skills (7,059 stars, MIT) is Meng To's curated library of portable Agent Skills for designers and builders using Codex, Claude, Cursor, Aura Build, Lovable, and related stacks. The collection emphasizes prompts-as-assets and reference-driven workflows: video/HTML capture → super prompts, Awwwards-quality web design, GSAP/Three.js, 14 SVG illustration styles, Diablo-like combat VFX, playable browser games, and agent-loop workflow skills — organized under `agent-skills/` by category rather than a flat skills list.

_All claims below are sourced from ../../raw/github/MengTo-Skills.md unless otherwise noted._

## What it does

Flagship Codex/web workflows include **Video to Super Prompt**, **HTML to Interaction Prompts**, **Stitched Full Page Capture**, and **Daily UI Inspiration** (browse → capture → study → prompt packs). Broader categories under `agent-skills/`:

- **`web-design/`** — landing page, pricing page, Awwwards-quality sites, GSAP, Three.js, shader cursor trails, and related playbooks.
- **`ui/`** — design-first UI prompting (with ARTICLE/REFERENCES).
- **`3d/`** — ultra-realistic water, underwater god rays, virtual tours, sky rays/backgrounds, falling leaves, four seasons, high-res textures/models, Retina rendering.
- **`illustration/`** — 14 hand-written SVG styles (flat, outlined cartoon, halftone, one-line, isometric, vintage emblem, etc.) with palettes, drawing kits, and render/lint loops.
- **`game-combat/`** / **`game-development/`** — combat animation polish, elemental skill VFX, isometric ARPG, enemy/monster systems, playable web-game testing.
- **`media/`** — Aura and Unsplash asset-image skills.
- **`codex/`** / **`workflow/`** — capture/inspiration loops and reusable agent operating procedures.

Philosophy: store good prompts as versioned files; prefer specs and references over vibes; treat skills as operating procedures with defaults and pitfalls.

## Installation

Skills are plain Markdown folders — load the relevant `SKILL.md` in Codex, Claude Code, Cursor rules/chat, or other agents. Repo behavior notes live in `CLAUDE.md`. Browse runnable demos via `DEMOS.md` / `SCREENSHOTS.md`. There is no single `npx skills add` one-liner called out as the primary path in the README; usage is "open the narrowest matching skill first, then follow its steps."

## Key features

- **Reference → prompt pipelines** — screen recordings and full-page captures become detailed, reusable prompts for HTML/Aura/Fable-style one-shots.
- **Large categorized library** — web design, 3D, illustration, game combat/dev, media, UI prompting, workflow.
- **Demos and screenshots** — `DEMOS.md` / `SCREENSHOTS` for runnable recreation prompts.
- **Portable by default** — each skill meant to work across users/repos unless project context is supplied locally.

## Architecture

```txt
agent-skills/
  3d/  codex/  game-combat/  game-development/
  illustration/  media/  ui/  web-design/  workflow/
```

Each skill is typically `agent-skills/<category>/<skill-name>/SKILL.md` with optional references, articles, scripts, demos, and assets. Supporting top-level files: `CLAUDE.md`, `DEMOS.md`, `SCREENSHOTS*`, `scripts/`, `assets/`.

## Example usage

Open `agent-skills/codex/video-to-superprompt/SKILL.md` (or a web-design landing-page skill) in the agent host, then supply a recording or reference and follow the skill's steps to produce a super prompt or implementation.

## Maintenance status

7,059 GitHub stars, 825 forks, MIT licensed, default branch `main`, most recent push 2026-10-25, no tagged releases. Primary language HTML (demos/assets). Actively expanded categorized library with screenshot/demo surface.
