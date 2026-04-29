---
type: source
source_url: https://www.langchain.com/
parent_slug: langchain.com
tags:
  - no-code-agents
  - approvals
  - sub-agents
  - integrations
  - long-term-memory
related: []
product: fleet
detail_level: deep
created: 2026-04-29
updated: 2026-04-29
---

Fleet is the no-code agent product inside the LangChain platform. It packages AI agents as configurable business tools rather than developer libraries, combining templates, integrations, channels, memory, approvals, and LangSmith-backed traces so teams can automate recurring work without building every agent in code.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## What it does

Fleet lets users create and manage AI agents that run routine workflows across business tools. The docs emphasize creating agents from templates, connecting apps, triggering work from chat or external channels like Slack, and using approvals to keep humans in control of important actions.

## Key features

- No-code agent creation and management.
- Workspace-level and per-agent tool integrations.
- Channels for chat, scheduled, or event-driven agent execution.
- Human approvals, agent instructions, and self-updates.
- Long-term memory and sub-agent support.
- Starter templates for common use cases.

## Architecture and concepts

Fleet's core model is a configurable agent surface layered over LangSmith infrastructure. Agents have identity, instructions, tools, channels, memory, sub-agents, and traces. Long-term memory can live in files such as `AGENTS.md`, `tools.json`, `subagents/*`, and `skills/*`, while runtime memory can be written into a memories folder so agents improve across future runs.

The docs also show that Fleet mixes centralized and per-agent configuration. Tools can be added globally from the workspace integrations tab or locally inside a specific agent editor, and templates provide reusable starting bundles of prompts, tools, and optional channels that users can clone and customize.

## Main APIs

Fleet is primarily presented through the LangSmith UI rather than through one code-first library. The main interfaces in the captured docs are the Fleet integrations tab, the agent editor, template cloning flows, custom model configuration for OpenAI- or Anthropic-compatible APIs, and remote MCP server connections that broaden the available tool surface.

## When to use

- You want business users or ops teams to build agents without starting from a codebase.
- You need approvals, channels, and integrations more than low-level orchestration primitives.
- You want reusable agent templates for common workflows like email, recruiting, or incident response.
- You need persistent memory and sub-agent patterns but prefer a managed UI over a library-first approach.

## Ecosystem

Fleet is tightly coupled to LangSmith. It inherits LangSmith organization settings and data handling, uses LangSmith tracing for execution visibility, supports MCP-based extensions, and complements the code-first LangChain and LangGraph products by giving non-developer teams a managed agent surface.
