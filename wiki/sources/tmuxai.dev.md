---
type: source
source_url: https://tmuxai.dev/
companion_urls:
  - https://github.com/alvinunreal/tmuxai
raw_files:
  - ../../raw/web/tmuxai.dev.md
  - ../../raw/github/alvinunreal-tmuxai.md
tags:
  - terminal-assistant
  - tmux
  - ai-agent
  - context-aware
  - observe-mode
  - watch-mode
  - knowledge-base
  - skills
  - go
related:
  - tmux-tmux
  - njbrake-agent-of-empires
  - warp.dev
  - happy.engineering
  - codeyai.space
  - Yeachan-Heo-oh-my-claudecode
product: tmuxai
detail_level: standard
created: 2026-05-02
updated: 2026-07-06
---

TmuxAI is an AI-powered, non-intrusive terminal assistant that runs inside a tmux session as a "pair programmer" alongside your existing workflow. Rather than replacing your shell or requiring a special terminal emulator, TmuxAI reads the live content of all visible tmux panes, communicates through a dedicated Chat Pane, and executes commands in a separate Exec Pane—always with user confirmation. With 1,790 GitHub stars and an active release cadence (v2.1.4 as of May 2026), TmuxAI sits at the intersection of AI agent tooling and the [[tmux-tmux]] ecosystem, and complements multi-agent session managers like [[njbrake-agent-of-empires]].

_All claims below are sourced from ../../raw/web/tmuxai.dev.md unless otherwise noted._

## What it does

TmuxAI attaches to your tmux session and organises the current window into three pane roles: a **Chat Pane** (REPL-like interface with syntax highlighting and auto-completion), an **Exec Pane** (where suggested commands run with your permission), and **Read-Only Panes** (all other panes, observed for context but never modified). When you type a request in the Chat Pane, TmuxAI captures the visible content of every pane, sends it along with your message and conversation history to a configured AI model, and returns a response that may include a command to execute.

## Key features

- **Observe Mode** (default) — reads pane context on each user message; commands require confirmation with a risk indicator (✓ safe, ? unknown, ! danger) before execution. (../../raw/github/alvinunreal-tmuxai.md)
- **Prepare Mode** — customises the shell prompt with special markers (`/prepare [shell]`) to enable exact command-completion detection and exit-code tracking, eliminating the fixed wait interval. Supports bash, zsh, fish. (../../raw/github/alvinunreal-tmuxai.md)
- **Watch Mode** — proactive monitoring; TmuxAI polls all panes on a configurable interval and offers suggestions based on a user-defined goal (e.g. "flag commands exposing sensitive data"). (../../raw/github/alvinunreal-tmuxai.md)
- **Knowledge Base** — inject markdown context files from `~/.config/tmuxai/kb/` into the conversation with `/kb load <name>`; auto-load on startup via config.
- **Skills** — structured SKILL.md-based instruction modules extending the KB system; supports auto-match against incoming messages using term-frequency scoring. Disabled by default. (../../raw/github/alvinunreal-tmuxai.md)
- **Multi-model support** — define multiple named model configs in `config.yaml` and switch with `/model <name>`. Supported providers: openrouter, openai, azure, gemini, bedrock, github-copilot.
- **Context squashing** — automatically summarises conversation history at 80% of `max_context_size` (default 100,000 tokens); manual squash with `/squash`.
- **Whitelist/blacklist patterns** — regex-based command confirmation bypass or force-confirm.
- **Universal terminal compatibility** — SSH sessions, database CLIs, network device shells, nested shells.

## Architecture

TmuxAI is written in Go and built around the `tmux capture-pane` and `tmux send-keys` primitives. (../../raw/github/alvinunreal-tmuxai.md) The internal package layout separates concerns into: `cli/` (CLI parsing), `config/` (YAML config loading), `internal/` (AI client, tmux pane capture, conversation management), `tasks/` (workflow execution), `logger/`, and `system/`. The AI client is provider-agnostic: it targets OpenAI-compatible chat-completion endpoints plus native SDKs for Gemini and GitHub Copilot. The knowledge base and skills subsystems inject context between the system prompt and conversation history; skills add a two-level loading model (L1 discovery block of descriptions, L2 lazy-loaded bodies). (../../raw/github/alvinunreal-tmuxai.md)

## Installation

```bash
# Quick install (Linux/macOS)
curl -fsSL https://get.tmuxai.dev | bash

# Homebrew
brew install tmuxai

# From source (Go required)
go install github.com/alvinunreal/tmuxai@main
```

Then create `~/.config/tmuxai/config.yaml` with at least one model entry before running `tmuxai` inside a tmux session. (../../raw/github/alvinunreal-tmuxai.md)

## Example usage

```bash
# Start TmuxAI in your tmux window
tmuxai

# In the Chat Pane:
TmuxAI » find large files and cleanup some space

TmuxAI» find . -type f -size +100M -exec du -h {} \; | sort -rh
Do you want to execute this command? [Y]es/No/Edit:

# Enable prepare mode for better shell tracking
TmuxAI » /prepare

# Enable watch mode for proactive monitoring
TmuxAI » /watch monitor log output for errors and suggest fixes

# Load a project-specific knowledge base
TmuxAI » /kb load docker-workflows

# Check context usage
TmuxAI » /info
```

## When to use

TmuxAI is the right choice when you want AI assistance at the terminal without abandoning your existing tmux-based workflow. It is especially useful for: exploratory debugging sessions across multiple panes, infrastructure work over SSH, learning more efficient shell commands via Watch Mode, and scripting repetitive CLI workflows through the conversational interface. It is not a code editor or IDE — for integrated coding-agent workflows across multiple repos, [[njbrake-agent-of-empires]] may be a better fit.

## Maintenance status

Apache License 2.0. 1,790 stars, 109 forks. Latest release: v2.1.4 (May 2026). Actively maintained by Boring Dystopia Development (alvinunreal). Issue tracker and discussion forums on GitHub. (../../raw/github/alvinunreal-tmuxai.md)

## Ecosystem

TmuxAI is part of a growing layer of AI tooling built on [[tmux-tmux]]:
- [[njbrake-agent-of-empires]] — session manager for running multiple AI coding agents in parallel tmux sessions; complementary at the session-orchestration layer.
- [tmux Plugin Manager (TPM)](https://github.com/tmux-plugins/tpm) — no direct integration, but TmuxAI works alongside any existing tmux config and plugins.
- The [[skills.sh]] ecosystem provides the SKILL.md format that TmuxAI's own Skills feature implements natively.
