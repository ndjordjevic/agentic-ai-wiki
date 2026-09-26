---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/rohitg00/ai-engineering-from-scratch
tags:
  - ml-education
  - build-it-use-it
  - agent-engineering
  - llms-from-scratch
  - mcp-curriculum
  - agent-skills-curriculum
  - i18n-pipeline
related:
  - fastai-fastbook
  - anthropics-skills
  - shareai-lab-learn-claude-code
product: ai-engineering-from-scratch
detail_level: standard
created: 2026-09-26
updated: 2026-09-26
---

AI Engineering from Scratch is a free, MIT-licensed, 523-lesson curriculum (20 phases, ~342 hours) spanning linear algebra and backpropagation through transformers, LLM engineering, and multi-agent swarms, implemented from raw math in Python, TypeScript, Rust, and Julia before showing the same concept in a production library. For the agentic-AI wiki it is notable as a rare end-to-end on-ramp: phases 13–16 (Tools & Protocols, Agent Engineering, Autonomous Systems, Multi-Agent & Swarms) teach MCP, Agent Skills, the agent loop, and swarm coordination with the same "build it from scratch, then use the framework" discipline applied to matrix math and attention earlier in the course, and the whole thing installs and runs itself as an Agent Skill inside a coding agent.

_All claims below are sourced from ../../raw/github/rohitg00-ai-engineering-from-scratch.md unless otherwise noted._

## What it does

The repo is a self-contained curriculum: 523 lessons across 20 phases (`phases/00-setup-and-tooling/` through `phases/19-capstone-projects/`), each lesson a folder with `code/` (runnable implementations), `docs/en.md` (the lesson narrative), and `outputs/` (the prompt, skill, agent, or MCP server the lesson produces). Every lesson follows a six-beat structure — Motto, Problem, Concept, Build It (raw math, no frameworks), Use It (the same thing in PyTorch/sklearn/etc.), Ship It (a reusable artifact). It doubles as an installable Agent Skill: `npx skills add rohitg00/ai-engineering-from-scratch` installs `start-learning`, `learn`, `course-guide`, `learn-mcp`, `learn-agent-skills`, `check-understanding`, and certification-tutor skills into Claude Code, Cursor, Codex, or other skill-capable hosts, so the course can teach itself one lesson per session inside the reader's own coding agent.

## Installation

Two independent installers, since the learning skills and the lesson artifacts serve different purposes:

```bash
# Learning skills (start-learning, learn, course-guide, learn-mcp, learn-agent-skills,
# check-understanding, certification tutors) — needs Node.js/npx only, no clone
npx skills add rohitg00/ai-engineering-from-scratch

# Lesson artifacts (396 skills + 99 prompts under phases/**/outputs/) — needs a clone
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
python3 scripts/install_skills.py <target>                # default: skills/, nested SKILL.md layout
python3 scripts/install_skills.py <target> --type all      # skills + prompts + agents
python3 scripts/install_skills.py <target> --phase 14       # one phase only
python3 scripts/install_skills.py <target> --tag rag        # filter by tag
```

`install_skills.py` refuses to overwrite an existing destination by default (`--force` to overwrite, `--dry-run` to preview) and writes a `manifest.json` inventory on every real run. Running a lesson locally needs only `python3` and, per-lesson, whatever the lesson's own `code/` requires (stdlib for most early lessons).

## Key features

- **523 lessons, 20 phases, ~342 hours** — Setup → Math Foundations → ML Fundamentals → Deep Learning Core → Computer Vision / NLP / Speech & Audio → Transformers → Generative AI → Reinforcement Learning → LLMs from Scratch → LLM Engineering → Multimodal AI → Tools & Protocols (MCP) → Agent Engineering → Autonomous Systems → Multi-Agent & Swarms → Infrastructure & Production → Ethics/Safety/Alignment → Capstone Projects.
- **Build It / Use It split** — every lesson implements the algorithm from raw math first (backprop, tokenizer, attention, agent loop), then runs the same concept through the production library, so the reader knows what the framework abstracts away.
- **Curated learning paths** — JSON manifests (`learning-paths/`) thread a subset of lessons into a themed route: a 17-lesson [Model Context Protocol (MCP) path](https://aiengineeringfromscratch.com/lesson?path=phases/13-tools-and-protocols/06-mcp-fundamentals&learningPath=model-context-protocol) (~23h) covering stateless requests, transports, bidirectional work, security, reliability, registry governance, and conformance; a five-lesson Agent Skills path (~9.5h) covering contract, discovery, invocation, sandboxing, and release evals; plus "Agent-Assisted Engineering" and "Product Judgment and Delivery" tracks.
- **Certification tracks** — `certifications/claude/` and `certifications/mcpa/` prepare readers for a Claude certification and the MCP Associate (MCPA) exam respectively, each with its own onboarding guide and tutor skill (`claude-certification`, `mcpa-certification`).
- **Self-verifying tooling** — `scripts/build_catalog.py` derives `catalog.json` (every phase/lesson/artifact) straight from disk so course counts can't drift from what's actually there; `scripts/audit_lessons.py` enforces ten invariant rules (directory shape, `docs/en.md` presence, non-empty `code/`, `quiz.json` schema, valid relative links) and is wired into CI; `scripts/lesson_run.py` byte-compiles every lesson's Python for syntax regressions, with an opt-in `--execute` mode (10s timeout per lesson).
- **Agent Workbench capstone** — the Phase 14 capstone ships a reusable multi-surface Agent Workbench pack (`AGENTS.md`, schemas, init/verify/handoff scripts) that `scripts/scaffold_workbench.py` can drop into any repo, wiring up a starter `task_board.json` and `agent_state.json`.
- **Free machine translation pipeline** — lesson prose (not code, math, or metadata) is translated by NLLB-200 inside GitHub Actions at zero API cost, published to a separate `translations` branch and fetched at runtime with English fallback; the README itself is hand-translated into 12 languages and committed to `main` (see `docs/i18n.md`).

## Architecture and concepts

Each lesson is a self-contained folder (`phases/<NN>-<phase-name>/<NN>-<lesson-name>/{code/, docs/en.md, outputs/}`), and the 20 phases form a dependency DAG rather than a strict line: Setup feeds Math Foundations, which feeds ML Fundamentals and then Deep Learning Core, which fans out into Computer Vision, NLP, Speech & Audio, and Reinforcement Learning; NLP feeds Transformers, which feeds Generative AI and LLMs from Scratch; LLMs from Scratch feeds LLM Engineering and Multimodal AI; LLM Engineering feeds Tools & Protocols, which feeds Agent Engineering, which fans out into Autonomous Systems, Multi-Agent & Swarms, and Infrastructure & Production — all converging on Capstone Projects. The i18n pipeline is a second, orthogonal architecture: `languages.json` is the single source of truth for which languages get machine-translated lessons versus hand-translated READMEs, a per-(language, phase) sha256 cache means only changed lessons are re-translated, and a placeholder-protection walker keeps code, math, and metadata headers byte-identical across translations (verified by an identity round-trip over all 523 lessons).

## Main APIs

The curriculum exposes itself through host-native skill invocations rather than a library API: `start-learning` (or `/start-learning` in Claude Code) runs a ten-question placement quiz and writes a personalized `LEARNING.md`; `learn` teaches one lesson per session (concept, math, code, quiz); `course-guide` jumps to the lesson covering a specific stuck point; `learn-mcp` and `learn-agent-skills` run the two focused learning paths; `check-understanding <phase>` quizzes a given phase. Script entry points (`build_catalog.py`, `install_skills.py`, `scaffold_workbench.py`, `audit_lessons.py`, `lesson_run.py`) are the tooling surface for maintainers and readers who prefer the CLI over the skill layer.

## When to use

Fits a reader who wants one spine from linear algebra to multi-agent production systems instead of scattered blog posts and papers — particularly useful for engineers who already use coding agents and want to understand what MCP, agent loops, and Agent Skills are actually doing underneath, since Phases 13–16 build those primitives from scratch before touching a framework. Senior engineers who only want the agent-engineering layer can start at Phase 14 directly (~60h) rather than working through the ML foundations.

## Maintenance status

57,698 GitHub stars, 10,047 forks. Default branch `main`. Latest release **v2026.09 "Edition 2026.09"** (2026-09-07). MIT license. Primary language: Python. Homepage: aiengineeringfromscratch.com. Maintained by Rohit Ghumare and the community; a GitHub Action (`curriculum.yml`) rebuilds and validates `catalog.json` on every PR and runs the lesson-audit script in warn-only mode for contributors.
