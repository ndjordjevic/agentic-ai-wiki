---
type: source
category: "Design & UI generation"
source_url: https://github.com/Owl-Listener/designer-skills
tags:
  - agent-skills
  - design-practice
  - claude-code-plugin
  - gemini-cli
  - design-systems
  - ux-research
  - visual-critique
  - marketplace
related:
  - elayadesign-ai-design-skills
  - jakubkrehel-skills
  - MengTo-Skills
  - leonxlnx-taste-skill
  - skills.sh
  - anthropics-skills
  - emilkowalski-skills
  - ConardLi-garden-skills
  - codeswithroh-tastemaker
  - ibelick-ui-skills
product: designer-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

Owl-Listener/designer-skills (3,124 stars, MIT) is the front-door marketplace for the Designer Skills Pack: **273 skills and 76 commands across 33 plugins in five collections** for Claude Code and Gemini CLI. This repo hosts the **design practice** collection (111 skills / 34 commands / 9 plugins spanning research → systems → UI → interaction → delivery) and pulls in four sibling marketplaces (AI product design, UX program management, design leadership, inclusive design). Situation-based routing via `INDEX.md` and `/designer-toolkit:start-here` distinguishes it from single-aesthetic anti-slop packs like [[leonxlnx-taste-skill]] or [[emilkowalski-skills]].

_All claims below are sourced from ../../raw/github/Owl-Listener-designer-skills.md unless otherwise noted._

## What it does

**Design practice plugins (this repo):** design-research, design-systems, ux-strategy, ui-design, interaction-design, prototyping-testing, design-ops, designer-toolkit, visual-critique — covering personas/journeys, tokens/components, competitive strategy, layout/type/color, micro-interactions/state machines, prototyping & A/B, handoff/sprints, presentations/case studies, and seven-axis visual critique.

**Sibling collections (separate repos, one marketplace add):** AI product design (`Owl-Listener/ai-design-skills`), UX PGM, design leadership, inclusive design.

Skills are domain knowledge (nouns); commands are workflows (verbs) such as `/design-research:discover`, `/ui-design:design-screen`, `/visual-critique:critique-screen`, `/design-ops:handoff`.

## Installation

```text
/plugin marketplace add Owl-Listener/designer-skills
# then /plugin → Discover → select collections/plugins

/plugin install ux-strategy@designer-skills
```

Gemini CLI: clone and copy `.gemini/extensions/` into the project. Non-coding onboarding is documented as Claude Code app → marketplace add → Discover install. Entry router: `/designer-toolkit:start-here`.

## Key features

- **Large design-ops surface** — research through critique and handoff, not only frontend visual polish.
- **Skills vs commands** — knowledge units composed by verb workflows (`plugin:verb` naming).
- **Situation index** — `INDEX.md` maps "I'm starting from nothing / auditing a screen / defending the work" to skills; frequently-confused pairs documented.
- **Selective install** — tick only the design plugins needed; sibling collections optional.
- **Dual host** — Claude Code marketplace plugins and Gemini CLI extensions.

## Architecture

Top-level plugin dirs: `design-research/`, `design-systems/`, `ux-strategy/`, `ui-design/`, `interaction-design/`, `prototyping-testing/`, `design-ops/`, `designer-toolkit/`, `visual-critique/`, plus `.claude-plugin/`, `.gemini/`, `INDEX.md`, templates (`SKILL_TEMPLATE.md`, `COMMAND_TEMPLATE.md`), and `scripts/`. Marketplace add of this repo surfaces plugins from the other four Owl-Listener collections as well.

## Example usage

```text
/plugin marketplace add Owl-Listener/designer-skills
/designer-toolkit:start-here
/visual-critique:critique-screen
/design-research:discover
```

## Maintenance status

3,124 GitHub stars, 423 forks, MIT licensed, default branch `main`, most recent push 2026-09-05, no tagged releases on this capture. Primary language Markdown. Substantial multi-collection suite with CHANGELOG and CONTRIBUTING; credited as an upstream by [[elayadesign-ai-design-skills]].
