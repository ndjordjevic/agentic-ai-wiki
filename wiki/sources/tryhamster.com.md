---
type: source
source_url: https://tryhamster.com/
tags:
  - ai-native-sdlc
  - product-planning
  - team-alignment
  - briefs
  - task-management
  - ai-coding-agents
  - mcp-server
  - cli-tool
related:
  - www.taskmaster.one
  - eyaltoledano-claude-task-master
  - anombyte93-prd-taskmaster
product: tryhamster
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Hamster is an AI-native product planning platform built for teams where AI agents do the implementation work. It addresses the "velocity gap" — individual developers ship 10× faster with AI, but teams stall on alignment, unclear requirements, and context loss. Hamster closes that gap with two interconnected products: **Hamster Studio** (a collaborative brief-and-plan workspace for the whole product team) and **Taskmaster** (a CLI/MCP task-management tool for individual developers and AI agents). Together they implement an AI-native SDLC: Brief → Align → Plan → Execute → Ship. The platform is backed by 25K+ GitHub stars (via the open-source Taskmaster core) and used by teams at NVIDIA, Google, Vercel, Shopify, Lenovo, SAP, and other enterprises.

_All claims below are sourced from ../../raw/web/tryhamster.com.md unless otherwise noted._

## What it does

Hamster bridges the gap between a product idea and a shipped pull request, replacing sprint ceremonies with an AI-driven loop. A product manager or founder describes what they want in a **Brief** — a structured document capturing the reasoning, constraints, and customer context. Hamster Studio uses AI to refine that brief collaboratively, generates a structured **Plan** of parent tasks and subtasks with acceptance criteria, and then dispatches the plan to AI coding agents (via **Cloud Agents** or the Hamster CLI) that open PRs without manual handoff. The **Taskmaster** CLI handles the agent-side execution: it parses PRDs into a structured task graph with dependency ordering, complexity scoring, and TDD automation.

## Key features

**Hamster Studio:**
- **Briefs**: AI-native product documents — write what you want to build, AI fills in gaps, surfaces questions, and keeps the full team aligned. Briefs carry status (Draft → Refining → Aligned → Shipping → Done) and collect team alignment votes before delivery.
- **Real-time collaboration**: Multiple people edit briefs simultaneously with live cursors, @mentions, version history, and conversation branching.
- **Plan generation**: One click turns a brief into an ordered task breakdown with subtasks and acceptance criteria; tasks appear incrementally as they are generated.
- **Agent Context / CLI**: `hamster sync` writes briefs, plans, and tasks into a `.hamster/` directory in the repo as markdown files that any AI coding agent can read directly.
- **Blueprints**: Persistent English documents describing stable aspects of the business (products, systems, teams); Hamster draws on these every time it helps plan or write.
- **Connections**: Two-way sync with GitHub, Linear, Jira, Slack, Notion, Google Drive, Figma, and 35+ other tools; AI searches all connected sources when working on a brief.
- **MCP server**: Available at `docs/hamster-studio/mcp` for agent integrations.
- **Cloud Agents**: Dispatch a brief directly to a configured cloud AI agent; it reads the full plan context and opens a PR.

**Taskmaster:**
- **PRD → Tasks → Subtasks → Done**: Parse a product-requirements document (`tm parse-prd`) into a structured, dependency-ordered task graph stored in `.taskmaster/`.
- **Complexity analysis**: `tm analyze-complexity` scores each task 1–10 and recommends which to break down further.
- **Live research**: `tm research` queries current sources for up-to-date best practices and library versions beyond the model's training cutoff.
- **TDD Autopilot**: State machine automating the Red → Green → Refactor cycle — creates branches, runs tests, retries on failure, produces a PR.
- **Tagged task lists**: Branch-isolated task contexts; switch instantly with no merge conflicts.
- **BYOK / Local Mode**: Works offline with your own API keys (Anthropic, OpenAI, Gemini, Ollama). Compatible with Claude Code and Gemini CLI without a separate API key.
- **MCP server**: Native MCP integration for Cursor, VS Code, Windsurf, Claude Code, and any terminal.
- **Open source**: MIT licensed; 25K+ GitHub stars; core will always be free.

## Architecture and concepts

The AI-native SDLC implemented by Hamster has five stages: **Brief** (capture intent with AI assistance), **Align** (get stakeholder consensus in minutes via voting), **Plan** (AI generates structured tasks from briefs), **Execute** (AI agents implement the plan), **Ship** (measure outcomes against goals). Hamster Studio covers the first three stages; Taskmaster covers Execute; both contribute to Ship via PR and issue-tracker sync.

The **Context Graph** is Studio's central data model: an accumulated representation of a team's work, built from connected tools (GitHub, Slack, Linear, Jira, Figma, Notion, Google Drive, meeting transcripts). Every brief, plan, and blueprint is grounded in the Context Graph, so AI output always reflects actual company context rather than generic templates.

**Briefs** are the unit of work: one brief = one aligned, deliverable unit. The Brief workspace supports AI-assisted chat refinement, document versioning, @mentions, guided research, and a deliver button. **Plans** are generated from briefs — parent tasks with subtasks and acceptance criteria — and sync to the repo via the CLI so agents consume live context. **Blueprints** serve as long-lived company memory: vision, strategy, personas, and engineering standards documented once and referenced automatically.

The relationship between Studio and Taskmaster is layered: Taskmaster works standalone for solo developers with their own API keys; Studio adds team alignment, collaborative briefs, real-time editing, and shared plans on top. The same CLI bridges both — `hamster sync` pulls team briefs and plans into the repo for Taskmaster (and any other agent) to consume.

## Main APIs

- **Hamster CLI**: `hamster sync` — syncs briefs/plans/tasks to `.hamster/` in the repo; `hamster brief create` — creates briefs from the terminal; slash commands for common workflows.
- **Taskmaster CLI** (`tm`): `tm parse-prd <file>` — parses PRD into task graph; `tm analyze-complexity` — scores tasks; `tm research <query>` — live web research; `tm next` — shows the next task to work on; `tm start <id>` / `tm done <id>` — task lifecycle; `tm loop` — automation loop.
- **MCP server (Studio)**: Tools available at `docs/hamster-studio/mcp/available-tools`; connect at `docs/hamster-studio/mcp/getting-started`.
- **MCP server (Taskmaster)**: Native MCP integration described at `product/taskmaster/mcp-server`.
- **Install Taskmaster**: `curl -sSL https://tryhamster.com/cli/install | bash`

## When to use

Use Hamster Studio when a product team (PMs, designers, engineers, founders) needs to align on *what* to build before handing work to AI coding agents — especially when context loss between planning and implementation is causing agents to "build the wrong thing fast." Studio is most valuable when multiple stakeholders need to sign off on scope and the deliverable is a PR opened by an AI agent rather than a human.

Use Taskmaster alone when a solo developer needs structured, dependency-aware task management for AI coding agents and wants a lightweight CLI/MCP tool without team collaboration overhead. It works offline with any major LLM.

Use both together (the recommended path) when a team does collaborative planning in Studio and individual developers or autonomous agents execute tasks via Taskmaster, with the CLI keeping both in sync through the shared `.hamster/` and `.taskmaster/` directories in the repo.

## Ecosystem

Hamster and Taskmaster integrate with all major AI coding agents: Claude Code, Codex, Gemini CLI, Grok, Cursor, GitHub Copilot, Roo Code, Windsurf, Aider, Cline, Amp. Issue tracker integrations include Linear, Jira, and GitHub Issues with two-way sync. Knowledge/document integrations include Notion, Google Drive, and Figma. Communication integration is via Slack (meeting agent captures decisions automatically).

The open-source Taskmaster core (`eyaltoledano/claude-task-master` on GitHub — see [[eyaltoledano-claude-task-master]]) has 25K+ stars and 1.5M+ downloads; the hosted version with Hamster Studio adds team features on top. The [[www.taskmaster.one]] source covers the standalone Taskmaster product marketing site.
