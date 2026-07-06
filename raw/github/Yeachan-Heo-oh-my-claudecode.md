# Yeachan-Heo/oh-my-claudecode

## Metadata
- Stars: 37438
- Primary language: TypeScript
- Default branch: main
- Latest release: v4.15.2 (2026-07-03)
- License: MIT License
- Homepage: https://oh-my-claudecode.dev
- Fetched: 2026-07-06
- Final URL: https://github.com/Yeachan-Heo/oh-my-claudecode

## Description
Teams-first Multi-agent orchestration for Claude Code

## README
English | [한국어](README.ko.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Português](README.pt.md)

# oh-my-claudecode

[![npm version](https://img.shields.io/npm/v/oh-my-claude-sisyphus?color=cb3837)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![npm downloads](https://img.shields.io/npm/dm/oh-my-claude-sisyphus?color=blue)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![GitHub stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat&color=yellow)](https://github.com/Yeachan-Heo/oh-my-claudecode/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Sponsor](https://img.shields.io/badge/Sponsor-❤️-red?style=flat&logo=github)](https://github.com/sponsors/Yeachan-Heo)
[![Discord](https://img.shields.io/discord/1452487457085063218?color=5865F2&logo=discord&logoColor=white&label=Discord)](https://discord.gg/PUwSMR9XNk)

> **For Codex users:** Check out [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) — the same orchestration experience for OpenAI Codex CLI.

**Multi-agent orchestration for Claude Code. Zero learning curve.**

_Don't learn Claude Code. Just use OMC._

[Get Started](#quick-start) • [Documentation](https://yeachan-heo.github.io/oh-my-claudecode-website) • [CLI Reference](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#cli-reference) • [Workflows](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#workflows) • [Migration Guide](docs/MIGRATION.md) • [Discord](https://discord.gg/PUwSMR9XNk)

---

## Core Maintainers

| Role           | Name        | GitHub                                         |
| -------------- | ----------- | ---------------------------------------------- |
| Creator & Lead | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |

## Ambassadors

| Name       | GitHub                                           |
| ---------- | ------------------------------------------------ |
| Sigrid Jin | [@sigridjineth](https://github.com/sigridjineth) |

## Document Specialists

| Name    | GitHub                                 |
| ------- | -------------------------------------- |
| devswha | [@devswha](https://github.com/devswha) |

## Top Collaborators

| Name           | GitHub                                         | Commits |
| -------------- | ---------------------------------------------- | ------- |
| JunghwanNA     | [@shaun0927](https://github.com/shaun0927)     | 65      |
| riftzen-bit    | [@riftzen-bit](https://github.com/riftzen-bit) | 52      |
| Seunggwan Song | [@Nathan-Song](https://github.com/Nathan-Song) | 20      |
| BLUE           | [@blue-int](https://github.com/blue-int)       | 20      |
| Junho Yeo      | [@junhoyeo](https://github.com/junhoyeo)       | 15      |

## Quick Start

**Step 1: Install**

Marketplace/plugin install (recommended for most Claude Code users).
These are Claude Code slash commands — enter them **one at a time** (pasting both lines at once will fail):

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

Then:

```bash
/plugin install oh-my-claudecode
```

If you prefer the npm CLI/runtime path instead of the marketplace flow:

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **Known npm warning:** npm may print `deprecated prebuild-install@7.1.3` during the CLI install.
> This currently comes from the upstream `better-sqlite3` native-addon dependency
> (`better-sqlite3 -> prebuild-install`); `prebuild-install@7.1.3` is still the latest
> published version, so there is no safe repo-side dependency bump or override to remove
> the warning yet. The warning is tracked in [#2913](https://github.com/Yeachan-Heo/oh-my-claudecode/issues/2913)
> and does not by itself mean the OMC CLI install failed.

**Step 2: Setup**

```bash
# Inside a Claude Code / OMC session
/setup
/omc-setup

# From your terminal
omc setup
```

If you run OMC via `omc --plugin-dir <path>` or `claude --plugin-dir <path>`, add `--plugin-dir-mode` to `omc setup` (or export `OMC_PLUGIN_ROOT` before running it) so the installer doesn't duplicate skills/agents that the plugin already provides at runtime. See the [Plugin directory flags section in REFERENCE.md](./docs/REFERENCE.md#plugin-directory-flags) for a complete decision matrix and all available flags.

**Step 3: Build something**

```bash
# Inside a Claude Code / OMC session
/autopilot "build a REST API for managing tasks"

# Natural-language in-session shortcut
autopilot: build a REST API for managing tasks
```

That's it. Everything else is automatic.

### CLI Commands vs In-Session Skills

OMC exposes two different surfaces:

- **Terminal CLI commands**: run `omc ...` from your shell after installing the npm/runtime path (`npm i -g oh-my-claude-sisyphus@latest`) or from a local checkout.
- **In-session skills**: run `/...` inside a Claude Code session after installing the plugin/setup flow.

| Feature                                        | Terminal CLI                                  | In-session skill                                                        | Notes                                                                                                                                |
| ---------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Setup                                          | `omc setup`                                   | `/setup` or `/omc-setup`                                                | Both are real entrypoints. `/setup` is the easiest plugin-first path.                                                                |
| Ask providers                                  | `omc ask codex "review this patch"`           | `/ask codex "review this patch"`                                        | Both route through the same advisor flow. Providers: `claude`, `codex`, `gemini`, `antigravity`, `grok`, `cursor`.                                            |
| Team orchestration                             | `omc team 2:codex "review auth flow"`         | `/team 3:executor "fix all TypeScript errors"`                          | Both exist, but they are different runtimes: `omc team` launches tmux CLI workers; `/team` runs the in-session native team workflow. |
| Autopilot / Ralph / Ultrawork / Deep Interview | —                                             | `/autopilot ...`, `/ralph ...`, `/ultrawork ...`, `/deep-interview ...` | These are in-session skills. There is no `omc autopilot` / `omc ralph` / `omc ultrawork` CLI subcommand in this repo.                |
| Autoresearch                                   | `omc autoresearch` (**hard-deprecated shim**) | `/deep-interview --autoresearch ...` + `/oh-my-claudecode:autoresearch` | Setup stays in deep-interview; execution now belongs to the stateful skill.                                                          |

### VS Code, Agent SDK, and automation scope

- **VS Code / IDE extension**: OMC does not ship a VS Code extension and does not document extension-specific install or automation flows. Use the Claude Code plugin or terminal CLI surfaces above; IDE integrations are only an optional way to access Claude Code itself.
- **Agent SDK / programmatic usage**: the npm package exports TypeScript helpers such as `createOmcSession()` and prompt expansion utilities for local Node.js programs using `@anthropic-ai/claude-agent-sdk`. This is a library surface, not a replacement for the Claude Code plugin UI.
- **CI/CD and headless automation**: prefer deterministic terminal commands (`omc setup`, `omc ask`, `omc session search`, repository scripts such as `npm run sync-metadata:verify`) and set `ANTHROPIC_API_KEY` or provider-specific CLI auth in the runner environment. Do not rely on interactive slash commands (`/autopilot`, `/ralph`, `/team`) in CI; they require an active Claude Code session.

### Not Sure Where to Start?

If you're uncertain about requirements, have a vague idea, or want to micromanage the design:

```
/deep-interview "I want to build a task management app"
```

The deep interview uses Socratic questioning to clarify your thinking before any code is written. It exposes hidden assumptions and measures clarity across weighted dimensions, ensuring you know exactly what to build before execution begins.

## Team Mode (Recommended)

Starting in **v4.1.7**, **Team** is the canonical orchestration surface in OMC. The legacy `swarm` keyword/skill has been removed; use `team` directly.

```bash
/team 3:executor "fix all TypeScript errors"
```

Use `/team ...` when you want Claude Code's in-session native team workflow. Use `omc team ...` when you want terminal-launched tmux CLI workers (`claude` / `codex` / `gemini` panes).

Team runs as a staged pipeline:

`team-plan → team-prd → team-exec → team-verify → team-fix (loop)`

Enable Claude Code native teams in `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

> If teams are disabled, OMC will warn you and fall back to non-team execution where possible.

### tmux CLI Workers — Codex, Gemini & Antigravity (v4.4.0+)

**v4.4.0 removes the Codex/Gemini MCP servers** (`x`, `g` providers). Use the CLI-first Team runtime (`omc team ...`) to spawn real tmux worker panes:

```bash
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team 2:antigravity "redesign UI components for accessibility"
omc team 1:claude "implement the payment flow"
omc team 1:cursor "implement the payment flow"
omc team status auth-review
omc team shutdown auth-review
```

`/omc-teams` remains as a legacy compatibility skill and now routes to `omc team ...`.

For mixed Codex + Antigravity work in one command, use the **`/ccg`** skill (routes via `/ask codex` + `/ask antigravity`, then Claude synthesizes; Gemini remains available as an enterprise/API-key fallback):

```bash
/ccg Review this PR — architecture (Codex) and UI components (Antigravity)
```

| Surface                         | Workers                       | Best For                                     |
| ------------------------------- | ----------------------------- | -------------------------------------------- |
| `omc team N:codex "..."`        | N Codex CLI panes             | Code review, security analysis, architecture |
| `omc team N:gemini "..."`       | N Gemini CLI panes            | UI/UX design, docs, large-context tasks (enterprise/API-key) |
| `omc team N:antigravity "..."`  | N Antigravity (`agy`) panes   | UI/UX design, docs, large-context tasks                      |
| `omc team N:grok "..."`         | N Grok Build CLI panes        | Code review, analysis cross-check            |
| `omc team N:cursor "..."`       | N Cursor agent panes          | Executor-style implementation tasks          |
| `omc team N:claude "..."`       | N Claude CLI panes            | General tasks via Claude CLI in tmux         |
| `/ccg`                          | /ask codex + /ask antigravity | Tri-model advisor synthesis                  |

Workers spawn on-demand and die when their task completes — no idle resource usage. Requires the selected CLI (`codex`, `gemini`, `agy` (antigravity), `grok`, or `cursor-agent`) installed/authenticated and an active tmux session.

Autopilot can prefer Cursor executor workers during team execution via `.claude/omc.jsonc`:

```jsonc
{
  "autopilot": {
    "execution": "team",
    "team": { "agentTypes": ["cursor"] }
  }
}
```

This config makes the autopilot execution stage use `omc team 1:cursor "..."` or `/omc-teams 1:cursor "..."` for executor-style implementation work. Reviewer, critic, security-review, validation verdict, and final approval roles remain native Claude/OMC reviewer roles; Cursor requires an installed/authenticated `cursor-agent`.

Native team worker worktrees are being added behind an opt-in/config gate. See [Native Team Worktree Mode](docs/TEAM-WORKTREE-MODE.md) for the workspace contract, canonical state-root rules, dirty-worktree preservation policy, and verification checklist.

> **Note: Package naming** — The project is branded as **oh-my-claudecode** (repo, plugin, commands), but the npm package is published as [`oh-my-claude-sisyphus`](https://www.npmjs.com/package/oh-my-claude-sisyphus). If you install or upgrade the CLI tools via npm/bun, use `npm i -g oh-my-claude-sisyphus@latest`; the package installs both `oh-my-claudecode` and the short `omc` command aliases.

### Updating

If you installed OMC via npm, upgrade with the published package name:

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **Package naming note:** the repo, plugin, and commands are branded **oh-my-claudecode**, but the published npm package name remains `oh-my-claude-sisyphus`. npm installs expose both `oh-my-claudecode` and `omc`; examples prefer `omc` for brevity.

If you installed OMC via the Claude Code marketplace/plugin flow, update with:

```bash
# 1. Update the marketplace clone
/plugin marketplace update omc

# 2. Re-run setup to refresh configuration
/setup
```

If you are developing from a local checkout or git worktree, update the checkout first, then re-run setup from that worktree so the active runtime matches the code you are testing.

> **Note:** If marketplace auto-update is not enabled, you must manually run `/plugin marketplace update omc` to sync the latest version before running setup.

If you experience issues after updating, clear the old plugin cache:

```bash
/omc-doctor
```

<h1 align="center">Your Claude Just Have been Steroided.</h1>

<p align="center">
  <img src="assets/omc-character.jpg" alt="oh-my-claudecode" width="400" />
</p>

---

## Why oh-my-claudecode?

- **Zero configuration required** - Works out of the box with intelligent defaults
- **Team-first orchestration** - Team is the canonical multi-agent surface
- **Natural language interface** - No commands to memorize, just describe what you want
- **Automatic parallelization** - Complex tasks distributed across specialized agents
- **Persistent execution** - Won't give up until the job is verified complete
- **Cost optimization** - Smart model routing saves 30-50% on tokens
- **Learn from experience** - Automatically extracts and reuses problem-solving patterns
- **Real-time visibility** - HUD statusline shows what's happening under the hood

---

## Features

### Orchestration Modes

Multiple strategies for different use cases — from Team-backed orchestration to token-efficient refactoring. [Learn more →](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#execution-modes)

| Mode                        | What it is                                                                              | Use For                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Team (recommended)**      | Canonical staged pipeline (`team-plan → team-prd → team-exec → team-verify → team-fix`) | Coordinated Claude agents on a shared task list                         |
| **omc team (CLI)**          | tmux CLI workers — real `claude`/`codex`/`gemini`/`antigravity`/`grok`/`cursor-agent` processes in split-panes       | Codex/Gemini/Antigravity/Grok/Cursor CLI tasks; on-demand spawn, die when done             |
| **ccg**                     | Tri-model advisors via `/ask codex` + `/ask antigravity`, Claude synthesizes             | Mixed backend+UI work needing both Codex and Antigravity                     |
| **Autopilot**               | Autonomous execution (single lead agent)                                                | End-to-end feature work with minimal ceremony                           |
| **Ultrawork**               | Maximum parallelism (non-team)                                                          | Burst parallel fixes/refactors where Team isn't needed                  |
| **Ralph**                   | Persistent mode with verify/fix loops                                                   | Tasks that must complete fully (no silent partials)                     |
| **UltraQA**                 | QA cycling until tests/build/lint/typecheck goals pass                                  | Quality gates that need repeat diagnose/fix cycles                      |
| **Claude Code `/goal`**     | Native Claude Code cross-turn goal loop                                                 | One measurable session completion condition; not an OMC evidence ledger |
| **Artifact-only Ultragoal** | Durable goal/checkpoint/evidence artifacts without starting a loop                      | Handoffs, audits, or unavailable/conflicting loop runtimes              |
| **Pipeline**                | Sequential, staged processing                                                           | Multi-step transformations with strict ordering                         |
| **Ultrapilot (legacy)**     | Deprecated compatibility mode (autopilot pipeline alias)                                | Existing workflows and older docs                                       |

### Goal Workflow Guidance

Use only one primary loop authority in a session. Claude Code `/goal` is useful for a native cross-turn completion condition, while Ralph owns single-agent verified completion, Team owns parallel staged execution, and UltraQA owns repeated quality-gate cycling. Artifact-only Ultragoal is the safe fallback when you need durable goal artifacts and evidence without starting another loop.

For `/goal` behavior, rely on Claude Code/Anthropic sources: the [Claude Code `/goal` docs](https://code.claude.com/docs/en/goal) and [Anthropic Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md). Do **not** claim the `/goal` evaluator independently runs commands or reads files; surface test output, diffs, and review evidence in the conversation before treating a goal as proven.

### Intelligent Orchestration

- **19 specialized agents** (with tier variants) for architecture, research, design, testing, data science
- **Smart model routing** - Haiku for simple tasks, Opus for complex reasoning
- **Automatic delegation** - Right agent for the job, every time
- **[Model × Agent Compatibility Matrix](docs/agents/model-compatibility.md)** - Which model to pair with each agent, with premium/balanced/budget presets

### Developer Experience

- **Magic keywords** - `ralph`, `ulw`, `ralplan`; Team stays explicit via `/team`
- **HUD statusline** - Real-time orchestration metrics in your status bar
  - If you launch Claude Code directly with `claude --plugin-dir <path>` (bypassing the `omc` shim), export `OMC_PLUGIN_ROOT=<path>` in your shell so the HUD bundle resolves to the same checkout as the plugin loader. See the [Plugin directory flags section in REFERENCE.md](./docs/REFERENCE.md#plugin-directory-flags) for details.
- **Skill learning** - Extract reusable patterns from your sessions
- **Analytics & cost tracking** - Understand token usage across all sessions

### Contributing

Want to contribute to OMC? See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full developer guide, including how to fork, set up a local checkout, link it as your active plugin, run tests, and submit PRs.

### Custom Skills

Learn once, reuse forever. OMC extracts hard-won debugging knowledge into portable skill files that auto-inject when relevant.

|                 | Project Scope                                            | User Scope        |
| --------------- | -------------------------------------------------------- | ----------------- |
| **Path**        | `.omc/skills/`                                           | `~/.omc/skills/`  |
| **Shared with** | Team (commit the skill file to keep it across worktrees) | All your projects |
| **Priority**    | Higher (overrides user)                                  | Lower (fallback)  |

```yaml
# .omc/skills/fix-proxy-crash.md
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

**Manage skills:** `/skill list | add | remove | edit | search`
**Skillify:** `/skillify` extracts reusable patterns with strict quality gates
**Auto-inject:** Matching skills load into context automatically — no manual recall needed

Project-scoped OMC-authored skills are stored in `.omc/skills/` and are intended to be committed when you want them shared. During slash/skill execution OMC also reads Claude Code workspace skills from `.claude/skills/` and compatibility skills from `.agents/skills/`, so existing workspace-local `SKILL.md` packages remain callable without copying them into user-global skills. If you create project-local skills inside a linked git worktree and do not commit them, they disappear when that worktree is removed.

### `.omc/` state and git

OMC writes runtime state, session data, plans, logs, handoffs, research notes, and local artifacts under `.omc/` by default. The repository `.gitignore` keeps that runtime data local with one intentional exception: `.omc/skills/**` remains committable for project-scoped skills you want to share with the team. Treat everything else under `.omc/` as local operational state that may contain prompts, transcripts, or machine-specific paths.

For linked git worktrees, the default `.omc/` directory lives inside that worktree, so deleting the worktree deletes its local OMC state. Set `OMC_STATE_DIR` if you want state to survive worktree deletion, or add a `.omc-workspace` marker when several independent repos should share one parent-level state root. See [OMC state, gitignore, worktree, and workspace contract](docs/REFERENCE.md#omc-state-gitignore-worktree-and-workspace-contract).

[Full feature list →](docs/REFERENCE.md)

### Multi-repo workspaces

When several independent git repos share a parent directory, drop a `.omc-workspace` marker at the parent so all sub-repos share one `.omc/` state root:

```bash
cd /path/to/parent-dir-with-many-repos
echo '{"id":"my-workspace"}' > .omc-workspace
# Sessions inside any sub-repo now share /path/.omc/
# For parallel ultragoal runs:
cd repo-A && omc ultragoal create-goals --auto-plan-id --brief "..."
cd ../repo-B && omc ultragoal create-goals --auto-plan-id --brief "..."
```

See [Multi-repo workspaces in REFERENCE.md](docs/REFERENCE.md#multi-repo-workspaces-with-omc-workspace) for resolution order, `OMC_STATE_DIR`, and workspace identifier options.

---

## In-session shortcuts

These shortcuts run **inside a Claude Code / OMC session**, not as terminal CLI commands. For shell commands, use the `omc ...` forms shown above. Team mode is explicit: use `/team ...` in-session or `omc team ...` from your shell rather than expecting a bare `team` keyword trigger.

| In-session form            | Kind                   | Effect                                 | Example                                        |
| -------------------------- | ---------------------- | -------------------------------------- | ---------------------------------------------- |
| `/team`                    | Slash skill            | Canonical Team orchestration           | `/team 3:executor "fix all TypeScript errors"` |
| `/ccg`                     | Slash skill            | `/ask codex` + `/ask antigravity` synthesis | `/ccg review this PR`                          |
| `/autopilot` / `autopilot` | Skill / prompt trigger | Full autonomous execution              | `/autopilot "build a todo app"`                |
| `/ralph` / `ralph`         | Skill / prompt trigger | Persistence mode                       | `/ralph "refactor auth"`                       |
| `/ultrawork` / `ulw`       | Skill / prompt trigger | Maximum parallelism                    | `/ultrawork "fix all errors"`                  |
| `/ralplan` / `ralplan`     | Skill / prompt trigger | Iterative planning consensus           | `/ralplan "plan this feature"`                 |
| `/deep-interview`          | Slash skill            | Socratic requirements clarification    | `/deep-interview "vague idea"`                 |
| `deepsearch`               | Prompt trigger         | Codebase-focused search routing        | `deepsearch for auth middleware`               |
| `ultrathink`               | Prompt trigger         | Deep reasoning mode                    | `ultrathink about this architecture`           |
| `cancelomc`, `stopomc`     | Prompt trigger         | Stop active OMC modes                  | `stopomc`                                      |

**Notes:**

- **ralph includes ultrawork**: when you activate ralph mode, it automatically includes ultrawork's parallel execution.
- `swarm` compatibility alias has been removed; migrate existing prompts to `/team` syntax.
- `plan this` / `plan the` keyword triggers were removed; use `ralplan` or explicit `/oh-my-claudecode:plan`.

## Utilities

### Provider Advisor (`omc ask` / `/ask`)

Run local provider CLIs and save a markdown artifact under `.omc/artifacts/ask/`.

```bash
# Terminal CLI
omc ask claude "review this migration plan"
omc ask codex --prompt "identify architecture risks"
omc ask gemini --prompt "propose UI polish ideas"
omc ask antigravity --prompt "propose UI polish ideas"
omc ask grok --prompt "cross-check this code review"
omc ask cursor --prompt "apply this implementation plan"
omc ask claude --agent-prompt executor --prompt "draft implementation steps"

# Inside a Claude Code / OMC session
/ask claude "review this migration plan"
/ask codex "identify architecture risks"
/ask antigravity "propose UI polish ideas"
/ask cursor "apply this implementation plan"
```

Canonical env vars:

- `OMC_ASK_ADVISOR_SCRIPT`
- `OMC_ASK_ORIGINAL_TASK`

Phase-1 aliases `OMX_ASK_ADVISOR_SCRIPT` and `OMX_ASK_ORIGINAL_TASK` are accepted with deprecation warnings.

### Autoresearch (stateful skill)

`omc autoresearch` is now a **hard-deprecated shim**. The authoritative workflow is:

```bash
/deep-interview --autoresearch improve startup performance
/oh-my-claudecode:autoresearch
```

- `deep-interview --autoresearch` generates/sets up the mission and evaluator
- `autoresearch` runs the bounded, single-mission stateful loop
- each iteration records evaluation JSON plus markdown decision logs
- non-passing iterations continue
- strict stopping is controlled by an explicit max-runtime ceiling

### Rate Limit Wait

Auto-resume Claude Code sessions when rate limits reset.

```bash
omc wait          # Check status, get guidance
omc wait --start  # Enable auto-resume daemon
omc wait --stop   # Disable daemon
```

**Requires:** tmux (for session detection)

### Monitoring & Observability

Use the HUD for live observability and the current session/replay artifacts for post-session inspection:

- HUD preset: `/oh-my-claudecode:hud setup` then use a supported preset such as `"omcHud": { "preset": "focused" }`
- Session summaries: `.omc/sessions/*.json`
- Replay logs: `.omc/state/agent-replay-*.jsonl`
- Live HUD rendering: `omc hud`
- Local friction reports: `omc session friction report --since 24h` summarizes context-bloat and operator-friction signals from local session artifacts without printing raw prompts or tool output; add `--json` for automation.

### Notification Tags (Telegram/Discord/Slack)

You can configure who gets tagged when stop callbacks send session summaries.

```bash
# Set/replace tag list
omc config-stop-callback telegram --enable --token <bot_token> --chat <chat_id> --tag-list "@alice,bob"
omc config-stop-callback discord --enable --webhook <url> --tag-list "@here,123456789012345678,role:987654321098765432"
omc config-stop-callback slack --enable --webhook <url> --tag-list "<!here>,<@U1234567890>"

# Incremental updates
omc config-stop-callback telegram --add-tag charlie
omc config-stop-callback discord --remove-tag @here
omc config-stop-callback discord --clear-tags
```

Tag behavior:

- Telegram: `alice` becomes `@alice`
- Discord: supports `@here`, `@everyone`, numeric user IDs, and `role:<id>`
- Slack: supports `<@MEMBER_ID>`, `<!channel>`, `<!here>`, `<!everyone>`, `<!subteam^GROUP_ID>`
- `file` callbacks ignore tag options

### OpenClaw Integration

Forward Claude Code session events to an [OpenClaw](https://openclaw.ai/) gateway to enable automated responses and workflows via your OpenClaw agent.

**Quick setup (recommended):**

```bash
/oh-my-claudecode:configure-notifications
# → When prompted, type "openclaw" → choose "OpenClaw Gateway"
```

**Manual setup:** create `~/.claude/omc_config.openclaw.json`:

```json
{
  "enabled": true,
  "gateways": {
    "my-gateway": {
      "url": "https://your-gateway.example.com/wake",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" },
      "method": "POST",
      "timeout": 10000
    }
  },
  "hooks": {
    "session-start": {
      "gateway": "my-gateway",
      "instruction": "Session started for {{projectName}}",
      "enabled": true
    },
    "stop": {
      "gateway": "my-gateway",
      "instruction": "Session stopping for {{projectName}}",
      "enabled": true
    }
  }
}
```

**Environment variables:**

| Variable                                   | Description               |
| ------------------------------------------ | ------------------------- |
| `OMC_OPENCLAW=1`                           | Enable OpenClaw           |
| `OMC_OPENCLAW_DEBUG=1`                     | Enable debug logging      |
| `OMC_OPENCLAW_CONFIG=/path/to/config.json` | Override config file path |

**Supported hook events (6 active in bridge.ts):**

| Event               | Trigger                                 | Key template variables                                |
| ------------------- | --------------------------------------- | ----------------------------------------------------- |
| `session-start`     | Session begins                          | `{{sessionId}}`, `{{projectName}}`, `{{projectPath}}` |
| `stop`              | Claude response completes               | `{{sessionId}}`, `{{projectName}}`                    |
| `keyword-detector`  | Every prompt submission                 | `{{prompt}}`, `{{sessionId}}`                         |
| `ask-user-question` | Claude requests user input              | `{{question}}`, `{{sessionId}}`                       |
| `pre-tool-use`      | Before tool invocation (high frequency) | `{{toolName}}`, `{{sessionId}}`                       |
| `post-tool-use`     | After tool invocation (high frequency)  | `{{toolName}}`, `{{sessionId}}`                       |

**Reply channel environment variables:**

| Variable                 | Description                    |
| ------------------------ | ------------------------------ |
| `OPENCLAW_REPLY_CHANNEL` | Reply channel (e.g. `discord`) |
| `OPENCLAW_REPLY_TARGET`  | Channel ID                     |
| `OPENCLAW_REPLY_THREAD`  | Thread ID                      |

See `scripts/openclaw-gateway-demo.mjs` for a reference gateway that relays OpenClaw payloads to a custom HTTPS automation endpoint.

---

## Documentation

- **[Full Reference](docs/REFERENCE.md)** - Complete feature documentation
- **[CLI Reference](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#cli-reference)** - All `omc` commands, flags, and tools
- **[Notifications Guide](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#notifications)** - Discord, Telegram, Slack, and webhook setup
- **[Recommended Workflows](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#workflows)** - Battle-tested skill chains for common tasks
- **[Release Notes](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#release-notes)** - What's new in each version
- **[Website](https://yeachan-heo.github.io/oh-my-claudecode-website)** - Interactive guides and examples
- **[Migration Guide](docs/MIGRATION.md)** - Upgrade from v2.x
- **[Architecture](docs/ARCHITECTURE.md)** - How it works under the hood
- **[Performance Monitoring](docs/PERFORMANCE-MONITORING.md)** - Agent tracking, debugging, and optimization
- **[Model × Agent Compatibility Matrix](docs/agents/model-compatibility.md)** - Which model to pair with each agent (premium / balanced / budget presets)
- **[Security Guide](SECURITY.md)** - Enterprise deployment and hardening

---

## Requirements

- [Claude Code](https://docs.anthropic.com/claude-code) CLI
- Claude Max/Pro subscription OR Anthropic API key

### Platform & tmux

OMC features like `omc team` and rate-limit detection require **tmux**:

| Platform       | tmux provider                                         | Install                 |
| -------------- | ----------------------------------------------------- | ----------------------- |
| macOS          | [tmux](https://github.com/tmux/tmux)                  | `brew install tmux`     |
| Ubuntu/Debian  | tmux                                                  | `sudo apt install tmux` |
| Fedora         | tmux                                                  | `sudo dnf install tmux` |
| Arch           | tmux                                                  | `sudo pacman -S tmux`   |
| Windows        | [psmux](https://github.com/marlocarlo/psmux) (native) | `winget install psmux`  |
| Windows (WSL2) | tmux (inside WSL)                                     | `sudo apt install tmux` |

> **Windows users:** [psmux](https://github.com/marlocarlo/psmux) provides a native `tmux` binary for Windows with 76 tmux-compatible commands. No WSL required.

### Optional: Multi-AI Orchestration

OMC can optionally orchestrate external AI providers for cross-validation and design consistency. These are **not required** — OMC works fully without them.

| Provider                                                                | Install                                                      | What it enables                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| [Antigravity CLI](https://antigravity.google) (`agy`)                   | Install per the [official instructions](https://antigravity.google) (provides the `agy` binary) | Design review, UI consistency — Google's successor to the Gemini CLI |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)               | `npm install -g @google/gemini-cli`                          | Design review, UI consistency (1M token context) — enterprise/API-key access unaffected |
| [Codex CLI](https://github.com/openai/codex)                            | `npm install -g @openai/codex`                               | Architecture validation, code review cross-check                          |
| [Grok Build](https://build.grok.com)                                    | Download from build.grok.com (`grok` at `~/.grok/bin/grok`) | Code review, analysis cross-check                                         |

> **Migrating from Gemini CLI:** Per Google's announcement, the Gemini CLI is being superseded by the Antigravity CLI (`agy`); see the [official Antigravity docs](https://antigravity.google). Use `omc team N:antigravity` and `omc ask antigravity` wherever you previously used `gemini`. Windows headless support for `agy` is unknown/untested — report issues upstream.

**Cost:** 3 Pro plans (Claude + Antigravity/Gemini + ChatGPT) cover everything for ~$60/month.

---

## License

MIT

---

<div align="center">

**Inspired by:** [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) • [claude-hud](https://github.com/ryanjoachim/claude-hud) • [Superpowers](https://github.com/obra/superpowers) • [everything-claude-code](https://github.com/affaan-m/everything-claude-code) • [Ouroboros](https://github.com/Q00/ouroboros)

**Zero learning curve. Maximum power.**

</div>

<!-- OMC:FEATURED-CONTRIBUTORS:START -->
## Featured by OmC Contributors

Top personal non-fork, non-archived repos from all-time OMC contributors (100+ GitHub stars).

- [@Yeachan-Heo](https://github.com/Yeachan-Heo) — [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) (⭐ 37k)
- [@junhoyeo](https://github.com/junhoyeo) — [tokscale](https://github.com/junhoyeo/tokscale) (⭐ 3.9k)
- [@psmux](https://github.com/psmux) — [psmux](https://github.com/psmux/psmux) (⭐ 2.6k)
- [@BowTiedSwan](https://github.com/BowTiedSwan) — [buildflow](https://github.com/BowTiedSwan/buildflow) (⭐ 294)
- [@J-Pster](https://github.com/J-Pster) — [Psters_AI_Workflow](https://github.com/J-Pster/Psters_AI_Workflow) (⭐ 291)
- [@MeroZemory](https://github.com/MeroZemory) — [ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp) (⭐ 279)
- [@alohays](https://github.com/alohays) — [awesome-visual-representation-learning-with-transformers](https://github.com/alohays/awesome-visual-representation-learning-with-transformers) (⭐ 270)
- [@jcwleo](https://github.com/jcwleo) — [random-network-distillation-pytorch](https://github.com/jcwleo/random-network-distillation-pytorch) (⭐ 263)
- [@shaun0927](https://github.com/shaun0927) — [openchrome](https://github.com/shaun0927/openchrome) (⭐ 220)
- [@HaD0Yun](https://github.com/HaD0Yun) — [Doyunha-Gopeak](https://github.com/HaD0Yun/Doyunha-Gopeak) (⭐ 216)
- [@emgeee](https://github.com/emgeee) — [mean-tutorial](https://github.com/emgeee/mean-tutorial) (⭐ 200)
- [@devswha](https://github.com/devswha) — [patina](https://github.com/devswha/patina) (⭐ 176)
- [@anduinnn](https://github.com/anduinnn) — [HiFiNi-Auto-CheckIn](https://github.com/anduinnn/HiFiNi-Auto-CheckIn) (⭐ 171)
- [@Znuff](https://github.com/Znuff) — [consolas-powerline](https://github.com/Znuff/consolas-powerline) (⭐ 146)

<!-- OMC:FEATURED-CONTRIBUTORS:END -->

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Yeachan-Heo/oh-my-claudecode&type=date&legend=top-left)](https://www.star-history.com/#Yeachan-Heo/oh-my-claudecode&type=date&legend=top-left)

## 💖 Support This Project

If Oh-My-ClaudeCode helps your workflow, consider sponsoring:

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-❤️-red?style=for-the-badge&logo=github)](https://github.com/sponsors/Yeachan-Heo)

### Why sponsor?

- Keep development active
- Priority support for sponsors
- Influence roadmap & features
- Help maintain free & open source

### Other ways to help

- ⭐ Star the repo
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Contribute code

## GEO visibility benchmark

OmC includes a [`geobench`](https://github.com/NomaDamas/geobench) product spec for measuring LLM hit rate, MRR, share of voice, and citations.

- Spec: [`geobench/oh-my-claudecode.yaml`](geobench/oh-my-claudecode.yaml)
- Runbook: [`docs/geobench.md`](docs/geobench.md)

## Docs

### docs/ARCHITECTURE.md
# Architecture

> How oh-my-claudecode orchestrates multi-agent workflows.

## Overview

oh-my-claudecode enables Claude Code to orchestrate specialized agents through a skill-based routing system. It is built on four interlocking systems: **Hooks** detect lifecycle events, **Skills** inject behaviors, **Agents** execute specialized work, and **State** tracks progress across context resets.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         OH-MY-CLAUDECODE                                 │
│                     Intelligent Skill Activation                         │
└─────────────────────────────────────────────────────────────────────────┘

  User Input                      Skill Detection                 Execution
  ──────────                      ───────────────                 ─────────
       │                                │                              │
       ▼                                ▼                              ▼
┌─────────────┐              ┌──────────────────┐           ┌─────────────────┐
│  "ultrawork │              │   CLAUDE.md      │           │ SKILL ACTIVATED │
│   refactor  │─────────────▶│   Auto-Routing   │──────────▶│                 │
│   the API"  │              │                  │           │ ultrawork +     │
└─────────────┘              │ Task Type:       │           │ default +       │
                             │  - Implementation│           │ git-master      │
                             │  - Multi-file    │           │                 │
                             │  - Parallel OK   │           │ ┌─────────────┐ │
                             │                  │           │ │ Parallel    │ │
                             │ Skills:          │           │ │ agents      │ │
                             │  - ultrawork ✓   │           │ │ launched    │ │
                             │  - default ✓     │           │ └─────────────┘ │
                             │  - git-master ✓  │           │                 │
                             └──────────────────┘           │ ┌─────────────┐ │
                                                            │ │ Atomic      │ │
                                                            │ │ commits     │ │
                                                            │ └─────────────┘ │
                                                            └─────────────────┘
```

The four systems flow in sequence:

```
User Input --> Hooks (event detection) --> Skills (behavior injection)
           --> Agents (task execution) --> State (progress tracking)
```

---

## Agent System

### Overview

OMC provides 19 specialized agents organized into 4 lanes. Each agent is invoked as `oh-my-claudecode:<agent-name>` and runs on the appropriate model tier.

### Build/Analysis Lane

Covers the full development lifecycle from exploration to verification.

| Agent | Default Model | Role |
|-------|---------------|------|
| `explore` | haiku | Codebase discovery, file/symbol mapping |
| `analyst` | opus | Requirements analysis, hidden constraint discovery |
| `planner` | opus | Task sequencing, execution plan creation |
| `architect` | opus | System design, interface definition, trade-off analysis |
| `debugger` | sonnet | Root-cause analysis, build error resolution |
| `executor` | sonnet | Code implementation, refactoring |
| `verifier` | sonnet | Completion verification, test adequacy confirmation |
| `tracer` | sonnet | Evidence-driven causal tracing, competing hypothesis analysis |

### Review Lane

Quality gates before handoff. Catches correctness and security issues.

| Agent | Default Model | Role |
|-------|---------------|------|
| `security-reviewer` | sonnet | Security vulnerabilities, trust boundaries, authn/authz review |
| `code-reviewer` | opus | Comprehensive code review, API contracts, backward compatibility |

### Domain Lane

Domain experts called in when needed.

| Agent | Default Model | Role |
|-------|---------------|------|
| `test-engineer` | sonnet | Test strategy, coverage, flaky-test hardening |
| `designer` | sonnet | UI/UX architecture, interaction design |
| `writer` | haiku | Documentation, migration notes |
| `qa-tester` | sonnet | Interactive CLI/service runtime validation via tmux |
| `scientist` | sonnet | Data analysis, statistical research |
| `git-master` | sonnet | Git operations, commits, rebase, history management |
| `document-specialist` | sonnet | External documentation, API/SDK reference lookup |
| `code-simplifier` | opus | Code clarity, simplification, maintainability improvement |

### Coordination Lane

Challenges plans and designs made by other agents. A plan passes only when no gaps can be found.

| Agent | Default Model | Role |
|-------|---------------|------|
| `critic` | opus | Gap analysis of plans and designs, multi-angle review |

### Model Routing

OMC uses three model tiers:

| Tier | Model | Characteristics | Cost |
|------|-------|-----------------|------|
| LOW | haiku | Fast and inexpensive | Low |
| MEDIUM | sonnet | Balanced performance and cost | Medium |
| HIGH | opus | Highest-quality reasoning | High |

Default assignments by role:
- **haiku**: Fast lookups and simple tasks (`explore`, `writer`)
- **sonnet**: Code implementation, debugging, testing (`executor`, `debugger`, `test-engineer`)
- **opus**: Architecture, strategic analysis, review (`architect`, `planner`, `critic`, `code-reviewer`)

### Delegation

Work is delegated through the Task tool with intelligent model routing:

```typescript
Task(
  subagent_type="oh-my-claudecode:executor",
  model="sonnet",
  prompt="Implement feature..."
)
```

**Delegate to agents when:**
- Multiple files need to change
- Refactoring is required
- Debugging or root-cause analysis is needed
- Code review or security review is needed
- Planning or research is required

**Handle directly when:**
- Simple file lookups
- Straightforward question answering
- Single-command operations

### Agent Selection Guide

| Task Type | Recommended Agent | Model |
|-----------|-------------------|-------|
| Quick code lookup | `explore` | haiku |
| Feature implementation | `executor` | sonnet |
| Complex refactoring | `executor` (model=opus) | opus |
| Simple bug fix | `debugger` | sonnet |
| Complex debugging | `architect` | opus |
| UI component | `designer` | sonnet |
| Documentation | `writer` | haiku |
| Test strategy | `test-engineer` | sonnet |
| Security review | `security-reviewer` | sonnet |
| Code review | `code-reviewer` | opus |
| Data analysis | `scientist` | sonnet |

### Typical Agent Workflow

```
explore --> analyst --> planner --> critic --> executor --> verifier
(discover)  (analyze)   (sequence)  (review)   (implement)  (confirm)
```

### Agent Role Boundaries

| Agent | Does | Does Not |
|-------|------|----------|
| `architect` | Code analysis, debugging, verification | Requirements gathering, planning |
| `analyst` | Find requirements gaps | Code analysis, planning |
| `planner` | Create task plans | Requirements analysis, plan review |
| `critic` | Review plan quality | Requirements analysis, code analysis |

---

## Skills System

### Overview

Skills are **behavior injections** that modify how the orchestrator operates. Instead of swapping agents, skills add capabilities on top of existing agents. OMC provides 31 skills total (28 user-invocable + 3 internal/pipeline).

### Skill Layers

Skills compose in three layers:

```
┌─────────────────────────────────────────────────────────────┐
│  GUARANTEE LAYER (optional)                                  │
│  ralph: "Cannot stop until verified done"                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  ENHANCEMENT LAYER (0-N skills)                              │
│  ultrawork (parallel) | git-master (commits) | frontend-ui-ux│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  EXECUTION LAYER (primary skill)                             │
│  default (build) | orchestrate (coordinate) | planner (plan) │
└─────────────────────────────────────────────────────────────┘
```

**Formula:** `[Execution Skill] + [0-N Enhancements] + [Optional Guarantee]`

Example:
```
Task: "ultrawork: refactor API with proper commits"
Active skills: ultrawork + default + git-master
```

### How to Invoke Skills

**Slash commands:**
```bash
/oh-my-claudecode:autopilot build me a todo app
/oh-my-claudecode:ralph refactor the auth module
/oh-my-claudecode:team 3:executor "implement fullstack app"
```

**Magic keywords** — include a keyword in natural language and the skill activates automatically:
```bash
autopilot build me a todo app      # activates autopilot
ralph: refactor the auth module    # activates ralph
ultrawork implement OAuth          # activates ultrawork
```

### Core Workflow Skills

#### autopilot
Full autonomous 5-stage pipeline from idea to working code.
- Trigger: `autopilot`, `build me`, `I want a`
```bash
autopilot build me a REST API with authentication
```

#### ralph
Repeating loop that does not stop until work is verified complete. The `verifier` agent confirms completion before the loop exits.
- Trigger: `ralph`, `don't stop`, `must complete`
```bash
ralph: refactor the authentication module
```

#### ultrawork
Maximum parallelism — launches multiple agents simultaneously.
- Trigger: `ultrawork`, `ulw`
```bash
ultrawork implement user authentication with OAuth
```

#### team
Coordinates N Claude agents with a 5-stage pipeline: `plan → prd → exec → verify → fix`
```bash
/oh-my-claudecode:team 3:executor "implement fullstack todo app"
```

#### ccg (Claude-Codex-Gemini)
Fans out to Codex and Antigravity simultaneously; Claude synthesizes the results. Gemini remains available as an enterprise/API-key fallback when using the legacy Gemini CLI.
- Trigger: `ccg`, `claude-codex-gemini`
```bash
ccg: review this authentication implementation
```

#### ralplan
Iterative planning: Planner, Architect, and Critic loop until they reach consensus.
- Trigger: `ralplan`
```bash
ralplan this feature
```

### Utility Skills

| Skill | Description | Command |
|-------|-------------|---------|
| `cancel` | Cancel active execution mode | `/oh-my-claudecode:cancel` |
| `hud` | Status bar configuration | `/oh-my-claudecode:hud` |
| `omc-setup` | Initial setup wizard | `/oh-my-claudecode:omc-setup` |
| `omc-doctor` | Diagnose installation | `/oh-my-claudecode:omc-doctor` |
| `skillify` | Extract reusable skills from session | `/oh-my-claudecode:skillify` (`learner` deprecated alias) |
| `skill` | Manage local skills (list/add/remove) | `/oh-my-claudecode:skill` |
| `trace` | Evidence-driven causal tracing | `/oh-my-claudecode:trace` |
| `release` | Automated release workflow | `/oh-my-claudecode:release` |
| `deepinit` | Generate hierarchical AGENTS.md | `/oh-my-claudecode:deepinit` |
| `deep-interview` | Socratic deep interview | `/deep-interview` |
| `sciomc` | Parallel scientist agent orchestration | `/oh-my-claudecode:sciomc` |
| `external-context` | Parallel document-specialist research | `/oh-my-claudecode:external-context` |
| `ai-slop-cleaner` | Clean AI expression patterns | `/oh-my-claudecode:ai-slop-cleaner` |
| `writer-memory` | Memory system for writing projects | `/oh-my-claudecode:writer-memory` |

### Magic Keyword Reference

| Keyword | Effect |
|---------|--------|
| `ultrawork`, `ulw`, `uw` | Parallel agent orchestration |
| `autopilot`, `build me`, `I want a`, `handle it all`, `end to end`, `e2e this` | Autonomous execution pipeline |
| `ralph`, `don't stop`, `must complete`, `until done` | Loop until verified complete |
| `ccg`, `claude-codex-gemini` | 3-model orchestration (use `antigravity` workers when using the Antigravity CLI) |
| `ralplan` | Consensus-based planning |
| `deep interview`, `ouroboros` | Socratic deep interview |
| `code review`, `review code` | Comprehensive code review mode |
| `security review`, `review security` | Security-focused review mode |
| `deepsearch`, `search the codebase`, `find in codebase` | Codebase search mode |
| `deepanalyze`, `deep-analyze` | Deep analysis mode |
| `ultrathink`, `think hard`, `think deeply` | Deep reasoning mode |
| `tdd`, `test first`, `red green` | TDD workflow |
| `deslop`, `anti-slop` | AI expression cleanup |
| `cancelomc`, `stopomc` | Cancel active execution mode |

### Keyword Detection Sources

Keywords are processed in two places:

| Source | Role | Customizable |
|--------|------|--------------|
| `config.jsonc` `magicKeywords` | 4 categories (ultrawork, search, analyze, ultrathink) | Yes |
| `keyword-detector` hook | 11+ triggers (autopilot, ralph, ccg, etc.) | No |

The `autopilot`, `ralph`, and `ccg` triggers are hardcoded in the hook and cannot be changed through config.

---

## Hooks

### Overview

Hooks are code that reacts to Claude Code lifecycle events. They run automatically when a user submits a prompt, uses a tool, or starts/ends a session. OMC implements agent delegation, keyword detection, and state persistence through this hook system.

### Lifecycle Events

Claude Code provides 11 lifecycle events. OMC registers hooks on these events:

| Event | When It Fires | OMC Usage |
|-------|---------------|-----------|
| `UserPromptSubmit` | User submits a prompt | Magic keyword detection, skill injection |
| `SessionStart` | Session begins | Initial setup, project memory load |
| `PreToolUse` | Before a tool is used | Permission validation, parallel execution hints |
| `PermissionRequest` | Permission requested | Bash command permission handling |
| `PostToolUse` | After a tool is used | Result validation, project memory update |
| `PostToolUseFailure` | After a tool fails | Error recovery handling |
| `SubagentStart` | Subagent starts | Agent tracking |
| `SubagentStop` | Subagent stops | Agent tracking, output verification |
| `PreCompact` | Before context compaction | Preserve critical information, save project memory |
| `Stop` | Claude is about to stop | Persistent mode enforcement, code simplification |
| `SessionEnd` | Session ends | Session data cleanup |

### system-reminder Injection

Hooks inject additional context to Claude via `<system-reminder>` tags:

```xml
<system-reminder>
hook success: Success
</system-reminder>
```

Injected pattern meanings:

| Pattern | Meaning |
|---------|---------|
| `hook success: Success` | Hook ran normally, continue as planned |
| `hook additional context: ...` | Additional context information, take note |
| `[MAGIC KEYWORD: ...]` | Magic keyword detected, execute indicated skill |
| `The boulder never stops` | ralph/ultrawork mode is active |

### Key Hooks

**keyword-detector** — fires on `UserPromptSubmit`. Detects magic keywords in user input and activates the corresponding skill.

**persistent-mode** — fires on `Stop`. When a persistent mode (ralph, ultrawork) is active, prevents Claude from stopping until work is verified complete.

**pre-compact** — fires on `PreCompact`. Saves critical information to the notepad before the context window is compressed.

**subagent-tracker** — fires on `SubagentStart` and `SubagentStop`. Tracks currently running agents; validates output on stop.

**context-guard-stop** — fires on `Stop`. Monitors context usage and warns when approaching the limit.

**code-simplifier** — fires on `Stop`. Disabled by default. When enabled, automatically simplifies modified files when Claude stops.

Enable via config:
```json
{
  "codeSimplifier": {
    "enabled": true,
    "extensions": [".ts", ".tsx", ".js", ".jsx", ".py", ".go", ".rs"],
    "maxFiles": 10
  }
}
```

### Hook Registration Structure

OMC hooks are declared in `hooks.json`. Each hook is a Node.js script with a timeout:

```json
{
  "UserPromptSubmit": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "node scripts/keyword-detector.mjs",
          "timeout": 5
        }
      ]
    }
  ]
}
```

- `matcher`: Pattern the hook responds to (`*` matches all input)
- `timeout`: Timeout in seconds
- `type`: Always `"command"` (runs an external command)

### Disabling Hooks

Disable all hooks:
```bash
export DISABLE_OMC=1
```

Skip specific hooks (comma-separated):
```bash
export OMC_SKIP_HOOKS="keyword-detector,persistent-mode"
```

---

## State Management

### Overview

OMC stores task progress and project knowledge in the `.omc/` directory. The state system preserves critical information even when context compaction resets the context window.

### Directory Structure

```
.omc/
├── state/                    # Per-mode state files
│   ├── autopilot-state.json  # autopilot progress
│   ├── ralph-state.json      # ralph loop state
│   ├── team/                 # team task state
│   ├── interop/              # cross-tool task/message envelopes
│   └── sessions/             # per-session state
│       └── {sessionId}/
├── notepad.md                # Compaction-resistant memo pad
├── project-memory.json       # Project knowledge store
├── plans/                    # Execution plans
├── notepads/                 # Per-plan knowledge capture
│   └── {plan-name}/
│       ├── learnings.md
│       ├── decisions.md
│       ├── issues.md
│       └── problems.md
├── prompts/                  # persisted prompt/response artifacts
├── autopilot/                # autopilot artifacts
│   └── spec.md
├── research/                 # Research results
└── logs/                     # Execution logs
```

### Control Plane vs Data Plane

OMC keeps orchestration metadata separate from large durable artifacts:

- **Control plane**: queue state, worker assignment, session state, and cross-tool task/message envelopes under `.omc/state/**`.
- **Data plane**: plans, specs, prompts, results, traces, and other durable artifacts under paths such as `.omc/plans/`, `.omc/notepads/`, `.omc/prompts/`, and `.omc/state/interop/artifacts/**`.
- **Concrete handoff examples**:
  - shared interop state keeps task/message metadata inline while storing oversized task descriptions, task results, and message bodies under `.omc/state/interop/artifacts/**`
  - prompt persistence stores durable prompt/response files under `.omc/prompts/**` and records descriptor metadata alongside job status

**Global State:**
- `~/.omc/state/{name}.json` — user preferences and global config

Legacy locations are auto-migrated on read.

This separation keeps schedulers and status checks small while allowing richer artifacts to remain durable and inspectable.

### Artifact Descriptors and Bounded Handoffs

When a handoff needs to reference a large artifact, prefer a descriptor/handle over pasting the full payload inline. The canonical descriptor shape is:

| Field | Purpose |
|------|---------|
| `kind` | Artifact category (plan, prompt, result, trace, etc.) |
| `path` | Durable path to the artifact |
| `contentHash?` | Optional integrity/checksum hint when available |
| `createdAt` | Creation timestamp |
| `producer` | Owning tool, skill, or worker |
| `sizeBytes?` | Optional payload size for threshold decisions |
| `retention` | Lifecycle hint for cleanup/ownership |
| `expiresAt?` | Optional expiry for short-lived artifacts |

**Bounded handoff rule:**

1. Keep small payloads inline when the call site's explicit threshold allows it.
2. Switch to a descriptor + short human-readable summary when the payload would bloat control-plane state.
3. Preserve ownership/retention metadata with the descriptor so later cleanup and audits remain deterministic.

### Notepad

**File:** `.omc/notepad.md`

The notepad survives context compaction. Content written to it persists even after the context window is reset.

Notes can be saved using the `notepad_write_manual` MCP tool or the `notepad_write_priority` tool for persistent notes.

**MCP Tools:**

| Tool | Description |
|------|-------------|
| `notepad_read` | Read notepad contents |
| `notepad_write_priority` | Write high-priority memo (permanent retention) |
| `notepad_write_working` | Write working memo |
| `notepad_write_manual` | Write manual memo |
| `notepad_prune` | Clean up old memos |
| `notepad_stats` | View notepad statistics |

**How it works:**
1. On `PreCompact` event, important information is saved to the notepad
2. After compaction, notepad contents are re-injected into context
3. Agents use the notepad to recover previous context

### Project Memory

**File:** `.omc/project-memory.json`

Project memory is a persistent store for project-level knowledge. It survives across sessions.

**MCP Tools:**

| Tool | Description |
|------|-------------|
| `project_memory_read` | Read project memory |
| `project_memory_write` | Overwrite entire project memory |
| `project_memory_add_note` | Add a note |
| `project_memory_add_directive` | Add a directive |

**Lifecycle integration:**
- `SessionStart`: Load project memory and inject into context
- `PostToolUse`: Extract project knowledge from tool results and save
- `PreCompact`: Save project memory before context compaction

### Session Scope

**Path:** `.omc/state/sessions/{sessionId}/`

Stores state isolated per session. Multiple sessions on the same project run simultaneously without state conflicts.

### Plan Notepad (Per-Plan Knowledge Capture)

**Path:** `.omc/notepads/{plan-name}/`

Stores learnings from each execution plan separately.

| File | Contents |
|------|----------|
| `learnings.md` | Discovered patterns, successful approaches |
| `decisions.md` | Architecture decisions and rationale |
| `issues.md` | Problems and blockers |
| `problems.md` | Technical debt and cautions |

All entries are timestamped automatically.

### Centralized State (Optional)

By default, state is stored in the project's `.omc/` directory and is deleted when the worktree is removed.

To preserve state across worktree deletions, set the `OMC_STATE_DIR` environment variable:

```bash
# Add to ~/.bashrc or ~/.zshrc
export OMC_STATE_DIR="$HOME/.claude/omc"
```

State is then stored at `~/.claude/omc/{project-identifier}/`. The project identifier is a hash of the Git remote URL, so the same repository shares state across different worktrees.

### Persistent Memory Tags

For critical information, use `<remember>` tags:

```xml
<!-- Retained for 7 days -->
<remember>API endpoint changed to /v2</remember>

<!-- Retained permanently -->
<remember priority>Never access production DB directly</remember>
```

| Tag | Retention |
|-----|-----------|
| `<remember>` | 7 days |
| `<remember priority>` | Permanent |

---

## Verification Protocol

The verification module ensures work completion with evidence:

**Standard Checks:**
- BUILD: Compilation passes
- TEST: All tests pass
- LINT: No linting errors
- FUNCTIONALITY: Feature works as expected
- ARCHITECT: Opus-tier review approval
- TODO: All tasks completed
- ERROR_FREE: No unresolved errors

Evidence must be fresh (within 5 minutes) and include actual command output.

---

## For More Details

- **Complete Reference**: See [REFERENCE.md](./REFERENCE.md)
- **Internal API**: See [FEATURES.md](./FEATURES.md)
- **User Guide**: See [README.md](../README.md)
- **Skills Reference**: See CLAUDE.md in your project

### docs/GETTING-STARTED.md
# Getting Started

> Quick start guide: from installation to your first OMC session.

If you're new to Oh My ClaudeCode (OMC), follow the steps below in order.

1. [Installation](#installation) - Install the OMC plugin and run initial setup
2. [First Session](#first-session) - Run your first task with autopilot
3. [Configuration](#configuration) - Customize settings and agent models per project

### What this guide covers

- How to install the OMC plugin
- Running your first autopilot session and understanding the flow
- Configuring per-user and per-project settings

### Prerequisites

- [Claude Code](https://docs.anthropic.com/claude-code) must be installed
- Claude Max/Pro subscription or an Anthropic API key is required

---

## Installation

OMC ships two surfaces and they are designed to coexist:

| Surface | What you get | Recommended install |
|---|---|---|
| **Claude Code plugin** (`oh-my-claudecode@omc`) | In-session skills, agents, hooks, statusline, MCP servers — the `/autopilot`, `/ralph`, `/ultrawork`, `/team` slash commands | Marketplace plugin install (Step 1–2 below) |
| **Terminal CLI** (`omc` binary, package `oh-my-claude-sisyphus`) | Shell commands: `omc setup`, `omc update`, `omc team`, `omc ask`, and a hard-deprecated `omc autoresearch` shim | `npm i -g oh-my-claude-sisyphus@latest` |

Most users want **both**: the plugin for the in-session experience, and the npm CLI for shell-side automation and updates. Running them in parallel is fully supported — `omc update` and `omc setup` are idempotent and detect the plugin install to avoid duplicating in-session skills (#2252).

> Older versions of this doc said OMC was "plugin-only". That was incorrect: the `omc` CLI is the canonical entry point for `omc setup`/`omc update` and is published on npm as `oh-my-claude-sisyphus`. See the [Quick Start in README.md](../README.md#quick-start) for the same two-path layout.

### Step 1: Add the marketplace source

Run the following command inside Claude Code:

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

### Step 2: Install the plugin

After adding the marketplace, install the plugin:

```bash
/plugin install oh-my-claudecode
```

### Step 2b (optional but recommended): install the terminal CLI

If you want `omc setup`, `omc update`, `omc team`, `omc ask`, etc. on your shell:

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **Known npm warning:** npm may print `deprecated prebuild-install@7.1.3` during this CLI install.
> The warning currently comes from the upstream `better-sqlite3` native-addon dependency
> (`better-sqlite3 -> prebuild-install`); `prebuild-install@7.1.3` is still the latest
> published version, so there is no safe repo-side dependency bump or override to remove it
> yet. The warning is tracked in [#2913](https://github.com/Yeachan-Heo/oh-my-claudecode/issues/2913)
> and does not by itself mean the OMC CLI install failed.

Both can be installed at the same time. The CLI auto-detects the plugin install and will not double-register skills under `~/.claude/skills/` (if you previously hit the duplicate-skill bug, run `omc update` once on 4.11.2+ — it self-heals leftover standalone skills that the plugin now provides via `prunePluginDuplicateSkills`).

### Step 3: Run initial setup

After installation, enter one of the following in Claude Code:

```bash
# Option 1: natural language
setup omc

# Option 2: skill command
/oh-my-claudecode:omc-setup
```

### Prerequisites summary

| Item | Requirement |
|------|-------------|
| Claude Code | Must be installed |
| Authentication | Claude Max/Pro subscription or `ANTHROPIC_API_KEY` environment variable |

### Choosing a setup scope

#### Project-scoped setup (recommended)

Applies OMC only to the current project:

```bash
/oh-my-claudecode:omc-setup --local
```

- Settings are saved to `./.claude/CLAUDE.md`
- No effect on other projects
- Existing global `CLAUDE.md` is preserved

#### Global setup

Applies OMC to all Claude Code sessions:

```bash
/oh-my-claudecode:omc-setup
```

- Settings are saved to `~/.claude/CLAUDE.md`
- Applied across all projects

> ⚠️ **Warning:** Global setup now asks explicitly before changing your base `~/.claude/CLAUDE.md`. The default choice is still overwrite. If you choose preserve mode instead, plain `claude` stays on your base config and `omc` force-loads the OMC companion config.

### Verifying the installation

To confirm everything is working, run the diagnostics tool:

```bash
/oh-my-claudecode:omc-doctor
```

This checks the following:

- Dependency installation status
- Configuration file errors
- Hook installation status
- Agent availability
- Skill registration status

### Running from a local checkout

If you're developing OMC or want to test unreleased features from a specific branch, you can launch Claude Code with your local checkout as the plugin:

```bash
omc --plugin-dir /path/to/oh-my-claudecode setup --plugin-dir-mode
```

This loads agents, skills, and commands directly from your checkout without copying them to `~/.claude/`. For detailed instructions and alternative flows, see [LOCAL_PLUGIN_INSTALL.md](./LOCAL_PLUGIN_INSTALL.md). For a complete decision matrix of plugin-dir flags and modes, see the [Plugin directory flags section in REFERENCE.md](./REFERENCE.md#plugin-directory-flags).

### Platform support

| Platform | Installation | Hook type |
|----------|--------------|-----------|
| macOS | Claude Code Plugin | Bash (.sh) |
| Linux | Claude Code Plugin | Bash (.sh) |
| Windows | WSL2 recommended | Node.js (.mjs) |

> ℹ️ **Note:** Native Windows support is experimental. For tmux-backed Team workers, OMC checks for a tmux-compatible binary first; native [psmux](https://github.com/psmux/psmux) is supported for PowerShell 7+ users who want visible Claude Code teammate panes in interactive team workflows. WSL2 remains the fallback when no compatible tmux is available or native Windows behavior is insufficient. psmux does not force worktree agents, non-interactive/print-mode agents, or model-selected in-process agents into visible panes.

### Updates

OMC automatically checks for updates every 24 hours. To update manually, re-run the plugin install command.

> ⚠️ **Warning:** After a plugin update, run `/oh-my-claudecode:omc-setup` again to apply the latest configuration.

### Uninstalling

```bash
/plugin uninstall oh-my-claudecode@oh-my-claudecode
```

---

## First Session

Once OMC is installed, run your first task immediately. Open Claude Code and type:

```bash
autopilot build me a hello world app
```

That single line is enough for OMC to run the full development pipeline automatically.

### What happens

When OMC detects the `autopilot` magic keyword, it starts a 5-stage pipeline:

### Stage 1: Expansion

The `analyst` and `architect` agents analyze the idea, clarify requirements, and produce a technical specification.

### Stage 2: Planning

The `planner` agent creates an execution plan. The `critic` agent reviews the plan and identifies gaps.

### Stage 3: Execution

The `executor` agent writes the code. Multiple agents work in parallel when needed.

### Stage 4: QA

Verifies that the build succeeds and tests pass. Automatically fixes failures and re-verifies.

### Stage 5: Validation

Specialist agents perform a final review of functionality, security, and code quality. Work is complete once all pass.

### HUD status display

While work is in progress, you can monitor the current state in the Claude Code status bar (HUD):

```
[OMC] autopilot:execution | agents:3 | todos:2/5 | ctx:45%
```

| Field | Meaning |
|-------|---------|
| `autopilot:execution` | Current stage within the autopilot pipeline |
| `agents:3` | Number of currently active agents |
| `todos:2/5` | Completed tasks / total tasks |
| `ctx:45%` | Context window usage percentage |

To configure the HUD display, run:

```bash
/oh-my-claudecode:hud setup
```

### Starting smaller

If autopilot feels too large, start with a single-task command:

```bash
# Code analysis
analyze why this test is failing

# File search
deepsearch for files that handle authentication

# Simple implementation
ultrawork add a health check endpoint
```

These keywords invoke a single appropriate agent directly, without running the full pipeline.

### Next steps

- [Configuration](#configuration) - Adjust agent models and features for your project
- [Architecture](./ARCHITECTURE.md) - Understand the relationship between agents, skills, and hooks

---

## Configuration

OMC supports two levels of configuration files.

| Scope | File path | Purpose |
|-------|-----------|---------|
| User (global) | `~/.config/claude-omc/config.jsonc` | Applied to all projects |
| Project | `.claude/omc.jsonc` | Applied to current project only |

> ⚠️ **Warning:** The configuration file format is JSONC (JSON with comments support). It is not a TypeScript config file (`omc.config.ts`).

### Configuration priority

When settings exist from multiple sources, they are merged in the following order (lower entries take precedence):

```
Defaults → User config (~/.config/claude-omc/config.jsonc)
         → Project config (.claude/omc.jsonc)
         → Environment variables
```

### Basic configuration structure

```jsonc
{
  // Per-agent model assignments
  "agents": {
    "explore": { "model": "haiku" },
    "executor": { "model": "sonnet" },
    "architect": { "model": "opus" }
  },

  // Feature toggles
  "features": {
    "parallelExecution": true,
    "lspTools": true,
    "astTools": true
  },

  // Magic keyword customization
  "magicKeywords": {
    "ultrawork": ["ultrawork", "ulw", "uw"],
    "search": ["search", "find", "locate"],
    "analyze": ["analyze", "investigate", "examine"],
    "ultrathink": ["ultrathink", "think", "reason"]
  },

  // Optional prompt-level company context contract
  "companyContext": {
    "tool": "mcp__vendor__get_company_context",
    "onError": "warn"
  }
}
```

### Company context via MCP

If your organization exposes internal guidance through a custom MCP server, configure the selected tool in OMC's standard config files:

```jsonc
{
  "companyContext": {
    "tool": "mcp__vendor__get_company_context",
    "onError": "warn"
  }
}
```

- Register the MCP server itself through the normal Claude/OMC MCP setup flow.
- `tool` is the full MCP tool name.
- `onError` controls prompt-level fallback: `warn` (default), `silent`, or `fail`.

This is an advisory workflow contract, not runtime enforcement. See [company-context-interface.md](./company-context-interface.md) for the full contract.

### Overriding agent models

You can change the AI model used by each agent:

```jsonc
{
  "agents": {
    // Upgrade explore agent to a stronger model
    "explore": { "model": "sonnet" },

    // Upgrade executor to opus for complex projects
    "executor": { "model": "opus" },

    // Cost saving: use haiku for documentation writing
    "writer": { "model": "haiku" }
  }
}
```

#### Default model mapping

| Agent | Default model | Role |
|-------|--------------|------|
| `explore` | haiku | Codebase discovery |
| `writer` | haiku | Documentation writing |
| `executor` | sonnet | Code implementation |
| `debugger` | sonnet | Debugging |
| `designer` | sonnet | UI/UX design |
| `verifier` | sonnet | Verification |
| `tracer` | sonnet | Evidence-driven causal tracing |
| `security-reviewer` | sonnet | Security vulnerabilities and trust boundaries |
| `test-engineer` | sonnet | Test strategy and coverage |
| `qa-tester` | sonnet | Interactive CLI/service runtime validation |
| `scientist` | sonnet | Data and statistical analysis |
| `git-master` | sonnet | Git operations and history management |
| `document-specialist` | sonnet | External documentation and API reference lookup |
| `architect` | opus | System design |
| `planner` | opus | Strategic planning |
| `critic` | opus | Plan review |
| `analyst` | opus | Requirements analysis |
| `code-reviewer` | opus | Comprehensive code review |
| `code-simplifier` | opus | Code clarity and simplification |

### Customizing magic keywords

You can change keywords in four categories via the `magicKeywords` section of `config.jsonc`:

```jsonc
{
  "magicKeywords": {
    // Triggers parallel execution mode
    "ultrawork": ["ultrawork", "ulw", "parallel"],

    // Triggers codebase search mode
    "search": ["search", "find", "locate", "grep"],

    // Triggers analysis mode
    "analyze": ["analyze", "debug", "investigate"],

    // Triggers deep reasoning mode
    "ultrathink": ["ultrathink", "think", "reason"]
  }
}
```

> ℹ️ **Note:** The `magicKeywords` section in `config.jsonc` only allows customizing four categories: `ultrawork`, `search`, `analyze`, and `ultrathink`. Keywords such as `autopilot`, `ralph`, and `ccg` are hardcoded in the keyword-detector hook and cannot be changed via config files.

### Model routing configuration

OMC automatically selects a model tier based on task complexity:

```jsonc
{
  "routing": {
    "enabled": true,
    "defaultTier": "MEDIUM",
    // Force all agents to inherit the parent model
    // (auto-activated when using CC Switch, Bedrock, or Vertex AI)
    "forceInherit": false
  }
}
```

| Tier | Model | Use case |
|------|-------|----------|
| LOW | haiku | Quick lookups, simple tasks |
| MEDIUM | sonnet | Standard implementation, general tasks |
| HIGH | opus | Architecture, deep analysis |

### CLAUDE.md configuration

OMC's default behavior is also configured via `CLAUDE.md` files. Running `/oh-my-claudecode:omc-setup` generates this file automatically.

| Scope | File | Description |
|-------|------|-------------|
| Global | `~/.claude/CLAUDE.md` | Shared settings across all projects |
| Project | `.claude/CLAUDE.md` | Per-project context and overrides |

### When to re-run setup

- After initial installation
- After an OMC update (to apply the latest configuration)
- When switching to a different machine
- When starting a new project (use the `--local` option)

### docs/FEATURES.md
# Developer API Reference

> Internal API documentation for oh-my-claudecode developers and contributors.

## Table of Contents
1. [Notepad Wisdom System](#notepad-wisdom-system)
2. [Delegation Categories](#delegation-categories)
3. [Directory Diagnostics](#directory-diagnostics)
4. [Dynamic Prompt Generation](#dynamic-prompt-generation)
5. [Agent Templates](#agent-templates)
6. [Session Resume](#session-resume)
7. [Autopilot](#autopilot)

---

## Notepad Wisdom System

Plan-scoped knowledge capture for agents executing tasks. Each plan gets its own notepad directory at `.omc/notepads/{plan-name}/` with four markdown files:

- **learnings.md**: Patterns, conventions, successful approaches
- **decisions.md**: Architectural choices and rationales
- **issues.md**: Problems and blockers
- **problems.md**: Technical debt and gotchas

All entries are timestamped automatically.

### Core Functions

```typescript
// Initialize notepad directory
initPlanNotepad(planName: string, directory?: string): boolean

// Add entries
addLearning(planName: string, content: string, directory?: string): boolean
addDecision(planName: string, content: string, directory?: string): boolean
addIssue(planName: string, content: string, directory?: string): boolean
addProblem(planName: string, content: string, directory?: string): boolean

// Read wisdom
readPlanWisdom(planName: string, directory?: string): PlanWisdom
getWisdomSummary(planName: string, directory?: string): string
```

### Types

```typescript
export interface WisdomEntry {
  timestamp: string;  // ISO 8601: "YYYY-MM-DD HH:MM:SS"
  content: string;
}

export type WisdomCategory = 'learnings' | 'decisions' | 'issues' | 'problems';

export interface PlanWisdom {
  planName: string;
  learnings: WisdomEntry[];
  decisions: WisdomEntry[];
  issues: WisdomEntry[];
  problems: WisdomEntry[];
}
```

### Usage Example

```typescript
import { initPlanNotepad, addLearning, readPlanWisdom } from '@/features/notepad-wisdom';

// Initialize and record
initPlanNotepad('api-v2-migration');
addLearning('api-v2-migration', 'API routes use Express Router pattern in src/routes/');

// Read back
const wisdom = readPlanWisdom('api-v2-migration');
console.log(wisdom.learnings[0].content);
```

---

## Delegation Categories

Semantic task classification that automatically determines model tier, temperature, and thinking budget.

### Available Categories

| Category | Tier | Temp | Thinking | Use For |
|----------|------|------|----------|---------|
| `visual-engineering` | HIGH | 0.7 | high | UI/UX, frontend, design systems |
| `ultrabrain` | HIGH | 0.3 | max | Complex reasoning, architecture, debugging |
| `artistry` | MEDIUM | 0.9 | medium | Creative solutions, brainstorming |
| `quick` | LOW | 0.1 | low | Simple lookups, basic operations |
| `writing` | MEDIUM | 0.5 | medium | Documentation, technical writing |
| `unspecified-low` | LOW | 0.1 | low | Default for simple tasks |
| `unspecified-high` | HIGH | 0.5 | high | Default for complex tasks |

### Core Functions

```typescript
// Resolve category configuration
resolveCategory(category: DelegationCategory): ResolvedCategory

// Auto-detect from prompt
detectCategoryFromPrompt(taskPrompt: string): DelegationCategory | null

// Get category with context
getCategoryForTask(context: CategoryContext): ResolvedCategory

// Enhance prompt with category guidance
enhancePromptWithCategory(taskPrompt: string, category: DelegationCategory): string

// Individual accessors
getCategoryTier(category: DelegationCategory): ComplexityTier
getCategoryTemperature(category: DelegationCategory): number
getCategoryThinkingBudget(category: DelegationCategory): ThinkingBudget
getCategoryThinkingBudgetTokens(category: DelegationCategory): number
getCategoryPromptAppend(category: DelegationCategory): string
```

### Types

```typescript
export type DelegationCategory =
  | 'visual-engineering'
  | 'ultrabrain'
  | 'artistry'
  | 'quick'
  | 'writing'
  | 'unspecified-low'
  | 'unspecified-high';

export type ThinkingBudget = 'low' | 'medium' | 'high' | 'max';

export interface ResolvedCategory {
  category: DelegationCategory;
  tier: ComplexityTier;
  temperature: number;
  thinkingBudget: ThinkingBudget;
  description: string;
  promptAppend?: string;
}

export interface CategoryContext {
  taskPrompt: string;
  agentType?: string;
  explicitCategory?: DelegationCategory;
  explicitTier?: ComplexityTier;
}
```

### Usage Example

```typescript
import { getCategoryForTask, enhancePromptWithCategory } from '@/features/delegation-categories';

const userRequest = 'Debug the race condition in payment processor';

const resolved = getCategoryForTask({ taskPrompt: userRequest });
// resolved.category === 'ultrabrain'
// resolved.temperature === 0.3

const enhancedPrompt = enhancePromptWithCategory(userRequest, resolved.category);
// Adds: "Think deeply and systematically. Consider all edge cases..."
```

---

## Directory Diagnostics

Project-level TypeScript/JavaScript QA enforcement using dual-strategy approach.

### Strategies

- **`tsc`**: Fast TypeScript compilation check via `tsc --noEmit`
- **`lsp`**: File-by-file Language Server Protocol diagnostics
- **`auto`**: Auto-selects best strategy (default, prefers tsc when available)

### API

```typescript
runDirectoryDiagnostics(directory: string, strategy?: DiagnosticsStrategy): Promise<DirectoryDiagnosticResult>
```

### Types

```typescript
export type DiagnosticsStrategy = 'tsc' | 'lsp' | 'auto';

export interface DirectoryDiagnosticResult {
  strategy: 'tsc' | 'lsp';
  success: boolean;
  errorCount: number;
  warningCount: number;
  diagnostics: string;
  summary: string;
}
```

### Usage Example

```typescript
import { runDirectoryDiagnostics } from '@/tools/diagnostics';

const result = await runDirectoryDiagnostics(process.cwd());

if (!result.success) {
  console.error(`Found ${result.errorCount} errors:`);
  console.error(result.diagnostics);
  process.exit(1);
}

console.log('Build quality check passed!');
```

---

## Dynamic Prompt Generation

Generate orchestrator prompts dynamically from agent metadata. Adding a new agent to `definitions.ts` automatically includes it in generated prompts.

### Core Functions

```typescript
// Generate full orchestrator prompt
generateOrchestratorPrompt(agents: AgentConfig[], options?: GeneratorOptions): string

// Convert definitions to configs
convertDefinitionsToConfigs(definitions: Record<string, {...}>): AgentConfig[]

// Individual section builders
buildHeader(): string
buildAgentRegistry(agents: AgentConfig[]): string
buildTriggerTable(agents: AgentConfig[]): string
buildToolSelectionSection(agents: AgentConfig[]): string
buildDelegationMatrix(agents: AgentConfig[]): string
buildOrchestrationPrinciples(): string
buildWorkflow(): string
buildCriticalRules(): string
buildCompletionChecklist(): string
```

### Types

```typescript
export interface GeneratorOptions {
  includeAgents?: boolean;
  includeTriggers?: boolean;
  includeTools?: boolean;
  includeDelegationTable?: boolean;
  includePrinciples?: boolean;
  includeWorkflow?: boolean;
  includeRules?: boolean;
  includeChecklist?: boolean;
}
```

### Usage Example

```typescript
import { getAgentDefinitions } from '@/agents/definitions';
import { generateOrchestratorPrompt, convertDefinitionsToConfigs } from '@/agents/prompt-generator';

const definitions = getAgentDefinitions();
const agents = convertDefinitionsToConfigs(definitions);
const prompt = generateOrchestratorPrompt(agents);
```

---

## Agent Templates

Standardized prompt structures for common task types.

### Exploration Template

For exploration, research, or search tasks.

**Sections:**
- **TASK**: What needs to be explored
- **EXPECTED OUTCOME**: What the orchestrator expects back
- **CONTEXT**: Background information
- **MUST DO**: Required actions
- **MUST NOT DO**: Constraints
- **REQUIRED SKILLS**: Skills needed
- **REQUIRED TOOLS**: Tools to use

**Location:** `src/agents/templates/exploration-template.md`

### Implementation Template

For code implementation, refactoring, or modification tasks.

**Sections:**
- **TASK**: Implementation goal
- **EXPECTED OUTCOME**: Deliverable
- **CONTEXT**: Project background
- **MUST DO**: Required actions
- **MUST NOT DO**: Constraints
- **REQUIRED SKILLS**: Skills needed
- **REQUIRED TOOLS**: Tools to use
- **VERIFICATION CHECKLIST**: Pre-completion checks

**Location:** `src/agents/templates/implementation-template.md`

---

## Session Resume

Wrapper for resuming background agent sessions with full context.

### API

```typescript
resumeSession(input: ResumeSessionInput): ResumeSessionOutput
```

### Types

```typescript
export interface ResumeSessionInput {
  sessionId: string;
}

export interface ResumeSessionOutput {
  success: boolean;
  context?: {
    previousPrompt: string;
    toolCallCount: number;
    lastToolUsed?: string;
    lastOutputSummary?: string;
    continuationPrompt: string;
  };
  error?: string;
}
```

### Usage Example

```typescript
import { resumeSession } from '@/tools/resume-session';

const result = resumeSession({ sessionId: 'ses_abc123' });

if (result.success && result.context) {
  console.log(`Resuming session with ${result.context.toolCallCount} prior tool calls`);

  // Continue with Task delegation
  Task({
    subagent_type: "oh-my-claudecode:executor",
    model: "sonnet",
    prompt: result.context.continuationPrompt
  });
}
```

---

## Autopilot

Autonomous execution from idea to validated working code through a 5-phase development lifecycle.

### 5-Phase Workflow

1. **Expansion** - Analyst + Architect expand idea into requirements and technical spec
2. **Planning** - Architect creates execution plan (validated by Critic)
3. **Execution** - Ralph + Ultrawork implement plan with parallel tasks
4. **QA** - UltraQA ensures build/lint/tests pass through fix cycles
5. **Validation** - Specialized architects perform functional, security, and quality reviews

### Core Types

```typescript
export type AutopilotPhase =
  | 'expansion'
  | 'planning'
  | 'execution'
  | 'qa'
  | 'validation'
  | 'complete'
  | 'failed';

export interface AutopilotState {
  active: boolean;
  phase: AutopilotPhase;
  iteration: number;
  max_iterations: number;
  originalIdea: string;

  expansion: AutopilotExpansion;
  planning: AutopilotPlanning;
  execution: AutopilotExecution;
  qa: AutopilotQA;
  validation: AutopilotValidation;

  started_at: string;
  completed_at: string | null;
  phase_durations: Record<string, number>;
  total_agents_spawned: number;
  wisdom_entries: number;
  session_id?: string;
}

export interface AutopilotConfig {
  maxIterations?: number;              // default: 10
  maxExpansionIterations?: number;     // default: 2
  maxArchitectIterations?: number;     // default: 5
  maxQaCycles?: number;                // default: 5
  maxValidationRounds?: number;        // default: 3
  parallelExecutors?: number;          // default: 5
  pauseAfterExpansion?: boolean;       // default: false
  pauseAfterPlanning?: boolean;        // default: false
  skipQa?: boolean;                    // default: false
  skipValidation?: boolean;            // default: false
  autoCommit?: boolean;                // default: false
  validationArchitects?: ValidationVerdictType[];
}
```

### State Management

```typescript
// Initialize session
initAutopilot(directory: string, idea: string, sessionId?: string, config?: Partial<AutopilotConfig>): AutopilotState

// Read/write state
readAutopilotState(directory: string): AutopilotState | null
writeAutopilotState(directory: string, state: AutopilotState): boolean
clearAutopilotState(directory: string): boolean

// Check status
isAutopilotActive(directory: string): boolean

// Phase transitions
transitionPhase(directory: string, newPhase: AutopilotPhase): AutopilotState | null
transitionRalphToUltraQA(directory: string, sessionId: string): TransitionResult
transitionUltraQAToValidation(directory: string): TransitionResult
transitionToComplete(directory: string): TransitionResult
transitionToFailed(directory: string, error: string): TransitionResult

// Update phase data
updateExpansion(directory: string, updates: Partial<AutopilotExpansion>): boolean
updatePlanning(directory: string, updates: Partial<AutopilotPlanning>): boolean
updateExecution(directory: string, updates: Partial<AutopilotExecution>): boolean
updateQA(directory: string, updates: Partial<AutopilotQA>): boolean
updateValidation(directory: string, updates: Partial<AutopilotValidation>): boolean

// Metrics
incrementAgentCount(directory: string, count?: number): boolean

// Paths
getSpecPath(directory: string): string  // .omc/autopilot/spec.md
getPlanPath(directory: string): string  // .omc/plans/autopilot-impl.md
```

### Prompt Generation

```typescript
// Phase-specific prompts
getExpansionPrompt(idea: string): string
getDirectPlanningPrompt(specPath: string): string
getExecutionPrompt(planPath: string): string
getQAPrompt(): string
getValidationPrompt(specPath: string): string

// Generic phase prompt
getPhasePrompt(phase: string, context: object): string

// Transition prompts
getTransitionPrompt(fromPhase: string, toPhase: string): string
```

### Validation Coordination

```typescript
export type ValidationVerdictType = 'functional' | 'security' | 'quality';
export type ValidationVerdict = 'APPROVED' | 'REJECTED' | 'NEEDS_FIX';

// Record verdicts
recordValidationVerdict(directory: string, type: ValidationVerdictType, verdict: ValidationVerdict, issues?: string[]): boolean

// Get status
getValidationStatus(directory: string): ValidationCoordinatorResult | null

// Control validation rounds
startValidationRound(directory: string): boolean
shouldRetryValidation(directory: string, maxRounds?: number): boolean
getIssuesToFix(directory: string): string[]

// Prompts and display
getValidationSpawnPrompt(specPath: string): string
formatValidationResults(state: AutopilotState): string
```

### Summaries

```typescript
// Generate summary
generateSummary(directory: string): AutopilotSummary | null

// Format summaries
formatSummary(summary: AutopilotSummary): string
formatCompactSummary(state: AutopilotState): string
formatFailureSummary(state: AutopilotState, error?: string): string
formatFileList(files: string[], title: string, maxFiles?: number): string
```

### Cancellation & Resume

```typescript
// Cancel and preserve progress
cancelAutopilot(directory: string): CancelResult
clearAutopilot(directory: string): CancelResult

// Resume
canResumeAutopilot(directory: string): { canResume: boolean; state?: AutopilotState; resumePhase?: string }
resumeAutopilot(directory: string): { success: boolean; message: string; state?: AutopilotState }

// Display
formatCancelMessage(result: CancelResult): string
```

### Usage Example

```typescript
import {
  initAutopilot,
  getPhasePrompt,
  readAutopilotState,
  transitionRalphToUltraQA,
  getValidationStatus,
  generateSummary,
  formatSummary
} from '@/hooks/autopilot';

// Initialize session
const idea = 'Create a REST API for todo management with authentication';
const state = initAutopilot(process.cwd(), idea, 'ses_abc123');

// Get expansion phase prompt
const prompt = getPhasePrompt('expansion', { idea });

// Monitor progress
const currentState = readAutopilotState(process.cwd());
console.log(`Phase: ${currentState?.phase}`);
console.log(`Agents spawned: ${currentState?.total_agents_spawned}`);

// Transition phases
if (currentState?.phase === 'execution' && currentState.execution.ralph_completed_at) {
  const result = transitionRalphToUltraQA(process.cwd(), 'ses_abc123');
  if (result.success) {
    console.log('Transitioned to QA phase');
  }
}

// Check validation
const validationStatus = getValidationStatus(process.cwd());
if (validationStatus?.allApproved) {
  const summary = generateSummary(process.cwd());
  if (summary) {
    console.log(formatSummary(summary));
  }
}
```

### State Persistence

All state is persisted to `.omc/state/autopilot-state.json` and includes:

- Active status and current phase
- Original user idea
- Phase-specific progress (expansion, planning, execution, qa, validation)
- Files created and modified
- Agent spawn count and metrics
- Phase duration tracking
- Session binding

---

## See Also

- [CHANGELOG.md](../CHANGELOG.md) - Version history
- [ARCHITECTURE.md](./ARCHITECTURE.md) - System architecture
- [MIGRATION.md](./MIGRATION.md) - Migration guide
- [Agent Definitions](../src/agents/definitions.ts) - Agent configuration

## Top-level structure

- `.claude-plugin/` — Claude Code plugin manifest (marketplace install entrypoint)
- `.clawhip`, `.codex`, `.omx` — provider-compat scaffolding (Codex/other CLI integration)
- `.github/` — CI workflows (boilerplate, not fetched)
- `AGENTS.md`, `CLAUDE.md` — agent instruction files consumed by OMC itself
- `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` — project metadata
- `README.md` + 12 localized README variants (de, es, fr, it, ja, ko, pt, ru, tr, vi, zh)
- `agents/` — 19 agent definition files (analyst, architect, code-reviewer, code-simplifier, critic, debugger, designer, document-specialist, executor, explore, git-master, planner, qa-tester, scientist, security-reviewer, test-engineer, tracer, verifier, writer)
- `assets/` — images (e.g. omc-character.jpg)
- `benchmark/`, `benchmarks/` — performance/quality benchmarking harnesses
- `bin/oh-my-claudecode.js` — CLI entrypoint (installs as `omc`)
- `bridge/` — external integration bridge (OpenClaw gateway, etc.)
- `commands/` — 20 slash-command definitions (ask, autoresearch, ccg, compact, configure-notifications, debug, deep-dive, deepinit, external-context, hud, learner, mcp-setup, omc-doctor, omc-setup, omc-teams, project-session-manager, psm, release, remember, sciomc)
- `dist/` — build output
- `docs/` — full documentation set (ARCHITECTURE.md, REFERENCE.md, FEATURES.md, GETTING-STARTED.md, MIGRATION.md, HOOKS.md, TOOLS.md, COMPATIBILITY.md, DEVELOPERS.md, TEAM-WORKTREE-MODE.md, SYNC-SYSTEM.md, settings-schema.md, ultragoal.md, geobench.md, plus subfolders agent-templates/, agents/, design/, issues/, shared/)
- `eslint.config.js`, `tsconfig.json`, `vitest.config.ts` — tooling config
- `examples/` — advanced-usage.ts, basic-usage.ts, delegation-enforcer-demo.ts, hooks.json, vendor-mcp-server
- `geobench/` — GEO visibility benchmark spec (oh-my-claudecode.yaml)
- `hooks/hooks.json` — lifecycle hook registration (UserPromptSubmit, Stop, PreCompact, SubagentStart/Stop, etc.)
- `missions/`, `research/`, `seminar/` — internal research/mission artifacts
- `package.json`, `package-lock.json` — npm package `oh-my-claude-sisyphus` (installs `oh-my-claudecode` + `omc` binaries)
- `scripts/` — build/release/sync scripts (e.g. openclaw-gateway-demo.mjs, sync-metadata:verify)
- `shellmark/` — shell integration helper
- `skills/` — 37 skill directories (ai-slop-cleaner, ask, autopilot, autoresearch, cancel, ccg, configure-notifications, debug, deep-dive, deep-interview, deepinit, external-context, hud, learner, local-build-reminder, mcp-setup, omc-doctor, omc-reference, omc-setup, omc-teams, plan, project-session-manager, ralph, ralplan, release, remember, sciomc, self-improve, setup, skill, skillify, team, trace, ultragoal, ultraqa, ultrawork, verify, visual-verdict, wiki)
- `src/` — TypeScript source: agents, autoresearch, cli, commands, config, constants, features, goal-workflows, hooks, hud, index.ts, installer, interop, lib, mcp, notifications, openclaw, planning, platform, providers, ralphthon, shared, skills, team, tools, types, ultragoal, utils, verification
- `templates/` — scaffolding templates
- `tests/` — fixtures, integration, lint, perf test suites
- `typos.toml` — spell-check config
