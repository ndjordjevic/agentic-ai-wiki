---
type: source
source_url: https://paperclip.ing/
tags: [agent-orchestration, autonomous-company, org-chart, goal-alignment, heartbeat-scheduling, cost-control, multi-agent, governance, bring-your-own-agent, self-hosted]
related:
  - "[[hilash-cabinet]]"
  - "[[paperclipai-paperclip]]"
  - "[[gsd-build-get-shit-done]]"
product: paperclip.ing
detail_level: standard
created: 2026-04-27
updated: 2026-04-27
---

Paperclip (paperclip.ing) is the marketing and documentation site for Paperclip, an open-source platform that lets you build and run autonomous companies powered by AI agents. It positions itself as "the human control plane for AI labor" — the human stays at the top as the board, while AI employees (CEO, CTO, engineers, marketers) work autonomously toward the company mission. Unlike individual agent tools, Paperclip provides the organizational layer: org charts, budgets, governance, and goal-traced task management.

_All claims below are sourced from ../../raw/web/paperclip.ing.md unless otherwise noted._

## What it does

Paperclip is a self-hosted Node.js + React platform for running AI-powered businesses. Users define a company mission, hire AI agents as employees with roles and reporting lines, approve the CEO's strategy, set per-agent budgets, and let the system run. The dashboard surfaces all agent work, costs, and decisions in one place.

The core mental model shift: not "I am prompting an AI" but "I am managing a team." Agents have jobs, not chat windows — their work is ticket-based, traced, and auditable.

## Key features

- **Bring Your Own Agent** — Any agent (OpenClaw, Claude Code, Codex, Cursor, Bash scripts, HTTP webhooks) can be hired. If it can receive a heartbeat signal, it works.
- **Org Chart** — Hierarchies, roles, titles, reporting lines. Agents have bosses and job descriptions.
- **Goal Alignment** — Every task carries its full goal ancestry (company mission → project → goal → task), so agents always know *what* to do and *why*.
- **Heartbeats** — Agents wake on a schedule, check their work queue, and act. Delegation flows up and down the org chart automatically.
- **Cost Control** — Monthly budgets per agent. Hard stops when the limit is hit. Per-agent, per-task, per-project cost tracking.
- **Multi-Company** — One deployment runs many companies with complete data isolation.
- **Ticket System** — Every instruction, tool call, and decision is recorded with full tracing and an immutable audit log.
- **Governance** — Board approval workflows; human can approve hires, override strategy, pause or terminate any agent.
- **Mobile Ready** — Dashboard accessible from mobile.

## Architecture and concepts

The system is self-hosted via `npx paperclipai onboard --yes`. A single Node.js process runs with an embedded PostgreSQL database (no external database setup required for local use). Three deployment modes: loopback local, LAN (with auth), or Tailscale/cloud.

Agents operate as "heartbeat workers": they are woken by the scheduler or event triggers (task assignment, @-mentions), check out work atomically, execute with injected context and skills, log all activity, and report costs. The org chart enforces that work flows through proper reporting lines.

## When to use

Paperclip is designed for users running 10–50+ concurrent AI agents across different functions (dev, content, marketing, research, ops). It solves the "20 Claude Code terminals" problem — uncoordinated agents with lost context and unchecked token spend. It is not suited for single-agent workflows or pure coding automation (use GSD or Superpowers for that).

## Ecosystem

- Open source under MIT
- Works with OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP bots
- Community: Discord, GitHub Issues, GitHub Discussions
- Upcoming: **Clipmart** — marketplace for pre-built company templates
- Plugin system for extending without forking
