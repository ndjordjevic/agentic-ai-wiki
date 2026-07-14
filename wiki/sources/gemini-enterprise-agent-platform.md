---
type: source
category: "Agent frameworks & SDKs"
source_url: https://cloud.google.com/products/gemini-enterprise-agent-platform
tags:
  - google-cloud
  - vertex-ai
  - agent-development-kit
  - model-garden
  - agent-studio
  - mlops
  - enterprise-agents
  - gemini
related:
  - antigravity.google
  - google-adk-go
  - adk.dev
product: gemini-enterprise-agent-platform
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

Gemini Enterprise Agent Platform is Google Cloud's rebrand and expansion of Vertex AI into a full-stack platform for building, scaling, governing, and optimizing enterprise AI agents. It's Google's answer to the same "agent platform" category as AWS Bedrock AgentCore or Azure AI Foundry — a single console spanning model access, agent-building tools, ML training/serving infrastructure, and governance, positioned as the technical foundation underneath the separate Gemini Enterprise app (which handles agent registration and org-wide governance).

_All claims below are sourced from ../../raw/web/gemini-enterprise-agent-platform.md unless otherwise noted._

## What it does

Agent Platform is a single console where technical teams build, scale, govern, and optimize agents grounded in enterprise data, then hand them off to Gemini Enterprise app for org-wide registration, management, and governance. It bundles four broad capability areas: agent building (Agent Studio, ADK), model access (200+ Google and third-party models via Model Garden), classic ML tooling (notebooks, custom training, prediction, pipelines), and MLOps (model evaluation, registry, feature store, monitoring). The product was formerly branded "Vertex AI" — existing Vertex AI functionality is preserved under the new name.

## Key features

- **Agent building surfaces** — [[antigravity.google|Google Antigravity]] is now available through Agent Platform as "a centralized app to steer, customize, and orchestrate agents," able to deploy multiple agents to execute workflows like product launches (code generation, brand asset creation, email production) concurrently; Agent Studio provides prompt design, testing, and management for Gemini models with natural-language, code, image, and video inputs.
- **Model Garden** — 200+ Google and third-party models, including Gemini 3.5, Anthropic's Claude model family, and open models like Gemma, with tuning options for customization and a dedicated Model Evaluation service for objective, data-driven model assessment.
- **Agent Development Kit (ADK)** — the framework referenced for building, customizing, and fine-tuning sophisticated agents on the platform (see [[google-adk-go]] and [[adk.dev]] for the SDK itself).
- **Classic ML infrastructure** — notebooks (Colab Enterprise or Workbench) natively integrated with BigQuery; Training and Prediction services for reducing training time and deploying models with open-source frameworks and Google's AI infrastructure; custom training with full control over ML framework, training code, and hyperparameter tuning.
- **MLOps tooling** — Model Evaluation, Pipelines (workflow orchestration), Model Registry, Feature Store, and drift/skew monitoring for managing ML projects across teams and the full model lifecycle.
- **Vector Search** — a managed vector search/serving product priced by data size, queries per second, and node count.

## Architecture and concepts

The platform is organized as four "How It Works" entry points on top of one console: **Agent Platform** itself (the unified build/scale/govern/optimize layer), **Agent Studio** (large generative model access, evaluation, tuning, deployment), **Model Garden** (discover/test/customize/deploy open-source and select models), and **Custom training** (full control over the ML training process). Agent Platform is explicitly positioned as the *developer-facing, build-time* layer, while the separate Gemini Enterprise app is the *organization-facing, run-time governance* layer — agents built here get "securely registered, managed, and governed" there once built.

## Main APIs

The Gemini API is accessible from within Agent Platform, with code samples published for Python, JavaScript, Java, Go, and Curl, plus an API-key path for quick testing. Programmatic entry points referenced on the page: the Agent Platform Gemini API setup guide, the ADK build docs, and a public sample-code/notebooks repository at `github.com/GoogleCloudPlatform/vertex-ai-samples` (also `github.com/GoogleCloudPlatform/generative-ai` for generative-AI-specific samples).

## When to use

Use Gemini Enterprise Agent Platform when you want a single GCP-native console spanning agent building, multi-provider model access (including non-Google models like Claude), and classic ML infrastructure (training/serving/MLOps) rather than assembling those pieces from separate open-source tools. It's aimed at enterprises already on Google Cloud who need governance and org-wide agent registration (via the companion Gemini Enterprise app) alongside the build tooling. Compare with [[adk.dev]] / [[google-adk-go]] if you want just the open-source agent-building SDK without the full managed-platform surface, or with [[antigravity.google]] if the entry point you care about is the IDE-style orchestration app rather than the cloud console.

## Ecosystem

Sits at the center of Google's agent stack: [[antigravity.google]] (Google Antigravity) is now surfaced as an app *within* Agent Platform for multi-agent workflow orchestration; the [[google-adk-go]] / [[adk.dev]] Agent Development Kit is the framework referenced for building agents on the platform; Model Garden interoperates with third-party models including Anthropic's Claude family. Pricing is consumption-based across generative AI usage (from $0.0001 per unit), custom training (contact sales), notebooks/compute (Compute Engine/Cloud Storage rates plus management fees), Pipelines ($0.03/run), and Vector Search (usage-based) — with $300 in free credits for new customers. Analyst positioning cited on the page: named a Leader in the 2025 IDC MarketScape for GenAI Life-Cycle Foundation Model Software, the Gartner Magic Quadrant for AI Application Development Platforms (Q4 2025), and the Forrester Wave for AI/ML Platforms (Q3 2024).
