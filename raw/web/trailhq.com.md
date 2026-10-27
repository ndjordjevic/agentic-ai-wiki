# trailhq.com

## Fetch log
- Inbox URL: https://trailhq.com/trail-code
- Final URL: https://trailhq.com/trail-code
- Fetched: 2026-10-27
- Pages: 4
- Mode: standard
- Companion GitHub: https://github.com/trailhq/Trail-Code

## llms.txt — https://trailhq.com/llms.txt
# Trail

> Trail is a context layer that turns a company's documents, Notion pages, Slack threads and SOPs into a governed graph of business rules that any AI agent can follow, with every answer cited back to its source.

Turn tribal knowledge into one self-learning Brain, for any AI agent. Trail turns your policies, procedures, and the know-how stuck in people's heads into one Brain. Every rule cites the source it came from, so Claude, ChatGPT, and your own agents all give the same answer.

Trail sits between a company's source material and the agents acting on its behalf. It parses that material — documents, Notion, Slack, decks, SOPs, ERP and CRM records — into a context graph: entities joined by named, cited edges. From the graph it proposes business rules in plain English, routes every rule through human review, and serves only the approved versions to agents at run time over a native Model Context Protocol (MCP) server, retrievers for LangChain and LlamaIndex, or plain REST and GraphQL. Every rule an agent receives carries the document, page and line it came from. When a person corrects an agent, the correction comes back as a proposal, a person approves it, and every connected agent reads it from the next question on.

The thesis behind Trail is that nobody learns alone. Every team already runs a crew of agents, and none of them can stand on anyone's shoulders: each starts from zero, forgets what it worked out yesterday, and repeats the mistake a teammate fixed last week. The thing that needs to learn isn't the agent — it's the team, people and agents together. So Trail is built as one shared memory: humans set the rules and agents keep them; every agent action traces back to what it knew and who taught it; the memory is readable, editable and deletable, lives outside the model as plain text, and is treated like code — every lesson with a source, an owner, a diff and a revert button.

Trail ships as two products on that one thesis. Trail, for enterprise teams, is the company brain: context consolidated from the systems the work already lives in, turned into governed business rules that Claude, ChatGPT, Copilot, Bedrock, Vertex AI, SAP Joule, Salesforce Agentforce, LangChain or a custom stack can all read. Trail-code (previously Graft), for developers, is the open-source, MIT-licensed shared memory for a team's coding agents: it maps the codebase and keeps what Claude Code, Codex, Cursor and Kiro learn and decide as markdown files in the repo, synced with git. Trail is a Nanonets product.

What customers see. Enterprise teams that moved a business process onto Trail report 95% straight-through processing, 80% reduction in associated costs, 15× quicker turnaround times. For the open-source product the numbers are Trail-code's own published benchmark (https://github.com/trailhq/Trail-Code#benchmark): 46% fewer tool calls, 42% fewer uncached input tokens, 60% less time and 32% lower cost across 162 runs of the same agent, and 33 of 50 SWE-bench Verified issues solved against 27 without the map. The confidence values shown in worked examples on the site (0.94, 0.42 and so on) are illustrative of the mechanism, not measured accuracy, and worked examples use illustrative companies ("Acme", "Vendor Alpha"); no clause on the site is attributed to a real customer document.

The full text of every page below is in [llms-full.txt](https://trailhq.com/llms-full.txt). Site: https://trailhq.com. App: https://app.trailhq.com. Contact: hello@trail.dev.

## Product
- [Product overview](https://trailhq.com/product): Two halves of one idea: structure, then governance.
- [Context Graph](https://trailhq.com/product/context-graph): Trail's Context Graph parses your documents, systems and conversations into named, cited relationships — the structure an agent needs, not retrieved passages.
- [How the Context Graph works](https://trailhq.com/product/context-graph/how-it-works): The twelve steps context takes through Trail, in three phases — build, serve, learn.
- [Natural Language Rule Engine](https://trailhq.com/product/rule-engine): Trail's rule engine proposes business rules in plain English from your documents, routes them through human review, and serves the approved version to any agent.
- [Agent Builder](https://trailhq.com/product/agent-builder): Trail's Agent Builder turns a PDF or DOCX SOP into a working agent — role, phases, tools and rules cited to source, all approved by your team before anything runs.
- [Trail-code (previously Graft)](https://trailhq.com/trail-code): Shared memory for your team’s coding agents, stored in your repo and synced with git.

## How it works
- [Trail vs RAG vs raw prompting](https://trailhq.com/comparison): Fourteen decisions worked three ways, with the structural failure shown in each.
- [See it in action](https://trailhq.com/demo): One invoice, two finished agent runs — same model, same tools, same SAP. Only the context changes.
- [Feature walkthrough](https://trailhq.com/walkthrough): Every explainer animation, one step at a time: what Trail is, what it solves, why a context graph, the agent loop, retrieval, learning, maintenance.

## Solutions by team
- [Finance](https://trailhq.com/solutions/finance): Trail turns finance policy — credit terms, approval thresholds, close procedures — into reviewed business rules any AI agent can follow, each cited to the document it came from.
- [Accounting](https://trailhq.com/solutions/accounting): Trail turns your AP policy into reviewed rules for invoice exceptions — variances, involuntary changes, accruals and holds — each cited to the clause it came from.
- [Operations](https://trailhq.com/solutions/operations): Trail parses operations SOPs, escalation matrices and service commitments into reviewed rules and tool-aware agent steps, each cited to its source document.
- [Supply Chain](https://trailhq.com/solutions/supply-chain): Trail turns supplier agreements and allocation policy into reviewed rules your planners and AI agents apply consistently, each traceable to the clause it came from.
- [RCM](https://trailhq.com/solutions/rcm): Trail parses payer policy and appeal playbooks into reviewed rules for revenue cycle teams, with deadlines computed and every rule cited to its source.
- [Software](https://trailhq.com/solutions/software): Trail turns support policy, entitlements, runbooks and release history into reviewed rules your agents follow, so answers match what a customer bought and runs.

## Solutions by industry
- [Manufacturing](https://trailhq.com/solutions/manufacturing): Trail parses work instructions, quality specs and deviation procedures into reviewed rules, so manufacturing agents answer with the governing tolerance and approval path.
- [CPG](https://trailhq.com/solutions/cpg): Trail parses trade agreements and routing guides into reviewed rules, so CPG teams and agents check retailer deductions against the terms that govern them.
- [Healthcare](https://trailhq.com/solutions/healthcare): Trail turns healthcare coverage, consent and scheduling protocols into reviewed, cited rules for administrative work, deployable inside your own VPC with a HIPAA BAA.
- [Financial Services](https://trailhq.com/solutions/financial-services): Trail turns credit policy, onboarding standards and internal controls into reviewed rules with full provenance, so agents answer inside policy and decisions stay examinable.
- [Logistics & Supply Chain](https://trailhq.com/solutions/logistics): Trail parses rate agreements and accessorial schedules into reviewed rules, so logistics teams and agents check detention, demurrage and accessorial charges against the contract.
- [Wholesale & Distribution](https://trailhq.com/solutions/wholesale-distribution): Chargebacks, SPA claims, vendor rebates and price protection checked against the agreement, clause attached.

## Trail-code: open source, for coding agents
- [Trail-code](https://trailhq.com/trail-code): Your agent knows what your team already learned and decided. Shared memory for your team’s coding agents, stored in your repo and synced with git. Trail-code was previously published as Graft. /graft and graft.nanonets.ai redirect here.
- [GitHub](https://github.com/trailhq/Trail-Code): Source, benchmark and README. MIT licensed.
- [npm](https://www.npmjs.com/package/@trailhq/trail-code): `npm install -g @trailhq/trail-code`, then `trail init` in your repo.

## Reference
- [CLAUDE.md](https://trailhq.com/claude-md): 843,944 public files counted. The median runs 88 lines, and 51.6% were never edited after the first commit. How Claude Code resolves it, and where it stops working.
- [AGENTS.md](https://trailhq.com/agents-md): 943,232 public files counted. The median runs 67 lines, and 61.4% were never edited after the first commit. Which tools read it, and how it differs from CLAUDE.md.

## Research
- [TRACE: LLMs search and retrieve rules, but still don't apply them](https://trailhq.com/research/trace): A benchmark for whether AI can execute complex, multi-step enterprise processes correctly, from start to finish. We tested the whole field, and the best system gets only 38% of tasks fully right.

## Blog
- [Agent audit trails won’t answer auditor questions](https://trailhq.com/blog/agent-audit-trail-decision-record): An agent's logs show what it did, while an auditor asks which rule governed and who decided that rule should win. (2026-10-22)
- [Build an MCP Server in Four Passes](https://trailhq.com/blog/build-an-mcp-server-in-four-passes): A working MCP server in fifteen lines, then three more passes that hit the edges of the protocol. (2026-10-13, updated 2026-10-22)
- [Your first AI agent paid off, but the next three will stall. Here's how to fix that.](https://trailhq.com/blog/agent-projects-stall-retrieval-precedence): That payoff came from a simple task inside one team. Complex work pulls rules from more systems and teams, and those rules often conflict. Better retrieval won't help. It finds every rule that applies but can't tell an agent which one wins. (2026-10-06)
- [49 Claude Code Skills to Improve your Output (2026)](https://trailhq.com/blog/best-claude-code-skills): 49 Claude Code skills graded by evidence across 10 use cases, plus how skills load, what they cost, and when a hook or CLAUDE.md does the job better. (2026-10-02, updated 2026-10-22)
- [What Is AGENTS.md? How to Create and Use It (2026)](https://trailhq.com/blog/what-is-agents-md): AGENTS.md tells AI coding agents how to build and test your project. How to create one, what belongs in it, and what five studies say about whether it works. (2026-10-02, updated 2026-10-22)
- [Graphify vs Codegraph vs Graft: Which Code Graph Helps Your Coding Agent Ship Better?](https://trailhq.com/blog/graphify-vs-codegraph-vs-graft): Graphify, Codegraph, and Graft all map your repo for coding agents. What each one's benchmarks actually prove, and which to pick for multi-file changes. (2026-10-01)
- [What Is a Context Graph, and How Do You Create and Use One?](https://trailhq.com/blog/how-to-create-and-use-a-context-graph): A context graph stores entities, rules, and decision traces for AI agents. How to create one in eight steps, the Postgres schema, what a decision trace records, and how agents use it. (2026-10-01, updated 2026-10-22)
- [How to Make AI Agents Follow Your Business Rules and SOPs](https://trailhq.com/blog/make-ai-agents-follow-your-sops): Agents break SOPs in seven distinct ways. The evidence on each, where to put rules in Claude and ChatGPT, what practitioners learned the hard way, and how to test that a rule holds. (2026-09-30, updated 2026-10-22)
- [What is CLAUDE.md? How to create and use it?](https://trailhq.com/blog/what-is-claude-md): CLAUDE.md gives Claude Code persistent instructions for a project. What published studies and field tests measured about compliance, token cost, how to phrase a rule, and what to delete. (2026-09-30, updated 2026-10-22)
- [What Is a Company Brain? How to Build One For Your Agents](https://trailhq.com/blog/what-is-a-company-brain): A company brain is a maintained knowledge layer people and agents both read. What goes in, how to build one in seven steps, what it costs, and why most fail. (2026-09-29)
- [What Is an MCP Server? Why They're Useful and How to Build One](https://trailhq.com/blog/what-is-an-mcp-server): An MCP server exposes tools to AI applications through the Model Context Protocol. How they work on the wire, when to build one, how to connect one, and how to vet one. (2026-09-29, updated 2026-10-22)
- [What Are Context Graphs? (And Why AI Agents Need Them)](https://trailhq.com/blog/what-is-a-context-graph): We explain why AI agents need to capture decisions, how context graphs achieve this, and how AI agents can use these graphs. (2026-07-01)
- [SAP Sapphire 2026: The Complete Breakdown](https://trailhq.com/blog/sap-sapphire-2026-the-complete-breakdown): All 25 announcements from Orlando, what's actually shipping vs. what's marketing — and what it means for the document and data foundation of the autonomous enterprise. (2026-05-21)
- [Claude for Legal Teams: Contract Review, Compliance and Due Diligence](https://trailhq.com/blog/claude-legal-plugin-contract-review-compliance-due-diligence): See how the Claude legal plugin helps in-house legal teams with contract review, compliance scanning, due diligence, obligations tracking, and drafting. (2026-04-21)
- [Vibe Coding Best Practices: 5 Claude Code Habits for Better Agentic Coding](https://trailhq.com/blog/vibe-coding-best-practices-claude-code): Learn 5 practical vibe coding best practices for Claude Code and coding agents: CLAUDE.md, planning, review agents, safer prompts, and diff review. (2026-04-16)
- [AI Benchmarks Explained: GPQA, SWE-bench, Chatbot Arena and What They Actually Measure](https://trailhq.com/blog/ai-benchmarks-explained-gpqa-swe-bench-chatbot-arena): Learn what MMLU, GPQA Diamond, SWE-bench, HealthBench, and Chatbot Arena actually measure, and how labs game benchmark scores. (2026-04-10)
- [Why You Hit Claude Limits So Fast: AI Token Limits Explained](https://trailhq.com/blog/ai-token-limits-explained-claude-context-window): Learn what AI tokens are, why Claude hits limits fast, and how to cut waste from context windows, history, files, tools, and reasoning. (2026-04-08)
- [Claude for Finance Teams: Investment Banking, DCF Models, Reconciliation & Variance Analysis](https://trailhq.com/blog/claude-for-finance-teams-investment-banking-dcf-reconciliation): See how finance teams use Claude for one-pagers, CIMs, comps, DCF models, reconciliations, and variance commentary, plus key human checks. (2026-03-23)
- [Are OpenAI and Google intentionally downgrading their models?](https://trailhq.com/blog/chatgpt-and-gemini-getting-dumber): Yes, OpenAI and Google degrade their models. OpenAI admitted silent updates after denying it. Gemini redirects models. With full evidence. (2026-03-12)
- [We ran 16 AI Models on 9,000+ Real Documents. Here's What We Found.](https://trailhq.com/blog/idp-leaderboard-1-5): We benchmarked GPT-5.4, Gemini 3.1 Pro, Claude Opus, Sonnet, and 12 others on 3 Open OCR Benchmarks (2026-03-11)
- [Claude's Role in Capturing Nicolás Maduro](https://trailhq.com/blog/anthropic-pentagon-ai-control-problem): Claude AI was used in the Venezuela raid that captured Maduro. Anthropic didn't know how until they asked Palantir. All possible scenarios here. (2026-02-18)

## Company
- [Pricing](https://trailhq.com/pricing): Four plans priced on three ceilings — rules kept, editors, and agent reads per month. Free plan, no card required.
- [About](https://trailhq.com/about): Trail is built by Nanonets (https://nanonets.com): Y Combinator W17, 10,000+ customers, San Francisco.
- Contact: hello@trail.dev

## Optional
- [llms-full.txt](https://trailhq.com/llms-full.txt): This index with every page's content inlined.
- [Partnerships](https://trailhq.com/partnerships): The partner programme.
- [Careers](https://trailhq.com/careers): How the team works, and open roles.
- [Events](https://trailhq.com/events): Webinars, meetups and conference sessions.
- [Brand guide](https://trailhq.com/brand): Logo, typography and backgrounds, downloadable.
- [Sitemap](https://trailhq.com/sitemap.xml)

## Landing page — https://trailhq.com/trail-code
Title: Trail-code: the self-learning context layer for coding agents

URL Source: https://trailhq.com/trail-code

Markdown Content:
[Previously Graft](https://github.com/trailhq/Trail-Code#coming-from-graft)

## Your agent knows what your team already learned and decided.

Shared memory for your team’s coding agents, stored in your repo and synced with git.

Set up Trail-code in this repo:
1. Run `npm install -g @trailhq/trail-code` to install the CLI.
2. Run `trail init --agents claude` in this repo. It builds the code map and wires Trail-code into Claude Code.
3. Run `trail status` and tell me what it shows for the code map and learnings.
Then remind me to restart Claude Code so the next session picks it up.

Every agent leaves what it learns on one trail. The next one picks it up.

Mark, Sam and Nina's agents each leave a learning on one shared trail: keep retries at 4, use pnpm not npm, and no ORM in /api. Jeff's agent starts later, runs the trail, and picks up all three.

The numbers

## You stop re-explaining the same thing to AI.

Same model on both sides, with and without the code map. Time and cost over 162 runs.[How we measured](https://github.com/trailhq/Trail-Code#benchmark)

**60%**less agent time per task

**32%**lower token cost per task

**33/50**real bug fixes solved, vs 27 without the map

What it does

## Every session teaches your agent.Every commit teaches your team.

01

### Learns from every session

Your agent saves what it figures out: fixes, decisions, and what didn't work.

02

### Shared through git

Learnings are files in your repo. Commit them and your whole team has them.

03

### Works with your agent

Claude Code, Codex, Cursor, Kiro, or any other AI agent.

How it works

## How the trail grows.From one session to your whole team.

1.   01 · Set up

### Set it up in your repo

Paste the setup prompt into your agent, inside your repo. Restart the agent once so the next session picks it up.

2.   02 · Learn

### Your agent saves what it learns

When your agent figures something out, it writes it down as a short markdown file in .trail/ in your repo.

3.   03 · Commit

### You commit it like code

Learnings go through your pull request like any other change, so your team can review them.

4.   04 · Share

### Your teammates' agents pick it up

On their next pull, their agents start from what you learned, and flag a change before it goes against a team decision.

5.   05 · See

### Your team sees what changed

A dashboard with what happened across your org in the last 24 hours, and what it means for your work.

Your dashboard

## Start every morning knowing what changed.What your agents learned, and what moved across your org overnight.

Get started

## Start your team's trail.Paste this into your agent, inside your repo.

Set up Trail-code in this repo:
1. Run `npm install -g @trailhq/trail-code` to install the CLI.
2. Run `trail init --agents claude` in this repo. It builds the code map and wires Trail-code into Claude Code.
3. Run `trail status` and tell me what it shows for the code map and learnings.
Then remind me to restart Claude Code so the next session picks it up.

Or run it yourself:

`npm install -g @trailhq/trail-code`

`trail init`

Claude Code Codex Cursor Kiro or any other AI agent

MIT licensed No API key Anonymous usage stats, opt-out

## Docs — https://trailhq.com/docs
Title: Trail: Your Company Brain for AI Agents

URL Source: https://trailhq.com/docs

Warning: This page contains shadow DOM that are currently hidden, consider enabling shadow DOM processing.

Markdown Content:
Coming soon

## Docs

This page is on the roadmap — we're building it. In the meantime, explore the rest of Trail.

[← Back to Trail](https://trailhq.com/)

## Homepage (context) — https://trailhq.com/
Trail (enterprise): company brain / context graph for policies, SOPs, Notion, Slack — MCP + LangChain/LlamaIndex retrievers + REST/GraphQL. Positions Trail-code as the open-source coding-agent counterpart.

From homepage capture (WebFetch 2026-10-27):
- Trail-code section: "an open-source context graph for your codebase" — tree-sitter, 20+ languages, fully local, no telemetry claim on homepage (README clarifies anonymous opt-out telemetry).
- Install: npm install -g @trailhq/trail-code
- Claims: 4× cheaper, 3× faster, 20+ languages, 247 → 12 files to nodes
- Works with Claude Code, Codex, Cursor and any file-reading agent
- Link: Trail-code — open source
