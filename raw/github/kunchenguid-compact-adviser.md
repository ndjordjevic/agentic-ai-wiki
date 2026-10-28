# kunchenguid/compact-adviser

## Metadata
- Stars: 224
- Primary language: TypeScript
- Default branch: main
- Latest release: compact-adviser-v0.1.14
- License: MIT License
- Homepage: https://github.com/kunchenguid/compact-adviser
- Fetched: 2026-10-28
- Final URL: https://github.com/kunchenguid/compact-adviser

## Description
"Work appears completed or recorded. Run /compact to save tokens."

## README
<h1 align="center">compact-adviser</h1>

<p align="center">
  <a href="LICENSE"
    ><img
      alt="License"
      src="https://img.shields.io/badge/license-MIT-green?style=flat-square"
  /></a>
  <a
    href="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square"
    ><img
      alt="Platform"
      src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square"
  /></a>
  <a href="https://x.com/kunchenguid"
    ><img
      alt="X"
      src="https://img.shields.io/badge/X-@kunchenguid-black?style=flat-square"
  /></a>
  <a href="https://discord.gg/Wsy2NpnZDu"
    ><img
      alt="Discord"
      src="https://img.shields.io/discord/1439901831038763092?style=flat-square&label=discord"
  /></a>
</p>

**compact-adviser** is an agent plugin that answers a single question: should I /compact now?

![Compact adviser status line: "Compact adviser: work appears completed or recorded. Run /compact to save tokens." shown above a terminal prompt](docs/hint-status-line.png)

It uses [Jev](https://typesafe.ai) to instantly judge whether the current session is likely at a boundary that's safe to compact.

It can give you a hint to run `/compact` - or, on Pi and Claude Code, if you opt in, it can run it for you at the right time automatically. Codex CLI and Grok are hint-only: nothing outside their sessions can trigger `/compact`.

Judgment is two one-sentence Jev questions in one request (is the unit finished; is this hands-on work or coordination), composed in code into one score. The hint floor is 0.90 while the context is mostly empty (through about 10%) and relaxes toward 0.50 by about 90% full - a wrong hint costs most when there is still room. "Full" means the point where the host compacts: on Claude Code that is its auto-compact threshold when enabled, elsewhere the model's window. If you would rather compact well before that (long contexts cost more every turn), set a context budget: the floor then relaxes as the context approaches the smaller of your budget and that point. Automatic mode is the same gate, plus a first-use confirmation.

## Quick Start

Prerequisites: Node 22+ (22.18+ for Codex and Grok), and one of [Pi](https://pi.dev) 0.82.0 or newer (verified on **0.85.1**), Claude Code 2.1.274 or newer (verified on **2.1.275**), Codex CLI 0.153.0 or newer (verified on **0.153.4**), or [Grok Build](https://docs.x.ai/build/overview) 1.0.34 or newer (verified on **1.0.34**), plus a [TypeSafe API key](https://console.typesafe.ai/settings/keys). Supply it as `TYPESAFE_API_KEY` in the launch environment or put it in the session cwd's `./.env`; Pi and Claude Code can also save it through their settings, while Codex and Grok provide an external compact-adviser CLI. Jev is TypeSafe's structured decision model; this package asks it two one-sentence classification questions and never asks it to write a summary.

Installing the package is consent to send eligible checkpoint context to TypeSafe when a key is available and the other product gates pass. With `TYPESAFE_BASE` set, that context and the key go to that base instead.

### Pi

```sh
pi install npm:compact-adviser
```

Restart Pi or run `/reload`, then `/compact-adviser`.
`/compact-adviser status` should say `Key: env`, `Key: saved`, or `Key: .env`.

To install from git: `pi install git:github.com/kunchenguid/compact-adviser` (add `-l` for project-local).

### Claude Code

This plugin uses Claude Mod which is an experimental feature that requires `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` in your environment.

```sh
claude plugin marketplace add kunchenguid/compact-adviser
claude plugin install compact-adviser@compact-adviser
CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude
```

Then `/compact-adviser`.

### Codex CLI

Codex support is **macOS and Linux only**. The plugin's hooks run through POSIX `sh`, matching
this repository's platform badge; Windows is not supported this ship.

```sh
codex plugin marketplace add kunchenguid/compact-adviser
codex plugin add compact-adviser@compact-adviser
```

Restart Codex and review the hook in `/hooks` once, so it is trusted. After a completed
checkpoint the advice appears as a `↳ Hook · Compact adviser: ...` line under the answer.

Codex is **hint-only**: it has no surface that lets another process run `/compact`, so there is
no automatic mode there. Settings live in a small CLI instead of a slash command; ask Codex for
"compact-adviser status" and the bundled skill runs it, or run it yourself:

```sh
node "$(ls -d "${CODEX_HOME:-$HOME/.codex}"/plugins/cache/*/compact-adviser/*/ | tail -1)src/cli.ts" status
```

### Grok Build

Grok is **hint-only**: nothing outside a running session can trigger `/compact`, so there is no automatic mode here. The hint is painted on the status row and never enters the model's context.

```sh
grok plugin install kunchenguid/compact-adviser#packages/grok-plugin --trust
```

(Install from the subdirectory, not the repository root: Grok also reads the Claude marketplace index in this repo, so a plain `grok plugin marketplace add` offers two plugins of the same name and refuses an unqualified install.)

Then two one-time steps, because Grok does not let a plugin do either of them for you. Start Grok and run:

```
/compact-adviser-install
```

That writes `${GROK_HOME:-~/.grok}/hooks/compact-adviser.json`, because **Grok 1.0.34 lists a plugin's own `hooks/hooks.json` but never loads it into a session**. Hooks in your own Grok home are always trusted, so nothing else is needed; delete that file to remove them. From a shell it is `node "$(node -e 'const l=JSON.parse(require("child_process").execFileSync("grok",["plugin","list","--json"],{encoding:"utf8"})); const p=(Array.isArray(l)?l:[]).find(x=>x&&x.name==="compact-adviser"); if(!p||typeof p.path!=="string") throw new Error("compact-adviser is not installed"); process.stdout.write(p.path)')/bin/adviser.ts" install`. After `install`, `${GROK_HOME:-~/.grok}/compact-adviser/adviser.sh` resolves the currently installed plugin the same way.

Then paste the `[ui.status_line]` block `install` printed into the config.toml path it named and restart Grok. The status row is off by default and only your own config can turn it on - a plugin cannot, and neither can a repository. Grok has one status row, so this script paints the built-in segments (`cwd`, `model`, `context`) too. Minimal render mode has no status row at all.

On Grok, save the TypeSafe key as `TYPESAFE_API_KEY` or a cwd `.env`, or with the CLI `key` command from a shell outside Grok. Do not type secrets after a Grok slash command; Grok appends those words to the model.

## If it does nothing

| Symptom | Cause |
| --- | --- |
| TypeSafe requires payment (HTTP 402) | Check the TypeSafe account's billing and credits; waiting alone will not resolve a payment requirement. Context stays unchanged. |
| `Key: missing` in `/compact-adviser status` (Pi, Claude Code) or `/compact-adviser` (Grok) | No `TYPESAFE_API_KEY` in the launch environment, saved settings, or the session cwd's `./.env` |
| No `/compact-adviser` command in Claude Code | `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` is not exactly `1` |
| Command exists, no hint | Context is below the constant 40,000-token minimum, the session is not idle, or the last turn was not a settled final answer |
| Claude Code: "nonessential traffic" | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` blocks plugin network requests |
| No hint in Codex | The hook is untrusted (review it in `/hooks`), Node is older than 22.18, or the hook cannot find Node at all - Codex rebuilds its PATH, so set `COMPACT_ADVISER_NODE` to an absolute `node` path |
| Grok: no hint row at all | `[ui.status_line]` is not set in the `config.toml` `install` named, or Grok is in minimal render mode |
| Grok: no hint after a completed turn | `/compact-adviser-install` has not run, so no Stop hook is judging |
| Pi print / RPC / JSON, Claude `-p`, or `codex exec` | The adviser stays inert in reliably detected non-interactive sessions |
| Nothing at all, in any host | `COMPACT_ADVISER_DISABLE` is set to a truthy value |

## Environment variables

| Variable | Effect |
| --- | --- |
| `TYPESAFE_API_KEY` | The Jev key; a saved key or the session cwd's `./.env` is used when this is unset |
| `TYPESAFE_BASE` | Replaces the TypeSafe API base URL, `https://api.typesafe.ai` by default; the request goes to `<base>/v1/systemone` with a trailing slash dropped. Read from the launch environment only, never a saved setting or `./.env`. It must be an `https` URL; plain `http` is accepted only for a loopback host (`127.0.0.1`, `[::1]`, `localhost`). Any other value, or one that carries credentials, a query or a fragment, is a configuration error: no request and no advice |
| `COMPACT_ADVISER_DISABLE` | `1`, `true`, `yes` or `on` (any case) makes the session inert: no TypeSafe request, no hint, no automatic compaction, no command. It wins over a saved `hint` or `auto` mode |
| `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` | Claude Code only; must be exactly `1` for the mod to load |
| `COMPACT_ADVISER_NODE` | Codex only; absolute path to a Node 22.18 or newer executable when the hook cannot find one on its rebuilt PATH |

Export `COMPACT_ADVISER_DISABLE=1` for unattended agent sessions, where advice has nobody to read it.

## What is sent to TypeSafe

| Included | Not sent |
| --- | --- |
| Bounded user constraints, up to the last 64 visible replies and tool results (clipped), short tool-result excerpts, an existing summary, saved-artifact names, omission markers | System prompts, hidden reasoning, images, environment variables, the API key in the model context and request body, complete transcripts |
| Best-effort redaction of known key patterns and obvious sensitive-file results | A guarantee. Uninstall or set mode Off for material that must not leave the machine |

Requests go to `https://api.typesafe.ai/v1/systemone`, or `<TYPESAFE_BASE>/v1/systemone` when that is set, are capped at 32,000 serialized UTF-8 bytes, and never treat an error as an affirmative judgment.
The TypeSafe API key never enters the model context or the request body; it is sent as the Authorization header to authenticate the call.
Details: [SECURITY.md](SECURITY.md).

## How It Works

```
settled turn
      │
      ▼
┌───────────────────┐
│ cheap local gates │  mode, 40k minimum, idle session, key, cooldowns
└─────────┬─────────┘
          ▼
┌───────────────────┐
│ TypeSafe Jev      │  done × shape score, floor slides 0.90→0.50 with usage
└─────────┬─────────┘
          ▼
 hint: run /compact     or, with explicit auto, native compaction
```

Automatic compaction is available on Pi and Claude Code. On Codex the same judgment only ever
produces the hint, as a `↳ Hook ·` line in the scrollback. On Grok the two halves are separate
processes: a `Stop` hook judges and records a verdict, and the `[ui.status_line]` script reads
that verdict and paints the hint. The Grok hook always allows the stop and prints nothing, so a
hint can never be fed back to the model.

On Claude Code, an optional `beforeCompactPrompt` setting (empty by default; set it in `/config`)
runs one turn before that automatic compaction, and only after auto mode is confirmed. Set it to
`/stow` to run the `stow` command first. Claude Code does not expand slash commands or `@file`
mentions in a prompt a plugin submits, and it rejects a plugin prompt that starts with `/`, so a
value that starts with `/` is run as a command instead of being sent to the model as text. If you
send your own prompt or run a command in between, or that turn is interrupted, errors, or does not
finish within 5 minutes, nothing is compacted. Hint mode, off, and an empty setting are unchanged. Pi, Codex, and
Grok do not have this setting.

## Usage

| Command | Effect |
| --- | --- |
| `/compact-adviser` (Pi and Claude Code) | Settings (mode, minimum, request log, TypeSafe API key) |
| `/compact-adviser auto` / `hint` / `off` (Pi and Claude Code) | Save that mode; auto asks for first-use confirmation |
| `/compact-adviser status` (Pi and Claude Code) | Mode, minimum, budget, context, key source (`env` / `saved` / `.env` / `missing`), cooldown |
| `/compact-adviser threshold 60000` (Pi and Claude Code) | Save an absolute token minimum |
| `/compact-adviser budget 450000` / `budget off` (Pi and Claude Code) | Save a context budget: the hint floor is fully relaxed at this many tokens, or at the host's own compaction point if that is smaller (off by default) |
| `/compact-adviser snooze` / `dismiss` (Pi and Claude Code) | Suppress the next three exchanges, or clear the current hint |
| `beforeCompactPrompt` in `/config` (Claude Code) | Optional text run before automatic compaction. Empty by default. `/stow` runs that command |
| `/compact-adviser` (Grok) | Show status; do not add arguments because Grok sends them to the model |
| `/compact-adviser-hint` / `/compact-adviser-off` (Grok) | Save hint-only mode, or disable the adviser |
| `/compact-adviser-snooze` / `/compact-adviser-dismiss` (Grok) | Suppress the next three exchanges, or clear the current hint |
| `/compact-adviser-install` (Grok) | Register the hooks and print the status-line block to paste into the named `config.toml` |
| `${GROK_HOME:-$HOME/.grok}/compact-adviser/adviser.sh threshold 60000` (Grok shell) | Save an absolute token minimum; `budget <tokens\|off>` saves a context budget; `help` lists the other shell-only settings |

On Codex the same commands are arguments to the plugin's `src/cli.ts` (`status`, `hint`, `off`,
`threshold`, `budget <tokens|off>`, `log on|off`, `key set|clear|status`) rather than a slash
command, because Codex plugins cannot register a command with code behind it. Codex has no
snooze or dismiss: the CLI cannot tell which session is current.

## Judge profiles

An optional [judge profile](docs/judge-profiles.md) changes the two questions, score weight, or floor schedule without changing shipped defaults. All four hosts accept the same bounded JSON string in the `profile` setting. Keep hint mode while evaluating a profile. Invalid profiles disable advice, and loading a profile never grants automatic-mode consent.

## Eval

Local judgment eval uses real session checkpoints to score when the adviser should suggest `/compact`. The curve below is from a follow-up-aware gold set (96 checkpoints, 40 sessions): as the context window fills, the score threshold loosens from **0.90** (≤10% used) to **0.50** (≥90% used) so **recall rises** while precision stays high - favoring token savings when compaction is about to be forced anyway.

![Use Jev to answer "should I /compact now?" — precision stays high while recall rises as context used goes from ≤10% to ≥90%](docs/eval-usage-floor-curve.png)

The judgment-eval harness lives in [packages/pi-extension/eval/](packages/pi-extension/eval/README.md). It is not a published dataset: point it at your own sessions and keep transcripts local.


## Docs
### docs/product-contract.md

# Shared product contract

This is a documentation contract, not a shared runtime or install-state layer.
Each harness implementation owns its event handling, dependencies, installation, configuration location, and session state.

## Semantics

- Modes: `hint` (default), `auto` (explicit experimental opt-in), and `off`.
A host that gives no process outside the session a way to run `/compact` ships `hint` and `off` only, and says so rather than offering an `auto` it cannot honour. Codex and Grok are such hosts.
- The hint is shown to the person, never to the model. A hint is never written into the conversation, returned as hook feedback, or used to keep the agent working.
- Hint text: Pi, Codex, and Grok display **Compact adviser: work appears completed or recorded. Run /compact to save tokens.** Claude Code's host adds **compact-adviser:**, so the mod supplies only **work appears completed or recorded. Run /compact to save tokens.**
- `minContextTokens` defaults to the constant **40000**, is configurable and persists with the selected mode.
There is no percentage-of-context-window condition.
- A size threshold makes a checkpoint eligible for judgment; it does not order compaction.
- Inspect cheap local state before any TypeSafe Jev request.
- TypeSafe/Jev snapshots include bounded user constraints from the mapped transcript, plus assistant replies and tool results that fall within its last 64 entries. Existing byte budgets still apply (about 14kB recent tail, per-message caps, 8kB user-constraint budget, and a 32kB request refuse path), so message count is not the tight payload bottleneck.
- Long tool-result dumps keep a head and tail slice with an explicit middle omission marker so one result cannot consume the tail budget.
- Optional TypeSafe request logging is off by default and can be enabled from the compact-adviser settings UI on Pi and Claude Code or the external CLI on Codex and Grok. When on, each request body and the matching Jev outcome are appended to a local jsonl log: successful outcomes include answers, score, usage, floor, and qualifies, plus the context budget when usage is measured against it (a budget is set and is smaller than the host's limit, or that limit is unknown); failures include only a sanitized error kind. Existing secret redaction applies, and the log never includes the API key. Pi uses one shared O_APPEND file. Claude writes one file per session (`compact-adviser-requests-<session-id>.jsonl`) because its host cannot atomically append. Codex writes the same per-session file name with O_APPEND. Grok also writes one O_APPEND file per session because every hook run is a separate process.
- Judge whether known next work can continue without exact older details, not whether context is merely large.
- One judgment decides both hint and auto: two atomic Jev questions in one request, `done` (is the assistant's own latest unit finished) and `shape` (is this conversation hands-on work or coordination), composed in code as score = P(finished) x (0.5 + 0.5 x P(hands_on)). The score must clear a floor that depends on context usage (context tokens over the limit at which the host compacts: Claude Code's auto-compact threshold when the host reports one as enabled, otherwise the model's window; Pi, Codex, and Grok expose no such threshold and use the window; an optional context budget, a token count the person sets on any host, replaces that limit as the denominator when it is smaller or the limit is unknown): 0.90 while usage is at most 10 %, 0.50 from 90 % on, and a linear ramp between (floor = 0.90 - 0.5 x (usage - 0.10), rounded to three decimals); unknown usage takes the strictest floor. An optional `profile` setting may replace the questions, the coordination weight, or the floor schedule on every host; see [judge-profiles.md](judge-profiles.md). Auto is not a higher bar. Mode only chooses what happens after a qualifying judgment (hint vs compact). Experimental auto still requires the existing first-use acknowledgement to turn auto on. Measured on the judgment-eval set against what users actually asked next: 95 % precision at 19 % recall at the strict end, 74 % / 91 % at the loose end, with no cliff between. A question that asked Jev to judge finished-and-hands-on in one step, and a companion "would older detail be lost" question, both measured worse and were not kept.
- `COMPACT_ADVISER_DISABLE` is a per-session kill switch. Set to `1`, `true`, `yes` or `on` (case-insensitive, surrounding whitespace ignored), it makes the product take no action for that process: no TypeSafe/Jev request, no hint, no automatic compaction, no command, and no status-line output that depends on a judgment. It wins over a saved `hint` or `auto` mode and over every other enablement path. Any other value, including unset, leaves behavior unchanged. Pi and Claude Code read it once when the session loads. Codex and Grok check it in each short-lived hook, status-line, or command process, all of which inherit the session's fixed environment. Every host parses it through a byte-identical `disable.ts`. Pi returns from install before registering hooks or `/compact-adviser`. Codex returns from the hook and CLI process before judging or running a command. Grok returns from hooks, status output, and commands before doing work.
- Non-interactive sessions stay inert when that can be detected reliably. Pi requires `mode === "tui"` with a UI; the Claude Code mod requires the host's `session.start` `isInteractive` flag and returns before command registration, session-record pruning, pending-save toasts, and compaction cooldown writes. Codex reads the rollout's `originator`. No host guesses from `CI` or similar ambient variables.
- Uncertain, stale, interrupted, or failed judgments leave context alone. A host whose only user-facing channel is permanent (Codex's hook output becomes a scrollback line that cannot be cleared) reports such a failure nowhere and simply backs off.
- Installing or loading the package is consent to send eligible checkpoint context to TypeSafe when a key is available and other product gates pass (mode, minimum context, idle session, and so on). Pi and Claude Code let a TypeSafe API key be entered in the compact-adviser menu. Codex provides an external settings CLI. On Grok, save one from an external shell (`key`), `TYPESAFE_API_KEY`, or a session-cwd `.env`. Do not type secrets after a Grok slash command: Grok appends extra words to the model. The TypeSafe API key never enters the model context or the request body; it is sent as the Authorization header to authenticate the call. After save the UI reports only presence or key source (`env` / `saved` / `.env` / `missing`), never the value. A non-empty launch-environment value wins over the saved key, which wins over a session-cwd `.env`.
- There is no separate sharing toggle. A saved `sharingConsent` value from an older version is ignored.
- Native compaction remains authoritative and lossy; no timing model promises perfect preservation.
- Configuration changes do not immediately compact.
Invalid values and cancellation preserve existing settings; failed saves are reported.

## Implementations

| Package | State | Installation |
| --- | --- | --- |
| `packages/pi-extension` | Pi implementation | Install this package path with `pi install` |
| `packages/claude-mod` | Claude Code mod (early-access function-hooks API) | Load this package path with `claude --plugin-dir` and `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` |
| `packages/codex-plugin` | Codex CLI plugin, hint-only | `codex plugin marketplace add` this repository, then `codex plugin add compact-adviser@compact-adviser` |
| `packages/grok-plugin` | Grok Build plugin, hint-only | `grok plugin install <path> --trust`, then `/compact-adviser-install` for the hooks and a `[ui.status_line]` opt-in for the hint |

Pi uses its own agent-directory `compact-adviser.json` and Pi session custom entries.
The Grok plugin uses its own `${GROK_HOME:-~/.grok}/compact-adviser/settings.json`, plus one file per session for cooldowns and one for the verdict the status line reads; its two halves are separate processes, so nothing is held in memory between them.
The Claude Code mod uses its own `userConfig` options (`mode`, `minContextTokens`, `contextBudgetTokens`, `logRequests`, `profile`, `beforeCompactPrompt`, `typesafeApiKey`) in Claude Code's settings, and its own plugin store for the automatic-mode acknowledgement and per-session cooldowns.
`beforeCompactPrompt` is Claude Code only and empty by default, so the other hosts are unchanged.
A non-empty value, and only in confirmed auto mode, runs as one turn before compaction; compaction follows only if that turn ends in a settled answer.
A leading `/` is a slash command, because a plugin prompt does not expand slash commands or `@file` mentions.
An intervening prompt or command, an interruption, an error, or a 5-minute timeout leaves context alone.
Pi does not share this setting: host parity is the judge questions, the score, and the floor, not each host's configuration.
Codex and Grok stay hint-only.
`typesafeApiKey` is hidden from `/config` so the host menu never draws the secret.
The Codex plugin owns `<CODEX_HOME>/compact-adviser/`: one `settings.json`, one cooldown record
per session, and the request logs. It does not touch `config.toml`, whose unknown keys are an
error under `--strict-config`, and it has no `auto` mode or acknowledgement to store.
Snooze and dismiss are a known gap: Codex gives neither the hook nor the CLI a reliable
current-session identity, so the CLI could only mutate the most recently written session record.
No implementation reads or mutates another's records.
No harness installs or loads another harness's runtime.


### docs/judge-profiles.md

# Judge profiles

A profile is a JSON object that changes judge questions or decision thresholds.
Use a profile to evaluate a session-specific policy without changing the shipped defaults.
The runtime judge remains TypeSafe Jev on every host.
An empty or absent `profile` setting uses the shipped policy.

Keep `mode` set to `hint` while evaluating a profile.
A profile changes the shared hint and auto gate, but it does not grant auto consent.
Evidence that a hint occurs at a good moment does not prove that compaction preserves needed context.
This feature does not change minimum token counts, cooldowns, or recovery gates.

## Format

This example reproduces the shipped score and floor schedule:

```json
{
  "version": 1,
  "coordinationWeight": 0.5,
  "floors": [[0.1, 0.9], [0.9, 0.5]]
}
```

The score is `P(finished) * (1 - coordinationWeight + coordinationWeight * P(hands_on))`.
The weight must be between zero and one.
A weight of zero removes the coordination penalty.
This is an available setting, not a recommendation.

Each floor point contains `[usageFraction, requiredScore]`.
The gate interpolates between points and rounds the result to three decimal places.
Usage below the first point uses the first floor.
Usage above the last point uses the last floor.
Unknown usage uses the first, strictest floor.
A single point sets a constant floor.

A profile accepts one to eight points.
Usage values must strictly increase, and floors must not increase.
Every value must be between zero and one.
The same host-specific usage denominator applies with and without a profile, and a context budget, when set, replaces it in both cases whenever the budget is smaller or the host limit is unknown.

The optional `questions` field replaces both questions in full.
It has the same structure as `QUESTIONS` in `packages/pi-extension/src/judge.ts`.
Only the instruction and criterion text can change.
Keep `type: "choice"`, both question keys, and all criterion keys:

- `done`: `finished`, `not_finished`, `unclear`.
- `shape`: `hands_on`, `coordinating`, `unclear`.

The serialized profile must fit within 4,096 UTF-8 bytes.
Unknown fields, empty text, invalid values, and malformed JSON disable advice.
Clear the setting or restore valid JSON to enable advice again.
Profiles cannot execute code, load files, or select another provider.

## Load a profile

The `profile` setting holds a JSON **string**, not an embedded object.
For the example above, the configuration field is:

```json
"profile": "{\"version\":1,\"coordinationWeight\":0.5,\"floors\":[[0.1,0.9],[0.9,0.5]]}"
```

Use the same string on each host:

- Pi: add `profile` to `compact-adviser.json` in the Pi agent directory, normally `~/.pi/agent`.
- Claude Code: set `compact-adviser.profile` in `/config` to the serialized JSON text, without the outer string quotes.
- Codex: add `profile` to `${CODEX_HOME:-~/.codex}/compact-adviser/settings.json`.
- Grok: add `profile` to `${GROK_HOME:-~/.grok}/compact-adviser/settings.json`.

Preserve existing fields, especially saved keys and mode consent.
If the configuration file does not exist, first use the host's adviser controls to create it.
Do not replace the whole file with the profile object.
To restore shipped behavior, set the string to `""` or remove the field.

Request logs contain the selected questions.
Response logs contain the score, floor, and decision from the selected profile.
A change to the profile during a pending judgment prevents that judgment from producing advice.

## Default equivalence

All four packages keep the same built-in questions, score, and floor schedule.
The profile parser and judge behavior are tested across hosts in
`packages/pi-extension/test/profile.test.ts`.
Each host also tests its hook or extension with a stored profile.
Default-equivalence tests compare emitted requests and decisions across usage boundaries.
No tailored profile is recommended by this feature alone.


## Top-level structure
```
.agents/, .claude-plugin/, .claude/, .grok-plugin/
docs/          # product-contract, judge-profiles, screenshots
packages/      # claude-mod, codex-plugin, grok-plugin, pi-extension
scripts/
AGENTS.md, CLAUDE.md, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, VISION.md
package.json, LICENSE
```
- Multi-harness packages: Claude Code mod, Codex plugin, Grok plugin, Pi extension
- Uses Jev to advise when `/compact` is safe
- `docs/product-contract.md`: product behavior contract

