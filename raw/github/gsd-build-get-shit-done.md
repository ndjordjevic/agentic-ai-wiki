# gsd-build/get-shit-done

## Metadata
- Stars: 57,187
- Primary language: JavaScript
- Default branch: main
- Latest release: v1.38.3 (2026-04-22)
- License: MIT
- Homepage: (none)
- Fetched: 2026-04-25
- Final URL: https://github.com/gsd-build/get-shit-done

## Description
A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae, Qwen Code, Cline, and CodeBuddy. Solves context rot — the quality degradation that happens as Claude fills its context window.

## README

<div align="center">

# GET SHIT DONE

**A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae, Qwen Code, Cline, and CodeBuddy.**

**Solves context rot — the quality degradation that happens as Claude fills its context window.**

</div>

### Why It Was Built

Built by TÂCHES, a solo developer who wanted AI coding without enterprise theater. The complexity is in the system, not the workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work.

GSD gives Claude everything it needs to do the work *and* verify it.

### Getting Started

```bash
npx get-shit-done-cc@latest
```

The installer prompts for:
1. **Runtime** — Claude Code, OpenCode, Gemini, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae, Qwen Code, CodeBuddy, Cline, or all
2. **Location** — Global (all projects) or local (current project only)

Verify with `/gsd-help` (Claude Code / Gemini / Copilot / etc.) or `$gsd-help` (Codex).

**Non-interactive install examples:**
```bash
npx get-shit-done-cc --claude --global   # Install to ~/.claude/
npx get-shit-done-cc --copilot --global  # Install to ~/.github/
npx get-shit-done-cc --all --global      # Install to all runtimes
```

**Recommended:** Run Claude Code with `claude --dangerously-skip-permissions` for frictionless automation.

### How It Works

#### 1. Initialize Project
```
/gsd-new-project
```
One command, one flow:
1. **Questions** — Asks until it understands your idea completely
2. **Research** — Spawns parallel agents to investigate the domain
3. **Requirements** — Extracts what's v1, v2, and out of scope
4. **Roadmap** — Creates phases mapped to requirements

**Produces:** `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `.planning/research/`, `CLAUDE.md`

#### 2. Discuss Phase
```
/gsd-discuss-phase 1
```
Captures implementation preferences before planning. Identifies gray areas based on what's being built (layout, API format, error handling, etc.). Produces `{phase}-CONTEXT.md` and `{phase}-DISCUSSION-LOG.md`.

#### 3. Plan Phase
```
/gsd-plan-phase 1
```
Deep research into the problem space, then generates a ranked plan of milestones with dependency analysis. Produces `{phase}-RESEARCH.md` and `{phase}-{N}-PLAN.md`.

#### 4. Execute Phase
```
/gsd-next
```
Executes the next planned milestone. Invokes parallel agents, runs post-execution verification with a Nyquist validator. Fails loudly on quality gates.

#### 5. Verify Work
```
/gsd-verify-phase 1
```
Spawns a strict verification agent that checks every requirement is met, every edge case is handled, and every test passes. Produces `{phase}-VERIFICATION.md`.

### v1.37.0 Highlights
- **Spiking & sketching** — `/gsd-spike` runs 2–5 focused experiments; `/gsd-sketch` produces interactive HTML mockup variants
- **Agent size-budget enforcement** — Tiered line-count limits (XL: 1,600 / Large: 1,000 / Default: 500) keep agent prompts lean
- **Shared boilerplate extraction** — Mandatory-initial-read logic extracted to reference files, reducing duplication

---

## Docs

### Architecture (docs/ARCHITECTURE.md)

# GSD Architecture

## System Overview

GSD is a meta-prompting layer that sits between you and an AI coding tool. Commands in `commands/` (or `skills/` for newer formats) are markdown files with XML prompt templates. When you invoke `/gsd-plan-phase 1`, Claude reads that markdown file and executes the embedded workflow.

## Design Principles

- **Context engineering over chat:** Every agent prompt is carefully sized and structured. XML formatting separates instructions from data.
- **State-first architecture:** All project state lives in `.planning/` as plain files. Agents read state at start, write updates at end.
- **Fail loudly:** Quality gates (Nyquist validation, schema drift detection, security enforcement) block progress rather than silently degrade.
- **Subagent orchestration:** Heavy workflows spawn parallel subagents (research, planning, verification) rather than doing everything in one long context.

## Component Architecture

```
gsd-build/get-shit-done/
├── commands/           # Markdown command files (legacy Claude Code format)
├── get-shit-done/      # Core source tree
│   ├── bin/            # Installer and CLI entry points
│   ├── contexts/       # Reusable context modules (injected into prompts)
│   ├── references/     # Reference files (shared boilerplate)
│   ├── templates/      # Scaffolding templates
│   └── workflows/      # Core workflow definitions
├── agents/             # 33 specialized sub-agent definitions
├── hooks/              # Claude Code hook scripts (compiled to hooks/dist/)
├── docs/               # User documentation
├── sdk/                # GSD SDK (queryable codebase intelligence)
└── scripts/            # Build and maintenance scripts
```

## Agent Model

GSD ships 33 specialized agents under `agents/`:
- **Research:** `gsd-advisor-researcher`, `gsd-ai-researcher`, `gsd-domain-researcher`, `gsd-phase-researcher`, `gsd-project-researcher`
- **Planning:** `gsd-planner`, `gsd-roadmapper`, `gsd-plan-checker`, `gsd-executor`
- **Quality:** `gsd-verifier`, `gsd-nyquist-auditor`, `gsd-eval-auditor`, `gsd-eval-planner`, `gsd-security-auditor`
- **Code:** `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-debugger`, `gsd-debug-session-manager`, `gsd-integration-checker`
- **UI:** `gsd-ui-auditor`, `gsd-ui-checker`, `gsd-ui-researcher`
- **Docs:** `gsd-doc-classifier`, `gsd-doc-synthesizer`, `gsd-doc-verifier`, `gsd-doc-writer`
- **Analysis:** `gsd-assumptions-analyzer`, `gsd-codebase-mapper`, `gsd-pattern-mapper`, `gsd-framework-selector`
- **Other:** `gsd-intel-updater`, `gsd-research-synthesizer`, `gsd-user-profiler`

## Hook System

Hooks run automatically via Claude Code's hook mechanism:
- **Context monitor hook:** Tracks context window fill; warns at configurable thresholds
- **Workflow guard hook:** Optional; blocks execution of workflow steps out of sequence
- **Read-before-edit guard:** Enforces reading files before editing (v1.32)
- **Commit-docs guard:** Prevents committing planning docs to source (v1.32)
- **Community hooks:** Opt-in additional hooks from the community (v1.32)

## File System Layout (runtime state)

```
.planning/
├── PROJECT.md          # Project vision and constraints
├── REQUIREMENTS.md     # Scoped requirements (REQ-XX IDs)
├── ROADMAP.md          # Phase breakdown with status
├── STATE.md            # Current position, decisions, metrics
├── config.json         # Workflow configuration
├── research/           # Domain research artifacts
├── {phase}-CONTEXT.md  # Per-phase discussion output
├── {phase}-RESEARCH.md # Per-phase research output
├── {phase}-{N}-PLAN.md # Per-phase milestone plans
└── {phase}-VERIFICATION.md  # Verification results
```

---

### Features Summary (docs/FEATURES.md — highlights)

**Core workflow features:**
1. **Project Initialization** (`/gsd-new-project`) — adaptive questioning, parallel research agents, requirements extraction, roadmap generation
2. **Phase Discussion** (`/gsd-discuss-phase`) — gray-area identification, decision capture before planning
3. **UI Design Contract** (`/gsd-ui-phase`) — frontend spec generation
4. **Phase Planning** (`/gsd-plan-phase`) — domain research + milestone breakdown + plan verification
5. **Phase Execution** (`/gsd-next`) — milestone execution with post-execution verification
6. **Work Verification** (`/gsd-verify-phase`) — strict requirements coverage check

**Quality assurance:**
- **Nyquist Validation** — ensures verification frequency matches implementation complexity
- **Plan Checking** — validates plans before execution
- **Schema Drift Detection** (v1.31) — flags ORM changes missing migrations
- **Security Enforcement** (v1.31) — ASVS-anchored threat model verification
- **Scope Reduction Detection** (v1.31) — prevents silent requirement dropping
- **Cross-Phase Regression Gate** — blocks phases from breaking prior verified work
- **Requirements Coverage Gate** — ensures all REQ-XX IDs are addressed

**Context engineering:**
- **Context Window Monitoring** — hook-based tracking of context fill percentage
- **Session Management** — state save/restore for long projects
- **Multi-Agent Orchestration** — parallel subagent spawning with size-budget enforcement
- **Model Profiles** — `quality`, `balanced`, `budget`, `adaptive`, `inherit` presets
- **Context-Window-Aware Prompt Thinning** (v1.36) — reduces prompt size near context limit
- **Persistent Context Threads** (v1.27) — long-running context strands across phases

**Advanced features:**
- **Spike Command** (v1.37) — time-boxed technical experiments with Given/When/Then verdicts
- **Sketch Command** (v1.37) — interactive HTML mockup generation
- **Plan Bounce** (v1.36) — external plan validation script integration
- **Cross-AI Execution Delegation** (v1.36) — delegate execution to another AI tool
- **GSD SDK** (v1.30) — queryable codebase intelligence layer
- **Global Learnings Store** (v1.34) — persistent cross-project knowledge
- **Safe Undo** (v1.34) — rollback execution steps
- **TDD Pipeline Mode** (v1.36) — test-driven development workflow
- **Workspace Support** — multi-repo isolated workspaces (`/gsd-new-workspace`)

---

### Configuration (docs/CONFIGURATION.md — key settings)

Config stored in `.planning/config.json`, managed via `/gsd-settings`.

**Key settings:**
| Setting | Default | Description |
|---------|---------|-------------|
| `mode` | `interactive` | `yolo` auto-approves; `interactive` confirms at each step |
| `granularity` | `standard` | `coarse` (3–5 phases), `standard` (5–8), `fine` (8–12) |
| `model_profile` | `balanced` | `quality`/`balanced`/`budget`/`adaptive`/`inherit` |
| `workflow.research` | `true` | Enable domain research step |
| `workflow.plan_check` | `true` | Enable plan checker before execution |
| `workflow.verifier` | `true` | Enable post-execution verifier |
| `workflow.nyquist_validation` | `true` | Enable Nyquist quality gate |
| `workflow.tdd_mode` | `false` | Test-driven development pipeline |
| `parallelization.enabled` | `true` | Enable parallel subagent spawning |
| `parallelization.max_concurrent_agents` | `3` | Parallel agent limit |
| `context_window` | `200000` | Context window size in tokens |
| `response_language` | `null` | Language for all agent responses |

**Integration settings (via `/gsd-settings-integrations`):**
- `brave_search` — Brave Search API key for web research
- `firecrawl` — Firecrawl API key for deep-crawl scraping
- `exa_search` — Exa Search API key for semantic search

---

### Commands Summary (docs/COMMANDS.md — key commands)

**Core workflow:**
| Command | Purpose |
|---------|---------|
| `/gsd-new-project [--auto @file.md]` | Initialize project from scratch |
| `/gsd-discuss-phase [N] [--all\|--auto\|--batch\|--power]` | Capture phase decisions |
| `/gsd-plan-phase [N] [--skip-research\|--validate\|--bounce]` | Research + plan a phase |
| `/gsd-next [--skip-verify\|--auto]` | Execute next milestone |
| `/gsd-verify-phase [N]` | Verify phase requirements |
| `/gsd-ui-phase [N]` | Generate UI design contract |

**Advanced workflow:**
| Command | Purpose |
|---------|---------|
| `/gsd-spike <topic>` | Time-boxed technical experiment |
| `/gsd-sketch <question>` | Interactive HTML mockup variants |
| `/gsd-map-codebase` | Analyze existing codebase for brownfield projects |
| `/gsd-plan-review-convergence N` | Cross-AI plan review loop |
| `/gsd-new-workspace --name X --repos r1,r2` | Multi-repo isolated workspace |
| `/gsd-autonomous [--to N\|--interactive]` | Fully autonomous execution |

**Maintenance:**
| Command | Purpose |
|---------|---------|
| `/gsd-settings` | Manage workflow toggles |
| `/gsd-settings-integrations` | Manage API keys |
| `/gsd-update` | Update GSD to latest version |
| `/gsd-debug [--diagnose]` | Debug GSD state |
| `/gsd-stats` | Project statistics dashboard |
| `/gsd-help` | Command reference |

---

## Top-level structure

```
gsd-build/get-shit-done/
├── .base64scanignore   # Security scan ignore file
├── .clinerules         # Cline runtime install target
├── .github/            # CI/CD workflows (skip)
├── .gitignore
├── .plans/             # Internal planning artifacts
├── .release-monitor.sh # Release automation script
├── .secretscanignore   # Secret scan ignore file
├── CHANGELOG.md        # Version history
├── CONTRIBUTING.md     # Contribution guide
├── LICENSE             # MIT
├── README.md           # Main documentation (multilingual: en, pt-BR, zh-CN, ja-JP, ko-KR)
├── SECURITY.md         # Security policy
├── VERSIONING.md       # Versioning policy
├── agents/             # 33 specialized sub-agent markdown definitions
├── assets/             # Terminal SVG and other assets
├── bin/                # Installer entry points (install.js, lib/)
├── commands/           # Legacy Claude Code command format
├── docs/               # User documentation
│   ├── AGENTS.md       # Agent instruction file
│   ├── ARCHITECTURE.md # System architecture
│   ├── BETA.md         # Beta features
│   ├── CLI-TOOLS.md    # CLI tools reference
│   ├── COMMANDS.md     # Command reference
│   ├── CONFIGURATION.md # Configuration schema
│   ├── FEATURES.md     # Feature reference (118KB — comprehensive)
│   ├── INVENTORY.md    # Component inventory
│   ├── README.md       # Docs index
│   ├── USER-GUIDE.md   # End-user workflow guide
│   ├── context-monitor.md
│   ├── manual-update.md
│   ├── skills/         # Skills discovery contract
│   ├── superpowers/    # Superpower feature docs
│   └── workflow-discuss-mode.md
├── get-shit-done/      # Core source tree
│   ├── bin/            # SDK CLI entry points
│   ├── contexts/       # Reusable context modules
│   ├── references/     # Shared boilerplate reference files
│   ├── templates/      # Scaffolding templates
│   └── workflows/      # Core workflow markdown definitions
├── hooks/              # Hook sources (compiled to hooks/dist/)
├── package.json        # npm package: get-shit-done-cc
├── scripts/            # Build and release scripts
├── sdk/                # GSD SDK source
├── tests/              # Test suite (vitest)
└── tsconfig.json       # TypeScript config
```
