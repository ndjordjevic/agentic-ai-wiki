# qa.tech

## Fetch log
- Inbox URL: https://qa.tech/
- Final URL: https://qa.tech/
- Fetched: 2026-05-25
- Pages: 6
- Mode: standard

## Landing page — https://qa.tech/

Trusted by high-performing engineering teams at: [various SaaS companies]

## Built for teams that ship fast and stay safe.

QA.tech is an AI testing solution that gives you continuous validation across your SDLC. From PR checks to production runs, our agents monitor every commit. Accelerate your release cycle without compromising your standards.

**Agentic QA Loop:** Code → PR (Dynamic testing, Exploratory tests across whole app) → Merge (Test on deploy) → Ship (Scheduled runs)

Testing types supported: E2E UI testing, PR testing, Dynamic testing, Mobile native testing, Cross-device testing, Regression testing, API testing, Email testing, SMS testing

### The validation layer that gives your team time back

**Ship features, not test suites.** Engineers focus on building. Agents handle the validation.

**Trust feedback, don't chase flakes.** Get certain results on every PR instead of debugging unstable automation.

**Make deploys boring.** Replace high-stress release scrambles with a predictable validation layer.

**No maintenance tax** — Your suite survives refactors, redesigns, and framework migrations. Engineers stop babysitting brittle scripts and get back to shipping features.

**Dynamic, visual testing** — Agents see your UI the way a user does – no selectors, no scripts. They work toward goals, not steps, so tests adapt as your product evolves.

**Validation built into your workflow** — From PR to production, agents run continuously – catching regressions before merge, validating deploys, exploring edge cases on a schedule.

> "We have replaced over 320h of manual testing every month with QA.tech." — Fredrik Seidl, CTO at Upsales

### Validate with context that compounds with every release

**Build tests in plain English** — Describe flows, edge cases, and domain rules in chat. Every briefing adds to what agents know and sticks across every run that follows.

**Context-aware PR reviews** — Connect GitHub and agents pick up every PR with its Vercel preview. QA.tech automatically runs dynamic tests and gives you fast feedback with failure breakdowns, screenshots, and explanation.

**Detailed debugging insights** — Screenshots, logs, and network activity for every step – plus the agent's reasoning at the point of failure. No guessing what broke. Time to root cause drops from hours to minutes.

### Quality that pays for itself

Projected ROI: 529% | Payback period: 3 months | Total saved: $4M+

QA spend comparison (36 months): Manual QA → Scripted SDET → QA.tech (lowest cost)

## Docs — https://docs.qa.tech/

QA.tech uses specialized AI agents to test your application like humans would, but faster and more thoroughly. The system automatically routes testing tasks to the right agent based on context — no manual configuration needed.

### AI Agent System

| Entry Point | Purpose | How It Activates |
|---|---|---|
| Chat Assistant | Interactive testing, test creation, site analysis | You start a conversation |
| PR Review | Autonomous testing of every pull request | Automatic on PR open/update |
| On-Demand PR Testing | Deep testing with custom instructions | `@qatech` mention in PR comments |

### Test Execution Model

QA.tech uses Claude Haiku 4.5 as the default AI model for test execution (fastest). Claude Sonnet 4.5 is available for complex scenarios requiring deeper reasoning. The AI model handles all test execution decisions: navigating your application, filling forms, clicking buttons, and verifying outcomes. You write test goals in natural language, and the model figures out how to achieve them.

### How PR Reviews Work (Autonomous Flow)

```
PR opened/updated
  ↓
1. Classify Changes → User-facing? Continue. Docs/infra only? Skip.
  ↓
2. Assess Coverage → Find relevant tests, identify gaps
  ↓
3. Create Tests (if needed) → Generate tests for untested functionality
  ↓
4. Run Tests → Execute against PR preview environment
  ↓
5. Post Review → ✅ Approve / ❌ Decline / ℹ️ Informational
```

AI uses semantic matching for test selection (not keyword matching). Gap-only test generation: creates 1–3 tests only when coverage gaps exist; most PRs create zero new tests. Auto-generated tests become permanent regression tests.

## AI Chat Assistant — https://docs.qa.tech/core-concepts/ai-chat-assistant

The AI Chat Assistant is built directly into the QA.tech platform. It uses 20+ specialized tools and natural language to help manage tests, analyze your application, and provide QA guidance.

**Quick Start Examples:**
- "Generate 5 tests for the checkout flow" → shows suggestions to review, edit, and add
- "Run the login test" → starts in background, notifies when complete
- "Add a logout step to the checkout test" → shows visual diff for approval, then validates
- "Crawl admin panel from the Login test" → crawls behind auth using login test's session

**Core Workflows:** Creating Tests, Running Tests, Editing Tests (with visual diff), Analyzing Application, Issue Tracking (Jira/Linear integration)

The assistant accesses detailed step-by-step results only for runs it triggered in the current conversation. For runs from dashboard/API/scheduled plans, use the Test Results dashboard.

## GitHub App for PR Reviews — https://docs.qa.tech/configuration/github-app

Autonomous AI-powered test coverage and reviews on every pull request. Posts native GitHub reviews with verdict (approve/request changes/comment), summary, test results table, and evaluation details. Adds commit status CI check indicator.

**What it does:**
- Intelligent Test Selection via AI semantic matching (typically 5–15 tests selected)
- Gap-Only Test Generation (1–3 new tests only when needed; most PRs create zero)
- Persistent Test Suite: auto-generated tests become permanent regression tests
- Preview Environment Testing against Vercel/other preview deployments
- Approval/Rejection with full results breakdown

Does not provide code quality opinions or implementation suggestions.

## MCP Server — https://docs.qa.tech/integrations/mcp

The QA.tech MCP server exposes test cases, runs, and applications to any MCP-compatible AI client (Claude Code, Cursor, Codex, Claude Desktop, Continue). Endpoint: `https://api.qa.tech/v1/mcp`.

**Five exposed tools:**
- `list_applications` (read) — lists applications under test
- `list_test_cases` (read) — lists test cases with filters
- `get_run` (read) — fetches a run by short ID
- `start_run` (write) — starts a new test run
- `rerun_run` (write) — reruns a specific run with optional filters

Install via: `claude mcp add --transport http qatech 'https://api.qa.tech/v1/mcp' --header 'Authorization: Bearer <API_KEY>'`

## CLI Overview — https://docs.qa.tech/cli/overview.md

The `@qadottech/cli` npm package provides a terminal interface for running tests, inspecting results, exposing local servers, and chatting with the QA agent.

**Key commands:** `qatech run`, `qatech status`, `qatech chat`, `qatech tunnel` (expose local ports), `qatech applications`, `qatech test-cases`, `qatech init` (generate Claude Code subagent and skill files), `qatech configure`

Install: `npm install -g @qadottech/cli`
