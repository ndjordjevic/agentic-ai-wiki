---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/bmad-code-org/BMAD-METHOD
tags:
  - agile-ai-development
  - structured-workflows
  - named-agents
  - skills-architecture
  - context-engineering
  - multi-agent
  - phase-driven-development
  - ide-integration
related:
  - obra-superpowers
  - coleam00-archon
  - gsd-build-get-shit-done
  - anthropics-skills
  - anombyte93-prd-taskmaster
  - factory.ai
  - othmanadi-planning-with-files
  - goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b
  - buildermethods-agent-os
  - the-new-sdlc-with-vibe-coding
product: bmad-method
detail_level: standard
created: 2026-05-22
updated: 2026-06-30
---

BMad Method (BMAD-METHOD) is a comprehensive, free, open-source Agile AI Driven Development framework with 47,851 stars that structures the entire software lifecycle — from brainstorming through deployment — as a progression of four phases, each powered by named AI agent personas and composable skill-based workflows. Where most AI coding tools respond to ad hoc prompts, BMad enforces structured methodology: analysis produces briefs and PRFAQs, planning produces a PRD, solutioning produces architecture and stories, and implementation executes stories one at a time with full traceability. The framework ships as an npm package (`npx bmad-method install`) that installs into any AI IDE (Claude Code, Cursor, Windsurf, and others) and is extended via official modules for testing, game dev, and creative workflows.

_All claims below are sourced from ../../raw/github/bmad-code-org-bmad-method.md unless otherwise noted._

## What it does

BMad Method provides a structured, agent-assisted development process grounded in agile best practices. Six named agent personas — Mary (Analyst), Paige (Technical Writer), John (PM), Sally (UX Designer), Winston (Architect), and Amelia (Developer) — each own a phase and a menu of workflow skills. Each workflow produces a specific artefact (`prd.md`, `architecture.md`, `story-[slug].md`, etc.) that serves as structured context for the next phase, preventing the context rot and inconsistent decisions that emerge from ad hoc prompting. The system is scale-domain-adaptive: it automatically adjusts planning depth from bug-fix-level quick flows up to full enterprise project planning.

## Key features

- **Four-phase lifecycle**: Analysis (optional) → Planning → Solutioning → Implementation, with explicit phase documents that chain together as context
- **34+ named workflow skills** covering brainstorming, market/domain/technical research, PRFAQ challenge, PRD creation/validation/update, UX design, architecture with ADRs, epic/story breakdown, implementation readiness gate, dev story execution, code review, sprint tracking, retrospective, and forensic investigation
- **`bmad-quick-dev`** — a unified quick flow that collapses all phases into one skill for small, well-understood tasks
- **Party Mode** (`bmad-party-mode`) — runs all agents simultaneously in one conversation; orchestrator picks the right persona per message for brainstorming, post-mortems, and architectural debates
- **`bmad-help` skill** — interactive guidance on what to do next, context-aware and updated when modules are added
- **Customisation stack** — team overrides via `_bmad/custom/*.toml` (committed) and personal `.user.toml` (gitignored); all agents and workflows inherit changes without source edits
- **Module ecosystem** — BMad Builder (BMB) for custom agent authoring; Test Architect (TEA) for risk-based testing; Game Dev Studio (BMGD); Creative Intelligence Suite (CIS)
- **Cross-IDE support** — ships `.claude-plugin/` and `.augment/` integrations; works with Claude Code, Cursor, Windsurf, and other AI IDEs

## Architecture

The framework is distributed as an npm package and installed into a project directory. The installer (`npx bmad-method install`) generates skill files under `.claude/skills/` (or the IDE equivalent), with one skill file per workflow and one per agent persona. Agent activation merges three TOML layers: the shipped `customize.toml`, a team overlay at `_bmad/custom/bmad-agent-{role}.toml`, and a personal `.user.toml` — resolved by a stdlib Python script at activation time.

Context flows through artefact files in a designated output directory (`_bmad-output/`). Each phase workflow reads the previous phase's output as input: the Architect reads `prd.md`; the Developer reads `architecture.md` and `story-[slug].md`. An optional `project-context.md` acts as a project constitution, generated once after architecture and loaded by every subsequent workflow. The `bmad-modules.yaml` manifest registers official and third-party modules; modules extend the skill set additively without modifying core files.

The agent activation flow has eight steps: resolve TOML overrides → run prepend steps → adopt persona → load persistent facts → load config → greet → run append steps → dispatch intent to menu item or present menu. Intent mapping is fuzzy: `"Hey Mary, let's brainstorm"` matches `bmad-brainstorming` (trigger `BP`) directly, skipping the menu.

## Installation

```bash
# Interactive installation
npx bmad-method install

# Non-interactive (CI/CD)
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes

# With module config overrides
npx bmad-method install --yes \
  --modules bmm --tools claude-code \
  --set bmm.project_knowledge=research \
  --set bmm.user_skill_level=expert
```

Prerequisites: Node.js ≥ 20.12, Python ≥ 3.10, `uv` package manager. After install, open the AI IDE in the project folder and invoke an agent or workflow skill directly.

## Example usage

```
# Activate the analyst agent and jump straight to brainstorming
Hey Mary, let's brainstorm

# Invoke a workflow skill directly
bmad-prd          ← create/update/validate the PRD
bmad-dev-story    ← implement the current story
bmad-quick-dev    ← quick flow for small/clear tasks
bmad-help         ← "what should I do next?"

# Party Mode — all agents in one room
bmad-party-mode
You: "Monolith or microservices for MVP?"
Architect: "Start monolith. Microservices add complexity you don't need at 1000 users."
PM: "Agree. Time to market matters more."
Dev: "Monolith with clear module boundaries. We can extract services later."
```

## Maintenance status

47,851 stars, 5,581 forks, MIT license, latest release v6.7.1 (~2026-05-19), active JavaScript codebase with conventional commits enforced. Community channels: Discord (open, no paywalls), YouTube tutorials, X/Twitter. Corporate sponsorship available via email. The project states it is "100% free and open source" and explicitly rejects gated content.

## Ecosystem

- **Official modules**: BMad Builder (BMB) for custom agent/workflow authoring; Test Architect (TEA) for risk-based test strategy; Game Dev Studio (BMGD) for Unity/Unreal/Godot workflows; Creative Intelligence Suite (CIS) for innovation and design thinking
- **Docs site**: https://docs.bmad-method.org with tutorials, how-to guides, reference, and a visual workflow-map diagram
- **Related methodologies**: [[obra-superpowers]] (spec-first, skill-based agent methodology), [[coleam00-archon]] (YAML-driven workflow engine for AI coding), [[gsd-build-get-shit-done]] (context-engineering spec-driven development)
