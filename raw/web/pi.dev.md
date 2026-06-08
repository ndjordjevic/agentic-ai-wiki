# pi.dev

## Fetch log
- Inbox URL: https://pi.dev/
- Final URL: https://pi.dev/
- Fetched: 2026-06-08
- Pages: 4 (homepage, /docs/latest, /packages, /models, /news)
- Mode: standard
- llms.txt: absent (404)
- Companion GitHub: earendil-works/pi → raw/github/earendil-works-pi.md

## Homepage — https://pi.dev/

Pi is a minimal terminal coding harness by Earendil Inc., MIT licensed. Described as "primitives, not features" — a lightweight shell that stays minimal while supporting deep customization via TypeScript extensions.

**Install:**
```
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```
Or via Linux/macOS installer script. Launch with `pi` in your project directory.

**Modes:**
- Interactive TUI (terminal UI with differential rendering)
- Print/JSON mode (non-interactive output)
- RPC mode (JSONL-based RPC for programmatic control)
- SDK mode (embed in Node.js applications)

**Provider support:** 15+ providers — Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, HuggingFace, Ant Ling, NVIDIA NIM, MiniMax, and more (968 models across 30+ providers).

**Session model:** Tree-structured conversation history stored in JSONL files at `~/.pi/sessions/`.

**Context:** Via AGENTS.md / SYSTEM.md in project directory.

**Extensions:** TypeScript-based extensions for sub-agents, plan mode, permission gates, SSH, sandboxing, MCP tool integration.

**npm package:** @earendil-works/pi-coding-agent
**GitHub:** https://github.com/earendil-works/pi
**Discord:** discord.com/invite/3cU7Bz4UPx

---

## Docs — https://pi.dev/docs/latest

Note: Doc sub-pages (e.g., /docs/latest/getting-started) return 404 in direct fetch (client-side SPA routing). Content below derived from docs homepage.

### Documentation sections

**Getting Started**
- Installation (npm global install, installer script)
- Authentication (provider API keys)
- Interactive usage (TUI walkthrough)
- Provider configuration
- Settings, keybindings, sessions, compaction

**Customization**
- Extensions (TypeScript, loaded from `~/.pi/agent/extensions/` or via `pi install`)
- Skills (SKILL.md-based agent skills)
- Prompt templates
- Themes
- Pi packages (install via `pi install npm:<name>`)
- Custom models/providers
- API implementations

**Programmatic Integration**
- SDK (`createAgentSession()` for Node.js embedding)
- RPC mode (JSONL over stdin/stdout)
- JSON event streams
- Custom TUI components

**Reference**
- JSONL session format
- SessionManager API

**Platform-Specific**
- Windows, Android (Termux), tmux, shell config

**Development**
- Contributing, build steps

**Containerization / Permissions:**
Pi runs with user-level permissions; no built-in sandbox. Three containerization patterns documented:
- OpenShell: policy-controlled sandbox around `pi` process
- Gondolin extension: route built-in tools into local Linux micro-VM
- Plain Docker: run `pi` in local container

---

## Packages — https://pi.dev/packages

3,726 packages indexed, installed via `pi install npm:<name>`.

Top packages by downloads:
- `context-mode` — 131,500 downloads
- `pi-subagents` — 103,200 downloads

---

## Models — https://pi.dev/models

968 models across 30+ providers. Browseable/filterable model registry.

---

## News — https://pi.dev/news

**Pi 0.78.1** (June 4, 2026):
- Added Ant Ling and NVIDIA NIM provider setup, MiniMax-M3 support
- Extensions can use `ctx.mode` and `ctx.getSystemPromptOptions()` to adapt across TUI/RPC/JSON/print modes

**Pi 0.78.0** (May 29, 2026):
- Named startup sessions via `--name` flag
- Built-in file tool titles render OSC 8 file:// hyperlinks

**Pi 0.77.0** (May 28, 2026):
- Claude Opus 4.8 support
- Selective tool disablement with `--exclude-tools` flag
- Headless Codex subscription login via device-code auth

**Breaking changes:**
- Node.js minimum v22.19.0 (since 0.75.0)
- Package scope migrated from `@mariozechner` to `@earendil-works` (since 0.74.0)
