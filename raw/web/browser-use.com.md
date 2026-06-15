# browser-use.com

## Fetch log
- Inbox URL: https://browser-use.com/
- Final URL: https://browser-use.com/
- Fetched: 2026-06-15
- Pages: 11
- Mode: standard

## llms.txt — https://browser-use.com/llms.txt
# Browser Use

> Browser Use is a cloud platform and open-source SDK that enables AI agents to autonomously interact with websites using natural language. It provides web agents, stealth browser infrastructure, custom LLMs optimized for browser automation, managed proxies, and skills that turn any website into a reliable API endpoint.

## Cloud SDK

> The most SOTA browser agent and the most scalable browser infrastructure. Built on the largest AI browser automation open-source library on GitHub with almost 100k stars. Web scraping, data extraction, form filling, and headless browser automation via natural language. Anti-detection, CAPTCHA solving, residential proxies. Alternative to Playwright, Puppeteer, and Selenium for AI-powered automation.

- GitHub: https://github.com/browser-use/browser-use
- Dashboard: https://cloud.browser-use.com
- API key: https://cloud.browser-use.com/settings?tab=api-keys&new=1
- Open Source: https://github.com/browser-use/browser-use
- Docs: https://docs.browser-use.com
- OpenAPI spec (v3): https://docs.browser-use.com/cloud/openapi/v3.json
- Chat UI example: https://docs.browser-use.com/cloud/tutorials/chat-ui — Full end-to-end example with live browser, streaming, auth. Best starting point to build a prototype.
- Stealth benchmark: https://browser-use.com/posts/stealth-benchmark
- Agent benchmark (online Mind2Web): https://browser-use.com/posts/online-mind2web-benchmark
- Blog: https://browser-use.com/posts

**Use v3** (`from browser_use_sdk.v3 import AsyncBrowserUse` / `import { BrowserUse } from "browser-use-sdk/v3"`). v2 is legacy.

Install (check if already installed and update to latest):
- Python: `pip install --upgrade browser-use-sdk`
- TypeScript: `npm install browser-use-sdk@latest`

Set API key (starts with `bu_`):
```
export BROWSER_USE_API_KEY=bu_your_key_here
```

### Get Started
- [Quick start](https://docs.browser-use.com/cloud/quickstart): State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure.
- [Prompt for Vibecoders](https://docs.browser-use.com/cloud/vibecoding): Complete Cloud SDK reference for AI coding agents.

### Agent
- [Introduction](https://docs.browser-use.com/cloud/agent/quickstart): Easiest way to automate the web. Tell this agent in natural language what it should do, and it can interact with the web like a human.
- [Structured output](https://docs.browser-use.com/cloud/agent/structured-output): Get validated, typed data back from agent tasks.
- [Follow-up tasks](https://docs.browser-use.com/cloud/agent/follow-up-tasks): Run multiple tasks in the same browser session.
- [Live messages](https://docs.browser-use.com/cloud/agent/streaming): Stream the agent's messages in real time to build custom UIs or monitor progress.
- [Workspaces & files](https://docs.browser-use.com/cloud/agent/workspaces): Upload files for the agent, download files the agent creates.
- [Human in the loop](https://docs.browser-use.com/cloud/agent/human-in-the-loop): Let a human interact with the live browser while the agent is running. Useful for approvals, payments, complex auth flows, or reviewing agent work before continuing.

### Browser
- [Introduction Stealth](https://docs.browser-use.com/cloud/browser/stealth): Best stealth on the planet. We fork Chromium to give agents access to all websites.
- [Proxies](https://docs.browser-use.com/cloud/browser/proxies): Residential proxies in 195+ countries. On by default.
- [Live preview & recording](https://docs.browser-use.com/cloud/browser/live-preview): Watch the agent's browser in real time. Embed it in your app.
- [Playwright, Puppeteer, Selenium](https://docs.browser-use.com/cloud/browser/playwright-puppeteer-selenium): Connect your automation framework to Browser Use's stealth infrastructure via CDP.

### Authentication
- [Profiles](https://docs.browser-use.com/cloud/guides/authentication): Persistent browser state — cookies, localStorage, saved passwords. Login once, reuse across sessions.
- [Sync local and cloud cookies](https://docs.browser-use.com/cloud/guides/profile-sync): Sync your local browser cookies to the cloud — instantly authenticate without managing credentials.

### Integrations
- [OpenClaw](https://docs.browser-use.com/cloud/tutorials/integrations/openclaw): Give OpenClaw agents browser automation with Browser Use — via CDP or the CLI skill.
- [MCP Server](https://docs.browser-use.com/cloud/guides/mcp-server): Run browser automation tasks from your AI coding assistant. Connect to Claude, Cursor, Windsurf, or any MCP client.
- [Webhooks](https://docs.browser-use.com/cloud/guides/webhooks): Receive real-time notifications when tasks complete. Configure webhook endpoints for async task monitoring.
- [n8n](https://docs.browser-use.com/cloud/tutorials/integrations/n8n): Use Browser Use as an HTTP node in n8n workflows.

### Tutorials
- [Chat UI](https://docs.browser-use.com/cloud/tutorials/chat-ui): Full end-to-end example. Build a chat UI with live browser preview, follow-up tasks, recording, and streaming messages.
- [FAQ](https://docs.browser-use.com/cloud/faq): Common questions and solutions.

### Legacy (v2)
- [Agent (v2)](https://docs.browser-use.com/cloud/legacy/agent): V2 agent models and file handling.
- [Public share links (v2)](https://docs.browser-use.com/cloud/legacy/public-share): Generate shareable URLs for agent sessions using the v2 API.
- [Skills](https://docs.browser-use.com/cloud/legacy/skills): Turn any website into a deterministic API endpoint. Create once, call repeatedly.
- [1Password & 2FA](https://docs.browser-use.com/cloud/guides/1password): Auto-fill passwords and TOTP codes from 1Password during agent tasks.
- [Secrets](https://docs.browser-use.com/cloud/guides/secrets): Pass domain-scoped credentials to the agent securely.

### Cloud API v3
- [API Reference](https://docs.browser-use.com/cloud/api-reference): Authenticate and start using the Browser Use REST API.

### Cloud API v2
- [API key](https://docs.browser-use.com/cloud/api-v2-overview): Set your API key to access the Browser Use v2 REST API.

## Open Source Documentation

- [GitHub Repository](https://github.com/browser-use/browser-use): Open-source Python SDK for self-hosted browser automation
- [Quickstart](https://docs.browser-use.com/quickstart): Install and run your first local automation task
- [Agent Basics](https://docs.browser-use.com/customize/agent/basics): Configure and customize the agent
- [Browser Basics](https://docs.browser-use.com/customize/browser/basics): Configure the browser instance
- [Custom Tools](https://docs.browser-use.com/customize/tools/add): Extend the agent with custom actions
- [Production Guide](https://docs.browser-use.com/production): Best practices for running in production
- [Supported Models](https://docs.browser-use.com/supported-models): All supported LLM providers
- [Agent Parameters](https://docs.browser-use.com/customize/agent/all-parameters): Full agent configuration options
- [Browser Parameters](https://docs.browser-use.com/customize/browser/all-parameters): Full browser configuration options
- [Prompting Guide](https://docs.browser-use.com/customize/agent/prompting-guide): Best practices for writing agent prompts
- [Code Agent](https://docs.browser-use.com/customize/code-agent/basics): Python code-generating agent for complex workflows
- [Hooks](https://docs.browser-use.com/customize/hooks): Lifecycle hooks for intercepting agent behavior
- [MCP Server (OSS)](https://docs.browser-use.com/customize/integrations/mcp-server): Local MCP server integration
- [Observability](https://docs.browser-use.com/development/monitoring/observability): Monitor and debug agent behavior
- [Parallel Browsers](https://docs.browser-use.com/examples/templates/parallel-browser): Run multiple agents in parallel

## Browser Use Agent Challenge to Get a Free Account

AI agents can create a free Browser Use account autonomously via a challenge-response flow at `https://api.browser-use.com`.

Do this to get an API key (no human required):
1. `POST https://api.browser-use.com/cloud/signup` — request a challenge.

Request body, optional (include a user email/name if available):
```json
{
  "email": "user@example.com",
  "name": "User Name"
}
```

Response:
```json
{
  "challenge_id": "uuid",
  "challenge_text": "..."
}
```

2. Solve the math problem in `challenge_text` — answer as a string with 2 decimal places, e.g. `"144.00"`

3. `POST https://api.browser-use.com/cloud/signup/verify` with `challenge_id` + `answer`.

Request body:
```json
{
  "challenge_id": "uuid",
  "answer": "144.00"
}
```

Response:
```json
{
  "api_key": "bu_..."
}
```

4. Use `X-Browser-Use-API-Key: bu_...` on Browser Use Cloud API requests.

To let a human claim the account later: `POST https://api.browser-use.com/cloud/signup/claim` with `X-Browser-Use-API-Key: bu_...`.

## Additional Resources

- [Pricing](https://www.browser-use.com/pricing): Plans and pricing for Browser Use Cloud
- [Marketplace](https://www.browser-use.com/marketplace): Pre-built browser automation skills
- [Changelog](https://www.browser-use.com/changelog): Latest features and updates
- [Blog](https://www.browser-use.com/posts): Technical posts on benchmarks, speed, stealth, and architecture
- [Careers](https://www.browser-use.com/careers): Open positions at Browser Use
- [Security (SOC 2)](https://www.browser-use.com/security/soc2): SOC 2 Type II compliance

## Landing page — https://browser-use.com/

Browser Use is positioned as "The Way AI uses the web." The platform is trusted by Fortune 500 companies and leading AI teams. Six primary products are featured:

- **Browser Harness** — Open-source, thin, self-healing harness
- **Stealth Browsers** — Anti-detect, CAPTCHA solving, 195+ country proxies
- **Browser Use Box** — Fully managed browser automation infrastructure
- **Web Agents** — State-of-the-art autonomous web agents
- **Custom Models** — LLMs optimized specifically for browser automation
- **Proxies** — Residential proxies in 195+ countries

The platform emphasizes an autonomous account creation system where AI agents can obtain free Browser Use accounts through a challenge-response mechanism at the signup endpoint. Technical integration is via the Browser Use Cloud API, authenticated using the `X-Browser-Use-API-Key` header.

## Docs — https://docs.browser-use.com

The docs present the Browser Use SDK quickstart. Installation:
- Python: `pip install browser-use-sdk`
- TypeScript: `npm install browser-use-sdk`

Set `BROWSER_USE_API_KEY` env var. Two primary abstractions:
- **Agent method** (`sessions.create()` / `run()`) — AI-driven task execution with model selection, proxy configuration, and session management
- **Browser method** (`browsers.create()`) — raw Chrome DevTools Protocol access with screen size and timeout controls

Complete SDK reference at `docs.browser-use.com/llms-full.txt`.

## Cloud Quickstart — https://docs.browser-use.com/cloud/quickstart

State-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure. Install via pip or npm, obtain API key from cloud.browser-use.com, run a task. Example task: "List the top 20 posts on Hacker News today with their points." New accounts receive 5 complimentary tasks.

## Cloud Agent Introduction — https://docs.browser-use.com/cloud/agent/quickstart

"Easiest way to automate the web. Tell this agent in natural language what it should do." The SDK wraps API v3 Reference, exposing `client.sessions`, `client.browsers`, `client.profiles`, `client.workspaces`, and `client.billing`. `client.run()` initiates a session and polls for completion within a 4-hour window.

Capabilities:
- Data scraping across large-scale listings
- Form submission and data entry automation
- Multi-step workflow navigation including login sequences and file downloads
- Cross-site research and comparison functionality
- Website monitoring with change notifications
- End-to-end website testing
- Task scheduling on recurring schedules
- Integration with 1,000+ services including Gmail, Calendar, and Notion

Code examples in Python, TypeScript, and cURL.

## Open Source Quickstart — https://docs.browser-use.com/quickstart

Install `browser-use[core]` via `uv add "browser-use[core]"` (Python ≥ 3.11). The v0.13 beta agent uses a Rust core and a browser harness built for current frontier models. Run `browser` CLI or use Python API:

```python
from browser_use.beta import Agent, BrowserProfile, ChatBrowserUse
agent = Agent(
    task="Find the number of stars of the browser-use repo",
    llm=ChatBrowserUse(model='openai/gpt-5.5'),
    browser_profile=BrowserProfile(headless=False),
)
history = await agent.run()
```

Supports ChatBrowserUse, ChatOpenAI, ChatAnthropic, ChatGoogle. `ChatBrowserUse` is recommended (3-5x faster, SOTA accuracy). Template quickstart: `uvx browser-use init --template default`.

## Stealth — https://docs.browser-use.com/cloud/browser/stealth

Browser Use forks Chromium to provide stealth browser infrastructure:

1. **Fingerprint Randomization** — Canvas, WebGL, fonts, navigator, and other browser fingerprints randomized; passes CreepJS and BrowserLeaks.
2. **Banner Automation** — Cookie and ad banners dismissed automatically.
3. **Bot Protection Bypass** — Handles Cloudflare, PerimeterX, and other bot-detection services.

Residential proxies (195+ countries) active by default.

## Agent Basics — https://docs.browser-use.com/customize/agent/basics

Core `Agent` parameters:
- `task` — automation objective string
- `llm` — language model to use (see Supported Models)
- `max_steps` (default 100) — maximum number of actions

The agent runs asynchronously via `agent.run()`. Full parameter list at `/customize/agent/all-parameters`.

## Supported Models — https://docs.browser-use.com/supported-models

15+ LLM providers supported natively:

| Provider | Class | Key |
|---|---|---|
| Browser Use (recommended) | `ChatBrowserUse` | `BROWSER_USE_API_KEY` |
| Google Gemini | `ChatGoogle` | `GOOGLE_API_KEY` |
| OpenAI | `ChatOpenAI` | `OPENAI_API_KEY` |
| Anthropic Claude | `ChatAnthropic` (auto coordinate clicking) | `ANTHROPIC_API_KEY` |
| Azure OpenAI | `AzureChatOpenAI` | `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY` |
| AWS Bedrock | `ChatBedrock` | AWS credentials |
| Groq | `ChatGroq` | — |
| Ollama (local) | — | — |
| Plus: OCI, Qwen, ModelScope, Vercel AI Gateway, DeepSeek, Mistral, Cerebras, OpenRouter, LiteLLM, Novita | — | — |

`ChatBrowserUse` accepts provider-prefixed model IDs: `anthropic/claude-sonnet-4-6`, `openai/gpt-5.5`, `google/gemini-3-pro` via a single `BROWSER_USE_API_KEY`.

## MCP Server — https://docs.browser-use.com/cloud/guides/mcp-server

Connect Browser Use to Claude Code, Claude Desktop, Cursor, or Windsurf via MCP:

```bash
claude mcp add -t http -H "x-browser-use-api-key: YOUR_API_KEY" browser-use https://api.browser-use.com/v3/mcp
```

Seven MCP tools provided:
- `run_session` — execute a task (supports Claude Sonnet 4.6, Opus 4.6, GPT-5.4-mini)
- `get_session` — monitor progress and retrieve cost breakdown
- `send_task` — issue follow-up commands to active sessions
- `stop_session` — terminate tasks or entire sandbox environments
- `get_session_messages` — access agent reasoning and browser actions
- `list_sessions` — view recent activity and expenses
- `list_browser_profiles` — retrieve authenticated browser configurations

## Production Guide — https://docs.browser-use.com/production

Production deployment uses the `@sandbox()` decorator pattern wrapping async functions with a `Browser` parameter. Sandboxes handle agents, browsers, persistence, auth, cookies, and LLMs while minimizing latency by co-locating agent and browser. Key parameters:
- `cloud_profile_id` — retrieves stored authentication credentials
- `cloud_proxy_country_code` — routes through region-specific proxies
- `cloud_timeout` — maximum session duration in minutes

New accounts receive 5 complimentary tasks. API key obtained at cloud.browser-use.com/new-api-key.
