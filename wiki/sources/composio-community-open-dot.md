---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/composio-community/open-dot
tags:
  - personal-agent-desktop-app
  - computer-use
  - composio-integrations
  - approval-rules
  - scheduled-routines
  - trigger-driven-agents
  - openrouter-open-models
  - encrypted-password-vault
related:
  - openrouter.ai
  - felix-forever-hermes-agent-desktop
  - omnigent-ai-omnigent
  - browserbase.com
  - vercel-labs-agent-browser
product: open-dot
detail_level: standard
created: 2026-10-02
updated: 2026-10-02
---

Open Dot is an open-source, self-hostable reimplementation of OpenAI's "Dots" personal agents — background agents that run continuously on your own Mac with your own OpenAI key (or open models like Kimi, DeepSeek and Qwen via OpenRouter) instead of requiring ChatGPT Pro/Business. It packages a full personal-agent stack — persistent browser sessions, app integrations, approval rules, scheduling, triggers, voice, and encrypted credentials — as a single Electron desktop app.

_All claims below are sourced from ../../raw/github/composio-community-open-dot.md unless otherwise noted._

## What it does
Each "dot" is a long-running personal agent with its own persistent, logged-in browser session that the user can watch and take over (e.g. for captchas or logins) via a Computer tab. Dots connect to Gmail, Calendar, Slack, Notion, GitHub, and 1,500+ other apps through [Composio](https://composio.dev), read data autonomously, but ask permission before sending, posting, paying, or changing anything. Passwords are encrypted via the macOS Keychain and typed directly into pages so the model never sees plaintext credentials. Users can call a dot and talk to it; requested work continues after hangup and the call transcript appears in the chat. Dots can be scheduled (e.g. a daily 8am inbox/calendar brief) or woken by Composio triggers (new email, new GitHub issue, etc.), and multiple dots can hand off work to each other, each keeping its own memory and reusable skills.

## Installation
Distributed as a desktop app: `pnpm install && pnpm desktop:build` produces an unsigned `.dmg` (first launch requires right-click → Open, since the build isn't notarized). Running from source needs Node 22+, pnpm, and Google Chrome (or Playwright's bundled Chromium): `cp .env.example .env.local`, `pnpm install`, `npx playwright install chromium`, then `pnpm dev` (serves at `localhost:3100`) with optional `pnpm desktop:dev` to open the Electron window on top. Configuration — OpenAI/OpenRouter/Composio/E2B API keys, model selection (`DOTS_MODEL`, `DOTS_REVIEW_MODEL`, `DOTS_VOICE_MODEL`), and the compute backend (`DOTS_COMPUTER`: cloud/docker/local) — is set via environment variables or pasted directly into the app's Settings.

## Key features
- **Persistent, takeover-able browser** per dot, with a live Computer-tab view.
- **Encrypted password vault** keyed to the macOS Keychain, filled directly into page fields.
- **Composio integration layer** for 1,500+ third-party apps (Gmail, Slack, Notion, GitHub, etc.), covering both read access and gated write actions.
- **Rule-based approval system**: a small review model checks each risky action against user-authored rules (e.g. "ask before replying to email") and surfaces an approve/deny card in the chat.
- **Voice calls** via OpenAI Realtime, with call transcripts merged into the regular text chat so work continues after hangup.
- **Scheduling and triggers**: routines run on a schedule; Composio triggers wake a dot on app events, though both only fire while the app is open (asleep Macs skip due routines/trigger events).
- **Multi-dot collaboration**: separate dots with distinct jobs can pass work to each other, and each accumulates its own memory and reusable "skills."
- **Pluggable execution backend**: dot code runs via an E2B cloud computer, a local Docker container, or a local folder on the Mac, selected automatically or forced via `DOTS_COMPUTER`.

## Architecture
The desktop shell (`electron/main.mjs`) starts a local Next.js server and opens the window, routing external links to the system browser; `scripts/desktop-*.mjs` pack the Next.js server into the packaged app. The agent core lives under `src/server/agent/`: `runtime.ts` runs the streaming Responses-API loop with a thread per chat and approval cards that pause/resume execution; `tools.ts` defines the dot's tools and each one's risk level; `review.ts` checks a proposed action against user rules; `prompt.ts` rebuilds the system prompt every turn from rules, memory, skills, and routines; `openrouter.ts` adds OpenRouter-routed open models, maintaining chat history app-side since OpenRouter itself is stateless. `src/server/computer/` abstracts over E2B cloud computers, Docker containers, and local folders, with `browser.ts` managing each dot's Chrome profile, computer-use actions, and the live/takeover view. Supporting modules: `composio.ts` (OAuth sign-in and app connections), `triggers.ts` (Composio trigger event stream), `voice.ts` (OpenAI Realtime calls), `vault.ts` (encrypted password store), `scheduler.ts` (routines), and `repo.ts`/`db.ts` (SQLite via `node:sqlite`). `src/app/api/events` streams live updates to the window's UI, which reads state via `useSyncExternalStore` (`src/lib/store.ts`). Dots use OpenAI's built-in `web_search` and `computer` tools (or OpenRouter's web search for open models); every other capability is a function tool, so any action can be routed through the approval rules first.

## Example usage
```bash
# from source
cp .env.example .env.local   # add OPENAI_API_KEY, or paste it in Settings later
pnpm install
npx playwright install chromium
pnpm dev                     # http://localhost:3100
pnpm desktop:dev             # optional: opens the desktop window on top of pnpm dev

# packaged app
pnpm install
pnpm desktop:build           # produces dist/Open Dot-<version>-arm64.dmg
```
In development, chats, the password vault, browser profiles, and workspaces are kept under `.data/`; in the packaged app they live in `~/Library/Application Support/Open Dot`.

## When to use
Fits users who want an always-on, self-hosted personal agent on their own Mac — handling inbox/calendar briefs, routine app actions, and multi-step tasks across many integrated services — without paying for ChatGPT Pro/Business or trusting a hosted vendor with Keychain-protected credentials. Not intended for multi-user or public-server deployment: there is no login screen, and routines/triggers only run while the app itself stays open (sleeping Macs skip due events).

## Maintenance status
396 stars, 43 forks, pushed as recently as 2026-09-30; no tagged releases and no license file at the time of this fetch. Actively developed (repo created the same week as OpenAI's "Dots" launch on 2026-09-29), with README explicitly noting the project "isn't affiliated with OpenAI."

## Ecosystem
Built on the OpenAI Responses API (model default e.g. `gpt-5.5`, review model `gpt-5.4-mini`, voice model `gpt-realtime-2.1`) with optional [[openrouter.ai|OpenRouter]] routing to open models (Kimi, DeepSeek, Qwen, GLM) that lack OpenAI's native computer-use tool and instead click/type by on-page text. App connectivity and triggers run through Composio (1,500+ app integrations); sandboxed/cloud code execution is optional via [E2B](https://e2b.dev); the UI is a Next.js app packaged with Electron; browser automation uses Playwright against the user's installed Chrome. Conceptually adjacent to other desktop personal-agent shells such as [[felix-forever-hermes-agent-desktop]] and multi-agent orchestration platforms like [[omnigent-ai-omnigent]], and shares the "agent drives a real browser session" model with browser-automation infrastructure such as [[browserbase.com]] and [[vercel-labs-agent-browser]].
