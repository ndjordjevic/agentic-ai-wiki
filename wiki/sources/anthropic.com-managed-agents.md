---
type: source
category: "Agent frameworks & SDKs"
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
parent_slug: anthropic.com
tags:
  - managed-agents
  - long-running-agents
  - multi-agent
  - harness-design
  - planner-generator-evaluator
  - autonomous-coding
  - context-resets
  - agent-sdk
related:
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
  - langchain.com-langgraph
  - njbrake-agent-of-empires
  - shareai-lab-learn-claude-code
  - gsd-build-get-shit-done
  - coleam00-archon
  - snarktank-ralph
  - how-claude-code-works-in-large-codebases
product: managed-agents
detail_level: deep
created: 2026-05-14
updated: 2026-07-01
---

Claude Managed Agents is Anthropic's fully managed agentic infrastructure on the [[anthropic.com]] platform: a pre-built harness with secure cloud containers, built-in context compaction, server-side session persistence, and multi-agent orchestration, so developers configure agent behavior rather than build and operate the execution layer. The primary source for this page is Anthropic's engineering article on harness design for long-running apps, which documents Anthropic's own experiments building complex harnesses on top of this infrastructure.

_All claims below are sourced from ../../raw/web/anthropic.com.md unless otherwise noted._

## What it does

Claude Managed Agents provides the complete runtime for autonomous Claude sessions. You define an **Agent** (model, system prompt, tools, MCP servers, skills), configure an **Environment** (container with pre-installed packages and network access rules), and start a **Session** (a running agent instance within that environment). The agent autonomously executes tools — bash, file ops, web search/fetch, MCP servers — streaming results back as server-sent events. Event history is persisted server-side and queryable in full. You can steer or interrupt mid-execution by sending additional events to the running session.

The platform is currently in beta (`managed-agents-2026-04-01` header required; SDK sets it automatically).

## Key features

- **Managed execution loop** — no agent-loop code to write; Anthropic's harness handles tool dispatch, error recovery, and result streaming
- **Secure cloud containers** — pre-installed packages (Python, Node.js, Go, etc.), configurable network access rules, persistent filesystem within a session
- **Automatic context compaction** — the SDK compacts growing context windows in-place; Opus 4.6+ rarely needs full context resets
- **Multi-agent orchestration** — one coordinator agent delegates to a roster of specialized sub-agents via session threads; each thread is context-isolated but shares the container filesystem
- **Stateful session persistence** — conversation history and event stream persisted server-side; queryable at any time
- **MCP server integration** — connect external tool providers without building custom tool wrappers
- **Agent Skills** — modular SKILL.md-based capability modules available inside managed sessions

## Architecture and concepts

Four core concepts compose every Managed Agents deployment:

| Concept | Description |
|---|---|
| **Agent** | Model, system prompt, tools, MCP servers, and skills — the agent's identity and capabilities |
| **Environment** | Container template: packages, network access, mounted files |
| **Session** | A running agent instance within an environment; produces a persistent event stream |
| **Events** | User turns, tool results, and status updates exchanged between the application and the agent |

### Multi-agent orchestration

Multi-agent sessions run one **coordinator** agent in the **primary thread** (the session-level event stream). The coordinator can spawn **session threads** — each thread is its own context-isolated event stream backed by a sub-agent. Threads share the same container and filesystem. Coordination patterns:

- **Parallelization:** fan out independent subtasks; coordinator synthesizes results
- **Specialization:** route to domain-focused agents (security, documentation, QA) instead of loading one agent with every capability
- **Escalation:** consult a more capable model for a subset of complex subtasks

Threads are persistent across the session: a coordinator can send follow-ups to previously delegated agents, which retain their full prior context. Up to 20 unique agents in the roster; up to 25 concurrent threads per session.

### Harness design findings (from Anthropic's engineering research)

The engineering article that is the primary source of this page documents Anthropic's experiments building harnesses on the Managed Agents SDK. Two key failure modes were identified in naive long-running agent implementations:

**Context anxiety** — as the context window fills, models change behavior: they rush through steps, declare tasks done prematurely, and wrap up early. Sonnet 4.5 exhibited this even with context compaction active, because compaction does not start from a clean slate. The solution was context resets: terminate the agent, start a fresh session, carry state in a structured handoff artifact. Opus 4.6's improved long-context retrieval largely eliminated context anxiety, making continuous sessions with automatic compaction viable.

**Poor self-evaluation** — agents reliably praise their own work even when it is mediocre or broken. An external evaluator agent, tuned to be skeptical, is far more tractable than making a generator self-critical.

The resulting architecture — inspired by Generative Adversarial Networks (GANs) — uses three agents:
1. **Planner** — expands a terse 1-4 sentence prompt into a full product spec; emphasizes high-level deliverables, not implementation details; weaves in AI feature opportunities
2. **Generator** — builds the product against the spec; works in sprints (Sonnet 4.5 era) or in a continuous session (Opus 4.6); self-evaluates before handing off
3. **Evaluator** — uses Playwright MCP to interact with the running application as a user would; grades against explicit criteria (functionality, visual design, code quality, product depth); each criterion has a hard threshold

Sprint contracts (pre-build negotiation between generator and evaluator on what "done" looks like) bridge the gap between high-level spec and testable implementation. Communication between agents is file-based: one agent writes, the other reads and responds.

**Results:**
- Retro game maker (Opus 4.5, full harness): 6 hr, $200 — functional game vs. solo run's non-functional $9 output
- DAW (Opus 4.6, simplified harness): 3 hr 50 min, $124 — working browser-based music production app in three build/QA cycles

**Harness evolution principle:** every harness component encodes an assumption about what the model cannot do on its own. Those assumptions go stale as models improve. The right practice: experiment with the current model, read its traces on realistic problems, strip away components that are no longer load-bearing, and add new components to reach greater capability.

## Main APIs

- `POST /v1/agents` — create an agent (define model, system prompt, tools, MCP servers, skills)
- `POST /v1/environments` — create an environment (container config)
- `POST /v1/sessions` — start a session (reference agent and environment)
- `GET /v1/sessions/:id/events/stream` — stream events from the primary thread (SSE)
- `GET /v1/sessions/:id/threads` — list session threads (multi-agent)
- `GET /v1/sessions/:id/threads/:thread_id/events/stream` — stream a specific thread

Rate limits: 300 req/min create endpoints, 600 req/min read endpoints (per organization). SDK available in Python and TypeScript.

## When to use

Use Claude Managed Agents when you need: long-running autonomous execution (minutes to hours); secure cloud containers without managing your own sandbox infrastructure; stateful sessions where history must survive across application restarts; or multi-agent workflows with specialized sub-agents. For tasks that require custom tool execution with fine-grained control over every turn, the [[anthropic.com-messages]] Messages API is the better fit. For harness patterns that wrap Claude Code rather than the API, see [[njbrake-agent-of-empires]] (session management) and [[shareai-lab-learn-claude-code]] (harness engineering curriculum).

## Ecosystem

Claude Managed Agents integrates with the Model Context Protocol (MCP) for connecting external tool providers, and with the Agent Skills system shared with Claude Code and the Messages API. The [[anthropics-skills]] repo ships the `frontend-design` skill referenced in the harness article. [[langchain.com-langgraph]] covers the open-source alternative for stateful, long-running agent graphs when you need to self-host the orchestration layer. The harness engineering concepts documented here (context resets, context anxiety, adversarial evaluation) are covered in video form in [[9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint]].
