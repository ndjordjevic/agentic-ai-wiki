# brave-search

## Fetch log
- Inbox URL: https://brave.com/search/api/
- Final URL: https://brave.com/search/api/
- Fetched: 2026-06-09
- Pages: 5
- Mode: standard

## Landing page — https://brave.com/search/api/

Brave Search API powers agents and chatbots with the world's largest independent index of the Web. The service provides real-time search data through multiple specialized endpoints including Web, Images, Videos, News, and LLM Context.

### Pricing Plans

**Search**: $5 per 1,000 requests with $5 monthly free credits. Includes custom reranking via Goggles, extra snippets, and schema-enriched results. Capacity: 50 queries/second.

**Answers**: $4 per 1,000 requests plus $5 per million tokens. Features grounding with citations and streaming. Capacity: 2 queries/second.

**Enterprise**: Custom terms and dedicated support available through contact form.

### Key Features

- World-class quality comparable to major search engines
- Independent index: 30+ billion pages updated 100 million times daily
- Search Goggles for custom result re-ranking and filtering
- Up to five real-time extra snippets per search
- Zero Data Retention for enterprise customers
- SOC 2 Type II attestation
- Privacy-first architecture with independent Web Discovery Project

### Developer Resources

- Documentation and code examples (Python, cURL, JavaScript, Go)
- MCP Server: https://github.com/brave/brave-search-mcp-server
- API Dashboard: https://api-dashboard.search.brave.com

### Navigation — Search API sections
- API features: https://brave.com/search/api/
- Developer docs: https://api-dashboard.search.brave.com/app/documentation/web-search/get-started
- Use cases: https://brave.com/search/api/use-cases/
- How-to guides: https://brave.com/search/api/guides/
- Latest API news: https://brave.com/category/brave-search-news/
- Tools & integrations: https://brave.com/search/api/tools/
- MCP Server: https://github.com/brave/brave-search-mcp-server
- Log in / sign up: https://api-dashboard.search.brave.com/login

## Use cases — https://brave.com/search/api/use-cases/

The Brave Search API has ten primary use cases:

### LLM Context Applications
1. **Connect internal chatbots to the open Web** — Enable proprietary-trained chatbots to access real-time web data securely.
2. **Improve accuracy of AI responses at lower costs** — Deliver pre-extracted, AI-optimized Web content rather than raw links requiring manual processing.
3. **Real-time grounding to reduce AI hallucinations** — Anchor chatbot responses to a verifiable, real-time Web index to prevent fabricated information.

### Business Intelligence
4. **Build a market-research agent** — Automate research tasks using AWS Bedrock AgentCore integration.
5. **Competitive intelligence for due diligence** — Maintain continuously updated company and competitor profiles with financial, operational, and strategic data.
6. **Real-time reputation tracking** — Monitor brand mentions and sentiment across sources to identify PR issues quickly.

### Enterprise Applications
7. **Analysis of legal docs and precedence** — Enable firms to cross-reference documents against case precedent and other contextual info from across the Web.
8. **Regulatory and compliance tracking** — Automatically monitor evolving regulations, SEC filings, AML guidelines across jurisdictions.
9. **Fraud and risk detection** — Augment internal data with real-time external intelligence on emerging fraud patterns.

### Retail & Consumer
10. **Unbiased tech reviews** — Deliver authentic reviews by filtering out SEO-spam and affiliate-link clutter using custom Goggles filters.

## Guides — https://brave.com/search/api/guides/

Recent integration guides:

- "How to use the Brave Search API with OpenClaw" (Apr 1, 2026)
- "How to add Brave Search to Claude Desktop with MCP" (May 6, 2025)
- "How to use Brave Search with Dify" (May 6, 2025)
- "How to use Brave Search with n8n (local)" (May 6, 2025)
- "Mapping the AI software and services landscape" (May 6, 2025)
- "How to use Brave Search with Open WebUI" (May 2, 2024)
- "Using Brave Search for higher quality training data and better AI" (Dec 15, 2023)
- "What is a search engine API?" (Sep 22, 2023)
- "How does the Brave Search API compare to other Web search API options?" (Sep 22, 2023)
- "Brave Search API vs the Bing API" (Sep 22, 2023)

## Web Search API docs — https://api-dashboard.search.brave.com/app/documentation/web-search/get-started

The Web Search endpoint retrieves relevant results from billions of indexed web pages with regularly updated fresh results.

### Key Capabilities
- **Freshness filtering**: `pd` (24h), `pw` (7 days), `pm` (31 days), `py` (1 year)
- **Geographic targeting**: country codes and language preferences
- **Extra snippets**: up to 5 additional excerpts per result (Pro plans)
- **Safe search controls**: `off`, `moderate`, or `strict`
- **Search operators**: exact phrases, exclusions, site-specific, file types

### Pagination
Uses `count` (max 20) and `offset` parameters. Check `more_results_available` before requesting additional pages.

### Local enrichments
Two-step process: query Web Search for location-based results, then use returned location IDs with `/local/pois` and `/local/descriptions` endpoints (max 20 IDs per request).

### Rich data enrichments
Real-time verticals: weather, sports scores, stocks, currency conversion, cryptocurrency, calculations. Request with `enable_rich_callback=1`, then fetch with returned `callback_key`.

### AI applications note
This endpoint is designed for human consumption. For AI agent applications, Brave recommends using the LLM Context endpoint instead.

## Tools & integrations — https://brave.com/search/api/tools/

24 tools and platforms with Brave Search API integration:

**Development Frameworks:** LangChain, CrewAI, LlamaIndex, Dify

**Code Editors & IDEs:** Cline (VS Code), Cursor, Windsurf, Zed, Avante.nvim (Neovim)

**Low-Code/No-Code:** Flowise, Microsoft Power Platform, Postman

**Chat & Productivity:** BoltAI (Mac), MindMac (macOS)

**Infrastructure & Deployment:** Blaxel, Docker Hub, AWS Marketplace

**Discovery & Documentation:** MCP.so, PulseMCP, Kiro

**Additional:** DeerFlow (open-source research assistant), Quivr (open-source RAG framework)
