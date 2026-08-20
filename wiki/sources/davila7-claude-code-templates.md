---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/davila7/claude-code-templates
tags:
  - claude-code
  - component-catalog
  - agents
  - commands
  - mcp-integrations
  - hooks
  - skills
  - session-analytics
related:
  - anthropics-skills
  - obra-superpowers
  - claudemarketplaces.com
  - skills.sh
  - bradautomates-claude-video
  - oso95-scroll-world
  - googleworkspace-cli
  - mvanhorn-last30days-skill
  - coreyhaines31-makerskills
  - nvidia-skillspector
product: claude-code-templates
detail_level: standard
created: 2026-07-14
updated: 2026-08-20
---

claude-code-templates (published to npm as `claude-code-templates`, browsable at [aitmpl.com](https://aitmpl.com)) is a large, actively maintained catalog and CLI installer for Claude Code components — 600+ agents, 200+ commands, 55+ MCP integrations, 60+ settings, 39+ hooks, 18+ autonomous "loops," and 14+ full project templates — plus a set of standalone dev tools (real-time session analytics dashboard, mobile conversation monitor, health-check diagnostics, plugin/marketplace dashboard). It's one of the largest third-party distribution points for ready-made Claude Code configuration in the ecosystem, aggregating and re-licensing components from several other community and Anthropic-official sources.

_All claims below are sourced from ../../raw/github/davila7-claude-code-templates.md unless otherwise noted._

## What it does

The core is a Node.js CLI (`npx claude-code-templates@latest`) that installs individual components or full stacks into a project's `.claude/` configuration in one command, e.g. `npx claude-code-templates@latest --agent development-tools/code-reviewer --yes` or a combined install of an agent + command + MCP in a single invocation. Interactive mode (no flags) walks through framework auto-detection and guided setup. Beyond installation, the CLI doubles as an operational toolkit: `--analytics` launches a real-time dashboard for live session state and performance metrics, `--chats` (optionally `--tunnel` via Cloudflare) gives a mobile-friendly view of ongoing Claude responses, `--health-check` runs installation diagnostics, and `--plugins` manages installed plugin marketplaces and permissions from one screen. A companion Rust implementation (`cli-rust/`) exists alongside the primary Node CLI.

## Key features

- **Component types**: Agents (AI specialists for specific domains — security auditor, React performance, database architecture), Commands (custom slash commands like `/generate-tests`, `/optimize-bundle`), MCPs (GitHub, PostgreSQL, Stripe, AWS, OpenAI and more), Settings (timeouts, memory, output styles), Hooks (pre-commit validation, post-completion triggers), Skills (progressive-disclosure capabilities such as PDF processing or Excel automation), and Loops (autonomous goal+interval+stop-condition workflows that chain other components, e.g. `--loop engineering/docs-sweep-loop`).
- **"Global Agents"**: agents createable once (`--create-agent <name>`) and invokable from any project via the Claude Code SDK, not scoped to a single repo.
- **Framework-aware setup**: auto-detects project stack (JS/TS — React, Vue, Angular, Node; Python — Django, Flask, FastAPI) and installs matching CLAUDE.md/commands; Go and Rust support listed as in progress.
- **Aggregated, re-licensed catalog**: pulls and republishes components from K-Dense-AI/claude-scientific-skills (139 skills, MIT), anthropics/skills (21 skills), anthropics/claude-code guides (10 skills), obra/superpowers (14 skills, MIT), alirezarezvani/claude-skills (36 skills, MIT), wshobson/agents (48 agents, MIT), plus awesome-claude-code (CC0) and awesome-claude-skills (Apache 2.0) — each retaining its original license and attribution.

## Architecture

The repo is a monorepo spanning several deployable surfaces: `cli-tool/` is the primary Node.js CLI package published to npm (components under `cli-tool/components/{type}/{category}/{name}.md`, kebab-case files with YAML frontmatter); `cli-rust/` is a parallel Rust implementation; `dashboard/` is an Astro app deployed to Cloudflare Pages (`app.aitmpl.com`) hosting the API routes and web dashboard; `cloudflare-workers/` holds independent Worker projects (notably a `crons` worker that replaced former Vercel cron jobs, calling dashboard API endpoints on a schedule via a shared secret); `docs/` is the static aitmpl.com component-browser website; `database/` holds Supabase/Neon schema assets. Key API endpoints live at `dashboard/src/pages/api/`: `/api/track-download-supabase` records every CLI install (Supabase-backed analytics), `/api/discord/interactions` powers a Discord bot (`/search`, `/info`, `/install`, `/popular`), and `/api/claude-code-check` polls upstream Claude Code releases every 30 minutes and stores results in Neon. (../../raw/github/davila7-claude-code-templates.md)

New or modified components must pass review by a dedicated `component-reviewer` subagent (checks YAML frontmatter validity, kebab-case naming, absence of hardcoded secrets, relative-only paths, description clarity, and correct category placement) before the catalog JSON is regenerated via `python scripts/generate_components_json.py`. Skills specifically are also statically scanned by SkillSpector (NVIDIA, Apache-2.0; 64 vulnerability-pattern checks covering prompt injection, data exfiltration, supply-chain risk, and dangerous code patterns) in `--no-llm` mode — a PR-triggered workflow blocks merges when a changed skill scores HIGH/CRITICAL (risk score > 50), and a separate weekly/manual workflow scans the full catalog without blocking. (../../raw/github/davila7-claude-code-templates.md)

## Example usage

```bash
# Install a complete development stack in one command
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# Single components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes

# Operational tools
npx claude-code-templates@latest --analytics       # live session dashboard
npx claude-code-templates@latest --health-check     # installation diagnostics
npx claude-code-templates@latest --chats --tunnel   # remote conversation monitor
```
(../../raw/github/davila7-claude-code-templates.md)

## Maintenance status

29,431 GitHub stars, 3,222 forks, MIT licensed, default branch `main`, latest tagged release v1.28.3 (2025-11-15), most recent push 2026-07-14. Sponsored/backed by Bright Data, Vercel OSS Program, Neon Open Source Program, and Anthropic's Claude for Open Source program — signals of active, well-resourced maintenance. Publishing follows a documented release checklist: regenerate the component catalog, run tests, bump `package.json` above the current npm registry version, publish with a granular npm token (2FA-bypass enabled, removed from local config immediately after use), then tag `vX.Y.Z`; the dashboard deploys automatically via GitHub Actions on pushes to `main`. (../../raw/github/davila7-claude-code-templates.md)

## Ecosystem

Sits in the Claude Code extension-discovery layer alongside catalog/marketplace sites like [[claudemarketplaces.com]] and directories like [[skills.sh]] — those index third-party skills and marketplaces broadly, while claude-code-templates both aggregates upstream sources (including [[anthropics-skills]] and [[obra-superpowers]], both explicitly credited in its attribution list) and ships its own installer CLI plus operational tooling (analytics, health-check, plugin dashboard) not offered by pure directories. Its Discord bot and Cloudflare-Worker-driven release-monitoring pipeline are unusual for a component catalog — most peers in this space are static or search-only indexes.
