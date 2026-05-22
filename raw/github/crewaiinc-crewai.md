# crewAIInc/crewAI

## Metadata
- Stars: 51,928
- Primary language: Python
- Default branch: main
- Latest release: 1.14.6a1 (2026-05-21, pre-release)
- License: MIT License
- Homepage: https://crewai.com
- Fetched: 2026-05-22
- Final URL: https://github.com/crewAIInc/crewAI

## Description
Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## README

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="docs/images/crewai_logo.png" width="600px" alt="Open source Multi-AI Agent orchestration framework">
  </a>
</p>

### Fast and Flexible Multi-Agent Automation Framework

> CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely **independent of LangChain or other agent frameworks**.
> It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario.

- **CrewAI Crews**: Optimize for autonomy and collaborative intelligence.
- **CrewAI Flows**: The **enterprise and production architecture** for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively

With over 100,000 developers certified through our community courses at [learn.crewai.com](https://learn.crewai.com), CrewAI is rapidly becoming the standard for enterprise-ready AI automation.

# CrewAI AMP Suite

CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation.

## Crew Control Plane Key Features:

- **Tracing & Observability**: Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces.
- **Unified Control Plane**: A centralized platform for managing, monitoring, and scaling your AI agents and workflows.
- **Seamless Integrations**: Easily connect with existing enterprise systems, data sources, and cloud infrastructure.
- **Advanced Security**: Built-in robust security and compliance measures ensuring safe deployment and management.
- **Actionable Insights**: Real-time analytics and reporting to optimize performance and decision-making.
- **24/7 Support**: Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues.
- **On-premise and Cloud Deployment Options**: Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements.

## Why CrewAI?

CrewAI unlocks the true potential of multi-agent automation, delivering the best-in-class combination of speed, flexibility, and control with either Crews of AI Agents or Flows of Events:

- **Standalone Framework**: Built from scratch, independent of LangChain or any other agent framework.
- **High Performance**: Optimized for speed and minimal resource usage, enabling faster execution.
- **Flexible Low Level Customization**: Complete freedom to customize at both high and low levels.
- **Ideal for Every Use Case**: Proven effective for both simple tasks and highly complex, real-world, enterprise-grade scenarios.
- **Robust Community**: Backed by a rapidly growing community of over **100,000 certified** developers.

## Getting Started

```bash
pip install uv
uv tool install crewai
crewai create crew my_crew
cd my_crew
crewai run
```

## Understanding Flows and Crews

**CrewAI Flows** are the enterprise and production backbone. They provide:
- Structured, event-driven execution with `@start()` and `@listen()` decorators
- State management (persist data across steps)
- Conditional logic, loops, and branching
- Seamless delegation to Crews

**CrewAI Crews** are teams of role-playing agents that collaborate on tasks. Each agent has:
- `role`, `goal`, `backstory` (YAML-configurable)
- Tools (CrewAI tools, LangChain tools, custom tools)
- Memory (short-term, long-term, entity, or unified `Memory` class)
- Optional delegation to other agents

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    backstory='...',
    tools=[search_tool],
    verbose=True
)

task = Task(
    description='Research the latest trends in {topic}',
    expected_output='A summary of top 3 developments',
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential
)
crew.kickoff(inputs={'topic': 'AI agents'})
```

## Key Concepts

### Agents
Autonomous units with `role`, `goal`, `backstory`, tools, memory, max_iter, allow_delegation. YAML or Python definition. Support code execution (Docker or unsafe mode), multimodal inputs, reasoning mode (pre-task planning), and structured output via Pydantic.

### Tasks
Work units with `description`, `expected_output`, `agent`, optional callbacks, output_pydantic/output_json, context injection from other tasks.

### Processes
- `sequential`: tasks run in order, each using previous output as context
- `hierarchical`: a manager agent delegates and orchestrates sub-agents

### Flows
Event-driven orchestration with `@start()`, `@listen()`, `@router()` decorators. Built-in state, UUID tracking, `flow.kickoff()` and `flow.plot()` for visualization.

### Memory
Unified `Memory` class replacing separate short/long/entity memory types. Uses LLM to infer scope/categories/importance. Composite scoring: semantic similarity + recency + importance.

### Tools
`pip install 'crewai[tools]'` for the CrewAI Tools package. Compatible with LangChain tools. Key tools: SerperDevTool, WebsiteSearchTool, FileReadTool, DirectoryReadTool, CodeInterpreterTool, DALL-E Tool, and 30+ others.

## Top-level structure
```
file   .editorconfig
file   .env.test
dir    .github         — CI/CD workflows
file   .gitignore
file   .pre-commit-config.yaml
file   .python-version
file   LICENSE         — MIT
file   README.md
file   conftest.py     — test configuration
dir    docs            — documentation source (Mintlify), includes en/, ko/, ar/, pt-BR/ locales
dir    lib             — library source code (crewai Python package)
file   pyproject.toml  — package metadata and dependencies
file   uv.lock         — lockfile
```
