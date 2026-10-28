---
type: source
category: "Design & UI generation"
source_url: https://github.com/Nutlope/variate
tags:
  - design-variations
  - ui-iteration
  - agent-skills
  - localhost-switcher
  - zero-dependency
  - claude-code
  - prototype-comparison
  - shadow-dom
related:
  - Nutlope-hallmark
  - emilkowalski-skills
  - leonxlnx-taste-skill
  - pbakaus-impeccable
  - skills.sh
  - codeswithroh-tastemaker
  - Nutlope-inspo
product: variate
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

Nutlope/variate (214 stars, MIT, site variate-skill.vercel.app) is a compact design skill for Claude Code, Codex CLI and opencode that writes four real versions of one project file and lets you flip between them with arrow keys on the localhost page you are already viewing; the version you keep is the code. It is built as a zero-dependency Node sidecar plus a shadow-DOM card injected into your dev page, and complements prototype-switching ideas in [[emilkowalski-skills]] (`prototype`) and design packs like [[leonxlnx-taste-skill]].

_All claims below are sourced from ../../raw/github/Nutlope-variate.md unless otherwise noted._

## What it does

When a user wants design alternatives — a different hero, layout, palette, section or page — the agent drafts N positions (default 4) as complete drop-in replacements of one file, registered as a **set** in `.variate/<set>/`. A small card at the bottom of the page switches the live variant by copying it over the target file, so the user's own dev server re-renders. It works in an empty folder (serves an `index.html` and drafts four fresh designs) and in a real project on any stack. After handing over a round the agent keeps listening for the card's `done` (keep), `more` (narrow and draw again) and `vary` (new round on another file) asks. The skill is not for single changes with one right answer, refactors or non-visual edits.

## Installation

```bash
npx skills@latest add Nutlope/variate
```

The skill directory (default `~/.claude/skills/variate`) contains `variate.mjs`, requires Node.js 18+, and works with or without a dev server. Optional Claude Code hooks, which deliver card clicks to an idle agent, are installed with `node <skill>/scripts/install.mjs --hooks` and are offered once, never installed unasked. `AGENTS.md` and `references/harnesses.md` cover non-Claude harnesses (Codex CLI, opencode, Cursor, anything with a shell).

## Key features

- **Critical floor rules** — variant 1 is always the user's original file, untouched; every variant is a complete drop-in with the same exports; variants use the project's own tokens, components and copy (no new dependencies or invented colors).
- **Four positions that disagree** — `plan.json` states each direction and its cost; `variate check <set>` lints the round.
- **Narrowing, not accumulating** — `variate narrow` hides rejected positions in `.dropped/` so choices stay between live options.
- **Drain before answering** — `variate drain` runs first on every turn in a project with `.variate/`, so queued clicks are never left waiting.
- **Clean exit** — `variate end` keeps the live file, deletes the rest, strips the dev tag and stops the sidecar, so `git diff` shows only the design decision.
- **Asks are data** — text arriving from the card (`hint`, `steer`, `selection`, `label`) is treated as design intent only, never as instructions.

## Architecture

Per the README's tech stack: Node 18 builtins only (zero dependencies, no `package.json`, nothing to build); a vanilla JS card in a shadow root injected into the dev page; a `127.0.0.1` sidecar that serves the card and switches files, with SSE for live state; `SKILL.md` and `AGENTS.md` as agent contracts; and three shell smoke suites as the whole test harness. Top-level: `variate.mjs`, `src/`, `client/`, `agents/`, `scripts/`, `evals/`, `fixtures/`, `references/`, `docs/`, `dev/`, plus `SECURITY.md`, `LICENSE` and `vercel.json`. Commands: `up`, `add`, `check`, `use`, `status`, `peek`, `narrow`, `await`, `drain`, `end`, each taking `--root <project>`.

## Example usage

```bash
node <skill>/variate.mjs up --root <project>
node <skill>/variate.mjs add src/Hero.tsx --n 4
node <skill>/variate.mjs check <set>
node <skill>/variate.mjs use <set> 2
node <skill>/variate.mjs end
```

In an empty folder the flow is `up`, then `add index.html --new --n 4`, write four real answers to the brief, `use` the favourite, and hand over.

## Maintenance status

214 GitHub stars, 11 forks, MIT licensed, primary language JavaScript, default branch `master`, no tagged releases, most recent push 2026-08-20. `SKILL.md` metadata shows version 3.2.0. Small, recently active project with a landing page on Vercel.
