---
type: source
source_url: https://openspec.dev/
companion_urls:
  - https://github.com/Fission-AI/OpenSpec
raw_files:
  - ../../raw/web/openspec.dev.md
  - ../../raw/github/fission-ai-openspec.md
tags:
  - spec-driven-development
  - ai-coding-agents
  - slash-commands
  - agentic-planning
  - change-management
  - brownfield-development
  - specification-first
  - agent-instructions
related:
  - github-spec-kit
  - gsd-build-get-shit-done
product: openspec
detail_level: standard
created: 2026-05-19
updated: 2026-05-19
---

OpenSpec is a lightweight, open-source spec-driven development (SDD) framework for AI coding assistants and CLIs — universal, requires no API keys, and no MCP. Built by Fission, it reached 49,000+ stars and supports 25+ coding tools natively (Claude Code, Cursor, Codex, GitHub Copilot, Windsurf, Gemini CLI, Cline, and more). Its central idea: AI agents perform better when requirements are captured as structured specs in the codebase before any code is written, and those specs persist across sessions, agents, and team members.

_All claims below are sourced from ../../raw/web/openspec.dev.md unless otherwise noted._

## What it does

OpenSpec introduces a spec layer between the human's intent and the AI's implementation. Rather than relying on chat history (which disappears) or detailed prompts (which don't persist), developers write machine-readable specs that live in the repository alongside code. When an agent needs context about how a feature should work, it reads the spec. When a change is proposed, OpenSpec generates a structured change folder with a proposal, delta specs, design doc, and task checklist — all before code is written.

The result is an artifact-guided workflow: human and AI align on requirements, the AI generates planning artifacts, the human reviews and refines, then implementation begins with full spec context available. After implementation, archived changes merge their delta specs back into the source-of-truth `openspec/specs/` directory, building a living specification of the entire codebase over time.

## Key features

- **Delta specs** — each change captures ADDED, MODIFIED, and REMOVED requirements relative to current specs; reviewers see intent, not just code diff
- **Change folders** — one folder per feature with `proposal.md`, `design.md`, `tasks.md`, and `specs/` artifacts; complete audit trail of every decision
- **Dual workflow profiles** — `core` profile offers `/opsx:propose → /opsx:apply → /opsx:archive`; expanded profile adds scaffolded artifact creation, fast-forward, verify, and bulk-archive commands
- **Universal tool support** — native integration with 25+ AI coding assistants via agent instruction files; no API keys or MCP server required
- **Brownfield-first** — designed for mature codebases; specs are created incrementally as features are built, not generated upfront en masse
- **Customizable schemas** — artifact sequences and dependencies are schema-driven; community schemas distributed as standalone repositories extend the base behavior (../../raw/github/fission-ai-openspec.md)

## Architecture

OpenSpec's architecture is a two-directory pattern in the repository root: (../../raw/github/fission-ai-openspec.md)

- **`openspec/specs/`** — the source of truth; plain Markdown files organized by capability domain (e.g., `specs/auth/`, `specs/payments/`). Each `spec.md` contains requirements in structured prose ("The system SHALL…") with Given/When/Then scenarios.
- **`openspec/changes/`** — proposed modifications; each change is a self-contained folder with planning artifacts and delta specs. Delta specs mirror the source-of-truth structure but only capture the diff.

Slash commands (installed as agent instruction files via `openspec init` and `openspec update`) run inside the coding agent's session. The agent reads specs for context, generates artifacts, and executes tasks — all mediated by the `@fission-ai/openspec` CLI package. (../../raw/github/fission-ai-openspec.md)

Schemas define artifact types and their dependency graph. The default `spec-driven` schema chains `proposal → specs → design → tasks`. Custom schemas can reorder artifacts, add new types, or enforce different sequencing. (../../raw/github/fission-ai-openspec.md)

## Installation

Requires Node.js 20.19.0 or higher. Also works with pnpm, yarn, bun, and nix. (../../raw/github/fission-ai-openspec.md)

```bash
# Install globally
npm install -g @fission-ai/openspec@latest

# Initialize in a project
cd your-project
openspec init

# Tell your AI to start
/opsx:propose <what-you-want-to-build>
```

Refresh agent instructions when upgrading: (../../raw/github/fission-ai-openspec.md)

```bash
npm install -g @fission-ai/openspec@latest
openspec update  # Regenerates agent instruction files in each project
```

## Example usage

```
You: /opsx:propose add-dark-mode

AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/ui/spec.md — delta requirements for UI domain
     ✓ design.md — technical approach
     ✓ tasks.md — implementation checklist
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
(../../raw/github/fission-ai-openspec.md)

## When to use

OpenSpec is the right fit when:
- AI-assisted features span multiple chat sessions and context gets lost
- Teams need reviewable intent alongside code diffs
- The codebase is mature (brownfield) and generating upfront specs is impractical
- Developers want to switch between coding agents without losing planning context
- Lightweight planning discipline is preferred over heavyweight project management

Not ideal for pure vibe-coding or for developers who want zero planning overhead. Specs require engagement — they work best when the developer reads, thinks through, and refines them.

## Maintenance status

49,025 stars, 3,446 forks, MIT License, TypeScript, latest release v1.3.1, actively maintained with 587+ commits, 201 branches, 36 tags. Developed by Fission (@TabishB lead contributor). Active Discord community. Workspace/team features in development. (../../raw/github/fission-ai-openspec.md)

## Ecosystem

OpenSpec competes directly with [[github-spec-kit]] (GitHub's Spec Kit — more heavyweight, rigid phase gates, Python-based) and Kiro (AWS — IDE-locked, Claude-only). OpenSpec's differentiators are universal tool compatibility and lightweight brownfield-first approach.

Community schemas extend the base workflow in ways analogous to how [[skills.sh]] distributes SKILL.md modules — third-party repositories publish schema bundles that integrate OpenSpec with other tools. (../../raw/github/fission-ai-openspec.md)

The `openspec/` folder in the repo contains OpenSpec's own specs and changes for its own development (dogfooding), providing a real-world reference for the spec-driven pattern.

## Documentation

Docs live in the GitHub repo at `docs/` with 11 Markdown files covering getting-started, workflows, commands, CLI, supported tools (25+), concepts, multi-language support, customization, opsx workflow, installation options, and migration guide. The website (openspec.dev) is a single-page Astro app; all deep docs are GitHub-only. (../../raw/github/fission-ai-openspec.md)
