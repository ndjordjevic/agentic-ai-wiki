---
type: source
category: "Design & UI generation"
source_url: https://duply.ai/
tags:
  - design-md
  - design-tokens
  - design-systems
  - vibe-coding
  - curated-library
  - brand-systems
  - ui-generation
related:
  - voltagent-awesome-design-md
  - open-design.ai
  - designmd.cc
  - stitch.withgoogle.com
  - pbakaus-impeccable
product: duply
detail_level: standard
created: 2026-07-10
updated: 2026-07-10
---

Duply is a curated library of 312+ real-world design systems, each published as a copy-paste-ready `DESIGN.md` file — structured color/typography/spacing/radius/component tokens plus a written analysis — so a coding agent (Claude Code, Cursor, v0, Lovable, Bolt) can reproduce a specific brand's visual language accurately instead of defaulting to a generic AI-template look.

_All claims below are sourced from ../../raw/web/duply.ai.md unless otherwise noted._

## What it does

Duply publishes one `DESIGN.md` per documented product (312 at the time of this ingest, including Anthropic, Claude, Airbnb, Stripe-adjacent fintechs, ClickHouse, Convex, and many dev-tools/SaaS brands), each with a written design analysis plus a raw markdown export (`https://duply.ai/<brand>/design-md/raw`). Pages are free to read and explicitly citable by URL per the site's own `llms.txt`. A `Full corpus` endpoint (`https://duply.ai/llms-full.txt`) concatenates every design system's raw `DESIGN.md` for one-fetch ingestion by an agent or script.

## Key features

- **312+ brand entries** spanning fintech, dev tools, AI products, productivity SaaS, and consumer sites, each with hex-level color roles, named typefaces, spacing/radius tokens, and a prose "brand voltage" analysis describing what carries the visual identity (a signature accent color, an oversized display typeface, a photographic hero, etc.).
- **`DESIGN.md` format** per the site's own explainer: colors organized by usage role (canvas, ink, surfaces, accent, semantic), a full typography scale (family, size, weight, line-height, letter-spacing), a spacing/radius/elevation rhythm, and component specs with do's/don'ts and responsive notes.
- **Library browsing** filterable by style, industry, color, and typeface (per `/library`).
- **Raw markdown export per entry** (`/<brand>/design-md/raw`) and a single-fetch full-corpus file (`/llms-full.txt`), both designed for direct agent ingestion rather than manual copy-paste from HTML.
- **Request-a-design** intake via email for brands not yet in the library.

## Architecture and concepts

Each entry is framed as an independent "design-system analysis of publicly observable patterns" — the site is explicit that it is not affiliated with or endorsed by the brands it documents, redistributes no proprietary assets, and substitutes documented alternatives for licensed typefaces. Several entries note when only a partial measurement was possible (e.g. a color-only frequency scan with typography/spacing/radius flagged as derived placeholders), which signals the underlying method is closer to visual/token inference from live pages than the DOM/CSSOM live-measurement approach [[designmd.cc]] uses.

## Main APIs

Not an SDK or CLI — Duply is a content library consumed via URL. The two integration points are the per-brand `/design-md/raw` markdown export and the `/llms-full.txt` full-corpus file; both are documented as free to fetch and cite.

## When to use

Reach for Duply when a coding agent needs to build in a specific, real brand's visual language and a ready-made entry already exists in the 312-brand library — pick a design, copy its `DESIGN.md` into the project, and instruct the agent to follow it exactly rather than inventing plausible-looking values. Less suited when the target brand isn't in the library (use [[designmd.cc]]'s live extractor instead) or when a generic/synthetic design system is wanted rather than a specific brand's reproduction.

## Ecosystem

Duply sits in the same `DESIGN.md`-as-project-context niche as [[voltagent-awesome-design-md]] (a smaller, GitHub-hosted curated catalog of 73+ brands) and [[open-design.ai]] (a full local design engine with 150+ bundled DESIGN.md systems, a daemon, and an MCP server) — all three distribute pre-made, brand-specific token files rather than measuring a URL live like [[designmd.cc]]. The `DESIGN.md` convention itself traces back to Google Stitch ([[stitch.withgoogle.com]]), and [[pbakaus-impeccable]] documents a related design-language skill for agents evolved from Anthropic's `frontend-design` skill. Duply differentiates on library size (312+ vs. 73+ for Awesome DESIGN.md) and on shipping both a per-brand raw export and a single-fetch full-corpus file.
