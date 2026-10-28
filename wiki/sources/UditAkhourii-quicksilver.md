---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/UditAkhourii/quicksilver
tags:
  - file-shortlist
  - jev-model
  - token-savings
  - claude-code-skill
  - bulk-judgment
  - log-triage
  - zero-deps
related:
  - typesafe.ai
  - dzhng-jevgrep
  - zilliztech-claude-context
  - tamaratran-fast-jev-compaction
product: quicksilver
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Quicksilver is a Claude Code skill (and plugin) that offloads bulk judgment calls — which files matter, which log lines are real failures, which tickets match a label — to Jev, TypeSafe's System One model. Jev returns typed verdicts (yes/no, a label, a score) and Claude gets back a shortlist, spending tokens on reasoning rather than skimming. On a 12-task benchmark the project claims a median ~82% cut in Claude tokens (headline **86%**), accuracy within 2 points of Claude alone on 8 of 12 tasks, up to 20× faster wall-clock on some tasks, and a median ~$0.004 of Jev per task; Jev is priced at $0.042 per million input tokens with free output.

_All claims below are sourced from ../../raw/github/UditAkhourii-quicksilver.md unless otherwise noted._

## What it does

A large share of Claude Code sessions is spent reading inputs only to decide whether they matter. Quicksilver hands those skim-and-decide steps to Jev in parallel (for example ranking 187 files for auth relevance and returning a few paths plus confidence). The skill is meant for needle-finding in large inputs, bulk routing with clear labels, and "where is X?" ranking across a codebase; borderline items are marked `?` for Claude to check. It is not for writing, editing, multi-step reasoning, or exact `grep` answers. On huge scans wall-clock can match Claude alone — the win is tokens and context, not always speed; `--fast` packs items for roughly 10× faster runs on obvious needles.

## Installation

```bash
npx github:UditAkhourii/quicksilver
```

The installer copies the skill into `~/.claude/skills/quicksilver` and prompts once for a Jev key (from console.typesafe.ai); then restart Claude Code. Alternatives include `npx github:UditAkhourii/quicksilver install --key YOUR_JEV_KEY`, Claude Code plugin marketplace install (`/plugin marketplace add UditAkhourii/quicksilver` then `/plugin install quicksilver@quicksilver`), or cloning and running `./install.sh` / `.\install.ps1`. `JEV_API_KEY` or `TYPESAFE_API_KEY` in the environment also works. Requires Node 18+; no npm dependencies.

## Key features

- **CLI surface for agents** — `qs filter`, `qs classify`, `qs rank`, `qs find`, `qs ask`, and `qs status` (key check + lifetime tokens saved); output is one line per hit, with repeated log patterns collapsed and borderline hits marked `?`, plus a per-run receipt (scanned/matched/borderline, time, Jev tokens/cost, Claude tokens not read).
- **Prompt discipline** — the skill pushes Claude toward one narrow typed judgment per question (yes/no, closed labels, or a rubric), with exact boundary cases and a catch-all label, and without arithmetic or dates.
- **Safety defaults** — never sends `.env*`, private keys, certificates, or credentials files; respects `.gitignore`; skips binaries and files over 2 MB. Content goes to TypeSafe's API (`api.typesafe.ai`); the README states TypeSafe says Jev is not trained on customer data. The key lives in `~/.quicksilver/config.json` with user-only permissions; `npx github:UditAkhourii/quicksilver setup --remove` deletes it.
- **Measured benchmark** — twelve tasks (real public data and synthetics) comparing Claude alone (Read/Grep/Glob) vs Claude + Quicksilver against hidden ground truth; reproducible under `bench/` (token accounting subtracts a fixed Claude overhead; Quicksilver is charged for SKILL.md, commands, and stdout Claude reads back).

## Architecture

Top-level layout includes `.claude-plugin/`, `bin/`, `assets/`, `bench/`, `skills/quicksilver/`, plus `install.sh` / `install.ps1`, `package.json`, and README. Flow: Claude asks a judgment question → Quicksilver calls Jev over the candidate set in parallel → Claude receives a short shortlist (paths/labels/scores and confidence) instead of reading the full corpus. Independent open-source project (MIT), not affiliated with Anthropic or TypeSafe AI. (../../raw/github/UditAkhourii-quicksilver.md)

## Example usage

```bash
qs filter   "Does this file handle user sessions?" src
qs filter   "Does this line report a failure?" app.log --lines
qs classify --labels "bug,feature,question" --items issues.jsonl
qs rank     "where do we issue refunds?" src --top 5
qs find     "the retry backoff logic" huge_module.py
qs ask      "Does this contract allow termination without notice?" --state @contract.txt
qs status
```

(../../raw/github/UditAkhourii-quicksilver.md)

## Maintenance status

MIT licensed (© Udit Akhouri); primary language JavaScript; default branch `main`; no tagged GitHub releases at ingest time (fetched 2026-10-28); ~131 stars. Zero npm dependencies; Node 18+. (../../raw/github/UditAkhourii-quicksilver.md)
