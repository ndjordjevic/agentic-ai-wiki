# tmuxai.dev

## Fetch log
- Inbox URL: https://tmuxai.dev/
- Final URL: https://tmuxai.dev/
- Fetched: 2026-05-02
- Pages: 3
- Mode: standard

## Landing page — https://tmuxai.dev/

# TmuxAI: AI-Powered, Non-Intrusive Terminal Assistant

TmuxAI is a non-intrusive terminal assistant that works alongside you in a tmux window. TmuxAI's design philosophy mirrors the way humans collaborate at the terminal. Just as a colleague sitting next to you, TmuxAI observes your screen, understands context from what's visible, and helps accordingly.

Install:
```bash
curl -fsSL https://get.tmuxai.dev | bash
```

GitHub: https://github.com/alvinunreal/tmuxai

### Features

**CONTEXT-AWARE TERMINAL ASSISTANCE** — TmuxAI reads and understands what's displayed across all your terminal panes in real-time, providing intelligent help based on what you're actually working on.

**ZERO-CONFIGURATION SETUP** — Works instantly with your existing tmux setup without requiring special shells, wrappers, or terminal emulators. Just install and run.

**UNIVERSAL TERMINAL COMPATIBILITY** — Works with nested shells, SSH connections, database CLIs, network equipment shells (Cisco IOS, Juniper, etc), and any other text-based terminal interface.

**PREPARE MODE** — Enhances command tracking with custom shell prompts that provide exact command completion detection and exit code awareness for more accurate assistance.

**WATCH MODE** — Transforms TmuxAI into a proactive assistant that monitors your terminal activity and offers improvements or explanations based on your specified goals.

**OPEN SOURCE** — Available as open source software under Apache License 2.0. Use TmuxAI for free and adapt it to your workflow.

### Footer navigation

Learn tmux:
- tmux Cheat Sheet: https://tmuxai.dev/tmux-cheat-sheet/
- tmux Shortcuts: https://tmuxai.dev/tmux-shortcuts/
- tmux Getting Started: https://tmuxai.dev/tmux-getting-started/
- tmux FAQ: https://tmuxai.dev/tmux-faq/
- tmux Plugins: https://tmuxai.dev/tmux-plugins/
- tmux Config Generator: https://tmuxai.dev/tmux-config/

Marketing comparisons:
- TmuxAI vs Warp: https://tmuxai.dev/tmuxai-vs-warp/
- Tmux vs Zellij: https://tmuxai.dev/tmux-vs-zellij/
- Tmux vs Screen: https://tmuxai.dev/tmux-vs-screen/
- Warp Alternatives: https://tmuxai.dev/warp-terminal-alternatives/

Project:
- GitHub Repository: https://github.com/alvinunreal/tmuxai
- License: Apache License 2.0

## Docs — https://tmuxai.dev/getting-started/

TmuxAI is an intelligent terminal assistant that lives inside your tmux sessions. Unlike other CLI AI tools, TmuxAI observes and understands the content of your tmux panes, providing assistance without requiring you to change your workflow or interrupt your terminal sessions.

Think of TmuxAI as a _pair programmer_ that sits beside you, watching your terminal environment exactly as you see it.

### TmuxAI Layout

TmuxAI operates within a single tmux window (one instance per window):

1. **Chat Pane** — REPL-like interface with syntax highlighting, auto-completion, and readline shortcuts.
2. **Exec Pane** — Where AI-suggested commands are executed. Force a specific pane with `--exec-pane`.
3. **Read-Only Panes** — All other panes provide context. TmuxAI reads but does not interact with them.

### Observe Mode (default)

1. User types a message in the Chat Pane.
2. TmuxAI captures context from all visible panes: current command, shell type, OS, pane content.
3. Sends message + context + history to the AI model.
4. AI responds; if a command is suggested, TmuxAI checks whitelist/blacklist patterns and shows a risk indicator (✓ safe, ? unknown, ! danger).
5. If approved, executes in Exec Pane, waits `wait_interval` (default 5s), re-captures output, sends back to AI.

### Prepare Mode

Enhances TmuxAI by customising the shell prompt with special markers for exact command-completion detection and exit-code awareness. Eliminates fixed wait intervals.

```
TmuxAI » /prepare         # auto-detect shell
TmuxAI » /prepare bash    # specify shell
```
Supports bash, zsh, and fish.

### Watch Mode

Continuously monitors terminal activity and provides proactive suggestions:

```
TmuxAI » /watch spot and suggest more efficient alternatives to my shell commands
TmuxAI » /watch flag commands that could expose sensitive data or weaken system security
TmuxAI » /watch monitor log output for errors, warnings, or critical issues and suggest fixes
```

### Knowledge Base

Markdown context files in `~/.config/tmuxai/kb/` injectable into the conversation:

```bash
TmuxAI » /kb                         # list
TmuxAI » /kb load docker-workflows   # load into context
TmuxAI » /kb unload docker-workflows # unload
```
Auto-load on startup via `knowledge_base.auto_load` in config.

### Skills

Extends the KB system with structured SKILL.md-based instruction modules. Auto-discovery, lazy loading, and optional auto-match against incoming messages. Disabled by default; enabled with `knowledge_base.skills.enabled: true`.

Budget controls: `max_l1_chars` (8,000), `max_loaded_chars` (32,000), `max_skill_chars` (20,000).

### Model Configuration

Supports multiple named model configurations:

```yaml
default_model: "fast"
models:
  fast:
    provider: "openrouter"
    model: "anthropic/claude-haiku-4.5"
    api_key: "sk-or-..."
```

Supported providers: `openrouter`, `openai`, `azure`, `gemini`, `bedrock`, `github-copilot`.

### Context Management (Squashing)

At 80% of `max_context_size` (default 100,000 tokens), TmuxAI auto-squashes conversation history. Manual: `TmuxAI » /squash`. Monitor: `TmuxAI » /info`.

### Core Commands

| Command | Description |
|---|---|
| `/prepare [shell]` | Enable prepare mode |
| `/watch <goal>` | Enable watch mode |
| `/kb [load/unload] <name>` | Manage knowledge bases |
| `/skill [load/unload/validate] <name>` | Manage skills |
| `/squash` | Compress context |
| `/info` | Show context usage |
| `/model <name>` | Switch AI model |

### Configuration reference (key settings)

```yaml
debug: false
yolo: false
max_context_size: 100000
max_capture_lines: 200
wait_interval: 5
exec_confirm: true
send_keys_confirm: true
paste_multiline_confirm: true
whitelist_patterns: ['^find(\s+.*)?$', '^pwd\s*$', '^cat(\s+.*)?$']
blacklist_patterns: ['rm\s+', 'mv\s+', 'dd\s+']
tmux:
  exec_split_args: ["-d", "-h"]
```
