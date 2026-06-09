---
type: source
source_url: https://skills.sh/
companion_urls:
  - https://github.com/vercel-labs/skills
raw_files:
  - ../../raw/web/skills.sh.md
  - ../../raw/github/vercel-labs-skills.md
tags:
  - agent-skills
  - skills-ecosystem
  - cli-tool
  - skill-discovery
  - agent-extensions
  - procedural-knowledge
  - multi-agent-compatibility
  - vercel
related:
  - paperclip.ing
  - shareai-lab-learn-claude-code
  - graphify.net
  - must-have-clis-2026
  - anthropics-skills
  - nidhinjs-prompt-master
  - obra-superpowers
  - github-spec-kit
  - browse.sh
  - openvibe.sh
  - vercel-labs-agent-browser
  - garrytan-gstack
  - voltagent-awesome-agent-skills
product: skills
detail_level: standard
created: 2026-04-30
updated: 2026-06-09
---

skills.sh is the open agent skills directory and ecosystem, built by Vercel, that lets developers discover, install, and publish reusable capability modules — called "skills" — for AI coding agents. It pairs a public leaderboard at skills.sh with an open-source CLI (`npx skills`) backed by the `vercel-labs/skills` repo, together forming the de-facto distribution layer for SKILL.md-based agent instructions across 50+ supported agents including Claude Code, GitHub Copilot, Cursor, Codex, OpenCode, and Windsurf.

_All claims below are sourced from ../../raw/web/skills.sh.md unless otherwise noted._

## What it does

skills.sh is the discovery and distribution hub for agent skills. The site surfaces a community-ranked leaderboard of GitHub repositories containing skill files, curated official skills published directly by technology vendors (Anthropic, Microsoft, OpenAI, GitHub, Sentry, Cloudflare, and many more), a security audit dashboard (combining Gen Agent Trust Hub, Socket, and Snyk), and a trending view showing recently popular skill repositories.

## Key features

- **Leaderboard** — aggregates anonymous telemetry from the CLI to rank skill repositories by install count, surfacing the most-used and most-popular skills in the ecosystem.
- **Official skills** — a dedicated `/official` page listing vendor-published skill repos from 70+ technology companies; entries include Anthropic (289 skills), Microsoft (446 skills across Azure), GitHub (354 skills), OpenAI (195), Sentry (271), Firecrawl (234), and many more.
- **Security audits** — `/audits` page shows per-skill audit results from three independent security providers; status values include Safe, Pending, and risk levels (Low/Med/High/Critical).
- **CLI (`npx skills`)** — the install, manage, and discovery interface for skills, open-source at `github.com/vercel-labs/skills` (../../raw/github/vercel-labs-skills.md); supports GitHub shorthand, full URLs, GitLab, and local paths.
- **Multi-agent support** — skills install to any of 50+ agents with a single command; the CLI auto-detects which agents are installed and places files in the correct agent-specific directory. (../../raw/github/vercel-labs-skills.md)

## Architecture

The `skills` CLI is a TypeScript tool distributed via `npx`. Skills are SKILL.md files with YAML frontmatter (`name:`, `description:`) placed in agent-specific directories; the CLI brokers discovery and placement. Installation supports two modes: **Symlink** (recommended — single canonical copy, symlinked to each agent directory) and **Copy** (independent copies per agent). Skills ship in repositories at conventional paths: `skills/`, `skills/.curated/`, `skills/.experimental/`, `.claude/skills/`, `.agents/skills/`, and equivalent agent-specific subdirectories. The CLI also reads `.claude-plugin/marketplace.json` for plugin-marketplace compatibility. (../../raw/github/vercel-labs-skills.md)

The leaderboard ranking uses anonymous telemetry from CLI installs — only which skill repo was installed, never personal information. Telemetry is disabled automatically in CI environments and can be suppressed via `DISABLE_TELEMETRY` or `DO_NOT_TRACK`. (../../raw/github/vercel-labs-skills.md)

## Installation

```bash
# Install a skill repo
npx skills add vercel-labs/agent-skills

# Install specific skills only
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install globally (all projects)
npx skills add vercel-labs/agent-skills -g

# Target specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a cursor

# Non-interactive (CI/CD)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y
```

Other commands: `npx skills list`, `npx skills find [query]`, `npx skills update [skills]`, `npx skills remove [skills]`, `npx skills init [name]` (scaffold a new SKILL.md). (../../raw/github/vercel-labs-skills.md)

## Example usage

```bash
# Discover what skills are available in a repo before installing
npx skills add vercel-labs/agent-skills --list

# Install all skills from a repo to all agents
npx skills add vercel-labs/agent-skills --all

# Install all skills for a specific agent (e.g., Claude Code)
npx skills add vercel-labs/agent-skills --skill '*' -a claude-code

# Search for skills by keyword
npx skills find typescript

# Update all installed skills
npx skills update -y
```

A minimal SKILL.md looks like:

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# My Skill

Instructions for the agent to follow when this skill is activated.
```

(../../raw/github/vercel-labs-skills.md)

## When to use

Use skills.sh when you want to extend your AI coding agent with pre-built or community-maintained procedural knowledge — for things like release-note generation, PR conventions, external service integrations (Linear, Notion, etc.), framework-specific best practices, or domain-specific workflows. It is the right starting point before writing a custom SKILL.md from scratch: search the leaderboard and official pages first to see if a skill already exists for your use case.

## Maintenance status

The `vercel-labs/skills` repo is actively maintained by Vercel with 16,547 stars, 1,339 forks, latest release v1.5.1 (2026-04-17), and a recent push date of 2026-04-28. The project is MIT-licensed. It is the reference implementation of the Agent Skills specification at agentskills.io and the infrastructure backing the skills.sh leaderboard. (../../raw/github/vercel-labs-skills.md)

## Ecosystem

skills.sh indexes the broader open-agent-skills ecosystem, which includes a formal specification at [agentskills.io](https://agentskills.io) and an official skills repository at `github.com/vercel-labs/agent-skills`. Skill compatibility varies slightly across agents — most support basic skills and `allowed-tools`; `context: fork` is Claude Code-only; Hooks are supported by Claude Code, Cline, and Kiro CLI. The ecosystem connects directly to the agent tooling space covered by [[paperclip.ing]], which uses Claude Code, Codex, Cursor, and OpenClaw as agent runtimes that skills can enhance.

## Documentation

The primary docs live at `skills.sh/docs` and cover installation, skill structure, ranking methodology, and security policy. Full CLI reference — all commands, options, compatibility tables, environment variables, and agent path tables — is in the README at `github.com/vercel-labs/skills`.
