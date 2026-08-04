# pbakaus/impeccable

## Metadata
- Stars: 54629
- Primary language: JavaScript
- Default branch: main
- Latest release: Extension 1.3.1 (2026-07-30)
- License: Apache License 2.0
- Homepage: https://impeccable.style
- Fetched: 2026-08-04
- Final URL: https://github.com/pbakaus/impeccable

## Description
The design language that makes your AI harness better at design.

## README

# Impeccable

Design guidance for AI coding agents. 1 skill, 23 commands, live browser iteration, and 59 deterministic detector rules for AI-generated frontend design.

> **Quick start:** From your project root, run `npx impeccable install`, then run `/impeccable init` inside your AI coding tool. Full docs: [impeccable.style](https://impeccable.style).

## Why Impeccable?

Anthropic's [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) was the first widely-used design skill for Claude. Impeccable started from there.

Every model trained on the same SaaS templates. Skip the guidance and you get the same handful of tells on every project: Inter for everything, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile above every heading.

Impeccable adds:
- **One setup flow.** `/impeccable init` writes `PRODUCT.md` and offers `DESIGN.md`, so later commands know the audience, brand/product lane, voice, anti-references, colors, type, and components.
- **23 commands.** A shared design vocabulary with your AI: `polish`, `audit`, `critique`, `distill`, `animate`, `bolder`, `quieter`, and more.
- **59 deterministic detector rules** plus LLM-only critique checks. The CLI and browser extension run the deterministic rules with no LLM and no API key.

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

#### Usage Examples

```
/impeccable audit blog           # Audit blog hub + post pages
/impeccable critique landing     # UX design review
/impeccable polish settings      # Final pass before shipping
/impeccable harden checkout      # Add error handling + edge cases
```

Or use `/impeccable` directly with a description:
```
/impeccable redo this hero section
```

### Anti-Patterns

The skill includes explicit guidance on what to avoid:

- Don't use overused fonts (Arial, Inter, system defaults)
- Don't use gray text on colored backgrounds
- Don't use pure black/gray (always tint)
- Don't wrap everything in cards or nest cards inside cards
- Don't use bounce/elastic easing (feels dated)

## See It In Action

Visit [the Neo Mirai case study](https://impeccable.style/cases/neo-mirai) to see a before/after case study of a real project transformed with Impeccable commands.

## Installation

### Option 1: CLI installer (Recommended)

From the root of your project, run:

```bash
npx impeccable install
```

This shows the harness folders it detected (for example `~/.claude`, `~/.codex`, `~/.grok`, or project-local `.cursor`), lets you keep the detected set or customize providers, then asks whether to install into the current project or globally. Use `--providers=claude,codex,cursor,grok` and `--scope=project|global` to skip those choices in scripts. On Claude Code, Cursor, Codex, GitHub Copilot, and Grok Build, it also installs the provider-native hook manifest for the current project. Works with Cursor, Claude Code, Gemini CLI, Codex CLI, Grok Build, and every other supported tool. Reload your harness afterward.

To refresh an existing install, run:

```bash
npx impeccable update
```

Codex users should open `/hooks` after install or update and approve the project hook when prompted. Codex tracks trust by hook definition, so updates that change `.codex/hooks.json` can require approval again. Grok Build users need project folder trust (`/hooks-trust` or launch with `--trust`) before `.grok/hooks/` scripts run.

### Option 2: Git Submodule

For teams that want to keep Impeccable vendored and updated through Git, add this repo as a submodule and link the compiled provider build into your harness folders:

```bash
git submodule add https://github.com/pbakaus/impeccable .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
git add .gitmodules .impeccable .claude .cursor
git commit -m "Add Impeccable skills"
```

Use the providers your project needs, for example `claude`, `cursor`, `gemini`, `codex`, `github`, `grok`, `opencode`, `pi`, `qoder`, `trae`, `trae-cn`, `rovo-dev`, or `vibe`. The command links individual skill folders from `.impeccable/dist/universal/` and leaves existing real skill directories untouched unless you pass `--force`.

To update later:

```bash
git submodule update --remote .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
```

### Option 3: Plugin install

**Claude Code:**
```bash
/plugin marketplace add pbakaus/impeccable
```

> Claude Code only. After adding the marketplace, open `/plugin` and install Impeccable from the list.

**Grok Build:**
```bash
grok plugin install pbakaus/impeccable#plugin --trust
```

> Grok Build only. The `#plugin` suffix installs the slim plugin package (skills, agents, and hooks) instead of the full monorepo. Then run `/impeccable init` in a Grok session. Project-scoped installs via `npx impeccable install --providers=grok` also work and write `.grok/skills/` plus `.grok/hooks/impeccable.json`.

### Option 4: Download from Website

Visit [impeccable.style](https://impeccable.style), download the ZIP for your tool, and extract to your project.

### Option 5: Copy from Repository

**Cursor:**
```bash
cp -r dist/cursor/.cursor your-project/
```

> **Note:** Cursor skills require setup:
> 1. Switch to Nightly channel in Cursor Settings → Beta
> 2. Enable Agent Skills in Cursor Settings → Rules
>
> [Learn more about Cursor skills](https://cursor.com/docs/context/skills)

**Claude Code:**
```bash
# Project-specific
cp -r dist/claude-code/.claude your-project/

# Or global (applies to all projects)
cp -r dist/claude-code/.claude/* ~/.claude/
```

**OpenCode:**
```bash
cp -r dist/opencode/.opencode your-project/
```

**Pi:**
```bash
cp -r dist/pi/.pi your-project/
```

**Gemini CLI:**
```bash
cp -r dist/gemini/.gemini your-project/
```

> **Note:** Gemini CLI skills require setup:
> 1. Install preview version: `npm i -g @google/gemini-cli@preview`
> 2. Run `/settings` and enable "Skills"
> 3. Run `/skills list` to verify installation
>
> [Learn more about Gemini CLI skills](https://geminicli.com/docs/cli/skills/)

**Codex CLI:**
```bash
# Project-local
cp -r dist/agents/.agents your-project/
mkdir -p your-project/.codex
cp dist/codex/.codex/hooks.json your-project/.codex/hooks.json

# Or install the skill user-wide. Copy .codex/hooks.json into each project
# where you want the design hook to run.
mkdir -p ~/.agents/skills
cp -r dist/agents/.agents/skills/* ~/.agents/skills/
```

> The asset-producer subagent ships nested inside the skill's own `agents/` folder, which Codex auto-discovers. No separate `.codex/agents/` copy is needed. The hook is project-local because Codex discovers hooks from `.codex/hooks.json` next to trusted project config.

**GitHub Copilot:**
```bash
cp -r dist/github/.github your-project/
```

**Trae:**
```bash
# Trae China (domestic version)
cp -r dist/trae/.trae-cn/skills/* ~/.trae-cn/skills/

# Trae International
cp -r dist/trae/.trae/skills/* ~/.trae/skills/
```

> **Note:** Trae has two versions with different config directories:
> - **Trae China**: `~/.trae-cn/skills/`
> - **Trae International**: `~/.trae/skills/`
>
> After copying, restart Trae IDE to activate the skills.

**Rovo Dev:**
```bash
# Project-specific
cp -r dist/rovo-dev/.rovodev your-project/

# Or global (applies to all projects)
cp -r dist/rovo-dev/.rovodev/skills/* ~/.rovodev/skills/
```

**Qoder:**
```bash
# Project-specific
cp -r dist/qoder/.qoder your-project/

# Or global (applies to all projects)
cp -r dist/qoder/.qoder/skills/* ~/.qoder/skills/
```

**Mistral Vibe:**
```bash
# Project-specific
cp -r dist/vibe/.vibe your-project/

# Or global (applies to all projects)
cp -r dist/vibe/.vibe/skills/* ~/.vibe/skills/
```

**Grok Build:**
```bash
# Project-specific
cp -r dist/grok/.grok your-project/

# Or global (applies to all projects)
cp -r dist/grok/.grok/skills/* ~/.grok/skills/
```

> Prefer `npx impeccable install --providers=grok` or `grok plugin install pbakaus/impeccable#plugin --trust` so the design hook installs too. Project hooks need `/hooks-trust` (or `--trust`) once per folder.

**Google Antigravity:**
```bash
# Project-specific
cp -r dist/antigravity/.agent your-project/

# Or global (applies to all projects)
mkdir -p ~/.gemini/config/skills
cp -r dist/antigravity/.agent/skills/* ~/.gemini/config/skills/
```

## Usage

Once installed, every command runs through the single `/impeccable` skill:

```
/impeccable audit        # Find issues
/impeccable polish       # Final cleanup
/impeccable distill      # Remove complexity
/impeccable critique     # Full design review
```

Type `/impeccable` alone to see the full command list.

Most commands accept an optional argument to focus on a specific area:

```
/impeccable audit the header
/impeccable polish the checkout form
```

If you reach for one command often, pin it with `/impeccable pin audit` to get `/audit` as a standalone shortcut.

**Note:** Codex uses skills here, not `/prompts:` commands. Open `/skills` or type `$impeccable`. Repo-local installs live in `.agents/skills/`; user-wide installs live in `~/.agents/skills/`. GitHub Copilot uses `.github/skills/`. Restart the tool if a newly installed skill does not appear.

## Keeping `.impeccable` out of git

As you run commands, Impeccable writes working files under `.impeccable/`: critique and polish screenshots, live-mode session and preview state, runtime caches, and per-developer config. Most of it is ephemeral and should not be committed, while a few files are shared project artifacts that belong in the repo. Add this block to your project's `.gitignore`:

```gitignore
# impeccable-ignore-start
# Ephemeral output, runtime state, and per-dev overrides.
# Unanchored: .impeccable may sit at the repo root or under a nested
# workspace (apps/web/.impeccable/...); anchored patterns would miss it.
# Shared artifacts stay tracked: config.json, live/config.json,
# design.json, critique/*.md.
.impeccable/config.local.json
.impeccable/hook.cache.json
.impeccable/hook.pending.json
.impeccable/*.png
.impeccable/live/server.json
.impeccable/live/sessions/
.impeccable/live/previews/
.impeccable/live/annotations/
.impeccable/live/cache/
.impeccable/live/manual-edit-apply-transaction.json
.impeccable/live/manual-edit-events.jsonl
.impeccable/live/manual-edit-evidence/
.impeccable/live/pending-manual-edits.json
.impeccable/live/deferred-svelte-component-accepts.json
.impeccable/live/*.png
# impeccable-ignore-end
```

The block is wrapped in `# impeccable-ignore-start` / `# impeccable-ignore-end` markers so you can recognize and refresh it later. Patterns are unanchored on purpose: in a monorepo the active project (and its `.impeccable/` directory) often lives under a nested workspace path like `apps/web/`, and a root-anchored pattern would miss it.

**Keep these tracked** (they are shared project artifacts, do not add them to `.gitignore`):

- `.impeccable/config.json` (unified shared config)
- `.impeccable/live/config.json` (live-mode framework wiring)
- `.impeccable/design.json` (shared design spec)
- `.impeccable/critique/*.md` (review reports)

If an ephemeral file (a screenshot, `config.local.json`) was committed before you added the block, `.gitignore` will not untrack it automatically. Run `git rm --cached <path>` to stop tracking it without deleting your local copy.

## Design hook

On Claude Code, GitHub Copilot, Codex, Cursor, and Grok Build, `npx impeccable install` and `npx impeccable update` install a provider-native hook manifest along with the skill payload. The hook runs the Impeccable design detector on direct UI file edits and surfaces findings back into the agent flow. Claude Code, GitHub Copilot, Codex, and Grok Build surface findings after the edit (and run a deeper pass on Stop where supported). Cursor blocks bad proposed writes before they land.

Installed hook surfaces:

- Claude Code: `.claude/settings.local.json` (gitignored, machine-local) runs `${CLAUDE_PROJECT_DIR}/.claude/skills/impeccable/scripts/hook.mjs`. A hook moved into the shared `settings.json` is honored in place.
- GitHub Copilot: `.github/hooks/impeccable.json` (committed, shared by the Copilot CLI and the cloud agent) runs `.github/skills/impeccable/scripts/hook.mjs`. The Copilot CLI activates it once the file is on the repository's default branch and the folder is trusted.
- Cursor: `.cursor/hooks.json` runs `.cursor/skills/impeccable/scripts/hook-before-edit.mjs`.
- Codex: `.codex/hooks.json` runs `.agents/skills/impeccable/scripts/hook.mjs`.

The installer preserves unrelated hook entries and settings. If a hook manifest is malformed, install/update aborts by default; rerun with `--force` to back up the malformed file as `.bak` and replace it.

On an interactive `install`/`update`, Impeccable explains the hook and offers to install it (default yes). Your choice is remembered per-developer in the gitignored `.impeccable/config.local.json`, so you are not asked again; `--no-hooks` skips it for that run without recording anything. Hook lifecycle settings live under the `hook` key of `.impeccable/config.json`; detector ignores live under `detector`, shared by `/impeccable hooks` and `npx impeccable detect`.

For debugging, set `hook.auditLog` in `.impeccable/config.json` to a path (or the legacy `IMPECCABLE_HOOK_LOG` env var) to write one NDJSON line per hook invocation. Leave it unset for normal use.

Codex requires one platform step that Impeccable cannot safely skip: open `/hooks` after install or update and approve the project hook. There is no Codex marketplace/plugin install flow for this hook.

Full hook docs: [impeccable.style/docs/hooks](https://impeccable.style/docs/hooks).

Manual copy commands are fallback/debug instructions. The normal path is:

```bash
npx impeccable install
npx impeccable update
```

## CLI

Impeccable includes a standalone CLI for detecting anti-patterns without an AI harness:

```bash
npx impeccable detect src/                   # scan a directory
npx impeccable detect index.html             # scan an HTML file
npx impeccable detect https://example.com    # scan a URL (Puppeteer)
npx impeccable detect --json .               # CI-friendly JSON output
npx impeccable detect --no-config src/       # raw scan, ignoring project config/context
npx impeccable ignores list                  # show detector ignores
npx impeccable ignores add-file "src/legacy/**"
npx impeccable ignores add-value overused-font Inter --reason "Brand font"
```

The detector catches 59 deterministic issues across AI slop (side-tab borders, purple gradients, bounce easing, dark glows) and general design quality (line length, cramped padding, small touch targets, skipped headings, and more).

By default, `detect` respects the same `.impeccable/config.json` and `.impeccable/config.local.json` detector config as the design hook: `detector.ignoreRules`, `detector.ignoreFiles`, `detector.ignoreValues`, and `detector.designSystem.enabled`. Hook lifecycle settings such as `hook.enabled` only affect automatic hook execution.

For a waiver that should travel with one file instead of the repo config, add an inline comment in the file: `<!-- impeccable-disable overused-font: exported brand doc -->`. The marker works in any comment syntax, scopes to the whole file (or one line with `impeccable-disable-line` / `impeccable-disable-next-line`), and is bypassed by `--no-inline-ignores` or `--no-config`.

Full detector docs: [impeccable.style/docs/detector](https://impeccable.style/docs/detector).

## Supported Tools

- [Cursor](https://cursor.com)
- [Claude Code](https://claude.ai/code)
- [GitHub Copilot](https://github.com/features/copilot)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [Codex CLI](https://github.com/openai/codex)
- [Grok Build](https://x.ai/cli)
- [OpenCode](https://opencode.ai)
- [Pi](https://pi.dev)
- [Kiro](https://kiro.dev)
- [Trae](https://trae.ai)
- [Rovo Dev](https://www.atlassian.com/software/rovo)
- [Qoder](https://qoder.com)
- [Mistral Vibe](https://docs.mistral.ai/vibe/code/overview)
- [Google Antigravity](https://antigravity.google)

## Community & Ecosystem

Join the community and ecosystem conversations:

- GitHub Discussions: file bugs, request features, and help newcomers.
- [Impeccable on npm](https://www.npmjs.com/package/impeccable): grab the CLI, follow releases, and star the package.
- Follow @pbakaus on Twitter for release notes, sample lint reports, and video highlights of new rules.

## Contributing

See [DEVELOP.md](docs/DEVELOP.md) for contributor guidelines and build instructions.

## License

Apache 2.0. See [LICENSE](LICENSE).

---

Created by [Paul Bakaus](https://www.paulbakaus.com)

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
license: License info (optional)
compatibility: Environment requirements (optional)
---
```

**Frontmatter fields** (based on Agent Skills spec):
- `name` (required): Skill identifier (1-64 chars, lowercase/numbers/hyphens)
- `description` (required): What the skill provides (1-1024 chars)
- `user-invocable` (optional): Boolean -- if `true`, the skill can be invoked as a slash command
- `argument-hint` (optional): Hint shown during autocomplete
- `license` (optional): License/attribution info
- `compatibility` (optional): Environment requirements
- `metadata` (optional): Arbitrary key-value pairs
- `allowed-tools` (optional, experimental): Pre-approved tools list

**Body placeholders** (replaced per-provider during build):
- `{{model}}` -- Provider-specific model name (e.g., "Claude", "Gemini", "GPT")
- `{{config_file}}` -- Provider-specific config file (e.g., "CLAUDE.md", ".cursorrules")
- `{{ask_instruction}}` -- How to ask the user for clarification
- `{{command_prefix}}` -- Slash command prefix (`/` for most, `$` for Codex)
- `{{available_commands}}` -- Comma-separated list of user-invocable commands

## Building

Developer Lab URLs: no-index visual harnesses and internal inspectors live under `/labs/<subject>`. Stable public references such as `/docs` and `/design-system` stay top-level.

Prerequisites: Bun (fast JavaScript runtime and package manager); no external dependencies required.

```bash
bun run build          # source-first build
bun run clean          # clean dist folder
bun run rebuild
```

### docs/HARNESSES.md (excerpt)

# Harness Skills Capabilities Reference

Source of truth for what each AI coding harness supports in terms of agent skills. Used to inform provider configs in `scripts/lib/transformers/providers.js`.

Last verified: 2026-04-28 (subagent landscape spot-checked 2026-06-28; Mistral Vibe row verified 2026-07-16; Grok Build row verified 2026-07-21)

## Official Documentation

| Harness | Docs URL |
|---------|----------|
| Claude Code | https://code.claude.com/docs/en/skills |
| Cursor | https://cursor.com/docs/context/skills |
| Gemini CLI | https://geminicli.com/docs/cli/skills/ |
| Codex CLI | https://developers.openai.com/codex/skills |
| GitHub Copilot (Agents) | https://code.visualstudio.com/docs/copilot/customization/agent-skills |
| Kiro | https://kiro.dev/docs/skills/ |
| OpenCode | https://opencode.ai/docs/skills/ |
| Pi | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md |
| Qoder | https://docs.qoder.com/extensions/skills |
| Trae | TBD (no official skills docs found yet) |
| Rovo Dev | https://support.atlassian.com/rovo/docs/extend-rovo-dev-cli-with-agent-skills |
| Mistral Vibe | https://docs.mistral.ai/vibe/code/cli/skills |
| Grok Build | https://docs.x.ai/build/features/skills-plugins-marketplaces |
| Antigravity | https://antigravity.google/docs/skills |

## Spec Compliance

All harnesses follow the [Agent Skills specification](https://agentskills.io/specification) to varying degrees. The spec defines these frontmatter fields: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.

Provider-specific extensions beyond the spec: `user-invocable`, `argument-hint`, `disable-model-invocation`, `allowed-tools` (extended syntax), `model`, `effort`, `context`, `agent`, `hooks`, `subtask`, `mcp`.

## Hook surface used by Impeccable

| Harness | Edit hook | Startup hook | Manifest location | Notes |
|---------|:---------:|:------------:|-------------------|-------|
| Claude Code | Yes (`PostToolUse`) | No | `.claude/settings.json` | Project-local settings entry installed by `npx impeccable skills install/update`. Runs `.claude/skills/impeccable/scripts/hook.mjs`. |
| Codex CLI | Yes (`PostToolUse`) | No | `.codex/hooks.json` | Project-local manifest installed with the `.agents/skills/impeccable` payload. Runs `.agents/skills/impeccable/scripts/hook.mjs` from the git root. Requires normal `/hooks` trust approval. |
| Cursor | Yes (`preToolUse`) | No | `.cursor/hooks.json` | Project-level manifest installed with `.cursor/skills/impeccable`. Runs `hook-before-edit.mjs` to block bad proposed writes before they land. Reloads on save; restart Cursor if hooks do not pick up. |
| Grok Build | Yes (`PostToolUse`) | No | `.grok/hooks/impeccable.json` | Project-local manifest installed with `.grok/skills/impeccable`. Claude-compatible matchers (`Edit\|Write\|MultiEdit`) alias to Grok tools. Also runs a Stop deep pass. Requires `/hooks-trust` or `--trust`. |
| All other harnesses | No | No | n/a | No documented hook surface today. Skill and commands still ship. |

## Skill Directory Structure

| Harness | Native directory | Also reads |
|---------|-----------------|------------|
| Claude Code | `.claude/skills/` | - |
| Cursor | `.cursor/skills/` | `.agents/skills/`, `.claude/skills/` |
| Gemini CLI | `.gemini/skills/` | `.agents/skills/` |
| Codex CLI | `.agents/skills/` (primary) | - |
| GitHub Copilot | `.github/skills/` | `.agents/skills/`, `.claude/skills/` |

### docs/STYLE.md (excerpt)

# STYLE.md

Editorial brief for impeccable.design. Read this before writing or editing user-facing copy: the homepage, sub-pages, command editorials, tutorials, and READMEs.

The bar: **for every paragraph, point to the sentence that makes it specifically yours.** If you can't, the paragraph is AI by default, even if a human typed it.

## Principles

1. Open with the reader's wrong belief, your strongest claim, or the example. No "in this guide", no "let's dive in".
2. Take a position someone could disagree with.
3. Name names. Use numbers. Real competitors, real customer names, real version numbers, real file paths, real benchmarks.
4. Verbs lead. Nouns follow. Imperative is fine. Active voice.
5. Vary sentence length on purpose. Long, long, short.
6. Prose carries the load; structure supports it. Bullets are for parallel options.
7. Plain words. Technical terms only when something specifically rests on them.
8. Allow ungrammatical fragments for rhythm.
9. Respect the reader's competence.
10. Read it aloud. Fix anything you stumble over.
11. Concrete over comprehensive. Trade coverage for momentum.
12. Close by handing off the next move. Don't summarize.

## Denylist

The build's `validateProse` step (in `scripts/build.js`) fails the build on banned words/phrases, grouped by category: stolen-engineer diction (`load-bearing`, `highest-leverage`, `biggest unlock`), internal jargon leaking out (`reflex defaults`, `collapses into monoculture`, `data-driven`), marketing voice (`seamless`, `robust`, `elevate`, `empower`, `underscore`, `pivotal`, `tapestry`), verbs (`delve`/`delves`/`delved`/`delving`), throat-clearing openers (`in today's...`, `gone are the days`, `whether you're...`, `let's dive in`), closers (`in summary`, `in conclusion`), and transitions (`moreover`, `furthermore`).

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
├── docs/               # DEVELOP.md, HARNESSES.md, STYLE.md, adr-live-variant-mode.md, LIVE-REWRITE-PLAN.md, openai-plugin-submission.md
├── demos/              # Demo projects
├── tests/               # Bun + Node test suite, antipattern fixtures, live-e2e, skill-behavior
├── plugin/             # Generated Claude Code plugin marketplace artifacts
├── dist/               # Generated provider output (gitignored in dev; synced on release)
├── skills-lock.json    # Lockfile pinning installed skill versions
├── .claude/             # Tracked generated Claude Code harness output
├── .claude-plugin/      # Claude Code plugin marketplace manifest
├── .cursor/             # Tracked generated Cursor harness output (skills + hooks.json)
├── .codex/              # Tracked generated Codex hooks manifest
├── .agents/             # Tracked generated Codex primary skills directory
├── .gemini/             # Tracked generated Gemini CLI harness output
├── .grok/                # Tracked generated Grok Build harness output (skills + hooks)
├── .impeccable/          # Impeccable's own dogfooded config/design context
├── .kiro/                # Tracked generated Kiro harness output
├── .opencode/            # Tracked generated OpenCode harness output
├── .pi/                  # Tracked generated Pi harness output
├── .qoder/               # Tracked generated Qoder harness output
├── .rovodev/             # Tracked generated Rovo Dev harness output
├── .trae/ / .trae-cn/    # Tracked generated Trae International / China harness output
├── .vibe/                # Tracked generated Mistral Vibe harness output
├── .github/             # CI workflows, generated Copilot skills/hooks
├── AGENTS.md           # Contributor guide for agents
├── CLAUDE.md           # Claude-specific project context
├── DESIGN.md           # Project design spec (dogfooding)
├── PRODUCT.md          # Product context (dogfooding)
├── NOTICE.md            # Attribution/notice file
├── README.npm.md        # npm-package-specific README variant
├── biome.json            # Linter/formatter config
├── bun.lock              # Bun lockfile
├── package.json        # npm package; bin: impeccable CLI
└── astro.config.mjs    # Site build config
```

**Annotated notes:**
- `skill/reference/` contains 23 command reference files (init.md, audit.md, polish.md, live.md, etc.)
- Root harness folders (`.claude/`, `.cursor/`, `.gemini/`, `.grok/`, `.kiro/`, `.opencode/`, `.pi/`, `.qoder/`, `.rovodev/`, `.trae/`, `.trae-cn/`, `.vibe/`, etc.) are generated distribution artifacts tracked for direct repo installs — the provider roster has grown substantially since the initial ingest (Kiro, OpenCode, Pi, Qoder, Rovo Dev, Trae, Mistral Vibe, Antigravity all added)
- `bun run build:release` syncs generated provider output; `.github/workflows/sync-generated-output.yml` auto-commits on main
- Issue-first contribution policy for outside contributors
