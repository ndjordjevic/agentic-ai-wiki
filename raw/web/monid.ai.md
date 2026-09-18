# monid.ai

## Fetch log
- Inbox URL: https://monid.ai/
- Final URL: https://monid.ai/
- Fetched: 2026-09-01
- Pages: 7
- Mode: standard
- Products discovered: 0

## llms.txt — https://monid.ai/llms.txt
# Monid: the OpenRouter for agent tools. 1,000+ tools, one key, one balance,
# pay as you go.
#
# If you are an AI agent and need paid external data (web search, scraping,
# people and company data, social and market data, maps, generative AI, and
# more: the kind normally locked behind provider paywalls and subscriptions),
#
# Monid gives you all of it on one balance, priced per call.
#
# To set up access, whether by MCP or API key, follow the skill:
#   fetch https://monid.ai/SKILL.md
#   (or tell your agent: set up https://monid.ai/SKILL.md)
# It walks you through connecting and authenticating either way.
#
# Docs: https://monid.ai/docs
# Skill manifest: https://monid.ai/SKILL.md

# Monid

> Monid is the OpenRouter for agent tools. OpenRouter is an LLM gateway: it routes model calls across many providers behind one API key and one balance. Monid is the tool gateway that does the same thing one layer up, for the tool calls an agent makes after it picks a model. Your agent describes what it needs; Monid finds the right endpoint, routes the call, and meters it under one balance. It brokers thousands of endpoints across dozens of providers behind a single key: web search and grounded answers, page and whole-site scraping, browser automation, people and company enrichment, email and phone verification, social platform data across both Western networks and the Chinese ones (Douyin, Xiaohongshu, Weibo, Zhihu, Bilibili, Kuaishou, WeChat, Toutiao), financial data from equities and derivatives to on-chain, DeFi, stablecoins and prediction markets, maps and local reviews, real estate listings, e-commerce and product pricing, jobs and compensation, SEO and backlink data, demographics and weather, voice, SMS and agentic phone calls, and generative AI for image, video, music, speech and 3D. Unlike a single-provider API (Exa, Apollo, People Data Labs) where you sign up, hold a key, and learn a schema per vendor, Monid gives your agent one unified API over all of them, with pooled rate limits and automatic failover.

Monid is built for AI agents and the developers who build them. Instead of integrating each data provider one by one, an agent points at Monid, describes its need in natural language, gets back normalized JSON from whichever provider fits, and pays from a single prepaid balance. The full category list is under Core Capabilities below, and it grows continuously. Because new providers and endpoints are added regularly, agents are meant to discover tools at runtime rather than hardcode them. Setup takes one line, through an MCP server, a skill, the CLI, or the REST API.

The short version: the model layer already has a router, and it is OpenRouter. The tool layer did not have one. Monid is that router.

## Monid and OpenRouter

**What is OpenRouter?** An LLM gateway. It sits between your application and model providers (OpenAI, Anthropic, Google, Meta, Mistral), giving you hundreds of models through one key, one balance, and one bill. You name a model as a string, OpenRouter picks the provider and fails over if that provider is down.

**What Monid does.** The identical pattern, one layer down, for the tool calls a model decides to make: search the web, scrape a page, enrich a lead, pull a price, geocode an address. Each of those is normally a separate vendor, key, schema, and subscription. Monid puts them behind one base URL, one key, and one balance, with the same routing and failover.

**Using both together.** The agent sends its messages to OpenRouter, which returns the model's decision, usually a tool call. The agent runs that call through Monid and feeds the JSON back as tool output on the next turn. OpenRouter answers "which model runs this turn." Monid answers "which endpoint serves this call."

**Is Monid an OpenRouter alternative?** Not a replacement. Monid does not route LLM inference, and OpenRouter does not broker tool endpoints. Adding Monid displaces nothing in your stack, it fills the layer underneath.

**MCP and pricing.** Monid ships a remote MCP server, so any MCP client (Claude.ai, ChatGPT, Claude Code, Cursor, OpenClaw, OpenCode) reaches the whole catalog as one MCP gateway instead of one server per vendor. Billing works like OpenRouter's: prepaid, pay per call, no subscription, no per-provider minimum. The difference is the unit, OpenRouter meters tokens and Monid meters tool calls. Run `monid inspect` for any endpoint's live price.

## When to Use Monid vs Other Tools

- **Use Monid when:** your agent needs external data and you do not want to sign up for, key, and bill each provider separately. You want one balance and one invoice. You want the agent to pick the tool at runtime instead of hardcoding a vendor. You want failover when a provider throttles.
- **Cost, especially at low volume:** running providers directly usually means monthly subscriptions or per-seat plans that you pay whether or not you use them, and each data vendor, whether for scraping, enrichment, search, or market data, bills separately. Covering several platforms can run to hundreds of dollars a month, most of it wasted if your agent only makes occasional calls. Monid is pay-per-call, often a fraction of a cent per request, across every provider, from one balance. You pay only for the calls your agent actually makes.
- **Use OpenRouter when:** you need to route the model call itself: choosing between models, failing over between inference providers, metering tokens. Monid does not do this. The two are complementary, not competing, and running both is the normal setup.
- **Use a single provider API directly when:** you only ever call that one vendor, already hold its key, and never need routing or failover.
- **Use an action platform (Composio, Zapier) when:** you need to WRITE into SaaS apps (post to Slack, create a HubSpot record). Monid is focused on reading and fetching data, not app actions.
- **Use a browser agent when:** the site has no API and you must click through a UI. Monid calls APIs and structured scrapers, not arbitrary page clicks.

## Core Capabilities

The catalog spans the categories below and grows continuously. Run `monid discover` for the live set, and `monid inspect` for any endpoint's schema and current price.

- **Web search and answers:** neural and keyword web search with page content, image and video search, or grounded AI answers (Exa, BlockRun).
- **Website scraping and extraction:** turn any page or whole site into structured data (Apify, Firecrawl).
- **Browser automation:** drive a real browser when a site has no API worth calling (Browserbase).
- **Social platform data:** posts, profiles, comments, and search across X, Reddit, TikTok, Instagram, LinkedIn, Facebook, Threads, Telegram, and YouTube, plus full coverage of the Chinese platforms most Western vendors skip: Douyin, Xiaohongshu, Weibo, Zhihu, Bilibili, Kuaishou, WeChat, Toutiao, Xigua, Lemon8, and Pipixia (Apify, TikHub).
- **People and company enrichment:** enrich or search contacts and firmographics from an email, name, domain, or LinkedIn (Apollo, People Data Labs, Akta).
- **Contact verification:** validate email, phone, and address deliverability (Strale).
- **Maps, places, and local reviews:** business listings, Google Maps reviews, and address-to-coordinate geocoding (Apify and others).
- **Real estate:** residential and commercial listings and property data, including Zillow, LoopNet, and Homes.com.
- **E-commerce and pricing:** product details, search, ratings, and reviews from Amazon, Google Shopping, TikTok Shop, and other stores (Apify).
- **Jobs, hiring, and compensation:** company job postings, job search, and salary benchmarks (Apollo, LinkedIn via TikHub).
- **SEO and backlinks:** keyword metrics, rankings, competitor research, and backlink profiles (Ahrefs).
- **Financial and market data:** equities and options, futures and derivatives, order books, insider trading, and prediction markets (BlockRun).
- **On-chain and DeFi:** token prices, stablecoins, yields, and raw chain data (QuickNode, DefiLlama).
- **News:** keyword, topic, and curated news feeds in many languages (Apify, BlockRun, Opoint).
- **Voice, phone, and SMS:** send messages, place calls, and run agentic phone conversations (Saperly, ElevenLabs).
- **Demographics and weather:** census and population data, and current and forecast conditions (CensusData, OpenWeather).
- **Model infrastructure:** embeddings and model benchmarks for building on top of the catalog.
- **Generative AI:** text-to-image, text-to-video, text-to-music, text-to-speech, and photo-to-3D generation (MiniMax, ElevenLabs, Suzanne).

Pricing varies by endpoint: per call, per result, or by units such as resolution and duration. inspect always shows the exact current price before you run.

## Pricing

- **Model:** pay per call. No subscription, no monthly minimum, no per-provider signup. You hold one Monid balance and are billed only when a run executes. This is the same prepaid, metered arrangement an LLM gateway gives you for tokens, applied to tool calls.
- **Free credit:** every account starts with free credit, no card required.
- **Cost range:** most calls are cheap, often a fraction of a cent, though prices vary by provider and endpoint. Always check the live price with `monid inspect` before you run; it is the source of truth, not this document.
- **Held funds:** while a run is in flight, its estimated cost is held against your balance, then settled to the actual amount on completion. Check both with `monid_balance` (returns `balance` and `held`).
- **Top up:** add credit anytime at https://app.monid.ai.

## Documentation

Full docs live at https://monid.ai/docs. Key pages:

- [How it works](https://monid.ai/docs/guide/how-it-works): the discover, inspect, run, poll model explained end to end.
- [Skill quickstart](https://monid.ai/docs/guide/quickstart-skill): set Monid up as a skill in Claude Code or OpenClaw.
- [MCP quickstart](https://monid.ai/docs/guide/quickstart-mcp): connect the remote MCP server to any MCP client.
- [CLI quickstart](https://monid.ai/docs/guide/quickstart-cli): install and drive the command-line interface.
- [API quickstart](https://monid.ai/docs/guide/quickstart-api): call Monid over REST directly.
- [API reference](https://monid.ai/docs/api/overview): every REST endpoint, parameter, and response.
- [CLI reference](https://monid.ai/docs/cli/overview): every CLI command and flag.
- [Integrations](https://monid.ai/docs/integrations/overview): supported agents and clients, with setup guides.
- [Docs index for LLMs](https://monid.ai/docs/llms.txt): machine-readable index of the full documentation.

## Product

- [Home](https://monid.ai): what Monid is, who it is for, and how it works.
- [The OpenRouter for agent tools](https://monid.ai/openrouter-for-agent-tools): what the phrase means, how the tool layer maps onto the model layer, and how the two run together.
- [Tools catalog](https://monid.ai/tools): browse the full catalog by category and provider.
- [Dashboard](https://app.monid.ai): create an account, manage your balance, and top up credit.
- [API keys](https://app.monid.ai/access/api-keys): generate and rotate API keys.
- [Skill manifest](https://monid.ai/SKILL.md): the machine-readable skill an agent loads to set up and use Monid.
- [Sitemap](https://monid.ai/sitemap.xml): index of all crawlable pages, covering site pages (pages.xml) and documentation (docs sitemap).
- [List your tool](https://forms.gle/NLPchCCwnTP6zQhV8): apply to add your API to the Monid catalog.

## Blog

- [Blog](https://monid.ai/blog): guides, use cases, and new tool announcements.

## Community and Support

- [X / Twitter](https://x.com/MonidHQ): announcements and product news.
- [Discord](https://discord.gg/rQzztcgJV8): community, questions, and feedback.
- [Support](mailto:support@monid.ai): email the team directly.

## Landing page — https://monid.ai/
Monid is a service that connects AI agents to 1,700+ tools and APIs across 55+ providers through a unified interface. It removes the need for individual API key management by operating on a single shared prepaid balance.

Three integration methods: **Skill** (one-line chat integration), **MCP** (remote server), and **CLI** (terminal installation). Users "tell your agent what to do. It picks the tools itself" through Monid's discovery system that ranks candidates by fit and cost.

Pay-per-call structure rather than subscriptions, starting with $1 free credit. The service charges roughly "$0.0013" per tool call, debited from a single unified balance accessible across all tools and providers.

Catalog examples cited on the landing page: sales intelligence (Apollo), AI media generation (MiniMax), web scraping (Reddit, TikTok, Instagram), real-time search (Octen), weather data (OpenWeather).

The company invites tool providers to list their APIs on the platform, with Monid handling traffic routing, call metering, and revenue sharing.

## How It Works — https://monid.ai/docs/guide/how-it-works
Monid operates as a unified API layer connecting users and AI agents to hundreds of web data sources through a consistent interface and single billing system.

Three-step discovery and execution model:

1. **Discover** — Search endpoints using natural language queries (e.g., "twitter posts").
2. **Inspect** — Review input requirements, output structure, and associated costs.
3. **Run** — Execute endpoints and retrieve results (with a poll step for long-running runs).

Key benefits: AI agents identify appropriate tools dynamically without pre-loading all possible endpoints into context windows; multiple data provider relationships collapse into a single API gateway with unified billing.

Pricing structure is pay-as-you-go drawing from prepaid wallet balances: per-call fees (fixed charge per execution) and per-result fees (variable charge based on returned items, potentially including a base fee).

Access through four interfaces: MCP integration, Skill installation, command-line tools, or HTTP API calls. No need to manage separate API keys, usage quotas, or vendor contracts across providers.

## Docs index — https://monid.ai/docs
Section headings: Welcome | Get started | Setup for AI Agents | Setup for Humans | References | Links

Getting-started cards:
- How It Works: /docs/guide/how-it-works
- MCP: /docs/guide/quickstart-mcp
- Skill: /docs/guide/quickstart-skill
- CLI: /docs/guide/quickstart-cli
- API: /docs/guide/quickstart-api

Reference cards:
- API Reference: /docs/api/overview
- CLI Reference: /docs/cli/overview
- Integrations: /docs/integrations/overview

External links: https://monid.ai/docs/llms.txt, https://monid.ai, https://monid.ai/tools

## MCP quickstart — https://monid.ai/docs/guide/quickstart-mcp
**MCP Server URL:** `https://mcp.monid.ai/v1` (Streamable HTTP transport)

**Authentication:** OAuth login via Monid account (sign up if needed).

Claude Code setup:
1. `claude mcp add --transport http monid https://mcp.monid.ai/v1`
2. Open Claude Code, type `/mcp`, select `monid`
3. Select **Authenticate** and complete authorization

Other clients:
- **Claude.ai (web):** Settings > Connectors > Add custom connector, name `Monid`, URL above.
- **Codex:** `codex mcp add monid --url https://mcp.monid.ai/v1`
- **OpenCode config:**
```json
{
  "mcp": {
    "monid": {
      "type": "remote",
      "url": "https://mcp.monid.ai/v1",
      "enabled": true
    }
  }
}
```
- **ChatGPT:** Settings > Plugins > Developer Mode, create new plugin named `monid` with the connection URL above.

Once connected you gain tools for discovering and running hundreds of data endpoints automatically.

## Skill quickstart — https://monid.ai/docs/guide/quickstart-skill
Install command (run inside your agent):
```
set up https://monid.ai/SKILL.md
```

Setup steps:
1. **Install the Skill** with the command above — gives the agent the ability to discover and run data endpoints across the web.
2. **Obtain an API key:** visit the Monid Dashboard (https://app.monid.ai), create an account, go to the API key management page (https://app.monid.ai/access/api-keys), generate a new key and copy it immediately ("it is only shown once"), share it with your agent for configuration.
3. **Start using:** the agent can then discover, inspect, and execute data endpoints automatically.

Authentication is API-key-based (as opposed to the MCP path's OAuth).

## Docs index for LLMs — https://monid.ai/docs/llms.txt
# Monid

## Docs

- [Welcome](https://monid.ai/docs/index.md)
- [How It Works](https://monid.ai/docs/guide/how-it-works.md): How Monid works, and how you (or your agent) pay for what you use.
- [Set Up with Skill](https://monid.ai/docs/guide/quickstart-skill.md): Give your AI agent the ability to discover and run data endpoints across the web.
- [Set Up with MCP](https://monid.ai/docs/guide/quickstart-mcp.md): Connect your AI client to Monid via MCP (Streamable HTTP).
- [Set Up with CLI](https://monid.ai/docs/guide/quickstart-cli.md): Install the Monid CLI and start querying data from the command line.
- [Set Up with API](https://monid.ai/docs/guide/quickstart-api.md): Call the Monid HTTP API directly with your own code.
- [Set Up with Claude Tag](https://monid.ai/docs/guide/quickstart-claude-tag.md): Connect Monid to Claude as a custom tool via a Claude Tag access bundle.
- [Pay with x402](https://monid.ai/docs/guide/pay-with-x402.md): Pay per run with a crypto wallet (USDC) using the x402 protocol instead of a prepaid Monid workspace balance.
- [API Overview](https://monid.ai/docs/api/overview.md): Discover, inspect, and run data endpoints programmatically.
- [Who Am I](https://monid.ai/docs/api/auth/whoami.md): Return the identity behind the current API key or OAuth access token.
- [List Workspaces](https://monid.ai/docs/api/auth/workspaces.md): List the workspaces your API key or OAuth token has access to.
- [Discover](https://monid.ai/docs/api/discover.md): Search for data endpoints using natural language.
- [Inspect](https://monid.ai/docs/api/inspect.md): Get full details for a specific data endpoint.
- [Run](https://monid.ai/docs/api/run.md): Execute a data endpoint.
- [List Runs](https://monid.ai/docs/api/runs/list.md): List runs for your workspace.
- [Get Run](https://monid.ai/docs/api/runs/get.md): Get the status and results of a specific run.
- [Stop Run](https://monid.ai/docs/api/runs/stop.md): Stop a running run.
- [Get Balance](https://monid.ai/docs/api/wallet/balance.md): Get the current wallet balance.
- [List Activities](https://monid.ai/docs/api/wallet/activities.md): List wallet transactions.
- [CLI Overview](https://monid.ai/docs/cli/overview.md): The Monid CLI lets you discover, inspect, and run data endpoints from the command line.
- [monid discover](https://monid.ai/docs/cli/discover.md): Search for data endpoints using natural language.
- [monid inspect](https://monid.ai/docs/cli/inspect.md): Get full details for a specific data endpoint.
- [monid run](https://monid.ai/docs/cli/run.md): Execute a data endpoint and retrieve results.
- [monid runs list](https://monid.ai/docs/cli/runs/list.md): List recent runs.
- [monid runs get](https://monid.ai/docs/cli/runs/get.md): Get the status and results of a specific run.
- [monid runs stop](https://monid.ai/docs/cli/runs/stop.md): Stop a queued or running run.
- [monid keys list](https://monid.ai/docs/cli/keys/list.md): List all locally stored API keys.
- [monid keys add](https://monid.ai/docs/cli/keys/add.md): Add an API key to your local credential store.
- [monid keys activate](https://monid.ai/docs/cli/keys/activate.md): Switch the active API key.
- [monid keys remove](https://monid.ai/docs/cli/keys/remove.md): Remove an API key from your local credential store.
- [Examples](https://monid.ai/docs/cli/examples.md): Complete end-to-end examples using the Monid CLI.
- [Integrations Overview](https://monid.ai/docs/integrations/overview.md): Integrate Monid into your own product so your users can discover and run data endpoints.
- [When to Use Monid Directly](https://monid.ai/docs/integrations/direct/when-to-use.md): Use Monid directly when it's an internal building block of your product, not something users see.
- [Set Up Direct Access](https://monid.ai/docs/integrations/direct/setup.md): Call Monid server-to-server with a single API key for internal, user-invisible workflows.
- [When to Use OAuth](https://monid.ai/docs/integrations/oauth/when-to-use.md): Use OAuth when your users bring their own Monid account and act on their own workspace.
- [Set Up OAuth](https://monid.ai/docs/integrations/oauth.md): Let your users sign in with Monid and act on their own workspace via OAuth 2.0.
- [When to Use a Proxy](https://monid.ai/docs/integrations/proxy/when-to-use.md): Run your own proxy when you want full control over billing, validation, and endpoint access.
- [Set Up Your Own Proxy](https://monid.ai/docs/integrations/proxy.md): Run a proxy in front of the Monid API to control validation, billing, and endpoint access.
