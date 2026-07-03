---
type: source
source_url: https://github.com/AsyncFuncAI/deepwiki-open
tags:
  - deepwiki-clone
  - self-hosted
  - repo-wiki-generator
  - docker
  - ollama
  - mcp-adjacent
related:
  - deepwiki.com
  - AIDotNet-OpenDeepWiki
  - he-yufeng-RepoWiki
  - langchain-ai-openwiki
product: deepwiki-open
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`AsyncFuncAI/deepwiki-open` (~17k stars, MIT) is the most popular community reimplementation of [[deepwiki.com]] — a self-hosted stack (Python API + Next.js UI) that ingests GitHub, GitLab, or Bitbucket repositories and produces interactive wikis with architecture diagrams and Q&A. It runs via Docker Compose, supports OpenAI, Google, OpenRouter, Azure OpenAI, and **Ollama** for local models, and persists indexes under `~/.adalflow`. Note: upstream branding has shifted toward a commercial "Grok Wiki 2.0" download at grok-wiki.com, but the OSS repo and Docker deployment remain the canonical self-host path.

_All claims below are sourced from ../../raw/github/AsyncFuncAI-deepwiki-open.md unless otherwise noted._

## What it does

deepwiki-open accepts a remote repository identifier (GitHub/GitLab/Bitbucket URL or `org/repo` form), analyzes code structure, generates documentation pages and visual diagrams, and serves them through a browser UI on ports 3000 (frontend) and 8001 (API). It targets teams who want DeepWiki-style "understand any repo" UX without sending code to Cognition's cloud.

## Installation

```bash
git clone https://github.com/AsyncFuncAI/deepwiki-open.git
cd deepwiki-open
# configure API keys in .env (OPENAI_API_KEY, GOOGLE_API_KEY, optional OPENROUTER, OLLAMA_HOST, Azure)
docker compose up
```

Or pull the pre-built image: `ghcr.io/asyncfuncai/deepwiki-open:latest` with `-v ~/.adalflow:/root/.adalflow` for persistence.

## Key features

- **Multi-forge support** — GitHub, GitLab, and Bitbucket repositories (remote URLs; not optimized for arbitrary local folders).
- **Docker-first deployment** — `docker-compose.yml`, optional LiteLLM and Ollama-local compose variants (`Dockerfile-ollama-local`, `Ollama-instruction.md`).
- **Interactive wiki UI** — Next.js frontend with generated architecture visualizations.
- **Bring-your-own-model** — OpenAI, Google, OpenRouter, Azure OpenAI, or local Ollama via environment variables.
- **Large community** — 17k+ stars; active Discord; most mature OSS DeepWiki clone by adoption.

## Architecture

Monorepo layout: `api/` (Python backend), `src/` + Next.js app (`next.config.ts`, `package.json`), Docker multi-stage build bundling API on port 8001 and Next standalone server on 3000. Data and cloned repo indexes persist in `~/.adalflow` on the host. Test suite under `tests/` with pytest.

## Example usage

```bash
docker compose up
# open http://localhost:3000, enter a repo like microsoft/vscode
```

For Ollama-only local inference, use the Ollama-specific Docker compose files documented in the repo.

## Maintenance status

17,138 stars, 1,923 forks, MIT licensed, Python + TypeScript, default branch `main`, last push 2026-06-03. No GitHub releases tagged; Docker images published via GHCR. Maintainer AsyncFuncAI; community Discord linked from README. Competes with [[AIDotNet-OpenDeepWiki]] (full platform + MCP) and [[he-yufeng-RepoWiki]] (lighter CLI for **local** paths).
