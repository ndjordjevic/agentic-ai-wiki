---
type: source
source_url: https://github.com/nadimtuhin/claude-token-optimizer
tags:
  - claude-code
  - token-optimization
  - claude-md
  - claudeignore
  - context-budget
  - claude-code-hooks
  - documentation-structure
  - framework-scaffolding
related:
  - how-claude-code-works-in-large-codebases
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - forrestchang-andrej-karpathy-skills
  - shareai-lab-learn-claude-code
  - getcaveman.dev
  - 6eanut-llm-wiki
  - obra-superpowers
product: claude-token-optimizer
detail_level: standard
created: 2026-07-01
updated: 2026-07-01
---

Claude Token Optimizer (`cto`) is an open-source npm CLI (499 stars, MIT) that structures a project's documentation so Claude Code loads only essential context at session start — typically ~800 tokens across four core files instead of 8,000–11,000 tokens of stale docs, session history, and task archives. It scaffolds `CLAUDE.md`, `.claudeignore`, `.claude/` support files, and `docs/learnings/` topic files; auto-detects 13 web frameworks; ships 12 Claude Code hook templates for active token monitoring and on-demand context injection; and provides maintenance commands (`measure`, `audit`, `compress`, `prune`, `diff`, `watch`) with CI-friendly JSON output.

_All claims below are sourced from ../../raw/github/nadimtuhin-claude-token-optimizer.md unless otherwise noted._

## What it does

The tool addresses Claude Code's tendency to auto-load all project documentation at session start, burning context on outdated session notes, completed task history, and archived docs before any coding begins. The author's RedwoodJS project went from ~11,000 startup tokens to ~1,300 total (~90% reduction) by restructuring docs into a tiered loading model: four essential files load at startup (~800 tokens), topic-based learnings in `docs/learnings/` load on demand (~500 tokens each), and everything in `.claude/completions/`, `.claude/sessions/archive/`, and `docs/archive/` costs zero tokens until explicitly requested via `.claudeignore` exclusion patterns.

## Installation

Three install paths, all producing the `cto` command:

```bash
# No install
npx claude-token-optimizer init

# One-line global install
curl -fsSL https://raw.githubusercontent.com/nadimtuhin/claude-token-optimizer/main/install.sh | bash

# npm global
npm install -g claude-token-optimizer
```

Run `cto measure` first to baseline current auto-loaded token cost before scaffolding.

## Key features

- **`cto init`:** Auto-detects framework from `package.json`, `requirements.txt`, `go.mod`, `composer.json`, `pom.xml`, or `Gemfile`; scaffolds optimized doc structure in ~30 seconds. Appends to existing `CLAUDE.md` without overwriting. Supports `--framework` override for 13 stacks (Express, Next.js, Vue, Nuxt, Angular, Django, Rails, NestJS, Laravel, FastAPI, Go, Spring Boot, Svelte).
- **`cto measure`:** Reports auto-loaded token breakdown; routes uninitialized projects to `init` and initialized ones to `compress`.
- **`cto audit`:** 19 structural health checks with `--fix` (auto-creates missing files, patches `.claudeignore`) and `--json` for CI (exits 1 on errors).
- **`cto compress` / `cto prune` / `cto diff`:** Deterministic CLAUDE.md compression, interactive stale-section pruning (archives, never deletes), and before/after token delta reporting.
- **`cto watch`:** Live ASCII token dashboard refreshing on file changes.
- **`cto hooks`:** Install, list, and export settings for 12 hook templates covering PreToolUse guards, UserPromptSubmit context injection from `docs/learnings/`, session snapshots, ghost-token scanning, and write-cost logging.
- **Framework examples:** 13 per-framework guides in `examples/` with top-5 critical mistakes (N+1 queries, auth issues, etc.).
- **Related:** pairs with [Claude Workflows](https://github.com/nadimtuhin/claude-workflows) — this repo optimizes what Claude knows; Workflows optimizes what Claude does.

## Architecture

The CLI is a Node.js package (`claude-token-optimizer` on npm) with `src/cli.js` routing to command modules under `src/commands/` (`init`, `measure`, `audit`, `compress`, `prune`, `diff`, `watch`, `hooks`, `update`) and shared logic in `src/lib/`. Scaffolding templates live in `templates/` including `completion-template.md`, `maintenance-guide.md`, and 12 shell hook scripts under `templates/hooks/`.

The documentation architecture it installs follows a three-tier loading model:

1. **Session-start tier** — `CLAUDE.md` plus `.claude/COMMON_MISTAKES.md`, `QUICK_START.md`, `ARCHITECTURE_MAP.md` (~800 tokens).
2. **On-demand tier** — `docs/learnings/<topic>.md` files loaded via the `user-prompt-inject-context` hook when user prompts match filenames (zero cost when not matched).
3. **Zero-cost tier** — `.claude/completions/`, `.claude/sessions/`, `docs/archive/` excluded via `.claudeignore` until explicitly requested.

Hook templates integrate at Claude Code lifecycle points: `pre-tool-token-guard` warns/blocks when auto-loaded files exceed thresholds (`CTO_WARN_TOKENS` default 2000, `CTO_BLOCK_TOKENS` default 8000); `user-prompt-inject-context` keyword-matches prompts against `docs/learnings/` filenames; `user-prompt-ghost-scanner` detects unreferenced CLAUDE.md sections consuming ghost tokens.

## Example usage

```bash
# Baseline, scaffold, verify
cto measure
cto init
cto audit --fix

# Ongoing maintenance
cto compress          # dry-run safe
cto prune             # interactive, archives stale sections
cto diff              # token savings report

# CI gate
npx claude-token-optimizer audit --json

# Install all monitoring hooks
cto hooks install --all
cto hooks settings    # pipe into ~/.claude/settings.json
```

Target project structure after `cto init`:

```
your-project/
├── CLAUDE.md
├── .claudeignore
├── .claude/
│   ├── COMMON_MISTAKES.md
│   ├── QUICK_START.md
│   ├── ARCHITECTURE_MAP.md
│   ├── completions/
│   └── sessions/
└── docs/
    ├── INDEX.md
    ├── learnings/
    └── archive/
```

## Maintenance status

- **499 GitHub stars**, 57 forks, MIT license, JavaScript primary language.
- **Default branch:** `main`. Last pushed 2026-06-28. No GitHub releases published yet; distributed via npm (`claude-token-optimizer`).
- **Active development:** CHANGELOG, CI via `.github/`, test suite under `tests/`.
- **Contributing gaps:** Rust (Actix/Axum), Phoenix, and ASP.NET Core framework examples sought.
