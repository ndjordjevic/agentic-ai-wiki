# crewai.com

## Fetch log
- Inbox URL: https://crewai.com/
- Final URL: https://crewai.com/
- Fetched: 2026-05-22
- Pages: 8
- Mode: standard

## Landing page — https://crewai.com/

CrewAI makes it easy for enterprises to operate teams of AI agents that perform complex tasks autonomously, reliably and with full control. Loved by AI builders. Trusted by AI leaders.

### Everything you need to succeed

**Easy** — Build a crew of AI agents that autonomously interact with enterprise applications and use tools to automate workflows and tasks, with or without writing code. Features: visual editor and AI copilot, integrated tools and triggers, intuitive and powerful APIs.

**Trusted** — Delegate critical tasks to agentic workflows that produce repeatable, reliable outcomes. Features: workflow tracing, agent training, task guardrails.

**Scalable** — Streamline and accelerate Agent AI adoption across every business unit, department and team with centralized management and comprehensive monitoring. Features: LLM and tool configuration, role-based access control, serverless containers.

### Stats
- 450,000,000+ agentic workflows ran per month
- 60% of the Fortune 500 use CrewAI
- 4,000+ sign-ups per week

### CrewAI AMP — The Agent Management Platform

CrewAI AMP enables enterprises to streamline and accelerate the adoption of AI agents across departments, business units and teams by supporting every stage from initial development to production scaling.

**Orchestrate** (built on CrewAI OSS): Planning, Reasoning, Memory, Tools, Knowledge

**Build and Integrate** (CrewAI Studio): Visual editor, APIs, Tools, Triggers

**Observe and Optimize**: Tracing, Training, Testing, Events

**Manage and Scale**: Monitoring, Permissions, Serverless, Teams

### Deployment Options

- **CrewAI AMP Cloud** — Manage the full AI agent lifecycle — build, test, deploy, and scale — with a visual editor and ready-to-use tools.
- **CrewAI AMP Factory** — All the power of AMP Cloud, deployed securely on your own infrastructure — on-prem or private VPCs in AWS, Azure, or GCP.
- **CrewAI OSS** — An open-source orchestration framework with high-level abstractions and low-level APIs for building complex, agent-driven workflows.

### Customer Case Studies

- **DocuSign**: 75% faster first contact with leads — extracted, consolidated and evaluated lead data from multiple internal systems with AI agents.
- **General Assembly**: 90% reduction in development time — streamlined and scaled curriculum design process with a crew of AI agents.
- **IBM**: Reduced manual coordination — integrated CrewAI with WatsonX.AI to leverage IBM's foundation-model runtime while coordinating legacy and modern systems.
- **Piracanjuba**: 95% response accuracy for customer support — replaced legacy RPA tooling with a crew of AI agents.
- **PwC**: 7x higher function spec and code generation accuracy — boosted code-generation accuracy from 10% to 70%.

## Docs — https://docs.crewai.com/

CrewAI is the leading open-source framework for orchestrating autonomous AI agents and building complex workflows. It empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence of **Crews** with the precise control of **Flows**.

With over 100,000 developers certified through community courses, CrewAI is the standard for enterprise-ready AI automation.

### Architecture

**Flows (The Backbone)**: Structured, event-driven workflows. Provide state management, conditional logic, branching, and loops. Use `@start()` and `@listen()` decorators. Each flow instance gets a unique UUID in state.

**Crews (The Intelligence)**: Teams of autonomous agents. Role-playing agents with specific goals and tools. Agents collaborate and delegate to complete complex tasks.

How it works: Flow triggers event → manages state → delegates to Crew → Crew agents collaborate → return result to Flow → Flow continues.

## Introduction — https://docs.crewai.com/en/introduction

CrewAI architecture balances autonomy with control. Flows provide scaffolding; Crews provide execution intelligence.

**When to use:**
- Simple automation: Single Flow with Python tasks
- Complex research: Flow managing state → Crew performing research
- Application backend: Flow handling API requests → Crew generating content → Flow saving to DB

**Start with a Flow** for any production-ready application; use a Crew within a Flow step for complex autonomous tasks.

## Agents — https://docs.crewai.com/en/concepts/agents

An `Agent` is an autonomous unit that can perform tasks, make decisions, use tools, communicate with other agents, maintain memory, and delegate tasks. Key attributes:

- `role`, `goal`, `backstory` — identity and motivation (YAML-configurable)
- `llm` — defaults to OpenAI GPT-4; overridable per agent
- `tools` — list of BaseTool instances
- `max_iter` — max decision iterations (default 20)
- `allow_delegation` — can delegate to other agents (default False)
- `memory` — agent-scoped or crew shared
- `reasoning` — pre-task planning mode (default False)
- `allow_code_execution` — Docker (safe) or direct (unsafe) code execution
- `multimodal` — supports image/file inputs

YAML configuration strongly recommended for maintainability.

## Crews — https://docs.crewai.com/en/concepts/crews

A crew represents a collaborative group of agents working together to achieve a set of tasks. Key attributes:

- `process` — `sequential` (default) or `hierarchical` (with manager LLM)
- `memory` — pass `True` for defaults or a configured `Memory()` instance
- `planning` — pre-run AgentPlanner adds plan to each task description
- `stream` — real-time output streaming via `CrewStreamingOutput`
- `checkpoint` — automatic state checkpointing for resumable execution
- `skills` — filesystem-based skill packages injected into agent prompts

Crews are defined via `@CrewBase` decorator class with `@agent`, `@task`, `@crew` decorators referencing YAML config files.

## Flows — https://docs.crewai.com/en/concepts/flows

Flows provide structured, event-driven workflow management.

- `@start()` — marks entry point(s); multiple start methods run in parallel
- `@listen(method)` — triggers when another method emits output
- `@router()` — conditional branching based on output
- Built-in state (dict or Pydantic model) with UUID per execution
- `flow.kickoff()` — execute the flow
- `flow.plot()` — generate visual execution graph
- `self.remember()` / `self.recall()` — built-in memory in Flows

## Memory — https://docs.crewai.com/en/concepts/memory

Unified `Memory` class replaces separate short-term, long-term, entity, and external memory types. Uses LLM to analyze content when saving (inferring scope, categories, importance). Adaptive-depth recall with composite scoring: semantic similarity + recency + importance.

Four usage modes:
1. **Standalone** — scripts, notebooks, CLI tools
2. **With Crews** — `memory=True` or pass `Memory()` instance; shared across agents
3. **With Agents** — scoped view for private context per agent
4. **With Flows** — built-in `self.remember()` / `self.recall()` / `self.extract_memories()`

## Tools — https://docs.crewai.com/en/concepts/tools

Tools are skills/functions agents use to perform actions. Install: `pip install 'crewai[tools]'`. Compatible with LangChain tools.

Key tools: ApifyActorsTool, BrowserbaseLoadTool, CodeDocsSearchTool, CodeInterpreterTool, ComposioTool, CSVSearchTool, DALL-E Tool, DirectorySearchTool, FileReadTool, GithubSearchTool, JSONSearchTool, MDXSearchTool, PDFSearchTool, PGSearchTool, SerperDevTool, TXTSearchTool, WebsiteSearchTool, WikipediaSearchTool, YoutubeChannelSearchTool.

All tools: error handling, caching (configurable), async support, `cache_function` attribute for fine-grained cache control.

Custom tools created via `@tool` decorator or subclassing `BaseTool`.

## Installation — https://docs.crewai.com/en/installation

```bash
# 1. Install uv
pip install uv

# 2. Create project
crewai create crew <project-name>
cd <project-name>

# 3. Edit agents.yaml and tasks.yaml
# 4. Run
crewai run
```

Project structure: `agents.yaml`, `tasks.yaml`, `.env`, `main.py`, `crew.py`, `tools/`, `knowledge/`
