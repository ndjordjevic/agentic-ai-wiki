# BloopAI/vibe-kanban

## Metadata
- Stars: 26494
- Primary language: Rust
- Default branch: main
- Latest release: v0.1.44 (2026-04-24)
- License: Apache License 2.0
- Homepage: https://www.vibekanban.com/
- Fetched: 2026-05-25
- Final URL: https://github.com/BloopAI/vibe-kanban

## Description
Get 10X more out of Claude Code, Codex or any coding agent

## README
<p align="center">
  <a href="https://vibekanban.com">Vibe Kanban</a>
</p>

<p align="center">Get 10X more out of Claude Code, Gemini CLI, Codex, Amp and other coding agents...</p>

**Vibe Kanban is sunsetting.** [Read the announcement.](https://www.vibekanban.com/blog/shutdown)

## Overview

In a world where software engineers spend most of their time planning and reviewing coding agents, the most impactful way to ship more is to get faster at planning and review.

Vibe Kanban is built for this. Use kanban issues to plan work, either privately or with your team. When you're ready to begin, create workspaces where coding agents can execute.

- **Plan with kanban issues** — create, prioritise, and assign issues on a kanban board
- **Run coding agents in workspaces** — each workspace gives an agent a branch, a terminal, and a dev server
- **Review diffs and leave inline comments** — send feedback directly to the agent without leaving the UI
- **Preview your app** — built-in browser with devtools, inspect mode, and device emulation
- **Switch between 10+ coding agents** — Claude Code, Codex, Gemini CLI, GitHub Copilot, Amp, Cursor, OpenCode, Droid, CCR, and Qwen Code
- **Create pull requests and merge** — open PRs with AI-generated descriptions, review on GitHub, and merge

One command. Describe the work, review the diff, ship it.

```bash
npx vibe-kanban
```

## Installation

Make sure you have authenticated with your favourite coding agent. A full list of supported coding agents can be found in the [docs](https://vibekanban.com/docs/supported-coding-agents). Then in your terminal run:

```bash
npx vibe-kanban
```

## Documentation

Head to the [website](https://vibekanban.com/docs) for the latest documentation and user guides.

## Self-Hosting

Want to host your own Vibe Kanban Cloud instance? See our [self-hosting guide](https://vibekanban.com/docs/self-hosting/deploy-docker).

## Support

We use [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) for feature requests. Please open a discussion to create a feature request. For bugs please open an issue on this repo.

## Contributing

We would prefer that ideas and changes are first raised with the core team via [GitHub Discussions](https://github.com/BloopAI/vibe-kanban/discussions) or [Discord](https://discord.gg/AC4nwVtJM3), where we can discuss implementation details and alignment with the existing roadmap.

## Development

### Prerequisites

- Rust (latest stable)
- Node.js (>=20)
- pnpm (>=8)

Additional development tools:
```bash
cargo install cargo-watch
cargo install sqlx-cli
```

Install dependencies:
```bash
pnpm i
```

### Running the dev server

```bash
pnpm run dev
```

This will start the backend and web app. A blank DB will be copied from the `dev_assets_seed` folder.

### Building the web app

```bash
cd packages/local-web
pnpm run build
```

### Build from source (macOS)

1. Run `./local-build.sh`
2. Test with `cd npx-cli && node bin/cli.js`

### Environment Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `POSTHOG_API_KEY` | Build-time | Empty | PostHog analytics API key |
| `POSTHOG_API_ENDPOINT` | Build-time | Empty | PostHog analytics endpoint |
| `PORT` | Runtime | Auto-assign | Server port |
| `BACKEND_PORT` | Runtime | 0 (auto-assign) | Backend server port (dev mode) |
| `FRONTEND_PORT` | Runtime | 3000 | Frontend dev server port (dev mode) |
| `HOST` | Runtime | 127.0.0.1 | Backend server host |
| `MCP_HOST` | Runtime | Value of HOST | MCP server connection host |
| `MCP_PORT` | Runtime | Value of BACKEND_PORT | MCP server connection port |
| `DISABLE_WORKTREE_CLEANUP` | Runtime | Not set | Disable git worktree cleanup |
| `VK_ALLOWED_ORIGINS` | Runtime | Not set | Allowed CORS origins for reverse proxy / custom domain |
| `VK_SHARED_API_BASE` | Runtime | Not set | Base URL for the remote/cloud API |
| `VK_SHARED_RELAY_API_BASE` | Runtime | Not set | Base URL for the relay API |
| `VK_TUNNEL` | Runtime | Not set | Enable relay tunnel mode |

**Self-Hosting with a Reverse Proxy:** Set `VK_ALLOWED_ORIGINS` to the full origin URL(s) where the frontend is accessible, e.g. `VK_ALLOWED_ORIGINS=https://vk.example.com`.

## Top-level structure
- `.cargo/` — Rust toolchain config
- `.github/` — CI/CD workflows (publish.yml)
- `AGENTS.md` — agent instruction file
- `CLAUDE.md` — Claude Code instruction file
- `CODE-OF-CONDUCT.md` — community standards
- `Caddyfile.example` — reverse proxy example config
- `Cargo.toml` / `Cargo.lock` — Rust workspace manifest
- `Dockerfile` — container build
- `README.md` — project overview
- `assets/` — static assets
- `crates/` — Rust source crates (core backend logic)
- `dev_assets_seed/` — blank DB for dev
- `docs/` — documentation source
- `local-build.sh` — macOS build script
- `LICENSE` — Apache License 2.0
