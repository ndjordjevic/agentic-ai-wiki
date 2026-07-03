---
type: source
source_url: https://github.com/langchain-ai/openwiki
tags: [openwiki-cli, agent-documentation, deepagents, self-updating-docs, github-actions, agents-md, provider-agnostic]
related: [6eanut-llm-wiki, langchain.com-deepagents, langchain.com-langsmith, langchain.com]
product: openwiki
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`langchain-ai/openwiki` is a TypeScript CLI, built by LangChain, that writes and maintains documentation for a codebase specifically so agents can consume it. Rather than a human-facing README generator, it runs a DeepAgents-backed agent that inspects a target repository and produces (and keeps refreshed) a structured `openwiki/` directory, then wires `AGENTS.md`/`CLAUDE.md` to point coding agents at it — an implementation of the same "compile knowledge once, look it up cheaply" idea seen in [[6eanut-llm-wiki]], but automated end-to-end by an LLM agent instead of a Claude Code skill workflow.

_All claims below are sourced from ../../raw/github/langchain-ai-openwiki.md unless otherwise noted._

## What it does

`openwiki` is installed globally (`npm install -g openwiki`) and run from inside the target repository. `openwiki --init` bootstraps documentation into `openwiki/` when none exists; `openwiki --update` refreshes it against repository changes. The CLI launches an interactive Ink-based terminal app by default so the user can chat with the agent and send follow-ups; `-p`/`--print` runs a single one-shot pass and prints the final output instead of staying open. It auto-exits after a successful non-interactive `--init`/`--update` run. On first run it walks the user through configuring an inference provider, API key, and model, saved to `~/.openwiki/.env`.

## Installation

```sh
npm install -g openwiki
openwiki --init
```

Optionally add the provided GitHub Actions workflow (`examples/openwiki-update.yml`) as `.github/workflows/openwiki-update.yml` so a scheduled job opens a PR once a day with documentation updates.

## Key features

- **Agent-oriented output, not human docs** — `AGENTS.md`/`CLAUDE.md` are automatically created or appended with a pointer to `openwiki/quickstart.md`, so coding agents pick up the generated wiki as their first stop; the repo dogfoods this on itself.
- **DeepAgents-backed runtime** — uses a [[langchain.com-deepagents|Deep Agents]] local-shell backend with a virtual filesystem rooted at the target repo, giving the documentation agent planning, file read/write tools, and subagent delegation rather than a single fixed prompt.
- **Multi-provider model support** — OpenRouter (default), Anthropic, OpenAI, Baseten, and Fireworks, each with pre-defined model shortlists (GLM, Kimi, Sonnet, etc.) plus support for arbitrary custom model IDs per provider; provider configs are centralized in `src/constants.ts`.
- **Git-evidence-driven updates** — `src/agent/utils.ts` collects git evidence and content snapshots and records successful runs in `openwiki/.last-update.json`, so `--update` runs are scoped to what actually changed.
- **Optional LangSmith tracing** — a LangSmith API key can be configured to trace OpenWiki's own agent runs to a "openwiki" project, tying it into [[langchain.com-langsmith|LangSmith]]'s observability tooling.
- **Scheduled self-maintenance** — the example GitHub Actions workflow runs the CLI on a cron schedule and opens a PR with doc updates, so the generated wiki stays current without a human re-running the tool.

## Architecture

The CLI surface is split across `src/cli.tsx` (Ink UI, run lifecycle, auto-exit) and `src/commands.ts` (argument parsing, help text). Documentation generation itself lives under `src/agent/`: `index.ts` creates the provider-specific model, runs the agent, and writes update metadata; `prompt.ts` assembles the documentation-run instructions and the rules for inserting into `AGENTS.md`/`CLAUDE.md`; `types.ts` holds shared run/event types; `utils.ts` handles git evidence collection and `.last-update.json`. Credential bootstrap (`src/credentials.tsx`) and persistence (`src/env.ts`) are separated from the agent runtime, so provider/model selection and secret storage don't leak into the documentation-generation logic. The repository's own generated output — under `openwiki/` (`quickstart.md`, `architecture/`, `cli/`, `agent/`, `operations/`) — is treated as agent-generated content, not application source, and is itself the dogfooded proof that the tool works on its own codebase.

## Example usage

```sh
openwiki --init
openwiki "Please generate documentation for this repository"
openwiki -p "Summarize what you can do"
openwiki --update
openwiki --help
```

## Maintenance status

1,314 stars, 102 forks as of 2026-07-03. MIT licensed, TypeScript, default branch `main`, no tagged releases yet — actively developed (pushed same day as this ingest). Built and maintained by the LangChain team ([[langchain.com]]), alongside [[langchain.com-deepagents|Deep Agents]] and [[langchain.com-langsmith|LangSmith]], which OpenWiki's runtime and optional tracing depend on respectively.
