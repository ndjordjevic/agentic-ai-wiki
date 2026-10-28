---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://github.com/google/elephant-goldfish-model
tags:
  - elephant-goldfish-model
  - spec-driven-development
  - goldfish-review
  - agent-skills
  - design-docs
  - zero-context-subagents
  - multi-harness-plugin
  - drift-detection
related:
  - github-spec-kit
  - openspec.dev
  - traycer.ai
  - buildermethods-agent-os
  - obra-superpowers
  - gsd-build-get-shit-done
  - othmanadi-planning-with-files
  - bmad-code-org-bmad-method
  - skills.sh
product: elephant-goldfish-model
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Elephant-Goldfish Model (EGM) is Google's open-source Agent Skills plugin (~3.9k★, Apache-2.0, v0.1.0) for Spec-Driven Development: a deep-context **Elephant** drafts design specs, then fresh zero-context **Goldfish** subagents stress-test them before implementation. It installs as the `egm` plugin across Antigravity, Claude Code/Cowork, Codex, ChatGPT Work, and omp, with seven skills, nine reviewer personas, and checked-in living docs under `docs/designs/`. Homepage: [egm.dev](https://egm.dev). Not an officially supported Google product.

_All claims below are sourced from ../../raw/github/google-elephant-goldfish-model.md unless otherwise noted._

## What it does

EGM packages a design-before-code workflow for coding agents. The Elephant holds project context, requirements, and earlier decisions while exploring and drafting. Goldfish reviewers see only the document and referenced source material—without the drafting conversation—to surface unstated assumptions, clarity gaps, and implementation risk. The human still owns architectural trade-offs and approval. Use it when a feature needs real design decisions; skip it for small, clear bug fixes.

## Installation

Install the **complete** plugin (skill-only copies break runtime reads of `agents/` and `resources/document_standards/`):

```sh
# Antigravity
agy plugin install https://github.com/google/elephant-goldfish-model

# Claude Code
claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm

# Codex
codex plugin marketplace add google/elephant-goldfish-model
codex plugin add egm@egm
```

Claude Cowork, ChatGPT Work, and omp have additional install paths documented in `docs/harnesses.md`. Start a new session after install. In Antigravity/Claude Code, slash commands use the `/egm:` prefix (e.g. `/egm:egm-brainstorm`); Codex uses the skill picker.

## Key features

- **Seven skills:** `egm-brainstorm` (concept → `concepts_brief.md` via clarifying questions + 6-lens Goldfish swarm), `egm-draft` (section-by-section design doc), `egm-review` (multi-stage Goldfish review), `egm-resolve` (triage findings in Elephant context), `egm-bootstrap` (bottom-up recursive README trees), `egm-review-loop` (configured concurrent reviewer groups), `egm-drift-report` (design/README vs code divergence).
- **Goldfish personas** in `agents/`: zoom-out, comprehension, design critic, implementation readiness, structural, style, codebase details, synthesizer, bootstrap orchestrator.
- **Document standards** under `resources/document_standards/` (feature-spec, heilmeier, implementation-readiness, re-implementation, zoom-out) that reviewers load as rubrics.
- **Artifact-first UX:** long drafts and review reports go to workspace/side-panel files, not chat dumps; optional `EGM artifact directory:` hint.
- **Living specs:** approved designs live under `docs/designs/`; drift skill recommended weekly.
- **Portable plugin:** root `plugin.json` (Agent Plugins 1.0.0) plus harness-specific manifests under `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`.

## Architecture

Four decoupled subsystems: Skills (`skills/`), Personas (`agents/`), Document Standards (`resources/document_standards/`), and Living Documentation (`docs/`). The architecture design doc frames failure modes EGM targets—hallucination cascades / context pollution, premature coding, chat-dump fatigue, and documentation drift—and a five-phase lifecycle: brainstorm → draft → isolated multi-stage review (zoom-out → comprehension → critic → readiness, with synthesizer fan-out/fan-in) → human PR → implement + periodic drift checks. Semantic boundaries in drafts separate high-level feature range from detailed implementation range so reviewers can target the right lens. Harnesses share one skill/persona text; this repo is the single plugin source (no forked skill trees).

## Example usage

```text
/egm-brainstorm Add webhook delivery to this project.
/egm-draft
/egm-review design_draft.md
```

Brainstorm and review require a harness that can spawn fresh subagents; same-context review is rejected as not a Goldfish review. After approval, ask the coding agent to implement against the design (typically saved under `docs/designs/`). Skills may be used out of order when that fits the bottleneck.

## Maintenance status

~3,880 stars, 244 forks; primary language Python (tests/packaging); default branch `main`; latest release **EGM v0.1.0** (2026-10-27); Apache-2.0. Homepage https://egm.dev (Astro site in `site/`). Authors of the architecture design include Jim Quinn, Elise Ewing, and Dave Rensin (essay originator). Offline unit tests via `pytest tests/unit`; opt-in live Claude/Codex integration probes. Harness fixture record covers Antigravity, Claude Code, and Codex as passing; Cowork/ChatGPT Work have open cloud verification gaps; omp has community install verification. Contribution policy forbids autonomous agent PRs and uses staged design-doc then implementation PRs for larger changes.
