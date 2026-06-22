# bytedance/deer-flow

## Metadata
- Stars: 73,041
- Forks: 9,879
- Primary language: Python
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://deerflow.tech
- Fetched: 2026-06-22
- Final URL: https://github.com/bytedance/deer-flow

## Description
DeerFlow is an open-source long-horizon SuperAgent harness for research, coding, and creation. It combines sub-agents, persistent memory, sandboxes, skills, MCP-style tool integration, and a gateway/frontend stack for running complex tasks that take minutes to hours.

## README
DeerFlow 2.0 is a ground-up rewrite of ByteDance's open-source agent harness. The repo positions DeerFlow as a super agent orchestration layer built around sub-agents, memory, sandboxes, tools, skills, and a message gateway. The official website is https://deerflow.tech.

The project highlights:
- Deep exploration and efficient research flow
- Extensible skills
- Sub-agent orchestration
- Persistent memory
- Sandboxed execution
- A full-stack app with backend, frontend, and Nginx reverse proxy

The quick start path is centered on `config.yaml` in the repo root:

```bash
cp config.example.yaml config.yaml
make setup
```

If Docker is available, the repository recommends Docker-first setup and a `make docker-init` / `make docker-start` flow. Otherwise it falls back to local development with `make check` and `make install`, then `make dev`.

The README also documents:
- recommended model providers and configuration examples
- sandbox mode
- MCP server integration
- IM channels
- LangSmith and Langfuse tracing
- a Python embedded client
- security guidance for deployment

## Docs

### Install.md
This file is explicitly for coding agents. It instructs them to clone the repo if needed, prefer Docker setup when available, avoid privileged installs, and stop after preparing the least risky working environment. Success means `config.yaml` exists, Docker prerequisites are prepared or local dependencies are installed, and the user receives the next launch command plus any missing config inputs.

### backend/README.md
The backend is a LangGraph-based AI super agent with sandbox execution, persistent memory, subagent delegation, and extensible tools. It exposes a Gateway API on port 8001, a Next.js frontend on port 3000, and an Nginx reverse proxy on port 2026. The architecture section describes the lead agent, middleware chain, sandbox providers, built-in tools, MCP tools, memory system, and REST routes for models, skills, uploads, memory, and threads.

### backend/docs/ARCHITECTURE.md
This doc expands the system diagram: Nginx routes `/api/langgraph/*` to the Gateway runtime, while `/api/*` serves REST APIs and `/` serves the frontend. It details the embedded agent runtime, thread state, middleware order, sandbox abstractions, and tool sources.

### backend/docs/SETUP.md
This doc explains how to place `config.yaml` in the project root, verify configuration, set environment variables such as `OPENAI_API_KEY`, and optionally pre-pull the sandbox image. It also documents config lookup order and the `DEER_FLOW_PROJECT_ROOT` and `DEER_FLOW_HOME` environment variables.

### backend/docs/MCP_SERVER.md
This doc covers `extensions_config.json`, MCP server setup, OAuth support for HTTP/SSE servers, and custom tool interceptors. It warns against adding an overlapping filesystem MCP server for the same DeerFlow workspace and points users to the built-in file tools instead.

### backend/CLAUDE.md
This file is the repo's agent guide. It describes the project structure, commands, harness/app split, middleware chain, sandbox system, and testing boundaries. It also notes that docs should be kept in sync with code changes.

### backend/AGENTS.md
A short pointer file that redirects agents to `CLAUDE.md`.

## Top-level structure
- `.agent/` — agent instructions and helper assets
- `backend/` — LangGraph backend, gateway, harness, and docs
- `frontend/` — Next.js web UI
- `contracts/` — project contracts
- `docs/` — repo-level documentation and planning notes
- `docker/` — Docker support files
- `pr-build/` — PR build helpers
- `scripts/` — repo scripts
- `skills/` — public and custom skill directories
- `tests/` — backend and integration tests
- `Makefile` — root entrypoint for setup and run commands
- `config.example.yaml` — main configuration template
- `extensions_config.example.json` — MCP/skills configuration template
- `README.md` / `Install.md` / `CHANGELOG.md` — top-level docs
