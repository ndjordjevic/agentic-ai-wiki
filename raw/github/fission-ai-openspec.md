# Fission-AI/OpenSpec

## Metadata
- Stars: 49025
- Forks: 3446
- Primary language: TypeScript
- Default branch: main
- Latest release: v1.3.1 (about 27 days ago)
- License: MIT License
- Homepage: https://openspec.dev/
- Fetched: 2026-05-19
- Final URL: https://github.com/Fission-AI/OpenSpec

## Description
Spec-driven development (SDD) for AI coding assistants.

## README

Our philosophy:
```
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises
```

> **New workflow now available!** We've rebuilt OpenSpec with a new artifact-guided workflow.
> Run `/opsx:propose "your idea"` to get started.

### See it in action

```text
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!

You: /opsx:apply
AI:  Implementing tasks...
     ✓ 1.1 Add theme context provider
     ✓ 1.2 Create toggle component
     ✓ 2.1 Add CSS variables
     ✓ 2.2 Wire up localStorage
     All tasks complete!

You: /opsx:archive
AI:  Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
     Specs updated. Ready for the next feature.
```

### Quick Start

Requires Node.js 20.19.0 or higher.

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

Then tell your AI: `/opsx:propose <what-you-want-to-build>`

For the expanded workflow (`/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:onboard`), select it with `openspec config profile` and apply with `openspec update`.

Also works with pnpm, yarn, bun, and nix. Supports 25+ tools.

### Docs
- Getting Started: docs/getting-started.md
- Workflows: docs/workflows.md
- Commands: docs/commands.md
- CLI: docs/cli.md
- Supported Tools: docs/supported-tools.md
- Concepts: docs/concepts.md
- Multi-Language: docs/multi-language.md
- Customization: docs/customization.md

### Community schemas
Third-party schema bundles distributed via standalone repositories that provide opinionated workflows integrating OpenSpec with other tools, similar to how github/spec-kit's community extension catalog handles tool integrations.

### Why OpenSpec?
AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written.

- **Agree before you build** — human and AI align on specs before code gets written
- **Stay organized** — each change gets its own folder with proposal, specs, design, and tasks
- **Work fluidly** — update any artifact anytime, no rigid phase gates
- **Use your tools** — works with 20+ AI assistants via slash commands

**vs. Spec Kit (GitHub)** — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.
**vs. Kiro (AWS)** — Powerful but locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use.

### Updating OpenSpec

```bash
npm install -g @fission-ai/openspec@latest
openspec update  # Refresh agent instructions in each project
```

**Model selection**: OpenSpec works best with high-reasoning models (Opus 4.5 and GPT 5.2 recommended).

**Context hygiene**: OpenSpec benefits from a clean context window. Clear context before starting implementation.

### Contributing
- Small fixes: Bug fixes, typo corrections → submit PRs directly
- Larger changes: Submit an OpenSpec change proposal first (practice what you preach)
- AI-generated code is welcome as long as it's been tested and verified

### Development
```bash
pnpm install
pnpm run build
pnpm test
pnpm run dev  # or pnpm run dev:cli
```

Conventional commits: `type(scope): subject`

### Telemetry
Collects only command names and version (anonymous). No arguments, paths, content, or PII. Opt-out: `export OPENSPEC_TELEMETRY=0`

## Docs

### docs/getting-started.md

# Getting Started

OpenSpec helps you and your AI coding assistant agree on what to build before any code is written.

**Default quick path (core profile):**
```
/opsx:propose ──► /opsx:apply ──► /opsx:sync ──► /opsx:archive
```

**Expanded path:**
```
/opsx:new ──► /opsx:ff or /opsx:continue ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive
```

**What OpenSpec Creates** (after `openspec init`):
```
openspec/
├── specs/              # Source of truth (your system's behavior)
│   └── <domain>/
│       └── spec.md
├── changes/            # Proposed updates (one folder per change)
│   └── <change-name>/
│       ├── proposal.md
│       ├── design.md
│       ├── tasks.md
│       └── specs/      # Delta specs (what's changing)
└── config.yaml         # Project configuration (optional)
```

**Artifacts:**
| Artifact | Purpose |
|----------|---------|
| `proposal.md` | The "why" and "what" — captures intent, scope, and approach |
| `specs/` | Delta specs showing ADDED/MODIFIED/REMOVED requirements |
| `design.md` | The "how" — technical approach and architecture decisions |
| `tasks.md` | Implementation checklist with checkboxes |

**How Delta Specs Work** — Delta specs use sections to indicate the type of change:
- `ADDED`: new requirement being introduced
- `MODIFIED`: changing an existing requirement
- `REMOVED`: requirement being deleted

### docs/concepts.md

# Concepts

OpenSpec is built around four principles:
```
fluid not rigid         — no phase gates, work on what makes sense
iterative not waterfall — learn as you build, refine as you go
easy not complex        — lightweight setup, minimal ceremony
brownfield-first        — works with existing codebases, not just greenfield
```

**The Big Picture:**
```
openspec/
  specs/          → Source of truth: how your system currently behaves
  changes/        → Proposed modifications: each change = one folder with artifacts + deltas
```

Specs and changes are separated. You can work on multiple changes in parallel without conflicts. Review a change before it affects the main specs. When archived, deltas merge cleanly into the source of truth.

**Coordination Workspaces** (under active development — not ready for production use): workspace = where related cross-repo changes live; link = stable name for a repo/folder; change = one planned piece of work.

**Glossary:**
| Term | Definition |
|------|------------|
| Artifact | A document within a change (proposal, design, tasks, or delta specs) |
| Archive | Completing a change and merging its deltas into main specs |
| Change | A proposed modification packaged as a folder with artifacts |
| Delta spec | A spec showing changes (ADDED/MODIFIED/REMOVED) relative to current specs |
| Domain | A logical grouping for specs (e.g., `auth/`, `payments/`) |
| Spec | A specification describing system behavior (requirements + scenarios) |
| Schema | A definition of artifact types and their dependencies |
| Source of truth | The `openspec/specs/` directory |

### docs/commands.md

# Commands

**Default Quick Path (`core` profile):**
| Command | Purpose |
|---------|---------|
| `/opsx:propose` | Create a change and generate planning artifacts in one step |
| `/opsx:explore` | Think through ideas before committing to a change |
| `/opsx:apply` | Implement tasks from the change |
| `/opsx:sync` | Merge delta specs into main specs |
| `/opsx:archive` | Archive a completed change |

**Expanded Workflow Commands (custom workflow selection):**
| Command | Purpose |
|---------|---------|
| `/opsx:new` | Start a new change scaffold |
| `/opsx:continue` | Create the next artifact based on dependencies |
| `/opsx:ff` | Fast-forward: create all planning artifacts at once |
| `/opsx:verify` | Validate implementation matches artifacts |
| `/opsx:bulk-archive` | Archive multiple changes at once |
| `/opsx:onboard` | Guided tutorial through the complete workflow |

Enable expanded commands: `openspec config profile` → select workflows → `openspec update`.

**`/opsx:propose` example:**
```
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md
     ✓ specs/ui/spec.md
     ✓ design.md
     ✓ tasks.md
     Ready for implementation. Run /opsx:apply.
```

### docs/workflows.md

# Workflows

**Philosophy: Actions, Not Phases**

```
Traditional (phase-locked):
  PLANNING ──────────► IMPLEMENTING ──────────► DONE

OPSX (fluid actions):
  proposal ──► specs ──► design ──► tasks ──► implement
      ▲           ▲          ▲                    │
      └───────────┴──────────┴────────────────────┘
               update as you learn
```

**Two Modes:**
1. Default Quick Path (`core` profile): `/opsx:propose → /opsx:apply → /opsx:sync → /opsx:archive`
2. Expanded/Full Workflow: Enable with `openspec config profile` + `openspec update`

**Workflow Patterns (Expanded Mode):**
- Quick Feature: `/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive`
- Exploratory: `/opsx:explore → /opsx:new → /opsx:continue → /opsx:apply → /opsx:archive`

## Top-level structure

```
.actrc                  — act (GitHub Actions local runner) config
.changeset/             — changeset versioning for releases
.devcontainer/          — VS Code dev container configuration
.github/                — CI/CD workflows (merge queue, tests)
AGENTS.md               — agent instructions for OpenSpec contributors
CHANGELOG.md            — release history
LICENSE                 — MIT License
MAINTAINERS.md          — core maintainers and advisors list
README.md               — main documentation and quick start
assets/                 — logo images and dashboard preview
bin/                    — CLI entry point binaries
build.js                — build script
docs/                   — user-facing documentation (11 markdown files)
openspec/               — OpenSpec's own specs and changes (dogfooding)
package.json            — npm package config (@fission-ai/openspec)
pnpm-lock.yaml          — pnpm lockfile
schemas/                — artifact schema definitions
scripts/                — utility scripts
src/                    — TypeScript source code
test/                   — test suite (vitest)
tsconfig.json           — TypeScript config
vitest.config.ts        — vitest test runner config
```
