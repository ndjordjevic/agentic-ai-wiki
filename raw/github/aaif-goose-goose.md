# aaif-goose/goose

## Metadata
- Stars: 48633
- Primary language: Rust
- Default branch: main
- Latest release: v1.37.0 (2026-06-03)
- License: Apache License 2.0
- Homepage: https://goose-docs.ai/
- Fetched: 2026-06-10
- Final URL: https://github.com/aaif-goose/goose

## Description
an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

## README

> **🦆 goose has moved!** This project has moved from `block/goose` to the [Agentic AI Foundation (AAIF)](https://aaif.io/) at the Linux Foundation. Some links and references are still being updated.

### goose

_your native open source AI agent — desktop app, CLI, and API — for code, workflows, and everything in between_

goose is a general-purpose AI agent that runs on your machine. Not just for code — use it for research, writing, automation, data analysis, or anything you need to get done.

A native desktop app for macOS, Linux, and Windows. A full CLI for terminal workflows. An API to embed it anywhere. Built in Rust for performance and portability.

goose works with 15+ providers — Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more. Use API keys or your existing Claude, ChatGPT, or Gemini subscriptions via [ACP](https://goose-docs.ai/docs/guides/acp-providers). Connect to 70+ extensions via the [Model Context Protocol](https://modelcontextprotocol.io/) open standard.

goose is part of the [Agentic AI Foundation (AAIF)](https://aaif.io/) at the Linux Foundation.

#### Get started

**Download the desktop app** for macOS, Linux, and Windows, or install the CLI:

```bash
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
```

#### Quick links
- Quickstart: https://goose-docs.ai/docs/quickstart
- Installation: https://goose-docs.ai/docs/getting-started/installation
- Documentation: https://goose-docs.ai/docs/category/getting-started
- Custom Distributions: build your own goose distro with preconfigured providers, extensions, and branding

## Docs

### goose Architecture

goose, an open source AI Agent, builds upon the basic interaction framework of LLMs (text in, text out) enhanced with tool integrations via extensions.

#### goose Components

goose operates using three main components:

- **Interface**: The desktop application or CLI — collects user input and displays outputs
- **Agent**: The agent runs goose's core logic, managing the interactive loop
- **Extensions**: Components that provide specific tools and capabilities. Enable actions like running commands and managing files

In a typical session, the interface spins up an instance of the agent, which connects to one or more extensions simultaneously. The interface can also create multiple agents for concurrent tasks.

#### Interoperability with Extensions

goose uses the Model Context Protocol (MCP) to connect to MCP systems/servers (referred to as "extensions" in goose). Extensions expose functionality through tools — functions that allow them to perform specific actions (e.g. run commands, file operations, Google Drive search).

goose includes built-in extensions for development, web scraping, automation, memory, and more. Supports connecting to external extensions or creating custom extensions as MCP servers.

#### Agent Client Protocol (ACP)

goose supports the Agent Client Protocol (ACP) in two ways:

- **goose as an ACP Server**: `goose acp` starts goose as an ACP server over stdio, letting editors like JetBrains and Zed connect to it directly
- **ACP Agents as Providers**: goose can delegate to external ACP agents (like Claude Code or Codex) as providers; the ACP agent handles tool execution internally; goose passes configured extensions through as MCP servers

#### Interactive Loop

1. **Human Request** — user provides request, question, command, or problem
2. **Provider Chat** — goose sends the request + list of available tools to the configured LLM provider
3. **Model Extension Call** — LLM creates a tool call request in JSON; goose executes it and gathers results
4. **Response to Model** — goose sends results back to the model; loop repeats if more tool calls needed
5. **Context Revision** — goose removes old/irrelevant information for token management
6. **Model Response** — LLM sends final response back to user

#### Error Handling

goose captures and handles traditional errors and execution errors (invalid JSON, missing tools, etc.) and sends them back to the model as tool responses — the LLM gets the information needed to resolve errors and continue.

#### Context Revision (Token Management)

- Summarizes with faster and smaller LLMs
- Includes everything vs. semantic search
- Algorithms to delete old or irrelevant content
- Uses find-and-replace instead of rewriting large files
- Uses ripgrep to skip system files; summarizes verbose command outputs

### Extensions Design

Extensions expose capabilities through the `Extension` trait:

```rust
#[async_trait]
pub trait Extension: Send + Sync {
    fn name(&self) -> &str;
    fn description(&self) -> &str;
    fn instructions(&self) -> &str;
    fn tools(&self) -> &[Tool];
    async fn status(&self) -> AnyhowResult<HashMap<String, Value>>;
    async fn call_tool(&self, tool_name: &str, parameters: HashMap<String, Value>) -> ToolResult<Value>;
}
```

Tools are defined with the `#[tool]` proc macro (from `goose-acp-macros`). Each tool must take a `Value` and return `AgentResult<Value>` (async).

Error handling uses two types:
- `ErrorData`: specific errors related to tool execution
- `anyhow::Error`: general purpose errors for extension status

### AGENTS.md (developer instructions)

goose is an AI agent framework in Rust with CLI and Electron desktop interfaces.

Build: `source bin/activate-hermit && cargo build`

Structure:
```
crates/
├── goose              # core logic
├── goose-acp-macros   # ACP proc macros
├── goose-cli          # CLI entry
├── goose-server       # backend (binary: goosed)
├── goose-mcp          # MCP extensions
├── goose-test         # test utilities
└── goose-test-support # test helpers

evals/open-model-gym/  # benchmarking / evals
ui/desktop/            # Electron app
ui/text/               # Ink-based terminal UI
```

## Top-level structure

```
.cargo/          — Rust toolchain config
.claude/         — Claude Code instructions
.codex/          — Codex agent instructions
.cursor/         — Cursor instructions
.devcontainer/   — Dev container config
.github/         — CI/CD workflows
AGENTS.md        — Agent development instructions (mirrors CLAUDE.md)
CLAUDE.md        — @AGENTS.md
CONTRIBUTING.md  — Contribution guidelines
CUSTOM_DISTROS.md — Building custom goose distributions
GOVERNANCE.md    — AAIF governance rules
Cargo.toml       — Rust workspace manifest
Dockerfile       — Container build
bin/             — Hermit toolchain activation + helper scripts
crates/          — Rust crates (goose, goose-cli, goose-server, goose-mcp, goose-providers, goose-sdk, goose-acp-macros, goose-sdk-types, goose-test, goose-test-support)
documentation/   — Docusaurus docs site (goose-docs.ai)
evals/           — Benchmarking / open-model-gym evaluations
examples/        — Example code (frontend_tools.py, mcp-wiki, plugins)
services/        — Backend services
ui/              — Desktop (Electron) and text (Ink/React) frontends
workflow_recipes/ — Pre-built workflow recipe YAML files
```
