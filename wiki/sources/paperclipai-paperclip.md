---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/paperclipai/paperclip
tags:
  - agent-orchestration
  - control-plane
  - multi-agent
  - heartbeat
  - org-chart
  - governance
  - cost-control
  - self-hosted
related:
  - paperclip.ing
  - hilash-cabinet
  - runcabinet.com
  - njbrake-agent-of-empires
  - joinoasis.com
  - skills.sh
  - zaro.ai
  - ruvnet-ruflo
  - 0xnyk-awesome-hermes-agent
product: paperclip
detail_level: standard
created: 2026-07-03
updated: 2026-07-07
---

Paperclip (`paperclipai/paperclip`) is an open-source Node.js + React control plane for running autonomous AI-agent companies — 72k+ GitHub stars, MIT license, TypeScript monorepo. It is not an agent framework; it is the organizational layer above any agent runtime (Claude Code, Codex, Cursor, OpenClaw, bash, HTTP bots). The repo implements twelve server subsystems — identity, org chart, work/tasks, heartbeat execution, workspaces, governance, budgets, routines, plugins, secrets, activity, and company portability — plus a built-in `skills/paperclip/SKILL.md` that defines how agents operate inside heartbeats (checkout-before-work, run-ID audit headers, scoped wake fast paths). See [[paperclip.ing]] for the unified product-site + repo view; this page is the GitHub-primary source.

_All claims below are sourced from ../../raw/github/paperclipai-paperclip.md unless otherwise noted._

## What it does

Paperclip lets operators define a company goal, hire AI agents into an org chart (CEO, CTO, engineers, etc.), set per-agent budgets, and run the company from a task-manager-style dashboard while agents execute on scheduled or event-driven heartbeats. The mental model is explicit: "If OpenClaw is an employee, Paperclip is the company." Agents bring their own prompts, models, and runtimes; Paperclip manages assignment, delegation up/down the org chart, goal ancestry on every task, atomic checkout locks, governance approvals, cost hard-stops, and multi-company isolation in one deployment.

## Installation

Recommended quickstart (self-hosted, no Paperclip account):

```bash
npx paperclipai onboard --yes
```

Bind presets for authenticated/private exposure:

```bash
npx paperclipai onboard --yes --bind lan
npx paperclipai onboard --yes --bind tailnet
```

From source (Node.js 20+, pnpm 9.15+):

```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip && pnpm install && pnpm dev
```

Dev mode starts the API at `http://localhost:3100` with embedded PGlite when `DATABASE_URL` is unset — no manual Postgres setup required.

## Key features

- **Bring your own agent** — local CLI/session adapters (Claude Code, Codex, Gemini, OpenCode, Pi, Cursor), HTTP/webhook bots (OpenClaw), command adapters, and external adapter plugins.
- **Goal alignment** — hierarchical tasks trace parentage to the company mission so agents always see the "why."
- **Heartbeats** — DB-backed wakeup queue with budget checks, workspace resolution, secret injection, skill loading, and structured run logs.
- **Org chart & governance** — roles, reporting lines, board approval workflows, pause/terminate, revisioned config with rollback.
- **Cost control** — monthly budgets per agent with hard stops; overspend auto-pauses agents and cancels queued work.
- **Ticket system** — issues with single assignee, blockers, comments, documents, attachments, work products, and full tool-call tracing.
- **Multi-company** — one deployment, many companies, complete data isolation.
- **Routines** — cron/webhook/API-triggered recurring tasks that create tracked issues and wake assigned agents.
- **Plugins** — instance-wide plugin system with out-of-process workers, job scheduling, and UI contributions.
- **Company portability** — import/export entire organizations with secret scrubbing and collision handling.

## Architecture

The control plane splits into two layers: (1) the Paperclip server — Express API + React board UI orchestrating identity, work, heartbeats, governance, budgets, and activity; (2) execution services via adapters that invoke external agent runtimes and phone home. The monorepo maps cleanly: `server/` (API), `ui/` (React + Vite), `packages/db` (Drizzle schema), `packages/shared`, `packages/adapters`, `packages/plugins`, `cli/` (`paperclipai` CLI), `doc/` (GOAL, PRODUCT, SPEC-implementation), and `skills/` (built-in agent skills).

Core engineering invariants from `AGENTS.md`: company-scoped entities everywhere, synchronized contracts across db/shared/server/ui, single-assignee task model, atomic issue checkout, approval gates, budget hard-stop auto-pause, and activity logging for mutating actions.

The built-in heartbeat skill (`skills/paperclip/SKILL.md`) is part of the architecture — agents wake in short windows, must `POST /api/issues/{id}/checkout` before work, include `X-Paperclip-Run-Id` on mutating calls, prefer `GET /api/agents/me/inbox-lite` for assignment triage, and use first-class `blockedByIssueIds` rather than free-text blockers.

## Example usage

Operator flow: onboard → create company with a goal → hire agents with adapter configs → approve strategy → monitor dashboard as heartbeats execute work.

Local agent CLI setup exports heartbeat env vars:

```bash
paperclipai agent local-cli <agent-id-or-shortname> --company-id <company-id>
```

Development workflows:

```bash
pnpm dev          # API + UI watch mode
pnpm test         # Vitest (default verification)
pnpm test:e2e     # Playwright (opt-in)
pnpm db:generate && pnpm db:migrate
```

## Maintenance status

Actively maintained: 72,610 stars, 13,539 forks, default branch `master`, latest release `v2026.626.0` (2026-06-27), pushed 2026-07-03. MIT license. Shipped milestones include plugin system, OpenClaw integration, company import/export, skills manager, scheduled routines, budgeting, agent reviews/approvals, and multiple human users. Roadmap items still open include cloud/sandbox agents, artifacts/work products, memory/knowledge, enforced outcomes, work queues, self-organization, CEO chat, cloud deployments, and a desktop app. Community: Discord, `@papercliping` on X, [awesome-paperclip](https://github.com/gsxdsm/awesome-paperclip) plugins. Telemetry is on by default; disable via `PAPERCLIP_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1`.
