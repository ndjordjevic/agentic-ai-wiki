---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/openai/symphony
tags:
  - codex-app-server
  - issue-tracker-orchestration
  - isolated-workspaces
  - workflow-md-contract
  - autonomous-implementation-runs
  - multi-tracker-adapters
  - harness-engineering
related:
  - openai-codex-plugin-cc
  - coleam00-harness-engineering-demo
  - karpathy-autoresearch
product: symphony
detail_level: standard
created: 2026-07-22
updated: 2026-07-22
---

Symphony is OpenAI's open-source orchestration pattern for turning tracker tickets into isolated, autonomous coding-agent runs. Instead of supervising one agent session at a time, teams operate a long-running service that continuously polls project work, dispatches per-issue runs in isolated workspaces, and treats `WORKFLOW.md` as a versioned policy contract for execution, validation, and handoff.

_All claims below are sourced from ../../raw/github/openai-symphony.md unless otherwise noted._

## What it does

Symphony defines a service-level control loop around coding agents: read eligible issues from a tracker, claim one, create a deterministic workspace for that issue, run an agent session in app-server mode, stream status back to the orchestrator, and stop/reconcile if issue state changes make the run ineligible. The project is intentionally split into a language-agnostic specification (`SPEC.md`) plus a reference Elixir implementation, so teams can either adopt the current prototype or reimplement the same orchestration contract in another stack.

## Installation

```bash
git clone https://github.com/openai/symphony
cd symphony/elixir
mise trust
mise install
mise exec -- mix setup
mise exec -- mix build
mise exec -- ./bin/symphony ./WORKFLOW.md
```

The Elixir implementation expects tracker credentials (for example `LINEAR_API_KEY`) and a workflow file with YAML frontmatter. It can also run from Burrito-built single-binary releases per platform.

## Key features

- Tracker-driven dispatch with bounded concurrency and retry handling.
- Per-issue workspace isolation so agent commands execute only inside the mapped workspace path.
- In-repo workflow policy (`WORKFLOW.md`) for poll cadence, tracker config, workspace hooks, codex command/sandbox policy, and prompt template.
- Multi-tracker adapter support in the reference implementation (Linear, GitHub Issues, Jira Cloud, Asana, GitLab).
- Host-side execution of tracker-native tools (`linear_graphql`, `github_api`, `jira_rest`, `asana_api`, `gitlab_api`) without requiring duplicate tracker login in the coding-agent child process.
- Automatic stop/cleanup behavior when issues move to terminal states.

## Architecture

The spec breaks Symphony into clear layers: workflow loader/config typing, tracker adapter, orchestrator runtime state, workspace manager, agent runner, and observability/logging surfaces. The orchestrator is the central owner of poll ticks, dispatch eligibility, retries with backoff, reconciliation of active runs, and release/stop transitions. The reference Elixir implementation follows the same shape and keeps environment/config policy concentrated in `WORKFLOW.md` plus typed config accessors, with runtime behavior documented by `elixir/AGENTS.md`.

## Example usage

A typical flow is to point Symphony at a project board, define active/terminal states in `WORKFLOW.md`, and run the service continuously. As tickets enter active states, Symphony launches isolated agent runs that can post proof artifacts (CI status, review signals, walkthrough notes) and advance work toward human-review/merge states according to the workflow policy. Teams manage throughput at the board/state level while keeping coding-agent execution unattended within each issue workspace.

## Maintenance status

26,126 stars, 2,639 forks, Apache 2.0 license, actively updated (pushed 2026-07-22), latest tagged release `v0.0.1` (2026-07-18). Primary language in the current reference implementation is Elixir, and the repository explicitly labels the implementation as an engineering preview intended for trusted environments.
