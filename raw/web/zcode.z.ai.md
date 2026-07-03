# zcode.z.ai

## Fetch log
- Inbox URL: https://zcode.z.ai/en
- Final URL: https://zcode.z.ai/en
- Fetched: 2026-07-03
- Pages: 6
- Mode: standard

## Landing page — https://zcode.z.ai/en
ZCode - Simple, Fast, Vibe‑Ready | Official Harness for GLM-5.2

Log in / Docs / Changelog / Community / 中文 / Log in

🎉 ZCode 3.0: GLM-5.2 optimized, better multi-agent collaboration

Simple, Fast, Vibe‑Ready! ZCode combines the best AI agents with your existing tools so you can plan, code, review, and deploy without friction.

Download ZCode — Download .dmg (Apple Silicon) — View all downloads

Example workspace shown: New Task ⌘N, Open Workspace, Skills, Tasks — projects visible: gomoku-ai, zcode-website, zcode-desktop, release-bot, with individual task/commit entries (e.g. "Refine start prompts, turn-state messaging, and win copy", "Wire in heuristic AI turns and the player-first game flow", "Adapt board scaling and portrait/landscape layout for mobile", "Add rules copy, restart entry points, and empty-state guidance", "Fix bottom pinning when the conversation view is resized", "Refresh hero visual workspace and task mock data", "Tighten homepage English copy and unify positioning with CTAs", "Tune hero breakpoints for 13-inch screens and mobile", "Add pricing FAQ content and enterprise capability notes", "Improve docs search highlighting and empty-state feedback", "Debug the sidebar state mismatch after session recovery", "Reduce repaint cost after terminal panel resize", "Fix sidebar collapsed state not restoring after restart", "Audit settings IA to reduce advanced-option sprawl", "Add recent items and keyboard hints to the command palette", "Add remote-dev guidance and permission hints to onboarding", "Hook up changelog generation and draft GitHub Releases", "Draft a failed-CI summary template with retry guidance", "Connect tag validation, version sync, and release-note preview", "Write release announcement templates for patch and feature drops", "Add idempotent retries and alert dedupe for failed releases").

Live demo transcript shown in the hero (Ryan Bot, branch upgrade/v3.0): building a Gomoku game — "Create an intelligent Gomoku (Five-in-a-Row) game where the player competes against a smart algorithm that can make strategic moves and accurately detect winning conditions." Goal Complete banner: "Gomoku vs. AI — implement computer moves with a heuristic algorithm — 5/5 · 2m · 89K tokens". Progress checklist: "Initialize board, piece rendering, and the 15×15 grid layout", "Implement player move interaction and win-detection logic", "Integrate a heuristic AI for automatic computer moves", "Adapt board scaling and portrait/landscape layout for mobile", "Add rules copy, restart entry points, and empty-state guidance".

GLM Coding Plan
Code with GLM Coding Plan — GLM is tuned for ZCode, making agentic coding faster and steadier. View plans.

- **GLM Coding Lite** — For lightweight workloads — $16.2/month ($18) — Base usage allowance included. Built for lightweight iteration on small repo. Rolling access to the latest flagship models and features. Supports 20+ coding tools, including deep ZCode integration.
- **GLM Coding Pro** (Popular) — For professional workloads — $64.8/month ($72) — Everything in Lite, plus 5x Lite usage. Built for day-to-day development on mid-sized repos. Priority access to the latest flagship models and features. Includes a curated selection of MCP tools. Faster generation speeds.
- **GLM Coding Max** (Max Usage) — For high-volume workloads — $144/month ($160) — Everything in Pro, plus 20x Lite usage. Built for advanced users working on mid-to-large repos. First access to the latest flagship models and features. Dedicated resources during peak times.

Prices and plan benefits may change. Final details are shown on z.ai.

Capabilities — Stay on the Frontier
From understanding legacy monoliths to shipping real-time features, ZCode keeps every engineer on the frontier of software development.
- **Long-running tasks** — Use Goals to manage complex work with continuous planning, execution, and verification.
- **Bot control** — Start and steer ZCode from WeChat, Feishu, or Telegram so work can keep moving anywhere.
- **Deep GLM-5.2 integration** — Optimized for GLM-5.2 across reasoning, coding, and multi-agent collaboration.

All Downloads — All ZCode installers for every platform:
- MacOS: macOS (Apple Silicon) .dmg v3.2.3; macOS (Intel) .dmg v3.2.3
- Windows: Windows (64-bit) .exe v3.2.3; Windows (ARM64) .exe v3.2.3
- Linux (Beta): Linux x64 .deb v3.2.3; Linux x64 .AppImage v3.2.3; Linux ARM64 .deb v3.2.3; Linux ARM64 .AppImage v3.2.3

© 2026 ZCode. All rights reserved. Terms of Service / Privacy Policy / Support & Feedback

## Docs — https://zcode.z.ai/en/docs/welcome
Left-hand documentation navigation tree:

**Get Started**
- ZCode for GLM-5.2
- Install
- Connect Models
- Feedback & Support

**Core Features**
- ZCode Agent
- Goal Mode
- Remote Control
- Task & File Management
- Bot Channel
- Edit History
- Subagents
- Skill
- MCP Servers
- Plugin
- Command
- Usage Stats

**Integration**
- Safety Confirmation
- Remote Development
- ADE Tools

**Support**
- Keyboard Shortcuts
- FAQ (Q&A)

Page summary: ZCode is described as "an Agentic Development Environment (ADE) built to bring GLM-5.2 into real coding workflows." The platform emphasizes long-context capabilities and sustained task execution across planning, coding, and review phases. Key benefits include quota discounts for GLM Coding Plan subscribers and a five-day free trial for new users. The interface supports desktop, mobile Remote control, and integration with Feishu and WeChat bots for distributed task management.

Discovered doc page paths (from nav links in welcome page HTML): /en/docs/ADE-tools, /en/docs/agents, /en/docs/bot-channel, /en/docs/commands, /en/docs/configuration, /en/docs/edit-history, /en/docs/feedback, /en/docs/goal, /en/docs/install, /en/docs/keyboard-shortcuts, /en/docs/mcp-services, /en/docs/plugin, /en/docs/qa, /en/docs/remote-control, /en/docs/remote-development, /en/docs/safety-confirm, /en/docs/skill, /en/docs/subagents, /en/docs/task-management, /en/docs/usage-stats, /en/docs/welcome

## Install — https://zcode.z.ai/en/docs/install
ZCode v3.2.3 supports multiple platforms:
- macOS (Apple Silicon): .dmg installer
- macOS (Intel): .dmg installer
- Windows: .exe installer (x64 and ARM64 versions)
- Linux: Beta builds available through a Feishu group

Installation steps by platform:
- Windows: "Download the installer, double-click it, and follow the setup wizard to complete installation."
- macOS: "Open the downloaded DMG file, drag ZCode.app into the Applications folder, and then launch it from Launchpad."
- Linux: users must join a beta group to access the installation package, then follow their distribution's standard installation process.

Post-installation: open the application and complete sign-in to access the AI-assisted development features. Page also links to model configuration, feedback submission, and FAQ.

## ZCode Agent — https://zcode.z.ai/en/docs/agents
ZCode Agent is the primary self-developed agent in ZCode, designed as the default entry point for creating new tasks. It is "deeply adapted for the GLM-5.2 model family" and excels at complex project understanding, long-task planning, and multi-turn context retention.

Key capabilities — input methods within the same task:
- `@` references for files
- `/` commands for saved prompts
- `$` skills for reusable workflows
- Model and execution mode switching
- Git branch context awareness

Project instructions — ZCode reads instructions from two sources:
1. User global: `~/.zcode/AGENTS.md` (cross-project preferences)
2. Workspace level: `AGENTS.md` in the current workspace (project-specific rules)

"ZCode only reads the user global AGENTS.md and the current Workspace AGENTS.md" — does not merge multiple instruction files across directory levels.

Execution modes (five, cycle with Shift+Tab):
- Default Mode (balanced approach)
- Confirm Before Changes (high-risk tasks)
- Auto Edit (routine iteration)
- Plan Mode (complex multi-step tasks)
- Full Access (lower-risk, faster progress)

## Goal Mode — https://zcode.z.ai/en/docs/goal
Goal Mode enables long-running task automation through explicit objective-setting. Users invoke `/goal` to establish a session objective, after which the agent iteratively works toward completion with automatic verification at each step.

Key commands:
- `/goal <objective>` — establish the session goal
- `/goal replace <objective>` — modify the current goal
- `/goal pause` — temporarily halt progress
- `/goal resume` — restart paused work
- `/goal clear` — remove goal constraints

Operational characteristics: once activated, the system continuously iterates until verification confirms objective completion. A summary panel displays real-time metrics including elapsed duration, token consumption, and iteration count. Users can intervene mid-task by replacing objectives or pausing operations without losing progress.

Recommended use cases: multi-round tasks with clear success criteria, such as module refactoring with maintained test coverage, resolving compilation errors, achieving specific performance benchmarks. "The clearer the success criteria, the more accurate each round's verification."

## MCP Servers — https://zcode.z.ai/en/docs/mcp-services
MCP (Model Context Protocol) connects external capabilities such as file systems, browser automation, memory, and databases to Agents. ZCode manages the MCP server configuration used by ZCode Agent in one place.

List groups:
- Configured MCP servers: servers you added manually — edit, delete, enable, or disable them directly.
- Plugin MCP servers: servers installed together with plugins, managed by the corresponding plugin.

Create an MCP server: Open Settings → MCP Servers, click New MCP Server in the upper-right corner. Form mode is the fastest way to add common stdio servers:
1. Choose a Scope: User (available in all workspaces) or Workspace (current project only).
2. Enter a name, such as `memory`.
3. Keep the type as `stdio` (SSE and HTTP remote servers also supported).
4. Enter the command, such as `npx`, and arguments, such as `-y @modelcontextprotocol/server-memory`.
5. If the server needs keys or paths, expand Environment variables and add them there.
6. Click Add, then confirm the server is enabled in the list.

ZCode also supports HTTP and SSE remote services, plus JSON configuration import.

Import from an external agent:
- Claude Code: `~/.claude/settings.json`
- Codex CLI: `~/.codex/config.toml`
- OpenCode: `~/.config/opencode/opencode.json`
- Generic `.agents`: `~/.agents/mcp.json`

Recommended setup — Zhipu-related MCP servers:
- `zai-mcp-server`: visual understanding for images and screenshots
- `web-search-prime`: web search capability
- `web-reader`: webpage reading and parsing

## FAQ (Q&A) — https://zcode.z.ai/en/docs/qa
1. What is ZCode's product positioning? ZCode is described as an "Agentic Development Environment (ADE)" that "puts AI Agents at the center of the workflow" rather than manual coding. It emphasizes full-context awareness and aims to strengthen long-task execution stability.
2. Is ZCode free? "The ZCode application itself is completely free." However, users need their own API Key or model service plan through providers like Zhipu, BigModel, Z.ai, or self-hosted services.
3. Terminal GLM API configuration — need to reconfigure? Yes. "Terminal environment variables and the ZCode desktop model setup are separate entry points, so configuration is not synced automatically."
4. Why does Connect keep loading? Check network connectivity to the model service and verify the account or API Key has active quota and model access.
5. Why can't I select folders with `@`? The `@` picker only selects individual files. To add entire folders, drag them directly from file explorers into the input box instead.
6. Endpoint differences (Coding Plan vs. Anthropic vs. OpenAI)? The three BigModel/Z.ai endpoints serve different purposes: Coding Plan for GLM Coding Plan subscribers, general OpenAI for resource packages, and Anthropic protocol for the same packages via Anthropic compatibility.

## Fetch notes
- `https://zcode.z.ai/llms.txt` returned the SPA's client-rendered HTML shell (no static llms.txt catalog), so it was treated as absent per protocol.
- No `github.com/<org>/<repo>` companion repository was found anywhere in the captured content — ZCode is closed-source/proprietary, distributed only as signed installers. No companion fetch performed.
- **Correction:** an initial WebFetch pass on the landing page hallucinated "AI-powered CLI tool from Anthropic." Verified against raw HTML (`curl`) that this is false — ZCode is Z.ai's (Zhipu AI) own harness for their GLM-5.2 model family and has no Anthropic affiliation. The content above reflects the verified raw fetch.
