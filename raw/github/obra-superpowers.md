# obra/superpowers

## Metadata
- Stars: 190063
- Primary language: Shell
- Default branch: main
- Latest release: v5.1.0 (2026-05-04)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-05-14
- Final URL: https://github.com/obra/superpowers

## Description
An agentic skills framework & software development methodology that works. A complete software development methodology for coding agents built on composable skills and initial instructions.

## README

# Superpowers

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI, and DRY.

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

## Installation

Installation differs by harness. Superpowers is available on the official Claude plugin marketplace:

```bash
/plugin install superpowers@claude-plugins-official
```

Or via the Superpowers marketplace:

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

Supported harnesses: Claude Code, Codex CLI, Codex App, Factory Droid, Gemini CLI, OpenCode, Cursor, GitHub Copilot CLI.

For OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

## The Basic Workflow

1. **brainstorming** — Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.

2. **using-git-worktrees** — Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.

3. **writing-plans** — Activates with approved design. Breaks work into bite-sized tasks (2–5 minutes each). Every task has exact file paths, complete code, verification steps.

4. **subagent-driven-development** or **executing-plans** — Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.

5. **test-driven-development** — Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

6. **requesting-code-review** — Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.

7. **finishing-a-development-branch** — Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## What's Inside

### Skills Library

**Testing**
- **test-driven-development** — RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** — 4-phase root cause process
- **verification-before-completion** — Ensure it's actually fixed

**Collaboration**
- **brainstorming** — Socratic design refinement
- **writing-plans** — Detailed implementation plans
- **executing-plans** — Batch execution with checkpoints
- **dispatching-parallel-agents** — Concurrent subagent workflows
- **requesting-code-review** — Pre-review checklist
- **receiving-code-review** — Responding to feedback
- **using-git-worktrees** — Parallel development branches
- **finishing-a-development-branch** — Merge/PR decision workflow
- **subagent-driven-development** — Fast iteration with two-stage review

**Meta**
- **writing-skills** — Create new skills following best practices
- **using-superpowers** — Introduction to the skills system (auto-loads at session start)

## Philosophy

- **Test-Driven Development** — Write tests first, always
- **Systematic over ad-hoc** — Process over guessing
- **Complexity reduction** — Simplicity as primary goal
- **Evidence over claims** — Verify before declaring success

## Community

Superpowers is built by Jesse Vincent and the team at Prime Radiant (https://primeradiant.com).

- **Discord**: https://discord.gg/35wsABTejz
- **Issues**: https://github.com/obra/superpowers/issues

## Docs

### AGENTS.md / CLAUDE.md

The repo includes detailed AGENTS.md and CLAUDE.md with contributor guidelines. The CLAUDE.md includes strong guidance for AI agents: a 94% PR rejection rate; all PRs must be based on real user problems, must fill the PR template completely, and must include human review of the full diff before submission. The maintainers explicitly state they reject "slop" — speculative, bulk, or fabricated PRs.

### using-superpowers skill (excerpt)

The `using-superpowers` skill is the bootstrap that loads at session start. It establishes the skill invocation rule: **invoke relevant or requested skills BEFORE any response or action**, even with a 1% chance of applicability. Skills override default system behavior but user instructions always take precedence.

Key skill invocation flow:
1. On any user message → check if any skill applies
2. If yes (even 1% chance) → invoke Skill tool
3. Announce "Using [skill] to [purpose]"
4. If skill has checklist → create todos
5. Follow skill exactly

### Skill invocation instruction priority:
1. User's explicit instructions (CLAUDE.md, AGENTS.md, direct requests) — highest
2. Superpowers skills — override default system behavior
3. Default system prompt — lowest

## Top-level structure

| Entry | Type | Notes |
|---|---|---|
| `skills/` | dir | 14 skill directories (brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills) |
| `.claude-plugin/` | dir | Claude Code plugin manifest |
| `.codex-plugin/` | dir | Codex plugin manifest |
| `.cursor-plugin/` | dir | Cursor plugin manifest |
| `.opencode/` | dir | OpenCode installation instructions |
| `hooks/` | dir | Git lifecycle hooks |
| `docs/` | dir | Extended documentation per harness |
| `tests/` | dir | Test suite |
| `scripts/` | dir | Release and update automation |
| `CLAUDE.md` | file | Agent-facing contributor guidelines (strict: 94% PR rejection rate, real-problem requirement) |
| `AGENTS.md` | file | Same content as CLAUDE.md for non-Claude agents |
| `GEMINI.md` | file | Gemini-specific agent instructions |
| `README.md` | file | User-facing documentation |
| `RELEASE-NOTES.md` | file | Release history |
| `package.json` | file | npm package metadata |
| `gemini-extension.json` | file | Gemini extension manifest |
| `.github/` | dir | CI/CD and PR templates |
