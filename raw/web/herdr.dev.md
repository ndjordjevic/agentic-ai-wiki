# herdr.dev

## Fetch log
- Inbox URL: https://herdr.dev/
- Final URL: https://herdr.dev/
- Fetched: 2026-07-09
- Pages: 8
- Mode: standard

## Landing page — https://herdr.dev/

**Title:** Herdr: one terminal for the whole herd

**Description:** Herdr is to coding agents what tmux is to terminals: an agent multiplexer that runs where your agents run. Real panes, agent state at a glance, ssh from anywhere, no app.

**Hero:**
> One terminal. The whole herd.
> Run all your coding agents from one terminal, on any box, even over ssh. Each runs in its own real terminal, on a server that keeps it alive when you close the laptop. See blocked, working, and done at a glance, and reattach from your phone.

- Stable Linux/macOS · Windows preview beta · no Electron, no account, no telemetry
- GitHub: https://github.com/ogulcancelik/herdr

**Install options:**
- Script: `curl -fsSL https://herdr.dev/install.sh | sh`
- Homebrew: `brew install herdr`
- Nix flake: `nix run github:ogulcancelik/herdr`
- Windows beta: `irm https://herdr.dev/install.ps1 | iex`

**Nav links:** Home, Compare, Plugins, Stats, Blog, Quick start, Docs, API, Install

## Docs — https://herdr.dev/docs/

New to terminal multiplexers?
You don't need to learn shortcuts to start. Herdr is mouse-first: click panes, drag borders, split and switch from right-click menus.

Coming from tmux or zellij?
You already know the model. The prefix is `ctrl+b`, panes persist, detach and reattach work the way you expect.

**Doc sections:**
- Agents — supported agents, detection behavior, integrations, custom labels, direct attach → /docs/agents/
- Session state — detach, restart restore, pane history replay, native agent resume, live handoff → /docs/session-state/
- Configuration — keybindings, themes, sidebar, notifications, scrollback, advanced → /docs/configuration/
- API — CLI and local socket API → /docs/socket-api/
- Plugins — author local executable workflow plugins with manifest actions and event hooks → /docs/plugins/
- Marketplace — share plugins from GitHub → /docs/marketplace/

## Quick start — https://herdr.dev/docs/quick-start/

Herdr launches or attaches to your default background session automatically. A workspace is a project-level container for tabs, panes, and agents.

Herdr is mouse-native: click panes, tabs, workspaces, and agents to focus them. Drag split borders to resize. Right-click for context menus. Drag-select text to copy; double-click a token to copy it directly.

Start a coding agent in a pane: run `claude`, `codex`, `pi`, `opencode`, or any other supported agent. Herdr detects it automatically. The sidebar shows agent state (working, blocked, done, idle) across every workspace.

**Common keybindings (prefix = ctrl+b):**

| Action | Key |
|---|---|
| Split right | prefix+v |
| Split down | prefix+minus |
| New tab | prefix+c |
| Next/previous tab | prefix+n / prefix+p |
| Workspace navigation | prefix+w |
| New workspace | prefix+shift+n |
| Detach client | prefix+q |

Press `prefix+q` or close the terminal window — the server and every agent keep running. Run `herdr` to reattach.

## Concepts — https://herdr.dev/docs/concepts/

**Workspace** — top-level project container. Use one workspace per repo/task/investigation. Sidebar state rolls up from agents inside it.

**Tab** — a layout inside a workspace. Use tabs to separate views (agents, logs, server, review). Addressable from CLI and socket API.

**Pane** — a real terminal. Herdr renders the output, sends input back, preserves the pane across client detach.

**Agent states:**

| State | Meaning |
|---|---|
| blocked | Needs input, approval, or a decision |
| working | Actively running |
| done | Finished and not yet looked at |
| idle | Finished or waiting and has been seen |
| unknown | Cannot confidently classify |

**Session** — a persistent Herdr server namespace. Default command attaches to default session. Named sessions: `herdr session attach <name>`.

**Modes:** terminal mode (sends keys to pane), prefix mode (waits for action key), navigate mode (workspace navigation surface).

## Agents — https://herdr.dev/docs/agents/

Herdr supports running multiple coding agents simultaneously. Agents have two detection mechanisms:
- **Lifecycle hooks** — when installed, the integration is authoritative for state
- **Screen manifest** — Herdr reads the bottom-buffer snapshot and evaluates TOML manifests

**Supported agents (selection):**

| Agent | State authority |
|---|---|
| Pi | lifecycle hooks or screen manifest |
| Claude Code | screen manifest |
| Codex | screen manifest |
| GitHub Copilot CLI | screen manifest |
| OpenCode | lifecycle plugin or screen manifest |
| Hermes Agent | lifecycle hooks or screen manifest |
| Kimi Code CLI | lifecycle hooks or screen manifest |
| MastraCode | lifecycle hooks |
| Antigravity CLI | screen manifest |
| Grok CLI | screen manifest |
| Amp | screen manifest |

Manifests live inside Herdr and are updated remotely without restart. Local overrides at `~/.config/herdr/agent-detection/<agent>.toml` always win.

On Linux with process isolation wrappers (VMs, Bubblewrap): set `HERDR_AGENT=<agent>` to tell Herdr which manifest to use.

## Session state — https://herdr.dev/docs/session-state/

| Case | Processes keep running | Layout returns | Screen returns | Agent conversation resumes |
|---|---|---|---|---|
| Detach and reattach | Yes | Yes | Yes | Yes |
| Server restart | No | Yes | Only with pane history | Only with native session restore |
| Update with --handoff | Best effort | Yes | Yes if handoff succeeds | Yes if handoff succeeds |

**Native session restore** — Herdr resumes supported agent panes after server restart using official integration-reported session references:

| Agent | Minimum integration version | Resume command |
|---|---|---|
| Claude Code | 6 | `claude --resume <id>` |
| Codex | 5 | `codex resume <id>` |
| GitHub Copilot CLI | 2 | `copilot --resume=<id>` |
| Pi | 2 | `pi --session <id>` |
| OpenCode | 5 | `opencode --session <id>` |
| Hermes Agent | 2 | `hermes --resume <id>` |

**Pane screen history** — off by default (can contain secrets). Enable from Settings > Experiments or via config. Stores recent terminal contents in `session-history.json`.

## Socket API — https://herdr.dev/docs/socket-api/

Herdr exposes a local socket API for scripts and agents:

| Layer | Use it for |
|---|---|
| Agent skill | Teaching a coding agent how to use Herdr from inside a pane |
| CLI wrappers | Shell scripts, simple orchestration, human debugging |
| Raw socket API | Custom tools, protocol clients, event subscribers |

Print schema: `herdr api schema --output herdr-api.schema.json`

**CLI examples:**

```bash
herdr workspace create --cwd ~/project --label api
herdr tab create --label logs
herdr pane split w1:p1 --direction right
herdr pane run w1:p2 "npm test"
herdr wait agent-status w1:p1 --status done
herdr pane read w1:p2 --source recent --lines 50
```

**Raw socket API method areas:** Server, Notification, Client, Session, Workspace, Tab, Pane, Agent, Integration, Config.

## Install — https://herdr.dev/docs/install/

```bash
# Script (Linux/macOS stable)
curl -fsSL https://herdr.dev/install.sh | sh

# Homebrew
brew install herdr

# mise
mise use -g herdr

# Nix flake
nix run github:ogulcancelik/herdr/v0.7.3

# Windows beta
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

Binary assets:

| System | Asset |
|---|---|
| Linux x86_64 | herdr-linux-x86_64 |
| Linux aarch64 | herdr-linux-aarch64 |
| macOS Intel | herdr-macos-x86_64 |
| macOS Apple silicon | herdr-macos-aarch64 |

Update: `herdr update` (for script installs; Homebrew/mise/Nix update through their own package manager).
