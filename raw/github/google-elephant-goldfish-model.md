# google/elephant-goldfish-model

## Metadata
- Stars: 3880
- Forks: 244
- Primary language: Python
- Default branch: main
- Latest release: v0.1.0 (2026-10-27)
- License: Apache License 2.0
- Homepage: https://egm.dev
- Fetched: 2026-10-28
- Final URL: https://github.com/google/elephant-goldfish-model

## Description
Open-source skills for designing and reviewing software with AI agents

## README
<p align="center">
  <a href="https://egm.dev"><img src="docs/assets/readme-header.svg" width="480" height="116" alt="Elephant-Goldfish Model"></a>
</p>

<p align="center">Design with an elephant. Review with a goldfish.</p>

<p align="center">
  <a href="#install">Install</a> &ensp;·&ensp;
  <a href="#try-your-first-design">Quickstart</a> &ensp;·&ensp;
  <a href="docs/getting_started.md">Documentation</a> &ensp;·&ensp;
  <a href="https://egm.dev">Website</a>
</p>

<br>

Thousands of Google engineers use EGM, an open-source plugin, to draft specs with deep-context agents and stress-test them with zero-context subagents before writing code.

**Elephant** holds your project context and drafts the specification. **Goldfish** reviewers examine the draft and referenced source material without the earlier conversation, helping expose unstated assumptions and blind spots. **You** make the architectural trade-offs and approve the specification before implementing.

Use it when a feature needs design decisions before implementation. For a small, clear bug fix, use your normal coding workflow.

## Install

Choose your coding agent. Install the complete plugin so its skills can read the reviewer prompts and document standards.

### Antigravity

```sh
agy plugin install https://github.com/google/elephant-goldfish-model
```

### Claude Code

```sh
claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm
```

### Codex

```sh
codex plugin marketplace add google/elephant-goldfish-model
codex plugin add egm@egm
```

Start a new session after installation. For **Claude Cowork** and **ChatGPT Work**, see the [setup guide](docs/harnesses.md).

## Try your first design

Open your project in your coding agent and choose a feature that needs design decisions. This example adds webhook delivery: what should happen when a delivery fails, or the same event arrives twice?

The commands below are shown without a prefix. In Antigravity (agy CLI) and Claude Code, add the `/egm:` prefix, for example `/egm:egm-brainstorm`. In Codex, select the corresponding EGM skill from the skill picker. Brainstorming and review require a session that can create fresh subagents.

<img src="skills/egm-brainstorm/assets/icon.svg" width="20" height="20" align="top" alt=""> **Explore the idea**

```text
/egm-brainstorm Add webhook delivery to this project.
```

Discuss requirements and trade-offs with the agent. Fresh reviewers challenge the proposal, and the agent saves the agreed direction in `concepts_brief.md`.

<img src="skills/egm-draft/assets/icon.svg" width="20" height="20" align="top" alt=""> **Draft the specification**

```text
/egm-draft
```

The agent turns the brief into `design_draft.md`, pausing after each section for your feedback in chat.

<img src="skills/egm-review/assets/icon.svg" width="20" height="20" align="top" alt=""> **Review the draft**

```text
/egm-review design_draft.md
```

Use the draft path returned by the agent.

Fresh reviewers check the design, its clarity, its fit with the code, and its implementation plan. Choose which findings to address. When you approve the design, ask your coding agent to implement it.

See the [workflow guide](docs/getting_started.md) for the full process, including saving approved specifications under `docs/designs/`.

## How it works

<table>
  <thead><tr><th align="left">Role</th><th align="left">Context</th><th align="left">Responsibility</th></tr></thead>
  <tbody>
    <tr valign="top"><td><strong>Elephant</strong></td><td>Your project, requirements, and earlier decisions</td><td>Explore the problem and draft the specification.</td></tr>
    <tr valign="top"><td><strong>Goldfish</strong></td><td>The document and its referenced source material, without the earlier conversation</td><td>Find missing assumptions, unclear requirements, and implementation risks.</td></tr>
    <tr valign="top"><td><strong>You</strong></td><td>The goals and constraints that matter</td><td>Resolve trade-offs, approve the design, and decide what to build.</td></tr>
  </tbody>
</table>

Goldfish reviews require fresh subagent contexts. If your agent cannot create them, EGM stops the review. A review does not replace tests or human judgment. See [supported environments and verification limits](docs/harnesses.md#support-status--contributing-other-harnesses).

## Choose a skill

You can use each skill when you need it. You do not have to follow the full sequence.

<table>
  <thead><tr><th align="left">Skill</th><th align="left">Use it to…</th></tr></thead>
  <tbody>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-brainstorm/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-brainstorm/SKILL.md">Brainstorm</a></td><td>Test an idea and write a concept brief.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-draft/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-draft/SKILL.md">Draft</a></td><td>Turn a brief or existing notes into a design document.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-resolve/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-resolve/SKILL.md">Resolve</a></td><td>Work through review findings and agree on changes.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-bootstrap/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-bootstrap/SKILL.md">Bootstrap</a></td><td>Create or update documentation for an existing codebase.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-review/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-review/SKILL.md">Review</a></td><td>Review a design with fresh agents across five stages.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-review-loop/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-review-loop/SKILL.md">Review&nbsp;loop</a></td><td>Run a configured group of reviewers for a specific review task.</td></tr>
    <tr valign="top"><td width="160" valign="top"><img src="skills/egm-drift-report/assets/icon.svg" width="20" height="20" alt="" align="top">&nbsp;<a href="skills/egm-drift-report/SKILL.md">Drift&nbsp;report</a></td><td>Compare checked-in documents with the current source code.</td></tr>
  </tbody>
</table>

## Learn more

- [Getting started](docs/getting_started.md): the workflow and project layout.
- [Setup](docs/harnesses.md): installation, agent capabilities, and known limits.
- [Architecture](https://github.com/google/elephant-goldfish-model/blob/main/docs/designs/architecture.md): how skills and reviewers fit together.
- [Testing](https://github.com/google/elephant-goldfish-model/blob/main/TESTING.md): checks, execution records, and verification limits.
- [Dave Rensin’s original essay](https://medium.com/@drensin/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874): the ideas behind EGM.

## Contribute

Read [contributing](https://github.com/google/elephant-goldfish-model/blob/main/CONTRIBUTING.md) for PRs, [issues](https://github.com/google/elephant-goldfish-model/issues) for bugs, and [discussions](https://github.com/google/elephant-goldfish-model/discussions) for questions.

## License

[Apache 2.0](LICENSE). This is not an officially supported Google product.

## Docs

### docs/getting_started.md — EGM Setup & Workflow Guide

The Elephant-Goldfish Model (EGM) is an implementation of Spec-Driven Development (SDD) based on Dave Rensin's essay *Elephants, Goldfish, and the New Golden Age of Software Engineering*. Recommendation: practice the conversational philosophy before relying on the packaged skills.

**Runtime:** skills and personas ship as a plugin for Antigravity, Claude Code, Claude Cowork, OpenAI Codex, and ChatGPT Work (see harnesses.md). Skills live in `skills/`; personas in `agents/`.

**Core loop (fluid — skills may be used out of order):**
1. `/egm-brainstorm` — clarify concept; spawn 6-lens Goldfish swarm; write `concepts_brief.md`
2. `/egm-draft` — turn brief into formal design under `docs/designs/`, section by section
3. `/egm-review` — multi-stage zero-context review for completeness, clarity, self-containment, readiness
4. Human review via PR — EGM does not replace human oversight
5. Implement against the approved design doc

**Drift:** `/egm-drift-report` compares design docs to code; recommended weekly.

**Bootstrap existing codebases:** recommended layout uses `docs/designs/` (with SITEMAP.md) and optional `_agents/skills/<project>_elephant`. `/egm-bootstrap` generates bottom-up recursive README.md trees (leaf → parent → root) for Elephant navigation. Optional project-context skill points LLMs at key docs and designs.

### docs/harnesses.md — Harnesses

One set of skills/personas; this repo is the plugin source for each harness (no forked skill text).

**Install (must install whole plugin — skill-only copies break runtime reads of `agents/` and `resources/document_standards/`):**
| Harness | Install |
| --- | --- |
| Antigravity | `agy plugin install https://github.com/google/elephant-goldfish-model` |
| Claude Code | `claude plugin marketplace add google/elephant-goldfish-model && claude plugin install egm@egm` |
| Claude Cowork | claude.ai/plugins or Cowork panel via marketplace `google/elephant-goldfish-model` |
| Codex | `codex plugin marketplace add google/elephant-goldfish-model && codex plugin add egm@egm` |
| ChatGPT | Personal: Plugins > Add > Upload archive; Workspace: Admin > Plugins > Import marketplace, path `.agents/plugins` |
| omp | `omp plugin marketplace add google/elephant-goldfish-model && omp plugin install egm@egm` |

Root `plugin.json` is canonical Agent Plugins 1.0.0 identity (omit `$schema` for omp compatibility). Marketplace files are discovery catalogs. Persona prompts in `agents/` register as named subagents where the harness supports it.

**Support status:** Antigravity, Claude Code, and Codex pass automated install/isolation/E2E fixtures. Claude Cowork (#105) and ChatGPT Work (#106) have install paths with open cloud trace gaps. omp (#186) has working install; E2E fixtures not yet automated.

**Artifact directory:** skills write to working dir or harness artifact dir; can set `EGM artifact directory: .dev/docs` in prompts/AGENTS.md/CLAUDE.md.

### docs/directory.md — Directory packages

`python3 scripts/pack_plugin.py --target claude|openai --output /tmp/egm-release` builds deterministic runtime folder+ZIP (stdlib only). Allowlist includes skills, personas, standards, runtime guides, manifests, icons; excludes site, tests, workflows, marketplace catalogs, hooks, build tools. Claude retain adapters; OpenAI excludes Claude components. Anthropic directory package checked in at `distributions/claude`.

### docs/designs/architecture.md — EGM Architecture & System Lifecycle

Authors: Jim Quinn (@quinnjim), Elise Ewing (@eewing314), Dave Rensin (@drensin). Status: Current. Date: 2026-06-06.

**Problem:** unstructured conversational codegen fails via (1) hallucination cascades / context pollution, (2) premature implementation, (3) chat dump fatigue, (4) documentation drift.

**Principles:** Elephant (deep-context draft) + Goldfish (zero-context review); human ownership of trade-offs; artifact-first UX; living specs in `docs/designs/`.

**Four subsystems:**
1. Skills Layer (`skills/`) — brainstorm, draft, review, review-loop, resolve, drift-report, bootstrap
2. Personas Layer (`agents/`) — Comprehension, Design Critic, Implementation Readiness, Codebase Auditor, Structural Validator, Style Editor, Synthesizer (+ zoom-out)
3. Document Standards (`resources/document_standards/`) — versioned rubrics
4. Living Documentation (`docs/`)

**Lifecycle:** brainstorm → draft → multi-stage Goldfish review (zoom-out, comprehension, critic, readiness via synthesizer fan-out/fan-in) → human PR → implement + periodic drift report.

**Artifact-first UX:** forbid dumping large drafts into chat; write workspace/side-panel artifacts; yield for checkpoints.

### docs/faq.md (excerpt)

Alternatives exist; EGM is one approach. Core artifacts: design doc, implementation checklist, enriched README context. Humans stay responsible for outcomes. Prefer EGM for important/uncertain changes, not every bug. Design completeness for zero-context agents is aspirational — use judgment like coaching a junior engineer.

### TESTING.md — EGM Testing Playbook

- Offline unit tests: `pytest tests/unit` (frontmatter schemas, link integrity, plugin manifests, marketplace paths). Needs Python 3.10+.
- Opt-in live Claude: `EGM_CLAUDE_LIVE=1 pytest tests/integration/test_claude.py` (Claude Code 2.1.271+)
- Opt-in live Codex: `EGM_CODEX_LIVE=1 pytest tests/integration/test_codex.py`
- Harness test record (2026-10-22..27): Antigravity CLI 1.4.5, Claude Code 2.1.308, Claude Cowork (partial), OpenAI Codex 0.163.0, ChatGPT Work, omp v18.12.6 (community install verification)

### AGENTS.md — Agent Guidelines

No autonomous PRs without human review. Triage taxonomy: Bug Fix/Minor Patch (≤100 non-test lines, <3 core files); Feature Stage 1 Design Doc PR; Feature Stage 2 Implementation PR. No artificial PR splitting. Fill `.github/PULL_REQUEST_TEMPLATE.md`.

### plugin.json

```json
{
  "name": "egm",
  "version": "0.1.0",
  "description": "Draft specs, review designs, and check implementation drift.",
  "author": { "name": "Google" },
  "homepage": "https://egm.dev",
  "repository": "https://github.com/google/elephant-goldfish-model",
  "license": "Apache-2.0"
}
```

### Skill SKILL.md frontmatter (descriptions)

| Skill | Description |
| --- | --- |
| egm-brainstorm | Interactive ideation; clarifying questions + Goldfish review → `concepts_brief.md` |
| egm-draft | Section-by-section design doc from brief/notes → `design_draft.md` / `docs/designs/` |
| egm-review | Five-phase Goldfish review: Zoom Out, Comprehension, Design Critique, Intermediate Zoom Out, Implementation Readiness |
| egm-resolve | Ingest Goldfish findings; propose fixes; interactive negotiation in Elephant context |
| egm-bootstrap | Recursive bottom-up README generation across a repo subtree |
| egm-review-loop | Configured concurrent reviewer group for a specific review task |
| egm-drift-report | Compare design docs/READMEs to current source; actionable drift report |

All skills set `disable-model-invocation: true` and `license: Apache-2.0`.

## Top-level structure
- `.agents/` — Codex/ChatGPT marketplace catalog under `plugins/` (discovery, not skill copies)
- `.claude-plugin/` — Claude marketplace.json, plugin.json, agent adapters, icon
- `.codex-plugin/` — Codex plugin.json
- `.github/` — workflows, PR template (boilerplate; not fetched in depth)
- `AGENTS.md` — contributor agent guidelines (no autonomous PRs; design-doc PR stages)
- `AI_POLICY.md` — AI contribution policy
- `CONTRIBUTING.md` — PR process
- `TESTING.md` — unit/integration/harness test playbook
- `agents/` — Goldfish persona prompts: bootstrap_orchestrator, codebase_details, comprehension, design_critic, implementation_readiness, structural, style, synthesizer, zoom_out
- `assets/` — plugin icon.svg
- `distributions/` — checked-in Claude directory package (`claude/`)
- `docs/` — getting_started, harnesses, directory, faq, privacy, releases, claude.md, codex.md, index; `docs/designs/` architecture + per-skill design docs
- `plugin.json` — canonical portable Agent Plugins 1.0.0 manifest (egm v0.1.0)
- `pyproject.toml` / `requirements-dev.txt` — pytest config and test deps
- `resources/` — document_standards (feature-spec, heilmeier, implementation-readiness, re-implementation, zoom-out), execution_instructions.md
- `scripts/` — pack_plugin.py, prepare_release.py
- `site/` — Astro marketing site for egm.dev
- `skills/` — seven EGM skills (each with SKILL.md, TEST.md, agents/, assets/, test_scenarios.yaml)
- `tests/` — unit/ and integration/ suites
