# michael-denyer/pstack-claude

## Metadata
- Stars: 747
- Primary language: JavaScript
- Default branch: main
- Latest release: v0.9.57 (2026-10-01)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-10-02
- Final URL: https://github.com/michael-denyer/pstack-claude

## Description
Claude Code, Codex, OpenCode, Gemini, and Prime Agent versions of Poteto's pstack. Rigorous agent workflows with Cursor primitives translated for other harnesses.

## README
# pstack

Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) is an opinionated Cursor skill stack that improves agent outcomes. This is a port for Claude Code, Codex and other agent harnesses. It tracks upstream and also carries named policy forks, each declared in [`tools/forks.json`](tools/forks.json).

Tell `poteto-mode` your goal and it will invoke the correct workflow for the task. It keeps your code concise, simple and verified.

For concurrency bugs and invariants that tests cannot reach, see the separate [agent-formal-verify](https://github.com/michael-denyer/agent-formal-verify) plugin, which adds TLA+ model checking and Lean proofs.

## Install

### Claude Code

Run in Claude Code:

```text
/plugin marketplace add michael-denyer/pstack-claude
/plugin install pstack@pstack-claude
```

### Codex

Run in your terminal:

```shell
codex plugin marketplace add michael-denyer/pstack-claude
codex plugin add pstack@pstack-claude
```

Run `setup-pstack` to change model defaults, set a reasoning effort per role (for example `arena runners: opus @xhigh, fable @max`, which Claude Code dispatches through the plugin's `pstack:effort-<level>` or `pstack:poteto-agent-<level>` agents; roles without a level keep the session's effort unless the sheet's `default effort` line names one), or turn automatic routing off. The plugin installs the routing hook on Claude Code and Codex; Codex asks you to trust it through `/hooks` before it runs. In Claude Code, use `/pstack:setup-pstack`.

For Prime Agent, OpenCode, Gemini CLI, or skills-only installs for any harness, see [shared installation](docs/reference.md#shared-skills-installation).

## Getting started

```text
Use poteto-mode to fix the search filter resetting when I change pages.
```

For a bug, it reproduces the failure, uses `how` and `why` to investigate, delegates the fix, then reruns the failing case. If the fix crosses a function boundary, it brings in `architect` before implementation. You receive the fix and the failing and passing evidence.

[Other playbooks](plugins/pstack/skills/poteto-mode/SKILL.md#playbooks) cover planning, features, refactoring, performance issues, investigations, prototypes, PR maintenance, shipping, and longer projects.

## Details

- [Skills and slash commands](docs/reference.md#slash-commands)
- [Runtime setup](docs/reference.md#runtime-support)
- [Models and dependencies](docs/reference.md#configuration-and-dependencies)
- [Maintenance and port scope](docs/reference.md#maintenance)

## Data handling

pstack has no server or telemetry. Anything its skills ask your agent to read, including session transcripts, goes to your model provider. Scripts run locally, and PR tools use your GitHub CLI login.

## Contributing

Thanks for helping make this port better. Bug reports, documentation fixes, and runtime improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the checks and where your change belongs. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## License

This port, including its modifications and additions, is also [MIT-licensed](LICENSE), © 2026 Michael Denyer. Original pstack © 2026 Lauren Tan; imported cursor-team-kit skills © 2026 Cursor. See [LICENSE-cursor-team-kit](LICENSE-cursor-team-kit) and [NOTICE.md](NOTICE.md).

## Docs

### docs/reference.md

# pstack reference

Start with the [README](../README.md) for installation and your first task.

## Slash commands

The package includes 54 skill directories: 31 public skills and 23 `principle-*` references. Claude Code uses `/pstack:<name>`. In Codex, request a skill by name or install the optional shortcuts for the `/name` form below.

Find each skill's instructions in the [skills tree](../plugins/pstack/skills/).

| command | use it when |
| --- | --- |
| `/poteto-mode` | default entry point for any non-trivial task |
| `/how` | walk through how a subsystem works |
| `/why` | investigate why something was built this way (parallel multi-MCP evidence) |
| `/architect` | settle types and module shape before writing code that crosses a function boundary |
| `/arena` | run N parallel attempts at the same task and pick the best parts |
| `/interrogate` | have three different models try to break a diff |
| `/automate-me` | draft your own personal -mode skill from recent transcripts |
| `/reflect` | capture a long task's lessons as a skill edit |
| `/tdd` | fix a bug by writing the failing test first, then the fix |
| `/typescript-best-practices` | ground type-system discipline in TypeScript syntax |
| `/teach` | explain a subsystem plainly by composing how + why |
| `/swarm` | fan out N parallel workers across slices or races, then return one aggregated report |
| `/technical-writing` | write docs, RFCs, readmes, PR descriptions, and commit messages to one layered standard |
| `/bro` | restate the last message in plain human language, no jargon |
| `/figure-it-out` | design a rigorous, auditable playbook for a task no bundled playbook fits |
| `/show-me-your-work` | log decisions to a reviewable tsv decision trail |
| `/blast-radius` | find what a change could break beyond the diff and prove safety by running code |
| `/recall` | catch up on recent working context from chat history, live state, and the shared record |
| `/setup-pstack` | configure pstack per-role model choices |
| `/unslop` | clean up writing by removing AI tells |
| `/no-comments` | strip comments before review, fix the accepted findings, encode claimed constraints |
| `/create-verification-skill` | generate a project-local verification skill and feature map |
| `/maintain-verification-skill` | re-sync a drifted verification skill and its feature map |
| `/deslop` | deslop a diff before commit |
| `/babysit` | monitor an open PR, fix CI/comments, keep it merge-ready |
| `/thermo-nuclear-code-quality-review` | extremely strict maintainability audit |
| `/make-pr-easy-to-review` | clean noisy history and improve PR description before review |
| `/fix-ci` | find failing PR checks, inspect logs, apply focused fixes |
| `/fix-merge-conflicts` | non-interactively resolve merge conflicts, validate, finalize |
| `/get-pr-comments` | fetch and summarize review comments from the active PR |
| `/what-did-i-get-done` | summarize authored commits over a user-chosen period |

## Runtime support

All runtimes share one skills tree (`plugins/pstack/skills/`). A skills-only installation includes the skills, scripts, agent references, and license notices. The Claude Code and Codex plugins also install automatic routing hooks. Codex command shortcuts are separate.

| Runtime | Setup and recorded verification |
| --- | --- |
| Claude Code | Install the marketplace plugin. Skills use Claude tool names and model defaults; the plugin installs automatic routing. |
| Codex | Install the native plugin through the repository's marketplace and trust its hook through `/hooks`. The Codex mapping translates Claude tools and model names. Shared skill symlinks were also detected in a live session. |
| Prime Agent | Its documentation describes shared-directory discovery; it has not been tested in a live session. Choose tools and models through Prime's configuration. |
| opencode | Discovery and reading a linked skill were verified on version 1.18.25. Configure agents, commands, and permissions in `opencode.json`. Its picker also lists principle skills. |
| Gemini CLI | Its documentation describes shared-directory discovery; it has not been tested in a live session. Use `/skills list` to check discovery and `/skills reload` after changes. |

These checks cover skill discovery. Delegation and multi-model workflows remain unverified on Prime Agent, opencode, and Gemini CLI. On those runtimes, agents must adapt Claude-specific tools, models, and configuration. The Codex mapping applies only to Codex.

### Automatic routing

The Claude Code and Codex plugins share a SessionStart hook (`plugins/pstack/hooks/session-start.sh`) that loads a short routing instruction (`plugins/pstack/hooks/session-start-context.md`) on startup, resume, clear, and compact. Codex requires the user to trust plugin hooks through `/hooks`. The instruction invokes `poteto-mode` when a task meets any of these conditions:

- It touches more than one file or changes a signature other files call.
- It involves a design or architecture choice.
- It concerns a bug with an unknown cause or a performance issue.

Smaller tasks proceed directly. The full skill loads when invoked, and explicit user instructions take precedence.

To disable routing, run `setup-pstack` and turn off the session hook. In Claude Code, use `/pstack:setup-pstack`. You can also write `session hook: off` in the runtime's sheet. The hook reads that setting before injecting its instruction. Without the setting, routing stays on.

Skills-only installs and other runtimes do not include the hook. Request `poteto-mode` explicitly, or add a standing instruction to the runtime's instruction file.

### Shared skills installation

Use this path for Prime Agent, opencode, Gemini CLI, or a skills-only Codex installation. Clone the repository and link its skills into `~/.agents/skills/`:

```shell
git clone https://github.com/michael-denyer/pstack-claude
cd pstack-claude
mkdir -p ~/.agents/skills
for s in plugins/pstack/skills/*/; do
  target=~/.agents/skills/"$(basename "$s")"
  test -e "$target" || test -L "$target" || ln -s "$PWD/$s" "$target"
done
```

Keep all skill directories, including the principle references. Leave the clone at this path while the links are installed.

### Manage linked skills

If a destination already exists, inspect it before replacing it. The installation skips existing files, directories, and links.

To update, pull changes in the clone that the links point to. To uninstall a linked skill, remove its link at `~/.agents/skills/<name>`. This removes it from every runtime using that directory.

### Install with the skills CLI

To install without keeping a local clone:

```shell
npx skills add https://github.com/michael-denyer/pstack-claude/tree/main/plugins/pstack/skills --skill "*" --agent "*" --yes
```

The CI installation check (`.github/workflows/ci.yml`) uses the skills CLI to copy the checkout's skill tree and compare the installed files with their sources.

### Codex

The native plugin manifest (`plugins/pstack/.codex-plugin/plugin.json`) points to the shared skills directory and the Codex SessionStart hook (`plugins/pstack/hooks/codex-hooks.json`). The marketplace catalog (`.agents/plugins/marketplace.json`) lists `pstack` in the `pstack-claude` marketplace. Review and trust the hook through `/hooks`; Codex asks again when its definition changes.

The README installation registers that catalog with `codex plugin marketplace add`, then installs the plugin with `codex plugin add`. These commands match the help output from `codex-cli 0.154.0-alpha.6.2`. A fresh native installation was not tested for this documentation change.

Request `poteto-mode` by name or select its entry, such as `pstack:poteto-mode`. To enable parallel subagents:

```toml
[features]
multi_agent = true
```

Add this setting to `~/.codex/config.toml` if subagents are disabled. Skills such as `arena`, `interrogate`, and `architect` use parallel agents. The mapping (`plugins/pstack/skills/poteto-mode/references/codex-tools.md`) describes a sequential fallback and translates Claude tool names, model defaults, and verification instructions.

For optional slash-command shortcuts, run this from the clone's root:

```shell
mkdir -p ~/.codex/prompts
for c in plugins/pstack/.codex-plugin/prompts/*.md; do
  target=~/.codex/prompts/"$(basename "$c")"
  test -e "$target" || test -L "$target" || ln -s "$PWD/$c" "$target"
done
```

Each shortcut invokes its skill. The commands skip existing files and links. Remove a shortcut by deleting its link at `~/.codex/prompts/<name>.md`. Both native-plugin and skills-only installations work without these shortcuts.

## Configuration and dependencies

Invoke setup-pstack to choose models for each role. It detects available models, confirms the choices, and writes an override sheet. Its runtime table names the sheet path and loading mechanism for each runtime. Defaults live in `plugins/pstack/models.json`.

For design comparisons and reviews, choose distinct models available to your runtime. The default panel uses different Claude models.

Install dependencies for the workflows you use:

| Dependency | When you need it |
| --- | --- |
| GitHub CLI, `gh` | PR monitoring and shipping. Authenticate with `gh auth login`. |
| Bun | The bundled `watch-pr` and `orch` scripts. Their bootstrap installs script dependencies on first run. |
| Graphite CLI, `gt` | The Orchestrate playbook and `orch` stack frontier. Shipping and autopilot playbooks use `gh` or Origin's CLI when available. |
| `plugin-dev` | Claude Code skill-authoring guidance used by `automate-me`, `reflect`, and `poteto-mode`. |

Install the Claude Code skill-authoring companion with:

```text
/plugin marketplace add anthropics/claude-plugins-official
/plugin install plugin-dev@claude-plugins-official
```

Those authoring workflows need `plugin-dev` for their guidance; other workflows do not. Codex uses the equivalent named in its mapping.

Playbooks use the runtime's task-tracking tools or an uncommitted `todo.md` checklist. For Claude Code, the repository documents `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`.

Use create-verification-skill to record how the agent should run and check your project, following the driver policy.

## Maintenance

### Repository layout

```text
.claude-plugin/marketplace.json    Claude Code marketplace
.agents/plugins/marketplace.json  Codex marketplace
plugins/pstack/
  .claude-plugin/plugin.json      Claude Code plugin manifest
  .codex-plugin/                  Codex manifest and generated prompt stubs
  skills/                        Shared skills, references, and scripts
  agents/                        Claude Code subagent definitions
  hooks/                         Claude Code startup routing
tools/                           Generation, validation, and upstream sync
tests/                           Repository checks
```

Skills-only installs use `plugins/pstack/skills/`. Agent references and license files are included under `poteto-mode/references/`.

### Generated files and checks

The generator (`tools/generate.mjs`) updates versions, model defaults, Codex prompts, and portable reference files. The slash-command table supplies the Codex prompt descriptions and order. Edit that table when changing a menu description, then regenerate. Keep a row for every public skill, with `poteto-mode` first.

Documentation fact tests (`tests/readme-facts.test.mjs`) check the skill counts and upstream pin. The table parser requires the header `| command | use it when |`.

Run the generator and repository tests with Bun:

```shell
bun tools/generate.mjs
bun test tests/
```

CI also checks shell scripts, workflows, Markdown, relative links, and the bundled Bun tools.

### Port scope and attribution

The skill tree is synced against upstream `12d587d` (v0.15.5).

This repository ports Lauren Tan's pstack from Cursor to Claude Code and shares the skills with other runtimes. It includes seven cursor-team-kit skills and an independently authored `babysit` skill. The port supplies Claude Code plugin registration and routing, Codex manifests and shortcuts, and the Codex tool mapping.

Cursor-specific automations, sticky-mode metadata, the Grok Bot UI workflow, and the Cursor UI tutorial are excluded. `tools/upstream.json` records the revisions and exclusions, `tools/substitutions.json` holds the Cursor-to-Claude rewrite rules, and `CHANGES.md` records each release. The bundled `thermo-nuclear-code-quality-review` provides a maintainability review when a workflow calls for one.

For skill changes, follow the sync boundary in CONTRIBUTING.md. Runtime adaptations and workflow changes both land here, and a workflow change is declared as a fork.

See the license summary in README.md for licenses and full-plugin attribution. `NOTICE-skills.md` is the notice for skills-only installations.

## Top-level structure
- `.agents/` — Codex plugin marketplace catalog (`.agents/plugins/marketplace.json`)
- `.claude-plugin/` — Claude Code marketplace manifest
- `.github/` — CI workflows, including the skills-CLI installation check
- `CHANGES.md` — per-release change log
- `CONTEXT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `NOTICE.md`, `NOTICE-skills.md`, `LICENSE`, `LICENSE-cursor-team-kit` — project/contribution/licensing docs
- `assets/` — images (e.g. `pstack-overview.png` workflow diagram)
- `docs/reference.md` — full slash-command table, runtime support matrix, configuration/dependencies, and maintenance notes (fetched in full above)
- `plugins/pstack/` — the actual plugin: `.claude-plugin/`, `.codex-plugin/` manifests; `skills/` (shared skill tree used by every runtime); `agents/` (Claude Code subagent definitions); `effort-agents/`; `hooks/` (Claude Code/Codex SessionStart routing hook); `models.json` (per-role model defaults)
- `tools/` — `forks.json` (named policy forks vs. upstream), `generate.mjs` (regenerates versions/prompts/reference files), `substitutions.json` (Cursor→Claude rewrite rules), `sync.mjs` (upstream sync), `upstream.json` (pinned upstream revision/exclusions), `validate-skills.mjs`
- `tests/` — repository checks, including `readme-facts.test.mjs` (skill-count and upstream-pin fact tests)
