# obra/superpowers

## Metadata
- Stars: 169143
- Primary language: Shell
- Default branch: main
- Latest release: v5.0.7 (about 26 days ago, ~2026-04-01)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-04-27
- Final URL: https://github.com/obra/superpowers

## Description
An agentic skills framework & software development methodology that works.

## README

# Superpowers

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY.

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

## Installation

### Claude Code Official Marketplace

```bash
/plugin install superpowers@claude-plugins-official
```

### Claude Code (Superpowers Marketplace)

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### OpenAI Codex CLI

Search for "superpowers" via `/plugins` → Install Plugin.

### Cursor (via Plugin Marketplace)

```text
/add-plugin superpowers
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
gemini extensions update superpowers  # to update
```

### OpenCode

Tell OpenCode: `Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md`

## The Basic Workflow

1. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.
2. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.
3. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.
4. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.
5. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.
6. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.
7. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## Skills Library

### Testing
- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

### Debugging
- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** - Ensure it's actually fixed

### Collaboration
- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)

### Meta
- **writing-skills** - Create new skills following best practices (includes testing methodology)
- **using-superpowers** - Introduction to the skills system

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

## Contributing

The general contribution process for Superpowers is below. Keep in mind that we don't generally accept contributions of new skills and that any updates to skills must work across all of the coding agents we support.

- Fork the repository
- Switch to the 'dev' branch
- Create a branch for your work
- Follow the `writing-skills` skill for creating and testing new and modified skills
- Submit a PR, being sure to fill in the pull request template.

See `skills/writing-skills/SKILL.md` for the complete guide.

## Community

Superpowers is built by [Jesse Vincent](https://blog.fsck.com) and the rest of the folks at [Prime Radiant](https://primeradiant.com).

- **Discord**: https://discord.gg/35wsABTejz
- **Issues**: https://github.com/obra/superpowers/issues

## License

MIT License

## Top-level structure

```
dir    .claude-plugin      ← Claude Code plugin config
dir    .codex-plugin       ← Codex CLI plugin config
dir    .codex              ← Codex agent instructions
dir    .cursor-plugin      ← Cursor plugin config
dir    .opencode           ← OpenCode install instructions
file   AGENTS.md           ← Contributor guidelines for AI agents (94% PR rejection policy)
file   CLAUDE.md           ← Claude Code contributor guidelines (same content as AGENTS.md)
file   GEMINI.md           ← Gemini CLI instructions
dir    agents              ← Agent-specific configuration
dir    assets              ← Static assets
dir    commands            ← Command definitions
dir    docs                ← Docs per-agent (README.codex.md, README.opencode.md, testing.md, etc.)
dir    hooks               ← Hook scripts
file   package.json        ← npm package definition
dir    scripts             ← Utility scripts
dir    skills              ← Skills library (14 skill directories)
dir    tests               ← Test suite
```

## Skills directory listing

```
dir    brainstorming
dir    dispatching-parallel-agents
dir    executing-plans
dir    finishing-a-development-branch
dir    receiving-code-review
dir    requesting-code-review
dir    subagent-driven-development
dir    systematic-debugging
dir    test-driven-development
dir    using-git-worktrees
dir    using-superpowers
dir    verification-before-completion
dir    writing-plans
dir    writing-skills
```

## AGENTS.md excerpt (contributor guidelines for AI agents)

This repo has a 94% PR rejection rate. Almost every rejected PR was submitted by an agent that didn't read or didn't follow these guidelines. Key policy points:

- Before opening a PR: read the PR template, search for existing PRs, verify real problem, confirm change belongs in core, show diff to human partner.
- Zero-dependency plugin by design — no third-party dependencies accepted.
- Skills are behavior-shaping code, not prose — changes require adversarial eval evidence.
- No domain-specific, project-specific, bulk/spray-and-pray, or fabricated PRs accepted.
- Skills use deliberately tuned language ("your human partner") that is not interchangeable with "the user".
