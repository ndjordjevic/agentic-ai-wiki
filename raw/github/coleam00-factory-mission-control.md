# coleam00/factory-mission-control

## Metadata
- Stars: 17
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: none
- Homepage: (none)
- Fetched: 2026-11-03
- Final URL: https://github.com/coleam00/factory-mission-control

## Description
Mission control for the AI Software Factory: the factory's architecture, its evolution, and every factory's PRD, issues and laps, live on Neon Realtime. Built by the factory itself.

## README
No repository README. The product contract is `docs/mission-control.prd.md`. `MISSION.md` is the compressed mission the factory must obey. `engineering.md` is how the repo is built.

## Docs

### MISSION.md

# Mission

Factory Mission Control makes the AI Software Factory visible: the factory's architecture as one
live map, how it has evolved and why, and for every application a factory builds, the product
document, its issues, the laps working through them, how each change was tested, and what waits on
the owner. Every panel is a live query on Neon Postgres, so the screen moves the moment an agent
writes. The product document is `docs/mission-control.prd.md`; it decides.

## Never

1. Never write to GitHub, to Archon, to a factory's repository or to Archon's tables. v1 is
   read-only toward everything it shows.
2. Never slow or break an Archon write. Whatever this app adds to the database fails silently
   and is counted, never raised into Archon's transaction.
3. Never store or show a holdout scenario's title, text, steps or thresholds. Holdouts are ids
   and verdicts.
4. Never send a secret to the browser: the Realtime secret, database URLs and GitHub tokens stay
   on the server and in the Neon Function.
5. Never poll. A panel that is not a live query (or derived from one) is not done.
6. Never hand-write the factory's architecture. It is parsed from the pinned code.
7. Never invent a look. The design is the Archon console's (docs/design/archon-console/).
8. Never become a second Archon console: one lap links to the console for its full log.
9. Never sum numbers across factories; each factory's numbers stand alone.


### engineering.md

# Engineering

How this repository is built. The product is `docs/mission-control.prd.md`; this file is how.

## Layout

| Path | What lives there |
|---|---|
| `app/` | The browser app: React 19, Vite 6, Tailwind v4, react-router 7. One file per screen under `app/routes/`, registered from the directory; a file's name encodes its path (`.` separates segments, `$name` is a parameter: `f.$factory.versions.tsx` serves `/f/:factory/versions`, #73). |
| `server/` | Bun + Hono: serves the built app, `/api/health`, `/api/build-id`, and the sealing API for live queries. At start on a `check-*` branch it loads the factories file it serves into `mc.factories`, as `migrate -- --configured-factories` does, and fails to start if that fails; it never writes `main` or a `rewind-*` branch. |
| `db/migrations/` | Numbered SQL files, applied in order by `bun run migrate`; each idempotent. A merged migration is never edited (main has applied it and never re-runs it): change it with a new, higher-numbered file. |
| `db/queries/` | Every live query, one file each, named for the panel that reads it. |
| `function/` | The Neon Function that receives GitHub webhooks (Hono, TypeScript). |
| `parsers/` | Pure functions: comment formats, pin trailers, DECISIONS.md, the architecture parser. |
| `scripts/` | `fixture:branch`, `fixture:drop`, `fixture:write`, `migrate`, `backfill`, `rewind:create`, `function:deploy`, `function:idle-check`. |
| `fixtures/` | `seed.sql`, `expected-scorecard.json`, `webhooks/` sample payloads, `pack/` (a snapshot of the pinned workflow pack), `factory-template/` (the fence files). |
| `harness/` | `design-probe.js` and the factory harness configuration. |
| `docs/design/archon-console/` | The Archon console's tokens and components, copied from Archon. The design source of truth. |
| `factories.json` | The factories the dashboard shows (PRD 11.6). |

## Rules

- TypeScript strict everywhere. Bun 1.4 for running, testing (`bun test`) and scripts. Biome for
  lint and format; `bun run check` runs type-check, lint and unit tests with no network.
- Every live query is a single read-only SELECT with no `now()`, no `random()` and no volatile
  function. Return timestamps; the browser computes elapsed times. Every table a live query reads
  has a primary key.
- Live queries read the dashboard's own tables, never Archon's `provider_event` rows.
- A live panel's speed is judged on the app's own work (owner decision, #13/#14, revised on #137):
  its query's `EXPLAIN ANALYZE` execution under 100 ms on the seed, and its rows on screen within
  500 ms of the first snapshot arriving (decode and render). Everything between the subscribe and
  that first snapshot is Neon's (connection, first-subscribe warm-up, delivery) and is judged only
  by Realtime `ready` within 2000 ms of navigation. Never show rows that did not come from a
  delivered subscription (no `initialData`), so a panel reads `ready` only when it is live.
- Nothing writes to Archon's tables. Triggers on them catch every error into `projection_errors`.
- Background repairs of the dashboard's own tables run as `reconcile:laps` / `reconcile` on the
  owner's schedule (every 10 minutes on the reference install), never by the app server or the
  webhook.
- Never connect to the `main` database branch from a check, a test or a lap. Use a `check-*` branch
  (`bun run fixture:branch`). `scripts/` refuses any other branch name for writes.
- Configuration by environment only: `MC_DATABASE_URL`, `NEON_REALTIME_SECRET`, `NEON_API_KEY`,
  `NEON_PROJECT_ID`, and optionally `MC_FACTORIES_FILE` (a factories file served instead of
  `factories.json`; checks use it to add a fixture-only factory, a real install leaves it unset).
  Never `DATABASE_URL`. Never commit a secret; `.mc-check.env` is gitignored.
- Serve on `127.0.0.1:<port>`, open as `http://localhost:<port>`, ports 8850-8864 only.
- Holdout scenario text never enters the dashboard's tables or screens: ids and verdicts only.
- Design: dark only, Geist for text and Geist Mono for data. Copy the components from
  `docs/design/archon-console/`. Colors live in one place: the tokens in `index.css` and
  `theme.css` there, copied identically into `app/styles.css` (`styles.test.ts` holds the copy,
  and the design probe fails any rendered color outside them). Change a color by changing its
  token, never inline. The surfaces are the near-black neutral console (cool charcoal, hue 265:
  page `--background`, then `--surface`, `--surface-elevated` and `--surface-hover` for the header,
  cards, panels and graph nodes), with no gradient and no blue tint on any surface. Dynamous Blue
  `#3B82F6` is the one accent (owner decisions #240 and 2026-10-28, "just some blue"): the active
  tab, the selection ring and focus; Dynamous Dark `#2563EB` for hover, Dynamous Light `#60A5FA`
  for link text. Text meets WCAG AA (4.5:1) on every surface. Status colors stay distinct from
  the accent: running is Dynamous Light and always pulses or glows; teal success, amber waiting,
  red failed (the brand's `#047857`, `#B45309` and `#B91C1C` are the `--*-strong` tokens).
  Magenta is not used. Data in Geist Mono with tabular
  numbers; section labels mono, uppercase, tracked. Empty states are one sentence and at most one
  button.
- Use a table only for a list of records a person scans row by row (recent laps, scorecard
  comparison, decisions ledger). Counts, distributions, status across many items and progress are
  drawn: bars, grids, tiles, graphs (owner decision, #241). A drawn section keeps every number and
  link the table had, as text beside the drawing, and its live updates.
- Tests sit next to the code they test (`*.test.ts`). Parsers are tested on the literal examples in
  the PRD's appendix and on `fixtures/pack/`.
- Stop every process you start by its process id; never kill by name.

## Deploying the webhook Function

- `bun run function:deploy -- --branch <check-*|main>` bundles `function/index.ts` with neonctl
  (pinned in devDependencies), deploys it as the Neon Function `mcwebhook` (runtime nodejs24) on
  that branch, and prints its URL. It needs `NEON_API_KEY`, `NEON_PROJECT_ID` and
  `GITHUB_WEBHOOK_SECRET`; `GITHUB_TOKEN` is optional and only raises GitHub's rate limit. It sets
  the Function's `MC_DATABASE_URL` to that branch's pooled connection string, so the Function
  writes only the branch it runs on. It refuses every branch but `check-*` and `main`; `main` is
  the owner's step after merge (PRD 11.3). It prints no secret, though they sit in neonctl's
  arguments while it runs.
- `bun run function:deploy -- --branch <branch> --delete` removes it. A check that deploys deletes
  its Function before `fixture:drop`.
- `function/index.ts` is the deployed entry (Node, `pg`); `function/dev.ts` is the local one (Bun).
  Both serve `createWebhookApp`.
- Registering the webhook (the owner, once per repository, after deploying to `main`): in GitHub,
  Settings, Webhooks, Add webhook, on each repository in `factories.json` and on
  `coleam00/ai-software-factory`, whose pushes carry pins, verdicts and `DECISIONS.md`. Payload
  URL: the printed URL. Content type: `application/json`. Secret: the `GITHUB_WEBHOOK_SECRET` the
  deploy used. SSL verification on. Events, under "Let me select individual events": Issues, Issue
  comments, Pull requests, Pushes, Labels. "Recent Deliveries" shows each answer: 200 recorded,
  401 the secret differs, 400 the content type is not JSON.

See [factory workflow policy](factory/WORKFLOW_POLICY.md) for factory-specific shared-workflow requirements.


### docs/factory-map.md

# Viewing the factory map

The selected factory needs at least one recorded lap before its map shows steps, even when
shared pinned architecture is already stored. A completed lap counts; no lap needs to be running.
This matches the versions screen's empty-factory rule and does not make pins factory-specific.

To follow the “See the factory” journey, select a factory with recorded laps and stored pinned
architecture, then open check-app from its map to read the prompt, holdout verifier and fence.
A factory with no laps instead shows “No factory map is available yet.” with no step links.
The same sentence covers missing architecture; it does not diagnose which prerequisite is absent.

The map updates live when the first lap arrives or the last lap is removed. Populated factories
keep their existing step details and per-factory counts.

The map draws every step a lap can run. Each include or loop group is a dashed box with the
including step at its top and the steps it expands inside, at every depth: ship holds deliver,
deliver holds rounds, and rounds holds implement, whose box holds its own implement step. A nested
step opens its own screen under the workflow that declares it: `ship/deliver/rounds/implement/implement`
opens `/steps/archon-implement/implement`. A lap on a nested step counts on that step and on every
box around it. The inputs archon-backlog and archon-holdouts and the manager archon-manager show
their own steps the same way, each counting that workflow's running runs. On a phone the loop's
spine stays in the first column, and a box wider than the screen scrolls sideways inside the map.

An include's own screen, such as deliver's, lists every step beneath it by its path there
(`rounds/implement/implement`, `rounds/reshape/implement`). Each entry opens that step's own
screen, which lists every place an include puts it and links back to each.

The Version control above the map lists every pin with recorded architecture, newest first, and
opens the map at an older one (`/?at=<pin>`). At that version each step opens its screen at the
same version, and the counts include only the running laps that ran it. Choosing the current
version removes `at`. A version that is not recorded for the factory reads “No version <pin> is
recorded for this factory.”


### docs/mission-control.prd.md

---
title: "Factory Mission Control - PRD v1"
type: prd
status: APPROVED for the first factory run (2026-10-24; Cole delegated sign-off; decisions in plans/factory-mission-control-2026-10-24.md section 9; reviewed by a subagent against them the same evening)
created: 2026-10-24
owner: Cole
product: Factory Mission Control, the live dashboard of the AI Software Factory
repository: coleam00/factory-mission-control (public)
tags: [prd, ai-software-factory, archon, neon, realtime, dashboard]
---

# Factory Mission Control - PRD v1

**What this is.** The product contract for a live dashboard of the AI Software Factory, built by
the factory itself. It shows the factory's architecture as one living map, how the factory has
evolved and why, and, for each application a factory is building, the product document, the
issues it was sliced into, every lap working through them, how each change was tested, and what
is waiting on the owner. Every panel is a live query: when an agent writes a row, the screen
changes, with no refresh.

**One deliberate judgement call, stated up front.** A PRD normally stays out of the stack. This one
does not (section 11), because the dashboard is a view onto systems that already exist (Archon's
run records, GitHub, the factory's pinned code, Neon Postgres with Realtime) and because it must
look like part of Archon. Leaving those open would let the factory reinvent them. Everything else
about how is the factory's.

---

## 1. The problem

The factory takes a product document in and ships merged pull requests out, several laps at a
time, while nobody watches. Its state is split across three places: Archon's run history, GitHub
(issues, labels, claim and review comments, pull requests) and the factory's own repository (the
pinned workflows, the decisions). To answer "what is it doing right now?", "where is it stuck?",
"is the change I made yesterday helping?" the owner flips between a terminal, a dozen GitHub tabs,
the Archon console and hand-written audit scripts. In October alone he rebuilt the same metrics by
hand at least six times (merges per hour, lap-hours per merge, app-check share of lap time, empty
laps, send-backs, cost per merge) to judge one change to the factory against the last.

The factory's architecture also changes every few days (a new step, a new gate, a new route), and
nothing shows what it is today, what each step does, or what each version cost and delivered.

## 2. Who it is for

1. **The factory owner** (Cole): runs several factories at once, changes the factory itself often,
   needs to see at a glance where each factory is, what is waiting on him, and whether a change to
   the factory helped.
2. **People learning the factory** (workshop and bootcamp members, video viewers): need to see the
   whole process, inputs to outputs, and click into any step to understand it.

## 3. The hypothesis, stated so it can be wrong

If every fact about the factory lands in one Postgres database and every panel is a live query,
the owner stops building audit scripts by hand: every factory change ships with a hypothesis and
gets judged from the dashboard within a day of laps, and an owner question waiting on him is seen
within minutes, not hours. It is wrong if, two weeks in, he is still writing throwaway metric
scripts, or still discovering stuck laps from a watchdog line.

## 4. In scope

### 4.1 Factory architecture: the home base (factory-agnostic)

The default screen. One map of the whole AI Software Factory process at the pinned version, from
inputs to outputs, laid out from the parsed workflows (section 11.4):

- **Inputs:** the product document; `archon-holdouts` (writing holdout scenarios); `archon-backlog`
  (slicing the product document into issues); the owner's decisions.
- **The loop:** every step of `archon-loop` in order (pick, claim, build, ship, subject, briefs,
  check-app, evidence, review, land, deploy, release), with ship expanded into the stages parsed
  from `archon-ship-block` and its includes.
- **The manager:** `archon-manager` above the loop.
- **Outputs:** merged pull requests, closed issues, deploys, owner questions, metrics lines.
- **Live:** each step shows, per factory, how many laps are on it now; a step with laps on it carries
  `data-live-count` greater than 0 and a running style.

Clicking a step opens its detail: its description; its inputs and outputs; the `when` condition
that routes a lap through it; its model tier; its workflow YAML; its prompt (the command file);
its inline subagents and their instruction files; the scripts it runs; and the hooks that apply
to it. For the holdout steps, the detail explains the fence: the hook file
(`.factory/hooks/holdout_fence.py` in the factory template), which agents it lets read the
scenarios, and how a verdict comes back. All of it comes from the pinned code, never typed in.

### 4.2 How the factory evolves

- **A version strip:** one entry per factory version, with its date, its pin commit's one-line
  reason, and its `Hypothesis` and `Measure` (section 11.5). A pin with no reason or trailers shows
  "not recorded".
- **A scorecard per version, per factory**, using exactly these definitions (one factory, laps whose
  run ran that version):

| Measure | Definition |
|---|---|
| lap | an `archon-loop` run |
| merge | a lap whose `land` step output has `outcome = merged` |
| empty lap | a lap whose `pick` output has `route = none` |
| failed lap | a lap whose run `status = failed` |
| send-back | a lap whose `review` output has `outcome = sent-back` |
| gate refusal | a lap whose `land` output has `outcome = refused`; its reason is the `reason` text |
| lap duration | run `completed_at` minus `started_at` |
| active hour | a UTC clock hour in which at least one lap was running |
| merges per active hour | merges / active hours |
| lap-hours per merge | sum of lap durations in hours / merges |
| app-check share | sum of `check-app` step `duration_ms` / sum of lap durations |
| cost per merge | sum of `cost_usd` of every step of every lap / merges |
| new holdout catch | an app-check line of kind `holdout` with verdict FAIL and empty `pre_existing` |

  Every number shows how many laps it rests on. Two versions can be compared side by side; a
  difference resting on fewer than 10 laps on either side is labelled "not yet meaningful".
- **Key decisions:** the entries of `DECISIONS.md` (section 11.5) on a timeline, each linked to the
  version its `Version:` line names.
- **Improvements being tested:** versions with a `Measure` and no verdict yet, and the laps each is
  still waiting for; versions with a verdict (helped, hurt, inconclusive) and its sentence.
- **Architecture diff:** for any two versions, which workflows, steps, prompts and subagents were
  added, removed or changed.

### 4.3 One factory: from product document to merged pull requests

Per factory (section 11.6):

- **Product document phases** with merged and total issues per phase.
- **The issue graph** from `Depends on: #n` lines, colored by state: waiting (open, no claim),
  claimed (a live `Loop claim`), pull request open, needs owner (label `needs-owner`), merged,
  closed. The longest open dependency chain is highlighted.
- **Lanes:** one row per running lap: the issue it claimed, its route and depth, the step it is
  on, when it entered that step (the browser shows elapsed time), its cost so far.
- **Recent laps:** every lap with its outcome (merged, sent back, gate refused, needs owner,
  nothing to do, failed), duration and cost.

### 4.4 The owner queue

Everything waiting on a person, per factory: open issues labeled `needs-owner`, and each open
question in the manager's `Owner decisions needed` issue with its options, recommendation, default
and the date the default applies, with how long each has waited. Each links to its GitHub thread,
where it is answered. v1 never answers anything itself.

### 4.5 Testing: how each change was checked

Per factory: the mix of routes and check depths; app-check lines by kind and verdict; holdout
verdicts by scenario id on the default branch (from the manager's `holdouts at` lines) and at
pull-request time (from app-check lines); scenarios failing on the default branch with their
tracking issues. Holdouts appear only by scenario id and verdict (invariant 3, section 11.7).

### 4.6 One lap

Every step the lap ran with start, duration, model, tokens and cost; its route and depth; the
app-check lines (kind, verdict, evidence count); the review outcome and dispositions; the merge
gate's outcome and reason; links to the pull request, the issue, and the run in the Archon console
(`<console>/console/r/<runId>`, section 11.6).

### 4.7 Rewind

Open the same dashboard on a Neon branch from a past moment (up to 7 days back): same screens,
same queries, older data, read-only. Rewind branches are created by the owner
(`bun run rewind:create <ISO time>`, which names them `rewind-<time>`); the dashboard lists them
and switches to one.

### 4.8 Health

Per factory: runs with status `pending`; runs with status `paused`; steps running longer than twice
that step's 90th-percentile `duration_ms` over its last 50 completions; failed laps by cause, from
the failing step's error text (`usage limit|429` = usage limit, `401|unauthor` = authentication,
`ECONN|ETIMEDOUT|fetch failed` = infrastructure, anything else = other); and workable issues (open,
no `needs-owner`, every `Depends on` closed, no live claim) against running laps.

## 5. Out of scope, forever

- Writing to GitHub, Archon or any factory from the dashboard in v1: no answering, approving,
  halting, launching or merging.
- Rebuilding Archon's run log viewer. One lap links to the Archon console for the full stream.
- Anything that requires changing the Archon engine or Archon's database schema.
- User accounts, sharing, or hosting the dashboard UI outside the owner's machine in v1. (The
  webhook receiver is a Neon Function, hosted by Neon, by decision.)
- Copying any holdout scenario text into the dashboard's own tables or screens.

## 6. Hard invariants

1. **Never slows or breaks Archon.** Anything the dashboard adds to the database (tables, triggers,
   views) can never make an Archon write fail or wait. A trigger catches its own errors and counts
   them in a table; it never raises. Triggers on Archon's tables fire only for step-level events
   (section 11.4).
2. **Read-only toward the factories.** Nothing the dashboard runs writes to GitHub, to a factory's
   repository, or to Archon's tables.
3. **Holdouts stay hidden.** The dashboard's own tables and screens hold a holdout's scenario id and
   verdict only, never a line's or a scenario's text. Archon's rows are read, never copied.
4. **Every number can be traced.** Each metric names the laps or rows it was computed from, and how
   many.
5. **Live means live.** Every panel is a Neon Realtime live query or derived from one. No polling
   and no refresh button.
6. **The architecture is the code.** The map, prompts and step details come from the pinned code at
   that version, parsed by a job, never typed in.
7. **Secrets never reach the browser.** The browser gets sealed live queries only; the Realtime
   secret, database URLs, the Neon API key and GitHub tokens stay on the server and in the Function.
8. **The `main` database branch is the owner's.** Laps and checks never migrate, seed, write to or
   delete `main`; Archon writes there. Checks run on their own branches (section 11.3).

## 7. The observable core journeys

1. **See the factory.** Open the dashboard: the architecture map at the current version, with live
   lap counts on the steps; open check-app and read its prompt, its holdout verifier and how the
   fence works.
2. **Watch a lap.** While a lap runs, its lane moves from step to step without a reload; when it
   merges, its issue turns merged and its phase bar fills.
3. **Judge a change.** Pick two versions on the strip and compare their scorecards and the
   architecture diff between them.
4. **Find what waits on me.** The owner queue lists every open owner question with its default date;
   a newly labelled `needs-owner` issue appears without a reload.
5. **Rewind.** Switch to a rewind branch and see the older version and its laps.

## 8. What "validated" means

### 8.1 Live

A row inserted into a source table (a step event, an issue, a comment) appears in every panel that
shows it within 5 seconds, with no reload. A panel left open for 3 minutes (three seal renewals)
still updates.

### 8.2 Correct

On the seed data (section 11.3), every scorecard number equals `fixtures/expected-scorecard.json`
exactly. That file is written by the seed issue, from the definitions in 4.2, not by the panel
issue. The version strip equals the pin commits in the seed. The issue graph equals the seed
issues' `Depends on` lines.

### 8.3 Design contract

The dashboard is part of Archon to the eye: the Archon console's theme tokens, fonts (Geist, Geist
Mono), status colors (blue running, teal success, amber waiting, red failed, magenta only for
identity) and component shapes, copied from `docs/design/archon-console/`. Dark only. On every
change that touches the frontend, `harness/design-probe.js` (written by the skeleton issue) reports
zero failures: only token colors and fonts, no browser-default controls, text contrast at least
4.5:1, no horizontal overflow at 1440 and 390 px, every control with an accessible name. A screenshot
of each touched screen is compared with the console references in `docs/design/archon-console/`
and the judgement quoted.

### 8.4 Fast

On the seed data, every home-screen panel shows `data-state="ready"` within 2 seconds of opening,
and no live query takes more than 500 ms to deliver its first snapshot.

### 8.5 What the checks cannot see, and who owns it

Whether the architecture map explains the factory well to a newcomer, and whether the scorecard's
measures are the right ones, are owner calls (product direction).

## 9. Success metrics

- In the two weeks after launch, the owner writes no throwaway metric script to judge a factory
  change.
- Every pin to the factory after launch carries `Hypothesis` and `Measure`, and gets a verdict.
- An owner question is seen within 10 minutes of being raised.

## 10. Owner decisions and open questions

- **Who decides:** Claude acts as owner for this factory's technical and small calls, each recorded
  with a reason. Product direction, scope, and look and feel wait for Cole, collected in one list a
  day.
- **Open:** how the scorecard should compare factories with very different apps (a GPU game and a
  web app). v1 shows each factory separately and never sums across them.

## 11. Decided stack and the runtime contract

### 11.1 Stack (decided)

- **Frontend:** React 19, Vite 6, Tailwind CSS v4 (`@theme inline` tokens), react-router 7 with one
  route file per screen registered from a directory (so screen issues never edit a shared router),
  hand-written components, lucide icons sparingly, dagre for graph layout. Copy the console tokens
  and components from `docs/design/archon-console/` rather than inventing new ones.
- **Live data:** Neon Realtime. Each panel is one `useLiveQuery` (`@neon/realtime-react`) on a
  sealed query (`createRealtime` and `seal` from `@neon/realtime/server`). Queries are read-only,
  deterministic single SELECTs: no `now()` (return timestamps; the browser does clock math). Until
  the database issue's spike proves which features Realtime accepts (CTE, LATERAL, DISTINCT ON,
  window functions), live queries are plain SELECTs with joins and aggregates, and the browser
  combines step-level rows.
- **Server:** one Bun + Hono process that serves the built app and seals queries (sealed queries
  expire every 60 seconds; the client renews through it). It holds the Realtime secret and the
  database URL.
- **Database:** Neon project `bold-mouse-41160836` ("factory-mission-control", aws us-east-1,
  Postgres 18), Realtime enabled, logical replication on, 7-day history. Every table a live query
  reads has a primary key.
- **Ingestion:** a Neon Function (Hono, TypeScript) receives GitHub webhooks (issues, issue comments,
  labels, pull requests, pushes) and upserts rows. A nightly reconcile reads the GitHub API. A
  backfill script loads history.
- **Tooling:** Bun 1.4 (`bun test`, `bun run`), TypeScript strict, Biome for lint and format.

### 11.2 Where each fact comes from

| Fact | Source | Path into the database |
|---|---|---|
| Laps, steps, timings, cost, model, route, depth, app-check lines, review outcome, merge-gate outcome | Archon's `remote_agent_workflow_runs` and `remote_agent_workflow_events` (`node_completed` rows carry the step's `structured_output`, `cost_usd`, `tokens`, `duration_ms`, `provider`, `model`; the step id is `step_name`) | Archon writes them (its `DATABASE_URL` is this project's `main`); triggers project step-level rows into the dashboard's tables |
| Which version a lap ran | the run's `metadata.workflow_source.digest` (a hash of the exact workflow pack it ran) | as above; versions are keyed by (factory, digest) and labelled with the most recent pin committed before the first run with that digest |
| Issues, labels, `Depends on`, PRD phase, claims, reviews, owner decisions, `Loop metrics` and `holdouts at` lines, pull requests | GitHub | webhook into the Neon Function; nightly reconcile; backfill |
| Versions, reasons, `Hypothesis`, `Measure`, verdicts | commits on `coleam00/ai-software-factory` | push webhook (section 11.5) |
| Key decisions | `DECISIONS.md` in `coleam00/ai-software-factory` | push webhook |
| Architecture | the pack at the pinned Archon commit (`.archon/workflows/sdlc/` in `coleam00/Archon`) and the factory template (`template/` in ai-software-factory) | the architecture job (11.4) |

Archon's `provider_event` rows (about 30 per step) are never read by a live query.

### 11.3 Runtime contract (what the factory drives)

- **`bun install`**, then **`bun run setup`**: installs and builds. Idempotent, non-interactive,
  works on Windows (Git Bash) and Linux.
- **`bun run serve -- --port <port>`**: serves the built app and the sealing API on
  `127.0.0.1:<port>` in the foreground until killed. The browser opens it as
  `http://localhost:<port>`: the only browser origins Realtime allows are `http://localhost:5173`
  (Vite dev) and `http://localhost:8850` through `8864`, so every app instance (each lap's, the
  holdout verifier's, CI's) uses a free port in 8850-8864.
- **Check branches.** A check never touches `main` (invariant 8). `bun run fixture:branch` creates
  a Neon branch `check-<id>` from the branch `fixture` (owner-made from `main`, holding Archon's
  schema and no app data), applies the repository's migrations, loads `fixtures/seed.sql` (rows for
  every dashboard table and a realistic set of Archon runs and events), writes the branch's
  connection string and Realtime secret to `.mc-check.env` (gitignored), which `serve` reads.
  `bun run fixture:drop` deletes that branch, and any `check-*` branch older than 3 hours. Both
  refuse to act on any branch not named `check-*`. `bun run fixture:write <kind>` inserts one
  realistic row of a kind (a step event, a label, a comment) into the check branch, to prove
  liveness. Migrations refuse a branch named `main`; only the owner runs `bun run migrate:main`.
- **Credentials** come from the environment the factory's launcher sets (worktrees carry no
  gitignored files): `NEON_API_KEY` (scoped to this project only), `NEON_PROJECT_ID`, and `gh`'s
  login for GitHub. The app itself reads `MC_DATABASE_URL` and `NEON_REALTIME_SECRET` (never
  `DATABASE_URL`, which Archon on this machine uses).
- **The Neon Function.** Laps build and test the webhook handler locally (`bun run function:dev`,
  with signed sample payloads in `fixtures/webhooks/`, verified with `GITHUB_WEBHOOK_SECRET=test`).
  A lap may deploy it (`bun run function:deploy`) to its own check branch to prove the deployed
  Function, and deletes it when the check ends (owner decision, #56). Deploying to `main` and
  registering webhooks are owner steps after merge.
- `GET /api/health` returns 200 once the app can serve; `GET /api/build-id` returns the git commit.
- **Checks:** `bun run check` (type-check, lint, unit tests, no network) and `bun run test:live`
  (the liveness checks against a check branch). CI runs `bun run check` on every pull request.

### 11.4 The architecture job and the Archon projection

- **Architecture job** (`bun run arch:parse <archon-sha> <factory-sha>`): reads the pack at that
  Archon commit and the factory template at that factory commit (from GitHub, or from a local
  path), and stores, per version: workflows, steps (id, kind, description, model tier, `when`,
  `depends_on`, `trigger_rule`, includes, inline subagents), edges, the workflow YAML, command and
  instruction text, and scripts. Includes are expanded the way Archon expands them. Its tests run
  on the committed pack snapshot in `fixtures/pack/` (no network).
- **Projection:** triggers on `remote_agent_workflow_events` declared
  `WHEN (NEW.event_type IN ('node_started','node_completed','node_failed','node_skipped'))` and on
  `remote_agent_workflow_runs` project into the dashboard's step and lap tables (step id from
  `step_name`; outputs from `data->'structured_output'`). Each trigger body catches every error and
  records it in a `projection_errors` table instead of raising.

### 11.5 Versions, verdicts and decisions

Every pin commit on ai-software-factory (`Pin Archon <sha>: <reason>`) carries two trailers:

```
Hypothesis: <what should change in the factory's behaviour>
Measure: <which scorecard measure, which direction, how many laps>
```

A verdict is a later commit on ai-software-factory with the trailer
`Verdict: <pin sha> helped|hurt|inconclusive: <one sentence>`. `DECISIONS.md` entries have the fixed
shape `## YYYY-MM-DD Title`, `Decision:`, `Why:`, `Replaces:`, `Version:`; `Version:` joins to a pin
by sha prefix.

### 11.6 Factories

`factories.json` (committed) lists each factory: name, GitHub repository, the Archon codebase name
its runs carry, and its Archon console URL. At launch only mission control's own runs are in this
database; North Star and DynaChat join when the owner moves their Archon data in. Every view is
keyed by factory and must work with exactly one.

### 11.7 Holdout ids

Scenario ids in `.factory/holdout/HOLDOUT.md` follow `H-<nn>` (for example `H-07`). The app check's
line `id` is a line number; the scenario id is the first `H-<nn>` in the line's text, which the
projection extracts and stores alone. A holdout line with no such id shows as `unidentified`.

## 12. Build order for the first run

Slice with `max_issues` 25. Three laps run at once: after the first items, most items depend only on
the seed, not on each other. Ingestion feeds the same tables the panels read, but no panel waits for
it: panels build against the seed.

1. **Skeleton:** the app serves per 11.3 with health and build-id; console tokens and base components
   from `docs/design/archon-console/`; one-route-file-per-screen routing; `harness/design-probe.js`;
   `bun run check`; CI.
2. **Check branches:** `fixture:branch`, `fixture:drop`, `fixture:write`, migrations runner refusing
   `main`, with an empty migration set.
3. **Schema and seed:** every dashboard table (GitHub mirror, versions, decisions, architecture, laps,
   steps, holdout verdicts, projection errors) with primary keys; `fixtures/seed.sql`;
   `fixtures/expected-scorecard.json`.
4. **Realtime spike and sealing API:** one live panel end to end on a check branch; records which SQL
   features Realtime accepted.
5. **Archon projection triggers** (deep check: invariant 1).
6. **Comment parsers:** claims, reviews, owner decisions, metrics and holdout lines, pin trailers,
   DECISIONS.md, as pure functions with unit tests on the examples in the appendix.
7. **Webhook Function handler** and **8. backfill and nightly reconcile** (both use 6).
9. **Architecture job** and **10. the home-base map with step detail** (10 uses 9).
11. **Version strip**, **12. scorecard and comparison**, **13. decisions timeline and improvements
    ledger**, **14. architecture diff** (14 uses 9).
15. **Phases and issue graph**, **16. lanes and recent laps**.
17. **Owner queue**, **18. testing panel**.
19. **One lap**, **20. rewind**.
21. **Health**.

## 13. Provenance

Written 2026-10-24 by Claude for Cole from: a read-only study of the Archon pack on
`factory/sdlc-on-dev`, the ai-software-factory repository, the vault's factory plans and run logs
since September, the 2026-10-24 holdout audit, the Archon console source (`packages/web`), Neon's
Realtime documentation, Cole's answers on 2026-10-24, and a review of the first draft against them.

## Appendix: the formats the parsers read

Literal examples (ids and numbers invented):

```
Loop claim: run 4f1c2a9e-7b3d-4e8a-9c21-5d6e7f8a9b0c
Route: simple
Area: app/routes/lanes.tsx
```

```
Loop claim released: run 4f1c2a9e-7b3d-4e8a-9c21-5d6e7f8a9b0c ended. Its `Loop review:` comment, if any, says what it did.
```

```
Loop review: merged (route: simple) at 9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c by the merge gate, after the review above.
Loop review: not merged (route: complex). The merge gate refused the reviewer's merge:

- it changes .claude/settings.json, which only the owner changes; the owner merges it by hand if it is intended

The next lap continues this pull request.
Loop review: sent back (route: continue)
```

`Loop metrics` issue body, one line per manager pass:

```
2026-10-25T14:20Z | merged since last pass: 4 (simple 2, complex 1, continue 1) | open PRs: 2 | loop send-backs since last pass: 1 | merge-gate refusals: 0 | ship correction rounds: 2 | needs-owner open: 1 | owner questions open: 2 | default branch checks: green (CI) | laps since last pass: 9 (empty 2, failed 0) | health actions: 1
2026-10-25T14:20Z | holdouts at 3e4f5a6b: H-01 PASS, H-02 FAIL #41, H-03 INCOMPLETE #42
```

`Owner decisions needed` issue, one section per question:

```
### Q3. Should the lanes panel show finished laps for an hour?
Options: A) yes, faded; B) no, only running laps.
Recommendation: A, so a merge that just happened is still visible.
If there is no answer by 2026-10-27 14:00 UTC, the loop will use A.
```

A pin commit and a verdict on ai-software-factory:

```
Pin Archon abd85896: holdouts fenced in the repository; the complex route runs dev's ship-block

Hypothesis: complex laps finish faster and are sent back less.
Measure: complex-route lap-hours per merge and send-backs per merge, over at least 10 complex laps.
```

```
Record the verdict on abd85896

Verdict: abd85896 helped: complex laps took 1.4 lap-hours per merge against 2.6, over 12 laps.
```


### FACTORY.md

# Factory operations

This application runs on a pinned Archon SDLC source. See
[factory/MIGRATION.md](factory/MIGRATION.md) for installing and upgrading it.

Shared workflow gates own every decision. Inspect a run's identity and status
before responding to a declared gate.

Project runtime scenarios: `harness/END-TO-END.md`.
Holdout scenarios: `.factory/holdout/HOLDOUT.md`, fenced by `.factory/hooks/holdout_fence.py`
(only the holdout-writer and holdout-verifier subagents may read it).
Ordinary checks: `python harness/ci.py`.

Record this application's tested source SHA, candidate, run IDs, coverage,
fresh-environment evidence and open integration limits here after testing.


### FACTORY_RULES.md

# Project workflow guidance

Keep project constraints and irreversible-action requirements in this file and the
native project guidance. Shared workflow gates own authorization. The factory does
not interpret this document as a private merge policy.

Preserve scope, tests, security invariants and secrets. Report failed or unavailable
checks truthfully. Ordinary static/unit success does not replace required runtime
or holdout verification. Each required assertion needs observable evidence.

Specify this application's protected paths, required validation coverage and
publication constraints in the shared workflow's supported inputs.

**Irreversible actions stop the factory.** Changing identity, authentication or who
may act as whom, and migrating or deleting stored data, are never decided by an
agent: an issue that needs one is held for a human.


### package.json

```json
{
  "name": "factory-mission-control",
  "private": true,
  "type": "module",
  "scripts": {
    "setup": "vite build",
    "serve": "bun server/main.ts",
    "check": "tsc --noEmit && biome check && bun test --timeout 60000 app server harness scripts parsers db function",
    "function:dev": "bun function/dev.ts",
    "function:deploy": "bun scripts/function-deploy.ts",
    "function:idle-check": "bun scripts/idle-check.ts",
    "migrate": "bun scripts/migrate.ts",
    "migrate:main": "bun scripts/migrate.ts --main",
    "arch:parse": "bun scripts/arch-parse.ts",
    "arch:parse:main": "bun scripts/arch-parse.ts --main",
    "backfill": "bun scripts/backfill.ts",
    "backfill:main": "bun scripts/backfill.ts --main",
    "reconcile": "bun scripts/backfill.ts --reconcile",
    "reconcile:main": "bun scripts/backfill.ts --reconcile --main",
    "reconcile:laps": "bun scripts/reconcile-laps.ts",
    "reconcile:laps:main": "bun scripts/reconcile-laps.ts --main",
    "rewind:create": "bun scripts/rewind-create.ts",
    "fixture:branch": "bun scripts/fixture/branch.ts",
    "fixture:drop": "bun scripts/fixture/drop.ts",
    "fixture:write": "bun scripts/fixture/write.ts",
    "fixture:seed": "bun scripts/fixture/seed.ts",
    "fixture:verify": "bun scripts/fixture/verify.ts",
    "projection:locks": "bun scripts/projection-locks.ts",
    "test:live": "bun scripts/test-live.ts"
  },
  "dependencies": {
    "@dagrejs/dagre": "^3.1.3",
    "@fontsource/geist": "^5.3.0",
    "@fontsource/geist-mono": "^5.3.0",
    "@neon/functions": "^0.11.0",
    "@neon/realtime": "0.1.2",
    "@neon/realtime-react": "0.1.1",
    "hono": "^4.13.13",
    "pg": "^8.23.1",
    "react": "^19.3.1",
    "react-dom": "^19.3.1",
    "react-router": "^7"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.6.3",
    "@electric-sql/pglite": "^0.5.11",
    "@electric-sql/pglite-socket": "0.2.14",
    "@tailwindcss/vite": "^4",
    "@types/bun": "^1.4.4",
    "@types/pg": "^8.23.1",
    "@types/react": "^19.3.0",
    "@types/react-dom": "^19.3.0",
    "@vitejs/plugin-react": "^5",
    "neonctl": "8.11.3",
    "tailwindcss": "^4",
    "typescript": "^7.0.2",
    "vite": "^6"
  }
}

```

### factories.json

```json
{
  "factories": [
    {
      "name": "mission-control",
      "repository": "coleam00/factory-mission-control",
      "codebase": "coleam00/factory-mission-control",
      "console": "http://localhost:3090"
    },
    {
      "name": "north-star",
      "repository": "coleam00/north-star-godot",
      "codebase": "coleam00/north-star-godot",
      "console": "http://localhost:3090"
    }
  ]
}

```

## Top-level structure
- `app/` — React 19 + Vite 6 + Tailwind v4 browser app. One route file per screen under `app/routes/`.
- `server/` — Bun + Hono: serves the built app, `/api/health`, `/api/build-id`, and seals Neon Realtime queries. Live sync, factory list, rewind.
- `db/` — numbered SQL migrations, live queries (one file per panel), projection tests. Migrations on `main` are owner-only.
- `function/` — Neon Function (Hono, TypeScript) that receives GitHub webhooks.
- `parsers/` — pure parsers for comment formats, pin trailers, `DECISIONS.md`, and the architecture map.
- `scripts/` — migrate, backfill, reconcile, architecture parse, fixture branches, webhook deploy, rewind.
- `fixtures/` — seed SQL, expected scorecard, sample webhooks, pinned pack snapshot, factory-template fence files.
- `harness/` — design probe and factory harness config.
- `docs/` — PRD (`mission-control.prd.md`), factory-map notes, `design/archon-console/` (copied Archon console tokens), `evidence/` for issues 89, 95, and 105.
- `factory/` — installed AI Software Factory consumer (this repo is itself built by the factory).
- `.factory/` — holdout and hooks. `.claude/settings.json` registers the holdout fence.
- `MISSION.md`, `FACTORY.md`, `FACTORY_RULES.md`, `engineering.md` — factory governance. `factories.json` lists factories the dashboard shows (mission-control and north-star at fetch time).
- `.github/` — CI boilerplate, not fetched.
