---
type: source
source_url: https://zcode.z.ai/en
tags: [agentic-cli, glm-5.2, ade, goal-mode, mcp-servers, bot-control, zhipu-ai]
related: [warp.dev, factory.ai]
product: zcode
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

ZCode is Z.ai's (Zhipu AI) desktop and CLI-adjacent "Agentic Development Environment" (ADE), built specifically around Zhipu's own GLM-5.2 model family rather than a model-agnostic design. It packages an agent-driven coding workflow — plan, code, review, deploy — with long-running task automation ("Goal Mode"), remote steering via chat bots, and MCP server integration, competing in the same space as other agentic coding CLIs/IDEs like [[warp.dev]] and [[factory.ai]] but tied to a single model vendor's ecosystem.

_All claims below are sourced from ../../raw/web/zcode.z.ai.md unless otherwise noted._

## What it does

ZCode is described in its own docs as an "Agentic Development Environment (ADE) built to bring GLM-5.2 into real coding workflows," putting an AI agent — not manual coding — at the center of the workflow. The primary "ZCode Agent" is the default entry point for new tasks and is "deeply adapted for the GLM-5.2 model family," aimed at complex project understanding, long-task planning, and multi-turn context retention. The app itself is free to download and use; users bring their own GLM API key or model service plan (Zhipu, BigModel, Z.ai, or self-hosted).

## Key features

- **Goal Mode** — invoked with `/goal <objective>`, this drives long-running task automation: the agent iterates with continuous planning, execution, and automatic verification until the stated objective is met. Supporting commands: `/goal replace`, `/goal pause`, `/goal resume`, `/goal clear`. A live panel tracks elapsed time, token consumption, and iteration count.
- **Bot control** — ZCode sessions can be started and steered remotely from WeChat, Feishu, or Telegram, letting work continue away from the desktop.
- **In-task input modes** — `@` file references, `/` saved-prompt commands, `$` reusable skills, plus model/execution-mode switching and git-branch context awareness, all within one task.
- **Five execution modes** (cycle with `Shift+Tab`): Default, Confirm Before Changes, Auto Edit, Plan Mode, and Full Access — trading off caution against speed.
- **MCP server management** — a single Settings panel for both manually configured MCP servers and plugin-bundled ones, supporting stdio/SSE/HTTP transports, JSON import, and importing existing MCP configs from Claude Code (`~/.claude/settings.json`), Codex CLI (`~/.codex/config.toml`), OpenCode, or a generic `~/.agents/mcp.json`. Zhipu recommends `zai-mcp-server` (visual understanding), `web-search-prime`, and `web-reader`.
- **Project instructions** — reads a user-global `~/.zcode/AGENTS.md` plus a workspace-level `AGENTS.md`; explicitly does not merge instruction files across other directory levels.

## Architecture and concepts

ZCode ships as a native desktop application (not a pure terminal CLI) with an embedded terminal/workspace view, task list, and per-task commit/diff tooling ("Git tools," "Changes +N -N," "Commit"). Each task tracks a running transcript of agent actions (tool calls, file writes, verification commands) alongside a step-by-step progress checklist, similar in spirit to other goal-tracking agent harnesses. The product is tightly coupled to GLM-5.2 as its reasoning/coding backend — it is a harness for that model family rather than a provider-agnostic tool.

## Main APIs

Not a developer API/SDK product — ZCode is an end-user application. Model access is mediated through GLM Coding Plan subscriptions or direct API keys against Zhipu/BigModel/Z.ai endpoints; the docs note that the "Coding Plan," "OpenAI-compatible," and "Anthropic-compatible" endpoints are three separate access paths to the same underlying GLM models, and that terminal environment variables are configured separately from the desktop app's model setup (no automatic sync).

## When to use

ZCode fits teams and individuals already committed to Zhipu's GLM-5.2 models who want an integrated agentic coding environment with built-in long-running task tracking and mobile/remote control via chat apps, rather than a model-agnostic harness. It is not a fit for users who need multi-vendor model flexibility inside one tool, since it markets itself as GLM-5.2-first.

## Ecosystem

Installers are distributed for macOS (Apple Silicon and Intel), Windows (64-bit and ARM64), and Linux (beta, via a Feishu group). Pricing runs through the GLM Coding Plan: Lite ($16.20/mo, lightweight iteration), Pro ($64.80/mo, 5x Lite usage plus curated MCP tools), and Max ($144/mo, 20x Lite usage with dedicated resources). No public GitHub repository was found for ZCode itself — it is closed-source/proprietary, distributed only as signed installers.

**Correction note:** an initial automated fetch of the landing page mis-summarized ZCode as "an AI-powered CLI tool from Anthropic." This is incorrect and was verified against the raw page HTML (no mention of Anthropic on the site at all) — ZCode is Zhipu AI's/Z.ai's own product for their GLM model family and has no Anthropic affiliation. See the raw capture's Fetch notes section.
