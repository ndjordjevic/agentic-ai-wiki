# usestrix/strix

## Metadata
- Stars: 27387
- Primary language: Python
- Default branch: main
- Latest release: v1.0.4 (2026-06-09)
- License: Apache License 2.0
- Homepage: https://strix.ai
- Fetched: 2026-06-30
- Final URL: https://github.com/usestrix/strix

## Description
Open-source AI penetration testing tool to find and fix your app's vulnerabilities.

## README

<p align="center">
  <a href="https://strix.ai/">
    <img src="https://github.com/usestrix/.github/raw/main/imgs/cover.png" alt="Strix Banner" width="100%">
  </a>
</p>

<div align="center">

# Strix

### The open-source AI pentesting tool. Autonomous AI hackers that find and fix your app's vulnerabilities.

</div>

> **New!** Strix integrates seamlessly with GitHub Actions and CI/CD pipelines. Automatically scan for vulnerabilities on every pull request and block insecure code before it reaches production.

---

## Strix Overview

Strix are autonomous AI penetration testing agents that act just like real hackers - they run your code dynamically, find vulnerabilities, and validate them through actual proof-of-concepts. Built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting or the false positives of static analysis tools.

**Key Capabilities:**

- **Full pentesting toolkit** - reconnaissance, exploitation, and validation out of the box
- **Multi-agent orchestration** - teams of AI pentesters that collaborate and scale
- **Real exploit validation** - working PoCs, not false positives like legacy vulnerability scanners
- **Developer‑first CLI** - actionable findings with remediation guidance
- **Auto‑fix & reporting** - generate patches and compliance-ready pentest reports

## Use Cases

- **Application Security Testing** - Detect and validate critical vulnerabilities in your applications
- **Rapid Penetration Testing** - Get penetration tests done in hours, not weeks, with compliance reports
- **Bug Bounty Automation** - Automate bug bounty research and generate PoCs for faster reporting
- **CI/CD Integration** - Run tests in CI/CD to block vulnerabilities before reaching production

## Quick Start

**Prerequisites:**
- Docker (running)
- An LLM API key from any supported provider (OpenAI, Anthropic, Google, etc.)

### Installation & First Scan

```bash
# Install Strix
curl -sSL https://strix.ai/install | bash

# Configure your AI provider
export STRIX_LLM="openai/gpt-5.4"
export LLM_API_KEY="your-api-key"

# Run your first security assessment
strix --target ./app-directory
```

> First run automatically pulls the sandbox Docker image. Results are saved to `strix_runs/<run-name>`

## Strix Platform

Try the Strix full-stack penetration testing platform at **[app.strix.ai](https://app.strix.ai)** - sign up for free, connect your repos and domains, and launch a pentest in minutes.

- **Validated findings with PoCs** - every vulnerability includes a working proof-of-concept exploit and reproduction steps
- **One-click autofix** - AI-generated security patches as ready-to-merge pull requests
- **Continuous pentesting** - always-on vulnerability scanning that keeps pace with your deployments
- **DevSecOps integrations** - GitHub, GitLab, Bitbucket, Slack, Jira, Linear, and CI/CD pipelines
- **Continuous learning** - AI that builds on past findings, adapts to your codebase, and reduces false positives over time

## Features

### Agentic Pentesting Tools

Strix agents come equipped with a comprehensive offensive security toolkit:

- **HTTP Interception Proxy** - Full request/response manipulation and analysis with Caido
- **Browser Exploitation** - Automated browser for testing XSS, CSRF, clickjacking, and auth bypass flows
- **Shell & Command Execution** - Interactive terminal for exploit development and post-exploitation
- **Custom Exploit Runtime** - Python sandbox for writing and validating proof-of-concept exploits
- **Reconnaissance & OSINT** - Automated attack surface mapping, subdomain enumeration, and fingerprinting
- **Static & Dynamic Code Analysis** - SAST + DAST capabilities for comprehensive application security testing
- **Vulnerability Knowledge Base** - Structured findings with CVSS scoring and OWASP classification

### Comprehensive Vulnerability Scanner

- **Broken Access Control** - IDOR, privilege escalation, auth bypass
- **Injection Attacks** - SQL injection, NoSQL injection, OS command injection, SSTI
- **Server-Side Vulnerabilities** - SSRF, XXE, insecure deserialization, RCE
- **Client-Side Attacks** - XSS (stored/reflected/DOM), prototype pollution, CSRF
- **Business Logic Flaws** - Race conditions, payment manipulation, workflow bypass
- **Authentication & Session** - JWT attacks, session fixation, credential stuffing vectors
- **Infrastructure & Cloud** - Misconfigurations, exposed services, cloud security issues
- **API Security** - Broken authentication, mass assignment, rate limiting bypass

### Graph of Agents (Multi-Agent Pentesting)

- **Distributed Pentesting** - Specialized AI agents for recon, exploitation, and post-exploitation
- **Scalable Security Testing** - Parallel execution across multiple targets for fast, comprehensive coverage
- **Dynamic Coordination** - Agents share discoveries, chain vulnerabilities, and collaborate like a red team

## Usage Examples

### Basic Usage

```bash
# Scan a local codebase
strix --target ./app-directory

# Security review of a GitHub repository
strix --target https://github.com/org/repo

# Black-box web application assessment
strix --target https://your-app.com
```

### Advanced Testing Scenarios

```bash
# Grey-box authenticated testing
strix --target https://your-app.com --instruction "Perform authenticated testing using credentials: user:pass"

# Multi-target testing (source code + deployed app)
strix -t https://github.com/org/app -t https://your-app.com

# White-box source-aware scan (local repository)
strix --target ./app-directory --scan-mode standard

# Focused testing with custom instructions
strix --target api.your-app.com --instruction "Focus on business logic flaws and IDOR vulnerabilities"

# Force PR diff-scope against a specific base branch
strix -n --target ./ --scan-mode quick --scope-mode diff --diff-base origin/main
```

### Headless Mode

```bash
strix -n --target https://your-app.com
```

### CI/CD (GitHub Actions)

```yaml
name: strix-penetration-test

on:
  pull_request:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Install Strix
        run: curl -sSL https://strix.ai/install | bash

      - name: Run Strix
        env:
          STRIX_LLM: ${{ secrets.STRIX_LLM }}
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
        run: strix -n -t ./ --scan-mode quick
```

### Configuration

```bash
export STRIX_LLM="openai/gpt-5.4"
export LLM_API_KEY="your-api-key"

# Optional
export LLM_API_BASE="your-api-base-url"
export PERPLEXITY_API_KEY="your-api-key"  # for search capabilities
export STRIX_REASONING_EFFORT="high"  # control thinking effort (default: high, quick scan: medium)
```

**Recommended models for best results:**

- OpenAI GPT-5.4 - `openai/gpt-5.4`
- Anthropic Claude Sonnet 4.6 - `anthropic/claude-sonnet-4-6`
- Google Gemini 3 Pro Preview - `vertex_ai/gemini-3-pro-preview`

## Enterprise Pentesting

Get the same Strix experience with enterprise-grade controls: SSO (SAML/OIDC), custom compliance-ready penetration testing reports (SOC 2, ISO 27001, PCI DSS), dedicated support & SLA, custom deployment options (VPC/self-hosted), BYOK model support.

## Documentation

Full documentation is available at **[docs.strix.ai](https://docs.strix.ai)**.

## Acknowledgements

Strix builds on the work of: LiteLLM, Caido, Nuclei, Playwright, and Textual.

> **Warning:** Only test apps you own or have permission to test. You are responsible for using Strix ethically and legally.

## Docs

### docs/index.mdx — Introduction

Strix are autonomous AI agents that act like real hackers—they run your code dynamically, find vulnerabilities, and validate them with proof-of-concepts.

**Key Capabilities:**
- Full hacker toolkit — Browser automation, HTTP proxy, terminal, Python runtime
- Real validation — PoCs, not false positives
- Multi-agent orchestration — Specialized agents collaborate on complex targets
- Developer-first CLI — Interactive TUI or headless mode for automation

**Security Tools table:**

| Tool | Purpose |
|------|---------|
| HTTP Proxy | Full request/response manipulation and analysis |
| Browser Automation | Multi-tab browser for XSS, CSRF, auth flow testing |
| Terminal | Interactive shells for command execution |
| Python Runtime | Custom exploit development and validation |
| Reconnaissance | Automated OSINT and attack surface mapping |
| Code Analysis | Static and dynamic analysis capabilities |

**Multi-Agent Architecture:**
- Distributed Workflows — Specialized agents for different attacks and assets
- Scalable Testing — Parallel execution for fast comprehensive coverage
- Dynamic Coordination — Agents collaborate and share discoveries

### docs/quickstart.mdx — Quick Start

Prerequisites: Docker (running), LLM API key.

Installation options:
```bash
# curl
curl -sSL https://strix.ai/install | bash

# pipx
pipx install strix-agent
```

Target types:
```bash
strix --target ./app-directory           # Local codebase
strix --target https://github.com/org/repo  # GitHub repository
strix --target https://your-app.com      # Live web application
strix -t https://github.com/org/repo -t https://your-app.com  # Multiple targets
```

### docs/advanced/configuration.mdx — Configuration Reference

Environment variables:

| Variable | Default | Description |
|---|---|---|
| `STRIX_LLM` | (required) | Model name in LiteLLM format |
| `LLM_API_KEY` | — | API key for LLM provider |
| `LLM_API_BASE` | — | Custom API base URL |
| `LLM_TIMEOUT` | 300 | Request timeout (seconds) |
| `STRIX_LLM_MAX_RETRIES` | 5 | Max retries for LLM API calls |
| `STRIX_REASONING_EFFORT` | high | Thinking effort: none/minimal/low/medium/high/xhigh |
| `PERPLEXITY_API_KEY` | — | Enables real-time web search for OSINT |
| `STRIX_TELEMETRY` | 1 | Set to 0/false to disable telemetry |
| `STRIX_IMAGE` | ghcr.io/usestrix/strix-sandbox:1.0.0 | Docker sandbox image |
| `STRIX_SANDBOX_EXECUTION_TIMEOUT` | 120 | Max sandbox execution time (seconds) |

Config file: `~/.strix/cli-config.json`

### docs/advanced/skills.mdx — Skills System

Skills are structured knowledge packages that give Strix agents deep expertise in specific vulnerability types, technologies, and testing methodologies.

When Strix spawns an agent, it selects up to 5 relevant skills based on context and injects them into the agent's system prompt.

**Skill categories:**

Vulnerabilities: `authentication_jwt`, `idor`, `sql_injection`, `xss`, `ssrf`, `csrf`, `xxe`, `rce`, `business_logic`, `race_conditions`, `path_traversal_lfi_rfi`, `open_redirect`, `mass_assignment`, `insecure_file_uploads`, `information_disclosure`, `subdomain_takeover`, `broken_function_level_authorization`

Frameworks: `fastapi`, `nextjs`

Technologies: `supabase`, `firebase_firestore`

Protocols: `graphql`

Tooling: `nmap`, `nuclei`, `httpx`, `ffuf`, `subfinder`, `naabu`, `katana`, `sqlmap`

Each skill is a Markdown file with YAML frontmatter. Community contributions welcome.

### docs/tools/overview.mdx — Agent Tools

| Tool | Purpose |
|---|---|
| Browser (Playwright) | Chrome automation for web UI testing |
| HTTP Proxy (Caido) | Intercepting and replaying requests |
| Terminal | Bash shell for security tools and commands |
| Sandbox Tools | Nuclei, ffuf, and pre-installed security tools |
| Python Runtime | Write and execute custom exploit scripts |
| File Editor | Read and modify source code |
| Web Search | Real-time OSINT via Perplexity |
| Notes | Document findings during scan |
| Reporting | Generate vulnerability reports with PoCs |

## Top-level structure

```
.github/          — GitHub workflows and org images
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
LICENSE           — Apache License 2.0
Makefile
README.md         — Main documentation
benchmarks/       — Performance benchmarks
containers/       — Docker/container configurations
docs/             — Documentation (Mintlify MDX format)
  advanced/       — Configuration and Skills docs
  cloud/          — Cloud platform docs
  integrations/   — CI/CD integration guides (GitHub Actions)
  llm-providers/  — LLM provider configuration
  tools/          — Agent tool documentation
  usage/          — CLI usage and scan modes
pyproject.toml    — Python package config (strix-agent on PyPI)
scripts/          — Utility scripts
strix.spec        — PyInstaller spec for binary builds
strix/            — Main Python source package
  agents/         — AI agent definitions
  config/         — Configuration handling
  core/           — Core logic
  interface/      — TUI/CLI interface
  report/         — Report generation
  runtime/        — Sandbox runtime
  skills/         — Built-in skill Markdown files
  telemetry/      — OpenTelemetry integration
  tools/          — Agent tool implementations
  utils/          — Utility modules
tests/            — Test suite
uv.lock           — uv dependency lockfile
```
