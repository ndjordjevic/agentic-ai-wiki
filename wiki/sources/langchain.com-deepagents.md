---
type: source
source_url: https://docs.langchain.com/oss/python/deepagents/overview
parent_slug: langchain.com
tags:
  - agent-harness
  - deepagents
  - subagents
  - context-management
  - coding-agent
  - cli
  - langchain-platform
related:
  - langchain.com-langchain
  - langchain.com-langgraph
  - google.github.io
  - antigravity.google
  - adk.dev
product: deepagents
detail_level: deep
created: 2026-04-29
updated: 2026-06-06
---

Deep Agents is the [[langchain.com]] platform's batteries-included "agent harness" — an opinionated, higher-level SDK built on top of LangGraph that adds planning capabilities, file-system context management, subagent spawning, and long-term memory out of the box. It also ships the Deep Agents CLI, a terminal coding agent built on the same SDK. The docs classify it as a distinct layer from frameworks (LangChain) and runtimes (LangGraph), positioning it for complex, multi-step tasks that require autonomous planning and decomposition.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## What it does

The Deep Agents SDK is a standalone library built on top of LangChain's core building blocks, using the [[langchain.com-langgraph|LangGraph]] runtime for durable execution, streaming, and human-in-the-loop. It is the easiest way to start building agents with built-in capabilities for task planning, file systems for context management, subagent spawning, and long-term memory. The repo contains the Deep Agents SDK package, the Deep Agents CLI (a terminal coding agent), and an ACP integration for use in code editors like Zed.

The LangChain concepts page classifies it as an "agent harness" alongside Claude Agent SDK and Manus — distinct from frameworks (which provide abstractions and integrations) and runtimes (which provide durable execution infrastructure). Agent harnesses are for more autonomous agents and agents faced with complex, non-deterministic tasks.

## Key features

- **Task planning** — built-in `write_todos` tool for breaking down complex tasks into discrete, trackable steps.
- **File-system context management** — `read_file`/`write_file` tools to offload large results and manage context across long sessions; pluggable backends (in-memory, local disk, durable stores, sandboxes, or custom).
- **Subagent delegation** — `task` tool for spawning specialized subagents in parallel to keep context clean.
- **Long-term memory** — persistent memory across conversations and threads.
- **Human-in-the-loop** — require human approval for sensitive operations; toggleable auto-approve.
- **Context compaction** — `compact_conversation` tool for summarizing older messages and offloading originals when token budget fills.
- **Provider-agnostic** — model string uses `provider:model` format (`openai:gpt-5.4`, `anthropic:claude-sonnet-4-6`, `google_genai:gemini-3.1-pro-preview`, etc.).
- **Shell execution** — `execute` tool for running commands via sandbox backends.
- **Permission rules** — declarative control over which files agents can read or write.

## Architecture and concepts

Deep Agents sits at the top of the [[langchain.com|LangChain]] open-source stack. The architecture is: [[langchain.com-langchain|LangChain]] (model/tool abstractions) → [[langchain.com-langgraph|LangGraph]] (durable execution runtime) → Deep Agents SDK (harness layer with built-in tools, planning, and file system). Agents are created with `create_deep_agent(model=..., tools=[...], system_prompt=...)` and invoked with `agent.invoke({"messages": [...]})`.

When a deep agent runs, it automatically: plans its approach using `write_todos`; conducts tool calls using custom and built-in tools; manages context by writing large results to file system tools; spawns subagents as needed via the `task` tool; and synthesizes a final response. Built-in streaming via LangGraph allows real-time observation of tool calls, tool results, and LLM responses.

## Main APIs

- `create_deep_agent(model, tools, system_prompt)` — primary factory function.
- Built-in tools: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`, `execute`, `web_search`, `fetch_url`, `task`, `ask_user`, `compact_conversation`, `write_todos`.
- CLI command: `deepagents` (interactive) or `deepagents -y` (auto-approve mode).
- Slash commands in CLI: `/model`, `/agents`, `/remember`, `/skill:<name>`.
- ACP integration for connecting to code editors like Zed.

## When to use

- You want agents that can handle complex, multi-step tasks that require planning and decomposition.
- You need to manage large amounts of context through file system tools and summarization.
- You want to delegate work to specialized subagents for context isolation.
- You need persistent memory across conversations and threads.
- You want a terminal coding agent (Deep Agents CLI) for autonomous dev-environment tasks.
- For simpler agents: use LangChain's `create_agent` or build a custom LangGraph workflow instead.

## Ecosystem

Deep Agents is tightly coupled to the [[langchain.com|LangChain]] platform. It builds on [[langchain.com-langchain|LangChain]] (abstractions) and [[langchain.com-langgraph|LangGraph]] (runtime), integrates with [[langchain.com-langsmith|LangSmith]] for tracing and debugging, and is positioned as the code-first counterpart to [[langchain.com-fleet|Fleet]] (the no-code agent surface). The companion repo at `https://github.com/langchain-ai/deepagents` contains the SDK, CLI, and examples.
