# alvinunreal/tmuxai

## Metadata
- Stars: 1,790
- Primary language: Go
- Default branch: main
- Latest release: v2.1.4 (about 22 hours ago)
- License: Apache License 2.0
- Homepage: https://tmuxai.dev
- Fetched: 2026-05-02
- Final URL: https://github.com/alvinunreal/tmuxai

## Description
AI-Powered, Non-Intrusive Terminal Assistant — an intelligent pair programmer that lives inside tmux sessions.

## README
TmuxAI is an intelligent terminal assistant that lives inside your tmux sessions. Unlike other CLI AI tools, TmuxAI observes and understands the content of your tmux panes, providing assistance without requiring you to change your workflow or interrupt your terminal sessions.

Think of TmuxAI as a _pair programmer_ that sits beside you, watching your terminal environment exactly as you see it. It can understand what you're working on across multiple panes, help solve problems and execute commands on your behalf in a dedicated execution pane.

### Human-Inspired Interface

TmuxAI's design philosophy mirrors the way humans collaborate at the terminal. Just as a colleague sitting next to you would observe your screen, understand context from what's visible, and help accordingly, TmuxAI:

1. **Observes**: Reads the visible content in all your panes
2. **Communicates**: Uses a dedicated chat pane for interaction
3. **Acts**: Can execute commands in a separate execution pane (with your permission)

### Installation

TmuxAI requires only tmux to be installed. Designed for Unix-based systems (Linux and macOS).

```bash
# Quick install
curl -fsSL https://get.tmuxai.dev | bash

# Homebrew
brew install tmuxai

# From source
go install github.com/alvinunreal/tmuxai@main
```

Manual download of pre-built binaries from GitHub releases is also supported.

### Post-Installation Setup

TmuxAI reads its configuration from `~/.config/tmuxai/config.yaml`:

```yaml
models:
  primary:
    provider: openrouter  # openrouter, openai or azure
    model: anthropic/claude-haiku-4.5
    api_key: sk-your-api-key
```

Then run `tmuxai` inside a tmux session.

### TmuxAI Layout

TmuxAI organizes your workspace into three pane roles:

1. **Chat Pane**: REPL-like interface with syntax highlighting, auto-completion, and readline shortcuts.
2. **Exec Pane**: Where commands are executed (with user confirmation). Force a specific pane with `--exec-pane`.
3. **Read-Only Panes**: All other panes — TmuxAI reads their content for context but does not interact.

### Observe Mode (default)

TmuxAI operates by default in observe mode:

1. User types a message in the Chat Pane.
2. TmuxAI captures context from all visible panes: current command, shell type, OS, pane content.
3. TmuxAI sends message + context + history to the AI model.
4. AI responds, possibly suggesting a command.
5. If a command is suggested, TmuxAI checks whitelist/blacklist patterns, shows a risk indicator (✓ safe, ? unknown, ! danger), and asks for confirmation.
6. If approved, executes in Exec Pane, waits `wait_interval` (default 5s), captures new output, sends back to AI.
7. Conversation continues until task is complete.

### Prepare Mode

Prepare mode customizes your shell prompt with special markers for exact command-completion detection and exit-code awareness, eliminating fixed wait intervals:

```
TmuxAI » /prepare         # auto-detect shell
TmuxAI » /prepare bash    # specify shell manually
```

Supports bash, zsh, and fish.

### Watch Mode

Watch Mode transforms TmuxAI into a proactive assistant that continuously monitors terminal activity:

```
TmuxAI » /watch spot and suggest more efficient alternatives to my shell commands
TmuxAI » /watch flag commands that could expose sensitive data or weaken system security
TmuxAI » /watch monitor log output for errors, warnings, or critical issues and suggest fixes
```

### Knowledge Base

Pre-defined context files in markdown format stored in `~/.config/tmuxai/kb/`:

```bash
TmuxAI » /kb                         # list available KBs
TmuxAI » /kb load docker-workflows   # load a KB into context
TmuxAI » /kb unload docker-workflows # unload
```

KBs can be auto-loaded on startup via `knowledge_base.auto_load` in config.

### Skills

The Skills system extends the Knowledge Base with structured, metadata-rich instructions (SKILL.md files with frontmatter). Skills can be auto-discovered, lazily loaded, and optionally auto-matched to incoming messages.

```bash
TmuxAI » /skill                      # list skills
TmuxAI » /skill load git-hooks       # lazy-load skill body
TmuxAI » /skill validate             # validate all skills
```

Skills are disabled by default; enable with `knowledge_base.skills.enabled: true`.

Auto-match (enabled with `auto_match: true`) analyses incoming messages and loads relevant skills automatically using term-frequency matching. Budget controls: `max_l1_chars` (8,000), `max_loaded_chars` (32,000), `max_skill_chars` (20,000).

### Model Configuration

Supports multiple named model configurations and hot-switching between them:

```yaml
default_model: "fast"
models:
  fast:
    provider: "openrouter"
    model: "anthropic/claude-haiku-4.5"
    api_key: "sk-or-..."
  smart:
    provider: "openrouter"
    model: "google/gemini-2.5-prod"
    api_key: "sk-or-..."
```

Supported providers: `openrouter`, `openai`, `azure`, `gemini`, `bedrock`, `github-copilot`.

### Context Management (Squashing)

When context reaches 80% of `max_context_size` (default 100,000 tokens), TmuxAI automatically summarises history. Manual squash: `TmuxAI » /squash`. Monitor with `TmuxAI » /info`.

### Core Commands

| Command | Description |
|---|---|
| `/prepare [shell]` | Enable prepare mode |
| `/watch <goal>` | Enable watch mode |
| `/kb [load/unload] <name>` | Manage knowledge bases |
| `/skill [load/unload/validate] <name>` | Manage skills |
| `/squash` | Manually compress context |
| `/info` | Show context usage |
| `/model <name>` | Switch AI model |

## Top-level structure
- `cli/` — CLI entry points and command parsing
- `config/` — configuration loading and validation
- `internal/` — core internal packages (AI client, tmux integration, pane capture, etc.)
- `logger/` — logging subsystem
- `system/` — OS/system utilities
- `tasks/` — task/workflow execution
- `main.go` — application entry point
- `config.example.yaml` — full annotated configuration example
- `install.sh` — installation script (mirrored at get.tmuxai.dev)
- `go.mod` / `go.sum` — Go module definition
- `.goreleaser.yml` — release automation configuration
