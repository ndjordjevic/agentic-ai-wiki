---
type: source
category: "Coding-agent harnesses & methodologies"
studied: true
source_url: https://github.com/coleam00/factory-mission-control
tags:
  - neon-realtime
  - live-dashboard
  - factory-observability
  - architecture-map
  - scorecard
  - read-only
  - github-webhooks
related:
  - coleam00-ai-software-factory
  - coleam00-archon
  - coleam00-agent-control-plane
product: factory-mission-control
detail_level: standard
created: 2026-11-03
updated: 2026-11-03
---

Factory Mission Control is the live dashboard for [[coleam00-ai-software-factory]], and it is built by that factory. It shows the factory's architecture as one map parsed from the pinned code, how that architecture has evolved and why, and — for each application a factory is building — the product document, the issues it was sliced into, the laps working through them, how each change was tested, and what is waiting on the owner. Every panel is a Neon Realtime query, so the screen moves when an agent writes a row. v1 never writes back to GitHub, Archon, or a factory repository.

_All claims below are sourced from ../../raw/github/coleam00-factory-mission-control.md unless otherwise noted._

## What it does

The problem the PRD names is that factory state is split across Archon run history, GitHub (issues, labels, claim and review comments, pull requests), and the factory repository (pinned workflows and `DECISIONS.md`). Answering "what is it doing right now?" meant a terminal, a dozen GitHub tabs, the Archon console, and hand-written metric scripts. The hypothesis is that if every fact lands in one Postgres database and every panel is a live query, the owner stops rebuilding those scripts and sees a question waiting on them within minutes. It is stated so it can be wrong: two weeks of still writing throwaway metric scripts, or still discovering stuck laps from a watchdog line, falsifies it.

There is no repository README. The product contract is `docs/mission-control.prd.md` (approved for the first factory run on 2026-10-24). `MISSION.md` compresses the never-list the factory must obey. The dashboard is deliberately not a second Archon console: one lap links to the console for its full log.

## Installation

The runtime contract the factory drives:

```bash
bun install
bun run setup          # vite build
bun run serve -- --port <port>
bun run check          # tsc, biome, bun test; no network
bun run migrate        # numbered SQL, idempotent; refuses branch name main
```

Serve on `127.0.0.1` and open `http://localhost:<port>`. Realtime allows only `http://localhost:5173` and ports 8850–8864, so every lap, holdout verifier, and CI instance takes a free port in that range. Checks never touch the `main` database branch. `bun run fixture:branch` creates `check-<id>` from an owner-made `fixture` branch, applies migrations, loads `fixtures/seed.sql`, and writes the connection string to gitignored `.mc-check.env`. `fixture:drop` deletes that branch and any `check-*` branch older than three hours. Only the owner runs `bun run migrate:main`.

Environment: `MC_DATABASE_URL`, `NEON_REALTIME_SECRET`, `NEON_API_KEY`, `NEON_PROJECT_ID`, and optionally `MC_FACTORIES_FILE`. Never `DATABASE_URL` (that name belongs to Archon on the same machine). `GET /api/health` returns 200 once the app can serve. `GET /api/build-id` returns the git commit.

The GitHub ingestion path is a Neon Function (`bun run function:deploy`). Deploying to `main` and registering webhooks (issues, issue comments, pull requests, pushes, labels) on each repository in `factories.json` and on `coleam00/ai-software-factory` are owner steps after merge.

## Key features

The home screen is a factory-agnostic architecture map at the pinned version: inputs (product document, `archon-holdouts`, `archon-backlog`, owner decisions), every step of `archon-loop`, ship expanded from `archon-ship-block`, `archon-manager` above the loop, and outputs (merged pull requests, closed issues, deploys, owner questions, metrics). Each step shows a live per-factory lap count. Clicking a step opens its description, inputs and outputs, `when` route, model tier, workflow YAML, prompt, inline subagents, scripts, and hooks — parsed from the pinned code, never typed in. Holdout steps explain the fence without showing scenario text. Nested includes draw as dashed boxes; a lap on a nested step counts on that step and on every box around it. `/?at=<pin>` opens an older recorded architecture. A factory with no recorded lap shows "No factory map is available yet."

A version strip lists each pin with its one-line reason and `Hypothesis` / `Measure` trailers from [[coleam00-ai-software-factory]]. The scorecard, per version and per factory, defines lap, merge, empty lap, failed lap, send-back, gate refusal, lap-hours per merge, app-check share, cost per merge, and new holdout catch. A difference resting on fewer than 10 laps on either side is labelled "not yet meaningful". Numbers are never summed across factories. `DECISIONS.md` entries sit on a timeline joined to the pin named in `Version:`. Two versions can show an architecture diff of workflows, steps, prompts, and subagents.

Per factory: product-document phases with merged and total issues, an issue graph from `Depends on: #n` (waiting, claimed, pull request open, `needs-owner`, merged, closed), a lane per running lap, and recent laps with outcome, duration, and cost. The owner queue lists `needs-owner` issues and open questions from the manager's "Owner decisions needed" issue, each linking to its GitHub thread. v1 never answers them. Testing panels show route and check-depth mix, app-check lines by kind and verdict, and holdout verdicts by scenario id only. One lap shows each step's start, duration, model, tokens, and cost, plus links to the pull request, the issue, and `<console>/console/r/<runId>`.

Rewind opens the same screens on a Neon branch from up to 7 days back (`bun run rewind:create <ISO time>`, branch name `rewind-<time>`), read-only. Health covers `pending` and `paused` runs, steps running longer than twice that step's 90th-percentile duration, failed laps by cause (usage limit, authentication, infrastructure, other), and workable issues against running laps.

## Architecture

Stack, decided in the PRD so the factory cannot reinvent it: React 19, Vite 6, Tailwind v4, react-router 7 with one route file per screen (a file name encodes the path: `f.$factory.versions.tsx` serves `/f/:factory/versions`). Live data is Neon Realtime (`@neon/realtime-react`): each panel is one `useLiveQuery` on a sealed read-only SELECT with no `now()`, no `random()`, and no volatile function. The browser computes elapsed time. A Bun + Hono server serves the built app and seals queries (they expire every 60 seconds; the client renews). The database is a Neon project with Postgres 18, logical replication, and 7-day history. Tooling is Bun 1.4, TypeScript strict, and Biome.

Facts arrive on three paths. Archon already writes laps, steps, cost, and structured outputs into this project's `main` branch; triggers on `node_started`, `node_completed`, `node_failed`, and `node_skipped` (and on workflow runs) project those rows into the dashboard's tables and catch every error into `projection_errors` instead of raising, so a dashboard fault cannot fail an Archon write. GitHub issues, labels, claims, and pull requests arrive through the Neon Function webhook, a nightly reconcile, and a backfill script. Versions, hypotheses, verdicts, and `DECISIONS.md` arrive from pushes to `coleam00/ai-software-factory`. Live queries never read Archon's `provider_event` rows. The architecture job (`bun run arch:parse`) reads the pack at an Archon commit and the factory template at a factory commit and stores workflows, steps, edges, YAML, prompts, and scripts. Tests run on the committed snapshot in `fixtures/pack/`.

`factories.json` at fetch time lists `mission-control` (`coleam00/factory-mission-control`, console `http://localhost:3090`) and `north-star` (`coleam00/north-star-godot`, same console). Every view is keyed by factory and must work with exactly one. Holdout scenario ids follow `H-<nn>`; the projection stores the id and the verdict, never the scenario text.

Design is copied from `docs/design/archon-console/`: dark only, Geist and Geist Mono, Dynamous Blue `#3B82F6` as the single accent. `harness/design-probe.js` fails any rendered color outside the tokens, contrast below 4.5:1, or horizontal overflow at 1440 and 390 px. Counts and progress are drawn (bars, grids, graphs via dagre); tables are reserved for records a person scans row by row. A live panel is judged on its own work: query execution under 100 ms on the seed, rows on screen within 500 ms of the first snapshot, Realtime `ready` within 2000 ms of navigation. No `initialData`, so a panel is ready only when it is live.

The same "watch the loop" job, on a different runtime, is [[coleam00-agent-control-plane]] (Pi loops, Neon history, a React dashboard). This repo is the factory-specific console and stays read-only toward [[coleam00-archon]].

## Example usage

`factories.json` names which factories appear:

```json
{
  "factories": [
    {
      "name": "mission-control",
      "repository": "coleam00/factory-mission-control",
      "codebase": "coleam00/factory-mission-control",
      "console": "http://localhost:3090"
    }
  ]
}
```

Owner operations after a merge: `bun run migrate:main`, `bun run function:deploy -- --branch main`, then register the printed webhook URL on each factory repository. Background repair of the dashboard's own tables is `reconcile:laps` / `reconcile` on the owner's schedule (every 10 minutes on the reference install), never from the app server or the webhook. A check that deploys a Function deletes it before `fixture:drop`.

Core journeys the PRD treats as observable: open the map and read the check-app prompt and fence; watch a lap move steps without a reload; compare two versions' scorecards and architecture diff; find the owner queue; switch to a rewind branch.

## Maintenance status

17 stars, 2 forks, primary language TypeScript, default branch `main`, no GitHub license, no releases. Last push 2026-10-29. The package is `"private": true`. The PRD's success bar is operational rather than a version number: in the two weeks after launch the owner writes no throwaway metric script, every later pin carries `Hypothesis` and `Measure` and gets a verdict, and an owner question is seen within 10 minutes. Out of scope forever in v1: writing to GitHub or Archon, rebuilding the run-log viewer, changing the Archon engine or schema, user accounts, and hosting the UI off the owner's machine (the webhook Function is the exception, hosted by Neon).
