---
type: source
source_url: https://github.com/forrestchang/andrej-karpathy-skills
tags:
  - claude-code-guidelines
  - karpathy-principles
  - agent-behavior
  - simplicity
  - surgical-changes
  - goal-driven-execution
  - claude-md
  - coding-discipline
related:
  - shareai-lab-learn-claude-code
  - anthropics-skills
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - how-claude-code-works-in-large-codebases
  - nidhinjs-prompt-master
  - gsd-build-get-shit-done
  - obra-superpowers
  - othmanadi-planning-with-files
  - mattpocock-skills
  - garrytan-gstack
  - nadimtuhin-claude-token-optimizer
  - kepano-obsidian-skills
  - coleam00-claude-memory-compiler
  - davidondrej-skills
  - claudemarketplaces.com
  - SnailSploit-Claude-Red
  - agricidaniel-claude-obsidian
product: andrej-karpathy-skills
detail_level: standard
created: 2026-05-11
updated: 2026-07-08
---

`andrej-karpathy-skills` (124,694 stars, MIT) is a single `CLAUDE.md` file — and matching Claude Code plugin skill — that encodes four behavioral principles for AI coding agents, derived directly from Andrej Karpathy's public critique of LLM coding assistants. It is one of the most-starred repositories in the agent-skills ecosystem and represents the community's distillation of Karpathy's observations into actionable, drop-in guidelines: don't assume, don't overcomplicate, don't touch what you weren't asked to touch, and define verifiable success criteria instead of vague imperatives.

_All claims below are sourced from ../../raw/github/forrestchang-andrej-karpathy-skills.md unless otherwise noted._

## What it does

The repository ships one primary artifact — `CLAUDE.md` — containing four principles that address the failure modes Karpathy identified in LLM-assisted coding. It also packages the same principles as a Claude Code plugin skill (`skills/karpathy-guidelines/SKILL.md`) for marketplace install, and as a Cursor project rule (`.cursor/rules/karpathy-guidelines.mdc`) for Cursor users. An `EXAMPLES.md` file provides before/after code examples for each principle.

## Key features

- **Four principles, one file** — the entire behavioral contract fits in a single short `CLAUDE.md`, designed to be merged into any project's existing guidelines.
- **Claude Code plugin** — installable via `/plugin marketplace add forrestchang/andrej-karpathy-skills` + `/plugin install andrej-karpathy-skills@karpathy-skills`; no manual file copying needed.
- **Cursor rule included** — `.cursor/rules/karpathy-guidelines.mdc` applies the same principles in Cursor with zero extra setup.
- **Language-agnostic** — no code in the repo; the guidelines apply to any language or framework.
- **Designed for merging** — explicitly intended to be appended to existing `CLAUDE.md` files alongside project-specific instructions.

## Architecture and concepts

The four principles and what each addresses:

| Principle | Core rule | Problem addressed |
|---|---|---|
| **Think Before Coding** | State assumptions explicitly; present interpretations; push back; stop when confused | Models silently picking wrong assumptions and running with them |
| **Simplicity First** | Minimum code to solve the problem; nothing speculative; rewrite 200-line solutions to 50 if possible | Overcomplication, bloated abstractions, unrequested "flexibility" |
| **Surgical Changes** | Touch only what the request requires; don't "improve" adjacent code; clean up only your own orphans | Orthogonal edits, drive-by refactoring, unexpected side effects |
| **Goal-Driven Execution** | Transform imperative tasks into verifiable goals; state a step-by-step plan with per-step verification checks | Weak success criteria that require constant clarification and human correction |

The Karpathy insight underpinning Goal-Driven Execution: *"LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."*

## Installation

**Claude Code plugin (recommended — applies across all projects):**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Per-project `CLAUDE.md` (new project):**
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

**Append to existing `CLAUDE.md`:**
```bash
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

**Via npx skills CLI:**
```bash
npx skills add forrestchang/andrej-karpathy-skills
```

## When to use

Use this whenever you want to reduce the most common and costly AI coding agent failure modes — silent wrong assumptions, overengineered solutions, untargeted edits, and vague task definitions — without writing custom instructions from scratch. It is the fastest path to applying Karpathy's recommendations to any Claude Code or Cursor project. The guidelines intentionally bias toward caution over speed; for trivial one-liner tasks, use judgment. Add project-specific rules below the Karpathy section to combine general discipline with domain constraints.

## Maintenance status

124,694 stars, 12,672 forks, no primary language (Markdown only), last pushed 2026-04-20. No versioned releases. MIT licensed. Actively referenced in the Claude Code community; the `skills/karpathy-guidelines` plugin is indexed in the [[skills.sh]] official registry and [[anthropics-skills]] ecosystem. The author (forrestchang) also maintains [Multica](https://github.com/multica-ai/multica), an open-source platform for running and managing coding agents with reusable skills.

## Ecosystem

Sits at the intersection of Claude Code behavioral guidelines and the Agent Skills ecosystem. The SKILL.md format connects it to [[anthropics-skills]] (Anthropic's official skills repo) and [[skills.sh]] (the distribution layer). The underlying philosophy — that harness engineers shape agent behavior through environment and instructions, not model training — is the same thesis developed through 12 sessions in [[shareai-lab-learn-claude-code]]. The four principles are a condensed, actionable form of what that curriculum treats as foundational harness engineering discipline.
