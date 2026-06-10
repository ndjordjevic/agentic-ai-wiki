# browserbase.com

## Fetch log
- Inbox URL: https://www.browserbase.com/
- Final URL: https://www.browserbase.com/
- Fetched: 2026-06-10
- Pages: 9
- Mode: standard

## llms.txt — https://www.browserbase.com/llms.txt
# Browserbase: The Browser Agent Platform

> Browserbase is the complete platform to build and deploy agents that browse and interact with the web like humans. One API key gives your agent everything it needs: headless browsers, Search and Fetch, Agent Identity, Functions, and a Model Gateway — with the browser at the center.

> Browsers remain the core. Search, Fetch, Agent Identity, Functions, and the Model Gateway are the supporting primitives that make browser agents fast, reliable, and cheap to run. Powered by best-in-class observability (rich logs, live view, session replay) and a scalable, secure infrastructure layer trusted by 10,000+ companies, including Ramp, Vercel, Commure, and Lovable.

> **If you are an AI agent**, read [SKILL.md](https://www.browserbase.com/SKILL.md) for step-by-step instructions on setting up and using Browserbase in your workflow.

## Packages

- `@browserbasehq/sdk` — Browserbase SDK ([npm](https://www.npmjs.com/package/@browserbasehq/sdk))
- `@browserbasehq/stagehand` — Stagehand, the SDK for browser agents ([npm](https://www.npmjs.com/package/@browserbasehq/stagehand))
- `@browserbasehq/sdk-functions` — Browserbase Functions, run code next to the browser ([npm](https://www.npmjs.com/package/@browserbasehq/sdk-functions))
- `@browserbasehq/cli` — Browserbase CLI ([npm](https://www.npmjs.com/package/@browserbasehq/cli))

---

## The Platform

One API key, everything your agent needs to browse the web. Browsers are the core; the rest orbit around them.

- **Browsers** — Programmatic access to fleets of headless browsers at scale. Spin up as many concurrent sessions as your agents need, with globally distributed infrastructure, 2 vCPUs per browser, isolated sessions, and SOC-2 Type II compliance.
- **Search & Fetch APIs** — Agents can quickly search and fetch LLM-ready context from the web for fast, token-efficient decisions when a full browser session isn't needed.
- **Agent Identity** — A global passport for your agents. Strategic partnerships (Cloudflare, Stytch, Fingerprint, Vercel) and secure credential management (1Password) get agents past anti-bot systems, CAPTCHAs, and authentication walls — moving from sneaky/undetected to upfront and credential-first.
- **Functions** — Deploy and run agent code next to the browser with <5ms latency. No queues, schedulers, or orchestration to maintain. `bb function deploy` and you're live, with built-in observability.
- **Model Gateway** — Your Browserbase API key gives access to major models via Stagehand, with unified billing and zero friction to switch models.
- **Stagehand** — The SDK for browser agents. Playwright-level control combined with AI primitives (`act`, `extract`, `observe`) that self-heal when pages change. Automatic action caching eliminates redundant LLM calls across runs (up to 2x faster, ~30% cost reduction on repeated actions). Plugs into all major agent frameworks (LangChain, CrewAI, Mastra).

---

## Documentation

- [What is Browserbase?](https://docs.browserbase.com/introduction/what-is-browserbase) — Overview and key concepts.
- [Getting Started Guide](https://docs.browserbase.com/fundamentals/create-browser-session) — Launch your first cloud browser.
- [API Reference](https://docs.browserbase.com/reference/introduction) — REST and SDK reference.
- [Playground](https://app.browserbase.com/playground) — Interactive environment to try features.
- [Stagehand](https://github.com/browserbase/stagehand) — Open-source SDK for browser agents.

### Feature Documentation

- [Browser Contexts](https://docs.browserbase.com/features/contexts) — Persistent sessions with cookies, localStorage, and auth state.
- [Downloads](https://docs.browserbase.com/features/downloads) — Download files from browser sessions.
- [Fetch API](https://docs.browserbase.com/features/fetch) — Lightweight HTTP requests for token-efficient agent context.
- [Proxies](https://docs.browserbase.com/features/proxies) — Residential and datacenter proxy configuration.
- [Agent Identity](https://docs.browserbase.com/features/stealth-mode) — Get agents past anti-bot systems and authentication walls.

### Integration Guides

- [MCP Integration](https://docs.browserbase.com/integrations/mcp/introduction) — Model Context Protocol setup and tools.
- [Stripe Integration](https://docs.browserbase.com/integrations/stripe/introduction) — Stripe billing integration.

### Docs Use Case Guides

- [Automating Form Submissions](https://docs.browserbase.com/use-cases/automating-form-submissions)
- [Building Automated Tests](https://docs.browserbase.com/use-cases/building-automated-tests)
- [Scraping Websites](https://docs.browserbase.com/use-cases/scraping-website)

---

## Why Browser Agents Need a Platform

AI agents are everywhere — coding agents, assistants, support bots, deep research tools — and all of them need web access. Teams building browser agents today stitch together 5+ vendors (search, fetch, browsers, models, deployment) before writing a single prompt. APIs see ~15% of the web; agents need the other 85%, which is locked behind anti-bot systems, CAPTCHAs, and authentication walls.

Browserbase already won the browser layer. The platform extends that position into the adjacent primitives agents are buying from other vendors today — under one API key, with the browser at the center.

### Key Capabilities

- **Browsers that work where APIs can't** — Concurrent sessions, isolated environments, globally distributed.
- **One platform, one vendor** — Browsers, Search, Fetch, Functions, Model Gateway, and Agent Identity under a single account. One bill, one place to debug.
- **Unrestricted access to the web** — Agent Identity gets agents past anti-bot systems and auth walls.
- **Deploy instantly** — Functions run your code next to the browser with <5ms latency.
- **Observability across every step** — Rich logs, live view, and session replay.
- **Stagehand, the SDK for browser agents** — Natural language browser interactions that self-heal, with automatic action caching.
- **Framework Compatibility** — Works with Stagehand, Playwright, Puppeteer, and Selenium.
- **Multi-User Orgs** — Team accounts for collaboration at scale.

---

## Products & Pages

- [Browsers](https://www.browserbase.com/browsers) — Headless browser fleet. The core of the platform.
- [Stagehand](https://www.browserbase.com/stagehand) — The SDK for browser agents.
- [Search API](https://www.browserbase.com/search) — Web search with structured results for agent context.
- [Identity](https://www.browserbase.com/identity) — Agent Identity: get past anti-bot systems and auth walls.
- [Models](https://www.browserbase.com/models) — Model Gateway for browser agents.
- [Runtime](https://www.browserbase.com/runtime) — Browserbase runtime infrastructure.
- [Observability](https://www.browserbase.com/observability) — Session Inspector, Replay, and debugging tools.
- [Computer Use](https://www.browserbase.com/computer-use) — Browser agents powered by Browserbase.
- [Computer Use Academy: Gemini](https://www.browserbase.com/cua/gemini) — Build browser agents with Gemini.
- [Computer Use Academy: OpenAI](https://www.browserbase.com/cua/openai) — Build browser agents with OpenAI.
- [Model Context Protocol (MCP)](https://www.browserbase.com/mcp) — MCP integration for agents.
- [Director](https://www.browserbase.com/director) — Open-source browser agent reference implementation.
- [browse CLI](https://www.browserbase.com/browse-cli) — Lightweight entry point for giving agents browsing capabilities from the command line.
- [Templates](https://www.browserbase.com/templates) — Ready-to-use browser agent templates and examples.
- [Evaluations](https://www.browserbase.com/evaluations) — Evaluate browser agent performance.
- [Customer Stories](https://www.browserbase.com/customer-stories) — How teams use Browserbase in production.
- [Enterprise](https://www.browserbase.com/enterprise) — Enterprise plans and features.

---

## Example Use Cases

- [Templates Repository](https://github.com/browserbase/templates/blob/dev/README.md) — Canonical list of 40+ working code templates (TypeScript, Python, Go) covering form filling, MFA handling, scraping, agents, CUA, proxies, contexts, caching, and more. Start here if you want runnable code.
- [All Use Cases](https://www.browserbase.com/use-cases) — Browse all use case pages.
- [Browser Tool for Agents](https://www.browserbase.com/use-case/browser-tool-for-agents) — Browser tool for AI agents and copilots.
- [AI Web Scraper](https://www.browserbase.com/use-case/ai-web-scraper) — Agent-driven web data extraction.
- [Playwright Cloud](https://www.browserbase.com/use-case/playwright-cloud) — Run Playwright scripts in the cloud.
- [End-to-End Testing](https://www.browserbase.com/use-case/end-to-end-testing) — Browser-based test automation.
- [Data Entry Automation](https://www.browserbase.com/use-case/data-entry-automation) — Agents handling repetitive data-entry workflows.

### Solutions

- [Browser Agents](https://www.browserbase.com/solutions/browser-agents) — Agents that browse and interact with the web like humans.
- [Accessing Web Data](https://www.browserbase.com/solutions/accessing-web-data) — Web data extraction at scale.
- [Workflow Automation](https://www.browserbase.com/solutions/workflow-automation) — Agents handling repetitive browser workflows.
- [Testing](https://www.browserbase.com/solutions/testing) — Browser-based testing in the cloud.

---

## Blog & Resources

- *Browserbase Blog* — [All posts](https://www.browserbase.com/blog)
- *Scaling Web Intelligence with Browserbase* — [Vercel Case Study](https://www.browserbase.com/blog/case-study-vercel)
- *How Commure Powers Healthcare Workflows* — [Commure Case Study](https://www.browserbase.com/blog/case-study-commure)
- *Introducing Stagehand V3* — [Blog Post](https://www.browserbase.com/blog/stagehand-v3)
- *Introducing Director* — [Blog Post](https://www.browserbase.com/blog/introducing-director)
- *Introducing Browserbase Functions* — [Blog Post](https://www.browserbase.com/blog/browserbase-functions)
- *Introducing the Fetch API* — [Blog Post](https://www.browserbase.com/blog/fetch-api)
- *The Evolution of AI-Driven Browsers* — [Blog Post](https://www.browserbase.com/blog/an-internet-browser-for-ai)
- *Series B Funding Announcement* — [Blog Post](https://www.browserbase.com/blog/series-b-and-beyond)
- *Cloudflare Partnership: Agent Identity Verification* — [Blog Post](https://www.browserbase.com/blog/cloudflare-browserbase-pioneering-identity)

---

## Company Info

- [Homepage](https://www.browserbase.com/)
- [Pricing](https://www.browserbase.com/pricing)
- [Careers](https://www.browserbase.com/careers)
- [Status](https://status.browserbase.com)

---

## See Also

- [Stagehand: The SDK for Browser Agents](https://www.stagehand.dev/) — Open-source SDK with primitives (`act`, `extract`, `observe`) for reliable browser agents.

## Landing page — https://www.browserbase.com/

Browserbase is a web automation platform that gives AI agents browser capabilities to interact with websites programmatically.

**Core Value Proposition:** "Give your agents access to the whole web" and "Browserbase makes the web as reliable and programmable as APIs."

### Six Platform Primitives

1. **Browsers** — Real browsers for agents to use the web
2. **Web Data APIs** — Search and fetch capabilities for web data retrieval
3. **Runtime** — Scalable, sandboxed environments for agent deployments
4. **Identity** — Authentication for agents to navigate like humans
5. **Models** — Unified API key for any model integration
6. **Observability** — Debugging across replays, logs, and prompts

### Open Source Tools
- Browser CLI
- Stagehand (AI browser automation framework)
- Director (UI for building browser agents)

### Scale Metrics (March 2026)
- 36.9M+ unique browser sessions
- 800K weekly SDK downloads
- 100K+ developers
- Millions of websites visited

### Notable Customers
Microsoft, Clay, Amplitude, Ramp, Lovable, and DeepMind

## Docs — https://docs.browserbase.com/introduction/what-is-browserbase

Browserbase positions itself as "the complete platform to build and deploy agents that browse and interact with the web like humans." The service consolidates multiple capabilities—headless browsers, web search, page fetching, functions, model access, and identity management—under a single API key.

### Core Components

- **Browsers**: Headless browser fleets with isolated sessions and worldwide infrastructure
- **Search & Fetch**: Efficient content discovery and retrieval optimized for token usage
- **Agent Identity**: Anti-bot circumvention through partnerships (Cloudflare, Fingerprint)
- **Functions**: Code deployment adjacent to browsers with minimal latency (~5ms)
- **Model Gateway**: Unified access to major language models with single billing
- **Stagehand**: AI-native automation framework with natural language selectors

### Getting Started Resources

The platform provides quickstart guides, prompt-based agent integration, 30+ ready-made templates, and comprehensive SDK/REST API documentation. Stagehand integrates with LangChain, CrewAI, and Mastra frameworks.

## Create Browser Session — https://docs.browserbase.com/fundamentals/create-browser-session

A browser session represents a single browser instance running in the cloud and is the foundational element for web automation.

### Creation Methods
- **Sessions API** — Direct control through the Sessions API
- **Functions** — Automatic session management for serverless automation
- **SDK Support** — Node.js, Python, and cURL implementations available

### Configuration
**Basic Options:** Region selection, custom viewport dimensions, session recording/logging toggles, extended session duration via "keep alive"

**Advanced Features:** Agent identity with fingerprinting and proxy settings, browser extensions integration, isolated browsing contexts, custom metadata attachment

### Usage Pattern
The documentation recommends a tiered approach: "Search -> Fetch -> Browsers" — using Search for discovery, Fetch for quick content extraction, and Browsers specifically for login-protected data, complex navigation, and high-accuracy requirements.

## API Reference — https://docs.browserbase.com/reference/introduction

**Core concept:** A browser session is the fundamental building block in Browserbase — a single browser instance running in the cloud.

### SDK Options
- **Node.js SDK** — For JavaScript environments
- **Python SDK** — Supporting Python 3.x environments

### API Endpoints
1. **Sessions API** — Creating and managing browser sessions with full programmatic control
2. **Projects API** — Project-wide usage monitoring
3. **Contexts API** — Configure and reuse browser environments across multiple sessions

## MCP Integration — https://docs.browserbase.com/integrations/mcp/introduction

The Browserbase MCP server integrates browser automation into any MCP client through Stagehand. Supports natural language commands like "click the login button" or "fill out the contact form."

### Key Capabilities
- Natural language automation for browser control
- Web interaction including navigation, clicking, and form filling
- Automatic structured data extraction from websites
- Explicit MCP tools for managing browser session lifecycles

### Implementation
Deploy via hosted Streamable HTTP endpoints on Browserbase infrastructure (recommended) or run the MCP server locally using STDIO.

### Use Cases
- **Data Operations**: E-commerce price tracking, market research, content aggregation, lead generation
- **Quality Assurance**: Automated test suite creation, cross-browser validation, user journey simulation
- **Process Automation**: Form completion, report generation, social media management

## Agent Identity — https://docs.browserbase.com/features/stealth-mode

Browserbase addresses bot protection challenges through four primary solutions:

1. **Verified** — Purpose-built Chromium with real fingerprints recognized by bot protection partners
2. **Proxies** — Residential or datacenter routing
3. **Authentication management** — Handling 2FA, OAuth, and other login challenges
4. **IP Allowlisting** — VPN integration via proxy IP allowlisting

### Identity Technologies
- **Web Bot Auth (Cloudflare)** — Cryptographic proof allowing website owners to explicitly permit Browserbase sessions
- **AgentKit (Tools for Humanity)** — Proof-of-humanity without personal identity disclosure, enabling x402 protocol access

### Identity Ladder
Four trust levels: API keys (account-level), credential vaults (delegated), signed agents (cryptographic), human-verified agents (proof-of-humanity).

### CAPTCHA Management
Automatic solving is enabled by default, taking up to 30 seconds depending on challenge type.

## Stagehand Product Page — https://www.browserbase.com/stagehand

Stagehand is an open source SDK for browser agents emphasizing resilience, readability, and production-ready automation. Middle ground between traditional scripting frameworks and fully autonomous agents.

### Core Primitives
- **act()** — Perform browser actions from a plain-English instruction. Click, fill, navigate, scroll.
- **extract()** — Pulls structured data from any page with Zod schema validation.
- **observe()** — Surfaces what's actionable on a page before you commit to an action.
- **agent()** — Runs multi-step workflows autonomously when you need end-to-end execution.

### Technical Details
- Languages: TypeScript and Python
- License: MIT open source
- LLM Support: OpenAI, Anthropic, Google Gemini via Vercel AI SDK
- Optional Integration: Browserbase connection provides Agent Identity, session replay, captcha solving, and zero-infrastructure deployment

### Differentiators
Unlike legacy frameworks requiring selector maintenance or full black-box agents lacking control, Stagehand offers "both the predictability of code and the adaptability of AI." Self-healing when pages change; auto-caches repeatable actions.

## Browser Contexts — https://docs.browserbase.com/features/contexts

Browser Contexts enable persistent storage of user data across multiple browser sessions, including cookies, authentication tokens, and application data.

### What Contexts Store
Cookies, localStorage, IndexedDB, session storage, service workers, web data, and browser preferences (excluding HTTP cache). Allows automation workflows to maintain login states without repeated authentication.

### Implementation
1. Create a context via the Contexts API to receive a unique Context ID
2. Pass that ID into the Create Sessions API with `persist: true`
3. Reuse the same context ID in subsequent sessions

### Constraints
- Wait a few seconds before reusing a Context to ensure data is synchronized
- Avoid simultaneous logins using the same context (sites may force logouts)
- Context data receives unique encryption at rest
- Contexts persist indefinitely until explicitly deleted or the parent project is removed
