# tt-a1i/archify

## Metadata
- Stars: 85989
- Primary language: JavaScript
- Default branch: main
- Latest release: v3.2.0
- License: MIT License
- Homepage: https://archify.si
- Pushed: 2026-10-20T03:38:17Z
- Fetched: 2026-10-20
- Final URL: https://github.com/tt-a1i/archify

## Description
Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

## README
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/archify-lockup-dark.svg" />
    <img src="docs/assets/archify-lockup-light.svg" alt="Archify" width="440" height="121" />
  </picture>
</p>
<h3 align="center">Turn anything you want to understand, plan, or share into an interactive visual.</h3>

<p align="center"><img src="docs/assets/archify-readme-hero.png" alt="Archify — interactive diagrams" width="960" /></p>

<p align="center"><strong>Official channels：</strong> <a href="https://archify.si">archify.si</a> · <a href="https://github.com/tt-a1i/archify">GitHub</a><br/>Archify is free and open source. Third-party online services and paid plans are operated by their respective providers and do not represent Archify. <a href="#official-services">Service details →</a></p>

<p align="center">Start with an idea, a question, or a plan. Describe it to your AI agent, and Archify turns it into an interactive HTML you can explore, customize, and share. From travel itineraries and learning maps to complex systems—make it your own.</p>

<p align="center">See what the community is creating—and imagine what you could make next.</p>

<p align="center">
  <a href="https://archify.si/gallery.html"><strong>Live demos</strong></a> &nbsp;·&nbsp;
  <a href="#start"><strong>Get started</strong></a> &nbsp;·&nbsp;
  <a href="https://archify.si/guide.html"><strong>Scenario guide</strong></a> &nbsp;·&nbsp;
  <a href="#community"><strong>Community</strong></a> &nbsp;·&nbsp;
  <a href="./README_ZH.md"><strong>简体中文</strong></a> &nbsp;·&nbsp;
  <a href="./README_JA.md"><strong>日本語</strong></a> &nbsp;·&nbsp;
  <a href="./README_KO.md"><strong>한국어</strong></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/31352?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-31352" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/31352" alt="tt-a1i/archify | Trendshift" width="250" height="55" /></a>
</p>

<p align="center">
  <a href="https://github.com/tt-a1i/archify/stargazers"><img src="https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&amp;color=E5B650&amp;logo=github&amp;label=Stars" alt="GitHub stars" /></a>
  <a href="https://skills.sh/tt-a1i/archify/archify"><img src="https://img.shields.io/badge/installs-130K%2B-0EA5E9?style=flat-square" alt="130K+ installs on skills.sh" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22c55e?style=flat-square" alt="MIT License" /></a>
  <a href="#installation-options"><img src="https://img.shields.io/badge/works_with-Claude_Code_%7C_Codex_%7C_Cursor_%7C_OpenCode-7C3AED?style=flat-square" alt="Works with Claude Code, Codex, Cursor, and OpenCode" /></a>
  <a href="CHANGELOG.md#320--2026-10-18"><img src="https://img.shields.io/badge/version-3.2.0-0891b2?style=flat-square" alt="Stable version 3.2.0" /></a>
</p>

<p align="center">
  <a href="https://archify.si/"><img src="https://img.shields.io/badge/Website-0891B2?style=for-the-badge" alt="Archify website" /></a>
  <a href="https://discord.gg/6xWMjgCeUq"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&amp;logo=discord&amp;logoColor=white" alt="Join Archify on Discord" /></a>
  <a href="#community"><img src="https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&amp;logo=wechat&amp;logoColor=white" alt="Archify WeChat group" /></a>
  <a href="#community"><img src="https://img.shields.io/badge/QQ-1688D8?style=for-the-badge&amp;logo=qq&amp;logoColor=white" alt="Archify QQ group" /></a>
  <a href="https://x.com/t20000622yy"><img src="https://img.shields.io/badge/Creator_on_X-181717?style=for-the-badge&amp;logo=x&amp;logoColor=white" alt="Follow the creator on X" /></a>
</p>

<p align="center"><a href="#sponsors"><strong>❤️ Partners & sponsors: Kimi Work · Supercode · OpenLux</strong></a></p>

## See Archify in action

<!-- archify-launch-video -->

https://github.com/user-attachments/assets/78570807-ba1d-4737-953f-55504a378a87

**One sentence. Your repo, mapped.** Watch the 35-second demo: explore the diagram, follow source links, and trace a path. [Try the interactive examples ↗](https://archify.si/gallery.html)

<a id="start"></a>

### Install, then describe your idea

Works with Cursor, Claude Code, Codex CLI, and OpenCode. See installation options below for additional integrations.

```bash
npx skills add tt-a1i/archify -g
```

Send this to your agent:

```text
Use Archify to diagram a web request: Browser calls the API,
the API checks Redis, and a cache miss queries PostgreSQL and fills the cache.
```

Then continue: “Add authentication”, “Highlight the cache-miss path”, or “Switch to the light theme”.

**No repository is required:** start with a description, or ask your agent to read a repository for a source-backed architecture diagram.

[Choose your agent](https://archify.si/start.html?agent=cursor&type=architecture) · [Installation details and update checks](#quick-start) · [Create and check diagrams with your agent](https://archify.si/agent-diagrams)

## Ask a question, get a one-page answer

Not every answer is one diagram. Ask your agent to answer as a page and Archify builds an **explainer**: the conclusion first, then one panel per question, with tables, steps, charts, code and validated diagrams.

[![An explainer page: the answer first, then steps beside the sequence diagram they walk through](docs/assets/explainer-tls-en.png)](https://archify.si/cases/explainer/tls-first-visit.html)

- **Conclusion first.** The answer and its reasons lead; every panel takes one question.
- **Diagrams that explain.** Steps sit beside the diagram they walk through and light its parts as you read. Click any node to open the full interactive view.
- **Easy to check.** Claims cite numbered sources; repository excerpts are pinned to a commit and open in a source card.
- **Easy to share.** One HTML file with four styles and light or dark themes. Export a PNG, WebP or JPG long image, or print to PDF. Ask about any panel to get a follow-up your agent can use to revise just that panel.

```text
Use Archify to answer as one page: our API's P99 went from 80 ms to 600 ms
while the mean barely moved. What is the likely cause, and how should we investigate?
```

Live examples: [First HTTPS visit](https://archify.si/cases/explainer/tls-first-visit.html) · [P99 latency (Chinese)](https://archify.si/cases/explainer/p99-tail-latency.html) · [How Archify finalize keeps the last good file, read from this repository (Chinese)](https://archify.si/cases/explainer/finalize-delivery.html) · [First rental checklist (Chinese)](https://archify.si/cases/explainer/first-rental.html)

<a id="sponsors"></a>

## ❤️ Sponsors

<p align="center">
  <a href="https://www.kimi.ai/?aff=archify"><img src="docs/assets/sponsors/archify-kimi-work.png" alt="Archify × Kimi Work collaboration banner" width="800" /></a>
</p>

**Archify × Kimi Work.** Find Archify in the Kimi Work plugin store as **Interactive Architecture Diagram**. Describe your system in one sentence to create an interactive diagram. **[Try it in Kimi Work →](https://www.kimi.ai/?aff=archify)**

<table>
<tr>
  <td align="center" width="240"><a href="https://supercode.sh/?utm_source=archify"><img src="https://cdn.supercode.sh/sponsors/supercode-logo.png" alt="Supercode" width="200"/></a><br/><strong><a href="https://supercode.sh/?utm_source=archify">supercode.sh</a></strong></td>
<td><a href="https://supercode.sh/?utm_source=archify">Supercode</a> sponsors Archify and enhances Codex and Cursor with token optimization, curated Skills, and spec-driven development. Archify is featured as a <a href="https://supercode.sh/en/skills/tt-a1i/archify/archify">Supercode Editor’s Choice</a> skill.<br/><br/><a href="https://supercode.sh/en/skills/tt-a1i/archify/archify"><img src="https://supercode.sh/badges/editors-choice.svg" alt="Supercode Editor’s Choice — Archify" width="240" height="55"/></a></td>
</tr>
<tr>
<td align="center" width="240"><a href="https://www.openlux.ai/register?channel=c_qdvanbpc"><img src="docs/assets/sponsors/openlux-logo.png" alt="OpenLux" width="200" /></a><br/><strong><a href="https://www.openlux.ai/register?channel=c_qdvanbpc">OpenLux</a></strong></td>
<td>Thank you to OpenLux for sponsoring this project! OpenLux is an all-in-one AI platform for businesses, bringing together leading AI models from major providers worldwide. With fast, reliable service and responsive technical support, OpenLux offers base pricing for Claude, OpenAI, and Gemini models as low as 8.82%, 4%, and 8% of official rates, respectively.<br/><br/>Exclusive offer for Archify users: Sign up through our referral link and enjoy up to 7.5% off credit top-ups!<br/><br/><a href="https://www.openlux.ai/register?channel=c_qdvanbpc">Get started with OpenLux →</a></td>
</tr>
<tr>
<td align="center" width="240"><a href="https://www.packyapi.ai/register?aff=bN97"><img src="docs/assets/sponsors/packycode-logo.png" alt="PackyCode" width="200" /></a><br/><strong><a href="https://www.packyapi.ai/register?aff=bN97">PackyCode</a></strong></td>
<td>Access leading AI models through PackyCode with one API endpoint and one API key. Enjoy automatic failover and dedicated high-speed routes for Codex and Claude Code.<br/><br/>Get started with $1 in free credits, a discount on your first top-up, and savings of up to 80% on eligible routes. Pay in RMB with no currency conversion markups or extra top-up fees.<br/><br/><a href="https://www.packyapi.ai/register?aff=bN97">Get started with PackyCode →</a></td>
</tr>
<tr>
<td align="center" width="240"><a href="https://www.aicodemirror.ai/register?invitecode=WC26FL"><img src="docs/assets/sponsors/aicodemirror-logo.jpg" alt="AICodeMirror" width="200" /></a><br/><strong><a href="https://www.aicodemirror.ai/register?invitecode=WC26FL">AICodeMirror</a></strong></td>
<td>Thank you to AICodeMirror for sponsoring Archify! AICodeMirror provides API relay services for Claude, Codex, and Gemini, with enterprise-grade concurrency, invoice issuance, and 24/7 technical support. Codex pricing starts at 7% of standard rates, with additional top-up discounts.<br/><br/>Exclusive offer for Archify users: Register through our referral link to receive 20% off your first top-up.<br/><br/><a href="https://www.aicodemirror.ai/register?invitecode=WC26FL">Try AICodeMirror →</a></td>
</tr>
<tr>
<td align="center" width="240"><a href="https://www.infistar.cc/register?aff=9N89LEMV&amp;ref_source=link"><img src="docs/assets/sponsors/infistar-logo.svg" alt="Infistar.cc" width="140" /></a><br/><strong><a href="https://www.infistar.cc/register?aff=9N89LEMV&amp;ref_source=link">Infistar.cc</a></strong></td>
<td>Thank you to Infistar.cc for sponsoring Archify! One API key covers text, image, and video creation with GPT, Claude, Gemini, DeepSeek, Qwen, Kling, and other models, without switching groups. Model API pricing starts at 1% of official rates, and AI images start at ¥0.06 each.<br/><br/>Exclusive offer for Archify users: Sign up through our referral link for $5 in trial credits and a special offer on your first top-up.<br/><br/><a href="https://www.infistar.cc/register?aff=9N89LEMV&amp;ref_source=link">Try Infistar →</a></td>
</tr>
<tr><td align="center" width="240"><a href="https://github.com/EverMind-AI/Raven"><img src="docs/assets/sponsors/evermind-archify-raven.png" alt="Archify × Raven" width="200" /></a><br/><strong><a href="https://github.com/EverMind-AI">EverMind</a> · <a href="https://github.com/EverMind-AI/Raven">Raven</a></strong></td><td>EverMind sponsors Archify and builds memory infrastructure for agents. Its <a href="https://github.com/EverMind-AI/Raven"><strong>Raven</strong></a> harness supports Archify as a Skill for verified, interactive system maps.</td></tr>
</table>

> Want to sponsor Archify? [Contact us by email.](mailto:2801884530@qq.com)

## Show what matters

| Explain an agent workflow | Follow a cache miss | Explore service relationships |
|---|---|---|
| [![Agent workflow tracing everything the planner drives](docs/assets/archify-demo-reach.png)](https://archify.si/gallery/artifacts/agent-tool-call.workflow.html?theme=dark&present=1#focus=planner&reach=downstream) | [![Cache-miss sequence showing the Web App to Postgres route](docs/assets/archify-demo-route.png)](https://archify.si/gallery/artifacts/cache-miss.sequence.html?theme=dark&present=1#route=web~db) | [![Production architecture comparing backend and database roles](docs/assets/archify-demo-lens.png)](https://archify.si/gallery/artifacts/production-deployment.architecture.html?theme=dark&present=1#lens=backend~database) |
| Trace everything downstream of one step. | Highlight the path from web app to database. | Focus on authored backend and database connections. |

The [Proof Lab](https://archify.si/gallery.html) contains all 11 checked-in scenarios, their JSON sources, and validation receipts.

### Understand a real repository

<sub>CODE → DIAGRAM · A source-backed system map</sub>

[![MCO runtime architecture generated from the public mco-org/mco repository](docs/assets/mco-runtime-share-card.png)](https://archify.si/cases/mco-runtime.architecture.html?theme=dark&present=1)

Archify traced [`mco-org/mco`](https://github.com/mco-org/mco) at `9f1a1cf` and produced this checked map. **[Open it ↗](https://archify.si/cases/mco-runtime.architecture.html?theme=dark&present=1)** · [trace reach ↗](https://archify.si/cases/mco-runtime.architecture.html?theme=dark#focus=router&reach=downstream) · [typed source](docs/cases/mco-runtime.architecture.json)

### Easy to extend. More ways to make it yours.

<sub>COMMUNITY STORIES · Selected examples shared by users</sub>

**Keep building after the diagram is generated.** Archify is open source and its output is standalone HTML. Ask your agent to adapt it, connect useful links, or add interactions for your own workflow. Community creations already span team collaboration, travel planning, legal citation checks, contract review, and incident retrospectives. These are just a few examples.

One user started with a hand-drawn multi-agent architecture, turned it into an interactive diagram, then added a Kimi execution pool through conversation. Others asked their agent to read a project and brought the resulting architecture into Feishu or DingTalk for team discussion.

Another user turned a Shanghai CityWalk guide into a four-day itinerary: switch between days, inspect a stop, and jump to Amap, Xiaohongshu, or Dianping. The author also added arrival check-ins and stop notes, turning the itinerary into a small tool to use during the trip. These extensions were added by the community author for this particular artifact.

**[▶ Explore the interactive Shanghai CityWalk](https://archify.si/cases/community/shanghai-citywalk.html)**

[![A community-created four-day Shanghai CityWalk itinerary](docs/assets/community/shanghai-citywalk.png)](https://archify.si/cases/community/shanghai-citywalk.html)

**[▶ Try the interactive version](https://archify.si/cases/community/shanghai-citywalk.html)** · Switch between D1–D4 and click a place to explore.

<sub>Community artifact · Shanghai CityWalk · Four days of routes and place links</sub>

### Download it. Open it. Explore it.

The output is a self-contained HTML file. Download it and open it in your browser to use the node details and path exploration included in that artifact. No Archify installation is needed to view it. Send the HTML to someone else and the interactions go with it; external websites and map links need a network connection.

**[Explore the Shanghai CityWalk ↗](https://archify.si/cases/community/shanghai-citywalk.html)** · **[Download HTML ↓](https://github.com/tt-a1i/archify/raw/refs/heads/main/docs/cases/community/shanghai-citywalk.html)**

<sub>Try switching between D1–D4, opening a place card, or following a map link. Times and place information reflect the author's original itinerary.</sub>

## Community and recognition

- **#1 on GitHub Trending's weekly, all-language repository list.** [Ranking screenshot published by the creator on September 1, 2026](https://x.com/t20000622yy/status/2094656813576880285), with all languages and “This week” selected.
- **Featured and interviewed by QbitAI.** [Project feature](https://www.qbitai.com/2026/09/482469.html) · [The developer's story](https://www.qbitai.com/2026/09/488519.html).
- **Shared with developer communities.** [midudev's post](https://x.com/midudev/status/2094425974406320207).

<sub>A selection of public coverage, community shares, and historical milestones. Follow the links for dates and sources.</sub>

## Preview

<details>
<summary>Themes, exports, and share cards</summary>

Same diagram, two themes, one click to switch:

| Dark | Light |
|---|---|
| ![Dark theme](docs/assets/archify-dark.png) | ![Light theme](docs/assets/archify-light.png) |

The Export menu copies PNG to the clipboard and downloads static or motion formats:

![Export menu](docs/assets/archify-menu.png)

After tracing a route, **Export → Route Share Card** downloads that authored path as a 1200×630 PNG with the full diagram retained for context.

![Route Share Card showing the exact Users to API Server path with the full architecture retained as context](docs/assets/archify-route-share-card.png)

After tracing authored `Upstream` or `Downstream` reach, **Export → Reach Share Card** captures that exact reading without claiming runtime impact.

![MCO downstream Reach Share Card showing authored relationships from Command Router](docs/assets/mco-runtime-reach-share-card.png)

Open [`examples/web-app.html`](examples/web-app.html) locally to try the complete viewer.

</details>

## Quick start

**Current stable version:** `v3.2.0`. See [Changelog](CHANGELOG.md#320--2026-10-18).

### 1. Install

```bash
npx skills add tt-a1i/archify -g
```

<details>
<summary>More installation options and update-check details</summary>

For an explicit, non-interactive Cursor install:

```bash
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```

To try without installing:

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

[DSH community opt-in](integrations/deepseek-harness/README.md): `dsh plugin --profile web add @tt-a1i/archify-dsh@1.0.0`

The [agent switcher](https://archify.si/start.html?agent=cursor&type=architecture) covers `cursor`, `codex`, `claude-code`, and `opencode`.

Archify may GET the fixed stable manifest solely to show an optional reminder; it never downloads or installs updates. Successful checks wait about 24 hours (±20%); active use retries failures after 6, then 24 hours. The server sees normal HTTP metadata (IP and time), but receives no version, Agent, project data, prompts, account/device ID, or ETag. You decide whether and when to update. Set `ARCHIFY_UPDATE_CHECK_DISABLED=1` to disable networking and reminder-state writes.

</details>

### Stay updated

- **Get release notifications:** select **Watch → Custom → Releases** at the top of this GitHub repository. Starring the project does not subscribe you to release notifications.
- **See what changed:** [Release notes](https://github.com/tt-a1i/archify/releases).
- **Use a feed reader:** [Subscribe to the release feed](https://github.com/tt-a1i/archify/releases.atom).

Installations with the update checker also check for newer stable releases during diagram delivery and can show a reminder. Older installations without the checker need a manual update to gain this feature. You choose whether and when to upgrade; Archify never installs updates automatically.

### 2. Start from a description — no repository required

```text
Use Archify to draw: Browser -> API -> Redis cache -> PostgreSQL fallback.
```

For source evidence, open a repository and ask:

```text
Analyze this repository, then use archify to create a high-level runtime architecture diagram.
Show 8–12 core components, one primary path, external dependencies, and trust boundaries.
Put supporting detail in cards instead of adding more edges.
```

### 3. Refine in chat

Continue with focused requests such as `add Redis`, `move auth to the left`, or `highlight the rollback path`. Archify keeps the typed source available for targeted iteration.

## Choose the right diagram

<details>
<summary>Ten diagram types, architecture comparisons, and examples</summary>


| Type | Best for | Include in your prompt |
|---|---|---|
| **Architecture** | Components, services, storage, boundaries | Scope, core components, primary path |
| **Workflow** | CI/CD, approvals, tool calls, runbooks | Participants, order, branches, exceptions |
| **Sequence** | API calls, cache fallback, auth, async traces | Callers, callees, returns, timing |
| **Data Flow** | Pipelines, lineage, PII, consumers | Sources, transforms, stores, boundaries |
| **Lifecycle** | States, retries, waits, terminal outcomes | States, events, retry and cancellation paths |
| **ERD** | Database schemas: tables, columns, keys, cardinality | Tables, every column with its type, primary/foreign/unique keys, relationship cardinality |
| **Class** | Classes, interfaces, selected members, type relationships | Types, key members, inheritance and implementations, composition, dependencies |
| **Tree** | Single-parent hierarchies: repositories, modules, capability breakdowns | Root, levels, what each branch contains |
| **Timeline** | When things happened: incident reviews, release histories | Timestamps with time zone, events, source lanes, whether times are observed or illustrative |
| **Waterfall** | Where the time went in one request or agent run | Spans, start times and durations, nesting, whether timings are measured or illustrative |

Architecture's optional `deployment-ownership` profile fails closed when authored owners, region placement, private database scope, or named crossings are missing; it is never implicit and does not inspect live infrastructure. See the [checked deployment proof](https://archify.si/gallery.html#proof-deployment-ownership).

For design or PR review, Architecture Delta compares validated Before / Delta / After snapshots with a machine receipt. Select an authored change or play one finite, viewer-only Review; it infers no impact, risk, or merge safety.

`node archify/bin/archify.mjs compare architecture base.json head.json architecture-delta.html --json`

[![Architecture Delta showing added, removed, changed, and moved authored facts](docs/assets/architecture-delta-proof.jpg)](examples/checkout-platform-delta.html)

Not sure which one fits? Use the [interactive scenario guide](https://archify.si/guide.html), or ask the zero-dependency CLI:

```bash
node archify/bin/archify.mjs guide "Show an API request with Redis cache miss"
node archify/bin/archify.mjs guide "Map Kafka topics, consumer groups, replay, and DLQ" --json
```

Workflow keeps the happy path clear across lanes:

![Workflow example](docs/assets/archify-workflow.png)

Sequence explains one interaction over time:

![Sequence example](docs/assets/archify-sequence.png)

Data Flow makes movement and sensitivity boundaries explicit:

![Data Flow example](docs/assets/archify-dataflow.png)

Lifecycle separates progress, waits, retries, and terminal outcomes:

![Lifecycle example](docs/assets/archify-lifecycle.png)

New in 3.1: ERD, Class, Tree, Timeline and Waterfall.

ERD keeps tables, every column and key, and relationship cardinality together:

![ERD example: an order management schema with customer, order, payment, inventory, product and order item tables grouped by domain](docs/assets/archify-erd.png)

Class shows contracts, selected members, and which types depend on or implement them:

![Class example: OrderService depends on the PaymentGateway interface, implemented by card and wallet gateways](docs/assets/archify-class.png)

Tree shows single-parent containment, such as a capability breakdown:

![Tree example: a payment platform broken down into orders, payments and operations capabilities](docs/assets/archify-tree.png)

Timeline places events on one proportional clock, with a lane per source:

![Timeline example: an illustrative payment incident with release, monitoring and response events on one clock](docs/assets/archify-timeline.png)

Waterfall shows where the time went across nested and overlapping spans:

![Waterfall example: illustrative timing of a checkout request where inventory lookup and discount calculation run concurrently](docs/assets/archify-waterfall.png)

Explore these examples: [`ERD`](https://archify.si/gallery/artifacts/orders.erd.html) · [`Class`](examples/class-payments-rendered.html) · [`Tree`](examples/tree-payment-platform-rendered.html) · [`Timeline`](examples/timeline-payment-incident-rendered.html) · [`Waterfall`](examples/waterfall-checkout-request-rendered.html). The Timeline and Waterfall examples use illustrative data; treat timestamps or durations as real only when they come from logs or traces.

Architecture examples: [`web-app`](examples/web-app.html) · [`Archify pipeline`](examples/archify-repo.html) · [`grid placement`](examples/archify-repo-grid.html) · [`desktop agent`](examples/maka-architecture.html)

</details>

## Why Archify

| Understand the structure | Walk through the story |
|---|---|
| Map components, workflows, and relationships from code or a description. | Explore nodes, follow paths, and share any view as a link. |
| **Extend it your way** | **Share the result** |
| Keep an editable source and build on the open-source code or generated HTML with your own interactions and use cases. | Share a self-contained HTML file or export images, video, and share cards. |

<details>
<summary>The engineering behind the experience</summary>


- **Layout judgment over generic auto-layout** — the agent chooses hierarchy, spacing, routes, and emphasis; shared automatic endpoints spread deterministically instead of piling arrows on one midpoint.
- **Typed JSON IR** — every renderer-backed mode has a schema and reproducible source.
- **Atomic validation before delivery** — schema, layout, HTML/SVG, route, and label-to-route clearance checks must all pass before a showcase artifact replaces the last known good output.
- **Failures come with a repair receipt** — `validate --json` and `deliver --json` return stable rule codes, the exact subject, measured evidence, and only supported repair controls instead of a Node stack or an unstructured retry guess.
- **Last-good live preview** — an optional desktop loop watches one JSON file, refreshes only after the latest candidate passes every gate, and keeps the previous verified diagram visible when a save is incomplete or invalid.
- **Truthful interaction** — focus, upstream/downstream reach, exact routes, role comparison, and stories reuse authored nodes and relationships instead of inventing topology or claiming runtime impact.
- **Source evidence, only when requested** — Evidence-backed Architecture nodes mark themselves `SRC n` and open Git-verified files and line ranges pinned to one public commit; ordinary artifacts stay source-free.
- **Portable by default** — the result is one HTML file; exports remain full-diagram and free of temporary viewer state.

Archify is not a general-purpose drawing editor or a Mermaid theme. It turns technical intent into a communication artifact.

</details>

## How it works

<details>
<summary>Generation, validation, preview, and delivery details</summary>

| Step | What happens |
|---|---|
| **Generate** | The agent creates typed JSON IR from your description. |
| **Validate** | Bundled validators and layout rules check the source; failures identify the exact local repair in machine-readable JSON. |
| **Preview (optional)** | A loopback-only desktop session watches one source and reloads only verified revisions; failures keep the last-good artifact. |
| **Deliver** | A same-directory candidate is rendered and checked; only a passing artifact atomically replaces the target, then optional `--open` launches that exact file. |
| **Iterate** | The agent updates the source while unrelated structure stays stable. |

Useful repository commands:

```bash
cd archify
node bin/archify.mjs doctor
node bin/archify.mjs demo /tmp/archify-demo
node bin/archify.mjs guide "Show CI/CD checks, approval, deploy, and rollback"
node bin/archify.mjs validate workflow examples/agent-tool-call.workflow.json --quality showcase --json
node bin/archify.mjs preview workflow examples/agent-tool-call.workflow.json /tmp/workflow.html --quality showcase
node bin/archify.mjs deliver workflow examples/agent-tool-call.workflow.json /tmp/workflow.html --quality showcase --open --json
```

`preview` is an explicit loopback-only desktop mode: it watches one JSON file on a random `127.0.0.1` port, keeps the last verified output through failures, stops with Ctrl-C, and adds no generated-HTML runtime. Use `--no-open` for tests or manual URL opening.

`deliver --open` is an opt-in one-shot handoff after commit. Opener failure preserves success; JSON remains on stdout and the absolute fallback path goes to stderr.

On failure, `validate --json` and `deliver --json` emit one JSON object. Apply only each `diagnostics[]` subject's `supportedFixes`, within the Skill's two correction rounds; visual review remains separate.

Settings:

```json
{
  "meta": {
    "locale": "en",
    "animation": "trace",
    "visual_preset": "signal-flow"
  }
}
```

`meta.locale` localizes page title, Legend, states/errors, a11y, HTML/SVG `lang`—never authored content. `en`, `zh-CN`, `zh-TW`, `es`, `ko`, and `ar` are bundled and need only `meta.locale`; `meta.translations` (canonical message key → translated string) overrides individual keys and keeps the rest of the language. Other languages supply their catalog there (see `archify/examples/locales/`), or the renderer falls back to English and discloses it. Static omits `animation`; `classic` defaults.

</details>

## Explore and share the output

| Action | Control |
|---|---|
| Open the factual Diagram Guide | <kbd>?</kbd> |
| Find and focus a semantic node | <kbd>/</kbd> |
| Trace upstream/downstream authored reach | Focus a node → `Upstream` / `Downstream` |
| Probe a directed route and inspect its journey | <kbd>R</kbd> or `PATH` |
| Compare one or two semantic roles | <kbd>L</kbd> or `LENS` |
| Open the live overview radar | <kbd>M</kbd> or `MAP` |
| Enter Presentation Stage | <kbd>F</kbd> |
| Choose visual style (`S` cycles) / toggle theme / open Export | <kbd>S</kbd> / <kbd>T</kbd> / <kbd>E</kbd> |
| Zoom or reset | <kbd>+</kbd> / <kbd>-</kbd> / <kbd>0</kbd> |

Stable links can restore `#focus=<id>`, `#focus=<id>&reach=upstream|downstream`, `#relation=<id>`, `#route=<source>~<target>`, and `#lens=<kind>~<kind>`. Live repeats connection flow until paused; semantic previews remain bounded. Motion respects `prefers-reduced-motion` and never enters canonical exports.

The complete generation and viewer contract lives in [`archify/SKILL.md`](archify/SKILL.md).

## Installation options

| Surface | Install location or method | Capability |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` or `.claude/skills/` | Full renderer + validation workflow |
| **Codex CLI** | `~/.agents/skills/` or `.agents/skills/` | Full renderer + validation workflow |
| **opencode** | `~/.config/opencode/skills/`, `.opencode/skills/`, or `.agents/skills/` | Full renderer + validation workflow |
| **Claude.ai** | Upload `archify.zip` under Settings → Capabilities → Skills | Depends on Node.js access in the sandbox |
| **Project Knowledge** | Upload `archify.zip` to the project | Prompt-driven architecture fallback |
| **Hermes Agent** | Opt-in: `hermes skills install skills-sh/tt-a1i/archify/archify -y` | Community Skill-only integration; Node `>=18`; not a Nous official product. No telemetry. It is not a switcher target. [Details](integrations/hermes-agent/README.md). |
| **DeepSeek Harness** | Opt-in: `dsh plugin --profile web add @tt-a1i/archify-dsh@1.0.0`. Invoke: `Use the archify skill to map this repository's runtime architecture.` Remove: `dsh plugin --profile web remove @tt-a1i/archify-dsh`. | Community integration for developer-preview `@deepseek-ai/dsh@0.1.2-rc.1`; Node `^22.19.0 \|\| >=24.0.0`; not an official DeepSeek product. No telemetry. Shell files need exact workspace paths, not Web Produced Files. [Details](integrations/deepseek-harness/README.md). |

## Reference and scope

- [Schema reference](archify/schemas/README.md) · [Skill](archify/SKILL.md) · [Examples](archify/examples/) · [Agent cookbook](docs/authoring-cookbook.md)
- [Changelog](CHANGELOG.md)
- [Roadmap](ROADMAP.md)
- [Generated Proof Lab](https://archify.si/gallery.html)

Automatic Mermaid parsing, general-purpose auto-layout, hosted sharing, and WYSIWYG editing are intentionally outside the current scope.

## Community

👋 **Welcome to the Archify Community!**

Connect with other users and developers, share ideas, request features, report bugs, discuss development, and help make Archify better together.

- <img src="docs/assets/community/discord.svg" alt="" width="18" /> [Discord](https://discord.gg/6xWMjgCeUq)
- <img src="docs/assets/community/wechat.svg" alt="" width="18" /> WeChat: scan the QR code below. WeChat group codes expire periodically; if this one has expired, ask for the current code through Discord or QQ.
- <img src="docs/assets/community/qq.svg" alt="" width="18" /> QQ group: `1121948602`

<table>
<tr>
  <td align="center"><strong><img src="docs/assets/community/wechat.svg" alt="" width="18" /> WeChat</strong><br/><img src="docs/assets/community/wechat-qr.png" alt="Archify Official WeChat group QR code" width="300" height="300" /></td>
  <td align="center"><strong><img src="docs/assets/community/qq.svg" alt="" width="18" /> QQ</strong><br/><img src="docs/assets/community/qq-qr.png" alt="Archify Official QQ group QR code" width="300" height="300" /></td>
</tr>
</table>

<a id="official-services"></a>

## Official channels and third-party services

- **Open-source project:** The source code and installation packages are free to use under the [MIT License](LICENSE).
- **Official website:** [archify.si](https://archify.si) currently provides project information, examples, and installation guidance.
- **Third-party services:** Pricing, data handling, and support are determined by the respective provider. A similar name or domain does not establish an official affiliation.

## License

[MIT](LICENSE) — free to use, modify, and distribute.

## Contributing

Building a standalone package on Archify? [Submit it to the community catalog](community/README.md#submitting-a-package); the guide includes a collapsible example and complete Chinese steps.

Issues, pull requests, and real-world diagrams are welcome. Start with the [contribution guide](CONTRIBUTING.md), use the reproducible bug form for failures, or submit a validated diagram through the [community showcase form](https://github.com/tt-a1i/archify/issues/new?template=showcase.yml).&nbsp;·&nbsp;[LINUX&nbsp;DO](https://linux.do)

## Support Archify

If Archify has been useful to you, you can support its continued development. Thank you for helping keep the project going ❤️

<details>
<summary>Support via WeChat Pay</summary>

Scan the QR code below with WeChat, or save it and open it in WeChat to scan.

<p align="center"><img src="docs/assets/support/wechat-pay.png" alt="WeChat Pay QR code to support the Archify maintainer" width="240" /></p>

</details>

<details>
<summary>Support via Alipay</summary>

Scan the QR code below with Alipay, or save it and open it in Alipay to scan.

<p align="center"><img src="docs/assets/support/alipay.png" alt="Alipay QR code to support the Archify maintainer (name redacted)" width="240" /></p>

</details>

Using Archify, sharing it, reporting bugs, and contributing improvements are also ways to help.

## Star History

<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tt-a1i/archify/star-history/assets/star-history-dark.svg" /><img alt="Star History" src="https://raw.githubusercontent.com/tt-a1i/archify/star-history/assets/star-history-light.svg" /></picture></p>

## Docs
### docs/ listing
```
file	.nojekyll
file	article-archify.md
file	article-cover.jpg
file	article-experiment.jpg
file	article-killed.jpg
file	article-layout-compare.jpg
file	article-pipeline.jpg
file	artifact-install-v2-measurement.md
dir	assets
file	authoring-cookbook.md
file	authoring-cookbook.zh-CN.md
dir	cases
file	cursor-acceptance-2026-07.md
file	deployment-ownership-profile-acceptance-2026-07-23.md
dir	evidence
file	gallery.html
dir	gallery
file	guide.html
file	index.html
dir	issue-52-visual-evidence
dir	reading-evidence
dir	releases
dir	research
dir	reviews
file	skill-embedded-optional-update-notifier-design.md
dir	skill-updates
dir	specs
file	start.html
```

### docs/article-archify.md
```
# 让 AI 画架构图不难。难的是决定不画什么。

> [!IMPORTANT]
> 这是基于 Archify v2.6 的历史文章，用于保留当时的设计背景，不代表当前功能、命令或产品边界。最新能力与安装方式以 [README](../README.md) 为准；仍然有效的架构取舍以 [ROADMAP](../ROADMAP.md) 为准。

![Archify cover — 左边自动布局死路，右边手动布局活路](article-cover.jpg)

一条命令：

```
node renderers/architecture/render-architecture.mjs web-app.json web-app.html
```

跑完你会得到一个独立的 HTML 文件。打开浏览器，深色/浅色一键切换。PNG、JPEG、WebP、SVG 四种导出，4x 原生光栅化，复制到剪贴板就能贴进 Notion 或 GitHub README。

看起来只是一张架构图。但打开浏览器你会注意到，这图不是均匀的方格阵列。

Auth Provider 飘在 AWS 区域的左上角外面——它不是 AWS 的资源。S3 放在 CloudFront 下方而非旁边——这是层级关系，不是同级关系。security-group 的虚线边界精确地画在 30px padding 处。

这些不是样式。是布局。

---

**Archify 是一个让 Claude 用自然语言画技术架构图的 Skill**。支持五种图表类型——Architecture（系统架构）、Workflow（工作流水线）、Sequence（调用时序）、Data Flow（数据管线）、Lifecycle（状态机）。每种都有独立的 JSON Schema、独立的渲染器、独立的布局规则检查。项目从 Cocoon AI 的 v1 分支重写而来，目前 v2.6，MIT 协议。

但这篇文章关心的不是功能列表。我关心的是一个设计决策——Archify 明确拒绝了自动布局引擎。而且这个拒绝不是"我们还没做"，是"我们实验验证了，这条路不通"。

---

## 一个实验：换 CSS 不换布局，能差多远？

Archify 的 Roadmap 里有一段不常出现在开源项目中的文字：

> **Auto-layout (dagre / elk-js) is a dead end for archify.**

为了验证这个判断，作者做了一个盲测实验。

原始实验用了五张真实 Mermaid 流程图，每张渲染三个版本：

- **版本 A**：原生 Mermaid，dagre 布局，默认主题。
- **版本 B**：同样 dagre 布局，但换上 archify 的深色配色、JetBrains Mono 字体、slate-900 背景。布局不动——只换皮。
- **版本 C**：archify 手动布局——Claude 分配语义类（`c-frontend`、`c-backend`、`c-security` 等），手动摆放坐标，archify CSS 是最后一步。

原始 15 张截图打乱、去标签，盲评 1-10 分。2026-09-01 因其中两个来源仓库没有可核验的再分发许可，当前仓库已移除这两组输入和衍生物，仅保留 3 图、9 张截图；因此原始 5 图实验无法再从当前 HEAD 完整复现。

结论写在 `experiments/v3-mermaid-validation/RESULT.md` 里，只一行：

> **C looks good; A and B both don't look good. B is not meaningfully better than A.**

换 CSS 不换布局，审美差距**无法弥合**。B 不比 A 更好看。一张均匀网格涂上更好的颜色，仍然是一张均匀网格。

![三列盲测对比：A=原生Mermaid 4分 · B=Mermaid+archify CSS 4分 · C=archify手动布局 9分](article-experiment.jpg)

这就是为什么 ROADMAP.md 里用了"dead end"这种词——不是因为 dagre 或 elk-js 不好，而是因为 Archify 的审美**不来自配色，来自空间叙事**。Auth Provider 为什么放在外面？S3 为什么比 CloudFront 低 30px？虚线边界为什么是 30/50 padding？这些都是 Claude 的判断。去掉布局判断，就去了产品骨头。

相应的，Roadmap 里 P1（Mermaid 解析器引入 dagre 自动布局）打了 **KILLED**。P3（end-to-end 解析管线）、P4（IR → Mermaid 输出、C4 输入）同样。

另外一个要命的问题也在 Roadmap 里写清楚了：

> **"Prettier Mermaid renderer" is already taken.** lukilabs/beautiful-mermaid 有 15 套主题（Tokyo Night、Catppuccin、Nord、Dracula），8.1k stars。Mermaid 11.14 自己加了 Neo/Redux 主题、ELK 布局、Hand Drawn 风格。做"更好看的 Mermaid"是已经被占领的赛道。

Archify 选的是一条更窄但更硬的路：**让 Claude 做信息架构决策，而不只是往布局引擎的输出上刷 CSS。**

---

## 不是"人类在环"，是"判断在环"

![Archify 渲染管线：自然语言 → Claude 推断空间关系 → JSON IR + Schema 验证 → 类型化渲染器 + 布局规则检查 → 独立 HTML](article-pipeline.jpg)

这句话你可能在别的 AI 工具文章里看过："人机协作"、"人类在回路中"。太模糊了——谁在回路里？做了什么事？

Archify 的回路里有一个具体的决策者：Claude。它做一件事——**从语义推断空间关系**。

举个例子。你要画一个 Web 应用架构：

```
用户说：AWS 上跑着 Next.js 前端、Go 后端和 PostgreSQL。
前端通过 CloudFront 分发，缓存打在 S3 上。
所有流量经过 WAF，auth 走独立 Identity Provider。
```

dagre 会怎么做：六个节点排成两行三列。整齐、均匀、无聊。

Claude 的答案——当 Archify 让它自己决定坐标时：S3 放在 CloudFront 下方而非旁边，因为"缓存打在 S3 上"意味着**层级关系**而非**同级关系**。Identity Provider 故意浮在 AWS region 边界外面，因为它不是 AWS 的资源。WAF 画在整个入口处。PostgreSQL 和 Go backend 靠得更近，因为它们高频交互。

这不是配色问题。这是**对"谁依赖谁"、"谁在外面"、"什么应该靠在一起"的空间翻译**。

![左：dagre 均匀网格 · 右：Claude 语义布局 —— auth 浮出边界、S3 在 CDN 下方、backend 靠紧 database](article-layout-compare.jpg)

这个设计哲学在 Archify 的架构上有个精确的落点：**类型化渲染器不是自动布局引擎**。

Workflow、Sequence、Dataflow、Lifecycle 四种模式的渲染器有预定义的 lane/stage/row 网格。它们告诉你哪些坐标是合法的——但是 Claude 仍然决定把哪个节点放进哪个泳道、哪个阶段、主路径上放哪些步、连接线走哪条 route。渲染器给的是约束，不是解。

举个具体的例子——layout-rules.test.mjs 里的一条断言：

```
节点重叠 → 报错："/nodes/3 (label: 'Data Cache') overlaps /nodes/5 (label: 'CDN Edge')"
标签越界 → 报错并给出数值阈值
跨泳道重叠 → 报错并命名两边的泳道名
```

这四种错误的返回格式不是随意写的。它们的格式专门服务于一件事——**让 LLM 能自我修复**。每条错误消息包含 JSON path、违规的两个对象名、超出的数值或合法范围。Claude 读到这种错误后，可以自己修正 JSON 并重新渲染，不需要人介入。

不是"人类在环"。是"判断在环"。人类提供的是判断——API 架构师理解"Identity Provider 不是 AWS 资源"——AI 负责执行判断（选坐标、定距离、调间距）并接受约束检查。

---

## 决心不做什么，比做了什么更难

翻 Archify 的 ROADMAP.md 和 CHANGELOG，最惊讶的不是它做了什么，是它**公开拒绝了多少东西**。

| 被拒绝的功能 | 理由 |
|---|---|
| dagre / elk-js 自动布局 | 实验证明 auto-layout + CSS 不比原生 Mermaid 更好 |
| Mermaid 解析器管线 | 同上的实验结论 |
| `?exportScale=N` URL 参数 | 诱导用户选低质量的缩放下采样，而项目已经有 4x 原生光栅化 |
| gzip+base64 分享链接 | XSS 向量，URL 长度限制，大家已经接受了"发 HTML 文件" |
| 色盲安全调色板 | 维护负担过重，CSS 变量系统使下游 fork 在约 30 行内就能完成 |
| 缩放/平移 UI | 浏览器原生双指缩放和 Cmd+滚轮已经可用 |
| 字体嵌入光栅导出 | 每文件增加约 150KB，收益有限 |
| PDF 导出按钮 | Cmd+P 自带打印样式表（`@page landscape`） |
| 多语言 UI | 保持界面极简，国际化交给下游 |

这些决策每一项都带着成本意识。gzip+base64 分享听起来方便——但一旦做了，就要一直维护 XSS 防护，还要处理 URL 长度在各个平台上的表现差异。"发 HTML 文件"在今天已经很自然了——Slack 传文件、GitHub 上传、邮件附件——再叠一层 base64 包装，增加的复杂度买回来的便利微乎其微。

另一类决策更有意思——"我们已经有了更好的替代方案"。4x 原生光栅化比 `?exportScale=N` 质量好得多；浏览器 Cmd+P 比内置 PDF 按钮稳定得多；CSS 变量系统比硬编码调色板灵活得多。**做了新东西，就可以不维护旧方案。**

Archify 在这件事上极其诚实。没有任何一项被拒绝的功能挂着"未来考虑"的标签。砍了就砍了，理由写清楚，不留后路。

这种诚实在中国开源项目里少见。大部分项目 Roadmap 里堆满了"计划中"、"考虑中"，Archify 的 Roadmap 却有一整节的 **KILLED**。

![九块"墓碑"——被明确拒绝的 9 个功能，每块写明理由](article-killed.jpg)

---

## 什么情况下它会失效

Archify 的布局哲学有一个硬前提：**负责做布局判断的那个人（或 AI）真的理解架构语义**。

当图太大时，这个前提会崩。一个 30 节点的微服务拓扑、横跨 3 个 region 的部署图——Claude 会在中间某个节点处丢失全局结构，开始随机分配坐标。它不会再被语义驱使，只是机械地在 viewBox 里填满剩余空间。这种时候，dagre 的均匀网格反而更好——至少它不出错。

第二类失效场景是：用户自己描述不清楚。"帮我画个架构图"——然后就没了。Archify 的 SKILL.md 在开头就告诉你，Claude 需要问清楚：组件类型、拓扑关系、安全边界、主要数据流。如果用户说不清楚，问出来的图也不会有信息架构。

第三类失效更微妙：当图的审美**不需要空间叙事**时，Archify 的所有设计都变成了过度设计。一个 4 步骤的审批流画在泳道里很清爽，但为了它走 JSON IR → schema 验证 → renderer 的全套流程，不如直接在 Excalidraw 里拖四个方块。

Archify 不适用于"所有图"。它适用于**那些组件之间的空间关系本身就携带信息的图**。

---

## 那么，Archify 真正值得学习的是什么？

不是配色系统。不是 4x 导出。甚至不是五种图表类型——类型会继续增加。

值得看的是三件事。

**第一，一个 AI 工具的设计哲学可以小到"一个实验结果"。**

Archify 拒绝 auto-layout 不是哲学讨论——是先跑了一个 5 张图的盲测，结果 B 不比 A 好，然后 ROADMAP 里所有跟 dagre 相关的任务集体被杀。设计决策不是从观点出发的，是从一堆截图和评分的表格出发的。这比任何关于"AI 工具该怎么设计"的方法论都可信。

**第二，"知道自己不是什么"比"知道自己是什么"更值钱。**

"Prettier Mermaid renderer is already taken" —— 这句话省了至少三个月的工作。Archify 不跟 beautiful-mermaid 比配色、不跟 Mermaid 11.14 比 Hand Drawn 风格。它选了一个更窄的赛道：信息架构。你画的是架构图，配色只是最后一步，布局才是主角——而布局是 Claude 的理解，不是 dagre 的均匀网格。

**第三，对 AI 来说，"约束"和"自由"不是对立的。**

Archify 的渲染器给你一个 lane/stage 网格（约束），但让你决定每个节点进哪个泳道、每个连接走哪条路由（自由）。Schema 验证会卡你格式（约束），但错误消息格式被专门设计成 Claude 能自动修复（自由）。如果你想让 Claude 稳定在一条特定的布局路径上，给它一个比"随便画"更窄的系统。

---

Archify 的 JSON IR 从第一天就强制声明 `schema_version`。最初五种图都固定为 `schema_version: 1`；现在 Workflow 是明确的例外：v1 继续合法并保持旧版固定布局，v2 则显式选择新的可读性编译器。其他四种图仍固定为 v1。打破性变更触发版本号升级，旧版本永远合法。

这一行比它前面 200 行的 SKILL.md 都更能说明问题。

因为这个字段承认了一件事：今天最好的布局判断，明天可能就不是最好的了。版本号是给未来留的退路——**在不知道明天会更好的情况下，先保证今天不会更差。**
```

### docs/artifact-install-v2-measurement.md
```
# Artifact → Install v2 measurement contract

Artifact → Install v2 is a bounded change to the existing journey. Proof Lab cards link to `start.html?type=<type>&source=gallery`, and the Start page selects the matching typed recipe and can copy the selected agent's install command plus the bounded prompt in one action. Generated artifacts no longer emit the former footer link; `source=artifact` remains accepted only for compatibility with already-shared artifact URLs.

The page records only coarse interaction steps:

- `start_view`
- `starter_copy`
- `global_install_copy`
- `project_install_copy`
- `prompt_copy`
- `proof_open`

Each event contains `schemaVersion`, `step`, the allow-listed source, diagram type, agent, and language. It never contains a repository path, diagram title, prompt text, node, relationship, source JSON, or user identifier. Unknown source values are normalized to `direct`.

## Privacy boundary

Events are capped at the latest 24 entries in `sessionStorage` under `archify.start.events.v1`. The page also dispatches the same detail as the `archify:start-funnel` browser event and exposes a read-only snapshot through `window.ArchifyStartMetrics.snapshot()`.

**No network request is made by Archify.** The page contains no `fetch`, `sendBeacon`, or XHR path. Closing the browser session discards the local receipt. A hosting operator must not attach an external event sink without a separate privacy decision, public disclosure, retention policy, and test update.

## Observable metrics

Within a controlled browser test or an explicitly instrumented host, compute:

- Legacy artifact arrival share: `source=artifact` `start_view` / all `start_view`
- Gallery arrival share: `source=gallery` `start_view` / all `start_view`
- Combined starter copy rate: `starter_copy / start_view`
- Any install copy rate: (`starter_copy` + `global_install_copy` + `project_install_copy`) / `start_view`
- Prompt-only copy rate: `prompt_copy / start_view`
- Proof reassurance rate: `proof_open / start_view`

Count at most one occurrence of each step per browser session when reporting conversion, even though the local diagnostic receipt retains repeated clicks. Segment only by the allow-listed source, type, agent, and language.

## What this does not prove

**First-diagram success is not observable from this static page.** A successful copy is an intent signal, not proof that installation completed, the agent generated a candidate, validation passed, or the user retained Archify. Do not label these ratios “activation,” “success,” or “retention.”

The Ordinary-Model Floor benchmark measures candidate quality independently. A future end-to-end activation metric would require an explicit, privacy-reviewed receipt boundary at the installed CLI or a voluntary user submission; it must not be inferred from Start-page clicks.

## Evaluation window

Before publishing a conversion claim:

1. Pin the repository commit and the exact v2 UI.
2. Validate the event contract in a real browser for artifact, gallery, direct, and rejected unknown-source URLs.
3. If an approved aggregate sink is later added, run a predeclared observation window and publish both session counts and rates; do not compare against a historical period that lacked equivalent instrumentation.
4. Keep deterministic page tests, package tests, and visual review as release gates regardless of copy rate.

Until an approved aggregate sink exists, the event receipt is for local QA and experiment readiness only.
```

### docs/authoring-cookbook.md
```
# Authoring Cookbook

Archify is primarily an Agent-facing Skill. Normal users can ask a Skill-capable Agent to generate the diagram; they do not need to learn the schema or run `validate`, `inspect`, or `deliver` themselves.

The manual workflow below is a reference for integration, contribution, and troubleshooting. The commands assume that you are in the repository's `archify/` directory, or in the root of an installed Archify skill.

## 1. Check the installation

Archify requires Node.js 18 or later. Run the doctor command before authoring a diagram:

```bash
node bin/archify.mjs doctor
```

If you are installing from npm-compatible skill tooling, the global install is:

```bash
npx skills add tt-a1i/archify -g
```

## 2. Choose a diagram type

Use the type that matches the question you want the reader to answer:

| Type | Use it for | Start with |
| --- | --- | --- |
| `architecture` | Components, services, storage, and boundaries | `examples/web-app.architecture.json` |
| `workflow` | Ordered work, approvals, branches, and runbooks | `examples/agent-tool-call.workflow.json` |
| `sequence` | Calls, returns, cache misses, and timing | `examples/cache-miss-request.sequence.json` |
| `dataflow` | Data movement, transformations, and consumers | `examples/product-analytics.dataflow.json` |
| `lifecycle` | States, retries, waits, and terminal outcomes | `examples/agent-run.lifecycle.json` |

When the type is unclear, ask the built-in scenario guide:

```bash
node bin/archify.mjs guide "Show an API request with a Redis cache miss" --json
```

The guide recommends a type and returns a recipe. It does not create the diagram for you.

## 3. Author one bounded source file

Start with one clear story. Keep the first diagram to roughly 8–12 primary nodes, one main path, and only the branches that help explain the question. The checked-in examples are safer starting points than copying a large generated artifact.

Every source needs a `schema_version`, a `diagram_type`, a `meta.title`, and the structural arrays required by that renderer. Read the [schema reference](../archify/schemas/README.md) for the exact fields and allowed values.

For a repository-backed Architecture diagram, add revision-pinned repository metadata and source ranges to the JSON, then pass the local repository path to the command:

```bash
node bin/archify.mjs validate architecture path/to/diagram.json \
  --repo-root path/to/repository --quality showcase --json
```

Archify verifies the Git origin, commit, blobs, and requested lines. Do not add source evidence when the repository or revision cannot be verified.

## 4. Validate before rendering a handoff

Use `standard` while exploring and `showcase` for a polished artifact or checked-in proof:

```bash
node bin/archify.mjs validate architecture examples/web-app.architecture.json \
  --quality showcase --json
```

On success, the JSON receipt contains the artifact checks and composition summary. On failure, it contains a `stage` and `diagnostics[]`; repair the named subject and use the listed `supportedFixes` before trying another change. A non-zero exit code is never a successful validation.

For Architecture layout inspection, use the renderer's machine-readable layout output:

```bash
node bin/archify.mjs inspect architecture path/to/diagram.json
```

`inspect` is currently Architecture-only and is useful when a geometry diagnostic names a route or placement problem.

## 5. Deliver the trusted artifact

`render` is useful for a quick local output. Use `deliver` when the file is a handoff, release artifact, or CI output:

```bash
node bin/archify.mjs deliver architecture examples/web-app.architecture.json \
  web-app.html --quality showcase --json
```

`deliver` freezes the input bytes, renders a same-directory candidate, runs the final artifact checks, and replaces the target only after every gate passes. Its receipt includes specification and artifact SHA-256 hashes. Add `--open` only for an interactive local handoff:

```bash
node bin/archify.mjs deliver architecture examples/web-app.architecture.json \
  web-app.html --quality showcase --open --json
```

To compare two Architecture snapshots, use `compare`. It writes the HTML and a sidecar receipt beside it:

```bash
node bin/archify.mjs compare architecture base.json head.json \
  architecture-delta.html --quality showcase --json
```

Repository revision, provider, link mode, or location representation changes are reported separately from component, relationship, and boundary changes. The Delta page never marks a graph entity as changed for provenance alone, and it does not expose repository URLs in the provenance summary.

## 6. Inspect the exact final file

The deterministic checks do not exercise the Viewer in a browser. Collect automated browser evidence from the exact delivered HTML when Chrome or Chromium is available:

```bash
node bin/archify.mjs visual-check web-app.html --json
```

This receipt measures bounded runtime behavior; it does not approve perceptual polish. Inspect the HTML or generated screenshots separately. Follow the [delivery contract](../archify/references/delivery-contract.md) when recording supplementary manual browser work; an unconstrained glance supports only perceptual review.

Use the delivery contract for the canonical browser-evidence coverage, artifact binding, visual-review status, and handoff fields. The [Skill contract](../archify/SKILL.md) explains the authoring invariants and the bounded repair loop.
```

### docs/authoring-cookbook.zh-CN.md
```
# Archify 编图实践手册

Archify 首先是面向 Agent 的 Skill。普通用户只需向支持 Skill 的 Agent 描述想要的图；不必学习 Schema，也不必自己运行 `validate`、`inspect` 或 `deliver`。

下面的手工流程面向集成、贡献和排错。命令假设你位于仓库的 `archify/` 目录，或已经安装好的 Archify Skill 根目录。

## 1. 检查安装

Archify 要求 Node.js 18 或更高版本。开始编图前先运行 doctor：

```bash
node bin/archify.mjs doctor
```

如果通过兼容 npm 的 Skill 工具安装，可以执行：

```bash
npx skills add tt-a1i/archify -g
```

## 2. 选择图表类型

根据读者需要回答的问题选择类型：

| 类型 | 适合说明 | 可从这里开始 |
| --- | --- | --- |
| `architecture` | 组件、服务、存储和边界 | `examples/web-app.architecture.json` |
| `workflow` | 有序工作、审批、分支和 Runbook | `examples/agent-tool-call.workflow.json` |
| `sequence` | 调用、返回、缓存未命中和时序 | `examples/cache-miss-request.sequence.json` |
| `dataflow` | 数据移动、转换和消费者 | `examples/product-analytics.dataflow.json` |
| `lifecycle` | 状态、重试、等待和终态 | `examples/agent-run.lifecycle.json` |

不确定类型时，可以询问内置场景指南：

```bash
node bin/archify.mjs guide "展示带 Redis 缓存未命中的 API 请求" --json --lang zh
```

指南会推荐类型并返回配方，但不会替你创建图。

## 3. 编写边界清楚的源文件

从一个明确故事开始。第一张图建议只保留约 8–12 个主要节点、一条主路径，以及确实能帮助解释问题的分支。相比复制大型生成成品，直接参考仓库内示例更稳妥。

每个源文件都需要 `schema_version`、`diagram_type`、`meta.title`，以及对应 Renderer 要求的结构数组。精确字段和允许值请阅读 [Schema 说明](../archify/schemas/README.md)。

如果要生成基于仓库证据的 Architecture 图，需要在 JSON 中加入固定版本的仓库元数据和源码范围，再把本地仓库路径传给命令：

```bash
node bin/archify.mjs validate architecture path/to/diagram.json \
  --repo-root path/to/repository --quality showcase --json
```

Archify 会校验 Git 远端、commit、blob 和请求的代码行。无法验证仓库或版本时，不要添加源码证据。

## 4. 先校验，再交付

探索阶段可以使用 `standard`，正式成品或仓库内证明建议使用 `showcase`：

```bash
node bin/archify.mjs validate architecture examples/web-app.architecture.json \
  --quality showcase --json
```

成功时，JSON 回执包含成品检查和构图摘要。失败时，回执包含 `stage` 和 `diagnostics[]`；只修复被点名的对象，并优先使用 `supportedFixes` 中列出的修复方式。退出码非零时，绝不能描述为校验成功。

Architecture 图需要检查布局时，可以使用 Renderer 的机器可读布局输出：

```bash
node bin/archify.mjs inspect architecture path/to/diagram.json
```

`inspect` 当前只支持 Architecture，适合诊断信息指向线路或摆放问题时使用。

## 5. 交付可信成品

`render` 适合快速本地输出；当文件要交给别人、用于发布或作为 CI 产物时，请使用 `deliver`：

```bash
node bin/archify.mjs deliver architecture examples/web-app.architecture.json \
  web-app.html --quality showcase --json
```

`deliver` 会冻结输入字节，在目标文件同目录生成候选文件，运行最终成品检查，并且只在全部门禁通过后替换目标。回执包含源文件和成品的 SHA-256 哈希。只有需要立即本地打开时才加 `--open`：

```bash
node bin/archify.mjs deliver architecture examples/web-app.architecture.json \
  web-app.html --quality showcase --open --json
```

要比较两份 Architecture 快照，请使用 `compare`。它会在 HTML 旁边写入 sidecar 回执：

```bash
node bin/archify.mjs compare architecture base.json head.json \
  architecture-delta.html --quality showcase --json
```

仓库 revision、provider、链接模式或地址表达方式的变化会与组件、关系和边界变化分开报告。仅来源发生变化时，Delta 页面不会把任何图实体标为已变化，来源摘要也不会暴露仓库 URL。

`compare` 首次读取两份输入后，会使用捕获的原始字节进行校验、计算回执哈希并生成差异；之后原文件的变化不会影响本次比较。非法原始字段仍会在规范化之前被拒绝。

## 6. 检查最终文件

确定性校验不会在真实浏览器中运行 Viewer。如果环境有 Chrome 或 Chromium，请对刚刚交付的 HTML 收集自动化浏览器证据：

```bash
node bin/archify.mjs visual-check web-app.html --json
```

这份回执只证明有限范围内的运行时表现，并不批准视觉质量。仍需单独检查 HTML 或生成的截图。记录补充性的手工浏览器工作时必须遵循[交付契约](../archify/references/delivery-contract.md)；不受约束的目检只影响视觉复核结论。

自动化浏览器证据的规范覆盖、成品绑定、视觉复核状态和交付回执字段请参阅交付契约。编图不变量和有上限的修复循环请参阅 [Skill 契约](../archify/SKILL.md)。
```

### docs/cursor-acceptance-2026-07.md
```
# Cursor acceptance record

> Verified: 2026-07-23
> Scope: project-local Cursor Agent Skill discovery and one checked Architecture delivery
> This is a dated compatibility record, not a claim that every Cursor version or model produces identical output.

## Environment

- Cursor Agent CLI: `2026.07.20-8cc9c0b`
- Model selection: `auto` (Cursor CLI default)
- OS: macOS 26.5.2 (`25F84`)
- Skills CLI: `skills@1.5.20`
- Archify source: `codex/cursor-onboarding`, based on `e7e22a1`

## Installation and discovery

The acceptance workspace was a new temporary directory. Archify was installed with the reproducible project command:

```bash
npx -y skills@1.5.20 add /path/to/archify \
  --skill archify --agent cursor --copy --yes
```

`skills list --agent cursor --json` reported one project-scoped `Cursor` installation at `.agents/skills/archify`. A new Cursor Agent session then independently reported that it had discovered:

```text
.agents/skills/archify/SKILL.md
```

The session ran `archify doctor` successfully before authoring. No Cursor-specific `SKILL.md`, renderer, schema, or prompt fork was present.

## End-to-end task

Cursor was asked to use Archify to create a six-component local event-processing Architecture diagram containing:

- Webhook Client
- API Gateway
- Event Router
- Worker
- PostgreSQL
- Dead Letter Queue

The authored main path was `Webhook Client → API Gateway → Event Router → Worker → PostgreSQL`; the explicit failure route was `Worker → Dead Letter Queue` with label `on failure`.

Cursor wrote only the typed source and checked HTML in the workspace root, in addition to installer-owned files. Its delivery receipt reported:

```text
validation: passed
visual_review: skipped (image reader unavailable in Cursor session)
correction_rounds: 0
quality: showcase
compositionStatus: pass
checksPassed: 9/9
errors: 0
warnings: 0
artifact.sha256: d4d443f160fafd7615234987a5572d7169916719b9a97b9231e9f48434c79e4a
artifact.bytes: 582743
```

An independent Archify `validate --json` and `check --json` rerun matched the nine passing checks, zero composition findings, byte count, and SHA-256 receipt.

## Browser review

The generated HTML was opened in the built-in browser at a 1280×720 desktop viewport. The complete six-node main path was readable in Presentation Stage, the Worker-to-DLQ relationship remained visually distinct, and selecting the authored `Failure to DLQ` chapter framed exactly Worker and Dead Letter Queue while leaving the rest as context. The Start page's Cursor selector, English/Chinese switching, agent URL state, and exact global/project install commands were also exercised. Finally, the landing Live Proof's script-only sandbox was checked through its initial Signal Flow chapter and a deliberate Blueprint switch. All three surfaces produced zero browser warnings or errors in the final clean sessions.

Result: **Cursor project installation, native Skill discovery, execution, verified delivery, and desktop browser presentation passed for the recorded environment.**

## Boundaries retained

- `skills use ... --agent cursor` is not documented because `skills@1.5.20` rejects that launcher.
- No physical `~/.cursor/skills` path is promised; Cursor also officially scans `.agents/skills`, which the verified installer uses.
- Global installation is documented as user-wide, project installation as repository-local, and both use explicit copy mode.
- This record does not benchmark other Cursor models, claim automatic updates, or replace Archify's deterministic and perceptual delivery gates.
```

### examples/ listing
```
file	archify-repo-grid.architecture.json
file	archify-repo-grid.html
file	archify-repo.architecture.json
file	archify-repo.html
file	checkout-platform-delta.html
file	checkout-platform-delta.receipt.json
file	class-payment-processors-rendered.html
file	class-payments-rendered.html
file	dataflow-product-analytics.html
file	erd-orders-rendered.html
file	lifecycle-agent-run.html
file	maka-architecture.architecture.json
file	maka-architecture.html
file	rag-pipeline.architecture.json
file	rag-pipeline.html
file	sequence-cache-miss-request.html
file	sequence-cache-miss.html
file	subscription-billing-rendered.html
file	timeline-archify-dev-activity-rendered.html
file	timeline-payment-incident-rendered.html
file	tree-archify-repository-rendered.html
file	tree-payment-platform-rendered.html
file	waterfall-checkout-request-rendered.html
file	waterfall-example-rebuild-rendered.html
file	web-app-rendered.html
file	web-app.html
file	workflow-agent-tool-call-rendered.html
file	workflow-agent-tool-call.html
```


### CLAUDE.md
```
# Claude Code instructions

Follow [AGENTS.md](AGENTS.md).

@AGENTS.md
```

### AGENTS.md
```
# Agent instructions

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for repository changes and [REVIEWING.md](REVIEWING.md) for reviews.

## PR preparation

Before requesting final review, follow the scoped [PR improvement check](CONTRIBUTING.md#pr-improvement-check) using the project Skills when applicable.

## Test selection

Before running tests, read [Choose evidence by impact](CONTRIBUTING.md#choose-evidence-by-impact) to select coverage for the changed behavior. Use the [focused test workflow](CONTRIBUTING.md#local-setup-and-verification) for local iteration. Before integration, follow [Final integration and follow-up](CONTRIBUTING.md#final-integration-and-follow-up) to verify CI and reused evidence against the final revision.

## Live Archify installations

Install, update, reinstall, or remove a live Archify installation only when the user explicitly requests that action. Repository editing, testing, reviewing, publishing, or syncing does not authorize installation. This applies to Skills CLI, manual ZIP copies, and DSH plugins. Reuse authorization already given for the same action and scope; ask only for unresolved decisions.

- Keep the source, Skill/package, target agents, and global/project scope within the request. Avoid bulk operations or force flags that expand that scope. An update notification is informational.
- Before a Skills CLI install, discover the selected source with `npx -y skills add <source> --list --full-depth` (default source: `tt-a1i/archify`) and verify exactly one Skill named `archify`. For an explicitly requested durable local source, inspect that checkout. Stop on failed or ambiguous discovery.
- Use the canonical remote source by default. Use a local source only when requested, from a durable checkout; live symlinks must not point into temporary directories or disposable worktrees.
- Preserve unrelated files and existing unmanaged destinations. Report a destination conflict before replacing it unless that exact replacement is already explicitly authorized; use the installer's documented conflict handling within the approved scope.
- Report the action, source, targets, and result, including skipped or failed destinations. A partial installation is not a complete success.
```

### CONTRIBUTING.md
```
# Contributing to Archify

Archify is Agent-first: people describe systems, and the Skill, typed JSON, renderers, validators, and delivery receipts produce reproducible diagrams. Keep each contribution focused on one user-visible behavior or one tightly related delivery slice. Maintainers and Agents reviewing a PR or a revised head follow [Reviewing](REVIEWING.md).

## Choose the right path

- Renderer, validator, package, or Viewer defect: use the [bug report form](.github/ISSUE_TEMPLATE/bug-report.yml).
- Standalone community package: follow the [submission guide](community/README.md#submitting-a-package) and submit one metadata file to `dev`.
- Reproducible real-world diagram: use the [showcase form](.github/ISSUE_TEMPLATE/showcase.yml).
- Changes to generation, layout/routing, validation, interaction, performance, dependencies, tests, or other behavior require a related issue and explicit maintainer agreement on the problem, value, and intended scope before substantial implementation or a formal PR. Use the bug form for defects and the [improvement proposal](.github/ISSUE_TEMPLATE/improvement.yml) for changes. Link an existing issue or recorded maintainer decision when available; a second approval thread is unnecessary.
- Purely mechanical documentation corrections, such as typos or repairing a broken link to its intended destination, may go directly to a PR. Describe why the change is mechanical. Authoring instructions, new policy, behavioral documentation, and test changes are not exempt just because they are small or text-only.
- Security vulnerabilities: follow [SECURITY.md](SECURITY.md).

Agreement on direction allows implementation to proceed; final acceptance still depends on the implementation, user-visible results, and maintenance cost. Draft PRs may support early discussion but do not replace scope agreement.

Do not include secrets, access tokens, credentials, private repository content, personal data, or customer data in fixtures, logs, screenshots, artifacts, or package tests.

## Coordinate related work

These steps apply to contributors, maintainers, and Agents:

- Before implementing, search existing issues and open PRs for the same problem, including related fixes under review.
- On the relevant issue, state your intended scope. Link the agreed discussion in the PR; use a draft only when an implementation sketch helps that discussion. Apply the mechanical-correction exception above without a separate planning issue.
- If work is already in progress, discuss the remaining gap on that issue or PR and agree on collaboration, a distinct scope, or consolidation before starting an overlapping implementation.
- When consolidating, link both PRs, explain which contributions are retained, and preserve attribution through original commits or appropriate co-author credit. Close the superseded PR once the retained contribution and attribution are present in the continuing PR.

A scope comment signals active work, not permanent ownership. If work pauses or changes direction, leave an update; others can propose taking it forward in the same thread.

## Prepare a reviewable change

Start from the latest `dev` and target `dev` for fixes and features. Check whether its existing controls already solve the reported case. Record the comparison base and candidate head.

Use Draft for unresolved scope or early implementation feedback. At this stage, provide the smallest reproduction and relevant checks. Prepare broad integration evidence and generated artifacts once the approach is settled.

Before requesting final review, explain:

- The current-base trigger, intended outcome, and why the benefit justifies the implementation and ongoing maintenance cost.
- The changed behavior and shared callers, existing behavior that must remain stable, and any intended compatibility changes.
- The applicable checks, actual results, and reproducible evidence links.

Use [the PR template](.github/PULL_REQUEST_TEMPLATE.md); link existing receipts or CI output instead of transcribing long logs. Classify impact by behavior and callers, not file extension or diff size.

## AI assistance and contributor responsibility

AI-assisted contributions are welcome. The same scope, evidence, and accountability requirements apply to contributors and maintainers, whether work is manual or delegated to an Agent.

Every PR must disclose whether AI was used. If used, name the tool(s), model when known, and the work they performed: investigation, design, code, tests, review, or writing/translation. Identify affected areas rather than estimating a percentage of generated lines. If model identity is unavailable, say so. Translation-only use can be disclosed in one sentence.

A human contributor must review the submitted changes and explanation, understand the approach and its impact, and be able to explain the choices and answer review questions. Name that accountable person by GitHub handle when an Agent or bot submits on their behalf. Agents may prepare changes, run checks, and draft replies under that person's direction; they must not claim human review or check a personal confirmation without that person's explicit confirmation. Project-approved automated review comments remain advisory evidence, not human acceptance.

Describe the problem's origin honestly: observed usage, a reproducible defect found during inspection, a synthetic probe, or a proposed improvement. Code inspection can reveal valid bugs; do not present a constructed case as a naturally occurring Agent failure. AI-generated descriptions and replies must be checked for factual accuracy, kept concise, and reflect the contributor's understanding. Translation and editing assistance are allowed.

Link actual validation results in the existing Tests run / Visual evidence sections. Distinguish checks run by an Agent, CI, and human inspection; preserve failures and disclose untested areas. An AI review, a green test run, or a disclosure checkbox alone does not establish useful or correct behavior. Full sessions are required only where the agreed benchmark/evidence scope calls for them; do not upload unrelated private conversations or hidden model reasoning.

Maintainers may request missing disclosure or evidence, defer review, or close a PR that lacks agreed scope, cannot be explained by its contributor, or contains unverified claims. Give a specific reason and a route back through the relevant issue. Repeated submissions that ignore this feedback may be restricted. Evaluate observable conduct and evidence rather than guessing AI use from writing style or an automated detector. Do not bulk-close older PRs solely because they predate this disclosure field.

Policy references consulted on 2026-10-16: [Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md), [LLVM](https://llvm.org/docs/AIToolPolicy.html), and [Astral](https://github.com/astral-sh/.github/blob/main/AI_POLICY.md). Archify's requirements are defined here; other projects' restrictions do not apply automatically.

## PR improvement check

Before requesting final review of a behavior-changing PR, assess the changed
behavior, direct callers, and affected tests with the project Skills:

- [test-value](.agents/skills/test-value/SKILL.md): use its implementation or
  pre-commit review mode to decide which tests to add, adapt, reuse, or retire.
  Protect user outcomes and real failure boundaries at proportionate cost.
- [simplify-codebase](.agents/skills/simplify-codebase/SKILL.md): use Focused
  Survey mode when the diff introduces or touches duplicate logic/state, dead
  paths, redundant layers, or another concrete complexity concern. Trace the
  relevant consumers before recommending a cut.

Keep this check within the PR's changed ownership boundaries. A conclusion of
“no worthwhile improvement” is valid. Pure prose or generated-only refreshes
with no behavior change may skip it; authored Skill instructions and behavioral
build inputs still need assessment. Apply proved improvements within the task's
existing authorization. Report changes that would retire a supported capability
or compatibility contract for maintainer decision.

Summarize useful findings, implemented improvements, or the reason for skipping
in the PR's existing problem/impact and test sections. Reuse applicable evidence
under [Choose evidence by impact](#choose-evidence-by-impact); this check adds no
separate audit report or CI gate. Repository instructions govern scope and
publication authority. Treat the two vendored Skills as read-only guidance in
ordinary PRs; update their pinned sources through a dedicated reviewed change.
See [Skill sources](.agents/README.md) for provenance and update procedure.

## Choose evidence by impact

| Impact | Typical change | Evidence to prepare |
| --- | --- | --- |
| Text or review policy | Explanatory prose, links, contributor/reviewer procedure | Check content, links, and consistency with affected templates or automation. No local renderer suite for repository-only prose. |
| Local behavior | One CLI path, focused test correction | Reproduction or rationale, affected tests, and relevant failure/compatibility cases. |
| Shared behavior | Geometry, text measurement, shared Viewer, evidence or delivery helpers | Trace callers; identify affected modes and contracts; compare fixed representative inputs on base and candidate, including relevant historical failures. |
| Contract change | Schema, defaults, validation acceptance, Skill or authoring instructions | Agreed scope and explicit allowed/preserved behavior, plus local/shared evidence appropriate to the implementation. |

Skill instructions, authored examples, build inputs, and generated-site sources are behavioral inputs even when they look like documentation. Policy changes need process review; runtime evidence depends on whether they affect runtime inputs.

Start with `npm test` for the core product smoke or focused checks for the affected behavior. Use `npm run test:full` when shared infrastructure, broad changes, or findings require wider coverage. Final review needs sufficient evidence for the impact above; relevant CI results can supply that coverage without repeating the same run locally. Identify the revision and coverage of reused results, and explain material gaps. Required remote CI and branch protection still apply.

Tests should protect a user outcome or a real failure boundary. Prefer rendered
content, successful interaction, preserved authored intent, and bounded work to
matching implementation source or freezing automatic layout coordinates. A
better automatic route, clearer copy, or equivalent refactor should not fail a
test merely because it differs from the old implementation. Delete redundant
source assertions when a behavior test owns that protection. Keep explicit
geometry, compatibility, accessibility, failure cleanup, and protection against
lost or corrupted output as observable contracts.

### Real generation comparisons

For PRs that change diagram generation, select and link before/after evidence using the [real repository benchmark](benchmarks/real-repo-generation/README.md). Its initial rollout is an agreed three-PR pilot; record the selected scope or a justified exemption before running. Contributors supply the comparison and session records; maintainers review outcomes and sample evidence. Synthetic error injection alone does not establish real Agent benefit. Reuse unaffected evidence at its recorded revision.

### CI by affected responsibility

CI uses the ownership groups in `scripts/ci-scope.mjs`. Product changes run core
CLI coverage on the maintained Node versions and the affected regression suites.
Renderer and Viewer changes also run the real browser gate and generated-output
checks. Filesystem, process, dependency, build, and workflow changes retain the
full regression and relevant Windows/package gates. New or modified test files
are executed; test helpers and fixtures take the conservative full path.
Repository prose and website-only changes use their own checks.

Unknown paths, an empty comparison, and an unavailable development-push base
select full coverage. An invalid PR comparison fails classification. Required
job names remain present, and a failed classification cannot turn into successful
skips. Main pushes and manual CI runs use complete coverage; releases explicitly
run `test:full`. New pushes cancel obsolete CI runs for the same PR.

## Product and compatibility contracts

- Existing schema-v1 typed JSON remains valid unless a reviewed change explicitly introduces a breaking rule and migration path.
- Preserve authored topology and intent; explicit geometry remains authoritative unless the contract says otherwise. Consult the [authoring contract](archify/references/authoring-contract.md) and relevant renderer documentation for details.
- `standard` preserves broad compatibility. A new `showcase` failure must identify a real, repairable defect and avoid rejecting necessary routing.
- Agent-facing failures belong in `diagnostics[]`: use a stable `code`, precise `subject`, concrete `evidence`, and executable `supportedFixes`. Preserve non-zero CLI exits and machine-readable receipts for failed stages.
- A validation rule expressing taste should begin with evidence or a warning. Before making it a hard error, check legitimate obstacles, shared ports, explicit routes, nested boundaries, and existing examples.
- Keep one canonical contract per behavior. Link the existing source instead of copying CLI stages, receipt fields, or error tables.

## Local setup and verification

The renderer package is in `archify/`; repository tests and their dependencies live at the root. Install both dependency sets before running tests. The supported Node range is defined in both package manifests.

```sh
npm ci
npm --prefix archify ci
npm test
npm run test:focus -- test/geometry.test.mjs
```

For the development loop, select the files covering the changed behavior with
`npm run test:focus -- test/<name>.test.mjs [test/<other>.test.mjs ...]`.
This runs only those suites, without the generated-output checks or golden pass.
It requires at least one file and rejects unknown files rather than silently
running the full suite. Paths are relative to the repository root; absolute
paths also work. Use `--list` with the same selection to inspect it without
running tests. A focused pass is evidence for that selection only.

To narrow a large file further, add a quoted Node test-name pattern (Node 18.11+):

```sh
npm run test:focus -- test/cli.test.mjs '--test-name-pattern=cli: validate'
```

Nested tests follow Node's filtering rules: include their parent test names in
the pattern as well. Check the reported pass/skip counts for the intended cases.

| Command | What it establishes |
| --- | --- |
| `npm test` / `npm run test:core` | Ten diagram types run through the public CLI, frozen v1 inputs remain usable, delivery receipts bind the actual files, and failed delivery preserves the previous artifact. No browser or perceptual acceptance is implied. |
| `npm run test:focus -- test/<name>.test.mjs` | Only the selected behavior or regression. |
| `npm run test:generated` | Viewer, brand marks, validators, release identity, and checked-in examples match their authoritative sources. Freshness does not establish visual quality. |
| `npm run test:full` | Generated checks followed by every discovered Node test file, including the detailed process, filesystem, installation, and failure matrices. |

The Node 18, 20, and 24 compatibility lanes run the same core product smoke via
`test:compat`. Detailed fault-injection matrices run on canonical Node 22 when
their responsibility is affected and in complete verification. The separate
browser, WebM, Windows, and package gates retain their distinct claims. Do not
repeat an unchanged complete run locally just because CI is also running it.

For full CI, Node 22 runs every discovered test file across two independent
machines using `node scripts/run-tests.mjs --shard=1/2` and `--shard=2/2`.
One shard also runs generated checks and the Hermes adapter contract once,
using the same installed dependencies. The existing `test (22)` check requires
both shards to succeed without reinstalling dependencies afterward. Other scopes do not
start these shards. Node 18, 20 and 24 compatibility checks start after scope
classification, without waiting for the complete regression shards.
`--list --shard=1/2` shows the selected files; shards cannot
be combined with explicit files or test-name filtering. Locally and in tagged
releases, `npm run test:full` still runs the complete inventory without sharding.

The Windows Node 22 lane owns the complete filesystem and fault-injection
matrices. Node 24 runs the core CLI smoke instead of repeating those matrices.
Both lanes, including tagged releases, still run the controlled case-sensitive
NTFS, UNC, extended-path, and 8.3-path scenarios. Use
`node scripts/run-windows-path-tests.mjs --list` (or `--smoke --list`) to inspect
the selected groups without running tests or creating Windows fixtures.

The test runners accept `--concurrency=N` to tune the number of simultaneous
test files on Node 18.19+, for example `npm run test:focus -- test/geometry.test.mjs --concurrency=4`. Headless
repository and compatibility runs default to the available CPU count, capped
at 4. Setting `ARCHIFY_CHROME` or running `test:browser` keeps the default at 2.
Older Node versions that lack this concurrency option retain Node's default.
Compare timing and results on the same machine before increasing concurrency;
browser tests can become slower or unstable under CPU contention.

Test through public behavior such as `render`, `validate`, `deliver`, `visual-check`, or final SVG/HTML. Behavioral fixes should include a regression that demonstrates the original failure. Private helper checks can supplement that evidence.

For geometry and layout changes, use the smallest redacted JSON reproduction, relevant checked-in examples, and frozen compatibility fixtures. Compare base and candidate with the same input and browser conditions. Identify intended changes and investigate unexpected ones; updating golden files alone does not establish visual or compatibility acceptance.

A visual PR must provide enough evidence to evaluate whether the intended user value was achieved, using screenshots, recordings, or reproducible steps. Keep viewport, theme, preset, diagram mode, zoom, and page state comparable. Report automated or browser evidence separately from perceptual review. Non-visual changes may omit the Visual evidence section.

Static SVG/XML checks cannot establish browser layout, font settling, or interaction behavior. When the adaptive reader or Viewer layout changes, run the real browser test from the repository root with Chrome available:

In a POSIX shell:

```sh
ARCHIFY_CHROME="/path/to/chrome" npm run test:browser -- test/desktop-reader-browser.test.mjs
```

In Windows PowerShell:

```powershell
$env:ARCHIFY_CHROME = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
npm run test:browser -- test/desktop-reader-browser.test.mjs
```

Replace the example Chrome path with your installed executable's path. In
PowerShell, the environment variable remains set for the current session.

A browser test skipped because Chrome was unavailable is **skipped**, not passed. Follow [the delivery contract](archify/references/delivery-contract.md) for visual evidence, receipts, and failure stages. Successful validation, atomic delivery, browser checks, and perceptual review establish different claims.

PR CI and tag releases run the same browser regression gate:

```sh
ARCHIFY_CHROME="/path/to/chrome" npm run test:browser
```

This command requires a usable Chrome/Chromium and fails when none is available.
Its maintained file list is in `scripts/browser-test-inventory.mjs`; add new browser
suites there so both workflows keep the same coverage. `npm run test:full`
retains optional browser skips. Real WebM decoding and site-language integration
remain in the separate `npm run test:webm` gate used by both workflows.

PR CI divides the maintained browser inventory into two disjoint file shards
with `npm run test:browser -- --shard=1/2` and `--shard=2/2`. Both run alongside
the independent WebM gate; the required `webm-artifact` check succeeds only
after both browser shards, WebM, and scope checks succeed. Tag releases and an
unqualified `npm run test:browser` still run the complete browser inventory.
`--list --shard=1/2` lists a shard without requiring Chrome. Shards cannot be
combined with explicit files or test-name filtering; every maintained file runs
in exactly one shard, and every executing shard still requires Chrome.

Only set `ARCHIFY_CHROME` for the browser run when you also plan to run the full
browser gate: many browser suites are included in `test:full` and would otherwise
execute again. The canonical regression suite, Node compatibility matrix, and
required browser gate establish their respective coverage. Reuse the applicable
final-head CI results instead of repeating an unchanged full suite locally.

## Packages and generated artifacts

Viewer maintenance starts in [`viewer/`](viewer/README.md). Edit its source
files, then run `npm run generate:viewer` from `archify/`; the delivered template
is generated and its freshness is checked by `npm run test:generated` (also part
of `test:full`).

Published artifacts must be reproducible from tracked content. Use a tracked-only, symlink-safe staging path or explicit allowlist, with negative coverage for untracked files and external symlinks. Test the extracted package outside the repository on the affected advertised hosts.

Review source and focused tests before regenerating artifacts. Regenerate only outputs whose authoritative inputs changed, from the final combined source:

```sh
node scripts/build-gallery.mjs docs
node scripts/build-guide.mjs docs/guide.html
node scripts/build-start.mjs docs/start.html
node scripts/build-readme-showcase.mjs
scripts/build-zip.sh /tmp/archify-contrib.zip
```

Canonical ZIP bytes require official Node 22 with bundled zlib `1.3.1-e00f703` (for example, the official Node 22.23.2 distribution). The builder rejects other Node majors and zlib versions before staging or replacing an archive. A distribution linked against system zlib can produce different bytes even at the same Node version; check the actual executable with `node -p 'JSON.stringify({ executable: process.execPath, node: process.versions.node, zlib: process.versions.zlib })'`. This packaging constraint does not change the Skill runtime's supported Node range. When updating the canonical toolchain, review archive reproducibility and the committed ZIP together.

Skill runtime, schema, renderer, and published Skill-instruction changes require checking ZIP freshness. Bundled example or Viewer changes normally require a Gallery rebuild.

List regenerated files and explain freshness when an affected output is left unchanged. Changes that do not affect generated outputs may omit that PR section. Resolve generated conflicts by rebuilding from combined source. Keep unrelated generated output out of the diff.

Treat published versions as immutable. Ordinary feature PRs do not change versions, tags, or distribution identities unless release work is explicitly in scope.

## Release checklist

Use this single checklist in the release PR or its linked release record. Link evidence at each stage; mark an item complete only when its stated outcome is verified, or record an explicit deferral with an owner, reason, and follow-up. PR completion, release publication, Pages deployment, and updates to live installations are separate outcomes. Existing gates in [CI](.github/workflows/ci.yml) and the [release workflow](.github/workflows/release.yml) already cover release identity, ZIP freshness, installation parser/real Skills CLI tests, three-platform package smoke, browser checks, and the published manifest's actual Release ZIP. Reuse those gates and their receipts rather than creating another release pipeline.

1. [ ] **Scope and revision.** Record the intended version/channel, release scope, final source SHA, comparison base, release notes, known issues, and required integration follow-ups. Follow the `dev` trial-use → `main` promotion process below. Pin evidence to its tested SHA; refresh the record when the candidate changes.
2. [ ] **Identity and build.** Verify package/Skill identity and generated outputs using the candidate revision's existing checks. Use the canonical Node/zlib toolchain above for `scripts/build-zip.sh`; confirm the committed `archify.zip` matches the clean tracked-source build. Do not change versions or regenerate unrelated artifacts in ordinary feature PRs. Preserve the previous stable manifest until the new stable Release exists.
3. [ ] **Final-head validation.** Account for the latest target base and verify required CI at the final candidate: identity and ZIP gates, schema/renderer tests, installation parser and real Skills CLI discovery, package smoke on Linux/macOS/Windows, browser/WebM checks, and affected website checks. Record run URLs, SHA, real-use evidence, and any skipped or unavailable checks; an earlier green head or zero checks is not final acceptance. Use commands from that revision's manifests/workflows: current `dev` installs root and renderer dependencies and runs `npm run test:full`, `npm run test:browser`, and `npm run test:webm` at the repository root (see [Local setup](#local-setup-and-verification)); older `main`/release revisions may run these from `archify/`. Website commands run in `website/`. Do not transplant a command or its working directory across revisions without checking.
4. [ ] **Authorized publication.** Confirm authorization for the exact release version/channel and source SHA before pushing a release tag. Stable `v<version>` tags must be annotated and resolve to the verified commit; the workflow checks tag/package identity and the release channel. Verify the resulting GitHub Release and its `archify.zip` asset, digest, and expected stable/prerelease status. Do not overwrite existing versions, tags, or assets to repair a release. Installing or updating a user's live installation requires its own authorization.
5. [ ] **Manifest, website, and integrations.** After the stable Release exists, publish `docs/skill-updates/archify/stable.json` in a follow-up commit through the normal branch process. Retain the `published-update-manifest` result that compares the actual Release ZIP, tagged archive, digest, and tagged Skill tree; wait for the gated `main` Pages deployment. Development/prerelease tags do not advance the stable notifier. Complete the [DSH synchronization checklist](#release-checklist-dsh-synchronization) or record an explicit deferral. Evaluate other integrations by their actual distribution mechanism: [Hermes](integrations/hermes-agent/README.md#install-shows-up-in-available-skills) installs the main Skill identifier; do not invent a separate Hermes release simply because Archify changed. Record any documentation/compatibility update or indexing lag that needs follow-up.
6. [ ] **Public acceptance and closure.** Check the public download and advertised installation/discovery paths against the released artifact in an isolated environment, without changing live user installations. Verify the public stable manifest, Pages version, installation instructions, and community catalog source/evidence/compatibility links describe what users can actually obtain; distinguish published, pending, and explicitly deferred integration versions. Record the final release/tag/SHA, asset digest, CI and deployment receipts, public acceptance result, and every remaining owner/follow-up. Only describe each channel as complete after its own verification.

### Release checklist: DSH synchronization

For every Archify release, record the DSH decision in the release PR or its linked follow-up. The Skill source is pinned: releasing Archify or updating `main` does not update the DSH package or existing installations. Use the [DSH release maintenance procedure](integrations/deepseek-harness/README.md#release-maintenance) for commands and host requirements.

- [ ] Assess whether the release needs a DSH update. Record the selected Archify source/version and plugin version, or an explicit deferral with its reason and follow-up. The plugin has its own version sequence; it need not match Archify's version.
- [ ] For a host-version change or compatibility report, complete the [host migration review](integrations/deepseek-harness/README.md#host-migration-review): pin official source tags/commits and registry identities, inventory the adapter's actual API/configuration touchpoints, and check the target host's compatibility checker (including prerelease semantics). Record applicable changes and gaps in any community reference; a heuristic scan or an accepted peer range is not support evidence. Do not widen peers or add exemptions merely to make installation pass.
- [ ] If syncing, update `integrations/deepseek-harness/release.json` to a full immutable `sourceCommit` and matching `skillVersion`; retain or deliberately update the exact tested DSH host version. Check both `archify/package.json` and `archify/skill-release.json` at that source. Identify any fixes included after the Archify version tag.
- [ ] Commit the adapter inputs before packing. Inspect the actual `.tgz`, including `release.json`, the bundled Skill version/content, license notices, and dependency exclusions; run the package contracts and real distribution acceptance (isolated install, discovery/load, installed Skill smoke, and uninstall). Before plugin publication, complete the DSH workflow's three-platform adapter release gate on the candidate commit and retain its receipts.
- [ ] Record a support-evid
```


## Top-level structure
```
dir	.agents	.agents
file	.coderabbit.yaml	.coderabbit.yaml
file	.gitattributes	.gitattributes
dir	.github	.github
file	.gitignore	.gitignore
file	AGENTS.md	AGENTS.md
file	CHANGELOG.md	CHANGELOG.md
file	CLAUDE.md	CLAUDE.md
file	CONTRIBUTING.md	CONTRIBUTING.md
file	DESIGN.md	DESIGN.md
file	LICENSE	LICENSE
file	PRODUCT.md	PRODUCT.md
file	README.md	README.md
file	README_EN.md	README_EN.md
file	README_JA.md	README_JA.md
file	README_KO.md	README_KO.md
file	README_ZH.md	README_ZH.md
file	REVIEWING.md	REVIEWING.md
file	ROADMAP.md	ROADMAP.md
file	SECURITY.md	SECURITY.md
file	THIRD_PARTY_NOTICES.md	THIRD_PARTY_NOTICES.md
file	archify.zip	archify.zip
dir	archify	archify
dir	benchmarks	benchmarks
dir	community	community
dir	docs	docs
dir	examples	examples
dir	experiments	experiments
dir	integrations	integrations
dir	journal	journal
file	package-lock.json	package-lock.json
file	package.json	package.json
dir	scripts	scripts
dir	test	test
dir	tools	tools
dir	viewer	viewer
dir	website	website
```
