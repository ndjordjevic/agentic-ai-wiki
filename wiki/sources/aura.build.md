---
type: source
category: "Design & UI generation"
source_url: https://www.aura.build/
tags:
  - ai-website-builder
  - landing-pages
  - design-mode
  - design-md
  - html-export
  - figma-export
  - prompt-credits
  - cms
related:
  - lovable.dev
  - bolt.new
  - open-design.ai
  - designmd.cc
  - voltagent-awesome-design-md
  - duply.ai
  - Nutlope-inspo
  - ui-skills.com
product: aura
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Aura (aura.build) is an AI website and landing-page builder aimed at polished marketing/UI craft: prompt with pro templates and `@` references, refine in Advanced Design Mode, then publish (CMS + SEO) or export real HTML/Tailwind/vanilla JS and Figma. It positions itself in the **design-to-HTML** lane versus [[lovable.dev]] (full-stack MVPs), Figma Make (Figma prototypes), and v0 (React/Vercel).

_All claims below are sourced from ../../raw/web/aura.build.md unless otherwise noted._

## What it does

Users generate landing pages and multi-page sites from prompts, optionally grounded in templates, components, snippets, DESIGN.md systems, screenshots, or Figma imports. After generation, Design Mode provides layers, auto breakpoints, measurement overlays, component replacement, and code snippets. Sites publish to friendly subdomains (`.or.build`), support custom domains and CMS, and export portable HTML or Figma layers — no proprietary runtime lock-in per product docs.

## Key features

- **@ references** — attach templates/components/snippets/prior iterations (up to ~100k characters of context).
- **Advanced Design Mode** — visual editor with 1,400+ replaceable components (docs); marketing comparison cites 2,800+ components / 5,000+ templates / 30,000+ assets.
- **Image tools** — Ideogram, Nano Banana, Flux 2 Pro; 20,000+ curated assets; image-to-HTML.
- **Multi-page + CMS** — element-to-page links, page transitions, collections/items by plan.
- **DESIGN.md systems** — generate from a site/template or browse public systems as reusable prompt context.
- **Predictable usage** — 1 prompt = 1 credit across models; Free / Pro ($12.50/mo annual) / Max / Ultra / Elite tiers; 3-day trial (20 prompts).
- **SEO publish tab** — titles/descriptions/keywords/favicons/page overrides; published domains serve robots.txt, sitemap.xml, llms.txt.

## Architecture and concepts

Hosted SaaS web app (not an open-source CLI). Output stack is standard HTML + Tailwind CSS + vanilla JavaScript. Docs live under `/learn/*` (Introduction is the hub); `llms.txt` lists primary surfaces (create, pricing, learn, components, assets, skills, design-systems, comparison). No companion GitHub repo discovered on landing or llms.txt.

## Main APIs

No public developer API documented in this ingest. Primary surfaces are the create prompt UI, Design Mode, Publish/SEO popover, and export (HTML / Figma console paste). Skills and DESIGN.md galleries are first-class site sections for prompt context.

## When to use

Choose Aura when the job is a **premium marketing/landing page** with visual iteration, CMS, and clean HTML/Figma handoff. Choose [[lovable.dev]] or [[bolt.new]] when you need full-stack app scaffolding; choose [[open-design.ai]] when you want a local, agent-CLI-driven design studio instead of a hosted builder.

## Ecosystem

Competes/compares with Lovable, Figma Make, v0, Framer, Webflow, Bolt, and other AI site builders (dedicated comparison page). DESIGN.md workflow overlaps [[designmd.cc]], [[voltagent-awesome-design-md]], and [[duply.ai]]. Design-taste / anti-slop needs may still want coding-agent skills like [[Nutlope-inspo]] or [[ui-skills.com]] alongside Aura.
