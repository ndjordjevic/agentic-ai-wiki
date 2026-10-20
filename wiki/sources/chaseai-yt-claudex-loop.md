---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/chaseai-yt/claudex-loop
tags:
  - cross-model-review
  - claude-code-skills
  - codex-cli
  - plan-review-loop
  - adversarial-review
  - model-routing
  - agent-skills
  - mit
related:
  - chaseai-yt-grill-me-codex
  - obra-superpowers
  - frankbria-ralph-claude-code
  - software-factory-claude-code
product: claudex-loop
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

`claudex-loop` is a Chase AI skill pack for working across Claude Code and Codex: four skills share one plugin distribution — `claudex-loop` (full recon → requirements → cross-provider plan review → build → independent inspection), standalone `claudex-route` (model/role recommendation or one scoped handoff), plus compatibility aliases `codex-review` and `codex-build`. ~3.1k GitHub stars, MIT, Python 3.10+ adapter with no runtime pip deps. Successor to `grill-me-codex` / `crucible` (legacy skills remain under `legacy/`).

_All claims below are sourced from ../../raw/github/chaseai-yt-claudex-loop.md unless otherwise noted._

## What it does

The core thesis: **whoever built it never grades it.** The host conversation handles requirements and coordination; the other provider reviews the plan with evidence; after authorized implementation, a fresh session of the non-builder inspects the code. Default pairings:

| Host | Plan review | Default build | Final inspection |
|------|-------------|-----------------|------------------|
| Claude Code | Codex | Claude | Fresh Codex |
| Codex | Claude | Codex | Fresh Claude |

`builder=claude` or `builder=codex` flips the build side; the inspector always uses the other provider. `claudex-route` is independent of the loop — recommend who should handle a task (or perform one handoff) without the approval-binding runner.

Artifacts: `PLAN.md` (what to build) and `PLAN-REVIEW-LOG.md` (findings, dispositions, models, proof, uncertainty); both paths configurable. CLI diagnostics land in a unique directory outside the target checkout.

## Installation

Both CLIs must be installed and authenticated for the full cross-provider workflow. Python **3.10+** runs the shared adapter; no separate API keys beyond CLI accounts. Check `codex --version` / `codex login status` and `claude --version` / `claude auth status`.

**Claude Code plugin:**

```text
/plugin marketplace add chaseai-yt/claudex-loop
/plugin install claudex-loop@claudex-loop
```

**Codex or manual (copy all skills together — aliases share `claudex-loop` runtime):**

```bash
mkdir -p ~/.agents/skills ~/.claude/skills
cp -R skills/. ~/.agents/skills/
cp -R skills/. ~/.claude/skills/
```

Route-only: copy `skills/claudex-route/` alone into `~/.agents/skills/` or `~/.claude/skills/`. Open a new session after install. Dev/verify: `pip install -r requirements-dev.txt`, then `python scripts/validate.py` and `python -m unittest discover -s tests -v`.

## Key features

- **Four-phase loop** — recon (assumptions ledger) → requirements/plan with acceptance checks → bounded plan-review rounds (`APPROVED` / `REVISE` / `BLOCKED`) → authorized build + proof commands + independent inspection.
- **Cross-provider sandboxing** — Codex reviews use read-only shell sandbox; Claude reviews expose file read/search only (customizations/MCP off). Builders use bounded permissions; delegated builds expect a clean checkout (worktree optional for unrelated work).
- **Approval binding** — runner validates structured review + plan path/SHA256; plan edits invalidate approval. Inspections fingerprint pre-build commit and change set (staged + untracked).
- **Configurable controls** — `mode` (`full` / `review`), `plan`/`log` paths, `builder`, per-role model/effort overrides, `rounds` (default 5), fix/inspection round caps, `research`, `inspect`, `PROOF_CMD`.
- **Claudex Route** — self-contained routing skill (no Python); recommendations alone do not launch another model or authorize edits.
- **Explicit Codex aliases** — `codex-review` / `codex-build` for compatibility; host-based routing prefers `claudex-loop`.

## Architecture

Distribution is a **skill + plugin** layout, not a long-running server:

- `skills/claudex-loop/` — full workflow + Python adapter/runtime references
- `skills/claudex-route/` — standalone routing instructions
- `skills/codex-review/`, `skills/codex-build/` — thin compatibility commands over shared loop runtime
- `.claude-plugin/`, `.codex-plugin/` — marketplace/plugin packaging
- `tests/`, `scripts/validate.py`, `VALIDATION.md` — CI on Windows/macOS/Linux with fake CLIs and disposable git repos

Host arbitrates findings, records decisions, and keeps the loop within round budgets. Requested vs observed models are logged separately; there is no silent model/provider fallback.

## Example usage

```text
claudex this feature — plan and implement it
claudex this plan, mode=review, plan=docs/migration.md, rounds=3
claudex this feature, builder=codex, reviewer_model=gpt-6-astra
claudex this feature, builder=claude, reviewer_model=claude-fable-5-1
claudex-route: Who should handle this CSV import feature? Prioritize cost.
```

After plugin install: `/claudex-loop:claudex-loop`, `/claudex-loop:claudex-route`, `/claudex-loop:codex-review`, `/claudex-loop:codex-build`. Manual Codex: `$claudex-loop` / `$claudex-route`.

## Maintenance status

- **Stars:** 3,141 (fetched 2026-10-20)
- **Latest release:** none tagged
- **License:** MIT (README / LICENSE; metadata also notes “Other”)
- **Language:** Python (adapter) + Markdown skills
- **Activity:** pushed 2026-10-14; CI + unittest suite; community PR acknowledgments in `ACKNOWLEDGMENTS.md`
- **History:** renamed from `grill-me-codex` / `crucible`; GitHub redirects still work
