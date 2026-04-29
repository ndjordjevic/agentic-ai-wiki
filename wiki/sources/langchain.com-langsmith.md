---
type: source
source_url: https://www.langchain.com/langsmith
parent_slug: langchain.com
tags:
  - observability
  - agent-evaluation
  - agent-deployment
  - tracing
  - agent-server
related: []
product: langsmith
detail_level: deep
created: 2026-04-29
updated: 2026-04-29
---

LangSmith is LangChain's framework-agnostic platform for understanding, testing, and operating AI agents. Within the broader LangChain platform it supplies the operational layer: tracing and monitoring during development and production, offline and online evaluation loops, and a deployment/runtime story built around Agent Server and managed infrastructure.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## What it does

LangSmith combines observability, evaluation, and deployment into one workflow for AI teams. The docs present it as a place to trace requests, inspect agent behavior, benchmark changes, test against datasets, deploy long-running agents, monitor production quality on live traffic, and manage deployments in one place.

It is intentionally framework-agnostic. The site and docs say teams can trace their preferred framework or custom stack, while the deployment docs explicitly support LangGraph as well as other frameworks.

## Key features

- Structured tracing and monitoring for agent runs.
- Offline and online evaluation workflows tied to datasets and production traces.
- Deployment infrastructure with cloud, hybrid, and self-hosted modes.
- Studio and runtime tools for developing, debugging, and operating deployed agents.
- SDK coverage for Python, TypeScript, Go, and Java.

## Architecture and concepts

LangSmith's operational model centers on a lifecycle: instrument the application, collect traces, turn those traces into evaluations or datasets, then deploy and monitor production runs. The evaluation docs make that feedback loop explicit by feeding failing production traces back into datasets and redeploying after fixes.

On the runtime side, Agent Server is the core systems piece. It organizes work around assistants, threads, runs, cron jobs, persistence, and a task queue. Deployments package graphs with a database and queue, persist checkpoints and long-term memory, and can run in single-host, split API/queue, or distributed modes.

## Main APIs

The main interfaces surfaced in the captured docs are the SDKs plus the Agent Server API. Agent Server exposes assistants, threads, runs, cron jobs, persistence, streaming, and deployment operations, while the deployment docs add higher-level concepts such as RemoteGraph composition, MCP, A2A, and Studio as operator-facing control surfaces.

## When to use

- You need visibility into agent decisions, cost, latency, or failures.
- You want repeatable evaluation loops before and after deployment.
- You need to run long-lived or stateful agents in production.
- You want one platform to connect local development, testing, deployment, and monitoring.

## Ecosystem

LangSmith sits at the center of the LangChain platform. LangChain quickstarts recommend it for tracing, LangGraph docs point to it for debugging and deployment, Fleet relies on LangSmith organization settings and tracing, and LangSmith Deployment exposes protocols like MCP and A2A for broader agent-system interoperability.
