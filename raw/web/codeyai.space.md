# codeyai.space

## Fetch log
- Inbox URL: https://www.codeyai.space/
- Final URL: https://www.codeyai.space/
- Fetched: 2026-07-04
- Pages: 12
- Mode: standard

## Landing page — https://www.codeyai.space/

Codey — Your Local Command Center for AI Work

# Your Local Command Center For AI Work

Build apps, run coding agents, automate workflows, and connect 70+ AI providers from one private workspace.

Download Codey | See what it can do

Built for people who want AI power without giving up control

LOCAL | AGENTS | APPS | AUTOMATE | PROVIDERS | PRIVACY

## Everything You Need To Build With AI Locally

Apps, agents, providers, skills, and automations in one private workspace.

### Local — Build With AI. Keep Control.
- Your code stays with you
- Desktop and TUI workflows
- Private projects, familiar files

### Agents — A Built-In AI Team
Prometheus builds, Athena plans, Scout explores, and Iris helps in the background.
- Specialized agents by default
- Parallel work without context waste
- Custom agents when you need your own

### Autopilot — Turn Ideas Into Production Apps
Matis can take an app idea from prompt to polished Next.js product with strong design taste built into the flow.
- End-to-end app generation
- Production-ready web surfaces
- Premium UI direction included

### Workpilot — Not Just Code. Real Work.
Hermes can browse, read docs, work with files, create documents, build sheets, prepare slides, handle PDFs, and automate through n8n.
- Docs, browser, files, PDFs
- Sheets, slides, and writing
- n8n automation built in

### Providers — Bring The AI Accounts You Already Have
Use Claude, Codex/OpenAI, Gemini, OpenRouter, local models, or any compatible provider without paying Codey for model usage.
- 70+ providers supported
- Claude Pro and Max friendly
- Custom providers and local models

## Choose How Much Codey Handles.
- **Co-Pilot** — Work with Prometheus and Athena when you want strong agent help while staying close to every decision.
- **Autopilot** — Let Matis plan, build, and polish a full web app when you want Codey to carry the whole flow.
- **Workpilot** — Let Hermes handle research, files, documents, spreadsheets, slides, PDFs, browsing, and n8n automation.

## Meet The Codey Agents
- **Prometheus** (Build agent) — Handles coding work, fixes, refactors, and implementation while staying grounded in your project.
- **Athena** (Planning agent) — Turns unclear work into a clean path before the build starts.
- **Scout** (Explore subagent) — Searches large codebases and brings back useful context without draining the main agent.
- **Iris** (General subagent) — Helps the main agent with focused side work, research, checks, and small execution tasks.
- **Matis** (Autopilot agent) — Builds full production web apps from idea to polished Next.js experience.
- **Hermes** (Workpilot agent) — Works across docs, browser, files, sheets, slides, PDFs, and n8n automations.

## Docs — https://www.codeyai.space/docs/intro

# Introduction to Codey

Codey is a secure, developer-focused AI coding agent. It is designed to work where you work: inside your local terminal, as a standalone desktop companion, or integrated with your favorite editors.

Unlike generic prompt-completion tools, Codey is project-aware, supports a secure local execution loop, and can coordinate specialized subagents to plan, write, and verify your code locally.

### Prerequisites
- A modern terminal emulator (e.g. Kitty, WezTerm, Alacritty, or Ghostty)
- API keys for your preferred LLM provider, or an account on Codey Zen for automatic curated routing

### Installation
```bash
curl -fsSL https://codey.ai/install | bash
# or: brew install fares-moustafa/tap/codey
```

### Connecting & Configuring
```bash
codey auth login
# or inside TUI: /connect
```

### Initializing a Project
```bash
codey
# Inside the TUI:
/init
```
Generates `AGENTS.md` in the project root. Switch between Build Mode and Plan Mode with Tab.

## Co-Pilot — https://www.codeyai.space/co-pilot

Co-Pilot keeps you hands-on while Prometheus builds, Athena plans, Scout explores, and Iris helps from your private local workspace.

Workflow:
1. Point Codey at the work — open a local project, describe the change
2. Plan before changing code — Athena shapes the approach; Scout gathers context
3. Build with Prometheus — edits, runs commands, explains tradeoffs, keeps changes reviewable

Built for: feature work with visible plan, bug fixes grounded in local context, refactors file-by-file, markdown/diagrams, parallel tasks, your own providers.

## Autopilot — https://www.codeyai.space/autopilot

Matis plans, builds, refines, and polishes production-ready Next.js apps from one focused prompt.

Workflow:
1. Describe the app — product idea, audience, interface feel
2. Matis builds the flow — pages, components, states, Next.js structure
3. Review and refine — redirect product, polish before ship

Examples: SaaS analytics dashboard, founder landing page, internal operations tool, AI product prototype.

Included in Codey Pro ($10/month): production-ready Next.js apps, premium UI direction, local workspace, your providers, reviewable files/changes/terminal output.

## Workpilot — https://www.codeyai.space/workpilot

Hermes researches, writes, organizes files, builds sheets, prepares slides, handles PDFs, and creates automations.

Toolbelt: Docs, Browser, Sheets, Slides, Writer, Automation (n8n), Files, PDF.

Workflow:
1. Assign the outcome — brief, deck, spreadsheet, research pass, automation
2. Gather the work — web, files, docs, PDFs, office-style tools
3. Review the deliverable — inspect, edit, keep in local workspace

Included in Codey Pro ($10/month) with Autopilot, custom agents, n8n integration.

## Pricing — https://www.codeyai.space/pricing

### Free ($0)
- Co-Pilot workspace, Desktop and TUI, local-first projects
- Bring your own providers, skills and markdown rendering, MCP-ready workflows

### Pro ($10/month)
- Autopilot with Matis, Workpilot with Hermes
- Custom agents, n8n integration and automation, advanced skills workflows, priority product features

Model usage stays with providers you already choose — Codey Pro charges for workspace and advanced agent modes, not model tokens.

## AI Agents Persona Config — https://www.codeyai.space/docs/agents

- **Primary Agents**: interact directly in chat; cycle with Tab (Built-ins: Build and Plan)
- **Subagents**: spawned by primary agents or @mentioned; run isolated parallel tasks (Built-ins: General and Explore)

Custom agents via markdown in `~/.config/codey/agents/<name>.md` (global) or `.codey/agents/<name>.md` (per-project):

```markdown
---
description: Reviews code changes for performance improvements
mode: subagent
model: anthropic/claude-sonnet-4-5
tools:
  write: false
  bash: false
---

You are a performance optimization expert...
```

## LLM Providers — https://www.codeyai.space/docs/providers

Supports 30+ providers including Anthropic, OpenAI, Google Gemini, Ollama (local), Amazon Bedrock, OpenRouter.

```bash
codey auth list
codey auth logout <provider-id>
```

## Pre-packaged Skills System — https://www.codeyai.space/docs/skills

Skills are folders with instruction prompts, reference templates, and scripts.

Common skills:
- browser-automation
- data-cleaning
- n8n-automation

Agent auto-loads matching skills when prompts match skill descriptions.

## Model Context Protocol (MCP) — https://www.codeyai.space/docs/mcp-servers

Local MCP servers via subprocess command; remote via HTTP/SSE. OAuth PKCE for remote servers; tokens in `~/.local/share/codey/mcp-auth.json`.

## Core Tools System — https://www.codeyai.space/docs/tools

| Tool ID | Purpose | Safe/Read-only |
| --- | --- | --- |
| read_file | Read file contents | Yes |
| write_to_file | Create/overwrite files | No |
| replace_file_content | Surgical edits | No |
| multi_replace_file_content | Multiple edits | No |
| run_command | Bash in project directory | No |
| list_dir | List files | Yes |
| grep_search | Ripgrep search | Yes |
| webfetch | Download/parse URLs | Yes |

## CLI Reference — https://www.codeyai.space/docs/cli

- `codey run "prompt"` — non-interactive single prompt
- `codey serve --port 4096` — local HTTP API + WebSocket
- `codey web` — start server and open web client
- `codey auth login|status` — credentials and subscription
- `codey agent create` — interactive custom agent builder
