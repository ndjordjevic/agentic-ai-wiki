# langchain-ai/openwiki

## Metadata
- Stars: 1314
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage:
- Fetched: 2026-07-03
- Final URL: https://github.com/langchain-ai/openwiki

## Description
OpenWiki is a CLI that writes and maintains agent documentation for your codebase.

## README
# OpenWiki

OpenWiki is a CLI that writes and maintains documentation for your codebase, built specifically for agents.

![OpenWiki](https://raw.githubusercontent.com/langchain-ai/openwiki/main/static/openwiki.png)

## Install

```sh
npm install -g openwiki
```

## Quick Start

Initialize OpenWiki, configure your model and API key, then generate documentation

```sh
openwiki --init
```

Then to ensure your documentation stays up-to-date, add the GitHub action to your repository to automatically open a PR once a day with documentation updates: [openwiki-update.yml](./examples/openwiki-update.yml)

Copy the contents of that file into `.github/workflows/openwiki-update.yml` in your repository.

## Usage

Start the interactive CLI:

```sh
openwiki
```

Start OpenWiki with an initial request:

```sh
openwiki "Please generate documentation for this repository"
```

Run a single command and exit:

```sh
openwiki -p "Summarize what you can do"
```

Initialize OpenWiki:

```sh
openwiki --init
```

Update existing documentation:

```sh
openwiki --update
```

Show help:

```sh
openwiki --help
```

`openwiki` creates initial documentation in `openwiki/` when no wiki exists. If `openwiki/` already exists, it refreshes that documentation from repository changes. By default, the CLI stays open after each run so you can send follow-up messages. Use `-p` or `--print` for a one-shot non-interactive run that prints the final assistant output.

`openwiki` will automatically append prompting to your `AGENTS.md` and/or `CLAUDE.md` files to instruct your coding agent to reference it when searching for context. If the file does not already exist in your repository, OpenWiki will create it for you.

On the first interactive run, OpenWiki will have you configure your inference provider, API key, and LLM. You will also be able to set a LangSmith API key to trace your OpenWiki runs to a LangSmith tracing project named "openwiki" (optional).

These configuration options and secrets will be saved to `~/.openwiki/.env` on your local machine.

## Customizing

OpenWiki supports OpenRouter, Fireworks, Baseten, OpenAI and Anthropic out of the box. By default, there are a few models pre-defined (GLM 5.2, Kimi K2.6, Sonnet 5, etc) but for each inference provider, OpenWiki will allow you to specify your own custom model ID.

If there's an inference provider or model you'd like to see added, please open a PR!

## Docs

### DEVELOPMENT.md
# Development

## Run Against Another Local Repo

Prerequisites:

- Node.js 20 or newer
- pnpm

Set up pnpm's global bin directory once if `pnpm link --global` has not worked
on this machine yet:

```sh
pnpm setup
```

Restart your shell, or source the profile file that `pnpm setup` changed. Then
set up and link this package:

```sh
cd /Users/bracesproul/code/lang-chain-ai/projects/agent-docs
pnpm install
pnpm run build
pnpm link --global
```

Run a dry test from the repo you want OpenWiki to inspect:

```sh
cd /path/to/target/repo
OPENWIKI_DEV=1 openwiki --dry-run
```

Run the real CLI from the target repo:

```sh
cd /path/to/target/repo
openwiki
openwiki -p "Summarize what you can do"
openwiki --modelId openai/gpt-5.5
openwiki "Please focus on API documentation"
```

The target repo is still the current working directory. The global link only
avoids typing the path to `dist/cli.js`.

If you do not want to configure pnpm globals, use a shell alias instead:

```sh
alias openwiki='node /Users/bracesproul/code/lang-chain-ai/projects/agent-docs/dist/cli.js'
```

That alias can go in `~/.zshrc` if you want it to persist.

After changing OpenWiki source code, rebuild from this package directory:

```sh
pnpm run build
```

The existing global link will keep using the rebuilt `dist/cli.js`.

Real runs can write:

- `openwiki/`
- `~/.openwiki/.env` for local OpenRouter model/key settings and optional LangSmith credentials

Scheduled update workflow example:

- `examples/openwiki-update.yml`

### AGENTS.md / CLAUDE.md (self-referential agent instructions)
Both files contain identical content, inserted by OpenWiki itself into this repo:

```
## OpenWiki

This repository has documentation located in the /openwiki directory.

Start here:

- [OpenWiki quickstart](openwiki/quickstart.md)

OpenWiki includes repository overview, architecture notes, workflows, domain concepts, operations, integrations, testing guidance, and source maps.

When working in this repository, read the OpenWiki quickstart first, then follow its links to the relevant architecture, workflow, domain, operation, and testing notes.
```

### openwiki/quickstart.md (dogfooded output of the tool itself)
# OpenWiki quickstart

OpenWiki is a TypeScript CLI that writes and maintains documentation for a repository using an agent-driven workflow. The package exposes a single `openwiki` binary, stores local credentials in `~/.openwiki/.env`, and records successful update metadata in `openwiki/.last-update.json`.

## What this repository does

- Launches an interactive Ink-based terminal app for chatting with the OpenWiki agent.
- Supports one-shot documentation runs with `--init`, `--update`, and `--print`.
- Supports multiple model providers — OpenRouter (default), Anthropic, OpenAI, Baseten, and Fireworks — each with their own API key and model list.
- Uses a DeepAgents local shell backend with virtual filesystem paths rooted at the target repository.
- Creates or refreshes documentation under the target repository's `openwiki/` directory.
- Auto-exits after successful `--init` or `--update` runs in an interactive terminal, so the CLI works as both a one-shot and interactive tool.
- Optionally schedules automated updates through a GitHub Actions workflow.

## Start here

- Architecture overview — runtime structure, major modules, and execution flow.
- CLI usage — commands, options, model/provider selection, and credential bootstrap.
- Agent workflow — how documentation runs are assembled and persisted.
- Credentials and updates — local env storage, metadata, and scheduled updates.

## Key source files

- `README.md` — user-facing installation and usage summary.
- `package.json` — bin entrypoint, scripts, and dependencies.
- `src/cli.tsx` — Ink UI, command execution, auto-exit, and run lifecycle.
- `src/commands.ts` — CLI parsing and help content.
- `src/agent/index.ts` — agent runtime, provider-specific model creation, fallback, and metadata writes.
- `src/agent/prompt.ts` — prompt assembly, documentation-run instructions, and AGENTS.md/CLAUDE.md insertion rules.
- `src/agent/utils.ts` — git evidence collection, content snapshot, and `.last-update.json` handling.
- `src/agent/types.ts` — shared agent types (`OpenWikiCommand`, `RunContext`, `UpdateMetadata`, run options/events).
- `src/env.ts` — `~/.openwiki/.env` persistence and credential diagnostics.
- `src/credentials.tsx` — interactive onboarding flow for provider selection, API keys, and model selection.
- `src/constants.ts` — provider configs, model options, env keys, and validation helpers.
- `.github/workflows/openwiki-update.yml` — scheduled automation example.

## Notes for future agents

- The repository is intentionally focused: the main product surface is the CLI plus the documentation-generation agent.
- Treat `openwiki/` in this repo as generated documentation output from a future OpenWiki run, not as application source.
- When changing behavior, verify both the CLI parser and the agent prompt/runtime, because user-visible semantics are split across `src/commands.ts`, `src/cli.tsx`, and `src/agent/*`.
- Provider support is centralized in `src/constants.ts`. Adding or changing a provider means updating `PROVIDER_CONFIGS`, the `OpenWikiProvider` type, and the model-creation branch in `src/agent/index.ts`.

## Top-level structure
- `.github/` — CI/workflow config (boilerplate, not detailed here)
- `AGENTS.md`, `CLAUDE.md` — identical agent-facing pointer docs, auto-inserted by OpenWiki, linking to `openwiki/quickstart.md`
- `DEVELOPMENT.md` — local dev/link instructions for running OpenWiki against another target repo
- `LICENSE` — MIT
- `README.md` — install/usage
- `examples/` — contains `openwiki-update.yml`, a scheduled GitHub Actions workflow example for automated doc updates
- `openwiki/` — OpenWiki's own dogfooded documentation output (`quickstart.md`, `agent/`, `architecture/`, `cli/`, `operations/`, `.last-update.json`)
- `package.json`, `pnpm-lock.yaml`, `tsconfig.json`, `eslint.config.js` — TypeScript/pnpm project config
- `src/` — CLI and agent source:
  - `cli.tsx` — Ink-based terminal UI, run lifecycle, auto-exit
  - `commands.ts` — CLI argument parsing and help text
  - `constants.ts` — provider configs (OpenRouter, Anthropic, OpenAI, Baseten, Fireworks), model options
  - `credentials.tsx` — interactive onboarding for provider/API key/model selection
  - `env.ts` — `~/.openwiki/.env` persistence
  - `agent/` — `index.ts` (agent runtime, provider-specific model creation, metadata writes), `prompt.ts` (prompt assembly, AGENTS.md/CLAUDE.md insertion rules), `types.ts` (shared types), `utils.ts` (git evidence collection, `.last-update.json` handling)
- `static/` — README screenshot asset
