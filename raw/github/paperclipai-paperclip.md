# paperclipai/paperclip

## Metadata
- Stars: 59268
- Primary language: TypeScript
- Default branch: master
- Latest release: v2026.416.0 (about 10 days ago)
- License: MIT License
- Homepage: https://paperclip.ing
- Fetched: 2026-04-27
- Final URL: https://github.com/paperclipai/paperclip

## Description
Open-source orchestration for zero-human companies

## README

# Open-source orchestration for zero-human companies

**If OpenClaw is an _employee_, Paperclip is the _company_**

Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own agents, assign goals, and track your agents' work and costs from one dashboard.

It looks like a task manager — but under the hood it has org charts, budgets, governance, goal alignment, and agent coordination.

**Manage business goals, not pull requests.**

|        | Step            | Example                                                            |
| ------ | --------------- | ------------------------------------------------------------------ |
| **01** | Define the goal | "Build the #1 AI note-taking app to $1M MRR."                    |
| **02** | Hire the team   | CEO, CTO, engineers, designers, marketers — any bot, any provider. |
| **03** | Approve and run | Review strategy. Set budgets. Hit go. Monitor from the dashboard.  |

> **COMING SOON: Clipmart** — Download and run entire companies with one click. Browse pre-built company templates — full org structures, agent configs, and skills — and import them into your Paperclip instance in seconds.

Works with: OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP webhooks.

*"If it can receive a heartbeat, it's hired."*

## Paperclip is right for you if

- You want to build **autonomous AI companies**
- You **coordinate many different agents** (OpenClaw, Codex, Claude, Cursor) toward a common goal
- You have **20 simultaneous Claude Code terminals** open and lose track of what everyone is doing
- You want agents running **autonomously 24/7**, but still want to audit work and chime in when needed
- You want to **monitor costs** and enforce budgets
- You want to manage your autonomous businesses **from your phone**

## Features

- **Bring Your Own Agent** — Any agent, any runtime, one org chart.
- **Goal Alignment** — Every task traces back to the company mission.
- **Heartbeats** — Agents wake on a schedule, check work, and act. Delegation flows up and down the org chart.
- **Cost Control** — Monthly budgets per agent. No runaway costs.
- **Multi-Company** — One deployment, many companies. Complete data isolation.
- **Ticket System** — Every conversation traced. Every decision explained. Full tool-call tracing and immutable audit log.
- **Governance** — You're the board. Approve hires, override strategy, pause or terminate any agent at any time.
- **Org Chart** — Hierarchies, roles, reporting lines. Your agents have a boss, a title, and a job description.
- **Mobile Ready** — Monitor and manage from anywhere.

## What Paperclip is not

| | |
|---|---|
| **Not a chatbot.** | Agents have jobs, not chat windows. |
| **Not an agent framework.** | We don't tell you how to build agents. We tell you how to run a company made of them. |
| **Not a workflow builder.** | No drag-and-drop pipelines. Paperclip models companies — with org charts, goals, budgets, and governance. |
| **Not a prompt manager.** | Agents bring their own prompts, models, and runtimes. Paperclip manages the organization they work in. |
| **Not a single-agent tool.** | This is for teams. If you have one agent, you probably don't need Paperclip. If you have twenty — you definitely do. |

## Why Paperclip is special

| | |
|---|---|
| **Atomic execution.** | Task checkout and budget enforcement are atomic. |
| **Persistent agent state.** | Agents resume the same task context across heartbeats. |
| **Runtime skill injection.** | Agents can learn Paperclip workflows at runtime. |
| **Governance with rollback.** | Approval gates, revisioned config, rollback. |
| **Goal-aware execution.** | Tasks carry full goal ancestry. |
| **Portable company templates.** | Export/import orgs, agents, and skills with secret scrubbing. |
| **True multi-company isolation.** | Company-scoped entities, separate data and audit trails. |

## Architecture (What's Under the Hood)

Paperclip is a full control plane, not a wrapper. Core systems:

```
┌──────────────────────────────────────────────────────────────┐
│                       PAPERCLIP SERVER                       │
│  Identity & Access │ Work & Tasks │ Heartbeat Execution │ Governance │
│  Org Chart & Agents│ Workspaces  │ Plugins            │ Budget & Costs │
│  Routines & Sched. │ Secrets     │ Activity & Events   │ Company Portability │
└──────────────────────────────────────────────────────────────┘
         ▲              ▲              ▲              ▲
   Claude Code     Codex CLI     CLI agents     HTTP/web bots
```

**System modules:**

- **Identity & Access** — Board users, agent API keys, short-lived run JWTs, company memberships.
- **Work & Task System** — Issues with company/project/goal/parent links, atomic checkout, blockers, comments, documents, attachments, labels.
- **Heartbeat Execution** — DB-backed wakeup queue, budget checks, workspace resolution, secret injection, skill loading, adapter invocation. Structured logs, cost events, audit trails.
- **Workspaces & Runtime** — Project workspaces, isolated execution workspaces (git worktrees, operator branches), runtime services.
- **Governance & Approvals** — Board approval workflows, execution policies, budget hard-stops, agent pause/resume/terminate.
- **Budget & Cost Control** — Token and cost tracking by company, agent, project, goal, issue, provider, model. Scoped budget policies with warning thresholds and hard stops.
- **Routines & Schedules** — Cron, webhook, and API triggers. Each routine creates a tracked issue and wakes the assigned agent.
- **Plugins** — Out-of-process workers, capability-gated host services, job scheduling, tool exposure, UI contributions.
- **Secrets & Storage** — Instance and company secrets, encrypted local storage, provider-backed object storage.
- **Company Portability** — Export/import entire organizations with secret scrubbing and collision handling.

## Quickstart

```bash
npx paperclipai onboard --yes
```

Or manual:
```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev
```

API server at `http://localhost:3100`. Embedded PostgreSQL created automatically.

**Requirements:** Node.js 20+, pnpm 9.15+

## Development commands

```bash
pnpm dev         # Full dev (API + UI, watch mode)
pnpm build       # Build all
pnpm typecheck   # Type checking
pnpm test        # Vitest test run
pnpm test:e2e    # Playwright browser suite
pnpm db:generate # Generate DB migration
pnpm db:migrate  # Apply migrations
```

## Roadmap (completed ✅ / planned ⚪)

- ✅ Plugin system
- ✅ OpenClaw integration
- ✅ companies.sh — import/export organizations
- ✅ AGENTS.md configurations
- ✅ Skills Manager
- ✅ Scheduled Routines
- ✅ Better Budgeting
- ✅ Agent Reviews and Approvals
- ✅ Multiple Human Users
- ⚪ Cloud / Sandbox agents
- ⚪ Artifacts & Work Products
- ⚪ Memory / Knowledge
- ⚪ CEO Chat
- ⚪ Cloud deployments
- ⚪ Clipmart (pre-built company templates)

## Top-level structure

```
packages/    — monorepo packages (server, UI, adapters, etc.)
server/      — main API server (Node.js)
ui/          — React dashboard
cli/         — CLI (paperclipai onboard, configure)
docs/        — documentation (agents-runtime.md, guides/, start/, api/, adapters/)
skills/      — built-in agent skills
scripts/     — build and utility scripts
tests/       — test suite (Vitest + Playwright e2e)
AGENTS.md    — agent developer instructions
adapter-plugin.md — adapter plugin guide
ROADMAP.md   — detailed roadmap
docker/      — Docker deployment files
```

Notable: `docs/guides/` has agent-developer and board-operator sub-guides; `docs/start/` has architecture.md, core-concepts.md, quickstart.md; `.agents/` and `.claude/` directories present for agent instruction files.
