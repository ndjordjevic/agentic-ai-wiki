# irishabh96/phasr

## Metadata
- Stars: 19
- Primary language: TypeScript
- Default branch: master
- Latest release: v0.2.4 (2026-06-22)
- License: MIT
- Homepage: https://phasr.sh
- Fetched: 2026-07-08
- Final URL: https://github.com/irishabh96/phasr

## Description
Desktop workspace for running multiple coding agents in parallel with isolated git worktrees.

## README

# Phasr

**Run multiple coding agents in parallel, each in its own isolated git worktree.**

Phasr is a desktop app that orchestrates concurrent coding-agent sessions
— Claude, Codex, Copilot, Gemini, OpenCode — with per-workspace git
worktrees, live terminal streaming, and an integrated git workflow.

> Pre-1.0, macOS (Apple Silicon) only. Builds are unsigned for now (see Install below). Intel Mac support isn't planned for pre-1.0.

## Screenshots

![Workspace — agent terminal with live streaming output](docs/screenshots/workspace.png)

## Install (macOS, Apple Silicon)

1. Grab the latest DMG from [Releases](https://github.com/irishabh96/phasr/releases) — look for `Phasr_<version>_aarch64.dmg`.

2. Open the DMG and drag **Phasr** to your **Applications** folder.

3. **First launch — Gatekeeper bypass (one-time).** Phasr is not yet code-signed, so macOS will refuse to open it and may show *"Phasr is damaged and can't be opened. You should move it to the Bin."* — the binary is fine, just quarantined. In Terminal, run:

   ```sh
   xattr -dr com.apple.quarantine /Applications/Phasr.app
   ```

   Then double-click Phasr normally. *(On macOS Sequoia and later, Apple removed the right-click → Open bypass dialog for unsigned apps, so the `xattr` command is the only path.)*

   We're working on a signed build for a future release.

## What you'll need

- One or more agent CLIs on your `PATH`. Phasr launches whichever one you choose per workspace.
  - `claude` (Anthropic's Claude Code)
  - `codex` (OpenAI Codex CLI)
  - `copilot` (GitHub Copilot CLI)
  - `gemini` (Google Gemini CLI)
  - `opencode`
- `git`.

You can add or edit agents from **Settings → Agents** inside the app.

## Develop / contribute

Quick start:

```sh
git clone https://github.com/irishabh96/phasr
cd phasr
pnpm install
pnpm tauri dev
```

Set `VITE_CLERK_PUBLISHABLE_KEY`, `VITE_SUPABASE_URL`, and `VITE_SUPABASE_ANON_KEY` in `.env.local` before launching. Phasr requires sign-in and cloud metadata sync. To enable React error reporting and masked Session Replay, also set `VITE_SENTRY_DSN`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full setup, common commands, and PR flow.

## Stack

- **Desktop shell**: Tauri 2 (Rust)
- **Frontend**: React 19 + Vite + Tailwind v4
- **Router / data**: TanStack Router + Query, Zustand
- **Local DB**: SQLite via `sqlx`
- **Terminals**: xterm.js + WebGL renderer, backed by a per-workspace PTY in Rust
- **Auth + cloud sync**: Clerk + Supabase, required at runtime

## Releases

Releases are cut by tagging `v*` on `master`. GitHub Actions builds the Apple Silicon DMG and uploads it as a draft release. See [RELEASING.md](RELEASING.md) for the maintainer flow.

## License

[MIT](LICENSE).

## Docs

### CONTRIBUTING.md (excerpt)

Prerequisites: Node 20+, pnpm 8+, Rust stable, Xcode Command Line Tools.

Quick start:
```sh
git clone https://github.com/irishabh96/phasr
cd phasr
pnpm install
pnpm tauri dev
```

Without cloud credentials, Phasr runs local-only: workspaces live in SQLite, no sign-in screen, no cross-device sync.

Optional cloud sync via `.env.local` with own Clerk + Supabase projects:
- VITE_CLERK_PUBLISHABLE_KEY
- VITE_SUPABASE_URL
- VITE_SUPABASE_ANON_KEY
- VITE_SENTRY_DSN (optional)

Common commands:
```sh
pnpm dev             # Vite dev server only
pnpm tauri dev       # Full desktop app (Rust + React)
pnpm typecheck       # tsc -b --noEmit
pnpm build           # Production web bundle
pnpm tauri build     # Production desktop binary
cargo test --manifest-path src-tauri/Cargo.toml
cargo check --manifest-path src-tauri/Cargo.toml
```

Code layout:
```
phasr/
├─ src/                              React app
│  ├─ routes/                        TanStack Router file routes
│  │  └─ _app/                       Auth-gated layout + nested routes
│  ├─ components/                    UI components
│  ├─ lib/                           Hooks, store, helpers
│  └─ index.css                      Tailwind v4 + design tokens
├─ src-tauri/                        Rust backend
│  ├─ src/
│  │  ├─ commands/                   Tauri command handlers
│  │  ├─ domain/                     Pure types
│  │  ├─ store/                      SQLite repositories
│  │  ├─ pty/                        PTY runtime
│  │  └─ git/                        Worktree + diff helpers
│  ├─ migrations/                    SQLx SQLite migrations
```

## Top-level structure

| Path | Notes |
|---|---|
| `.github/` | CI workflows (release builds) |
| `auth-bridge/` | Auth integration bridge |
| `docs/` | Screenshots and project docs |
| `public/` | Static assets |
| `scripts/` | Build/utility scripts |
| `src/` | React 19 frontend (TanStack Router, components, lib) |
| `src-tauri/` | Tauri 2 Rust backend — commands, domain, store, pty, git, orchestrator, sync |
| `supabase/` | Supabase migrations and cloud schema |
| `CONTRIBUTING.md` | Contributor setup and code layout |
| `RELEASING.md` | Release tagging and DMG build flow |
| `SECURITY.md` | Security policy |
| `package.json` / `pnpm-lock.yaml` | Node dependencies |
| `vite.config.ts` / `vitest.config.ts` | Frontend build and test config |
