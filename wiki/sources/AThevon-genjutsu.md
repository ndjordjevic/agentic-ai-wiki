---
type: source
category: "Design & UI generation"
source_url: https://github.com/AThevon/genjutsu
tags:
  - claude-code-skills
  - motion-design
  - anti-slop
  - gsap
  - interaction-thesis
  - design-systems
  - bunshin
  - creative-coding
related:
  - leonxlnx-taste-skill
  - dembrandt-dembrandt-skills
  - INSANE0777-Awwwards-mcp
  - dembrandt-dembrandt
  - Nutlope-hallmark
  - obra-superpowers
product: genjutsu
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

genjutsu (~695★, MIT badge, Python packaging for Claude skills, v4.1.1) is a set of Claude Code / claude.ai / Cowork creative-coding skills for motion, micro-interactions, and design systems across web (GSAP, Motion, Three.js, CSS), Android (Compose), and Apple (SwiftUI). It proposes an interaction thesis you approve before writing code — anti-AI-slop by design.

_All claims below are sourced from ../../raw/github/AThevon-genjutsu.md unless otherwise noted._

## What it does

Three scales of skill: **cast** (change one part of a page), **paint** (plan/build a whole page), and **bunshin** (full agent system — parallel subagents under a shared style with checker agents). Skills stop at gates (interaction thesis, visual identity, design system) and show a proposal before implementing.

## Installation

See https://genjutsu.athevon.dev/docs/install — works with Claude Code, claude.ai, Cowork, and npx per README badges. Latest release `v4.1.1`.

## Key features

- Cast / Paint / Bunshin skill ladder for scoped vs systemic UI work
- Proposal-before-code gates with preview/replay options
- Motion and design-system modules ("jutsu") plus "tells" / principles docs
- Multi-platform targets: web motion stacks, Jetpack Compose, SwiftUI
- Explicit anti-slop measurement narrative in the README

## Architecture

Skill pack + documentation site rather than a runtime app. Bunshin orchestrates parallel page builders under shared style with verification agents — an opinionated multi-agent design harness packaged as skills.

## Example usage

Invoke cast for a single interaction (e.g. hero parallax), paint for a full page, or bunshin for a multi-page site under one visual system; approve the thesis/preview before code lands.

## Maintenance status

~695 stars, 52 forks, release `v4.1.1`, homepage https://genjutsu.athevon.dev, license marked Other in GitHub API with MIT badge in README.
