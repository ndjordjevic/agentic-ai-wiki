---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://github.com/anombyte93/prd-taskmaster
tags:
  - prd-generation
  - taskmaster-integration
  - claude-code-skill
  - requirements-engineering
  - ai-dev-workflow
  - tdd
  - validation-automation
  - skill-md
related:
  - bmad-code-org-bmad-method
  - anthropics-skills
  - nidhinjs-prompt-master
  - othmanadi-planning-with-files
  - backnotprop-plannotator
  - goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b
  - eyaltoledano-claude-task-master
  - www.taskmaster.one
  - phuryn-pm-skills
product: prd-taskmaster
detail_level: standard
created: 2026-05-22
updated: 2026-07-06
---

PRD-Taskmaster is a Claude Code skill (4,447 stars) that drives a 12-step interactive workflow to produce engineer-focused Product Requirements Documents (PRDs) and wire them directly into Taskmaster AI for automatic task generation. Where most AI coding assistants generate requirements on demand from a single prompt, prd-taskmaster structures the process: it asks 12+ discovery questions, validates the resulting PRD against 13 quality criteria, initialises a `.taskmaster/` directory, and then optionally executes the generated tasks autonomously — with rollback, DateTime tracking, and user-test checkpoints built in.

_All claims below are sourced from ../../raw/github/anombyte93-prd-taskmaster.md unless otherwise noted._

## What it does

PRD-Taskmaster converts a vague feature idea into a comprehensive, validated PRD and a ready-to-execute Taskmaster task tree. The skill activates on phrases like "I want a PRD for…" or "create product requirements for…". It runs a preflight check to detect existing PRDs, crash-state, and whether Taskmaster is available via MCP or CLI, then leads the user through structured discovery before generating and scoring the document.

## Installation

Clone into `~/.claude/skills/` and Claude Code picks it up automatically:

```bash
cd ~/.claude/skills
git clone https://github.com/anombyte93/prd-taskmaster.git
```

Codex is also supported (untested): run Codex in the cloned directory and issue `/init`.

## Key features

- **12-step structured workflow** — preflight → PRD detection → Taskmaster detection → discovery questions → PRD generation → validation → task parsing → user-test insertion → tracking setup → execution mode selection
- **13-point quality validation** — scores PRDs as EXCELLENT / GOOD / ACCEPTABLE / NEEDS_WORK; catches vague language, missing acceptance criteria, non-testable requirements
- **Taskmaster auto-detection** — prefers MCP (`task-master-ai` MCP server) over CLI; blocks gracefully with install instructions if neither is found
- **Autonomous execution modes** — Sequential to Checkpoint, Parallel to Checkpoint (3 concurrent), Full Autonomous (5 concurrent), Manual Control; all include DateTime tracking, git branch-per-task, and rollback
- **Auto-resume after crash** — `script.py preflight` detects incomplete session state and offers resume from subtask, task, or checkpoint
- **CLAUDE.md generation** — produces a project-root TDD workflow guide (RED → GREEN → REFACTOR) that persists AI behaviour across the project lifetime

## Architecture

The v3.0 "Codification Refactor" splits responsibilities cleanly: `script.py` owns all deterministic operations (preflight JSON, validate-prd, load-template, calc-tasks, gen-test-tasks, gen-scripts, backup-prd, log-progress); `SKILL.md` owns all AI judgment (questions, content synthesis, mode recommendations). This prevents AI hallucination of structural operations while keeping content quality in the model. Runtime artefacts live under `.taskmaster/scripts/` — five Python/Bash utilities generated on demand per project.

## Example usage

```
User: "I want a PRD for adding two-factor authentication"
```

The skill runs preflight, asks 13 discovery questions, writes `.taskmaster/docs/prd.md`, scores it (e.g. "58/60 — EXCELLENT"), parses tasks via MCP (`parse_prd` + `expand_all`), inserts USER-TEST checkpoints every 5 tasks, and offers handoff or autonomous execution.

With Taskmaster CLI after handoff:
```bash
taskmaster parse-prd --input .taskmaster/docs/prd.md --research
taskmaster expand-all --research
taskmaster next-task
```

## When to use

Use prd-taskmaster when you have a feature idea and want to systematically extract requirements before writing code — especially when using Taskmaster or another AI task-breakdown tool that needs detailed, testable specs. It is most valuable for medium-to-large features (the skill estimates effort in tasks and hours), web/API projects, and teams adopting AI-assisted development who want consistent PRD structure without hours of manual writing. It is less suited to one-off scripts, minimal documentation workflows, or projects with strict proprietary PRD templates.

## Maintenance status

4,447 stars, 42 forks, MIT licence, latest release v3.0.0. Last pushed 2026-04-26. Beta status by the author's own declaration — primarily tested for web/API projects in English. English-only, taskmaster-workflow-assumed. Feedback and contributions welcomed via GitHub Issues/Discussions.

## Ecosystem

prd-taskmaster pairs tightly with [Taskmaster AI](https://github.com/eyaltoledano/claude-task-master) (the `task-master-ai` MCP server / npm CLI) for task generation. It also generates `CLAUDE.md` and optionally `codex.md` to guide subsequent AI sessions through TDD. See [[bmad-code-org-bmad-method]] for a more opinionated, phase-driven alternative that also produces PRDs as intermediate artefacts inside a full agile AI workflow. For standalone skill architecture patterns see [[anthropics-skills]] and [[nidhinjs-prompt-master]].
