---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/github/awesome-copilot
tags:
  - agent-skills
  - custom-agents
  - copilot-instructions
  - plugin-marketplace
  - agentic-workflows
  - session-hooks
  - awesome-list
related: [voltagent-awesome-agent-skills, anthropics-skills]
product: awesome-copilot
detail_level: standard
created: 2026-10-01
updated: 2026-10-01
---

GitHub's official community-maintained catalog for customizing GitHub Copilot — a single repository bundling custom agents, path-scoped instructions, Agent Skills, session hooks, Agentic Workflows, and installable plugins, all discoverable through a dedicated marketplace site and machine-readable `llms.txt`. It is the canonical "awesome list" for the Copilot ecosystem specifically (as opposed to Claude-/general-agent-focused lists like [[voltagent-awesome-agent-skills]]), maintained directly by GitHub with automated quality gates for external contributions.

_All claims below are sourced from ../../raw/github/github-awesome-copilot.md unless otherwise noted._

## What it does

The repo aggregates six primitive types for extending GitHub Copilot: **Agents** (`*.agent.md`, 222 entries) that specialize Copilot's coding agent for a domain via file-based config and optional MCP servers; **Instructions** (`*.instructions.md`, 194 entries) that apply coding standards automatically by file-pattern match; **Skills** (folders with `SKILL.md` + bundled assets, 426 entries) following the Agent Skills specification for progressive-disclosure, on-demand capabilities; **Hooks** (folders with `README.md` + `hooks.json`, 8 entries) that trigger on Copilot coding-agent session events (`sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `errorOccurred`); **Agentic Workflows** (8 `.md` files compiled via `gh aw compile` into GitHub Actions) for event-triggered or scheduled repository automation; and **Plugins** (curated bundles of agents/skills/hooks around a theme, 100 entries) installable as one unit.

## Installation

Per-primitive install paths, all via the main README / docs catalogs:
- **Agents / Instructions:** click the VS Code or VS Code Insiders install badge next to an entry, or download the `.agent.md` / `.instructions.md` file directly into the repo (`.github/copilot-instructions.md` for repo-wide instructions, or `.github/instructions/` for path-scoped ones in VS Code).
- **Skills:** `gh skills install github/awesome-copilot <skill-name>` (requires GitHub CLI v2.90.0+), or copy the skill folder manually into a local skills directory.
- **Hooks:** copy the hook folder into `.github/hooks/`, `chmod +x` any bundled scripts, commit to the default branch.
- **Agentic Workflows:** install the `gh aw` extension (`gh extension install github/gh-aw`), copy the workflow `.md` into `.github/workflows/`, then `gh aw compile` to generate the `.lock.yml`.
- **Plugins:** `copilot plugin install <plugin-name>@awesome-copilot` in Copilot CLI (the marketplace is pre-registered by default) — or `@agentPlugins` / "Chat: Plugins" in VS Code's Extensions view.

## Key features

- **Marketplace-first distribution:** Awesome Copilot is registered as a default plugin marketplace in both Copilot CLI and VS Code, so plugins install with a single command — no manual marketplace registration needed for most users.
- **Machine-readable catalog:** a structured `llms.txt` at `awesome-copilot.github.com/llms.txt` lists all agents, instructions, and skills for AI-agent consumption, plus a full-text-searchable **Learning Hub** website with guides on agents, skills, instructions, hooks, MCP servers, and the Copilot coding agent.
- **Canvas extensions:** a separate `extensions/` directory holds reusable interactive VS Code Chat "canvas" UI sources (e.g. `accessibility-kanban`, `diagram-viewer`, `git-worktree-explorer`, `jupyter-notebooks`), which several plugins bundle alongside their agents/skills.
- **Contributor tooling:** `eng/` ships Node.js scripts for plugin-schema validation, skill/plugin scaffolding (`create-skill.mjs`, `create-plugin.mjs`), and automated external-contribution quality gates (`external-plugin-quality-gates.mjs`, `external-plugin-intake.mjs`) that vet community PRs before merge.

## Architecture

The repo is a flat, type-partitioned monorepo rather than a single framework: `agents/`, `instructions/`, `skills/`, `hooks/`, `workflows/`, and `plugins/` each hold self-contained files/folders validated against JSON Schemas in `.schemas/`. `docs/README.<type>.md` are generated catalog pages (one per primitive type) that the root `README.md` links out to; the `website/` directory builds the separately hosted marketplace/search site from this same data. `AGENTS.md` documents the repo structure explicitly for AI coding agents working in the repo itself — a notable instance of a project using its own target format (Copilot-oriented guidance files) to guide contributions to itself.

## Example usage

Install a themed plugin directly from the default marketplace:
```bash
copilot plugin install context-engineering@awesome-copilot
```
Or, on an older CLI/custom setup where the marketplace isn't pre-registered:
```bash
copilot plugin marketplace add github/awesome-copilot
copilot plugin install <plugin-name>@awesome-copilot
```
Install a single skill via GitHub CLI:
```bash
gh skills install github/awesome-copilot acquire-codebase-knowledge
```

## When to use

Reach for this repo when customizing GitHub Copilot specifically (agents, instructions, skills, hooks, workflows, or plugins scoped to Copilot CLI / VS Code / Copilot coding agent) rather than a general or Claude-oriented agent setup — it is the first-party, actively curated source for that ecosystem, with built-in install affordances (VS Code badges, `gh` CLI commands, plugin marketplace) that most community lists lack.

## Ecosystem

Positioned alongside other Copilot-customization primitives already in this wiki: it packages the same Agent Skills specification referenced by [[voltagent-awesome-agent-skills]] and [[anthropics-skills]], but is organized around GitHub Copilot's specific primitive types (agents, hooks, Agentic Workflows, plugins) rather than being Claude- or spec-driven-development-centric like [[obra-superpowers]] or [[github-spec-kit]]. Its Agentic Workflows primitive depends on the separate `github/gh-aw` CLI/spec.
