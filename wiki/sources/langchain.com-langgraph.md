---
type: source
source_url: https://www.langchain.com/langgraph
parent_slug: langchain.com
tags:
  - agent-runtime
  - durable-execution
  - human-in-the-loop
  - state-graphs
  - orchestration
related:
  - langchain.com-deepagents
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
  - gsd-build-get-shit-done
  - microsoft-autogen
product: langgraph
detail_level: deep
created: 2026-04-29
updated: 2026-06-10
---

LangGraph is the lower-level orchestration framework and runtime in the LangChain stack. It is designed for long-running, stateful agents that need durable execution, human-in-the-loop pauses, memory, streaming, and explicit control over workflow shape rather than a single high-level agent abstraction.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## What it does

LangGraph provides the primitives for building, managing, and deploying long-running agents and workflows. The docs describe it as low-level and focused on orchestration, while the public product page emphasizes controlled agent behavior, human moderation, persistent memory, streaming, and customizable single-agent and multi-agent flows.

## Key features

- Durable execution with persisted checkpoints.
- Human-in-the-loop via interrupts and resumption.
- Memory for stateful agents across sessions and threads.
- Streaming and runtime visibility.
- Flexible workflow patterns such as routing, orchestrator-worker, and evaluator-optimizer.

## Architecture and concepts

LangGraph is built around explicit graph structure rather than a single hidden loop. The docs use `StateGraph` to model workflows and agents, distinguish fixed workflows from dynamic agents, and document reusable patterns like prompt chaining, parallelization, routing, orchestrator-worker, and evaluator-optimizer loops.

Its human-in-the-loop model is checkpoint-driven. `interrupt()` pauses execution, persists state through the checkpointer, and resumes later through `Command(resume=...)`, with `thread_id` acting as the stable pointer back to saved state. That same persistence model underpins durable execution, debugging, and deployment.

## Main APIs

The captured docs surface `StateGraph`, `Send`, `interrupt()`, and `Command(resume=...)` as the main LangGraph building blocks. They also describe graph compilation, threaded resumption semantics, and the use of LangGraph graphs as deployable units in LangSmith Agent Server.

## When to use

- You need long-running or stateful agents that must survive failure and resume cleanly.
- You want explicit control over workflow structure or multi-agent coordination.
- You need human approval or external input to pause and resume execution safely.
- You have outgrown a higher-level agent abstraction and need runtime-level orchestration.

## Ecosystem

LangGraph is tightly connected to the rest of the [[langchain.com|LangChain]] stack. It commonly uses [[langchain.com-langchain|LangChain]] components for models and tools, recommends [[langchain.com-langsmith|LangSmith]] for debugging and deployment, and underpins the production runtime story that LangSmith Deployment exposes for long-running agent workloads.
