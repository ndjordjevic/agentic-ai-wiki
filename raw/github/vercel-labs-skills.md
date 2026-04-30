# vercel-labs/skills

## Metadata
- Stars: 16547
- Forks: 1339
- Primary language: TypeScript
- Default branch: main
- Latest release: v1.5.1 (2026-04-17)
- License: n/a
- Homepage: https://skills.sh
- Fetched: 2026-04-30
- Final URL: https://github.com/vercel-labs/skills

## Description
The open agent skills tool — `npx skills`

## README
# skills

The CLI for the open agent skills ecosystem.

<!-- agent-list:start -->
Supports **OpenCode**, **Claude Code**, **Codex**, **Cursor**, and [50 more](#supported-agents).
<!-- agent-list:end -->

## Install a Skill

```bash
npx skills add vercel-labs/agent-skills
```

### Source Formats

```bash
# GitHub shorthand (owner/repo)
npx skills add vercel-labs/agent-skills

# Full GitHub URL
npx skills add https://github.com/vercel-labs/agent-skills

# Direct path to a skill in a repo
npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

# GitLab URL
npx skills add https://gitlab.com/org/repo

# Any git URL
npx skills add git@github.com:vercel-labs/agent-skills.git

# Local path
npx skills add ./my-local-skills
```

### Options

| Option                    | Description                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-g, --global`            | Install to user directory instead of project                                                                                                       |
| `-a, --agent <agents...>` | Target specific agents (e.g., `claude-code`, `codex`). See Supported Agents                                                                        |
| `-s, --skill <skills...>` | Install specific skills by name (use `'*'` for all skills)                                                                                         |
| `-l, --list`              | List available skills without installing                                                                                                           |
| `--copy`                  | Copy files instead of symlinking to agent directories                                                                                              |
| `-y, --yes`               | Skip all confirmation prompts                                                                                                                      |
| `--all`                   | Install all skills to all agents without prompts                                                                                                   |

### Examples

```bash
# List skills in a repository
npx skills add vercel-labs/agent-skills --list

# Install specific skills
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install a skill with spaces in the name (must be quoted)
npx skills add owner/repo --skill "Convex Best Practices"

# Install to specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# Non-interactive installation (CI/CD friendly)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Install all skills from a repo to all agents
npx skills add vercel-labs/agent-skills --all

# Install all skills to specific agents
npx skills add vercel-labs/agent-skills --skill '*' -a claude-code

# Install specific skills to all agents
npx skills add vercel-labs/agent-skills --agent '*' --skill frontend-design
```

### Installation Scope

| Scope       | Flag      | Location            | Use Case                                      |
| ----------- | --------- | ------------------- | --------------------------------------------- |
| **Project** | (default) | `./<agent>/skills/` | Committed with your project, shared with team |
| **Global**  | `-g`      | `~/<agent>/skills/` | Available across all projects                 |

### Installation Methods

| Method                    | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Symlink** (Recommended) | Creates symlinks from each agent to a canonical copy. Single source of truth, easy updates. |
| **Copy**                  | Creates independent copies for each agent. Use when symlinks aren't supported.              |

## Other Commands

| Command                      | Description                                   |
| ---------------------------- | --------------------------------------------- |
| `npx skills list`            | List installed skills (alias: `ls`)           |
| `npx skills find [query]`    | Search for skills interactively or by keyword |
| `npx skills remove [skills]` | Remove installed skills from agents           |
| `npx skills update [skills]` | Update installed skills to latest versions    |
| `npx skills init [name]`     | Create a new SKILL.md template                |

### `skills list`

```bash
# List all installed skills (project and global)
npx skills list

# List only global skills
npx skills ls -g

# Filter by specific agents
npx skills ls -a claude-code -a cursor
```

### `skills find`

```bash
# Interactive search (fzf-style)
npx skills find

# Search by keyword
npx skills find typescript
```

### `skills update`

```bash
# Update all skills (interactive scope prompt)
npx skills update

# Update a single skill by name
npx skills update my-skill

# Update multiple specific skills
npx skills update frontend-design web-design-guidelines

# Update only global or project skills
npx skills update -g
npx skills update -p

# Non-interactive (auto-detects scope)
npx skills update -y
```

| Option          | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `-g, --global`  | Only update global skills                                                 |
| `-p, --project` | Only update project skills                                                |
| `-y, --yes`     | Skip scope prompt (auto-detect: project if in a project dir, else global) |
| `[skills...]`   | Update specific skills by name instead of all                             |

### `skills init`

```bash
# Create SKILL.md in current directory
npx skills init

# Create a new skill in a subdirectory
npx skills init my-skill
```

### `skills remove`

```bash
# Remove interactively (select from installed skills)
npx skills remove

# Remove specific skill by name
npx skills remove web-design-guidelines

# Remove multiple skills
npx skills remove frontend-design web-design-guidelines

# Remove from global scope
npx skills remove --global web-design-guidelines

# Remove from specific agents only
npx skills remove --agent claude-code cursor my-skill

# Remove all installed skills without confirmation
npx skills remove --all
```

| Option         | Description                                      |
| -------------- | ------------------------------------------------ |
| `-g, --global` | Remove from global scope (~/) instead of project |
| `-a, --agent`  | Remove from specific agents (use `'*'` for all)  |
| `-s, --skill`  | Specify skills to remove (use `'*'` for all)     |
| `-y, --yes`    | Skip confirmation prompts                        |
| `--all`        | Shorthand for `--skill '*' --agent '*' -y`       |

## What are Agent Skills?

Agent skills are reusable instruction sets that extend your coding agent's capabilities. They're defined in `SKILL.md` files with YAML frontmatter containing a `name` and `description`.

Skills let agents perform specialized tasks like:
- Generating release notes from git history
- Creating PRs following your team's conventions
- Integrating with external tools (Linear, Notion, etc.)

## Supported Agents

Skills can be installed to any of these agents:

| Agent | `--agent` | Project Path | Global Path |
|-------|-----------|--------------|-------------|
| AiderDesk | `aider-desk` | `.aider-desk/skills/` | `~/.aider-desk/skills/` |
| Amp, Kimi Code CLI, Replit, Universal | `amp`, `kimi-cli`, `replit`, `universal` | `.agents/skills/` | `~/.config/agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` |
| Augment | `augment` | `.augment/skills/` | `~/.augment/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| Cline, Dexto, Warp | `cline`, `dexto`, `warp` | `.agents/skills/` | `~/.agents/skills/` |
| Codex | `codex` | `.agents/skills/` | `~/.codex/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Goose | `goose` | `.goose/skills/` | `~/.config/goose/skills/` |
| Kilo Code | `kilo` | `.kilocode/skills/` | `~/.kilocode/skills/` |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |
| OpenCode | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` |
| OpenHands | `openhands` | `.openhands/skills/` | `~/.openhands/skills/` |
| Roo Code | `roo` | `.roo/skills/` | `~/.roo/skills/` |
| Trae | `trae` | `.trae/skills/` | `~/.trae/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| (+ many more) | | | |

## Creating Skills

Skills are directories containing a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# My Skill

Instructions for the agent to follow when this skill is activated.

## When to Use

Describe the scenarios where this skill should be used.

## Steps

1. First, do this
2. Then, do that
```

### Required Fields

- `name`: Unique identifier (lowercase, hyphens allowed)
- `description`: Brief explanation of what the skill does

### Optional Fields

- `metadata.internal`: Set to `true` to hide the skill from normal discovery. Internal skills are only visible and installable when `INSTALL_INTERNAL_SKILLS=1` is set.

### Skill Discovery

The CLI searches for skills in these locations within a repository:
- Root directory (if it contains `SKILL.md`)
- `skills/`
- `skills/.curated/`
- `skills/.experimental/`
- `skills/.system/`
- `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, `.goose/skills/`, etc. (all agent-specific paths)

### Plugin Manifest Discovery

If `.claude-plugin/marketplace.json` or `.claude-plugin/plugin.json` exists, skills declared in those files are also discovered. Enables compatibility with the Claude Code plugin marketplace ecosystem.

## Compatibility

Skills are generally compatible across agents since they follow a shared [Agent Skills specification](https://agentskills.io). Some features are agent-specific (e.g., `context: fork` only on Claude Code; Hooks on Claude Code, Cline, and Kiro CLI).

## Environment Variables

| Variable                  | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| `INSTALL_INTERNAL_SKILLS` | Set to `1` or `true` to show and install skills marked as `internal: true` |
| `DISABLE_TELEMETRY`       | Set to disable anonymous usage telemetry                                   |
| `DO_NOT_TRACK`            | Alternative way to disable telemetry                                       |

## Telemetry

Collects anonymous usage data (which skills are installed — no personal info). Automatically disabled in CI environments.

## Related Links

- [Agent Skills Specification](https://agentskills.io)
- [Skills Directory](https://skills.sh)
- [Vercel Agent Skills Repository](https://github.com/vercel-labs/agent-skills)

## License

MIT

## Top-level structure
- `.github/` — CI/CD workflows
- `.gitignore`
- `.husky/` — git hooks
- `.prettierrc` — code formatter config
- `AGENTS.md` — agent instructions file
- `README.md`
- `ThirdPartyNoticeText.txt` — third-party license notices
- `bin/` — CLI entry points
- `build.config.mjs` — build configuration
- `package.json`
- `pnpm-lock.yaml`
- `scripts/` — utility scripts
- `skills/` — skill definitions shipped with the CLI
- `src/` — TypeScript source code
- `tests/` — test files
- `tsconfig.json` — TypeScript configuration
