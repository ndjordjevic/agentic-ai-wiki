---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://github.com/chaseai-yt/grill-me-codex
tags:
  - cross-model-review
  - claude-code-skills
  - adversarial-review
  - codex-cli
  - plan-first
  - sandboxed-review
  - fork-of-grill-me
  - three-act-workflow
related:
  - mattpocock-skills
  - shadcn-improve
  - seangeng.com-plan-optimizer
  - othmanadi-planning-with-files
product: grill-me-codex
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

`grill-me-codex` (666 stars, MIT) is a three-act Claude Code skill family built on top of Matt Pocock's `grill-me`/`grill-with-docs` skills that adds cross-model adversarial review: after Claude interrogates the human to lock a plan (Act 1, Pocock's original work), the plan is handed to OpenAI Codex — a rival, different-provider model — which tears it apart over several read-only review rounds until both models sign off (Act 2, this repo's addition). An optional Act 3 flips the roles entirely: Codex writes the code from the frozen plan with full write access, while Claude reads the diff like a contributor PR and re-verifies independently. The core thesis is explicit: a model that plans and writes the build can't be trusted to grade its own work, so a second provider does the grading.

_All claims below are sourced from ../../raw/github/chaseai-yt-grill-me-codex.md unless otherwise noted._

## What it does

Four skills cover different entry points into the same three-act pattern: `grill-me-codex` (plan from scratch, one-question-at-a-time interrogation, then Codex review), `grill-with-docs-codex` (same, but checks the plan against a project's `CONTEXT.md` glossary and writes ADRs inline), `codex-review` (skip Act 1 — you already have a plan, just want the cross-model stress-test), and `codex-build` (skip straight to Act 3 — you have a reviewed spec and want Codex to implement it while Claude verifies). Every review round is logged to two artifacts: `PLAN.md` (the clean final plan) and `PLAN-REVIEW-LOG.md` (the full round-by-round argument, including build-phase fix rounds when Act 3 runs).

## Installation

Copy the skill folders directly into the Claude Code skills directory — no marketplace or plugin manager:
```bash
cp -r skills/* ~/.claude/skills/          # macOS / Linux
Copy-Item -Recurse skills\* $env:USERPROFILE\.claude\skills\   # Windows PowerShell
```
Then invoke with `/grill-me-codex`, `/grill-with-docs-codex`, `/codex-review`, or `/codex-build`. Requires Codex CLI ≥ 0.130 (`npm install -g @openai/codex@latest` — older versions error on the default model) and a one-time `codex login` (any ChatGPT tier works); the skills deliberately avoid pinning a Codex model variant since ChatGPT-account auth rejects `gpt-5.x-codex` pins. (../../raw/github/chaseai-yt-grill-me-codex.md)

## Key features

- **Cross-provider adversarial review (Act 2)** — Codex reviews `PLAN.md` in a read-only sandbox and returns `VERDICT: APPROVED` or `VERDICT: REVISE`; Claude revises and *resumes the same Codex session* (not a fresh one) so Codex remembers its prior critiques and only checks whether they were addressed. Bounded by `MAX_ROUNDS` (default 5) — hits the cap and flags a deadlock rather than faking an approval.
- **Role-flipped build (Act 3, optional)** — after human sign-off, `codex-build` hands the frozen `PLAN.md` to Codex with full write access (`--yolo`); Codex implements and runs tests. Claude then reads the complete diff like a contributor PR and re-runs the proof test itself — Codex's own claims are treated as advisory, not proof. Fix rounds are capped (`MAX_FIX_ROUNDS`, default 2); past that, Claude finishes by hand instead of endless ping-pong.
- **Hard sandbox discipline** — Act 2's read-only enforcement is done explicitly per-call (`-s read-only` on first call, `-c sandbox_mode="read-only"` on every resume) because Codex's `resume` subcommand doesn't accept `-s` and would otherwise silently inherit the user's `config.toml` sandbox default, which may be `danger-full-access`.
- **Session identity discipline** — Act 3 resumes require the long flag `--dangerously-bypass-approvals-and-sandbox` (no `--yolo` shorthand on resume) and must always target an explicit `thread_id`, never `--last`, since a missing or wrong id can silently continue a different session.
- **Human gates exactly three times total**: plan kickoff, plan sign-off before any code, and diff sign-off before commit. Claude, not Codex, always writes the commit.
- **Bonus image generation** — Codex sessions carry a native, ChatGPT-account-backed image-generation tool (no separate API key), so a build spec can include "generate these assets yourself" steps with exact paths/dimensions.

## Architecture

`skills/` holds four independent skill folders (`grill-me-codex/`, `grill-with-docs-codex/`, `codex-review/`, `codex-build/`), each a self-contained Claude Code skill invoked via its own slash command. The design deliberately separates *who has write access when*: Acts 1–2 keep Codex strictly read-only across every round (enforced per-invocation, not just at session start), while Act 3 inverts that and gates the resulting blast radius with a clean-git-tree precondition, a bounded fix-round count, and mandatory human diff review before commit. All rounds — review and build — append to one shared `PLAN-REVIEW-LOG.md`, so a single artifact narrates the whole lifecycle: grilled → reviewed → built → verified. (../../raw/github/chaseai-yt-grill-me-codex.md)

## Example usage

```
/grill-me-codex                 # Act 1: Claude interrogates you to lock a plan, then Codex reviews it
/grill-with-docs-codex          # same, but checked against CONTEXT.md + writes ADRs
/codex-review rounds=3          # skip Act 1 — you already have a plan, just get the Codex stress-test
/codex-build                    # Act 3: Codex implements the signed-off plan; Claude verifies the diff
```
(../../raw/github/chaseai-yt-grill-me-codex.md)

## Maintenance status

666 GitHub stars, 80 forks, MIT license (README states MIT; GitHub API reports license `Other`, likely metadata lag), default branch `main`, most recent push 2026-07-08, no tagged releases. Small, single-purpose repo (no primary language detected — pure skill/Markdown package). Credits Act 1 to Matt Pocock's `mattpocock/skills` (MIT) and Act 3's delegation pattern to Peter Steinberger's `codex-first`; Acts 2–3 and packaging are attributed to Chase AI. (../../raw/github/chaseai-yt-grill-me-codex.md)

## Ecosystem

A direct downstream fork/extension of [[mattpocock-skills]] — Act 1 (`grill-me`, `grill-with-docs`) is Pocock's unmodified work, reused here and extended with the Codex adversarial-review and role-flipped-build acts. Sits in the same plan-first methodology space as [[seangeng.com-plan-optimizer]] and [[othmanadi-planning-with-files]], but is distinguished by being explicitly **cross-provider**: where most plan-review skills in this wiki (including [[shadcn-improve]]'s audit-and-plan approach) use one model throughout, this one structurally requires a second, independently-authenticated provider (Codex CLI) so the reviewer can't share blind spots with the author.
