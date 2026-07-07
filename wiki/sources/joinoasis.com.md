---
type: source
source_url: https://www.teamoffsite.ai/
tags:
  - multi-agent-orchestration
  - no-code-agents
  - agent-guardrails
  - mcp-integration
  - agent-approval-gates
  - agent-memory
  - workflow-automation
related:
  - crewai.com
  - strandsagents.com
  - paperclip.ing
  - paperclipai-paperclip
  - app.sauna.ai
  - vellum.ai
product: joinoasis
detail_level: standard
created: 2026-06-18
updated: 2026-07-07
---

Oasis (joinoasis.com, formerly teamoffsite.ai, operated by Mercury Intelligence Inc.) is a no-code workspace for composing and operating coordinated AI agent teams. It positions itself as the production-ready runtime layer for teams that need to deploy multi-agent workflows in 30 seconds without writing orchestration code — shipping policies, approval gates, and Slack + iMessage hand-off as first-class features. The product is notable for publishing a rich developer-facing glossary under the `mercury.build` brand (which now redirects to joinoasis.com), covering foundational multi-agent concepts: agent guardrails, agent memory, computer use AI, multi-agent orchestration, reliable long-running agents, and the Model Context Protocol.

_All claims below are sourced from ../../raw/web/joinoasis.com.md unless otherwise noted._

## What it does

Oasis lets teams spin up coordinated AI agent teams through a no-code interface, with the core promise of a 30-second setup time. Agents run with policies and configurable approval gates so that irreversible actions (writes, external messages) require human sign-off before execution. Finished outputs are handed off via Slack or iMessage, keeping the human review loop in the channels teams already use. The platform also speaks MCP natively, allowing agents to connect to Gmail, Slack, Notion, and CRMs by toggling a connector rather than writing custom integration code.

## Key features

- **No-code agent team composition** — build and configure multi-agent workflows through a UI, not code.
- **Policies and approval gates** — per-tool allow/deny rules and mandatory approval on writes; the enforcement layer runs outside the agent and cannot be bypassed by the model.
- **Slack + iMessage hand-off** — agents deliver results and escalations directly into team messaging channels.
- **MCP-native tool calling** — MCP-compatible connectors for common SaaS tools; agents call tools through the same approval checkpoints as any other action.
- **Iteration caps and audit log** — configurable hard stops on unattended runs; an immutable per-iteration audit log of every tool call, reasoning step, and approval decision.
- **Agent memory across sessions** — episodic and semantic memory persisted across runs without a separate vector store setup.
- **Proton** — a second product listed in the site footer at `/proton`; details not available in the standard-level capture.

## Architecture and concepts

Oasis is built around three control surfaces: capability boundaries (what tools an agent can call), approval gates (which actions need human sign-off before execution), and an external state store (decision and tool-call history persisted outside the agent's context window). The enforcement layer is structurally isolated — the agent cannot read or modify its own guardrails. This design directly addresses the failure modes documented in the platform's glossary: agents that re-implement prior decisions, contradict earlier choices, or locate and modify their own constraint modules.

The multi-agent runtime runs planner and executor agents in a shared workspace. Every iteration is inspectable, and state persists between steps so long-running dispatches survive server restarts without a separate Postgres or queue. The glossary covers the conceptual underpinning: externalize state, isolate capabilities, cap iterations, mark side effects idempotent, and checkpoint with a durable execution engine (Temporal, Inngest, Restate are cited as comparable patterns).

## Main APIs

The standard-level capture does not expose a detailed API reference. The site advertises machine-readable entry points for agent integrations:
- `joinoasis.com/llms.txt` — site map for language models
- `joinoasis.com/llms-full.txt` — expanded index with full content
- `joinoasis.com/.well-known/agent-skills/index.json` — agent skills discovery index

## When to use

Use Oasis when a team needs multi-agent workflows in production without engineering custom orchestration, especially when audit trails, configurable approval gates, and revocable capabilities are required for security review or compliance sign-off. It fits use cases in engineering, sales, recruiting, and legal (all listed as target verticals). It is most relevant when the bottleneck is not building the agent but deploying it safely with human-in-the-loop oversight and integration into messaging tools already in use.

## Ecosystem

Oasis / Mercury Intelligence Inc. also operates:
- `mercury.build` (redirects to joinoasis.com) — brand under which the multi-agent platform and glossary are marketed to developers.
- `joinoasis.com/glossary` — a public developer-facing glossary covering agent guardrails, agent memory, computer use AI, multi-agent orchestration, long-running agent reliability, and MCP. The glossary is the primary SEO and education surface for the Mercury brand.
- Twitter/X: `@mercury_build`

The blog covers adjacent topics including Hermes Agent (Nous Research), no-code agent building tools (n8n, Lindy, Relevance AI, Make.com), and comparisons between AI agents and traditional automations.
