# forrestchang/andrej-karpathy-skills

## Metadata
- Stars: 124694
- Primary language: (none — Markdown only)
- Default branch: main
- Latest release: none
- License: MIT (per README; licenseInfo not set via API)
- Homepage: (none)
- Fetched: 2026-05-11
- Final URL: https://github.com/forrestchang/andrej-karpathy-skills

## Description
A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. Packages the guidelines as a Claude Code plugin skill (`skills/karpathy-guidelines/SKILL.md`) and a Cursor rule (`.cursor/rules/karpathy-guidelines.mdc`).

## README
# Karpathy-Inspired Claude Code Guidelines

A single `CLAUDE.md` file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

## The Problems

From Andrej's post:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."

> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

## The Solution

Four principles in one file that directly address these issues:

| Principle | Addresses |
|-----------|-----------|
| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity First** | Overcomplication, bloated abstractions |
| **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| **Goal-Driven Execution** | Leverage through tests-first, verifiable success criteria |

## Install

**Option A: Claude Code Plugin (recommended)**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Option B: CLAUDE.md (per-project)**
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
# or append to existing:
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

## Key Insight

From Andrej: "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

## Customization

Designed to be merged with project-specific instructions. Add to existing `CLAUDE.md` or create new. Biases toward caution over speed — use judgment for trivial tasks.

## Docs

### CLAUDE.md — full content

```markdown
# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.
```

### skills/karpathy-guidelines/SKILL.md
Single file skill wrapping the same four principles in SKILL.md format for the Claude Code plugin marketplace.

### .claude-plugin/marketplace.json + plugin.json
Plugin registry metadata declaring the `karpathy-skills` bundle containing `skills/karpathy-guidelines`.

### .cursor/rules/karpathy-guidelines.mdc
Cursor project rule applying the same four principles inside Cursor. See CURSOR.md for setup.

## Top-level structure
```
.claude-plugin/                       — marketplace.json, plugin.json (Claude Code plugin registry)
.cursor/
  rules/karpathy-guidelines.mdc       — Cursor project rule equivalent of CLAUDE.md
CLAUDE.md                             — the primary artifact: four Karpathy-inspired behavioral principles
CURSOR.md                             — Cursor-specific setup guide
EXAMPLES.md                           — real-world before/after code examples for each of the four principles
README.md                             — English documentation
README.zh.md                          — Simplified Chinese translation
skills/
  karpathy-guidelines/
    SKILL.md                          — Claude Code plugin skill wrapping the four principles
```
