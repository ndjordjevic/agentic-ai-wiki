---
type: source
category: "Design & UI generation"
source_url: https://github.com/pbakaus/impeccable
tags:
  - agent-skills
  - frontend-design
  - design-md
  - anti-patterns
  - design-hooks
  - live-mode
  - multi-harness
  - design-detector
related:
  - anthropics-skills
  - voltagent-awesome-design-md
  - designmd.cc
  - open-design.ai
  - stitch.withgoogle.com
  - skills.sh
  - forrestchang-andrej-karpathy-skills
  - claudemarketplaces.com
  - SnailSploit-Claude-Red
  - using-claude-code-unreasonable-effectiveness-html
product: impeccable
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Impeccable (44K+ stars, Apache 2.0, latest release Skill 3.9.1) is Paul Bakaus's design language for AI coding agents — one skill with 23 slash commands, live browser iteration, 45 deterministic anti-pattern detector rules, and provider-native design hooks for Cursor, Claude Code, Codex, and GitHub Copilot. It evolved from Anthropic's `frontend-design` skill into a full harness-agnostic design system: `/impeccable init` writes `PRODUCT.md` and `DESIGN.md`, commands like `audit`, `polish`, `critique`, and `live` give agents a shared design vocabulary, and `npx impeccable detect` runs the same rules in CI without an LLM.

_All claims below are sourced from ../../raw/github/pbakaus-impeccable.md unless otherwise noted._

## What it does

Impeccable ships design guidance as an installable Agent Skill plus a standalone CLI. The single `/impeccable` skill exposes 23 commands covering the full design workflow: `init` (one-time setup writing `PRODUCT.md` and `DESIGN.md`), `shape`/`craft` (plan-then-build), `critique` (UX review), `audit` (a11y/performance/responsive checks), `polish`/`distill`/`bolder`/`quieter` (refinement), `animate`/`colorize`/`typeset`/`layout` (targeted fixes), `harden`/`onboard`/`clarify`/`adapt`/`optimize`, and `live` (visual variant mode in the browser). A config-driven build factory in `scripts/lib/transformers/` compiles `skill/SKILL.src.md` into provider-specific formats for 12+ harnesses (Cursor, Claude Code, Codex, Gemini CLI, GitHub Copilot, Grok Build, OpenCode, Pi, Kiro, Trae, Rovo Dev, Qoder). The design hook runs the deterministic detector on UI file edits — Cursor blocks bad writes pre-tool-use; Claude Code, Copilot, and Codex surface findings post-edit.

## Installation

Recommended path from any project root:

```bash
npx impeccable install
```

The installer detects harness folders (`~/.claude`, `~/.cursor`, `.agents`, etc.), lets you choose providers and project vs global scope, and installs both the skill payload and hook manifests. Flags: `--providers=claude,codex,cursor`, `--scope=project|global`, `--no-hooks`. Refresh with `npx impeccable update`. Alternatives: git submodule + `npx impeccable link`, Claude Code plugin marketplace (`/plugin marketplace add pbakaus/impeccable`), Grok Build plugin, ZIP download from impeccable.style, or manual `dist/` copy per provider.

After install, run `/impeccable init` inside your coding tool. Codex users must approve the project hook via `/hooks` after each install or update.

## Key features

- **23 design commands** behind one `/impeccable` skill — `pin audit` creates standalone `/audit` shortcuts.
- **45 deterministic detector rules** in `cli/engine/detect-antipatterns.mjs` — AI slop (purple gradients, Inter overuse, side-tab borders, bounce easing, icon-tile stacks) plus quality checks (line length, touch targets, heading skips). No LLM, no API key.
- **Provider-native design hooks** for Claude Code (`.claude/settings.json`), Cursor (`.cursor/hooks.json`, pre-edit block), Codex (`.codex/hooks.json`), GitHub Copilot (`.github/hooks/impeccable.json`).
- **Live mode** (`/impeccable live`) — visual variant iteration in the browser with session state under `.impeccable/live/`.
- **PRODUCT.md + DESIGN.md setup** — `init` distinguishes brand (marketing) vs product (app UI) surfaces and writes shared design context every command reads.
- **Standalone CLI** — `npx impeccable detect src/`, `--json` for CI, inline `impeccable-disable` waivers, shared `.impeccable/config.json` detector config with hooks.
- **Chrome browser extension** — same detector rules as CLI and site overlay.
- **12+ harness support** via config-driven provider transformers; HARNESSES.md tracks per-harness frontmatter and hook capabilities.

## Architecture

Source-first monorepo (Bun, ESM, Astro site). `skill/` holds `SKILL.src.md` plus `reference/` (23 command docs), `scripts/`, and `agents/` (including Codex asset-producer subagent). `scripts/lib/transformers/providers.js` defines one config entry per harness; `bun run build` generates `dist/` without syncing tracked harness folders, `bun run build:release` syncs `.claude/`, `.cursor/`, `.agents/`, etc. The anti-pattern engine (`cli/engine/detect-antipatterns.mjs`) feeds three consumers: CLI, browser overlay (`detect-antipatterns-browser.js`), and Chrome extension — all regenerated together on rule changes. Marketing site at `site/` deploys to Cloudflare Pages (impeccable.style). Tests span Bun unit tests, Node jsdom fixture suite, opt-in live-e2e against framework dev servers, and LLM-backed skill-behavior tests for the Setup flow.

## Example usage

```bash
# Install and initialize
npx impeccable install
# Then in your coding agent:
/impeccable init
/impeccable audit the header
/impeccable polish settings
/impeccable live hero section

# CI without an agent
npx impeccable detect src/ --json
npx impeccable ignores add-value overused-font Inter --reason "Brand font"
```

Pin frequently used commands: `/impeccable pin audit` → `/audit`.

## Maintenance status

44,388 stars, 2,533 forks, pushed 2026-07-08, default branch `main`, latest release Skill 3.9.1 (2026-07-01), Apache 2.0, homepage impeccable.style, npm package `impeccable` v3.2.0. Issue-first contribution policy for outside contributors. `.github/workflows/sync-generated-output.yml` auto-commits generated harness output after source changes land on `main`.
