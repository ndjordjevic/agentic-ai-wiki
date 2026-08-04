---
type: source
category: "Design & UI generation"
source_url: https://impeccable.style/
companion_urls:
  - https://github.com/pbakaus/impeccable
raw_files:
  - ../../raw/web/impeccable.style.md
  - ../../raw/github/pbakaus-impeccable.md
tags:
  - design-vocabulary
  - ai-slop-detection
  - live-mode
  - design-context
  - multi-harness
  - anti-pattern-detector
  - design-hooks
  - browser-extension
related:
  - pbakaus-impeccable
  - anthropics-skills
  - designmd.cc
  - stitch.withgoogle.com
product: impeccable.style
detail_level: standard
created: 2026-08-04
updated: 2026-08-04
---

Impeccable's public site (impeccable.style) is the documentation and marketing front for [[pbakaus-impeccable]], Paul Bakaus's design vocabulary skill for AI coding agents. Where the GitHub repo captures source code and build internals, the site is the day-to-day reference: command docs, the Slop catalog of AI-generated UI anti-patterns, the Live Mode workflow, and tutorials for getting a project set up end to end.

_All claims below are sourced from ../../raw/web/impeccable.style.md unless otherwise noted._

## What it does

Impeccable installs as a single `/impeccable` skill exposing 23 commands — `init`, `shape`, `critique`, `audit`, `polish`, `bolder`/`quieter`, `distill`, `harden`, `onboard`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`, `clarify`, `adapt`, `optimize`, and `live` — plus a standalone CLI and Chrome extension that run 64 deterministic anti-pattern detection rules with no LLM call required. The site organizes the workflow around four stages: set context (`init`), iterate (targeted commands or Live Mode), pre-ship polish (`audit`/`clarify`/`harden`), and maintain (`extract`/`document`) as the design system drifts.

## Key features

- **Design Context** (`/docs/context`) — `PRODUCT.md` (platform, users, purpose, brand) and `DESIGN.md` (colors, type, components, radii) give every command shared project memory, classified into four visitor modes: Persuade, Operate, Read, Experience.
- **Live Mode** (`/live-mode`) — pick an element in a running dev server, drop a comment or stroke, and three production-quality variants swap in via the framework's HMR (Vite, Next.js, SvelteKit, Astro, Nuxt, Bun, plain HTML); accepting a variant rewrites the source file and consolidates CSS into the real stylesheet, not inline.
- **Slop catalog** (`/slop`) — 64 anti-pattern rules across 9 categories (design-system drift, visual details, typography, color & contrast, layout & space, motion, copy, imagery, general quality), enforced via CLI, browser extension, or the `critique` command.
- **23-command vocabulary** shared across every supported harness, letting an agent be told "polish the checkout form" instead of a freeform prompt.
- **Platform-aware auditing** — `PRODUCT.md` platform axis (`web`/`ios`/`android`/`adaptive`) drives native-specific accessibility and conformance checks. (../../raw/github/pbakaus-impeccable.md)

## Architecture

The site (Astro, deployed to Cloudflare Pages at impeccable.style) is generated from the same source-first monorepo as the skill: `skill/SKILL.src.md` and `skill/reference/` compile through a config-driven provider factory (`scripts/lib/transformers/providers.js`) into per-harness formats for 14+ tools (Claude Code, Cursor, Codex CLI, Gemini CLI, GitHub Copilot, Grok Build, OpenCode, Pi, Kiro, Trae, Rovo Dev, Qoder, Mistral Vibe, Google Antigravity). The anti-pattern engine (`cli/engine/detect-antipatterns.mjs`) feeds the CLI, the site's detector overlay, and the Chrome extension from one rule set — the site's `llms.txt` and docs pages describe the product surface; the repo is where that surface is actually built. (../../raw/github/pbakaus-impeccable.md)

## Installation

```bash
npx impeccable install
```

detects installed harness folders, lets you pick providers and project vs. global scope, and — on Claude Code, Cursor, Codex, GitHub Copilot, and Grok Build — installs the provider-native design hook alongside the skill. Refresh with `npx impeccable update`. Alternatives documented on the site and in the repo: git submodule + `npx impeccable link`, the Claude Code plugin marketplace (`/plugin marketplace add pbakaus/impeccable`), a Grok Build plugin install, ZIP download from impeccable.style, or manual `dist/` copies per provider. (../../raw/github/pbakaus-impeccable.md)

## Example usage

```bash
npx impeccable install
# then inside the coding agent:
/impeccable init
/impeccable audit the header
/impeccable live hero section
/impeccable polish settings

# CLI without an agent
npx impeccable detect src/ --json
```

(../../raw/github/pbakaus-impeccable.md)

## When to use

Reach for Impeccable when an AI coding agent is doing frontend work and keeps reproducing the same generic tells — purple gradients, Inter everywhere, cards nested in cards, oversized icon tiles. The site's `designing` workflow page positions it as the layer between "describe what you want" and shipped UI: `init` captures brand/product context once, then every subsequent command (`polish`, `critique`, `audit`, `live`) reads that context instead of re-deriving it. It explicitly warns against stacking Impeccable with Anthropic's own `frontend-design` skill, over-pinning commands, or skipping `init`.

## Maintenance status

54,629 stars, default branch `main`, latest release Extension 1.3.1 (2026-07-30), Apache 2.0, npm package `impeccable`. Issue-first contribution policy for outside contributors; `.github/workflows/sync-generated-output.yml` auto-commits generated per-harness output when source changes land on `main`. (../../raw/github/pbakaus-impeccable.md)

## Ecosystem

Impeccable started from Anthropic's [[anthropics-skills]] `frontend-design` skill and extends it into a full harness-agnostic design system. It sits alongside other design-context tools in the wiki like [[designmd.cc]] (DESIGN.md via live DOM extraction) and Google's [[stitch.withgoogle.com]] DESIGN.md format, which Impeccable's `document` command targets directly for portability.

## Documentation

The docs site (`/docs`) organizes reference material into Concepts (Design Context, New work, Config and ignores, Detector CLI, Design hooks, Doctor) and Command Reference (one page per slash command). `llms.txt` at the domain root enumerates the full site structure — Start Here, Tutorials, Concepts and Reference, Command Reference, Developer Resources, and Optional (case studies, the public design system, the detector lab) — as the canonical machine-readable index of the site.
