---
type: source
source_url: https://paperclip.ing
companion_urls:
  - https://github.com/paperclipai/paperclip
raw_files:
  - ../../raw/web/paperclip.ing.md
  - ../../raw/github/paperclipai-paperclip.md
tags:
  - agent-orchestration
  - ai-company
  - multi-agent
  - heartbeat
  - org-chart
  - governance
  - cost-control
  - self-hosted
related:
  - paperclipai-paperclip
  - hilash-cabinet
  - runcabinet.com
  - skills.sh
  - njbrake-agent-of-empires
  - joinoasis.com
  - zaro.ai
product: paperclip
detail_level: standard
created: 2026-04-28
updated: 2026-07-03
---

Paperclip is an open-source Node.js + React control plane for running autonomous AI-agent companies. Rather than being an agent framework, it is the organizational layer around a team of agents — providing org charts, goal alignment, heartbeat scheduling, per-agent budgets, governance workflows, a full ticket system, and multi-company isolation. The product site and companion GitHub repo present the same core idea from two angles: operator-facing positioning on the web side and concrete server, UI, adapter, and skill implementation details on the GitHub side. (../../raw/github/paperclipai-paperclip.md)

_All claims below are sourced from ../../raw/web/paperclip.ing.md unless otherwise noted._

## What it does

Paperclip lets you build and run an AI-agent company by providing the organizational infrastructure around any set of agents. The mental model is three steps: define a company goal, hire AI agents into roles (CEO, CTO, engineers, etc.), then approve the strategy and let agents execute autonomously while you monitor from a dashboard. Paperclip positions itself explicitly as "if OpenClaw is an employee, Paperclip is the company."

It is not a chatbot, not an agent framework, not a workflow builder, and not a prompt manager. It is the control plane that sits above agent runtimes and gives them structure: task ownership, budget enforcement, hierarchical delegation, approval gates, and persistent session state.

## Key features

Paperclip's web-facing feature set centers on bring-your-own-agent compatibility, org charts, goal alignment, heartbeats, cost control, multi-company isolation, a traced ticket system, and governance. The site frames these as the missing company-level layer above individual agent runtimes and emphasizes practical operator outcomes like budget enforcement, auditability, and persistent coordination across many agents.

On the implementation side, the companion repo adds technical detail behind those product claims: atomic task checkout and budget enforcement, persistent agent state across heartbeats, runtime skill injection, governance with rollback, portable company templates, and company-scoped isolation enforced throughout the stack. (../../raw/github/paperclipai-paperclip.md)

## Architecture

Paperclip is implemented as a full control plane with 12 named server subsystems: Identity & Access, Org Chart & Agents, Work & Task System, Heartbeat Execution, Workspaces & Runtime, Governance & Approvals, Budget & Cost Control, Routines & Schedules, Plugins, Secrets & Storage, Activity & Events, and Company Portability. The repo is organized around these concerns with `server/` for the Express API and orchestration layer, `ui/` for the React + Vite board, and `packages/` for shared types, adapters, plugins, database schema, and the MCP server. (../../raw/github/paperclipai-paperclip.md)

The built-in `skills/paperclip/SKILL.md` shows how agents are expected to operate inside that architecture: short heartbeat runs, mandatory issue checkout before work, compact wake payloads for comment-driven runs, and a required `X-Paperclip-Run-Id` header on mutating API calls so each agent action is tied back to a specific run. That makes the heartbeat skill part of the system design, not just an add-on integration. (../../raw/github/paperclipai-paperclip.md)

## Installation

```bash
# Quickstart — embedded PostgreSQL auto-provisioned, no setup required
npx paperclipai onboard --yes

# With explicit binding
npx paperclipai onboard --yes --bind lan
npx paperclipai onboard --yes --bind tailnet

# Manual (from source)
git clone https://github.com/paperclipai/paperclip.git
cd paperclip && pnpm install && pnpm dev
```

Paperclip's recommended install path is `npx paperclipai onboard --yes`, which defaults to a trusted local first run. It also supports `--bind lan` and `--bind tailnet` presets for more explicit exposure modes. Manual setup from source uses `pnpm install` and `pnpm dev`, with Node.js 20+ and pnpm 9.15+, and dev mode auto-provisions embedded PostgreSQL/PGlite when `DATABASE_URL` is unset. (../../raw/github/paperclipai-paperclip.md)

## Example usage

The basic operator flow is to onboard a local instance, define a company goal, hire agents into roles, and then let those agents run on scheduled or event-driven heartbeats while you review strategy and intervene through governance controls. On the CLI side, the repo shows both the quickstart path and a local agent setup flow such as `paperclipai agent local-cli <agent-id> --company-id <id>` for installing the Paperclip heartbeat skill and exporting the needed environment variables. (../../raw/github/paperclipai-paperclip.md)

For development, the repo advertises `pnpm dev`, `pnpm build`, `pnpm typecheck`, `pnpm test`, `pnpm test:e2e`, `pnpm db:generate`, and `pnpm db:migrate` as the main workflows. The AGENTS guide also recommends cheap default verification through `pnpm test` and identifies `doc/GOAL.md`, `doc/PRODUCT.md`, `doc/SPEC-implementation.md`, `doc/DEVELOPING.md`, and `doc/DATABASE.md` as the core project documents to read first. (../../raw/github/paperclipai-paperclip.md)

## When to use

- You have many AI agents (Claude Code, Codex, OpenClaw, etc.) doing parallel work and need a unified control point.
- You need persistent task state that survives agent restarts.
- You need per-agent budget enforcement to avoid runaway costs.
- You want to run autonomous background work (recurring reports, customer support, triage) without manual kick-offs.
- You are building or operating a multi-product AI portfolio and need one dashboard across companies.
- Probably overkill for a single-agent hobby project.

## Maintenance status

Paperclip is actively maintained on GitHub: the companion repo was fetched at 59,894 stars, carries an MIT license, and had a latest release of `v2026.427.0` dated 2026-04-27. The public roadmap extends beyond the shipped core into cloud/sandbox agents, artifacts and work products, memory/knowledge, enforced outcomes, work queues, self-organization, automatic organizational learning, CEO chat, cloud deployments, and a desktop app. (../../raw/github/paperclipai-paperclip.md)

## Ecosystem

- **Plugins** — community plugins at [awesome-paperclip](https://github.com/gsxdsm/awesome-paperclip)
- **Clipmart** — coming soon: marketplace for pre-built company templates
- **MCP server** — `packages/mcp-server/` provides an MCP interface
- **Community** — Discord (`discord.gg/m4HZY7xNG3`), Twitter/X (`@papercliping`)
- **Telemetry** — anonymous, opt-out via `PAPERCLIP_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1`

## Documentation

The web docs are organized with a Diataxis-style split across tutorials, how-to guides, reference, and explanation pages. The captured docs index highlights tutorials for first-company setup and first heartbeat runs, explanation pages about the "human control plane for AI labor" model and governance trade-offs, and a reference area for REST API endpoints, CLI flags, skill manifests, and adapter configuration. The docs are still being built out, but they already show that Paperclip treats product positioning, operator workflow, and agent execution guidance as first-class documentation surfaces.
