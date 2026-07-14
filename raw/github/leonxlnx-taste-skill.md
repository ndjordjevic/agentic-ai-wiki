# Leonxlnx/taste-skill

## Metadata
- Stars: 63152
- Primary language: JavaScript
- Default branch: main
- Latest release: (none)
- License: MIT License
- Homepage: https://tasteskill.dev
- Fetched: 2026-07-14
- Final URL: https://github.com/Leonxlnx/taste-skill

## Description
Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop

## README

# Taste Skill

*The Anti-Slop Frontend Framework for AI Agents*

Portable **Agent Skills** that upgrade AI-built interfaces: stronger layout, typography, motion, and spacing instead of boilerplate-looking UIs. This repo also includes **image-generation skills** for reference boards (web, mobile, brand kits). Pair them with **ChatGPT Images** or similar generators, then hand the frames to Codex, Cursor, or Claude Code for implementation.

MIT License · Agent Skills compatible (vercel-labs/agent-skills) · Works with Codex, Cursor, Claude.

### Disclaimer

Taste Skill has no official token, coin, or crypto project. Any token using the author's name, image, or project is unaffiliated and not endorsed.

### Installing

The `npx skills add` CLI (vercel-labs/agent-skills) scans the `skills/` folder in this repo, so all skills below (code and image-generation) install the same way.

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

Install a single skill by its **install name** (the `name:` field inside the SKILL frontmatter, not the folder name):

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Any `SKILL.md` can also be copied into a project or pasted into ChatGPT / Codex conversations.

**Updating from v1:** the default `taste-skill` (install name `design-taste-frontend`) is now **v2 (experimental)**, a substantial rewrite of the original v1 — re-running the install command upgrades in place (install name unchanged). Projects depending on exact v1 behavior can pin to `design-taste-frontend-v1`. Full v1→v2 diff and rationale in `CHANGELOG.md`.

### Skills

Each skill does one job — implementation skills output code, image-generation skills output reference images only.

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **taste-skill** | `design-taste-frontend` | 🆕 v2 (experimental) — substantial rewrite of the default skill. Reads the brief, infers the design language, tunes three dials (VARIANCE / MOTION / DENSITY). Brief inference, design-system map, hard em-dash ban, canonical GSAP code skeletons, redesign-audit protocol, strict pre-flight check. |
| **taste-skill-v1** | `design-taste-frontend-v1` | The original v1, preserved for projects depending on its exact behavior. |
| **gpt-tasteskill** | `gpt-taste` | Stricter variant for GPT/Codex: higher layout variance, stronger GSAP direction, aggressive anti-slop. |
| **image-to-code-skill** | `image-to-code` | Image-first pipeline: generate site references, analyze them, then implement the frontend to match. |
| **redesign-skill** | `redesign-existing-projects` | Existing projects: audit the UI first, then fix layout, spacing, hierarchy, styling. |
| **soft-skill** | `high-end-visual-design` | Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion. |
| **output-skill** | `full-output-enforcement` | When the model ships half-finished work: full output, no placeholder comments. |
| **minimalist-skill** | `minimalist-ui` | Editorial product UI (Notion/Linear vibes), restrained palette, crisp structure. |
| **brutalist-skill** | `industrial-brutalist-ui` | Hard mechanical language: Swiss type, sharp contrast, experimental layout. |
| **stitch-skill** | `stitch-design-taste` | Google Stitch-compatible rules, including optional `DESIGN.md` export format. |

**Image generation skills** (produce design images only, no code — use with ChatGPT Images, Codex image mode, or any agent that generates images):

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **imagegen-frontend-web** | `imagegen-frontend-web` | Website comps: hero, landing, multi-section with strong typography, spacing, anti-slop art direction. |
| **imagegen-frontend-mobile** | `imagegen-frontend-mobile` | Mobile screens and flows: iOS/Android/cross-platform, mockups, readable type, coherent sets. |
| **brandkit** | `brandkit` | Brand-kit boards: logo directions, palettes, type, identity applications across categories. |

**Which one should I use?** Start with **taste-skill** as the safest general default. Pin to **taste-skill-v1** if depending on exact prior behavior. Use **gpt-taste** for stricter GPT/Codex-oriented rules. Use **image-to-code-skill** for image → analyze → code workflows. Use **redesign-skill** to improve an existing codebase instead of greenfield styling. Add **soft-skill**, **minimalist-skill**, or **brutalist-skill** once the visual direction is chosen. Add **output-skill** if the agent keeps truncating output. Use the imagegen skills when the deliverable is images (comps, flows, identity boards) to hand to a coding agent afterward.

**Image-first tip:** for `image-to-code-skill`, state the pipeline explicitly in the prompt, e.g. "follow the skill: generate images, then analyze, then code."

**ChatGPT Images and Codex:** attach or paste `imagegen-frontend-web`, `imagegen-frontend-mobile`, or `brandkit` and ask for the frames needed, then feed the renders to Codex, Cursor, or Claude Code.

### Settings (taste-skill only)

Numbers at the top of the file are 1-10 dials:

- **DESIGN_VARIANCE**: Layout experimentation (lower: centered/clean · higher: asymmetric/modern).
- **MOTION_INTENSITY**: Animation depth (lower: hover · higher: scroll/magnetic).
- **VISUAL_DENSITY**: Information per viewport (lower: spacious · higher: dense dashboards).

### Research

Background writing that shaped these skills lives in `research/`.

### Common Questions

**How is this different from other AI design skills?** Multiple specialized variants, adjustable dials in key skills, anti-repetition rules informed by dedicated research. All are framework-agnostic across major coding agents.

**Does it work with React, Vue, Svelte?** Yes — rules target design intent, not a single framework API.

**What is SKILL.md?** A portable instruction file agents can load automatically; install via `npx skills add` or by copying into a repo or conversation.

**Do image-generation skills install with `npx skills add`?** Yes — they live under `skills/` alongside the code skills so the same CLI discovers them.

### License

MIT License · Copyright (c) 2026 Leonxlnx

## Top-level structure

- `skills/` — thirteen self-contained skills, each installable individually or as a batch: `taste-skill/`, `taste-skill-v1/`, `gpt-tasteskill/`, `image-to-code-skill/`, `redesign-skill/`, `soft-skill/`, `output-skill/`, `minimalist-skill/`, `brutalist-skill/`, `stitch-skill/`, `imagegen-frontend-web/`, `imagegen-frontend-mobile/`, `brandkit/`, plus `skills/llms.txt`
- `.claude-plugin/` — Claude Code marketplace plugin manifest
- `research/` — background writing that shaped the skills
- `examples/` — sample output images (e.g. `floria-top.webp`, `floria-bottom.webp`)
- `assets/` — README banner, sponsor logos, button graphics
- `scripts/`, `skill.sh` — helper scripts
- `CHANGELOG.md` — full v1→v2 diff and rationale
- `LICENSE` (MIT)
