# paperclip.ing

## Fetch log
- Inbox URL: https://paperclip.ing
- Final URL: https://paperclip.ing
- Fetched: 2026-04-28
- Pages: 6 (llms.txt + landing page + /docs + /docs/tutorials/ + /docs/explanation/ + /docs/reference/)

## llms.txt (if present)

# Paperclip

> The human control plane for AI labor.

Paperclip is an open-source platform that lets you build and run autonomous companies powered by AI agents. You define the goal, hire AI employees (CEO, CTO, engineers, designers, marketers), set budgets, and your business runs itself.

## Getting Started

GitHub: https://github.com/paperclipai/paperclip

Run this single command to set up Paperclip:

```
npx paperclipai onboard --yes
```

Interactive setup walks you through database configuration and creating your first company. No Paperclip account required. No agents installed automatically. Self-hosted. MIT licensed.

You can run Paperclip as a local instance or a remote deploy. Locally, a single Node.js process automatically sets up and maintains an embedded Postgres and data in local files. When you're ready for the cloud, Paperclip makes that easy too.

## How It Works

1. **Define the goal.** Set a company mission like "Build the #1 AI note-taking app to $1M MRR."
2. **Hire the team.** CEO, CTO, engineers, designers, marketers — any bot, any provider.
3. **Approve and run.** Review the CEO's strategy. Set budgets. Hit go. Monitor from the dashboard.

## Key Features

- **Bring Your Own Agent**: Any agent, any runtime, one org chart. Claude Code, OpenClaw, Python scripts, shell commands, HTTP webhooks — anything that can receive a heartbeat signal.
- **Org Chart**: Hierarchies, roles, reporting lines. Your agents have a boss, a title, and a job description.
- **Goal Alignment**: Every task traces back to the company mission. Agents know what to do and why.
- **Heartbeats**: Agents wake on a schedule, check work, and act. Delegation flows up and down the org chart.
- **Cost Control**: Monthly budgets per agent. When they hit the limit, they stop. No runaway costs.
- **Multi-Company**: One deployment, many companies. Complete data isolation. One control plane for your portfolio.
- **Ticket System**: Every conversation traced. Every decision explained. Full tool-call tracing and audit log.
- **Governance**: You're the board. Approve hires, override strategy, pause or terminate any agent at any time.

## What Paperclip Is

- An org chart for agents
- A governance layer where you sit at the top
- A cost control system with per-agent budgets
- Full observability with traced tickets and logged tool calls
- A multi-company runtime for running one or fifty AI businesses

## What Changes With Paperclip

Without Paperclip, you juggle agent tabs, lose context on reboot, manually gather context, re-invent task management between agents, and risk runaway token costs.

With Paperclip, tasks are ticket-based, context flows from goals to tasks automatically, org charts and delegation work out of the box, and cost tracking throttles agents when they exceed budgets.

## Source Code

The full source code is available on GitHub. You can browse the implementation, read the code directly, and contribute:

https://github.com/paperclipai/paperclip

## Links

- Website: https://paperclip.ing
- GitHub: https://github.com/paperclipai/paperclip

## Landing page — https://paperclip.ing

# Paperclip — The human control plane for AI labor

Hire AI employees, set goals, automate jobs and your business runs itself.

**Quickstart:** Open source. Self-hosted. Interactive setup walks you through database, auth, and your first company. No Paperclip account required.

```
$ npx paperclipai onboard --yes
```

### 3-step model

01. **Define the goal.** "Build the #1 AI note-taking app to $1M MRR."
02. **Hire the team.** CEO, CTO, engineers, designers, marketers — any bot, any provider.
03. **Approve and run.** Review the CEO's strategy. Set budgets. Hit go. Monitor from the dashboard.

### Key product claims (from testimonials and feature highlights)

- "OpenClaw is an employee, Paperclip is the company."
- Not a chatbot. Not an agent framework. Not a workflow builder. Not a prompt manager. Not a single-agent tool — this is for teams, hierarchies, companies.
- Works with: OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP webhooks. "If it can receive a heartbeat, it's hired."
- Mobile-ready dashboard for monitoring.

### Positioning (FAQ)

- Q: How is Paperclip different from agents like OpenClaw or Claude Code? A: Paperclip uses those agents. It orchestrates them into a company — with org charts, budgets, goals, governance, and accountability.
- Q: What happens when an agent hits its budget limit? A: At 100% utilization the agent auto-pauses and new tasks are blocked. Soft warning at 80%. Board can override.
- Q: Do agents run continuously? A: By default, Paperclip runs agents on scheduled heartbeats and/or notifications. Continuous agents like OpenClaw can also be hooked in.
- Q: Can I run multiple companies? A: Yes. A single deployment can run dozens of companies with complete data isolation.
- Q: Is Paperclip open source? A: Yes. MIT licensed, self-hosted, no account required.

### Advanced capabilities

- **Atomic execution**: task checkout and budget enforcement are atomic — no double-work, no runaway spend.
- **Persistent agent state**: agents resume same task context across heartbeats.
- **Runtime skill injection**: agents learn Paperclip workflows and project context at runtime without retraining.
- **Governance with rollback**: approval gates enforced, config changes revisioned.
- **Goal-aware execution**: tasks carry full goal ancestry.
- **Portable company templates**: export/import orgs, agents, skills with secret scrubbing.
- **True multi-company isolation**: every entity is company-scoped.

## Docs index — https://paperclip.ing/docs

Documentation organized with Diataxis (4 quadrants):

- **Tutorials** (`/docs/tutorials/`) — step-by-step walkthroughs from zero to working setup.
- **How-to Guides** (`/docs/how-to/`) — recipes for specific goals once you know the basics.
- **Reference** (`/docs/reference/`) — API surface, CLI flags, config knobs.
- **Explanation** (`/docs/explanation/`) — ideas behind Paperclip: why the control plane exists, how governance works.
- **Glossary** (`/docs/glossary/`)
- **Changelog** (`/changelog/`)

> Note: Docs are in active build-out — many sections are stubs at time of fetch.

## Tutorials — https://paperclip.ing/docs/tutorials/

Learning-oriented walkthroughs:
- Your first Paperclip company
- Hiring your first agent
- Running your first heartbeat

```
# Shape your first agent's AGENTS.md
paperclipai agent local-cli claudecoder --company-id <your-company-id>
```

## Explanation — https://paperclip.ing/docs/explanation/

Understanding-oriented context:
- Why the "human control plane for AI labor" framing
- How heartbeats, skills, and chains of command fit together
- The governance model — approvals, budgets, audit trails
- Trade-offs compared to building on agents directly

Key phrase from the docs: "Paperclip is not a single agent framework. It's the control plane you wrap around a team of them."

## Reference — https://paperclip.ing/docs/reference/

Information-oriented reference:
- REST API endpoints (`/api/...`)
- CLI commands and flags for `paperclipai`
- Skill manifest schema
- Agent `adapterConfig` fields

Reference is being generated from TypeScript types and CLI source. Until then, the authoritative references are the Paperclip heartbeat skill shipped with each install and the `paperclipai` CLI `--help` output.
