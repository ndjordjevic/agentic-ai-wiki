# Nutlope/hallmark

## Metadata
- Stars: 18952
- Primary language: CSS
- Default branch: main
- Latest release: none (no tagged releases)
- License: MIT License
- Homepage: https://www.usehallmark.com/
- Fetched: 2026-07-28
- Final URL: https://github.com/Nutlope/hallmark

## Description
Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

## README

# Hallmark

**A design skill for Claude Code, Cursor, and Codex that refuses to look AI-generated.**

[Live demo →](https://www.usehallmark.com) · twenty themes · four verbs · press `T` to cycle.

Made by Together AI.

Hallmark picks a macrostructure for the brief, dresses it in one of twenty themes, runs fifty-seven slop-test gates plus a pre-emit self-critique, and refuses the on-distribution defaults every LLM was trained into. Two pages by Hallmark for two different briefs feel like different sites, not colour-swaps of the same template.

## Four verbs

| Verb | What it does |
| --- | --- |
| *(default)* | Build new UI. Picks a macrostructure, applies the rule-set, runs the slop test before handing back. |
| `hallmark audit <target>` | Score existing code against the anti-patterns. Punch list, no edits. |
| `hallmark redesign <target>` | Throw out the structure, keep copy + IA + brand, rebuild with a different fingerprint. |
| `hallmark study <screenshot \| URL>` | Extract the DNA from a design you admire: macrostructure, type-pairing, colour anchor. Refuses pixel-clones and paid templates. Optionally emits a portable `design.md` for handoff to other AI tools. |

## Different briefs, different shapes

Each generated page is self-contained HTML + CSS, stamped with its macrostructure in a CSS comment. Example gallery spans a sourdough app hero (Bubble theme), a content-extraction API (Cobalt), a record-label EP (Carnival), an AI reasoning tool (Lumen), a tea menu (Custom), a honey farm (Garden), a risograph print fair (Riso), a type studio (Custom), a SaaS product page (modern-minimal), a travel booking app (atmospheric), a Moroccan fashion brand, and a dev-infrastructure site. Browse the full set at usehallmark.com or under `site/_tests/`.

## Custom (new)

When a brief carries creative intent that no catalog theme fits, Hallmark switches to **Custom** and designs the page from scratch: a made-to-measure palette, type, and layout — same 57 slop-test gates, no template underneath. It stays a quiet branch; vanilla briefs never see it. Protocol lives in `skills/hallmark/references/custom-theme.md`.

## Install

```
npx skills add nutlope/hallmark
```

Re-run any time to update. Or copy `SKILL.md` + `references/` into:
- **Claude Code**: `~/.claude/skills/hallmark/`
- **Cursor**: `.cursor/rules/hallmark.mdc` (body of `SKILL.md`, no frontmatter)
- **Codex**: `~/.codex/skills/hallmark/` (personal) or `.codex/skills/hallmark/` (project-scoped)

The rule-set lives in `SKILL.md` and `references/`. Worked examples in `docs/recipes.md` and `docs/study-examples.md`.

## Licence

MIT. Use it, fork it, ship it.

## Docs

### skills/hallmark/SKILL.md (excerpt)

```yaml
---
name: hallmark
description: "Anti-AI-slop design skill for greenfield pages, audits, redesigns, and design extraction from URLs or screenshots. Use when the user asks to build a new app or landing page, wants to redesign something, invokes Hallmark by name, or uses audit/redesign/study."
version: 1.1.0
---
```

A design skill for AI coding assistants. Makes the UIs they generate look made, not generated. Hallmark is opinionated, short, and boring on purpose. It encodes a tight set of rules — drawn from the consensus of the anti-AI-slop design field (Anthropic's frontend-design skill, the Claude cookbook on frontend aesthetics, and the "tactile rebellion" movement) — and refuses to let the model fall back to the defaults every LLM was trained on. The differentiator: Hallmark insists on **structural variety**, not just visual variety — two pages for two different briefs should not share the same hero → 3-feature → CTA → footer rhythm; they should feel like different sites, not different colour-swaps of the same template (see `references/structure.md`). Powered by Together AI.

**How to use this skill** — one default behaviour, three explicit verbs:

| Invocation | What it does |
| --- | --- |
| *(default)* | User asked to design or build something new. Follow the Design flow. |
| `hallmark audit <target>` | Read the target, score it against the anti-pattern list, return a ranked punch list. Do not edit. |
| `hallmark redesign <target> [--mood <name>]` | Take the target's content and intent, redesign the visual structure inside existing implementation boundaries unless the user confirms a full rebuild; preserve routes, component ownership, copy intent, brand, and information architecture. |
| `hallmark study <screenshot \| URL>` | Extract the DNA (macrostructure, archetypes, type-pairing, colour anchor) from a design; produce a diagnosis report, then optionally rebuild using the extracted DNA or emit a portable `design.md`. URL mode reads the page's HTML/CSS via WebFetch (exact fonts/colours, no rhythm judgment); image mode reads a screenshot. Never copies pixels; refuses template-marketplace URLs; tighter refusal layer for `design.md` emission than for diagnosis alone. |

### ROADMAP.md (excerpt)

**Now:** Nanobanana hook for image-heavy briefs — today the integration is recommend-only (Hallmark tells the user to go generate an image and bring it back); image-heavy briefs (e-commerce, travel, food, lookbook) route to typography-only and feel underserved. Plan: add a first-class hook that writes a prompt, invokes the API, ingests the returned image, and wires it into the build (cached by prompt hash), paired with a new image-led theme (working title *Plate*) tuned for full-bleed photographic compositions.

**Next:**
- **Brand-first flow** — from a short product description, generate a complete brand (palette, type system, voice, custom imagery via Nanobanana) and lock it into a `design.md`; the user then runs Hallmark normally and the site builds against that generated brand across pages.
- **Theme-aware motion tokens** — per-theme `--dur-micro` / `--dur-short` / `--dur-long`, scaled by the table in `skills/hallmark/references/microinteractions.md` (e.g. Atelier should feel slower than Brutal; today they share durations).
- **`hallmark variant`** — produce three structurally distinct versions of the same brief side-by-side; the user picks one or asks for a fourth, addressing the biggest cause of "AI feel": users accepting the first output because they didn't know it could be different.

## Top-level structure

- `LICENSE` — MIT
- `README.md` — project overview (fetched above)
- `ROADMAP.md` — near-term and future plans (excerpt fetched above)
- `docs/` — `recipes.md` (worked examples), `study-examples.md`, `talk-slides.md`, `screenshots/` (gallery images)
- `site/` — the live demo site (Next.js/Vercel deploy) including `site/_tests/` example gallery pages
- `skills/hallmark/` — the runnable skill: `SKILL.md` plus `references/` (rule-set files including `structure.md`, `custom-theme.md`, `microinteractions.md`)
- `package.json`, `vercel.json` — project/deploy config
- `.gitignore` — boilerplate, not fetched
