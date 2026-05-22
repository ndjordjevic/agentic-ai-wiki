---
type: source
source_url: https://openvibe.sh/
companion_urls:
  - https://github.com/wasp-lang/open-vibe
raw_files:
  - ../../raw/web/openvibe.sh.md
  - ../../raw/github/wasp-lang-open-vibe.md
tags:
  - claude-code
  - vibe-coding
  - saas-course
  - agent-tutoring
  - wasp-framework
  - open-saas
  - web-dev-learning
  - pair-programming
related:
  - shareai-lab-learn-claude-code
  - skills.sh
product: openvibe
detail_level: standard
created: 2026-05-22
updated: 2026-05-22
---

Open Vibe is a free, MIT-licensed, agent-driven web development course that turns Claude Code (or any capable AI coding agent) into a pair-programming tutor. Instead of static tutorials or black-box vibe-coding platforms, Open Vibe embeds the curriculum directly in `llms.txt` — the agent fetches structured module files, alternates between TUTOR MODE and PAIR PROGRAMMER MODE, and guides the learner through building a real SaaS while explaining every concept along the way. The course is built by the Wasp team and uses the Open SaaS template as the production substrate for Phase 2.

_All claims below are sourced from ../../raw/web/openvibe.sh.md unless otherwise noted._

## What it does

Open Vibe delivers a progressive web development curriculum via AI agent instruction files. The entry point is a single prompt — `curl -fsSL https://openvibe.sh/llms.txt` — which loads the course index into the agent's context. The agent then asks the learner which phase to start, fetches the relevant module files with `curl`, and follows step-by-step instructions that alternate between teaching concepts and writing code. Each module tracks progress via a `public/course-progress.json` file written by the agent into the learner's project.

## Key features

- **No signup, no cost** — fully open source under MIT; runs entirely on the learner's machine.
- **Agent-native curriculum** — modules are structured markdown with explicit `RUN:`, `SAY:`, `ASK:`, and `LEARNER:` prefixes that give the agent precise instructions without ambiguity.
- **Two-phase structure** — Phase 1 builds a task-management app from scratch (beginner); Phase 2 builds a production SaaS on Open SaaS (intermediate).
- **Live interactive diagrams** — the running app can render `BEHIND THE SCENES` overlay diagrams (e.g. showing the HTTP request chain for "add task") triggered by agent commands. (../../raw/github/wasp-lang-open-vibe.md)
- **Progress tracking** — `public/course-progress.json` lets the agent resume mid-module without repeating completed beats.
- **Canary verification** — each module ends with a canary string so the agent can confirm it fetched the raw file and not a summarized version.
- **Works with multiple agents** — Claude Code, Cursor, Codex, GitHub Copilot, OpenCode, or any agent that can run `curl` and execute terminal commands. (../../raw/github/wasp-lang-open-vibe.md)

## Architecture

The course is a static Astro site (`github.com/wasp-lang/open-vibe`) hosting markdown module files under `public/modules/`. The site itself is a marketing/landing page; all instructional content lives in the `public/` directory and is served as plain text — no API, no authentication, no server state. (../../raw/github/wasp-lang-open-vibe.md)

The agent orchestration model:
1. Learner pastes one prompt into their agent; agent curls `llms.txt`.
2. `llms.txt` describes the phase structure and instructs the agent to ask which phase before fetching further.
3. Agent fetches `setup.md` then the phase-specific module files in order.
4. Each module is self-contained: it defines the agent's role, pacing rules, which commands the agent executes vs. which the learner runs, and all dialogue beats.
5. The app being built (Wasp todo app or Open SaaS) runs locally on the learner's machine; the agent never touches a remote deployment during the course. (../../raw/github/wasp-lang-open-vibe.md)

## Installation

No installation of Open Vibe itself is needed. The learner runs one setup script and one prompt: (../../raw/github/wasp-lang-open-vibe.md)

```bash
# 1. Set up environment (Node.js, Wasp CLI, optional Docker for Phase 2)
curl -fsSL https://openvibe.sh/setup.sh | bash

# 2. Start the course — paste this into your agent
I want to ship my app with Open Vibe. Run `curl -fsSL https://openvibe.sh/llms.txt` and follow the file's instructions.
```

Phase 2 additionally requires Docker (Open SaaS uses Postgres via Docker).

## Example usage

The learner opens their project directory in Claude Code and pastes the prompt. The agent responds: (../../raw/github/wasp-lang-open-vibe.md)

```
> I want to ship my app with Open Vibe. Run `curl -fsSL https://openvibe.sh/llms.txt` and follow the file's instructions.

● Running curl -fsSL https://openvibe.sh/llms.txt...
● [reads file]
● "Welcome! This course has two starting points — Phase 1 (basics) or Phase 2 (SaaS). Which do you want to start with?"
```

From there the agent fetches the appropriate module, runs environment checks, creates the Wasp project, and begins the beat-by-beat tutoring flow. Each beat starts with a hardcoded box title and the agent follows SAY:/ASK:/LEARNER:/RUN: prefixes exactly.

## When to use

Open Vibe is the right choice when:
- A developer (beginner to intermediate) wants to build a real SaaS product while simultaneously understanding the systems underneath it.
- The learner is frustrated by black-box vibe-coding platforms (where credits burn without comprehension) and wants to break the "prompt-fix loop."
- The goal is to ship a deployable SaaS using Open SaaS (auth, payments, admin, email, AI) as the starting template.
- The learner already has Claude Code, Cursor, or another capable coding agent and wants structured guidance rather than ad hoc prompting.

## Maintenance status

36 stars on GitHub; no formal releases yet (v1.0 announced via landing page). Built and maintained by the Wasp team (wasp.sh). Discord support available at discord.gg/rzdnErX. Last pushed 2026-05-14. License not formally specified in the repository but the landing page states MIT. (../../raw/github/wasp-lang-open-vibe.md)

## Ecosystem

- **[Wasp](https://wasp.sh)** — the full-stack framework used to build the learner's app in both phases.
- **[Open SaaS](https://opensaas.sh)** — the production-ready SaaS template used in Phase 2 (auth, payments via Stripe/Lemon Squeezy/Polar, admin, email, AI-ready).
- **Agent compatibility** — Claude Code, Cursor, Codex, GitHub Copilot, OpenCode.
- The GitHub repository (`github.com/wasp-lang/open-vibe`) is the canonical source for module files and the setup script; the site at `openvibe.sh` is the human-facing landing page. (../../raw/github/wasp-lang-open-vibe.md)
