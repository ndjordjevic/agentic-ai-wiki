---
type: overview
domain: "Agentic AI Frameworks"
created: 2026-04-28
updated: 2026-04-29
sources:
  - "[[paperclip.ing]]"
  - "[[modelcontextprotocol-servers-tree-main-src-sequentialthinking]]"
  - "[[langchain.com]]"
  - "[[langchain.com-langsmith]]"
  - "[[langchain.com-fleet]]"
  - "[[langchain.com-langchain]]"
  - "[[langchain.com-langgraph]]"
  - "[[langchain.com-deepagents]]"
---

# Agentic AI Frameworks — overview

[[paperclip.ing]] introduces Paperclip, an open-source control plane for running autonomous AI-agent companies. It sits above agent runtimes like Claude Code, Codex, Cursor, OpenClaw, bash agents, and HTTP bots and provides the organizational layer those runtimes lack: an org chart with hierarchical reporting, a heartbeat execution loop that wakes agents on schedule, an atomic ticket system with checkout locks, per-agent budget enforcement with hard stops, board-level governance and approval gates, and complete multi-company data isolation in a single Node.js + React deployment. The source also shows how Paperclip packages this operating model into both a public product site and a companion GitHub repo with a built-in heartbeat skill, plugin system, portability features, and an actively maintained roadmap.

[[modelcontextprotocol-servers-tree-main-src-sequentialthinking]] documents the Sequential Thinking MCP Server, a focused MCP server that exposes a single `sequential_thinking` tool for structured, revisable, branching reasoning inside an MCP-aware host. The source captures the tool's input schema, the intended problem-solving workflow, practical verification steps, and concrete installation patterns for Claude Desktop, VS Code, Codex CLI, NPX, and Docker.

[[langchain.com]] reframes LangChain as a multi-product agent-engineering platform rather than just a library. The umbrella source ties together [[langchain.com-langsmith]], [[langchain.com-fleet]], [[langchain.com-langchain]], [[langchain.com-langgraph]], and [[langchain.com-deepagents]] and shows how observability, no-code business agents, higher-level framework primitives, lower-level orchestration, and an autonomous agent harness are positioned as one integrated stack.

[[langchain.com-langsmith]] adds the operational layer to the wiki's agentic AI coverage: framework-agnostic tracing, offline and online evaluation loops, deployment options, Agent Server runtime architecture, and the production feedback cycle that turns traces into datasets and redeployable improvements. It is especially useful for understanding how agent teams move from experimentation to monitored production systems.

[[langchain.com-fleet]] contributes the no-code side of the LangChain ecosystem. It covers business-facing agents built from templates, integrations, channels, approvals, long-term memory files, and sub-agents, showing how LangChain's platform story extends beyond developer libraries into managed agent operations for non-engineering teams.

[[langchain.com-langchain]] documents the high-level open-source framework path: `create_agent`, model and tool abstractions, middleware-based dynamic routing, and the batteries-included approach to getting useful agents running quickly. It complements the lower-level orchestration material elsewhere in the wiki by covering the higher-abstraction starting point for code-first agent development.

[[langchain.com-langgraph]] captures the runtime-oriented end of the stack: explicit state graphs, durable execution, interrupt-driven human-in-the-loop patterns, workflow topologies like routing and orchestrator-worker, and thread-based resumption semantics. It adds a strong reference point for stateful, long-running agent systems that need more control than a single high-level agent loop.

[[langchain.com-deepagents]] adds the agent-harness layer to the wiki, completing the three-tier open-source stack under LangChain. It covers the Deep Agents SDK — a batteries-included framework built on LangGraph that adds planning with `write_todos`, file-system context management, subagent spawning, and long-term memory — together with the Deep Agents CLI, a terminal coding agent built on the same SDK. This is a new product added to the platform since the initial ingest.
