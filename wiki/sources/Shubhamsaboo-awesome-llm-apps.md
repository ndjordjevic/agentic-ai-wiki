---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/Shubhamsaboo/awesome-llm-apps
tags:
  - awesome-list
  - agent-examples
  - rag-tutorials
  - multi-agent-teams
  - agent-skills
  - mcp-agents
  - voice-agents
  - generative-ui
related:
  - voltagent-awesome-agent-skills
  - HKUDS-LightRAG
  - crewai.com
  - adk.dev
  - pydantic-pydantic-ai
  - langchain.com-langgraph
product: awesome-llm-apps
detail_level: standard
created: 2026-07-17
updated: 2026-07-17
---

Awesome LLM Apps is a large curated collection (123,196 stars, Apache-2.0) of 100+ hand-built, runnable AI agent, RAG, and LLM applications, maintained by Unwind AI. Unlike a links-only awesome-list, every entry is a working, cloneable project — single-file starter agents, production-style multi-agent teams, RAG pipelines, voice agents, MCP-connected agents, generative UI agents, and installable agent skills — spanning Claude, GPT, Gemini, DeepSeek, Llama, and Qwen. It functions as both a hands-on gallery of agent-building patterns across major frameworks and a weekly-updated on-ramp for developers evaluating an approach before committing to it.

_All claims below are sourced from ../../raw/github/Shubhamsaboo-awesome-llm-apps.md unless otherwise noted._

## What it does

The repository organizes 100+ example applications into twelve top-level categories: Agent Skills, Starter AI Agents, Advanced AI Agents, Always-on Agents, Multi-agent Teams, Voice AI Agents, Generative UI and Agentic Frontends, Autonomous Game-Playing Agents, MCP AI Agents, RAG (20+ tutorials from basic chains to agentic/multi-source), LLM Apps with Memory, Chat with X, LLM Optimization Tools, LLM Fine-tuning, and two framework crash courses (Google ADK, OpenAI Agents SDK). Each entry links to a self-contained project directory with its own README and dependencies; the parent site theunwindai.com publishes matching step-by-step tutorials.

## Installation

Two installation paths: install a single agent skill into a coding agent, or clone and run a full example app.

```bash
# Give a coding agent a new skill in 10 seconds
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard

# Clone and run any agent in 30 seconds
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
pip install -r requirements.txt
streamlit run travel_agent.py
```

## Key features

- **Agent Skills section** — installable Claude Code / Codex / Cursor skills (e.g. Project Graveyard, Scope Creep Detector, Self-Improving Agent Skills), each passing a security + eval CI gate before merge.
- **Starter AI Agents** — 12 single-file agents runnable with just an API key (travel planning, data analysis, medical imaging, meme generation via browser automation, music generation, mixture-of-agents aggregation).
- **Advanced AI Agents** — 20+ production-style single- and multi-agent apps with tools, memory, and multi-step reasoning (fraud investigation, VC due diligence, self-evolving agents via EvoAgentX, hash-chained trust-gated research teams).
- **Multi-agent Teams** — 13 agent-team examples (legal, recruitment, real estate, competitor intelligence, teaching faculties) covering CrewAI, AG2, and custom orchestration patterns.
- **RAG tutorials** — 20 pipelines spanning local (Qdrant, no API keys), corrective (CRAG), hybrid search, vision RAG, multimodal RAG, knowledge-graph RAG with citations, and RAG failure diagnostics.
- **MCP AI Agents, Generative UI, Voice AI, Always-on Agents** — dedicated sections for Model Context Protocol integrations, agents that render interactive UI (kanban boards, dashboards, shadcn components), real-time speech agents, and scheduled/event-driven background agents.
- **Framework crash courses** — deep, model-agnostic walkthroughs of the Google ADK and OpenAI Agents SDK covering tools, memory, callbacks, plugins, handoffs, and multi-agent patterns.

## Architecture

Each top-level directory (`starter_ai_agents/`, `advanced_ai_agents/`, `rag_tutorials/`, `agent_skills/`, `mcp_ai_agents/`, `voice_ai_agents/`, `generative_ui_agents/`, `always_on_agents/`, `advanced_llm_apps/`, `ai_agent_framework_crash_course/`) contains one independent project per example, each with its own dependencies and README rather than a shared framework or monorepo package. `agent_skills/` is the exception: entries there are SKILL.md-based capability modules distributable via `npx skills add`, not standalone apps. A handful of entries (Openwork browser agent, a Wispr Flow voice-dictation clone) are pointers to sibling external repos rather than in-tree code.

## Example usage

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
pip install -r requirements.txt
streamlit run travel_agent.py
```

Most `starter_ai_agents/` and `rag_tutorials/` entries follow this same clone → `pip install -r requirements.txt` → `streamlit run <file>.py` pattern; `advanced_ai_agents/` and `advanced_llm_apps/` entries may require additional API keys or vector-store setup per their own READMEs.

## When to use

Use this repository to see a working, minimal reference implementation before building an agent or RAG pipeline from scratch — pick the closest matching pattern (starter single-file agent, multi-agent team, RAG variant, voice agent, MCP agent) and adapt it rather than starting from an empty project. The two framework crash courses (Google ADK, OpenAI Agents SDK) are a useful side-by-side reference when choosing between agent frameworks. Not a production framework or SDK itself — each example is a standalone teaching artifact, not a maintained library with a stability guarantee.

## Ecosystem

- [[voltagent-awesome-agent-skills]] — a dedicated curated registry of agent skills; this repo's `agent_skills/` section is a smaller, hand-built counterpart with its own CI-gated quality bar.
- [[HKUDS-LightRAG]] — a standalone RAG framework; several `rag_tutorials/` entries here demonstrate comparable retrieval patterns (hybrid search, knowledge-graph RAG) at tutorial scale rather than as a reusable library.
- [[crewai.com]] and [[adk.dev]] — frameworks directly used by several `advanced_ai_agents/` and `multi_agent_apps/` examples, and by the dedicated ADK crash course.
- [[pydantic-pydantic-ai]] — used by the Typed Agentic RAG tutorial for validated, citation-backed answers.
- [[langchain.com-langgraph]] — underlies the AI Blog Search agentic RAG tutorial.
- theunwindai.com — the companion tutorial site (repo homepage) publishing step-by-step write-ups for each example, with new templates added weekly.
