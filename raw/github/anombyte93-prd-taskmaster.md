# anombyte93/prd-taskmaster

## Metadata
- Stars: 4447
- Forks: 42
- Primary language: Python
- Default branch: main
- Latest release: v3.0.0 - Codification Refactor (2026-01-26 approx)
- License: MIT
- Homepage: (none)
- Last pushed: 2026-04-26
- Fetched: 2026-05-22
- Final URL: https://github.com/anombyte93/prd-taskmaster

## Description
AI-powered PRD generation for Claude Code with taskmaster integration

## README
# PRD-Taskmaster: AI-Generated Product Requirements Documents

> **Comprehensive PRD generation optimized for AI-assisted development workflows**

## What is This?

A Claude Code skill that generates **detailed, engineer-focused Product Requirements Documents (PRDs)** designed to work seamlessly with AI task breakdown tools like Taskmaster.

Think of it as your AI product manager that asks the right questions, writes comprehensive specs, and sets you up for successful implementation.

## Why You Might Want This

### The Problem

You have an idea for a feature or product, but:
- Writing comprehensive PRDs takes hours
- You're not sure what details to include
- You want to use AI task breakdown tools (like Taskmaster) but they need detailed requirements
- Vague specs lead to vague tasks, which lead to poor implementations

### The Solution

This skill:
1. **Asks 12+ detailed questions** to extract everything from your brain
2. **Generates a comprehensive PRD** with all the sections engineers need
3. **Sets up taskmaster integration** with proper directory structure
4. **Validates quality** with automated checks (13 different validations)
5. **Suggests task breakdowns** with complexity estimates and dependencies

**Result:** You go from "I have an idea" to "I have a complete, validated PRD ready for AI task generation" in minutes.

## Installation

### Option A: Claude Code CLI (Recommended)

```bash
cd ~/.claude/skills
git clone https://github.com/anombyte93/prd-taskmaster.git
```

Claude Code recognizes the skill automatically on the next invocation.

### Option B: Codex (Untested)

Clone the repo and run Codex in the `prd-taskmaster` directory; then `/init` so Codex reads `SKILL.md`.

## Quick Start Guide

Activation phrases:
- "I want a PRD for adding two-factor authentication"
- "Create product requirements for a user dashboard"
- "Write a PRD for integrating with Stripe payments"
- "Generate requirements for building a dark mode feature"

### What Happens Next

1. Asks 12+ detailed discovery questions
2. Analyzes your codebase (if applicable)
3. Generates a comprehensive PRD
4. Sets up `.taskmaster/` integration directory
5. Validates with 13 automated quality checks
6. Shows summary and next steps

## What You Get

### Comprehensive PRD

Sections: Executive Summary · Problem Statement · Goals & Metrics · User Stories · Functional Requirements · Technical Considerations · Task Breakdown Hints · Dependencies · Out of Scope

### Taskmaster Integration

```
.taskmaster/
├── docs/
│   ├── prd.md
│   └── architecture.md
├── tasks/
│   └── .gitkeep
└── notes/
    └── .gitkeep
```

### CLAUDE.md / codex.md — TDD Workflow Guide

Generated project-root file guides the AI to:
- Follow TDD (RED → GREEN → REFACTOR)
- Use blind-validator agent for PRD validation
- Execute parallel tasks
- Enforce quality gates before marking tasks complete
- Follow taskmaster best practices

### Quality Validation — 13 checks

- All required sections present
- Requirements are testable
- Success metrics are SMART
- Technical considerations address architecture
- Task breakdown hints included
- Dependencies are mapped

## Advanced Usage

### Taskmaster Auto-Detection

The skill auto-detects and prefers MCP over CLI:
1. Detects MCP Task-Master-AI (if installed in Claude Code)
2. Falls back to CLI (`npm install -g task-master-ai`)
3. Provides installation instructions if neither is available

With MCP: direct function calls, no shell dependency, automatic task init/parse/expand.

With CLI:
```bash
taskmaster parse-prd --input .taskmaster/docs/prd.md --research
taskmaster expand-all --research
taskmaster next-task
```

### Customizing Templates

Edit files in `templates/`:
- `taskmaster-prd-comprehensive.md` — full 12-section PRD
- `taskmaster-prd-minimal.md` — quick template for simple features

## How It Works (v3.0 — 12-Step Workflow)

1. **Preflight & Resume Detection** — runs `script.py preflight`; detects crash state, existing PRD, taskmaster presence
2. **Detect Existing PRD** — offers execute/update/replace/review
3. **Detect Taskmaster** — blocks if neither MCP nor CLI found
4. **Discovery Questions** — 13 questions: 5 essential, 4 technical, 3 taskmaster-specific, 1 open-ended
5. **Initialize Taskmaster** — `script.py init-taskmaster`
6. **Generate PRD** — loads template, AI fills with discovery answers, writes `.taskmaster/docs/prd.md`
7. **Validate PRD Quality** — `script.py validate-prd`; grades EXCELLENT/GOOD/ACCEPTABLE/NEEDS_WORK
8. **Parse & Expand Tasks** — MCP (`parse_prd`, `expand_all`) or CLI
9. **Insert User Test Tasks** — every 5 tasks adds a USER-TEST checkpoint
10. **Setup Tracking Scripts** — generates 5 scripts: track-time.py, rollback.sh, learn-accuracy.py, security-audit.py, execution-state.py
11. **Choose Next Action** — handoff (show commands) or autonomous execution
12. **Summary & Start** — displays PRD location, task counts, validation score, phases, checkpoints

## Execution Modes

| Mode | Description |
|---|---|
| Sequential to Checkpoint | Tasks one-by-one; stops at USER-TEST for validation |
| Parallel to Checkpoint | Up to 3 concurrent independent tasks; stops at USER-TEST |
| Full Autonomous | Up to 5 concurrent; auto-completes USER-TEST |
| Manual Control | User issues "next task" / "task {id}" / "parallel {ids}" |

All modes include: DateTime tracking, progress logging, git branch-per-task (`task-{id}-{slug}`), rollback support, and state tracking.

## v2.0 / v3.0 Enhancements

- **DateTime tracking** — UTC timestamps, duration calculation, JSON state persistence
- **Instant rollback** — `rollback.sh X` reverts to any checkpoint tag
- **Accuracy learning** — analyzes estimated vs actual times, learns from pace
- **Security audit checklist** — auto-generated per codebase
- **Auto-resume after crash** — detects incomplete sessions, offers multiple resume points
- **v3.0 Codification Refactor** — deterministic ops moved to `script.py`; AI handles judgment only

## Status & Known Limitations

Status: Beta (primarily tested for web/API projects, English only, creator's own workflow)
- Assumes taskmaster workflow
- May ask redundant questions for very simple features
- Validation guidance only, not enforcement

## Docs

`reference/` directory:
- `taskmaster-integration-guide.md` — Taskmaster best practices, requirement format, task generation patterns
- `validation-checklist.md` — quality criteria detail

## Top-level structure

```
prd-taskmaster/
├── SKILL.md                   ← Main agent instruction file (12-step skill definition, 480+ lines)
├── SKILL.md.pre-codify        ← Pre-v3.0 skill definition (pre-codification refactor snapshot)
├── README.md                  ← Developer/public documentation
├── LICENSE                    ← MIT
├── CONTRIBUTING.md            ← Contribution guide
├── CODE_OF_CONDUCT.md         ← Code of conduct
├── install.sh                 ← Optional install helper
├── script.py                  ← Deterministic operations (preflight, validate-prd, load-template,
│                                 calc-tasks, gen-test-tasks, gen-scripts, backup-prd, log-progress)
├── templates/
│   ├── CLAUDE.md.template     ← Project-root TDD workflow guide template
│   ├── taskmaster-prd-comprehensive.md  ← Full 12-section PRD template
│   └── taskmaster-prd-minimal.md        ← Quick PRD template
├── scripts/
│   └── setup-taskmaster.sh    ← Creates .taskmaster/ directory structure
├── reference/
│   ├── taskmaster-integration-guide.md  ← PRD writing best practices for taskmaster
│   └── validation-checklist.md          ← Quality check criteria
└── .taskmaster/
    ├── docs/
    │   └── prd.md             ← Demo/reference PRD
    └── scripts/               ← Runtime tracking scripts (generated by gen-scripts)
```
