---
type: source
category: "Browser & web automation"
source_url: https://github.com/jackwener/opencli
tags:
  - browser-cli
  - chrome-extension
  - site-adapters
  - logged-in-browser
  - agent-browser
  - opencli
  - deterministic-cli
  - browser-bridge
related:
  - vercel-labs-agent-browser
  - microsoft-playwright-mcp
  - browse.sh
  - Tencent-BrowserSkill
  - browser-use.com
  - playwright.dev-agent-cli
  - zenbu-labs-terminal-browser
product: opencli
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

jackwener/opencli (30,698 stars, Apache-2.0; npm `@jackwener/opencli`, homepage opencli.info) turns websites and your logged-in Chrome session into deterministic CLI commands for humans and AI agents. It offers 100+ built-in site adapters, a general-purpose `opencli browser` automation surface positioned as an alternative to [[vercel-labs-agent-browser]], and skills for driving pages and authoring adapters. Browser access goes through a Browser Bridge Chrome extension plus a local daemon, so credentials stay in the browser.

_All claims below are sourced from ../../raw/github/jackwener-opencli.md unless otherwise noted._

## What it does

OpenCLI gives one surface for three kinds of automation: **built-in adapters** for sites such as Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, Twitter/X and LinkedIn; **agent-driven browsing** of any page via `opencli browser` primitives (navigate, state, click, type, fill, extract, screenshot, network) using your logged-in Chrome; and **adapter authoring** with `opencli browser` plus the `opencli-adapter-author` skill (recon → endpoint discovery → auth choice → field decoding → `adapter test`). Agents read pages as structured DOM snapshots rather than screenshots. Commands default to a JSON envelope (`{"ok": true, "data": ...}` or an error with `code`, `message`, `hint`) with logs on stderr, and exit codes follow `sysexits.h` (`66` empty, `69` bridge down, `75` timeout, `77` auth required, `78` config error). The README notes commands themselves invoke no LLM; an orchestrating agent has its own model costs.

## Installation

```bash
npm install -g @jackwener/opencli      # Node.js >= 20.18.1
opencli doctor                         # after installing the Browser Bridge extension
npx skills add jackwener/opencli       # agent skills
```

Desktop users can instead install **OpenCLIApp** (opencli.info/download), which bundles the runtime and a tray UI. The Browser Bridge extension comes from the Chrome Web Store or a manual unpacked release zip. Multiple Chrome profiles can be aliased with `opencli profile list|rename|use`.

## Key features

- **Deterministic adapters** — 100+ sites with structured output schemas; output as `json` (default), `table`, `yaml`, `md` or `csv`, pipeable and CI-friendly.
- **Four skills** — `opencli-browser` (ad-hoc driving), `opencli-adapter-author`, `opencli-autofix` (repair broken adapters), `opencli-usage` (command reference).
- **Named sessions** — page operations require `--session <name>`; tab targeting via `tab list/new/select` and `--tab <targetId>`; `OPENCLI_CLOSE_OWNED_TAB=1` closes temporary tabs.
- **Plugin system** — `opencli plugin install github:user/repo`, with community plugins (Albato, Amap, Goofish, Taobao, Juejin and others) listed.
- **Downloads** — images, video, audio and articles from supported platforms (video needs `yt-dlp`).
- **Remote browsers** — `OPENCLI_CDP_ENDPOINT` for a Chrome DevTools Protocol endpoint; site pooling via `OPENCLI_SITE_SLOTS`.

## Architecture

TypeScript/JS CLI in `src/`, the Chrome Browser Bridge in `extension/`, built-in site adapters in `clis/`, agent skills in `skills/` (the four above plus `smart-search`), and VitePress docs in `docs/` (guide, adapters, advanced, developer, comparison). Also `cases/`, `designs/`, `autoresearch/`, `tests/`, `scripts/`, `cli-manifest.json` and `llms.txt`. Personal adapters live in `~/.opencli/clis/`, and site knowledge persists to `~/.opencli/sites/<site>/`. The daemon auto-starts; status is at `localhost:19825/status`.

## Example usage

```bash
opencli browser open https://example.com --session research
opencli browser state --session research
opencli hackernews top --limit 5
opencli bilibili hot -f csv
opencli browser close --session research
```

## Maintenance status

30,698 GitHub stars, 3,009 forks, Apache-2.0, primary language JavaScript, default branch `main`, latest release v2.0.2 (2026-10-20), most recent push 2026-10-26. The canonical GitHub name is `OpenCLI` (inbox URL `jackwener/opencli` resolves case-insensitively). The v2 line changed CLI syntax and JSON output (e.g. `analyze`/`discover` replaced by `state --diagnostics` and `network --static`). Actively maintained, with a Chinese README, a Chrome Web Store listing and an OpenCLIApp desktop build.
