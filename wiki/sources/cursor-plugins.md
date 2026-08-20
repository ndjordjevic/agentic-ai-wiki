---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/cursor/plugins
tags:
  - cursor-plugins
  - agent-skills
  - plugin-marketplace
  - cursor-sdk
  - code-review-automation
  - principle-skills
related:
  - anthropics-skills
  - coreyhaines31-makerskills
product: cursor-plugins
detail_level: standard
created: 2026-07-24
updated: 2026-08-20
---

Official marketplace repo for Cursor's plugin system: a spec for packaging Cursor plugins (skills, rules, MCP servers, hooks) plus 13 first-party and community plugins bundling 75 agent skills for CI, code review, PR workflows, learning, orchestration, and disciplined engineering practices. It is a concrete, large-scale example of the "plugin bundles skills + rules + MCP config" pattern also seen in [[anthropics-skills]], useful for comparing how Cursor structures its marketplace against Anthropic's skill ecosystem.

_All claims below are sourced from ../../raw/github/cursor-plugins.md unless otherwise noted._

## What it does
Cursor plugins are standalone directories at the repo root, each with a `.cursor-plugin/plugin.json` manifest declaring the plugin's name, author, category, and pointers to its `skills/` (Agent Skills as `SKILL.md` files), `rules/` (`.mdc` Cursor rules), and optional `mcp.json` (MCP server definitions) or `hooks/`. The root `.cursor-plugin/marketplace.json` lists every plugin for discovery, and `schemas/` holds the JSON Schemas (`marketplace.schema.json`, `plugin.schema.json`) that validate both levels of manifest, checked by `scripts/validate-plugins.mjs`.

## Key features
13 plugins ship in the repo (11 documented in the README table, plus `ralph-loop` and `teaching` present as valid plugin directories not yet listed there):

- **agent-compatibility** — CLI-backed repo compatibility scans plus agents that audit startup, validation, and docs against reality (1 skill: `check-agent-compatibility`).
- **cli-for-agent** — Patterns for designing agent-friendly CLIs: flags, `--help` with examples, pipelines, errors, idempotency, dry-run (1 skill: `cli-for-agents`).
- **continual-learning** — Incremental transcript-driven memory updates for `AGENTS.md` using high-signal bullet points (1 skill: `continual-learning`).
- **create-plugin** — Scaffold and validate new Cursor plugins (2 skills: `create-plugin-scaffold`, `review-plugin-submission`).
- **cursor-sdk** — Guidance for building on the Cursor TypeScript SDK (`@cursor/sdk`): runtime selection, auth, streaming, MCP, error handling (1 skill: `cursor-sdk`).
- **cursor-team-kit** — Cursor's own internal team workflows: CI, code review, shipping, local automation, verification (18 skills covering compiler checks, PR creation/review, CI fixing, merge-conflict resolution, smoke tests, weekly reviews, and more).
- **docs-canvas** — Renders documentation as a navigable Cursor Canvas with sections, TOC, and cross-references (1 skill: `docs-canvas`).
- **orchestrate** — Fans a large task out across parallel Cursor cloud agents (planners, workers, verifiers) via the SDK, invoked only via explicit `/orchestrate <goal>` (1 skill: `orchestrate`).
- **pr-review-canvas** — Renders a PR diff review as an interactive Canvas grouped by reviewer importance (1 skill: `pr-review-canvas`).
- **pstack** — Lauren Tan's large third-party plugin ("go fast, go deep first"): 38 skills spanning named workflows (`architect`, `arena`, `blast-radius`, `figure-it-out`, `interrogate`, `recall`, `reflect`, `teach`, `tdd`, `unslop`, `why`, `how`, `show-me-your-work`, and more) plus 22 standalone "principle" skills — each one auto-applying engineering discipline rules (boundary discipline, root-cause fixes, idempotent operations, type-system discipline, minimizing reader load, subtract-before-you-add, and others) rather than being explicitly invoked.
- **ralph-loop** — Continuous self-referential AI loops implementing the "Ralph Wiggum technique": run the agent in a while-true loop with the same prompt until task completion (3 skills: `ralph-loop`, `cancel-ralph`, `ralph-loop-help`).
- **teaching** — Skill mapping, practice plans, and learning retrospectives; builds personalized roadmaps with milestones (2 skills: `create-learning-path`, `run-learning-retrospective`).
- **thermos** — "Thermo-nuclear" branch review: deep security/correctness audits and harsh code-quality rubrics via parallel subagents (3 skills: `thermo-nuclear-review`, `thermo-nuclear-code-quality-review`, `thermos`, which runs both in parallel and synthesizes findings).

Full skill-by-skill descriptions for all 75 skills are in `../../raw/github/cursor-plugins.md` under `## Docs`.

## Architecture
Manifests form a two-level hierarchy: a repo-root `marketplace.json` enumerates plugins, and each plugin's `plugin.json` declares its own metadata plus relative paths to its `skills/`, `rules/`, and optional `mcp.json`/`hooks/` directories. Skills follow the same `SKILL.md`-with-YAML-frontmatter convention as Anthropic's Agent Skills (`name`, `description`, optional `disable-model-invocation: true` to make a skill invoke-only rather than auto-triggered, and in `pstack`'s case a `mode: true` flag for whole-session style skills like `Poteto Mode`).

## Example usage
Plugins are consumed by installing the repo (or individual plugin directories) into a Cursor workspace's plugin path so their `skills/`, `rules/`, and `mcp.json` are picked up by the IDE; `scripts/validate-plugins.mjs` is the repo's own CI check that a submitted plugin's manifest and skill frontmatter conform to `schemas/plugin.schema.json` before merge.

## When to use
Reach for this repo as a reference implementation when designing a plugin/skill marketplace (manifest schema, validation script, category taxonomy), or to adopt individual plugins directly: `cursor-team-kit` and `thermos` for CI/PR/code-review automation, `pstack` for a dense library of engineering-discipline skills, `cursor-sdk`/`orchestrate` for programmatic multi-agent Cursor workflows, and `ralph-loop`/`teaching` for iterative-development and learning-support loops.

## Ecosystem
Plugins interoperate loosely: `cursor-team-kit` and `thermos` both ship a `thermo-nuclear-code-quality-review` skill (shared workflow, packaged in two places), and `pr-review-canvas` exists both as its own plugin and duplicated inside `cursor-team-kit`. The pattern of bundling skills + rules + MCP config into one installable plugin parallels [[anthropics-skills]]'s skill-marketplace approach, though Cursor's manifest adds an explicit two-level (marketplace + plugin) schema with CI validation.
