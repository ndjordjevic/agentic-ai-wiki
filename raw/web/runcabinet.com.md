# runcabinet.com

## Fetch log
- Inbox URL: https://runcabinet.com/
- Final URL: https://runcabinet.com/
- Fetched: 2026-04-29
- Pages: 2
- Mode: deep
- Products discovered: 0

## Discovery audit

- Candidates from llms.txt (depth 1/2/3): None — https://runcabinet.com/llms.txt returned 404
- Candidates from landing page: Cabinet (single product, hero + nav confirm one product), /media (press/community page — excluded)
- Candidates from sitemap.xml: None — https://runcabinet.com/sitemap.xml returned 404
- Candidates from GitHub URLs: github.com/hilash/cabinet (single repo-root URL)

- Classified as products: Cabinet — single product, confirmed by hero section, nav structure, and sole repo URL. len(products) = 1 < 2 → single-product deep mode; products = []
- Classified as excluded: /media (press/community content, not a product), #features/#karpathy/#compare/#agents/#get-started (same-page anchor sections), discord.gg/... (community link), runcabinet.com/waitlist (waitlist form — not a product)
- Classified as sub-section of existing product: n/a — only one product found

## Landing page — https://runcabinet.com/

free project · open source · self-hosted

/ˈkab.ɪ.nət/

noun

1. A cupboard with shelves or drawers for storing or displaying items.
   "a filing cabinet"

2. (politics) The committee of senior ministers responsible for controlling government policy.
   "a cabinet meeting"

3. (software) An AI-first knowledge base where files live on disk and a team of AI agents helps you execute.
   "I asked my cabinet to research the market and draft the blog post"

origin — mid 16th century: from cabinet, diminutive of Old French cabine.
definition 3 — 2026, open source.

Install: $npx cabinetai run

## Your knowledge base. Your AI team.

A free and open-source AI-first startup OS where everything lives as markdown files on disk. No database. No vendor lock-in.

No subscription. No trial. No paywall. Clone it, run it, and make it your own.

Properties: Markdown on disk | Self-hosted | Git-backed | AI-native | Open source

GitHub: https://github.com/hilash/cabinet
Discord: https://discord.gg/hJa5TRTbTH
Cloud waitlist: https://runcabinet.com/waitlist

### Real Use Cases: How people actually use Cabinet

Knowledge base + agents + files. One OS for wildly different workflows.

Use case 1 — Startup OS (Solo Founder): "I run my entire startup from here. Strategy in /strategy/, roadmap in /product/roadmap.md, ICP in /market/icp.md. My CEO agent attends every planning session — I open a page, describe the week, and it challenges my assumptions and updates the mission board."

### The Problem: Your AI agents have no memory

Every time you start a new Claude session, it forgets everything. Your project context, your decisions, your research — gone. You keep re-explaining the same things. Cabinet gives your AI a persistent brain: a knowledge base that both you and your agents read and write to, 24/7.

Without Cabinet: Scattered docs in Notion. AI sessions that forget context. Manual copy-paste between tools. Scripts held together with tape.

With Cabinet: One knowledge base. AI agents that remember everything. Scheduled jobs that compound. Your team grows while you sleep.

Design Principle: If it feels like enterprise workflow software, it's wrong. If it feels like watching a team work, it's right.

### Ship HTML apps inside your knowledge base

This is the biggest difference between Cabinet and tools like Obsidian or Notion. Drop an `index.html` into any folder and it renders as a live, interactive app.

- Full-screen mode: add a `.app` marker — sidebar and AI panel auto-collapse
- AI-generated apps: ask Claude to build a dashboard, it writes the HTML directly into your KB
- Version controlled: every change is tracked in git, same as your markdown pages
- No build step: plain HTML/CSS/JS. Works with React, Vue, or vanilla

### Features: Everything you need. Nothing you don't.

- WYSIWYG + Markdown: Rich text editing with Tiptap. Tables, code blocks, slash commands. Toggle to raw markdown anytime.
- AI Agents: Onboard a CEO, Editor, Marketer. Each has goals, skills, scheduled jobs. Watch them work like a real team.
- Embedded HTML Apps: Drop an index.html in any folder — it renders as an iframe. Full-screen mode for dashboards and tools.
- Web Terminal: Full Claude Code terminal in the browser. xterm.js + node-pty. Run commands without leaving Cabinet.
- File-Based Everything: No database. Markdown on disk. Drag-and-drop tree sidebar. Your data is always yours, always portable.
- Git-Backed History: Every save auto-commits. Full diff viewer. Restore any page to any point in time. Linked repo support.
- Scheduled Jobs: Cron-based agent automation. Reddit scout every 6 hours. Weekly reports on Monday. Your AI team never sleeps.
- Missions & Tasks: Break goals into missions. Assign tasks to agents. Track progress with Kanban boards and progress bars.
- Internal Chat: Built-in team channels. Agents and humans communicate. @mention an agent to trigger a response.
- Full-Text Search: Cmd+K instant search across all pages. Fuzzy matching. FlexSearch index rebuilt on every change.
- PDF & CSV First-Class: PDFs render inline. CSVs open as editable tables with add/delete rows and columns. Auto-save with git commit.
- Linked Git Repos: Add .repo.yaml to link KB directories to source code repos. AI agents read and reference your codebase.

### The Shift: Why the world needs Cabinet

Andrej Karpathy recently described the future of knowledge work. Cabinet is that future, built today.

Karpathy quotes on LLM knowledge bases:
- "Using LLMs to build personal knowledge bases for various topics of research interest. A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge."
- "Raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki."
- "I think there is room here for an incredible new product instead of a hacky collection of scripts."

How Cabinet maps to Karpathy's vision:
- Data Ingest: Karpathy "Index source docs into raw/, LLM compiles a wiki" → Drag PDFs, CSVs, HTML apps, markdown into the KB. AI agents auto-organize and cross-link.
- IDE / Viewer: Karpathy "Uses Obsidian as the frontend to view compiled wiki" → Built-in WYSIWYG editor, PDF viewer, CSV editor, embedded HTML apps, web terminal — all in one UI.
- Q&A: Karpathy "Once wiki is big enough, ask LLM complex questions against it" → AI panel with @mentions. Agents reference the entire KB. Ask questions, get answers with page citations.
- Output: Karpathy "Render markdown, slide shows, matplotlib images back into Obsidian" → Agents write directly to the KB. Slides, dashboards, reports — all viewable inline. Output compounds.
- Automation: Karpathy "Manually runs LLM health checks, vibe-coded a search engine" → Scheduled cron jobs, agent heartbeats, mission boards. Your AI team runs 24/7 without scripts.

### Comparison: Not another note-taking app

Obsidian is a markdown editor. Notion is a team wiki. Paperclip orchestrates agents. Cabinet is the only tool that combines a knowledge base, AI agents, and embedded apps in one self-hosted OS.

| Feature | Cabinet | Obsidian | Notion | Paperclip |
|---|---|---|---|---|
| Knowledge base / wiki | ✓ | ✓ | ✓ | ✗ |
| Markdown files on disk | ✓ | ✓ | ✗ | ✗ |
| Self-hosted / local-first | ✓ | ✓ | ✗ | ✓ |
| AI agent orchestration | ✓ | ✗ | ✗ | ✓ |
| Agent org chart / hierarchy | ✗ | ✗ | ✗ | ✓ |
| Agent heartbeats / scheduling | ✓ | ✗ | ✗ | ✓ |
| Agent budget controls | ✗ | ✗ | ✗ | ✓ |
| Embedded HTML apps | ✓ | ✗ | ✗ | ✗ |
| Web terminal (xterm.js) | ✓ | ✗ | ✗ | ✗ |
| WYSIWYG editor | ✓ | ✓ | ✓ | ✗ |
| PDF / CSV viewing & editing | ✓ | ✗ | ✗ | ✗ |
| Git-backed version history | ✓ | via plugin | ✗ | ✗ |
| Internal team chat | ✓ | ✗ | ✓ | ✗ |
| Mission / task system | ✓ | ✗ | ✓ | ✓ |
| Linked Git repos | ✓ | ✗ | ✗ | ✗ |
| No database required | ✓ | ✓ | ✗ | ✗ |

vs Paperclip: Paperclip is excellent at agent orchestration — org charts, budgets, audit logs. But it has no knowledge base, no editor, no content layer. Cabinet gives your agents a brain to read and write to, plus HTML apps, a terminal, and a full wiki.

### AI Team: Hire your AI team in 5 questions

Answer 5 questions. A CEO agent appears. It suggests teammates. Each agent has goals, skills, and recurring jobs.

Pre-built agent templates (20 total):
- CEO Agent (Lead): Strategic planning, goal tracking, task delegation. Creates missions, coordinates the team. Recurring jobs: Weekly report, Goal review.
- Editor (Specialist): KB content editing, formatting, linking. Recurring jobs: Content review, Link checker.
- Content Marketer (Specialist): Blog posts, social media, newsletters. Recurring jobs: Reddit scout, Blog drafts.
- SEO Specialist: Keyword research, site optimization. Recurring jobs: Keyword tracker, Competitor scan.
- Sales Agent: Lead generation, outreach, pipeline tracking. Recurring jobs: Lead scorer, Follow-up drafter.
- QA Agent: Review, proofread, fact-check content across the KB. Recurring jobs: Content audit, Broken link scan.
- Also: COO, CFO, CTO, Product Manager, UX Designer, Social Media, Growth Marketer, Copywriter, DevOps Engineer, Customer Success, Data Analyst, People Ops, Legal Advisor, Researcher.

### How It Works: From zero to AI team in 2 minutes

01 — Install & Run: One command. `npx cabinetai run`
02 — Answer 5 Questions: What's your company? What do you do? What are your goals? Cabinet builds your custom AI team.
03 — Watch Your Team Work: Agents create missions, write content, scout Reddit, review quality — all on schedule.
04 — Knowledge Compounds: Every agent run, every edit, every research session adds to the KB. Your system gets smarter every day.

Contact: hi@runcabinet.com

## In the Wild — https://runcabinet.com/media

### Why knowledge bases matter now

LLMs don't know your codebase, your team's decisions, or your project history. Every time you start a new session, that context is gone. The Karpathy Effect — the compounding value of feeding rich, structured context into a model — only works if you have a place to store and retrieve that context reliably.

Most developers are still copy-pasting files and hoping for the best. There's a better way.

### Cabinet is the solution

Cabinet gives your AI agents a persistent, structured memory of everything that matters: your docs, decisions, architecture, and tribal knowledge — all indexed and ready to inject into any LLM context window.

Stop re-explaining your stack on every prompt. Let Cabinet handle the context so you can focus on building.
