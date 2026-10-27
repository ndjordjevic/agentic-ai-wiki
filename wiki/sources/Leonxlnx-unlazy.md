---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/Leonxlnx/unlazy
tags:
  - completion-discipline
  - depth-tree
  - acceptance-gates
  - gate-check
  - agent-skills
  - parallel-dispatch
  - stop-hook
  - coding-agent-harness
related:
  - obra-superpowers
  - gsd-build-get-shit-done
  - snarktank-ralph
  - frankbria-ralph-claude-code
  - Chachamaru127-claude-code-harness
  - skills.sh
  - coleam00-skills
  - garrytan-gstack
product: unlazy
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

unlazy is an anti-laziness Agent Skill for coding agents (4,140 stars, MIT, JavaScript, source targeting 2.1.0 with no tagged GitHub release yet). It turns substantial work into a completion-discipline loop: write an acceptance ledger first, run reviewed shell oracles through a zero-dependency Node checker, reverify returned work, and report only what evidence supports. The Depth Tree decomposes multi-part tasks into owned leaves with integration gates; optional scoped orchestration under `.unlazy/<scope>/` adds ownership leases, rolling native-agent dispatch waves, and an optional Claude Code Stop hook that blocks exit while gates or waves are incomplete.

_All claims below are sourced from ../../raw/github/Leonxlnx-unlazy.md unless otherwise noted._

## What it does

unlazy fights premature “done” reports by making incompleteness visible and testable. Before implementing, the agent authors `GATES.md` (solo) or a scoped `PLAN.md` plus per-leaf / per-branch ledgers (orchestrated). Runnable gates declare indented `CHECK:` and `EXPECT:` lines; the checker (`scripts/gate-check.mjs`) counts a gate met only when the process exits 0, the expectation matches combined output, and automatic evidence carries a versioned SHA-256 definition digest of the parsed oracle. Manual gates keep ordinary human evidence. Abandonment (`ABANDON:`) is terminal handoff—never success—and surfaces as `HANDOFF REQUIRED`. Triggers include `/unlazy`, `$unlazy`, `tree N`, “gates”, and natural-language cues from the skill description.

## Installation

Install via the skills CLI for supported agents:

```text
npx skills add Leonxlnx/unlazy
```

Use `-g` for a user-level install or `--all` for every detected agent. Manual clone targets include `~/.claude/skills/unlazy` (Claude Code) and `~/.codex/skills/unlazy` (Codex). Invoke as `/unlazy` where slash skills exist, `$unlazy` in Codex, or by description trigger. Core is `SKILL.md`; the checker and optional hook need Node 16+ and ship with no third-party runtime packages. Pin an exact commit when you need an immutable install—the README states current source targets `2.1.0` without a tagged release.

## Key features

- **Gate contract** — Markdown ledgers with runnable `CHECK:`/`EXPECT:`/`CWD:` attributes, optional `OWNS:` for parallel leaves, and fail-closed parsing (zero gates, duplicate ids, incomplete runnable gates, blank abandonments rejected).
- **`gate-check.mjs` modes** — `--status` (always non-executing), normal dry print for unapproved oracles, `--approve`, `--reverify`, scoped aggregate reduction, opt-in `--jobs 1..64` for independent checks with ledger-order reporting.
- **`gate-lint.mjs`** — Advisory, non-executing audit of weak ledger patterns; `--strict` fails on warnings.
- **Depth Tree** — Split at real domain/component/verification boundaries; each leaf is one coherent deliverable with ownership, dependencies, and gates; branches carry integration gates; effort is controlled by gates and four work passes, not arithmetic depth claims.
- **Scoped orchestration** — `.unlazy/<scope>/` holds `PLAN.md`, ledgers, `dispatch.json`, and status logs; leaf states `WAITING`/`READY`/`IN-FLIGHT`/`VERIFIED`/`ABANDONED`; ownership leases via `--claim` / `--release`.
- **Native dispatch waves** — For each independent READY set, open a wave, launch every host agent with a recorded handle, seal before waiting; auditable `abandon --reason` on irrecoverable partial launch.
- **Optional Claude Code Stop hook** — `install-hooks.mjs` installs a Stop hook that returns `decision: "block"` while unmet gates or incomplete waves remain; six no-progress blocks release the wedge; `--uninstall` removes it.
- **Security boundary** — Approvals under `~/.unlazy/approved` (or `UNLAZY_APPROVAL_DIR`) outside the repo; bind ledger/gate/oracle/shell/PATH/platform; approval is consent, not a sandbox; scopes and leases coordinate cooperating processes only.

## Architecture

The skill is filesystem-first: templates (`gates-leaf.md`, `gates-node.md`, `PLAN.md`), reference docs (`references/method.md`, `gates.md`, `orchestration.md`, `dispatch.md`, `parallel.md`, `token-economy.md`), and Node scripts under `scripts/` plus `scripts/lib/` (gates parser, dispatch, check-supervisor, regex workers, process-tree). Verification has four layers: leaf self-check, parent `--reverify`, branch integration, and the optional Stop hook as a structural backstop that does not execute checks. Evidence binds definition digests separately from runtime approval identity; `--status` and Stop detect definition drift without resolving a shell. Rolling dispatch starts newly ready leaves when a verified leaf unblocks them; check execution stays sequential by default. Codex metadata lives in `agents/openai.yaml` with `allow_implicit_invocation: true`. Research notes in `research/validation-protocol.md` treat early “effort multiplies with depth” arithmetic as design history, not reproducible benchmarks.

## Example usage

Solo quick start with an explicit tree trigger:

```text
/unlazy tree 5 refactor the payment module and verify every migration path
```

Copy `templates/gates-leaf.md` to `GATES.md`, inspect without executing, then approve and run:

```text
node <path-to-skill>/scripts/gate-check.mjs --status GATES.md
node <path-to-skill>/scripts/gate-check.mjs --approve GATES.md
node <path-to-skill>/scripts/gate-check.mjs --reverify GATES.md
```

For parallel scoped work, claim a leaf after declaring disjoint `OWNS:` paths:

```text
node <path-to-skill>/scripts/gate-check.mjs --scope api --leaf leaf-1.2.1 --claim
```

Install the optional Stop hook only with user consent:

```text
node <path-to-skill>/scripts/install-hooks.mjs
```

## Maintenance status

4,140 stars, 322 forks, MIT License, primary language JavaScript, default branch `main`, last push 2026-09-03. Package name `unlazy-skill` at version `2.1.0` in source; no GitHub Releases listed at fetch time—pin commits for immutability. Test suite covers contract, dispatch, hardening, lint, stress, and self-check via `npm test` scripts with Node >=16 and zero runtime dependencies. Actively documented security and changelog surface for the unreleased 2.1.0 tree.
