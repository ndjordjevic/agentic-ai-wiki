---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/warpdotdev/warp-factory-examples
tags:
  - warp-factories
  - multi-agent-sdlc
  - oz-platform
  - multi-harness
  - event-triggers
  - scorers-skills
related:
  - warp.dev
product: warp-factory-examples
detail_level: standard
created: 2026-10-06
updated: 2026-10-06
---

`warpdotdev/warp-factory-examples` is the official example repository for Warp Factories — declarative, file-defined multi-agent SDLC pipelines on Warp's Oz cloud agent platform. Each of its eight example trees is a complete, runnable factory definition (`factory.yaml` plus `agents/`, `automations/`, `runners/`, and optional `scorers/`/`skills/` directories) that teams copy into their own repo, customize, and register with Warp. It matters for understanding how Oz factories are structured in practice — from the five stock agents Warp creates automatically, through a full issue-to-PR lifecycle with Slack/Linear/GitHub intake, to multi-harness (Warp Agent + Claude Code + Codex) and self-hosted-worker topologies. See [[warp.dev]] for the parent product.

_All claims below are sourced from ../../raw/github/warpdotdev-warp-factory-examples.md unless otherwise noted._

## What it does

The repo provides working, copy-ready configurations (schema version `v1alpha1`) for Warp Factories: event-driven, multi-agent pipelines that react to GitHub issues/PRs, Slack messages, Linear tickets, schedules, or webhooks, and run one or more agents (each with its own model/harness, compute, secrets, and MCP servers) through defined stages to produce artifacts like pull requests or review comments.

## Installation

Copy an example directory into your own repository — each is self-contained, and the registered root is the directory containing `factory.yaml` (not necessarily the repo root). Work through the example's "Make it yours" checklist to replace placeholders (mostly `acme/*` repo names), then in Warp create a factory with a GitHub-backed definition pointing at the repo/branch/directory; pushes sync the definition once the `warp/factory-config` check passes.

## Key features

- **8 progressive examples:** `00-warp-default-agents` (the five stock agents with real prompts/models), `01-single-repo-quickstart` (smallest working tree), `02-sdlc-issue-to-pr` (full triage→spec→implement→review lifecycle with Slack/Linear/GitHub intake and per-stage models/compute), `03-multi-harness` (Warp Agent foreman + Claude Code implementer + Codex reviewer with managed-secret harness auth), `04-code-review-only` (single reviewer/foreman agent posting advisory PR findings), `05-ui-verification` (computer-use agent that runs the app and verifies labeled UI behavior in a browser), `06-common-automations` (CI-failure triage, weekly dependency audits, docs-on-push checks, Slack reaction intake), and `07-self-hosted-worker` (quickstart topology pointed at a managed self-hosted worker)
- **Layout-as-identity:** a resource's name is its path (`agents/<name>/agent.md`, `automations/<name>/automation.md`, `runners/<name>.yaml`, `scorers/<name>/scorer.md`); renaming means moving the file
- **Exactly one foreman:** exactly one agent per factory declares `agentType: FOREMAN` (alias `MAIN`)
- **Harness vs. model exclusivity:** `model` (Warp Agent harness shorthand) and `harness` are mutually exclusive everywhere; `agentDefaults` must declare exactly one
- **Non-merging overrides:** declaring `secrets` or `mcpServers` on an agent or automation replaces the inherited list rather than merging with it
- **Scoped skills:** skills under `skills/` are available to every agent in the factory; skills under `agents/<name>/skills/` are scoped to that one agent
- **Validation tooling:** `scripts/validate_factory_files.py <example-dir>` checks that a tree is a valid factory definition; additional scripts (`check_conventions.py`, `verify_default_agents.py`) enforce repo conventions

## Architecture

A factory definition root is any directory containing `factory.yaml`; it declares triggers (labeled issues, pull requests, schedules, Slack/Linear/GitHub events, webhooks), one or more agents (each with a role, model/harness choice, prompt, and optional secrets/MCP servers), and optional `automations/`, `runners/` (execution environment, including self-hosted worker targets), `scorers/`, and `skills/` subdirectories. Pipelines compose per-stage agents — e.g. `02-sdlc-issue-to-pr`'s intake → triage → spec → implementation → review chain — with independent model/compute choices per stage, and `03-multi-harness` demonstrates swapping the underlying coding-agent harness (Warp Agent, Claude Code, Codex) per role within one factory.

## Example usage

```bash
python3 scripts/validate_factory_files.py examples/01-single-repo-quickstart
```

Validates that the quickstart tree (one repo, two agents, one labeled-issue trigger, one PR output) is a well-formed factory definition before registering it with Warp.

## Maintenance status

31 stars, 5 forks, MIT-licensed, primary language Python, pushed 2026-08-25, no tagged releases (examples are versioned by commit, not release tags).

## Ecosystem

Part of the Warp/Oz ecosystem documented at `docs.warp.dev/factories` — see [[warp.dev]] for the broader Agentic Development Environment and Oz cloud agent platform these factories run on.
