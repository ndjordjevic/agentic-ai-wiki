# Gitlawb/openclaude

## Metadata
- Stars: 27861
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.15.0 (2026-05-26)
- License: Other
- Homepage: https://openclaude.gitlawb.com
- Fetched: 2026-05-27
- Final URL: https://github.com/Gitlawb/openclaude

## Description
runs anywhere. uses anything

## README
# OpenClaude

OpenClaude is an open-source coding-agent CLI for cloud and local model providers.

Use OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported backends while keeping one terminal-first workflow: prompts, tools, agents, MCP, slash commands, and streaming output.

OpenClaude is also mirrored to GitLawb:
[gitlawb.com/node/repos/z6MkqDnb/openclaude](https://gitlawb.com/node/repos/z6MkqDnb/openclaude)

## Why OpenClaude

- Use one CLI across cloud APIs and local model backends
- Save provider profiles inside the app with `/provider`
- Run with OpenAI-compatible services, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported providers
- Keep coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools
- Use the bundled VS Code extension for launch integration and theme support

## Quick Start

### Install

```bash
npm install -g @gitlawb/openclaude
```

### Start

```bash
openclaude
```

Inside OpenClaude:

- run `/provider` for guided provider setup and saved profiles
- run `/onboard-github` for GitHub Models onboarding

### Fastest OpenAI setup

```bash
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_API_KEY=sk-your-key-here
export OPENAI_MODEL=gpt-4o

openclaude
```

### Fastest local Ollama setup

```bash
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_MODEL=qwen2.5-coder:7b

openclaude
```

## Supported Providers

| Provider | Setup Path | Notes |
| --- | --- | --- |
| OpenAI-compatible | `/provider` or env vars | Works with OpenAI, OpenRouter, DeepSeek, Groq, Mistral, LM Studio, and other compatible `/v1` servers |
| Hicap | `/provider` or OpenAI-compatible env vars | Uses `api-key` auth, discovers models from unauthenticated `/models`, and supports Responses mode for `gpt-` models |
| Gemini | `/provider` or env vars | Supports API key only |
| GitHub Models | `/onboard-github` | Interactive onboarding with saved credentials |
| Codex OAuth | `/provider` | Opens ChatGPT sign-in in your browser and stores Codex credentials securely |
| Codex | `/provider` | Uses existing Codex CLI auth, OpenClaude secure storage, or env credentials |
| Gitlawb Opengateway | `/provider` or zero-config fallback | Free smart gateway at `https://opengateway.gitlawb.com/v1`; routes Xiaomi MiMo and GMI Cloud partner models by `OPENAI_MODEL` |
| Xiaomi MiMo | `/provider` or env vars | OpenAI-compatible API at `https://api.xiaomimimo.com/v1`; uses `MIMO_API_KEY` and defaults to `mimo-v2.5-pro` |
| Ollama | `/provider` or env vars | Local inference with no API key |
| Atomic Chat | `/provider`, env vars, or `bun run dev:atomic-chat` | Local Model Provider; auto-detects loaded models |
| Bedrock / Vertex / Foundry | env vars | Additional provider integrations for supported environments |

## What Works

- **Tool-driven coding workflows**: Bash, file read/write/edit, grep, glob, agents, tasks, MCP, and slash commands
- **Streaming responses**: Real-time token output and tool progress
- **Tool calling**: Multi-step tool loops with model calls, tool execution, and follow-up responses
- **Images**: URL and base64 image inputs for providers that support vision
- **Provider profiles**: Guided setup plus saved user-level provider profile support
- **Local and remote model backends**: Cloud APIs, local servers, and Apple Silicon local inference

## Agent Routing

OpenClaude can route different agents to different models through settings-based routing. This is useful for cost optimization or splitting work by model strength.

Add to `~/.openclaude.json`:

```json
{
  "agentModels": {
    "deepseek-v4-flash": {
      "base_url": "https://api.deepseek.com/v1",
      "api_key": "sk-your-key"
    },
    "gpt-4o": {
      "base_url": "https://api.openai.com/v1",
      "api_key": "sk-your-key"
    }
  },
  "agentRouting": {
    "Explore": "deepseek-v4-flash",
    "Plan": "gpt-4o",
    "general-purpose": "gpt-4o",
    "frontend-dev": "deepseek-v4-flash",
    "default": "gpt-4o"
  }
}
```

## Web Search and Fetch

By default, `WebSearch` works on non-Anthropic models using DuckDuckGo. For Anthropic-native backends and Codex responses, OpenClaude keeps the native provider web search behavior. `WebFetch` works but can fail on JavaScript-rendered sites. Set a [Firecrawl](https://firecrawl.dev) API key for Firecrawl-powered search/fetch behavior:

```bash
export FIRECRAWL_API_KEY=your-key-here
```

## Headless gRPC Server

OpenClaude can be run as a headless gRPC service, allowing integration of its agentic capabilities into other applications, CI/CD pipelines, or custom UIs. Uses bidirectional streaming for real-time text chunks, tool calls, and permission requests.

```bash
npm run dev:grpc
```

The gRPC definitions are in `src/proto/openclaude.proto`. Clients can be generated in Python, Go, Rust, or any other language.

## Source Build And Local Development

```bash
bun install
bun run build
node dist/cli.mjs
```

## Repository Structure

- `src/` - core CLI/runtime
- `scripts/` - build, verification, and maintenance scripts
- `docs/` - setup, contributor, and project documentation
- `python/` - standalone Python helpers and their tests
- `vscode-extension/openclaude-vscode/` - VS Code extension
- `.github/` - repo automation, templates, and CI configuration
- `bin/` - CLI launcher entrypoints

## VS Code Extension

Included in [`vscode-extension/openclaude-vscode`](vscode-extension/openclaude-vscode) for OpenClaude launch integration, provider-aware control-center UI, and theme support.

## Docs

### Advanced Setup (docs/advanced-setup.md)

Covers source builds, provider configuration examples (OpenAI, Codex, DeepSeek, Gemini, Ollama, and others), runtime diagnostics, and provider profile management.

### Architecture: Integrations (docs/architecture/integrations.md)

OpenClaude's provider system is descriptor-first. Descriptors under `src/integrations/` define vendors, gateways, brands, shared model metadata, validation hints, discovery strategy, and supported transport capabilities. Registry helpers load those descriptors and expose route/model lookups. Runtime metadata bridges descriptor state into request execution.

Key layers:
1. `src/integrations/descriptors.ts` — descriptor shapes
2. `src/integrations/index.ts` and `registry.ts` — load and expose registered vendors, gateways, brands, models
3. `src/integrations/routeMetadata.ts` — resolves route labels/defaults and maps active env state onto route ids
4. `src/integrations/runtimeMetadata.ts` — derives request-time OpenAI-shim behavior from active route + model
5. Discovery, validation, and provider-profile helpers — consume descriptor metadata

Gateway routing contract: `transportConfig.kind` is the routing contract — `local`, `openai-compatible`, `anthropic-proxy`, `bedrock`, `vertex`, or other transport families.

Known intentional long-term exceptions: GitHub dual-mode (Anthropic-native + OpenAI/Codex), Mistral dedicated request shaping, Azure auth/deployment, Gemini credential handling, DeepSeek/Moonshot reasoning shaping, Bedrock/Vertex/Foundry SDK flows, MiniMax dedicated `/usage`, Anthropic-native thinking preservation.

## Top-level structure

```
src/           — core CLI/runtime (TypeScript)
docs/          — setup guides, architecture docs, integration docs
  advanced-setup.md
  architecture/
    integrations.md   — descriptor-first provider architecture
  assets/
  hook-chains.md
  integrations/
  litellm-setup.md
  non-technical-setup.md
  quick-start-mac-linux.md
  quick-start-windows.md
vscode-extension/  — VS Code extension (openclaude-vscode)
python/        — standalone Python helpers and tests
scripts/       — build, verification, maintenance scripts
tests/         — test suite (Bun test runner)
web/           — web assets
bin/           — CLI launcher entrypoints
.github/       — CI, PR checks, workflows
Dockerfile     — container build
PLAYBOOK.md    — contributor playbook
SECURITY.md    — security policy
CONTRIBUTING.md
CHANGELOG.md
package.json   — npm package (@gitlawb/openclaude)
tsconfig.json
```
