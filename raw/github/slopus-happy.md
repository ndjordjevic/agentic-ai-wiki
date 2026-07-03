# slopus/happy

## Metadata
- Stars: 22374
- Primary language: TypeScript
- Default branch: main
- Latest release: cli-1.1.10 (2026-06-23)
- License: MIT License
- Homepage: https://happy.engineering
- Fetched: 2026-07-03
- Final URL: https://github.com/slopus/happy

## Description
Mobile and Web client for Codex and Claude Code, with realtime voice, encryption and fully featured

## README
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/.github/logotype-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="/.github/logotype-light.png">
    <img src="/.github/logotype-dark.png" width="400" alt="Happy">
  </picture>
</div>

<h1 align="center">
  Mobile and Web Client for Claude Code & Codex
</h1>

<h4 align="center">
Use Claude Code or Codex from anywhere with end-to-end encryption.
</h4>

<div align="center">
  
[📱 **iOS App**](https://apps.apple.com/us/app/happy-claude-code-client/id6748571505) • [🤖 **Android App**](https://play.google.com/store/apps/details?id=com.ex3ndr.happy) • [🌐 **Web App**](https://app.happy.engineering) • [🎥 **See a Demo**](https://youtu.be/GCS0OG9QMSE) • [📚 **Documentation**](https://happy.engineering/docs/) • [💬 **Discord**](https://discord.gg/fX9WBAhyfD)

</div>

<h3 align="center">
Step 1: Download App
</h3>

<h3 align="center">
Step 2: Install CLI on your computer
</h3>

```bash
npm install -g happy
```

> Migrated from the `happy-coder` package. Thanks to [@franciscop](https://github.com/franciscop) for donating the `happy` package name!

<h3 align="center">
Step 3: Start using `happy` instead of `claude` or `codex`
</h3>

```bash
# Instead of claude, use:
happy claude
# or
happy codex
```

## How does it work?

On your computer, run `happy` instead of `claude` or `happy codex` instead of `codex` to start your AI through our wrapper. When you want to control your coding agent from your phone, it restarts the session in remote mode. To switch back to your computer, just press any key on your keyboard.

## 🔥 Why Happy Coder?

- 📱 **Mobile access to Claude Code and Codex** - Check what your AI is building while away from your desk
- 🔔 **Push notifications** - Get alerted when Claude Code and Codex needs permission or encounters errors  
- ⚡ **Switch devices instantly** - Take control from phone or desktop with one keypress
- 🔐 **End-to-end encrypted** - Your code never leaves your devices unencrypted
- 🛠️ **Open source** - Audit the code yourself. No telemetry, no tracking

## 📦 Project Components

- **[Happy App](https://github.com/slopus/happy/tree/main/packages/happy-app)** - Web UI + mobile client (Expo)
- **[Happy CLI](https://github.com/slopus/happy/tree/main/packages/happy-cli)** - Command-line interface for Claude Code and Codex
- **[Happy Agent](https://github.com/slopus/happy/tree/main/packages/happy-agent)** - Remote agent control CLI (create, send, monitor sessions)
- **[Happy Server](https://github.com/slopus/happy/tree/main/packages/happy-server)** - Backend server for encrypted sync

## 🏠 Who We Are

We're engineers scattered across Bay Area coffee shops and hacker houses, constantly checking how our AI coding agents are progressing on our pet projects during lunch breaks. Happy Coder was born from the frustration of not being able to peek at our AI coding tools building our side hustles while we're away from our keyboards. We believe the best tools come from scratching your own itch and sharing with the community.

## 📚 Documentation & Contributing

- **[Documentation Website](https://happy.engineering/docs/)** - Learn how to use Happy Coder effectively
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute, PR guidelines, and development setup
- **[Edit docs at github.com/slopus/slopus.github.io](https://github.com/slopus/slopus.github.io)** - Help improve our documentation and guides

## License

MIT License - see [LICENSE](LICENSE) for details.

## Docs
### docs/ — internal architecture and protocol references
Key files: `cli-architecture.md`, `backend-architecture.md`, `encryption.md`, `protocol.md`, `happy-wire.md`, `permission-resolution.md`, `deployment.md`, `multi-process.md`

### packages/ — monorepo layout
- `happy-app` — Expo mobile + web UI
- `happy-cli` — wraps Claude Code / Codex, streams encrypted state
- `happy-agent` — remote session control CLI
- `happy-server` — relay server (also published standalone for self-hosting)

## Top-level structure
| Path | Role |
|---|---|
| `.agents/`, `.claude/`, `.codex/` | Agent instruction files for development |
| `.github/` | Logos, CI, community assets |
| `docs/` | Contributor-facing architecture, encryption, protocol specs |
| `environments/` | Deployment environment configs |
| `packages/` | Monorepo: happy-app, happy-cli, happy-agent, happy-server |
| `scripts/` | Build and release automation |
| `AGENTS.md` | Agent instructions for contributors |
| `Dockerfile`, `Dockerfile.server`, `Dockerfile.webapp` | Container builds |
| `pnpm-workspace.yaml` | pnpm monorepo root |
