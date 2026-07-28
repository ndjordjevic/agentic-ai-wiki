---
type: source
category: "Model infra, ML & providers"
source_url: https://www.nvidia.com/en-eu/ai-data-science/products/nemo/
tags:
  - agent-lifecycle-suite
  - microservices
  - nvidia-nim
  - fine-tuning
  - guardrails
  - reinforcement-learning
  - gpu-accelerated
  - nemotron-models
related:
  - nvidia-nemotron-3-ultra
  - nvidia-skillspector
  - huggingface.co
  - pytorch.org
  - ollama-ollama
  - developers.openai.com
product: nemo
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

NVIDIA NeMo is an "agent-first" open suite of libraries, microservices, and foundation models for building, deploying, and optimizing AI agents at GPU scale across cloud, on-premises, or hybrid environments. Rather than a single agent-authoring SDK like [[langchain.com-langgraph]] or [[crewai.com]], NeMo is best understood as an end-to-end agent lifecycle platform spanning data prep, model fine-tuning, guardrails, deployment, and observability — positioning it alongside [[huggingface.co]] and [[pytorch.org]] in this wiki's model-infrastructure category rather than the agent-framework category.

_All claims below are sourced from ../../raw/web/nvidia.com.md unless otherwise noted._

## What it does

NeMo organizes agent development into three lifecycle phases — Build, Deploy, and Optimize — each backed by a dedicated tool or microservice. It integrates with existing AI frameworks and tools rather than replacing them, letting teams bring their own agent-authoring stack while using NeMo for the surrounding data, training, safety, and deployment infrastructure. The `docs.nvidia.com/nemo/` documentation site organizes the suite into six top-level areas: Get Started, Microservices, Framework, Libraries, Blueprints, and Deploy.

## Key features

**Build phase:**
- **NeMo Curator** — data cleaning and preparation for training/fine-tuning datasets
- **NeMo Data Designer** — synthetic dataset creation (Early Access)
- **NeMo Anonymizer** — privacy-preserving data processing
- **NVIDIA Nemotron** — NVIDIA's own foundation models for reasoning and vision (see also [[nvidia-nemotron-3-ultra]])
- **NeMo Evaluator** — model benchmarking

**Deploy phase:**
- **NVIDIA NIM** — optimized, containerized inference microservices
- **NeMo Guardrails** — safety and compliance controls for agent outputs
- **NeMo Auditor** — vulnerability identification

**Optimize phase:**
- **NeMo Relay** — agent monitoring and observation
- **NeMo Customizer** — fine-tuning microservice
- **NeMo RL** — reinforcement-learning techniques for agents
- **NeMo Gym** — simulated training environments

**NeMo Agent Toolkit** (separately documented, `docs.nvidia.com/nemo/agent-toolkit/`) is an open-source, evaluation-focused framework for building and optimizing agentic workflows: it supports building workflows (functions, function groups, LLMs, embedders, retrievers, memory systems, object stores), running them via existing agent frameworks including LangGraph, and exposing them via MCP, FastMCP, or A2A servers. It ships built-in agent patterns (ReAct, Reasoning, ReWOO, Router agents) and third-party integrations (AWS Bedrock, OCI).

## Architecture and concepts

NeMo's documentation groups its components into **NeMo Microservices** (containerized APIs: Data Designer, Customizer, Evaluator, Retriever, Guardrails), the **NeMo Framework** (open-source model-development tooling: Curator, RL, AutoModel, Megatron-Bridge, Run, Export and Deploy, VFM, Skills, Speech, Gym), and the standalone **NeMo Agent Toolkit**. Deployment is handled through **NVIDIA NIM**, **NIM Operator**, and the broader **NVIDIA AI Factory** offering, with **Reference Blueprints** (AI-Q Deep Researcher, Data Flywheel, RAG) provided as jumpstart templates for common agentic use cases.

## Main APIs

The suite is API/microservice-oriented rather than exposing one unified SDK: each component (Curator, Customizer, Evaluator, Guardrails, etc.) ships its own containerized API, while NeMo Agent Toolkit provides Python builders, a CLI, and a plugin/extension system for custom components (per its own docs navigation: Components, Extend, Reference sections covering authentication, builders, CLI commands, data models, LLMs, retrievers, and observability).

## When to use

NeMo fits organizations already committed to NVIDIA GPU infrastructure that want an integrated pipeline from data curation through fine-tuning, safety guardrails, and production inference — particularly enterprises using NVIDIA AI Enterprise for support and security guarantees. Because the NeMo Agent Toolkit explicitly runs workflows built with other frameworks (LangGraph named specifically), NeMo is complementary to rather than competing with agent-authoring frameworks like [[langchain.com-langgraph]], [[crewai.com]], [[agno.com]], and [[mastra.ai]] — teams can keep their existing agent code and adopt NeMo for the surrounding lifecycle infrastructure.

## Ecosystem

NeMo's constituent projects are largely developed under the `github.com/NVIDIA-NeMo` GitHub organization (an org, not a single repo — this page captures the product suite as presented on nvidia.com; individual component repos such as NeMo Curator, NeMo RL, or the NeMo Agent Toolkit would need separate ingests for repo-level detail). NIM microservices underpin the Deploy phase and are shared infrastructure with other NVIDIA AI product lines (Dynamo, cuOpt, Riva). NVIDIA's Nemotron foundation models ([[nvidia-nemotron-3-ultra]]) are the suite's own model family, usable alongside third-party models via [[huggingface.co]] or [[ollama-ollama]] within the same pipeline.
