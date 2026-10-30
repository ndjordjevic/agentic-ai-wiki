---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://www.youtube.com/watch?v=DMlBzXvG22g
tags:
  - claude-code-tools
  - token-savings
  - visual-planning
  - agent-plugins
  - voice-to-agent
  - workflow-roundup
related:
  - rtk-ai-rtk
  - getcaveman.dev
  - dietrichgebert-ponytail
  - agricidaniel-claude-obsidian
  - kepano-obsidian-skills
  - wisprflow.ai
  - microsoft-TokenEconomizer
  - kunchenguid-lavish-axi
  - obsidian.md
  - buildpartner.ai
  - small-business
  - hex.kitlangton.dev
product: free-claude-tools-roundup
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

A 15-minute Austin Marchese roundup of eight free tools for Claude Code users — visual planning (Lavish), input/output token cutting (RTK, Caveman, Ponytail), Claude Code Projects for parallel work, BuildPartner.ai for discovery, Obsidian for live markdown review, Anthropic's small-business plugin, and Hex for voice-to-Claude — arguing that workflow tooling matters more than which model is smartest.

_All claims below are sourced from ../../raw/youtube/DMlBzXvG22g-8-free-ai-tools-every-claude-user-must-u.md unless otherwise noted._

## What the video is about

Austin Marchese walks through eight free (or free-tier) tools he says every Claude Code user should adopt to build faster and spend fewer tokens. The framing is explicit: none of the picks are about model IQ; they change how you plan, what the model sees, how much it writes, how you discover plugins, and how you talk to the agent. Sponsored segment for Whop appears at the end; the eight tools themselves are presented as free to start.

## Key points by chapter

**Tool 1: Lavish (Plan Visually) (0:00)**
Complex plans in chat become walls of text that are hard to navigate. Lavish turns a plan into a visual document you can comment on; comments can reorder tools or swap items, then "send to agent" updates the plan. For apps/UI work it can show a mock-up before build. Install by pasting the linked plugin into Claude ("download lavish" + link).

**Tool 2: RTK (Stop Paying For Noise) (1:25)**
RTK ("Rust Token Killer") filters shell/command output so Claude only sees what matters — e.g. ~15k raw tokens of check output compressed toward ~1.8k. Claimed savings around 70%+ on noisy command feedback. Demo shows integrating RTK and watching token burn drop on the same change/check loop. Contrasted with unfiltered dumps after every verification command.

**Tool 3: Caveman + Ponytail (Make Claude Write Less) (4:32)**
RTK cuts input tokens; this pair cuts output. Ponytail pushes YAGNI / simplest-thing-that-works (README claims ~54% less code, cheaper/faster runs). Caveman compresses Claude's prose ("few word do trick" Office/Kevin bit). Before/after screenshots show terse caveman replies vs. verbose filler.

**Tool 4: Claude Code Projects (Not What You Think) (6:41)**
Not the old Artifacts-style "Projects" — Claude Code Projects runs work in parallel sessions/lanes so multiple threads progress without serial chat bottlenecks. Framed as how power users structure concurrent Claude work rather than one long thread.

**Tool 5: BuildPartner.ai (How I Found These Tools) (8:39)**
[[buildpartner.ai]] (social feed) is how Austin discovers Claude plugins and community tools — a discovery surface for the ecosystem rather than a build runtime. Used as the meta-layer for finding Lavish, RTK, and the rest.

**Tool 6: Obsidian (See What Claude Is Writing) (10:02)**
Point [[obsidian.md|Obsidian]] at the markdown/files Claude is editing so you can read live structured notes instead of only chat. Useful for reviewing plans, skills, and docs Claude writes without scrolling the transcript.

**Tool 7: Anthropic's Small Business Plugin (10:50)**
Anthropic's official [[small-business]] plugin ships Claude skills aimed at running a business (ops, content, etc.). Austin teases a follow-up deep dive on ~13 new skills in that plugin as a window into how Anthropic designs skills.

**Tool 8: Hex (Talk To Claude Instead Of Typing) (12:17)**
[[hex.kitlangton.dev|Hex]] is voice input for Claude: speak stream-of-consciousness so ideas can evolve mid-recording, then send to the agent. Secondary use as a speaking coach (filler-word history). Recap: stack RTK/Caveman/Ponytail for spend, Lavish/Projects/BuildPartner for planning/discovery, Obsidian + Hex for review and voice, plus the small-business plugin for Anthropic's skill patterns. Whop sponsor close.

## Notable quotes

> "None of these are about which model is smartest. They're about how you work with it."

> "Why waste time say lot word when few word do trick?" (Office/Kevin clip used to pitch Caveman)

> "If you use all these tools, your wins will start stacking."

## Speaker context

Austin Marchese runs a YouTube channel on practical Claude Code / AI builder workflows; this episode (uploaded 2026-10-14) cross-sells a follow-up on Anthropic's small-business plugin skills and links plugins from the video description / BuildPartner discovery path.
