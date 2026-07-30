# serper.dev

## Fetch log
- Inbox URL: https://serper.dev/
- Final URL: https://serper.dev/
- Fetched: 2026-07-30
- Pages: 1
- Mode: standard

## Landing page — https://serper.dev/

**Title:** Serper - The World's Fastest and Cheapest Google Search API
**Meta description:** "Industry-leading SERP API, delivering lightning-fast Google search results in 1-2 seconds, at an unbeatable price starting at $0.30 per 1,000 queries."

**Core pitch:** Serper positions itself as "The World's Fastest & Cheapest Google Search API," delivering results in 1-2 seconds without requiring credit-card signup. New users get 2,500 complimentary queries. The platform claims over 850,000 companies and developers as active users, with rates cited as "up to 10 times cheaper than competitors such as SerpAPI and Bright Data."

**Supported search types:** standard web search, image search, news aggregation, maps and places/location data, video results, shopping product feeds, Google Scholar (academic papers), patent databases, and autocomplete suggestions.

**API response examples shown on the page:** JSON-formatted responses for each search type — organic results with titles, URLs, and snippets; academic results with publication dates and citation counts; shopping results with pricing, delivery information, and retailer details; patent results with inventors, assignees, filing dates, and technical figures. The demo shows 10 organic results per search type, thumbnails, ratings where applicable, and full source URLs. Multilingual support is demonstrated via language-selection toggles (e.g. "en" / "🇺🇸" for US region).

**Pricing (pay-as-you-go credits, no subscription):**
- Starter: $50 for 50,000 credits
- Standard: $375 for 500,000 credits
- Scale: $1,250 for 2.5 million credits
- Ultimate: $3,750 for 12.5 million credits

**Integrations mentioned:** LangChain, CrewAI, Jan AI, Haystack.

**Other site sections/nav:** Playground (interactive API tester, requires account login), Pricing, Sign up, Dashboard (account management, login-gated). Documentation is referenced as living on Medium rather than a dedicated docs subdomain/path. Status page and a Twitter/X presence are also referenced.

## Notes on discovery

- `llms.txt` at `https://serper.dev/llms.txt` returns a 404 (Next.js not-found page) — treated as absent.
- No `/docs`, `/documentation`, or `docs.serper.dev` found (404 / DNS failure respectively); `sitemap.xml` also 404s.
- `/playground` requires authentication (login form) — no public API reference content is reachable there without an account.
- No `github.com/<org>/<repo>` link found anywhere in the landing-page markup — Serper is a closed-source hosted API; no companion GitHub repo.
