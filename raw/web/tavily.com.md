# tavily.com

## Fetch log
- Inbox URL: https://www.tavily.com/
- Final URL: https://www.tavily.com/
- Fetched: 2026-10-15
- Pages: 11
- Mode: standard
- Notes: https://www.tavily.com/llms.txt redirects to https://docs.tavily.com/llms.txt. Landing page captured via Jina Reader; docs pages fetched as Markdown (`.md` suffix) from docs.tavily.com.

## llms.txt — https://docs.tavily.com/llms.txt
# Tavily Docs

> Tavily is the web layer for AI agents: real-time web search, content extraction, site crawling, site mapping, and cited research — returned as clean, LLM-ready content instead of raw HTML. This index helps agents and developers find the right Tavily doc fast.

Use Tavily to find current web sources, read selected pages, explore a site's content, or produce a cited research report.

## Start Here For Agents

If you are an AI agent — or building one — start with the canonical setup guide:

- [Agents: Tavily setup & tool-choice guide](https://docs.tavily.com/agents.md): Choose how to connect (SDK/API, MCP, or CLI + Skills), choose the right capability (Search, Extract, Map, Crawl, Research), and apply recommended defaults.
- [Documentation MCP setup](https://docs.tavily.com/agents.md#documentation-mcp-server): Search and read Tavily's documentation. MCP endpoint: `https://docs.tavily.com/mcp` (Streamable HTTP).

Then use this file ([llms.txt](https://docs.tavily.com/llms.txt)) to find a specific page, [llms-full.txt](https://docs.tavily.com/llms-full.txt) for the full text of all docs, or append `.md` to any docs URL to fetch that single page as Markdown.

## Quick Start: CLI (fastest way to get started)

Install the Tavily CLI and log in — two commands:

```
pip install tavily-cli
tvly login
```

`tvly login` opens a browser for authentication. Then search, extract, crawl, and research from the terminal:

```
tvly search "latest AI news"
tvly extract "https://example.com"
tvly crawl "https://docs.example.com" --depth 2
tvly research "compare React vs Svelte for production apps"
```

Installing the CLI also installs Agent Skills for coding agents like Claude Code, Cursor, and Codex — they remind the agent to use Tavily for search, extract, crawl, and research. Get a free API key at https://app.tavily.com (1,000 credits/month, no credit card required).

## Alternative: Remote MCP Server

Connect any MCP client to Tavily's remote server — no local install required:

```
https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>
```

OAuth 2.0 is supported, so no API key needs to be hardcoded. For example, in Claude Code:

```
claude mcp add tavily-remote-mcp --transport http https://mcp.tavily.com/mcp/
```

## Choose How To Connect

Choose based on what Tavily must do, not only where you are running:

- **SDK / API** — you are building Tavily into an application, backend, or agent runtime that will call it in production.
- **MCP** — you need Tavily available to agents across an org, a managed environment, or multiple agent clients; governed and reusable.
- **CLI + Skills** — you need Tavily during the local coding or research session you are in right now.

Agent Toolkit is a developer resource for *building* production research agents, not a path for agents to configure Tavily autonomously.

## Choose A Capability

- **Search** — start here when sources are unknown or current web context is needed.
- **Extract** — use when the URL is known or selected from Search.
- **Map** — use before Crawl to understand a site's structure.
- **Crawl** — use when many pages on a site need to be read.
- **Research** — use when the output should be a cited synthesis: a report, comparison, or decision-ready answer.

Recommended defaults for agents: prefer `search_depth="advanced"`, add `chunks_per_source=3` for stronger evidence per source, use `max_results=5` for focused answers (10 for broader research), and avoid `include_answer` unless you need a quick answer seed.

## Getting Started

- [About](https://docs.tavily.com/documentation/about.md): What Tavily is and why it exists.
- [Quickstart](https://docs.tavily.com/documentation/quickstart.md): Start searching with Tavily in under 5 minutes.
- [Credits & Pricing](https://docs.tavily.com/documentation/api-credits.md): How to get and manage your Tavily API credits.
- [Rate Limits](https://docs.tavily.com/documentation/rate-limits.md): API rate limits for development and production.
- [Try Tavily Without an API Key](https://docs.tavily.com/documentation/keyless.md): Use Search and Extract for free, with zero setup — no account or API key. Keyless is free and rate-limited; hit the cap and sign up for a free API key (1,000 credits/month, no credit card).
- [Frequently Asked Questions](https://docs.tavily.com/faq/faq.md): Common questions about Tavily.
- [Help Center](https://docs.tavily.com/documentation/help.md): Get help and support.

## API Reference

- [Introduction](https://docs.tavily.com/documentation/api-reference/introduction.md): Easily integrate our APIs with your services.
- [Search](https://docs.tavily.com/documentation/api-reference/endpoint/search.md): Execute a real-time web search optimized for AI agents.
- [Extract](https://docs.tavily.com/documentation/api-reference/endpoint/extract.md): Extract clean content from one or more URLs.
- [Crawl](https://docs.tavily.com/documentation/api-reference/endpoint/crawl.md): Graph-based website traversal with built-in extraction and intelligent discovery.
- [Map](https://docs.tavily.com/documentation/api-reference/endpoint/map.md): Traverse a site like a graph to generate a comprehensive site map.
- [Create Research Task](https://docs.tavily.com/documentation/api-reference/endpoint/research.md): Run comprehensive research that searches, analyzes sources, and generates a cited report.
- [Get Research Task Status](https://docs.tavily.com/documentation/api-reference/endpoint/research-get.md): Retrieve the status and results of a research task by request ID.
- [Streaming](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming.md): Stream real-time research progress and results.
- [Feedback](https://docs.tavily.com/documentation/api-reference/endpoint/feedback.md): Submit feedback on a search request or session to improve result quality (beta).
- [Usage](https://docs.tavily.com/documentation/api-reference/endpoint/usage.md): Get API key and account usage details.
- [Logs](https://docs.tavily.com/documentation/api-reference/endpoint/logs.md): Retrieve per-request usage logs for your API keys (paid plans).

## Enterprise API

- [Generate Keys](https://docs.tavily.com/documentation/enterprise/generate-keys.md): Generate one or more API keys with custom configuration.
- [Deactivate Keys](https://docs.tavily.com/documentation/enterprise/deactivate-keys.md): Deactivate API keys in bulk by `request_id` or individually.
- [Key Info](https://docs.tavily.com/documentation/enterprise/key-info.md): Get information about an API key.
- [Organization Usage](https://docs.tavily.com/documentation/enterprise/org-usage.md): Retrieve usage, pay-as-you-go cost, and request counts for every API key under an organization you own.

## SDKs

- [Python Quickstart](https://docs.tavily.com/sdk/python/quick-start.md): Integrate Tavily natively in Python apps. Install with `pip install tavily-python`.
- [Python SDK Reference](https://docs.tavily.com/sdk/python/reference.md): Full Python SDK reference.
- [JavaScript Quickstart](https://docs.tavily.com/sdk/javascript/quick-start.md): Integrate Tavily natively in JavaScript/TypeScript. Install with `npm i @tavily/core`.
- [JavaScript SDK Reference](https://docs.tavily.com/sdk/javascript/reference.md): Full JavaScript/TypeScript SDK reference.

## Public repositories

- [Python SDK](https://github.com/tavily-ai/tavily-python): Source code and examples for `tavily-python`.
- [JavaScript SDK](https://github.com/tavily-ai/tavily-js): Source code and examples for `@tavily/core`.
- [Agent Skills](https://github.com/tavily-ai/skills): Official skills for using Tavily in coding agents.

## Best Practices

- [Search](https://docs.tavily.com/documentation/best-practices/best-practices-search.md): Optimize queries, filters, and advanced parameters.
- [Extract](https://docs.tavily.com/documentation/best-practices/best-practices-extract.md): Choose the right extraction approach and parameters.
- [Crawl](https://docs.tavily.com/documentation/best-practices/best-practices-crawl.md): Focus crawls and extract content efficiently.
- [Research](https://docs.tavily.com/documentation/best-practices/best-practices-research.md): Write effective prompts and configure output formats.
- [API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management.md): Handle key leaks and rotation.

## Ecosystem

- [Tavily MCP Server](https://docs.tavily.com/documentation/mcp.md): Use the Tavily API from any MCP client (Claude, Cursor, and more).
- [Tavily CLI](https://docs.tavily.com/documentation/tavily-cli.md): Search, extract, crawl, map, and research the web from your terminal.
- [Tavily Agent Skills](https://docs.tavily.com/documentation/agent-skills.md): Skills that add Tavily's web capabilities to AI coding agents.
- [Tavily x402](https://docs.tavily.com/documentation/machine-payments/x402.md): Agents pay per request for Advanced Search in USDC on Base — no API key, no account.

## Integrations

- [OpenAI Agent Builder](https://docs.tavily.com/documentation/integrations/agent-builder.md): Empower OpenAI's Agent Builder with real-time web access via Tavily MCP.
- [Agno](https://docs.tavily.com/documentation/integrations/agno.md): Use Tavily with the Agno agent framework.
- [Anthropic](https://docs.tavily.com/documentation/integrations/anthropic.md): Add real-time web search to Claude tool-calling agents.
- [Arcade.dev](https://docs.tavily.com/documentation/integrations/arcade-dev.md): Governed Tavily access via the Arcade.dev MCP Gateway.
- [Cartesia](https://docs.tavily.com/documentation/integrations/cartesia.md): Build real-time voice agents that search and extract with the Cartesia Line SDK.
- [Claude](https://docs.tavily.com/documentation/integrations/claude.md): Use Tavily across the Claude ecosystem as a Connector or Plugin.
- [Composio](https://docs.tavily.com/documentation/integrations/composio.md): Unified tool management across agent frameworks.
- [Convex](https://docs.tavily.com/documentation/integrations/convex.md): Web search and content extraction in Convex apps via the `@tavily/convex-tavily` component.
- [CrewAI](https://docs.tavily.com/documentation/integrations/crewai.md): Build multi-agent CrewAI workflows with web research.
- [Devin](https://docs.tavily.com/documentation/integrations/devin.md): Connect Tavily to Devin via the MCP Marketplace.
- [Dify](https://docs.tavily.com/documentation/integrations/dify.md): No-code LLM app building with Tavily.
- [ElevenLabs](https://docs.tavily.com/documentation/integrations/elevenlabs.md): Give ElevenLabs agents live web search.
- [FlowiseAI](https://docs.tavily.com/documentation/integrations/flowise.md): Visual LLM orchestration with Tavily.
- [Google ADK](https://docs.tavily.com/documentation/integrations/google-adk.md): Use Tavily with Google's Agent Development Kit.
- [Gradium](https://docs.tavily.com/documentation/integrations/gradium.md): Use Tavily web search with Gradium voice AI agents.
- [Grok Build](https://docs.tavily.com/documentation/integrations/grok-build.md): Real-time web search and research in xAI's Grok Build coding agent.
- [Haystack](https://docs.tavily.com/documentation/integrations/haystack.md): Use Tavily in Haystack pipelines via `tavily-haystack`.
- [Hermes Agent](https://docs.tavily.com/documentation/integrations/hermes-agent.md): Built-in web search and extraction for Hermes Agent, with keyless access and no plugin required.
- [LangChain](https://docs.tavily.com/documentation/integrations/langchain.md): LangChain's recommended search tool.
- [Langflow](https://docs.tavily.com/documentation/integrations/langflow.md): Build multi-agent and RAG apps visually with Tavily.
- [LibreChat](https://docs.tavily.com/documentation/integrations/librechat.md): Web search, extraction, and agent tools inside LibreChat.
- [LlamaIndex](https://docs.tavily.com/documentation/integrations/llamaindex.md): Search the web from LlamaIndex RAG pipelines.
- [Make](https://docs.tavily.com/documentation/integrations/make.md): No-code workflow automation with Tavily.
- [Mastra](https://docs.tavily.com/documentation/integrations/mastra.md): First-class Mastra tools for search, extract, crawl, and map.
- [Merge Gateway](https://docs.tavily.com/documentation/integrations/merge-gateway.md): Use Tavily as the search engine behind Merge Gateway's web search tool.
- [Microsoft 365 Copilot](https://docs.tavily.com/documentation/integrations/microsoft.md): Use Tavily as a declarative agent in Microsoft 365 Copilot or as a Copilot Cowork plugin.
- [n8n](https://docs.tavily.com/documentation/integrations/n8n.md): No-code workflow automation with Tavily.
- [OpenAI](https://docs.tavily.com/documentation/integrations/openai.md): Grounded web search for OpenAI function-calling agents.
- [OpenClaw](https://docs.tavily.com/documentation/integrations/openclaw.md): Add web search and extraction to agents across messaging apps.
- [OpenCode](https://docs.tavily.com/documentation/integrations/opencode.md): Web search, extraction, crawling, and research in the OpenCode terminal agent.
- [Pydantic AI](https://docs.tavily.com/documentation/integrations/pydantic-ai.md): Type-safe AI agents with Tavily.
- [StackAI](https://docs.tavily.com/documentation/integrations/stackai.md): Enhance StackAI workflows with real-time web data.
- [TrueFoundry](https://docs.tavily.com/documentation/integrations/truefoundry.md): Managed Tavily MCP access through the TrueFoundry MCP Gateway.
- [Scalekit](https://docs.tavily.com/documentation/integrations/scalekit.md): Connect agents to Tavily's MCP server through Scalekit AgentKit with managed OAuth.
- [Tines](https://docs.tavily.com/documentation/integrations/tines.md): Automated, no-code intelligence workflows.
- [Vellum](https://docs.tavily.com/documentation/integrations/vellum.md): Built-in web search provider in the Vellum Assistant.
- [Vercel AI SDK](https://docs.tavily.com/documentation/integrations/vercel.md): Add web search, extraction, crawling, and mapping to Vercel AI agents.
- [Zapier](https://docs.tavily.com/documentation/integrations/zapier.md): Connect Tavily to thousands of apps, no code required.

## Partnerships

- [Amazon Bedrock AgentCore](https://docs.tavily.com/documentation/partnerships/amazon.md): Tavily MCP for scalable agent deployment on AWS.
- [Microsoft Azure](https://docs.tavily.com/documentation/partnerships/azure.md): Tavily Remote MCP with Azure AI Foundry and MCP Center.
- [Databricks](https://docs.tavily.com/documentation/partnerships/databricks.md): Tavily MCP for real-time web search and RAG on Databricks.
- [IBM watsonx Orchestrate](https://docs.tavily.com/documentation/partnerships/ibm.md): Tavily research capabilities in IBM watsonx Orchestrate.
- [Snowflake](https://docs.tavily.com/documentation/partnerships/snowflake.md): Tavily as a native app on the Snowflake Marketplace.

## Examples

- [Examples Hub](https://docs.tavily.com/examples/hub.md): Build with Tavily — from quick API recipes to production research agents.
- [Agent Toolkit](https://docs.tavily.com/examples/agent-toolkit/overview.md): Production-grade research agents with battle-tested tools and patterns.
- [Agent Toolkit: Tools Reference](https://docs.tavily.com/examples/agent-toolkit/tools.md): Optimized retrieval primitives for research agents.
- [Agent Toolkit: Chatbot](https://docs.tavily.com/examples/agent-toolkit/chatbot.md): Route between quick search and deep research by query complexity.
- [Agent Toolkit: Hybrid Research](https://docs.tavily.com/examples/agent-toolkit/hybrid-research.md): Combine an internal knowledge base with real-time web research.
- [Agent Toolkit: Company Intelligence](https://docs.tavily.com/examples/agent-toolkit/company-intelligence.md): Crawl, extract, and search for company analysis.
- [Agent Toolkit: Social Media Research](https://docs.tavily.com/examples/agent-toolkit/social-media-research.md): Research a topic across TikTok, Reddit, X, LinkedIn, and more.
- [Web Search Essentials](https://docs.tavily.com/examples/quick-tutorials/search-api.md): Find real-time info, monitor news, and filter by domain.
- [Clean Content Extraction](https://docs.tavily.com/examples/quick-tutorials/extract-api.md): Pull clean markdown or text from any webpage.
- [Site Structure Discovery with Map](https://docs.tavily.com/examples/quick-tutorials/map-api.md): Discover all URLs on a domain, then extract targeted content.
- [Website Crawling and Content Extraction](https://docs.tavily.com/examples/quick-tutorials/crawl-api.md): Extract content from entire websites and build retrieval pipelines.
- [Deep Research with Streaming](https://docs.tavily.com/examples/quick-tutorials/research-streaming.md): Multi-source research with polling/streaming and structured output.
- [Product News Tracker](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker.md): Track real-time product news with Tavily's APIs.
- [Cookbook](https://docs.tavily.com/examples/quick-tutorials/cookbook.md): Guided Jupyter notebooks covering Tavily's APIs.
- [Chat](https://docs.tavily.com/examples/use-cases/chat.md): A conversational agent with search, crawl, and extract.
- [Company Research](https://docs.tavily.com/examples/use-cases/company-research.md): In-depth company research with Search and Extract.
- [Crawl to RAG](https://docs.tavily.com/examples/use-cases/crawl-to-rag.md): Turn any website into a searchable knowledge base.
- [Data Enrichment](https://docs.tavily.com/examples/use-cases/data-enrichment.md): Enhance datasets with Tavily's APIs.
- [Market Researcher](https://docs.tavily.com/examples/use-cases/market-researcher.md): Market insights and analysis for stocks in your portfolio.
- [Meeting Prep](https://docs.tavily.com/examples/use-cases/meeting-prep.md): A meeting-prep agent with real-time research and calendar integration.
- [RAG Evaluation](https://docs.tavily.com/examples/use-cases/web-eval.md): Web-based RAG evaluation with Tavily and LangGraph.
- [Open Source Projects](https://docs.tavily.com/examples/open-sources/projects.md): Popular open-source projects showcasing Tavily.

## Updates

- [Changelog](https://docs.tavily.com/changelog.md): Latest changes to Tavily's APIs and docs.

## OpenAPI Specs

- [OpenAPI](https://docs.tavily.com/documentation/api-reference/openapi.json): Machine-readable OpenAPI specification.

## Optional

- [API Playground](https://app.tavily.com/playground): Try Tavily's APIs interactively.
- [Community](https://discord.gg/TPu2gkaWp2): Join the Tavily Discord.
- [Blog](https://tavily.com/blog): Product updates and technical content.

## Landing page — https://www.tavily.com/

**Tavily ranks #1 in Company Search Benchmark. [Explore the results →](https://www.tavily.com/blog/your-agent-has-the-company-name-how-much-can-it-actually-tell-you-about-it)**

[![Image 5: Tavily by Nebius](https://www.tavily.com/logos/tavily-full.svg)](https://www.tavily.com/)

Product Solutions Resources[Docs](https://docs.tavily.com/)[Pricing](https://www.tavily.com/pricing)

Endpoints

[Overview The web access layer for AI agents](https://www.tavily.com/product)[Search Fast and relevant web results](https://docs.tavily.com/documentation/api-reference/endpoint/search)[Extract Clean and structured content for LLMs](https://docs.tavily.com/documentation/api-reference/endpoint/extract)[Research An agent for in-depth web research](https://docs.tavily.com/documentation/api-reference/endpoint/research)[Crawl Content extracted from entire websites](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)[Map Discover URLs across any website](https://docs.tavily.com/documentation/api-reference/endpoint/map)

Industries

[Financial](https://www.tavily.com/solutions/financial-services)[Insurance](https://www.tavily.com/solutions/insurance)

Explore

[Use Cases](https://www.tavily.com/use-cases)[Post-Training](https://www.tavily.com/solutions/post-training)

Learn

[Blog](https://www.tavily.com/blog)[Certification](https://www.tavily.com/certification)[Events](https://www.tavily.com/events)

Company

[About](https://www.tavily.com/about)[Customers](https://www.tavily.com/customer-stories)[Careers](https://www.tavily.com/careers)

[](https://x.com/tavilyai)[](https://www.linkedin.com/company/tavily)[](https://community.tavily.com/)

Contact Log in

[![Image 6: Tavily by Nebius](https://www.tavily.com/logos/tavily-full.svg)](https://www.tavily.com/)

![Image 7](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2F49a9b081b6c696977c112781c322aa1af700b435-3270x2000.png%3Frect%3D0%2C0%2C3270%2C1483%26w%3D1600%26q%3D75%26auto%3Dformat&w=3840&q=75)

# Connect your AI agents to the web

One secure API for real-time web access.

[Start for free](https://app.tavily.com/home)

Copy setup prompt![Image 8](https://www.tavily.com/_next/image?url=%2Flogos%2Feditors%2FClaude.webp&w=48&q=75)![Image 9](https://www.tavily.com/_next/image?url=%2Flogos%2Feditors%2Fcodex.webp&w=48&q=75)![Image 10](https://www.tavily.com/_next/image?url=%2Flogos%2Feditors%2Fcursor.webp&w=48&q=75)

search extract crawl research search extract crawl research

## Trusted by 3M+ developers around the world

![Image 11: WRITER](https://cdn.sanity.io/images/5tlb0lxv/production/a6aa3b4863c0bf12915aa7b3b545e2d35ae1b371-111x36.svg?h=70&q=75&auto=format)

![Image 12: MongoDB](https://cdn.sanity.io/images/5tlb0lxv/production/16ff2c3504d94e5df8c89eb17c3db0734d67d98a-139x35.svg?h=70&q=75&auto=format)

[![Image 13: JetBrains](https://cdn.sanity.io/images/5tlb0lxv/production/a2c41b1b27ac117e4e42327eb64ff35b42d240ae-164x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/jetbrains)

![Image 14: GROQ](https://cdn.sanity.io/images/5tlb0lxv/production/4c6f0ed3fc67abac3289eb50fc8237b5d1f3adf0-2000x568.png?h=70&q=75&auto=format)

[![Image 15: Rox](https://cdn.sanity.io/images/5tlb0lxv/production/fe7603bb2c1a2f3b9fd40b93648600d8f3c61d7e-55x20.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/rox)

![Image 16: LangChain](https://cdn.sanity.io/images/5tlb0lxv/production/17a41ff0375408b9c2f90335f342fc3a694bd8a6-3000x554.png?h=70&q=75&auto=format)

[![Image 17: Monday](https://cdn.sanity.io/images/5tlb0lxv/production/fbfe747f3d3d8e4ab219b92ec04fd7f385a7f0a8-194x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/monday.com)[![Image 18: Bellcyber](https://cdn.sanity.io/images/5tlb0lxv/production/fdd17a078a267ae49c9dfc404dc6787d59d0bafb-890x258.png?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/bell-cyber)

![Image 19: AWS](https://cdn.sanity.io/images/5tlb0lxv/production/9177596d793b26d549174af03474d5baf630ea01-59x35.svg?h=70&q=75&auto=format)

![Image 20: Mastercard](https://cdn.sanity.io/images/5tlb0lxv/production/8820e6a5c2de2d4c3bfab35d2c75731be207348b-3840x790.png?h=70&q=75&auto=format)

[![Image 21: IBM](https://cdn.sanity.io/images/5tlb0lxv/production/1198f02ebfa2ea912b7fb62ba1502cf312a4f96b-95x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/bell-cyber)

![Image 22: Ironclad](https://cdn.sanity.io/images/5tlb0lxv/production/5d0f82653aecbc78852d0ff5d59a46e8c3c37fa6-186x35.svg?h=70&q=75&auto=format)

![Image 23: Troutman Pepper Locke](https://cdn.sanity.io/images/5tlb0lxv/production/12f2d53f068e3408c96b2cdb3cf36916a351fcef-1500x499.png?h=70&q=75&auto=format)

[![Image 24: BMO](https://cdn.sanity.io/images/5tlb0lxv/production/8bca732842bd4396f7991237d7d4ac09ecde1bba-207x72.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/BMO-AML)

![Image 25: Extend](https://cdn.sanity.io/images/5tlb0lxv/production/09cf2dc9be4ca8a21232a08ccdfc86b4dfa2f049-1500x653.png?h=70&q=75&auto=format)

[![Image 26: Peerbound](https://cdn.sanity.io/images/5tlb0lxv/production/f7f525b6a44e0765e42f1f12259daa83ab74bbf8-1024x192.png?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/peerbound)

![Image 27: WRITER](https://cdn.sanity.io/images/5tlb0lxv/production/a6aa3b4863c0bf12915aa7b3b545e2d35ae1b371-111x36.svg?h=70&q=75&auto=format)

![Image 28: MongoDB](https://cdn.sanity.io/images/5tlb0lxv/production/16ff2c3504d94e5df8c89eb17c3db0734d67d98a-139x35.svg?h=70&q=75&auto=format)

[![Image 29: JetBrains](https://cdn.sanity.io/images/5tlb0lxv/production/a2c41b1b27ac117e4e42327eb64ff35b42d240ae-164x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/jetbrains)

![Image 30: GROQ](https://cdn.sanity.io/images/5tlb0lxv/production/4c6f0ed3fc67abac3289eb50fc8237b5d1f3adf0-2000x568.png?h=70&q=75&auto=format)

[![Image 31: Rox](https://cdn.sanity.io/images/5tlb0lxv/production/fe7603bb2c1a2f3b9fd40b93648600d8f3c61d7e-55x20.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/rox)

![Image 32: LangChain](https://cdn.sanity.io/images/5tlb0lxv/production/17a41ff0375408b9c2f90335f342fc3a694bd8a6-3000x554.png?h=70&q=75&auto=format)

[![Image 33: Monday](https://cdn.sanity.io/images/5tlb0lxv/production/fbfe747f3d3d8e4ab219b92ec04fd7f385a7f0a8-194x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/monday.com)[![Image 34: Bellcyber](https://cdn.sanity.io/images/5tlb0lxv/production/fdd17a078a267ae49c9dfc404dc6787d59d0bafb-890x258.png?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/bell-cyber)

![Image 35: AWS](https://cdn.sanity.io/images/5tlb0lxv/production/9177596d793b26d549174af03474d5baf630ea01-59x35.svg?h=70&q=75&auto=format)

![Image 36: Mastercard](https://cdn.sanity.io/images/5tlb0lxv/production/8820e6a5c2de2d4c3bfab35d2c75731be207348b-3840x790.png?h=70&q=75&auto=format)

[![Image 37: IBM](https://cdn.sanity.io/images/5tlb0lxv/production/1198f02ebfa2ea912b7fb62ba1502cf312a4f96b-95x35.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/bell-cyber)

![Image 38: Ironclad](https://cdn.sanity.io/images/5tlb0lxv/production/5d0f82653aecbc78852d0ff5d59a46e8c3c37fa6-186x35.svg?h=70&q=75&auto=format)

![Image 39: Troutman Pepper Locke](https://cdn.sanity.io/images/5tlb0lxv/production/12f2d53f068e3408c96b2cdb3cf36916a351fcef-1500x499.png?h=70&q=75&auto=format)

[![Image 40: BMO](https://cdn.sanity.io/images/5tlb0lxv/production/8bca732842bd4396f7991237d7d4ac09ecde1bba-207x72.svg?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/BMO-AML)

![Image 41: Extend](https://cdn.sanity.io/images/5tlb0lxv/production/09cf2dc9be4ca8a21232a08ccdfc86b4dfa2f049-1500x653.png?h=70&q=75&auto=format)

[![Image 42: Peerbound](https://cdn.sanity.io/images/5tlb0lxv/production/f7f525b6a44e0765e42f1f12259daa83ab74bbf8-1024x192.png?h=70&q=75&auto=format)Case Study](https://www.tavily.com/customer-stories/peerbound)

/the web access layer for agents

## Loved by developers, built for enterprises

`tavily.search()`

Found sources

Relevant chunks

Relevant chunks

### Ground models with fresh web context

Retrieve live web data, extract relevant content, and return it structured and chunked for models, so agents reason over facts without hallucinating.

![Image 43: Tavily](https://www.tavily.com/logos/tavily-mark-black.svg)

### Handle thousands of web queries in seconds

A production-grade retrieval stack with real-time search, intelligent caching, and indexing keeps latency predictable as traffic grows.

`{"query":"hello@company.com","search_depth":,"max_results":,"include_answer":"error":"Query blocked, PII detected with type: EMAIL"}`

### Ship to production with built-in safeguards

Requests pass through security, privacy, and content validation layers that block PII leakage, prompt injection, and malicious sources.

/security
## Enterprise-grade security, built in.

*   ![Image 44: SOC 2](https://cdn.sanity.io/images/5tlb0lxv/production/36b511f0b167d31a3d615f08f6b846e57d6c8035-58x58.svg)
*   ![Image 45: ZDR](https://cdn.sanity.io/images/5tlb0lxv/production/095ba4bd0869ff34be7ebc664e1311f20472cc60-38x56.svg)
*   ![Image 46: GDPR](https://cdn.sanity.io/images/5tlb0lxv/production/643869df56ef620be654292e8932ea895d978a66-65x62.svg)
*   ![Image 47: ISO 27001](https://cdn.sanity.io/images/5tlb0lxv/production/81d4ad571d6427f9fc54cbb2142f969e11c4c9d2-41x53.svg)

/customers

## Teams ship on Tavily

[View all stories](https://www.tavily.com/customer-stories)

*   [Video 3](https://www.tavily.com/) ![Image 48: Rox](https://cdn.sanity.io/images/5tlb0lxv/production/fe7603bb2c1a2f3b9fd40b93648600d8f3c61d7e-55x20.svg?w=400&q=75&auto=format)
How Rox Cut Account Research from a Week to Seconds with Tavily Watch video[Read story](https://www.tavily.com/customer-stories/rox)  [Video 4](https://www.tavily.com/)  
*   [![Image 49: Jet Brains](https://cdn.sanity.io/images/5tlb0lxv/production/60c8291d2fb74a43f2565d450b86c7a368898c56-164x35.svg?w=400&q=75&auto=format) > “Before web search, the model would hallucinate library methods it didn't know. I ran into this myself building a Telegram integration; it was confidently wrong. Grounding it with real-time web search fixed that immediately. ![Image 50](https://cdn.sanity.io/images/5tlb0lxv/production/7c5e5155321fcd0f5e1e24e1d198d5212bd4e43a-538x538.jpg?w=96&q=75&auto=format)Nick Frolov Head of Product, JetBrains Read story](https://www.tavily.com/customer-stories/jetbrains)
*   [![Image 51: Peerbound](https://cdn.sanity.io/images/5tlb0lxv/production/f7f525b6a44e0765e42f1f12259daa83ab74bbf8-1024x192.png?w=400&q=75&auto=format) 100%description accuracy, up from 20% Read story](https://www.tavily.com/customer-stories/peerbound)

/benchmarks

## Web search driven by research

Company Search

Overall Profiles Financials News & Markets

Answer Quality Score × 100

### [About this benchmark↗](https://www.tavily.com/blog/your-agent-has-the-company-name-how-much-can-it-actually-tell-you-about-it)

This benchmark evaluates how well search providers equip AI agents to answer company research questions. Built around real production query patterns, it tests factual correctness, financial accuracy, and freshness across companies worldwide.

### [Methodology↗](https://huggingface.co/datasets/Tavily/tavily-company-search-benchmark)

Dataset: Tavily's Company Search benchmark

Model: Same set of models for every provider; grounding provided by an AI agent using search results from all providers compared

Scoring: Weighted answer quality, graded by a shared AI judge: complete (1.0), partial (0.85), related (0.15), or irrelevant (0.0)

Normalization: Every provider is judged against the same provider-agnostic reference, using answers written by the shared model from that provider's own search results

Retrieval: max 10 documents per query

/proof is in the numbers

## Trusted in production. Proven at scale.

300M+

monthly requests handled

99.99% uptime 

SLA powering mission-critical systems

180 ms

p50 on Tavily /search making us fastest on the market

3M+

developers using Tavily

Billions

of pages crawled and extracted without downtime

Easy to integrate

with your favorite frameworks and agents

300M+

monthly requests handled

99.99% uptime 

SLA powering mission-critical systems

180 ms

p50 on Tavily /search making us fastest on the market

3M+

developers using Tavily

Billions

of pages crawled and extracted without downtime

Easy to integrate

with your favorite frameworks and agents

/press room

## Tavily in action

[![Image 52: Tavily is Joining Nebius](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2F52bad8aeac15354a0477cf16df30a8bd9ef639b6-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### Tavily is Joining Nebius](https://www.tavily.com/blog/tavily-is-joining-nebius)[![Image 53: Databricks Partners with Tavily on MCP Marketplace](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2Ff0067718585e80b23f2f20fb904eb6621f494b50-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### Databricks Partners with Tavily on MCP Marketplace](https://www.databricks.com/blog/accelerate-ai-development-databricks-discover-govern-and-build-mcp-and-agent-bricks)[![Image 54: IBM Partners with Tavily on WatsonX Platform](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2F44683843cfded0723e763cb394c5e1df282d9b93-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### IBM Partners with Tavily on WatsonX Platform](https://www.ibm.com/new/announcements/driving-smarter-data-enrichment-ibm-and-tavily-partner-for-agentic-ai-solutions)[![Image 55: JetBrains Integrates Tavily for Real-Time AI Search](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2F393b84e533026efab38c1a7c863238a6c46ac772-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### JetBrains Integrates Tavily for Real-Time AI Search](https://www.tavily.com/blog/jetbrains-tavily)[![Image 56: Tavily releases /research endpoint, achieves state-of-the-art](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2F11bb4783c38f80932f0eda608430ee0235611dcc-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### Tavily releases /research endpoint, achieves state-of-the-art](https://chat-research.tavily.com/)[![Image 57: Tavily raises $25M Series A Funding](https://www.tavily.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F5tlb0lxv%2Fproduction%2Fe892ebdb4cb6b40525205c4dfde63ac18badf06b-700x346.webp%3Fw%3D700%26h%3D346%26q%3D75%26auto%3Dformat&w=3840&q=75) ### Tavily raises $25M Series A Funding](https://techcrunch.com/2025/08/06/tavily-raises-25m-to-connect-ai-agents-to-the-web/)

![Image 58](https://www.tavily.com/_next/image?url=%2Ffooter-hero-bg.webp&w=3840&q=75)

## Power your AI with real-time web search

[Try it out](https://app.tavily.com/home)[Explore API docs](https://docs.tavily.com/)

[![Image 59: Tavily](https://www.tavily.com/logos/tavily-mark-black.svg)](https://www.tavily.com/)
Built by researchers. Trusted by 3M+ developers.

Opt into comms 
By submitting my email address, I agree to receive marketing communications. For more information, please see the[Privacy Policy](https://www.tavily.com/privacy).

[](https://x.com/tavilyai)[](https://www.linkedin.com/company/tavily)[](https://github.com/tavily-ai)[](https://www.youtube.com/@TavilyAI)[](https://community.tavily.com/)[](https://luma.com/eventstavily)

## Product

[Overview](https://www.tavily.com/product)[Pricing](https://www.tavily.com/pricing)[Docs](https://docs.tavily.com/)

## Solutions

[Financial Services](https://www.tavily.com/solutions/financial-services)[Insurance](https://www.tavily.com/solutions/insurance)[Post-Training](https://www.tavily.com/solutions/post-training)[Use Cases](https://www.tavily.com/use-cases)

## Resources

[Blog](https://www.tavily.com/blog)[Events](https://www.tavily.com/events)[Customers](https://www.tavily.com/customer-stories)[Certification](https://www.tavily.com/certification)[Community](https://www.tavily.com/community)

## Company

[About](https://www.tavily.com/about)[Careers](https://www.tavily.com/careers)[Partnerships](https://www.tavily.com/partnerships)[Startups](https://www.tavily.com/startups)[Brand](https://www.tavily.com/brand)[Contact](https://www.tavily.com/contact)

## Trust

[Trust Center](https://trust.tavily.com/)[Privacy Policy](https://www.tavily.com/privacy)[Privacy Requests](https://www.tavily.com/legal/privacy-requests)Manage cookies Accessibility

[![Image 60](https://www.tavily.com/compliance/soc2.svg)![Image 61](https://www.tavily.com/compliance/iso.svg)](https://trust.tavily.com/)

© 2026 Tavily Inc. All rights reserved.

[support@tavily.com](mailto:support@tavily.com)

[Website Terms](https://www.tavily.com/website-terms)[Platform Terms](https://www.tavily.com/terms)[Cookie Notice](https://www.tavily.com/cookie-policy)[Acceptable Use](https://www.tavily.com/acceptable-use-policy)

## About — https://docs.tavily.com/documentation/about


# About

> Welcome to Tavily!

<Note>
  Looking for a step-by-step tutorial to get started in under 5 minutes? Head to our [Quickstart guide](/guides/quickstart) and start coding!
</Note>

## Who are we?

We're a team of AI researchers and developers passionate about helping you build the next generation of AI assistants.
Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.

## What is the Tavily Search Engine?

Building an AI agent that leverages realtime online information is not a simple task. Scraping doesn't scale and requires expertise to refine, current search engine APIs don't provide explicit information to queries but simply potential related articles (which are not always related), and are not very customziable for AI agent needs. This is why we're excited to introduce the first search engine for AI agents - [Tavily](https://app.tavily.com).

Tavily is a search engine optimized for LLMs, aimed at efficient, quick and persistent search results. Unlike other search APIs such as Serp or Google, Tavily focuses on optimizing search for AI developers and autonomous AI agents. We take care of all the burden of searching, scraping, filtering and extracting the most relevant information from online sources. All in a single API call!

To try the API in action, you can now use our hosted version on our [API Playground](https://app.tavily.com/playground).

<Info>
  If you're an AI developer looking to integrate your application with our API, or seek increased API limits, [please reach out!](mailto:support@tavily.com)
</Info>

## Why choose Tavily?

Tavily shines where others fail, with a Search API optimized for LLMs.

<AccordionGroup>
  <Accordion title="Purpose-Built">
    Tailored just for LLM Agents, we ensure the search results are optimized for [RAG](https://towardsdatascience.com/retrieval-augmented-generation-intuitively-and-exhaustively-explain-6a39d6fe6fc9). We take care of all the burden in searching, scraping, filtering and extracting information from online sources. All in a single API call! Simply pass the returned search results as context to your LLM.
  </Accordion>

  <Accordion title="Versatility">
    Beyond just fetching results, the Tavily Search API offers precision. With customizable search depths, domain management, and parsing HTML content controls, you're in the driver's seat.
  </Accordion>

  <Accordion title="Performance">
    Committed to speed and efficiency, our API guarantees real-time and trusted information. Our team works hard to improve Tavily's performance over time.
  </Accordion>

  <Accordion title="Integration-friendly">
    We appreciate the essence of adaptability. That's why integrating our API with your existing setup is a breeze. You can choose our [Python library](https://pypi.org/project/tavily-python/), [JavaScript package](https://www.npmjs.com/package/@tavily/core) or a simple API call. You can also use Tavily through any of our supported partners such as [LangChain](/integrations/langchain) and [LlamaIndex](/integrations/llamaindex).
  </Accordion>

  <Accordion title="Transparent & Informative">
    Our detailed documentation ensures you're never left in the dark. From setup basics to nuanced features, we've got you covered.
  </Accordion>
</AccordionGroup>

## How does the Search API work?

Traditional search APIs such as Google, Serp and Bing retrieve search results based on a user query. However, the results are sometimes irrelevant to the goal of the search, and return simple URLs and snippets of content which are not always relevant. Because of this, any developer would need to then scrape the sites to extract relevant content, filter irrelevant information, optimize the content to fit LLM context limits, and more. This task is a burden and requires a lot of time and effort to complete. The Tavily Search API takes care of all of this for you in a single API call.

The Tavily Search API aggregates up to 20 sites per a single API call, and uses proprietary AI to score, filter and rank the top most relevant sources and content to your task, query or goal.
In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal search experience for LLMs.

Tavily can also help your AI agent make better decisions by including a short answer for cross-agent communication.

<Tip>
  With LLM hallucinations, it's crucial to optimize for RAG with the right context and information. This is where Tavily comes in, delivering accurate and precise information for your RAG applications.
</Tip>

## Getting started

[Sign up](https://app.tavily.com) for Tavily to get your API key. You get **1,000 free API Credits every month**. No credit card required.

<Card icon="key" href="https://app.tavily.com" title="Get your free API key" horizontal>
  You get 1,000 free API Credits every month. **No credit card required.**
</Card>

Head to our [API Playground](https://app.tavily.com/playground) to familiarize yourself with our API.

To get started with Tavily's APIs and SDKs using code, head to our [Quickstart Guide](/guides/quickstart) and follow the steps.

<Note>
  Got questions? Stumbled upon an issue? Simply intrigued? Don't hesitate! Our support team is always on standby, eager to assist. Join us, dive deep, and redefine your search experience! [Contact us!](mailto:support@tavily.com)
</Note>

## Quickstart — https://docs.tavily.com/documentation/quickstart


# Quickstart

> Start searching with Tavily in under 5 minutes.

## Get your free Tavily API key

Head to the [Tavily Platform](https://app.tavily.com) and sign in (or create an account). Then, copy one of your API keys from your dashboard.

<Card icon="key" href="https://app.tavily.com" title="Get your free API key" horizontal>
  You get 1,000 free API Credits every month. **No credit card required.**
</Card>

## Install Tavily

Install the Tavily SDK in your language of choice.

<CodeGroup>
  ```bash Python theme={null}
  pip install tavily-python
  ```

  ```bash JavaScript theme={null}
  npm i @tavily/core
  ```
</CodeGroup>

## Start searching with Tavily

Run your first Tavily Search in 4 lines of code. Simply replace the API key in this snippet with your own.

<CodeGroup>
  ```python Python theme={null}
  from tavily import TavilyClient

  tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
  response = tavily_client.search("Who is Leo Messi?")

  print(response)
  ```

  ```js JavaScript theme={null}
  const { tavily } = require("@tavily/core");

  const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
  const response = await tvly.search("Who is Leo Messi?");

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.tavily.com/search \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer tvly-YOUR_API_KEY" \
    -d '{"query": "Who is Leo Messi?"}'
  ```
</CodeGroup>

## Next steps

That's all it takes to start using Tavily's basic features!

If you want to learn how to implement more complex workflows in Python, check out our intermediate-level [Getting Started notebook](https://colab.research.google.com/drive/1dWGtS3u4ocCLebuaa8Ivz7BkZ_40IgH1).

Or, dive deep into our API and read about the different parameters on our [API Reference](/documentation/api-reference/introduction) page, and learn how to integrate natively with one of our [SDKs](/sdk).

## Agents — https://docs.tavily.com/agents


# Agents

> The canonical setup guide for AI agents and the developers who build them: choose how to connect to Tavily, choose the right capability, and use agent-grade defaults.

Tavily is the web layer for AI agents. Use Tavily when an agent needs live web **search**, page **extraction**, site **crawling**, site **mapping**, or cited **research**.

This page answers three questions, in order:

1. [Which Tavily docs should an agent fetch?](#1-agent-readable-docs)
2. [How should I connect to Tavily?](#2-choose-how-to-connect)
3. [Which Tavily capability should I use?](#3-choose-a-capability)

## 1. Agent-readable docs

Every Tavily docs page is also served as clean Markdown — append `.md` to any docs URL.

**Start here.** Use [`https://docs.tavily.com/llms.txt`](https://docs.tavily.com/llms.txt) as the documentation index, this page ([`agents.md`](https://docs.tavily.com/agents.md)) as the canonical setup guide, and [`https://docs.tavily.com/llms-full.txt`](https://docs.tavily.com/llms-full.txt) for the full text of all docs.

| Resource | What it is | When to fetch it |
| - | - | - |
| [`llms.txt`](https://docs.tavily.com/llms.txt) | Compact index of every Tavily doc. | First, to find the right page. |
| [`agents.md`](https://docs.tavily.com/agents.md) | This setup guide. | When configuring Tavily or choosing a path. |
| [`llms-full.txt`](https://docs.tavily.com/llms-full.txt) | Full text of all docs. | When you need broad context and have the budget. |
| Page `.md` URLs | Markdown version of one page. | When you already know the page you need. |

### Documentation MCP server

Mintlify hosts a documentation MCP server for searching and reading Tavily's public docs. For Tavily's web search and extraction tools, follow the [Tavily MCP Server guide](/documentation/mcp).

To connect to the documentation server, use the settings below. No Tavily API key or sign-in is required.

* **Server URL:** `https://docs.tavily.com/mcp`
* **Transport:** Streamable HTTP

For Claude Code:

```bash theme={null}
claude mcp add --transport http tavily-docs https://docs.tavily.com/mcp
```

After connecting, try asking: "Find the URL limit for Tavily Extract in the documentation."

The documentation server also provides a tool for submitting documentation feedback.

## 2. Choose how to connect

Choose based on what Tavily must **do**, not only where you happen to be running.

| If you are… | Use | Why it fits | Start at |
| - | - | - | - |
| An autonomous agent with no credentials or API key | **Keyless / MCP** | No key, no account — add a header for Search/Extract, or use the no-key remote MCP. Upgrade to SDK/API for Crawl, Map, or Research. | [`/documentation/keyless`](https://docs.tavily.com/documentation/keyless.md) |
| Building Tavily into an app, backend, or agent runtime that calls it in production | **SDK / API** | Your code calls Tavily directly at runtime. Get a free key at app.tavily.com. | [`/documentation/api-reference/introduction`](https://docs.tavily.com/documentation/api-reference/introduction.md) |
| Setting Tavily up for a team or org, or standardizing it across many agent clients (e.g. everyone's Cursor / Claude Code) | **MCP** | Governed, shared, reusable access via the remote server (OAuth or API key). | [`/documentation/mcp`](https://docs.tavily.com/documentation/mcp.md) |
| Adding Tavily to your own local coding or research session right now (single developer, not a team rollout) | **CLI + Skills** | Terminal access to search, extract, and research; install the CLI and run `tvly login`. | [`/documentation/agent-skills`](https://docs.tavily.com/documentation/agent-skills.md) |

**Quick rules**

* Production app or runtime → **SDK / API**.
* Shared across a team or org — even in Cursor or Claude Code → **MCP**.
* Just your own local session → **CLI + Skills**.
* Terminal access alone doesn't make CLI the right fit — match the choice to where Tavily ultimately needs to run.

**Connect**

Once you've picked a path, here's the one-step setup for each:

```bash API theme={null}
curl --request POST \
  --url https://api.tavily.com/search \
  --header 'Authorization: Bearer tvly-YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"query": "your query"}'
```

```bash MCP theme={null}
# Add the remote server (Claude Code example)
claude mcp add tavily-remote-mcp --transport http https://mcp.tavily.com/mcp/
```

```bash CLI theme={null}
pip install tavily-cli
tvly login
```

## No account? Connect without a key

For autonomous agents that can't manage credentials, Tavily offers two no-key paths.

| Path | What it is | Start at |
| - | - | - |
| **Keyless** | Search and Extract **only** — send header `X-Tavily-Access-Mode: keyless`, or use the remote MCP with no key. Crawl, Map, and Research require an API key. | [`/documentation/keyless`](https://docs.tavily.com/documentation/keyless.md) |
| **x402** | Pay-per-request Advanced Search **only** (no Extract/Crawl/Map/Research) in USDC on Base over the x402 protocol — no key, no account, no human. | [`/documentation/machine-payments/x402`](https://docs.tavily.com/documentation/machine-payments/x402.md) |

## 3. Choose a capability

Lead with **Search** when sources are unknown; move to the others once you have URLs or a site to work through.

| Capability | Use it when | Reference |
| - | - | - |
| **Search** | Sources are unknown or current web context is needed — the default start. | [`/endpoint/search`](https://docs.tavily.com/documentation/api-reference/endpoint/search.md) |
| **Extract** | You already have the URL, or picked one from Search. | [`/endpoint/extract`](https://docs.tavily.com/documentation/api-reference/endpoint/extract.md) |
| **Map** | You need a site's structure before crawling it. | [`/endpoint/map`](https://docs.tavily.com/documentation/api-reference/endpoint/map.md) |
| **Crawl** | Many pages on a site must be read. | [`/endpoint/crawl`](https://docs.tavily.com/documentation/api-reference/endpoint/crawl.md) |
| **Research** | The output should be cited synthesis: a report, comparison, or decision-ready answer. | [`/endpoint/research`](https://docs.tavily.com/documentation/api-reference/endpoint/research.md) |

> **Search or Research?** Use Search when you need raw source URLs and content to process yourself. Use Research when you need a finished, multi-source answer with citations.

## Recommended defaults

These favor quality, which is what most agent workflows need. See [Best Practices for Search](/documentation/best-practices/best-practices-search) for the full reference.

* Prefer **`search_depth="advanced"`** for source discovery, comparisons, and high-confidence answers; use `"basic"` for quick lookups.
* For latency-sensitive use cases, **`fast`** and **`ultra-fast`** trade some relevance for lower latency.
* Add **`chunks_per_source=3`** for stronger evidence per source (chunks require advanced, basic or fast depth).
* Use **`max_results=5`** for focused answers, **`10`** for broader research.
* Use **`include_domains`** / **`exclude_domains`** when source trust matters.
* Prefer **Search → Extract** for grounded answers: Search to find sources, then Extract for full content.
* Avoid **`include_answer`** unless you need a quick answer seed — and still verify against sources.
* Use **Research** for cited synthesis: a report, comparison, or decision-ready answer.

A typical agent-grade Search call:

```python Python theme={null}
from tavily import TavilyClient

client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = client.search(
    "your query",
    search_depth="advanced",
    chunks_per_source=3,
    max_results=5,
)
```

```javascript JavaScript theme={null}
const { tavily } = require("@tavily/core");

const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
const response = await tvly.search("your query", {
  searchDepth: "advanced",
  chunksPerSource: 3,
  maxResults: 5,
});
```

```bash cURL theme={null}
curl --request POST \
  --url https://api.tavily.com/search \
  --header 'Authorization: Bearer tvly-YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "your query",
    "search_depth": "advanced",
    "chunks_per_source": 3,
    "max_results": 5
  }'
```

## Availability

Some Tavily capabilities, limits, and defaults depend on your account, plan, or enterprise configuration. If a tool or parameter is unavailable, check the relevant endpoint docs and your account settings before retrying a different workflow.

> **Developer resource:** [Agent Toolkit](https://docs.tavily.com/examples/agent-toolkit/overview.md) is for developers *building* production research agents, not for agents configuring Tavily autonomously. Reach for it when you need deeper research flows, retrieval orchestration, deduplication, summarization, or structured outputs.

## Credits & Pricing — https://docs.tavily.com/documentation/api-credits


# Credits & Pricing

> Learn how to get and manage your Tavily API Credits.

## Free API Credits

<Card icon="key" href="https://app.tavily.com" title="Get your free API key" horizontal>
  You get 1,000 free API Credits every month. **No credit card required.**
</Card>

## Pricing Overview

Tavily operates on a simple, credit-based model:

* **Free**: 1,000 credits/month
* **Pay-as-you-go**: \$0.008 per credit (allows you to be charged per credit once your plan’s credit limit is reached).
* **Monthly plans**: \$0.0075 - \$0.005 per credit
* **Enterprise**: Custom pricing and volume

| **Plan** | **Credits per month** | **Monthly price** | **Price per credit** |
| - | - | - | - |
| **Researcher** | 1,000 | Free | - |
| **Project** | 4,000 | \$30 | \$0.0075 |
| **Bootstrap** | 15,000 | \$100 | \$0.0067 |
| **Startup** | 38,000 | \$220 | \$0.0058 |
| **Growth** | 100,000 | \$500 | \$0.005 |
| **Pay as you go** | Per usage | \$0.008 / Credit | \$0.008 |
| **Enterprise** | Custom | Custom | Custom |

Head to [billing](https://app.tavily.com/billing) to explore our different options and manage your plan.

## API Credits Costs

### Tavily Search

Your [search depth](/api-reference/endpoint/search#body-search-depth) determines the cost of your request.

* **Basic Search (`basic`):**
  Each request costs **1 API credit**.

* **Advanced Search (`advanced`):**
  Each request costs **2 API credits**.

### Tavily Extract

The number of successful URL extractions and your [extraction depth](/api-reference/endpoint/extract#body-extract-depth) determines the cost of your request. You never get charged if a URL extraction fails.

* **Basic Extract (`basic`):**
  Every 5 successful URL extractions cost **1 API credit**

* **Advanced Extract (`advanced`):**
  Every 5 successful URL extractions cost **2 API credits**

### Tavily Map

The number of pages mapped and whether or not natural-language [instructions](/documentation/api-reference/endpoint/map#instructions) are specified determines the cost of your request. You never get charged if a map request fails.

* **Regular Mapping:**
  Every 10 successful pages returned cost **1 API credit**

* **Map with (`instructions`):**
  Every 10 successful pages returned cost **2 API credits**

### Tavily Crawl

Tavily Crawl combines both mapping and extraction operations, so the cost is the sum of both:

* **Crawl Cost = Mapping Cost + Extraction Cost**

For example:

* If you crawl 10 pages with basic extraction depth, you'll be charged **1 credit for mapping** (10 pages) + **2 credits for extraction** (10 successful extractions ÷ 5) = **3 total credits**
* If you crawl 10 pages with advanced extraction depth, you'll be charged **1 credit for mapping** + **4 credits for extraction** = **5 total credits**

### Tavily Research

Tavily Research follows a dynamic
pricing model with minimum and maximum credit consumption boundaries associated
with each request. The minimum and maximum boundaries differ based on if the
request uses `model=mini` or `model=pro`.

| Request Cost Boundaries | model=pro | model=mini |
| - | - | - |
| Per-request minimum | 15 credits | 4 credits |
| Per-request maximum | 250 credits | 110 credits |

## Try Tavily Without an API Key — https://docs.tavily.com/documentation/keyless


# Try Tavily Without an API Key

> Use Tavily Search and Extract for free, with zero setup. No account, no API key, no configuration. Keyless responses are identical to keyed responses.

Drop Tavily into an agent or script in seconds. When you're ready for production, swap in an API key. No code changes required.

## Why Tavily?

Tavily is an AI search engine optimized for agent consumption. Built-in tools like `web_search` and `web_fetch` return raw HTML or shallow snippets, so your agent spends tokens parsing, filtering, and guessing what's relevant. Tavily Search returns clean, ranked, and scored results optimized for LLM consumption. Tavily Extract pulls structured content from any URL without dealing with JavaScript rendering or HTML cleanup. The result: fewer tokens, better context, more reliable agent behavior.

Use Tavily Search and Extract for free, with zero setup. No account, no API key, no configuration. Your agent gets real results immediately and can upgrade to an API key whenever you need higher limits.

<Note>
  **Free, with a clear upgrade path.** Keyless access is free and rate-limited, ideal for exploration and light use. Hit the cap and you don't have to pay: sign up for a free API key (1,000 credits/month, no credit card) and swap it in. No code changes required.
</Note>

<Info>
  **Same results, same schema.** Keyless responses are identical to keyed responses. Your agent can't tell the difference on success.
</Info>

## Direct API

Send a request with the `X-Tavily-Access-Mode: keyless` header. That's it.

<CodeGroup>
  ```bash Search theme={null}
  curl -X POST https://api.tavily.com/search \
    -H "Content-Type: application/json" \
    -H "X-Tavily-Access-Mode: keyless" \
    -d '{"query": "latest AI news", "max_results": 3}'
  ```

  ```bash Extract theme={null}
  curl -X POST https://api.tavily.com/extract \
    -H "Content-Type: application/json" \
    -H "X-Tavily-Access-Mode: keyless" \
    -d '{"urls": ["https://www.tavily.com"]}'
  ```
</CodeGroup>

The response follows the standard Tavily response schema. See the [API Reference](/documentation/api-reference/endpoint/search) for details.

## MCP Server

Connect to the [Tavily Remote MCP](/documentation/mcp) with the keyless header. Your agent gets `tavily-search` and `tavily-extract` tools with zero configuration.

```bash Claude Code theme={null}
claude mcp add tavily-remote-mcp --transport http https://mcp.tavily.com/mcp/ \
  --header "X-Tavily-Access-Mode: keyless"
```

The header is required — without it the server asks your client to sign in. Clients that only accept a URL can't send it; use an API key with those.

### Agent-installable prompt

Paste this into any AI assistant to let it set up Tavily itself:

```text theme={null}
Set up the Tavily MCP server so you can search the web and extract content from URLs. Follow these steps:

1. Detect which platform you're running on (Claude Code, Cursor, Windsurf, Claude Desktop, etc.)
2. Install the Tavily MCP server using the correct method for your platform:
   - Server URL: https://mcp.tavily.com/mcp/
   - Transport: Streamable HTTP
   - Headers: `X-Tavily-Access-Mode: keyless` (required, selects free keyless access)
   - Authentication: no API key or account needed
3. Verify the server is connected and you have access to the tavily-search and tavily-extract tools.
4. Run a test search (e.g. "Tavily API features for search, extract, crawl, and research") to confirm you get real results from a live source.
5. Report back whether setup succeeded.
```

## Supported endpoints

| Endpoint | Keyless | Notes |
| - | - | - |
| `/search` | Yes | Full search with all parameters |
| `/extract` | Yes | Content extraction from URLs |

## Rate limits

Keyless access is free but rate-limited. When you hit the limit, [sign up](https://app.tavily.com) for a free API key to keep going. Pass it as a Bearer token and nothing else changes:

```bash theme={null}
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -d '{"query": "latest AI news"}'
```

<Info>
  When you hit a limit, Tavily returns natural-language instructions telling your agent what happened and how to continue.
</Info>

## FAQ

<AccordionGroup>
  <Accordion title="Do keyless and keyed responses look different?">
    No. Success responses are identical, with the same fields and the same schema. Your agent can switch from keyless to keyed without changing how it parses responses.
  </Accordion>

  <Accordion title="Can I use keyless and an API key together?">
    If you send both `X-Tavily-Access-Mode: keyless` and a valid `Authorization: Bearer` header, the API key takes precedence. The request uses your account's limits, not the keyless budget.
  </Accordion>

  <Accordion title="What if I need /crawl, /map, or /research?">
    These endpoints require an API key. [Sign up](https://app.tavily.com) to access them. You get 1,000 free credits monthly.
  </Accordion>
</AccordionGroup>

## Rate Limits — https://docs.tavily.com/documentation/rate-limits


# Rate Limits

> Learn about Tavily's API rate limits for both  development and production environments.

We offer two types of rate limits based on the environment associated with your API key.

<Card icon="key" href="https://app.tavily.com" title="Get your API key" horizontal>
  Create your Development or Production API keys.
</Card>

| Environment | Requests per minute (RPM) |
| - | - |
| `Development` | 100 |
| `Production` | 1,000 |

## Crawl Endpoint Rate Limits

The crawl endpoint has a separate rate limit that applies to both development and production keys:

| Environment | Requests per minute (RPM) |
| - | - |
| `Development` | 100 |
| `Production` | 100 |

## Research Endpoint Rate Limits

The research endpoint has a separate rate limit that applies to both development and production keys for creating research tasks. Note that polling requests to retrieve the status of ongoing research tasks follow the default rate limits as decribed above.

| Environment | Requests per minute (RPM) |
| - | - |
| `Development` | 20 |
| `Production` | 20 |

## Usage Endpoint Rate Limits

The usage endpoint has a separate rate limit that applies to both development and production keys:

| Environment | Requests per 10 minutes |
| - | - |
| `Development` | 10 |
| `Production` | 10 |

## Handling Rate Limit Responses

When an API-key request exceeds a rate limit, the API returns `429 Too Many Requests`. If the response includes `Retry-After`, wait the indicated number of seconds before retrying. For example:

```http theme={null}
HTTP/2 429 Too Many Requests
Content-Type: application/json
Retry-After: 60

{
  "detail": {
    "error": "Your request has been blocked due to excessive requests. Please reduce the rate of requests."
  }
}
```

The 60-second delay is an example; use the value returned in the response. Error messages can vary by the limit reached; use the HTTP status and header for retry handling rather than matching the message text. [Keyless access](/documentation/keyless) uses a different error format and separate limits.

<Tip>
  1. Access to production keys requires either an active **Paid Plan** or **PAYGO** enabled. More information can be found [here](/guides/api-credits).
  2. When using the REST API, ensure you include your API key in the header to apply the correct rate limits.
</Tip>

## Tavily MCP Server — https://docs.tavily.com/documentation/mcp


# Tavily MCP Server

> Tavily MCP Server allows you to use the Tavily API in your MCP clients.

<CardGroup cols={2}>
  <Card title="GitHub" icon="github" href="https://github.com/tavily-ai/tavily-mcp" horizontal>
    `/tavily-ai/tavily-mcp`

    <img noZoom src="https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social" alt="GitHub Repo stars" />
  </Card>

  <Card title="NPM" icon="npm" href="https://www.npmjs.com/package/tavily-mcp" horizontal>
    `@tavily/mcp`

    <img noZoom src="https://img.shields.io/npm/dt/tavily-mcp" alt="npm" />
  </Card>
</CardGroup>

<Tip>
  **Compatible with both [Cursor](https://cursor.sh) and [Claude Desktop](https://claude.ai/download)!**

  Tavily MCP is also compatible with any MCP client.
</Tip>

<Info>
  **Check out our
  [tutorial](https://medium.com/@dustin_36183/building-a-knowledge-graph-assistant-combining-tavily-and-neo4j-mcp-servers-with-claude-db92de075df9)
  on combining Tavily MCP with Neo4j MCP server!**
</Info>

<Frame>
  <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/mcp-demo.gif?s=387a3d560de94008f981b8896dcb25d2" alt="Tavily MCP Demo" width="800" height="909" data-path="images/mcp-demo.gif" />
</Frame>

<Tabs>
  <Tab title="Overview">
    The Model Context Protocol (MCP) is an open standard that enables AI systems to interact seamlessly with various data sources and tools, facilitating secure, two-way connections.

    Developed by Anthropic, the Model Context Protocol (MCP) enables AI assistants like Claude to seamlessly integrate with Tavily's advanced search and data extraction capabilities. This integration provides AI models with real-time access to web information, complete with sophisticated filtering options and domain-specific search features.
  </Tab>

  <Tab title="Features">
    The Tavily MCP server provides:

    * Seamless interaction with the tavily-search and tavily-extract tools
    * Real-time web search capabilities through the tavily-search tool
    * Intelligent data extraction from web pages via the tavily-extract tool
  </Tab>
</Tabs>

## Remote MCP Server

The easiest way to take advantage of Tavily MCP is by using the remote URL. This provides a seamless experience without requiring local installation or configuration.

Simply use the remote MCP server URL with your Tavily API key:

```
https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key> 
```

Get your Tavily API key from [tavily.com](https://www.tavily.com/).

<Note>
  **No key?** Your client will prompt you to sign in. For free keyless access instead, see [keyless](/documentation/keyless).
</Note>

### Connect to Cursor

<a href="cursor://anysphere.cursor-deeplink/mcp/install?name=tavily-remote-mcp&config=eyJjb21tYW5kIjoibnB4IC15IG1jcC1yZW1vdGUgaHR0cHM6Ly9tY3AudGF2aWx5LmNvbS9tY3AvP3RhdmlseUFwaUtleT08eW91ci1hcGkta2V5PiIsImVudiI6e319">
  <img noZoom src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install MCP Server" />
</a>

Click the ⬆️ Add to Cursor ⬆️ button, this will do most of the work for you but you will still need to edit the configuration to add your API-KEY. You can get a Tavily API key [here](https://www.tavily.com/).

once you click the button you should be redirect to Cursor ...

You will then be redirected to your `mcp.json` file where you have to add `your-api-key`.

```json theme={null}
{
  "mcpServers": {
    "tavily-remote-mcp": {
      "command": "npx -y mcp-remote https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>",
      "env": {}
    }
  }
}
```

### Connect to Claude Desktop

Claude desktop now supports adding `integrations` which is currently in beta. An integration in this case is the Tavily Remote MCP, below I will explain how to add the MCP as an `integration` in Claude desktop.

Open claude desktop, click the button with the two sliders and then navigate to add integrations. Name the integration and insert the Tavily remote MCP url with your API key. You can get a Tavily API key [here](https://www.tavily.com/). Click `Add` to confirm.

### OpenAI

Allow models to use remote MCP servers to perform tasks.

* You first need to export your OPENAI\_API\_KEY
* You must also add your Tavily API-key to `<your-api-key>`, you can get a Tavily API key [here](https://www.tavily.com/)

```python theme={null}
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "tavily",
            "server_url": "https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>",
            "require_approval": "never",
            ## Optional default parameters:
            "headers": {
                "DEFAULT_PARAMETERS": json.dumps({
                    "include_favicon": True,
                    "include_images": False,
                    "include_raw_content": False,
                }),
            },
        },
    ],
    input="Do you have access to the tavily mcp server?",
)

print(resp.output_text)
```

### Connect to Claude Code

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) natively supports remote MCP servers with OAuth authentication. Add Tavily to your Claude Code configuration by running:

```bash theme={null}
claude mcp add tavily-remote-mcp --transport http https://mcp.tavily.com/mcp/
```

When you start a new conversation, Claude Code will open a browser window for you to complete the OAuth flow and authorize access to your Tavily account. No API key needed in the URL — authentication is handled automatically via OAuth.

You can also manually add the following to your `.claude/settings.json`:

```json theme={null}
{
  "mcpServers": {
    "tavily-remote-mcp": {
      "type": "http",
      "url": "https://mcp.tavily.com/mcp/"
    }
  }
}
```

Alternatively, you can also connect using `mcp-remote`:

```bash theme={null}
claude mcp add tavily-remote-mcp -- npx -y mcp-remote https://mcp.tavily.com/mcp
```

### Clients that don't support remote MCPs

mcp-remote is a lightweight bridge that lets MCP clients that can only talk to local (stdio) servers securely connect to remote MCP servers over HTTP + SSE with OAuth-based auth, so you can host and update your server in the cloud while existing clients keep working. It serves as an experimental stop-gap until popular MCP clients natively support remote, authorized servers.

```json theme={null}
{
    "tavily-remote": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>"
      ]
    }
}
```

### OAuth Authentication

The Tavily Remote MCP server supports secure OAuth authentication, allowing you to connect and authorize seamlessly with compatible clients.

<AccordionGroup>
  <Accordion title="Using MCP Inspector" icon="magnifying-glass">
    Open the MCP Inspector and click "Open Auth Settings". Select the OAuth flow and complete these steps:

    1. Metadata discovery
    2. Client registration
    3. Preparing authorization
    4. Request authorization and obtain the authorization code
    5. Token request
    6. Authentication complete

    Once finished, you will receive an access token that lets you securely make authenticated requests to the Tavily Remote MCP server.
  </Accordion>

  <Accordion title="Using Other MCP Clients" icon="plug">
    You can configure your MCP client to use OAuth without including your Tavily API key in the URL. For example, in Cursor's `mcp.json`:

    ```json theme={null}
    {
      "mcpServers": {
        "tavily-remote-mcp": {
          "command": "npx mcp-remote https://mcp.tavily.com/mcp",
          "env": {}
        }
      }
    }
    ```

    If you need to clear stored OAuth credentials and reauthenticate, run:

    ```bash theme={null}
    rm -rf ~/.mcp-auth
    ```
  </Accordion>
</AccordionGroup>

<Note>
  **API Key Selection for OAuth**

  When using OAuth authentication, you can control which API key is used by naming a key `mcp_auth_default` in your Tavily dashboard:

  * **Personal account**: If you have a key named `mcp_auth_default` in your personal account, it will be used for all OAuth-authenticated requests.
  * **Team account**: If your team has a key named `mcp_auth_default`, it will be used for all OAuth-authenticated requests.
  * **Both set**: If both your personal account and your team have a key named `mcp_auth_default`, the **personal key takes priority**.
  * **Neither set**: If no `mcp_auth_default` key exists, the `default` key in your personal account will be used. If no `default` key is set, the first available key will be used.

  OAuth authentication is optional—you can still use API key authentication at any time by including your Tavily API key in the URL query parameter (`?tavilyApiKey=...`) or by setting it in the Authorization header.
</Note>

Alternatively, you can also run the MCP server locally.

### Default Parameters

When using the remote MCP, you can specify default parameters for all requests by including a `DEFAULT_PARAMETERS` header containing a JSON object with your desired defaults. Example:

```
{"include_images":true, "search_depth": "advanced", "max_results": 10}
```

### Session & User Attribution

The remote MCP server automatically attaches identifiers to every Tavily API call so requests can be attributed back to a session. It generates `X-Session-Id` on its own, while `X-Human-Id` is forwarded only when supplied by the client.

* **`X-Session-Id`** — generated per MCP session (the `mcp-session-id` returned during the MCP `initialize` handshake). All tool calls within the same MCP session share the same value.
* **`X-Human-Id`** — if your client provides an `X-Human-Id` header (or `humanId` query parameter on the MCP URL), it is forwarded through to the Tavily API, helping Tavily better understand multi-step interactions and improve response quality. For security, Tavily hashes human IDs before processing or storing them.

See [Session Tracking](/documentation/api-reference/introduction#session--user-tracking) for the underlying API contract.

## Local Installation

### Prerequisites

<AccordionGroup>
  <Accordion title="Required Tools" icon="wrench">
    * [Tavily API key](https://app.tavily.com/home)
      * If you don't have a Tavily API key, you can sign up for a free account [here](https://app.tavily.com/home)
    * [Claude Desktop](https://claude.ai/download) or [Cursor](https://cursor.sh)
    * [Node.js](https://nodejs.org/) (v20 or higher)
      * You can verify your Node.js installation by running:
        ```bash theme={null}
        node --version
        ```
  </Accordion>

  <Accordion title="Git Installation (Optional)" icon="code-branch">
    Only needed if using Git installation method:

    * On macOS: `brew install git`
    * On Linux:
      * Debian/Ubuntu: `sudo apt install git`
      * RedHat/CentOS: `sudo yum install git`
    * On Windows: Download [Git for Windows](https://git-scm.com/download/win)
  </Accordion>
</AccordionGroup>

<CodeGroup>
  ```bash NPX theme={null}
  npx -y tavily-mcp@0.1.3
  ```

  ```bash Git theme={null}
  git clone https://github.com/tavily-ai/tavily-mcp.git
  cd tavily-mcp
  npm install
  npm run build
  ```
</CodeGroup>

<Note>
  Although you can launch a server on its own, it's not particularly helpful in
  isolation. Instead, you should integrate it into an MCP client.
</Note>

### Configuring MCP Clients

<Tabs>
  <Tab title="Cursor">
    > **Note**: Requires Cursor version 0.45.6 or higher

    To set up the Tavily MCP server in Cursor:

    1. Open Cursor Settings
    2. Navigate to Features > MCP Servers
    3. Click on the "+ Add New MCP Server" button
    4. Fill out the following information:
       * **Name**: Enter a nickname for the server (e.g., "tavily-mcp")
       * **Type**: Select "command" as the type
       * **Command**: Enter the command to run the server:
         ```bash theme={null}
         env TAVILY_API_KEY=tvly-YOUR_API_KEY npx -y tavily-mcp@0.1.3
         ```
         <Warning>Replace `tvly-YOUR_API_KEY` with your Tavily API key from [app.tavily.com/home](https://app.tavily.com/home)</Warning>

    <Frame>
      <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/cursor-reference.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=fb7da4e530057cf30d5e2fcf6de69f28" alt="Cursor Interface Example" width="1088" height="436" data-path="images/cursor-reference.png" />
    </Frame>
  </Tab>

  <Tab title="Claude Desktop">
    <CodeGroup>
      ```bash macOS theme={null}
      # Create the config file if it doesn't exist
      touch "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

      # Opens the config file in TextEdit
      open -e "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

      # Alternative method using Visual Studio Code
      code "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
      ```

      ```bash Windows theme={null}
      code %APPDATA%\Claude\claude_desktop_config.json
      ```
    </CodeGroup>

    Add this configuration (replace `tvly-YOUR_API_KEY-here` with your [Tavily API key](https://tavily.com/api-keys)):

    ```json Configuration theme={null}
    {
      "mcpServers": {
        "tavily-mcp": {
          "command": "npx",
          "args": ["-y", "tavily-mcp@0.1.2"],
          "env": {
            "TAVILY_API_KEY": "tvly-YOUR_API_KEY-here"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### Default Parameters

For local MCP setups, you can set default parameter values using the `DEFAULT_PARAMETERS` environment variable. This allows you to configure default search behavior without specifying these parameters in every request.

```json theme={null}
{
  "mcpServers": {
    "tavily-mcp": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": "your-api-key-here",
        "DEFAULT_PARAMETERS": "{\"include_images\": true, \"max_results\": 15, \"search_depth\": \"advanced\"}"
      }
    }
  }
}
```

### Session & User Attribution

The local MCP server automatically attaches identifiers to every Tavily API call so requests can be attributed back to a session:

* **`X-Session-Id`** — auto-generated once per MCP process and reused for every tool call.
* **`X-Human-Id`** — if you set the `HUMAN_ID` environment variable, that value is forwarded through to the Tavily API on every request, helping Tavily better understand multi-step interactions and improve response quality. For security, Tavily hashes human IDs before processing or storing them.

See [Session Tracking](/documentation/api-reference/introduction#session--user-tracking) for the underlying API contract.

## Usage Examples

<AccordionGroup>
  <Accordion title="Tavily Search Examples" icon="magnifying-glass">
    1. **General Web Search**:

    ```
    Can you search for recent developments in quantum computing?
    ```

    2. **News Search**:

    ```
    Search for news articles about AI startups from the last 7 days.
    ```

    3. **Domain-Specific Search**:

    ```
    Search for climate change research on nature.com and sciencedirect.com
    ```
  </Accordion>

  <Accordion title="Tavily Extract Examples" icon="file-export">
    **Extract Article Content**: `Extract the main content from this article:
          https://example.com/article`
  </Accordion>

  <Accordion title="Combined Usage" icon="wand-magic-sparkles">
    ```
    Search for news articles about AI startups from the last 7 days and extract the main content from each article to generate a detailed report.
    ```
  </Accordion>
</AccordionGroup>

## Troubleshooting

<Accordion title="Server Not Found" icon="server">
  If you encounter server connection issues, run these commands to verify your environment:

  ```bash theme={null}
  npm --version
  node --version
  ```

  Make sure to also check your configuration syntax for any errors.
</Accordion>

<Accordion title="NPX Issues" icon="terminal">
  If experiencing problems with npx, locate your executable:

  ```bash theme={null}
  which npx
  ```

  <Tip>
    Once you have the path, update your configuration to use the full path to the npx executable.
  </Tip>
</Accordion>

<Accordion title="API Key Issues" icon="key">
  When troubleshooting API key problems, verify that your key is:

  * Properly formatted with the `tvly-` prefix
  * Valid and active in your Tavily dashboard
  * Correctly configured in your environment variables

  <Tip>
    You can test your API key validity by making a simple test request through the [Tavily Playground](https://app.tavily.com/playground)
  </Tip>
</Accordion>

## Acknowledgments

<CardGroup cols={2}>
  <Card title="Model Context Protocol" icon="book" href="https://modelcontextprotocol.io">
    For the MCP specification
  </Card>

  <Card title="Anthropic" icon="robot" href="https://www.anthropic.com/claude">
    For Claude Desktop
  </Card>
</CardGroup>

## Tavily CLI — https://docs.tavily.com/documentation/tavily-cli


# Tavily CLI

> Search, extract, crawl, map, and research the web from your terminal.

<CardGroup cols={2}>
  <Card title="PyPI" icon="python" href="https://github.com/tavily-ai/tavily-cli" horizontal>
    `tavily-cli`
  </Card>

  <Card title="Get API Key" icon="key" href="https://app.tavily.com" horizontal>
    Sign up at tavily.com
  </Card>
</CardGroup>

The Tavily CLI (`tvly`) brings the full Tavily API to your command line. Run web searches, extract content from URLs, crawl websites, discover sitemaps, and launch deep research — all from a single tool.

Every command supports `--json` for machine-readable output, making it easy to integrate into scripts, pipelines, and AI agent workflows.

## Installation

Install with the official installer:

```bash theme={null}
curl -fsSL https://cli.tavily.com/install.sh | bash
```

Or install manually:

```bash theme={null}
uv tool install tavily-cli   # or: pip install tavily-cli
```

Verify the install:

```bash theme={null}
tvly --version
```

## Authentication

You need a Tavily API key to use the CLI. Get one for free at [tavily.com](https://tavily.com).

<AccordionGroup>
  <Accordion title="Option 1: Login with an API key (recommended)" icon="key" defaultOpen="true">
    ```bash theme={null}
    tvly login --api-key tvly-YOUR_API_KEY
    ```

    This stores your key in `~/.tavily/config.json` (readable only by your user).
  </Accordion>

  <Accordion title="Option 2: Browser-based OAuth" icon="browser">
    ```bash theme={null}
    tvly login
    ```

    This opens your browser for authentication. Tokens are stored in `~/.mcp-auth/`.

    <Note>OAuth login requires Node.js/npx to be available on your system.</Note>
  </Accordion>

  <Accordion title="Option 3: Environment variable" icon="code">
    ```bash theme={null}
    export TAVILY_API_KEY=tvly-YOUR_API_KEY
    ```
  </Accordion>
</AccordionGroup>

### Check Your Auth Status

```bash theme={null}
tvly auth
```

### Log Out

```bash theme={null}
tvly logout
```

This removes stored credentials from disk.

## Session Tracking

The CLI automatically attaches a unique `session_id` to every command it runs, so requests from the same shell invocation can be grouped together. This applies to `tvly search`, `extract`, `crawl`, `map`, and `research`.

To also associate requests with a specific end-user, set the `TAVILY_HUMAN_ID` environment variable:

```bash theme={null}
export TAVILY_HUMAN_ID=h_4f9ac
```

Alternatively, add a `human_id` field to `~/.tavily/config.json` — the environment variable takes precedence if both are set.

For security, Tavily hashes human IDs before processing or storing them. See [Session Tracking](/documentation/api-reference/introduction#session--user-tracking) in the API reference for details.

## Commands

<AccordionGroup>
  <Accordion title="tvly search" icon="magnifying-glass">
    Search the web using Tavily's AI-optimized search engine.

    ```bash theme={null}
    tvly search "your search query"
    ```

    **Reading from stdin:**

    ```bash theme={null}
    echo "your query" | tvly search -
    ```

    #### Options

    | Option | Type | Default | Description |
    | - | - | - | - |
    | `--depth` | `ultra-fast` \| `fast` \| `basic` \| `advanced` | `basic` | Search depth. Higher depth returns more detailed results. |
    | `--max-results` | `0–20` | `5` | Number of results to return. |
    | `--topic` | `general` \| `news` \| `finance` | `general` | Optimize search for a specific topic. |
    | `--time-range` | `day` \| `week` \| `month` \| `year` | — | Filter results to a relative time window. |
    | `--start-date` | `YYYY-MM-DD` | — | Only include results published after this date. |
    | `--end-date` | `YYYY-MM-DD` | — | Only include results published before this date. |
    | `--include-domains` | comma-separated | — | Restrict results to these domains. |
    | `--exclude-domains` | comma-separated | — | Exclude results from these domains. |
    | `--country` | country code | — | Boost results from a specific country. |
    | `--include-answer` | `basic` \| `advanced` | — | Include an AI-generated answer with results. |
    | `--include-raw-content` | `markdown` \| `text` | — | Include full page content for each result. |
    | `--include-images` | flag | `false` | Include image results. |
    | `--include-image-descriptions` | flag | `false` | Include AI-generated image descriptions. |
    | `--chunks-per-source` | integer | — | Number of content chunks per source (requires `fast` or `advanced` depth). |
    | `-o` / `--output` | file path | — | Save output to a file. |
    | `--json` | flag | `false` | Output raw JSON. |

    #### Examples

    ```bash theme={null}
    # Basic search
    tvly search "best programming languages 2025"

    # News from the past week
    tvly search "AI regulation" --topic news --time-range week

    # Advanced search with AI answer
    tvly search "how does transformer architecture work" --depth advanced --include-answer advanced

    # Restrict to specific sites
    tvly search "python tutorials" --include-domains realpython.com,docs.python.org

    # Save results to a file
    tvly search "climate change data" -o results.txt
    ```
  </Accordion>

  <Accordion title="tvly extract" icon="file-lines">
    Extract clean, readable content from one or more URLs.

    ```bash theme={null}
    tvly extract <url> [<url> ...]
    ```

    You can pass up to 20 URLs at once.

    #### Options

    | Option | Type | Default | Description |
    | - | - | - | - |
    | `--query` | string | — | Rerank extracted chunks by relevance to this query. |
    | `--chunks-per-source` | `1–5` | — | Number of content chunks per URL (requires `--query`). |
    | `--extract-depth` | `basic` \| `advanced` | `basic` | Extraction depth. `advanced` handles JavaScript-rendered pages. |
    | `--format` | `markdown` \| `text` | `markdown` | Output format for extracted content. |
    | `--include-images` | flag | `false` | Include image URLs found on the page. |
    | `--timeout` | `1–60` | — | Maximum wait time in seconds. |
    | `-o` / `--output` | file path | — | Save output to a file. |
    | `--json` | flag | `false` | Output raw JSON. |

    #### Examples

    ```bash theme={null}
    # Extract content from a URL
    tvly extract https://example.com/article

    # Extract multiple URLs
    tvly extract https://example.com/page1 https://example.com/page2

    # Extract with relevance filtering
    tvly extract https://docs.python.org/3/tutorial/ --query "list comprehensions" --chunks-per-source 3

    # Extract JavaScript-rendered content
    tvly extract https://example.com/spa-page --extract-depth advanced
    ```
  </Accordion>

  <Accordion title="tvly crawl" icon="spider-web">
    Crawl a website starting from a URL and extract content from every discovered page.

    ```bash theme={null}
    tvly crawl <url>
    ```

    #### Options

    | Option | Type | Default | Description |
    | - | - | - | - |
    | `--max-depth` | `1–5` | `1` | How many levels deep to crawl from the start URL. |
    | `--max-breadth` | integer | `20` | Maximum links to follow per page. |
    | `--limit` | integer | `50` | Total page cap for the crawl. |
    | `--instructions` | string | — | Natural language guidance for the crawler (e.g., "only follow documentation pages"). |
    | `--chunks-per-source` | `1–5` | — | Chunks per page (requires `--instructions`). |
    | `--extract-depth` | `basic` \| `advanced` | `basic` | Extraction depth for crawled pages. |
    | `--format` | `markdown` \| `text` | `markdown` | Output format for extracted content. |
    | `--select-paths` | comma-separated regex | — | Only crawl paths matching these patterns. |
    | `--exclude-paths` | comma-separated regex | — | Skip paths matching these patterns. |
    | `--select-domains` | comma-separated regex | — | Only follow links to matching domains. |
    | `--exclude-domains` | comma-separated regex | — | Skip links to matching domains. |
    | `--allow-external` / `--no-external` | flag | — | Whether to follow links to external domains. |
    | `--include-images` | flag | `false` | Include images found on pages. |
    | `--timeout` | `10–150` | — | Maximum wait time in seconds. |
    | `-o` / `--output` | file path | — | Save full JSON output to a file. |
    | `--output-dir` | directory path | — | Save each crawled page as a separate `.md` file. |
    | `--json` | flag | `false` | Output raw JSON. |

    #### Examples

    ```bash theme={null}
    # Crawl a docs site (1 level deep)
    tvly crawl https://docs.example.com

    # Deep crawl with a page limit
    tvly crawl https://docs.example.com --max-depth 3 --limit 100

    # Crawl only blog posts
    tvly crawl https://example.com --select-paths "/blog/.*"

    # Save each page as a markdown file
    tvly crawl https://docs.example.com --output-dir ./docs-mirror

    # Guided crawl
    tvly crawl https://docs.example.com --instructions "focus on API reference pages"
    ```
  </Accordion>

  <Accordion title="tvly map" icon="sitemap">
    Discover all URLs on a website without extracting content. Useful for building sitemaps or understanding site structure.

    ```bash theme={null}
    tvly map <url>
    ```

    #### Options

    | Option | Type | Default | Description |
    | - | - | - | - |
    | `--max-depth` | `1–5` | `1` | How many levels deep to discover links. |
    | `--max-breadth` | integer | `20` | Maximum links to follow per page. |
    | `--limit` | integer | `50` | Maximum total URLs to discover. |
    | `--instructions` | string | — | Natural language guidance for URL discovery. |
    | `--select-paths` | comma-separated regex | — | Only include URLs matching these path patterns. |
    | `--exclude-paths` | comma-separated regex | — | Exclude URLs matching these path patterns. |
    | `--select-domains` | comma-separated regex | — | Only include URLs from matching domains. |
    | `--exclude-domains` | comma-separated regex | — | Exclude URLs from matching domains. |
    | `--allow-external` / `--no-external` | flag | — | Whether to include external domain links. |
    | `--timeout` | `10–150` | — | Maximum wait time in seconds. |
    | `-o` / `--output` | file path | — | Save output to a file. |
    | `--json` | flag | `false` | Output raw JSON. |

    #### Examples

    ```bash theme={null}
    # Discover URLs on a site
    tvly map https://example.com

    # Deep URL discovery
    tvly map https://docs.example.com --max-depth 3 --limit 200

    # Only find API doc URLs
    tvly map https://docs.example.com --select-paths "/api/.*"

    # Save URL list to a file
    tvly map https://example.com -o urls.txt
    ```
  </Accordion>

  <Accordion title="tvly research" icon="magnifying-glass-chart">
    Launch deep, multi-step research on any topic. Tavily's research engine searches the web, synthesizes sources, and produces a comprehensive report with citations.

    ```bash theme={null}
    tvly research "your research topic"
    ```

    This is equivalent to `tvly research run "your research topic"`.

    **Reading from stdin:**

    ```bash theme={null}
    echo "your topic" | tvly research -
    ```

    #### Options

    | Option | Type | Default | Description |
    | - | - | - | - |
    | `--model` | `mini` \| `pro` \| `auto` | `auto` | Research model. `mini` is faster, `pro` is more thorough, `auto` picks the best fit. |
    | `--no-wait` | flag | `false` | Return the `request_id` immediately without waiting for completion. |
    | `--stream` | flag | `false` | Stream results in real-time as the research progresses. |
    | `--output-schema` | file path | — | Path to a JSON schema file for structured output. |
    | `--citation-format` | `numbered` \| `mla` \| `apa` \| `chicago` | — | Citation style for the research report. |
    | `--poll-interval` | seconds | `10` | How often to check for completion. |
    | `--timeout` | seconds | `600` | Maximum time to wait for results. |
    | `-o` / `--output` | file path | — | Save the report to a file. |
    | `--json` | flag | `false` | Output raw JSON. |

    #### Subcommands

    **Check status of a running research task:**

    ```bash theme={null}
    tvly research status <request_id>
    ```

    **Poll a research task until it completes:**

    ```bash theme={null}
    tvly research poll <request_id>
    ```

    The `poll` subcommand accepts `--poll-interval`, `--timeout`, `-o`, and `--json`.

    #### Examples

    ```bash theme={null}
    # Quick research
    tvly research "comparison of React vs Vue in 2025"

    # Thorough research with the pro model
    tvly research "impact of AI on healthcare" --model pro

    # Stream results as they come in
    tvly research "quantum computing breakthroughs" --stream

    # Fire-and-forget: get the ID, poll later
    tvly research "market analysis of EVs" --no-wait
    # ... later:
    tvly research poll <request_id>

    # Save the report to a file with APA citations
    tvly research "effects of remote work on productivity" --citation-format apa -o report.md
    ```
  </Accordion>
</AccordionGroup>

## Interactive Mode

Run `tvly` with no arguments to enter an interactive REPL where you can run commands without the `tvly` prefix:

```bash theme={null}
tvly
```

```
❯ search "latest AI news"
❯ extract https://example.com
❯ exit
```

## Global Options

These options work with the top-level `tvly` command:

| Option | Description |
| - | - |
| `--version` | Print the CLI version and exit. |
| `--status` | Print the version and authentication status. |
| `--json` | Output as JSON (applies to `--version` and `--status`). |
| `--help` | Show help for any command. |

```bash theme={null}
tvly --version
tvly --status
tvly search --help
```

## JSON Mode

Add `--json` to any command to get machine-readable JSON output. This is useful for piping into other tools like `jq`, or for integration with scripts and AI agents.

```bash theme={null}
# Pipe search results through jq
tvly search "AI news" --json | jq '.results[].title'

# Use in a shell script
RESULTS=$(tvly search "latest papers on RAG" --json)
```

All human-readable output (spinners, status messages) is written to stderr, so stdout contains only the clean JSON when `--json` is used.

## Environment Variables

| Variable | Description |
| - | - |
| `TAVILY_API_KEY` | Your Tavily API key. Takes precedence over stored credentials. |

<Accordion title="Exit Codes">
  | Code | Meaning |
  | - | - |
  | `0` | Success. |
  | `2` | Invalid input or usage error (e.g., missing required argument). |
  | `3` | Authentication error (no API key found, or login failed). |
  | `4` | API error (rate limit, invalid request, server error). |
</Accordion>

## Uninstall

```bash theme={null}
pip uninstall tavily-cli
```

To also remove stored credentials:

```bash theme={null}
rm -rf ~/.tavily ~/.mcp-auth
```

## Tavily Search — https://docs.tavily.com/documentation/api-reference/endpoint/search


# Tavily Search

> Execute a search query using Tavily Search.



## OpenAPI

````yaml POST /search
openapi: 3.0.3
info:
  title: Tavily Search and Extract API
  description: >-
    Our REST API provides seamless access to Tavily Search, a powerful search
    engine for LLM agents, and Tavily Extract, an advanced web scraping solution
    optimized for LLMs.
  version: 1.0.0
servers:
  - url: https://api.tavily.com/
security: []
tags:
  - name: Search
  - name: Extract
  - name: Crawl
  - name: Map
  - name: Research
  - name: Feedback
  - name: Usage
  - name: Logs
paths:
  /search:
    post:
      summary: Search for data based on a query
      description: Execute a search query using Tavily Search.
      operationId: search
      requestBody:
        description: Parameters for the Tavily Search request.
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: The search query to execute with Tavily.
                  example: who is Leo Messi?
                search_depth:
                  type: string
                  description: >-
                    Controls the latency vs. relevance tradeoff and how
                    `results[].content` is generated:

                    - `advanced`: Highest relevance with increased latency. Best
                    for detailed, high-precision queries. Returns multiple
                    semantically relevant snippets per URL (configurable via
                    `chunks_per_source`).

                    - `basic`: A balanced option for relevance and latency.
                    Ideal for general-purpose searches. Returns multiple
                    semantically relevant snippets per URL (configurable via
                    `chunks_per_source`).

                    - `fast`: Prioritizes lower latency while maintaining good
                    relevance. Returns multiple semantically relevant snippets
                    per URL (configurable via `chunks_per_source`).

                    - `ultra-fast`: Minimizes latency above all else. Best for
                    time-critical use cases. Returns one NLP summary per URL.


                    **Cost**:

                    - `basic`, `fast`, `ultra-fast`: 1 API Credit

                    - `advanced`: 2 API Credits


                    See [Search Best
                    Practices](/documentation/best-practices/best-practices-search#search-depth)
                    for guidance on choosing the right search depth.
                  enum:
                    - advanced
                    - basic
                    - fast
                    - ultra-fast
                  default: basic
                chunks_per_source:
                  type: integer
                  description: >-
                    Chunks are short content snippets (about 500 characters each
                    for `basic` and `fast`, 800 for `advanced`) pulled directly
                    from the source. Use `chunks_per_source` to define the
                    maximum number of relevant chunks returned per source and to
                    control the `content` length. Chunks will appear in the
                    `content` field as: `<chunk 1> [...] <chunk 2> [...] <chunk
                    3>`. Adjacent chunks may be joined into one longer passage,
                    so chunk length is a target, not a hard limit. Available
                    when `search_depth` is `advanced`, `basic` or `fast`.
                  default: 3
                  minimum: 1
                  maximum: 3
                max_results:
                  type: integer
                  example: 1
                  description: The maximum number of search results to return.
                  default: 10
                  minimum: 0
                  maximum: 20
                topic:
                  type: string
                  description: >-
                    The category of the search.`news` is useful for retrieving
                    real-time updates, particularly about politics, sports, and
                    major current events covered by mainstream media sources.
                    `general` is for broader, more general-purpose searches that
                    may include a wide range of sources.
                  default: general
                  enum:
                    - general
                    - news
                    - finance
                time_range:
                  type: string
                  description: >-
                    The time range back from the current date to filter results
                    based on publish date or last updated date. Useful when
                    looking for sources that have published or updated data. By
                    default, results with no detectable published date are not
                    removed; set `filter_by_published_date` to `true` to remove
                    them.
                  enum:
                    - day
                    - week
                    - month
                    - year
                    - d
                    - w
                    - m
                    - 'y'
                  default: null
                start_date:
                  type: string
                  description: >-
                    Will return all results after the specified start date based
                    on publish date or last updated date. Required to be written
                    in the format YYYY-MM-DD. By default, results with no
                    detectable published date are not removed; set
                    `filter_by_published_date` to `true` to remove them.
                  example: '2025-02-09'
                  default: null
                end_date:
                  type: string
                  description: >-
                    Will return all results before the specified end date based
                    on publish date or last updated date. Required to be written
                    in the format YYYY-MM-DD. By default, results with no
                    detectable published date are not removed; set
                    `filter_by_published_date` to `true` to remove them.
                  example: '2025-12-29'
                  default: null
                include_published_date:
                  type: boolean
                  description: >-
                    Include a `published_date` field in each result. The date is
                    Tavily's best estimate of when the source was published or
                    last updated, so it can be later than the original publish
                    date. Results with no detectable date return `null`.
                    Automatically enabled when `topic` is `news`.


                    **Note**: this feature is currently in beta.
                  default: false
                filter_by_published_date:
                  type: boolean
                  description: >-
                    Remove results whose published date falls outside the
                    `time_range`, `start_date`, or `end_date` window. Results
                    with no detectable published date are also removed. Setting
                    this to `true` also enables `include_published_date`.


                    If you want date-window filtering but don't want to lose
                    sources without a detectable date, leave this `false` and
                    set `include_published_date: true` together with a date
                    range instead.
                  default: false
                include_answer:
                  oneOf:
                    - type: boolean
                    - type: string
                      enum:
                        - basic
                        - advanced
                  description: >-
                    Include an LLM-generated answer to the provided query.
                    `basic` or `true` returns a quick answer. `advanced` returns
                    a more detailed answer.
                  default: false
                include_raw_content:
                  oneOf:
                    - type: boolean
                    - type: string
                      enum:
                        - markdown
                        - text
                  description: >-
                    Include the cleaned and parsed HTML content of each search
                    result. `markdown` or `true` returns search result content
                    in markdown format. `text` returns the plain text from the
                    results and may increase latency.
                  default: false
                include_images:
                  type: boolean
                  description: >-
                    Include images in the response. Returns both a top-level
                    `images` list of query-related images and an `images` array
                    inside each result object with images extracted from that
                    specific source.
                  default: false
                include_image_descriptions:
                  type: boolean
                  description: >-
                    When `include_images` is `true`, also add a descriptive text
                    for each image.
                  default: false
                include_favicon:
                  type: boolean
                  description: Whether to include the favicon URL for each result.
                  default: false
                include_domains:
                  type: array
                  description: >-
                    A list of domains to specifically include in the search
                    results. Maximum 300 domains.
                  items:
                    type: string
                  default: []
                exclude_domains:
                  type: array
                  description: >-
                    A list of domains to specifically exclude from the search
                    results. Maximum 150 domains.
                  items:
                    type: string
                  default: []
                include_domains_mode:
                  type: string
                  description: >-
                    Controls how `include_domains` is applied. `restrict` limits
                    results to only the listed domains. `prefer` also searches
                    the rest of the web, so results outside `include_domains`
                    can still surface, rather than excluding them. Defaults to
                    `restrict`, so `include_domains` acts as a hard filter
                    unless set to `prefer`. Setting it without `include_domains`
                    returns a 400 error.
                  enum:
                    - restrict
                    - prefer
                  default: restrict
                country:
                  type: string
                  description: >-
                    Boost search results from a specific country. This will
                    prioritize content from the selected country in the search
                    results. Available only if topic is `general`.
                  enum:
                    - afghanistan
                    - albania
                    - algeria
                    - andorra
                    - angola
                    - argentina
                    - armenia
                    - australia
                    - austria
                    - azerbaijan
                    - bahamas
                    - bahrain
                    - bangladesh
                    - barbados
                    - belarus
                    - belgium
                    - belize
                    - benin
                    - bhutan
                    - bolivia
                    - bosnia and herzegovina
                    - botswana
                    - brazil
                    - brunei
                    - bulgaria
                    - burkina faso
                    - burundi
                    - cambodia
                    - cameroon
                    - canada
                    - cape verde
                    - central african republic
                    - chad
                    - chile
                    - china
                    - colombia
                    - comoros
                    - congo
                    - costa rica
                    - croatia
                    - cuba
                    - cyprus
                    - czech republic
                    - denmark
                    - djibouti
                    - dominican republic
                    - ecuador
                    - egypt
                    - el salvador
                    - equatorial guinea
                    - eritrea
                    - estonia
                    - ethiopia
                    - fiji
                    - finland
                    - france
                    - gabon
                    - gambia
                    - georgia
                    - germany
                    - ghana
                    - greece
                    - guatemala
                    - guinea
                    - haiti
                    - honduras
                    - hungary
                    - iceland
                    - india
                    - indonesia
                    - iran
                    - iraq
                    - ireland
                    - israel
                    - italy
                    - jamaica
                    - japan
                    - jordan
                    - kazakhstan
                    - kenya
                    - kuwait
                    - kyrgyzstan
                    - latvia
                    - lebanon
                    - lesotho
                    - liberia
                    - libya
                    - liechtenstein
                    - lithuania
                    - luxembourg
                    - madagascar
                    - malawi
                    - malaysia
                    - maldives
                    - mali
                    - malta
                    - mauritania
                    - mauritius
                    - mexico
                    - moldova
                    - monaco
                    - mongolia
                    - montenegro
                    - morocco
                    - mozambique
                    - myanmar
                    - namibia
                    - nepal
                    - netherlands
                    - new zealand
                    - nicaragua
                    - niger
                    - nigeria
                    - north korea
                    - north macedonia
                    - norway
                    - oman
                    - pakistan
                    - panama
                    - papua new guinea
                    - paraguay
                    - peru
                    - philippines
                    - poland
                    - portugal
                    - qatar
                    - romania
                    - russia
                    - rwanda
                    - saudi arabia
                    - senegal
                    - serbia
                    - singapore
                    - slovakia
                    - slovenia
                    - somalia
                    - south africa
                    - south korea
                    - south sudan
                    - spain
                    - sri lanka
                    - sudan
                    - sweden
                    - switzerland
                    - syria
                    - taiwan
                    - tajikistan
                    - tanzania
                    - thailand
                    - togo
                    - trinidad and tobago
                    - tunisia
                    - turkey
                    - turkmenistan
                    - uganda
                    - ukraine
                    - united arab emirates
                    - united kingdom
                    - united states
                    - uruguay
                    - uzbekistan
                    - venezuela
                    - vietnam
                    - yemen
                    - zambia
                    - zimbabwe
                  default: null
                language:
                  type: string
                  description: >-
                    Boost search results in a specific language. Accepts an ISO
                    639-1 code (e.g. `en`, `fr`, `zh-cn`) or an English language
                    name (e.g. `english`, `french`). By default this only boosts
                    matching-language results in ranking; pass
                    `filter_by_language: true` to strictly filter out
                    non-matching results instead. For best results, write your
                    `query` in the same language you set here.
                  example: en
                  default: null
                filter_by_language:
                  type: boolean
                  description: >-
                    Strictly filter out search results that don't match the
                    `language` parameter, instead of only boosting them in
                    ranking. Requires `language` to be set; returns a 400 error
                    otherwise.
                  default: false
                auto_parameters:
                  type: boolean
                  description: >-
                    When `auto_parameters` is enabled, Tavily automatically
                    configures search parameters based on your query's content
                    and intent. You can still set other parameters manually, and
                    your explicit values will override the automatic ones. The
                    parameters `include_answer`, `include_raw_content`, and
                    `max_results` must always be set manually, as they directly
                    affect response size. Note: `search_depth` may be
                    automatically set to advanced when it's likely to improve
                    results. This uses 2 API credits per request. To avoid the
                    extra cost, you can explicitly set `search_depth` to
                    `basic`.
                  default: false
                exact_match:
                  type: boolean
                  description: >-
                    Ensure that only search results containing the exact quoted
                    phrase(s) in the query are returned, bypassing synonyms or
                    semantic variations. Wrap target phrases in quotes within
                    your query (e.g. `"John Smith" CEO Acme Corp`). Punctuation
                    is typically ignored inside quotes.
                  default: false
                include_usage:
                  type: boolean
                  description: Whether to include credit usage information in the response.
                  default: false
                safe_search:
                  type: boolean
                  description: >-
                    Whether to filter out adult or unsafe content from results.
                    Not supported for `fast` or `ultra-fast` search depths.
                  default: false
              required:
                - query
      responses:
        '200':
          description: Search results returned successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  query:
                    type: string
                    description: The search query that was executed.
                    example: Who is Leo Messi?
                  answer:
                    type: string
                    description: >-
                      A short answer to the user's query, generated by an LLM.
                      Included in the response only if `include_answer` is
                      requested (i.e., set to `true`, `basic`, or `advanced`)
                    example: >-
                      Lionel Messi, born in 1987, is an Argentine footballer
                      widely regarded as one of the greatest players of his
                      generation. He spent the majority of his career playing
                      for FC Barcelona, where he won numerous domestic league
                      titles and UEFA Champions League titles. Messi is known
                      for his exceptional dribbling skills, vision, and
                      goal-scoring ability. He has won multiple FIFA Ballon d'Or
                      awards, numerous La Liga titles with Barcelona, and holds
                      the record for most goals scored in a calendar year. In
                      2014, he led Argentina to the World Cup final, and in
                      2015, he helped Barcelona capture another treble. Despite
                      turning 36 in June, Messi remains highly influential in
                      the sport.
                  images:
                    type: array
                    description: >-
                      A list of query-related images from image search. If
                      `include_image_descriptions` is true, each item will have
                      `url` and `description`. Note: per-result images are also
                      returned inside each result object's `images` field.
                    example: []
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                        description:
                          type: string
                  results:
                    type: array
                    description: A list of sorted search results, ranked by relevancy.
                    items:
                      type: object
                      properties:
                        title:
                          type: string
                          description: The title of the search result.
                          example: Lionel Messi Facts | Britannica
                        url:
                          type: string
                          description: The URL of the search result.
                          example: https://www.britannica.com/facts/Lionel-Messi
                        content:
                          type: string
                          description: A short description of the search result.
                          example: >-
                            Lionel Messi, an Argentine footballer, is widely
                            regarded as one of the greatest football players of
                            his generation. Born in 1987, Messi spent the
                            majority of his career playing for Barcelona, where
                            he won numerous domestic league titles and UEFA
                            Champions League titles. Messi is known for his
                            exceptional dribbling skills, vision, and goal
                        score:
                          type: number
                          format: float
                          description: The relevance score of the search result.
                          example: 0.81025416
                        raw_content:
                          type: string
                          description: >-
                            The cleaned and parsed HTML content of the search
                            result. Only if `include_raw_content` is true.
                          example: null
                        published_date:
                          type: string
                          description: >-
                            Tavily's best estimate of when the source was
                            published or last updated. Can be later than the
                            original publish date. `null` if no date could be
                            detected. Only returned when
                            `include_published_date` is `true` (automatically
                            enabled when `topic` is `news`).
                          example: Tue, 11 Mar 2025 17:00:00 GMT
                        favicon:
                          type: string
                          description: The favicon URL for the result.
                          example: https://britannica.com/favicon.png
                        images:
                          type: array
                          description: >-
                            A list of images extracted from this search result.
                            Only included when `include_images` is `true`. If
                            `include_image_descriptions` is `true`, each item
                            will have `url` and `description`.
                          items:
                            type: object
                            properties:
                              url:
                                type: string
                              description:
                                type: string
                        id:
                          type: string
                          description: Unique identifier for this result
                          example: a3f9c2-04
                  auto_parameters:
                    type: object
                    description: >-
                      A dictionary of the selected auto_parameters, only shown
                      when `auto_parameters` is true.
                    example:
                      topic: general
                      search_depth: basic
                  response_time:
                    type: number
                    format: float
                    description: Time in seconds it took to complete the request.
                    example: '1.67'
                  usage:
                    type: object
                    description: Credit usage details for the request.
                    example:
                      credits: 1
                  request_id:
                    type: string
                    description: >-
                      A unique request identifier you can share with customer
                      support to help resolve issues with specific requests.
                    example: 123e4567-e89b-12d3-a456-426614174111
                required:
                  - query
                  - results
                  - images
                  - response_time
                  - answer
        '400':
          description: Bad Request - Your request is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: >-
                    <400 Bad Request, (e.g Invalid topic. Must be 'general' or
                    'news'.)>
        '401':
          description: Unauthorized - Your API key is wrong or missing.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: 'Unauthorized: missing or invalid API key.'
        '422':
          description: >-
            Request validation failed. The detail array identifies invalid
            fields.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationError'
              example:
                detail:
                  - type: string_type
                    loc:
                      - body
                      - query
                    msg: Input should be a valid string
                    input: []
        '429':
          description: >-
            Too Many Requests. Error messages and retry delays can vary by
            rate-limit rule.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: >-
                    Your request has been blocked due to excessive requests.
                    Please reduce the rate of requests.
          headers:
            Retry-After:
              $ref: '#/components/headers/RetryAfter'
        '432':
          description: Key limit or Plan Limit exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: >-
                    <432 Custom Forbidden Error (e.g This request exceeds your
                    plan's set usage limit. Please upgrade your plan or contact
                    support@tavily.com)>
        '433':
          description: PayGo limit exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: >-
                    This request exceeds the pay-as-you-go limit. You can
                    increase your limit on the Tavily dashboard.
        '500':
          description: Internal Server Error - We had a problem with our server.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
              example:
                detail:
                  error: Internal Server Error
      security:
        - bearerAuth: []
      x-codeSamples:
        - lang: python
          label: Python SDK
          source: |-
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.search("Who is Leo Messi?")

            print(response)
        - lang: javascript
          label: JavaScript SDK
          source: |-
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.search("Who is Leo Messi?");

            console.log(response);
components:
  schemas:
    ApiError:
      type: object
      properties:
        detail:
          type: object
          properties:
            error:
              type: string
    ValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            type: object
            properties:
              loc:
                type: array
                items:
                  oneOf:
                    - type: string
                    - type: integer
              msg:
                type: string
              type:
                type: string
              input: {}
              ctx:
                type: object
  headers:
    RetryAfter:
      description: >-
        When present, the number of seconds to wait before retrying. Read the
        returned value; the delay can vary.
      schema:
        type: integer
        minimum: 0
      example: 60
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header in the form Bearer <token>, where <token>
        is your Tavily API key (e.g., Bearer tvly-YOUR_API_KEY).

````