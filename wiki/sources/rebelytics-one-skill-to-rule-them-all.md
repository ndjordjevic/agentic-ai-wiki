---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/rebelytics/one-skill-to-rule-them-all
tags:
  - task-observer
  - meta-skill
  - skill-improvement
  - observation-log
  - augmented-expertise
  - claude-code-skills
  - skills-sh
  - self-improving
related:
  - anthropics-skills
  - skills.sh
  - coreyhaines31-makerskills
  - obra-superpowers
  - coleam00-skills
  - davidondrej-skills
  - addyosmani-agent-skills
product: one-skill-to-rule-them-all
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

rebelytics/one-skill-to-rule-them-all (3,584 stars, CC BY 4.0) is Eoghan Henn's `task-observer` meta-skill — a skill that watches your work sessions, logs corrections, gaps and judgement calls as observations, and turns them into reviewed improvements to your other skills (and to itself). It is a practical application of the Augmented Expertise methodology, installs through `npx skills` / [[skills.sh]], and sits alongside skill-authoring packs like [[anthropics-skills]] as the maintenance layer: skills that learn from use instead of staying frozen.

_All claims below are sourced from ../../raw/github/rebelytics-one-skill-to-rule-them-all.md unless otherwise noted._

## What it does

Task Observer runs alongside normal work and looks for three things: **corrections and adjustments** (a signal a skill is unclear or incomplete), **gaps no skill covers yet** (repeated manual work flagged as a new-skill candidate), and **its own blind spots**. Each session produces a structured observation log — what it noticed, which skills are affected, and suggested improvements. Patterns that span skills are captured as **cross-cutting principles** in a separate file, against which new or updated skills are checked automatically. The author reports over 1,900 observations across 84 skills, most turned into improvements, and most of those skills were themselves created from observations.

The observer never edits installed skills directly: in interactive review you approve each change; a scheduled review applies only no-decision changes to staged copies under `skill-updates/`; nothing goes live until you install the updated bundle. The README contrasts it with Claude Code project memory (per-project notes applied automatically) and the `/insights` command (a snapshot report with no running log), and says a pitfall stored in project memory more than once is a signal it belongs in a skill. It also states an honest boundary: with only a handful of skills, built-in memory may cover much of the same ground with less overhead.

## Installation

```bash
npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer   # add -g for all projects
```

This is the most-used route (the skills.sh listing reports 13,000+ installs). In the Claude apps (web, desktop, mobile, Cowork) upload the `.skill` bundle from the latest release via Settings → Customize; in Claude Code place the folder at `.claude/skills/task-observer/`. Installing alone is not enough: add the activation instruction from `references/environments.md` to `CLAUDE.md` (or a session-start hook), because description matching under-triggers. Verify in a *new* session by checking that `skill-observations/observation-log/` appears after real work. Installing only `SKILL.md` works but runs degraded.

## Key features

- **Observation log as a directory** — one small Markdown file per observation with frontmatter (status, skill, type, date) under `skill-observations/observation-log/`; resolved entries move to `archive/`, so Claude scans headers instead of rereading the backlog.
- **Weekly review** — offered when more than 7 days have passed with open observations; the author schedules a Monday/Wednesday/Friday run over 20–30 open observations.
- **Self-improvement** — the observer logs improvements to its own methodology and triggering behavior.
- **Open-source vs internal skills** — a confidentiality boundary with safeguards against leaking client or personal data into open-source skills.
- **Dual-layer activation** — the skill's own triggers plus a `CLAUDE.md` instruction to run the Session Start Protocol.
- **Handoff-doc mode** — in Claude.ai chat without filesystem access, it produces a handoff document at session end.
- **Community** — 100+ contributors credited in commit history, 270+ issues and PRs closed; user-made Codex (AllstarGER) and OpenCode (tmogeid) variants are linked.

## Architecture

A small bundle: `SKILL.md` (frontmatter version 3.8.1, core capped at 682 lines), `references/` loaded on demand (`weekly-review.md`, `skill-authoring.md`, `observation-log.md`, `signals.md`, `environments.md`, `migration.md`), and five helper scripts in `scripts/` (pre-3.0 log migration, observation-file creator, session-start scan, per-skill observation lookup, bundle validation gate). Also `.claude-plugin/` manifest, `USER-GUIDE.md`, and community files. The workspace should be one stable absolute path outliving sessions (e.g. a Cowork shared folder or a user-scope path), never an ephemeral worktree. The skill needs no network in normal operation. It was designed for Claude Cowork and tested on Claude.ai (handoff mode), mobile and Claude Code in the desktop app; Claude Code without the desktop app, Openclaw and Hermes are reported to work, while other platforms need adaptation of Claude-centric concepts.

## Example usage

```text
# End of a session
> Any observations logged?
# Claude lists captured observations; later a scheduled review applies them to staged skill updates
```

The author also recommends kickstarting with a personal writing-style skill built from your best pre-AI writing samples, then pasting back your edited drafts so the observer refines it over time.

## Maintenance status

3,584 GitHub stars, 351 forks, CC BY 4.0 (credit Eoghan Henn / rebelytics.com), default branch `main`, latest release v3.8.0 (2026-10-23), most recent push 2026-10-26. Primary content is Markdown. Actively maintained and listed in several skill directories and awesome-lists; independent security audits (Gen Agent Trust Hub, Socket, Snyk) are reported on the skills.sh listing, plus an Oathe Security badge.
