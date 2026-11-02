---
type: source
category: "Agent frameworks & SDKs"
studied: true
source_url: https://docs.anthropic.com
subpages:
  - anthropic.com-messages
  - anthropic.com-managed-agents
tags:
  - anthropic
  - claude-api
  - agentic-platform
  - multi-agent
  - agent-skills
  - managed-agents
  - messages-api
related:
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
  - anthropics-skills
  - anthropics-claude-agent-sdk-python
  - langchain.com
  - the-new-sdlc-with-vibe-coding
product: anthropic-developer-platform
detail_level: deep
created: 2026-05-14
updated: 2026-11-02
---

**Anthropic's developer platform** (umbrella) — Claude for building agents via two surfaces: the **Messages API** (you own the loop) and **Claude Managed Agents** (Anthropic runs the harness). This page is the hub that ties those products together; deep harness-design research lives on [[anthropic.com-managed-agents]] and in video form on [[9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint]].

_All claims below are sourced from ../../raw/web/anthropic.com.md unless otherwise noted._

## Products

- [[anthropic.com-messages]] — Direct model access via the Messages API; custom agent loops, tool use, and Agent Skills for modular capability extension.
- [[anthropic.com-managed-agents]] — Pre-built managed agent harness for long-running autonomous tasks; multi-agent orchestration, secure containers, and stateful sessions.

## Architecture

Anthropic's developer platform is split into two surfaces designed for different levels of control and infrastructure ownership. The Messages API gives developers direct access to Claude models — they own the agent loop, tool orchestration, and state management. Claude Managed Agents flips this: Anthropic provides the harness, container runtime, event streaming, and session persistence so developers can focus on agent configuration (model, system prompt, tools, MCP servers, skills) rather than infrastructure.

Agent Skills are a cross-cutting feature: modular SKILL.md-based capability modules that work across both surfaces — in Claude Code, Claude.ai, and the Claude API. They use progressive disclosure (Level 1 metadata always loaded; Level 2 instructions loaded on demand; Level 3 bundled scripts/resources loaded as needed) to minimize context overhead while providing deep domain expertise on demand.

## When to use the platform

Use the **Messages API** when you need fine-grained control over the conversation loop, custom tool execution, or want to wire Claude into an existing infrastructure stack. Use **Claude Managed Agents** when you need long-running autonomous execution (minutes to hours), do not want to manage containers or agent loops yourself, or require stateful session history and built-in context compaction. Both surfaces are well-suited for agentic AI workflows; the choice depends on how much infrastructure you want to own.

## Documentation

Documentation lives at [docs.anthropic.com](https://docs.anthropic.com), organized into two main subsections corresponding to the two developer surfaces: `build-with-claude` (Messages API, Agent Skills, tools, features) and `managed-agents` (Managed Agents harness, multi-agent orchestration, events/streaming). First-party harness research for long-running agents is covered on [[anthropic.com-managed-agents]] and summarized in [[9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint]].
