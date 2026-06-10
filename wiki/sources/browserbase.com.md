---
type: source
source_url: https://www.browserbase.com/
companion_urls:
  - https://github.com/browserbase/stagehand
raw_files:
  - ../../raw/web/browserbase.com.md
  - ../../raw/github/browserbase-stagehand.md
tags:
  - browser-automation
  - headless-browser
  - web-agents
  - agent-infrastructure
  - stagehand
  - mcp-integration
  - web-scraping
  - playwright-compatible
related:
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - browse.sh
product: browserbase
detail_level: standard
created: 2026-06-10
updated: 2026-06-10
---

Browserbase is the complete cloud platform for building and deploying AI agents that browse and interact with the web like humans. Rather than stitching together multiple vendors for browsers, search, identity, and model access, Browserbase consolidates everything under one API key — with headless browser fleets at the core and Search, Fetch, Agent Identity, Functions, and a Model Gateway orbiting around them. Trusted by 10,000+ companies including Ramp, Vercel, Commure, and Lovable, the platform handles over 36.9M unique browser sessions with 100K+ developers and 800K weekly SDK downloads.

_All claims below are sourced from ../../raw/web/browserbase.com.md unless otherwise noted._

## What it does

Browserbase gives AI agents reliable access to the 85% of the web that is locked behind anti-bot systems, CAPTCHAs, authentication walls, and dynamic JavaScript — the part traditional fetch/search APIs cannot reach. An agent connects to the platform with a single API key and gets:

- **Headless browser fleets** with concurrent sessions, globally distributed infrastructure, 2 vCPUs per browser, isolated environments, and SOC-2 Type II compliance.
- **Search & Fetch APIs** for token-efficient web data retrieval when a full browser session is not needed.
- **Agent Identity** — a global passport that gets agents past anti-bot systems using cryptographic verification (Cloudflare), real fingerprints (Stytch, Fingerprint), and credential vaults (1Password).
- **Functions** — deploy and run agent code next to the browser with <5ms latency; `bb function deploy` and you're live.
- **Model Gateway** — access major LLMs via Stagehand under one Browserbase API key, with unified billing.
- **Stagehand SDK** — natural language `act()`, `extract()`, `observe()`, and `agent()` primitives that self-heal when pages change and cache repeated actions (up to 2× faster, ~30% cost reduction).

## Key features

- **Session lifecycle management** — create sessions via Sessions API, Functions, or SDK (Node.js, Python, cURL); configure region, viewport, keep-alive, metadata, and concurrency per plan. (../../raw/github/browserbase-stagehand.md)
- **Browser Contexts** — persist cookies, localStorage, IndexedDB, and session storage across sessions; reuse a Context ID with `persist: true` to skip repeated authentication.
- **MCP integration** — Browserbase MCP server exposes browser automation to any MCP client through Stagehand; supports hosted Streamable HTTP or local STDIO deployment. Supports natural language commands like "click the login button."
- **Stagehand action caching** — repeatable actions are cached across runs, eliminating redundant LLM calls; self-heals when pages change without manual selector updates.
- **Observability** — rich logs, live view, and session replay via Session Inspector across every browser session.
- **Framework compatibility** — Playwright, Puppeteer, Selenium for code-first control; Stagehand for AI-native automation; integrations with LangChain, CrewAI, and Mastra.
- **40+ ready-made templates** covering TypeScript, Python, and Go for form filling, MFA handling, scraping, CUA, proxies, and more.

## Architecture

Browserbase is structured as a platform with a browser layer at the center surrounded by supporting primitives: (../../raw/github/browserbase-stagehand.md)

- The **browser fleet** is the core execution environment — isolated Chromium instances in the cloud, accessible via standard WebDriver/CDP APIs.
- **Stagehand** (`packages/core` in the monorepo) wraps the browser with AI primitives; `packages/server-v3` runs as a standalone server; `packages/cli` provides the `bb` command-line tool.
- The **Contexts API** provides stateful session environments; context data is encrypted at rest and persists across session creation/teardown cycles.
- The **Functions** runtime executes agent code co-located with the browser, eliminating network round-trips for actions.
- **Agent Identity** operates through an identity ladder: API keys → credential vaults → signed agents (cryptographic, via Cloudflare Web Bot Auth) → human-verified agents (via AgentKit/Tools for Humanity).

## Installation

Install the SDK: (../../raw/github/browserbase-stagehand.md)

```bash
# Node.js
npm install @browserbasehq/sdk @browserbasehq/stagehand

# Python
pip install browserbase stagehand

# CLI
npx create-browser-app      # scaffold a new project
bb function deploy           # deploy a Function
```

Set `BROWSERBASE_API_KEY` and `BROWSERBASE_PROJECT_ID` in the environment.

## Example usage

```typescript
import { Stagehand } from "@browserbasehq/stagehand";

const stagehand = new Stagehand({ env: "BROWSERBASE" });
await stagehand.init();

const page = stagehand.context.pages()[0];
await page.goto("https://example.com");

// Natural language action
await stagehand.act("click the sign-in button");

// Structured extraction with Zod schema
const { price } = await stagehand.extract(
  "extract the current price",
  z.object({ price: z.string() })
);

// Multi-step autonomous execution
const agent = stagehand.agent();
await agent.execute("Find the cheapest flight to NYC next Friday");
``` (../../raw/github/browserbase-stagehand.md)

## When to use

Use Browserbase when:
- Your agent needs to access login-protected sites, handle CAPTCHAs, or interact with JavaScript-heavy pages that pure fetch/search APIs cannot reach.
- You are building browser agents at scale and need isolated, reproducible, concurrent sessions in the cloud.
- You want to consolidate browsers, identity, search, fetch, model access, and deployment under one vendor and one bill.
- You need production-grade observability (session replay, live view) across automated browser workflows.
- You are building with Playwright, Puppeteer, or Selenium and want to move from local execution to cloud infrastructure without rewriting.

Use the Search & Fetch APIs (not full browser sessions) for token-efficient context retrieval when page interactivity and auth bypass are not required.

## Ecosystem

Browserbase sits at the intersection of browser automation and agentic AI infrastructure. Key ecosystem relationships:

- **Stagehand** (`github.com/browserbase/stagehand`, 23K+ stars, MIT) is the primary open-source SDK and the recommended way to interact with Browserbase from code or agent frameworks.
- **Director** (`director.ai`) is an open-source browser agent reference implementation for visual, "vibe code" agent building on top of Stagehand.
- **browse CLI** provides a lightweight command-line interface for giving agents web browsing capabilities.
- Competes and overlaps with [[microsoft-playwright-mcp]] (MCP-based browser automation) and [[vercel-labs-agent-browser]] (hosted browser infrastructure for agents); Browserbase differentiates on Agent Identity, Stagehand AI primitives, and the unified platform story.
- Integrates with [[browse.sh]] patterns and the broader agent-framework ecosystem ([[crewai.com]], LangChain, Mastra).

## Documentation

Full documentation at `docs.browserbase.com`. Key sections: `introduction/what-is-browserbase`, `fundamentals/create-browser-session`, `features/contexts`, `features/stealth-mode`, `integrations/mcp/introduction`, `reference/introduction`. Stagehand-specific docs at `docs.stagehand.dev`.
