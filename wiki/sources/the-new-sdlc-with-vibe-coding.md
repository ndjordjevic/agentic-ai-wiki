---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://drive.google.com/file/d/1IR7CddF_2FyQo_PdfBNTaEA50EGiVt2r/view
tags:
  - vibe-coding
  - agentic-engineering
  - sdlc
  - context-engineering
  - harness
  - developer-workflow
  - ai-development
  - agent-skills
  - factory-model
  - pdf
  - whitepaper
related:
  - coleam00-harness-engineering-demo
  - anthropic.com
  - skills.sh
  - bmad-code-org-bmad-method
  - greptile.com
  - qa.tech
  - goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b
  - buildermethods-agent-os
  - agents-cli
  - antigravity.google
  - othmanadi-planning-with-files
  - lovable.dev
  - bolt.new
product: the-new-sdlc-with-vibe-coding
detail_level: standard
created: 2026-06-30
updated: 2026-07-01
---

[[the-new-sdlc-with-vibe-coding]] is a 51-page whitepaper by Addy Osmani, Shubham Saboo, and Sokratis Kartakis (May 2026), published as Day 2 in Google's Agents Whitepaper Series. It provides the most comprehensive published framework for understanding how AI is reshaping the software development life cycle — specifically, how to move from casual "vibe coding" to disciplined "agentic engineering." It is foundational reading for any engineering team adopting AI coding agents at scale, supplying the mental models, spectrum taxonomy, economic analysis, and actionable guidance that connect abstract AI capabilities to daily engineering practice.

_All claims below are sourced from ../../raw/web/the-new-sdlc-with-vibe-coding.md unless otherwise noted._

## What it does

The paper traces the full arc of AI-assisted software development: from the emergence of vibe coding as a term and practice, through the intermediate modes of structured AI assistance, to the disciplined discipline of agentic engineering. It defines the spectrum between these endpoints across six dimensions (intent specification, verification, codebase understanding, error handling, scope, and risk profile), then systematically examines how each phase of the SDLC is transformed by AI. The paper introduces and names three major conceptual frameworks — the spectrum, the harness, and the factory model — and closes with actionable starting points for individual developers, engineering leaders, and organizations.

## Key arguments and concepts

### The vibe coding to agentic engineering spectrum

The spectrum's key differentiator is not whether AI is used — it's how much structure, verification, and human judgment surrounds the AI's output. At the vibe coding end: casual prompts, no systematic verification, copy-paste error recovery, high risk, fine for disposable prototypes. At the agentic engineering end: formal specs and AGENTS.md files, automated test suites and CI/CD gates, LM judges for evals, self-diagnosing agents within defined bounds, appropriate only for production systems. Most professional work falls somewhere in between.

The single sharpest discriminator is **verification**: tests check deterministic outputs; evals check non-deterministic trajectories (did the agent use the right tools, take the right steps). Without both, the practice is always vibe coding, regardless of prompt sophistication.

### Context engineering as the real skill

The insight that prompt cleverness matters less than context quality has given rise to **context engineering** — providing AI agents with rich, structured information about the codebase, architecture, conventions, and intent. Six types of context every agent needs: Instructions, Knowledge, Memory, Examples, Tools, and Guardrails.

The critical design decision is **static vs. dynamic context**: static (system prompts, rule files, persona definitions) is always present and expensive per token; dynamic (skills, RAG results, tool outputs) is loaded on demand and costs tokens only when needed. **Agent Skills** are the primary pattern for dynamic context: structured, portable packages of procedural knowledge that load only when task-matched, allowing an agent to carry dozens of specializations while paying for only one at a time. Skills solve four persistent problems: context rot from overloaded prompts, absent procedural memory for LLMs, operational overhead of multi-agent architectures, and the need for portability across tools.

### The harness: Agent = Model + Harness

The model is not the agent. A raw model becomes an agent only once a harness provides it state, tool execution, feedback loops, and enforceable constraints. The behavior developers experience with Claude Code, Cursor, Codex, or Cline is dominated by what the harness does — not by which model is underneath. The harness has six components: Instructions/Rule Files, Tools, Sandboxes, Orchestration Logic, Guardrails/Hooks, and Observability.

The evidence is striking: on Terminal Bench 2.0, one team moved a coding agent from outside the Top 30 to the Top 5 by changing only the harness with no model change. A LangChain study raised a benchmark score by 13.7 points by tweaking only the system prompt, tools, and middleware around a fixed model. **Most agent failures, examined honestly, are configuration failures** — a missing tool, a vague rule, an absent guardrail, or a noisy context window — not model failures.

The harness maps directly to SDLC phases: Requirements/Planning = configuring the harness (AGENTS.md, rule files, tool access definitions); Implementation = running the harness (sandboxes, tool execution); Testing/QA = the feedback loop (orchestration routes failures back to model); Code Review/Deployment/Maintenance = observing the harness (hooks block unsafe commits, observability tracks token costs and agent drift).

### The factory model

The developer's primary output is no longer code — it's the system that produces code: specifications, agents, test suites, feedback loops, and guardrails. The factory manager analogy: the developer designs the assembly line and ensures quality control, rather than assembling widgets by hand. The shift is from giving agents step-by-step instructions to giving agents success criteria and letting them iterate.

### Conductor vs. orchestrator developer roles

Developers move fluidly between two modes:
- **Conductor** (real-time direction): watching code appear in the IDE, making moment-to-moment corrections. Tools: GitHub Copilot, Gemini Code Assist, Cursor, Windsurf. Risk: bottleneck if every keystroke needs human direction.
- **Orchestrator** (async delegation): defining goals at a high level, assigning to background agents, reviewing results. Tools: Google Jules, GitHub Copilot agent mode, Claude Code. Requires specification, decomposition, evaluation, and system design skills.

The orchestrator role demands a fundamentally different skill set from traditional software engineering — the same skills that make humans irreplaceable in agentic systems.

### The 80% problem

AI agents rapidly generate ~80% of code for a feature; the remaining 20% — edge cases, error handling, integration points, subtle correctness requirements — requires deep contextual knowledge current models often lack. The failure modes have evolved from visible syntax errors to insidious conceptual failures: wrong business logic assumptions, missing edge cases, architectural decisions that create long-term maintenance burdens. The code "looks right" and may pass basic tests. The effective response is to reserve human attention for what AI struggles with (ambiguous requirements, architectural trade-offs, correctness verification) while using AI for what it excels at (rapid implementation of well-specified tasks).

### Three places coding agents appear in daily work

1. **In the editor:** inline completions, chat panels, codebase-aware suggestions (Copilot, Cursor, Windsurf, JetBrains)
2. **In the terminal:** full codebase access, multi-file edits, tool execution, iterate on failures (Claude Code, Codex CLI, Antigravity, Cline, OpenCode)
3. **In the background:** autonomous cloud-hosted sandbox runs producing PRs (Jules, Copilot agent mode, Cursor background agents, AlphaEvolve)

### Production-ready agents via vibe coding workflow

The prototype-to-production path has collapsed. The same terminal-based workflow now produces production agents with persistent memory, scoped permissions, eval coverage, and observability. Google's Agents CLI packages this as seven skills covering the full ADK lifecycle — scaffold, write, evaluate, deploy, observe — so developers never leave their preferred coding agent. Coordination protocols: MCP for tool access, A2A for cross-agent delegation.

## Economics: CapEx vs. OpEx

Vibe coding appears cheap (low CapEx: just a subscription) but hides massive compounding OpEx: token burn from prompting loops with low first-pass success, maintenance tax on unstructured "spaghetti" AI code, and expensive security remediation in production. Agentic engineering inverts this: higher upfront CapEx (schema design, test suite construction, context structuring) yields dramatically lower marginal OpEx per feature shipped. Context engineering is explicitly a financial strategy — dense high-signal context vs. raw 100k-token repository dumps. Intelligent model routing (frontier models for complex decisions, small fast models for deterministic tasks) compounds the cost reduction.

## Actionable recommendations

**Individual developers:**
- Write AGENTS.md first (stack, conventions, hard rules, workflow); add a rule each time the agent misbehaves
- Install agent skills for your coding agent (Agents CLI or equivalent)
- Pick one repetitive workflow as the first agent to build end-to-end
- Write tests and evals before generating code — they are the contract with the AI
- Review every line the agent produces that ships; be skeptical of anything that looks clever
- Maintain core engineering skills (debugging, system design, performance intuition) — AI multiplies your expertise, not your ignorance

**Engineering leaders:**
- Treat context engineering artifacts (AGENTS.md, system prompts, eval suites, skill libraries) as first-class code: versioned, reviewed, owned
- Set the bar at the eval, not the demo; define scoring rubrics (task success, tool use quality, trajectory compliance, hallucination, response quality)
- Retrain reviewers on AI failure modes: hallucinated dependencies, inadequate error handling, subtle correctness gaps
- Make the vibe-coding vs. agentic-engineering boundary explicit in team norms — which environments warrant which mode
- Build and maintain shared harness infrastructure: system prompts, skill libraries, MCP connections, eval harnesses

**Organizations:**
- Treat AI-assisted development as engineering investment; pair AI tooling with eval coverage, observability, and architectural standards
- Build the production substrate (trajectory evals in CI, full traces, scoped permissions, security review) before the first production agent ships
- Adopt MCP (tool access) and A2A (cross-agent delegation) as open standards to preserve multi-vendor flexibility
- Plan for hybrid human-agent teams with explicit handoff protocols; agents are participants, not just tools
- Reframe hiring and development around judgment, specification, evaluation, and architectural review — not implementation velocity

## Three durable principles

1. **Structure scales, vibes don't.** Production software needs the full agentic engineering discipline.
2. **AI amplifies your engineering culture.** It multiplies both strengths and weaknesses.
3. **The human role is evolving, not diminishing.** Architecture, specification, evaluation, and system design become the primary craft.

> *"Generation is solved. Verification, judgment, and direction are the new craft."*

## Ecosystem connections

This paper names and contextualizes most of the major tools in this wiki: [[skills.sh]] (Agent Skills ecosystem); Claude Code, Cursor, Codex (conductor tools); Jules, Copilot agent mode (orchestrator tools); MCP (tool protocol); A2A (inter-agent delegation); AGENTS.md / CLAUDE.md / GEMINI.md (rule files). The harness concept underpins [[coleam00-harness-engineering-demo]] (a live implementation of harness engineering). The factory model and spec-first approach connect to [[bmad-code-org-bmad-method]], [[buildermethods-agent-os]], and [[othmanadi-planning-with-files]]. The evals-in-CI recommendation aligns with [[greptile.com]] (AI code review) and [[qa.tech]] (AI E2E testing). The workflow methodology sections complement [[goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b]] (Cole Medin's complete agentic coding workflow). The context engineering framework is the conceptual grounding for skills hosted on [[skills.sh]], and the harness anatomy maps directly to [[anthropic.com]]'s harness design principles for long-running apps.
