---
type: source
source_url: https://browser-use.com/
companion_urls:
  - https://github.com/browser-use/browser-use
raw_files:
  - ../../raw/web/browser-use.com.md
  - ../../raw/github/browser-use-browser-use.md
tags:
  - browser-automation
  - web-agents
  - stealth-browser
  - mcp-integration
  - llm-agents
  - python-sdk
  - cloud-agent
  - playwright-alternative
related:
  - abacus.ai
  - browserbase.com
  - microsoft-playwright-mcp
  - elevenlabs.io
  - marketstack.com
  - firecrawl.dev
  - integuru.com
product: browser-use
detail_level: standard
created: 2026-06-15
updated: 2026-07-06
---

Browser Use is a cloud platform and open-source Python SDK (≈99k GitHub stars) that enables LLMs to autonomously interact with websites using natural language. It provides a self-healing browser harness, stealth Chromium infrastructure, custom models optimized for browser tasks, managed residential proxies, and an MCP server that connects browser automation to Claude, Cursor, Windsurf, and other coding assistants.

_All claims below are sourced from ../../raw/web/browser-use.com.md unless otherwise noted._

## What it does

Browser Use lets AI agents drive a real browser — clicking, typing, navigating, extracting data, submitting forms, handling authentication — through natural language task descriptions. The platform has two deployment modes:

- **Cloud SDK** (`browser-use-sdk`) — fully managed agents running on Browser Use's infrastructure with CAPTCHA solving, anti-detect Chromium, and 195+ country residential proxies. New accounts receive 5 free tasks.
- **Open-source SDK** (`browser-use` Python package) — self-hosted automation; the v0.13 beta introduces a Rust core (`from browser_use.beta import Agent`) for lower latency and a persistent tool loop modeled on coding agents. Legacy `from browser_use import Agent` still supported.

Both modes share `ChatBrowserUse` as the recommended inference backend — an in-house model completing tasks 3–5× faster than general-purpose LLMs with SOTA benchmark accuracy.

## Key features

**Cloud SDK:**
- Natural language task specification; no explicit browser scripting required
- Structured output — validated, typed data returned from tasks
- Follow-up tasks — chain commands within a single browser session
- Live messages streaming — real-time agent reasoning for custom UIs
- Human-in-the-loop — pause for approvals, payments, or complex auth flows
- Workspaces and files — upload/download files to/from agent sessions
- Authentication profiles — persist cookies and localStorage; sync local browser state to cloud
- 1,000+ service integrations (Gmail, Slack, Notion, Calendar, and more)

**Open-source SDK:** (../../raw/github/browser-use-browser-use.md)
- Custom tools via `@tools.action` decorator for extending agent capabilities (../../raw/github/browser-use-browser-use.md)
- CLI for persistent, scriptable browser control between commands (../../raw/github/browser-use-browser-use.md)
- Template quickstart (`uvx browser-use init --template default|advanced|tools`) (../../raw/github/browser-use-browser-use.md)
- Code agent mode for Python-generating workflows
- Lifecycle hooks for intercepting agent behavior
- Parallel browser execution for multi-agent runs

## Architecture

The open-source agent's execution model: (../../raw/github/browser-use-browser-use.md)

```
Python API -> Rust core -> Browser harness -> Web task done
```

The v0.13 Rust-powered beta agent introduces a persistent tool loop with recovery cycles inspired by coding agents. Key classes: `Agent` (task executor), `BrowserProfile` (browser instance configuration), `ChatBrowserUse` / `ChatOpenAI` / `ChatAnthropic` / `ChatGoogle` (LLM adapters). (../../raw/github/browser-use-browser-use.md)

The cloud agent wraps the v3 REST API (`api.browser-use.com`), exposing `client.sessions`, `client.browsers`, `client.profiles`, `client.workspaces`, and `client.billing`. `client.run()` initiates a session that polls for completion within a 4-hour window.

Pydantic v2 models are used for all internal action schemas, task inputs/outputs, and tools I/O, ensuring robust validation and LLM-call integrity. (../../raw/github/browser-use-browser-use.md)

## Installation

**Cloud SDK (Python):**
```bash
pip install --upgrade browser-use-sdk
export BROWSER_USE_API_KEY=bu_your_key_here
```

**Cloud SDK (TypeScript):**
```bash
npm install browser-use-sdk@latest
```

**Open-source SDK:** (../../raw/github/browser-use-browser-use.md)
```bash
uv add "browser-use[core]"   # Python ≥ 3.11; [core] installs Rust runtime
uvx browser-use install       # Downloads Chromium
browser                        # CLI entrypoint
```

**MCP server (Claude Code):**
```bash
claude mcp add -t http -H "x-browser-use-api-key: YOUR_API_KEY" browser-use https://api.browser-use.com/v3/mcp
```

**Claude Code skill (open-source):** (../../raw/github/browser-use-browser-use.md)
```bash
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

## Example usage

**Open-source agent (v0.13 beta):** (../../raw/github/browser-use-browser-use.md)
```python
from browser_use.beta import Agent, BrowserProfile, ChatBrowserUse
import asyncio

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(model='openai/gpt-5.5'),
        browser_profile=BrowserProfile(headless=False),
    )
    history = await agent.run()
    print(history.final_result())

asyncio.run(main())
```

**Custom tool extension:** (../../raw/github/browser-use-browser-use.md)
```python
from browser_use import Tools

tools = Tools()

@tools.action(description='Fetch the current stock price for a ticker symbol.')
def get_stock_price(ticker: str) -> str:
    # ... custom implementation
    return f"Price: $42.00"

agent = Agent(task="Check AAPL price and compare to S&P 500", llm=llm, tools=tools)
```

**Cloud SDK task via `client.run()`:**
```python
from browser_use_sdk.v3 import AsyncBrowserUse
import asyncio

async def main():
    async with AsyncBrowserUse() as client:
        result = await client.run("List the top 20 posts on Hacker News with their points")
        print(result)

asyncio.run(main())
```

**Production deployment using `@sandbox()`:**
```python
from browser_use import sandbox, Browser, Agent, ChatBrowserUse

@sandbox(cloud_proxy_country_code="US", cloud_timeout=30)
async def run_task(browser: Browser):
    agent = Agent(task="Fill out this job application form", llm=ChatBrowserUse(), browser=browser)
    return await agent.run()
```

## When to use

Use **Browser Use Cloud** when:
- Complex, multi-step tasks requiring CAPTCHA solving, anti-bot bypass, or geo-specific proxies
- Production workflows needing persistent auth profiles, 1,000+ service integrations, and uptime guarantees
- Fastest results matter: cloud agent outperforms open-source on complex tasks (per BU Bench V1)

Use **Open-source SDK** when:
- Deep code-level integration or custom tool extension is required
- Self-hosting is a constraint (privacy, cost, compliance)
- Pairing with `Browser(use_cloud=True)` for stealth/proxy benefits while keeping the agent local

## Maintenance status

Actively maintained. (../../raw/github/browser-use-browser-use.md)
- Stars: ~98,869 (as of 2026-06-15), 11k+ forks (../../raw/github/browser-use-browser-use.md)
- Latest release: v0.13.2 (2026-06-12) — introduces Rust core beta (../../raw/github/browser-use-browser-use.md)
- License: MIT (../../raw/github/browser-use-browser-use.md)
- Primary language: Python (../../raw/github/browser-use-browser-use.md)
- SOC 2 Type II compliant (cloud platform)
- Open benchmark: github.com/browser-use/benchmark — 100 real-world browser tasks

## Ecosystem

- **MCP Server** — 7 tools for task execution, session monitoring, follow-up commands, and browser profile management; connects to Claude, Cursor, Windsurf via HTTP
- **n8n integration** — Browser Use as an HTTP node in n8n workflows
- **Playwright/Puppeteer/Selenium CDP** — connect existing automation frameworks to Browser Use's stealth infrastructure
- **Marketplace** — pre-built automation skills for common website patterns
- **Community** — Discord, X (@browser_use)
- **Comparable tools:** [[browserbase.com]] (alternative managed browser infrastructure with Stagehand SDK); [[microsoft-playwright-mcp]] (MCP server for Playwright-based browser control)

## Documentation

Cloud docs: `docs.browser-use.com/cloud/` (quickstart, agent, browser, auth, integrations, tutorials, API v3). Open-source docs: `docs.browser-use.com/` (quickstart, customize, production, supported models). Complete SDK reference for LLMs: `docs.browser-use.com/llms-full.txt`.
