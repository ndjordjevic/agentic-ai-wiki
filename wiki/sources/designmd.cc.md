---
type: source
category: "Design & UI generation"
source_url: https://designmd.cc/
companion_urls:
  - https://github.com/adityarajdigital/designmd
raw_files:
  - ../../raw/web/designmd.cc.md
  - ../../raw/github/adityarajdigital-designmd.md
tags:
  - design-md
  - design-tokens
  - live-dom-extraction
  - cssom-measurement
  - agent-ui
  - cli-tool
  - design-systems
related:
  - voltagent-awesome-design-md
  - open-design.ai
  - stitch.withgoogle.com
  - pbakaus-impeccable
product: designmd.cc
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

DesignMD is a free web tool and CLI (`@designmdcc/cli`) that measures a live production website's DOM and CSSOM — not a screenshot — and generates a portable `DESIGN.md` spec with real CSS variables, typography, spacing scale, breakpoints, and interaction states, purpose-built as project-root context for coding agents like Claude Code, Cursor, and GitHub Copilot.

_All claims below are sourced from ../../raw/web/designmd.cc.md unless otherwise noted._

## What it does

Paste any URL into designmd.cc, or run `npx @designmdcc/cli <url> > DESIGN.md`, and DesignMD opens the page in a headless browser to extract a measured design specification in roughly 12 seconds — colors, typography, spacing scale, CSS variables, responsive breakpoints, interaction states, and component patterns. As of this ingest the platform has generated 5,121+ `DESIGN.md` files. A companion benchmarks catalog (`designmd.cc/benchmarks`) hosts 56 pre-generated sites across 13 categories for browsing without running an extraction.

## Key features

- **Live DOM/CSSOM measurement, not screenshots or guesses** — colors from computed-style sampling, typography from the cascade, breakpoints from live `@media` rule enumeration, hover/focus states from CSSOM pseudo-class traversal ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).
- **Three access paths**: web UI (5 free analyses/day, no signup), zero-install CLI (`npx @designmdcc/cli <url>`), and a pre-generated benchmarks catalog.
- **CLI flags** — `--out=PATH` to write to file, `--json` for token-only extraction (skips the LLM formatting step entirely, free and instant, does not count against the rate quota), `--force` to bypass cache and re-measure, `--quiet` to suppress stderr progress ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).
- **Self-hosting override** via `DESIGNMD_API` environment variable to point the CLI at a regional or internal endpoint ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).
- **Distinct exit codes** (`0` success, `1` user error, `2` transient/retry, `3` network error) so scripts and agents can branch on failure mode ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).

## Architecture

The public GitHub repo is explicitly scoped as the "public developer surface" — CLI source, sample `DESIGN.md` outputs, an AI-workflow integration guide, FAQ, and UI screenshots. It excludes the actual extraction pipeline, browser instrumentation, LLM prompts/synthesis logic, server internals, rate-limiting, caching, and auth — those remain proprietary to the hosted service at designmd.cc ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)). The measurement flow is `URL → live browser measurement → structured tokens → DESIGN.md → AI agent`; the LLM stage is described as a formatter over measured data, not a source of invented values ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).

## Installation

```bash
npx @designmdcc/cli stripe.com > DESIGN.md
# or, for repeat use:
npm install -g @designmdcc/cli
dmd stripe.com > DESIGN.md
```

Requires Node 18+. No account, config, or API key needed for anonymous use ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).

## Example usage

```bash
dmd stripe.com > ./design/stripe.md          # pipe into a project file
dmd https://linear.app | pbcopy               # send to clipboard
dmd vercel.com --json | jq '.colors'          # token-only, no LLM call
DESIGNMD_API=https://my-designmd.internal dmd notion.so   # self-hosted endpoint
```

For Claude Code, the README recommends adding to `CLAUDE.md`: *"When building any UI in this project, read @DESIGN.md before generating code. Use the colors, typography, and spacing from that file exactly — do not invent brand values."* Cursor projects add an equivalent instruction to `.cursor/rules` ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).

## When to use

Reach for DesignMD when a coding agent needs to rebuild or match a specific brand's real visual system rather than inventing plausible-looking values — e.g. cloning a competitor's UI patterns, prototyping against a known design language, or giving an agent ground-truth tokens instead of a screenshot that loses structural information. The site frames three failure modes it avoids: agents hallucinating colors/fonts from a prompt, hand-documented token sheets going stale within weeks, and screenshot-to-vision-model pipelines losing structural intent. Re-run with `--force` when the source site redesigns, since the spec is a point-in-time snapshot.

## Maintenance status

Companion repo `adityarajdigital/designmd`: 49 stars, 5 forks, MIT license (repo materials only — production pipeline is proprietary), latest release `v0.1.2` (2026-05-20), default branch `main`, built by Aditya Raj (adityaraj.info). Contribution is scoped to bug reports, benchmark suggestions, and documentation/example PRs — not core pipeline changes ([../../raw/github/adityarajdigital-designmd.md](../../raw/github/adityarajdigital-designmd.md)).

## Ecosystem

DesignMD's output format sits in the same `DESIGN.md`-as-project-context niche popularized by Google Stitch and cataloged by [[voltagent-awesome-design-md]] and [[open-design.ai]] — where those two focus on distributing pre-made brand `DESIGN.md` files, DesignMD is a live, on-demand extractor: point it at any URL and get a measured spec in ~12 seconds rather than picking from a curated library. The README explicitly targets the same coding-agent audience (Claude Code, Cursor, Windsurf, Aider, Copilot, Cline, Continue) and documents per-tool integration patterns for each.
