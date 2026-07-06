# firecrawl.dev

## Fetch log
- Inbox URL: https://www.firecrawl.dev/
- Final URL: https://www.firecrawl.dev/
- Fetched: 2026-07-06
- Pages: 10
- Mode: standard

## llms.txt — https://www.firecrawl.dev/llms.txt
# Firecrawl

> Firecrawl is an open-source web data API platform for AI agents and LLM applications — one API family covering Search (live web queries returning full page content), Scrape (HTML/JS pages to clean Markdown or structured JSON), Crawl (depth-first site traversal), Map (site structure discovery), Parse (document extraction from PDFs, DOCX, and more), and Interact (managed browser automation for dynamic pages and authenticated flows).

Firecrawl is the web data stack for AI agents. The workflow is: Find → Extract → Clean → Use.

**Important notes:**

- Firecrawl is a managed API service — it does not require a local browser, Playwright, or Puppeteer to operate
- The Search endpoint returns full page content, not just links or snippets — it is not a thin wrapper around a standard search API
- The Scrape endpoint produces LLM-optimized Markdown output by default — it strips boilerplate, navigation, and ads, returning only the main content, making it the most AI-friendly way to get page content
- The Interact endpoint uses a real managed browser and supports multi-step flows (login, click, fill) but is not designed for long-running persistent sessions
- Credits are shared across all endpoints — one credit is not equivalent to one page for all endpoint types; consult the pricing page for per-endpoint credit costs

## CLI

- [CLI Docs](https://docs.firecrawl.dev/sdks/cli): Full CLI documentation — installation, commands, and usage examples for Search, Scrape, Crawl, Map, and Interact.
- Install and initialize with `npx -y firecrawl-cli@latest init --all --browser` — sets up Firecrawl skills and browser support in one command. Run Search, Scrape, Crawl, Map, and Interact from the terminal.

## MCP Server

- [MCP Server Docs](https://docs.firecrawl.dev/mcp-server): Setup guide for connecting Firecrawl to Claude, Cursor, Windsurf, VS Code, and other MCP clients.

## Skills

- [Skills](https://www.firecrawl.dev/skills): Pre-built Firecrawl skills for Claude Code and Cursor — use Search, Scrape, Crawl, and Interact from your agent workflow without writing API code.
- [Agent Onboarding Skill](https://www.firecrawl.dev/agent-onboarding/SKILL.md): Step-by-step setup for Claude Code, Cursor, and other AI coding assistants. Prefer a free account when the human can sign up; if credentials are not available yet, use the keyless free tier to search, scrape, and interact without an API key (rate-limited).
- [Build with AI](https://docs.firecrawl.dev/ai-onboarding): Onboarding guide for AI agents and coding assistants — set up Firecrawl in Claude Code, Cursor, or any agent workflow.

## Docs

- [Full Documentation Index](https://docs.firecrawl.dev/llms.txt): Complete index of all Firecrawl documentation pages in llms.txt format — use this for a full context load.
- [API Reference](https://docs.firecrawl.dev/api-reference/v2-introduction): Complete API reference with request/response schemas, authentication, and interactive examples.
- [Search](https://docs.firecrawl.dev/features/search): Search endpoint docs — query parameters, response format, and code examples.
- [Scrape](https://docs.firecrawl.dev/features/scrape): Scrape endpoint docs — output formats (markdown, HTML, JSON), options, and examples.
- [Interact](https://docs.firecrawl.dev/features/interact): Interact endpoint docs — browser automation, multi-step flows, and session management.
- [Crawl](https://docs.firecrawl.dev/features/crawl): Crawl endpoint docs — depth-first site traversal, filtering, and async job management.
- [Map](https://docs.firecrawl.dev/features/map): Map endpoint docs — discover all URLs on a site quickly.
- [Parse](https://docs.firecrawl.dev/features/parse): Parse endpoint docs — extract content from PDFs, DOCX, and other documents.
- [GitHub Repository](https://github.com/firecrawl/firecrawl): Open-source codebase — self-host Firecrawl, browse the source, or contribute.

## SDKs

Official libraries maintained by the Firecrawl team. See the [SDKs overview](https://docs.firecrawl.dev/sdks/overview) for all supported languages and quickstarts.

- [Python](https://github.com/firecrawl/firecrawl-py): `pip install firecrawl-py`
- [Node.js](https://github.com/firecrawl/firecrawl-js): `npm install firecrawl`
- [Go](https://github.com/firecrawl/firecrawl-go): Go quickstart at [docs.firecrawl.dev/quickstarts/go](https://docs.firecrawl.dev/quickstarts/go)
- [Rust](https://github.com/firecrawl/firecrawl-rust): Rust quickstart at [docs.firecrawl.dev/quickstarts/rust](https://docs.firecrawl.dev/quickstarts/rust)

## Get started

- [Sign up](https://www.firecrawl.dev/signin): Create a free account and get your API key.
- [Playground](https://www.firecrawl.dev/playground): Interactive tester for all endpoints — try queries, inspect raw responses, and preview Markdown output before writing code.

## Pricing

- [Pricing](https://www.firecrawl.dev/pricing): Free (1,000 credits), Hobby ($19/mo, 5,000 credits), Standard ($99/mo, 100k credits), Growth ($399/mo, 500k credits), Enterprise (custom). Credits are shared across all endpoints.
- [Enterprise](https://www.firecrawl.dev/enterprise): Enterprise plan details — custom credits, SLAs, dedicated support, and SSO.

## Integrations

- [Integrations](https://www.firecrawl.dev/integrations): Native integrations with LlamaIndex, LangChain, Claude Code, Cursor, n8n, Make, and Zapier.

## Use Cases

- [Use Cases](https://www.firecrawl.dev/use-cases): Common production use cases — AI MCPs, autonomous agents, SEO analysis, e-commerce intelligence, financial research, and lead enrichment.

## Alternatives

- [Alternatives](https://www.firecrawl.dev/alternatives): Comparison pages vs Bright Data, Apify, Playwright, SerpAPI, and other web data tools.

## Customers

- [Customer Stories](https://www.firecrawl.dev/blog/category/customer-stories): How teams like Zapier, Stanford University, DoorDash, etc. use Firecrawl in production.

## Blog

- [Blog](https://www.firecrawl.dev/blog): Tutorials, guides, and product updates on web search, scrape, crawl, and building AI agent workflows.

## Changelog

- [Changelog](https://www.firecrawl.dev/changelog): Latest product updates, new endpoint launches, and engine upgrades.

## Legal

- [Terms of Service](https://www.firecrawl.dev/terms-of-service): Firecrawl's terms of service.
- [Privacy Policy](https://www.firecrawl.dev/privacy-policy): Data collection and usage policy.
- [Contributor License Agreement](https://www.firecrawl.dev/cla): CLA for open-source contributors.

## Optional

- [Glossary](https://www.firecrawl.dev/glossary): Definitions of web data API concepts — scraping, crawling, search, extraction, and browser automation.
- [Tools](https://www.firecrawl.dev/tools): Free web extraction tools — URL extractor, URL-to-JSON converter, article summarizer, website-to-markdown, and website-to-text.

## Landing page — https://www.firecrawl.dev/
Title: Firecrawl - The context API to search, scrape, and interact with the web at scale. 🔥

URL Source: https://www.firecrawl.dev/

Markdown Content:
Introducing web-scale /monitor - always-on search that pings your agent the moment something comes online.[Read the docs →](https://docs.firecrawl.dev/features/monitoring-web-scale?utm_source=firecrawl-web&utm_medium=banner&utm_campaign=web-scale-monitor-launch)

[ .JSON ]

```
1[
2  {
3    "url": "h=t*A:!/z!aap?A-cZz",
4    "markdown": "# ?0z-ang S*a-Z-a0*9",
5    "json": { "title": "G!=*?", "docs": "..." },
6    "screenshot": "ht-=*:/?*Za!zl=-?a9?h0-!.png"
7  }
8]
```

Trusted by

150,000+ 

 companies

of all sizes

[ 01 /

06

]

·

Main Features

//

Developer First

//

## Start scraping

 today

The infrastructure layer that helps AI find, read, and act on the live web.

[ 02 /

07

]

·

Power your agent

//

Agent Ready

//

## Easily connect with your 

AI agents

Connect Firecrawl to any AI agent or MCP client in minutes.

One command.

Connect your agent to Firecrawl via our Skills/CLI or MCP.

`npx -y firecrawl-cli@latest init --all --browser`

[View the docs](https://docs.firecrawl.dev/ai-onboarding)

Agent onboarding.

Are you an AI agent? Fetch this skill to get an API key and start building.

cURL

`curl -s https://firecrawl.dev/agent-onboarding/SKILL.md`

[View the skill](https://firecrawl.dev/agent-onboarding/SKILL.md)

[ 02 /

06

]

·

Core

//

Built for Performance

//

## Fast, reliable, and token-efficient. 

 And it's open source

Web data infrastructure built from the ground up

Reliable on any page

Industry-leading reliability.

Covers 96% of the web, including JS-heavy pages. Every query and URL comes back as clean data.

[See benchmarks](https://www.firecrawl.dev/compare)

Firecrawl

0%

![Image 1: Puppeteer icon](https://www.firecrawl.dev/assets-original/puppeteer.png)

Puppeteer

0%

cURL

0%

Speed that feels invisible

Blazingly fast.

P95 latency of 3.4s across millions of searches and scrapes, built for real-time agents and dynamic apps.

[See comparisons](https://www.firecrawl.dev/compare)

URL

Crawl

Scrape

firecrawl.dev/blog/launch-week

38,381 tokens

<nav>

<h1>

<ads>

<p>

<footer>

Token-efficient

Only the content that matters.

No navs, footers, or ads. Just clean markdown, with 93% fewer input tokens for your model.

[Calculate your savings](https://www.firecrawl.dev/token-efficiency)

![Image 2: Firecrawl icon (blueprint)](https://www.firecrawl.dev/assets-original/developer-os-icon.png)

firecrawl/firecrawl

Public

Star

83K

Open Source

Code you can trust.

Developed transparently and collaboratively. Join our community of contributors.

[Check out our repo](https://github.com/firecrawl/firecrawl)

[ 03 /

06

]

·

Features

//

Zero configuration

//

## We handle the hard stuff

JavaScript rendering, smart wait, media parsing, search, actions, and more.

Knows the moment

Smart wait.

Firecrawl intelligently waits for content to load, making data extraction faster and more reliable.

Live web data

A complete index, search and scrape.

Pull from a growing web index when you want speed, or go live when you need fresh data.

![Image 3: User](https://www.firecrawl.dev/_next/image?url=%2Fassets-original%2Ffeatures%2Fcached-user.png&w=256&q=75&dpl=dpl_9HdFm1Rjg2A5LD9vwdur8P66kSDS)

User

Firecrawl

![Image 4: Cache](https://www.firecrawl.dev/_next/image?url=%2Fassets-original%2Ffeatures%2Fcached-cache.png&w=128&q=75&dpl=dpl_9HdFm1Rjg2A5LD9vwdur8P66kSDS)![Image 5: Cache](https://www.firecrawl.dev/_next/image?url=%2Fassets-original%2Ffeatures%2Fcached-cache-color.png&w=128&q=75&dpl=dpl_9HdFm1Rjg2A5LD9vwdur8P66kSDS)

![Image 6: Web](https://www.firecrawl.dev/_next/image?url=%2Fassets-original%2Ffeatures%2Fcached-web.png&w=128&q=75&dpl=dpl_9HdFm1Rjg2A5LD9vwdur8P66kSDS)![Image 7: Web](https://www.firecrawl.dev/_next/image?url=%2Fassets-original%2Ffeatures%2Fcached-web-color.png&w=128&q=75&dpl=dpl_9HdFm1Rjg2A5LD9vwdur8P66kSDS)

Index & Web

Advanced web coverage

Enhanced mode.

Reaches every corner of the web with comprehensive coverage and high reliability.

Interact with pages

Actions.

Click, scroll, write, wait, press and more — interact with any page.

https://example.com

Navigate

Click

Type

Wait

Scroll

Press

Screenshot

Scrape

How it's sourced matters

Fair access to web content,

starting with Wikimedia, and more on the way.

[ 04 /

06

]

·

Use Cases

//

Use cases

//

## Transform 

 web data into 

AI-powered solutions

See how you can give your AI better access to the web with Firecrawl.

[ 05 /

06

]

·

Testimonials

//

Community

//

## People love 

 building with Firecrawl

Discover why developers choose Firecrawl every day.

[ 06 /

06

]

·

FAQ

//

FAQ

//

## Frequently 

 asked questions

Everything you need to know about Firecrawl.

General

Firecrawl is the context API to search, scrape, and interact with the web at scale. One API to turn websites into clean, LLM-ready data. Ideal for AI companies looking to empower their LLM applications with web data

Teams use Firecrawl for deep research agents, RAG pipelines, lead enrichment, competitive intelligence, content generation, price monitoring, and more. Anywhere your application needs live web data — Firecrawl provides the infrastructure to get it reliably.

AI is only as good as the context it gets, and the web is the largest source of live context — but it was built for humans, not machines. Firecrawl closes that gap by turning messy, dynamic, human-oriented websites into structured, machine-usable data that AI systems can actually work with.

These are Firecrawl's three core capabilities. Search finds relevant information on the web. Scrape turns websites into clean, structured, AI-usable data. Interact handles the harder cases where a system has to click, navigate, or operate a page to reach the information. Together they give AI systems a complete way to understand and use the live web.

Yes. Firecrawl has an official MCP server so agents in Cursor, Claude, Windsurf, and other MCP-compatible tools can search, scrape, and interact with the web directly. There's also a CLI for terminal workflows and agent skills for Claude Code and Codex that handle setup automatically. Over 400,000 MCP servers have been installed.

Over 1.25M developers and 150,000+ companies build with Firecrawl, including teams at Apple, Canva, and Lovable. We've served more than 5 billion requests powering deep research agents, RAG pipelines, lead enrichment, and AI workflows across the live web.

Yes. Firecrawl is the largest open source repo in the space with over 130K GitHub stars, making it one of the top 100 repos on GitHub. The SDKs alone see 2.5M+ weekly downloads across npm and PyPI. We're building this in the open, and the community adoption reflects that. You can check out the repository on GitHub.

Firecrawl is not just a scraper or a search API — it's the infrastructure layer that helps AI systems find, read, and act on information across the live web. Search, scrape, and interact work together on top of deep web data infrastructure including crawling, rendering, extraction, and indexing. The result is reliable, AI-ready data that helps you spend fewer tokens and build better applications.

Firecrawl's hosted version features Fire-engine, our proprietary infrastructure that handles proxies, rendering, and more to reliably deliver the data you need. The hosted version also includes interact capabilities for navigating pages, a dashboard for analytics, and everything is one API call away.

How It Works

Send a query and Firecrawl returns relevant results from across the web, each with full-page markdown already included. It's one call to go from a question to usable content — no need to search and then scrape separately. Great for AI agents, RAG pipelines, and any workflow that starts with a question instead of a URL.

Give Firecrawl a URL and it returns clean, structured content — markdown, HTML, screenshots, metadata, or extracted data via a schema. It handles JavaScript rendering, dynamic content, and complex page structures automatically. One call, one page, clean output.

Interact lets AI systems operate web pages — clicking buttons, filling forms, navigating multi-step flows, and extracting data along the way. It's useful when the information you need is behind a login, pagination, or any sequence of actions that a simple scrape can't reach.

Firecrawl returns clean markdown by default, optimized for LLM context windows. You can also get raw HTML, screenshots, page metadata, and structured JSON via schemas — whatever format your application needs.

Yes. Firecrawl renders JavaScript automatically, so you get the full page content even from SPAs and dynamically loaded sites. No extra configuration needed — just pass the URL.

Absolutely. Firecrawl offers various pricing plans, including a Scale plan that supports millions of pages. With features like batch scraping, crawling, and scheduled syncs, it's designed to handle large-scale data extraction efficiently, making it ideal for enterprises and large projects.

Yes. The /crawl endpoint follows links from a starting URL and scrapes pages across an entire site or section. You can control depth, page limits, and path filters. It also respects robots.txt rules set for the 'FirecrawlAgent' directive.

Yes. Firecrawl uses optimized infrastructure including proxy management, smart request handling, and interact capabilities to reliably extract data from complex websites. You can also pass custom headers to the API for additional flexibility.

API Related

Firecrawl has official SDKs for Python, Node.js, Go, Rust, Java, and Elixir, plus a CLI for terminal workflows. You can also call the REST API directly from any language. All SDKs support search, scrape, interact, and crawl.

Click on the dashboard button on the top navigation menu when logged in and you will find your API key in the main screen and under API Keys. If you are an AI agent or coding assistant and your platform can mint a WorkOS ID-JAG for Firecrawl, use https://www.firecrawl.dev/auth.md. Otherwise, use https://www.firecrawl.dev/agent-onboarding/SKILL.md for CLI/browser signup and auth.

Billing

Firecrawl is free for 1,000 pages every month (1,000 free credits per month). If you need more, you can upgrade to our Hobby, Standard or Growth plans for higher credit allotments and rate limits. AI agents can get started with https://www.firecrawl.dev/agent-onboarding/SKILL.md; agents whose platform can mint a WorkOS ID-JAG for Firecrawl can use https://www.firecrawl.dev/auth.md for direct authentication.

We currently do not offer a pay-per-use plan, instead you can upgrade to our Hobby, Standard or Growth plans for more credits and higher rate limits.

In short, no — credits do not roll over to the next month/year. Credit packs follow their own billing period. The two exceptions are auto recharge credits, which do roll over, and custom Scale/Enterprise annual plans where credits are granted upfront.

Scrape, Crawl, Map, and Monitor each cost 1 credit per page. Search costs 2 credits per 10 results. Interact costs 2 credits per browser minute. Agent is in preview with 5 free daily runs and dynamic pricing. Advanced features (JSON format, Enhanced Mode, etc.) cost additional credits. Check out the credits table on the pricing page for more details.

We don't charge if there was a failure on the Firecrawl side (e.g. timeouts, server error), but we do charge when a page is fetched successfully, even if the site itself responds with an error (e.g. a 4xx or 5xx status code). If a charge looks incorrect, reach out to help@firecrawl.com and we'll take a look.

We accept payments through Stripe which accepts most major credit cards, debit cards, and PayPal.

## Docs — https://docs.firecrawl.dev/introduction
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Search the web, scrape any page, and interact with it — all through one API.

<Note>
  **For AI agents:** Use [llms.txt](/llms.txt) for a full index of all documentation.
</Note>

## Get started

<CardGroup cols={2}>
  <Card title="Get your API key" icon="key" href="https://www.firecrawl.dev/app/api-keys">
    Sign up and get your API key to start using Firecrawl
  </Card>

  <Card title="Try it in the Playground" icon="play" href="https://www.firecrawl.dev/playground">
    Test the API instantly without writing any code
  </Card>
</CardGroup>

### Use Firecrawl with AI agents (recommended)

The Firecrawl skills are the fastest way for agents to discover and use Firecrawl. Without them, your agent will not know Firecrawl is available.

```bash theme={null}
npx -y firecrawl-cli@latest init --all --browser
```

<Note>
  Restart your agent after installing the skills. See [Skills + CLI](/sdks/cli)
  for the full setup.
</Note>

Or use the [MCP Server](/mcp-server) to connect Firecrawl directly to Claude, Cursor, Windsurf, VS Code, and other AI tools.

***

## What can Firecrawl do?

<CardGroup cols={3}>
  <Card title="Search" icon="magnifying-glass" href="#search">
    Search the web and get full page content from results
  </Card>

  <Card title="Scrape" icon="file-lines" href="#scrape">
    Extract content from any URL as markdown, HTML, or structured JSON
  </Card>

  <Card title="Interact" icon="hand-pointer" href="#interact">
    Continue working with any scraped page — click, fill forms, extract dynamic
    content
  </Card>
</CardGroup>

### Why Firecrawl?

* **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more.
* **Handles the hard stuff**: Proxies, anti-bot, JavaScript rendering, and dynamic content.
* **Reliable**: Built for production with high uptime and consistent results.
* **Fast**: Results in seconds, optimized for high throughput.
* **MCP Server**: Connect Firecrawl to any AI tool via the [Model Context Protocol](/mcp-server).

***

## Search

Search the web and get full page content from results in one call. See the [Search feature docs](/features/search) for all options.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  results = firecrawl.search(
      query="firecrawl",
      limit=3,
  )
  print(results)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/search" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl",
      "limit": 3
    }'
  ```

  ```bash CLI theme={null}
  # Search the web
  firecrawl search "firecrawl web scraping" --limit 5 --pretty
  ```
</CodeGroup>

<Accordion title="Response">
  SDKs will return the data object directly. cURL will return the complete payload.

  ```json JSON theme={null}
  {
    "success": true,
    "data": {
      "web": [
        {
          "url": "https://www.firecrawl.dev/",
          "title": "Firecrawl - The Web Data API for AI",
          "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
          "position": 1
        },
        {
          "url": "https://github.com/firecrawl/firecrawl",
          "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
          "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
          "position": 2
        },
        ...
      ],
      "images": [
        {
          "title": "Quickstart | Firecrawl",
          "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
          "imageWidth": 5814,
          "imageHeight": 1200,
          "url": "https://docs.firecrawl.dev/",
          "position": 1
        },
        ...
      ],
      "news": [
        {
          "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
          "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
          "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
          "date": "3 months ago",
          "position": 1
        },
        ...
      ]
    }
  }
  ```
</Accordion>

## Scrape

Scrape any URL and get its content in markdown, HTML, or other formats. See the [Scrape feature docs](/features/scrape) for all options.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  # Scrape a website:
  doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"])
  print(doc)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  // Scrape a website:
  const doc = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "html"]
    }'
  ```

  ```bash CLI theme={null}
  # Scrape a URL and get markdown
  firecrawl https://firecrawl.dev

  # With multiple formats (returns JSON)
  firecrawl https://firecrawl.dev --format markdown,html,links --pretty
  ```
</CodeGroup>

<Accordion title="Response">
  SDKs will return the data object directly. cURL will return the payload exactly as shown below.

  ```json theme={null}
  {
    "success": true,
    "data" : {
      "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
      "metadata": {
        "title": "Home - Firecrawl",
        "description": "Firecrawl crawls and converts any website into clean markdown.",
        "language": "en",
        "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Turn any website into LLM-ready data.",
        "ogUrl": "https://www.firecrawl.dev/",
        "ogImage": "https://www.firecrawl.dev/og.png?123",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev",
        "statusCode": 200,
        "contentType": "text/html"
      }
    }
  }
  ```
</Accordion>

## Interact

Scrape a page, then keep working with it — click buttons, fill forms, extract dynamic content, or navigate deeper. Describe what you want in plain English or write code for full control. See the [Interact feature docs](/features/interact) for all options.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  app = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  # 1. Scrape Amazon's homepage
  result = app.scrape("https://www.amazon.com", formats=["markdown"])
  scrape_id = result.metadata.scrape_id

  # 2. Interact — search for a product and get its price
  app.interact(scrape_id, prompt="Search for iPhone 16 Pro Max")
  response = app.interact(scrape_id, prompt="Click on the first result and tell me the price")
  print(response.output)

  # 3. Stop the session
  app.stop_interaction(scrape_id)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const app = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: 'fc-YOUR-API-KEY',
  });

  // 1. Scrape Amazon's homepage
  const result = await app.scrape('https://www.amazon.com', { formats: ['markdown'] });
  const scrapeId = result.metadata?.scrapeId;

  // 2. Interact — search for a product and get its price
  await app.interact(scrapeId, { prompt: 'Search for iPhone 16 Pro Max' });
  const response = await app.interact(scrapeId, { prompt: 'Click on the first result and tell me the price' });
  console.log(response.output);

  // 3. Stop the session
  await app.stopInteraction(scrapeId);
  ```

  ```bash cURL theme={null}
  # 1. Scrape Amazon's homepage
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{"url": "https://www.amazon.com", "formats": ["markdown"]}')

  SCRAPE_ID=$(echo $RESPONSE | jq -r '.data.metadata.scrapeId')

  # 2. Interact — search for a product and get its price
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape/$SCRAPE_ID/interact" \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Search for iPhone 16 Pro Max"}'

  curl -s -X POST "https://api.firecrawl.dev/v2/scrape/$SCRAPE_ID/interact" \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Click on the first result and tell me the price"}'

  # 3. Stop the session
  curl -s -X DELETE "https://api.firecrawl.dev/v2/scrape/$SCRAPE_ID/interact"
  ```

  ```bash CLI theme={null}
  # 1. Scrape Amazon's homepage (scrape ID is saved automatically)
  firecrawl scrape https://www.amazon.com

  # 2. Interact — search for a product and get its price
  firecrawl interact "Search for iPhone 16 Pro Max"
  firecrawl interact "Click on the first result and tell me the price"

  # 3. Stop the session
  firecrawl interact stop
  ```
</CodeGroup>

<Accordion title="Response">
  ```json Response theme={null}
  {
    "success": true,
    "cdpUrl": "wss://browser.firecrawl.dev/...",
    "liveViewUrl": "https://liveview.firecrawl.dev/...",
    "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
    "output": "The iPhone 16 Pro Max (256GB) is priced at $1,199.00.",
    "exitCode": 0,
    "killed": false
  }
  ```
</Accordion>

***

## More capabilities

<CardGroup cols={2}>
  <Card title="Agent" icon="robot" href="/features/agent">
    Autonomous web data gathering powered by AI
  </Card>

  <Card title="Interact" icon="hand-pointer" href="/features/interact">
    Click, fill forms, extract dynamic content
  </Card>

  <Card title="Webhooks" icon="webhook" href="/webhooks">
    Async event delivery
  </Card>

  <Card title="Browser Sandbox" icon="browser" href="/features/browser">
    Managed browser sessions for interactive workflows
  </Card>

  <Card title="Map" icon="map" href="/features/map">
    Discover all URLs on a website
  </Card>

  <Card title="Crawl" icon="spider-web" href="/features/crawl">
    Recursively gather content from entire sites
  </Card>
</CardGroup>

***

## Resources

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/api-reference/v2-introduction">
    Complete API documentation with interactive examples
  </Card>

  <Card title="SDKs" icon="boxes-stacked" href="/sdks/overview">
    Python, Node.js, CLI, and community SDKs
  </Card>

  <Card title="Open Source" icon="github" href="/contributing/open-source-or-cloud">
    Self-host Firecrawl or contribute to the project
  </Card>

  <Card title="Integrations" icon="puzzle-piece" href="/developer-guides/llm-sdks-and-frameworks/openai">
    LangChain, LlamaIndex, OpenAI, and more
  </Card>
</CardGroup>

## Scrape — https://docs.firecrawl.dev/features/scrape
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Scrape

> Turn any url into clean data

Firecrawl converts web pages into markdown, ideal for LLM applications.

* It manages complexities: proxies, caching, rate limits, js-blocked content
* Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images
* Outputs clean markdown, structured data, screenshots or html.

For details, see the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

<Card title="Try it in the Playground" icon="play" href="https://www.firecrawl.dev/playground?endpoint=scrape">
  Test scraping in the interactive playground — no code required.
</Card>

<Note>If a request fails, see [Errors](/api-reference/errors) for the full catalog of error codes, causes, remedies, and retry guidance.</Note>

## Scraping a URL with Firecrawl

### /scrape endpoint

Used to scrape a URL and get its content.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )
  ```

  ```js Node theme={null}
  // npm install firecrawl

  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });
  ```

  ```bash CLI theme={null}
  # Install globally with npm
  npm install -g firecrawl

  # Authenticate (one-time setup)
  firecrawl login
  ```
</CodeGroup>

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  # Scrape a website:
  doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"])
  print(doc)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  // Scrape a website:
  const doc = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "html"]
    }'
  ```

  ```bash CLI theme={null}
  # Scrape a URL and get markdown
  firecrawl https://firecrawl.dev

  # With multiple formats (returns JSON)
  firecrawl https://firecrawl.dev --format markdown,html,links --pretty
  ```
</CodeGroup>

For more details about the parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

<Tip>
  **PDFs and documents:** `/scrape` auto-detects PDFs, DOCX, and other document types from URLs. Pass a PDF URL the same way you would any webpage -- Firecrawl parses it and returns clean markdown. For local files that are not accessible by URL, use [`/parse`](/features/parse) instead.

  ```python Python theme={null}
  doc = firecrawl.scrape("https://example.com/report.pdf", formats=["markdown"])
  print(doc.markdown)
  ```
</Tip>

<Info>
  Each scrape consumes 1 credit. Additional credits apply for certain options: JSON mode costs 4 additional credits per page, question and highlights formats cost 4 additional credits per page per format, enhanced proxy costs 4 additional credits per page, PII redaction costs 4 additional credits per page, PDF parsing costs 1 credit per PDF page, and audio or video extraction costs 4 additional credits per page.
</Info>

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json theme={null}
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200,
      "contentType": "text/html"
    }
  }
}
```

## Scrape Formats

You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:

* Markdown (`markdown`)
* Summary (`summary`)
* HTML (`html`) - cleaned version of the page's HTML
* Raw HTML (`rawHtml`) - unmodified HTML as received from the page
* Screenshot (`screenshot`, with options like `fullPage`, `quality`, `viewport`) — screenshot URLs expire after 24 hours
* Links (`links`)
* JSON (`json`) - structured output
* Images (`images`) - extract all image URLs from the page
* Branding (`branding`) - extract brand identity and design system
* Product (`product`) - extract a structured product (title, price, availability, variants) from product pages
* Audio (`audio`) - extract MP3 audio from supported video URLs, e.g. YouTube (returns a signed GCS URL, expires after 1 hour)
* Video (`video`) - extract best-quality video from supported video URLs, e.g. YouTube (returns a signed GCS URL, expires after 1 hour)
* Query (`query`, with `prompt` and optional `mode`) - ask a natural-language question about the page; the answer is returned in the `answer` field

Output keys will match the format you choose.

## Extract structured data

### /scrape (with json) endpoint

Used to extract structured data from scraped pages.

<Tip>
  Extracting products? For product pages, the [`product` format](#extract-product-data) returns structured product fields (title, price, availability, variants) deterministically — no LLM call and no schema to define. Reach for `json` when you need custom fields or non-product pages.
</Tip>

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from pydantic import BaseModel

  app = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  class CompanyInfo(BaseModel):
      company_mission: str
      supports_sso: bool
      is_open_source: bool
      is_in_yc: bool

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "schema": CompanyInfo.model_json_schema()
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import { Firecrawl } from "firecrawl";
  import { z } from "zod";

  const app = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR_API_KEY",
  });

  // Define schema to extract contents into
  const schema = z.object({
    company_mission: z.string(),
    supports_sso: z.boolean(),
    is_open_source: z.boolean(),
    is_in_yc: z.boolean()
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      schema: schema
    }],
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [ {
          "type": "json",
          "schema": {
            "type": "object",
            "properties": {
              "company_mission": {
                        "type": "string"
              },
              "supports_sso": {
                        "type": "boolean"
              },
              "is_open_source": {
                        "type": "boolean"
              },
              "is_in_yc": {
                        "type": "boolean"
              }
            },
            "required": [
              "company_mission",
              "supports_sso",
              "is_open_source",
              "is_in_yc"
            ]
          }
        } ]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  app = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  result = app.scrape(
      'https://firecrawl.dev',
      formats=[{
        "type": "json",
        "prompt": "Extract the company mission from the page."
      }],
      only_main_content=False,
      timeout=120000
  )

  print(result)
  ```

  ```js Node theme={null}
  import { Firecrawl } from "firecrawl";

  const app = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR_API_KEY",
  });

  const result = await app.scrape("https://firecrawl.dev", {
    formats: [{
      type: "json",
      prompt: "Extract the company mission from the page."
    }]
  });

  console.log(result);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://firecrawl.dev",
        "formats": [{
          "type": "json",
          "prompt": "Extract the company mission from the page."
        }]
      }'
  ```
</CodeGroup>

Output:

```json JSON theme={null}
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### JSON format options

When using the `json` format, pass an object inside `formats` with the following parameters:

* `schema`: JSON Schema for the structured output.
* `prompt`: Optional prompt to help guide extraction when a schema is present or when you prefer light guidance.

## Extract brand identity

### /scrape (with branding) endpoint

The branding format extracts comprehensive brand identity information from a webpage, including colors, fonts, typography, spacing, UI components, and more. This is useful for design system analysis, brand monitoring, or building tools that need to understand a website's visual identity.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key='fc-YOUR_API_KEY',
  )

  result = firecrawl.scrape(
      url='https://firecrawl.dev',
      formats=['branding']
  )

  print(result['branding'])
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const result = await firecrawl.scrape('https://firecrawl.dev', {
      formats: ['branding']
  });

  console.log(result.branding);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["branding"]
    }'
  ```
</CodeGroup>

### Response

The branding format returns a comprehensive `BrandingProfile` object with the following structure:

```json Output theme={null}
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Branding Profile Structure

The `branding` object contains the following properties:

* `colorScheme`: The detected color scheme (`"light"` or `"dark"`)
* `logo`: URL of the primary logo
* `colors`: Object containing brand colors:
  * `primary`, `secondary`, `accent`: Main brand colors
  * `background`, `textPrimary`, `textSecondary`: UI colors
  * `link`, `success`, `warning`, `error`: Semantic colors
* `fonts`: Array of font families used on the page
* `typography`: Detailed typography information:
  * `fontFamilies`: Primary, heading, and code font families
  * `fontSizes`: Size definitions for headings and body text
  * `fontWeights`: Weight definitions (light, regular, medium, bold)
  * `lineHeights`: Line height values for different text types
* `spacing`: Spacing and layout information:
  * `baseUnit`: Base spacing unit in pixels
  * `borderRadius`: Default border radius
  * `padding`, `margins`: Spacing values
* `components`: UI component styles:
  * `buttonPrimary`, `buttonSecondary`: Button styles
  * `input`: Input field styles
* `icons`: Icon style information
* `images`: Brand images (logo, favicon, og:image)
* `animations`: Animation and transition settings
* `layout`: Layout configuration (grid, header/footer heights)
* `personality`: Brand personality traits (tone, energy, target audience)

### Combining with other formats

You can combine the branding format with other formats to get comprehensive page data:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key='fc-YOUR_API_KEY',
  )

  result = firecrawl.scrape(
      url='https://firecrawl.dev',
      formats=['markdown', 'branding', 'screenshot']
  )

  print(result['markdown'])
  print(result['branding'])
  print(result['screenshot'])
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const result = await firecrawl.scrape('https://firecrawl.dev', {
      formats: ['markdown', 'branding', 'screenshot']
  });

  console.log(result.markdown);
  console.log(result.branding);
  console.log(result.screenshot);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": ["markdown", "branding", "screenshot"]
    }'
  ```
</CodeGroup>

## Extract product data

The `product` format extracts a structured product **deterministically** — the same kind of structured output as the [`json` format](#extract-structured-data), but without an LLM call or a schema you define, purpose-built for product pages. If you've been pulling product fields with a `json` schema, use `formats: ["product"]` instead — it's faster and cheaper, just limited to products.

It returns a `product` object with title, brand, category, description, and variants — where each variant carries price, original price, availability, and images — useful for price monitoring, catalog ingestion, or comparison-shopping tools.

### /scrape (with product) endpoint

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key='fc-YOUR_API_KEY',
  )

  result = firecrawl.scrape(
      url='https://example.com/products/wireless-headphones',
      formats=['product']
  )

  print(result['product'])
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const result = await firecrawl.scrape('https://example.com/products/wireless-headphones', {
      formats: ['product']
  });

  console.log(result.product);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com/products/wireless-headphones",
      "formats": ["product"]
    }'
  ```
</CodeGroup>

### Response

The product format returns a `product` object with the following structure:

```json Output theme={null}
{
  "success": true,
  "data": {
    "product": {
      "title": "Wireless Noise-Cancelling Headphones",
      "brand": "Acme",
      "category": "Electronics > Audio > Headphones",
      "url": "https://example.com/products/wireless-headphones",
      "description": "Over-ear wireless headphones with active noise cancellation, 30-hour battery life, and plush memory-foam ear cushions for all-day comfort.",
      "variants": [
        {
          "id": "wireless-headphones-black",
          "sku": "ACME-WH-BLACK",
          "title": "Wireless Noise-Cancelling Headphones — Black",
          "values": {
            "color": "Black"
          },
          "price": {
            "amount": 199.99,
            "currency": "USD",
            "formatted": "$199.99"
          },
          "sale": {
            "originalPrice": {
              "amount": 249.99,
              "currency": "USD",
              "formatted": "$249.99"
            }
          },
          "availability": {
            "inStock": true,
            "text": "In Stock"
          },
          "images": [
            {
              "url": "https://example.com/images/headphones-black.jpg",
              "alt": "Wireless Noise-Cancelling Headphones — Black"
            }
          ]
        }
      ]
    }
  }
}
```

### Product object structure

The `product` object contains the following properties:

* `title`: The product name
* `brand`: The product brand (optional)
* `category`: The product category (optional)
* `url`: The canonical URL of the product
* `description`: The product description (optional)
* `variants`: Array of product variants. Pricing, availability, and images live on each variant — a single-SKU product still returns exactly one variant carrying these. Each variant has:
  * `id`, `sku`, `title`: variant identifiers and label (all optional)
  * `values`: a map of option name to value, e.g. `{ "color": "Charcoal" }` (optional)
  * `price`: the current price object (optional):
    * `amount`: The numeric price value
    * `currency`: The currency code, reported only when the page sources it (optional)
    * `formatted`: The price as displayed on the page (optional)
  * `sale`: present only when the variant is discounted (optional). Contains:
    * `originalPrice`: The original (pre-discount) price, same shape as `price`
  * `availability`: availability information, always present on a variant:
    * `inStock`: Whether the variant is in stock
    * `text`: The raw availability text from the page (optional)
  * `images`: array of variant images, each with a `url` and optional `alt` text (optional)

### How product extraction works

The product format extracts the product deterministically from on-page structured data — no LLM is involved. It merges multiple sources by priority: **JSON-LD > schema.org microdata > RDFa > embedded state (`__NEXT_DATA__`/Nuxt/Apollo/Redux/Remix) > AliExpress `runParams` > GA4 `dataLayer` > OpenGraph/`<meta>`**. The merge is identity-aware, so fields from different products are never combined. Currency is reported only when the page sources it.

<Note>
  Product extraction is fail-closed: ambiguous pages yield no product, and weaker sources such as OpenGraph only contribute when a price is present. On a page with no extractable product, the response omits the `product` object and adds a `warning` (e.g. "No product found...").
</Note>

<Note>
  **Self-hosting:** the `product` format is backed by a dedicated product-extraction service. On Firecrawl Cloud it works out of the box. If you self-host, set `PRODUCT_EXTRACTION_SERVICE_URL` to point at that service — when it is unset, requesting the `product` format returns a warning and no product (the same pattern the audio/video formats use for their service).
</Note>

### Combining with other formats

You can combine the product format with other formats to get comprehensive page data:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key='fc-YOUR_API_KEY',
  )

  result = firecrawl.scrape(
      url='https://example.com/products/wireless-headphones',
      formats=['markdown', 'product']
  )

  print(result['markdown'])
  print(result['product'])
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const result = await firecrawl.scrape('https://example.com/products/wireless-headphones', {
      formats: ['markdown', 'product']
  });

  console.log(result.markdown);
  console.log(result.product);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com/products/wireless-headphones",
      "formats": ["markdown", "product"]
    }'
  ```
</CodeGroup>

## Audio extraction

The `audio` format extracts audio from supported websites (e.g. YouTube) as MP3 files and returns a signed Google Cloud Storage URL. This is useful for building audio processing pipelines, transcription services, or podcast tools.

<Info>
  Audio extraction costs 5 credits per page (1 base + 4 additional).
</Info>

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape("https://www.youtube.com/watch?v=dQw4w9WgXcQ", formats=["audio"])
  print(doc.audio)  # Signed GCS URL to the MP3 file
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://www.youtube.com/watch?v=dQw4w9WgXcQ', {
    formats: ['audio']
  });

  console.log(doc.audio); // Signed GCS URL to the MP3 file
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
      "formats": ["audio"]
    }'
  ```
</CodeGroup>

## Video extraction

The `video` format extracts best-quality video from supported websites (e.g. YouTube) and returns a signed Google Cloud Storage URL. This is useful for building video processing pipelines, moderation tools, or media archiving workflows.

<Info>
  Video extraction costs 5 credits per page (1 base + 4 additional).
</Info>

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape("https://www.youtube.com/watch?v=dQw4w9WgXcQ", formats=["video"])
  print(doc.video)  # Signed GCS URL to the video file
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://www.youtube.com/watch?v=dQw4w9WgXcQ', {
    formats: ['video']
  });

  console.log(doc.video); // Signed GCS URL to the video file
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
      "formats": ["video"]
    }'
  ```
</CodeGroup>

<span id="question-format" />

## Question format

Use the `question` format to ask a natural-language question about the page. Firecrawl returns the answer in the response's `answer` field.

<Info>
  The `question` format costs 5 credits per page (1 base + 4 additional for the LLM call).
</Info>

Options inside the format object:

* `question` (required for `type: "question"`): the question to answer. Maximum 10,000 characters.

You can combine `question` with other formats — for example, request `markdown` and `question` together to get page content and an answer in a single call.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape(
      "https://firecrawl.dev",
      formats=[{"type": "question", "question": "What is Firecrawl?"}],
  )
  print(doc.answer)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://firecrawl.dev', {
    formats: [{ type: 'question', question: 'What is Firecrawl?' }],
  });

  console.log(doc.answer);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": [
        { "type": "question", "question": "What is Firecrawl?" }
      ]
    }'
  ```
</CodeGroup>

The `question` format is also available in `/search` via `scrapeOptions`, which runs the same extraction across each search result.

<span id="highlights-format" />

## Highlights format

Use the `highlights` format to find relevant source text from the page. Firecrawl returns the selected text in the response's `highlights` field.

<Info>
  The `highlights` format costs 5 credits per page (1 base + 4 additional for the LLM call).
</Info>

Options inside the format object:

* `query` (required for `type: "highlights"`): the source-text selection request. Maximum 10,000 characters.

You can combine `highlights` with other formats — for example, request `markdown` and `highlights` together to get page content and source text in a single call.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape(
      "https://firecrawl.dev",
      formats=[{"type": "highlights", "query": "What is Firecrawl?"}],
  )
  print(doc.highlights)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://firecrawl.dev', {
    formats: [{ type: 'highlights', query: 'What is Firecrawl?' }],
  });

  console.log(doc.highlights);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://firecrawl.dev",
      "formats": [
        { "type": "highlights", "query": "What is Firecrawl?" }
      ]
    }'
  ```
</CodeGroup>

The `highlights` format is also available in `/search` via `scrapeOptions`, which runs the same extraction across each search result.

## PII redaction

Set `redactPII: true` to redact personally identifiable information from returned markdown. The `markdown` field contains the redacted result.

See [PII Redaction](/features/pii-redaction) for SDK, cURL, CLI, and MCP examples.

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

<Tip>
  **We recommend [Interact](/features/interact) over actions: our newer, more powerful way to interact with scraped pages.**

  Interact runs as a stateful browser session that stays alive across calls, so you can drive a page turn-by-turn with either:

  * **Natural language** for flexible, non-deterministic flows. e.g. *“search for ‘wireless headphones’, filter to 4+ stars under \$200, and return the results”*.
  * **Playwright or agent-browser code** for deterministic steps. e.g. `await page.click('#export')`.

  Interact also supports profiles, persistent sessions, and a live embeddable browser view (with an interactive mode where end users can drive the browser themselves).
</Tip>

Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.

It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

### Example

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape(
      url="https://example.com/login",
      formats=["markdown"],
      actions=[
          {"type": "write", "text": "john@example.com"},
          {"type": "press", "key": "Tab"},
          {"type": "write", "text": "secret"},
          {"type": "click", "selector": 'button[type="submit"]'},
          {"type": "wait", "milliseconds": 1500},
          {"type": "screenshot", "full_page": True},
      ],
  )

  print(doc.markdown, doc.screenshot)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://example.com/login', {
    formats: ['markdown'],
    actions: [
      { type: 'write', text: 'john@example.com' },
      { type: 'press', key: 'Tab' },
      { type: 'write', text: 'secret' },
      { type: 'click', selector: 'button[type="submit"]' },
      { type: 'wait', milliseconds: 1500 },
      { type: 'screenshot', fullPage: true },
    ],
  });

  console.log(doc.markdown, doc.screenshot);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/scrape \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://example.com/login",
        "formats": ["markdown"],
        "actions": [
          { "type": "write", "text": "john@example.com" },
          { "type": "press", "key": "Tab" },
          { "type": "write", "text": "secret" },
          { "type": "click", "selector": "button[type=\"submit\"]" },
          { "type": "wait", "milliseconds": 1500 },
          { "type": "screenshot", "fullPage": true },
        ],
    }'
  ```
</CodeGroup>

### Output

<CodeGroup>
  ```json JSON theme={null}
  {
    "success": true,
    "data": {
      "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",
      "actions": {
        "screenshots": [
          "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"
        ],
        "scrapes": [
          {
            "url": "https://www.firecrawl.dev/",
            "html": "<html><body><h1>Firecrawl</h1></body></html>"
          }
        ]
      },
      "metadata": {
        "title": "Home - Firecrawl",
        "description": "Firecrawl crawls and converts any website into clean markdown.",
        "language": "en",
        "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Turn any website into LLM-ready data.",
        "ogUrl": "https://www.firecrawl.dev/",
        "ogImage": "https://www.firecrawl.dev/og.png?123",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "http://google.com",
        "statusCode": 200
      }
    }
  }
  ```
</CodeGroup>

For workflows that require richer browser control after scraping, such as authenticated sessions, multi-step navigation, or a live view of the page, we recommend [Interact](/features/interact) over extending the actions array.

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences.

### How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

### Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  doc = firecrawl.scrape('https://example.com',
      formats=['markdown'],
      location={
          'country': 'US',
          'languages': ['en']
      }
  )

  print(doc)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const doc = await firecrawl.scrape('https://example.com', {
    formats: ['markdown'],
    location: { country: 'US', languages: ['en'] },
  });

  console.log(doc.metadata);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "formats": ["markdown"],
      "location": { "country": "US", "languages": ["en"] }
    }'
  ```
</CodeGroup>

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

## Caching and maxAge

To make requests faster, Firecrawl serves results from cache by default when a recent copy is available.

* **Default freshness window**: `maxAge = 172800000` ms (2 days). If a cached page is newer than this, it’s returned instantly; otherwise, the page is scraped and then cached.
* **Performance**: This can speed up scrapes by up to 5x when data doesn’t need to be ultra-fresh.
* **Always fetch fresh**: Set `maxAge` to `0`. Note that this bypasses the cache entirely, so every request goes through the full scraping pipeline, meaning that the request will take longer to complete and is more likely to fail. Use a non-zero `maxAge` if freshness on every request is not critical.
* **Avoid storing**: Set `storeInCache` to `false` if you don’t want Firecrawl to cache/store results for this request.
* **Cache-only lookup**: Set `minAge` to perform a cache-only lookup without triggering a fresh scrape. The value is in milliseconds and specifies the minimum age the cached data must be. If no cached data is found, a `404` with error code `SCRAPE_NO_CACHED_DATA` is returned. Set `minAge` to `1` to accept any cached data regardless of age.
* **Change tracking**: Requests that include `changeTracking` bypass the cache, so `maxAge` is ignored.
* **Credits**: Cached results still cost 1 credit per page. Caching improves speed, not credit usage.

Example (force fresh content):

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  doc = firecrawl.scrape(url='https://example.com', max_age=0, formats=['markdown'])
  print(doc)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', { maxAge: 0, formats: ['markdown'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "maxAge": 0,
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

Example (use a 10-minute cache window):

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  doc = firecrawl.scrape(url='https://example.com', max_age=600000, formats=['markdown', 'html'])
  print(doc)
  ```

  ```js Node theme={null}

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const doc = await firecrawl.scrape('https://example.com', { maxAge: 600000, formats: ['markdown', 'html'] });
  console.log(doc);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "maxAge": 600000,
      "formats": ["markdown", "html"]
    }'
  ```
</CodeGroup>

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

### How it works

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.

The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  job = firecrawl.batch_scrape([
      "https://firecrawl.dev",
      "https://docs.firecrawl.dev",
  ], formats=["markdown"], poll_interval=2, wait_timeout=120)

  print(job)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const job = await firecrawl.batchScrape([
    'https://firecrawl.dev',
    'https://docs.firecrawl.dev',
  ], { options: { formats: ['markdown'] }, pollInterval: 2, timeout: 120 });

  console.log(job);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/batch/scrape" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "urls": ["https://firecrawl.dev", "https://docs.firecrawl.dev"],
      "formats": ["markdown"]
    }'
  ```
</CodeGroup>

### Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### Synchronous

```json Completed theme={null}
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Asynchronous

You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.

```json theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Enhanced Mode

For complex websites, Firecrawl offers enhanced mode that provides better success rates while maintaining privacy.

Learn more about [Enhanced Mode](/features/enhanced-mode).

## Zero Data Retention (ZDR)

Firecrawl supports Zero Data Retention (ZDR) for teams with strict data handling requirements. When enabled, Firecrawl will not persist any page content or extracted data beyond the lifetime of the request.

To enable ZDR, set `zeroDataRetention: true` in your request:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

ZDR is available on Enterprise plans and must be enabled for your team. Visit [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) to get started.

ZDR adds **1 additional credit per page** on top of the base scrape cost.

<Note>
  Screenshots are not available in ZDR mode. Because screenshots require uploading to persistent storage, they are incompatible with the ZDR guarantee. Requests that include both `zeroDataRetention: true` and a `screenshot` format will return an error.
</Note>

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

## Crawl — https://docs.firecrawl.dev/features/crawl
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Crawl

> Recursively crawl a website and get content from every page

Crawl submits a URL to Firecrawl and recursively discovers and scrapes every reachable subpage. It handles sitemaps, JavaScript rendering, and rate limits automatically, returning clean markdown or structured data for each page.

* Discovers pages via sitemap and recursive link traversal
* Supports path filtering, depth limits, and subdomain/external link control
* Returns results via polling, WebSocket, or webhook

<Card title="Try it in the Playground" icon="play" href="https://www.firecrawl.dev/playground?endpoint=crawl">
  Test crawling in the interactive playground — no code required.
</Card>

## Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )
  ```

  ```js Node theme={null}
  // npm install firecrawl

  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });
  ```

  ```bash CLI theme={null}
  # Install globally with npm
  npm install -g firecrawl

  # Authenticate (one-time setup)
  firecrawl login
  ```
</CodeGroup>

## Basic usage

Submit a crawl job by calling `POST /v2/crawl` with a starting URL. The endpoint returns a job ID that you use to poll for results.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  docs = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=10)
  print(docs)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const docs = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 10 });
  console.log(docs);
  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/crawl" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
  ```

  ```bash CLI theme={null}
  # Start a crawl job (returns job ID)
  firecrawl crawl https://firecrawl.dev

  # Wait for completion with progress
  firecrawl crawl https://firecrawl.dev --wait --progress --limit 100
  ```
</CodeGroup>

<Info>
  Each page crawled consumes 1 credit. The default crawl `limit` is 10,000 pages. Before starting, the crawl endpoint checks that your remaining credits can cover the `limit` — if not, it returns a **402 (Payment Required)** error. Set a lower `limit` to match your intended crawl size (e.g. `limit: 100`) to avoid this. Additional credits apply for certain options: JSON mode costs 4 additional credits per page, enhanced proxy costs 4 additional credits per page, and PDF parsing costs 1 credit per PDF page.
</Info>

### Scrape options

All options from the [Scrape endpoint](/api-reference/endpoint/scrape) are available in crawl via `scrapeOptions` (JS) / `scrape_options` (Python). These apply to every page the crawler scrapes, including formats, proxy, caching, actions, location, and tags.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

  # Crawl with scrape options
  response = firecrawl.crawl('https://example.com',
      limit=100,
      scrape_options={
          'formats': [
              'markdown',
              { 'type': 'json', 'schema': { 'type': 'object', 'properties': { 'title': { 'type': 'string' } } } }
          ],
          'proxy': 'auto',
          'max_age': 600000,
          'only_main_content': True
      }
  )
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR_API_KEY' });

  // Crawl with scrape options
  const crawlResponse = await firecrawl.crawl('https://example.com', {
    limit: 100,
    scrapeOptions: {
      formats: [
        'markdown',
        {
          type: 'json',
          schema: { type: 'object', properties: { title: { type: 'string' } } },
        },
      ],
      proxy: 'auto',
      maxAge: 600000,
      onlyMainContent: true,
    },
  });
  ```
</CodeGroup>

## Checking crawl status

Use the job ID to poll for the crawl status and retrieve results.

<CodeGroup>
  ```python Python theme={null}
  status = firecrawl.get_crawl_status("<crawl-id>")
  print(status)
  ```

  ```js Node theme={null}
  const status = await firecrawl.getCrawlStatus("<crawl-id>");
  console.log(status);
  ```

  ```bash cURL theme={null}
  # After starting a crawl, poll status by jobId
  curl -s -X GET "https://api.firecrawl.dev/v2/crawl/<jobId>" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY"
  ```

  ```bash CLI theme={null}
  # Check crawl status using job ID
  firecrawl crawl <job-id>
  ```
</CodeGroup>

<Note>
  Job results are available via the API for 24 hours after completion. After this period, you can still view your crawl history and results in the [activity logs](https://www.firecrawl.dev/app/logs).
</Note>

<Note>
  Pages in the crawl results `data` array are pages that Firecrawl successfully scraped, even if the target site returned an HTTP error like 404. The `metadata.statusCode` field shows the HTTP status code from the target site. To retrieve pages that Firecrawl itself failed to scrape (e.g. network errors, timeouts, or robots.txt blocks), use the dedicated [Get Crawl Errors](/api-reference/endpoint/crawl-get-errors) endpoint (`GET /crawl/{id}/errors`).
</Note>

### Response handling

The response varies based on the crawl's status. For incomplete or large responses exceeding 10MB, a `next` URL parameter is provided. You must request this URL to retrieve the next 10MB of data. If the `next` parameter is absent, it indicates the end of the crawl data.

<Info>
  The `skip` and `next` parameters are only relevant when hitting the API directly.
  If you're using the SDK, pagination is handled automatically and all
  results are returned at once.
</Info>

<CodeGroup>
  ```json Scraping theme={null}
  {
    "status": "scraping",
    "total": 36,
    "completed": 10,
    "creditsUsed": 10,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=10",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```

  ```json Completed theme={null}
  {
    "status": "completed",
    "total": 36,
    "completed": 36,
    "creditsUsed": 36,
    "expiresAt": "2024-00-00T00:00:00.000Z",
    "next": "https://api.firecrawl.dev/v2/crawl/123-456-789?skip=26",
    "data": [
      {
        "markdown": "[Firecrawl Docs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
        "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
        "metadata": {
          "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
          "language": "en",
          "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
          "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
          "ogLocaleAlternate": [],
          "statusCode": 200
        }
      },
      ...
    ]
  }
  ```
</CodeGroup>

## SDK methods

There are two ways to use crawl with the SDK.

### Crawl and wait

The `crawl` method waits for the crawl to complete and returns the full response. It handles pagination automatically. This is recommended for most use cases.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl
  from firecrawl.types import ScrapeOptions

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Crawl a website:
  crawl_status = firecrawl.crawl(
    'https://firecrawl.dev', 
    limit=100, 
    scrape_options=ScrapeOptions(formats=['markdown', 'html']),
    poll_interval=30
  )
  print(crawl_status)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
    limit: 100,
    scrapeOptions: {
      formats: ['markdown', 'html'],
    }
  })

  console.log(crawlResponse)
  ```
</CodeGroup>

The response includes the crawl status and all scraped data:

<CodeGroup>
  ```bash Python theme={null}
  success=True
  status='completed'
  completed=100
  total=100
  creditsUsed=100
  expiresAt=datetime.datetime(2025, 4, 23, 19, 21, 17, tzinfo=TzInfo(UTC))
  next=None
  data=[
    Document(
      markdown='[Day 7 - Launch Week III.Integrations DayApril 14th to 20th](...',
      metadata={
        'title': '15 Python Web Scraping Projects: From Beginner to Advanced',
        ...
        'scrapeId': '97dcf796-c09b-43c9-b4f7-868a7a5af722',
        'sourceURL': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
        'url': 'https://www.firecrawl.dev/blog/python-web-scraping-projects',
        'statusCode': 200
      }
    ),
    ...
  ]
  ```

  ```js Node theme={null}
  {
    success: true,
    status: "completed",
    completed: 100,
    total: 100,
    creditsUsed: 100,
    expiresAt: "2025-04-23T19:28:45.000Z",
    data: [
      {
        markdown: "[Day 7 - Launch Week III.Integrations DayApril ...",
        html: `<!DOCTYPE html><html lang="en" class="light" style="color...`,
        metadata: [Object],
      },
      ...
    ]
  }
  ```
</CodeGroup>

### Start and check later

The `startCrawl` / `start_crawl` method returns immediately with a crawl ID. You then poll for status manually. This is useful for long-running crawls or custom polling logic.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
  print(job)

  # Check the status of the crawl
  status = firecrawl.get_crawl_status(job.id)
  print(status)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
  console.log(id);

  // Check the status of the crawl
  const status = await firecrawl.getCrawlStatus(id);
  console.log(status);

  ```

  ```bash cURL theme={null}
  curl -s -X POST "https://api.firecrawl.dev/v2/crawl" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 10
    }'
  ```

  ```bash CLI theme={null}
  # Start crawl (async, returns job ID immediately)
  firecrawl crawl https://firecrawl.dev --limit 100

  # Then check status later
  firecrawl crawl <job-id>
  ```
</CodeGroup>

The initial response returns the job ID:

```json theme={null}
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

## Real-time results with WebSocket

The watcher method provides real-time updates as pages are crawled. Start a crawl, then subscribe to events for immediate data processing.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from firecrawl import AsyncFirecrawl

  async def main():
      firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

      # Start a crawl first
      started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

      # Watch updates (snapshots) until terminal status
      async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
          if snapshot.status == "completed":
              print("DONE", snapshot.status)
              for doc in snapshot.data:
                  print("DOC", doc.metadata.source_url if doc.metadata else None)
          elif snapshot.status == "failed":
              print("ERR", snapshot.status)
          else:
              print("STATUS", snapshot.status, snapshot.completed, "/", snapshot.total)

  asyncio.run(main())
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

  // Start a crawl and then watch it
  const { id } = await firecrawl.startCrawl('https://mendable.ai', {
    excludePaths: ['blog/*'],
    limit: 5,
  });

  const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

  watcher.on('document', (doc) => {
    console.log('DOC', doc);
  });

  watcher.on('error', (err) => {
    console.error('ERR', err?.error || err);
  });

  watcher.on('done', (state) => {
    console.log('DONE', state.status);
  });

  // Begin watching (WS with HTTP fallback)
  await watcher.start();
  ```
</CodeGroup>

## Webhooks

You can configure webhooks to receive real-time notifications as your crawl progresses. This allows you to process pages as they are scraped instead of waiting for the entire crawl to complete.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Event types

| Event             | Description                              |
| ----------------- | ---------------------------------------- |
| `crawl.started`   | Fires when the crawl begins              |
| `crawl.page`      | Fires for each page successfully scraped |
| `crawl.completed` | Fires when the crawl finishes            |
| `crawl.failed`    | Fires if the crawl encounters an error   |

### Payload

```json theme={null}
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Page data for 'page' events
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Verifying webhook signatures

Every webhook request from Firecrawl includes an `X-Firecrawl-Signature` header containing an HMAC-SHA256 signature. Always verify this signature to ensure the webhook is authentic and has not been tampered with.

1. Get your webhook secret from the [Advanced tab](https://www.firecrawl.dev/app/settings?tab=advanced) of your account settings
2. Extract the signature from the `X-Firecrawl-Signature` header
3. Compute HMAC-SHA256 of the raw request body using your secret
4. Compare with the signature header using a timing-safe function

<Warning>
  Never process a webhook without verifying its signature first. The `X-Firecrawl-Signature` header contains the signature in the format: `sha256=abc123def456...`
</Warning>

For complete implementation examples in JavaScript and Python, see the [Webhook Security documentation](/webhooks/security). For comprehensive webhook documentation including detailed event payloads, payload structure, advanced configuration, and troubleshooting, see the [Webhooks documentation](/webhooks/overview).

## Configuration reference

The full set of parameters available when submitting a crawl job:

| Parameter               | Type       | Default     | Description                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ---------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                   | `string`   | (required)  | The starting URL to crawl from                                                                                                                                                                                                                                                                                                                                       |
| `limit`                 | `integer`  | `10000`     | Maximum number of pages to crawl                                                                                                                                                                                                                                                                                                                                     |
| `maxDiscoveryDepth`     | `integer`  | (none)      | Maximum depth from the root URL based on link-discovery hops, not the number of `/` segments in the URL. Each time a new URL is found on a page, it is assigned a depth one higher than the page it was discovered on. The root site and sitemapped pages have a discovery depth of 0. Pages at the max depth are still scraped, but links on them are not followed. |
| `includePaths`          | `string[]` | (none)      | URL pathname regex patterns to include. Only matching paths are crawled.                                                                                                                                                                                                                                                                                             |
| `excludePaths`          | `string[]` | (none)      | URL pathname regex patterns to exclude from the crawl                                                                                                                                                                                                                                                                                                                |
| `regexOnFullURL`        | `boolean`  | `false`     | Match `includePaths`/`excludePaths` against the full URL (including query parameters) instead of just the pathname                                                                                                                                                                                                                                                   |
| `crawlEntireDomain`     | `boolean`  | `false`     | Follow internal links to sibling or parent URLs, not just child paths                                                                                                                                                                                                                                                                                                |
| `allowSubdomains`       | `boolean`  | `false`     | Follow links to subdomains of the main domain                                                                                                                                                                                                                                                                                                                        |
| `allowExternalLinks`    | `boolean`  | `false`     | Follow links to external websites                                                                                                                                                                                                                                                                                                                                    |
| `sitemap`               | `string`   | `"include"` | Sitemap handling: `"include"` (default), `"skip"`, or `"only"`                                                                                                                                                                                                                                                                                                       |
| `ignoreQueryParameters` | `boolean`  | `false`     | Avoid re-scraping the same path with different query parameters                                                                                                                                                                                                                                                                                                      |
| `ignoreRobotsTxt`       | `boolean`  | `false`     | Ignore the website's robots.txt rules. **Enterprise only** — contact [support@firecrawl.com](mailto:support@firecrawl.com) to enable.                                                                                                                                                                                                                                |
| `robotsUserAgent`       | `string`   | (none)      | Custom User-Agent string for robots.txt evaluation. When set, robots.txt is fetched with this User-Agent and rules are matched against it instead of the default. **Enterprise only** — contact [support@firecrawl.com](mailto:support@firecrawl.com) to enable.                                                                                                     |
| `delay`                 | `number`   | (none)      | Delay in seconds between scrapes to respect rate limits. Setting this forces concurrency to 1.                                                                                                                                                                                                                                                                       |
| `maxConcurrency`        | `integer`  | (none)      | Maximum concurrent scrapes. Defaults to your team's concurrency limit.                                                                                                                                                                                                                                                                                               |
| `scrapeOptions`         | `object`   | (none)      | Options applied to every scraped page (formats, proxy, caching, actions, etc.)                                                                                                                                                                                                                                                                                       |
| `webhook`               | `object`   | (none)      | Webhook configuration for real-time notifications                                                                                                                                                                                                                                                                                                                    |
| `prompt`                | `string`   | (none)      | Natural language prompt to generate crawl options. Explicitly set parameters override generated equivalents.                                                                                                                                                                                                                                                         |

## Important details

<Warning>
  By default, crawl ignores sublinks that are not children of the URL you provide. For example, `website.com/other-parent/blog-1` would not be returned if you crawled `website.com/blogs/`. Use the `crawlEntireDomain` parameter to include sibling and parent paths. To crawl subdomains like `blog.website.com` when crawling `website.com`, use the `allowSubdomains` parameter.
</Warning>

* **Sitemap discovery**: By default, the crawler includes the website's sitemap to discover URLs (`sitemap: "include"`). If you set `sitemap: "skip"`, only pages reachable through HTML links from the root URL are found. Assets like PDFs or deeply nested pages listed in the sitemap but not directly linked from HTML will be missed. For maximum coverage, keep the default setting.
* **Credit usage**: Each page crawled costs 1 credit. JSON mode adds 4 credits per page, enhanced proxy adds 4 credits per page, and PDF parsing costs 1 credit per PDF page.
* **Result expiration**: Job results are available via the API for 24 hours after completion. After that, view results in the [activity logs](https://www.firecrawl.dev/app/logs).
* **Crawl errors**: The `data` array contains pages Firecrawl successfully scraped. Use the [Get Crawl Errors](/api-reference/endpoint/crawl-get-errors) endpoint to retrieve pages that failed due to network errors, timeouts, or robots.txt blocks.
* **Non-deterministic results**: Crawl results may vary between runs of the same configuration. Pages are scraped concurrently, so the order in which links are discovered depends on network timing and which pages finish loading first. This means different branches of a site may be explored to different extents near the depth boundary, especially at higher `maxDiscoveryDepth` values. To get more deterministic results, set `maxConcurrency` to `1` or use `sitemap: "only"` if the site has a comprehensive sitemap.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

## Search — https://docs.firecrawl.dev/features/search
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Search the web and get full content from results

Search the web and get clean, structured content from every result in a single API call. Pass a query to `/search` and Firecrawl returns titles, descriptions, and URLs. Add `scrapeOptions` to also retrieve full-page markdown, HTML, links, or screenshots for each result.

For the full parameter list, see the [Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search).

<Card title="Try it in the Playground" icon="play" href="https://www.firecrawl.dev/playground?endpoint=search">
  Test searching in the interactive playground — no code required.
</Card>

## Performing a Search with Firecrawl

### /search endpoint

Used to perform web searches and optionally retrieve content from the results.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )
  ```

  ```js Node theme={null}
  // npm install firecrawl

  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });
  ```

  ```bash CLI theme={null}
  # Install globally with npm
  npm install -g firecrawl

  # Authenticate (one-time setup)
  firecrawl login
  ```
</CodeGroup>

### Basic Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  results = firecrawl.search(
      query="firecrawl",
      limit=3,
  )
  print(results)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer $FIRECRAWL_API_KEY" for higher rate limits:
  curl -s -X POST "https://api.firecrawl.dev/v2/search" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl",
      "limit": 3
    }'
  ```

  ```bash CLI theme={null}
  # Search the web
  firecrawl search "firecrawl web scraping" --limit 5 --pretty
  ```
</CodeGroup>

### Response

SDKs will return the data object directly. cURL will return the complete payload.

```json JSON theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

<Note>
  **SDK users:** search results are grouped by source type, not under a generic `.data` array. Access web results with `result.web`, news with `result.news`, and images with `result.images`.

  ```python Python theme={null}
  result = firecrawl.search("query")
  for item in result.web or []:
      print(item.url, item.title)
  ```

  ```js JavaScript theme={null}
  const result = await firecrawl.search("query");
  for (const item of result.web ?? []) {
    console.log(item.url, item.title);
  }
  ```
</Note>

## Search result types

In addition to regular web results, Search supports specialized result types via the `sources` parameter:

* `web`: standard web results (default)
* `news`: news-focused results
* `images`: image search results

You can request multiple sources in a single call (e.g., `sources: ["web", "news"]`). When you do, the `limit` parameter applies **per source type** — so `limit: 5` with `sources: ["web", "news"]` returns up to 5 web results and up to 5 news results (10 total). If you need different parameters per source (for example, different `limit` values or different `scrapeOptions`), make separate calls instead.

## Search Categories

Filter search results by specific categories using the `categories` parameter:

* `github`: Search within GitHub repositories, code, issues, and documentation
* `research`: Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
* `pdf`: Search for PDFs

### GitHub Category Search

Search specifically within GitHub repositories:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Research Category Search

Search academic and research websites:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "machine learning transformers",
    "categories": ["research"],
    "limit": 10
  }'
```

### Mixed Category Search

Combine multiple categories in one search:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "neural networks",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

## Domain Filters

Use `includeDomains` to restrict search results to specific domains, or `excludeDomains` to remove specific domains from the search. These fields add `site:` and `-site:` operators to the query internally, so pass domains only without a protocol or path.

<Note>
  `includeDomains` and `excludeDomains` are mutually exclusive. Use one or the other in a single request.
</Note>

### Include Domains

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping",
    "includeDomains": ["firecrawl.dev", "docs.firecrawl.dev"],
    "limit": 10
  }'
```

### Exclude Domains

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping tools",
    "excludeDomains": ["example.com"],
    "limit": 10
  }'
```

### Category Response Format

Each search result includes a `category` field indicating its source:

```json theme={null}
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Neural Network Implementation",
        "description": "A PyTorch implementation of neural networks",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Advances in Neural Network Architecture",
        "description": "Research paper on neural network improvements",
        "category": "research"
      }
    ]
  }
}
```

Examples:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### HD Image Search with Size Filtering

Use images operators to find high-resolution images:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'
```

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Common HD resolutions:**

* `imagesize:1920x1080` - Full HD (1080p)
* `imagesize:2560x1440` - QHD (1440p)
* `imagesize:3840x2160` - 4K UHD
* `larger:1920x1080` - HD and above
* `larger:2560x1440` - QHD and above

## Search with Content Scraping

Search and retrieve content from the search results in one operation.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR_API_KEY",
  )

  # Search and scrape content
  results = firecrawl.search(
      "firecrawl web scraping",
      limit=3,
      scrape_options={
          "formats": ["markdown", "links"]
      }
  )
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const results = await firecrawl.search('firecrawl', {
    limit: 3,
    scrapeOptions: { formats: ['markdown'] }
  });
  console.log(results);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer fc-YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -d '{
      "query": "firecrawl web scraping",
      "limit": 3,
      "scrapeOptions": {
        "formats": ["markdown", "links"]
      }
    }'
  ```

  ```bash CLI theme={null}
  # Search and scrape results
  firecrawl search "firecrawl" --scrape --scrape-formats markdown --limit 5 --pretty
  ```
</CodeGroup>

Every option in scrape endpoint is supported by this search endpoint through the `scrapeOptions` parameter.

### Response with Scraped Content

```json theme={null}
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - The Ultimate Web Scraping API",
      "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nThe Ultimate Web Scraping API\n\n## Turn any website into clean, structured data\n\nFirecrawl makes it easy to extract data from websites for AI applications, market research, content aggregation, and more...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - The Ultimate Web Scraping API",
        "description": "Firecrawl is a powerful web scraping API that turns any website into clean, structured data for AI and analysis.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Search then Scrape (Two-Step Pattern)

If you need to filter or process search results before scraping, use a two-step approach: search first, then scrape the URLs you want.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Step 1: Search
  results = firecrawl.search("firecrawl web scraping", limit=5)

  # Step 2: Scrape each result URL for full content
  for item in results.web or []:
      page = firecrawl.scrape(item.url, formats=["markdown"])
      print(page.markdown[:200])
  ```

  ```js JavaScript theme={null}
  import Firecrawl from '@mendable/firecrawl-js';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });

  // Step 1: Search
  const results = await firecrawl.search("firecrawl web scraping", { limit: 5 });

  // Step 2: Scrape each result URL for full content
  for (const item of results.web ?? []) {
    const page = await firecrawl.scrape(item.url, { formats: ["markdown"] });
    console.log(page.markdown?.substring(0, 200));
  }
  ```
</CodeGroup>

<Tip>
  **When to use which approach:**

  * **One-step** (`scrapeOptions` in search): You want content from all results. Simpler and faster.
  * **Two-step** (search then scrape): You want to filter, rank, or selectively scrape results. More flexible.

  Both approaches use Firecrawl for the scrape step. Do not use generic HTTP fetching or summarize from search snippets alone -- the full page content from Firecrawl scrape is what makes results grounded and complete.
</Tip>

## Advanced Search Options

Firecrawl's search API supports various parameters to customize your search:

### Location Customization

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR_API_KEY",
  )

  # Search with location settings (Germany)
  search_result = firecrawl.search(
      "web scraping tools",
      limit=5,
      location="Germany"
  )

  # Process the results
  for result in search_result.data:
      print(f"Title: {result['title']}")
      print(f"URL: {result['url']}")
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  // Search with location settings (Germany)
  const results = await firecrawl.search('web scraping tools', {
    limit: 5,
    location: "Germany"
  });

  // Process the results
  console.log(results);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer fc-YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -d '{
      "query": "web scraping tools",
      "limit": 5,
      "location": "Germany"
    }'
  ```

  ```bash CLI theme={null}
  # Search with location
  firecrawl search "local restaurants" --location "San Francisco,California,United States" --country US --pretty
  ```
</CodeGroup>

### Time-Based Search

Use the `tbs` parameter to filter results by time. Note that `tbs` only applies to `web` source results — it does not filter `news` or `images` results. If you need time-filtered news, consider using a `web` source with the `site:` operator to target specific news domains.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )

  results = firecrawl.search(
      query="firecrawl",
      limit=5,
      tbs="qdr:d",
  )
  print(len(results.get('web', [])))
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });

  const results = await firecrawl.search('firecrawl', {
    limit: 5,
    tbs: 'qdr:d', // past day
  });

  console.log(results.web);
  ```

  ```bash cURL theme={null}
  # No API key needed to get started — add -H "Authorization: Bearer fc-YOUR_API_KEY" for higher rate limits:
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -d '{
      "query": "latest web scraping techniques",
      "limit": 5,
      "tbs": "qdr:w"
    }'
  ```

  ```bash CLI theme={null}
  # Search with time filter (past week)
  firecrawl search "firecrawl updates" --tbs qdr:w --limit 5 --pretty
  ```
</CodeGroup>

Common `tbs` values:

* `qdr:h` - Past hour
* `qdr:d` - Past 24 hours
* `qdr:w` - Past week
* `qdr:m` - Past month
* `qdr:y` - Past year
* `sbd:1` - Sort by date (newest first)

For more precise time filtering, you can specify exact date ranges using the custom date range format:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the client with your API key
  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Search for results from December 2024
  search_result = firecrawl.search(
      "firecrawl updates",
      limit=10,
      tbs="cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  )
  ```

  ```js JavaScript theme={null}
  import { Firecrawl } from 'firecrawl';

  // Initialize the client with your API key
  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  // Search for results from December 2024
  firecrawl.search("firecrawl updates", {
    limit: 10,
    tbs: "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
  })
  .then(searchResult => {
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "firecrawl updates",
      "limit": 10,
      "tbs": "cdr:1,cd_min:12/1/2024,cd_max:12/31/2024"
    }'
  ```
</CodeGroup>

You can combine `sbd:1` with time filters to get date-sorted results within a time range. For example, `sbd:1,qdr:w` returns results from the past week sorted newest first, and `sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` returns results from December 2024 sorted by date.

### Custom Timeout

Set a custom timeout for search operations:

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  # Initialize the client with your API key
  firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

  # Set a 30-second timeout
  search_result = firecrawl.search(
      "complex search query",
      limit=10,
      timeout=30000  # 30 seconds in milliseconds
  )
  ```

  ```js JavaScript theme={null}
  import { Firecrawl } from 'firecrawl';

  // Initialize the client with your API key
  const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

  // Set a 30-second timeout
  firecrawl.search("complex search query", {
    limit: 10,
    timeout: 30000  // 30 seconds in milliseconds
  })
  .then(searchResult => {
    // Process results
    console.log(searchResult.data);
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer fc-YOUR_API_KEY" \
    -d '{
      "query": "complex search query",
      "limit": 10,
      "timeout": 30000
    }'
  ```
</CodeGroup>

## Zero Data Retention (ZDR)

For teams with strict data handling requirements, Firecrawl offers Zero Data Retention (ZDR) options for the `/search` endpoint via the `enterprise` parameter. ZDR search is available on Enterprise plans — visit [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) to get started.

<Note>
  This is separate from the `zeroDataRetention` scrape option, which controls ZDR for scraping operations. See [Scrape ZDR](/features/scrape#zero-data-retention-zdr) for details. The `enterprise` parameter only applies to the search portion of the request.
</Note>

### End-to-End ZDR

With end-to-end ZDR, both Firecrawl and our upstream search provider enforce zero data retention. No query or result data is stored at any point in the pipeline.

* **Cost:** 10 credits per 10 results
* **Parameter:** `enterprise: ["zdr"]`

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### Anonymized ZDR

With anonymized ZDR, Firecrawl enforces full zero data retention on our side. Our search provider may cache the query, but it is fully anonymized — no identifying information is attached.

* **Cost:** 2 credits per 10 results
* **Parameter:** `enterprise: ["anon"]`

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### Combining Search ZDR with Scrape ZDR

If you are using search with content scraping (`scrapeOptions`), the `enterprise` parameter covers the search portion while `zeroDataRetention` in `scrapeOptions` covers the scraping portion. To get full ZDR across both, set both:

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## Cost Implications

The cost of a search is 2 credits per 10 results, rounded up (1–10 results = 2 credits, 11–20 = 4 credits, and so on). If scraping options are enabled, the standard scraping costs apply to each search result:

* **Basic scrape**: 1 credit per webpage
* **PDF parsing**: 1 credit per PDF page
* **Enhanced proxy mode**: 4 additional credits per webpage
* **JSON mode**: 4 additional credits per webpage

To help control costs:

* Set `parsers: []` if PDF parsing isn’t required
* Use `proxy: "basic"` instead of `"enhanced"` when possible, or set it to `"auto"`
* Limit the number of search results with the `limit` parameter

## Advanced Scraping Options

For more details about the scraping options, refer to the [Scrape Feature documentation](https://docs.firecrawl.dev/features/scrape). Everything except for the FIRE-1 Agent and Change-Tracking features are supported by this Search endpoint.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

## Search feedback

When a search result is useful or misses important content, submit feedback with `POST /v2/search/{jobId}/feedback`. The first feedback submission for a search job can refund 1 credit, subject to team limits, and helps improve Firecrawl search quality. See [Search Feedback](/api-reference/endpoint/search-feedback).

## Map — https://docs.firecrawl.dev/features/map
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Map

> Input a website and get all the urls on the website - extremely fast

## Introducing /map

The easiest way to go from a single url to a map of the entire website. This is extremely useful for:

* When you need to prompt the end-user to choose which links to scrape
* Need to quickly know the links on a website
* Need to scrape pages of a website that are related to a specific topic (use the `search` parameter)
* Only need to scrape specific pages of a website

<Card title="Try it in the Playground" icon="play" href="https://www.firecrawl.dev/playground?endpoint=map">
  Test mapping in the interactive playground — no code required.
</Card>

## Mapping

### /map endpoint

Used to map a URL and get urls of the website. This returns most links present on the website.

URLs are primarily discovered from the website's sitemap, supplemented with SERP (search engine) results and previously crawled pages to improve coverage. You can control sitemap behavior with the `sitemap` parameter.

### Installation

<CodeGroup>
  ```python Python theme={null}
  # pip install firecrawl-py

  from firecrawl import Firecrawl

  firecrawl = Firecrawl(
    # No API key needed to get started — add one for higher rate limits:
    # api_key="fc-YOUR-API-KEY",
  )
  ```

  ```js Node theme={null}
  // npm install firecrawl

  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({
    // No API key needed to get started — add one for higher rate limits:
    // apiKey: "fc-YOUR-API-KEY",
  });
  ```

  ```bash CLI theme={null}
  # Install globally with npm
  npm install -g firecrawl

  # Authenticate (one-time setup)
  firecrawl login
  ```
</CodeGroup>

### Usage

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
  res = firecrawl.map(url="https://firecrawl.dev", limit=50, sitemap="include")
  print(res)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const res = await firecrawl.map('https://firecrawl.dev', { limit: 50, sitemap: 'include' });
  console.log(res);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.firecrawl.dev/v2/map \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer YOUR_API_KEY' \
      -d '{
        "url": "https://firecrawl.dev"
      }'
  ```

  ```bash CLI theme={null}
  # Map a website to discover URLs
  firecrawl map https://firecrawl.dev

  # Output as JSON with limit
  firecrawl map https://firecrawl.dev --json --limit 100 --pretty
  ```
</CodeGroup>

<Info>
  Each map request consumes 1 credit per call, regardless of the number of URLs returned. For example, setting `limit` to 100,000 still uses 1 credit.
</Info>

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```json theme={null}
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "Turn any url into clean data"
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "5 Easy Ways to Access GLM-4.5",
      "description": "Discover how to access GLM-4.5 models locally, through chat applications, via the official API, and using the LLM marketplaces API for seamless integration i..."
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "Preview the API response and get the code snippets for the API"
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - The Web Data API for AI",
      "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders. Clean, structured, and ..."
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - The Web Data API for AI",
      "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders. Clean, structured, and ..."
    },
    ...
  ]
}
```

<Warning>
  Title and description are not always present as it depends on the website.
</Warning>

#### Map with search

Map with `search` param allows you to search for specific urls inside a website.

```bash cURL theme={null}
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

Response will be an ordered list from the most relevant to the least relevant.

```json theme={null}
{
  "status": "success",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Firecrawl Docs",
      "description": "Firecrawl documentation"
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "Firecrawl Python SDK",
      "description": "Firecrawl Python SDK documentation"
    },
    ...
  ]
}
```

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences, similar to the scrape endpoint.

### How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to 'US' if not specified.

### Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

* `country`: ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP'). Defaults to 'US'.
* `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

<CodeGroup>
  ```python Python theme={null}
  from firecrawl import Firecrawl

  firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

  res = firecrawl.map('https://example.com',
      location={
          'country': 'US',
          'languages': ['en']
      }
  )

  print(res)
  ```

  ```js Node theme={null}
  import { Firecrawl } from 'firecrawl';

  const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

  const res = await firecrawl.map('https://example.com', {
    location: { country: 'US', languages: ['en'] },
  });

  console.log(res.metadata);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.firecrawl.dev/v2/map" \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "url": "https://example.com",
      "location": { "country": "US", "languages": ["en"] }
    }'
  ```
</CodeGroup>

For more details about supported locations, refer to the [Proxies documentation](/features/proxies).

## Considerations

This endpoint prioritizes speed, so it may not capture all website links. It primarily relies on the website's sitemap, supplemented by cached crawl data and search engine results. For a more thorough and up-to-date list of URLs, consider using the [/crawl](/features/crawl) endpoint instead.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

## API Reference Introduction — https://docs.firecrawl.dev/api-reference/introduction
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Firecrawl API Reference

## Features

<CardGroup cols={3}>
  <Card title="Scrape" icon="markdown" href="/api-reference/endpoint/scrape" color="FF713C">
    Extract content from any webpage in markdown or json format.
  </Card>

  <Card title="Crawl" icon="spider" href="/api-reference/endpoint/crawl-post" color="FF713C">
    Crawl entire websites, extract their content and metadata.
  </Card>

  <Card title="Map" icon="map" href="/api-reference/endpoint/map" color="FF713C">
    Get a complete list of URLs from any website quickly and reliably.
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/api-reference/endpoint/search" color="FF713C">
    Search the web and get full page content in any format.
  </Card>
</CardGroup>

## Agentic Features

<CardGroup cols={3}>
  <Card title="Extract" icon="barcode-read" href="/api-reference/endpoint/extract" color="FF713C">
    Extract structured data from entire webpages using natural language.
  </Card>
</CardGroup>

## Base URL

All requests contain the following base URL:

```bash theme={null}
https://api.firecrawl.dev 
```

## Authentication

For authentication, it's required to include an Authorization header. The header should contain `Bearer fc-123456789`, where `fc-123456789` represents your API Key.

```bash theme={null}
Authorization: Bearer fc-123456789
```

​

## Response codes

Firecrawl employs conventional HTTP status codes to signify the outcome of your requests.

Typically, 2xx HTTP status codes denote success, 4xx codes represent failures related to the user, and 5xx codes signal infrastructure problems.

| Status | Description                                               |
| ------ | --------------------------------------------------------- |
| 200    | Request was successful.                                   |
| 400    | Verify the correctness of the parameters.                 |
| 401    | The API key was not provided.                             |
| 402    | Payment required                                          |
| 404    | The requested resource could not be located.              |
| 408    | The request timed out (e.g., page took too long to load). |
| 429    | The rate limit has been surpassed.                        |
| 5xx    | Signifies a server error with Firecrawl.                  |

Refer to the Error Codes section for a detailed explanation of all potential API errors.

### Firecrawl error codes

When a 408 or 5xx error occurs, Firecrawl provides more specific error codes to clarify what went wrong.​

| Error Code                           | Status | Description                                                                                                                                                                            |
| ------------------------------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SCRAPE_TIMEOUT`                     | 408    | The page took too long to load or render. Try increasing the `timeout` parameter (up to 60000ms).                                                                                      |
| `SCRAPE_ALL_ENGINES_FAILED`          | 500    | All scraping engines failed.                                                                                                                                                           |
| `SCRAPE_SSL_ERROR`                   | 500    | Page SSL certificate is invalid. You can use `skipTlsVerification:true` to bypass this check.                                                                                          |
| `SCRAPE_SITE_ERROR`                  | 500    | Unrecoverable site error.                                                                                                                                                              |
| `SCRAPE_DNS_RESOLUTION_ERROR`        | 500    | DNS resolution failed.                                                                                                                                                                 |
| `SCRAPE_ACTION_ERROR`                | 500    | Error while performing a page action.                                                                                                                                                  |
| `SCRAPE_PDF_PREFETCH_FAILED`         | 500    | Failed to prefetch PDF.                                                                                                                                                                |
| `SCRAPE_PDF_INSUFFICIENT_TIME_ERROR` | 500    | Not enough time to process PDF.                                                                                                                                                        |
| `SCRAPE_PDF_ANTIBOT_ERROR`           | 500    | PDF blocked by anti-bot mechanisms.                                                                                                                                                    |
| `SCRAPE_ZDR_VIOLATION_ERROR`         | 500    | Zero Data Retention conflict: occurs when `zeroDataRetention:true` but another option (e.g. `screenshot`) requires temporary storage.                                                  |
| `SCRAPE_UNSUPPORTED_FILE_ERROR`      | 500    | Unsupported file type or file size exceeds 10MB limit.                                                                                                                                 |
| `SCRAPE_LOCKDOWN_CACHE_MISS`         | 404    | Lockdown mode is enabled but no cached data is available for the URL. Seed the cache with a non-lockdown scrape first, or disable `lockdown`. See [Lockdown Mode](/features/lockdown). |
| `UNKNOWN_ERROR`                      | 500    | Generic or unexpected error.                                                                                                                                                           |

## 429 responses

When you exceed your plan's rate or concurrency limits, the API returns a 429 response code. See [Rate Limits](/rate-limits) for per-plan limits.

## SDKs Overview — https://docs.firecrawl.dev/sdks/overview
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Firecrawl SDKs are wrappers around the Firecrawl API to help you easily search, scrape, and interact with the web.

Use an SDK to search, scrape, and interact with the web without managing raw HTTP requests. Each SDK wraps the Firecrawl API with idiomatic helpers for authentication, polling, and error handling.

## Official SDKs

<CardGroup cols={2}>
  <Card title="Python SDK" icon="python" href="python">
    For Python apps, with sync and async support.
  </Card>

  <Card title="Node SDK" icon="node" href="node">
    For Node.js and TypeScript apps.
  </Card>

  <Card title="Go SDK" icon="golang" href="go">
    For Go applications.
  </Card>

  <Card title="Java SDK" icon="java" href="java">
    For Java and JVM-based applications.
  </Card>

  <Card title="Ruby SDK" icon="gem" href="ruby">
    For Ruby and Rails applications.
  </Card>

  <Card title="Rust SDK" icon="rust" href="rust">
    For Rust applications, with full v2 API support.
  </Card>

  <Card title=".NET SDK" icon="microsoft" href="dotnet">
    For .NET and ASP.NET Core applications.
  </Card>

  <Card title="PHP SDK" icon="php" href="php">
    For PHP and Laravel applications.
  </Card>

  <Card title="Elixir SDK" icon="droplet" href="elixir">
    For Elixir and Phoenix applications.
  </Card>

  <Card title="CLI" icon="terminal" href="cli">
    Run Firecrawl from the command line.
  </Card>
</CardGroup>

## MCP Server — https://docs.firecrawl.dev/mcp-server
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.firecrawl.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Firecrawl MCP Server

> Use Firecrawl's API through the Model Context Protocol

A Model Context Protocol (MCP) server implementation that integrates [Firecrawl](https://github.com/firecrawl/firecrawl) for searching, scraping, and interacting with the web. Our MCP server is open-source and available on [GitHub](https://github.com/firecrawl/firecrawl-mcp-server).

## Features

* Search the web and get full page content
* Scrape any URL into clean, structured data
* Parse local files such as PDFs, DOCX, XLSX, and HTML
* Interact with pages — click, navigate, and operate
* Deep research with autonomous agent
* Cloud and self-hosted support
* Streamable HTTP support

## Installation

You can either use our remote hosted URL or run the server locally. Get your API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

<Note>
  **No API key?** Connect to `https://mcp.firecrawl.dev/v2/mcp` to use the remote keyless free tier. It is free and rate-limited per IP; see [Rate Limits](/rate-limits#keyless-no-api-key) for the current keyless tool list. Set `FIRECRAWL_API_KEY` to unlock every MCP tool plus higher limits.
</Note>

### Remote hosted URL

With an API key (unlocks every tool plus higher limits):

```bash theme={null}
https://mcp.firecrawl.dev/{FIRECRAWL_API_KEY}/v2/mcp
```

Or connect without an API key to get started on the remote keyless free tier (rate-limited per IP; see [Rate Limits](/rate-limits#keyless-no-api-key) for the current tool list):

```bash theme={null}
https://mcp.firecrawl.dev/v2/mcp
```

### Running with npx

```bash theme={null}
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Manual Installation

```bash theme={null}
npm install -g firecrawl-mcp
```

### Running on Cursor

<a href="cursor://anysphere.cursor-deeplink/mcp/install?name=firecrawl&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImZpcmVjcmF3bC1tY3AiXSwiZW52Ijp7IkZJUkVDUkFXTF9BUElfS0VZIjoiWU9VUi1BUEktS0VZIn19">
  <img src="https://cursor.com/deeplink/mcp-install-dark.png" alt="Add Firecrawl MCP server to Cursor" style={{ maxHeight: 32 }} />
</a>

#### Manual Installation

Configuring Cursor 🖥️
Note: Requires Cursor version 0.45.6+
For the most up-to-date configuration instructions, please refer to the official Cursor documentation on configuring MCP servers:
[Cursor MCP Server Configuration Guide](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

To configure Firecrawl MCP in Cursor **v0.48.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add new global MCP server"
4. Enter the following code:
   ```json theme={null}
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

To configure Firecrawl MCP in Cursor **v0.45.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add New MCP Server"
4. Enter the following:
   * Name: "firecrawl-mcp" (or your preferred name)
   * Type: "command"
   * Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> If you are using Windows and are running into issues, try `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Replace `your-api-key` with your Firecrawl API key. If you don't have one yet, you can create an account and get it from [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)

After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use Firecrawl MCP when appropriate, but you can explicitly request it by describing your web data needs. Access the Composer via Command+L (Mac), select "Agent" next to the submit button, and enter your query.

### Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

```json theme={null}
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Running with Streamable HTTP Mode

To run the server using streamable HTTP transport locally instead of the default stdio transport:

```bash theme={null}
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

Use the url: [http://localhost:3000/v2/mcp](http://localhost:3000/v2/mcp) or [https://mcp.firecrawl.dev/\{FIRECRAWL\_API\_KEY}/v2/mcp](https://mcp.firecrawl.dev/\{FIRECRAWL_API_KEY}/v2/mcp)

### Installing via Smithery (Legacy)

To install Firecrawl for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl):

```bash theme={null}
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

### Running on VS Code

For one-click installation, click one of the install buttons below\...

[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22apiKey%22%2C%22description%22%3A%22Firecrawl%20API%20Key%22%2C%22password%22%3Atrue%7D%5D\&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22firecrawl-mcp%22%5D%2C%22env%22%3A%7B%22FIRECRAWL_API_KEY%22%3A%22%24%7Binput%3AapiKey%7D%22%7D%7D\&quality=insiders)

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.

```json theme={null}
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "Firecrawl API Key",
        "password": true
      }
    ],
    "servers": {
      "firecrawl": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "env": {
          "FIRECRAWL_API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others:

```json theme={null}
{
  "inputs": [
    {
      "type": "promptString",
      "id": "apiKey",
      "description": "Firecrawl API Key",
      "password": true
    }
  ],
  "servers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "${input:apiKey}"
      }
    }
  }
}
```

**Note:** Some users have reported issues when adding the MCP server to VS Code due to how it validates JSON with an outdated schema format ([microsoft/vscode#155379](https://github.com/microsoft/vscode/issues/155379)).
This affects several MCP tools, including Firecrawl.

**Workaround:** Disable JSON validation in VS Code to allow the MCP server to load properly.\
See reference: [directus/directus#25906 (comment)](https://github.com/directus/directus/issues/25906#issuecomment-3369169513).

The MCP server still works fine when invoked via other extensions, but the issue occurs specifically when registering it directly in the MCP server list. We plan to add guidance once VS Code updates their schema validation.

### Running on Claude Desktop

Add this to the Claude config file:

```json theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

If you get a "Couldn't reach the MCP server" error, your Claude Desktop version may not support streamable HTTP transport. Use the local npx approach instead (requires [Node.js](https://nodejs.org)):

```json theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

If you see a `spawn npx ENOENT` error, Node.js is not installed or not in your system PATH. Install Node.js from [nodejs.org](https://nodejs.org) (LTS version), then fully restart Claude Desktop. On Windows, you can also run `where npx` in Command Prompt and use the full path (e.g. `C:\\Program Files\\nodejs\\npx.cmd`) as the `command` value.

### Running on Claude Code

Add the Firecrawl MCP server using the Claude Code CLI. You can use the remote hosted URL or run locally:

```bash theme={null}
# Remote hosted URL (recommended)
claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/your-api-key/v2/mcp

# Or run locally via npx
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

### Running on Google Antigravity

Google Antigravity allows you to configure MCP servers directly through its Agent interface.

<img src="https://mintcdn.com/firecrawl/rxzXygFiVc0TDh5X/images/guides/mcp/antigravity-mcp-installation.gif?s=19297c26dad5ed191862571618ce8c0a" alt="Antigravity MCP Installation" width="1280" height="720" data-path="images/guides/mcp/antigravity-mcp-installation.gif" />

1. Open the Agent sidebar in the Editor or the Agent Manager view
2. Click the "..." (More Actions) menu and select **MCP Servers**
3. Select **View raw config** to open your local `mcp_config.json` file
4. Add the following configuration:

```json theme={null}
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```

5. Save the file and click **Refresh** in the Antigravity MCP interface to see the new tools

Replace `YOUR_FIRECRAWL_API_KEY` with your API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys).

### Running on n8n

To connect the Firecrawl MCP server in n8n:

1. Get your Firecrawl API key from [https://firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
2. In your n8n workflow, add an **AI Agent** node
3. In the AI Agent configuration, add a new **Tool**
4. Select **MCP Client Tool** as the tool type
5. Enter the MCP server Endpoint (replace `{YOUR_FIRECRAWL_API_KEY}` with your actual API key):

```
https://mcp.firecrawl.dev/{YOUR_FIRECRAWL_API_KEY}/v2/mcp
```

6. Set **Server Transport** to **HTTP Streamable**
7. Set **Authentication** to **None**
8. For **Tools to include**, you can select **All**, **Selected**, or **All Except** - this will expose the Firecrawl tools (scrape, crawl, map, search, extract, etc.)

For self-hosted deployments, run the MCP server with npx and enable HTTP transport mode:

```bash theme={null}
env HTTP_STREAMABLE_SERVER=true \
    FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
    FIRECRAWL_API_URL=YOUR_FIRECRAWL_INSTANCE \
    npx -y firecrawl-mcp
```

This will start the server on `http://localhost:3000/v2/mcp` which you can use in your n8n workflow as Endpoint. The `HTTP_STREAMABLE_SERVER=true` environment variable is required since n8n needs HTTP transport.

## Configuration

### Environment Variables

#### Cloud and self-hosted API

* `FIRECRAWL_API_KEY`: Your Firecrawl API key
  * Required when using cloud API (default)
  * Optional when using self-hosted instance with `FIRECRAWL_API_URL`
* `FIRECRAWL_API_URL` (Optional): Custom API endpoint for self-hosted instances
  * Example: `https://firecrawl.your-domain.com`
  * If not provided, the cloud API will be used (requires API key)

### Configuration Examples

For cloud API usage:

```bash theme={null}
export FIRECRAWL_API_KEY=your-api-key
```

For self-hosted instance:

```bash theme={null}
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com
export FIRECRAWL_API_KEY=your-api-key  # If your instance requires auth
```

### Custom configuration with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json theme={null}
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Hosted MCP vs local MCP

The hosted MCP server is optimized for safe remote use. Some options that are available when running the MCP server locally are narrowed or unavailable remotely:

* Hosted keyless mode exposes only the keyless-supported tools and is rate-limited per IP.
* Local-only file reads are available only when you run the MCP server locally.
* Webhooks and local file paths should be configured from a local or self-hosted MCP server when the agent needs access to local resources.

### Rate Limiting

Rate limits are enforced by Firecrawl. Use an API key for higher limits and access to the full tool set.

## Available Tools

### 1. Scrape Tool (`firecrawl_scrape`)

Scrape content from a single URL with advanced options.

```json theme={null}
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formats": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

To redact personally identifiable information, include `redactPII` in the scrape tool arguments.

```json theme={null}
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com/contact",
    "formats": ["markdown"],
    "redactPII": true
  }
}
```

### 2. Map Tool (`firecrawl_map`)

Map a website to discover all indexed URLs on the site.

```json theme={null}
{
  "name": "firecrawl_map",
  "arguments": {
    "url": "https://example.com",
    "search": "blog",
    "sitemap": "include",
    "includeSubdomains": false,
    "limit": 100,
    "ignoreQueryParameters": true
  }
}
```

#### Map Tool Options:

* `url`: The base URL of the website to map
* `search`: Optional search term to filter URLs
* `sitemap`: Control sitemap usage - "include", "skip", or "only"
* `includeSubdomains`: Whether to include subdomains in the mapping
* `limit`: Maximum number of URLs to return
* `ignoreQueryParameters`: Whether to ignore query parameters when mapping

**Best for:** Discovering URLs on a website before deciding what to scrape; finding specific sections of a website.
**Returns:** Array of URLs found on the site.

### 3. Search Tool (`firecrawl_search`)

Search the web and optionally extract content from search results.

```json theme={null}
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "your search query",
    "limit": 5,
    "location": "United States",
    "tbs": "qdr:m",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

#### Search Tool Options:

* `query`: The search query string (required)
* `limit`: Maximum number of results to return
* `location`: Geographic location for search results
* `tbs`: Time-based search filter (e.g., `qdr:d` for past day, `qdr:w` for past week, `qdr:m` for past month)
* `filter`: Additional search filter
* `sources`: Array of source types to search (`web`, `images`, `news`)
* `scrapeOptions`: Options for scraping search result pages
* `enterprise`: Array of enterprise options (`default`, `anon`, `zdr`)

### 4. Parse Tool (`firecrawl_parse`)

Parse a local file such as a PDF, DOCX, XLSX, or HTML document into clean, LLM-ready data.

```json theme={null}
{
  "name": "firecrawl_parse",
  "arguments": {
    "filePath": "/absolute/path/to/report.pdf",
    "formats": ["markdown"]
  }
}
```

When you run Firecrawl MCP locally against a Firecrawl API instance with `FIRECRAWL_API_URL`, the MCP server can read `filePath` directly and sends the file bytes to `/v2/parse`.

When you use the remote hosted MCP server, the hosted server cannot read files from your machine. In that case `firecrawl_parse` uses a two-step handoff that also works on the remote keyless URL:

1. Call `firecrawl_parse` with `filePath`. The tool returns a pre-filled upload command and a `nextToolCall` containing an `uploadRef`.
2. Run the upload command on the machine that can read the file, then call `firecrawl_parse` again with the returned `uploadRef`.

The upload command sends the file bytes to a short-lived signed upload target. It does not include your Firecrawl API key.

#### Parse Tool Options:

* `filePath`: Local path to the file you want to parse. Use this for the first call.
* `uploadRef`: Reference returned by the first hosted-MCP call. Use this for the second call after the upload succeeds.
* `formats`: Output formats. Defaults to `markdown`.
* `parsers`: Parser controls, such as PDF parsing options.
* `contentType`: Optional file MIME type override.
* `declaredSizeBytes`: Optional file size hint. Files are limited to 50 MB.

**Best for:** Local or non-public documents that are not available at a public URL.

**Not recommended for:** Public document URLs. Use `firecrawl_scrape` instead; it will detect and parse documents from URLs.

### 5. Crawl Tool (`firecrawl_crawl`)

Start an asynchronous crawl with advanced options.

```json theme={null}
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDiscoveryDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 6. Check Crawl Status (`firecrawl_check_crawl_status`)

Check the status of a crawl job.

```json theme={null}
{
  "name": "firecrawl_check_crawl_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Returns:** Status and progress of the crawl job, including results if available.

### 7. Extract Tool (`firecrawl_extract`)

Extract structured information from web pages using LLM capabilities. Supports both cloud AI and self-hosted LLM extraction.

```json theme={null}
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

Example response:

```json theme={null}
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

#### Extract Tool Options:

* `urls`: Array of URLs to extract information from
* `prompt`: Custom prompt for the LLM extraction
* `schema`: JSON schema for structured data extraction
* `allowExternalLinks`: Allow extraction from external links
* `enableWebSearch`: Enable web search for additional context
* `includeSubdomains`: Include subdomains in extraction

When using a self-hosted instance, the extraction will use your configured LLM. For cloud API, it uses Firecrawl's managed LLM service.

### 8. Agent Tool (`firecrawl_agent`)

Autonomous web research agent that independently browses the internet, searches for information, navigates through pages, and extracts structured data based on your query. This runs asynchronously -- it returns a job ID immediately, and you poll `firecrawl_agent_status` to check when complete and retrieve results.

```json theme={null}
{
  "name": "firecrawl_agent",
  "arguments": {
    "prompt": "Find the top 5 AI startups founded in 2024 and their funding amounts",
    "schema": {
      "type": "object",
      "properties": {
        "startups": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "funding": { "type": "string" },
              "founded": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

You can also provide specific URLs for the agent to focus on:

```json theme={null}
{
  "name": "firecrawl_agent",
  "arguments": {
    "urls": ["https://docs.firecrawl.dev", "https://firecrawl.dev/pricing"],
    "prompt": "Compare the features and pricing information from these pages"
  }
}
```

#### Agent Tool Options:

* `prompt`: Natural language description of the data you want (required, max 10,000 characters)
* `urls`: Optional array of URLs to focus the agent on specific pages
* `schema`: Optional JSON schema for structured output

**Best for:** Complex research tasks where you don't know the exact URLs; multi-source data gathering; finding information scattered across the web; extracting data from JavaScript-heavy SPAs that fail with regular scrape.

**Returns:** Job ID for status checking. Use `firecrawl_agent_status` to poll for results.

### 9. Check Agent Status (`firecrawl_agent_status`)

Check the status of an agent job and retrieve results when complete. Poll every 15-30 seconds and keep polling for at least 2-3 minutes before considering the request failed.

```json theme={null}
{
  "name": "firecrawl_agent_status",
  "arguments": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

#### Agent Status Options:

* `id`: The agent job ID returned by `firecrawl_agent` (required)

**Possible statuses:**

* `processing`: Agent is still researching -- keep polling
* `completed`: Research finished -- response includes the extracted data
* `failed`: An error occurred

**Returns:** Status, progress, and results (if completed) of the agent job.

### 10. Interact with a Page (`firecrawl_interact`)

Interact with a page in a live browser session: click buttons, fill forms, extract dynamic content, or navigate deeper.

Use one of two targeting modes:

* Pass `url` to open and interact with a fresh page in one MCP call.
* Pass `scrapeId` from a previous `firecrawl_scrape` call to reuse the already-loaded page.

Do not pass both `url` and `scrapeId`. Provide either `prompt` or `code`. `scrapeOptions` can only be used with `url` mode.

**URL mode example:**

```json theme={null}
{
  "name": "firecrawl_interact",
  "arguments": {
    "url": "https://example.com/products",
    "prompt": "Click on the first product and tell me its price"
  }
}
```

**Scrape reuse example:**

```json theme={null}
{
  "name": "firecrawl_interact",
  "arguments": {
    "scrapeId": "scrape-id-from-previous-scrape",
    "prompt": "Click the Sign In button"
  }
}
```

#### Interact Tool Options:

* `url`: Page to interact with; opens the session for you. Use this or `scrapeId`.
* `scrapeId`: Scrape job ID from a previous `firecrawl_scrape` call. Use this or `url`.
* `prompt`: Natural language instruction describing the action to take. Provide `prompt` or `code`.
* `code`: Code to execute in the browser session. Provide `code` or `prompt`.
* `language`: `bash`, `python`, or `node` (optional, defaults to `node`, only used with `code`).
* `timeout`: Execution timeout in seconds, 1–300 (optional, defaults to 30).
* `scrapeOptions`: Optional scrape controls used only with `url` mode.

**Best for:** Multi-step workflows on a single page — searching a site, clicking through results, filling forms, extracting data that requires interaction.

**Returns:** Interaction result including output and live view URLs.

### 11. Stop Interact Session (`firecrawl_interact_stop`)

Stop an interact session for a scraped page. Call this when you are done interacting to free resources.

```json theme={null}
{
  "name": "firecrawl_interact_stop",
  "arguments": {
    "scrapeId": "scrape-id-from-previous-scrape"
  }
}
```

#### Interact Stop Options:

* `scrapeId`: The scrape ID for the session to stop (required)

**Returns:** Confirmation that the session has been stopped.

## Logging System

The server includes comprehensive logging:

* Operation status and progress
* Performance metrics
* Credit usage monitoring
* Rate limit tracking
* Error conditions

Example log messages:

```
[INFO] Firecrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Starting crawl for URL: https://example.com
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...
```

## Error Handling

The server provides robust error handling:

* Automatic retries for transient errors
* Rate limit handling with backoff
* Detailed error messages
* Credit usage warnings
* Network resilience

Example error response:

```json theme={null}
{
  "content": [
    {
      "type": "text",
      "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
    }
  ],
  "isError": true
}
```

## Development

```bash theme={null}
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Run tests: `npm test`
4. Submit a pull request

### Thanks to contributors

Thanks to [@vrknetha](https://github.com/vrknetha), [@cawstudios](https://caw.tech) for the initial implementation!

Thanks to MCP.so and Klavis AI for hosting and [@gstarwd](https://github.com/gstarwd), [@xiangkaiz](https://github.com/xiangkaiz) and [@zihaolin96](https://github.com/zihaolin96) for integrating our server.

## License

MIT License - see LICENSE file for details
