# OthmanAdi/planning-with-files

## Metadata
- Stars: 22015
- Primary language: Python
- Default branch: master
- Latest release: v2.41.0 (2026-05-24)
- License: MIT
- Homepage: (none)
- Fetched: 2026-05-25
- Final URL: https://github.com/OthmanAdi/planning-with-files

## Description
Claude Code skill implementing Manus-style persistent markdown planning — the workflow pattern behind the $2B acquisition.

## README

<div align="center">
<img src="media/banner.png" alt="planning-with-files" width="100%">
</div>

# Planning with Files

> **Work like Manus** — the AI agent company Meta acquired for **$2 billion**.

[![Benchmark](https://img.shields.io/badge/Benchmark-96.7%25_pass_rate-brightgreen)](docs/evals.md)
[![A/B Verified](https://img.shields.io/badge/A%2FB_Blind-3%2F3_wins-brightgreen)](docs/evals.md)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1)](https://getskillcheck.com)
[![Security Verified](https://img.shields.io/badge/Security-Audited_%26_Fixed_v2.21.0-blue)](docs/evals.md)
[![Version](https://img.shields.io/badge/version-2.41.0-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Claude Code plugin that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage — the exact pattern that made Manus worth billions.

## Quick Install

```bash
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g
```

Available in 6 languages: English, Arabic (ar), German (de), Spanish (es), Chinese Simplified (zh), Chinese Traditional (zht).

Works with Claude Code, Cursor, Codex, Gemini CLI, and 40+ agents supporting the Agent Skills spec.

## Why This Skill?

On December 29, 2025, Meta acquired Manus for $2 billion. In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering**.

> "Markdown is my 'working memory' on disk. Since I process information iteratively and my active context has limits, Markdown files serve as scratch pads for notes, checkpoints for progress, building blocks for final deliverables."
> — Manus AI

## The Problem

Claude Code (and most AI agents) suffer from:

- **Volatile memory** — TodoWrite tool disappears on context reset
- **Goal drift** — After 50+ tool calls, original goals get forgotten
- **Hidden errors** — Failures aren't tracked, so the same mistakes repeat
- **Context stuffing** — Everything crammed into context instead of stored

## The Solution: 3-File Pattern

For every complex task, create THREE files:

```
task_plan.md      → Track phases and progress
findings.md       → Store research and findings
progress.md       → Session log and test results
```

### The Core Principle

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## The Manus Principles

| Principle | Implementation |
|-----------|----------------|
| Filesystem as memory | Store in files, not context |
| Attention manipulation | Re-read plan before decisions (hooks) |
| Error persistence | Log failures in plan file |
| Goal tracking | Checkboxes show progress |
| Completion verification | Stop hook checks all phases |

## Usage

Once installed, the AI agent will:

1. **Ask for your task** if no description is provided
2. **Create `task_plan.md`, `findings.md`, and `progress.md`** in your project directory
3. **Re-read plan** before major decisions (via PreToolUse hook)
4. **Remind you** to update status after file writes (via PostToolUse hook)
5. **Store findings** in `findings.md` instead of stuffing context
6. **Log errors** for future reference
7. **Verify completion** before stopping (via Stop hook)

Invoke with:
- `/planning-with-files:plan` - Type `/plan` to find in autocomplete (v2.11.0+)
- `/planning-with-files:status` - Type `/plan:status` for progress at a glance (v2.15.0+)
- `/planning-with-files:start` - Original start command

## Benchmark Results

Formally evaluated using Anthropic's skill-creator framework (v2.22.0). 10 parallel subagents, 5 task types, 30 objectively verifiable assertions, 3 blind A/B comparisons.

| Test | with_skill | without_skill |
|------|-----------|---------------|
| Pass rate (30 assertions) | **96.7%** (29/30) | 6.7% (2/30) |
| 3-file pattern followed | 5/5 evals | 0/5 evals |
| Blind A/B wins | **3/3 (100%)** | 0/3 |
| Avg rubric score | **10.0/10** | 6.8/10 |

## Key Rules

1. **Create Plan First** — Never start without `task_plan.md`
2. **The 2-Action Rule** — Save findings after every 2 view/browser operations
3. **Log ALL Errors** — They help avoid repetition
4. **Never Repeat Failures** — Track attempts, mutate approach

## Supported IDEs (17+ Platforms)

### Enhanced Support (hooks + lifecycle automation)

| IDE | Integration |
|-----|-------------|
| Claude Code | Plugin + SKILL.md + Hooks |
| Cursor | Skills + hooks.json |
| GitHub Copilot | Hooks (incl. errorOccurred) |
| Mastra Code | Skills + Hooks |
| Gemini CLI | Skills + Hooks |
| Kiro | Agent Skills |
| Codex | Skills + Hooks |
| Hermes Agent | Skill + Project Plugin |
| CodeBuddy | Skills + Hooks |
| FactoryAI Droid | Skills + Hooks |
| OpenCode | Skills + Custom session storage |

### Standard Agent Skills Support

| IDE | Skill Discovery Path |
|-----|---------------------|
| Continue | `.continue/skills/` |
| Pi Agent | `.pi/skills/` |
| OpenClaw | `.openclaw/skills/` |
| Antigravity | `.agent/skills/` |
| Kilocode | `.kilocode/skills/` |
| AdaL CLI (Sylph AI) | `.adal/skills/` |

## When to Use

**Use this pattern for:**
- Multi-step tasks (3+ steps)
- Research tasks
- Building/creating projects
- Tasks spanning many tool calls

**Skip for:**
- Simple questions
- Single-file edits
- Quick lookups

## Notable Features (Recent Versions)

- **v2.41.0**: Windows exec-bit test skip + attestation-locking docs
- **v2.40.0**: Slug-mode resolution fixes + perf cache + KV-cache hygiene
- **v2.39.0**: Pi Coding Agent full hook parity extension + Codex hooks flag fix
- **v2.38.0**: Claude Code turn-loop integration (`/plan-goal`, `/plan-loop`, PreCompact hook)
- **v2.37.0**: Hash attestation (`/plan-attest` + SHA-256 tamper detection)
- **v2.36.0**: Parallel plan isolation (`.planning/YYYY-MM-DD-slug/`), Codex session isolation
- **v2.35.1**: Shebang portability fix (`/usr/bin/env bash`)

## Community

- 22,015 stars, 1,954 forks
- Multiple community forks: devis (interview workflow), multi-manus-planning, plan-cascade (multi-level orchestration)
- Used in ClarityFinance AI, CCteam-creator, claude-harness projects
- Bilingual skill hub (buzhangsan/skill-manager) indexing 31,000+ skills includes planning-with-files

## Acknowledgments

- **Manus AI** — For pioneering context engineering patterns
- **Anthropic** — For Claude Code, Agent Skills, and the Plugin system
- Based on [Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## Docs

Key documentation files in `docs/`:
- `installation.md` — All installation methods
- `quickstart.md` — 5-step quick start guide
- `workflow.md` — Detailed workflow documentation
- `evals.md` — Full benchmark methodology and results
- `article.md` — Technical write-up
- `attestation-locking.md` — Plan attestation and locking
- `troubleshooting.md` — Common issues
- Platform guides: `cursor.md`, `copilot.md`, `gemini.md`, `codex.md`, `opencode.md`, `mastra.md`, `kiro.md`, `hermes.md`, `codebuddy.md`, `factory.md`, `pi-agent.md`, `openclaw.md`, `continue.md`, `boxlite.md`, `adal.md`, `antigravity.md`, `kilocode.md`, `windows.md`

## Top-level structure

```
.claude-plugin/         — Plugin manifest and marketplace metadata
.codebuddy/             — CodeBuddy IDE skill adapter
.codex/                 — Codex CLI skills + lifecycle hooks
.continue/              — Continue.dev skills + .prompt files
.cursor/                — Cursor skills + hooks.json
.factory/               — FactoryAI Droid skills + hooks (v2.26.0+)
.gemini/                — Gemini CLI skills + hooks (5 lifecycle events)
.github/                — GitHub Copilot hooks config and scripts
.gitignore
.hermes/                — Hermes Agent skill adapter
.kiro/                  — Kiro Agent Skills (v2.27.0+)
.mastracode/            — Mastra Code skills + hooks
.opencode/              — OpenCode skills with custom session storage
.pi/                    — Pi Agent skills (npm package)
AGENTS.md               — Agent reference card (commit rules, release checklist, 19-file version bump scope)
CHANGELOG.md            — Detailed version history (79970 bytes)
CITATION.cff            — Citation metadata
CONTRIBUTORS.md         — Full contributors list
LICENSE                 — MIT License
MIGRATION.md            — Migration guide
README.md               — Main documentation (30195 bytes)
commands/               — Plugin slash commands (plan, plan-ar, plan-de, plan-es, start)
docs/                   — 27 platform setup guides and documentation files
examples/               — Integration examples (BoxLite quickstart)
media/                  — Banner and media assets
scripts/                — Hook scripts: init-session.sh, check-complete.sh, set-active-plan.sh, resolve-plan-dir.sh, attest-plan.sh
skills/                 — Skill variants: planning-with-files (en), -ar, -de, -es, -zh, -zht
templates/              — Planning file templates (task_plan.md, findings.md, progress.md)
tests/                  — Test suite (130 passing + 2 pre-existing Windows exec-bit)
```
