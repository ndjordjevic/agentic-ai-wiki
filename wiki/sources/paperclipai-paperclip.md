---
type: source
source_url: https://github.com/paperclipai/paperclip
tags: [agent-orchestration, autonomous-company, org-chart, heartbeat-scheduling, cost-control, governance, plugin-system, multi-agent, bring-your-own-agent, typescript, nodejs]
related:
  - "[[hilash-cabinet]]"
  - "[[paperclip.ing]]"
  - "[[gsd-build-get-shit-done]]"
product: paperclip.ing
detail_level: standard
created: 2026-04-27
updated: 2026-04-27
---

`paperclipai/paperclip` is the open-source codebase (59k+ stars, MIT, TypeScript/Node.js) for Paperclip — the company-level orchestration layer for teams of AI agents. Where individual agent tools like [[hilash-cabinet]] and [[gsd-build-get-shit-done]] address memory management and coding workflows, Paperclip addresses the layer above: how do you coordinate 10–50 AI agents, assign them company goals, track their costs, enforce governance, and maintain accountability across dozens of concurrent autonomous tasks?

_All claims below are sourced from ../../raw/github/paperclipai-paperclip.md unless otherwise noted._

## What it does

Paperclip is a Node.js server + React dashboard that runs a company made of AI agents. Users define a company mission, hire agents as named employees with roles (CEO, CTO, engineer), approve the CEO's strategy, set budgets, and the system coordinates delegation, scheduling, cost tracking, and governance. The key insight: "If OpenClaw is an employee, Paperclip is the company."

Not a workflow builder or prompt manager — it models the *organizational layer*: org charts, budgets, goals, task checkout, delegation chains, and audit logs.

## Installation

```bash
npx paperclipai onboard --yes
```

Or manually:
```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev   # API at http://localhost:3100, embedded Postgres created automatically
```

**Requirements:** Node.js 20+, pnpm 9.15+

## Key features

- **Bring Your Own Agent** — Any agent that can receive a heartbeat signal: Claude Code, OpenClaw, Codex, Cursor, bash scripts, HTTP bots. No vendor lock-in.
- **Org Chart** — Agents have roles, titles, reporting lines, and budgets. Hierarchical delegation works out of the box.
- **Goal Alignment** — Every task carries full goal ancestry (company mission → project → goal → task). Agents always know *what* and *why*.
- **Heartbeat Execution** — DB-backed wakeup queue; agents wake on schedule, atomic task checkout, budget check, skill injection, execution, structured logs, cost events, audit trail. Orphaned runs auto-recovered.
- **Cost Control** — Token and cost tracking by company/agent/project/goal/issue/provider/model. Scoped budget policies with warning thresholds and hard stops. Overspend auto-pauses agents.
- **Governance & Approvals** — Board approval workflows, execution policies with review/approval stages, agent pause/resume/terminate, full audit log.
- **Multi-Company** — Company-scoped entities; one deployment runs many isolated companies.
- **Ticket System** — Issues with atomic checkout, blocker dependencies, comments, documents, attachments, work products, immutable audit trail.
- **Plugin System** — Out-of-process plugin workers, capability-gated host services, job scheduling, tool exposure, UI contributions.
- **Company Portability** — Export/import entire organizations (agents, skills, projects, routines) with secret scrubbing.
- **Routines & Schedules** — Cron, webhook, and API triggers; each routine creates a tracked issue and wakes the assigned agent.

## Architecture

Full control plane, not a wrapper around another tool. Monorepo (`pnpm` workspaces):

```
packages/    — server, UI, adapters, core libs
server/      — Node.js API server
ui/          — React dashboard
cli/         — paperclipai onboard/configure CLI
docs/        — guides (agent-developer, board-operator, adapters), start/, api/
skills/      — built-in agent skills
AGENTS.md    — agent developer instructions
```

**Core subsystems:**

| Subsystem | Responsibility |
|---|---|
| Identity & Access | Board users, agent API keys, run JWTs, company memberships |
| Work & Task System | Issues with goal ancestry, atomic checkout, execution locks, blocker deps |
| Heartbeat Execution | DB-backed wakeup, budget checks, skill loading, adapter invocation, recovery |
| Workspaces & Runtime | Git worktrees, operator branches, runtime services (dev servers, preview URLs) |
| Governance | Board approvals, execution policies, decision tracking, budget hard-stops |
| Budget & Cost Control | Multi-dimensional cost tracking, scoped policies, auto-pause on overspend |
| Routines & Schedules | Cron/webhook/API triggers, concurrency policies, tracked issue creation |
| Plugins | Out-of-process workers, capability gating, UI contributions |
| Company Portability | Export/import orgs with secret scrubbing and collision handling |

## Example usage

1. `npx paperclipai onboard --yes` — interactive setup
2. Create a company with a mission (e.g. "Build the #1 AI note-taking app to $1M MRR")
3. Hire agents: assign Claude Code as CTO, OpenClaw as CMO, Codex as engineer
4. Set per-agent monthly budgets
5. Approve CEO's strategy; agents begin running on heartbeat schedule
6. Monitor work, costs, and decisions from the dashboard (or mobile)

## Maintenance status

Actively maintained: v2026.416.0 released ~10 days ago; 59k stars; MIT license. Community on Discord. Roadmap includes Clipmart (pre-built company templates), cloud deployments, memory/knowledge subsystem, CEO Chat, and MAXIMIZER MODE.
