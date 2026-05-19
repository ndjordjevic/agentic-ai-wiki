# github/spec-kit

## Metadata
- Stars: 102408
- Primary language: Python
- Default branch: main
- Latest release: v0.8.11 (2026-05-16)
- License: MIT License
- Homepage: https://github.github.com/spec-kit/
- Fetched: 2026-05-19
- Final URL: https://github.com/github/spec-kit

## Description
💫 Toolkit to help you get started with Spec-Driven Development

## README

<div align="center">
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.

---

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Requires **uv** (https://docs.astral.sh/uv/). Replace `vX.Y.Z` with the latest tag from Releases:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

### 2. Initialize a project

```bash
specify init my-project --integration copilot
cd my-project
```

### 3. Establish project principles

Launch your coding agent in the project directory. Most agents expose spec-kit as `/speckit.*` slash commands; Codex CLI in skills mode uses `$speckit-*` instead.

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 4. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums.
```

### 5. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

### 6. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

### 7. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

## 🤖 Supported AI Coding Agent Integrations

Spec Kit works with 30+ AI coding agents — both CLI tools and IDE-based assistants.

Run `specify integration list` to see all available integrations in your installed version.

## Available Slash Commands

#### Core Commands

| Command | Agent Skill | Description |
|---|---|---|
| `/speckit.constitution` | `speckit-constitution` | Create or update project governing principles and development guidelines |
| `/speckit.specify` | `speckit-specify` | Define what you want to build (requirements and user stories) |
| `/speckit.plan` | `speckit-plan` | Create technical implementation plans with your chosen tech stack |
| `/speckit.tasks` | `speckit-tasks` | Generate actionable task lists for implementation |
| `/speckit.taskstoissues` | `speckit-taskstoissues` | Convert generated task lists into GitHub issues for tracking and execution |
| `/speckit.implement` | `speckit-implement` | Execute all tasks to build the feature according to the plan |

#### Optional Commands

| Command | Agent Skill | Description |
|---|---|---|
| `/speckit.clarify` | `speckit-clarify` | Clarify underspecified areas (recommended before `/speckit.plan`) |
| `/speckit.analyze` | `speckit-analyze` | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`) |
| `/speckit.checklist` | `speckit-checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency |

## 🔧 Specify CLI Reference

For full command details, options, and examples, see the CLI Reference at https://github.github.io/spec-kit/reference/overview.html.

## 🧩 Making Spec Kit Your Own: Extensions & Presets

Spec Kit can be tailored through two complementary systems — **extensions** and **presets**:

| Priority | Component Type | Location |
|---|---|---|
| ⬆ 1 | Project-Local Overrides | `.specify/templates/overrides/` |
| 2 | Presets — Customize core & extensions | `.specify/presets/templates/` |
| 3 | Extensions — Add new capabilities | `.specify/extensions/templates/` |
| ⬇ 4 | Spec Kit Core — Built-in SDD commands & templates | `.specify/templates/` |

### Extensions — Add New Capabilities

Use **extensions** when you need functionality beyond Spec Kit's core. Extensions introduce new commands and templates.

```bash
# Search available extensions
specify extension search

# Install an extension
specify extension add <extension-name>
```

### Presets — Customize Existing Workflows

Use **presets** when you want to change *how* Spec Kit works without adding new capabilities.

```bash
# Search available presets
specify preset search

# Install a preset
specify preset add <preset-name>
```

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase | Focus | Key Activities |
|---|---|---|
| **0-to-1 Development** ("Greenfield") | Generate from scratch | Start with high-level requirements, generate specifications, plan implementation steps, build production-ready applications |
| **Creative Exploration** | Parallel implementations | Explore diverse solutions, support multiple technology stacks & architectures, experiment with UX patterns |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | Add features iteratively, modernize legacy systems, adapt processes |

## 🔧 Prerequisites

- Linux/macOS/Windows
- Supported AI coding agent
- uv (https://docs.astral.sh/uv/) for package management (recommended) or pipx for persistent installation
- Python 3.11+
- Git

## Docs

### docs/quickstart.md

Recommended Workflow:

For quick experiments, use the lean feature path: `/speckit.specify` -> `/speckit.plan` -> `/speckit.tasks` -> `/speckit.implement`.

For production features or any work with meaningful ambiguity, treat `/speckit.clarify`, `/speckit.checklist`, and `/speckit.analyze` as regular quality gates:

```text
/speckit.constitution -> /speckit.specify -> /speckit.clarify -> /speckit.checklist -> /speckit.plan -> /speckit.tasks -> /speckit.analyze -> /speckit.implement
```

Install via uvx (no persistent install required):

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

Or install persistently:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Context Awareness: Spec Kit commands automatically detect the active feature based on your current Git branch (e.g., `001-feature-name`). To switch between different specifications, simply switch Git branches.

### docs/concepts/sdd.md

**What is Spec-Driven Development?**

Spec-Driven Development flips the script on traditional software development — specifications become executable, directly generating working implementations rather than just guiding them.

Core Philosophy:
- Intent-driven development where specifications define the "what" before the "how"
- Rich specification creation using guardrails and organizational principles
- Multi-step refinement rather than one-shot code generation from prompts
- Heavy reliance on advanced AI model capabilities for specification interpretation

Docs structure (`docs/`): quickstart.md, installation.md, upgrade.md, local-development.md, concepts/ (sdd.md), reference/ (CLI reference, integrations, extensions, presets), community/ (extensions, presets, walkthroughs, friends), install/ (uv, etc.), template/

## AGENTS.md (key agent integration documentation)

**About Spec Kit and Specify:**

GitHub Spec Kit is a comprehensive toolkit for implementing Spec-Driven Development (SDD). The toolkit includes templates, scripts, and workflows. Specify CLI bootstraps projects with the Spec Kit framework, setting up directory structures, templates, and AI agent integrations.

**Integration Architecture:**

Each AI agent is a self-contained integration subpackage under `src/specify_cli/integrations/<key>/`. Built-in integrations are registered via `INTEGRATION_REGISTRY` in `__init__.py`.

Base classes:
- `MarkdownIntegration` — standard markdown commands (`.md`) — most agents use this
- `TomlIntegration` — TOML-format commands (`.toml`)
- `YamlIntegration` — YAML recipe files (`.yaml`)
- `SkillsIntegration` — skill directories (`speckit-<name>/SKILL.md`)
- `IntegrationBase` — fully custom output (companion files, settings merge, etc.)

Key integration config fields: `key`, `config` (name/folder/commands_subdir/install_url/requires_cli), `registrar_config` (dir/format/args/extension), `context_file`.

Special integrations:
- **Copilot**: uses `.agent.md` commands + companion `.prompt.md` files, merges `.vscode/settings.json`; supports skills mode via `--integration-options="--skills"` → `speckit-<name>/SKILL.md` under `.github/skills/`
- **Gemini**: TOML format, `.gemini/commands/`, `{{args}}` placeholder
- **Codex**: SkillsIntegration, `.agents/skills/`, `AGENTS.md` context file
- **Goose**: YAML format, `.goose/recipes/`, `{{args}}` placeholder

Argument Patterns:
- Markdown/prompt-based: `$ARGUMENTS`
- TOML/YAML-based: `{{args}}`
- Script placeholders: `{SCRIPT}` (replaced with actual script path)

## Top-level structure

```
.devcontainer/          — Dev container configuration for VS Code / Codespaces
.github/                — CI/CD workflows and GitHub configuration (boilerplate)
.gitattributes          — Git line-ending settings
.gitignore              — Standard Python ignores
.markdownlint-cli2.jsonc — Markdown lint configuration
.zenodo.json            — Academic citation metadata
AGENTS.md               — AI agent integration docs and architecture reference
CHANGELOG.md            — Version history and release notes
CITATION.cff            — Citation file for academic use
CODE_OF_CONDUCT.md
CONTRIBUTING.md         — Contribution guidelines
DEVELOPMENT.md          — Developer setup and workflow
LICENSE                 — MIT License
README.md               — Primary project documentation
SECURITY.md
SUPPORT.md
docs/                   — Full documentation (GitHub Pages via DocFX)
extensions/             — Community extension catalog and publishing guide
integrations/           — Integration definitions and catalog
media/                  — Logos, screenshots, GIFs
```
