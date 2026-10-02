---
type: source
category: "Browser & web automation"
source_url: https://www.tapkit.ai/
tags:
  - real-device-automation
  - ios-accessibility-api
  - mcp-server
  - rest-api
  - screenshot-vision-loop
  - bring-your-own-device
related:
  - browser-use.com
  - browserbase.com
  - Tencent-BrowserSkill
product: tapkit
detail_level: standard
created: 2026-10-02
updated: 2026-10-02
---

TapKit turns a real, physical iPhone connected to a Mac into a programmatic API for AI agents, giving agents the same screenshot → act → re-check loop that browser-automation tools provide for the web, but against the real App Store apps, signed-in accounts, and notifications a user already has on their phone — the kind of surface a web API or a simulator can't reach. It matters to this wiki as the mobile-device counterpart to agent-driven browser control tools like [[browser-use.com]] and [[browserbase.com]], extending agentic UI automation from the browser tab to the physical device.

_All claims below are sourced from ../../raw/web/tapkit.ai.md unless otherwise noted._

## What it does

TapKit is bring-your-own-device: a user connects their own iPhone to a Mac running the TapKit app, which exposes the phone as a controllable surface. Agents or scripts send actions — tap, swipe, type, screenshot — and TapKit executes them on the physical device via Apple's accessibility features, with nothing installed on the iPhone itself (no jailbreak, no developer mode). The typical agent loop is screenshot → send to a vision model → get an action → execute on device, repeated until the task is done.

## Key features

- **Real-device control, not a simulator** — simulators can't install or use real App Store apps; TapKit drives an actual iPhone with real accounts, messages, and notifications already signed in.
- **Multiple phones per Mac** — up to seven iPhones from one Mac, with phones shared across a team.
- **Three integration surfaces** — a hosted MCP server, a REST API with a Python SDK, and a Mac/Web app for no-code, human-driven control of the same connected phones.
- **Built-in agent** — the Mac app includes its own chat-driven agent ("Do anything" box) that can carry out a task on the phone directly, in addition to connecting external agents.
- **Human takeover** — a person can watch the agent work on the phone and step in anytime for a login, correction, or any step they want to handle themselves.

## Architecture and concepts

A phone only accepts actions when its Mac app is open, signed in, and the phone is connected, unlocked, and active on the subscription. Every action runs as a job on the phone's Mac: a REST request waits up to 60 seconds by default for the job to finish (or returns immediately with `?async=true` for polling), and failed actions still return HTTP 200 with the error in `result.error` (a `TIMEOUT` job error after 60 seconds). Screenshots are JPEGs scaled so the long edge is at most 1344 pixels, and all tool/action coordinates are pixels in that scaled image measured from the top-left corner — the server maps them back to the phone's native resolution.

## Main APIs

The MCP server (`https://mcp.tapkit.ai/mcp`, Streamable HTTP transport, OAuth 2.1 with PKCE) exposes tools starting with `list_phones` — every other tool takes the `phone_id` it returns: `get_phone_status`, `screenshot`, `tap`, `double_tap`, `triple_tap`, `long_press`, `flick`, `drag`, `hold_and_drag`, `type_text` (US-ASCII, up to 100 characters), `press_key` (with `control`/`shift`/`alternate`/`command` modifiers), and `press_home`. Action tools don't return a screenshot — callers call `screenshot` separately to see the result, and each connection is limited to 300 requests per minute. The REST API (`https://api.tapkit.ai/v1`, authenticated with an `X-API-Key: tk_...` header) exposes the same action set over HTTP for code that isn't using an agent framework, plus job polling via `?async=true` and `/api-reference/get-job`.

## When to use

TapKit targets the gap left by posting/REST APIs and device farms: use a dedicated posting API when a single endpoint covers the whole job, but use TapKit when an authorized agent needs the real mobile app itself — drafts, notifications, account switching, identity verification, or steps that cross multiple apps. It's also positioned against the iOS Simulator (can't run real App Store apps or use real accounts) and against iPhone-mirroring-style MCP setups and hosted device farms, per TapKit's own comparison pages (`/compare/tapkit-vs-appium`, `/compare/tapkit-vs-ios-simulator`, `/compare/tapkit-vs-iphone-mirroring-mcp`, `/compare/tapkit-vs-device-farms`, `/compare/tapkit-vs-posting-apis`).

## Ecosystem

TapKit ships first-party plugins/skills for Claude and Codex/ChatGPT in addition to its generic MCP server, so agents in those tools can be pointed at a connected iPhone directly. The macOS app's auto-update feed lives in a public GitHub repo (`Jootsing-Research/tapkit-releases`), but that repo only hosts the Sparkle appcast and release artifacts — TapKit's core product is closed-source, so no companion repo was ingested. Pricing is $49/month per connected phone (five phones for $245/month), with every plan including the Mac app, web app, API, and agent integrations.
