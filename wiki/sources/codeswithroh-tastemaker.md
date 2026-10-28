---
type: source
category: "Design & UI generation"
source_url: https://github.com/codeswithroh/tastemaker
tags:
  - agent-skills
  - anti-slop
  - design-taste
  - palette-generator
  - contrast-matrix
  - style-lock
  - claude-code-plugin
  - local-scripts
related:
  - leonxlnx-taste-skill
  - emilkowalski-skills
  - ConardLi-garden-skills
  - jakubkrehel-skills
  - skills.sh
  - elayadesign-ai-design-skills
  - Owl-Listener-designer-skills
  - MengTo-Skills
  - Nutlope-variate
product: tastemaker
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

Tastemaker (501 stars, MIT) is a Claude Code–first Agent Skill (also Windsurf / Gemini CLI) that grounds AI UI in real reference pixels, a contrast-checked generated palette, and persistent local taste memory — so agents stop defaulting to indigo-gradient "AI slop." Unlike prompt-only taste packs, it ships Python scripts (`generate_palette.py`, `check_contrast.py`, `extract_palette.py`, `anti_slop_scan.py`, `audit_motion.py`, …) that enforce legibility contracts and write project locks under `.tastemaker/` plus a durable `~/.tastemaker/profile.md`. Live demo: https://tastemaker-skill.online.

_All claims below are sourced from ../../raw/github/codeswithroh-tastemaker.md unless otherwise noted._

## What it does

On UI build/style requests the skill: reads the idea/spec; builds a reference board when cold-starting; generates a fresh mood-based OKLCH palette that satisfies a contrast matrix by construction; locks style to `.tastemaker/style-lock.md`; sources attribution-free photos/icons/illustrations and a constructed logo; wires GSAP/ScrollTrigger motion; runs anti-slop and motion audits; and records keep/reject evidence for the next project. It separates **verified** checks (WCAG contrast math) from **judgment** (taste heuristics and profile memory). Cursor installs are explicitly called out as degraded today (`.mdc` conversion strips `references/` and `scripts/`).

## Installation

```bash
# Claude Code plugin (recommended)
/plugin marketplace add codeswithroh/tastemaker
/plugin install tastemaker@codeswithroh

# Manual — copy skills/tastemaker only
git clone https://github.com/codeswithroh/tastemaker /tmp/tastemaker
cp -r /tmp/tastemaker/skills/tastemaker ~/.claude/skills/tastemaker

# Gemini CLI
gemini skills install https://github.com/codeswithroh/tastemaker --path skills/tastemaker
```

Python 3 + Pillow recommended for deterministic palette extraction (`pip install Pillow`); vision fallback if Pillow is missing. Homepage: https://tastemaker-skill.online.

## Key features

- **Runnable constraints** — contrast matrix and anti-slop/motion scanners, not just written preferences.
- **Fresh palette per project** — mood → hue range → harmony rule → lightness solved for WCAG floors; `--seed` for reproducibility.
- **Pixel grounding** — `extract_palette.py` reads real colors from reference images.
- **Persistent taste** — project `style-lock.md` / `decisions.log` and user `~/.tastemaker/profile.md`.
- **Assets in one pass** — Openverse photos, Iconify icons, recolored illustrations, geometric logo + favicons.
- **Honest Cursor caveat** — full mechanism needs native SKILL.md + subdirs; Cursor conversion currently loses scripts/references.

## Architecture

Core skill at `skills/tastemaker/` (`SKILL.md`, `references/`, `scripts/`, vendored `ideagram/` illustration sub-skill). Repo also includes `.claude-plugin/`, `docs/`, `research/`, `site/` / `web/` / `worker/` for the demo site, and `.tastemaker/` examples. Everything runs locally — no hosted backend or API key required for the skill itself.

## Example usage

```bash
/plugin install tastemaker@codeswithroh
# then simply:
# build a landing page for a coffee subscription
# (skill triggers; palette + lock + assets + motion in one pass)
```

```bash
python3 scripts/generate_palette.py --mood technical
```

## Maintenance status

501 GitHub stars, 51 forks, MIT licensed, default branch `main`, most recent push 2026-10-11, no tagged releases. Primary language Python. Active skill with live compare demo and CHANGELOG; smaller star count than sibling design packs but unusually script-enforced for the category.
