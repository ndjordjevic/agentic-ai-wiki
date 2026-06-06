---
type: source
source_url: https://github.com/Agent-Field/pr-af
tags:
  - pr-review
  - multi-agent
  - agentfield
  - evidence-grounding
  - ci-cd
  - github-actions
  - adversarial-review
  - ast-verification
  - compound-risks
related:
  - everyinc-compound-engineering-plugin
  - qa.tech
  - garrytan-gstack
  - openrouter.ai
product: pr-af
detail_level: standard
created: 2026-06-06
updated: 2026-06-06
---

PR-AF is an open-source, AgentField-native pull request reviewer that builds a custom multi-agent review strategy for every PR instead of running a single LLM pass with a fixed checklist. It dynamically compiles review dimensions from the diff topology, spawns parallel reviewer agents with runtime-crafted prompts, grounds findings with programmatic AST extraction, challenges its own claims adversarially, synthesizes compound cross-file risks, and posts evidence-backed inline GitHub comments. A deep review of a ~500-line PR costs roughly $0.80 in BYOK LLM calls and typically runs 35–50 minutes — positioning it as a CI/CD gatekeeper for architectural depth rather than fast inner-loop feedback.

_All claims below are sourced from ../../raw/github/agent-field-pr-af.md unless otherwise noted._

## What it does

PR-AF accepts a GitHub PR URL (or diff-only / local-repo modes), fetches full PR context via the GitHub API, and executes a seven-phase adaptive pipeline on the AgentField control plane. Unlike static review bots, the planner is a meta-prompting `.harness()` that reasons about what aspects of *this specific PR* need scrutiny — auth changes get security-focused reviewers, logging refactors get consistency reviewers — with no hardcoded reviewer categories. Findings that cannot be irrefutably grounded in extracted code are silently pruned; survivors pass a falsifiability gate before becoming inline comments. Output includes structured JSON (severity, file, line, evidence, compound-risk links) and posted GitHub review annotations.

## Installation

```bash
git clone https://github.com/Agent-Field/pr-af.git && cd pr-af
cp .env.example .env          # Add OPENROUTER_API_KEY, GH_TOKEN
docker compose up --build
```

Starts the AgentField control plane at `http://localhost:8080` plus the PR-AF agent. Requires Python 3.11+, Docker, an OpenRouter API key, and a GitHub token with PR read/write permissions.

## Key features

- **Dynamic review dimensions** — planner generates N parallel reviewer prompts at runtime from PR anatomy; no fixed security/performance/style checklist.
- **Evidence grounding** — AST extraction engine pulls caller snippets and import contexts; unsubstantiated LLM claims are pruned before surfacing.
- **Compound vulnerability synthesis** — clusters isolated anomalies across files (e.g. exposed API key + DB merge bug) into coordinated high-severity findings.
- **Adversarial falsifiability gates** — dedicated adversary agent attempts to invalidate each finding before it reaches the developer.
- **AI-generated PR awareness** — intake classifier scores AI-authorship confidence and adjusts review plan (hallucination checks, over-abstraction scrutiny).
- **Three input modes** — full GitHub PR URL, diff-only lightweight, or local repo + branch refs.
- **Multiple output formats** — GitHub inline review, structured JSON, SARIF, Markdown report.
- **Budget management** — per-phase cost caps, model routing (budget/mid/premium tiers), hard loop limits on reference-follows and coverage iterations.
- **One-call DX** — `af call pr-af.review --in '{"pr_url": "..."}'` via AgentField CLI (af ≥ 0.1.87) with live progress streaming.

## Architecture

The pipeline has seven phases: (1) **Intake** — `.ai()` classification with `.harness()` fallback for ambiguous PRs; (2) **Anatomy** — programmatic diff parsing + blast-radius computation (code) plus semantic narrative understanding (`.harness()`); (3) **Planning** — meta-prompting planner crafts all reviewer dimensions; (4) **Parallel review** — N generic `.harness()` reviewers consume dynamically crafted prompts; (5) **Review layer** — cross-reference resolver, adversary, and coverage gate consume a streaming findings queue; (6) **Synthesis** — deterministic scoring (code); (7) **Output** — line mapping, comment formatting, GitHub API posting (code).

Source layout under `src/pr_af/`: `orchestrator.py` (phase coordination), `diff_engine.py` and `blast_radius.py` (pure code, no LLM), `agents/` (intake, anatomy, planner, reviewer, cross_ref, adversary, coverage, gap_reviewer), `schemas/` (Pydantic models for gates and pipeline), `github/` (API client, diff parser), `scoring.py` (deterministic severity), `config.py` (model assignments, budget caps, behavioral tuning). PR-AF is built on [AgentField](https://github.com/Agent-Field/agentfield) primitives: `.ai()` for flat-schema gates, `.harness()` for multi-turn code navigation.

Three nested control loops (inner per-reviewer adaptation, middle cross-agent deep-dives, outer coverage iterations) each have hard caps to prevent unbounded cost. Model routing philosophy: budget models for gates/classification, premium models for planner, reviewers, cross-ref, and adversary.

## Example usage

**AgentField CLI (recommended):**

```bash
af call pr-af.review --in '{"pr_url": "https://github.com/owner/repo/pull/123"}'
```

**HTTP API:**

```bash
curl -X POST http://localhost:8080/api/v1/execute/async/pr-af.review \
  -H "Content-Type: application/json" \
  -d '{"input": {"pr_url": "https://github.com/owner/repo/pull/123"}}'

curl http://localhost:8080/api/v1/executions/<execution_id>
```

**GitHub Actions (label-triggered):** add workflow at `.github/workflows/pr-af-review.yml`; triggers when the `pr-af` label is applied to a PR. Checks out PR-AF, starts `docker compose`, runs `python3 scripts/ci_runner.py` with `GITHUB_TOKEN` and `OPENROUTER_API_KEY`.

## Maintenance status

28 stars, 2 forks. Default branch `main`. No published releases yet. Apache 2.0 license. Python 99.2%. Last pushed 2026-06-05. Built by Agent-Field; README recommends pairing with Claude Code for local development and PR-AF as the final GitHub Actions architectural gate.

## Ecosystem

PR-AF runs on the AgentField control plane (`agentfield.dev`); requires `OPENROUTER_API_KEY` for LLM routing. README positions it against Claude Code CLI (fast inner loop) and commercial SaaS reviewers (CodeRabbit, Codex) — PR-AF targets deep CI/CD audits with extremely low false positives at the cost of 35–50 minute runs. Related resources in this wiki: [[everyinc-compound-engineering-plugin]] (multi-agent tiered code review for Claude Code), [[qa.tech]] (AI-powered PR testing and validation layer), [[garrytan-gstack]] (sprint pipeline with `/review` step), [[openrouter.ai]] (BYOK unified API gateway used for LLM calls).
