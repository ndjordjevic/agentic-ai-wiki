---
type: source
source_url: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
tags:
  - claude-code
  - enterprise-adoption
  - claude-md
  - harness-engineering
  - agentic-search
  - skills
  - hooks
  - lsp
related:
  - shareai-lab-learn-claude-code
  - anthropics-skills
  - anthropic.com-managed-agents
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - forrestchang-andrej-karpathy-skills
  - skills.sh
  - coleam00-harness-engineering-demo
  - coleam00-helpline
  - njbrake-agent-of-empires
  - nadimtuhin-claude-token-optimizer
  - happy.engineering
product: claude-code
detail_level: standard
created: 2026-07-01
updated: 2026-07-03
---

Anthropic's official "Claude Code at scale" article documents how Claude Code operates in production across multi-million-line monorepos, legacy systems, and distributed multi-repo architectures — and the configuration, harness, and organizational patterns that separate successful enterprise rollouts from stalled adoption. It argues that agentic filesystem search (not RAG indexing) is Claude Code's navigation model, that the harness extension layer matters as much as the model, and that large-codebase success depends on layered CLAUDE.md files, path-scoped skills, plugins for distribution, LSP for symbol-level navigation, MCP for internal tools, and dedicated ownership for configuration governance.

_All claims below are sourced from ../../raw/web/how-claude-code-works-in-large-codebases.md unless otherwise noted._

## What it does

The article is the first installment in Anthropic's **Claude Code at scale** blog series. It synthesizes patterns observed across real enterprise deployments — monorepos, decades-old legacy code, dozens of microservices, and organizations with thousands of developers — into actionable guidance for teams evaluating or expanding Claude Code. It defines "large codebase" broadly (millions of lines, multi-repo, or unconventional languages like C/C++/C#/Java/PHP) and positions the article as a starting point before org-specific customization via Anthropic's Applied AI team.

## Key features

**Agentic search vs. RAG indexing:** Claude Code navigates like a human engineer — filesystem traversal, file reads, grep, reference following — with no centralized embedding index to build or maintain. RAG-based coding tools fail at scale when embedding pipelines lag active commits; agentic search always works from the live codebase. The tradeoff: navigation quality depends on upfront context setup (CLAUDE.md, skills); vague queries across billion-line repos hit context limits before work begins.

**Harness extension layer (build order matters):**

1. **CLAUDE.md** — loaded every session; root for big picture, subdirectories for local conventions; keep lean to avoid performance drag.
2. **Hooks** — self-improving setup via stop hooks (propose CLAUDE.md updates post-session) and start hooks (dynamic per-module context); deterministic lint/format enforcement.
3. **Skills** — progressive disclosure for specialized expertise; path-scoped activation (e.g., payments deployment skill only in `/payments/`).
4. **Plugins** — bundle skills + hooks + MCP for org-wide distribution via managed marketplaces; prevents tribal knowledge.
5. **LSP** — symbol-level navigation ("go to definition", "find references"); critical for C/C++ and multi-language monorepos; accessed through plugin layer.
6. **MCP servers** — connect to internal docs, ticketing, analytics, structured search tools.
7. **Subagents** — isolated context windows for exploration vs. editing; read-only subagent maps subsystem, main agent edits with full picture.

**Three deployment configuration patterns:**

- **Navigable at scale** — lean layered CLAUDE.md, initialize in subdirectories (not repo root), per-subdirectory test/lint commands, `.ignore` + version-controlled `permissions.deny`, codebase maps for unconventional structures, LSP for symbol search over grep.
- **Active CLAUDE.md maintenance** — review every 3–6 months and after major model releases; rules that compensated for old model limitations become overhead or constraints on newer models.
- **Organizational ownership** — pre-rollout infrastructure investment, agent manager / DRI role, centralized plugin marketplace, approved skills list, cross-functional governance working groups (engineering + security).

## Architecture and concepts

**Navigation model:** No server-side index upload. Each developer's local instance reads the live tree. Quality scales with codebase legibility investment — hierarchical CLAUDE.md loading (additive as Claude walks directories), @-mentioning specific paths, and codebase-map markdown for flat or unconventional layouts.

**Harness > model misconception:** Teams over-index on model benchmarks; the five extension points + LSP + subagents determine real-world performance more than model choice alone.

**CLAUDE.md layering mechanics:** Claude walks up the directory tree loading every CLAUDE.md found; subdirectory initialization scopes work without losing root context. Root file = pointers and critical gotchas only.

**Governance at scale:** Regulated industries need early answers on skill/plugin approval, preventing duplicate internal tooling, and ensuring AI-generated code follows the same review process as human code. Recommended: limited initial access, defined approved skills, required code review, expand as confidence builds.

## Main APIs

Not an API reference — the article covers Claude Code's extension configuration surfaces:

- **CLAUDE.md** — project context files (root + subdirectory)
- **Hooks** — event-triggered scripts (start, stop, tool-use)
- **Skills** — `SKILL.md` packages with progressive disclosure and optional path scoping
- **Plugins** — installable bundles distributed via managed marketplaces
- **LSP plugins** — language-server integrations for symbol navigation
- **MCP servers** — Model Context Protocol connections to internal systems
- **Subagents** — delegated isolated Claude instances
- **`.claude/settings.json`** — `permissions.deny` for version-controlled file exclusions

## When to use

Use this guidance when rolling out Claude Code across large or complex codebases — especially monorepos, legacy systems, multi-repo microservice architectures, or organizations with hundreds/thousands of developers. The patterns apply before broad access: invest in navigability (CLAUDE.md hierarchy, LSP, codebase maps), harness distribution (plugins, approved skills), and organizational ownership (DRI or agent manager) rather than expecting bottom-up adoption to self-organize. Teams already using [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]] or [[forrestchang-andrej-karpathy-skills]] CLAUDE.md templates should read this for enterprise-scale layering (skills over CLAUDE.md, hooks for self-improvement, path scoping). For harness architecture fundamentals, see [[shareai-lab-learn-claude-code]]; for Anthropic's own long-running harness research, see [[anthropic.com-managed-agents]].

## Ecosystem

The article references the broader Claude Code extension ecosystem documented across this wiki: Agent Skills ([[anthropics-skills]], [[skills.sh]]), plugin marketplaces, MCP integrations ([[microsoft-playwright-mcp]] and org-specific servers), and harness engineering patterns ([[coleam00-harness-engineering-demo]], [[njbrake-agent-of-empires]]). Claude Code for Enterprise is the commercial entry point for org-wide deployment. Future installments in the "Claude Code at scale" series will address edge cases (hundreds of thousands of folders, non-git VCS) not covered here.
