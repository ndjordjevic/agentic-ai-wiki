# snarktank/ralph

## Metadata
- Stars: 19,297
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://x.com/ryancarson/status/2008548371712135632
- Fetched: 2026-05-20
- Final URL: https://github.com/snarktank/ralph

## Description
Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.

## README

# Ralph

![Ralph](ralph.webp)

Ralph is an autonomous AI agent loop that runs AI coding tools ([Amp](https://ampcode.com) or [Claude Code](https://docs.anthropic.com/en/docs/claude-code)) repeatedly until all PRD items are complete. Each iteration is a fresh instance with clean context. Memory persists via git history, `progress.txt`, and `prd.json`.

Based on [Geoffrey Huntley's Ralph pattern](https://ghuntley.com/ralph/).

[Read my in-depth article on how I use Ralph](https://x.com/ryancarson/status/2008548371712135632)

## Prerequisites

- One of the following AI coding tools installed and authenticated:
  - [Amp CLI](https://ampcode.com) (default)
  - [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- `jq` installed (`brew install jq` on macOS)
- A git repository for your project

## Setup

### Option 1: Copy to your project

Copy the ralph files into your project:

```bash
# From your project root
mkdir -p scripts/ralph
cp /path/to/ralph/ralph.sh scripts/ralph/

# Copy the prompt template for your AI tool of choice:
cp /path/to/ralph/prompt.md scripts/ralph/prompt.md    # For Amp
# OR
cp /path/to/ralph/CLAUDE.md scripts/ralph/CLAUDE.md    # For Claude Code

chmod +x scripts/ralph/ralph.sh
```

### Option 2: Install skills globally (Amp)

Copy the skills to your Amp or Claude config for use across all projects:

For AMP
```bash
cp -r skills/prd ~/.config/amp/skills/
cp -r skills/ralph ~/.config/amp/skills/
```

For Claude Code (manual)
```bash
cp -r skills/prd ~/.claude/skills/
cp -r skills/ralph ~/.claude/skills/
```

### Option 3: Use as Claude Code Marketplace

Add the Ralph marketplace to Claude Code:

```bash
/plugin marketplace add snarktank/ralph
```

Then install the skills:

```bash
/plugin install ralph-skills@ralph-marketplace
```

Available skills after installation:
- `/prd` - Generate Product Requirements Documents
- `/ralph` - Convert PRDs to prd.json format

Skills are automatically invoked when you ask Claude to:
- "create a prd", "write prd for", "plan this feature"
- "convert this prd", "turn into ralph format", "create prd.json"

### Configure Amp auto-handoff (recommended)

Add to `~/.config/amp/settings.json`:

```json
{
  "amp.experimental.autoHandoff": { "context": 90 }
}
```

This enables automatic handoff when context fills up, allowing Ralph to handle large stories that exceed a single context window.

## Workflow

### 1. Create a PRD

Use the PRD skill to generate a detailed requirements document:

```
Load the prd skill and create a PRD for [your feature description]
```

Answer the clarifying questions. The skill saves output to `tasks/prd-[feature-name].md`.

### 2. Convert PRD to Ralph format

Use the Ralph skill to convert the markdown PRD to JSON:

```
Load the ralph skill and convert tasks/prd-[feature-name].md to prd.json
```

This creates `prd.json` with user stories structured for autonomous execution.

### 3. Run Ralph

```bash
# Using Amp (default)
./scripts/ralph/ralph.sh [max_iterations]

# Using Claude Code
./scripts/ralph/ralph.sh --tool claude [max_iterations]
```

Default is 10 iterations. Use `--tool amp` or `--tool claude` to select your AI coding tool.

Ralph will:
1. Create a feature branch (from PRD `branchName`)
2. Pick the highest priority story where `passes: false`
3. Implement that single story
4. Run quality checks (typecheck, tests)
5. Commit if checks pass
6. Update `prd.json` to mark story as `passes: true`
7. Append learnings to `progress.txt`
8. Repeat until all stories pass or max iterations reached

## Key Files

| File | Purpose |
|------|---------|
| `ralph.sh` | The bash loop that spawns fresh AI instances (supports `--tool amp` or `--tool claude`) |
| `prompt.md` | Prompt template for Amp |
| `CLAUDE.md` | Prompt template for Claude Code |
| `prd.json` | User stories with `passes` status (the task list) |
| `prd.json.example` | Example PRD format for reference |
| `progress.txt` | Append-only learnings for future iterations |
| `skills/prd/` | Skill for generating PRDs (works with Amp and Claude Code) |
| `skills/ralph/` | Skill for converting PRDs to JSON (works with Amp and Claude Code) |
| `.claude-plugin/` | Plugin manifest for Claude Code marketplace discovery |
| `flowchart/` | Interactive visualization of how Ralph works |

## Critical Concepts

### Each Iteration = Fresh Context

Each iteration spawns a **new AI instance** (Amp or Claude Code) with clean context. The only memory between iterations is:
- Git history (commits from previous iterations)
- `progress.txt` (learnings and context)
- `prd.json` (which stories are done)

### Small Tasks

Each PRD item should be small enough to complete in one context window. If a task is too big, the LLM runs out of context before finishing and produces poor code.

### AGENTS.md Updates Are Critical

After each iteration, Ralph updates the relevant `AGENTS.md` files with learnings. This is key because AI coding tools automatically read these files, so future iterations (and future human developers) benefit from discovered patterns, gotchas, and conventions.

### Feedback Loops

Ralph only works if there are feedback loops:
- Typecheck catches type errors
- Tests verify behavior
- CI must stay green (broken code compounds across iterations)

### Browser Verification for UI Stories

Frontend stories must include "Verify in browser using dev-browser skill" in acceptance criteria. Ralph will use the dev-browser skill to navigate to the page, interact with the UI, and confirm changes work.

### Stop Condition

When all stories have `passes: true`, Ralph outputs `<promise>COMPLETE</promise>` and the loop exits.

## Docs

### AGENTS.md

# Ralph Agent Instructions

## Overview

Ralph is an autonomous AI agent loop that runs AI coding tools (Amp or Claude Code) repeatedly until all PRD items are complete. Each iteration is a fresh instance with clean context.

## Commands

```bash
# Run the flowchart dev server
cd flowchart && npm run dev

# Build the flowchart
cd flowchart && npm run build

# Run Ralph with Amp (default)
./ralph.sh [max_iterations]

# Run Ralph with Claude Code
./ralph.sh --tool claude [max_iterations]
```

## Key Files

- `ralph.sh` - The bash loop that spawns fresh AI instances (supports `--tool amp` or `--tool claude`)
- `prompt.md` - Instructions given to each AMP instance
- `CLAUDE.md` - Instructions given to each Claude Code instance
- `prd.json.example` - Example PRD format
- `flowchart/` - Interactive React Flow diagram explaining how Ralph works

## Patterns

- Each iteration spawns a fresh AI instance (Amp or Claude Code) with clean context
- Memory persists via git history, `progress.txt`, and `prd.json`
- Stories should be small enough to complete in one context window
- Always update AGENTS.md with discovered patterns for future iterations

### CLAUDE.md (iteration prompt for Claude Code)

You are an autonomous coding agent working on a software project.

**Task:** Read `prd.json`, pick the highest priority story where `passes: false`, implement it, run quality checks, commit with message `feat: [Story ID] - [Story Title]`, set `passes: true`, append to `progress.txt`.

Key rules:
- Work on ONE story per iteration
- ALL commits must pass quality checks (typecheck, lint, test)
- Append learnings to `progress.txt` and update CLAUDE.md files with reusable patterns
- Frontend stories require browser verification via dev-browser skill
- If ALL stories have `passes: true`, reply with `<promise>COMPLETE</promise>`

### prompt.md (iteration prompt for Amp)

Identical task flow as CLAUDE.md, with Amp-specific tooling:
- Includes thread URL in progress.txt (`https://ampcode.com/threads/$AMP_CURRENT_THREAD_ID`) for cross-iteration reference via `read_thread` tool
- AGENTS.md files are updated (Amp convention) rather than CLAUDE.md

### ralph.sh (main loop)

Bash script supporting `--tool amp|claude` flag and configurable `max_iterations` (default 10). For each iteration:
1. Runs the selected tool with the relevant prompt file
2. Pipes output to stderr while capturing it
3. Checks output for `<promise>COMPLETE</promise>` → exits 0 if found
4. Sleeps 2 seconds between iterations

On branch change: automatically archives previous `prd.json` + `progress.txt` to `archive/YYYY-MM-DD-feature-name/` and resets `progress.txt` for the new run.

## Top-level structure

```
.claude-plugin/          — Claude Code marketplace manifest (marketplace.json, plugin.json)
.github/                 — GitHub workflows (boilerplate; skipped)
.gitignore               — standard ignores
AGENTS.md                — agent instruction file for Amp/Claude
CLAUDE.md                — per-iteration prompt template for Claude Code
LICENSE                  — MIT License
README.md                — full setup and workflow documentation
flowchart/               — interactive React Flow visualization (Next.js app; npm run dev to run)
prd.json.example         — example PRD schema with userStories[], branchName, passes fields
prompt.md                — per-iteration prompt template for Amp
ralph-flowchart.png      — static flowchart image (binary; skipped)
ralph.sh                 — main bash loop script
ralph.webp               — project logo (binary; skipped)
skills/
  prd/                   — skill for generating Product Requirements Documents
  ralph/                 — skill for converting markdown PRDs to prd.json format
```
