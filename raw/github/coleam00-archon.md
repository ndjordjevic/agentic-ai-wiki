# coleam00/Archon

## Metadata
- Stars: 21,422
- Primary language: TypeScript
- Default branch: dev
- Latest release: v0.3.11 (Archon CLI v0.3.11, 2026-05-13)
- License: MIT
- Homepage: https://archon.diy
- Fetched: 2026-05-14
- Final URL: https://github.com/coleam00/Archon

## Description
The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

## README
<p align="center">
  <img src="assets/logo.png" alt="Archon" width="160" />
</p>

<h1 align="center">Archon</h1>

<p align="center">
  The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.
</p>

---

Archon is a workflow engine for AI coding agents. Define your development processes as YAML workflows - planning, implementation, validation, code review, PR creation - and run them reliably across all your projects.

Like what Dockerfiles did for infrastructure and GitHub Actions did for CI/CD - Archon does for AI coding workflows. Think n8n, but for software development.

### Why Archon?

When you ask an AI agent to "fix this bug", what happens depends on the model's mood. It might skip planning. It might forget to run tests. It might write a PR description that ignores your template. Every run is different.

Archon fixes this. Encode your development process as a workflow. The workflow defines the phases, validation gates, and artifacts. The AI fills in the intelligence at each step, but the structure is deterministic and owned by you.

- **Repeatable** - Same workflow, same sequence, every time. Plan, implement, validate, review, PR.
- **Isolated** - Every workflow run gets its own git worktree. Run 5 fixes in parallel with no conflicts.
- **Fire and forget** - Kick off a workflow, go do other work. Come back to a finished PR with review comments.
- **Composable** - Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation, review). The AI only runs where it adds value.
- **Portable** - Define workflows once in `.archon/workflows/`, commit them to your repo. They work the same from CLI, Web UI, Slack, Telegram, or GitHub.

### What It Looks Like

Here's an example of an Archon workflow that plans, implements in a loop until tests pass, gets your approval, then creates the PR:

```yaml
# .archon/workflows/build-feature.yaml
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"

  - id: implement
    depends_on: [plan]
    loop:
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
      fresh_context: true

  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"

  - id: review
    depends_on: [run-tests]
    prompt: "Review all changes against the plan. Fix any issues."

  - id: approve
    depends_on: [review]
    loop:
      prompt: "Present the changes for review. Address any feedback."
      until: APPROVED
      interactive: true

  - id: create-pr
    depends_on: [approve]
    prompt: "Push changes and create a pull request"
```

### Getting Started

**Full Setup (5 minutes):**
```bash
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```
Then say: "Set up Archon"

**Quick Install (30 seconds):**
```bash
# macOS / Linux
curl -fsSL https://archon.diy/install | bash

# Homebrew
brew install coleam00/archon/archon
```

### Built-in Workflows

| Workflow | What it does |
|----------|-------------|
| `archon-assist` | General Q&A, debugging, exploration |
| `archon-fix-github-issue` | Classify issue → investigate/plan → implement → validate → PR → smart review → self-fix |
| `archon-idea-to-pr` | Feature idea → plan → implement → validate → PR → 5 parallel reviews → self-fix |
| `archon-plan-to-pr` | Execute existing plan → implement → validate → PR → review → self-fix |
| `archon-issue-review-full` | Comprehensive fix + full multi-agent review pipeline |
| `archon-smart-pr-review` | Classify PR complexity → run targeted review agents → synthesize findings |
| `archon-comprehensive-pr-review` | Multi-agent PR review (5 parallel reviewers) with automatic fixes |
| `archon-create-issue` | Classify problem → gather context → investigate → create GitHub issue |
| `archon-validate-pr` | Thorough PR validation testing both main and feature branches |
| `archon-resolve-conflicts` | Detect merge conflicts → analyze both sides → resolve → validate → commit |
| `archon-feature-development` | Implement feature from plan → validate → create PR |
| `archon-architect` | Architectural sweep, complexity reduction, codebase health improvement |
| `archon-refactor-safely` | Safe refactoring with type-check hooks and behavior verification |
| `archon-ralph-dag` | PRD implementation loop - iterate through stories until done |
| `archon-remotion-generate` | Generate or modify Remotion video compositions with AI |
| `archon-test-loop-dag` | Loop node test workflow - iterative counter until completion |
| `archon-piv-loop` | Guided Plan-Implement-Validate loop with human review between iterations |

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Platform Adapters (Web UI, CLI, Telegram, Slack,       │
│                    Discord, GitHub)                     │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                     Orchestrator                        │
│          (Message Routing & Context Management)         │
└─────────────┬───────────────────────────┬───────────────┘
              │                           │
      ┌───────┴────────┐          ┌───────┴────────┐
      │                │          │                │
      ▼                ▼          ▼                ▼
┌───────────┐  ┌────────────┐  ┌──────────────────────────┐
│  Command  │  │  Workflow  │  │    AI Assistant Clients  │
│  Handler  │  │  Executor  │  │   (Claude / Codex / Pi)  │
│  (Slash)  │  │  (YAML)    │  │                          │
└───────────┘  └────────────┘  └──────────────────────────┘
      │              │                      │
      └──────────────┴──────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│              SQLite / PostgreSQL (7 Tables)             │
│   Codebases • Conversations • Sessions • Workflow Runs  │
│    Isolation Environments • Messages • Workflow Events  │
└─────────────────────────────────────────────────────────┘
```

### Web UI

Archon includes a web dashboard. Key pages:
- **Chat** - Conversation interface with real-time streaming and tool call visualization
- **Dashboard** - Mission Control for monitoring running workflows, with filterable history
- **Workflow Builder** - Visual drag-and-drop editor for creating DAG workflows with loop nodes
- **Workflow Execution** - Step-by-step progress view for any running or completed workflow

### Platform Adapters

| Platform | Setup time |
|----------|-----------|
| Telegram | 5 min |
| Slack | 15 min |
| GitHub Webhooks | 15 min |
| Discord | 5 min |

### Documentation

Full documentation at **[archon.diy](https://archon.diy)**. Topics: Getting Started, The Book of Archon, CLI Reference, Authoring Workflows, Authoring Commands, Configuration, AI Assistants, Deployment, Architecture, Troubleshooting.

## CLAUDE.md (agent instructions)

**Remote Agentic Coding Platform**: Control AI coding assistants (Claude Code SDK, Codex SDK) remotely from Slack, Telegram, and GitHub. Built with Bun + TypeScript + SQLite/PostgreSQL, single-developer tool for AI-assisted development practitioners.

Core principles: Platform Agnostic (unified conversation interface), Type Safety (strict TypeScript, Zod schemas), Git as First-Class Citizen (worktrees for parallelism, never assume `main`), KISS, YAGNI, DRY + Rule of Three, SRP + ISP, Fail Fast.

Git workflow: `main` is release branch; `dev` is working branch; `/release` skill for changelog + version bump + PR. Releases follow semver.

Key packages: `adapters/` (Slack, Telegram, GitHub, Discord, Web), `cli/`, `core/`, `git/`, `isolation/`, `providers/` (Claude/Codex/Pi), `server/`, `web/`, `workflows/`.

## Top-level structure

```
.archon/              — Archon runtime config for this repo's own development
  commands/           — Reusable slash-command markdown files
  workflows/          — Workflow YAML files (defaults/, experimental/, maintainer/, test-workflows/)
  config.yaml         — Archon config
.claude/              — Claude Code agent context files
.github/              — GitHub workflows (CI, test.yml), PR template
assets/               — Logo and static assets
auth-service/         — Authentication service
deploy/               — Deployment configurations (Caddyfile, scripts)
homebrew/             — Homebrew tap formula
migrations/           — Database schema migrations
packages/             — Bun monorepo packages:
  adapters/           — Platform adapter implementations
  cli/                — Archon CLI binary
  core/               — Core orchestrator + message routing
  docs-web/           — Documentation website (archon.diy)
  git/                — Git operations library (worktrees, branches)
  isolation/          — Worktree isolation environments
  paths/              — Path utilities
  providers/          — AI provider clients (Claude Code SDK, Codex SDK, Pi)
  server/             — HTTP/API server (Hono + Zod OpenAPI)
  web/                — Web UI frontend (React)
  workflows/          — Workflow engine: DAG executor, loop nodes, YAML loader
scripts/              — Build, release, and utility scripts
CLAUDE.md             — Agent coding instructions (CRITICAL)
CHANGELOG.md          — Keep a Changelog format
Dockerfile            — Multi-stage Docker build
docker-compose.yml    — Compose setup for local dev and production
```
