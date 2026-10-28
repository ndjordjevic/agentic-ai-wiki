---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/valentynkit/jev-belay
tags:
  - stop-hook
  - completion-verification
  - jev-model
  - fail-open
  - claude-code-plugin
  - transcript-evidence
related:
  - typesafe.ai
  - RiskAverseTech-toolgate
  - coldteadotai-abide
  - snarktank-ralph
  - obra-superpowers
  - Larkspur-Wang-Jev_steer_or_queue
product: jev-belay
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

jev-belay is a Claude Code Stop hook (MIT, JavaScript) that blocks an unverified "done": it reads the turn's transcript locally for file changes and test/build/lint evidence, and only when something changed and no check has passed since does it spend one Typesafe Jev call (four questions, ~$0.00005, ~346 ms median) on whether the closing message is an unverified completion claim. If so, the turn does not end and Claude gets a reason to run the suite; every other stop costs nothing, and every error path fails open (lets the turn end).

_All claims below are sourced from ../../raw/github/valentynkit-jev-belay.md unless otherwise noted._

## What it does

On Stop, the hook exits immediately when a prior block is active, the session block cap is hit, or no API key is set. Otherwise it reads the transcript slice since the last user prompt (folding matching `subagents/` turns since 0.2.0): belt 1 looks for a named test/build/lint runner (plus optional custom `check` regex); belt 2 looks for runner summaries in output. If nothing changed or a check passed after the last change, it exits 0 with no network. Only then does it take the closing message and ask Jev four questions — `claims_done`, `claims_verified`, `verification_applies`, `outcome` — and `decide()` either exits 2 with a block reason or exits 0. On a 100-stop labeled audit slice the shipped threshold reports AUROC 0.976 vs 0.777 for wording alone, blocking 8/100 stops (7 rightly). Honest limit: turns with no file edits never reach Jev, so a read-only "confirmed, tests pass" sails through.

## Installation

As a Claude Code plugin:

```
/plugin marketplace add valentynkit/jev-belay
/plugin install jev-belay@jev-belay
```

Claude Code prompts for a TypeSafe key (Keychain) plus threshold, decision log, shadow mode, and custom check command (editable via `/config`). Manual install wires a Stop command hook in `~/.claude/settings.json` with `TYPESAFE_API_KEY` (or `JEV_API_KEY`) in an `env` block. Requires Node 20+ and Claude Code 2.1.196+ for `prompt_id`. Notable knobs: `JEV_BELAY_THRESHOLD` (default 0.70), `JEV_BELAY_SHADOW`, `JEV_BELAY_LOG`, `JEV_BELAY_CHECK`, `JEV_BELAY_TIMEOUT_MS`, `JEV_MODEL` (pinned to `jev-1.13.0`). Plugin options as `CLAUDE_PLUGIN_OPTION_*` override plain env vars.

## Key features

- **Evidence before judgement** — local regex belts establish run facts; Jev is only asked when edits exist and nothing fresh passed.
- **Fail-open** — missing key, network failure, garbage payload/answer → exit 0; the turn ends.
- **Cheap when it fires** — one call, four questions; ~17.7% of stops in one corpus reach the question; others are a free transcript read.
- **Loop safety** — at most one block per prompt, none within 60 s of the last, three per session (host also caps consecutive blocks).
- **Shadow mode and live view** — shadow reports what it would block without stopping Claude; `JEV_BELAY_LOG` enables `belay.mjs watch` / `stats` / `last`.
- **Skills** — `/jev-belay:why` explains the last decision; `/jev-belay:doctor` checks install.
- **Minimal egress** — request carries task, final message, and two counts (`file_changes`, `checks_run`); no diffs, tool inputs, or file contents; secret-shaped strings redacted.

## Architecture

Decision flow is owned by `belay.mjs`: Stop payload on stdin → local evidence gate → optional one Jev call → exit 2 (block) or 0 (allow). Code owns transcript walk, counting, thresholds, timeouts, and dedup; Jev owns one judgment. Question wording and both regex belts are credited to pi-warden; the project's motivation cites limpet's wording-only calibration (~AUROC 0.50). `tui.mjs` powers the live decision view; `hooks/hooks.json` wires Claude Code; `skills/doctor` and `skills/why` are plugin skills; `tools/` includes `fake-jev.mjs`, corpus extract/label, and measure scripts; `corpus/RUBRIC.md` defines the `false_done` labeling conjunction used in evaluation.

## Example usage

Try without a real key (fake Jev + sample Stop payload):

```
node tools/fake-jev.mjs --port 4321 &
JEV_BASE_URL=http://127.0.0.1:4321 node belay.mjs < test/stop-blocked.json; echo $?
echo 'not json' | node belay.mjs; echo $?
node belay.mjs --replay demo/sample-decisions.jsonl
```

The first exits 2 with the reason Claude would see; unreadable stdin exits 0. With the log enabled, `node belay.mjs watch`, `stats`, and `last` inspect decisions. A typical block message tells Claude it reported completion after file changes with no test/build/lint since the last change and asks it to run checks or admit none exist.

## Maintenance status

MIT License; default branch `main`; latest release **v0.2.0** at ingest (41 stars, primary language JavaScript). Offline tests via `npm test` against `tools/fake-jev.mjs`; `node belay.mjs doctor` checks key, host version, hook registration, and a round trip. Measurement (`npm run measure` with `--ablation` / `--sweep`) reproduces AUROC and threshold figures on a user-built redacted corpus. Credits pi-warden (question wording, regex belts) and limpet (published calibration that motivated evidence-first design).
