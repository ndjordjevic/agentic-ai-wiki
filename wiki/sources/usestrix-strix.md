---
type: source
source_url: https://github.com/usestrix/strix
tags:
  - ai-pentesting
  - penetration-testing
  - autonomous-agents
  - security-testing
  - multi-agent
  - vulnerability-scanner
  - cli-tool
  - ci-cd-security
related:
  - litellm.ai
  - microsoft-playwright-mcp
product: strix
detail_level: standard
created: 2026-06-30
updated: 2026-06-30
---

Strix is an open-source AI penetration testing framework that deploys autonomous AI agents to find and validate security vulnerabilities through real proof-of-concept exploits — not static analysis false positives. At 27k+ GitHub stars, it sits at the intersection of agentic AI orchestration and application security, making it directly relevant to the Agentic AI Frameworks wiki as a production example of multi-agent coordination applied to offensive security.

_All claims below are sourced from ../../raw/github/usestrix-strix.md unless otherwise noted._

## What it does

Strix agents behave like human penetration testers: they run target applications dynamically, discover attack surfaces through reconnaissance, craft and execute exploits, and produce working proof-of-concept code for every confirmed finding. It accepts local codebases, GitHub repositories, and live URLs as targets, and supports both an interactive terminal TUI and headless `-n` mode for CI/CD pipelines.

## Installation

```bash
# curl installer (recommended)
curl -sSL https://strix.ai/install | bash

# or via pipx
pipx install strix-agent
```

Requires Docker (running) and an LLM API key. Configuration is stored in `~/.strix/cli-config.json` and can be passed via environment variables:

```bash
export STRIX_LLM="openai/gpt-5.4"
export LLM_API_KEY="your-api-key"
```

LLM routing is handled through LiteLLM (see [[litellm.ai]]), enabling any provider format (`openai/`, `anthropic/`, `vertex_ai/`, Ollama, etc.).

## Key features

- **Real exploit validation** — every finding ships with a working PoC; no unverified theoretical findings from static analysis
- **Multi-agent orchestration** — a graph of specialized AI agents (recon, exploitation, post-exploitation) run in parallel and share discoveries in real time
- **Comprehensive vulnerability coverage** — OWASP Top 10 and beyond: SQL injection, XSS, SSRF, XXE, IDOR, JWT attacks, race conditions, business logic flaws, infrastructure misconfigurations
- **Skills system** — structured knowledge packages injected into agent context at spawn time; up to 5 skills per agent drawn from 30+ categories (vulnerability techniques, frameworks, tools like Nuclei/ffuf/sqlmap)
- **Multiple target modes** — local directory, GitHub repo URL, or live web app URL; multi-target `-t` flag supported
- **Scan modes** — `quick` (diff-scoped for PRs), `standard` (default), full; `STRIX_REASONING_EFFORT` controls LLM thinking depth
- **Headless CI/CD mode** — `-n/--non-interactive` flag; exits non-zero when vulnerabilities are found; native GitHub Actions integration

## Architecture

Strix runs an **agentic loop** inside a Docker sandbox container. Each scan spawns a graph of specialized agents: a coordinator agent delegates tasks to specialist agents for reconnaissance, exploitation, and validation. Agents communicate shared findings and chain vulnerabilities cooperatively (e.g., an SSRF finding informs a subsequent privilege escalation attempt).

The sandbox environment pre-installs the full offensive security toolkit: Caido HTTP proxy for request interception and replay, Playwright-powered browser (see [[microsoft-playwright-mcp]]) for client-side attack testing, an interactive Bash shell, a Python sandbox for writing custom PoC scripts, Nuclei/ffuf/nmap/httpx/sqlmap and other standard pentest tools.

Source-code targets are copied into the sandbox container (up to 1 GB, configurable via `STRIX_MAX_LOCAL_COPY_MB`). The container is isolated per run; results are written to `strix_runs/<run-name>/`. Telemetry is emitted as OpenTelemetry spans, both locally to `events.jsonl` and optionally to a remote OTLP endpoint.

## Example usage

```bash
# Local codebase scan
strix --target ./app-directory

# GitHub repository review
strix --target https://github.com/org/repo

# Authenticated grey-box testing
strix --target https://your-app.com \
  --instruction "Perform authenticated testing using credentials: user:pass"

# Focused scope
strix --target api.your-app.com \
  --instruction "Focus on business logic flaws and IDOR vulnerabilities"

# Multi-target white-box testing
strix -t https://github.com/org/app -t https://your-app.com

# Headless PR diff scan
strix -n --target ./ --scan-mode quick --scope-mode diff --diff-base origin/main
```

CI/CD (GitHub Actions):

```yaml
- name: Run Strix
  env:
    STRIX_LLM: ${{ secrets.STRIX_LLM }}
    LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
  run: strix -n -t ./ --scan-mode quick
```

## Maintenance status

Active — 27,387 stars, latest release v1.0.4 (2026-06-09), pushed 2026-06-30. Licensed Apache 2.0. Primary language Python. Published to PyPI as `strix-agent`. The project has a hosted cloud platform at `app.strix.ai` with enterprise tiers (SSO, compliance reports, VPC deployment). Community on Discord (`discord.gg/strix-ai`).
