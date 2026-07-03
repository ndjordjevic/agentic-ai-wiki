---
type: source
source_url: https://github.com/Gitlawb/openclaude
tags:
  - open-source-coding-agent
  - multi-provider-cli
  - provider-adapter
  - openai-compatible
  - local-model-support
  - agent-routing
  - grpc-server
  - typescript
related:
  - openrouter.ai
  - litellm.ai
  - snarktank-ralph
  - openai-codex-plugin-cc
  - happy.engineering
product: openclaude
detail_level: standard
created: 2026-05-27
updated: 2026-07-03
---

OpenClaude is an open-source coding-agent CLI (27,800+ stars) that ports the Claude Code terminal workflow to any model provider. It replaces Anthropic's backend with a descriptor-first integration layer, letting teams use OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Ollama, Atomic Chat, and other backends while keeping a single set of tools: bash, file read/write/edit, grep, glob, agents, tasks, MCP, and streaming slash commands. Sponsored by GitLawb, Bankr.bot, Atomic Chat, and Xiaomi MiMo and released under an open license, it is the primary community answer to "Claude Code, but with the model of my choice."

_All claims below are sourced from ../../raw/github/gitlawb-openclaude.md unless otherwise noted._

## What it does

OpenClaude wraps a coding-agent runtime (prompts, tool loops, streaming output) in a provider-agnostic shell. The user installs `@gitlawb/openclaude` via npm, points it at any OpenAI-compatible endpoint or uses the in-app `/provider` wizard, and gets the full Claude Code–style workflow — bash execution, file editing, grep/glob search, multi-step agent tasks, MCP servers, and web tools — regardless of which model is running underneath.

## Key features

- **Provider breadth**: OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, Gitlawb Opengateway, Xiaomi MiMo, Bedrock, Vertex, Foundry — configured via `/provider` wizard or environment variables.
- **Agent routing**: Per-agent model routing via `~/.openclaude.json`. Map named agent types (`Explore`, `Plan`, `general-purpose`, `frontend-dev`) to different model endpoints; unmatched agents fall back to the global provider.
- **Tool-complete coding loop**: Bash, file read/write/edit, grep, glob, agents, tasks, MCP, and web tools work uniformly across providers.
- **Headless gRPC server**: Run the engine as a gRPC service on `localhost:50051`; bidirectional streaming delivers text chunks, tool calls, and permission prompts. `src/proto/openclaude.proto` enables client generation in Python, Go, Rust, etc.
- **DuckDuckGo web search fallback**: Non-Anthropic models get free web search via DuckDuckGo; Firecrawl is available for JS-rendered pages.
- **VS Code extension**: Included at `vscode-extension/openclaude-vscode` — launch integration, provider-aware control-centre UI, theme support.

## Architecture

OpenClaude's provider system is **descriptor-first**. Descriptors in `src/integrations/` define vendors, gateways, brands, model catalogs, validation hints, discovery strategy, and transport capability flags. The registry (`src/integrations/index.ts`, `registry.ts`) loads those descriptors and exposes route/model lookups. Runtime metadata (`routeMetadata.ts`, `runtimeMetadata.ts`) bridges descriptor state into request execution without maintaining a separate per-provider switch.

`transportConfig.kind` is the routing contract: `local`, `openai-compatible`, `anthropic-proxy`, `bedrock`, `vertex`, or another supported transport family. Gateway `category` (local/hosted/aggregating) is display metadata only — runtime selection must key off `transportConfig.kind`.

Several intentional long-term exceptions exist for real protocol divergence: GitHub dual-mode transport (Anthropic-native for Claude models, OpenAI/Codex for Copilot traffic), Mistral request shaping, Azure auth/deployment contracts, Gemini credential handling, DeepSeek/Moonshot `reasoning_content` shaping, Bedrock/Vertex/Foundry dedicated SDK flows, and Anthropic-native thinking block preservation during conversation recovery.

## Installation

```bash
npm install -g @gitlawb/openclaude
```

Alternatively, build from source with Bun 1.3.13+:

```bash
git clone https://github.com/Gitlawb/openclaude.git
cd openclaude && bun install && bun run build && npm link
```

Guides for non-technical users, Windows, macOS/Linux, Android, and advanced setups are in `docs/`.

## Example usage

```bash
# Quickest OpenAI path
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_API_KEY=sk-your-key-here
export OPENAI_MODEL=gpt-4o
openclaude

# Local Ollama model
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_MODEL=qwen2.5-coder:7b
openclaude

# Inside OpenClaude: guided provider setup
/provider

# Headless gRPC server
npm run dev:grpc
```

## When to use

Use OpenClaude when you want the Claude Code agent loop (tool-driven coding, multi-step tasks, MCP) but need to run against a non-Anthropic model — whether for cost, compliance, latency, or access reasons. Agent routing makes it especially suitable for teams that want to split workloads across cheap fast models and expensive strong models. The gRPC server mode is the right fit when embedding OpenClaude's engine in a CI pipeline or custom UI.

## Maintenance status

27,861 stars and 8,625 forks as of 2026-05-27. Latest release v0.15.0 shipped 2026-05-26 — actively maintained with frequent releases. Sponsored by four organisations (GitLawb, Bankr.bot, Atomic Chat, Xiaomi MiMo). Licensed under "Other" (see LICENSE — originated from the Claude Code codebase; not affiliated with or endorsed by Anthropic).
