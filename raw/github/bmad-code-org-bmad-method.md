# bmad-code-org/BMAD-METHOD

## Metadata
- Stars: 47851
- Primary language: JavaScript
- Default branch: main
- Latest release: v6.7.1 (~2026-05-19)
- License: MIT
- Homepage: https://docs.bmad-method.org
- Fetched: 2026-05-22
- Final URL: https://github.com/bmad-code-org/BMAD-METHOD

## Description
Breakthrough Method for Agile AI Driven Development

## README

![BMad Method](banner-bmad-method.png)

**Build More Architect Dreams** — An AI-driven agile development module for the BMad Method Module Ecosystem, the best and most comprehensive Agile AI Driven Development framework that has true scale-adaptive intelligence that adjusts from bug fixes to enterprise systems.

**100% free and open source.** No paywalls. No gated content. No gated Discord. We believe in empowering everyone, not just those who can pay for a gated community or courses.

### Why the BMad Method?

Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI.

- **AI Intelligent Help** — Invoke the `bmad-help` skill anytime for guidance on what's next
- **Scale-Domain-Adaptive** — Automatically adjusts planning depth based on project complexity
- **Structured Workflows** — Grounded in agile best practices across analysis, planning, architecture, and implementation
- **Specialized Agents** — 12+ domain experts (PM, Architect, Developer, UX, and more)
- **Party Mode** — Bring multiple agent personas into one session to collaborate and discuss
- **Complete Lifecycle** — From brainstorming to deployment

[Learn more at **docs.bmad-method.org**](https://docs.bmad-method.org)

### 🚀 What's Next for BMad?

**V6 is here and we're just getting started!** The BMad Method is evolving rapidly with optimizations including Cross Platform Agent Team and Sub Agent inclusion, Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works.

### Quick Start

**Prerequisites**: Node.js v20.12+ · Python 3.10+ · uv

```bash
npx bmad-method install
```

Follow the installer prompts, then open your AI IDE (Claude Code, Cursor, etc.) in your project folder.

**Non-Interactive Installation** (for CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

### Modules

| Module | Purpose |
|---|---|
| **BMad Method (BMM)** | Core framework with 34+ workflows |
| **BMad Builder (BMB)** | Create custom BMad agents and workflows |
| **Test Architect (TEA)** | Risk-based test strategy and automation |
| **Game Dev Studio (BMGD)** | Game development workflows (Unity, Unreal, Godot) |
| **Creative Intelligence Suite (CIS)** | Innovation, brainstorming, design thinking |

### Documentation

[BMad Method Docs Site](https://docs.bmad-method.org) — Tutorials, guides, concepts, and reference

### Community

- Discord: https://discord.gg/gk8jAdXWmj
- YouTube: https://youtube.com/@BMadCode
- X / Twitter: https://x.com/BMadCode
- Website: https://bmadcode.com

## Docs

### docs/reference/workflow-map.md

The BMad Method (BMM) is a module in the BMad Ecosystem, targeted at following the best practices of context engineering and planning. AI agents work best with clear, structured context. The BMM system builds that context progressively across 4 distinct phases — each phase, and multiple workflows optionally within each phase, produce documents that inform the next, so agents always know what to build and why.

**Phase 1: Analysis (Optional)**

Explore the problem space and validate ideas before committing to planning.

| Workflow | Purpose | Produces |
|---|---|---|
| `bmad-brainstorming` | Brainstorm Project Ideas with guided facilitation | `brainstorming-report.md` |
| `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` | Validate market, technical, or domain assumptions | Research findings |
| `bmad-product-brief` | Capture strategic vision — best when your concept is clear | `product-brief.md` |
| `bmad-prfaq` | Working Backwards — stress-test and forge your product concept | `prfaq-{project}.md` |

**Phase 2: Planning**

| Workflow | Purpose | Produces |
|---|---|---|
| `bmad-prd` | Create, update, or validate a PRD — three intents in one skill | `prd.md`, `addendum.md`, `decision-log.md` |
| `bmad-create-ux-design` | Design user experience (when UX matters) | `ux-spec.md` |

**Phase 3: Solutioning**

| Workflow | Purpose | Produces |
|---|---|---|
| `bmad-create-architecture` | Make technical decisions explicit | `architecture.md` with ADRs |
| `bmad-create-epics-and-stories` | Break requirements into implementable work | Epic files with stories |
| `bmad-check-implementation-readiness` | Gate check before implementation | PASS/CONCERNS/FAIL decision |

**Phase 4: Implementation**

| Workflow | Purpose | Produces |
|---|---|---|
| `bmad-sprint-planning` | Initialize tracking | `sprint-status.yaml` |
| `bmad-create-story` | Prepare next story for implementation | `story-[slug].md` |
| `bmad-dev-story` | Implement the story | Working code + tests |
| `bmad-code-review` | Validate implementation quality | Approved or changes requested |
| `bmad-correct-course` | Handle significant mid-sprint changes | Updated plan or re-routing |
| `bmad-retrospective` | Review after epic completion | Lessons learned |
| `bmad-investigate` | Forensic case investigation | `{slug}-investigation.md` |

**Quick Flow (Parallel Track)**

| Workflow | Purpose | Produces |
|---|---|---|
| `bmad-quick-dev` | Unified quick flow — clarify, plan, implement, review | `spec-*.md` + code |

### docs/reference/agents.md

Default BMM agents with their skill IDs, menu triggers, and primary workflows:

| Agent | Skill ID | Triggers | Primary workflows |
|---|---|---|---|
| Analyst (Mary) | `bmad-analyst` | `BP`, `MR`, `DR`, `TR`, `CB`, `WB`, `DP` | Brainstorm, Market Research, Domain Research, Technical Research, Create Brief, PRFAQ Challenge, Document Project |
| Product Manager (John) | `bmad-pm` | `CP`, `VP`, `EP`, `CE`, `IR`, `CC` | Create/Validate/Edit PRD, Create Epics and Stories, Implementation Readiness, Correct Course |
| Architect (Winston) | `bmad-architect` | `CA`, `IR` | Create Architecture, Implementation Readiness |
| Developer (Amelia) | `bmad-agent-dev` | `DS`, `QD`, `QA`, `CR`, `SP`, `CS`, `ER` | Dev Story, Quick Dev, QA Test Generation, Code Review, Sprint Planning, Create Story, Epic Retrospective |
| UX Designer (Sally) | `bmad-ux-designer` | `CU` | Create UX Design |
| Technical Writer (Paige) | `bmad-tech-writer` | `DP`, `WD`, `US`, `MG`, `VD`, `EC` | Document Project, Write Document, Update Standards, Mermaid Generate, Validate Doc, Explain Concept |

### docs/explanation/named-agents.md (excerpts)

BMad's agent model rests on three primitives:

| Primitive | What it provides | Where it lives |
|---|---|---|
| **Skill** | Capability — a discrete thing the assistant can do | `.claude/skills/{skill-name}/SKILL.md` |
| **Named agent** | Persona continuity — wraps a menu of related skills with consistent voice, principles | Skills whose directory starts with `bmad-agent-*` |
| **Customization** | Team and personal overrides via TOML that reshape agent behavior | `_bmad/custom/{skill-name}.toml` (committed) / `.user.toml` (personal, gitignored) |

Six named agents ship with BMad, each anchored to a phase of the BMad Method:
- 📊 **Mary**, Business Analyst (Analysis)
- 📚 **Paige**, Technical Writer (Analysis)
- 📋 **John**, Product Manager (Planning)
- 🎨 **Sally**, UX Designer (Planning)
- 🏗️ **Winston**, System Architect (Solutioning)
- 💻 **Amelia**, Senior Engineer (Implementation)

### docs/explanation/analysis-phase.md (excerpt)

The Analysis phase (Phase 1) helps you think clearly about your product before committing to building it. Every tool in this phase is optional, but skipping analysis means the PRD is built on assumptions instead of insight.

Tools: Brainstorming, Research (Market/Domain/Technical), Product Brief, PRFAQ (Amazon Working Backwards adapted as an interactive challenge).

### docs/explanation/party-mode.md (excerpt)

Party Mode (`bmad-party-mode`) runs all your AI agents (PM, Architect, Dev, UX Designer) in one conversation. BMad Master orchestrates, picking relevant agents per message. Agents respond in character, agree, disagree, and build on each other's ideas. Good for: big decisions with tradeoffs, brainstorming sessions, post-mortems, sprint retrospectives and planning.

## AGENTS.md

```
# BMAD-METHOD

Open source framework for structured, agent-assisted software delivery.

## Rules

- Use Conventional Commits for every commit.
- Before pushing, run `npm ci && npm run quality` on `HEAD` in the exact checkout you are about to push.
  `quality` mirrors the checks in `.github/workflows/quality.yaml`.
- Skill validation rules are in `tools/skill-validator.md`.
- Deterministic skill checks run via `npm run validate:skills` (included in `quality`).
```

## Top-level structure

```
AGENTS.md               — agent coding instructions (Conventional Commits, quality gate)
CHANGELOG.md            — version history
CONTRIBUTING.md         — contribution guidelines
CONTRIBUTORS.md         — contributor list
LICENSE                 — MIT
README.md               — main documentation
README_CN.md            — Chinese translation
README_VN.md            — Vietnamese translation
SECURITY.md             — security policy
TRADEMARK.md            — BMad/BMAD-METHOD trademark notice
bmad-modules.yaml       — module registry manifest
package.json            — npm package (distributed as `bmad-method`)
src/
  bmm-skills/           — core BMad Method Module skills (agent + workflow skill files)
  core-skills/          — cross-module core skills (bmad-help, etc.)
  scripts/              — installer and build scripts
docs/
  explanation/          — concept guides (named agents, party mode, analysis phase, etc.)
  how-to/               — task guides (install, customize, upgrade, etc.)
  reference/            — reference docs (agents, commands, modules, workflow-map)
  tutorials/            — getting started tutorial
tools/                  — skill-validator and build tooling
evals/                  — evaluation harnesses
website/                — docs site source
.claude-plugin/         — Claude Code plugin integration
.augment/               — Augment AI integration
```
