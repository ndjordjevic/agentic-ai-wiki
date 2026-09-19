---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/affaan-m/ECC
tags: [claude-code-plugin, multi-harness-adapter, agent-catalog, tdd-enforcement, agent-skills, instinct-based-learning, memory-vault, agentshield-security-scanner]
related: [Yeachan-Heo-oh-my-claudecode, obra-superpowers, davila7-claude-code-templates, deepseek-ai-deepseek-harness, Chachamaru127-claude-code-harness]
product: ecc
detail_level: standard
created: 2026-09-19
updated: 2026-09-19
---

ECC ("Everything Claude Code") is a large, actively-shipped Claude Code plugin — 68 subagents, 292 skills, 94 legacy command shims, hooks, rules, and a cross-harness memory system — packaged as a coordinated "plan → test → implement → review → verify → remember → improve" engineering process rather than a loose grab-bag of prompts. It matters to this wiki as one of the most fully-built examples of an installable, opinionated coding-agent operating layer: it is primary/stable on Claude Code, has a native Codex plugin path, and ships capability-limited adapters for Cursor, OpenCode, Gemini, Zed, GitHub Copilot, Antigravity, Qwen, Kimi Code, Hermes, OpenClaw, CodeBuddy, and JoyCode — with an explicit support-status matrix rather than a claim of full parity across harnesses.

_All claims below are sourced from ../../raw/github/affaan-m-ECC.md unless otherwise noted._

## What it does
ECC installs a coordinated engineering system on top of a coding agent: TDD enforcement (RED → GREEN → REFACTOR with evidence), fresh-context code review, build-error resolvers and code reviewers per language (Go, Python, Java, Rust, Kotlin, C++, F#, TypeScript, Django, Spring Boot, HarmonyOS/ArkTS, and more), a Memory Vault for cross-harness handoffs, instinct-based continuous learning that promotes recurring session patterns into reusable skills, and AgentShield, a separate security scanner (secrets, permissions, hook injection, MCP risk, agent-config review) that can run adversarial red-team/blue-team/auditor passes with three Opus agents. The project is model-agnostic at the transport layer — it works through any Anthropic-compatible gateway or self-hosted endpoint the harness is already configured with.

## Installation
The recommended path is a guided installer, `npx ecc-universal@2.2.1 setup` (also runnable via pnpm/yarn/bun), which inventories the official marketplace and every native Claude install scope before writing anything, and can be re-run to update, change scope, or change hook profile. A multi-harness variant (`ecc-universal install --guided`) configures Claude Code, Codex, and Kimi Code together in one reviewed flow. Claude Code's native path is `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc`; Codex has an equivalent native marketplace/plugin flow (`codex plugin marketplace add` / `codex plugin add ecc@ecc`). The project is explicit that installing the same harness twice via different methods (e.g. the plugin plus a full manual `install.sh --profile full`) duplicates skills, commands, and hooks, and documents a specific uninstall/reset order to recover from a stacked install.

## Key features
- **68 subagents** for planning (planner, architect), TDD (tdd-guide), review (code-reviewer, security-reviewer, and ~20 language/framework-specific reviewers and build-error resolvers), ML pipeline review (mle-reviewer), RAG pipeline review (rag-pipeline-reviewer), and harness tuning (harness-optimizer, loop-operator).
- **292 skills** as the canonical workflow surface (commands/ is being phased out in favor of skills), spanning TDD, security review, per-language/per-framework patterns (Django, Laravel, Spring Boot/Quarkus, Rails, Go, Python, Swift, Perl, C++), continuous-learning-v2 (confidence-scored instinct extraction), unified-memory (the Memory Vault), and ito-compute (a GPU-compute RFQ bridge to a separate "Itô" provider).
- **AgentShield**: a standalone, separately installed security auditor (`ecc-agentshield` on npm) covering secrets detection, permission auditing, hook-injection analysis, MCP server risk profiling, and agent-config review, with 102 static analysis rules and an optional three-Opus-agent adversarial deep-analysis mode (`--opus --stream`).
- **Memory Vault** (`ecc memory`): a portable, Markdown-based (`ecc.memory.v1`) cross-harness memory format for project/team/user-scoped handoffs between Claude, Codex, Hermes, OpenClaw, and Kimi, explicitly documented as unreviewed context rather than executable policy.
- **GateGuard**: built-in guardrails that gate destructive shell commands (`rm`, force/path `git checkout`, destructive `find -exec`) before they run.
- Token-optimization guidance baked into the docs (recommended `sonnet` default, capped `MAX_THINKING_TOKENS`, earlier auto-compact threshold) and a `/context-budget` command for trimming loaded rules and MCP servers.

## Architecture and concepts
The repo root (`agents/`, `skills/`, `commands/`, `rules/`, `hooks/`, `scripts/`) is the single source of truth; every harness-specific directory (`.cursor/`, `.codex/`, `.opencode/`, `.zed/`, `.gemini/`, `.kimi/`, `.hermes/`, `.openclaw/`, `.codebuddy/`, `.qwen/`, `.kiro/`, `.pi/`, `.trae/`, `.adal/`) is described as an adapter that packages or maps those same workflows rather than maintaining a separate copy. Root `AGENTS.md` is the universal cross-tool instruction file read natively by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot instead reads `.github/copilot-instructions.md` plus `.github/prompts/*.prompt.md` files, since Copilot has no hook system or subagent API. A DRY adapter pattern lets Cursor reuse Claude Code's Node.js hook scripts by transforming Cursor's larger hook-event surface (20 events vs Claude Code's 8) through `.cursor/hooks/adapter.js`. Skills use a shared `SKILL.md` + YAML-frontmatter format that is portable across Claude Code, Codex, and OpenCode.

## Example usage
```
npx ecc-universal@2.2.1 setup                 # guided Claude Code plugin install/update
npx ecc-universal@2.2.1 install --guided \
  --harness claude --harness codex --harness kimi \
  --claude-scope local --claude-hooks standard --profile core --yes

/ecc:plan "Add user authentication with OAuth"  # planner creates an implementation blueprint
tdd-workflow skill                              # tdd-guide enforces write-tests-first
/code-review                                    # code-reviewer checks the work from a fresh context

agentshield scan --path .                       # scan the agent/hook/MCP config surface
agentshield scan --path . --opus --stream       # three-Opus red-team/blue-team/auditor deep scan
```
(../../raw/github/affaan-m-ECC.md)

## Maintenance status
262,260 GitHub stars and 39,232 forks as of fetch time, MIT license, current release v2.2.1 (2026-09-08), pushed as recently as 2026-09-19. The README describes itself as maintained by a single primary developer who ships weekly across seven harnesses, funded by GitHub Sponsors and a paid "ECC Pro" hosted GitHub App tier for private-repo scanning; the OSS core itself stays MIT-licensed. A per-harness support-status table distinguishes "stable primary" (Claude Code), "supported native plugin" (Codex), "beta" (Cursor, OpenCode), "instruction-only" (GitHub Copilot), and "experimental/minimal" (Gemini, Zed, Antigravity, Qwen, Hermes, OpenClaw, Kimi, CodeBuddy, JoyCode) adapters, along with named open OS-specific defects (a macOS Bash 3.2 incompatibility in one shell path, open Windows-native defects in the continuous-learning observer daemon and memory-vault writes). (../../raw/github/affaan-m-ECC.md)

## Ecosystem
ECC positions itself in the same "agent harness" space as [[Yeachan-Heo-oh-my-claudecode]] (multi-agent Claude Code orchestration plugin) and [[Chachamaru127-claude-code-harness]] (a smaller, Go-native multi-harness harness), and shares the skills-as-canonical-surface philosophy of [[obra-superpowers]]. Its component-catalog framing (agents/skills/commands/rules counted and browsable, with a desktop Tkinter dashboard) echoes [[davila7-claude-code-templates]]'s catalog approach, though ECC ships the components as an installable plugin/CLI rather than a template gallery. Its plugin-based architecture with everything as a swappable module is a narrower, Claude-Code-first counterpart to [[deepseek-ai-deepseek-harness]]'s fully composable model-adapter/tool/subagent plugin system. Optional multi-model orchestration commands (`/multi-plan`, `/multi-execute`, etc.) depend on a separate, non-bundled `ccg-workflow` runtime; optional GPU compute access depends on a separate "Itô" CLI and compute marketplace that ECC explicitly does not bundle, audit, or provision on its own.
