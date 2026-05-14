---
type: source
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
parent_slug: anthropic.com
tags:
  - messages-api
  - claude
  - tool-use
  - agent-skills
  - direct-api
  - custom-agent-loops
  - function-calling
related:
  - anthropics-skills
  - nidhinjs-prompt-master
product: messages
detail_level: deep
created: 2026-05-14
updated: 2026-05-14
---

The Messages API is Anthropic's direct model-access surface for building Claude-powered applications. Developers construct every conversation turn, manage state, and write their own tool loop — giving maximum control and flexibility for custom agent architectures. It is the foundation for the Agent Skills system, which layers modular, on-demand capability modules on top of the raw API.

_All claims below are sourced from ../../raw/web/anthropic.com.md unless otherwise noted._

## What it does

The Messages API provides synchronous and batch access to Claude models. Callers send structured message arrays with optional tool definitions; Claude returns completions that may include tool call requests the caller resolves. The API supports text and image input, multi-turn conversation, system prompts, structured outputs, extended thinking (Sonnet 4.6+), and prompt caching. It is available through the Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI, and Microsoft Foundry.

## Key features

- **Tool use / function calling** — define tools with JSON schemas; Claude issues tool_use content blocks that callers resolve and feed back as tool_result blocks
- **Agent Skills** — modular SKILL.md-based capability modules with progressive three-tier loading (metadata → instructions → resources/scripts), reusable across sessions without context penalty
- **Extended thinking** — available on Sonnet 4.6+; lets Claude reason through complex problems before responding
- **Batch processing** — Message Batches API for high-throughput, cost-optimized offline workloads
- **Prompt caching** — reduce cost and latency on repeated long system prompt prefixes
- **Vision** — all current Claude models accept image input

## Architecture and concepts

The Messages API is stateless: each request is a self-contained array of messages plus system prompt. State management, conversation persistence, and tool execution are the caller's responsibility. This gives full control but requires building the agent loop from scratch.

**Agent Skills** sit above the raw API and use the Claude model's filesystem access (via VM environment) to implement progressive disclosure. A Skill is a directory containing a `SKILL.md` with YAML frontmatter (`name:`, `description:`) and markdown instructions, optionally bundled with executable scripts and reference files. Loading levels:

| Level | Triggered | Token cost |
|---|---|---|
| Metadata (name + description) | Always, at startup | ~100 tokens per Skill |
| Instructions (SKILL.md body) | When Skill is triggered by request | Under 5k tokens |
| Resources and code (scripts, reference files) | On demand via bash | Effectively unlimited |

When Claude runs a bundled script, only the script's output enters the context window — the code itself does not. This makes skills far more efficient than having Claude generate equivalent logic on the fly. Pre-built Agent Skills cover PowerPoint, Excel, Word, and PDF; custom Skills can be created in Claude Code, uploaded via the Claude API, or added in claude.ai settings.

## Main APIs

- `POST /v1/messages` — single synchronous message turn
- `POST /v1/messages/batches` — batch processing (Message Batches API)
- `POST /v1/agent-skills` — upload and manage custom Agent Skills
- `GET /v1/models` — list available models with capabilities and token limits

SDK available in Python and TypeScript (and via REST). Authentication via `x-api-key` header.

## When to use

Use the Messages API when you need full control over the agent loop, custom tool execution pipelines, or integration with an existing infrastructure stack. It is the right choice for: one-off API calls, custom multi-agent orchestration you want to own, latency-sensitive applications requiring a specific control flow, and scenarios where you need to tightly budget token usage per turn. When you need the platform to manage the agent loop, container runtime, and session state for you, prefer [[anthropic.com-managed-agents]].

## Ecosystem

The Messages API is the integration layer for Anthropic's **Agent Skills** ecosystem, shared with Claude Code, Claude.ai, and Claude Platform. The [[anthropics-skills]] repository is the canonical reference for SKILL.md patterns and ships 17 production and example skills (including `frontend-design`, `skill-creator`, `mcp-builder`, and four document-processing skills). The [[skills.sh]] directory lists the broader community ecosystem of 289+ indexed skills from Anthropic and third-party publishers. Third-party frameworks like [[langchain.com-langchain]] and [[langchain.com-langgraph]] wrap the Messages API to provide higher-level abstractions for complex agent architectures.
