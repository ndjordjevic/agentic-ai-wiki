---
type: source
source_url: https://deepwiki.com/
tags:
  - repo-documentation
  - codebase-wiki
  - mcp-server
  - ask-devin
  - devin
  - github-indexing
  - context-grounded-qa
related:
  - cognition.ai
  - langchain-ai-openwiki
  - 6eanut-llm-wiki
  - microsoft-playwright-mcp
  - mcp.sentry.dev
product: deepwiki
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

DeepWiki is Cognition's free public service that auto-generates interactive, source-linked documentation wikis for GitHub repositories — architecture diagrams, navigable topic pages, and grounded Q&A — powered by the same indexing stack behind [[cognition.ai|Devin]]. At `deepwiki.com` anyone can browse wikis for popular open-source repos or submit a public repo URL for indexing; agents can reach the same corpus programmatically via the no-auth **DeepWiki MCP** server at `https://mcp.deepwiki.com/mcp`. It matters for this wiki as a hosted, always-fresh alternative to local agent-wiki generators like [[6eanut-llm-wiki]] and [[langchain-ai-openwiki]].

_All claims below are sourced from ../../raw/web/deepwiki.com.md unless otherwise noted._

## What it does

DeepWiki turns unfamiliar GitHub repositories into browsable, conversational documentation. For each indexed repo (e.g. `deepwiki.com/langchain-ai/langchain`), Devin's indexer produces a structured wiki with purpose/scope summaries, architecture overviews, package or module breakdowns, ecosystem integration notes, and inline links back to relevant source files. The landing page invites users to pick from hundreds of pre-indexed popular repos or use **Add repo** to queue a new public GitHub URL. **Ask Devin** on the public site provides context-grounded Q&A over the generated wiki; the full Devin app adds advanced code search, planning, and session creation on top of the same index.

## Key features

- **Auto-generated repo wikis** — architecture diagrams, sectioned documentation, and source links produced automatically when a repo is indexed (onboarding for Devin customers; on-demand for public repos at deepwiki.com).
- **Public catalog** — free access to wikis for major OSS projects (React, LangChain, Playwright, Ollama, AutoGPT, etc.) without login.
- **Ask Devin (public)** — natural-language questions answered with citations grounded in the indexed codebase and wiki content.
- **DeepWiki MCP** — free remote MCP at `https://mcp.deepwiki.com/mcp` with three tools: `read_wiki_structure`, `read_wiki_contents`, and `ask_question`; no authentication for public repos.
- **`.devin/wiki.json` steering** — repo maintainers can supply `repo_notes` and explicit `pages` arrays to override default cluster-based wiki planning for large monorepos (up to 30 pages, 80 for enterprise).
- **Refresh cadence** — indexed wikis show last-indexed dates and enforce a cooldown before manual refresh (e.g. "wait 2 days to refresh again" on active repos).
- **Open-source support** — Cognition offers $500 Devin credits to OSS maintainers via the Devin Open Source Initiative; README badge maker promotes indexed repos.

## Architecture and concepts

DeepWiki sits on Cognition's repo-indexing pipeline shared with Devin. Indexing analyzes repository structure, clusters code into documentation topics, and emits hierarchical wiki pages with parent/child relationships. For large repos, automatic cluster planning may skip folders; `.devin/wiki.json` lets teams pin critical paths (e.g. `cui/`, `backend/`, `infra/`) and define an explicit page tree with `title`, `purpose`, and optional `parent` fields. Public DeepWiki exposes read-only wikis and basic Ask Devin; private repos and full platform features (sessions, playbooks, knowledge, scheduling) require Devin MCP (`https://mcp.devin.ai/mcp`) with an API key.

The generated wikis follow a consistent shape: overview → architecture → package/module ecosystem → integrations → build/tooling — illustrated in the captured LangChain wiki sample (Runnable interface, LangGraph/LangSmith/Deep Agents integrations, monorepo tooling table).

## Main APIs

DeepWiki's primary agent-facing surface is the **DeepWiki MCP server**:

| Tool | Purpose |
| --- | --- |
| `read_wiki_structure` | List documentation topics for a GitHub repo |
| `read_wiki_contents` | Retrieve wiki page content for a repo |
| `ask_question` | Natural-language Q&A grounded in the indexed repo |

**Wire protocol:** Streamable HTTP at `https://mcp.deepwiki.com/mcp` (recommended); legacy SSE at `/sse` is deprecated. Client config uses `url` in most MCP hosts (Cursor, Claude Code) or `serverUrl` in Devin Desktop — wrong field names silently ignore the server.

There is no public REST API for triggering indexing outside the deepwiki.com UI ("Add repo") and Devin onboarding flows.

## When to use

DeepWiki fits when a coding agent or human needs fast orientation on an unfamiliar **public** GitHub repo without cloning and reading it end-to-end — onboarding, dependency audit, architecture review, or pre-task planning. Wire the DeepWiki MCP into Cursor, Claude Code, or other MCP clients when agents should pull repo-specific context on demand rather than relying on stale training data. For **private** repos, persistent agent sessions, or platform management (playbooks, schedules), use Devin MCP instead. For maintaining documentation inside your own repo as files agents read locally, prefer [[langchain-ai-openwiki]] or [[6eanut-llm-wiki]].

## Ecosystem

DeepWiki is a Cognition product alongside [[cognition.ai|Devin]] (autonomous software engineer), Ask Devin, and Devin Desktop. It complements MCP servers already in this wiki — [[microsoft-playwright-mcp]], [[mcp.sentry.dev]] — as another remote context provider, but scoped to pre-indexed GitHub wikis rather than live browser or error-tracking APIs. OpenAI documents DeepWiki MCP integration examples; Cognition cross-links Devin docs at `docs.devin.ai/work-with-devin/deepwiki` and `deepwiki-mcp`.
