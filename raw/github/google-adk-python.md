# google/adk-python

## Metadata
- Stars: 20339
- Primary language: Python
- Default branch: main
- Latest release: v2.3.0 (2026-06-18)
- License: Apache License 2.0
- Homepage: https://adk.dev
- Fetched: 2026-06-30
- Final URL: https://github.com/google/adk-python

## Description
An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

## README

# Agent Development Kit (ADK) 2.0

An open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

Important Links: [Docs](https://adk.dev), [Samples](https://github.com/google/adk-samples), [ADK Web](https://github.com/google/adk-web).

> **BREAKING CHANGES FROM 1.x** — Breaking changes to agent API, event model, and session schema. Sessions from ADK 2.0 are readable by ADK 1.28+ but incompatible with older 1.x.

## What's New in 2.0

- **Workflow Runtime**: Graph-based execution engine — routing, fan-out/fan-in, loops, retry, state management, dynamic nodes, human-in-the-loop, nested workflows.
- **Task API**: Structured agent-to-agent delegation — multi-turn task mode, single-turn controlled output, mixed delegation, HITL, task agents as workflow nodes.

## Installation

```bash
pip install google-adk
pip install "google-adk[extensions]"  # optional integrations
```

Requirements: Python 3.10+. Release cadence ~bi-weekly.

## Quick Start

> ADK applications use **`Agent`** (instructions, tools, behavior) and **`Workflow`** (graph-based orchestration).

### Agent

```python
from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Greet the user warmly.",
)
```

### Workflow

```python
from google.adk import Agent, Workflow

generate_fruit_agent = Agent(name="generate_fruit_agent", instruction="Return the name of a random fruit.")
generate_benefit_agent = Agent(name="generate_benefit_agent", instruction="Tell me a health benefit about the specified fruit.")

root_agent = Workflow(
    name="root_agent",
    edges=[("START", generate_fruit_agent, generate_benefit_agent)],
)
```

### Run Locally

```bash
adk run path/to/my_agent      # Interactive CLI
adk web path/to/agents_dir    # Web UI (multi-agent directories)
```

## Top-level structure

| Path | Purpose |
|---|---|
| `src/` | ADK Python package source |
| `contributing/` | workflow_samples/, task_samples/ |
| `tests/` | Test suite |
| `docs/` | Documentation assets |
| `llms.txt`, `llms-full.txt` | LLM-readable doc catalogs |
| `AGENTS.md` | Agent contributor instructions |
| `scripts/` | Build/utility scripts |

## Multi-language ecosystem

ADK is also available in TypeScript (`@google/adk`), Go (`google.golang.org/adk`), Java (`com.google.adk:google-adk`), and Kotlin (`com.google.adk:google-adk-kotlin-core`). Python repo is the primary reference implementation.
