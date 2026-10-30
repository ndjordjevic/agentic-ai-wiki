---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/kunchenguid/compact-adviser
tags:
  - context-compaction
  - jev-model
  - compact-hint
  - multi-harness
  - pi-extension
  - claude-code-plugin
  - typesafe-api
related:
  - typesafe.ai
  - tamaratran-fast-jev-compaction
  - chopratejas-headroom
  - mksglu-context-mode
  - nadimtuhin-claude-token-optimizer
  - microsoft-TokenEconomizer
product: compact-adviser
detail_level: standard
created: 2026-10-28
updated: 2026-10-30
---

compact-adviser is a multi-harness agent plugin that answers one question: should I `/compact` now? It uses TypeSafe Jev to judge whether the current session is at a boundary safe to compact, then shows a hint (or, on Pi and Claude Code with explicit opt-in, runs compaction automatically). Codex CLI and Grok Build are hint-only. Judgment is two one-sentence Jev questions in one request (is the unit finished; is this hands-on work or coordination), composed in code into a score; the hint floor starts at 0.90 when context is mostly empty (~10%) and relaxes toward 0.50 by ~90% full. Prerequisites include Node 22+ and a TypeSafe API key (`TYPESAFE_API_KEY`, saved settings, or cwd `./.env`).

_All claims below are sourced from ../../raw/github/kunchenguid-compact-adviser.md unless otherwise noted._

## What it does

After a settled turn, cheap local gates (mode, 40k-token minimum by default, idle session, key, cooldowns) decide whether to call Jev. Jev returns `done` and `shape` answers; the package scores `P(finished) × (0.5 + 0.5 × P(hands_on))` and compares against a usage-dependent floor (or a user-set context budget if smaller than the host compaction point). Qualifying judgments produce a human-facing hint — never written into the model context — or, in confirmed `auto` mode on Pi/Claude Code, native compaction. Uncertain, failed, or disabled judgments leave context alone. Installing the package is consent to send eligible checkpoint context to TypeSafe when a key is available and other gates pass; payloads are capped at 32k serialized UTF-8 bytes and never treat errors as affirmative.

## Installation

**Pi** (0.82.0+, verified on 0.85.1):

```sh
pi install npm:compact-adviser
```

Restart Pi or `/reload`, then `/compact-adviser`. Git install: `pi install git:github.com/kunchenguid/compact-adviser` (`-l` for project-local).

**Claude Code** (2.1.274+, verified on 2.1.275; needs function hooks):

```sh
claude plugin marketplace add kunchenguid/compact-adviser
claude plugin install compact-adviser@compact-adviser
CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude
```

Then `/compact-adviser`.

**Codex CLI** (0.153.0+, verified on 0.153.4; macOS/Linux only, hint-only):

```sh
codex plugin marketplace add kunchenguid/compact-adviser
codex plugin add compact-adviser@compact-adviser
```

Restart Codex and trust the hook in `/hooks`. Settings via the plugin's `src/cli.ts` (`status`, `hint`, `off`, `threshold`, `budget`, `log`, `key`).

**Grok Build** (1.0.34+, hint-only):

```sh
grok plugin install kunchenguid/compact-adviser#packages/grok-plugin --trust
```

Then `/compact-adviser-install` (writes hooks under `GROK_HOME`) and paste the printed `[ui.status_line]` block into the named `config.toml`.

## Key features

- **Hint vs auto modes** — `hint` (default), `auto` (Pi/Claude Code only, first-use confirmation), and `off`; Codex and Grok ship hint/off only.
- **Usage-sliding score floor** — 0.90 at ≤10% context used → 0.50 at ≥90%, with optional context budget as the denominator when smaller than the host limit.
- **Multi-harness packages** — `packages/pi-extension`, `packages/claude-mod`, `packages/codex-plugin`, `packages/grok-plugin`; shared judge semantics, separate install/state per host.
- **Privacy-bounded TypeSafe payload** — bounded user constraints, last 64 visible replies/tool results (clipped), short excerpts, existing summary, artifact names; not system prompts, hidden reasoning, images, env vars, or full transcripts. Key goes only as Authorization header.
- **Session kill switch** — `COMPACT_ADVISER_DISABLE=1|true|yes|on` disables all advice/compaction for that process; inert in detected non-interactive sessions.
- **Optional judge profiles** — JSON string overriding questions, coordination weight, or floor schedule (≤4,096 UTF-8 bytes); invalid profiles disable advice; never grants auto consent.
- **Claude-only `beforeCompactPrompt`** — optional pre-compaction turn in confirmed auto mode (e.g. `/stow` as a command); empty by default.

## Architecture

Flow: settled turn → local gates → TypeSafe Jev (`done` × `shape` score) → hint or auto compact. On Claude Code the mod uses early-access function hooks and stores mode/key/budget in Claude settings plus a plugin store for auto acknowledgement and cooldowns. Codex writes settings, cooldowns, and request logs under `<CODEX_HOME>/compact-adviser/` and surfaces advice as a `↳ Hook ·` scrollback line. On Grok, a Stop hook judges and records a verdict while a separate `[ui.status_line]` script paints the hint — the hook always allows stop and prints nothing, so hints never enter the model. Pi uses agent-directory `compact-adviser.json` and session custom entries. No host installs or mutates another's runtime. (../../raw/github/kunchenguid-compact-adviser.md)

## Example usage

On Pi or Claude Code, open settings with `/compact-adviser`, check `/compact-adviser status` for mode, minimum, budget, context, and key source (`env` / `saved` / `.env` / `missing`), then `/compact-adviser hint` or `/compact-adviser auto` (auto prompts for first-use confirmation). Raise the absolute floor with `/compact-adviser threshold 60000`, or set `/compact-adviser budget 450000` so the score floor fully relaxes at that token count (or the host compaction point if smaller). `/compact-adviser snooze` suppresses the next three exchanges; `dismiss` clears the current hint. On Codex, run the same verbs against the cached plugin's `src/cli.ts` (no snooze/dismiss — CLI cannot identify the current session). On Grok use `/compact-adviser` for status, `/compact-adviser-hint` / `-off` / `-snooze` / `-dismiss`, and shell `adviser.sh` for threshold/budget. Hint text (Pi/Codex/Grok): "Compact adviser: work appears completed or recorded. Run /compact to save tokens." (../../raw/github/kunchenguid-compact-adviser.md)

## Maintenance status

MIT licensed; default branch `main`; latest release `compact-adviser-v0.1.14` at ingest; 224 stars; platforms macOS and Linux (Codex explicitly not Windows this ship). Claude Code path depends on experimental function hooks (`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`). Product contract and judge-profile docs live under `docs/`; judgment-eval harness is local-only under `packages/pi-extension/eval/` (not a published dataset). (../../raw/github/kunchenguid-compact-adviser.md)
