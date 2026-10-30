---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/blader/humanizer
tags:
  - agent-skill
  - humanizer
  - anti-ai-writing
  - prose-rewriting
  - wikipedia-ai-tells
  - voice-matching
  - skills-cli
related:
  - Nutlope-hallmark
  - leonxlnx-taste-skill
  - dmmulroy-anti-slop
  - impeccable.style
product: humanizer
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

blader/humanizer is an agent skill that rewrites AI-sounding prose so it reads like a person wrote it, without changing meaning. It is grounded in Wikipedia's Signs of AI writing guide, exposes `/humanizer` across Claude Code, Codex, and other skill-capable agents, and explicitly does not aim to beat AI detectors.

_All claims below are sourced from ../../raw/github/blader-humanizer.md unless otherwise noted._

## What it does

Humanizer marks AI-writing tells (strongest first), drafts a rewrite without treating the original structure as fixed, checks the draft against its pattern list and the original claims, then emits a final version. It does not invent facts: names, numbers, dates, quotes, and citations must come from the source or the writer, and it asks when a needed detail is missing. Pasted text gets a visible first rewrite, a short critique of remaining artificiality, and a final version; pointed at a file, it edits only prose and leaves code, data, frontmatter, and link targets alone. Personal writing keeps opinions and quirks; technical and reference prose stays neutral and plain. Getting past AI detectors is not a goal—detectors still flag most output. In a blind test cited in the README, judges preferred Humanizer's rewrite over the original AI text 16/16.

## Installation

Once installed, the skill answers to `/humanizer`.

**Claude Code** (plugin; needs Claude Code 2.1.142+; older versions use the skills CLI fallback below):

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

The plugin answers to `/humanizer:humanizer`.

**Codex:**

```bash
npx skills add blader/humanizer --global --agent codex
```

**Claude.ai / Claude Desktop:** download the repo ZIP and upload it as a skill in Settings.

**Other agents** (Gemini CLI, GitHub Copilot, Windsurf, and every agent the Skills CLI supports):

```bash
npx skills add blader/humanizer --global --agent '*'
```

Omit `--global` to install only in the current project. For unsupported agents, copy `SKILL.md` into the agent's skill folder. Older Claude Code: `npx skills add blader/humanizer --global --agent claude-code`.

## Key features

- **Five strongest tells** rewritten on sight: Not X but Y; one-line closers; deep-sounding sayings; staged run-ups ("Here's the thing"); arguing with no one.
- **26 patterns** in six groups (staging, rhythm by rule, inflation/borrowed authority, formatting by rule, chat/draft leftovers, writing for the wrong reader), numbered by strength/frequency; patterns marked weak alone only count when several tells share a passage.
- **Voice matching** — paste 2–3 paragraphs of your writing and Humanizer follows rhythm, word choice, punctuation, and deliberate quirks (including dashes if you use them).
- **Meaning-preserving** — content claims stay; significance inflation, chatbot wrappers, and decorative bold/emoji headings are stripped.
- **File-aware edits** — prose only; code, data, frontmatter, and link targets untouched.
- Sponsored by cfo.ai; listed on [skills.sh/blader/humanizer](https://skills.sh/blader/humanizer).

## Architecture

Portable core is a root `SKILL.md` plus supporting `agents/` and `scripts/`. Host adapters ship as `.claude-plugin/` (`marketplace.json`, `plugin.json`) and `.cursor-plugin/`. Top-level also includes `AGENTS.md`, `CHANGELOG.md`, and MIT `LICENSE`. Pattern taxonomy and rewrite rationale mirror Wikipedia's Signs of AI writing / WikiProject AI Cleanup; the README frames LLM default next-token choices as the root of the tells Humanizer targets.

## Example usage

```text
/humanizer

[paste your text here]
```

Plain language also works (`Please humanize this text: …`), or point at a file (`Humanize the prose in docs/launch-post.md`). For voice matching:

```text
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs]

Now humanize this text:
[paste AI text]
```

## Maintenance status

62,529 stars, 4,954 forks, Python primary language, default branch `main`, last pushed 2026-10-28. Latest release tagged Humanizer (2026-09-28). MIT License. Homepage: https://skills.sh/blader/humanizer.

## When to use

Reach for Humanizer when agents (or you) produce launch posts, docs, or marketing copy that still carries common AI tells—Not X but Y, dramatic closers, staged run-ups—and you want meaning-preserving prose cleanup rather than a visual/UI anti-slop pack or a code-pattern linter. Prefer it when Wikipedia-style AI-writing patterns are the failure mode; do not use it expecting detector evasion.

## Ecosystem

Sits with other anti-slop / taste skills in this wiki: [[Nutlope-hallmark]] (structural UI variety and slop-test gates), [[leonxlnx-taste-skill]] (aesthetic taste), [[dmmulroy-anti-slop]] (Oxlint code-pattern rules), and [[impeccable.style]] (design/UI taste). Humanizer is prose-focused and Wikipedia-pattern-driven rather than design- or TypeScript-lint-driven. Install path is the cross-agent [skills CLI](https://github.com/vercel-labs/skills) / skills.sh listing plus Claude Code marketplace plugin.
