# Felix-Forever/hermes-agent-desktop

## Metadata
- Stars: 53
- Primary language: HTML
- Default branch: main
- Latest release: v1.0.0 (2026-04-12)
- License: MIT License
- Homepage: https://github.com/NousResearch/hermes-agent
- Fetched: 2026-06-10
- Final URL: https://github.com/Felix-Forever/hermes-agent-desktop

## Description
Multi-Agent AI Desktop Client — 20 specialists auto-collaborate on your tasks. Visual Skill Store, PM orchestrator, streaming chat. Works with Kimi K2.5/Qwen/DeepSeek/GPT-4o. Built on Hermes Agent.

## README
<p align="center">
  <img src="https://img.shields.io/badge/Hermes_Agent-Desktop-4f6ef7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHJ4PSI2IiBmaWxsPSIjNGY2ZWY3Ii8+PHRleHQgeD0iMTIiIHk9IjE3IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IndoaXRlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5IPC90ZXh0Pjwvc3ZnPg==" alt="Hermes Agent Desktop">
</p>

<h1 align="center">Hermes Agent Desktop</h1>

<p align="center">
  <strong>The Desktop Client That Turns Hermes Agent Into a Full AI Team</strong>
</p>

> **Not just a GUI wrapper** — this is a ground-up rebuild of the Hermes Agent experience. We added a **complete visual multi-agent collaboration system** and an **integrated Skill Store** that the original CLI version doesn't have.

[Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research is already the most capable open-source AI agent. This desktop client takes it further — replacing the single-agent terminal with a **20-person AI team** led by a Project Manager who automatically understands your requirements, decomposes complex tasks, delegates to the right specialists, and delivers integrated results. No prompt engineering required.

Built with a clean Apple-inspired design, zero Electron bloat, and works with any OpenAI-compatible LLM provider (DashScope, DeepSeek, OpenAI, Anthropic, OpenRouter, and more).

## What's New vs Original Hermes Agent

| | Original Hermes (CLI) | Hermes Agent Desktop |
|---|---|---|
| **Interface** | Terminal TUI | Native desktop GUI with Apple-style design |
| **Agent Model** | Single agent, one conversation | **20 specialized AI agents** collaborating in real-time |
| **Task Handling** | User manually prompts | **PM auto-decomposes tasks**, delegates to experts, synthesizes results |
| **Skill Discovery** | `hermes skills` CLI command | **Visual Skill Store** with 50+ curated skills, one-click install, search & filter |
| **Agent Management** | Not available | **Full CRUD dashboard** — create, configure, monitor agents with live status |
| **Workspace** | `cd` in terminal | **Native folder picker** with recent workspace history |
| **Model Switching** | Config file edit | **One-click model switcher** in the input area |

### Why Multi-Agent Matters

A single AI agent can write code — but building a real product needs a **team**. This client gives you:

- A **Project Manager** who breaks "build me an e-commerce platform" into 12 actionable sub-tasks
- A **Product Manager** who writes the PRD before any code is touched
- A **UI Designer** who defines the interface before the frontend engineer starts
- **3 Engineers** (frontend, backend, full-stack) who write actual code in their domains
- A **QA Engineer** who catches what the developers missed
- An **Architect** who ensures the pieces fit together at scale

All orchestrated automatically. You describe what you want; the team delivers.

## Features

### Multi-Agent Collaboration System

- **20 Built-in AI Agents** — Project Manager, Product Manager, UI Designer, Frontend/Backend/Full-stack Engineers, QA, Architect, DevOps, Data/AI Engineer, Security Expert, Operations, Marketing, Business Analyst, Tech Writer, Translator, Legal Counsel, DBA, Creative Director
- **Project Manager as Orchestrator** — Automatically receives requirements, decomposes tasks, delegates to specialists, tracks progress, and synthesizes deliverables
- **Real-time Agent Status** — Dashboard showing which agents are active, task progress, and completion stats
- **Agent CRUD** — Create, edit, and delete custom agents with configurable system prompts, models, and skill tags

### Chat Interface

- **Streaming SSE Responses** — Real-time token-by-token display with typing cursor animation
- **Multi-Agent Response Sections** — Clearly labeled sections showing which agent contributed what
- **Rich Markdown Rendering** — Headings, code blocks with syntax highlighting & copy button, tables, blockquotes, lists, inline code
- **Tool Call Indicators** — Collapsible panels showing agent tool usage, auto-collapsed after completion
- **Session Management** — Multiple conversations with history, auto-save to localStorage

### Integrated Skill Store

The original Hermes Agent requires CLI commands to discover and install skills. A **visual Skill Store** is built directly into the desktop client:

- **50+ Curated Skills** — Covering AI search, browser automation, code execution, data processing, content creation, and more
- **One-Click Install** — Click "+" to install any skill instantly, with loading animation and toast confirmation
- **Smart Search** — Real-time fuzzy search across all skill names and descriptions
- **Category Tags** — Skills organized by type (Search, Agent, Development, Productivity, Security, etc.)
- **Direct Store Access** — Link to the full CocoLoop marketplace for browsing hundreds more

### Desktop Experience

- **Native macOS Window** — Powered by pywebview with system-native chrome
- **Workspace Selector** — Native folder picker dialog for setting working directory
- **Model Switcher** — Quick switch between models (Kimi K2.5, Qwen Plus/Max, DeepSeek V3/R1)
- **Settings Panel** — Configure API endpoint, key, and model
- **Apple-Inspired Design** — Clean grey palette, card-based layout, smooth animations

## Quick Start

### Prerequisites

- **macOS** (primary), Linux, or WSL2
- **Python 3.11+**
- **Git**

### Installation

```bash
git clone https://github.com/Felix-Forever/hermes-agent-desktop.git
cd hermes-agent-desktop
git clone --depth 1 https://github.com/NousResearch/hermes-agent.git hermes-core
python3.11 -m venv venv
source venv/bin/activate
pip install -e "./hermes-core[all,dev]"
pip install pywebview
cp .env.example .env
# Edit .env and add your API key
python app.py
```

## Configuration

### Environment Variables (`.env`)

```env
DASHSCOPE_API_KEY=your-api-key-here
BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MODEL=kimi-k2.5
```

### Supported LLM Providers

| Provider | Base URL | Models |
|----------|----------|--------|
| **Alibaba DashScope** | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `kimi-k2.5`, `qwen-plus`, `qwen-max`, `deepseek-v3`, `deepseek-r1` |
| **OpenAI** | `https://api.openai.com/v1` | `gpt-4o`, `gpt-4o-mini` |
| **OpenRouter** | `https://openrouter.ai/api/v1` | 200+ models |
| **DeepSeek** | `https://api.deepseek.com/v1` | `deepseek-chat`, `deepseek-reasoner` |
| **Moonshot/Kimi** | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |

## Architecture

```
hermes-agent-desktop/
├── app.py              # Backend: aiohttp API server + pywebview launcher
├── index.html          # Frontend: single-file HTML/CSS/JS application
├── .env.example        # Environment variable template
├── README.md
└── docs/
    └── screenshots/    # App screenshots
```

### How It Works

```
┌─────────────────────────────────┐
│   pywebview Desktop Window      │
│   ┌───────────────────────────┐ │
│   │   HTML/CSS/JS Frontend    │ │
│   │   • Chat UI (SSE stream)  │ │
│   │   • Agents Dashboard      │ │
│   │   • Skill Store           │ │
│   │   • Orchestrator Logic    │ │
│   └──────────┬────────────────┘ │
└──────────────┼──────────────────┘
               │ HTTP / SSE
               ▼
┌─────────────────────────────────┐
│   Python aiohttp Backend        │
│   • /v1/chat/completions (SSE)  │
│   • /v1/models                  │
│   • /api/choose-folder          │
│   • Creates AIAgent per request │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│   Hermes AIAgent Core           │
│   • LLM API (OpenAI-compatible) │
│   • Tool Execution (60+ tools)  │
│   • Memory & Skills System      │
│   • Session Persistence (SQLite)│
└─────────────────────────────────┘
```

### Multi-Agent Orchestration Flow

```
User Input → Project Manager (Orchestrator)
    │
    ├── UI Designer → [Design]
    ├── Frontend Eng → [Code]
    ├── Backend Eng → [API]
    └── QA Engineer → [Tests]
    │
    └── Project Manager (Synthesize) → Final Delivery
```

## Tech Stack

- **Frontend**: Vanilla HTML5 + CSS3 + JavaScript (zero dependencies, single-file)
- **Backend**: Python 3.11 + aiohttp (lightweight async HTTP server)
- **Desktop**: pywebview (native OS webview, no Electron bloat)
- **Agent Core**: [Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research
- **LLM**: Any OpenAI-compatible API provider

## Top-level structure

```
.env.example     — environment variable template
.gitignore
LICENSE          — MIT
README.md
app.py           — aiohttp backend server + pywebview launcher (main entry point)
index.html       — entire frontend: single-file HTML/CSS/JS application
docs/
  screenshots/   — UI screenshots (chat, agents, skills, settings)
```

Notes: No CLAUDE.md/AGENTS.md/GEMINI.md. Minimal structure: two-file app (app.py + index.html) wrapping NousResearch/hermes-agent as a git submodule dependency.
