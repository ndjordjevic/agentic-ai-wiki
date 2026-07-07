# davidondrej/skills

## Metadata
- Stars: 1546
- Primary language: (none detected)
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-07
- Final URL: https://github.com/davidondrej/skills

## Description
access to david ondrej's personal agent skills

## README
# davidondrej-skills

David Ondrej's official Agent Skills.

This repository contains reusable skills for AI coding agents, research agents,
and workflow agents. Each skill packages a focused workflow into instructions
that an agent can load when the task calls for it.

Use these skills as practical building blocks for agentic work: improving
codebases, preparing content, researching ideas, reviewing presentations,
working with transcripts, and other repeatable workflows from David's stack.

Skills are grouped into category folders under `skills/`. Each skill lives in
its own folder and starts with a `SKILL.md` file that explains when and how to
use it.

- `skills/agent-orchestration/` — Running, scheduling, delegating to, and coordinating AI coding agents, including agent-to-agent workflows, agent loops, and agent benchmarks.
- `skills/skill-authoring/` — Creating, improving, distributing, and publishing Agent Skills and agent context files.
- `skills/research-and-web/` — Finding and pulling information from the web, research APIs, browsers, and YouTube.
- `skills/thinking-and-docs/` — Structured thinking, interviewing, teaching, and turning ideas into clear documentation.
- `skills/ops-and-setup/` — Machine, server, security, and tool setup, configuration, and operations.

## Docs

No `docs/` folder in this repo. Per-skill `SKILL.md` frontmatter (name + description, fetched from each of the 31 skill folders) captures the operative content:

### skills/agent-orchestration/

**agent-self-scheduling**
> Make an AI agent run on a schedule, loop, or interval — cron, heartbeats, recurring autonomous checks. Use for "run every N minutes", "schedule a task", "run on a loop", "heartbeat". Covers external clocks (Claude Code, Codex, Pi) vs Hermes' built-in scheduler.

**cmux**
> MUST be read ANY time you interact with cmux in ANY way — listing/inspecting/creating/closing cmux workspaces, panes, or surfaces; reading or capturing pane/screen output; sending input or keys to a pane/surface; delegating to, polling, or checking on other agents running in cmux panes/surfaces; building or rearranging terminal layout; cmux browser automation; sending notifications/flashes/status/progress to the sidebar; editing cmux settings; or integrating an agent with cmux hooks. macOS only (14.0+).

**codex-subagent**
> Launch OpenAI Codex CLI as a subagent (ChatGPT subscription auth, no API key). Use when delegating a self-contained coding task to Codex from another agent — parallel implementation work, a second opinion, or an independent verification pass. (`disable-model-invocation: true`)

**delegating-to-agents**
> How to delegate work to another AI agent (Pi, Codex, Claude Code, Hermes) — picking the right agent, sending prompts to TUI agents, polling progress. Read BEFORE any `cmux send`/`tmux send-keys` to an agent, or whenever delegating, relaying, spawning, or orchestrating agent-to-agent work.

**fable-safe-prompt**
> Rewrite a user's prompt to reduce the chance it trips Claude Fable 5's server-side safety classifiers (cyber/bio guardrails that force-route to Opus 4.8 or return stop_reason "refusal"). Use when the user hands you a prompt that touches cybersecurity, auth, exploits, malware, pentesting, or other dual-use topics and asks to make it "Fable-safe", "guardrail-safe", "won't get flagged/refused/downgraded". (`disable-model-invocation: true`)

**goal-loop**
> Explain and write effective instructions for the `/goal` feature — the persistent self-checking agent loop (plan → act → test → review → iterate), available in agents like Codex, Claude Code, and Hermes Agent. Use when the user mentions `/goal`, "goal loop", "Ralph loop", wants to kick off a long-running autonomous agent run, asks how to write a goal prompt, or wants a one-paragraph goal instruction drafted.

**handoff**
> Compact the current conversation into a single, detailed handoff message — everything that happened, why it happened, and what's left — output in a code block so it can be copy-pasted into a fresh agent session. Use when hitting context limits, switching focus, ending a work session, or partitioning a task across fresh contexts. (`disable-model-invocation: true`)

**markdown-rendering**
> How to reliably open a markdown file in a cmux right pane without it rendering blank. Use whenever opening/showing/rendering a .md file in cmux's right pane via `cmux markdown open`. Covers the move-surface blank-render bug and the only two reliable approaches — open it correctly the first time, or close the existing right pane(s) first then open a fresh right pane.

**run-deep-swe**
> Score any AI model on the DeepSWE coding-agent benchmark via the OpenRouter API. Use when the user wants an independent, reproducible coding-agent eval — "run DeepSWE", "benchmark this model on DeepSWE", "score model X on the coding benchmark", or to verify vendor-reported coding scores. Covers setup, OpenRouter wiring for mini-swe-agent, single-task/subset/full 113-task runs, and leaderboard submission. (`disable-model-invocation: true`)

### skills/ops-and-setup/

**anti-sleep**
> Keep the user's MacBook awake with macOS caffeinate — prevent sleep, screen dimming, or both, for a set duration or while a process runs. Use when the user says "don't let my mac sleep", "keep the screen on", "anti-sleep", "caffeinate", or wants the machine awake overnight / during a long build.

**cyber-audit**
> Read-only exposure audit of the user's MacBook (and ~/Documents/code projects) for a CVE, breach, malicious package, or other security advisory, then write a structured report to ~/Documents/security-audits/. Use when the user shares a breach/CVE/malware/supply-chain advisory and asks if they're affected. Output matches the existing audit format in ~/Documents/security-audits/. (`disable-model-invocation: true`)

**pi-custom-model**
> Register a custom or variant model (e.g. an OpenRouter ":nitro"/":floor"/":exacto" slug) in the Pi Agent so it can be set as the global default. Use when Pi silently falls back to a different model after setting defaultModel, or when a model slug isn't in Pi's bundled list. Triggers on "Pi reset my model", "Pi won't use this model", "Pi default keeps reverting". (`disable-model-invocation: true`)

**setup-help**
> Walk the user through setting up anything step by step. Use when the user asks for help setting up, configuring, installing, or getting something working. Differentiator: gives one current step at a time, then always lists every remaining setup step after each response. (`disable-model-invocation: true`)

**vps-server-management**
> Use when the user wants to manage their VPS servers and the AI agents running inside them — connecting, deploying, monitoring, restarting, and operating remote hosts and their agents. Triggers on VPS, server management, remote host, SSH into server, manage my servers, agents on the server.

### skills/research-and-web/

**browser-harness**
> Direct browser control via CDP. Use when the user wants to automate, scrape, test, or interact with web pages. Connects to the user's already-running Chrome.

**deep-research**
> Run a deep, source-backed research query via DeepAPI (deepapi.co) POST /v1/research/deep. Builds a rigorous one-paragraph research prompt (per research-prompt rules), fires it, and saves a cited markdown report. Use when the user asks for "deep research", "deepapi research", "perplexity deep research" (legacy trigger). Differentiator vs the deepapi skill: full research workflow (prompt + run + report file), not raw endpoint access. (`disable-model-invocation: true`)

**deepapi**
> Use DeepAPI for scraping and safe email with DEEPAPI_API_BASE_URL and DEEPAPI_API_KEY.

**pi-web-search**
> ONLY for Pi Agents — all other agents have their own web tools. How Pi accesses the web via the pi-web-access package — search, fetch URLs/PDFs/YouTube/GitHub. Use whenever a Pi task needs current info, docs, news, prices, or content from a specific URL.

**research-prompt**
> Write a single-paragraph Deep Research prompt to hand to a human researcher (or a deep-research AI). Use when the user wants a research brief, a "deep research prompt", a one-paragraph task for a researcher. Produces ONE tight paragraph with full context, numbered sub-questions, and per-finding output format.

**youtube-transcript**
> Use whenever the user needs the transcript of a YouTube video — fetching, extracting, downloading, or pulling captions/subtitles/transcript text from a YouTube URL. Primary path is DeepAPI (deepapi.co); yt-dlp is the local fallback.

### skills/skill-authoring/

**distribute-skill-to-all-agents**
> Distribute a skill across the 4 agent skill folders (Codex, Claude Code, Pi, Hermes) so all agents see it. Use when the user says "distribute this skill", "sync skills across agents", or after creating/updating a skill that should be global. Covers the symlink layout and the ~/.pi/agent/skills trap.

**effective-agent-skills**
> How to write effective agent skills — what to do, what not to do, anatomy, progressive disclosure, design patterns, anti-patterns, testing, security. Read this whenever a skill (Claude Skill, Agent Skill, SKILL.md) is being created, edited, reviewed, or debugged. Use when the user says "create a skill", "new skill", "update this skill", "improve a skill", "why isn't my skill triggering".

**folder-specific-claude-and-agents-md**
> Create a specialized CLAUDE.md (+ AGENTS.md symlink) inside a specific folder to give future agents folder-scoped context. Use when the user asks to create a CLAUDE.md for a folder, write folder instructions, or add agent context to a directory. (`user-invocable: true`)

**push-skill-to-github**
> Commit and push agent-skill changes to the user's private skills GitHub repo (rooted at ~/.agents). Use after creating or updating any skill, when the user says "push the skill", "push skills to github", "save the skill to my repo", or "update the skills repo". Handles staging, committing, pushing, and cleaning up the cmux pane used to do it.

### skills/thinking-and-docs/

**brain-to-docs**
> Use when the user wants to extract project vision, decisions, and preferences from their head into clear documentation (README + ADRs) through a back-and-forth Q&A loop. Triggers on "brain-to-docs", "build out the docs", "extract the vision", "let's document this project".

**copywriting**
> How David Ondrej writes. Use EVERY time you write copy or any text on David's behalf — tweets, DMs, YouTube titles and descriptions, GitHub About and READMEs, landing pages, bios, emails, product copy, announcements. Covers his two styles (authentic and formal) and when to use each.

**grill-me**
> Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". (`disable-model-invocation: true`)

**interview-style-doc-building**
> Use when the user wants to build a structured strategic document by answering questions (life priorities, goals docs, framework files, ranked lists, principles, reviews). Interview one question at a time, patch the file after each answer, then re-ask. Not for day planning (use day-plan).

**read-all-adrs**
> Read every ADR markdown file in the project's docs/adr/ folder so you have full context on past decisions. Use only when the user explicitly calls it. (`disable-model-invocation: true`)

**short**
> Manually-invoked skill that forces the agent to compress its current answer — strip filler, simplify wording, and cut length while keeping the substance. Use when the user says "short", "shorter", "simpler", "too long", "tl;dr". (`disable-model-invocation: true`)

**teach**
> Teach the user a new skill or concept, within this workspace. (`disable-model-invocation: true`, argument-hint: "What would you like to learn about?")

## Top-level structure
- `.gitignore`
- `LICENSE` — MIT
- `README.md` — category overview (reproduced above)
- `skills/` — 5 category folders, 31 total skills, each with a `SKILL.md` (some categories also include supporting scripts/docs not fetched here; `deepapi` skill folder additionally carries a `version:` frontmatter field instead of a body preview)
