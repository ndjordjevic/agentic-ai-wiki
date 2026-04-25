---
type: synthesis
domain: "Agentic AI"
created: 2026-04-25
updated: 2026-04-25
sources:
  - "[[coleam00-claude-memory-compiler]]"
---

# Agentic AI — overview

[[coleam00-claude-memory-compiler]] introduces a concrete, open-source implementation of the Karpathy LLM Knowledge Base pattern applied to AI coding sessions: Claude Code hooks automatically capture conversation transcripts, the Claude Agent SDK distills them into daily logs, and a compiler step organizes those logs into cross-referenced markdown concept articles stored in `knowledge/`. Retrieval is index-guided (no vector database), making the system fast, cheap, and transparent at personal scale (50–500 articles). The repo demonstrates a complete agentic memory pipeline — hook-based capture, background LLM extraction, incremental compilation, and health-checked maintenance — and is the first source in this wiki establishing the foundational patterns for agentic AI memory and self-improving knowledge bases.
