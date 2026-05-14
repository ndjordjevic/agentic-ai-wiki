# gsd-build/get-shit-done

## Metadata
- Stars: 62040
- Primary language: JavaScript
- Default branch: main
- Latest release: v1.42.0-rc4 (2026-05-14, pre-release)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-05-14
- Final URL: https://github.com/gsd-build/get-shit-done

## Description
A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES. Solves context rot — the quality degradation that happens as your AI fills its context window.

## README

<div align="center">

# GET SHIT DONE

**A light-weight meta-prompting, context engineering, and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more.**

**Solves context rot — the quality degradation that happens as your AI fills its context window.**

```bash
npx get-shit-done-cc@latest
```

*"If you know clearly what you want, this WILL build it for you. No bs."*

*"I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."*

*"By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."*

**Trusted by engineers at Amazon, Google, Shopify, and Webflow.**

</div>

---

## Why I Built This

I'm a solo developer. I don't write code — Claude Code does.

Other spec-driven tools exist, but they're all built for 50-person engineering orgs — sprint ceremonies, story points, stakeholder syncs, Jira workflows. I'm not that. I'm a creative person trying to build great things consistently.

So I built GSD. The complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work.

The system gives Claude everything it needs to do the work *and* verify it. I trust the workflow. It just does a good job.

— **TÂCHES**

---

## How It Works

The loop is six commands. Each one does exactly one thing.

### 1. Initialize

```bash
/gsd-new-project
```

Questions → research → requirements → roadmap. You approve it, then you're ready to build.

> **Already have code?** Run `/gsd-map-codebase` first. It analyzes your stack, architecture, and conventions so `/gsd-new-project` asks the right questions.

### 2. Discuss

```bash
/gsd-discuss-phase 1
```

Your roadmap has a sentence per phase. That's not enough to build it the way *you* imagine it. Discuss captures your decisions before anything gets planned: layouts, API shapes, error handling, data structures — whatever gray areas exist for this specific phase.

### 3. Plan

```bash
/gsd-plan-phase 1
```

Research → plan → verify, in a loop until the plans pass. Each plan is small enough to execute in a fresh context window.

### 4. Execute

```bash
/gsd-execute-phase 1
```

Plans run in parallel waves. Each executor gets a fresh 200k-token context. Each task gets its own atomic commit. Walk away, come back to completed work with a clean git history.

Your main context window stays at 30–40%. The work happens in the subagents.

### 5. Verify

```bash
/gsd-verify-work 1
```

Walk through what was built. Anything broken gets a diagnosed fix plan — ready for immediate re-execution. You don't debug manually; you just run execute again.

### 6. Repeat → Ship

```bash
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

Loop discuss → plan → execute → verify → ship until the milestone is done. Then archive, tag, and start the next one fresh.

---

## Getting Started

```bash
npx get-shit-done-cc@latest
```

The installer prompts for your runtime and whether to install globally or locally.

Install only the skills you need with `--profile=core` (six core-loop skills), `--profile=standard` (core + phase management), or the default full install.

---

## Commands

| Command | What it does |
|---------|--------------|
| `/gsd-new-project` | Questions → research → requirements → roadmap |
| `/gsd-discuss-phase [N]` | Capture implementation decisions before planning |
| `/gsd-plan-phase [N]` | Research + plan + verify |
| `/gsd-execute-phase <N>` | Execute plans in parallel waves |
| `/gsd-verify-work [N]` | Manual acceptance testing |
| `/gsd-ship [N]` | Create PR from verified phase work |
| `/gsd-progress --next` | Auto-detect and run the next step |
| `/gsd-complete-milestone` | Archive milestone and tag release |
| `/gsd-new-milestone` | Start next version |
| `/gsd:surface` | Enable/disable skill clusters at runtime without reinstall |

---

## Why It Works

Three things most AI-coding setups get wrong:

**1. Context bloat.** As a session grows, quality degrades. GSD keeps your main context clean by doing the heavy work in fresh subagent contexts.

**2. No shared memory.** GSD maintains structured artifacts that survive session boundaries: `PROJECT.md` (vision), `REQUIREMENTS.md` (scope), `ROADMAP.md` (where you're going), `STATE.md` (current position and decisions), `CONTEXT.md` (per-phase implementation decisions).

**3. No verification.** Code that "runs" isn't code that "works." GSD's verify step walks you through what was built, diagnoses failures with dedicated debug agents, and generates fix plans before you declare a phase done.

---

## Configuration

Settings live in `.planning/config.json`. Key dials:

| Setting | What it controls |
|---------|-----------------|
| `mode` | `interactive` (confirm each step) or `yolo` (auto-approve) |
| Model profiles | `quality` / `balanced` / `budget` — controls which model each agent uses |
| `workflow.research` / `plan_check` / `verifier` | Toggle quality agents |
| `parallelization.enabled` | Run independent plans simultaneously |

---

## Documentation

| Doc | What's in it |
|-----|-------------|
| [User Guide](docs/USER-GUIDE.md) | End-to-end walkthrough, install options, all runtime flags |
| [Commands](docs/COMMANDS.md) | Every command with flags and examples |
| [Configuration](docs/CONFIGURATION.md) | Full config schema, model profiles, git branching |
| [Architecture](docs/ARCHITECTURE.md) | How the multi-agent orchestration works |
| [CLI Tools](docs/CLI-TOOLS.md) | `gsd-sdk query` and programmatic SDK dispatch |
| [Features](docs/FEATURES.md) | Complete feature index |
| [Changelog](CHANGELOG.md) | What changed in each release |

## Docs

### docs/ARCHITECTURE.md (excerpt)

GSD is a **meta-prompting framework** that sits between the user and AI coding agents. It provides:

1. **Context engineering** — Structured artifacts that give the AI everything it needs per task
2. **Multi-agent orchestration** — Thin orchestrators that spawn specialized agents with fresh context windows
3. **Spec-driven development** — Requirements → research → plans → execution → verification pipeline
4. **State management** — Persistent project memory across sessions and context resets

Architecture layers:
- **Command Layer** (`commands/gsd/*.md`) — User-facing slash commands, installed per-runtime
- **Workflow Layer** (`get-shit-done/workflows/*.md`) — Orchestration logic: loads context, spawns agents, manages state
- **Agent Layer** — Fresh-context specialized agents (researchers, planners, executors, verifiers)
- **CLI Tools Layer** — `gsd-sdk query` + `gsd-tools.cjs` programmatic bridge
- **File System** (`.planning/`) — `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `config.json`, `phases/`, `research/`

**Two-stage hierarchical routing (v1.40):** Six namespace meta-skills (`gsd-workflow`, `gsd-project`, `gsd-quality`, `gsd-context`, `gsd-manage`, `gsd-ideate`) route to concrete sub-skills, reducing eager skill-listing from ~2,150 tokens to ~120 tokens per turn.

**Design principles:**
- Fresh context per agent (eliminates context rot)
- Thin orchestrators (spawn, collect, route — no heavy lifting)
- File-based state (human-readable Markdown + JSON, no server)
- Absent = enabled (missing config keys default to `true`)
- Defense in depth (plan verification, atomic commits, post-execution verification, UAT gate)

## Top-level structure

| Entry | Type | Notes |
|---|---|---|
| `commands/` | dir | User-facing slash commands (`gsd/*.md`) — installed as custom commands per runtime |
| `get-shit-done/` | dir | Workflow orchestration files (`workflows/*.md`) |
| `agents/` | dir | Specialized agent definitions |
| `sdk/` | dir | `gsd-sdk` CLI + programmatic bridge (`GSDTools/query-runtime-bridge.ts`) |
| `hooks/` | dir | Git hooks and lifecycle automation |
| `scripts/` | dir | Installer, migration, and release scripts |
| `tests/` | dir | Vitest test suite (including workflow size-budget tests) |
| `bin/` | dir | CLI entry points |
| `docs/` | dir | Full documentation (ARCHITECTURE.md, USER-GUIDE.md, COMMANDS.md, CONFIGURATION.md, FEATURES.md, INVENTORY.md, ADRs) |
| `assets/` | dir | Terminal SVG screenshots and media |
| `CLAUDE.md` | file | Agent-facing contributor guidelines; issue tracker and triage label references |
| `CONTEXT.md` | file | Single-context repo; domain docs for agent sessions |
| `CHANGELOG.md` | file | Release history |
| `package.json` | file | npm package (`get-shit-done-cc`); Node.js / JavaScript |
| `vitest.config.ts` | file | Test configuration |
| `.plans/` | dir | Internal planning artifacts (agent-written) |
| `.github/` | dir | CI workflows and PR templates |
