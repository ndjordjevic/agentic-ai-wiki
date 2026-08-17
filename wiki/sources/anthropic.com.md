---
type: source
category: "Agent frameworks & SDKs"
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
subpages:
  - anthropic.com-messages
  - anthropic.com-managed-agents
tags:
  - anthropic
  - claude-api
  - agentic-platform
  - multi-agent
  - harness-design
  - agent-skills
  - long-running-agents
related:
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
  - anthropics-skills
  - anthropics-claude-agent-sdk-python
  - langchain.com
  - the-new-sdlc-with-vibe-coding
product: anthropic.com
detail_level: deep
created: 2026-05-14
updated: 2026-06-30
---

Anthropic is an AI safety company that offers the Claude model family and a two-surface developer platform: the **Messages API** for custom agent loops with direct model access, and **Claude Managed Agents** for fully managed, long-running agentic infrastructure. The engineering blog documents first-party harness research, most notably a GAN-inspired multi-agent architecture (planner + generator + evaluator) for building complex applications autonomously over multi-hour sessions.

_All claims below are sourced from ../../raw/web/anthropic.com.md unless otherwise noted._

## Products

- [[anthropic.com-messages]] — Direct model access via the Messages API; custom agent loops, tool use, and Agent Skills for modular capability extension.
- [[anthropic.com-managed-agents]] — Pre-built managed agent harness for long-running autonomous tasks; multi-agent orchestration, secure containers, and stateful sessions.

## Architecture

Anthropic's developer platform is split into two surfaces designed for different levels of control and infrastructure ownership. The Messages API gives developers direct access to Claude models — they own the agent loop, tool orchestration, and state management. Claude Managed Agents flips this: Anthropic provides the harness, container runtime, event streaming, and session persistence so developers can focus on agent configuration (model, system prompt, tools, MCP servers, skills) rather than infrastructure.

Agent Skills are a cross-cutting feature: modular SKILL.md-based capability modules that work across both surfaces — in Claude Code, Claude.ai, and the Claude API. They use progressive disclosure (Level 1 metadata always loaded; Level 2 instructions loaded on demand; Level 3 bundled scripts/resources loaded as needed) to minimize context overhead while providing deep domain expertise on demand.

The engineering blog documents harness research conducted on the Managed Agents surface using the Claude Agent SDK, including a three-agent architecture (planner → generator → evaluator) that produced rich full-stack applications over multi-hour autonomous runs.

## When to use the platform

Use the **Messages API** when you need fine-grained control over the conversation loop, custom tool execution, or want to wire Claude into an existing infrastructure stack. Use **Claude Managed Agents** when you need long-running autonomous execution (minutes to hours), do not want to manage containers or agent loops yourself, or require stateful session history and built-in context compaction. Both surfaces are well-suited for agentic AI workflows; the choice depends on how much infrastructure you want to own.

## Documentation

Documentation lives at [docs.anthropic.com](https://docs.anthropic.com), organized into two main subsections corresponding to the two developer surfaces: `build-with-claude` (Messages API, Agent Skills, tools, features) and `managed-agents` (Managed Agents harness, multi-agent orchestration, events/streaming). The engineering blog at `anthropic.com/engineering` publishes original harness research including the multi-agent harness design, context engineering, and context anxiety posts referenced in [[9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint]].
