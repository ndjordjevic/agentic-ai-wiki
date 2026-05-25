---
type: source
source_url: https://vibekanban.com/
companion_urls:
  - https://github.com/BloopAI/vibe-kanban
raw_files:
  - ../../raw/web/vibekanban.com.md
  - ../../raw/github/BloopAI-vibe-kanban.md
tags:
  - kanban-board
  - multi-agent-workflow
  - coding-agent-orchestration
  - plan-review-loop
  - git-worktrees
  - diff-review
  - developer-productivity
  - parallel-agents
related:
  - factory.ai
  - traycer.ai
  - eyaltoledano-claude-task-master
  - www.taskmaster.one
product: vibekanban
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Vibe Kanban is an open-source project management tool designed to accelerate the human planning and review work that AI coding agents depend on. Built by bloop (now sunsetting as a company but continuing as a community-maintained open-source project), it addresses the emerging bottleneck in AI-assisted development: while coding agents can work on infinite tasks in parallel, humans still need to plan and review that work — making planning and review the new speed limit for shipping software.

_All claims below are sourced from ../../raw/web/vibekanban.com.md unless otherwise noted._

## What it does

Vibe Kanban sits between the human and the coding agent. The workflow is three steps: **Plan** (create issues on the kanban board describing the work), **Prompt** (create a workspace that launches a coding agent with the issue as its prompt), **Review** (inspect diffs, leave inline comments, send feedback back to the agent). This cycle repeats until the work is ready for a pull request.

Supports 10+ coding agents out of the box: Claude Code, OpenAI Codex, GitHub Copilot, Gemini CLI, Amp, Cursor Agent CLI, OpenCode, Factory Droid, Claude Code Router (CCR), and Qwen Code.

## Key features

- **Kanban issues** — create, prioritise (Urgent/High/Medium/Low), assign, and tag issues; parent/child relationships for decomposing larger work. The issue description becomes the agent's prompt verbatim.
- **Workspaces** — each workspace creates git worktrees for one or more selected repositories, launches the coding agent, and isolates all changes from the main branch. Multiple sessions per workspace allow parallel agent conversations. (../../raw/github/BloopAI-vibe-kanban.md)
- **Diff review** — changes panel shows syntax-highlighted unified/side-by-side diffs; hover a line to add an inline comment that gets sent back to the agent in the chat. (../../raw/github/BloopAI-vibe-kanban.md)
- **Built-in browser preview** — test the running app without leaving the workspace; supports devtools, inspect mode, and device emulation.
- **MCP server** — exposes a Vibe Kanban MCP server so agents can query issue context programmatically; also supports connecting external MCP servers to enhance agent capabilities.
- **GitHub and Azure Repos integrations** — create pull requests with AI-generated descriptions, manage branches, and merge without leaving the app.
- **Cloud and self-hosting** — teams can share projects, issues, and organisations via Vibe Kanban Cloud or self-host with the provided Docker Compose stack.

## Architecture

Vibe Kanban is a Rust backend with a Node.js/pnpm frontend, started with a single `npx vibe-kanban` command. The backend manages git worktree lifecycle, agent process orchestration, and a local SQLite database (seeded from `dev_assets_seed/`). Environment variables configure host, ports, CORS origins, and optional relay-tunnel mode for remote access. (../../raw/github/BloopAI-vibe-kanban.md)

Agent processes are launched as subprocesses from within a workspace's worktree directory. The MCP server runs co-located with the backend, sharing the same `MCP_HOST`/`MCP_PORT` configuration. (../../raw/github/BloopAI-vibe-kanban.md)

## Installation

```bash
npx vibe-kanban
```

No global install required. Authenticate with your chosen coding agent first; see [docs/supported-coding-agents](https://vibekanban.com/docs/supported-coding-agents) for per-agent setup. (../../raw/github/BloopAI-vibe-kanban.md)

## Example usage

1. Run `npx vibe-kanban` — opens the UI in the browser.
2. Create an issue: "Fix login timeout on slow connections — users on 3G see a 5 s timeout; add exponential backoff."
3. Click **Create Workspace** on the issue — select your repo and branch, choose Claude Code.
4. Agent begins working immediately; switch to the changes panel when it finishes.
5. Review the diff, hover line 42, add comment: "validate input before the retry loop."
6. Submit feedback — agent receives the comment and iterates.
7. When satisfied, create a PR from the workspace; merge via GitHub integration. (../../raw/github/BloopAI-vibe-kanban.md)

## When to use

Use Vibe Kanban when running multiple coding agents in parallel — it eliminates idle time by letting you context-switch between agents at review time rather than waiting for one to finish. It is also the right choice when team coordination around agent work matters: shared kanban boards, organisations, and projects make multi-person agent-assisted workflows tractable. For solo use without team features, sign-in can be skipped.

## Maintenance status

26,494 stars; 2,774 forks; Apache-2.0 license. Latest release: v0.1.44 (2026-04-24). The company (bloop) is shutting down; the project is transitioning to community-maintained open source. Remote cloud services will be removed within 30 days; local workspace functionality continues unaffected. Roadmap for the community edition to be published. (../../raw/github/BloopAI-vibe-kanban.md)

## Ecosystem

Vibe Kanban is agent-agnostic by design — it wraps any CLI-based coding agent. [[factory.ai]]'s Factory Droid is among the supported agents, as is [[traycer.ai]]'s planning-oriented workflow. The MCP server integration means agents with MCP client support can pull issue context directly, reducing manual copy-paste of task descriptions. Self-hosting with Docker Compose is documented for teams that need air-gapped or on-prem deployments.
