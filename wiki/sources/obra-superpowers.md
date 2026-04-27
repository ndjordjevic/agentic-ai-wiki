---
type: source
source_url: https://github.com/obra/superpowers
tags: [agentic-skills-framework, subagent-driven-development, tdd, claude-code, cursor, codex, gemini-cli, copilot, spec-driven-development, workflow-automation, multi-agent, plugin-architecture]
related:
  - "[[gsd-build-get-shit-done]]"
product: superpowers
detail_level: standard
created: 2026-04-27
updated: 2026-04-27
---

Superpowers is a composable agentic skills framework and software development methodology — the highest-starred project in this wiki at 169k+ stars — that wraps coding agents (Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot CLI, OpenCode) in a structured, skills-driven workflow. Unlike prompt libraries, skills trigger automatically; the agent checks for relevant skills before any task, making the workflows mandatory rather than optional. The core loop is: socratic design brainstorming → spec-reviewed plan → subagent-driven task execution → two-stage code review → branch finalization.

_All claims below are sourced from ../../raw/github/obra-superpowers.md unless otherwise noted._

## What It Does

Superpowers sits between the developer and their coding agent as a plugin installed into the agent's runtime. When the agent sees that something is being built, it does not jump into writing code — it invokes the `brainstorming` skill to refine the idea through Socratic questioning, produces a spec in reviewable chunks, then invokes `writing-plans` to produce a bite-sized implementation plan. From there, `subagent-driven-development` dispatches fresh subagents per task with two-stage review (spec compliance, then code quality). The `test-driven-development` skill enforces the RED-GREEN-REFACTOR cycle at every step, including deleting code written before tests.

The system solves three problems common to AI coding agents:

1. **Unstructured execution** — agents jump to code without understanding the real goal. Brainstorming and spec sign-off gates prevent this.
2. **Context drift** — long autonomous sessions deviate from the agreed plan. Two-stage subagent review catches deviation before it compounds.
3. **Untested output** — agents skip tests or write them after the fact. The TDD skill enforces write-failing-test-first and deletes post-hoc code.

## Installation

Superpowers is available via the official Claude plugin marketplace and a Superpowers-maintained marketplace, plus native extension mechanisms for each supported agent:

```bash
# Claude Code (official marketplace)
/plugin install superpowers@claude-plugins-official

# Claude Code (Superpowers marketplace)
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# GitHub Copilot CLI
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace

# Gemini CLI
gemini extensions install https://github.com/obra/superpowers

# Cursor
/add-plugin superpowers
```

For OpenCode, instruct the agent to fetch and follow the `INSTALL.md` from the raw GitHub URL. Updates are often automatic depending on the agent runtime.

## Key Features

- **14 composable skills** covering the full development lifecycle: brainstorming, planning, execution, debugging, review, and branch management.
- **Automatic skill triggering** — no invocation commands required; the agent checks for relevant skills before each task.
- **Subagent-driven development** — each task dispatched to a fresh subagent, reducing context contamination; two-stage review (spec compliance → code quality) before moving forward.
- **TDD enforcement** — RED-GREEN-REFACTOR cycle; deletes code written before failing tests.
- **Parallel agent dispatching** — `dispatching-parallel-agents` skill for concurrent independent workstreams.
- **Git worktree integration** — each feature branch gets an isolated worktree; `finishing-a-development-branch` offers merge/PR/keep/discard options with worktree cleanup.
- **Cross-agent compatibility** — a single zero-dependency plugin works across Claude Code, Cursor, Codex, Gemini CLI, Copilot CLI, and OpenCode.
- **Skill authoring** — `writing-skills` skill guides agents in creating new skills with adversarial pressure testing methodology.

## Architecture

Superpowers is a zero-dependency plugin (no external packages). Skills are files under `skills/<skill-name>/SKILL.md` — markdown documents that shape agent behavior when loaded. The agent runtime loads skill files on demand or automatically when context triggers a match.

Plugin adapter directories (`.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.opencode/`) provide runtime-specific manifests and install hooks. A `commands/` directory provides command definitions. Agent-specific instruction files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) carry contributor guidelines and AI-specific policies.

The `hooks/` directory provides lifecycle hooks, and `scripts/` provides utility scripts for version bumping and release automation. The test suite lives in `tests/`.

Skills use deliberately tuned language — notably "your human partner" instead of "the user" — which is intentional behavior-shaping terminology, not stylistic preference.

## Skills Reference

| Skill | Phase | Purpose |
|---|---|---|
| `brainstorming` | Design | Socratic requirements refinement; produces spec document |
| `writing-plans` | Planning | Bite-sized tasks with file paths, code, and verification steps |
| `using-git-worktrees` | Setup | Isolated branch workspace; clean test baseline |
| `subagent-driven-development` | Execution | Fresh subagent per task; two-stage spec+quality review |
| `executing-plans` | Execution | Batch execution with human checkpoints |
| `dispatching-parallel-agents` | Execution | Concurrent independent subagent workstreams |
| `test-driven-development` | Implementation | RED-GREEN-REFACTOR; deletes pre-test code |
| `systematic-debugging` | Debugging | 4-phase root-cause process |
| `verification-before-completion` | Debugging | Confirms fix is real, not cosmetic |
| `requesting-code-review` | Review | Pre-review checklist against plan |
| `receiving-code-review` | Review | Structured response to feedback |
| `finishing-a-development-branch` | Finalization | Merge/PR/keep/discard with worktree cleanup |
| `writing-skills` | Meta | Skill authoring guide with testing methodology |
| `using-superpowers` | Meta | Introduction to the skills system |

## Maintenance Status

Actively maintained by Jesse Vincent and Prime Radiant. Latest release v5.0.7. 169k+ stars, 14.9k forks. 94% PR rejection rate — contributions require specific evidence of real problems and cross-agent compatibility. New skills are generally not accepted; skill modifications require adversarial eval results.
