---
type: source
category: "Design & UI generation"
source_url: https://github.com/VoltAgent/awesome-design-md
tags:
  - design-md
  - design-systems
  - agent-ui
  - vibe-coding
  - design-tokens
  - brand-systems
  - google-stitch
  - awesome-list
related:
  - voltagent-awesome-agent-skills
  - open-design.ai
  - lovable.dev
  - bolt.new
  - skills.sh
  - anthropics-skills
  - stitch.withgoogle.com
  - using-claude-code-unreasonable-effectiveness-html
  - designmd.cc
  - pbakaus-impeccable
  - duply.ai
product: awesome-design-md
detail_level: standard
created: 2026-07-02
updated: 2026-07-10
---

Awesome DESIGN.md is VoltAgent's curated catalog of 73+ agent-readable brand design systems (95,082 stars, MIT) — plain-text `DESIGN.md` files reverse-engineered from real websites so coding agents can generate UI that matches a target brand's visual language without Figma exports or JSON schemas. The repo popularizes the Google Stitch `DESIGN.md` convention as the design counterpart to `AGENTS.md`: drop a file in the project root, tell the agent "build me a page that looks like this," and get consistent tokens, typography, component rules, and prompt guides. Brands span AI platforms (Claude, Cursor, VoltAgent), SaaS (Linear, Stripe, Notion), fintech, automotive, and a retro-web nostalgia series.

_All claims below are sourced from ../../raw/github/voltagent-awesome-design-md.md unless otherwise noted._

## What it does

Awesome DESIGN.md is a discovery and distribution layer for the `DESIGN.md` format — a markdown design-system document that AI agents read to generate visually consistent UI. Each entry in `design-md/<brand>/` captures a real site's complete visual language: color roles with hex values, typography hierarchy, component stylings, layout principles, elevation rules, do's/don'ts, responsive behavior, and ready-to-use agent prompts. The README catalogs 73+ brands across nine categories (AI & LLM platforms, developer tools, backend/DevOps, productivity SaaS, design tools, fintech, e-commerce, media, automotive) plus a retro-web nostalgia series. Companion site getdesign.md hosts browsable previews and accepts custom DESIGN.md requests.

## Key features

- **73+ production-grade DESIGN.md files** extracted from live sites — not surface-level color swatches but full design depth including analyzed patterns, tokens, and guardrails.
- **Stitch DESIGN.md format** with nine canonical sections: Visual Theme & Atmosphere, Color Palette & Roles, Typography Rules, Component Stylings, Layout Principles, Depth & Elevation, Do's and Don'ts, Responsive Behavior, Agent Prompt Guide.
- **YAML-frontmatter token blocks** per brand — semantic color roles (`primary`, `canvas`, `surface-1`, `ink-muted`), full typography scale tables (font family, size, weight, line-height, letter-spacing), and prose design philosophy in the `description` field.
- **AGENTS.md / DESIGN.md pairing** — explicit documentation that `AGENTS.md` tells coding agents how to build while `DESIGN.md` tells design agents how the project should look and feel.
- **Category-organized Awesome list** covering brands agents commonly emulate: Linear, Vercel, Stripe, Cursor, Claude, Shopify, Apple, Tesla, and 65+ more.
- **Retro Web nostalgia series** — period-accurate DESIGN.md files for Dell (1996) and Nintendo.com (2001) for vintage UI generation.
- **getdesign.md ecosystem** — request custom DESIGN.md extractions, browse hosted previews, and sponsor product placement alongside the collection.

## Architecture

The repository is a content catalog, not a runtime or SDK. Top-level structure is minimal: `README.md` (Awesome-list index), `CONTRIBUTING.md`, `LICENSE`, and `design-md/` containing 74 brand directories. Each brand folder holds a `DESIGN.md` (the primary agent artifact) and a `README.md`; preview HTML catalogs are referenced in documentation and served via getdesign.md CDN. Files follow the [Google Stitch DESIGN.md specification](https://stitch.withgoogle.com/docs/design-md/specification/) with VoltAgent's extended sections. No build step, no package manager, no API — agents consume the markdown directly. Maintained by VoltAgent (same org behind [[voltagent-awesome-agent-skills]] and the VoltAgent TypeScript agent framework).

## Example usage

```bash
# Copy a brand's DESIGN.md into your project root
curl -o DESIGN.md https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/linear.app/DESIGN.md

# Then instruct your coding agent:
# "Build a landing page using DESIGN.md for visual consistency."
```

Workflow: (1) pick a brand from the README or `design-md/` folder, (2) copy its `DESIGN.md` to the project root (or reference it in agent instructions), (3) prompt the agent to generate UI against those tokens and rules. Works with Claude Code, Cursor, Codex, Google Stitch, and any agent that reads project markdown files.

## When to use

Use this repository when:
- Generating UI that should match a specific brand's visual identity (marketing pages, demos, prototypes) without manual design handoff.
- Bootstrapping a `DESIGN.md` for a new project by starting from a proven brand template.
- Comparing how different SaaS products structure their design tokens for agent consumption.
- Teaching agents the `DESIGN.md` convention alongside `AGENTS.md` project instructions.

Not a substitute for [[open-design.ai]] when you need a full local design platform with daemon, MCP server, and artifact generation — this repo is the portable token library; Open Design is the integrated design engine. Contribution policy does not accept new DESIGN.md PRs (quality-controlled curation only).

## Maintenance status

95,082 stars, 11,228 forks, MIT License, actively maintained (last pushed 2026-06-16). No versioned releases. Contribution policy: improvements to existing files require opening an issue first; new DESIGN.md submissions are not accepted via PR to preserve curation quality. Backed by VoltAgent with Discord community (s.voltagent.dev/discord) and sponsor program. Ranked ~#150 globally on GitHub at time of README publication.

## Ecosystem

- [[voltagent-awesome-agent-skills]] — VoltAgent's parallel Awesome-list for `SKILL.md` agent capabilities; Awesome DESIGN.md is the design-system counterpart in the same distribution philosophy.
- [[open-design.ai]] — open-source agent-native design platform with 150+ DESIGN.md brand systems, daemon, and MCP server; overlaps in DESIGN.md distribution but adds a full local design engine and artifact pipeline.
- [[lovable.dev]] and [[bolt.new]] — AI app builders where dropping a DESIGN.md into the project context directly improves generated UI consistency.
- [[skills.sh]] — Vercel's skill distribution layer; DESIGN.md files serve a parallel role for visual instructions rather than behavioral skills.
- Google Stitch ([[stitch.withgoogle.com]]) — originated the DESIGN.md concept and specification this repo implements and extends.
