---
type: source
source_url: https://www.codeyai.space/
tags:
  - local-first
  - coding-agent
  - multi-agent
  - bring-your-own-provider
  - mcp
  - skills
  - autopilot
  - n8n
  - next-js-generation
  - tui
related:
  - warp.dev
  - factory.ai
  - tmuxai.dev
  - happy.engineering
  - zcode.z.ai
  - openvibe.sh
product: codey
detail_level: standard
created: 2026-07-04
updated: 2026-07-04
---

Codey is a local-first "AI development OS" — a private desktop and terminal workspace that runs specialized coding agents, generates production Next.js apps, delegates knowledge work, and connects 70+ LLM providers without routing model usage through Codey's billing. Built-in agents (Prometheus, Athena, Scout, Iris, Matis, Hermes) cover the Co-Pilot, Autopilot, and Workpilot modes; Pro is $10/month for advanced modes while model costs stay with the providers you already pay for.

_All claims below are sourced from ../../raw/web/codeyai.space.md unless otherwise noted._

## What it does

Codey installs on your machine (`curl -fsSL https://codey.ai/install | bash` or Homebrew) and provides a TUI, desktop app, CLI (`codey run`, `codey serve`, `codey web`), and web client. On first use, `/init` inspects the repo and generates `AGENTS.md`. Tab switches between **Build Mode** (edits + commands) and **Plan Mode** (read-only analysis). Primary agents handle the main thread; subagents run isolated parallel tasks. Custom agent personas are defined in markdown under `~/.config/codey/agents/` or `.codey/agents/`.

## Key features

- **Co-Pilot** — Hands-on coding with Prometheus (build), Athena (plan), Scout (explore), Iris (helper); you stay at every decision.
- **Autopilot (Matis)** — Prompt-to-polished Next.js app generation with premium UI direction; Pro only.
- **Workpilot (Hermes)** — Research, docs, browser, sheets, slides, PDFs, files, and n8n automations; Pro only.
- **70+ LLM providers** — Claude, OpenAI/Codex, Gemini, OpenRouter, Ollama, Bedrock, custom endpoints; BYOK — no Codey markup on tokens.
- **Skills system** — Pre-packaged workflows (browser-automation, data-cleaning, n8n-automation) auto-loaded when prompts match.
- **MCP support** — Local subprocess and remote HTTP/SSE servers; OAuth PKCE with token storage in `~/.local/share/codey/mcp-auth.json`.
- **Core tools** — read/write/edit files, bash, grep, list_dir, webfetch with permission schemas.
- **Custom agents** — Markdown-defined personas with model, mode (primary/subagent), and tool restrictions; `@mention` invocation.

## Architecture and concepts

Codey separates **workspace subscription** (Pro unlocks Autopilot/Workpilot/custom agents/n8n) from **model billing** (always via your provider accounts). The agent loop is project-aware: tools execute locally in the project directory with guardrails. Primary vs subagent split mirrors patterns in [[factory.ai]] and [[shareai-lab-learn-claude-code]] — primary agents own the conversation; subagents (Scout, Iris, custom) handle parallel context gathering or side tasks without polluting main context. Build/Plan mode toggle is a first-class safety boundary. Codey Zen offers optional curated routing if you prefer not to manage keys manually.

## Main APIs

CLI surface:
- `codey run "prompt"` — headless single-shot
- `codey serve --port 4096 --hostname 127.0.0.1` — HTTP + WebSocket for editors/desktop
- `codey web` — local server + browser UI
- `codey auth login|list|logout|status` — provider credentials and Pro sync
- `codey agent create` — interactive custom agent builder

TUI commands include `/init`, `/connect`. Configuration supports MCP blocks, provider options (e.g. Bedrock region/profile), themes, keybinds, LSP, formatters, permissions.

## When to use

Codey fits developers who want a unified local agent workspace — coding, app generation, and office-style knowledge work — without surrendering code to a hosted black box or paying a middleman for model tokens. Co-Pilot is free with BYOK; Pro makes sense when you need Matis (vibe-to-Next.js) or Hermes (docs/sheets/slides/n8n). Compare terminal-native alternatives [[warp.dev]] and [[tmuxai.dev]], enterprise orchestration [[factory.ai]], mobile session extension [[happy.engineering]], and vendor-locked IDEs [[zcode.z.ai]].

## Ecosystem

Codey Labs ships desktop + TUI + CLI from one install. Skills extend agents for browser automation and n8n pipelines. n8n integration in Pro connects local agents to external automation graphs. No public GitHub repo was discovered on the marketing site — the product appears closed-source with docs at `codeyai.space/docs`. Product Hunt listing referenced on the homepage.
