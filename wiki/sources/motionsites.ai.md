---
type: source
source_url: https://motionsites.ai/
tags:
  - ai-design-prompts
  - landing-page-templates
  - animated-backgrounds
  - prompt-library
  - no-code-website-builder
related:
  - bolt.new
product: motionsites
detail_level: standard
created: 2026-06-16
updated: 2026-06-16
---

MotionSites is a curated, paid library of copy-paste AI design prompts — hero sections, full landing pages, animated backgrounds, and gradients — intended for use inside AI website builders (e.g. [[bolt.new|Bolt.new]]) rather than a framework or SDK. It's relevant to this wiki as an example of "prompt as product": instead of shipping code, the product packages reusable natural-language prompts that an AI builder executes to generate UI.

_All claims below are sourced from ../../raw/web/motionsites.ai.md unless otherwise noted._

## What it does

MotionSites gives designers and builders one-click access to prompt templates that produce hero sections, full landing pages, animated gradients, and reusable UI sections inside AI website builders. Prompts are organized into three browsable libraries: Sections, Backgrounds, and Gradients, plus a members-only Templates area for complete website templates assembled from those prompts.

## Key features

- **Sections library** — described as "The #1 Most Powerful Sections Prompt Library," covering portfolio sections, error pages, feature blocks, cards/carousels, forms, pricing layouts, testimonials, dashboards, footers, and CTAs.
- **Backgrounds library** — handcrafted animated background/motion video assets (e.g. "Aurora Drift," "Sunset Bloom," "Cosmic Drift," "Neon Pulse"), updated daily.
- **Gradients library** — a curated collection of animated gradients for use in the same prompt-driven workflow.
- Each asset is tagged **"Copy"** (free to grab) or **"Premium"** (subscription-gated), and some templates reference Bolt.new integration for direct deployment.

## Architecture and concepts

The product is not a code library or API — it is a content library of natural-language prompts and copyable asset URLs (background videos hosted on Supabase/CloudFront) that a separate AI website builder consumes to generate a page. There is no companion open-source repository; the asset pipeline and prompt authoring are closed.

## Main APIs

Not applicable — there is no SDK or API. The unit of reuse is a prompt or asset URL that a user pastes into an external AI builder's interface.

## When to use

Useful for builders who want fast, visually polished landing pages from an AI website generator without writing prompts from scratch — pay for the curated library instead of iterating on prompt wording. Less relevant for teams building agentic systems or needing programmatic/API-driven website generation.

## Ecosystem

MotionSites is the consumer/template-library counterpart to **Design Rocket** (designrocket.io), a sibling platform from the same team that teaches AI-powered design skills ("Master AI-powered design, Start Learning for Free"). Pricing runs through yearly or lifetime "Go Unlimited" / "Power" tiers (with Parity Deals regional discounts observed), positioned as a low-cost alternative to agency design work.
