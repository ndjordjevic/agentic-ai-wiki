---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://www.greptile.com/
tags:
  - ai-code-review
  - pr-review
  - github-integration
  - gitlab-integration
  - graph-based-context
  - self-hosting
  - mcp-server
  - feedback-learning
related:
  - qa.tech
  - agent-field-pr-af
  - traycer.ai
  - factory.ai
  - the-new-sdlc-with-vibe-coding
  - sentry.io
  - coderabbit.ai
product: greptile
detail_level: standard
created: 2026-06-24
updated: 2026-08-25
---

Greptile is a cloud-native AI code review agent that automatically reviews every pull request using whole-repository context rather than just the diff. It integrates with GitHub and GitLab as an app/webhook, builds a graph of the entire codebase (every function, class, import, and dependency), and posts high-signal findings — logic errors, security issues, architectural inconsistencies — within approximately three minutes of a PR opening. Greptile is designed as the "central validation layer" for teams using AI coding agents (Claude Code, Codex, Cursor, Devin), complementing code generation by providing independent review. It is not an open-source project; cloud deployment requires a subscription, and self-hosting requires a commercial license from Greptile.

_All claims below are sourced from ../../raw/web/greptile.com.md unless otherwise noted._

## What it does

Greptile connects to a repository via the GitHub App (or GitLab token + webhook), indexes the codebase into a repository graph, then triggers on every pull request. On each PR it analyzes the diff in the context of the full graph, posts a review summary with confidence indicators, inline comments with suggested fixes, and a "Fix All" button that dispatches every issue directly to a connected coding agent. After 2–3 weeks of thumbs-up/thumbs-down feedback and reply training from the team, Greptile's learning system suppresses suggestions the team consistently ignores and reinforces the patterns they prefer — reducing noise over time without manual rule editing.

## Key features

- **Graph-based codebase context** — indexes every function, class, import, and dependency into a traversable graph; during review, queries the graph to surface impacted callers, detect cross-file inconsistencies, and reference similar patterns already in the codebase.
- **High-signal findings** — defaults to logic, security, performance, and architectural issues; style and syntax comments are configurable and can be disabled or tuned via `strictness` in `greptile.json`.
- **Learning system** — adapts via PR reactions (👍/👎), developer replies, and commit-based analysis of which comments were actually addressed; after a few weeks reduces noise to team-specific preferences without manual upkeep.
- **Fix with your Agent** — every comment includes a "Fix with your Agent" button (and a "Fix All" button on the review summary) that sends the issue with file paths, line numbers, and suggested code directly to Claude Code, OpenAI Codex, Conductor, Cursor, or Devin.
- **MCP server** — a Greptile MCP server exposes PR comments, feedback patterns, coding standards, and review status to any MCP-compatible IDE or agent (Cursor, Windsurf, Claude Desktop, Codex CLI) without switching to GitHub or the Greptile dashboard.
- **Enterprise deployment** — SOC2 Type II cloud, self-hosted Docker Compose (single VM, up to ~100 developers), self-hosted Kubernetes (Helm charts, 100+ developers), and air-gapped deployments with customer-managed LLMs.
- **Configurable via `greptile.json`** — repo-level config file controls strictness, comment types, trigger behavior (draft PRs, update-only), ignore patterns, and LLM model selection; overrides dashboard settings; read from the PR source branch.

## Architecture and concepts

Greptile's core architecture is built around three layers:

**Repository graph** — at onboarding (or on webhook push), Greptile parses every file to extract directories, files, functions, classes, and variables, then maps all relationships (function calls, imports, dependencies, variable usage) into a stored graph. This graph is pre-built and queried in real time during each PR review, enabling sub-3-minute review latency regardless of repo size.

**PR review flow** — on a new PR webhook event, Greptile: (1) fetches the diff; (2) queries the graph for dependencies and callers of changed symbols; (3) checks for pattern consistency against similar constructs in the codebase; (4) applies any `greptile.json` and Dashboard configuration; (5) posts a structured review with summary, confidence scores, diagrams, and inline comments with suggested fixes.

**Learning and memory system** — a continuous feedback loop reads team PR comments (for automatic pattern extraction), developer replies to Greptile comments (positive/context-setting/dismissive), and thumbs-up/thumbs-down reactions; tracks which comments were addressed in the final commit vs. the first commit; adjusts comment-type weights and suppression thresholds accordingly. Critical issue types (security, logic errors) are never suppressed regardless of learning signals.

**Self-hosted deployment** requires three LLM model types: a smart/reasoning model (Claude 3.5 Sonnet+, GPT-4o) for code review and agent tasks; a fast model (GPT-4o-mini, Claude Haiku) for summarization; and an embeddings model (text-embedding-3-small, AWS Titan V2) for code indexing. Supported LLM providers: OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, GCP Vertex AI. External dependencies include PostgreSQL with pgvector and Redis; these can be customer-managed or provisioned via the Terraform template (AWS only).

## When to use

Greptile is best suited for teams that: (a) ship frequent PRs and want automated, codebase-aware review that scales without reviewer fatigue; (b) are integrating AI coding agents (Codex, Claude Code, Cursor, Devin) and need an independent review layer that doesn't generate code itself; (c) require enterprise compliance (SOC2 Type II, SSO/SAML, audit logs, data sovereignty) or air-gapped deployments with custom LLM providers.

It is not a linter replacement, not a static analysis tool, and not a code generation tool — Greptile explicitly positions itself as review-only ("the reviewer should not be the author").

## Ecosystem

Greptile integrates directly with **GitHub** (Cloud, Enterprise Server) and **GitLab** (Cloud, Self-Managed, with Perforce also supported for self-hosted). Its "Fix with your Agent" feature integrates with **Claude Code**, **OpenAI Codex**, **Conductor**, **Cursor**, and **Devin**. The MCP server works with **Cursor**, **Windsurf**, **Claude Desktop**, and **Codex CLI**. The REST API supports integration with Slack, Sentry, and custom GitHub workflows. For competitors and comparisons, see the Greptile vs Bugbot and Greptile vs CodeRabbit pages on the site.

Related sources in this wiki with PR review and code quality overlap: [[qa.tech]] (AI-driven E2E test generation with PR integration), [[agent-field-pr-af]] (multi-agent adversarial PR review with AST verification), [[traycer.ai]] (spec-driven AI coding planning and verification), [[factory.ai]] (coding agents with Droids and mission-based workflows).
