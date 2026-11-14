# firecrawl/skills

## Metadata
- Stars: 156
- Primary language: n/a (skills catalog)
- Default branch: main
- Latest release: none
- License: ISC
- Homepage: 
- Fetched: 2026-11-14
- Final URL: https://github.com/firecrawl/skills

## Description
Firecrawl agent skills for Claude Code, Codex and Cursor: web search, scraping, crawling and browser interaction. Firecrawl is the most complete web data API for AI agents.

## README
# Firecrawl Skills

The full catalog of Firecrawl skills for AI coding agents, following the [Agent Skills](https://agentskills.io) format. Available as a plugin for Claude Code, Cursor, and OpenAI Codex.

> **This repository is a distribution catalog.** Every directory under `skills/` is a CI-synced mirror. Install skills from here; contribute skill changes at the source repository. Repository-level metadata is maintained here.

## Install

```bash
npx skills add firecrawl/skills
```

Without `-y` this opens an interactive picker over the whole catalog. Install a specific skill by name (names are path-independent):

```bash
npx skills add firecrawl/skills --skill firecrawl-build
```

For CLI onboarding (installs the Firecrawl CLI plus the core skills, with optional workflow skills):

```bash
npx -y firecrawl-cli@latest init
```

## Catalog layout

| Category | Path | What it's for | Source of truth |
|---|---|---|---|
| Core | [`skills/core/`](./skills/core) | The Firecrawl primitives for live web work during an agent session (search, scrape, crawl, interact — via the CLI or MCP), plus the research paper index and developer index skills | [`firecrawl/cli`](https://github.com/firecrawl/cli/tree/main/skills) |
| Build | [`skills/build/`](./skills/build) | Integrating Firecrawl APIs into product code: SDKs, REST, endpoint selection, API keys | [`firecrawl/firecrawl`](https://github.com/firecrawl/firecrawl/tree/main/skills) (`skills/`) |
| Workflows | [`skills/workflows/`](./skills/workflows) | End-to-end session recipes: lead gen, deep research, SEO audit, knowledge bases, and more | [`firecrawl/firecrawl-workflows`](https://github.com/firecrawl/firecrawl-workflows) |

## Contributing: where does my PR go?

- **Core skills, including the research and developer index skills** → PR [`firecrawl/cli`](https://github.com/firecrawl/cli).
- **Build/SDK skills** → PR [`firecrawl/firecrawl`](https://github.com/firecrawl/firecrawl) (`skills/`).
- **Workflow skills** → PR [`firecrawl/firecrawl-workflows`](https://github.com/firecrawl/firecrawl-workflows).

Do not submit changes to files under `skills/` in this catalog. CI replaces those directories during the next source sync. Repository-level metadata is maintained here.

## Skills

### Core (`skills/core/`)

Skills that teach agents the [Firecrawl CLI](https://github.com/firecrawl/cli) for live web work — `firecrawl`, `firecrawl-scrape`, `firecrawl-search`, `firecrawl-crawl`, `firecrawl-map`, `firecrawl-interact`, `firecrawl-agent`, `firecrawl-monitor`, `firecrawl-parse`, `firecrawl-download` — plus the index skills backing the `firecrawl research` and `firecrawl developer` commands:

| Skill                                                                  | Description                                                                                                                      |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [`firecrawl-research-index`](./skills/core/firecrawl-research-index)   | Find papers in the research paper index — biomedical and life-science literature (PubMed, bioRxiv, medRxiv) plus arXiv preprints |
| [`firecrawl-developer-index`](./skills/core/firecrawl-developer-index) | Answer developer questions from issues, pull requests, READMEs, and documentation pages                                          |

### Build (`skills/build/`)

| Skill                                                                     | Description                                                             |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`firecrawl-build`](./skills/build/firecrawl-build)                       | Firecrawl application API umbrella skill                                |
| [`firecrawl-build-onboarding`](./skills/build/firecrawl-build-onboarding) | Get `FIRECRAWL_API_KEY` into a project and choose the right SDK/docs    |
| [`firecrawl-build-scrape`](./skills/build/firecrawl-build-scrape)         | Integrate `/scrape` for single-page extraction                          |
| [`firecrawl-build-search`](./skills/build/firecrawl-build-search)         | Integrate `/search` for discovery-first workflows                       |
| [`firecrawl-build-interact`](./skills/build/firecrawl-build-interact)     | Integrate `/interact` for clicks, forms, and dynamic flows after scrape |

### Workflows (`skills/workflows/`)

End-to-end recipes such as [`firecrawl-lead-gen`](./skills/workflows/firecrawl-lead-gen), [`firecrawl-deep-research`](./skills/workflows/firecrawl-deep-research), [`firecrawl-seo-audit`](./skills/workflows/firecrawl-seo-audit), [`firecrawl-competitive-intel`](./skills/workflows/firecrawl-competitive-intel), and more — see [`skills/workflows/`](./skills/workflows) for the full set, and [`firecrawl-workflows`](./skills/workflows/firecrawl-workflows) for the umbrella skill and authoring guide.

## MCP Server

The plugin includes Firecrawl MCP configuration for the official [Firecrawl MCP server](https://github.com/firecrawl/firecrawl-mcp-server), so editors that support bundled MCP metadata can wire Firecrawl tools with `FIRECRAWL_API_KEY`.

## Plugins

This repo serves as a plugin for multiple platforms, bundling the core and build skills (workflows are session recipes, not editor-integration material):

- **Claude Code** - `.claude-plugin/`
- **Cursor** - `.cursor-plugin/`
- **OpenAI Codex** - `.codex-plugin/`

## Prerequisites

- A Firecrawl account or self-hosted Firecrawl deployment
- API key stored in `FIRECRAWL_API_KEY` for cloud usage

Get your API key at [firecrawl.dev/app](https://www.firecrawl.dev/app). If you do not have one yet, [`firecrawl-build-onboarding`](./skills/build/firecrawl-build-onboarding) includes the browser authorization flow.

## Which skills do I need?

- **"Search/scrape the web for me right now, during this session"** → core skills (`skills/core/`)
- **"Query published research papers or developer docs indexes"** → index skills (`skills/core/`)
- **"Add Firecrawl to this codebase"** → build skills (`skills/build/`)
- **"Run an end-to-end task like lead gen or deep research"** → workflow skills (`skills/workflows/`)

Both usage paths follow Firecrawl's onboarding skill (same install, different use cases): [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md).

## Docs (Source of Truth)

Read the source-of-truth page for your project language:

- **Node / TypeScript**: [docs.firecrawl.dev/agent-source-of-truth/node](https://docs.firecrawl.dev/agent-source-of-truth/node)
- **Python**: [docs.firecrawl.dev/agent-source-of-truth/python](https://docs.firecrawl.dev/agent-source-of-truth/python)
- **Rust**: [docs.firecrawl.dev/agent-source-of-truth/rust](https://docs.firecrawl.dev/agent-source-of-truth/rust)
- **Java**: [docs.firecrawl.dev/agent-source-of-truth/java](https://docs.firecrawl.dev/agent-source-of-truth/java)
- **Elixir**: [docs.firecrawl.dev/agent-source-of-truth/elixir](https://docs.firecrawl.dev/agent-source-of-truth/elixir)
- **cURL / REST**: [docs.firecrawl.dev/agent-source-of-truth/curl](https://docs.firecrawl.dev/agent-source-of-truth/curl)

## License

ISC


## Docs

### skills/core/firecrawl-alexandria/SKILL.md
---
name: firecrawl-alexandria
description: Find a direct path to structured data through ready-made workflows, data APIs, and indexes. Follow the search skill to discover and inspect tools, then the scrape skill to execute them.
---

# A direct path to structured data

Alexandria brings ready-made website workflows, API providers, and specialized indexes into Firecrawl search and scrape. Semantic discovery finds capabilities by the data you need; domain matching connects web results to tools that may retrieve richer structured data beyond the page. Discover a tool that fits the task and get structured results directly, reducing the browsing, parsing, and repeated requests needed to assemble the data yourself.

- [Search](../firecrawl-search/SKILL.md) to find web results and relevant tools, then inspect only the contracts needed for the task.
- [Scrape](../firecrawl-scrape/SKILL.md) to execute a selected tool or read a URL. For large retained results, use its remote Bash guidance to select the data you need.

Use ordinary web results when they answer the question; use a provider tool when its coverage and inputs fit.

## Alexandria feedback (refunds 1 credit)

Alexandria coverage grows from what agents report. Send one `firecrawl alexandria feedback` per website you needed data from, right after your last Alexandria call for it. No job ID is needed. Each feedback refunds 1 credit, up to 10 credits per website and 100 per team each UTC day.

Feedback can describe any of these outcomes:

- A tool answered the need, fully or partly.
- A tool ran but returned wrong or incomplete data, or failed.
- No provider covers the website, or a provider exists but lacks the capability you needed, and you fell back to web search, scrape, or Agent.

**Opt out:** if `FIRECRAWL_NO_ENDPOINT_FEEDBACK=1` (or `FIRECRAWL_DISABLE_ENDPOINT_FEEDBACK=1`) is set, the CLI silently skips the call and never sends anything. Respect that; do not try to work around it. (Team admins can also disable this server-side; the API returns `feedbackErrorCode: "TEAM_OPTED_OUT"` and the CLI exits 0 silently.)

**Rules to know before you call this:**

- **Time window:** must be sent within 20 minutes of your team's most recent Alexandria search, discovery, or execution. Each Alexandria call restarts the window. Late feedback is rejected (`feedbackErrorCode: "FEEDBACK_WINDOW_EXPIRED"`).
- **`--url` is the website the user needed data from**, not the provider and not a Firecrawl page. `--requested-functionality` is what they needed from it, in one sentence. These two fields are the most important: they aggregate across teams and tell us which sites and workflows to add next.
- **`--objective` is the underlying goal** behind the session: what you or your user were ultimately trying to accomplish, in one sentence (for example, "Shortlist federal IT contracts to bid on this quarter"). It is broader than `--requested-functionality`, which covers only this website.
- **`--rationale` explains the rating** from observed results: which provider or capability served or failed the need, and how. Two or three sentences, no raw results pasted in.
- **`--provider-feedback`** is a JSON array of `{name, issue, why}` for providers that were missing, thin, or unavailable. Issues: `missing_provider` (no provider covers the site), `insufficient_coverage` (exists, but data was thin, stale, or partial for this market or segment), `provider_unavailable` (could not be called), `other`.
- **`--capability-feedback`** is a JSON array of `{name, provider, issue, why, requestedFunctionality?}` for capabilities that were missing, wrong, or failed. Issues: `new_capability_request` (ask the provider to add one; `requestedFunctionality` required), `missing_capability` (provider exists but lacks it), `insufficient_functionality` (exists but cannot take the input or filter you needed), `incorrect_result`, `execution_error`, `other`. Use `name` and `provider` exactly as discovery returned them; for a capability that does not exist yet, name what it should be.
- **Rate honestly:** `good` when a tool answered the need, `partial` when it answered some of it or with gaps, `bad` when nothing available answered it or what ran was wrong or failed. Every rating gets the same refund.
- **Website refund cap (per website, per UTC day, default 10 credits).** Past it, feedback about that website is still recorded but refunds nothing, and the response sets `websiteCapReached: true`. Feedback about other websites still refunds.
- **Daily refund cap (per team, per UTC day, default 100 credits).** Past the cap, feedback is still recorded but refunds nothing. The response includes `creditsRefundedToday`, `dailyRefundCap`, and `dailyCapReached`. **When `dailyCapReached: true`, stop sending Alexandria feedback for the rest of the UTC day.**
- **`--silent &`** is the right pattern: exit code 0 even on failure, so a rejected call never crashes your pipeline.

```bash
# Example: send once per website, within 20 minutes of your last Alexandria call. Replace the
# placeholders with what actually happened; drop --provider-feedback or
# --capability-feedback when there is nothing to report at that level.
firecrawl alexandria feedback \
  --rating "<good|partial|bad>" \
  --url "https://sam.gov" \
  --requested-functionality "Active contracts by agency with their attachments" \
  --objective "Shortlist federal IT contracts to bid on this quarter" \
  --rationale "sam-gov/contracts returned the contract list, but no capability exposes attachment links, so those were scraped from the web instead." \
  --capability-feedback '[{"name":"attachments","provider":"sam-gov","issue":"new_capability_request","why":"Attachments were the point of the task","requestedFunctionality":"Given a contract ID, return attachment URLs and document text"}]' \
  --silent &
```

If you report a site with no provider coverage, use `--provider-feedback '[{"name":"<site or provider>","issue":"missing_provider","why":"<what was needed>"}]'` and rate `bad`; that is the signal we use to onboard new providers.

`--silent` suppresses output and `&` runs it in the background so feedback never blocks you. Run `firecrawl alexandria feedback --help` for every option.


## Top-level structure
- .claude-plugin
- .codex-plugin
- .cursor-plugin
- .gitattributes
- .github
- .gitignore
- .mcp.json
- AGENTS.md
- CLAUDE.md
- LICENSE
- README.md
- mcp.json
- skills

### skills/core/
- README.md
- firecrawl-agent
- firecrawl-alexandria
- firecrawl-crawl
- firecrawl-developer-index
- firecrawl-download
- firecrawl-interact
- firecrawl-map
- firecrawl-monitor
- firecrawl-parse
- firecrawl-research-index
- firecrawl-scrape
- firecrawl-search
- firecrawl
