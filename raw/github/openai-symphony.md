# openai/symphony

## Metadata
- Stars: 26126
- Primary language: Elixir
- Default branch: main
- Latest release: v0.0.1 (2026-07-18)
- License: Apache License 2.0
- Homepage: https://openai.com/index/open-source-codex-orchestration-symphony/
- Fetched: 2026-07-22
- Final URL: https://github.com/openai/symphony

## Description
Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.

## README
# Symphony

Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage
work instead of supervising coding agents.

[![Symphony demo video preview](.github/media/symphony-demo-poster.jpg)](https://player.vimeo.com/video/1186371009?h=5626e4b899)

_In this [demo video](https://player.vimeo.com/video/1186371009?h=5626e4b899), Symphony monitors a Linear board for work and spawns agents to handle the tasks. The agents complete the tasks and provide proof of work: CI status, PR review feedback, complexity analysis, and walkthrough videos. When accepted, the agents land the PR safely. Engineers do not need to supervise Codex; they can manage the work at a higher level._

> [!WARNING]
> Symphony is a low-key engineering preview for testing in trusted environments.

## Running Symphony

### Requirements

Symphony works best in codebases that have adopted
[harness engineering](https://openai.com/index/harness-engineering/). Symphony is the next step --
moving from managing coding agents to managing work that needs to get done.

### Option 1. Make your own

Tell your favorite coding agent to build Symphony in a programming language of your choice:

> Implement Symphony according to the following spec:
> https://github.com/openai/symphony/blob/main/SPEC.md

### Option 2. Use our experimental reference implementation

Check out [elixir/README.md](elixir/README.md) for instructions on how to set up your environment
and run the Elixir-based Symphony implementation. You can also ask your favorite coding agent to
help with the setup:

> Set up Symphony for my repository based on
> https://github.com/openai/symphony/blob/main/elixir/README.md

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Docs

### SPEC.md

Language-agnostic service specification for Symphony as a long-running scheduler/runner that polls a tracker, creates per-issue isolated workspaces, and runs coding-agent sessions. It defines normative behavior for orchestration state, retries, reconciliation, workspace lifecycle, and workflow policy loading from `WORKFLOW.md`.

Key points captured from the spec:
- Symphony is a scheduler/runner and tracker reader, not a full workflow engine.
- Per-issue workspace isolation is a hard boundary.
- Workflow policy is versioned in-repo via `WORKFLOW.md`.
- The orchestrator owns polling, dispatch, retries, stop/release decisions, and runtime state.
- Coding-agent child processes should not require direct tracker credential access when host-side secret references are used.

### elixir/README.md

Reference Elixir/OTP implementation guide:
- Tracker adapters included: Linear, GitHub Issues, Jira Cloud, Asana, and GitLab.
- Uses Codex App Server mode inside each issue workspace.
- Supports tracker-native tools (`linear_graphql`, `github_api`, `jira_rest`, `asana_api`, `gitlab_api`) executed with host-side auth.
- If a claimed issue enters terminal states (`Done`, `Closed`, `Cancelled`, `Duplicate`), Symphony stops the agent and cleans matching workspaces.
- Includes setup commands with `mise`, `mix setup`, `mix build`, and `./bin/symphony ./WORKFLOW.md`.
- Documents optional observability server via `--port`, plus YAML-frontmatter workflow config and prompt body contract.

### elixir/WORKFLOW.md

Concrete workflow profile used by the reference implementation:
- `tracker.kind: linear` with active states (`Todo`, `In Progress`, `Merging`, `Rework`) and terminal states (`Closed`, `Cancelled`, `Duplicate`, `Done`).
- Poll interval: `5000ms`.
- Workspace root: `~/code/symphony-workspaces`.
- `after_create` hook clones `openai/symphony` and prepares Elixir deps.
- Agent concurrency defaults: `max_concurrent_agents: 10`, `max_turns: 20`.
- Codex command defaults to app-server mode with explicit model config and workspace-write sandboxing.
- Prompt body encodes unattended execution rules, state-machine routing (`Todo`/`In Progress`/`Human Review`/`Merging`/`Rework`), persistent workpad behavior, and validation discipline.

### docs/

- `docs/symphony-smoke-board-review.md` — board review smoke-test marker.
- `docs/symphony-smoke-test-one.md` — isolated Jira smoke-test marker.

## Top-level structure
- `.codex/` — Codex-specific helpers (`skills/`, `worktree_init.sh`)
- `.github/` — media and workflow automation assets (boilerplate; not fetched)
- `README.md` — high-level concept and run options
- `SPEC.md` — language-agnostic orchestration specification
- `docs/` — smoke-test documentation files
- `elixir/` — reference implementation (OTP app, runtime config, docs, tests)
  - `AGENTS.md` — implementation conventions and validation rules
  - `WORKFLOW.md` — default tracker/workspace/codex policy contract
  - `lib/` — orchestrator, config, adapters, runner, workspace management
  - `test/` — behavior and integration tests for runtime flows
