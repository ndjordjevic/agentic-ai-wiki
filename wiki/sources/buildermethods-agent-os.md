---
type: source
source_url: https://github.com/buildermethods/agent-os
tags:
  - standards-management
  - spec-driven-development
  - context-injection
  - codebase-standards
  - agent-workflow
  - claude-code
  - plan-mode
  - scaffold-commands
related:
  - bmad-code-org-bmad-method
  - github-spec-kit
  - gsd-build-get-shit-done
  - anthropics-skills
  - obra-superpowers
  - eyaltoledano-claude-task-master
  - garrytan-gstack
product: agent-os
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Agent OS is an open-source framework (4,635 stars, MIT) by Brian Casel / Builder Methods that solves the context-injection problem in AI-assisted development: agents lack knowledge of a project's own conventions, so they drift from team standards. Agent OS addresses this with two interlocking mechanisms — a standards library the team maintains in markdown, and a set of slash commands (`/discover-standards`, `/inject-standards`, `/index-standards`, `/shape-spec`, `/plan-product`) that extract conventions from the codebase, keep them indexed, and inject only the relevant subset into each agent conversation. Version 3.0 (January 2026) streamlined the architecture by removing its own orchestration phases and deferring to Plan Mode in Claude Code or Cursor, repositioning Agent OS as a pure standards-and-spec layer rather than a full dev-cycle harness.

_All claims below are sourced from ../../raw/github/buildermethods-agent-os.md unless otherwise noted._

## What it does

Agent OS gives AI coding agents access to a project's evolving conventions and specifications without manual copy-paste. It maintains a `agent-os/standards/` directory of concise markdown files, an `agent-os/product/` directory for product mission and roadmap, and an `agent-os/specs/` folder for feature plans. The slash commands tie these together: `/discover-standards` extracts patterns from existing code, `/index-standards` rebuilds the `index.yml` lookup map, `/inject-standards` reads that map and pushes the right standards into context before the agent writes code, and `/shape-spec` prompts targeted clarifying questions in plan mode then saves the result. The result is a lightweight "operating system" overlay that works with any language, any framework, and any AI tool (Claude Code, Cursor, Antigravity, and others).

## Key features

- **`/discover-standards`** — agent analyzes codebase structure, identifies major areas, drafts concise standard documents for human review, and saves them to `agent-os/standards/<area>/`
- **`/index-standards`** — scans all standards `.md` files, generates 1-2 sentence descriptions for each, and writes `agent-os/standards/index.yml` — the lookup map used by `/inject-standards`
- **`/inject-standards`** — auto-suggest mode reads `index.yml` and matches current context to relevant standards; explicit mode injects named files directly (e.g. `/inject-standards api/response-format`)
- **`/shape-spec`** — must run in plan mode; asks targeted questions about scope, pulls relevant standards via inject, and saves a structured plan to `agent-os/specs/`
- **`/plan-product`** — interactive conversation that creates `agent-os/product/mission.md`, `roadmap.md`, and `tech-stack.md`
- **Profile inheritance** — `config.yml` defines named profiles with optional `inherits_from` chains, enabling shared base standards across multiple projects
- **Sync script** — `scripts/sync-to-profile.sh` pushes project-level standards back to the shared profile, keeping the team's base standards up to date

## Architecture

Agent OS is a filesystem-first framework with no runtime process. It installs into a project via `scripts/project-install.sh`, which copies commands and profile templates into the project root. The directory layout is:

```
agent-os/
  product/          ← mission.md, roadmap.md, tech-stack.md
  standards/
    index.yml       ← fast-lookup map (key: file path, value: 1-2 sentence description)
    <area>/         ← one subfolder per concern area (api/, database/, frontend/, etc.)
      *.md          ← individual standard files
  specs/            ← feature plans produced by /shape-spec
commands/
  agent-os/         ← slash command .md files loaded by the AI coding agent
config.yml          ← version, default_profile, optional inheritance map
profiles/
  <name>/
    global/         ← global standards for this profile (e.g. tech-stack.md)
```

The slash commands are markdown files interpreted by the AI coding agent (not executable scripts). `index.yml` is the performance key: without it, injecting standards would require loading every file; with it, `/inject-standards` reads one small YAML to pick the relevant files. The framework intentionally delegates orchestration, task tracking, and subagent management to the hosting agent tool (Claude Code plan mode, Cursor, etc.). (../../raw/github/buildermethods-agent-os.md)

## Installation

```bash
# Install into a project (run from project root)
bash <(curl -fsSL https://raw.githubusercontent.com/buildermethods/agent-os/main/scripts/project-install.sh)
```

After install, run `/plan-product` in your AI coding agent to set up product docs, then `/discover-standards` to extract initial standards from the codebase. Run `/index-standards` whenever standards files change.

## Example usage

Typical workflow in Claude Code or Cursor:

```
# Before starting a feature
/inject-standards                 # auto-suggest mode — reads index.yml, injects relevant standards

# Or inject explicitly before writing API code
/inject-standards api/response-format api/error-handling

# Shape a spec in plan mode
/shape-spec                       # prompts for scope, injects standards, saves to agent-os/specs/

# After refactoring, update standards
/discover-standards               # area: routing
/index-standards                  # rebuild index.yml
```

## Maintenance status

Agent OS has 4,635 GitHub stars and an active release history (v3.0.0 released January 2026, with post-release patches for POSIX compatibility). The project is MIT-licensed. The creator Brian Casel actively maintains it through Builder Methods Pro, a paid community offering official support. The v3.0 release was a deliberate architecture simplification — removing phase-management layers — reflecting the framework's long-term direction toward a slim standards-and-spec overlay rather than a full orchestration harness.

## Ecosystem

Agent OS works alongside any AI coding agent that supports slash commands or custom instructions. Official support for Claude Code, Cursor, Antigravity; any agent that reads markdown command files works. It pairs naturally with frameworks like [[bmad-code-org-bmad-method]] (full spec-driven dev lifecycle), [[github-spec-kit]] (spec-driven development with a `specify` CLI), and [[gsd-build-get-shit-done]] (context management commands for Claude Code). The `standards_as_claude_code_skills` config option (introduced in v2.1) converts standards into [[anthropics-skills]]-compatible Claude Code Skills for teams already using that ecosystem. Brian Casel publishes accompanying tutorials on the Builder Methods YouTube channel.
