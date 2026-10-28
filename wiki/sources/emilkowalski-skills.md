---
type: source
category: "Design & UI generation"
source_url: https://github.com/emilkowalski/skills
tags:
  - agent-skills
  - animation
  - design-engineering
  - anti-slop
  - react-native-expo
  - sonner
  - ui-review
  - skills-sh
related:
  - leonxlnx-taste-skill
  - skills.sh
  - jakubkrehel-skills
  - ConardLi-garden-skills
  - elayadesign-ai-design-skills
  - codeswithroh-tastemaker
  - MengTo-Skills
  - Owl-Listener-designer-skills
  - Nutlope-variate
  - img2threejs-img2threejs
  - ibelick-ui-skills
  - FloWritesCode-fwc-swiftui-skills
  - ui-skills.com
product: skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

emilkowalski/skills (50,398 stars, MIT) is Emil Kowalski's Agent Skills pack for designers and engineers — animation craft, design-engineering judgment, and UI stress-testing distilled from work at Vercel and Linear. Distributed via `npx skills` / [[skills.sh]], it targets the failure mode where agents pick the wrong easing, over-animate, or hand-roll abandoned UI primitives, and is a common upstream credit for other design skill packs such as [[leonxlnx-taste-skill]] and [[elayadesign-ai-design-skills]].

_All claims below are sourced from ../../raw/github/emilkowalski-skills.md unless otherwise noted._

## What it does

The repo ships fifteen portable skills under `skills/`. The flagship `emil-design-eng` bundles animation and design advice; dedicated skills cover building animations from scratch (`animate`, `animate-expo` for React Native/Expo), reviewing and improving motion (`review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance`, `animation-vocabulary`), Apple/WWDC-derived interface principles (`apple-design`), Swift writing (`write-swift`), library selection (`pick-ui-library`), multi-variant prototyping (`prototype`), mobile-web native feel (`mobile-native`), worst-case data breaking (`break-ui`), and Sonner toast guidance (`ask-sonner`). The README frames the pack as domain expertise amplified by agents — a shortcut past generic AI UI — not a replacement for learning design and code.

## Installation

```bash
npx skills@latest add emilkowalski/skills
```

Skills are also listed on [[skills.sh]] at the emilkowalski/skills path. Newsletter signup for updates is at aiforui.dev/skills.

## Key features

- **Animation-first craft rules** — easing, duration, property choice, and performance pitfalls that agents commonly miss (`ease-in` on enter, layout thrash, JS-thread motion on native).
- **Review and opportunity skills** — strict animation review, prioritized improvement plans any agent can execute, and explicit guidance on what *not* to animate.
- **Cross-platform coverage** — web animation plus Expo/React Native (`animate-expo`, `mobile-native`) and Swift (`write-swift`).
- **Library taste** — `pick-ui-library` steers agents toward maintained libraries Emil trusts instead of reinventing toasts or abandoned packages.
- **Prototype switcher** — `prototype` builds multiple UI variants behind a switcher for comparison.
- **Worst-case UI stress** — `break-ui` forces long names, empty lists, huge counts, and awkward labels.

## Architecture

Top-level content is a `skills/` tree of self-contained skill folders (each with `SKILL.md`), plus `performance-cheatsheet.md`, license, and README. No runtime package — distribution is the Agent Skills / [[skills.sh]] convention. Homepage: https://emilkowal.ski/skill.

## Example usage

```bash
npx skills@latest add emilkowalski/skills
# then ask the agent to review animations, improve motion, or build with emil-design-eng
```

## Maintenance status

50,398 GitHub stars, 2,935 forks, MIT licensed, default branch `main`, most recent push 2026-10-11, no tagged releases. Primary language Markdown. Active public skill pack with a [[skills.sh]] badge and newsletter channel.
