---
type: source
source_url: https://github.com/nidhinjs/prompt-master
tags: [prompt-engineering, claude-skill, skill-md, multi-tool-routing, token-efficiency, agentic-ai, prompt-templates, intent-extraction]
related: [anthropics-skills, skills.sh, forrestchang-andrej-karpathy-skills]
product: prompt-master
detail_level: standard
created: 2026-05-13
updated: 2026-05-13
---

Prompt Master is a Claude skill (SKILL.md-based, v1.6.0, 7,412 stars, MIT) that acts as an on-demand prompt engineer: it intercepts a user's rough idea, identifies the target AI tool, silently extracts nine dimensions of intent, routes to one of 12 prompt architectures, audits for token waste, and delivers a single production-ready prompt. It covers 30+ tool profiles spanning reasoning LLMs, coding agents, image generators, video AI, voice AI, and workflow automation, making it the broadest multi-tool prompt-engineering skill in the Claude ecosystem to date.

_All claims below are sourced from ../../raw/github/nidhinjs-prompt-master.md unless otherwise noted._

## What it does

Prompt Master solves the re-prompting loop: users write a vague prompt, get wrong output, re-prompt, and waste API credits across multiple attempts. The skill eliminates this by extracting intent precisely before generating a prompt. It activates only when the user explicitly asks to write, fix, improve, or adapt a prompt for a specific AI tool — it does not activate for general conversation, coding tasks, or document writing. The output is always a single copyable block with a one-line strategy note; no explanatory scaffolding is shown unless the user asks.

## Key features

- **9-dimension intent extraction** — silently extracts Task, Target tool, Output format, Constraints, Input, Context, Audience, Success criteria, and Examples before writing anything. Missing critical dimensions trigger clarifying questions (max 3).
- **30+ tool profiles** — dedicated routing for Claude, ChatGPT/GPT-5.x, Gemini 2.x, o3/o4-mini, DeepSeek-R1, MiniMax, Claude Code, Cursor, Windsurf, Cline, GitHub Copilot, Bolt/v0/Lovable, Devin, Manus, Perplexity, Midjourney, DALL-E 3, Stable Diffusion, ComfyUI, Sora/Runway, ElevenLabs, Zapier/Make/n8n, and more.
- **12 prompt templates** — RTF, CO-STAR, RISEN, CRISPE, Chain of Thought, Few-Shot, File-Scope, ReAct+Stop Conditions, Visual Descriptor, Reference Image Editing, ComfyUI, and Prompt Decompiler. Template selection is automatic and silent.
- **5 safe techniques only** — Role Assignment, Few-Shot Examples, XML Structural Tags, Grounding Anchors, and Chain of Thought. Explicitly excluded: Tree of Thought, Graph of Thought, Universal Self-Consistency, prompt chaining (all flagged as fabrication risks in single-prompt contexts).
- **Memory Block system** — extracts prior session decisions and prepends a structured `## Memory (Carry Forward)` block so the AI never contradicts earlier architecture choices.
- **Token efficiency audit** — strips every word that does not change output; goal is the sharpest prompt, not the longest.
- **Universal Fingerprint fallback** — for tools not in the profile list, a 4-question fingerprint generates a quality prompt for any AI system.

## Architecture

The skill is structured as a three-zone SKILL.md (`SKILL.md`, 26KB): PRIMACY ZONE (identity, hard rules, output format lock), MIDDLE ZONE (intent extraction, tool routing, template dispatch), and BOTTOM ZONE (diagnostics and fallbacks). A `references/` folder holds the full pattern library (`patterns.md`, 37 credit-killing patterns with before/after examples) and template library (`templates.md`, 12 full templates) that the skill reads at routing time. The repository is pure Markdown — no source code or build system.

The routing logic enforces tool-specific rules: o3/o4-mini and DeepSeek-R1 receive short clean instructions with CoT removed (reasoning models think internally); Claude Code prompts always include stop conditions, file scope, and checkpoint output; Cursor/Windsurf prompts use the File-Scope template with explicit file paths and do-not-touch lists; image AI prompts follow the Visual Descriptor format (comma-separated, parameters, negative prompt required).

## Installation

**Claude.ai (recommended):**
1. Download the repo as a ZIP.
2. Go to **claude.ai → Sidebar → Customize → Skills → Upload a Skill**.

**Claude Code (alternative):**
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

## Example usage

```
Write me a prompt for Cursor to refactor my auth module
```
→ Skill extracts: Target=Cursor, Task=refactor, file scope unknown → asks for file path → generates File-Scope template with `src/auth.js`, function name, do-not-touch list.

```
Here's a bad prompt I wrote for GPT-4o, fix it: [paste prompt]
```
→ Routes to Prompt Decompiler mode, identifies weak dimensions, rebuilds with output contract and verbosity constraint.

```
Generate a Midjourney prompt for a cyberpunk city at night
```
→ Routes to Visual Descriptor template: comma-separated descriptors, lighting anchors, `--ar 16:9 --v 6 --style raw`, negative prompt appended.

## When to use

Use Prompt Master when you find yourself re-prompting the same AI tool more than once to get the output you wanted, when switching to an unfamiliar tool (image AI, video AI, coding agents), or when adapting an existing prompt for a different AI system. It is particularly valuable for teams standardizing prompts across Claude Code, Cursor, and autonomous agents where vague instructions cause hallucinations or overreach.

## Maintenance status

7,412 stars, 812 forks, MIT License. No releases (distributed as a skill ZIP/clone). Latest version is 1.6.0 (Opus 4.7 routing update, May 2026). Actively maintained with regular version bumps as new AI tools and models are released. Primary language: Markdown.
