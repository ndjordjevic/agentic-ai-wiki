---
type: source
category: "Design & UI generation"
source_url: https://github.com/Nutlope/hallmark
tags:
  - anti-ai-slop
  - design-skill
  - slop-test-gates
  - macrostructure
  - agent-skill
  - design-extraction
  - theme-catalog
related:
  - leonxlnx-taste-skill
  - voltagent-awesome-design-md
  - open-design.ai
  - anthropics-skills
product: hallmark
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

Hallmark is an open-source design skill (Together AI, 18,900+ stars) for Claude Code, Cursor, and Codex that targets a specific failure mode of AI-generated UI: every model converges on the same hero → 3-feature → CTA → footer template regardless of brief. It picks a macrostructure per brief, applies one of twenty curated themes (or a from-scratch "Custom" branch when no theme fits), runs 57 slop-test gates plus a pre-emit self-critique, and refuses the on-distribution defaults models were trained into — the explicit goal being **structural** variety between pages, not just palette-swap variety. See [[Nutlope-hallmark]].

_All claims below are sourced from ../../raw/github/Nutlope-hallmark.md unless otherwise noted._

## What it does

Hallmark has one default behavior and three explicit verbs, invoked as `hallmark <verb> <target>`: the default builds new UI (picks a macrostructure, applies the rule-set, runs the slop test before handing back); `audit <target>` scores existing code against the anti-pattern list and returns a ranked punch list without editing; `redesign <target> [--mood <name>]` keeps a target's content, copy, and information architecture but rebuilds its visual/interaction layer with a different structural fingerprint; and `study <screenshot | URL>` extracts a design's "DNA" (macrostructure, archetypes, type-pairing, colour anchor) and either rebuilds the user's content using that DNA or emits a portable `design.md` for handoff to other AI tools. URL-mode study reads a live page's HTML/CSS via WebFetch (exact fonts and colours, no rhythm judgment); it refuses to pixel-clone or extract from template-marketplace URLs.

## Installation

```
npx skills add nutlope/hallmark
```

Re-runnable to update. Alternatively, copy `SKILL.md` + `references/` directly into an agent's skill directory: `~/.claude/skills/hallmark/` for Claude Code, `.cursor/rules/hallmark.mdc` (body only, no frontmatter) for Cursor, or `~/.codex/skills/hallmark/` (personal) / `.codex/skills/hallmark/` (project-scoped) for Codex.

## Key features

- 20 built-in themes plus a **Custom** branch: when a brief carries creative intent no catalog theme fits, Hallmark designs a made-to-measure palette, type, and layout from scratch instead — the same 57 slop-test gates apply, just with no template underneath.
- Each generated page is self-contained HTML + CSS, stamped with its chosen macrostructure in a CSS comment, so provenance is inspectable per page.
- The rule-set explicitly draws on "the consensus of the anti-AI-slop design field" — cited as Anthropic's frontend-design skill, the Claude cookbook on frontend aesthetics, and the broader "tactile rebellion" design movement.
- Roadmap items (not yet shipped, per `ROADMAP.md`): a first-class Nanobanana image-generation hook for image-heavy briefs (e-commerce, travel, food) that today route to typography-only output; a "brand-first" flow that generates and locks a full brand (palette, type, voice) into a `design.md` before building pages against it; theme-aware motion-duration tokens; and a `hallmark variant` verb to produce multiple structurally distinct options side-by-side, aimed at the failure mode of users accepting the first output because they didn't know it could be different.

## Architecture

The rule-set and verb logic live in `skills/hallmark/SKILL.md` plus a `references/` directory (including `structure.md` for macrostructure rules, `custom-theme.md` for the from-scratch branch protocol, and `microinteractions.md` for motion timing tables). The live demo and example gallery (`site/`, including `site/_tests/`) are a separate Next.js/Vercel-deployed site at usehallmark.com used both as a showcase and as a working reference for the theme catalog.

## Example usage

Default invocation via natural-language request in an agent that has the skill installed (e.g. "build me a landing page for a sourdough app"), or explicit verb syntax: `hallmark audit <target>`, `hallmark redesign <target> --mood <name>`, `hallmark study <screenshot-or-URL>`. Worked examples are collected in `docs/recipes.md` and `docs/study-examples.md`.

## When to use

Fits AI coding assistants (Claude Code, Cursor, Codex) generating new landing pages, auditing or redesigning existing UI, or extracting a reusable design system from an admired reference (screenshot or live URL). Its differentiator versus generic "make it look nice" prompting is the structural-variety guarantee: two different briefs should produce pages that read as different sites, not re-skins of one template.

## Maintenance status

18,952 stars, 952 forks, MIT licensed, primary language CSS, default branch `main`, no tagged GitHub releases as of the fetch date (2026-07-28). Actively maintained per its `ROADMAP.md`, which lists concrete near-term (Nanobanana image hook) and next-tier (brand-first flow, motion tokens, `hallmark variant`) work items.

## Ecosystem

Made by Together AI. Positions itself against the same "AI slop" aesthetic problem as [[leonxlnx-taste-skill]] (an anti-slop frontend skill family with GSAP motion and design dials) and the `design.md` portable-DNA format also used by [[voltagent-awesome-design-md]] and [[open-design.ai]] — Hallmark's `study` verb can emit its own `design.md` output for handoff to other tools in that ecosystem. Distributed as an installable Agent Skill alongside the broader catalog in [[anthropics-skills]].
