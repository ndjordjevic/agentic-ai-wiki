---
type: synthesis
domain: "Agentic AI"
created: 2026-04-25
updated: 2026-04-25
sources:
  - "[[coleam00-claude-memory-compiler]]"
  - "[[runcabinet.com]]"
  - "[[hilash-cabinet]]"
  - "[[gsd-build-get-shit-done]]"
---

# Agentic AI — overview

[[coleam00-claude-memory-compiler]] introduces a concrete, open-source implementation of the Karpathy LLM Knowledge Base pattern applied to AI coding sessions: Claude Code hooks automatically capture conversation transcripts, the Claude Agent SDK distills them into daily logs, and a compiler step organizes those logs into cross-referenced markdown concept articles stored in `knowledge/`. Retrieval is index-guided (no vector database), making the system fast, cheap, and transparent at personal scale (50–500 articles). The repo demonstrates a complete agentic memory pipeline — hook-based capture, background LLM extraction, incremental compilation, and health-checked maintenance — and is the first source in this wiki establishing the foundational patterns for agentic AI memory and self-improving knowledge bases.

[[runcabinet.com]] extends the wiki's coverage from memory-pipeline tooling to full agentic knowledge-base deployment: Cabinet is a self-hosted, file-based "OS for knowledge work" where custom AI agents operate against a persistent markdown knowledge store with goals, skills, and cron-scheduled jobs. Where [[coleam00-claude-memory-compiler]] shows how to build and maintain a knowledge base from AI session transcripts, [[runcabinet.com]] shows what a production system looks like when agents live inside that knowledge base and act autonomously — bridging personal memory compilation to team-scale agent orchestration. Both systems share the Karpathy no-vector-database design principle (index-guided retrieval over flat files), reinforcing that paradigm as a convergent pattern across independent implementations.

[[gsd-build-get-shit-done]] completes the picture of Agentic AI development tooling by representing the meta-prompting and spec-driven development layer — the highest-adoption project in this wiki at 57k+ stars. Where prior sources focus on AI memory (capturing and retrieving knowledge across sessions), GSD focuses on AI execution reliability: imposing a structured phase lifecycle, enforcing quality gates (Nyquist validation, schema drift detection, scope reduction detection), and orchestrating 33 specialized sub-agents across research, planning, execution, and verification. GSD is a runtime-agnostic meta-prompting system — commands are markdown files with XML prompt templates read by the AI at invocation time — making it complementary to, rather than overlapping with, [[hilash-cabinet]] and [[coleam00-claude-memory-compiler]]: those systems build and maintain project knowledge; GSD structures how that knowledge gets acted on. The combination of all three sources captures the full agentic AI stack: memory compilation → persistent knowledge base → structured execution workflow.
