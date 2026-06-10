# hermes-agent.nousresearch.com

## Fetch log
- Inbox URL: https://hermes-agent.nousresearch.com/
- Final URL: https://hermes-agent.nousresearch.com/
- Fetched: 2026-06-10
- Pages: 8
- Mode: standard

## Landing page — https://hermes-agent.nousresearch.com/

**Hermes Agent — The Agent That Grows With You**

Navigation: Docs | Portal | Desktop App | GitHub | Discord

Hermes Agent is an open source tool released under the MIT License. It functions as "an autonomous agent that lives on your server, remembers what it learns, and gets more capable the longer it runs."

**Installation:**
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Key Features:**
- Multi-platform connectivity (Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI)
- Persistent memory and auto-generated skills
- Natural language scheduling for automated tasks
- Subagent delegation and parallel processing
- Sandboxing with six backend options (local, Docker, SSH, Singularity, Modal, Daytona)
- Web search, browser automation, vision capabilities, and multi-model reasoning

**Footer:** Version 0.16.0 | Developed by Nous Research | MIT License © 2026

## Docs — https://hermes-agent.nousresearch.com/docs

Hermes Agent is "the self-improving AI agent built by Nous Research" with a distinctive learning loop that creates skills from experience and improves them during use.

**Installation Methods:**
- Desktop: Download installer from hermes-agent.nousresearch.com/desktop
- Linux/macOS/WSL2/Android: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Windows PowerShell: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`

**Core Capabilities:**
- Closed-loop learning with persistent cross-session memory
- Deployment flexibility across local, Docker, SSH, Daytona, Singularity, and Modal backends
- 60+ built-in tools including web search, image generation, TTS, and browser automation
- MCP (Model Context Protocol) server integration
- Voice mode with real-time interaction capabilities
- Skill creation and community sharing via agentskills.io

**Machine-readable documentation indexes:** `/llms.txt` (~17 KB) and `/llms-full.txt` (~1.8 MB) for programmatic access.

## Skills Hub — https://hermes-agent.nousresearch.com/docs/skills

Skills discovery platform for Hermes Agent. Designed to "Discover, search, and install from 88k+ skills across every registry."

**Navigation:** Docs | Skills | Download | Language selector (English, 简体中文)

**Skills Categories:**
- Built-in skills
- Optional skills
- Community skills

**Documentation Links (from skills hub navigation):**
- Getting Started/Quickstart
- User Guide (CLI)
- Developer Guide (Architecture)
- Reference (CLI Commands)

**Community & Resources:**
- Discord community
- GitHub repository and issues
- Skills Hub at agentskills.io
- Desktop download option

Built by Nous Research · MIT License · 2026

## Quickstart — https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

**Installation:** Hermes Desktop installer (macOS/Windows), shell script (Linux/macOS/WSL2/Android Termux), or PowerShell (Windows).

**Provider Selection:** The guide emphasizes choosing an AI provider as "the single most important setup step."

Options:
- Nous Portal (subscription-based)
- OpenAI, Anthropic, OpenRouter
- Local models (Ollama, LM Studio)
- 30+ additional providers (DeepSeek, xAI, Google Gemini, AWS Bedrock, etc.)

**Key requirement:** Models must support at least 64,000 tokens of context.

**Core Features after setup:**
- Run terminal commands through the agent
- Use slash commands (`/help`, `/tools`, `/model`)
- Enable voice mode via `faster-whisper`
- Connect messaging platforms (Telegram, Discord, Slack, WhatsApp, Signal, Email, Teams)
- Install reusable skills from the Skills Hub
- Configure MCP servers and editor integration (ACP)

**Recovery Toolkit:** `hermes doctor` → `hermes model` → `hermes setup` → session checks → gateway status.

## Skills System — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

Skills are on-demand knowledge documents that agents load when needed, following a progressive disclosure pattern to minimize token usage. Compatible with the agentskills.io open standard.

**Storage:** All skills reside in `~/.hermes/skills/` as the primary source of truth.

```
~/.hermes/skills/
├── category/
│   ├── skill-name/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   ├── templates/
│   │   ├── scripts/
│   │   └── assets/
```

**Progressive Disclosure Loading:**
- Level 0: `skills_list()` returns metadata (~3k tokens)
- Level 1: `skill_view(name)` loads full content
- Level 2: `skill_view(name, path)` retrieves specific files

**Skill Format:** YAML frontmatter with metadata including name, description, version, platforms, and optional conditional activation settings.

**Usage:** Access via slash commands (`/skill-name`), natural conversation, or bundled commands that load multiple skills simultaneously.

**Advanced Capabilities:**
- Platform-specific skills (macOS, Linux, Windows)
- Conditional activation via `fallback_for_toolsets`, `requires_toolsets`
- External skill directories via config.yaml
- Skill bundles for grouping multiple skills under one slash command
- Agent-managed skills: agents create and update their own skills via the `skill_manage` tool

**Skills Hub Sources:**
- Official optional skills
- skills.sh directory
- Well-known endpoints (`/.well-known/skills/`)
- Direct GitHub repositories
- Third-party marketplaces (ClawHub, LobeHub, browse.sh)
- Direct URLs to single-file SKILL.md files

**Security:** All hub-installed skills undergo security scanning. Trust levels range from builtin to community, with policy overrides available.

**Custom Taps:** Publish curated skill collections as GitHub repositories for team sharing.

## Memory — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory

Hermes Agent has bounded, curated memory that persists across sessions.

**Memory Files:**

| File | Purpose | Char Limit |
|---|---|---|
| MEMORY.md | Agent's personal notes — environment facts, conventions, things learned | 2,200 chars (~800 tokens) |
| USER.md | User profile — preferences, communication style, expectations | 1,375 chars (~500 tokens) |

Both stored in `~/.hermes/memories/` and injected into the system prompt as a frozen snapshot at session start.

**Frozen snapshot pattern:** The system prompt injection is captured once at session start and never changes mid-session. Changes persist to disk immediately but don't appear until the next session (preserves LLM prefix cache for performance).

**Memory Tool Actions:** `add`, `replace` (substring matching), `remove` (substring matching)

**Session Search:** Beyond MEMORY.md and USER.md, the agent can search past conversations via `session_search` tool using SQLite FTS5. All CLI and messaging sessions stored in `~/.hermes/state.db`.

**External Memory Providers:** 8 plugins available including Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover, and Supermemory. Run alongside built-in memory, adding knowledge graphs, semantic search, automatic fact extraction.

**Capacity management:** When memory is full, the tool returns an error asking the agent to consolidate or replace entries.

**write_approval gate:** `memory.write_approval: true` stages writes for user approval before committing; supports both foreground inline approval and background staged approval.

**Configuration:**
```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200
  user_char_limit: 1375
  write_approval: false
```

## Architecture — https://hermes-agent.nousresearch.com/docs/developer-guide/architecture

**System Overview:** Hermes Agent operates through three main entry points: CLI, Gateway API Server, and ACP (Python Library). These feed into the core AIAgent orchestration engine.

**Key Components:**
- **Core Agent Loop** (`run_agent.py`): Synchronous orchestration engine handles provider selection, prompt construction, tool execution, retries, fallback, callbacks, compression, and persistence.
- **Prompt Assembly**: Multi-tier system combining stable identity/tool guidance with context files and volatile memory blocks via `prompt_builder.py` and `prompt_caching.py`.
- **Provider Resolution**: Maps provider-model pairs to API modes and credentials across 18+ providers with OAuth support.
- **Tool Registry** (`tools/registry.py`): Manages 70+ tools across ~28 toolsets with 6 terminal execution backends.
- **Session Persistence**: SQLite-based with lineage tracking and atomic writes for conversation history.

**Data Flow Patterns:**
1. CLI: User input → prompt building → API call → tool dispatch → response display
2. Gateway: Platform event → authorization → AIAgent execution → platform delivery
3. Cron: Scheduled jobs → fresh agent → skill injection → platform targeting

**Design Principles:** Prompt stability (no mid-conversation mutations), observable execution (visible tool calls), interruptibility, platform-agnostic core logic, loose coupling through registries, profile isolation for concurrent operation.

## Messaging Gateway — https://hermes-agent.nousresearch.com/docs/user-guide/messaging

**Platform Coverage:** 24+ messaging platforms including Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email, Home Assistant, Mattermost, Matrix, DingTalk, Feishu/Lark, WeCom, Weixin, BlueBubbles (iMessage), QQ, Microsoft Teams, LINE, ntfy, and browser.

**Feature Comparison across platforms:** Voice support, Image handling, File attachments, Threaded conversations, Emoji reactions, Typing indicators, Message streaming. Discord, Slack, Matrix, and Feishu/Lark rank highest with full feature support.

**Setup:** `hermes gateway setup` — interactive wizard with arrow-key navigation.

**Core Commands within messaging:**
- `/new` or `/reset` — reset conversation
- `/model` — change AI model
- `/personality` — adjust tone
- `/status` — session info
- `/background` — run independent tasks

**Security Architecture:** Defaults to denying access unless users are allowlisted or paired via DM. `TELEGRAM_ALLOWED_USERS` environment variable and DM pairing via one-time codes.

**Session Management:** Sessions persist until reset, with configurable reset policies (daily at specific times or after idle periods) per platform in `~/.hermes/gateway.json`.

**Service Operations:** Linux uses systemd (user or system-wide); macOS uses launchd agents.

**Advanced Features:** Automatic circuit breakers for failed adapters, session resumption after restarts, background task execution, tool-progress notifications with platform-specific mobile-friendly defaults.
