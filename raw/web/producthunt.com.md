# producthunt.com

## Fetch log
- Inbox URL: https://www.producthunt.com/
- Final URL: https://www.producthunt.com/
- Fetched: 2026-07-01
- Pages: 7
- Mode: standard
- Note: Direct WebFetch blocked by Cloudflare (403); captures via Jina Reader fallback (r.jina.ai). llms.txt unavailable (Cloudflare challenge on curl).

## Landing page — https://www.producthunt.com/
Title: Product Hunt – The best new products in tech.

Primary navigation (header):
- Best Products → https://www.producthunt.com/categories
- Launches → leaderboard, launch archive, Launch Guide (https://www.producthunt.com/launch)
- News → Newsletter, Stories, Changelog
- Forums → Forums, Kitty Points Leaderboard, Streaks, Events (https://lu.ma/producthunt)
- Advertise → https://www.producthunt.com/sponsor

## Top Products Launching Today
Featured daily leaderboard products (examples from capture):
- Akiflow — Manage tasks and calendars from Claude, ChatGPT or Cursor
- Supafax — Email-native assistant that learns how you work
- Dayflow — Open source tools that help you get promoted
- Pluno — Browser agent that's 10x faster than Claude
- AgentPeek, Framer AI Agents, Tinkerfont, Brain2Qwerty v2, Load Nova, Justwrite, Oakamo, Clade, Bilt.me - Figma, DropK, iVox, Midway Chat

Sections also include Yesterday's Top Products, Last Week's Top Products, Last Month's Top Products.

Newsletter CTA: "Get the best of Product Hunt, directly in your inbox." → https://www.producthunt.com/newsletters

Footer categories (sample):
- Engineering & Development: Vibe Coding Tools, AI Coding Agents, AI Code Editors
- LLMs: AI Chatbots, AI Infrastructure Tools, Prompt Engineering Tools
- Productivity: AI notetakers, Note and writing apps, Team collaboration software, Search, AI Workflow Automation
- Marketing & Sales: Lead generation software, Marketing automation platforms
- Design & Creative: Video editing, Design resources, Graphic design tools, AI Generative Media
- Social & Community: Social Networking, Professional networking platforms, Community management
- Finance: Accounting software, Fundraising resources, Investing
- AI Agents: AI Voice Agents

Footer links: Newsletter, Apps, About, FAQ (https://help.producthunt.com/), Terms, Privacy, Advertise, llms.txt (https://www.producthunt.com/llms.txt), Contact: hello@producthunt.com

## About page — https://www.producthunt.com/about
# About Product Hunt

## Discover the best new products — ranked daily by the Product Hunt community.

Product Hunt highlights the best new products every day with a community-driven leaderboard. Browse by category or topic to compare apps, tools, and startups across AI, design, developer tools, and more. Read real reviews, explore alternatives, and see what has traction.

Links: About us, Brand guidelines, We're hiring (https://product-hunt.breezy.hr/), FAQ (https://help.producthunt.com/)

Press: "Product Hunt has become a must-read site in Silicon Valley." — The Verge

Team (leadership sample):
- Rajiv Ayyangar — CEO
- Mike Kerzhner — CTO
- Gabe Perez — Community
- Aine O'Leary — Community
- Aaron O'Leary — Content
- Julia Weinberg — Partnerships and Operations
- Alex Gap — Engineering
- Jake Crump — GM of Core Product
- Cory Lane — Head of Ad Sales
- Juan Secchi — Community
- Josh Buckley — President
- Ryan Hoover — Founder

## Docs — https://help.producthunt.com/
Title: Home | Product Hunt Help Center

Advice and answers from the Product Hunt Team. Contact: hello@producthunt.com

Collections:
- Posting — 33 articles
- Browsing — 6 articles
- Support — 10 articles
- Product Hunt — 17 articles
- Product Pages — 5 articles
- Mobile — 6 articles
- Advertising — 2 articles

## Product Hunt API Documentation — https://api.producthunt.com/v2/docs
# Welcome to the Product Hunt API 2.0

The goal of this API is to provide access to Product Hunt data via a simple GraphQL interface.

### Privileges (OAuth scopes)
- **Public:** Access public information on Product Hunt.
- **Private:** Access Product Hunt on behalf of the authenticated user (e.g. read goals).
- **Write:** Take actions on behalf of the user (e.g. mark goals complete/incomplete). Partial write access granted case-by-case; contact hello@producthunt.com.

Default apps are read-only (`public` scope).

### Accessing Endpoints
- API endpoint: **https://api.producthunt.com/v2/api/graphql**
- Requires `access_token` in Authorization header: `Authorization: Bearer {token}`
- Rate limiting applied; faster access available on request.

### Authentication paths
- OAuth user flow: authorize → token → test
- OAuth client-only flow for public endpoints without user context
- Developer token (non-expiring, account-linked) available in API dashboard: https://www.producthunt.com/v2/oauth/applications

### Commercial use
Product Hunt API must not be used for commercial purposes without contacting hello@producthunt.com.

### Attribution
Include attribution linking back to Product Hunt; logo assets at https://s3.amazonaws.com/producthunt/ph_brand_assets.zip

### Related resources
- GraphQL Reference: https://api-v2-docs.producthunt.com/
- API Explorer: https://ph-graph-api-explorer.herokuapp.com/
- Issues/feedback: https://github.com/producthunt/producthunt-api/issues
- Third-party integrations wiki: https://github.com/producthunt/producthunt-api/wiki/Product-Hunt-APIs
- Code examples wiki: https://github.com/producthunt/producthunt-api/wiki/Code-Examples

## GraphQL Reference — https://api-v2-docs.producthunt.com/
GraphQL documentation generated by graphql-docs.

Operations:
- Query, Mutation

Queries: collection, collections, comment, post, posts, topic, topics, user, viewer

Mutations: userFollow, userFollowUndo

Objects include: Post, Comment, Topic, User, Viewer, Vote, Collection, PageInfo, and GraphQL introspection types.

## posts query — https://api-v2-docs.producthunt.com/query/posts/
Look up Posts by various parameters.

Arguments:
- after, before (String) — cursor pagination
- featured (Boolean) — featured or not featured
- first, last (Int) — pagination limits
- order (PostsOrder) — sort order
- postedAfter, postedBefore (DateTime) — date filters; postedAfter defaults to 1 month ago for performance
- topic (String) — filter by topic slug
- twitterUrl (String) — filter by twitter URL
- url (String) — filter by product URL

Return fields: edges, nodes, pageInfo, totalCount

## Launch Guide — https://www.producthunt.com/launch
# Product Hunt Launch Guide

## Interested in sharing something you made? DO IT!
Complete guide for launching on Product Hunt.

### How to launch (sections)
- Getting started — https://www.producthunt.com/launch/how-product-hunt-works
- Launching a product — https://www.producthunt.com/launch/launch-day-duties
- Growing a community — https://www.producthunt.com/launch/days-after-launch
- Definitions — https://www.producthunt.com/launch/definitions

### Case studies
- Notion — community building on Product Hunt
- Framer — product-market fit via Product Hunt
- Loom — 12 launches over time

### Common questions (selected)
- **Is Product Hunt free?** Yes, 100% free.
- **How does Product Hunt work?** Makers share products via hunting (submission); community upvotes, comments, shares; daily homepage leaderboard including Product of the Day.
- **What is Product Hunt?** Global community of makers, technophiles, product people, entrepreneurs, investors, creators, early adopters.
- **Best day to launch?** The day you're most prepared.
- **Company accounts?** Prohibited — personal accounts only.
- **When to launch?** 12:01 am Pacific Time recommended for prepared makers.
- **Do you need a hunter?** No — makers encouraged to hunt their own products.
- **How to launch?** Log in → Submit → New Product → enter URL → complete submission flow.
- **Promotion rules:** Cannot ask for upvotes directly; ask people to visit and comment instead.

### Maker resources
- Maker learning series (videos): https://www.youtube.com/playlist?list=PLPbokyho5ngEd2HYPkt0RqdnIkhfEIu9Y
- Community guidelines: https://help.producthunt.com/en/articles/3615694-community-guidelines
