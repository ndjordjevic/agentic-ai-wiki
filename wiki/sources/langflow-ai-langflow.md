---
type: source
category: "Workflow automation & no-code platforms"
source_url: https://github.com/langflow-ai/langflow
tags:
  - visual-flow-builder
  - low-code-ai
  - multi-agent-orchestration
  - mcp-server
  - workflow-api
  - python-custom-components
  - langchain-ecosystem
related:
  - n8n.io
  - crewai.com
  - langchain.com-langgraph
product: langflow
detail_level: standard
created: 2026-07-22
updated: 2026-07-22
---

Langflow is an open-source visual platform for designing, testing, and deploying LLM-powered agent workflows, combining a node-based builder with production deployment surfaces (REST API and MCP server) in one stack. It targets teams that want no-code/low-code flow authoring without giving up code-level extensibility, offering Python custom components, broad model/tool integrations, and infrastructure paths from local desktop to cloud/server deployment.

_All claims below are sourced from ../../raw/github/langflow-ai-langflow.md unless otherwise noted._

## What it does

Langflow lets builders compose AI systems as connected flow graphs, where agents, tools, prompts, memory, retrieval, and integration components are wired visually and executed through the same runtime. Each project can expose flows as callable APIs and as MCP tools, so the same flow can be consumed by apps, automations, or MCP-compatible clients without rebuilding logic for each channel.

## Installation

```bash
uv pip install langflow -U
uv run langflow run
```

Langflow supports Python 3.10-3.14 for local OSS installs and also ships desktop builds (Windows/macOS) and Docker images (`langflowai/langflow:latest`) for quicker onboarding and deployment.

## Key features

- Visual drag-and-drop flow builder with interactive playground testing.
- Multi-agent flow patterns with tool ports and conversation/retrieval orchestration.
- MCP support in both directions: Langflow as MCP server (flows as tools) and MCP client (external tools via MCP Tools component).
- API-first execution model with workflow run/build endpoints and tweakable runtime parameters.
- Python-level extensibility through custom components and source-code access.
- Large integration surface across major LLM providers, vector stores, and third-party service bundles.

## Architecture

Langflow is a full-stack monorepo with a Python backend/runtime (`src/...`) and a docs/frontend surface (`docs/...` plus web assets), organized around flow execution, component registries, API services, and deployment tooling. The repository includes explicit agent guidance files (`AGENTS.md`, `CLAUDE.md`) and deep API/docs coverage for project, flow, build, monitor, and OpenAI-compatible response endpoints, indicating a design aimed at both interactive UI use and programmatic embedding.

## Example usage

A common pattern is: build an agent flow visually, connect tools (including MCP Tools), test behavior in the playground, then call that same flow from code through Langflow's API or expose it through the project's MCP endpoint (`/api/v1/mcp/project/<PROJECT_ID>/streamable`) so external MCP clients can invoke it as a tool.

## Maintenance status

152,186 stars, 9,623 forks, MIT license, latest release `v1.10.2` (2026-07-07), and active updates (pushed 2026-07-22). The repo includes contributor, security, release, and development workflows plus a large versioned documentation set, consistent with an actively maintained production project.
