# greptile.com

## Fetch log
- Inbox URL: https://www.greptile.com/
- Final URL: https://www.greptile.com/
- Fetched: 2026-06-24
- Pages: 9
- Mode: standard

## llms.txt — https://www.greptile.com/llms.txt
# Greptile

> Greptile is an AI code review agent for GitHub and GitLab. It reviews pull requests with whole-repo context (not just diffs), produces actionable feedback, and adapts to team preferences through configurable standards and feedback-driven learning.

If evaluating: Key features → Benchmarks → Security → Pricing.  
If implementing: Quickstart → GitHub/GitLab integration → Customization overview → Troubleshooting.

## Start here

- [What is Greptile?](https://www.greptile.com/docs/introduction): Concepts + mental model: repository graph indexing, PR review flow, and feedback-driven learning.
- [5-minute quickstart](https://www.greptile.com/docs/quickstart): Fast setup (GitHub App or GitLab token+webhook) and run your first automated PR review.
- [Key features](https://www.greptile.com/docs/code-review/key-features): Differentiators overview: repository graph context, high-signal findings (not nitpicks), learning via feedback, MCP IDE workflows, and enterprise/self-host deployment.
- [Anatomy of a review](https://www.greptile.com/docs/code-review/first-pr-review): What Greptile posts on PRs and how to interpret each component (summary, confidence, diagrams, inline comments).

## Evaluate

- [Benchmarks](https://www.greptile.com/benchmarks): Methodology + results comparing 5 tools on 50 real bug PRs with default settings; links to reproducible sources and protocol.
- [Examples](https://www.greptile.com/examples): Public PR links showing real Greptile summaries and links to PRs with Greptile comments on popular repos.
- [Customers](https://www.greptile.com/customers): Proof and outcomes: quotes + case studies across company sizes and workflows.
- [Pricing](https://www.greptile.com/pricing): Plans, billing mechanics, 14 day free trial, and FAQs (review bot seats, contracts, chat/API pricing).
- [Brex case study](https://www.greptile.com/customers/brex): Brex Q&A on rollout, adoption, and how Greptile fits a large production workflow.

## How Greptile works

- [Graph-based codebase context](https://www.greptile.com/docs/how-greptile-works/graph-based-codebase-context): How Greptile builds and uses a repository graph to reason beyond the diff.
- [Memory and learning](https://www.greptile.com/docs/how-greptile-works/memory-and-learning): How PR comments/replies and thumbs up/down reactions tune future reviews and reduce noise over time.
- [Reducing nitpicks](https://www.greptile.com/docs/how-greptile-works/nitpicks): How Greptile suppresses low-impact feedback and focuses on what teams actually act on.
- [Custom rules](https://www.greptile.com/docs/how-greptile-works/custom-rules): What you can enforce (architecture/security/performance/standards) and how rules show up in reviews.

## Implement

- [GitHub/GitLab integration](https://www.greptile.com/docs/integrations/github-gitlab-integration): Connect providers and ensure reviews trigger reliably (GitHub App; GitLab token+webhooks; repo enablement).
- [Developer essentials](https://www.greptile.com/docs/code-review/developer-essentials): Day-to-day workflow: trigger with `@greptileai`, ask targeted checks, review drafts, train via thumbs up/down and replies.
- [Tips & recipes](https://www.greptile.com/docs/code-review/tips-recipes): Playbooks: draft PR "local review", RFC/doc review, partial reviews, and high-signal prompt patterns.
- [Troubleshooting](https://www.greptile.com/docs/troubleshooting/common-issues): Fix common failures: config not applying, reviews not running, webhook/filter issues, slow/stuck reviews.
- [Deployment options](https://www.greptile.com/docs/deployment-options): Decision guide for cloud vs self-host, plus Docker Compose vs Kubernetes and the supported setup paths.

## Configure reviews

- [Customization overview](https://www.greptile.com/docs/code-review/customization-overview): Where configuration lives (Dashboard vs repo `greptile.json`) and how precedence/scope works.
- [greptile.json reference](https://www.greptile.com/docs/code-review/greptile-json-reference): Full config schema; must be in repo root and read from PR source branch; overrides dashboard settings (strictness, comment types, filters, triggers, model).
- [Controlling nitpickiness](https://www.greptile.com/docs/code-review/controlling-nitpickiness): Tune strictness, comment types, ignore patterns, and trigger behavior to control signal vs noise.
- [Custom standards & rules](https://www.greptile.com/docs/code-review/custom-standards): Add enforceable standards (rules + style-guide files), scope them, verify they apply, debug misses.
- [Training the learning system](https://www.greptile.com/docs/code-review/training-the-learning-system): How to train Greptile with thumbs up/down reactions and short explanations; what each signal teaches.
- [Pattern repositories](https://www.greptile.com/docs/code-review/pattern-repositories): Reference related repos (shared libs/docs/services) during review via `patternRepositories` for cross-repo context.

## Advanced use cases

- [MCP overview](https://www.greptile.com/docs/mcp-v2/overview): Use Greptile from IDE/agents: fetch PR feedback, apply fixes, manage standards, check status.
- [IDE setup](https://www.greptile.com/docs/mcp-v2/setup): Configure Greptile MCP in Cursor/Claude/VS Code and verify tools are enabled.
- [MCP custom context](https://www.greptile.com/docs/mcp-v2/custom-context): Manage coding standards from your IDE: list, search, and create custom-context patterns via MCP.
- [MCP tools reference](https://www.greptile.com/docs/mcp-v2/tools): Complete API reference for MCP tools, including repository-parameter requirements and request/response shapes.
- [API introduction](https://www.greptile.com/docs/api-reference/introduction): API overview: index repos, query/search in natural language, and integrate with Slack/Sentry/GitHub workflows.
- [Webhooks](https://www.greptile.com/docs/api-reference/webhooks): Verify webhooks and parse `sessionId`, `sources`, `statusEndpoint`; troubleshoot common review failures.

## Security and legal

- [Security](https://www.greptile.com/security): Security controls + hosting model, inference/data handling, logging/storage options, and links to related legal documents.
- [Privacy policy](https://www.greptile.com/security/privacy): Privacy notice for services + site: what Personal Information is processed, how it's shared, and user rights.
- [Subprocessors](https://www.greptile.com/security/subprocessors): Subprocessor list (purpose + location) and how changes are communicated.
- [Terms of service](https://www.greptile.com/terms-of-service): Terms governing use of Greptile services, including data safeguards and processing provisions.

## Content (selected)

- [Best AI code review tools](https://www.greptile.com/content-library/best-ai-code-review-tools): Explains how AI code review works, tradeoffs, and a shortlist of top tools plus setup best practices.
- [Software Needs An Independent Auditor](https://www.greptile.com/blog/auditor): Why AI-generated code needs an independent PR "auditor" and why Greptile is review-only (it doesn't generate code).
- [Greptile v3, an agentic approach to code review](https://www.greptile.com/blog/greptile-v3-agentic-code-review): Deep dive on the v3 agentic workflow and why it drives higher action rate and higher signal-to-noise than v2.
- [AI Code Review: Should the Author Be The Reviewer?](https://www.greptile.com/blog/ai-code-reviews-conflict): When your author is an AI, your reviewer should be independent; explains the incentives and why AI code needs closer review.

## Optional

- [Greptile (homepage)](https://www.greptile.com/): One-page overview + entry point; links to benchmarks, examples, docs, security, and trial.
- [Enterprise](https://www.greptile.com/enterprise): Enterprise evaluation: deployment options, governance/compliance posture, and rollout guidance.
- [Podium case study](https://www.greptile.com/customers/podium): Additional case study focused on high-volume review workflows.
- [Blog](https://www.greptile.com/blog): Blog index (product releases, engineering deep dives, company updates).
- [Content library](https://www.greptile.com/content-library): Index of buyer guides and comparisons (link specific articles when citing).
- [What is AI code review?](https://www.greptile.com/what-is-ai-code-review): Long-form guide explaining AI code review, outputs, and evaluation criteria.
- [Greptile vs Bugbot](https://www.greptile.com/greptile-vs-bugbot): Comparison page: workflow/architecture differences plus benchmark-backed examples.
- [Greptile vs CodeRabbit](https://www.greptile.com/greptile-vs-coderabbit): Comparison page: workflow/architecture differences plus benchmark-backed examples.

## Landing page — https://www.greptile.com/

The Central Validation Layer.

Designed to work seamlessly with every coding agent, Greptile serves as the unified validation agent for all code changes.

## Docs — https://www.greptile.com/docs/introduction

# Overview - What is Greptile?

Greptile is an AI code review agent that automatically reviews every pull request with complete understanding of your codebase.

Unlike traditional linters that check files in isolation, Greptile builds a graph of your entire repository to understand how changes affect the whole system.

## How it works

1. Connects to your repository — Install the GitHub/GitLab app and select repos. Greptile builds a complete graph of your codebase - every function, class, and dependency.
2. Reviews PRs automatically — On every pull request, Greptile analyzes changes with full context. Posts findings in ~3 minutes as PR comments with suggested fixes.
3. Fix with one click — Every review comment includes a Fix with your Agent button that sends the issue — with file paths, line numbers, and suggested code — straight to Claude Code, Codex, Conductor, Cursor, or Devin. A Fix All button in the review summary sends every issue at once.
4. Learns from your team — Your 👍/👎 reactions and replies teach Greptile what matters. After 2-3 weeks, it stops commenting on things you don't care about.

## Why teams choose Greptile

- Catches issues humans miss: Full codebase context means Greptile sees how changes affect distant parts of your system
- Reduces noise over time: Learning system adapts to your team's preferences, suppressing irrelevant suggestions
- No context switching: Fix issues directly in your IDE without jumping between PR and code
- Enterprise ready: SOC2 Type II, self-hosting options, SSO/SAML, audit logs

## Technical details

- Languages: All languages supported
- Platforms: GitHub Cloud & Enterprise Server; GitLab Cloud & Self-Managed
- Deployment: Greptile Cloud (SOC2 Type II), Docker Compose, Kubernetes with Helm, Air-gapped environments

## Measurable impact

- ~3 minutes average review time
- 100K+ bugs caught in production every month
- 9x faster time to merge
- 5 minutes setup to first review

## Key Features — https://www.greptile.com/docs/code-review/key-features

Full codebase context: Greptile builds a graph of your repository (functions, classes, imports, dependencies) and uses it during reviews to reason about ripple effects beyond the diff. Surfaces impacted callers and contracts, detects cross-file inconsistencies and missing validations, references similar patterns already in your codebase.

High-signal findings (not nitpicks): Focus on issues that matter by default; control verbosity with strictness and comment-type filters. Logic, security, performance, architectural issues by default. Style and syntax can be reduced or disabled. Per-repository rules with greptile.json.

Learns your team's standards: Greptile adapts over time using thumbs up/down and short replies. Suppresses suggestions your team routinely ignores, reinforces patterns your team prefers, auto-discovers custom rules from team discussions.

Fix All with AI: Every review comment includes a "Fix with your Agent" button that sends the issue — with file paths, line numbers, and suggested code — directly to your coding agent. A "Fix All" button in the review summary sends every issue at once. Supports Claude Code, OpenAI Codex, Conductor, Cursor, and Devin. Comments resolve when you push the fix.

Auto-resolution from your IDE (MCP): Resolve Greptile comments without leaving your editor. Open files, apply suggested fixes, mark threads resolved. Works with Cursor, Windsurf, Claude Desktop, Codex CLI.

Enterprise-grade deployment: Cloud (SOC2 Type II), self-hosted Docker/Kubernetes, air-gapped. SSO/SAML, audit logging, role-based access. Customer-managed PostgreSQL + pgvector, Redis (self-hosted).

Configuration you control: Use greptile.json for repo-level behavior (strictness, commentTypes, triggerOnUpdates, ignorePatterns).

## Graph-based Codebase Context — https://www.greptile.com/docs/how-greptile-works/graph-based-codebase-context

Greptile builds a complete graph of your codebase to understand how code changes affect other parts of your system, enabling context-aware code reviews that catch issues traditional tools miss.

Codebase Indexing: When you sign up, Greptile builds a complete graph of your repository containing every code element (files, functions, classes, imports, variables). The indexing process: Repository Scanning → Relationship Mapping → Graph Storage.

How Greptile Analyzes Functions: When reviewing a changed function, Greptile queries the graph to understand: (1) Function dependencies — direct calls, imports used, variables accessed; (2) Function usage — everywhere the function is called and impact analysis; (3) Pattern consistency — checks if new code follows existing patterns in the codebase (e.g., parameterized queries vs. string concatenation for SQL).

Real-time Graph Queries: Every time a file is reviewed, Greptile queries the pre-built graph to instantly know import dependencies, function calls, callers, and similar patterns.

## Memory and Learning — https://www.greptile.com/docs/how-greptile-works/memory-and-learning

Greptile's memory system learns from every interaction with your team to deliver increasingly personalized and actionable code review suggestions.

How Greptile Learns: (1) Reading team comments on PRs — observes patterns in team code review discussions; (2) Learning from replies to Greptile — your responses teach it what matters (positive, context-setting, or dismissive); (3) Learning from reactions — thumbs up/down reactions provide instant feedback on suggestion quality.

Learning Nitpickiness Levels: Greptile analyzes which comments get addressed by comparing first and last commits (commit-based learning), then applies adaptive noise filtering. High-nitpick teams get more style feedback; low-nitpick teams see only security and logic issues after suppression thresholds are reached.

## Deployment Options — https://www.greptile.com/docs/deployment-options

Quick Decision: Use Cloud if you want Greptile running in minutes with zero infrastructure management. Use Self-Hosted if you need data sovereignty, air-gapped environments, or custom LLM providers. For self-hosted, use Docker Compose for up to 100 developers (single VM) or Kubernetes for 100+ developers (horizontal scaling, high availability).

Self-Hosted: Docker Compose — Runs all services on a single Linux VM using Docker Compose. Two setup paths: AWS with Terraform (automated VPC/EC2/RDS/Redis provisioning via single `terraform apply`), or Manual Setup (provision VM yourself, clone repo, configure .env, run Docker Compose — works anywhere Docker runs).

VM Sizing Requirements:
- 5-10 devs: 4 cores, 16GB RAM, 100GB storage
- ~50 devs: 8 cores, 32GB RAM, 200GB storage
- 100 devs: 32 cores, 128GB RAM, 500GB storage

Software: Linux (Ubuntu 20.04+, Amazon Linux 2023), Docker 23.x+, Docker Compose v2.5+. Network: inbound port 3007 for webhooks, outbound HTTPS to LLM and SCM providers.

Self-Hosted: Kubernetes — Runs services across a Kubernetes cluster using Helm charts. Provides horizontal scaling, rolling updates, and high availability. Requires Kubernetes 1.21+ (1.25+ recommended), Helm 3.0+. External services: PostgreSQL with pgvector (RDS recommended), Redis (ElastiCache recommended).

External Dependencies for all self-hosted:
- LLM Providers (3 model types): Smart/reasoning (Claude 3.5 Sonnet+, GPT-4o), Fast (GPT-4o-mini, Claude Haiku), Embeddings (text-embedding-3-small, Titan V2)
- Supported LLM providers: OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, GCP Vertex AI
- SCM: GitHub/GitHub Enterprise (App + webhook), GitLab (OAuth app), Perforce (env vars)
- Container Registry: access to Greptile's Docker images (contact Greptile for credentials)

Pricing: Self-hosted requires a license (contact hello@greptile.com).

## MCP Overview — https://www.greptile.com/docs/mcp-v2/overview

The Greptile MCP server lets AI coding assistants (Claude, Cursor, Copilot, Codex) access your code review data directly. Instead of switching to GitHub or the Greptile dashboard, you can fetch comments, apply fixes, and manage coding patterns from your editor.

What You Can Do:
- Fetch PR comments — Get unaddressed Greptile feedback for any PR
- Apply suggested fixes — Comments often include code suggestions you can apply directly
- Search feedback patterns — Find recurring issues across all your reviews
- Manage coding standards — View and create your team's custom context patterns
- Check review status — See which comments are addressed before merging

Covers: Setup (configure MCP in Claude, Cursor, VS Code, or Codex CLI), Auto-Fix Workflow, Agent Skills (automate the full auto-fix loop in Claude Code), Custom Context (manage coding patterns), Reports (generate review analytics), Tools Reference (complete API documentation).
