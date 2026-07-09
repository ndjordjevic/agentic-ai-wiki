---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/ruvnet/ruflo
tags:
  - agent-harness
  - meta-harness
  - swarm-coordination
  - mcp-server
  - self-learning
  - vector-memory
  - claude-code-plugin
  - federation
related:
  - paperclipai-paperclip
  - crewai.com
  - skills.sh
  - shareai-lab-learn-claude-code
  - gsd-build-get-shit-done
  - obra-superpowers
  - hermes-agent.nousresearch.com
  - vercel-labs-agent-browser
  - langchain.com-langgraph
  - litellm.ai
  - microsoft-autogen
  - Yeachan-Heo-oh-my-claudecode
product: ruflo
detail_level: standard
created: 2026-07-03
updated: 2026-07-06
---

Ruflo (`ruvnet/ruflo`, formerly Claude Flow) is an open-source agent meta-harness for Claude Code and Codex — 62k+ GitHub stars, MIT license, TypeScript monorepo with a Rust engine backbone (Cognitum.One). It wraps coding agents with an orchestration layer: 100+ specialized agents, swarm topologies with Byzantine/Raft/Gossip consensus, HNSW vector memory (AgentDB), SONA self-learning, 35 Claude Code plugins, ~210 MCP tools, 27 lifecycle hooks, multi-provider LLM routing, zero-trust agent federation, and optional MetaHarness auditing. One `npx ruflo init` installs hooks, MCP server, daemon, and project scaffolding; a lighter plugin-only path adds slash commands without the full loop.

_All claims below are sourced from ../../raw/github/ruvnet-ruflo.md unless otherwise noted._

## What it does

Ruflo is the harness around the model — the execution layer that gives Claude Code or Codex tools, memory, loops, sandboxes, and controls so agents can collaborate rather than run in isolation. The mental model from the README: **Agent = Model + Harness.** Ruflo coordinates swarms (hierarchical, mesh, ring, star, hybrid, adaptive), routes tasks intelligently, persists memory across sessions via AgentDB + HNSW, learns successful patterns through SONA/ReasoningBank, and exposes everything through an MCP server and CLI (`npx ruflo`). It integrates natively with Claude Code (plugins + hooks + MCP), OpenAI Codex (AGENTS.md workflow), and Hermes among other runtimes. Hosted UIs include flo.ruv.io (multi-model MCP chat) and goal.ruv.io (GOAP goal planner with live agent dashboard).

## Installation

**Path A — Claude Code plugins only** (slash commands, no MCP/hooks):

```bash
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
```

**Path B — Full CLI install** (recommended for production):

```bash
# Interactive wizard (all platforms including Windows PowerShell)
npx ruflo@latest init wizard

# One-line POSIX installer
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash

# Register MCP server in Claude Code
claude mcp add ruflo -- npx ruflo@latest mcp start
```

Prerequisites: Node.js 20+, Claude Code installed globally (`npm install -g @anthropic-ai/claude-code`).

## Key features

- **100+ specialized agents** — coder, reviewer, tester, security-architect, queen-coordinator, and domain roles across 8 categories.
- **Swarm & Hive Mind** — 6 topologies, queen-led coordination, Byzantine/Raft/Quorum/Gossip/CRDT consensus, collective memory with TTL namespaces.
- **Self-learning** — SONA neural patterns, ReasoningBank, trajectory learning, 9 RL algorithms, EWC++ memory preservation.
- **Vector memory** — AgentDB with HNSW indexing, RVF binary format, sub-ms retrieval, cross-session persistence.
- **35 Claude Code plugins** — modular marketplace (swarm, RAG memory, federation, security audit, SPARC methodology, neural trader, etc.).
- **~210 MCP tools** — core, intelligence, agents, memory, devtools groups; parallel tool execution in the web UI.
- **27 lifecycle hooks** — auto-route tasks, learn from patterns, coordinate agents in the background after `init`.
- **Multi-provider routing** — Claude, GPT, Gemini, Cohere, Ollama with failover; ruvLLM for local self-improving models.
- **Agent federation** — zero-trust cross-machine collaboration with mTLS + ed25519, PII-gated outbound pipeline, behavioral trust scoring.
- **MetaHarness auditing** — readiness scoring (1–100), MCP security scan, genome fingerprinting, drift detection, `ruflo eject` to standalone toolkit.
- **Security** — AIDefence prompt-injection blocking, CVE remediation, input validation, path traversal prevention.
- **Background workers** — 12 auto-triggered workers (audit, optimize, testgaps, etc.).

## Architecture

V3 is organized as bounded-context npm packages under a DDD layout:

| Module | Role |
|--------|------|
| `@claude-flow/hooks` | 27 event-driven lifecycle hooks, ReasoningBank pattern learning |
| `@claude-flow/memory` | AgentDB, RVF format, HnswLite, SONA persistence, MemoryGraph |
| `@claude-flow/swarm` | 6 topologies, Byzantine consensus, auto-scaling |
| `@claude-flow/neural` | SONA self-learning, 9 RL algorithms |
| `@claude-flow/security` | AIDefence, CVE remediation, validation |
| `@claude-flow/plugins` | WASM RuVector plugins, semantic search |
| `@claude-flow/cli` | 26 commands, 140+ subcommands |
| `@claude-flow/browser` | 59 MCP browser tools (integrates agent-browser) |

Data flow: User → Claude Code/CLI → Orchestration (MCP Server, Router, Hooks) → Swarm Coordination (Queen, Topology, Consensus) → 100+ Agents → Memory & Learning (AgentDB, HNSW, SONA) → LLM Providers.

The orchestrator/executor split in `AGENTS.md` is explicit: Ruflo tracks state and coordinates; the coding agent (Codex, Claude Code) writes code and runs commands. Coordination commands return instantly — the executor must immediately continue with actual work.

Repo layout: `ruflo/` (TypeScript monorepo), `plugins/` (35 native plugins), `v3/goal_ui/` (GOAP planner), `docs/` (USERGUIDE, federation, benchmarks), `crates/` (Rust engine), `.harness/` (metaharness claims).

## Example usage

```bash
# Full init with hooks + MCP + daemon
npx ruflo@latest init wizard

# Hive mind swarm with Byzantine consensus
npx ruflo hive-mind init
npx ruflo hive-mind spawn "Build REST API with tests" --queen-type strategic --consensus byzantine

# Memory: search before starting, store after success
npx ruflo memory search --query "auth refactor patterns"
npx ruflo memory store --key "jwt-middleware" --value "used jose library" --namespace patterns

# MetaHarness audit before shipping
npx ruflo metaharness score --path .
npx ruflo metaharness mcp-scan --path . --fail-on high

# Federation: cross-team agent collaboration
npx ruflo federation init
npx ruflo federation join wss://peer.example.com:8443
```

Codex workflow per `AGENTS.md`: `memory_search` → `swarm_init` → **you execute the code** → `memory_store`. Never stop after a coordination command.

## Maintenance status

62,733 stars, 7,369 forks, TypeScript primary language, default branch `main`, latest release v3.16.3 (2026-07-01 — security release for MCP bridge RCE). MIT license. Homepage: Cognitum.One. Actively maintained with 8.1M+ ecosystem npm downloads. Web UI beta at flo.ruv.io; goal planner at goal.ruv.io. Issues tracked at github.com/ruvnet/claude-flow (legacy name). Community: Agentics Foundation Discord.
