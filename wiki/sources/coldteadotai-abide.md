---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/coldteadotai/abide
tags:
  - rules-enforcement
  - rubric
  - agents-md
  - jev
  - coding-agent-hooks
  - project-rules
  - calibrated-probability
  - edit-repair
related:
  - typesafe.ai
  - RiskAverseTech-toolgate
  - valentynkit-jev-belay
  - obra-superpowers
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
product: abide
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Abide enforces project instruction rules that no linter can check — from AGENTS.md, CLAUDE.md, and related files — by compiling them into a committed rubric and scoring every edit (or turn) with TypeSafe's Jev decision model. On a break it names the rule and asks the agent to repair in the same turn. It hooks Claude Code, Codex, OpenCode, and Pi; checks cost about 300 ms and a few thousandths of a cent per edit under the author's measurements.

_All claims below are sourced from ../../raw/github/coldteadotai-abide.md unless otherwise noted._

## What it does

Session start hashes instruction files and has the agent compile them into `.abide/rubric.json` when they change. Turn start snapshots the working tree; after each edit, edit-phase rules run on that hunk; end of turn diffs the whole turn and runs turn-phase rules (plus edit-phase rules for shell-written files). Each rule is one Jev question on the rule plus the diff — never the conversation — returning a calibrated probability. Verdicts ≥ 0.8 tell the agent to repair; 0.5–0.8 are human notes only; below 0.5 are silent. Rules a linter could check are left to the linter; Abide ships no built-in rules. Replay of 93 real Claude Code sessions (1,256 edits, 147 turns) reported roughly 1 in 13 turns breaking a rule, with Jev flagging 39 edits / 15 turns and an independent reviewer confirming 10 / 11.

## Installation

```
npx @coldtea/abide login    # TypeSafe or Vercel AI Gateway key → ~/.abide/.env or .env.local
npx @coldtea/abide init     # hooks into every agent found on this machine
```

Per agent: `init claude` → `~/.claude/settings.json`; `init codex` → `~/.codex/hooks.json` (accept via `/hooks`); `init opencode` → OpenCode plugin; `init pi` → Pi extension. Add `--project` for repo-local install. Uninstall with `abide uninstall [agent]`.

## Key features

- **Your rubric, committed** — `.abide/rubric.json` quotes the instruction line each rule came from; hand-written rubrics can set `"manual": true` so compile leaves them alone.
- **Edit vs turn timing** — rules run after each edit or once against the whole-turn diff; optional `scope` globs per rule.
- **CLI toolkit** — `audit`, `check`, `report`, `replay`, `compile`, `calibrate`, `tune`, `bench`; several accept `--json`.
- **`.abideignore`** — repo-root picomatch globs skip files for every rule.
- **Fail open on miss** — no key or no network: the edit proceeds unchecked and the miss is logged in `.abide/events.jsonl`.
- **Privacy path** — changed lines go to TypeSafe (or Vercel AI Gateway with `zeroDataRetention: true`) under your key; no Cold Tea server in the path. Optional `TYPESAFE_AI_BASE_URL` for self-hosted/proxy/mock.

## Architecture

Monorepo: `packages/schema` (zod schemas for rubric, hook payloads, verdicts, events), `packages/cli` (abide command, hook script, OpenCode plugin, Pi extension), `skills/abide-compile` (agent procedure to compile a rubric). Four hook moments per agent (session start, turn start, after edit, end of turn). OpenCode and Pi use plugins/extensions rather than process hooks; Pi registers `pi.on()` handlers and allows at most one final repair continuation. Key lookup: environment, then `.env.local` / `.env` at repo root, then `~/.abide/.env`. Hooks exit 0 with a hard deadline so a check failure cannot break the session.

## Example usage

```
abide audit src/
abide check
abide report
abide compile
abide calibrate
abide replay claude
```

A violating edit surfaces a named rule and score, e.g. rule `api-validation-uses-yup` scored 0.86, with "Repair … now, then continue with the task."

## Maintenance status

MIT licensed; TypeScript; default branch `master`; no tagged GitHub releases at ingest (613 stars). Pi extension documented as tested with Pi 0.99.1; native-binary Pi builds not yet exercised end-to-end. Live Pi repair test is opt-in (`ABIDE_PI_LIVE=1`). Cost/latency figures in the README were measured 2026-09-18 direct to TypeSafe.
