---
type: source
source_url: https://youtu.be/goOZSXmrYQ4
tags: [greenfield-development, piv-loop, ai-layer, prd-creation, prime-command, subagents, on-demand-context, agentic-coding-workflow]
related:
  - coleam00-archon
  - anombyte93-prd-taskmaster
  - bmad-code-org-bmad-method
  - backnotprop-plannotator
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
product: agentic-coding-workflow
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

A 42-minute walkthrough by Cole Medin of his complete greenfield agentic coding workflow built around a dead-simple AI layer (PRD + global rules + commands + subagents) and a three-phase PIV loop (Plan, Implement, Validate) that lets a solo developer build production-grade software with Claude Code in hours instead of weeks — demonstrated live by building a self-hosted Linktree-style link-in-bio app.

_All claims below are sourced from ../../raw/youtube/goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b.md unless otherwise noted._

## What the video is about

Cole Medin presents a practical greenfield AI coding framework that avoids over-engineering. The framework has two main phases: first, setting up the AI layer — the collection of context assets a coding agent needs at the start of a project (PRD, global rules, reusable commands, and subagents for research); second, running a repeating PIV loop (Plan, Implement, Validate) for each feature or phase of work. The video critiques over-engineered multi-agent systems and more complex frameworks like BMAD and GitHub Spec Kit as harder to personalize, while positioning this workflow as a minimal, evolvable starting point. The live demo builds a self-hosted link-in-bio page builder from scratch using Claude Code, walking through every phase in real time.

## Key points by chapter

**The Dead Simple Framework for AI Coding**
The framework is intentionally minimal: two phases (AI layer setup, then PIV loops), all universal across coding agents. Brownfield (existing codebase) workflows are treated as a separate topic. The AI layer starter kit is published in a GitHub repo linked in the description (`coleam00/link-in-bio-page-builder`, see `.claude/`).

**Creating the AI Layer for Your Codebase**
The AI layer consists of: (1) a PRD (`prd.md`) capturing scope and architecture; (2) a global rules file (`AGENTS.md` or `CLAUDE.md`) capturing permanent conventions; (3) reusable commands/skills, with a `/prime` command as the most important; (4) a `reference/` folder for on-demand context files. The AI layer is designed to be generic at start and progressively specialized as the codebase grows. Simpler than BMAD or Spec Kit by design — easier to make your own.

**PRD Creation - The Ultimate Planning Tool**
PRD creation starts as a casual unstructured conversation with the agent about the idea, tech stack, and rough architecture. Once enough context is established, a `/create-prd` command formalizes the conversation into a structured PRD. Subagents run research in parallel during PRD creation. The PRD covers the initial greenfield build only; future features shift to brownfield development.

**Subagents for Research**
Subagents are used exclusively for research and planning — never for implementation, because implementation requires the full context of files being edited. The key principle is context isolation: research subagents load tens or hundreds of thousands of tokens but return only their summary findings to the main context, keeping the primary context window clean. Claude Code has built-in exploration and research subagents; other agents may require manual subagent setup.

**Global Rules and On Demand Context**
Global rules (`AGENTS.md`) hold constraints that should always be in context: run commands, testing strategy, logging conventions, and style guidelines. On-demand context files live in `reference/` and are loaded only when relevant (e.g., a front-end component guide loaded only during front-end work). This keeps the always-loaded context lean. Rules evolve most aggressively as the codebase grows.

**The Prime Command**
The `/prime` command runs at the start of every new Claude Code session. It guides the agent through codebase exploration — reading documentation, checking git log for history, identifying main entry points — and outputs a summary of its mental model. The developer validates this understanding before starting feature work. The git log serves as long-term memory, letting the agent understand how the codebase has evolved. The prime command is designed to evolve as the project matures.

**The PIV Loop Framework**
PIV = Plan, Implement, Validate. Each iteration takes a focused unit of work (usually one PRD phase) through three stages: (1) Plan — vibe planning conversation, then a structured plan created with a `/plan` command, using subagents for codebase analysis; (2) Implement — the `/execute` command runs the plan in a fresh context window, delegating all coding to the agent; (3) Validate — human code review plus live manual testing, then add regression tests via a test command. The plan document is the only context passed to the execute command, keeping implementation context minimal and clean.

**Live Feature Implementation + Validation**
A live demo of a full PIV loop implementing the complete link-in-bio app (user accounts, link management, analytics, public profiles). The `/execute` command is invoked with the plan path; the agent implements end-to-end with screenshot validation. Human validation follows: code review (for technical reviewers) plus manual live testing. The demo shows the resulting app working with display names, avatars, and link management within one PIV cycle.

**Keeping Your Codebase Reliable**
After the initial foundation, a regression testing framework is essential. The strategy: after each PIV loop, generate an end-to-end test command from the agent's own test log, so future loops can verify prior features still work. Third-party tools like QA Tech (AI testing agents that adapt as the codebase grows) can automate this. Building and maintaining this test harness is incremental and runs in parallel with feature development.

**Evolve Your Coding Agent Over Time**
When a bug is found, the response has two tracks: fix the code, and fix the AI layer so it cannot happen again. This might mean adding rules, refining on-demand context, or adding a test command. Three parallel tracks compound over time: codebase, test base, and AI layer all grow together, making the coding agent progressively more reliable and specific to the project. Example: discovering a style preference gap led to adding explicit style guidelines to the rules file and front-end on-demand context.

## Notable quotes

> "You don't want to spend more time creating your agentic coding workflows than you do actually coding."

> "I don't recommend using sub-agents for implementation, because with implementation we usually care about all of the context of the files that we've been editing and creating."

> "We are doing three things in parallel. As we're building out our code base, we are evolving our test base, our code base, and our AI layer. And man, does that compound over time."

## Speaker context

Cole Medin is a developer and content creator focused on agentic AI coding systems, running the Dynamous community and Agentic Coding Course at `dynamous.ai`. The video is a companion to the GitHub repo `coleam00/link-in-bio-page-builder` which contains the starter AI layer (commands, rules) used in the demo. A follow-up brownfield development video is referenced as forthcoming.
