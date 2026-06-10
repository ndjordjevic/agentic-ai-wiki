---
type: source
source_url: https://github.com/Felix-Forever/hermes-agent-desktop
tags:
  - multi-agent-collaboration
  - desktop-gui
  - pywebview
  - skill-store
  - pm-orchestrator
  - hermes-agent
  - openai-compatible
  - python
related:
  - hermes-agent.nousresearch.com
product: hermes-agent-desktop
detail_level: standard
created: 2026-06-10
updated: 2026-06-10
---

Hermes Agent Desktop is an open-source, native desktop client (Python 3.11 + pywebview, MIT License, v1.0.0) that extends the Hermes Agent CLI into a full multi-agent collaboration environment. Where the original Hermes Agent provides a single terminal-based agent, this desktop application adds a **20-specialist AI team** orchestrated by a Project Manager agent: the PM automatically decomposes user requirements, delegates sub-tasks to domain specialists (UI Designer, Frontend/Backend/Full-stack Engineers, QA, Architect, DevOps, DBA, and more), and synthesizes integrated deliverables. The entire frontend is a single-file HTML/CSS/JS application served by a lightweight aiohttp backend with no Electron dependency.

_All claims below are sourced from ../../raw/github/felix-forever-hermes-agent-desktop.md unless otherwise noted._

## What it does

Hermes Agent Desktop wraps the Hermes Agent core (`NousResearch/hermes-agent`, cloned as a local dependency) in a native macOS/Linux desktop window. It adds three capabilities absent from the CLI: (1) a **20-agent collaboration system** with a Project Manager orchestrator that auto-decomposes tasks, (2) a **visual Skill Store** surfacing 50+ curated skills from the CocoLoop marketplace with one-click install, search, and category filtering, and (3) a **full Agent CRUD dashboard** for creating, configuring, and monitoring custom agents with live status and tool counts.

## Key features

- **20 built-in AI agents** covering all major product-development roles: Project Manager, Product Manager, UI Designer, Frontend/Backend/Full-stack Engineer, QA, Architect, DevOps, Data/AI Engineer, Security Expert, DBA, Tech Writer, Translator, Legal Counsel, Creative Director, Operations, Marketing, Business Analyst.
- **PM orchestrator pattern** — the Project Manager receives user input, decomposes it into sub-tasks, delegates to specialists, tracks progress, and synthesizes a final integrated result; no manual prompt engineering required.
- **Streaming SSE responses** — real-time token-by-token display with per-agent section dividers and collapsible tool-call panels.
- **Visual Skill Store** — 50+ skills from CocoLoop Skill Hub with real-time search, category tags, and one-click install; links to the full CocoLoop marketplace.
- **Agent CRUD dashboard** — full create/edit/delete for custom agents with configurable system prompts, models, and skill tags.
- **Single-file frontend** — zero JavaScript dependencies; entire UI is `index.html`; avoids Electron.
- **Model switcher** — one-click switch between Kimi K2.5, Qwen Plus/Max, DeepSeek V3/R1 in the input area.
- **Multi-provider support** — any OpenAI-compatible endpoint: Alibaba DashScope, OpenAI, OpenRouter, DeepSeek, Moonshot/Kimi, Anthropic.

## Architecture

The application has two layers connected by HTTP/SSE. The **backend** (`app.py`) is a Python aiohttp server that exposes `/v1/chat/completions` (SSE stream), `/v1/models`, and `/api/choose-folder`; it instantiates a Hermes `AIAgent` per request using the Hermes Agent core cloned at `hermes-core/`. The **frontend** (`index.html`) is a single-file HTML/CSS/JS app served by pywebview as a native desktop window; it handles the Chat UI, Agents Dashboard, Skill Store, and the multi-agent orchestration logic (PM system prompt construction and section-labeled response assembly).

The multi-agent orchestration runs entirely in the frontend's orchestration logic: the PM system prompt encodes all 20 agent definitions; when a task arrives, the frontend composes the PM prompt, dispatches to the backend, and renders labeled response sections from the streamed output.

## Installation

```bash
git clone https://github.com/Felix-Forever/hermes-agent-desktop.git
cd hermes-agent-desktop
git clone --depth 1 https://github.com/NousResearch/hermes-agent.git hermes-core
python3.11 -m venv venv && source venv/bin/activate
pip install -e "./hermes-core[all,dev]" pywebview
cp .env.example .env  # add API key
python app.py
```

Configure `.env` with `DASHSCOPE_API_KEY` (or any OpenAI-compatible key), `BASE_URL`, and `MODEL`.

## Example usage

```bash
python app.py          # launch the native desktop window
# or for UI development only:
python -m http.server 8643 --directory .
```

Within the app: type a complex task (e.g. "build me an e-commerce platform") and the Project Manager automatically decomposes it into sub-tasks, assigns them to specialists, and returns an integrated result. Use the Agents Dashboard to create custom agents or monitor live agent status. Open the Skill Store to browse and install skills.

## Maintenance status

Stars: 53 | Forks: 12 | License: MIT | Latest release: v1.0.0 (2026-04-12) | Language: HTML (single-file frontend). Active repository; single initial release. Roadmap items include real skill installation via the Hermes CLI backend, true parallel agent-to-agent message passing, workspace file-tree browser, voice I/O, plugin system for custom tools, dark mode, and Windows/Linux native builds.

## Ecosystem

Built on [[hermes-agent.nousresearch.com]] (NousResearch/hermes-agent) as the core agent runtime. Skills sourced from CocoLoop Skill Hub (`hub.cocoloop.cn`). Supports all OpenAI-compatible LLM providers. The original Hermes Agent CLI is a prerequisite (cloned as a local dependency during installation, not installed as a package).
