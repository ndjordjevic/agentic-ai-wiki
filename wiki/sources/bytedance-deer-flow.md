---
type: source
source_url: https://github.com/bytedance/deer-flow
tags:
  - superagent-harness
  - subagents
  - sandbox-execution
  - persistent-memory
  - skill-loading
  - mcp-tools
  - langgraph-runtime
  - nextjs-ui
related: []
product: deer-flow
detail_level: standard
created: 2026-06-22
updated: 2026-06-22
---

DeerFlow is ByteDance's open-source long-horizon super-agent harness: a full-stack system that combines a LangGraph-based backend, sandboxed execution, persistent memory, sub-agent delegation, skills, MCP tooling, and a web UI into one orchestration layer for multi-minute and multi-hour agentic work. The 2.0 rewrite emphasizes practical agent operations over a thin library API, with a repo layout that makes the runtime, gateway, frontend, and configuration surface easy to inspect and extend.

_All claims below are sourced from ../../raw/github/bytedance-deer-flow.md unless otherwise noted._

## What it does

DeerFlow turns the agent stack into a productized harness: the backend runs the lead agent, tools, memory, middleware, and subagents; the frontend provides the user interface; and Nginx exposes a single entrypoint. The repo frames the system as a "deep exploration and efficient research flow" for tasks that require long-running coordination, file operations, tool use, and iterative completion.

## Key features

- **Sub-agent orchestration** — the runtime can delegate work to additional agents instead of forcing everything through one prompt loop.
- **Sandboxed execution** — per-thread isolated workspaces support safe command execution and file operations.
- **Persistent memory** — the agent keeps context across conversations through a dedicated memory layer.
- **Extensible skills** — behavior can be augmented through SKILL.md-style modules.
- **MCP integration** — configurable model-context tools extend the runtime with external systems and custom servers.
- **Full-stack delivery** — backend, frontend, and reverse proxy are all part of the same repo and deployment story.

## Architecture

The architecture centers on a Gateway API that hosts the LangGraph-compatible runtime and REST endpoints. Nginx sits in front as a reverse proxy, routing `/api/langgraph/*` to the agent runtime, `/api/*` to the Gateway, and non-API traffic to the Next.js frontend. The lead agent is assembled from a middleware chain that handles thread data, uploads, sandbox acquisition, summarization, task tracking, titles, memory, vision inputs, and clarification handling.

The backend docs also describe the harness/app split: reusable agent runtime code lives under the harness package, while the application layer owns the FastAPI gateway and channel integrations. That separation is a core design choice of the repo and shows up throughout the directory layout and tests.

## Installation

The repo's preferred setup path is:

```bash
cp config.example.yaml config.yaml
make setup
```

If Docker is available, use the Docker-first path (`make docker-init` before launch). If not, fall back to local setup with `make check`, `make install`, and then `make dev`. Configuration lives in `config.yaml` at the repo root; the docs also mention `extensions_config.json` for MCP servers and skills.

## Example usage

```bash
make setup
make dev
```

For Docker-oriented setups, the docs recommend:

```bash
make docker-init
make docker-start
```

The agent-facing install doc also points coding agents at `Install.md` and tells them to stop once the environment is prepared and the next launch command is clear.

## Maintenance status

This is an actively maintained repo with 73,041 stars, 9,879 forks, Python as the primary language, MIT licensing, and a `main` default branch. The README notes that DeerFlow 2.0 is a ground-up rewrite and that active development moved to 2.0 while the original 1.x branch remains available.

## Ecosystem

DeerFlow sits in the overlapping space of agent harnesses, skill systems, sandboxed runtimes, and MCP-enabled tool orchestration. Its closest conceptual neighbors in this wiki are the other harness and framework pages, but DeerFlow is more opinionated because it ships the agent runtime, deployment path, and UI together in one repo.
