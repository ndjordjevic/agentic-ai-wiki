---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/Chachamaru127/claude-code-harness
tags:
  - claude-code-harness
  - plan-work-review
  - spec-first
  - agent-skills
  - go-native-guardrails
  - multi-harness-adapter
  - tdd-enforcement
  - release-evidence
related:
  - obra-superpowers
  - gsd-build-get-shit-done
  - coleam00-helpline
  - Yeachan-Heo-oh-my-claudecode
  - github-spec-kit
  - shareai-lab-learn-claude-code
  - buildermethods-agent-os
  - 0xnyk-awesome-hermes-agent
  - openai-codex-plugin-cc
  - everyinc-compound-engineering-plugin
  - snarktank-ralph
  - frankbria-ralph-claude-code
  - how-to-master-dynamic-workflows-claude-code-6-patterns-14-steps
product: claude-code-harness
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
updated: 2026-07-08
---

Claude Code Harness (2,951 ★, MIT, v4.16.4, Shell/Go) is a Claude Code plugin that replaces ad-hoc agent coding with a disciplined **Plan → Work → Review → Release** operating loop. Five verb skills (`/harness-plan`, `/harness-work`, `/harness-review`, `/harness-sync`, `/harness-release`) keep the surface small while `spec.md` and `Plans.md` become the source of truth — unobserved data stays `unknown` rather than being invented. A Go-native guardrail engine (`go/`, `bin/harness*`) enforces permission boundaries without requiring Node.js. Claude Code is the only `supported` host; Codex CLI, OpenCode, and Cursor are `internal-compatible`; Copilot CLI and Codex app are `candidate`. The project is self-referential — it uses its own harness to develop itself.

_All claims below are sourced from ../../raw/github/Chachamaru127-claude-code-harness.md unless otherwise noted._

## What it does

Harness wraps Claude Code (and bounded adapter paths for Codex, OpenCode, Cursor) in a repeatable delivery loop. Instead of plans living in chat and review happening too late, the default workflow becomes: (1) `/harness-plan` drafts `spec.md` and `Plans.md` with scope, acceptance criteria, unknowns, and stop conditions; (2) the user approves or corrects the generated contract; (3) `/harness-work` implements only the approved slice with TDD when required; (4) `/harness-review` runs independently from implementation and treats major findings as blockers; (5) `/harness-release` packages verified evidence for PR or release. Non-trivial planning records `team_validation_mode` and validates through sub-agent or manual-pass perspectives (spec/Plans alignment, memory reuse, product fit, security, works-in-practice). The user's job is contract approval, not hand-writing plans.

## Key features

- **Five verb skills** — `harness-plan`, `harness-work`, `harness-review`, `harness-sync`, `harness-release` as the primary workflow surface; 30+ supporting skills under `skills/`.
- **Dual SSOT contracts** — `spec.md` (product contract) and `Plans.md` (task ledger) with precedence `spec.md > sub-spec > Plans.md`.
- **Go-native guardrail engine** — `go/` + prebuilt `bin/harness*` binaries; rules R01–R13 enforce deny/ask on protected paths, force-push, settings self-modification, and direct Codex MCP use.
- **Independent review gate** — `/harness-review` separates review from implementation; parallel `code-reviewer` sub-agents for security, performance, and quality.
- **Multi-harness adapters** — separate plugin trees for Claude (`.claude-plugin/`), Codex (`.codex-plugin/`, `codex/`), Cursor (`.cursor-plugin/`, `.cursor/`), OpenCode (`opencode/`) with explicit support-tier boundaries.
- **Breezing** — Agent-teams parallel full-run (`/breezing`) for larger task lists; still gated by plan quality and review.
- **Codex companion review** — schema-backed second opinion via `scripts/codex-companion.sh review --base` (not raw `codex exec`).
- **Optional harness-mem** — cross-session memory companion (`github.com/Chachamaru127/harness-mem`) when configured.
- **Migration tooling** — `bin/harness doctor --migration-report` inventories stale caches without deleting data.
- **Honest support boundaries** — `not_observed != absent`; does not inherit Superpowers or Hermes Agent claims.

## Architecture

Three-layer design: **Skill Layer** (`skills/*/SKILL.md` — self-contained knowledge units with `description` and `allowed-tools`), **Workflow Layer** (`workflows/*.yaml` — orchestrates skills per phase), **Profile Layer** (maps workflows to commands and allowed skill categories). Hooks (`hooks/`) fire at SessionStart, PreToolUse, PostToolUse, and Stop. Configuration schema (`claude-code-harness.config.schema.json`) enforces safety modes and protected paths.

The repo ships multi-harness packaging: Claude plugin marketplace install, Codex setup via `scripts/setup-codex.sh --user`, OpenCode via `scripts/setup-opencode.sh`, Cursor via `scripts/setup-cursor.sh`. The Phase 73 tool capability matrix (`docs/tool-capability-matrix.md`) documents per-host capability status and explicitly forbids false parity — Claude Code has runtime PreToolUse hooks; Codex uses contract injection + post quality gate + merge gate.

Self-referential development: the project uses its own harness loop to improve itself. SSOT memory lives in `.claude/memory/decisions.md` (Why) and `.claude/memory/patterns.md` (How). Test tampering is absolutely prohibited.

## Installation

**Claude Code (supported path):**

```bash
claude
/plugin marketplace add Chachamaru127/claude-code-harness
/plugin install claude-code-harness@claude-code-harness-marketplace
/harness-setup
```

Then run `/harness-plan` with a small request to verify the trigger path.

**Other hosts (see support tier):**
- Codex CLI: `scripts/setup-codex.sh --user` → `$harness-plan`
- OpenCode: `scripts/setup-opencode.sh` → ask for `harness-plan`
- Cursor: `scripts/setup-cursor.sh` → `/harness-plan` or `/breezing`

Requirements: Claude Code v2.1+, project repo with write access. No Node.js required for the Go-native guardrail engine.

## Example usage

```bash
# Plan a small change
/harness-plan Improve the README onboarding flow

# After approving spec.md + Plans.md, implement one task
/harness-work 1.1.1

# Independent review
/harness-review

# Full plan execution (after baseline is known)
/harness-work all

# Release evidence packaging
/harness-release

# Existing-user migration inventory (no deletion)
bin/harness doctor --migration-report
```

## Maintenance status

2,951 GitHub stars, 282 forks, MIT license, latest release v4.16.4 (2026-06-28), last push 2026-07-07. Actively maintained with extensive docs, CI validation (`tests/validate-plugin.sh`, `scripts/ci/check-consistency.sh`), and changelog discipline. Claude Code compatibility baseline: v2.1+; latest verified snapshot at Claude Code 2.1.74. Support tiers are contract-documented and conservative — hosts only move up when Harness has its own bootstrap, trigger, runtime, and release evidence. Issues and PRs welcome per CONTRIBUTING.md.
