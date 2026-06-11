---
type: source
source_url: https://github.com/santifer/career-ops
tags:
  - job-search-automation
  - claude-code-skills
  - agentic-workflow
  - playwright-scraping
  - pdf-generation
  - multi-agent-batch
  - go-tui
  - multi-harness
related:
  - obra-superpowers
  - gsd-build-get-shit-done
  - anthropics-skills
product: career-ops
detail_level: standard
created: 2026-06-11
updated: 2026-06-11
---

Career-Ops is an open-source, AI-powered job search automation system — 52,587 stars, MIT license, v1.10.0 — that turns any AI coding CLI into a full end-to-end job search command center. Built by Santiago (santifer), who used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role. It is CLI-agnostic, shipping native support for Claude Code, Gemini CLI, OpenCode, Codex, Qwen, GitHub Copilot, and Kimi through dedicated harness wrappers (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude-plugin/`, etc.). The system is not a spray-and-pray tool — it is explicitly a filter: it helps surface the few high-signal offers out of hundreds and strongly discourages applying to anything scoring below 4.0/5.

_All claims below are sourced from ../../raw/github/santifer-career-ops.md unless otherwise noted._

## What it does

Career-Ops wraps 15 skill modes (under `modes/*.md`) around three core pipelines: single-offer evaluation, portal scanning, and batch processing. A user pastes a job description URL or raw text; the system detects the archetype (one of six types: LLMOps, Agentic, PM, SA, FDE, Transformation), runs a 6-block A-through-F evaluation against the user's `cv.md`, produces a structured report, generates an ATS-optimized PDF CV, and writes a tracker entry — all in one slash command. Portal scanning hits Greenhouse/Ashby/Lever APIs with zero LLM tokens; batch processing runs N headless `claude -p` workers in parallel. A Go/Bubble Tea terminal dashboard lets users browse, filter, and manage their pipeline interactively.

## Key features

- **6-Block evaluation system** — Blocks A–F cover role summary, CV match (gaps + mitigation), level strategy, comp research (WebSearch), CV personalization plan, and interview prep (STAR+Reflection stories). Block G is a posting-legitimacy check that flags scams and ghost jobs.
- **ATS PDF generation** — keyword-injected CVs using a Playwright HTML→PDF pipeline with Space Grotesk + DM Sans typography.
- **Cover letter generator** — research-backed letters with keyword mirroring, four interactive angle prompts (why/problems/approach/tone), draft-in-chat approval gate, and A4 PDF output.
- **Portal scanner** — 45+ pre-configured companies (Anthropic, OpenAI, ElevenLabs, n8n, Retool, Mistral, etc.) across Ashby/Greenhouse/Lever/Wellfound; `--verify` flag adds Playwright liveness checks to drop expired postings.
- **Batch processing** — `batch-runner.sh` orchestrates N parallel headless CLI workers, each producing a report + PDF + tracker TSV line; the orchestrator handles state, retries, and resume.
- **Interview story bank** — accumulates STAR+Reflection stories across evaluations into a reusable master bank at `interview-prep/story-bank.md`.
- **Negotiation scripts** — salary negotiation frameworks, geographic discount pushback, competing offer leverage.
- **Dashboard TUI** — Go + Bubble Tea + Lipgloss (Catppuccin Mocha theme); 6 filter tabs, 4 sort modes, lazy-loaded previews, inline status changes.
- **Auto-update system** — each session silently checks for updates; only announces when one is available. User controls whether to apply, dismiss, or rollback.

## Architecture

The architecture follows a two-layer data contract enforced in `AGENTS.md`: the **User Layer** (`cv.md`, `config/profile.yml`, `modes/_profile.md`, `portals.yml`, `data/*`, `reports/*`) is never auto-updated; the **System Layer** (`modes/_shared.md`, all skill modes, scripts, dashboard, templates) is auto-updatable via `update-system.mjs`. All user customizations (archetypes, scoring weights, location preferences, proof points) must go to `modes/_profile.md` or `config/profile.yml` — never to `_shared.md` — so system updates cannot overwrite user data.

The evaluation pipeline:
```
Input (URL or JD text)
  → Archetype detection (6 types)
  → A-F evaluation (reads cv.md + article-digest.md + config/profile.yml)
  → report.md + ATS PDF + tracker TSV entry
```

The scanner:
```
portals.yml config → scan.mjs (zero-token API calls)
  → pipeline.md (URL inbox)
  → optional --verify (Playwright liveness)
```

Batch processing:
```
batch-input.tsv → batch-runner.sh → N × headless CLI workers
  → merge-tracker.mjs → data/applications.md
```

Pipeline integrity is maintained by `verify-pipeline.mjs`, `dedup-tracker.mjs`, `normalize-statuses.mjs`, `merge-tracker.mjs`, and `cv-sync-check.mjs`.

## Installation

```bash
npx @santifer/career-ops init
cd career-ops
claude   # or: gemini / codex / opencode / qwen
```

First launch runs onboarding interactively — the agent asks for your CV, profile, and target roles through conversation; nothing to edit by hand. Prerequisites checked via `node doctor.mjs --json`.

## Example usage

```
/career-ops {paste JD text or URL}  → full auto-pipeline
/career-ops scan                    → scan 45+ portals for new offers
/career-ops pdf                     → generate ATS-optimized CV
/career-ops cover                   → generate cover letter
/career-ops batch                   → batch evaluate multiple offers
/career-ops tracker                 → view application status dashboard
/career-ops deep                    → deep company research
```

Or paste a job URL directly — career-ops auto-detects it and runs the full pipeline.

## When to use

Career-Ops is the right choice for technical job seekers — particularly AI/ML engineers and PMs — who want to replace manual spreadsheet tracking with an agentic pipeline. It excels when the candidate faces high-volume screening (dozens to hundreds of listings) and wants quality-filtered, personalized applications rather than mass submissions. Because it runs entirely locally, all CV and personal data stays on the user's machine. It is deliberately not a hosted SaaS — the system never auto-submits applications; the human always reviews and approves before any action reaches a recruiter.

## Maintenance status

52,587 stars, 10,551 forks, JavaScript primary language (Go for the dashboard), last pushed 2026-06-11. Latest release v1.10.0 (2026-06-11). MIT License. Featured in Wired and Business Insider. Active community via Discord. Companion project `cv-santiago` (open-source portfolio site) also available.

## Ecosystem

Career-Ops lives squarely in the Claude Code skill-mode ecosystem: its `modes/*.md` files follow the same SKILL.md-based skill pattern used by [[obra-superpowers]] and [[anthropics-skills]], and it uses identical multi-harness wrapper files (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`) to support 7 AI CLIs from a single codebase. Like [[gsd-build-get-shit-done]], it exposes a slash-command interface over a structured agentic pipeline with persistent Markdown-based state — but the domain is job search rather than software development. The Playwright-based portal scanning is the same browser automation approach used in [[microsoft-playwright-mcp]], and the batch processing architecture (headless `claude -p` workers + orchestrator script) mirrors the multi-agent execution patterns documented in [[anthropic.com-managed-agents]].
