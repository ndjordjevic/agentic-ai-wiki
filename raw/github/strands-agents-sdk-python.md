# strands-agents/sdk-python

## Metadata
- Stars: 5910
- Primary language: Python
- Default branch: main
- Latest release: v1.40.0 (about 6 days ago)
- License: Apache License 2.0
- Homepage: https://strandsagents.com
- Fetched: 2026-05-21
- Final URL: https://github.com/strands-agents/sdk-python

## Description
A model-driven approach to building AI agents in just a few lines of code.

## README

<div align="center">
  <h1>Strands Agents</h1>
  <h2>A model-driven approach to building AI agents in just a few lines of code.</h2>
</div>

Strands Agents is a simple yet powerful SDK that takes a model-driven approach to building and running AI agents. From simple conversational assistants to complex autonomous workflows, from local development to production deployment, Strands Agents scales with your needs.

### Feature Overview

- **Lightweight & Flexible**: Simple agent loop that just works and is fully customizable
- **Model Agnostic**: Support for Amazon Bedrock, Anthropic, Gemini, LiteLLM, Llama, Ollama, OpenAI, Writer, and custom providers
- **Advanced Capabilities**: Multi-agent systems, autonomous agents, and streaming support
- **Built-in MCP**: Native support for Model Context Protocol (MCP) servers, enabling access to thousands of pre-built tools

### Quick Start

```bash
pip install strands-agents strands-agents-tools
```

```python
from strands import Agent
from strands_tools import calculator
agent = Agent(tools=[calculator])
agent("What is the square root of 1764")
```

> **Note**: For the default Amazon Bedrock model provider, you'll need AWS credentials configured and model access enabled for Claude 4 Sonnet in the us-west-2 region.

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install strands-agents strands-agents-tools
```

### Python-Based Tools

```python
from strands import Agent, tool

@tool
def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())

agent = Agent(tools=[word_count])
response = agent("How many words are in this sentence?")
```

Hot reloading from directory:
```python
agent = Agent(load_tools_from_directory=True)  # watches ./tools/ for changes
```

### MCP Support

```python
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

aws_docs_client = MCPClient(
    lambda: stdio_client(StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]))
)

with aws_docs_client:
   agent = Agent(tools=aws_docs_client.list_tools_sync())
   response = agent("Tell me about Amazon Bedrock")
```

### Multiple Model Providers

Built-in providers:
- Amazon Bedrock, Anthropic, Gemini, Cohere, LiteLLM, llama.cpp, LlamaAPI, MistralAI, Ollama, OpenAI, OpenAI Responses API, SageMaker, Writer
- Custom providers via interface

```python
from strands import Agent
from strands.models import BedrockModel
from strands.models.ollama import OllamaModel
from strands.models.gemini import GeminiModel

# Bedrock
agent = Agent(model=BedrockModel(model_id="us.amazon.nova-pro-v1:0", temperature=0.3, streaming=True))

# Gemini
agent = Agent(model=GeminiModel(client_args={"api_key": "..."}, model_id="gemini-2.5-flash"))

# Ollama (local)
agent = Agent(model=OllamaModel(host="http://localhost:11434", model_id="llama3"))
```

## Top-level structure

```
.codecov.yml          — code coverage config
.github/              — CI/CD workflows
.gitignore
.markdown-link-check.json
.pre-commit-config.yaml
AGENTS.md             — agent instruction file (coding assistant rules)
CONTRIBUTING.md
LICENSE               — Apache 2.0
NOTICE
README.md
SECURITY.md
docs/                 — documentation source
pyproject.toml        — package configuration, dependencies
src/                  — main source code (strands package)
tests/                — unit tests
tests_integ/          — integration tests
```

### Key source modules (src/)

The `strands` package contains:
- `Agent` class — main entry point with agent loop
- `tool` decorator — define Python functions as agent tools
- `models/` — provider adapters (BedrockModel, OllamaModel, GeminiModel, etc.)
- `tools/mcp.py` — MCPClient integration
- `hooks/` — lifecycle event system (BeforeToolCallEvent, AfterToolCallEvent, etc.)
- `agent/conversation_manager.py` — Null, SlidingWindow, Summarizing managers
- `vended_plugins/steering.py` — SteeringHandler, Guide, Proceed

### Ecosystem repos under strands-agents org

- `strands-agents/sdk-python` — Python SDK (this repo)
- `strands-agents/sdk-typescript` — TypeScript SDK
- `strands-agents/tools` — community tools package (30+ tools)
- `strands-agents/agent-builder` — agent that helps build Strands agents
- `strands-agents/mcp-server` — MCP server for IDE integration (Kiro, Cursor, Claude, Cline)
- `strands-agents/samples` — sample applications
- `strands-agents/agent-sop` — standard operating procedures for agents
