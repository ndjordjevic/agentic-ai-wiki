---
type: source
category: "Security"
source_url: https://github.com/nvidia/skillspector
tags:
  - skill-security-scanner
  - prompt-injection-detection
  - mcp-security
  - supply-chain-security
  - vuln-scoring
  - sarif-reporting
  - install-gating
related:
  - skills.sh
  - davila7-claude-code-templates
  - nvidia.com
product: skillspector
detail_level: standard
created: 2026-07-20
updated: 2026-07-28
---

SkillSpector is NVIDIA's open-source security scanner for AI agent skills, focused on evaluating whether a skill is safe to install before it reaches an agent runtime. It combines static pattern checks, optional LLM semantic analysis, and live supply-chain vulnerability lookups to produce a risk score and an install recommendation (`SAFE`, `CAUTION`, or `DO_NOT_INSTALL`) that can be used in local workflows, CI gates, or MCP-mediated install pipelines.

_All claims below are sourced from ../../raw/github/nvidia-skillspector.md unless otherwise noted._

## What it does

The CLI scans skills from multiple source forms (directory, single SKILL.md, Git URL, zip) and evaluates them against 68 vulnerability patterns across 17 categories, including prompt injection, anti-refusal patterns, data exfiltration, privilege escalation, supply-chain risks, memory poisoning, tool misuse, and MCP-specific least-privilege/tool-poisoning checks. It emits a consolidated risk score (0-100), severity band, and recommendation suitable for policy-driven install gating.

A baseline workflow (`skillspector baseline`) supports suppressing reviewed/accepted findings so rescans surface only new issues and risk scores reflect untriaged risk.

## Installation

Primary install path is `uv tool`:

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
```

MCP mode requires the extra dependency group:

```bash
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

## Key features

- **Two-stage analysis**: static analyzers first, optional LLM semantic filtering/intent analysis second.
- **SC4 live vulnerability lookups**: OSV.dev batch queries for dependency CVEs with offline fallback behavior.
- **Machine-consumable outputs**: JSON and SARIF for CI/IDE integrations, plus terminal/markdown for human review.
- **Recommendation model**: score-to-action mapping (`SAFE` / `CAUTION` / `DO_NOT_INSTALL`) with explicit exit-code semantics.
- **MCP runtime guardrail mode**: exposes `scan_skill` via MCP so install decisions can be enforced in agent workflows.
- **Permission/metadata safety checks for MCP skills**: LP1-LP4 least-privilege analyzer and TP1-TP4 tool-poisoning analyzer family.

## Architecture

The project is a Python scanner centered in `src/` with test coverage under `tests/`, analyzer-specific design docs under `docs/`, and optional MCP serving mode through `skillspector mcp`. The detection pipeline is explicitly split into static analysis (regex/AST/YARA/supply-chain checks) and optional LLM semantic analysis. Key infrastructure surfaces include `model_registry.yaml` (provider defaults), a Dockerized runtime, and baseline suppression schema examples (`.skillspector-baseline.example.yaml`) for policy-managed adoption.

## Example usage

```bash
skillspector scan ./my-skill/ --format json --output report.json
skillspector scan ./my-skill/ --no-llm
skillspector baseline ./my-skill/ -o .skillspector-baseline.yaml
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml
```

MCP mode:

```bash
skillspector mcp
claude mcp add skillspector -- skillspector mcp
```

## Maintenance status

13,453 stars, 1,109 forks, Apache-2.0 licensed, default branch `main`, last push 2026-07-14, and no tagged release listed at ingest time. The repo has active documentation for analyzer internals, CI-friendly output contracts, and explicit security-reporting policy, positioning it as an actively maintained security control in the agent-skills ecosystem.
