# pbakaus/impeccable

## Metadata
- Stars: 44388
- Primary language: JavaScript
- Default branch: main
- Latest release: Skill 3.9.1 (2026-07-01)
- License: Apache License 2.0
- Homepage: https://impeccable.style
- Fetched: 2026-07-08
- Final URL: https://github.com/pbakaus/impeccable

## Description
The design language that makes your AI harness better at design.

## README

# Impeccable

Design guidance for AI coding agents. 1 skill, 23 commands, live browser iteration, and 45 deterministic detector rules for AI-generated frontend design.

> **Quick start:** From your project root, run `npx impeccable install`, then run `/impeccable init` inside your AI coding tool. Full docs: [impeccable.style](https://impeccable.style).

## Why Impeccable?

Anthropic's [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) was the first widely-used design skill for Claude. Impeccable started from there.

Every model trained on the same SaaS templates. Skip the guidance and you get the same handful of tells on every project: Inter for everything, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile above every heading.

Impeccable adds:
- **One setup flow.** `/impeccable init` writes `PRODUCT.md` and offers `DESIGN.md`, so later commands know the audience, brand/product lane, voice, anti-references, colors, type, and components.
- **23 commands.** A shared design vocabulary with your AI: `polish`, `audit`, `critique`, `distill`, `animate`, `bolder`, `quieter`, and more.
- **45 deterministic detector rules** plus LLM-only critique checks. The CLI and browser extension run the deterministic rules with no LLM and no API key.

## What's Included

### The Skill: impeccable

The skill installs as one command:

```bash
/impeccable <command> <target>
```

Start every new project with:

```bash
/impeccable init
```

`init` asks whether the surface is brand (marketing, landing, portfolio) or product (app UI, dashboard, tool), then writes design context that every later command reads.

### 23 Commands

All commands are accessed through `/impeccable`:

| Command | What it does |
|---------|--------------|
| `/impeccable craft` | Full shape-then-build flow with visual iteration |
| `/impeccable init` | One-time setup: gather design context, write PRODUCT.md and DESIGN.md, configure live mode, recommend next steps |
| `/impeccable document` | Generate root DESIGN.md from existing project code |
| `/impeccable extract` | Pull reusable components and tokens into the design system |
| `/impeccable shape` | Plan UX/UI before writing code |
| `/impeccable critique` | UX design review: hierarchy, clarity, emotional resonance |
| `/impeccable audit` | Run technical quality checks (a11y, performance, responsive) |
| `/impeccable polish` | Final pass, design system alignment, and shipping readiness |
| `/impeccable bolder` | Amplify boring designs |
| `/impeccable quieter` | Tone down overly bold designs |
| `/impeccable distill` | Strip to essence |
| `/impeccable harden` | Error handling, i18n, text overflow, edge cases |
| `/impeccable onboard` | First-run flows, empty states, activation paths |
| `/impeccable animate` | Add purposeful motion |
| `/impeccable colorize` | Introduce strategic color |
| `/impeccable typeset` | Fix font choices, hierarchy, sizing |
| `/impeccable layout` | Fix layout, spacing, visual rhythm |
| `/impeccable delight` | Add moments of joy |
| `/impeccable overdrive` | Add technically extraordinary effects |
| `/impeccable clarify` | Improve unclear UX copy |
| `/impeccable adapt` | Adapt for different devices |
| `/impeccable optimize` | Performance improvements |
| `/impeccable live` | Visual variant mode: iterate on elements in the browser |

Use `/impeccable pin <command>` to create standalone shortcuts (e.g., `pin audit` creates `/audit`).

### Anti-Patterns

The skill includes explicit guidance on what to avoid:

- Don't use overused fonts (Arial, Inter, system defaults)
- Don't use gray text on colored backgrounds
- Don't use pure black/gray (always tint)
- Don't wrap everything in cards or nest cards inside cards
- Don't use bounce/elastic easing (feels dated)

## Installation

### Option 1: CLI installer (Recommended)

```bash
npx impeccable install
npx impeccable update
```

### Option 2: Git Submodule

```bash
git submodule add https://github.com/pbakaus/impeccable .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
```

### Option 3: Plugin install

**Claude Code:** `/plugin marketplace add pbakaus/impeccable`

**Grok Build:** `grok plugin install pbakaus/impeccable --trust`

### Option 4: Download from Website

Visit [impeccable.style](https://impeccable.style), download the ZIP for your tool.

### Option 5: Copy from Repository

Provider-specific `dist/` folders for Cursor, Claude Code, Codex, Gemini CLI, GitHub Copilot, OpenCode, Pi, Trae, Rovo Dev, Qoder.

## Design hook

On Claude Code, GitHub Copilot, Codex, and Cursor, `npx impeccable install` installs a provider-native hook manifest. The hook runs the Impeccable design detector on direct UI file edits. Cursor blocks bad proposed writes before they land; Claude Code, Copilot, and Codex surface findings after the edit.

## CLI

```bash
npx impeccable detect src/                   # scan a directory
npx impeccable detect index.html             # scan an HTML file
npx impeccable detect https://example.com    # scan a URL (Puppeteer)
npx impeccable detect --json .               # CI-friendly JSON output
npx impeccable ignores list                  # show detector ignores
```

The detector catches 45 deterministic issues across AI slop (side-tab borders, purple gradients, bounce easing, dark glows) and general design quality (line length, cramped padding, small touch targets, skipped headings).

## Supported Tools

Cursor, Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, Grok Build, OpenCode, Pi, Kiro, Trae, Rovo Dev, Qoder.

## License

Apache 2.0.

## Docs

### docs/DEVELOP.md (excerpt)

# Developer Guide

## Architecture

The skill at `skill/` is transformed into provider-specific formats by a config-driven factory. Each provider is defined as a config object in `scripts/lib/transformers/providers.js` -- adding a new provider requires only a new config entry.

For detailed harness capabilities (which frontmatter fields each supports, placeholder systems, directory structures), see HARNESSES.md.

## Source Format

### Skill (`skill/SKILL.src.md`)

```yaml
---
name: skill-name
description: What this skill provides
argument-hint: "[target]"
user-invocable: true
---
```

**Frontmatter fields** (based on Agent Skills spec):
- `name` (required): Skill identifier (1-64 chars, lowercase/numbers/hyphens)
- `description` (required): What the skill provides (1-1024 chars)
- `user-invocable` (optional): Boolean -- if `true`, the skill can be invoked as a slash command
- `argument-hint` (optional): Hint shown during autocomplete

**Body placeholders** (replaced per-provider during build):
- `{{model}}` -- Provider-specific model name
- `{{config_file}}` -- Provider-specific config file
- `{{command_prefix}}` -- Slash command prefix

## Building

```bash
bun run build          # source-first build
bun run build:release  # release build + sync tracked harness folders
bun run rebuild
bun test tests/build.test.js
bun run test
```

### docs/HARNESSES.md (excerpt)

# Harness Skills Capabilities Reference

Source of truth for what each AI coding harness supports in terms of agent skills.

## Official Documentation

| Harness | Docs URL |
|---------|----------|
| Claude Code | https://code.claude.com/docs/en/skills |
| Cursor | https://cursor.com/docs/context/skills |
| Gemini CLI | https://geminicli.com/docs/cli/skills/ |
| Codex CLI | https://developers.openai.com/codex/skills |
| GitHub Copilot (Agents) | https://code.visualstudio.com/docs/copilot/customization/agent-skills |

## Hook surface used by Impeccable

| Harness | Edit hook | Manifest location |
|---------|:---------:|-------------------|
| Claude Code | Yes (`PostToolUse`) | `.claude/settings.json` |
| Codex CLI | Yes (`PostToolUse`) | `.codex/hooks.json` |
| Cursor | Yes (`preToolUse`) | `.cursor/hooks.json` |

## Skill Directory Structure

| Harness | Native directory | Also reads |
|---------|-----------------|------------|
| Claude Code | `.claude/skills/` | - |
| Cursor | `.cursor/skills/` | `.agents/skills/`, `.claude/skills/` |
| Gemini CLI | `.gemini/skills/` | `.agents/skills/` |
| Codex CLI | `.agents/skills/` (primary) | - |
| GitHub Copilot | `.github/skills/` | `.agents/skills/`, `.claude/skills/` |

### AGENTS.md (excerpt)

`skill/` is the source of truth for the Impeccable skill: `SKILL.src.md`, `reference/`, `scripts/`, and `agents/`. Build logic lives in `scripts/`, with provider configs in `scripts/lib/transformers/`. The CLI and anti-pattern detector live in `cli/`, the browser extension in `extension/`, the Astro website in `site/`, Cloudflare Pages Functions in `functions/`, and regression coverage in `tests/`.

`cli/engine/detect-antipatterns.mjs` is the source of truth for the rule engine. It feeds the CLI, the site overlay, the Chrome extension, and the homepage `DETECTION_COUNT`.

## Top-level structure

```
pbakaus/impeccable/
├── skill/              # Source of truth: SKILL.src.md, reference/ (23 command docs), scripts/, agents/
├── cli/                # Standalone CLI + anti-pattern detector engine (detect-antipatterns.mjs)
├── extension/          # Chrome browser extension (regenerated from cli/engine)
├── site/               # Astro marketing/docs website (impeccable.style)
├── functions/          # Cloudflare Pages Functions
├── scripts/            # Build system: provider transformers, validation, zip bundles
├── docs/               # DEVELOP.md, HARNESSES.md, STYLE.md, adr-live-variant-mode.md
├── demos/              # Demo projects
├── tests/              # Bun + Node test suite, antipattern fixtures, live-e2e, skill-behavior
├── plugin/             # Generated Claude Code plugin marketplace artifacts
├── dist/               # Generated provider output (gitignored in dev; synced on release)
├── .claude/            # Tracked generated Claude Code harness output
├── .cursor/            # Tracked generated Cursor harness output (skills + hooks.json)
├── .codex/             # Tracked generated Codex hooks manifest
├── .agents/            # Tracked generated Codex primary skills directory
├── .github/            # CI workflows, generated Copilot skills/hooks
├── AGENTS.md           # Contributor guide for agents
├── CLAUDE.md           # Claude-specific project context
├── DESIGN.md           # Project design spec (dogfooding)
├── PRODUCT.md          # Product context (dogfooding)
├── package.json        # npm package (v3.2.0); bin: impeccable CLI
└── astro.config.mjs    # Site build config
```

**Annotated notes:**
- `skill/reference/` contains 23 command reference files (init.md, audit.md, polish.md, live.md, etc.)
- Root harness folders (`.claude/`, `.cursor/`, etc.) are generated distribution artifacts tracked for direct repo installs
- `bun run build:release` syncs generated provider output; `.github/workflows/sync-generated-output.yml` auto-commits on main
- Issue-first contribution policy for outside contributors
