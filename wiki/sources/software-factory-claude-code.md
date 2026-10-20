---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/zazencodes/zazencodes-season-3/tree/main/src/software-factory-claude-code
tags:
  - software-factory
  - claude-code-subagents
  - multi-reviewer-loop
  - git-worktrees
  - spec-build-review-approve
  - file-based-orchestration
related:
  - warpdotdev-warp-factory-examples
  - coleam00-archon
  - coleam00-harness-engineering-demo
  - dark-factory-autonomous-ai-codebase
  - chaseai-yt-claudex-loop
  - Kevin-Liu-01-Claude-of-Tanks
product: software-factory-claude-code
detail_level: standard
created: 2026-10-13
updated: 2026-10-20
---

ZazenCodes' "Software Factory for Claude Code" is a small, copy-in template that turns a Claude Code session into an autonomous feature pipeline built from just one skill (`/factory`), seven subagents, and plain markdown files. You type `/factory <feature>`; agents write a spec, build it on its own branch in its own git worktree, review it from four angles (security, UX, UI, code) in parallel, and either merge it to `main` or hand it to a human. It matters for this wiki as a deliberately minimal, readable reference for the "software factory" / dark-factory pattern using only native Claude Code primitives, with no external framework or runtime, plus a live HTML dashboard so you can watch jobs move through the stages.

_All claims below are sourced from ../../raw/web/software-factory-claude-code.md unless otherwise noted._

## What it does

The folder is laid out like a repo root (`.claude/` + `factory/`) so it can be copied straight into a project. The Claude Code session that runs `/factory` becomes the orchestrator: it spawns every agent and is the only writer of the job's `job.json`. The loop is:

```
feature → spec-writer → builder → [security, ux, ui, code] → WAIT FOR ALL
                           ▲                                      │
                           └──── any CHANGES: resume builder ◄────┤
                                                                  ▼ all PASS
                                     merge to main ◄─ APPROVE ─ approver ─ ESCALATE → needs-human
```

## Key features

- **Seven role subagents with model tiers:** `spec-writer`, `builder`, `reviewer-security`, and `approver` run on Opus; `reviewer-ux`, `reviewer-ui`, and `reviewer-code` run on Sonnet.
- **File-based contracts:** agents get context from files, not the conversation, and each writes only its own file. Every review starts with `VERDICT: PASS` or `VERDICT: CHANGES`; `decision.md` starts with `APPROVE` or `ESCALATE`.
- **Parallel review with a hard barrier:** the four reviewers run in parallel, and a round is complete only when all four review files exist ("WAIT FOR ALL").
- **Bounded rework:** on any CHANGES verdict, the same named builder is resumed, at most twice, so a job gets at most three review rounds before it escalates.
- **Worktree-per-job parallelism:** each job runs in `../<repo>-factory/<job-id>/` on a `factory/<job-id>` branch, so you can open several Claude sessions and run `/factory` in each to build features concurrently.
- **Visual dashboard:** a single `dashboard.html` (served with `python3 -m http.server` from `factory/`) polls every two seconds and shows jobs as cards moving across stages, with reviewer chips filling in as verdicts land and needs-human jobs highlighted.
- **Backlog queue:** `/factory next` pulls the first unchecked item from `factory/backlog.md`.

## Architecture and concepts

- **Orchestrator skill** (`.claude/skills/factory/SKILL.md`) runs the loop, spawns agents, and keeps one `job.json` per job with `stage` (`spec`, `build`, `review`, `approve`, `merged`, `needs-human`), current `round`, and per-reviewer verdicts. Per-job state files, rather than one shared board file, let several sessions run jobs without write contention.
- **Job folders** (`factory/jobs/<job-id>/`) are gitignored runtime state holding `spec.md`, `build.md`, `round-N/review-{security,ux,ui,code}.md`, any `rework-K.md`, and `decision.md`.
- **Repo-agnostic agents:** no repo-specific knowledge lives in the agent files. Every agent reads `AGENTS.md` (or `CLAUDE.md`) for fresh-checkout setup, the dev server port, and test/build/lint commands.
- **Approver as a risk gate:** the approver only approves when every acceptance criterion is met, all final-round reviews pass, and the branch merges cleanly. It escalates anything that touches money, auth, permissions, deploy/CI/build config, schema migrations, email, production data, or new dependencies, as well as specs that rest on business decisions. (Details are from the repo's `approver.md`, read alongside the page capture.)
- **Browser verification:** the builder and the UX and UI reviewers use the [`agent-browser`](https://github.com/vercel-labs/agent-browser) CLI to check the running app, with per-job dev-server ports so parallel jobs don't see each other's pages.

## Main APIs

```
/factory <feature>               run a new job through the loop
/factory next                    run the first unchecked item in factory/backlog.md
/factory approve <job-id>        merge a needs-human job into main
/factory rework <job-id> <note>  send a needs-human job back to the builder with feedback
```

Setup: copy `.claude/` and `factory/` into the repo root, delete the example jobs and checked backlog items, add `/factory/jobs/` to `.gitignore`, make sure `AGENTS.md`/`CLAUDE.md` documents setup, dev server, and validation commands, install `agent-browser` if the project has pages, commit on `main`, then run `/factory <feature>`. The README recommends asking Claude to tailor the deliberately general review checklists to your stack.

## When to use

Use it when you want a readable, hackable starting point for an unattended spec → build → multi-angle review → gated merge loop entirely inside Claude Code, especially for web apps where UI/UX checks against a running server are useful. Two example jobs from zazencodes.com (Vue + Firebase) show both outcomes. `001-blog-reading-time` passed all reviews but was escalated because it edited a prerender script, which counts as a deploy change. `002-not-found-page` was merged automatically. `BUILD_PROMPT.md` keeps the original one-shot prompt that generated the factory. It describes an earlier single `board.json` design that has since been replaced by per-job `job.json` files and worktrees.

## Ecosystem

Part of the `zazencodes/zazencodes-season-3` repo of video companion projects. Compared with [[warpdotdev-warp-factory-examples]] (file-defined multi-agent SDLC pipelines on Warp's hosted Oz platform) and [[coleam00-archon]] (a YAML DAG workflow engine with worktree isolation), this factory gets the same shape from Claude Code's built-in skills and subagents alone, in the spirit of [[coleam00-harness-engineering-demo]]. It is a concrete, small-scale instance of the "dark factory" idea described in [[dark-factory-autonomous-ai-codebase]], with a human escalation path kept deliberately in the loop.
