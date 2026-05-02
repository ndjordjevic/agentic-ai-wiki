---
type: overview
domain: "Agentic AI Frameworks"
created: 2026-04-28
updated: 2026-05-02
sources:
  - "[[paperclip.ing]]"
  - "[[modelcontextprotocol-servers-tree-main-src-sequentialthinking]]"
  - "[[langchain.com]]"
  - "[[langchain.com-langsmith]]"
  - "[[langchain.com-fleet]]"
  - "[[langchain.com-langchain]]"
  - "[[langchain.com-langgraph]]"
  - "[[langchain.com-deepagents]]"
  - "[[runcabinet.com]]"
  - "[[skills.sh]]"
  - "[[canva.com]]"
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

[[runcabinet.com]] introduces Cabinet, a free and open-source self-hosted AI-first startup OS where all knowledge lives as markdown files on disk. It bridges the gap between note-taking tools (Obsidian, Notion) and agent orchestration platforms (Paperclip) by combining a WYSIWYG knowledge base, 20 pre-built AI agent templates with cron-based scheduling, embedded live HTML apps, a browser-based web terminal, and git-backed version history — all without a database or vendor lock-in. Cabinet operationalizes Andrej Karpathy's LLM-wiki pattern as a product, positioning itself as the persistent memory layer for both human and AI work in a self-hosted startup OS.

[[skills.sh]] covers the open agent skills directory and ecosystem built by Vercel, which provides the de-facto distribution layer for SKILL.md-based capability modules across 50+ AI coding agents. The source captures the leaderboard (community-ranked by anonymous install telemetry), the official skills registry (70+ technology vendors publishing skills directly, including Anthropic, Microsoft, GitHub, OpenAI, Sentry, and Cloudflare), a security audit dashboard, and the full CLI reference for `npx skills` backed by the open-source `vercel-labs/skills` repo. It adds a concrete picture of how procedural knowledge is packaged, discovered, and installed across the multi-agent tooling ecosystem referenced throughout this wiki.

[[canva.com]] documents Canva as an AI-powered visual design platform with a developer layer directly relevant to agentic AI workflows. Its remote MCP server (`https://mcp.canva.com/mcp`) exposes design generation, editing, asset management, and export as MCP-compatible tools consumable by Claude, ChatGPT, Codex, Gemini, Cursor, and VS Code agents. The Connect APIs enable external platforms to embed Canva capabilities via REST (autofill brand templates, bulk create, resize, export, comments), and the Apps SDK allows JavaScript plugins to run inside the Canva editor. This source is notable as a concrete example of an established SaaS product opening its design capabilities to AI agents through the Model Context Protocol.
