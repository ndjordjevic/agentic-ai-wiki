# topoteretes/cognee

## Metadata
- Stars: 28990
- Primary language: Python
- Default branch: main
- Latest release: v1.4.0.dev0 (2026-07-20)
- License: Apache License 2.0
- Homepage: https://www.cognee.ai
- Fetched: 2026-07-21
- Final URL: https://github.com/topoteretes/cognee

## Description
Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.

## README
<div align="center">
  <a href="https://github.com/topoteretes/cognee">
    <img src="https://raw.githubusercontent.com/topoteretes/cognee/refs/heads/dev/assets/cognee-logo-transparent.png" alt="Cognee Logo" height="60">
  </a>

  <br />

  Cognee - The Open-Source AI Memory Platform for Agents

  <p align="center">
  <a href="https://www.youtube.com/watch?v=8hmqS2Y5RVQ&t=13s">Demo</a>
  .
  <a href="https://docs.cognee.ai/">Docs</a>
  .
  <a href="https://cognee.ai">Learn More</a>
  ·
  <a href="https://discord.gg/NQPKmU5CCg">Join Discord</a>
  ·
  <a href="https://www.reddit.com/r/AIMemory/">Join r/AIMemory</a>
  .
  <a href="https://github.com/topoteretes/cognee-community">Community Plugins & Add-ons</a>
  </p>
</div>

📄 Read the research paper: [Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning](https://arxiv.org/abs/2505.24478) — Markovic et al., 2025

## About Cognee

Cognee is an open-source AI memory platform for AI Agents. Ingest data in any format, and Cognee continuously builds a self-hosted knowledge graph that gives your agents persistent long-term memory across sessions. Cognee combines vector embeddings, graph reasoning, and cognitive-science-grounded ontology generation to make documents both searchable by meaning and connected by relationships that evolve as your knowledge does.

Available as a plugin for OpenClaw (`cognee-openclaw` on npm), a plugin for Claude Code (`claude-code-plugin` in `topoteretes/cognee-integrations`), a Rust client (`cognee-rs`), and a TypeScript client (`@cognee/cognee-ts`).

### Why use Cognee:

- Easily Build Company Brain - unify data from various sources in one place and enable Agents with your domain knowledge
- Knowledge infrastructure — unified ingestion, graph/vector search, runs locally, ontology grounding, multimodal
- Persistent and Learning Agents - learn from feedback, context management, cross-agent knowledge sharing
- Reliable and Trustworthy Agents - agentic user/tenant isolation, traceability, OTEL collector, audit traits

## Basic Usage & Feature Guide

An end-to-end Colab walkthrough covers Cognee's core features.

## Quickstart

### Prerequisites

- Python 3.10 to 3.14

### Step 1: Install Cognee

```bash
uv pip install cognee
```

### Step 2: Configure the LLM
```python
import os
os.environ["LLM_API_KEY"] = "YOUR OPENAI_API_KEY"
```
Alternatively, create a `.env` file using the `.env.template`. To integrate other LLM providers, see the LLM Provider Documentation.

### Step 3: Run the Pipeline

Cognee's API gives you four operations — `remember`, `recall`, `forget`, and `improve`:

```python
import cognee
import asyncio


async def main():
    # Store permanently in the knowledge graph (runs add + cognify + improve)
    await cognee.remember("Cognee turns documents into AI memory.")

    # Store in session memory (fast cache, syncs to graph in background)
    await cognee.remember("User prefers detailed explanations.", session_id="chat_1")

    # Query with auto-routing (picks best search strategy automatically)
    results = await cognee.recall("What does Cognee do?")
    for result in results:
        print(result)

    # Query session memory first, fall through to graph if needed
    results = await cognee.recall("What does the user prefer?", session_id="chat_1")
    for result in results:
        print(result)

    # Delete when done
    await cognee.forget(dataset="main_dataset")


if __name__ == '__main__':
    asyncio.run(main())

```

### Use the Cognee CLI

```bash
cognee-cli remember "Cognee turns documents into AI memory."

cognee-cli recall "What does Cognee do?"

cognee-cli forget --all
```

To open the local UI, run:
```bash
cognee-cli -ui
```

> **Note:** The MCP server launched by `cognee-cli -ui` runs inside a Docker container.
> Docker Desktop, Colima, or any OCI-compatible runtime with a working `docker` CLI is
> required.

## Run with Docker

Cognee publishes prebuilt images to Docker Hub on every push to `main`:
`cognee/cognee` (the API server) and `cognee/cognee-mcp` (the MCP server).

### Option A — Docker Compose (build from source)

```bash
cp .env.template .env   # then edit .env and set LLM_API_KEY

# Start the API server (http://localhost:8000)
docker compose up

# Optional profiles (combine as needed):
docker compose --profile ui up        # + frontend on http://localhost:3000
docker compose --profile mcp up       # + MCP server on http://localhost:8001
docker compose --profile postgres up  # + Postgres/PGVector
docker compose --profile neo4j up     # + Neo4j
```

> The `cognee` and `cognee-mcp` services publish different host ports (`8000` vs `8001`), so you can run both at once.

### Option B — Pull the prebuilt image (no clone required)

```bash
# Create a minimal .env in the current directory
echo 'LLM_API_KEY="YOUR_OPENAI_API_KEY"' > .env

# API server
docker run --env-file ./.env -p 8000:8000 --rm -it cognee/cognee:main

# MCP server (HTTP transport)
docker pull cognee/cognee-mcp:main
docker run -e TRANSPORT_MODE=http --env-file ./.env -p 8000:8000 --rm -it cognee/cognee-mcp:main
```

## Use with AI Agents

### Claude Code

Install the Cognee memory plugin (`topoteretes/cognee-integrations`) to give Claude Code persistent memory across sessions. The plugin captures prompts, tool traces, and assistant responses into session memory, injects relevant context on every prompt, and syncs session memory into the permanent knowledge graph at session end.

**Install** from the Claude Code marketplace, before launching Claude Code, so the first `claude` launch is a clean session that bootstraps memory automatically:

```bash
# Add the marketplace and install the plugin (one-time, user-scoped)
claude plugin marketplace add topoteretes/cognee-integrations
claude plugin install cognee-memory@cognee

# Set env vars for your mode (see below), then launch
export LLM_API_KEY="sk-..."   # local mode; or COGNEE_BASE_URL + COGNEE_API_KEY for cloud
claude
```

**Local mode** (default) — the plugin bootstraps a local Cognee API at `http://localhost:8011`. Only `LLM_API_KEY` is required; the Cognee API key is auto-minted if absent.

**Cognee Cloud or a remote server** — set both `COGNEE_BASE_URL` and `COGNEE_API_KEY`.

On startup you should see a "Cognee Memory Connected" system message.

The plugin hooks into Claude Code's lifecycle — `SessionStart` selects mode and sets up identity, `UserPromptSubmit` injects dataset-scoped context, `PostToolUse` captures tool traces, `Stop` writes the assistant's answer, `PreCompact` preserves memory across context resets, and `SessionEnd` triggers the final sync into the permanent graph.

### Connect to Cognee Cloud

```python
import cognee

await cognee.serve(url="https://your-instance.cognee.ai", api_key="ck_...")

await cognee.remember("important context")
results = await cognee.recall("what happened?")

await cognee.disconnect()
```

## Examples

Browse more examples in the `examples/` folder — demos, guides, custom pipelines, and database configurations.

**Use Case 1 — Customer Support Agent:** unifies data sources, reconstructs interaction timelines, retrieves similar resolved cases, maps to the best resolution strategy, and updates memory after execution so the agent never repeats the same mistake.

**Use Case 2 — Expert Knowledge Distillation (SQL Copilot):** extracts and stores patterns from expert SQL queries and workflows, maps the current schema to previously seen structures, retrieves similar tasks and their successful implementations, and adapts expert reasoning to the current context.

## Run the Whole Memory Layer on Postgres

Graph memory traditionally means operating a stack — a graph database for relationships, a vector database for embeddings, Redis for sessions, and a relational database for metadata — all deployed, secured, and paid for before an agent remembers anything. In cognee 1.0 you can run the entire memory layer on a single Postgres instance.

| Memory layer | Traditional stack | cognee on Postgres |
| --- | --- | --- |
| Relationships | Neo4j or another graph database | cognee's Postgres graph backend |
| Embeddings | Dedicated vector database | pgvector |
| Sessions | Redis | SQL session-cache backend |
| Metadata | Relational database | same Postgres |

The graph still exists — it just lives inside the same Postgres-backed memory layer as the text, metadata, and embeddings, so retrieval moves between similarity and structure without crossing service boundaries. In CI benchmarks, Postgres search ran ~10% faster than the separate graph-plus-vector setup.

Postgres is the default recommended for most deployments, but dedicated backends can be swapped in when a workload needs them (Neo4j and Neptune for graphs, Redis for sessions, pgvector and LanceDB for vectors, plus Qdrant, ChromaDB, Weaviate, and Milvus via community adapters). Local development stays fully embedded — SQLite, LanceDB, and Kuzudb — with no extra services to stand up.

```bash
pip install "cognee[postgres]"
```

```bash
DB_PROVIDER=postgres
VECTOR_DB_PROVIDER=pgvector
GRAPH_DATABASE_PROVIDER=postgres
CACHE_BACKEND=postgres

DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=cognee
DB_PASSWORD=cognee
DB_NAME=cognee_db
```

## Deploy Cognee

Use Cognee Cloud for a fully managed experience, or self-host with one of several 1-click deployment configurations:

| Platform | Best For | Command |
|----------|----------|---------|
| **Cognee Cloud** | Managed service, no infrastructure to maintain | Sign up or `await cognee.serve()` |
| **Modal** | Serverless, auto-scaling, GPU workloads | `bash distributed/deploy/modal-deploy.sh` |
| **Railway** | Simplest PaaS, native Postgres | `railway init && railway up` |
| **Fly.io** | Edge deployment, persistent volumes | `bash distributed/deploy/fly-deploy.sh` |
| **Render** | Simple PaaS with managed Postgres | Deploy to Render button |
| **Daytona** | Cloud sandboxes (SDK or CLI) | `distributed/deploy/daytona_sandbox.py` |
| **Islo** | Isolated cloud sandboxes (SDK) | `distributed/deploy/islo_sandbox.py` |

## Use Cognee in Other Languages

Cognee ships official clients for Rust (`cognee-rs`, `cargo add cognee`) and TypeScript (`@cognee/cognee-ts`, `npm install @cognee/cognee-ts`).

## Benchmarks

Cognee was run against BEAM, a long-context benchmark that tests whether a system can keep track of a long conversation as it changes — a more useful test for agent memory than typical needle-in-a-haystack benchmarks. Using only cognee's default settings and standard open-source features (no custom models, no BEAM-specific pipelines), it beat the previous state of the art at the 100K-token setting and matched it at 10M tokens.

| Benchmark | Setting | cognee | Previous SOTA | Obsidian / RAG baseline |
|-----------|---------|--------|---------------|--------------------------|
| BEAM | 100K tokens | **0.79** (>0.8 with per-question routing) | 0.735 | ~0.33 |
| BEAM | 10M tokens | **0.67** | 0.641 | ~0.33 |

These numbers are a directional signal rather than a definitive measure — see the BEAM preliminary report for full methodology, caveats, and what the results actually mean.

## Research & Citation

Research paper on optimizing knowledge graphs for LLM reasoning:

```bibtex
@misc{markovic2025optimizinginterfaceknowledgegraphs,
      title={Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning},
      author={Vasilije Markovic and Lazar Obradovic and Laszlo Hajdu and Jovan Pavlovic},
      year={2025},
      eprint={2505.24478},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2505.24478},
}
```

## Top-level structure
- `AGENTS.md`, `CLAUDE.md` — agent instruction files (repo dogfoods its own memory plugin/tooling for contributors)
- `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `DCO.md`, `NOTICE.md` — project governance docs
- `README.md` + `README_ko.md` — localized readmes
- `Dockerfile`, `Dockerfile.ci`, `docker-compose.yml`, `entrypoint.sh` — container build/run (profiles: `ui`, `mcp`, `postgres`, `neo4j`, per README)
- `.env.example`, `.env.template` — configuration templates (`LLM_API_KEY`, DB provider settings)
- `assets/` — logo, demo GIF, architecture SVGs (`remember.svg`, `recall.svg`)
- `bin/` — CLI entry scripts
- `cognee/` — main Python package: `api/`, `cli/`, `eval_framework/` (includes BEAM benchmark report), `infrastructure/`, `memory/`, `migration/`, `modules/`, `pipelines/`, `shared/`, `tasks/`, `tests/`; plus `alembic/` migrations, `low_level.py`, `skill.md`, `version.py`
- `cognee-mcp/` — MCP server package (has its own README covering SSE/stdio transports and client config)
- `cognee-frontend/` — local UI served via the `ui` Docker Compose profile
- `cognee-starter-kit/` — starter-kit scaffolding
- `cognee_db_workers/` — database worker processes
- `deployment/`, `distributed/` — deploy scripts and worker configs for Modal, Railway, Fly.io, Render, Daytona, Islo sandboxes
- `docs/` — `docker-colima-setup.md` (Docker/Colima runtime setup for the MCP server's containerized launch)
- `evals/`, `examples/`, `notebooks/`, `tests/`, `tools/`, `working_dir_error_replication/` — evaluation harnesses, runnable examples/notebooks, test suite, dev tooling
- `kuzu/`, `licenses/`, `logs/` — embedded graph-db data, third-party license texts, log output
- `pyproject.toml`, `poetry.lock`, `uv.lock`, `mise.toml` — Python packaging/toolchain (supports poetry and uv)
