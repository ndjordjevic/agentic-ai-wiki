---
type: source
category: "Browser & web automation"
source_url: https://qa.tech/
tags:
  - ai-testing
  - e2e-testing
  - pr-review
  - browser-automation
  - ci-cd
  - mcp-server
  - github-integration
  - agentic-qa
related:
  - agent-field-pr-af
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - greptile.com
  - the-new-sdlc-with-vibe-coding
  - sentry.io
  - coderabbit.ai
product: qa
detail_level: standard
created: 2026-05-25
updated: 2026-08-25
---

QA.tech is an AI-powered end-to-end testing platform that runs autonomous agents throughout the software delivery lifecycle — from automated PR reviews against preview deployments to scheduled production monitoring. Rather than scripting selectors or maintaining brittle automation suites, teams describe test goals in plain English and agents execute, adapt, and generate tests continuously. The platform bills itself as a "validation layer" that replaces manual QA bottlenecks; one customer (Upsales, ~150 employees) reported replacing 320 hours of monthly manual testing.

_All claims below are sourced from ../../raw/web/qa.tech.md unless otherwise noted._

## What it does

QA.tech provides continuous validation across the full SDLC. Its core agentic QA loop spans: code change → PR (dynamic testing, exploratory tests) → merge (test on deploy) → ship (scheduled runs). The platform supports E2E UI testing, PR testing, dynamic testing, mobile native testing (iOS/Android), cross-device testing, regression testing, API testing, email testing, and SMS testing.

Three specialized AI agents route testing tasks automatically:

| Entry Point | Purpose | How It Activates |
|---|---|---|
| Chat Assistant | Interactive testing, test creation, site analysis | User starts a conversation |
| PR Review | Autonomous testing of every pull request | Automatic on PR open/update |
| On-Demand PR Testing | Deep testing with custom instructions | `@qatech` mention in PR comments |

## Key features

**Selector-free, goal-driven testing** — Agents navigate your UI as a user would; no CSS selectors or scripted steps. Tests describe *what* to achieve, not *how*. This means tests survive UI refactors, redesigns, and framework migrations without manual maintenance.

**Gap-only PR test generation** — On every PR, the GitHub App uses semantic matching to select relevant existing tests (typically 5–15) and only creates new tests (1–3) when genuine coverage gaps exist; most PRs generate zero new tests. Auto-generated tests become permanent regression tests.

**Context-aware PR reviews** — Posts native GitHub reviews with verdict (approve/request changes/comment), test results table, screenshots, and failure breakdowns. Also posts commit status CI checks. Does not offer code quality opinions or implementation suggestions.

**Agentic Chat Assistant** — A natural-language interface with 20+ specialized tools for creating tests, running them, editing via visual diff, crawling behind authentication, bulk editing, and integrating with Jira/Linear for issue tracking.

**Detailed debugging insights** — For every failed step: screenshots, network activity logs, console logs, and the agent's reasoning at the point of failure. Time to root cause drops from hours to minutes.

**Projected ROI** — 529% ROI, 3-month payback period, $4M+ total saved (based on 36-month model vs. manual QA and scripted SDET approaches).

## Architecture and concepts

Test execution uses **Claude Haiku 4.5** (default, fastest) or **Claude Sonnet 4.5** (complex scenarios requiring deeper reasoning). The model handles all execution decisions — navigation, form-filling, button clicks, verification — while humans write test goals in natural language.

Key organizational concepts:
- **Projects / Applications / Environments** — Hierarchy for managing test infrastructure across teams and deployment targets
- **Test Plans** — Groups of test cases executed together as a unit
- **Knowledge Graph** — A digital representation of facts and relations about your application; built via crawling sessions and accumulated via chat briefings. Compounds with every run.
- **Test Dependencies** — Control execution order, manage browser state isolation, structure multi-user scenarios
- **Configs** — Reusable data shared across tests (credentials, environment variables)
- **Issues** — Auto-detected problems: failed tests, JavaScript console errors, WCAG accessibility violations

**Agent Cache** — Speeds up test execution by reusing browser state from completed dependency tests. Session state lifetime is configurable.

## Main APIs

**REST API** (`https://api.qa.tech/v1/`) — Endpoints for starting runs, getting run status, listing/creating test cases, managing applications, uploading mobile app builds, creating remote tunnels (Cloudflare-backed, for testing behind firewalls), and triggering chat conversations.

**MCP Server** (`https://api.qa.tech/v1/mcp`) — Five tools exposed to any MCP-compatible AI client (Claude Code, Cursor, Codex, Claude Desktop, Continue):
- `list_applications` (read), `list_test_cases` (read), `get_run` (read), `start_run` (write), `rerun_run` (write)

Install in Claude Code: `claude mcp add --transport http qatech 'https://api.qa.tech/v1/mcp' --header 'Authorization: Bearer <API_KEY>'`

**CLI** (`npm install -g @qadottech/cli`) — Terminal interface for running tests, checking status, exposing local dev servers via tunnel, chatting with the agent, and generating Claude Code subagent/skill files (`qatech init`).

## When to use

QA.tech fits teams that:
- Ship frequently and need fast, certain feedback on every PR without maintaining test scripts
- Run preview deployments (Vercel, etc.) and want automated coverage on every change
- Want to eliminate manual regression testing cycles without investing in SDET infrastructure
- Need exploratory testing or edge-case discovery that scripted automation misses

AI agents are best for exploratory testing, coverage of new features, form-filling with realistic data, and testing preview environments. Traditional scripts remain better for exact-same-steps deterministic flows and complex numerical assertions. QA.tech is complementary to, not a replacement for, scripted tests where determinism matters.

## Ecosystem

**CI/CD integrations**: GitHub Actions, GitLab (MR reviews + API runs), Vercel preview protection bypass, SSH/remote tunnel for environments behind firewalls.

**Notification integrations**: Slack (AI-powered testing assistance in workspace), Microsoft Teams, status badges (SVG).

**Issue tracker integrations**: Jira, Linear, Trello — exportable from the Chat Assistant.

**Testing capabilities**: API call testing, email inbox access, SMS testing, mobile app testing (iOS/Android via app build uploads), file upload/download testing, cross-device presets, BankID (SE).

**Documentation**: https://docs.qa.tech/ — organized into core-concepts, configuration, integrations, test-features, best-practices, api-reference, and CLI sections.
