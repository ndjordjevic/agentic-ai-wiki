---
type: source
category: "MCP servers & integrations"
source_url: https://www.producthunt.com/
companion_urls:
  - https://github.com/producthunt/producthunt-api
raw_files:
  - ../../raw/web/producthunt.com.md
  - ../../raw/github/producthunt-producthunt-api.md
tags:
  - product-discovery
  - launch-platform
  - maker-community
  - graphql-api
  - oauth
  - go-to-market
  - startup-distribution
  - agent-products
related:
  - lovable.dev
  - bolt.new
  - open-design.ai
  - skills.sh
  - browse.sh
  - postiz.com
  - warp.dev
  - planana.xyz
  - claudemarketplaces.com
product: producthunt
detail_level: standard
created: 2026-07-01
updated: 2026-07-07
---

Product Hunt is a community-driven discovery platform where makers submit new tech products daily and the audience upvotes, comments, and ranks them on a public leaderboard — including Product of the Day. For the agentic-AI ecosystem it matters twice: as the primary launch channel where AI coding agents, MCP servers, skills repos, and agent harnesses surface to early adopters, and as a programmatic data source via its GraphQL API v2 (companion starter kit at `producthunt/producthunt-api`). The platform pairs editorial discovery (categories spanning AI Agents, Vibe Coding Tools, and AI Coding Agents) with maker tooling (Launch Guide, forums, newsletters) and a read-mostly API for posts, topics, users, and collections.

_All claims below are sourced from ../../raw/web/producthunt.com.md unless otherwise noted._

## What it does

Product Hunt operates as a daily-ranked product leaderboard backed by a global maker community. Makers hunt (submit) products; community members upvote, comment, and share; top products compete for homepage placement and badges like Product of the Day. The site organizes discovery through category taxonomies (Engineering & Development, LLMs, Productivity, AI Agents, and more), leaderboards (today, yesterday, week, month), product pages with reviews and alternatives, forums, stories, newsletters, and a structured Launch Guide for first-time submitters.

## Key features

- **Daily leaderboard** — homepage surfaces top launches with upvote-driven ranking refreshed daily.
- **Category taxonomy** — browse and compare products across AI-centric categories including AI Coding Agents, Vibe Coding Tools, AI Workflow Automation, and AI Voice Agents.
- **Launch Guide** — interactive maker resource covering how Product Hunt works, launch-day duties, post-launch community growth, definitions glossary, and case studies (Notion, Framer, Loom).
- **Forums & community** — discussion threads, kitty-points leaderboard, visit streaks, and Luma-hosted events.
- **Product pages** — per-product hubs with reviews, alternatives, and maker comments.
- **GraphQL API v2** — programmatic access to posts, topics, users, collections, and comments at `https://api.producthunt.com/v2/api/graphql` with OAuth2 (`public`, `private`, `write` scopes). (../../raw/github/producthunt-producthunt-api.md)
- **API starter kit** — official `producthunt/producthunt-api` repo provides an OAuth-integrated Node/React reference app proxying GraphQL requests. (../../raw/github/producthunt-producthunt-api.md)

## Architecture

The public site is a Cloudflare-protected web application (direct scraping blocked; API and docs endpoints are more accessible). The API layer is GraphQL-first: a single endpoint (`/v2/api/graphql`) serves queries (`posts`, `post`, `topics`, `topic`, `user`, `viewer`, `collections`, `comment`) and limited mutations (`userFollow`, `userFollowUndo`). Authentication uses OAuth2 with either user-context tokens (authorize → token flow) or client-credentials tokens for public-scope read access. Rate limits apply by default; elevated throughput requires contacting Product Hunt. The companion starter kit runs an Express server (`index.js`) that proxies React client requests to `/graphql`, encrypting user access tokens in session cookies. (../../raw/github/producthunt-producthunt-api.md)

## Installation

To run the official API starter kit locally:

```bash
git clone git@github.com:producthunt/producthunt-api.git
cd producthunt-api
yarn   # or npm install
cp .env.sample .env
# Set PH_APP_API_KEY, PH_APP_API_SECRET, PH_APP_REDIRECT_URI, PH_APP_REQUESTED_SCOPES
yarn build && yarn start
# Open https://localhost:3000
```

For scripts needing only public data, obtain a client-credentials token:

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"client_id":"YOUR_KEY","client_secret":"YOUR_SECRET","grant_type":"client_credentials"}' \
  https://api.producthunt.com/v2/oauth/token
```

Alternatively, generate a non-expiring developer token from the API dashboard at `https://www.producthunt.com/v2/oauth/applications`. (../../raw/github/producthunt-producthunt-api.md)

## Example usage

Query today's featured posts via GraphQL (requires bearer token):

```graphql
{
  posts(first: 10, order: RANKING) {
    edges {
      node {
        name
        tagline
        votesCount
        url
      }
    }
  }
}
```

POST to `https://api.producthunt.com/v2/api/graphql` with header `Authorization: Bearer {token}`. The `posts` query supports filters for `featured`, `topic`, `postedAfter`/`postedBefore`, `url`, and cursor pagination (`first`/`after`). Explore interactively via the GraphiQL explorer at `https://ph-graph-api-explorer.herokuapp.com/`.

## When to use

Use Product Hunt when launching a new agent tool, MCP server, skills directory, or AI product and you want distribution to early-adopter makers and investors. Use the API when building dashboards, launch monitors, competitive intelligence tools, or agent workflows that need structured access to Product Hunt posts, topics, and user data — bearing in mind commercial use requires explicit permission and write scopes are granted case-by-case.

## Maintenance status

The API v2 documentation and GraphQL reference are actively maintained; issues are tracked on GitHub (`producthunt/producthunt-api`, 367 stars, JavaScript, default branch `master`, last push August 2024). The starter kit README notes the React build lacks HMR and welcomes PRs. Product Hunt's core platform (leaderboards, Launch Guide, AI-heavy category taxonomy) is actively updated as of July 2026. (../../raw/github/producthunt-producthunt-api.md)

## Ecosystem

Product Hunt sits at the distribution layer of the maker stack — complementary to code hosting (GitHub), skills distribution ([[skills.sh]]), and social scheduling ([[postiz.com]]). Many products in this wiki's agentic-AI category (AI coding agents, browser agents, MCP tools) appear as daily launches. Third-party API wrappers and integrations are catalogued in the repo wiki at `github.com/producthunt/producthunt-api/wiki/Product-Hunt-APIs`. Help center articles cover posting, browsing, product pages, mobile, and advertising. Maker education videos are published on YouTube.

## Documentation

- Help Center: `https://help.producthunt.com/` (posting, browsing, support, product pages)
- API docs: `https://api.producthunt.com/v2/docs`
- GraphQL reference: `https://api-v2-docs.producthunt.com/`
- Launch Guide: `https://www.producthunt.com/launch`
