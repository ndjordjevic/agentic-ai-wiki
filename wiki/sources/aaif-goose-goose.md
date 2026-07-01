---
type: source
source_url: https://github.com/aaif-goose/goose
tags: [ai-agent, mcp, multi-provider, rust, desktop-app, cli, acp, open-source, extensions, linux-foundation]
related: [njbrake-agent-of-empires, strandsagents.com, microsoft-agent-framework, omnigent-ai-omnigent, warp.dev, getcaveman.dev]
product: goose
detail_level: standard
created: 2026-06-10
updated: 2026-07-01
---

goose is an open-source, general-purpose AI agent built in Rust (48,633 stars, Apache-2.0) that runs natively on your machine as a desktop app (macOS, Linux, Windows), a CLI, or an embedded API. Originally developed at Block and now stewarded by the Agentic AI Foundation (AAIF) at the Linux Foundation, it is designed for research, writing, automation, data analysis, and code — not just code suggestions. goose connects to 15+ LLM providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more) and exposes 70+ capabilities through MCP extensions, making it one of the most provider-agnostic and extensible local AI agents in this wiki.

_All claims below are sourced from ../../raw/github/aaif-goose-goose.md unless otherwise noted._

## What it does

goose executes tasks on a user's machine using a three-component architecture: an **Interface** (desktop app or CLI), an **Agent** (core Rust logic running the interactive loop), and **Extensions** (MCP servers that expose tools). The interface spins up one or more agent instances, each connecting to extensions simultaneously. Extensions provide the actual capabilities — file operations, shell commands, web scraping, memory, automation, and custom tools. Users issue requests in natural language; goose handles the full tool-call cycle and produces results.

## Key features

- **Multi-provider**: works with any LLM via API keys or existing Claude, ChatGPT, and Gemini subscriptions through the Agent Client Protocol (ACP)
- **MCP-native**: all extensions are MCP servers; connects to 70+ community and first-party extensions
- **ACP support**: `goose acp` starts goose as an ACP server over stdio for editors like JetBrains and Zed; also supports delegating to external ACP agents (Claude Code, Codex) as providers
- **Desktop + CLI + API**: single codebase (Rust workspace) targets all three interfaces
- **Custom distributions**: `CUSTOM_DISTROS.md` documents how to package goose with preconfigured providers, extensions, and branding
- **Workflow recipes**: YAML-based automation playbooks (e.g., `goose-self-test.yaml`)
- **Open governance**: Apache-2.0 license, AAIF governance at Linux Foundation, public `GOVERNANCE.md`

## Architecture

The interactive loop runs as follows:

1. The user issues a request via Interface (desktop or CLI)
2. goose forwards the request plus a list of available tool definitions to the configured LLM provider
3. The LLM produces a tool call in JSON; goose executes it via the appropriate extension and collects results
4. Results go back to the model; steps 3–4 repeat until no more tool calls are needed
5. Context revision trims stale or irrelevant messages for token efficiency (uses smaller/faster LLMs for summarization, ripgrep for file skips, find-and-replace instead of full file rewrites)
6. The model sends a final response

The Rust workspace is organized into focused crates: `goose` (core agent logic), `goose-cli` (CLI entry point), `goose-server` (HTTP backend; binary `goosed`), `goose-mcp` (built-in MCP extensions), `goose-providers` (provider adapters), `goose-sdk` / `goose-sdk-types` (SDK layer), `goose-acp-macros` (proc macros for ACP tool definition), plus test support crates. The desktop UI is an Electron app (`ui/desktop/`) and the terminal UI uses Ink/React (`ui/text/`).

Extensions implement the `Extension` Rust trait, exposing `name`, `description`, `instructions`, and `tools`. Tools are async functions returning `AgentResult<Value>` and are defined using the `#[tool]` proc macro. This uniform interface makes it straightforward to write custom MCP extensions that goose can discover and call.

## Installation

**Desktop app:** Download from https://goose-docs.ai/docs/getting-started/installation (macOS, Linux, Windows).

**CLI:**
```bash
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
```

**Build from source:**
```bash
source bin/activate-hermit   # hermit toolchain
cargo build --release
```

## Example usage

Run a workflow recipe:
```bash
goose run --recipe goose-self-test.yaml
```

Start as an ACP server:
```bash
goose acp
```

Run the CLI interactively (provider configured via `goose configure`):
```bash
goose session
```

## When to use

goose fits best when you need a local, self-hosted AI agent that can use any LLM provider and integrate with a broad extension ecosystem via MCP. It is a strong choice for teams that want a desktop app and a CLI out of the same binary, want to avoid vendor lock-in at the model layer, or need to build custom extension integrations using idiomatic Rust. It competes in the same space as [[njbrake-agent-of-empires]] (session manager for multiple agents) and [[microsoft-agent-framework]] (enterprise agent SDK) but is positioned as a first-class general-purpose agent rather than a meta-coordinator or enterprise framework.

## Ecosystem

goose is part of the AAIF (Agentic AI Foundation) at the Linux Foundation alongside other open-source agentic projects. The documentation site runs on Docusaurus at https://goose-docs.ai/. Community channels include Discord (discord.gg/goose-oss), YouTube, LinkedIn, and X. The `evals/open-model-gym/` directory provides benchmarking infrastructure for comparing model and provider performance. Multiple coding agents in the wiki (Claude Code, Codex) can be used as ACP providers within goose.

## Maintenance status

48,633 stars, v1.37.0 (2026-06-03), Apache-2.0. Primary language: Rust. Latest push: 2026-06-10. Governance under AAIF / Linux Foundation. The repository is actively maintained with CI, release cadence, and a public governance document.
