# nidhinjs/prompt-master

## Metadata
- Stars: 7412
- Forks: 812
- Primary language: (none — pure Markdown)
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-05-13
- Final URL: https://github.com/nidhinjs/prompt-master

## Description
A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention. No re-prompting your way to an answer you should have gotten on attempt one.

## README

![](https://i.postimg.cc/kG03s7tk/prompt-banner.png)

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention. No re-prompting your way to an answer you should have gotten on attempt one.

**Works with:** Claude, ChatGPT, Gemini, o1/o3, MiniMax, Cursor, Claude Code, GitHub Copilot, Windsurf, Bolt, v0, Lovable, Devin, Perplexity, Midjourney, DALL-E, Stable Diffusion, ComfyUI, Sora, Runway, ElevenLabs, Zapier, Make, and any AI tool you throw at it.

---

### 🚀 Installation

#### RECOMMENDED - Claude.ai (browser)

1. Download this repo as a ZIP
2. Go to **claude.ai → Sidebar → Customize → Skills → Upload a Skill**

#### OR Clone directly into Claude Code skills directory (Not Suggested)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

### 🔥 The Problem This Solves

Every AI user wastes credits the same way:

> Write vague prompt → get wrong output → re-prompt → get closer → re-prompt again → finally get what you wanted on attempt 4

That's 3 wasted API calls. Multiply by 50 prompts a day. That's real money and real time gone.

**The key insight:**

> "The best prompt is not the longest. It's the one where every word is load-bearing."

Most "prompt generators" make prompts longer. This skill makes them sharper.

---

### 🎯 Usage

In Claude, you can invoke the skill naturally:

```
Write me a prompt for Cursor to refactor my auth module
```

```
I need a prompt for Claude Code to build a REST API — ask me what you need to know
```

```
Here's a bad prompt I wrote for GPT-4o, fix it: [paste prompt]
```

```
Generate a Midjourney prompt for a cyberpunk city at night
```

Or explicitly invoke it:

```
/prompt-master

I want to ask Claude Code to build a todo app with React and Supabase
```

---

### How It Works

Prompt Master runs a structured pipeline on every request:

1. **Detects the target tool** — figures out which AI system the prompt is for and routes silently to the right approach
2. **Extracts 9 dimensions of intent** — task, input, output, constraints, context, audience, memory, success criteria, examples
3. **Asks targeted clarifying questions** — max 3 questions if critical info is missing, never more
4. **Routes to the right framework** — picks and applies the correct prompt architecture automatically, never shown to the user
5. **Applies safe techniques only** — role assignment, few-shot examples, XML structure, grounding anchors, memory block as needed
6. **Runs a token efficiency audit** — strips every word that doesn't change the output
7. **Delivers the prompt** — one clean copyable block with a one-line strategy note

---

### 🤝 Works With Any AI Tool

Prompt Master includes specific profiles for 20+ tools. For anything not on the list, it uses a **Universal Fingerprint**: 4 questions that let it write a quality prompt for any AI system it has never seen before.

**Tool profiles (30+):**

| Tool | Category | What Prompt Master Fixes |
|------|----------|--------------------------|
| **Claude** | Reasoning LLM | Removes padding, adds XML structure, specifies length |
| **ChatGPT / GPT-5.x** | Reasoning LLM | Output contract, verbosity control, completion criteria |
| **Gemini 2.x** | Reasoning LLM | Grounding anchors, citation rules, format locks |
| **o3 / o4-mini** | Thinking LLM | Short clean instructions only — never adds CoT |
| **Ollama** | Local LLM | Asks which model is loaded, includes system prompt for Modelfile |
| **Qwen 2.5 / Qwen3** | Open-weight LLM | Chat template format, thinking vs non-thinking mode detection |
| **Local models (Llama, Mistral)** | Open-weight LLM | Shorter prompts, simpler structure, no complex nesting |
| **DeepSeek-R1** | Reasoning LLM | Short clean instructions, strips CoT, suppresses thinking output if needed |
| **MiniMax (M2.7 / M2.5)** | Reasoning LLM | Temperature clamping, thinking tag control, structured output optimization |
| **Claude Code** | Agentic AI | Stop conditions, file scope, checkpoint output |
| **Cursor / Windsurf** | IDE AI | File path, function name, do-not-touch list, sequential prompt guidance |
| **Cline (formerly Claude Dev)** | Agentic IDE | File scope, approval gates, stop conditions, task breakdown |
| **GitHub Copilot** | Autocomplete AI | Exact function contract as docstring |
| **Bolt / v0 / Lovable** | Full-stack generator | Stack spec, version, what NOT to scaffold |
| **Devin / SWE-agent** | Autonomous agent | Starting state, target state, stop conditions |
| **Manus** | Autonomous agent | Task outcome focus, permission scope, memory anchors |
| **Perplexity / SearchGPT** | Search AI | Mode spec: search vs analyze vs compare |
| **Midjourney** | Image AI | Comma-separated descriptors, parameters, negative prompts |
| **DALL-E 3** | Image AI | Prose description, text exclusion — edit vs generate detection |
| **Stable Diffusion** | Image AI | Weight syntax `(word:1.3)`, CFG guidance, mandatory negative prompt |
| **ComfyUI** | Image AI | Positive/negative node split, checkpoint-specific syntax |
| **Sora / Runway** | Video AI | Camera movement, duration, cut style |
| **ElevenLabs** | Voice AI | Emotion, pacing, emphasis, speech rate |
| **Zapier / Make / n8n** | Workflow automation | Trigger app + event, action app + field mapping |

---

### 📐 12 Prompt Templates (Auto-Selected)

| Template | Best For |
|----------|----------|
| **RTF** (Role, Task, Format) | Fast one-shot tasks |
| **CO-STAR** (Context, Objective, Style, Tone, Audience, Response) | Professional documents, reports, business writing |
| **RISEN** (Role, Instructions, Steps, End Goal, Narrowing) | Complex multi-step projects |
| **CRISPE** (Capacity, Role, Insight, Statement, Personality, Experiment) | Creative work, brand voice, iterative content |
| **Chain of Thought** | Math, logic, debugging, multi-step analysis |
| **Few-Shot** | Consistent structured output, pattern replication |
| **File-Scope Template** | Cursor, Windsurf, Copilot — any code editing AI |
| **ReAct + Stop Conditions** | Claude Code, Devin, AutoGPT — any autonomous agent |
| **Visual Descriptor** | Midjourney, DALL-E, Stable Diffusion, Sora — generation |
| **Reference Image Editing** | Editing an existing image — detects edit vs generate automatically |
| **ComfyUI** | Node-based image workflows — positive/negative split per checkpoint |
| **Prompt Decompiler** | Breaking down, adapting, simplifying, or splitting existing prompts |

---

### 🛡️ 5 Safe Techniques, Applied When Needed

| Technique | What It Does |
|-----------|-------------|
| **Role Assignment** | Assigns a specific expert identity to calibrate depth and vocabulary |
| **Few-Shot Examples** | Adds 2-5 examples when format consistency matters more than instructions |
| **XML Structural Tags** | Wraps sections in XML for Claude-based tools that parse it reliably |
| **Grounding Anchors** | Adds anti-hallucination rules for factual and citation tasks |
| **Chain of Thought** | Forces step-by-step reasoning for logic tasks — never applied to o1/o3 |

Explicitly excluded (fabrication risk): Tree of Thought, Graph of Thought, Universal Self-Consistency, prompt chaining.

---

### 🧠 Memory Block System

When your conversation has history, Prompt Master pulls out prior decisions and prepends a Memory Block so the AI never contradicts earlier work:

```
## Memory (Carry Forward from Previous Context)
- Stack: React 18 + TypeScript + Supabase
- Auth uses JWT stored in httpOnly cookies, not localStorage
- Component naming convention: PascalCase, no default exports
```

---

### ℹ️ Version History

- **1.6.0** — Opus 4.7 update. Added Template M (Opus 4.7 Task Brief). Updated Claude and Claude Code routing for literalism, adaptive thinking, xhigh effort, and session hygiene. Added patterns 36–37.
- **1.5.0** — Added more tool routing. New Agentic AI and 3D Model AI routing added.
- **1.4.0** — Added reference image editing detection, ComfyUI support, Prompt Decompiler mode.
- **1.3.0** — Rebuilt around PAC2026 positional structure (30/55/15). Silent routing replaces user-facing framework selection.
- **1.2.0** — Restructured for attention architecture. Removed fabrication-prone techniques.
- **1.1.0** — Expanded tool coverage, added memory block system, 35 credit killing patterns.
- **1.0.0** — Initial release.

---

### 📄 License

MIT: See LICENSE for details.

## Docs

### references/patterns.md (excerpt)

37 patterns that waste tokens and cause re-prompts. Categories:

**Task Patterns (7):** Vague task verb, Two tasks in one prompt, No success criteria, Over-permissive agent, Emotional task description, Build-the-whole-thing, Implicit reference.

**Context Patterns (6):** Assumed prior knowledge, No project context, Forgotten stack, Hallucination invite, Undefined audience, No mention of prior failures.

**Format Patterns (6):** Missing output format, Implicit length, No role assignment, Vague aesthetic adjectives, No negative prompts for image AI, Prose prompt for Midjourney.

**Scope Patterns (6):** No scope boundary, No stack constraints, No stop condition for agents, No file path for IDE AI, Wrong template for tool, Pasting entire codebase.

**Reasoning Patterns (5):** No CoT for logic task, Adding CoT to reasoning models, No self-check, Expecting inter-session memory, Contradicting prior decisions.

**Agentic Patterns (7 incl. 36–37):** No starting state, No target state, Silent agent, Unlocked filesystem, No human review trigger, Vague first turn on Opus 4.7, Context rot on long sessions.

### references/templates.md

12 full prompt templates (RTF, CO-STAR, RISEN, CRISPE, Chain of Thought, Few-Shot, File-Scope, ReAct+Stop, Visual Descriptor, Reference Image Editing, ComfyUI, Prompt Decompiler). Each template is the full fill-in-the-blank structure used when the skill routes to that category.

## Top-level structure

```
prompt-master/
├── LICENSE              — MIT license
├── README.md            — Full documentation, installation, usage examples, tool profiles, templates list
├── SKILL.md             — Main skill file (agent instruction file for Claude): PRIMACY ZONE identity + hard rules, MIDDLE ZONE tool routing + intent extraction, BOTTOM ZONE output format and diagnostics. 26KB. Version 1.6.0.
└── references/
    ├── patterns.md      — 37 credit-killing prompt patterns with before/after examples (6KB)
    └── templates.md     — 12 full prompt templates referenced by routing logic (17KB)
```

Notes:
- No `docs/` or `examples/` folder — all documentation is in README.md and references/
- `SKILL.md` is the canonical agent instruction file; README.md is the human-facing companion
- Pure Markdown repository — no source code, no build system
- `references/` folder holds pattern and template data loaded by the skill at runtime
