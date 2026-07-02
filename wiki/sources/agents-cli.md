---
type: source
source_url: https://google.github.io/agents-cli/
companion_urls:
  - https://github.com/google/agents-cli
raw_files:
  - ../../raw/web/agents-cli.md
  - ../../raw/github/google-agents-cli.md
tags:
  - agents-cli
  - google-cloud
  - adk
  - agent-skills
  - eval-lifecycle
  - gemini-enterprise
  - deployment
  - observability
related:
  - skills.sh
  - must-have-clis-2026
  - x.com-ericzakariasson-building-clis-for-agents
  - the-new-sdlc-with-vibe-coding
  - microsoft-agent-framework
  - langchain.com-deepagents
  - antigravity.google
  - adk.dev
  - teng-lin-notebooklm-py
product: agents-cli
detail_level: standard
created: 2026-06-30
updated: 2026-07-02
---

Google's **agents-cli** is a CLI and skills package for the Gemini Enterprise Agent Platform. It is explicitly a tool *for* coding agents (Claude Code, Codex, Antigravity CLI, and others), not a coding agent itself: it installs seven lifecycle skills plus terminal commands so your agent can scaffold, build, evaluate, deploy, publish, and observe ADK-based agents on Google Cloud without you mastering every underlying service. The docs site and companion GitHub repo (`google/agents-cli`, 3.7k+ stars, Apache 2.0, Python) present the same product from operator-facing documentation and implementation detail respectively. (../../raw/github/google-agents-cli.md)

_All claims below are sourced from ../../raw/web/agents-cli.md unless otherwise noted._

## What it does

Agents CLI wraps Google's Agent Development Kit (ADK) with an opinionated production loop: write a `.agents-cli-spec.md`, scaffold a ~72-file project, build the agent body, evaluate against datasets before every deploy, ship to Agent Runtime / Cloud Run / GKE, optionally register with Gemini Enterprise, and observe via Cloud Trace and BigQuery analytics. It works two ways — with a coding agent (skills drive the right CLI command at each phase) or standalone from the terminal (every command runs without an agent).

The core mental model is four CLI verbs on rotation forever: `scaffold`, `eval`, `deploy`, observe. Production traffic feeds tomorrow's eval dataset, closing the loop between notebook demo and live system.

## Key features

**Seven agent skills** install into supported coding agents and encode lifecycle opinions:

| Skill | Coverage |
|---|---|
| `google-agents-cli-workflow` | Development lifecycle, code preservation, model selection |
| `google-agents-cli-adk-code` | ADK Python API — agents, tools, orchestration, callbacks, state |
| `google-agents-cli-scaffold` | Project scaffolding — `create`, `enhance`, `upgrade` |
| `google-agents-cli-eval` | Evaluation — datasets, metrics, generate/grade, compare, analyze, optimize |
| `google-agents-cli-deploy` | Deployment — Agent Runtime, Cloud Run, GKE, CI/CD, secrets |
| `google-agents-cli-publish` | Gemini Enterprise registration |
| `google-agents-cli-observability` | Cloud Trace, logging, BigQuery agent analytics |

**CLI surface** spans scaffold, develop, evaluate, deploy/publish, infrastructure, and data ingestion. Notable eval commands beyond the core `eval generate` / `eval grade` loop: `eval dataset synthesize` (cold-start multi-turn scenarios), `eval compare`, `eval analyze` (failure-mode clustering), `eval metric list`, and `eval optimize` (auto-tune prompts). Infrastructure commands include `infra single-project`, `infra cicd`, `infra datastore`, and `data-ingestion`. (../../raw/github/google-agents-cli.md)

**Agent templates:** `adk` (general-purpose ADK agent with A2A built in) and `agentic_rag` (retrieval-augmented agent with datastore scaffolding). Prototype mode (`--prototype --yes`) skips infrastructure decisions; `scaffold enhance` adds deployment, CI/CD, or RAG later.

**Deployment targets:** Agent Runtime (extended sessions, checkpointing), Cloud Run, GKE. Optional per-agent service identity (`--agent-identity`), IAP gating (`--iap`), and Workload Identity Federation in scaffolded CI.

## Architecture

Agents are built on ADK (`google.adk.agents.Agent`, `google.adk.apps.App`, `google.adk.models.Gemini`) with four ingredients: model, instruction, tools, and an `App` wrapper. Multi-agent systems use ADK orchestration or the A2A protocol (built into the `adk` template) for cross-process specialist coordination. Stateful production agents can use Agent Platform managed sessions (`--session-type agent_platform_sessions`) and Vertex AI Memory Bank for long-term memory across sessions. (../../raw/github/google-agents-cli.md)

The eight-phase lifecycle maps phases to skills and CLI verbs: Spec → Scaffold → Build → Orchestrate → Evaluate → Deploy → Publish → Observe. Evaluation uses the Gemini Enterprise Agent Platform GenAI Eval SDK under the hood, with built-in metrics (`general_quality`, `tool_use_quality`, `hallucination`, `grounding`, `safety`, multi-turn variants) plus custom code-execution and LLM-as-judge metrics in `eval_config.yaml`.

Scaffolded projects ship ~72 files: agent code, tests, eval boilerplate, Terraform, GitHub Actions workflows, and deploy manifests. Cloud Trace is enabled by default in deployed agents; `--bq-analytics` at scaffold time adds BigQuery prompt/response logging.

## Installation

```bash
# Recommended — CLI + skills
uvx google-agents-cli setup

# Skills only (agent handles CLI)
npx skills add google/agents-cli

# pipx alternative
pipx install google-agents-cli && agents-cli setup
```

Prerequisites: Python 3.11+, `uv`, Node.js (for skills installation). Platform support: macOS, Linux, Windows WSL 2 (native Windows not officially supported). For local dev without GCP, set `GEMINI_API_KEY` from AI Studio; existing `gcloud` Application Default Credentials are picked up automatically. (../../raw/github/google-agents-cli.md)

## Example usage

**With a coding agent** — after `uvx google-agents-cli setup`, ask your agent:

```
Build a support agent that answers questions from our docs
```

The agent reads installed skills and drives scaffold → build → eval → deploy.

**Manual workflow:**

```bash
agents-cli scaffold create my-agent --prototype --yes
cd my-agent && agents-cli install && agents-cli playground   # ADK web UI at :8080
agents-cli eval generate && agents-cli eval grade              # iterate until threshold
agents-cli deploy --dry-run && agents-cli deploy
agents-cli publish gemini-enterprise                         # optional
```

Quick smoke test: `agents-cli run "your prompt"`. Code quality: `agents-cli lint` (Ruff). (../../raw/github/google-agents-cli.md)

## When to use

- You want a coding agent to build production-grade ADK agents on Google Cloud without learning every GCP service and ADK API surface.
- You need the eval-before-deploy loop (datasets, LLM-as-judge, CI integration) that most agent demos skip.
- You are targeting Gemini Enterprise Agent Platform (Agent Runtime, Memory Bank, managed sessions, enterprise registration).
- You want scaffolded Terraform + GitHub Actions CI/CD + observability out of the box.
- **Not a fit** for non-Python agents (Go, Java, TypeScript), real-time voice/video, or multi-cloud deployments — the docs explicitly list these as not yet supported.

## Maintenance status

Actively maintained by Google: 3,697 stars, 429 forks, latest release `v0.6.1` (2026-06-28), Apache 2.0 license, Python primary language. Pre-GA offering subject to Google Cloud Pre-GA terms. Issue tracker and `agents-cli@google.com` for feedback. Evolved from Agent Starter Pack (migration guide in docs). (../../raw/github/google-agents-cli.md)

## Ecosystem

- **ADK** — underlying agent framework (`adk.dev`); agents-cli is the lifecycle tooling around it, not a replacement.
- **Gemini Enterprise Agent Platform** — deployment runtime, eval SDK, Agent Garden templates, enterprise catalog.
- **Compatible coding agents** — Antigravity CLI, Claude Code, Codex, and any agent supporting the skills format.
- **Adjacent skill suites** — docs suggest pairing with [agent-skills](https://github.com/addyosmani/agent-skills) (general SE workflows) or [google/skills](https://github.com/google/skills) (GCP foundations).
- **PyPI** — `google-agents-cli` package.

## Documentation

Docs at [google.github.io/agents-cli](https://google.github.io/agents-cli/) cover Getting Started, The Lifecycle (eight phases), tutorials (coding-agent and manual), Use Cases (12 patterns from beginner to advanced A2A), Development/Evaluation/Deployment/CI/CD guides, Observability (Cloud Trace, BigQuery plugin), CLI reference, and skills reference. MkDocs Material site built from `docs/src/` in the repo.
