# Chachamaru127/claude-code-harness

## Metadata
- Stars: 2951
- Primary language: Shell
- Default branch: main
- Latest release: v4.16.4 (2026-06-28)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-08
- Final URL: https://github.com/Chachamaru127/claude-code-harness

## Description
Claude Code Dedicated Development Harness - Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle

## README
# Claude Code Harness

**Plan. Work. Review. Ship.**
*A disciplined delivery loop for Claude Code, with bounded paths for Codex and OpenCode.*

Claude Code is powerful, but raw agent work drifts: plans live in chat, tests
become optional, review happens too late, and release evidence gets rebuilt by
memory. Harness turns that into one repeatable operating path.

After install, the default changes from "ask the agent to code" to:

1. write the spec and plan,
2. implement only the approved slice,
3. verify the result,
4. review independently,
5. package evidence for PR or release.

## Quickstart

| Path | Start |
|---|---|
| New user | Tool-first onboarding (`docs/onboarding/index.md`) |
| Existing user | Migration check (`docs/onboarding/migration.md`) |
| Claude Code fast path | Install in 30 seconds (below) |
| Non-engineer / jargon help | Plain-language glossary (`docs/onboarding/glossary.md`) |
| Trigger proof | Skill trigger gate (`docs/onboarding/skill-trigger-acceptance.md`) |

## Install in 30 Seconds

```bash
claude
/plugin marketplace add Chachamaru127/claude-code-harness
/plugin install claude-code-harness@claude-code-harness-marketplace
/harness-setup
```

Next command: run `/harness-plan` with one small request.

```bash
/harness-plan Improve the README onboarding flow
```

## First 15 Minutes

1. Install through your tool route.
2. Run `/harness-setup` or the equivalent setup script.
3. Run `/harness-plan` with a small request; Harness writes the `spec.md` and
   `Plans.md` drafts for you to check. Small typo, docs, and status updates stay
   lightweight.
4. Approve the generated contract or reply with the correction you want.
5. Run the smallest approved task, for example `/harness-work 1.1.1`.
6. Run `/harness-review` and keep the verification output.

Your job is not to hand-write the plan. It is to approve or correct the
generated contract before execution continues.

## How It Works

Harness adds a source-of-truth loop around agent work.
The 5 verb skills keep that surface small: plan, work, review, sync, release.

1. You describe the outcome in normal language.
2. `/harness-plan` drafts or updates `spec.md` and `Plans.md` with scope,
   acceptance criteria, unknowns, and stop conditions.
3. Non-trivial planning records `team_validation_mode` and validates the plan
   through team/sub-agent or manual-pass perspectives for spec/Plans alignment,
   memory reuse, product fit, security fit, and works-in-practice.
4. Harness treats those files as the source of truth. Data the agent has not
   seen stays `unknown` instead of being silently invented.
5. `/harness-work` implements the approved slice with TDD and verification.
6. `/harness-review` separates review from implementation.
7. `/harness-release` packages only verified evidence.

## Commands

| Command | What happens inside |
|---------|---------------------|
| `/harness-setup` | Installs project guidance, command surfaces, hooks, and checks so the workflow starts from one known baseline. |
| `/harness-plan` | Turns intent into `spec.md` and `Plans.md`, including scope, acceptance criteria, dependencies, unknowns, stop conditions, and non-trivial planning validation. |
| `/harness-work` | Executes one approved task or range, adds tests when required, runs verification, and keeps work inside the plan. |
| `/harness-work all` | Runs the approved plan through implementation and review paths; use after the plan is clear and the repo baseline is known. |
| `/harness-review` | Reviews the result separately from implementation and treats major findings as blockers. |
| `/harness-release` | Checks release readiness, CHANGELOG/tag boundaries, and evidence packaging after implementation and review are complete. |
| `bin/harness doctor --migration-report` | Inventories old plugin caches, Codex skills, OpenCode files, symlinks, and memory state without deleting data. |

## Basic Workflow

| Stage | Output | Gate |
|-------|--------|------|
| Investigate | Evidence and unknowns | Do not promote unobserved data into claims. |
| Plan | `spec.md` + `Plans.md` | User approves or corrects the generated contract. |
| Work | Code and tests | TDD required when the task says so. |
| Review | Independent verdict | Major findings block completion. |
| PR | Evidence pack | PR ready is not release ready. |
| Release | Tag/release artifacts | Release preflight must pass on the release path. |

## Install By Tool

| Tool | Tier | Route |
|---|---|---|
| Claude Code | `supported` | Claude plugin marketplace, then `/harness-setup`. |
| Codex CLI | `internal-compatible` | `scripts/setup-codex.sh --user`; direct plugin smoke is tracked separately. |
| Codex app | `candidate` | Candidate smoke only; do not reuse Codex CLI proof. |
| OpenCode | `internal-compatible` | `scripts/setup-opencode.sh`; runtime parity is not claimed. |
| Cursor | `internal-compatible` | `scripts/setup-cursor.sh` real-directory local install; top support tier still gated on workflow smoke. |
| GitHub Copilot CLI | `candidate` | Manual profile research only. |
| Antigravity CLI | `future/unsupported` | No end-user install route in this phase. |

## Requirements

- Claude Code v2.1+ for the supported Claude path.
- A project repository with write access for local setup.
- No Node.js is required for the Go-native guardrail engine.
- Optional [harness-mem](https://github.com/Chachamaru127/harness-mem) for
  cross-session memory when configured and healthy.

## Advanced

| Capability | What it adds | Boundary |
|------------|--------------|----------|
| Breezing | Planner/Critic/Worker style team execution for larger task lists. | Still gated by plan quality and review. |
| Codex companion review | Schema-backed Codex second opinion through `scripts/codex-companion.sh`. | Raw `codex exec` is not the Harness companion path. |
| OpenCode bootstrap | Mirrors Harness guidance into OpenCode-compatible surfaces. | Real runtime parity is not claimed. |
| harness-mem | Project-scoped memory and recall across sessions. | Optional companion; purge remains explicit. |

## Docs

### docs/ARCHITECTURE.md (excerpt)

Claude harness uses a modular Plan → Work → Review cycle supported by Skills, Rules, and Hooks.

**3-layer architecture:**
- **Skill Layer**: `SKILL.md` files — self-contained knowledge units for specific tasks.
- **Workflow Layer**: `*.yaml` files orchestrate skills for development phases.
- **Profile Layer**: defines which workflows map to which commands and allowed skill categories.

**Key components:**
- **Skills**: each skill declares `description` (when to use) and `allowed-tools` for safe autonomous discovery.
- **Rules**: `claude-code-harness.config.schema.json` enforces safety (`dry-run`, protected paths).
- **Hooks**: SessionStart, PostToolUse, Stop — automatic scripts at key process points.
- **Parallel review**: `/harness-review` can launch multiple `code-reviewer` sub-agents in parallel.

### docs/CLAUDE_CODE_COMPATIBILITY.md

- Supported baseline: Claude Code v2.1+, Node.js 18+, plugin version 3.10.2
- Latest verified snapshot: Claude Code 2.1.74, Node.js v24.10.0
- Covers: `/harness-setup`, `/harness-plan`, `/harness-work`, `/harness-review`, `/harness-release`
- Go-native guardrail engine in `go/`; hook shims in `hooks/`; CI packaging checks
- Windows: native `bin/harness-windows-amd64.exe` via shim; skills shipped as real directories (not symlinks)
- Extra validation needed: Breezing/agent teams, Codex CLI, Cursor 2-agent, video/slide gen, memory/daemon integrations

### docs/onboarding/index.md (excerpt)

Tool-first onboarding with explicit support tiers:
- Claude Code: `supported`
- Codex CLI, OpenCode, Cursor: `internal-compatible`
- Codex app, GitHub Copilot CLI: `candidate`
- Antigravity CLI: `future/unsupported`

Rule: `not_observed != absent` — missing local proof means "not proven here", not "impossible" or "supported".

### docs/tool-capability-matrix.md (excerpt)

Phase 73 host capability matrix — contract document, not marketing.
False parity is forbidden: same capability name ≠ same enforcement strength.
Claude Code has PreToolUse/PostToolUse hooks; Codex uses contract injection + post quality gate + merge gate.
Cursor is `internal-compatible` with observed Desktop skill loading but no public supported claim.

### CLAUDE.md (excerpt — development guide)

Self-referential project: uses the harness to improve the harness.

**Repository structure:**
`.claude-plugin/` plugin manifest / `.claude/` runtime state / `.cursor/` Cursor adapter / `agents/` sub-agents / `skills/` primary skills / `skills-codex/` Codex variants / `hooks/` / `scripts/` / `go/` Harness v4 Go native engine / `docs/` / `templates/` / `tests/`

**Top skill areas:**
- harness-work, breezing, harness-review, harness-plan, harness-sync, memory, cognitive-load surfaces

**Permission boundaries (multi-layer defense R01-R13):**
- deny: `.claude-plugin/settings*`, `.claude/settings*`, eslint/tsconfig, `.github/workflows/*`
- ask/deny: `git push --force`, `git reset --hard`, protected branch push
- deny: `mcp__codex__*` (direct Codex MCP use)

**SSOT:** `.claude/memory/decisions.md` (Why), `.claude/memory/patterns.md` (How)

## Top-level structure

```
claude-code-harness/
├── .claude-plugin/         # Plugin manifest, hooks.json, marketplace metadata
├── .claude/                # Claude runtime: rules, memory, hooks config
├── .cursor-plugin/         # Cursor adapter manifest
├── .cursor/                # Cursor commands, rules, skills
├── .codex-plugin/          # Codex plugin packaging
├── agents/                 # Sub-agent definitions (Markdown)
├── bin/                    # Go-native harness binaries (darwin/linux/windows) + harness shim
├── docs/                   # Extensive docs: onboarding, architecture, compatibility, policies
│   ├── onboarding/         # Tool-first install, migration, glossary, trigger acceptance
│   ├── architecture/       # Architecture subdocs
│   ├── evidence/           # Verification contracts (e.g. work-all)
│   └── tool-capability-matrix.md
├── go/                     # Harness v4 Go-native guardrail engine (cmd/, internal/, pkg/)
├── hooks/                  # Hook shims (SessionStart, PreToolUse, PostToolUse, Stop)
├── monitors/               # Monitoring utilities
├── opencode/               # OpenCode-compatible mirror (skills, AGENTS.md)
├── scripts/                # Setup scripts (codex, opencode, cursor), CI, companion review
├── skills/                 # 30+ SKILL.md workflow skills
│   ├── harness-plan/       # Planning: spec.md + Plans.md contract
│   ├── harness-work/       # Implementation from approved plan slice
│   ├── harness-review/     # Independent review (separate from implementation)
│   ├── harness-sync/       # Plans.md ↔ git ↔ implementation alignment
│   ├── harness-release/    # Release readiness and evidence packaging
│   ├── harness-setup/      # Bootstrap install
│   ├── breezing/           # Agent-teams parallel full-run
│   └── ...                 # cursor-*, memory, session-*, ci, deploy, etc.
├── skills-codex/           # Codex-specific skill variants
├── templates/              # Config and output templates
├── tests/                  # Plugin validation, consistency, e2e scripts
├── workflows/              # Workflow YAML orchestration
├── spec.md                 # Product contract (source of truth)
├── Plans.md                # Task ledger (source of truth)
├── CLAUDE.md               # Agent development guide for this repo
├── IMPLEMENTATION_GUIDE.md # Implementation reference
├── harness.toml            # Harness config
└── CHANGELOG.md            # User-facing version history
```

**Annotated notes:**
- **5 verb skills** (`harness-plan`, `harness-work`, `harness-review`, `harness-sync`, `harness-release`) are the primary user-facing workflow surface; dozens of supporting skills exist under `skills/`.
- **Go-native core** (`go/`, `bin/harness*`) — guardrail engine; no Node.js required for core safety.
- **Multi-harness adapters**: separate plugin trees for Claude (`.claude-plugin/`), Codex (`.codex-plugin/`, `codex/`), Cursor (`.cursor-plugin/`, `.cursor/`), OpenCode (`opencode/`).
- **Self-referential**: repo uses its own harness loop to develop itself (`spec.md` + `Plans.md` as SSOT).
- **Optional memory**: [harness-mem](https://github.com/Chachamaru127/harness-mem) companion for cross-session recall.
- **Support boundary**: does not inherit claims from Superpowers, Hermes Agent, or other projects; hosts move up only with Harness-specific bootstrap/trigger/runtime/release evidence.
