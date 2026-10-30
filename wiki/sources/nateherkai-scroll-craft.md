---
type: source
category: "Design & UI generation"
source_url: https://github.com/nateherkai/scroll-craft
tags:
  - agent-skill
  - scroll-driven-sites
  - design-system
  - fingerprint-gate
  - playwright-verify
  - claude-code-plugin
  - immersive-landing
  - craft-standards
related:
  - oso95-scroll-world
  - leonxlnx-taste-skill
  - Nutlope-hallmark
  - pbakaus-impeccable
product: scroll-craft
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

scroll-craft is an agent skill (also a Claude Code plugin) for building premium, immersive, scroll-driven websites with an explicit design standard — treating interaction and craft as one job. It ships a shared workflow (brief → grammar → feel curve → build → verify), eight mutually exclusive page grammars, a fingerprint gate against self-repetition, a fixed `scrollcraft` engine themed only via tokens, and a Playwright/ffmpeg verification harness. Version 0.3.0 documents the process behind ten approved immersive sites as worked examples.

_All claims below are sourced from ../../raw/github/nateherkai-scroll-craft.md unless otherwise noted._

## What it does

When an agent follows the skill, it plans a site around one of eight page grammars (filmic one-shot, chaptered editorial, live surface, continuous world, typographic poster, gallery, split stage, rhythmic cutlist), invents a required signature move, and must clear a fingerprint gate vs prior builds on at least 4 of 6 dimensions (grammar, nav, hero, act shape, close, signature move). Craft rules cover a feeling curve and single engineered peak, typography floor, spacing scale, six-role colour system, depth tools, brand-kit precedence, and a refuse list (feature-card grids, gradient text, AI-purple, cream-and-brass defaults, invented stats, etc.).

Scroll is the timeline: scrubbed video, pinned sections, sideways rails, assembling headlines, shifting page grounds, and pointer-driven motion. After build, a headless browser walks every scroll position and reports dead scroll, cues that never reach full opacity, contrast on the composited page, and stuck video posters, then writes a contact sheet.

## Installation

**Codex / other skill hosts:** clone the repo and keep `plugins/nateherk-design/skills/scroll-craft/` intact. Copy that folder into `.agents/skills/` (Codex) or the agent's documented skills directory, or leave the repo in the workspace and ask the agent to read `SKILL.md`.

**Claude Code plugin:**

```bash
/plugin marketplace add nateherkai/scroll-craft
/plugin install nateherk-design
```

Invoke with `/nateherk-design:scroll-craft`. If prompted, run `/reload-plugins`. For local plugin hacking: `claude --plugin-dir ./plugins/nateherk-design`.

**Requirements:** Node 18+, a full ffmpeg build (scrub-capable encoding; `SCROLLCRAFT_FFMPEG` override), `playwright-core` + Chrome in the build folder, optional `KIE_AI_API_KEY` only if generating assets.

## Key features

- **Eight exclusive page grammars** — each forbids what the others require so builds cannot quietly converge
- **Fingerprint registry** — workspace `FINGERPRINTS.md` gates uniqueness against *your* prior pages (starts empty by design)
- **Feeling curve + peak-end** — one emotion line per act; one engineered peak owns asset budget and scroll room
- **Design floor** — type, spacing, colour roles, depth tools, brand hard rules, refuse list
- **Verification harness** — dead scroll, cue opacity, contrast, stuck posters, contact sheet
- **Fixed engine** — `engine/scrollcraft.js` + `.css` never edited per project; theme with six colour tokens and two fonts; drive bespoke motion off `--sc-p`
- **Approved collection (0.3.0)** — process docs for ten sites (AI Automation Society, PERKFORM, Glaido, etc.) plus hero-depth guidance
- **Workspace resolution** — `SCROLLCRAFT_HOME`, nearest `.scrollcraft.json`, or `<project>/scrollcraft`

## Architecture

Skill package under `plugins/nateherk-design/skills/scroll-craft/`:

- `SKILL.md` — procedure (brief, grammar, score, build, verify)
- `references/` — approved-collection, hero-depth, uniqueness, feel, devices, worldflight, worlds, taste, assets, verify, plus `template.html`
- `engine/` — shared scrollcraft runtime (mechanism only)
- `templates/` — empty fingerprint registry seed
- `scripts/` — `doctor`, `workspace`, `kie`, `encode`, `serve`, `shoot`, `worldflight-assert`

Marketplace metadata lives in `.claude-plugin/`. Builds land in `<workspace>/builds/<name>/`. Honest limitations: author has only run builds on Windows (path search covers macOS/Linux; overrides available); generated video can be expensive; the skill is intentionally opinionated.

## Example usage

First-run checks from the repo root:

```bash
node plugins/nateherk-design/skills/scroll-craft/scripts/doctor.mjs
node plugins/nateherk-design/skills/scroll-craft/scripts/workspace.mjs --ensure
```

Claude Code after plugin install:

```
/nateherk-design:scroll-craft
```

Any coding agent with the folder in workspace:

```text
Read plugins/nateherk-design/skills/scroll-craft/SKILL.md and use it to build
my website. Follow the referenced design and verification workflow.
```

## Maintenance status

4,232 GitHub stars, 606 forks, JavaScript, MIT License, default branch `main`, no GitHub releases listed (README documents 0.3.0 skill content), last push 2026-09-30. Changelog lives at `plugins/nateherk-design/skills/scroll-craft/CHANGELOG.md` and records what broke on each build and the resulting rule.
