---
type: source
source_url: https://open-design.ai/
companion_urls:
  - https://github.com/nexu-io/open-design
raw_files:
  - ../../raw/web/open-design.ai.md
  - ../../raw/github/nexu-io-open-design.md
tags:
  - local-first
  - byok
  - agent-native-design
  - claude-design-alternative
  - skill-md
  - design-systems
  - mcp-server
  - open-source
related:
  - skills.sh
  - anthropics-skills
  - obra-superpowers
  - lovable.dev
product: open-design
detail_level: standard
created: 2026-06-09
updated: 2026-07-01
---

Open Design (open-design.ai, 62,118 GitHub stars, Apache-2.0, v0.9.0) is the open-source, local-first alternative to Claude Design — a complete agent-native design platform that turns any coding agent CLI (Claude Code, Codex, Cursor, Gemini CLI, 21+ others) into a design engine via composable SKILL.md skills and portable DESIGN.md brand systems. It is both a native desktop app (macOS, Windows, Linux AppImage) and a filesystem-first toolkit that generates HTML, PDF, PPTX, MP4, and HyperFrame artifacts — without locking output into a vendor cloud. The project was created in direct response to Anthropic's Claude Design launch in April 2026 and positions itself as the open-source, self-hostable, multi-agent equivalent. (../../raw/github/nexu-io-open-design.md)

_All claims below are sourced from ../../raw/web/open-design.ai.md unless otherwise noted._

## What it does

Open Design implements the same four-stage artifact-first loop that Claude Design introduced — Detect → Discover → Direct → Deliver — but replaces the closed system with a filesystem of SKILL.md skills, DESIGN.md brand systems, and workflow plugins that any supported agent can read, write, and remix. The `od` CLI and daemon run locally on the user's machine; artifacts land in the project directory rather than vendor infrastructure. The result is a design engine where the coding agent already installed on the developer's laptop — not a proprietary cloud runtime — is the creative executor.

At `standard` detail this ingest captured the landing page, docs overview, quickstart, agents catalog, skills catalog, and compare hub.

## Key features

- **155 SKILL.md skills** covering scenario (new generation, Figma migration, code migration, plugin authoring), export (Next.js, React, Vue 3), utility (brief parsing, PPTX-HTML fidelity audit, GitHub repo creation), and design plugins
- **150+ portable DESIGN.md brand systems** — Linear, Vercel, Stripe, Apple, Cursor, Figma, Anthropic, Tesla, Notion, Supabase and more — loaded automatically by the daemon at startup
- **261 workflow plugins** installable from the plugin catalog
- **21+ coding-agent adapters** with Tier 1 first-party support (Claude Code, Codex, Cursor Agent, Gemini CLI, GitHub Copilot CLI, OpenCode, Qwen) and Tier 2/3 support for Grok, Hermes, Kimi CLI, Devin, DeepSeek, Pi, Mistral Vibe, Kiro, Kilo, Qoder, Cline, Trae, Antigravity, OpenClaw; install via `od mcp install <agent>` (../../raw/github/nexu-io-open-design.md)
- **BYOK at every layer** — credentials stored locally; direct API calls from user machine to providers; provider switch requires only a credential swap
- **HyperFrames** — HTML+CSS+GSAP motion graphics rendered to deterministic MP4 via headless Chrome + FFmpeg, with Seedance 2.0, Veo 3, Kling 2, Suno v5, and Lyria 2 integration
- **93 image prompt templates** and 11 HyperFrames video templates shipped with the repo
- **MCP server** exposed via `od mcp install <agent>` — runs a daemon at localhost:7456 (or 17456 in dev mode) serving skills, design systems, and plugins to any MCP-compatible agent

## Architecture

The architecture separates three deployment topologies: **Topology A** (fully local — Next.js dev server + od daemon + agent CLI, all on the user's machine), **Topology B** (web UI on Vercel, daemon on user's machine connected via cloudflared tunnel), and **Topology C** (web UI on Vercel + direct Anthropic API, no daemon, degraded — no filesystem artifacts). (../../raw/github/nexu-io-open-design.md)

The adapter layer is the core design decision: every coding agent CLI implements an `AgentAdapter` interface with `detect()`, `capabilities()`, and `run()`. Detection runs all adapters in parallel on daemon start via PATH scan + config-dir probe and caches results in `~/.open-design/agents.json` with a 24h TTL. Agent event types are `thinking`, `tool_call`, `tool_result`, `text_delta`, `file_write`, `error`, and `done`. The daemon accepts requests in each provider's native format; SSRF protection blocks internal IPs and link-local ranges at the edge. (../../raw/github/nexu-io-open-design.md)

The web app has four panes — chat, artifact tree, preview iframe (sandboxed), and comment/slider overlay — connected via an in-memory session bus. The transport layer supports daemon SSE, api-direct, and browser modes depending on topology. (../../raw/github/nexu-io-open-design.md)

## Installation

```bash
# Desktop app (recommended — zero config, auto-detects all CLIs on $PATH)
# Download from https://open-design.ai or GitHub Releases
# macOS (Apple Silicon + Intel), Windows x64, Linux AppImage

# Install into coding agent (no UI)
curl -fsSL https://open-design.ai/install.sh | sh -s <agent>
# <agent> = claude | codex | cursor | copilot | openclaw | antigravity | gemini
#           | pi | vibe | hermes | cline | kimi | trae | opencode

# Run from source (Node ~24, pnpm 10.33.x — Node 22 not supported)
git clone https://github.com/nexu-io/open-design.git
cd open-design && corepack enable && pnpm install
pnpm tools-dev run web

# Docker
docker compose up -d  # in deploy/ directory; serves on http://localhost:7456
```
(../../raw/github/nexu-io-open-design.md)

## Example usage

Once installed, inside Claude Code or any supported agent:

```
> Use open-design to generate a landing page with the Linear design system
```

The agent reads `skills/`, picks the right `SKILL.md`, binds the named `DESIGN.md`, and emits an `<artifact>` previewable at `http://localhost:7456`. The workflow is: pick a skill and design system → type the brief in the entry view → artifact streams into a sandboxed iframe → edit inline or export HTML/PDF/PPTX/ZIP/Markdown. (../../raw/github/nexu-io-open-design.md)

Adding a new coding agent adapter is one entry in `apps/daemon/src/agents.ts`; the adapter spec and stdio transport contract are in `docs/new-agent-runtime-acp.md`. (../../raw/github/nexu-io-open-design.md)

## When to use

Open Design fits when the team needs agent-generated design artifacts — prototypes, dashboards, decks, images, or HyperFrame video — with a specific brand identity (DESIGN.md) applied consistently across runs, without sending work to a hosted vendor cloud. It is the right choice over Claude Design when self-hosting, multi-agent support, or open-source extensibility is required; over Figma when pixel-less, agent-driven artifact output is preferred; over v0/[[lovable.dev]]/Bolt when local execution and BYOK economics matter. It requires a local daemon plus at least one supported coding agent CLI.

## Maintenance status

62,118 stars, Apache-2.0, v0.9.0 (latest release 2026-06-02), active development with pushes as of 2026-06-09. The Open Design Fellow program is open for community contributors; `MAINTAINERS.md` covers details. Discord at discord.gg/qhbcCH8Am4 for community support. 6,950 forks. Primary language: TypeScript. (../../raw/github/nexu-io-open-design.md)

## Ecosystem

Open Design references several projects in this wiki: [[skills.sh]] is the distribution platform through which OD skills are installable via `npx skills`; [[anthropics-skills]] is the upstream Claude Skills ecosystem OD's SKILL.md format follows; [[obra-superpowers]] is the methodology layer built on the same SKILL.md pattern. Pi (earendil-works) is listed as a Tier 2 supported agent. The project acknowledges Open CoDesign as a sibling open-source project compatible through OD's skill protocol.

Related GitHub repositories mentioned in the source: `github.com/nexu-io/open-design` (primary), `github.com/heygen-com/hyperframes` (HyperFrames video framework, integrated as first-class citizen), `github.com/multica-ai/multica` (inspiration for PATH-scan detection + daemon architecture), `github.com/farion1231/cc-switch` (inspiration for per-agent config format + symlink skill distribution).

## Documentation

The `docs/` directory in the companion repo covers architecture, agent-adapters, skills-protocol, modes, plugins-spec, roadmap, deployment (Docker + Vercel), i18n (13 languages), and testing. The `QUICKSTART.md` provides a three-command path for source installs. The open web entry points are at https://open-design.ai/docs/, with the quickstart at https://open-design.ai/quickstart/ and agent catalog at https://open-design.ai/agents/.
