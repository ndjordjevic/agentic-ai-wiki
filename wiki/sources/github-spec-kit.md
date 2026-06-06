---
type: source
source_url: https://github.com/github/spec-kit
tags:
  - spec-driven-development
  - ai-coding-agents
  - slash-commands
  - agent-skills
  - workflow-automation
  - specify-cli
  - specification-first
related:
  - gsd-build-get-shit-done
  - anthropics-skills
  - obra-superpowers
  - skills.sh
  - openspec.dev
  - openai-codex-plugin-cc
  - buildermethods-agent-os
  - x.com-ericzakariasson-building-clis-for-agents
product: spec-kit
detail_level: standard
created: 2026-05-19
updated: 2026-06-06
---

Spec Kit is GitHub's open-source toolkit for Spec-Driven Development (SDD), a methodology that inverts the traditional "code first, specify later" pattern: specifications become executable artifacts that directly drive AI-powered implementation rather than serving as disposable scaffolding. With 102k+ stars and active releases, it is one of the most widely adopted structured AI coding agent workflows in the ecosystem. The `specify` CLI bootstraps projects with template directories, slash commands, and multi-agent integrations (30+ supported agents), turning a vague idea into a constitution → spec → plan → tasks → implementation pipeline managed entirely through coding-agent commands.

_All claims below are sourced from ../../raw/github/github-spec-kit.md unless otherwise noted._

## What it does

Spec Kit provides an end-to-end structured development workflow for AI coding agents. Rather than prompting an agent directly with "build me X", the developer uses a staged sequence of slash commands that progressively sharpen a vague idea into an executable implementation plan, with each step producing a committed artifact the agent can reference in subsequent steps. The toolkit ships as a Python CLI (`specify-cli`) that initialises any directory with the required template files and wires up whichever coding agent integration the developer uses.

## Key features

- **`/speckit.constitution`** — establishes governing project principles (code quality standards, architectural decisions, organisational constraints) stored as `.specify/memory/constitution.md`; consulted by the agent throughout all subsequent phases.
- **`/speckit.specify`** — turns a natural-language problem description into a structured functional specification with user stories and requirements (tech-stack-agnostic).
- **`/speckit.clarify`** — interrogates the specification to surface ambiguities before planning begins; reduces rework.
- **`/speckit.checklist`** — validates requirements completeness, clarity, and consistency ("unit tests for English").
- **`/speckit.plan`** — produces a technical implementation plan given a chosen tech stack and architecture.
- **`/speckit.analyze`** — cross-checks spec, plan, and tasks for consistency before implementation starts.
- **`/speckit.tasks`** — decomposes the plan into a granular, ordered task list; optionally converts tasks to GitHub Issues via `/speckit.taskstoissues`.
- **`/speckit.implement`** — executes all tasks sequentially to build the feature.
- **Extensions** — community-contributed packages that add brand-new commands or workflows (e.g., Jira integration, V-model test tracing, post-implementation review).
- **Presets** — template/command overrides that customise *how* Spec Kit works without adding new capabilities (e.g., Agile vs. Waterfall framing, compliance-oriented spec format, domain-specific terminology, full pirate-speak).
- **Branch-scoped context** — commands automatically detect the active spec from the current Git branch (e.g., `001-feature-name`), keeping parallel development streams isolated.

## Architecture

The Python source lives under `src/specify_cli/`. Each AI agent is a self-contained integration subpackage at `src/specify_cli/integrations/<key>/`, exposing a class that declares metadata and inherits setup/teardown logic from one of five base classes: `MarkdownIntegration`, `TomlIntegration`, `YamlIntegration`, `SkillsIntegration`, or `IntegrationBase`. All built-in integrations are instantiated and loaded into a global `INTEGRATION_REGISTRY` via `_register_builtins()`.

Template resolution at runtime walks a priority stack top-down:

1. Project-local overrides (`.specify/templates/overrides/`)
2. Installed presets (`.specify/presets/templates/`)
3. Installed extensions (`.specify/extensions/templates/`)
4. Spec Kit core defaults (`.specify/templates/`)

Command files are written into agent directories at install time (`specify init` / `specify extension add` / `specify preset add`); the first-match file wins when multiple presets or extensions provide the same command.

Supported command file formats: Markdown (`.md`, most agents), TOML (Gemini), YAML (Goose), and skill directories (`speckit-<name>/SKILL.md` for skills-mode agents such as Codex CLI and Copilot with `--skills`).

## Installation

Requires Python 3.11+ and `uv`. One-shot via `uvx` (no persistent install):

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

Persistent install:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Then bootstrap a project for a specific agent (defaults to GitHub Copilot in non-interactive sessions):

```bash
specify init my-project --integration copilot
specify init my-project --integration codex --integration-options="--skills"
specify init my-project --integration gemini
```

See `specify integration list` for all 30+ supported agents.

## Example usage

Full greenfield feature workflow:

```text
/speckit.constitution Create principles focused on code quality, TDD, functional patterns.
/speckit.specify Build a photo album organiser with drag-and-drop album re-ordering, tile-view within albums, and no nested albums.
/speckit.clarify Focus on offline storage and accessibility requirements.
/speckit.checklist
/speckit.plan Use Vite, vanilla JS/CSS/HTML, SQLite for metadata.
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Each command writes a committed artifact (e.g., `specs/001-feature/`, `.specify/memory/constitution.md`) that the agent reads in subsequent steps. Switching Git branches switches the active spec context automatically.

## When to use

Spec Kit is best suited for: greenfield features where clarity of intent matters before touching code; brownfield work where a detailed plan prevents scope creep; teams that want reproducible, spec-anchored artifacts rather than ephemeral chat-driven development; and organisations that need compliance-ready or audit-traceable specifications. It is less necessary for one-off scripting or exploratory micro-tasks where the overhead of the full pipeline outweighs the benefit.

## Maintenance status

102,408 stars; MIT licence; latest release v0.8.11 (2026-05-16); actively maintained by GitHub. The repository includes `CITATION.cff` and `.zenodo.json` for academic citation. Community extensions, presets, and walkthroughs are catalogued on GitHub Pages at https://github.github.io/spec-kit/.

## Ecosystem

Spec Kit integrates with 30+ coding agents including Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, Cursor, Windsurf, Kiro CLI, Goose, Forge, Pi, opencode, and others. The community extensions and presets registries (hosted on GitHub Pages) are the primary discovery layer. Related tools in this wiki: [[gsd-build-get-shit-done]] offers a similar slash-command-driven structured workflow pattern; [[anthropics-skills]] and [[obra-superpowers]] cover agent skill/capability packaging; [[skills.sh]] is the broader skills distribution ecosystem that Spec Kit's skills-mode integrations participate in.
