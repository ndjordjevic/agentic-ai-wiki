---
type: overview
domain: "Agentic AI Frameworks"
created: 2026-04-28
updated: 2026-04-28
sources:
  - "[[paperclip.ing]]"
  - "[[modelcontextprotocol-servers-tree-main-src-sequentialthinking]]"
---

# Agentic AI Frameworks — overview

[[paperclip.ing]] introduces Paperclip, an open-source control plane for running autonomous AI-agent companies. It sits above agent runtimes like Claude Code, Codex, Cursor, OpenClaw, bash agents, and HTTP bots and provides the organizational layer those runtimes lack: an org chart with hierarchical reporting, a heartbeat execution loop that wakes agents on schedule, an atomic ticket system with checkout locks, per-agent budget enforcement with hard stops, board-level governance and approval gates, and complete multi-company data isolation in a single Node.js + React deployment. The source also shows how Paperclip packages this operating model into both a public product site and a companion GitHub repo with a built-in heartbeat skill, plugin system, portability features, and an actively maintained roadmap.

[[modelcontextprotocol-servers-tree-main-src-sequentialthinking]] documents the Sequential Thinking MCP Server, a focused MCP server that exposes a single `sequential_thinking` tool for structured, revisable, branching reasoning inside an MCP-aware host. The source captures the tool's input schema, the intended problem-solving workflow, practical verification steps, and concrete installation patterns for Claude Desktop, VS Code, Codex CLI, NPX, and Docker.
