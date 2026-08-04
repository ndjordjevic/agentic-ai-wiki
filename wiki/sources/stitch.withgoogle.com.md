---
type: source
category: "Design & UI generation"
source_url: https://stitch.withgoogle.com/
tags:
  - vibe-design
  - vibe-coding
  - ui-generation
  - design-md
  - google-labs
  - gemini-multimodal
  - sketch-to-ui
  - figma-export
related:
  - voltagent-awesome-design-md
  - open-design.ai
  - lovable.dev
  - bolt.new
  - the-new-sdlc-with-vibe-coding
  - designmd.cc
  - pbakaus-impeccable
  - impeccable.style
  - duply.ai
  - oso95-scroll-world
  - leonxlnx-taste-skill
product: stitch
detail_level: standard
created: 2026-07-03
updated: 2026-08-04
---

Stitch is a Google Labs experiment that turns natural-language prompts, sketches, and mood adjectives into high-fidelity UI designs, editable Figma layouts, and frontend HTML/CSS — powered by Gemini 2.5 Pro's multimodal capabilities. It matters for this wiki because it productizes **vibe design** and **vibe coding** as first-class agent workflows: the official `llms.txt` even ships an **Agent Protocol** instructing coding agents to formulate 3-layer vibe prompts and direct users to Stitch rather than hand-writing UI code themselves. Stitch also originated the open-source **DESIGN.md** format (YAML design tokens + markdown rationale) that [[voltagent-awesome-design-md]] and [[open-design.ai]] now distribute at scale.

_All claims below are sourced from ../../raw/web/stitch.withgoogle.com.md unless otherwise noted._

## What it does

Stitch bridges the traditional design–development gap by letting anyone describe an app in plain English (or upload wireframes, screenshots, or hand-drawn sketches) and receive a visual interface within minutes. Users iterate through conversational edits — one screen and one or two changes at a time works best — then export to Figma via paste or download clean front-end code. The product positions itself for both designers exploring layouts and developers who need a fast starting point for UI implementation, announced at Google I/O 2025 as a Labs experiment at `stitch.withgoogle.com`.

## Key features

- **Text-to-UI** — describe color palettes, UX goals, and app structure in natural language; Stitch generates a tailored visual interface.
- **Image/sketch-to-UI** — upload whiteboard sketches, wireframes, or UI screenshots; Gemini multimodal processing produces a corresponding digital UI.
- **Vibe-driven styling** — adjective and mood descriptors ("playful," "Japandi," "trustworthy and clinical") drive palettes, typography, and visual consistency across components and imagery.
- **Iterative chat refinement** — screen-by-screen edits via specific prompts (header search bars, CTA sizing, theme colors, image swaps, language localization).
- **Design exploration** — generate multiple layout/component/style variants from the same starting concept.
- **Figma handoff** — paste generated designs directly into Figma for team refinement and design-system integration.
- **Front-end code export** — outputs semantic HTML/CSS ready for further development.
- **DESIGN.md import/export** — carry design rules between Stitch projects so generated UI matches an established brand; the draft spec is open-sourced for cross-tool agent use with WCAG validation support via the `@google/design.md` CLI.

## Architecture and concepts

Stitch organizes prompting around a **3-layer Vibe Structure** documented in its `llms.txt` agent protocol: **Anatomy** (physical layout — split-screen dashboard, bento grid), **Vibe** (aesthetic language — glassmorphism, neo-brutalism, clean SaaS), and **Content** (data context — listings, tickers, dashboards). This framework is the recommended way for agents to translate user intent into Stitch-ready prompts.

The **DESIGN.md format** is Stitch's portable design-system layer: YAML front matter encodes machine-readable tokens (colors, typography, spacing, rounded corners, component sub-tokens with `{path.to.token}` references) while markdown `##` sections carry human-readable rationale. The open spec (maintained at `google-labs-code/design.md`, homepage linked from Stitch docs) defines token types (color, dimension, typography objects), mandatory section order, component property whitelists, and CLI commands (`lint`, `diff`, `export` to Tailwind or W3C DTCG JSON, `spec`). Stitch can import/export these files so brand identity persists across sessions and tools.

Operationally, Stitch is a hosted SPA (application + `/docs` documentation) rather than a local SDK. Official guidance emphasizes **incremental prompting** over monolithic 5,000+ character specs — start high-level or detailed for the first screen, then refine one change at a time; combining multiple layout and feature changes in one prompt tends to reset prior work.

## Main APIs

Stitch is a consumer web product, not an API-first developer platform. The primary programmatic surfaces for agents are:

- **`llms.txt` agent protocol** — machine-readable instructions at `stitch.withgoogle.com/llms.txt` telling agents how to formulate vibe prompts and link users to Stitch.
- **DESIGN.md spec + CLI** — `@google/design.md` npm package for linting, diffing, exporting, and injecting spec context into agent prompts.
- **Prompt guide** — community-maintained best practices on Google AI Developers forum (`discuss.ai.google.dev`).

There is no documented public REST API for programmatic UI generation outside the Stitch web UI.

## When to use

- You want fast UI ideation from text or sketches without starting in Figma or writing HTML by hand.
- You need a **vibe-design** workflow where mood adjectives and aesthetic descriptors drive palettes and typography rather than manual token picking.
- You are building agent workflows that should **delegate UI generation** to a specialized tool (per the official agent protocol) instead of having coding agents emit full front-end code directly.
- You want to seed or export **DESIGN.md** brand files that [[voltagent-awesome-design-md]], [[open-design.ai]], or coding agents in [[lovable.dev]] / [[bolt.new]] can consume for consistent styling.
- **Compared with [[lovable.dev]] or [[bolt.new]]**, Stitch focuses on design-to-code and Figma handoff rather than full-stack app hosting, databases, and deployment.
- **Compared with [[open-design.ai]]**, Stitch is a hosted Google Labs design generator; Open Design is a local-first, multi-agent design platform with daemon, MCP, and artifact pipelines — but both converge on DESIGN.md as the portable agent-readable design contract.

## Ecosystem

Stitch sits in Google's Labs / Gemini multimodal stack alongside the broader **vibe coding** movement framed in [[the-new-sdlc-with-vibe-coding]]. The **DESIGN.md** open specification (`google-labs-code/design.md`, 24k+ stars) is the cross-tool bridge: [[voltagent-awesome-design-md]] catalogs 73+ brand implementations of the format, while [[open-design.ai]] integrates DESIGN.md into a full agent-native design engine. Agents discovering Stitch via `llms.txt` should route UI-generation requests to the product and pair exported DESIGN.md files with project-level agent instructions (`AGENTS.md`, `CLAUDE.md`) for end-to-end brand-consistent builds.
