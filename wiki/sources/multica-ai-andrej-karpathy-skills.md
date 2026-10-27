---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/multica-ai/andrej-karpathy-skills
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
  - forrestchang-andrej-karpathy-skills
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - obra-superpowers
  - shareai-lab-learn-claude-code
  - gsd-build-get-shit-done
  - dietrichgebert-ponytail
  - mattpocock-skills
product: andrej-karpathy-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

multica-ai/andrej-karpathy-skills (225,112 stars) is a single `CLAUDE.md` of four behavioral principles — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution — derived from Andrej Karpathy's observations on LLM coding pitfalls. It carries the same four principles as [[forrestchang-andrej-karpathy-skills]]; this Multica-org copy is the higher-starred listing and its README banner promotes the Multica platform (an open-source platform for running and managing coding agents with reusable skills). The content is the Karpathy CLAUDE.md; the install commands in the README still point at the `forrestchang/andrej-karpathy-skills` repo. See also [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]].

_All claims below are sourced from ../../raw/github/multica-ai-andrej-karpathy-skills.md unless otherwise noted._

## What it does

The README quotes Karpathy's complaints: models make wrong assumptions and run with them unchecked, overcomplicate code and APIs (1000 lines where 100 would do), and change or remove comments and code they don't understand as side effects. The `CLAUDE.md` answers with four principles:

1. **Think Before Coding** — state assumptions, present multiple interpretations, push back when a simpler approach exists, stop and ask when confused.
2. **Simplicity First** — no unrequested features, no single-use abstractions, no speculative configurability or impossible-case error handling; "if 200 lines could be 50, rewrite it."
3. **Surgical Changes** — don't improve adjacent code, match existing style, mention unrelated dead code rather than deleting it, remove only orphans your own change created; every changed line should trace to the request.
4. **Goal-Driven Execution** — turn tasks into verifiable goals ("Fix the bug" → "write a test that reproduces it, then make it pass") and state a brief plan with a verify check per step.

## Installation

```text
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

Or per project: `curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md` for a new project, or append the file to an existing `CLAUDE.md`. A committed Cursor rule (`.cursor/rules/karpathy-guidelines.mdc`) applies the same guidelines in Cursor; `CURSOR.md` explains setup.

## Key features

- **Four-principle contract** in one file, each mapped to a failure mode (wrong assumptions, bloat, orthogonal edits, weak success criteria).
- **Verification loop framing** — Karpathy's "don't tell it what to do, give it success criteria and watch it go" underpins Goal-Driven Execution.
- **Self-check signals** — fewer unnecessary diff changes, fewer overcomplication rewrites, clarifying questions before implementation, and minimal PRs.
- **Composable** — designed to merge with project-specific `CLAUDE.md` rules.
- **Explicit tradeoff** — biased toward caution over speed; trivial tasks (typo fixes, one-liners) call for judgment.

## Architecture

No runtime. Top-level: `CLAUDE.md` (the four principles), `CURSOR.md` (Cursor-adapted guidelines), `EXAMPLES.md` (before/after examples), `skills/karpathy-guidelines` (the Claude Code plugin skill), `.claude-plugin/`, `.cursor/`, and `README.md` / `README.zh.md`. The README links the originating Karpathy post on X.

## Example usage

```markdown
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have tests
- Follow the existing error handling patterns in `src/utils/errors.ts`
```

Append project rules like these to the Karpathy `CLAUDE.md`, as the README's Customization section suggests.

## Maintenance status

225,112 GitHub stars, 22,503 forks, no primary language (Markdown), default branch `main`, no tagged releases, most recent push 2026-04-20. GitHub lists no license, though the README states MIT. Static guidance file with a plugin and Cursor rule; low churn.
