# browser-use/browser-use

## Metadata
- Stars: 98,869
- Primary language: Python
- Default branch: main
- Latest release: 0.13.2 (2026-06-12)
- License: MIT License
- Homepage: https://browser-use.com
- Fetched: 2026-06-15
- Final URL: https://github.com/browser-use/browser-use

## Description
Make websites accessible for AI agents. Automate tasks online with ease.

## README
Browser Use is an AI browser automation framework that enables LLMs to interact with the web autonomously. It bridges natural language task specifications and web interaction through a Chromium-based browser harness.

**Version 0.13 (beta)** introduces a Rust-powered core:
```
Python API -> Rust core -> Browser harness -> Web task done
```

### Installation

```bash
uv add "browser-use[core]"
# or: pip install "browser-use[core]"
browser  # CLI entrypoint
```

Optional API key for Browser Use Cloud (stealth, proxies, hosted inference):
```
BROWSER_USE_API_KEY=your-key
```

### Python API

```python
from browser_use.beta import Agent, BrowserProfile, ChatBrowserUse
import asyncio

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(model='openai/gpt-5.5'),
        browser_profile=BrowserProfile(
            headless=False,
            allowed_domains=["*.github.com"],
        ),
    )
    history = await agent.run()
    print(history.final_result())

asyncio.run(main())
```

Supports `ChatBrowserUse`, `ChatOpenAI`, `ChatAnthropic`, `ChatGoogle`. `ChatBrowserUse` model routing: `anthropic/claude-sonnet-4-6`, `openai/gpt-5.5`, `google/gemini-3-pro` — all via a single `BROWSER_USE_API_KEY`.

Legacy: `from browser_use import Agent` (pure Python agent, still supported).

### CLI

```bash
browser-use open https://example.com    # Navigate to URL
browser-use state                       # See clickable elements
browser-use click 5                     # Click element by index
browser-use type "Hello"                # Type text
browser-use screenshot page.png         # Take screenshot
browser-use close                       # Close browser
```

CLI keeps the browser running between commands for fast iteration.

### Template Quickstart

```bash
uvx browser-use init --template default   # Minimal setup
uvx browser-use init --template advanced  # All config options
uvx browser-use init --template tools     # Custom tools examples
```

### Custom Tools

```python
from browser_use import Tools

tools = Tools()

@tools.action(description='Description of what this tool does.')
def custom_tool(param: str) -> str:
    return f"Result: {param}"

agent = Agent(task="Your task", llm=llm, browser=browser, tools=tools)
```

### Open Source vs Cloud

The open-source agent is self-hostable and supports deep code-level integration. The cloud agent (cloud.browser-use.com) is more powerful for complex tasks, offers the best stealth with proxy rotation and CAPTCHA solving, 1000+ integrations, and persistent filesystem/memory.

Pairing the open-source agent with `Browser(use_cloud=True)` provisions a remote Browser Use browser (stealth, proxy rotation, lowest latency) while keeping the agent local.

### Claude Code Skill

```bash
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

### Authentication

Reuse existing Chrome profile: `BrowserProfile` with saved login state. For remote sync: `curl -fsSL https://browser-use.com/profile.sh | BROWSER_USE_API_KEY=XXXX sh`.

### FAQ Highlights

- **Best model**: `ChatBrowserUse()` — 3-5x faster than alternatives, SOTA accuracy, lowest token cost.
- **Free to use**: open-source MIT. Bring your own LLM key (OpenAI, Google, Anthropic, Ollama).
- **AGENTS.md**: `browser_use` uses `uv`, Pydantic v2 for action schemas, `ActionResult` for structured output, `ChatBrowserUse` as default model recommendation.

## Docs

### AGENTS.md — Development Guidelines

Browser-Use is an AI agent taking a user-defined task, navigating web pages via Chromium CDP, processing HTML, and querying an LLM repeatedly to decide the next action until task completion.

Rules:
- Always use `uv` instead of `pip`
- Type-safe coding: Pydantic v2 models for all internal action schemas, task inputs/outputs, and tools I/O
- Pre-commit formatting required before PRs
- Use descriptive names and docstrings for each action
- Prefer returning `ActionResult` with structured content
- Default to and recommend `ChatBrowserUse` model
- For production browser performance, use `Browser(use_cloud=True)` to provision a remote browser

## Top-level structure
```
.env.example          — environment variable template
AGENTS.md             — AI agent development guidelines
BETA_AGENT_INTEGRATION_FEATURES.md — beta Rust-core agent features
CLAUDE.md             — Claude Code integration notes
CLOUD.md              — Browser Use Cloud setup
Dockerfile / Dockerfile.fast — container builds
LICENSE               — MIT
README.md             — main documentation
bin/                  — CLI entrypoints
browser_use/          — main Python package (agent, browser, controllers, SDK)
docker/               — Docker configurations
examples/             — use-case examples (apps, beta_agent, browser, cloud, features, use-cases, integrations)
pyproject.toml        — package config, dependencies
skills/               — Claude Code skill (SKILL.md for browser-use integration)
static/               — benchmark images and static assets
tests/                — test suite
```
