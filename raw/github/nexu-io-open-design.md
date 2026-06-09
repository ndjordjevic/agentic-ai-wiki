# nexu-io/open-design

## Metadata
- Stars: 62118
- Primary language: TypeScript
- Default branch: main
- Latest release: open-design-v0.9.0 (2026-06-02)
- License: Apache License 2.0
- Homepage: https://open-design.ai
- Fetched: 2026-06-09
- Final URL: https://github.com/nexu-io/open-design

## Description
Local-first, open-source Claude Design alternative. Native desktop app. 259+ Skills · 142+ Design Systems. Web · desktop · mobile prototypes · slides · images · videos · HyperFrames. Sandboxed preview · HTML/PDF/PPTX/MP4 export. Claude Code / OpenClaw / Codex / Cursor / OpenCode / Qwen / Copilot / Hermes / Kimi & 17+ CLIs.

## README
<h1 align="center">Open Design: The open-source Claude Design alternative</h1>

> 🔥 **Open Design 0.9.0 is here: create without the setup.** The official Model Router is built right into the app — no extra configuration, no CLI to install, no API key to prepare. Just open the app, sign in, and start designing and creating right away.
>
> 🏅 **The Open Design Fellow program is now open.** If you also believe design should be open — become an Open Design Fellow, shape the product alongside the core team, and help more people take part in defining the future of design. Details → `MAINTAINERS.md` and Discord.

## What is Open Design

🎨 **The local-first, open-source Claude Design alternative.** 🖥️ **Native desktop app for macOS and Windows.** ⚡ **100+ skills** · ✨ **150 brand-grade `DESIGN.md` systems** · 📦 **261 ready-to-use plugins.** 🖼️ Generates **web · desktop · mobile prototypes**, **live dashboards / artifacts**, **decks**, **images**, **video**, plus **HyperFrames** motion graphics. 🔒 Sandboxed iframe preview · HTML / PDF / PPTX / MP4 export. 🤖 **Runs on Claude Code · OpenClaw · Codex · Cursor · OpenCode · Qwen · Copilot · Hermes · Kimi · Antigravity and 21 local CLIs**, or any OpenAI-compatible endpoint via BYOK.

Open Design is what you get when the **agent-native** loop Anthropic shipped with Claude Design — discover the brief, lock the direction, stream the artifact, critique, deliver — stops being closed and becomes a **filesystem of skills, design systems, and plugins** that the coding agents already on your laptop can read, write, and remix.

### Core pages

- **Home** — overview entry point; pick a skill and a design system, type the brief
- **Automation** — orchestrate repetitive design workflows into reusable, schedulable automations
- **Design System** — distill your team's `DESIGN.md` into a brand contract that shapes every output
- **Plugin** — browse, install, and distribute workflow plugins to extend generation on demand
- **Integrations** — connect external systems and MCP tools; use Open Design from any IDE, script, or automation

### Studio artifact types

- **Prototype** — single-page HTML artifacts that read your design system and render in a sandboxed iframe
- **HyperFrame** — programmatic motion and animated graphics, rendered to a real MP4 (e.g. 1920×1080 · 30fps)
- **Deck** — pitch decks exportable to PPTX / PDF
- **Image** — brand-grade images and visual assets with high-resolution generation

### Platform Compatibility

| Coding agent | Status | MCP install |
|---|:---:|---|
| Claude Code | ✅ Supported | `od mcp install claude` |
| Codex CLI | ✅ Supported | `od mcp install codex` |
| Cursor | ✅ Supported | `od mcp install cursor` |
| VS Code + GitHub Copilot | ✅ Supported | `od mcp install copilot` |
| GitHub Copilot CLI | ✅ Supported | `od mcp install copilot` |
| Gemini CLI | ✅ Supported | `od mcp install gemini` |
| OpenCode | ✅ Supported | `od mcp install opencode` |
| OpenClaw | ✅ Supported | `od mcp install openclaw` |
| Antigravity | ✅ Supported | `od mcp install antigravity` |
| Cline | ✅ Supported | `od mcp install cline` |
| Trae | ✅ Supported | `od mcp install trae` |
| Kimi CLI | ✅ Supported | `od mcp install kimi` |
| Pi Agent | ✅ Supported | `od mcp install pi` |
| Mistral Vibe CLI | ✅ Supported | `od mcp install vibe` |
| Hermes Agent | ✅ Supported | `od mcp install hermes` |

### Why Open Design

In April 2026, Anthropic released Claude Design — the first time an LLM stopped writing prose and started delivering design artifacts directly. Open Design is the open-source alternative: same loop, same artifact-first mental model, none of the lock-in.

Key differentiators:
- 🤖 Agent-native, model-agnostic — doesn't ship an agent; your existing CLI is the engine
- 🧠 Brand-grade by default — every render reads the active `DESIGN.md` (9-section schema: palette, type, spacing, motion, voice, anti-patterns)
- 🖥️ Local-first, BYOK at every layer — native desktop apps for macOS, Windows, Linux AppImage
- 🌍 Composable on three planes — Plugins (runnable workflows) · skills (design taste) · design systems (brand)
- 🔁 Refresh an existing codebase — hand a git repo + `DESIGN.md` to the agent
- 🔒 Privacy by conviction — everything runs where your data lives

| | Claude Design | Figma | Lovable / v0 / Bolt | Open Design |
|---|---|---|---|---|
| Open source | ❌ | ❌ | ❌ | ✅ Apache-2.0 |
| Self-host / desktop | ❌ | ❌ | ❌ | ✅ macOS + Windows + Vercel |
| Agent-native (runs in your CLI) | Anthropic only | ❌ | Cloud agent only | ✅ 21 CLIs + BYOK |
| Brand-grade DESIGN.md | Proprietary | Theme JSON | Limited tokens | ✅ 150 systems shipped |
| Skills / plugins / templates | Closed | Plugin store | Closed | ✅ 100+ skills · 261 plugins |
| HyperFrames (HTML→MP4) | ❌ | ❌ | ❌ | ✅ First-class |

### Quick start

```bash
# Desktop app (recommended — zero config)
# Download from https://open-design.ai or GitHub Releases

# Install into your coding agent (no UI)
curl -fsSL https://open-design.ai/install.sh | sh -s <agent>
# <agent> = claude | codex | cursor | copilot | openclaw | antigravity | gemini
#         | pi | vibe | hermes | cline | kimi | trae | opencode

# Run from source
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable && pnpm install
pnpm tools-dev run web
# Node ~24, pnpm 10.33.x required
```

## Docs

### Agent Adapters (docs/agent-adapters.md)

The adapter layer delegates the entire agent loop — model calls, tool use, context management, permission handling, resume, cancel — to the user's existing code agent CLI. OD's job is to detect it, feed it a skill + prompt + working directory, and stream its output back to the web UI.

Every adapter implements the `AgentAdapter` interface:
- `detect()` — null if not installed
- `capabilities()` — returns `AgentCapabilities` (surgicalEdit, nativeSkillLoading, streaming, resume, permissionMode)
- `run(params)` — `AsyncIterable<AgentEvent>`
- `cancel(runId)`, `resume?(runId, message)`

Detection strategy: run all adapters' `detect()` in parallel on daemon start using PATH scan + config-dir probe. Cache in `~/.open-design/agents.json` with 24h TTL. Re-detect on daemon SIGHUP.

Agent event types: thinking, tool_call, tool_result, text_delta, file_write, error, done.

### Architecture (docs/architecture.md)

Three deployment topologies:

**Topology A — Fully local (default):** browser → Next.js dev server (localhost:3000) → od daemon (Node, port 7456) → spawns claude/codex/cursor. `pnpm tools-dev run web` starts both. Zero config. No accounts.

**Topology B — Web on Vercel + daemon on user's machine:** browser → od.yourdomain.com (Vercel) → ws:// tunnel → od daemon on user's laptop → spawns CLIs. User runs `od daemon --expose` which prints a tunnel URL.

**Topology C — Web on Vercel + direct API:** browser → Vercel serverless → Anthropic Messages API (BYOK stored in browser). No local CLI/daemon. Degraded experience (no filesystem artifacts, no PPTX export).

Component diagram: chat pane + artifact tree + preview iframe + comment/slider overlay — all connected via session bus → transport layer (daemon SSE | api-direct | browser).

## Top-level structure

```
apps/          — Next.js web app + daemon (Node long-running process)
assets/        — shared static assets
charts/        — Helm charts for Kubernetes deployment
craft/         — craft principles content
data/          — data files
deploy/        — Docker Compose + Vercel deployment configs
design-systems/ — 150+ DESIGN.md brand system files
design-templates/ — output templates (HTML/PPT/HyperFrames)
docs/          — architecture, agent-adapters, skills-protocol, modes, roadmap, i18n
e2e/           — end-to-end tests
mocks/         — test mocks
packages/      — shared TypeScript packages
plugins/       — 261 workflow plugins
prompt-templates/ — 93 image prompt templates + 39 Seedance + 11 HyperFrames video templates
scripts/       — build/release scripts
skills/        — 100+ SKILL.md skill files
specs/         — product specs
story/         — Storybook stories
templates/     — project templates
tools/         — dev tooling

AGENTS.md      — agent instruction file
CLAUDE.md      — Claude Code instruction file
QUICKSTART.md  — 3-command quickstart
CHANGELOG.md   — version history
MAINTAINERS.md — Open Design Fellow program
```
