---
type: source
source_url: https://factory.ai/
tags:
  - enterprise-ai-agents
  - agent-native-development
  - droid-cli
  - coding-agents
  - missions
  - skills
  - hooks
  - multi-agent-orchestration
related:
  - traycer.ai
  - crewai.com
  - strandsagents.com
  - langchain.com
  - bmad-code-org-bmad-method
  - openai-codex-plugin-cc
product: factory
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Factory is the enterprise platform for agent-native software development, centered on an AI agent called **Droid** that automates coding, testing, review, and deployment end-to-end. Available as a CLI (`droid`), desktop app, and web app, Factory bundles five interoperating capability layers — Missions (multi-agent orchestration), Skills (reusable procedures), Hooks (lifecycle automation), Custom Droids (specialized subagents), and MCP (tool connectivity) — into a production-ready system for teams that need to move fast without bypassing compliance, security, or code ownership. Factory raised a $150M Series C at a $1.5B valuation and claims 7× faster feature delivery, 96.1% migration time reduction, and 95.8% on-call resolution time savings for enterprise customers.

_All claims below are sourced from ../../raw/web/factory.ai.md unless otherwise noted._

## What it does

Factory's core product is Droid, a terminal-based AI coding agent that takes natural-language tasks and translates them into full code changes — reading files, editing code, running commands, creating commits, and opening pull requests. Droid integrates natively with GitHub, GitLab, Jira, Linear, Notion, Sentry, Slack, PagerDuty, and 100+ other tools. It operates with complete visibility: every change goes through a diff review step before being applied, preserving human oversight.

Installation is one curl command: `curl -fsSL https://app.factory.ai/cli | sh`. The CLI runs in an interactive full-screen TUI with spec mode, bash passthrough, and a multi-session overlay called Mission Control.

## Key features

- **Factory Missions** — Structured multi-agent orchestration for large features. Droid collaborates upfront to build a plan (features, milestones, ordering, skills), then an orchestrator coordinates specialized worker droids and validator droids in parallel. Workers tackle features; validators verify each milestone. Run interactively with `/missions` or headlessly via `droid exec --mission -f mission.md`.
- **Skills** — Reusable `SKILL.md` files that package procedures, domain knowledge, and tool workflows. Skills live at repo level (`.factory/skills/<name>/SKILL.md`) or user level (`~/.factory/skills/`). The Droid auto-invokes matching skills or you can call them with `/skill-name`. Skills are composable, version-controlled, and shareable via git or plugin marketplaces.
- **Hooks** — Shell commands registered to agent lifecycle events (`PreToolUse`, `PostToolUse`, `Notification`, `Stop`, `SessionStart`, etc.). Used for automatic code formatting, secret detection, compliance logging, file protection, and notification routing. Encode "always-on" rules as hooks rather than prompt instructions for deterministic enforcement.
- **Custom Droids (Subagents)** — Define specialized subagents with their own system prompts, tool access, and model choices. Worker missions delegate to custom droids. Managed via `/droids`.
- **MCP (Model Context Protocol)** — Connect Droid to external tools and data sources via the standard MCP interface. Managed with `droid mcp add` or `/mcp`.
- **Plugins** — Installable bundles of skills, commands, droids, and hooks distributed through marketplaces. Installed via `droid plugin install` or `/plugins`.
- **Bring Your Own Key (BYOK)** — Use your own API keys for OpenAI, Anthropic, Google Gemini, Groq, Fireworks AI, DeepInfra, Baseten, Ollama, Hugging Face, or OpenRouter.
- **Droid Computers** — Persistent, long-lived compute environments (cloud-managed or bring-your-own machine) for remote Droid execution outside a laptop session.
- **Droid Exec (Headless)** — Non-interactive execution mode for CI/CD pipelines and automation scripts: `droid exec "task description"`.
- **AutoWiki** — `/wiki` command generates a comprehensive project wiki from the codebase, kept up to date in the Factory App and GitHub Wiki with a CI action.
- **Readiness Report** — `/readiness-report` evaluates a repository's autonomy maturity with an Agent Readiness score.
- **Droid Shield** — Automatic secret detection in git commits. Droid Shield Plus adds AI-powered prompt injection and sensitive data scanning (enterprise, powered by Palo Alto Networks Prisma AIRS).

## Architecture and concepts

Factory's capability stack has three interlocking layers:

1. **Agent core (Droid)** — An iterative planning-then-execution loop. Droid switches between Chat mode (interactive dialogue), Spec mode (structured planning before implementation), and Bash mode (direct shell passthrough). Context management is explicit: `/fork` branches sessions, `/compress` compacts context, and AGENTS.md seeds project conventions.

2. **Configuration layer** — Skills, Hooks, Custom Droids, MCP servers, and Mixed Models are configured statically (in `.factory/` or `~/.factory/`) and injected into the Droid runtime per task. This is the "playbook encoding" layer: engineering conventions become reproducible behaviors rather than ephemeral prompts.

3. **Orchestration layer (Missions)** — For large work, Droid transitions from a single-agent loop to a multi-agent orchestration model. An orchestrator decomposes the plan into features and milestones, spawns worker droids per feature, and runs validator droids at each milestone. The cost heuristic is `total runs ≈ #features + 2 * #milestones`. Workers inherit the caller's Skills, Hooks, Custom Droids, MCP integrations, and AGENTS.md.

The **Deferred Context Engine** (recently shipped) keeps skills, plugins, and MCP tool schemas reachable without loading every schema on every turn, reducing input-token overhead at scale.

## Main APIs

- **Droid CLI** — `droid`, `droid exec`, `droid mcp add`, `droid plugin install`. Full reference at `docs.factory.ai/reference/cli-reference.md`.
- **Session API** — Create, update, list, interrupt, and message sessions programmatically (`POST /api-reference/sessions/create-a-session`). Enabled for selected organizations.
- **Computer API** — Create, refresh, restart, and delete persistent compute environments (`/api-reference/computers/`).
- **Organization API** — Manage users, credits limits, and enterprise control settings (`/api-reference/organization/`).
- **Analytics API** — REST API for org-level usage metrics, Factory Standard Credits consumption, tool usage, and productivity analytics.
- **Readiness Reports API** — Programmatic access to agent readiness scores.
- **OpenAPI spec** — `https://api.factory.ai/api/v0/openapi.json`

## When to use

Factory's primary target is **enterprise engineering teams** that need AI automation at scale with compliance requirements. It is especially well-suited to:

- Teams with large, complex codebases where deep codebase understanding (AGENTS.md, organizational knowledge) drives quality
- Organizations running brownfield migrations, framework upgrades, or large refactors (Missions + validator droids catch regressions at each milestone)
- DevOps/platform teams wanting to encode coding standards, security policies, and deployment gates as deterministic hooks rather than fragile prompt instructions
- Companies that cannot use consumer AI coding tools due to data-residency, air-gap, or SOC-2 requirements

For individual developers or small teams without enterprise compliance needs, the free/pro tiers expose the same Droid CLI capabilities; the enterprise tier adds dedicated compute, SSO/SAML, custom integrations, and 24/7 support.

## Ecosystem

Factory connects into the standard enterprise development stack: GitHub/GitLab (PR and code review), Jira/Linear (issue tracking), Notion/Confluence/Google Drive (documentation and context), Slack/Microsoft Teams (notifications), Sentry/PagerDuty (incident response), CircleCI/GitHub Actions (CI/CD), and IDE plugins for VS Code, JetBrains, and Zed.

The open-source org at `github.com/Factory-AI` includes `vfs` ("The filesystem for agents"), reflecting Factory's investment in the underlying agent infrastructure. Factory also publishes research benchmarks (Agent Arena, Legacy-Bench, Terminal Bench, Review Benchmark, Next.js Evals) to quantify AI agent performance across dimensions that matter for enterprise reliability.
