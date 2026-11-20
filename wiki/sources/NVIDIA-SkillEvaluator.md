---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://github.com/NVIDIA/SkillEvaluator
tags:
  - skill-evaluation
  - agent-skills
  - quality-gates
  - harness-check
  - live-agent-eval
  - ci-templates
  - skill-deduplication
  - nvidia
related:
  - nvidia-skillspector
  - edonadei-caliper
  - skills.sh
  - anthropics-skills
  - nvidia.com
product: skillevaluator
detail_level: standard
created: 2026-11-20
updated: 2026-11-20
studied: true
---

NVIDIA/SkillEvaluator (4,189★, Apache-2.0, PyPI `skillevaluator` v1.0.1) is a multi-tier framework for evaluating AI agent skills and plugins: static quality/security/harness gates, semantic overlap detection, synthetic eval dataset generation, and live with/without-skill agent runs that measure Skill Lift. It ships reusable GitHub/GitLab CI templates and an installable agent skill, and is part of the NVIDIA Verified Skills pipeline alongside [[nvidia-skillspector]].

_All claims below are sourced from ../../raw/github/NVIDIA-SkillEvaluator.md unless otherwise noted._

## What it does

SkillEvaluator checks Agent Skills–spec folders (`SKILL.md` plus supporting files) before merge and measures whether a skill improves real agent task results. Tier 1 runs 500+ static rules and detection patterns (quality, schema, version, PII, license, Unicode, script linting, harness compatibility, security via SkillSpector/Gitleaks/Bandit/optional Semgrep, optional dependency audit). Tier 2 finds repeated guidance inside a skill or overlap across a catalog. Tier 3 runs the same tasks with and without the skill in a sandbox (Harbor by default; NeMo Gym optional) and reports Skill Lift. Operators can run the CLI, add CI via `skillevaluator ci init` or copied templates, or install the bundled skill and ask an agent to evaluate another skill.

## Installation

Python 3.12–3.14. Lightweight CLI (Tier 1 quality / basic static):

```bash
pip install skillevaluator
# or
uv tool install --python 3.13 skillevaluator
```

All tiers (embeddings/chat + Harbor live eval + security extras):

```bash
pip install "skillevaluator[all]"
# or
uv tool install --python 3.13 --reinstall "skillevaluator[all]"
```

GitHub source installs and scanner/Docker/provider setup are documented under Installation / Installation Options. Docs: https://docs.nvidia.com/skills/skillevaluator/.

## Key features

- **Three independent tiers** — Validation (Tier 1), Deduplication (Tier 2), Live Agent Evaluation (Tier 3); `skillevaluator validate` runs the combined pipeline with autopilot for skills.
- **Harness Check** — no API key or agent run; versioned profiles report whether Codex, Claude Code, OpenCode, Hermes, OpenClaw, Copilot CLI, etc. will load the skill (description length limits, scan paths).
- **CI templates** — GitHub Actions and GitLab skill-check bundles (`ci/bundles/`), optional PR comments and hosted report publisher; guided setup via `skillevaluator ci init`.
- **Agent skill** — `npx skills add NVIDIA/SkillEvaluator` installs `skills/skillevaluator` so coding agents can run evaluations on request.
- **Reports** — CLI, JSON, HTML outputs; optional Streamlit performance dashboard extra; publication-evidence status can stay `INCOMPLETE` until scanners/LLM stages run.
- **Research** — arXiv 2608.20614; CITATION.cff for paper + release/commit citation.

## Architecture

Python package under `src/skillevaluator/` with a large Click CLI (`cli.py`), Tier1/2/3 packages, harness profiles, deduplication/embedding, evaluation/reporting, and many `plugin_*` modules for discovery, manifests, MCP, permissions, and risk. Base install stays static-validation capable (Bandit + uv for SkillSpector provisioning in 1.0.1); LLM clients, Harbor (`harbor[gke]==0.25.0`), and pip-audit live behind extras. Docs are Fern MDX under `docs/` published to docs.nvidia.com; `ci/` owns reusable workflows and report plumbing; `skills/skillevaluator/` is the agent-facing skill; Harbor powers sandboxed Tier 3 runs and [[nvidia-skillspector]] provides specialized skill security scanning inside Tier 1.

## Example usage

```bash
# Keyless quality score (bundled example after clone)
skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality

# Harness compatibility
skillevaluator harness-check ./my-skill

# Tier 1 static only
skillevaluator tier1 ./my-skill --no-llm -o reports/tier1

# Full validate (needs provider + scanners; Docker for Tier 3)
export SKILL_EVAL_LLM_PROVIDER=nv_build
export NVIDIA_API_KEY='nvapi-...'
skillevaluator doctor --env-mode docker
skillevaluator validate ./my-skill

# CI onboarding in a skills repo
skillevaluator ci init
```

## Maintenance status

4,189 stars, 545 forks, Apache-2.0, default branch `main`, latest release **v1.0.1** (2026-11-18), last push 2026-11-20. Support level is **Experimental** (community best-effort, no SLA). Homepage/docs at https://docs.nvidia.com/skills/skillevaluator/; PyPI package `skillevaluator`. Peer measurement tools in this wiki include [[edonadei-caliper]]; distribution/discovery sits with [[skills.sh]] and the Agent Skills pattern illustrated by [[anthropics-skills]].
