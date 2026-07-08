# phasr.sh

## Fetch log
- Inbox URL: https://phasr.sh/
- Final URL: https://phasr.sh/
- Fetched: 2026-07-08
- Pages: 11
- Mode: standard

## Landing page — https://phasr.sh/

Phasr: Open-Source AI Agent Workspace

Now in public beta

# Run AI coding agents in parallel

Open-source desktop workspace for multi-agent development. Isolate every task with Git worktrees, review real-time diffs, and merge only what is approved.

Download for macOS | View on GitHub

macOS · Free & open source

Built for teams using: Claude Code, Codex CLI, Gemini CLI, Aider, Cursor, Zed, VS Code, JetBrains, Git, GitHub, Linear, Supabase, Vercel, Neovim

## Features — Everything needed to orchestrate AI coding agents

A review-first workspace for parallel execution, Git worktree isolation, and controlled merges.

### Parallel Execution — Run dozens of agents at once

Launch multiple AI coding agents across independent tasks at the same time. Each agent gets an isolated environment with live status and progress visibility.

- Concurrent task execution across agents
- Real-time progress tracking and status
- Automatic resource management

### Universal Compatibility — Works with any CLI agent

Agent-agnostic by design. If it runs in a terminal, it runs in Phasr. No vendor lock-in, no proprietary protocols, and no forced provider choices.

Compatible agents listed: Claude Code (Anthropic), Codex CLI (OpenAI), Gemini CLI (Google), Cursor Agent (Cursor), Aider (Open Source), OpenCode (Open Source)

### Isolation — Changes stay isolated

Every agent runs in its own Git worktree. No file collisions, no shared working-directory conflicts, and no forced merges.

- Automatic Git worktree creation
- Zero-conflict parallel development
- Clean merge paths to main

Example worktrees: feat/auth-middleware from main · 6 files · 4 ahead; feat/rate-limit from main · 4 files · 2 ahead; fix/webhook-retry from main · 2 files · 1 ahead

### IDE Integration — Open in any editor

One-click deep links into VS Code, Cursor, JetBrains, Xcode, or any editor you prefer. Review and edit agent-generated code in your native environment.

Keyboard shortcuts: VS Code ⌘⇧V, Cursor ⌘⇧C, Zed ⌘⇧Z, JetBrains ⌘⇧J, Sublime ⌘⇧S, Terminal ⌘⇧T, Xcode ⌘⇧X, Finder ⌘⇧F

### Code Review — Review changes with clarity

See exactly what each agent changed. File-level diffs, line counts, and approval workflows keep humans in control before anything touches your main branch.

- Per-agent file diffs and change summaries
- Approve, reject, or request modifications
- Side-by-side comparison views

Actions: Reject | Approve & Merge

## Blog — Engineering playbooks for AI coding agents

Guides on parallel execution, Git worktree isolation, and human-in-the-loop review workflows.

- Why parallel agent execution changes everything (Engineering, Mar 12, 2026) — https://phasr.sh/blog/parallel-agent-execution
- Git worktree isolation: how Phasr prevents agents from colliding (Architecture, Mar 5, 2026) — https://phasr.sh/blog/git-worktree-isolation
- From prompt to PR: designing a human-in-the-loop review pipeline (Workflow, Feb 26, 2026) — https://phasr.sh/blog/human-in-the-loop-review
- The multi-model future: why agent orchestration should be provider-agnostic (Industry, Feb 18, 2026) — https://phasr.sh/blog/multi-model-future

Available for macOS · Open source under MIT

## Blog index — https://phasr.sh/blog

Engineering — Why parallel agent execution changes everything — https://phasr.sh/blog/parallel-agent-execution — Mar 12, 2026 — 6 min read

Architecture — Git worktree isolation: how Phasr prevents agents from colliding — https://phasr.sh/blog/git-worktree-isolation — Mar 5, 2026 — 7 min read

Workflow — From prompt to PR: designing a human-in-the-loop review pipeline — https://phasr.sh/blog/human-in-the-loop-review — Feb 26, 2026 — 8 min read

Industry — The multi-model future: why agent orchestration should be provider-agnostic — https://phasr.sh/blog/multi-model-future — Feb 18, 2026 — 5 min read

## Roadmap — https://phasr.sh/roadmap

Product Roadmap — What we are shipping next. Last updated March 2026.

Q1 2026 — Core Workspace Foundation — Shipped
- Parallel task execution in isolated worktrees
- File-level review and approval flow
- One-click opening in major IDEs

Q2 2026 — Team Collaboration Layer — In Progress
- Shared project spaces with role-based access
- Team activity feed and review assignments
- Reusable task templates for common workflows

Q3 2026 — Cloud Workspaces — PRO (Coming Soon) — Planned
- Cloud-hosted workspaces with secure access
- Sync workspace state across devices
- Fast boot for ready-to-code environments

Q3 2026 — Mobile App — PRO (Coming Soon) — Planned
- Live task status and notifications
- Agent conversation management from mobile
- Quick approve/reject actions for changes

Q4 2026 — Integrations — PRO — Planned
- Two-way sync for issues and pull requests
- Link roadmap work to project trackers
- Automation hooks for deployment workflows

Q4 2026 — Enterprise Readiness — Planned
- SSO, SCIM, and centralized admin controls
- Audit logs with exportable compliance reports
- Self-hosted deployment option

## Docs — https://phasr.sh/docs

Getting started — https://phasr.sh/docs/getting-started — Install Phasr, open a repository, and run your first multi-agent task in minutes.

Agent setup — https://phasr.sh/parallel-ai-coding-agents — Configure Claude Code, Codex CLI, Gemini CLI, Aider, and terminal-native agents.

Git worktree isolation — https://phasr.sh/git-worktree-isolation-for-ai-agents — Understand branch-per-task isolation and conflict-free merge workflows.

Review workflow — https://phasr.sh/human-in-the-loop-ai-code-review — Apply approval gates so every AI-generated change is reviewed before merge.

## Getting started — https://phasr.sh/docs/getting-started

Quickstart:
1. Install Phasr and open your repository workspace.
2. Connect your preferred coding agents (Claude Code, Codex CLI, Gemini CLI, or Aider).
3. Create independent tasks and launch them in parallel.
4. Review each worktree diff, approve clean changes, and merge.

Task planning checklist:
- Each task should touch a narrow file set and single objective.
- Assign branch naming conventions for traceability.
- Enable test commands per task for automated validation.
- Route high-risk diffs through explicit human approval.

## Parallel AI coding agents — https://phasr.sh/parallel-ai-coding-agents

Task decomposition — Break large requests into small independent units so agents can execute in parallel with minimal overlap.

Concurrency control — Launch many tasks at once while preserving separate worktrees and branch history for each agent.

Review queues — Prioritize high-risk diffs and merge approved tasks without blocking the rest of your pipeline.

## Git worktree isolation for AI agents — https://phasr.sh/git-worktree-isolation-for-ai-agents

Why branches are not enough — Branches point to commits. They do not provide separate working directories for concurrent agents.

Worktree lifecycle in Phasr — Create isolated worktree, run task, review diff, merge approved branch, and clean up the workspace.

Merge strategy checklist:
- Use branch-per-task naming for traceability.
- Require tests before review approval.
- Merge only approved branches into target branch.
- Remove completed worktrees to keep environments clean.

## Human-in-the-loop AI code review — https://phasr.sh/human-in-the-loop-ai-code-review

Diff triage — Review changes by file and risk surface so reviewers can focus effort where regressions are most likely.

Approval gates — Require explicit approval before merge, with support for reject and revision requests.

Revision loop — Send focused review feedback back to agents and iterate without losing branch context.

## Git worktree isolation (blog) — https://phasr.sh/blog/git-worktree-isolation

When you run multiple AI agents against the same codebase, isolation isn't optional. Without it, agents overwrite each other's files, produce unresolvable merge conflicts, and generate diffs built on half-finished work.

Containers are conceptually clean but operationally heavy — seconds to start, significant memory, container runtime required on every machine.

Git branches alone don't solve the problem — branches are pointers without separate working directories. Two agents on different branches sharing one worktree clobber uncommitted changes on checkout.

Git worktrees are the sweet spot — separate working directory linked to the same Git repository, own branch/index/files, shared object store. Nearly instant creation, minimal disk space, zero extra infrastructure.

In Phasr, launching an agent task creates a new worktree from current HEAD. Agent operates exclusively in that worktree. When done, changes are committed to the worktree's branch and presented for review.

Worktrees are disposable — once merged or discarded, removed with a single command.

Constraint: each worktree must be on a unique branch. Phasr auto-generates unique branch names per task (e.g., phasr/task-1742-add-rate-limiting).

Alternatives considered: tmpfs copies, shallow clones, overlay filesystems. Worktrees won — no special permissions, every OS, every Git GUI, zero maintenance.

## Human-in-the-loop review (blog) — https://phasr.sh/blog/human-in-the-loop-review

Principle: agents propose, humans approve. Every AI-generated change is a proposal until a human reviews and merges. Nothing lands in main without explicit approval.

Pipeline stages:
1. Agent works in isolated worktree, streaming progress in real time — watch diff evolve file by file.
2. Review surface when agent signals done — purpose-built diff viewer highlighting semantic structure (new functions, modified signatures, changed imports). Inline annotations flag large deletions, new dependencies, modified test assertions.
3. Human acts — Approve (one click → PR against target branch), Request modifications (agent re-enters worktree with feedback), or Discard (worktree cleaned up).

UX iterations: file-by-file view with summary panel for most-changed files; risk score heuristic flags critical paths (auth, payments, database migrations).

Inline chat: comment on any diff line; agent sees it as context when asked to revise.

## Multi-model future (blog) — https://phasr.sh/blog/multi-model-future

No single model is best at everything. Model selection should be per-task, not per-organization.

Most AI coding tools are tightly coupled to a single provider — switching models means switching tools.

Phasr is provider-agnostic: configure model per task; different tasks in same session can use different models. Orchestration layer adapts prompts, manages context windows, normalizes output.

Cost routing: 20 parallel agents on most expensive model burns budget fast; routing straightforward tasks to cheaper models can cut spend ~60%.
