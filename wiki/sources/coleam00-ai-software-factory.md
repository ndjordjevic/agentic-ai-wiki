---
type: source
category: "Coding-agent harnesses & methodologies"
studied: true
source_url: https://github.com/coleam00/ai-software-factory
tags:
  - archon-sdlc
  - autonomous-delivery
  - holdout-verification
  - merge-gate
  - human-in-the-loop
  - archon-loop
  - software-factory
related:
  - coleam00-archon
  - coleam00-factory-mission-control
  - coleam00-agent-control-plane
  - coleam00-harness-engineering-demo
  - software-factory-claude-code
  - dark-factory-autonomous-ai-codebase
product: ai-software-factory
detail_level: standard
created: 2026-11-03
updated: 2026-11-03
---

AI Software Factory is Cole Medin's installable consumer of the [[coleam00-archon]] SDLC pack: you write the release (a PRD or filed issues), the factory builds it as independently reviewed pull requests, and you judge the result in staging. It is explicitly not a dark factory. Humans stay at the two places they add the most — deciding what to build, and deciding whether what landed is right — while the middle (triage through verification and merge) runs on Archon workflows. The repo itself is a thin wrapper: setup, scheduling, project context, and ordinary app resources. It does not ship its own agent workflows.

_All claims below are sourced from ../../raw/github/coleam00-ai-software-factory.md unless otherwise noted._

## What it does

The factory starts from a PRD for the next release, or from issues on an app that already exists. `archon-backlog` slices a PRD into linked, ordered issues (the first one makes the product runnable end to end). `archon-loop` then keeps a backlog moving unattended, one move per lap: an agent picks one item, builds it, and reviewers that did not write it decide whether it merges. Merged work lands in staging. Anything that is off becomes a new issue and the factory picks it up.

Trusting a merge you did not read is treated as the hard half. A deterministic merge gate lands only what an evidence record supports. Protected paths (`MISSION.md`, `FACTORY.md`, `FACTORY_RULES.md`, `harness/**`, `.factory/**`, `factory/**`, `.claude/settings.json`, `.ignore`) cannot be changed by a reviewed delivery. Irreversible actions — identity, authentication, who may act as whom, migrating or deleting stored data — stop the factory for a human.

The companion dashboard is [[coleam00-factory-mission-control]], which reads `DECISIONS.md` and pin trailers from this repo. The same shape of spec → build → parallel review → approve, built only from Claude Code primitives, is [[software-factory-claude-code]]. The README's refusal of a lights-out pipeline is the practical counterpart of [[dark-factory-autonomous-ai-codebase]].

## Installation

Paste the README's setup prompt to a coding agent inside the application repo. The agent clones this repository (outside the app), runs `python ~/ai-software-factory/bin/factory.py init` from the application root, configures Archon with the chosen coding agent and model tiers, and helps write the three files nobody else can write. Requirements: git, Python 3.10+, `gh` authenticated with the `workflow` scope (`gh auth login -s workflow` and `gh auth setup-git`), a GitHub remote, a coding agent, bun, and uv. The installer brings a pinned Archon source, including the shared workflows. It preserves project configuration on upgrades, does not configure provider authentication or model tiers, and does not start a schedule.

Default pin at fetch time: Archon revision `1cfb8fc541580fe5edf15e9a504b572bc9bb45bb` on branch `factory/sdlc-on-dev`. `pack.json` must name the same revision. `init` also adds a pointer to `factory/WORKFLOW_POLICY.md` in the project's root `engineering.md`.

A server that never sleeps is the intended host. `docs/server-cheat-sheet.md` is an ordered set of prompts (SSH key, VPS, toolchain, two human browser logins, factory install, runtime wiring) and stops before scheduling so one issue can be watched first. Ubuntu agents may run `bin/bootstrap-ubuntu.sh`. The smallest recommended plan is 8 GB of RAM. Linux timers are systemd user units; `PATH` is captured from the shell that ran `schedule install`, `IS_SANDBOX=1` lets Claude Code run unattended as root, and the Claude token stays in a mode-600 `~/.factory-env`.

## Key features

Three human-owned files decide whether the factory stays on the product:

- `MISSION.md` — what the product is, and an out-of-scope list (aim for at least five things a reasonable person would ask for) so a plausible request can be recognised as drift. Hard invariants cannot be tuned by an issue. Open questions may be proposed and built against, but the merge is held for a human.
- `harness/END-TO-END.md` — two to five journeys in plain English that a real user takes today. "The page loads" is rejected as a bar. Journeys for behaviour that does not exist yet leave the gate red, except when the repo holds only a PRD.
- `.factory/holdout/HOLDOUT.md` — independent scenarios written from the product document, not from the issues. Committed so the team shares them, and fenced so builders cannot read them.

The holdout fence (`.factory/hooks/holdout_fence.py`, registered in `.claude/settings.json`) refuses every agent except `holdout-writer` and `holdout-verifier` any call that would reveal a scenario. `.ignore` keeps Grep and Glob out. The app check and the manager see a verdict and what a user sees, never the scenario. The fence is a Claude Code hook; a Codex or Pi factory keeps the holdout outside the repo and passes that path as the `holdout` input. `factory doctor` runs the hook and reports whether the fence holds and is committed.

Shared Archon workflows, not factory Python, own every AI step: `archon-backlog`, `archon-holdouts`, `archon-ship-block`, `archon-validate`, `archon-verify-runtime`, `archon-verify-runtime-suite`, `archon-regress`, `archon-discoveries`, `archon-merge-queue`, `archon-deploy`, `archon-loop`, and `archon-manager`. Ship runs its own triage. Factory Python does not dispatch individual stages and must not grow direct coding-agent subprocesses.

Scheduling is Archon's. After one watched lap, `.factory/schedule.json` names the workflow, inputs, and `parallel` (1–8, default 1). `schedule install` writes `.factory/trigger.json`; `--apply` registers the OS timer (launchd, Task Scheduler, or systemd). Each tick runs `schedule fire`, which calls `archon trigger fire` and `archon workflow wake`. A tick while every lap is busy is skipped. `archon-loop` claims work with a GitHub comment so parallel laps do not collide. `archon-manager` runs on a slower schedule and also watches runs that never started, infrastructure failures, leftover app instances, and empty laps. `pause` stops the timer from starting laps but still wakes runs waiting on CI. `halt` blocks new launches. The scheduler abandons a `running` lap whose log has been silent for 60 minutes, keeping the branch.

Merge policy: free private GitHub repos cannot report branch protection, so `required_checks` in `harness/harness.config.json` must name CI jobs (or `"none"`). Left empty, the merge queue holds every PR. `publish_holds` does not authorize merging.

Check depth is proportional to risk (light, normal, deep). At normal depth the holdout verifier runs only scenarios whose `Touches` line matches the work item. The manager still runs every scenario on the default branch.

## Architecture

`docs/derivation.md` splits ownership: the Archon SDLC pack owns agent execution, stage composition, retry policy, approval gates, and forge mutations. The factory installs a complete pinned source, prepares project data, invokes native entrypoints, and displays engine state. An earlier design kept a six-stage scheduler, acceptance receipts, and deployment inside the factory; those now live in the shared workflows. Engine changes on the pin branch are refused — missing engine behaviour is worked around in workflow files.

`DECISIONS.md` is append-only (newest first) so [[coleam00-factory-mission-control]] can parse it. Each entry is `Decision`, `Why`, `Replaces`, and `Version` (the Archon pin). The recorded arc: agents over deterministic gate scripts (2026-10-12); a hybrid loop that routes simple work in-loop and complex work through ship (2026-10-13); parallel laps with claims (2026-10-14); evidence-checked gates after an audit found escaped defects graded PASS (2026-10-17); checking proportional to risk (2026-10-21); holdouts inside the repo behind a hook, and no Archon engine changes (2026-10-24); the complex route uses dev's `archon-ship-block` and the forked workflows are removed (2026-10-24); the scheduler abandons silent laps (2026-10-26); a lap runs only the holdouts its work item exercises (2026-10-26). An open decision remains on the manager's schedule and health duty.

`archon-loop` is the recommended scheduled workflow. Each lap picks one move and routes it to an in-loop builder or to `archon-ship`, then a black-box app check (merge tested against the default branch, with probes, a defects-seen record, and evidence the next step verifies by script) and a reviewer decide. A deterministic merge gate merges only what that record supports. The scheduler starts a lap only when there is workable work. Pin commits are expected to carry `Hypothesis` and `Measure` trailers so the dashboard can score a version.

Layout: `bin/factory.py` is the install CLI; `template/` is what `init` copies (`factory/consumer.py`, `pack.json`, `WORKFLOW_POLICY.md`, `RUNTIME_HOST.md`, `harness/`, the mission template). `docs/incidents.md` is the historical failure log the decisions were forced by.

This is the production factory in the Cole Medin harness family, beside the teaching loop in [[coleam00-harness-engineering-demo]] and the Pi-based durable loop in [[coleam00-agent-control-plane]].

## Example usage

From the application repo after install:

```bash
python factory/consumer.py doctor
python factory/consumer.py list
python factory/consumer.py run archon-loop --input merge=approve
python factory/consumer.py run archon-holdouts --input source=<path to the PRD>
python factory/consumer.py run archon-backlog --input prd=<path to the PRD> --input publication=approve
python factory/consumer.py schedule install --apply
python factory/consumer.py halt
```

`merge=approve` makes the reviewer approve instead of merging, so the first lap can be watched. Doctor checks the installation and available workflows; it does not prove a live agent can sign in. Leave scheduling off until that lap has been seen. With `deploy` and `health` commands set, a confirmed merge runs `archon-deploy` and reads the deployed revision back. Without them, a merge is only a merge.

A schedule that allows three parallel laps looks like:

```json
{
  "workflow": "archon-loop",
  "parallel": 3,
  "inputs": {
    "runtime": "/private/runtime/scenario.json",
    "merge": "auto"
  }
}
```

The factory adds `holdout=.factory/holdout/HOLDOUT.md` and the project's `protected_paths` unless the schedule names them.

## Maintenance status

481 stars, 83 forks, primary language Python, default branch `main`, no GitHub license, no releases. Last push 2026-10-31. The integration note in `docs/first-hour.md` still says live end-to-end validation is required; installation checks alone do not prove a successful factory run. Workflow improvements belong in Archon's SDLC pack, not in this repo. Upgrades are `git pull --ff-only` on the factory clone, then rerun `init`; see `template/factory/MIGRATION.md`. Neutral Archon users do not need `MISSION.md` or `factory/WORKFLOW_POLICY.md`.
