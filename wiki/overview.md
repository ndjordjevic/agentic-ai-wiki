---
type: synthesis
domain: "Agentic AI"
created: 2026-04-25
updated: 2026-04-27
sources:
  - "[[coleam00-claude-memory-compiler]]"
  - "[[runcabinet.com]]"
  - "[[hilash-cabinet]]"
  - "[[gsd-build-get-shit-done]]"
---

# Agentic AI — overview

[[coleam00-claude-memory-compiler]] introduces a concrete, open-source implementation of the Karpathy LLM Knowledge Base pattern applied to AI coding sessions: Claude Code hooks automatically capture conversation transcripts, the Claude Agent SDK distills them into daily logs, and a compiler step organizes those logs into cross-referenced markdown concept articles stored in `knowledge/`. Retrieval is index-guided (no vector database), making the system fast, cheap, and transparent at personal scale (50–500 articles). The repo demonstrates a complete agentic memory pipeline — hook-based capture, background LLM extraction, incremental compilation, and health-checked maintenance — and is the first source in this wiki establishing the foundational patterns for agentic AI memory and self-improving knowledge bases.

[[runcabinet.com]] extends the wiki's coverage from memory-pipeline tooling to full agentic knowledge-base deployment: Cabinet is a self-hosted, file-based "OS for knowledge work" where custom AI agents operate against a persistent markdown knowledge store with goals, skills, and cron-scheduled jobs. Where [[coleam00-claude-memory-compiler]] shows how to build and maintain a knowledge base from AI session transcripts, [[runcabinet.com]] shows what a production system looks like when agents live inside that knowledge base and act autonomously — bridging personal memory compilation to team-scale agent orchestration. Both systems share the Karpathy no-vector-database design principle (index-guided retrieval over flat files), reinforcing that paradigm as a convergent pattern across independent implementations.

[[hilash-cabinet]] is the open-source codebase behind [[runcabinet.com]] — the same product viewed from the implementation side rather than the product-marketing side (the two are grouped under `product: cabinet`). Where the marketing source describes what Cabinet *does*, the GitHub source exposes *how* it is built: a three-tier architecture (data tier on disk, Next.js application tier, unified WebSocket daemon tier), a structured provider adapter layer abstracting Claude Code and Codex behind `claude_local` / `codex_local` adapters, agent personas as files in `.agents/` directories with a `.cabinet` manifest defining cabinet identity and parent–child shared-context paths, and node-cron-driven job scheduling. Together with [[runcabinet.com]] it gives the wiki both the user-facing and engineering-facing view of the same agentic-knowledge-base implementation, which is useful when comparing Cabinet's approach against [[coleam00-claude-memory-compiler]]'s narrower memory-compilation scope.

[[gsd-build-get-shit-done]] completes the picture of Agentic AI development tooling by representing the meta-prompting and spec-driven development layer — the highest-adoption project in this wiki at 57k+ stars. Where prior sources focus on AI memory (capturing and retrieving knowledge across sessions), GSD focuses on AI execution reliability: imposing a structured phase lifecycle, enforcing quality gates (Nyquist validation, schema drift detection, scope reduction detection), and orchestrating 33 specialized sub-agents across research, planning, execution, and verification. GSD is a runtime-agnostic meta-prompting system — commands are markdown files with XML prompt templates read by the AI at invocation time — making it complementary to, rather than overlapping with, [[hilash-cabinet]] and [[coleam00-claude-memory-compiler]]: those systems build and maintain project knowledge; GSD structures how that knowledge gets acted on. The combination of these sources captures the full agentic AI stack: memory compilation → persistent knowledge base → structured execution workflow.
