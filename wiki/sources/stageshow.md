---
type: source
category: "Design & UI generation"
source_url: https://github.com/benjitaylor/skills/tree/main/stageshow
tags:
  - agent-skill
  - faux-ui
  - product-demo
  - react-kit
  - motion-choreography
  - marketing-hero
  - cursor-walkthrough
  - film-rehearsal
related:
  - AThevon-genjutsu
  - ParthJadhav-app-store-screenshots
  - dembrandt-dembrandt-skills
  - Nutlope-hallmark
  - nateherkai-scroll-craft
  - leonxlnx-taste-skill
  - skills.sh
product: stageshow
detail_level: standard
created: 2026-11-09
updated: 2026-11-09
---

stageshow (v1.1.1 skill; MIT; lives under `benjitaylor/skills` ~2.8k★) is an Agent Skill plus self-contained React/CSS kit for building faux product UI — still illustrations or short cursor-driven demos framed like marketing heroes, feature cards, phones, terminals, and bento grids — with a film/rehearsal gate instead of browser automation.

_All claims below are sourced from ../../raw/web/stageshow.md unless otherwise noted._

## What it does

It teaches agents to author miniature, believable product screens: quiet chrome, real words only where the story lands, intentional crop/bleed, and motion where every cursor move has a cause. Output is React using the shipped `kit/` (`Stage`, `Act`, `Window`, `Phone`, motion primitives), not live browser driving — `a.click()` draws a cursor press; `a.set()` changes the scene. Gold examples under `examples/` plus `references/` (framing, craft, motion, rehearse, teaching) define the quality bar.

## Key features

- Skill workflow: plan medium/place/look/story → copy closest gold → restyle to the brief → choreograph with `Act` → rehearse with `scripts/film.mjs --gate`.
- React kit: stage/scale, window and phone chrome, cursor, bars/rows/text, charts, notifications, motion helpers (`Collapse`, `Roll`, `Fly`, `Stream`, …).
- Looks and fidelity modes (light/dark/blueprint/glass; minimal/standard/realistic) with token mapping guidance.
- Large gold/product-study/specimen example set (hero-demo, linear, ai-chat, figma, finder, phones, …).
- Local playground (`npm run dev`) and contact-sheet filming at shown width and 390 for QA.

## Architecture and concepts

Packaged as a skill directory: `SKILL.md` is the operating contract; `kit/` is the reusable component library; `references/` holds still-frame and motion rules; `scripts/` films and gates demos with Playwright; `examples/` and `teaching/` supply good/bad pairs. The core idea is authored illustration — simplify content, not context — with five named failure modes (too much, wireframe, boxed, flat, bland) and a poster-first story so reduced-motion and thumbnails still read.

## Main APIs

Agent-facing: install/use the `stageshow` skill when someone wants mocked UI, product demos, hero shots, or cursor walkthroughs. Code-facing: import from `kit/index.ts`; drive scenes through `Act` (`set`, `wait`, `move`, `click`, `type`, …); mark targets with `data-target` / `data-cursor` and measure with `rect()`. Film via `node scripts/film.mjs "<preview>/?capture=<name>" --select '#example' --still|--gate`.

## When to use

- Marketing heroes, feature cards, docs illustrations that must look like a real product.
- Animated demos where one interaction happens and the loop must pass a contact-sheet gate.
- Preferring authored React faux UI over screenshot pastes or live browser automation.
- Matching a product's tokens/chrome while keeping filler quiet at the edges.

## Ecosystem

Lives in Benji Taylor's `benjitaylor/skills` monorepo (~2.8k★) alongside other agent skills; skill metadata version 1.1.1; package `stageshow` 0.1.0 (Node ≥20.19, React 18, lucide-react, Vite playground, playwright-core for film). Adjacent wiki design-skill pages include [[AThevon-genjutsu]], [[ParthJadhav-app-store-screenshots]], and [[nateherkai-scroll-craft]].
