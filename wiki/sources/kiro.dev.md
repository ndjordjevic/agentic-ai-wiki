---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://kiro.dev/
tags: [coding-agent, ide, cli, spec-driven-development, hooks, steering, aws, agent-skills, mcp]
related: [herdr.dev, cognition.ai, factory.ai]
product: kiro
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

Kiro is a coding agent from Amazon available as an IDE, CLI, and web interface — the successor to Amazon Q Developer. Its defining approach is **spec-driven development**: rather than vibe-coding from prompts, Kiro formalizes feature work into three structured artifacts (requirements, design, tasks) and executes tasks with parallel agents, dependency-aware wave scheduling, and real-time progress tracking. Kiro also brings **hooks** (event-triggered automations that run on file save, tool use, spec task start, etc.) and **steering** (persistent markdown context files that keep Kiro aware of your tech stack, architecture, and conventions across all sessions). A shared Kiro Agent Server engine powers IDE, CLI, and web under a unified model.

_All claims below are sourced from ../../raw/web/kiro.dev.md unless otherwise noted._

## What it does

Kiro helps developers transform ideas into working software through structured, agent-driven workflows:

- **Specs** — three-phase workflow (Requirements/Bug Analysis → Design → Tasks) that produces `requirements.md`, `design.md`, and `tasks.md`. Feature Specs and Bugfix Specs. Quick Plan auto-generates all three artifacts without approval gates. Tasks run with dependency-graph wave scheduling — independent tasks execute concurrently within each wave.
- **Hooks** — event-driven automations stored in `.kiro/hooks/` or `~/.kiro/hooks/`. Trigger on file save/create/delete, pre/post tool use, pre/post spec task, user prompt submission, or session start. Actions are agent prompts or shell commands; blocking hooks (exit code 2) can prevent tool use or prompt execution.
- **Steering** — persistent markdown context at workspace scope (`.kiro/steering/`) or global scope (`~/.kiro/steering/`). Supports three foundational files (product, tech, structure) plus custom files with `fileMatch` inclusion modes. Compatible with the AGENTS.md standard.
- **Powers** — dynamic loading of context and MCP servers for instant framework expertise
- **Agent Skills** — portable instruction packages using the open Agent Skills standard
- **MCP** — connect to Model Context Protocol servers for additional tools and context

## Key features

- **Three interfaces, one engine** — IDE (VS Code-based), CLI (terminal with rich TUI, headless mode, ACP protocol), and Web (browser-based with autonomous mode, scheduled automations, isolated sandbox). CLI 3.0 unifies all three on the Kiro Agent Server.
- **Spec-driven development** — formal requirements → design → tasks pipeline with parallel task execution; distinguishes spec work from exploratory vibe coding.
- **Hooks system** — 10 trigger types covering the full agent lifecycle; workspace and user-level scope; natural language hook creation ("Ask Kiro to create a hook").
- **Steering files** — workspace and global scope; `always` or `fileMatch` inclusion modes; team-deployable via MDM/Group Policy; AGENTS.md-compatible.
- **Multi-model access** — Claude Opus 4.8 through Qwen3 Coder Next (0.05x cost), plus Auto routing. Free tier includes Claude Sonnet 4.5, DeepSeek 3.2, MiniMax M2.5, Qwen3 Coder Next, GLM-5.
- **Code Intelligence (CLI)** — tree-sitter built-in, optional LSP integration, symbol search, pattern matching, codebase exploration.
- **Agent Client Protocol (ACP)** — Kiro CLI can run as an ACP-compliant agent for programmatic client integration.

## Architecture and concepts

Kiro's configuration and artifacts follow an `.kiro/` convention:
- `.kiro/hooks/` — workspace hook JSON files
- `.kiro/steering/` — workspace steering markdown files
- `.kiro/specs/` — spec artifacts (requirements, design, tasks)

Global equivalents at `~/.kiro/hooks/`, `~/.kiro/steering/`. Workspace settings override global settings.

The **Kiro Agent Server** (CLI 3.0, early access) is a unified runtime that powers IDE, CLI, and Web from the same engine — enabling consistent behavior across interfaces. The CLI also exposes an **Agent Client Protocol (ACP)** endpoint for programmatic integration.

Steering file **inclusion modes**: `always` (default, loaded into every interaction) or `fileMatch` (loaded only when working with matching files via `fileMatchPattern` YAML front matter). This lets teams separate universal conventions from domain-specific guidance (e.g. React component standards load only for `.tsx` files).

## Main APIs

**CLI commands (selection):**
```bash
kiro                        # launch interactive chat
kiro --headless             # non-interactive mode for CI/CD
kiro --v3                   # use CLI 3.0 (Kiro Agent Server)
```

**Hooks JSON schema:**
```json
{
  "version": "v1",
  "hooks": [{
    "name": "lint-on-save",
    "trigger": "PostFileSave",
    "matcher": "\\.ts$",
    "action": { "type": "command", "command": "npm run lint" },
    "timeout": 30,
    "enabled": true
  }]
}
```

**Steering file with fileMatch inclusion:**
```markdown
---
inclusion: fileMatch
fileMatchPattern: "components/**/*.tsx"
---
Always use functional components. Prefer hooks over class components...
```

**Models:** `Auto` (default), Claude Opus/Sonnet/Haiku, DeepSeek 3.2, MiniMax M2.5, GLM-5, Qwen3 Coder Next.

## When to use

Use Kiro when:
- Building complex features that benefit from formal requirements and design documentation before coding
- Debugging where systematic root cause analysis and regression prevention matters
- Running automated quality gates (lint, tests, security checks) automatically via hooks
- Working in large codebases where persistent steering context replaces per-session explanation
- CI/CD automation requiring headless agent execution
- Teams that want consistent standards enforced across every developer session via team-deployed steering files

Use vibe/chat mode within Kiro for quick exploratory coding and prototyping.

## Ecosystem

Kiro is the successor to Amazon Q Developer (migration guides for both IDE and CLI). It supports MCP servers for external tool integration, the open Agent Skills standard for portable instruction packages, and the AGENTS.md standard for steering. Kiro CLI is supported by [[herdr.dev]] as a detected agent. Comparable coding agent IDEs include [[cognition.ai]] (Devin) and [[factory.ai]] (Droids). Plans: Free, Pro ($19/mo), Pro+ ($39/mo), Power ($79/mo), with per-model credit pricing.
