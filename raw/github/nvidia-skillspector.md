# nvidia/skillspector

## Metadata
- Stars: 13453
- Primary language: Python
- Default branch: main
- Latest release: (none)
- License: Apache License 2.0
- Homepage: (none)
- Fetched: 2026-07-20
- Final URL: https://github.com/NVIDIA/SkillSpector

## Description
Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks.

## README
# SkillSpector

**Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills.

## Overview

AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. Research states **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**.

SkillSpector frames the core question as: **"Is this skill safe to install?"**

## Features

- Multi-format input: scan Git repos, URLs, zip files, directories, or single files
- **68 vulnerability patterns** across 17 categories
- Two-stage analysis: static analysis + optional LLM semantic evaluation
- Live vulnerability lookup via OSV.dev (SC4) with offline fallback
- Output formats: terminal, JSON, Markdown, SARIF
- Risk scoring: 0-100 with recommendation mapping
- Baseline suppression for accepted findings (`skillspector baseline`)

## Quick Start

### Installation (uv)

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
# Update later:
uv tool update skillspector
```

MCP mode install:

```bash
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

### Basic Usage

```bash
# Scan a local skill directory
skillspector scan ./my-skill/

# Scan a single SKILL.md file
skillspector scan ./SKILL.md

# Scan a Git repository
skillspector scan https://github.com/user/my-skill

# Scan a zip file
skillspector scan ./my-skill.zip
```

### Output Formats

```bash
skillspector scan ./my-skill/                              # terminal
skillspector scan ./my-skill/ --format json --output report.json
skillspector scan ./my-skill/ --format markdown --output report.md
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

### Baseline / false-positive suppression

```bash
skillspector baseline ./my-skill/ -o .skillspector-baseline.yaml
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml --show-suppressed
```

### LLM providers (README table highlights)

- `openai` (`OPENAI_API_KEY`)
- `anthropic` (`ANTHROPIC_API_KEY`)
- `anthropic_proxy` (Vertex-style endpoint + bearer key)
- `bedrock` (SigV4 via boto3)
- `nv_build` (`NVIDIA_INFERENCE_KEY`)
- `claude_cli` / `codex_cli` (local authenticated CLI session, no API key env var required)

Skip semantic stage:

```bash
skillspector scan ./my-skill/ --no-llm
```

### MCP Server

SkillSpector can run as an MCP server and expose one tool:

- `scan_skill(target, use_llm=true, output_format="json")`

Commands:

```bash
skillspector mcp
skillspector mcp --transport http --host 127.0.0.1 --port 8000
claude mcp add skillspector -- skillspector mcp
```

HTTP transport note from README: no built-in auth; remote exposure requires an authenticated reverse proxy. Over HTTP, local paths and `file://` URLs are blocked; remote Git and zip URLs are accepted.

### Risk scoring

- CRITICAL: +50
- HIGH: +25
- MEDIUM: +10
- LOW: +5
- Executable scripts multiplier: 1.3x

Severity bands:
- 0-20: LOW (`SAFE`)
- 21-50: MEDIUM (`CAUTION`)
- 51-80: HIGH (`DO_NOT_INSTALL`)
- 81-100: CRITICAL (`DO_NOT_INSTALL`)

### Exit codes

- `0`: scan completed and risk score <= 50
- `1`: scan completed and risk score > 50
- `2`: error

## Docs

### docs/SUPPRESSION.md (baseline model)

- Baselines suppress known findings so risk score reflects only un-triaged issues.
- Supports both exact fingerprints and drift-tolerant glob rules.
- Suppressed findings are excluded from score and SARIF; visible with `--show-suppressed` and always listed in JSON output.

### docs/SC4-osv-live-vulnerability-lookups.md

- SC4 moved from small static CVE lists to OSV.dev `querybatch`.
- Covers both PyPI and npm without auth token.
- Uses in-memory caching and graceful fallback to bundled static lists when OSV is unavailable.
- Removed fragile custom version-comparison dependence from primary path.

### docs/B.3.1-mcp-least-privilege.md

- Analyzer compares declared manifest permissions against detected code capabilities.
- Emits LP1-LP4 findings:
  - LP1 underdeclared capability (HIGH)
  - LP2 wildcard permission (MEDIUM)
  - LP3 missing permission declaration (MEDIUM)
  - LP4 overdeclared permission (LOW)
- Static-only node (no LLM/network), fast execution.

### docs/B.3.2-mcp-tool-poisoning.md

- Tool metadata treated as attack surface (name, description, triggers, parameters).
- TP1-TP4 checks:
  - hidden instructions
  - unicode deception
  - parameter description injection
  - description-behavior mismatch (optional LLM check)
- Covers MITRE ATLAS AML.T0080-style poisoning vectors.

### SECURITY.md (top-level)

- NVIDIA security policy and reporting path.
- Security concerns should be reported via NVIDIA's vulnerability reporting channel, not public issue disclosure first.

## Top-level structure

- `src/` — core scanner implementation and analyzer pipeline
- `tests/` — unit/integration tests
- `docs/` — architecture, analyzers, suppression, SC4/OSV notes, MCP-specific docs
- `extensions/` — extension packaging
- `contrib/` — batch scan tooling and supporting docs
- `model_registry.yaml` — provider/model defaults
- `pyproject.toml` / `uv.lock` — Python packaging and dependencies
- `package.json` — Node-side metadata/tooling hooks
- `langgraph.json` — LangGraph config
- `Dockerfile` — containerized scanner runtime
- `.skillspector-baseline.example.yaml` — baseline suppression example schema
