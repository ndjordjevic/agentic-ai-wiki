# buildermethods/agent-os

## Metadata
- Stars: 4635
- Primary language: Shell
- Default branch: main
- Latest release: v3.0.0 (2026-01-20)
- License: MIT License
- Homepage: https://buildermethods.com/agent-os
- Fetched: 2026-05-25
- Final URL: https://github.com/buildermethods/agent-os

## Description
Agent OS is a system for injecting your codebase standards and writing better specs for spec-driven development.

## README

<img width="1200" height="675" alt="Agent OS" src="https://github.com/user-attachments/assets/97ad4491-d199-4b9b-9482-ae710291dfb4" />

## Agents that build the way you would

[Agent OS](https://buildermethods.com/agent-os) helps you shape better specs, keeps agents aligned in a lightweight system that fits how you already build.

Works alongside Claude Code, Cursor, Antigravity, and other AI tools. Any language, any framework.

**Core capabilities:**

- **Discover Standards** — Extract patterns and conventions from your codebase into documented standards
- **Deploy Standards** — Intelligently inject relevant standards based on what you're building
- **Shape Spec** — Create better plans that lead to better builds
- **Index Standards** — Keep your standards organized and discoverable

---

### Documentation & Installation

Docs, installation, usage, & best practices 👉 [It's all here](https://buildermethods.com/agent-os)

---

### Follow updates & releases

Read the [changelog](CHANGELOG.md)

[Subscribe to be notified of major new releases of Agent OS](https://buildermethods.com/agent-os)

---

### Created by Brian Casel @ Builder Methods

Created by Brian Casel, the creator of [Builder Methods](https://buildermethods.com), where Brian helps professional software developers and tools build with AI.

Get Brian's free resources on building with AI:
- [Builder Briefing newsletter](https://buildermethods.com)
- [YouTube](https://youtube.com/@briancasel)

Join [Builder Methods Pro](https://buildermethods.com/pro) for official support and connect with our community of AI-first builders.

## Docs

### config.yml
```yaml
version: 3.0
default_profile: default

# Optional: define inheritance relationships for profiles
# Profiles not listed here still work, they just have no inheritance
# profiles:
#   profile-a:
#     inherits_from: default
#   profile-b:
#     inherits_from: profile-a
```

### commands/agent-os/discover-standards.md (excerpt)
```markdown
# Discover Standards

Extract tribal knowledge from your codebase into concise, documented standards.

## Important Guidelines
- **Always use AskUserQuestion tool** when asking the user anything
- **Write concise standards** — Use minimal words. Standards must be scannable by AI agents without bloating context windows.
- **Offer suggestions** — Present options the user can confirm, choose between, or correct.

## Process

### Step 1: Determine Focus Area
Check if the user specified an area when running this command. If not, analyze the codebase
structure, identify 3-5 major areas (e.g., Frontend, Backend, Cross-cutting), and prompt via
AskUserQuestion.

### Step 2 onward: Review existing standards, draft new ones, save to agent-os/standards/<area>/
```

### commands/agent-os/index-standards.md (excerpt)
```markdown
# Index Standards

Rebuild and maintain the standards index file (`index.yml`).

## Purpose
The index enables `/inject-standards` to suggest relevant standards without reading all files.
It maps each standard to a brief description for quick matching.

## Process
1. Scan all .md files in `agent-os/standards/` and subfolders
2. Load existing `agent-os/standards/index.yml` if present
3. Identify new/changed files, generate 1-2 sentence descriptions for each
4. Write updated index.yml
```

### commands/agent-os/inject-standards.md (excerpt)
```markdown
# Inject Standards

Inject relevant standards into the current context, formatted appropriately for the situation.

## Usage Modes
- Auto-Suggest Mode: `/inject-standards` — analyzes context, suggests relevant standards
- Explicit Mode: `/inject-standards api/response-format` — directly injects specified standards

## Step 1: Detect Context Scenario
Determine if we're in a conversation, plan, or skill context to format output appropriately.
Read index.yml (if present) to find standards matching the current task/file context.
```

### commands/agent-os/shape-spec.md (excerpt)
```markdown
# Shape Spec

Gather context and structure planning for significant work. **Run this command while in plan mode.**

## Prerequisites
Must be run in plan mode. If NOT in plan mode, stop and tell the user to enter plan mode first.

## Process
1. Clarify what we're building (scope, constraints, goal)
2. Surface relevant standards via inject-standards
3. Ask targeted clarifying questions
4. Save resulting plan to agent-os/specs/ folder
```

### commands/agent-os/plan-product.md (excerpt)
```markdown
# Plan Product

Establish foundational product documentation through an interactive conversation.
Creates mission, roadmap, and tech stack files in `agent-os/product/`.

## Process
1. Check for existing product docs (mission.md, roadmap.md, tech-stack.md)
2. If existing, offer to start fresh or update specific files
3. One question at a time: what are you building, who is it for, what's the roadmap, tech stack?
4. Write files to agent-os/product/
```

### profiles/default/global/tech-stack.md (example)
```markdown
# Tech Stack

## Frontend
- React 18 with TypeScript
- Tailwind CSS v4 for styling
- Vite for build tooling

## Backend
- Node.js with Express
- TypeScript

## Database
- PostgreSQL
```

### CHANGELOG (key versions)

**v3.0 (2026-01-20):**
- `/discover-standards` — agent surfaces, suggests, and creates standards from codebase
- `/inject-standards` — injects relevant standards using new `index.yml` for automatic detection
- Sync script — syncs project standards back to base profiles
- Spec creation now defers to Plan Mode (Claude Code, Cursor) — the industry-standard approach for 2026+
- `/shape-spec` enhances plan mode with targeted questions, saves plan to `agent-os/specs/`
- Profile inheritance now defined in main `config.yml`
- Implementation/orchestration phases retired (frontier models handle these natively)

**v2.1.0 (2025-10-21):**
- Added Claude Code Skills support (`standards_as_claude_code_skills: true`)
- Enable/disable delegation to Claude Code subagents (`use_claude_code_subagents`)
- Replaced single/multi-agent modes with flexible config options
- Went from 4 to 6 development phases: plan-product, shape-spec, write-spec, create-tasks, implement-tasks, orchestrate-tasks

## Top-level structure

```
buildermethods/agent-os/
├── README.md              — overview and links to docs
├── CHANGELOG.md           — version history (v1 through v3.0)
├── LICENSE                — MIT
├── config.yml             — top-level config: version, default_profile, profile inheritance
├── commands/
│   └── agent-os/          — slash commands for AI coding agents
│       ├── discover-standards.md  — extract codebase conventions into standards docs
│       ├── index-standards.md     — rebuild standards index.yml for fast lookup
│       ├── inject-standards.md    — inject relevant standards into context (auto or explicit)
│       ├── plan-product.md        — establish product mission/roadmap/tech-stack docs
│       └── shape-spec.md          — shape a spec while in plan mode
├── profiles/
│   └── default/
│       └── global/
│           └── tech-stack.md      — default global tech stack template
└── scripts/
    ├── project-install.sh         — install Agent OS into a project
    ├── sync-to-profile.sh         — sync project standards back to profile
    └── common-functions.sh        — shared shell utilities
```
