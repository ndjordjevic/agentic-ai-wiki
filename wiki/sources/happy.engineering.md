---
type: source
source_url: https://happy.engineering/
companion_urls:
  - https://github.com/slopus/happy
raw_files:
  - ../../raw/web/happy.engineering.md
  - ../../raw/github/slopus-happy.md
tags:
  - claude-code
  - mobile-client
  - remote-coding
  - end-to-end-encryption
  - voice-coding
  - relay-server
  - push-notifications
  - multi-session
related:
  - how-claude-code-works-in-large-codebases
  - shareai-lab-learn-claude-code
  - warp.dev
  - tmuxai.dev
  - openvibe.sh
  - codeyai.space
  - gitlawb-openclaude
  - pushover.net
  - app.sauna.ai
product: happy
detail_level: standard
created: 2026-07-03
updated: 2026-07-07
---

Happy Coder is an MIT-licensed, open-source mobile and web client for Claude Code and Codex that runs agents on hardware you own — laptop, desktop, server, or Raspberry Pi — and extends the same terminal session to iOS, Android, and the browser with real-time sync, push notifications, voice-to-action, and end-to-end encryption. With 22k+ GitHub stars and no subscription, it occupies the "lightweight reach extension" niche distinct from cloud VM mobile agents (Cursor Mobile, Terragon) and subscription remote clients (Omnara, CodeRemote).

_All claims below are sourced from ../../raw/web/happy.engineering.md unless otherwise noted._

## What it does

Happy wraps Claude Code (or Codex) via the `happy` CLI (`npm i -g happy`), encrypts terminal state and conversation, and relays it through a dumb relay server so you can monitor, approve, and steer the same session from a phone or web app. The product thesis is not "code on a phone" but **continuous session handoff**: start at your desk, continue planning or issuing commands while away, return to the exact same Claude Code context without export or rebuild. Multiple concurrent sessions across machines are supported; every Claude Code feature available in the terminal (plan mode, custom agents, MCP servers, slash commands) is intended to work through Happy because the CLI is the source of truth.

## Key features

- **Real-time bidirectional sync** — WebSocket connection between CLI and mobile; messages appear on both devices instantly; no primary/secondary device model.
- **Multi-session management** — independent Claude Code sessions per project with isolated context, pause/resume, background preservation.
- **End-to-end encryption** — ChaCha20-Poly1305; QR-based ECDH pairing; relay stores only encrypted blobs; master secret never leaves the phone. (../../raw/github/slopus-happy.md)
- **Offline-resilient relay** — encrypted blob queue survives intermittent mobile connectivity; CLI keeps uploading while phone catches up.
- **Push notifications** — alerts when Claude needs input, hits errors, or finishes work.
- **Voice agent** — Eleven Labs STT + customizable on-phone agent that translates spoken rambling into structured Claude Code prompts (not just dictation).
- **Permission prompts on mobile** — intercept MCP tool calls and file edits for Allow/Deny before execution when away from desk.
- **Self-hostable relay** — ~1,300-line TypeScript server (`happy-server`), Docker/Kubernetes deploy, `HAPPY_SERVER_URL` override.
- **Zero cloud agent cost** — uses your Claude Code/Codex subscription and your machines; Happy itself is free.

## Architecture

Three components: **happy-cli** (wraps Claude Code/Codex, serializes terminal state, encrypts outbound), **happy-app** (Expo mobile + web UI, decrypts and renders), **happy-server** (relay — forwards encrypted messages, cannot decrypt). (../../raw/github/slopus-happy.md)

Monorepo packages: `packages/happy-app`, `happy-cli`, `happy-agent` (remote session control CLI), `happy-server`. Contributor docs specify keeping the relay "dumb" — business logic lives in the mobile app; CLI exposes a generic run-command-and-report API.

Authentication uses zero round-trip challenge-response: device signs a random challenge with its key pair; server verifies and stores only a hash of the public key as channel ID. Encrypted blobs are persisted for session history and disconnect tolerance.

## Installation

```bash
npm install -g happy   # Node.js 18+
happy --auth           # QR code to pair mobile app
happy claude           # or: happy codex
```

Mobile: iOS App Store, Google Play, or web at `app.happy.engineering`. (../../raw/github/slopus-happy.md)

## Example usage

```bash
# Pair phone to desktop once
happy --auth

# Start Claude Code through Happy wrapper
happy claude

# Switch to phone — same session continues remotely
# Press any key on keyboard to reclaim desktop control
```

Typical workflow from docs: plan a feature on phone during commute → review generated diffs at desk in the same session → optionally seed overnight tasks via voice or mobile planning before sleep, wake to push notification with files ready for review.

## When to use

Choose Happy when you already run Claude Code locally, want mobile visibility and steering without adopting a cloud sandbox workflow, care about E2E encryption and self-hosting, or need voice + push notifications while away from the keyboard. Mobile fits planning, momentum, and coarse-grained direction; desktop remains essential for multi-file review and precise editing — Happy optimizes the **handoff between those modes**, not replacement of the desk setup.

## Maintenance status

22,374 GitHub stars, 1,862 forks, TypeScript monorepo, MIT license, active development (pushed 2026-07-03). Latest CLI release: `cli-1.1.10` (2026-06-23). Documentation site at happy.engineering/docs; community Discord linked from README. (../../raw/github/slopus-happy.md)

## Ecosystem

Positioned against Omnara, ClaudeCodeUI, Cursor Mobile, Terragon, CodeRemote, SSH+tmux, and Kisuke — Happy's differentiators are MIT licensing, no subscription, local agent execution (full MCP/custom agents), E2E encryption on the community relay, and native mobile UX with voice. Complements [[how-claude-code-works-in-large-codebases]] harness patterns (CLAUDE.md, MCP, skills) because agents run on your existing configured machine. Overlaps [[warp.dev]] and [[tmuxai.dev]] in terminal-adjacent agent access but targets mobile session sync rather than in-terminal pair programming or tmux pane observation.
