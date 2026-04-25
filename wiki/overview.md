---
type: synthesis
domain: "Agentic AI"
created: 2026-04-25
updated: 2026-04-25
sources:
  - "[[coleam00-claude-memory-compiler]]"
  - "[[runcabinet.com]]"
  - "[[hilash-cabinet]]"
---

# Agentic AI — overview

[[coleam00-claude-memory-compiler]] introduces a concrete, open-source implementation of the Karpathy LLM Knowledge Base pattern applied to AI coding sessions: Claude Code hooks automatically capture conversation transcripts, the Claude Agent SDK distills them into daily logs, and a compiler step organizes those logs into cross-referenced markdown concept articles stored in `knowledge/`. Retrieval is index-guided (no vector database), making the system fast, cheap, and transparent at personal scale (50–500 articles). The repo demonstrates a complete agentic memory pipeline — hook-based capture, background LLM extraction, incremental compilation, and health-checked maintenance — and is the first source in this wiki establishing the foundational patterns for agentic AI memory and self-improving knowledge bases.

[[runcabinet.com]] extends the wiki's coverage from memory-pipeline tooling to full agentic knowledge-base deployment: Cabinet is a self-hosted, file-based "OS for knowledge work" where custom AI agents operate against a persistent markdown knowledge store with goals, skills, and cron-scheduled jobs. Where [[coleam00-claude-memory-compiler]] shows how to build and maintain a knowledge base from AI session transcripts, [[runcabinet.com]] shows what a production system looks like when agents live inside that knowledge base and act autonomously — bridging personal memory compilation to team-scale agent orchestration. Both systems share the Karpathy no-vector-database design principle (index-guided retrieval over flat files), reinforcing that paradigm as a convergent pattern across independent implementations.

[[hilash-cabinet]] is the source code complement to [[runcabinet.com]], providing code-level detail on Cabinet's architecture: a three-tier system (file data layer → Next.js app → WebSocket daemon), a provider adapter layer supporting Claude Code and Codex with per-run model overrides, a `.cabinet` manifest format for hierarchical cabinet trees with parent-child context sharing, and a `cabinetai` CLI that auto-manages versioned app installations. This source elevates the wiki's understanding from product-level description to implementation-level architecture, making it possible to reason about how persistent agent memory, multi-model provider switching, and embedded HTML app execution are actually built — and offers a direct comparison point to [[coleam00-claude-memory-compiler]]'s Python/hooks approach to the same persistent-memory problem.
