---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://www.sonarsource.com/
tags:
  - code-verification
  - static-analysis
  - quality-gates
  - agent-centric-development-cycle
  - sonarqube-mcp-server
  - agent-context-injection
  - automated-remediation
  - ai-code-review
related:
  - coderabbit.ai
  - greptile.com
  - openqodex-openqodex
  - The-PR-Agent-pr-agent
product: sonarsource
detail_level: standard
created: 2026-10-15
updated: 2026-10-26
---

Sonar (SonarSource) is the company behind SonarQube, a long-established static-analysis and code-quality platform that it now positions as an independent, "zero-trust" verification layer for AI-written code. Its framework for this is the **Agent Centric Development Cycle (AC/DC)**: **Guide** agents with project context and constraints, **Verify** their output, and **Solve** findings with verified fixes. These stages run across three loops: inside the agent's session, in CI, and as background tech-debt cleanup. Several agent-facing products sit on top of the SonarQube engine: Sonar Vortex for in-loop context and verification, the SonarQube MCP Server, the SonarQube CLI, one-command agent plugins for Claude Code, Codex, Copilot CLI, Cursor and Antigravity, the Remediation and Hunter agents, and Gitar for AI PR review. For this wiki, Sonar is the deterministic-analysis counterpart to LLM-based code reviewers. It is a way to put quality gates inside the coding agent's own loop instead of only at the pull request.

_All claims below are sourced from ../../raw/web/sonarsource.com.md unless otherwise noted._

## What it does

SonarQube (Server, Cloud, and Community Build) performs deterministic-first analysis across 40+ languages. It reasons over syntax, control and data flow, taint analysis, software composition analysis (SCA), secrets, infrastructure as code, and architecture. It enforces **quality gates** that give a go/no-go verdict for every analysis, whether a human or an agent wrote the code. Sonar claims a 3.2% false-positive rate, more than 7M developers, and use at 75% of the Fortune 100. It also claims SonarQube users have 44% lower AI outage risk and up to 8% lower token usage.

AC/DC maps Sonar's products onto three loops:

| Loop | Where it runs | Sonar products |
|---|---|---|
| **Agentic Loop** | Inside each agent reasoning step | Sonar Vortex, SonarQube MCP Server, SonarQube CLI, SonarQube for IDE |
| **CI Verification Loop** | At sandbox exit / PR | SonarQube quality gate, Advanced Security, Gitar |
| **Code Maintenance Loop** | Background | SonarQube Remediation Agent, AI CodeFix |

## Key features

- **Sonar Vortex** is a context engine for coding agents. Before the agent writes, it injects repository and architecture context, coding guidelines drawn from the project's own issue history, security policies, approved libraries, and license policies. After each edit, it verifies the change at CI-level precision "in seconds" by reusing the latest stored CI analysis for the branch. Sonar pitches it as a fix for the "eternal new-joiner" problem, where agents burn tokens on grep and find every session, and as a better option than static prompt files that go stale. Vortex needs a prior CI analysis of the project and is sold through sales.
- **SonarQube MCP Server.** It runs in three ways: as a managed native endpoint in SonarQube Cloud (no Docker, with a fixed subset of tools), as an extension on SonarQube Server 2026.3+ that exposes `/mcp`, or as a self-hosted Docker stdio server. Tools include issue search, quality-gate status, `analyze_code_snippet`, dependency-risk search, and changing an issue's status or marking false positives. Only the local stdio server can run Vortex, because the hosted server has no filesystem access.
- **SonarQube CLI** (`sonar`) handles secrets scanning, pre-commit git hooks, and issue queries with JSON or **TOON** output meant to be piped into LLMs. It also runs analysis through the SonarQube A3S API, can run an MCP server, stores tokens in the OS keychain, and offers `sonar integrate <agent>` for agent setup.
- **SonarQube Remediation Agent** fixes backlog issues assigned by rule, severity, or project. It can also run on a schedule or be triggered by a failed PR gate. It works in a closed loop: generate a fix, apply it in a sandbox, re-scan with the Sonar engine, then either discard it or open a PR. You bring your own LLM (GPT-5.5 or Claude Opus 4.6). It runs on the "Sonar Foundation Agent", which Sonar says is #1 on SWE-bench Verified. It supports Java, JS, TS, and Python, with C# also listed, on GitHub, Azure DevOps, and SonarQube Cloud Enterprise.
- **SonarQube Hunter Agent** uses playbook-driven LLM security research (hunt, confirm, explain, integrate) to find intent-level flaws that SAST misses: broken access control and IDOR, business-logic abuse, and authentication or session gaps. Sonar claims 90% precision, repeatable results, and 200+ zero-days found in open source.
- **Gitar** is an AI PR reviewer and "change verification agent". It posts one consolidated high-signal comment, root-causes CI failures (separating real breakage from flaky tests), commits fixes, and iterates until CI is green. Merge policies are written in plain English under `.gitar/rules/`. Pricing is $20 per user per month for Core, $40 for Pro, and per-PR enterprise pricing.
- **Other products:** SonarQube Advanced Security (SCA, taint analysis, secrets, IaC, and `check_dependency` with malicious-package detection), SonarQube Architecture (current versus intended module structure, exposed over MCP), and SonarSweep (private beta: context files embedded in the repo, plus remediation of AI training datasets).

## Architecture and concepts

The AC/DC page argues that verification has become the bottleneck now that agents write code faster than teams can review it. It also argues that neither deterministic analysis nor LLM review is enough alone. SonarQube's "mathematical" analysis covers known patterns with auditable rule, location, and data-flow explanations. Gitar and Hunter add LLM reasoning for logic and intent bugs. The "independent and zero trust" principle means the agent that reviews code should not be the one that wrote it.

Inside the agent loop, AC/DC defines an explicit **in-loop gate**: a task is not complete until `run_advanced_code_analysis` comes back clean for every changed file. `get_project_quality_gate_status` only reflects the last CI run and cannot see uncommitted work, so it is a branch-readiness check, not an edit exit criterion. The Remediation Agent is the "Solve" stage outside the coding loop. It has no MCP tool. It works the main-branch backlog and open PRs from SonarQube Cloud and opens its own PRs.

## Main APIs

**MCP tools for agents without a plugin.** These require the local stdio server, the workspace mounted at `/app/mcp-workspace`, and `SONARQUBE_TOOLSETS=vortex,issues,quality-gates,rules`. Sonar publishes a drop-in `AGENTS.md` that tells agents when to call each one:

- **Guide:** `get_guidelines` (`mode`: `project_based` / `category_based` / `combined`). Semantic navigation through ASTs and control flow, used instead of grep: `search_by_signature_patterns`, `search_by_body_patterns`, `get_source_code`. Architecture tools: `get_current_architecture` (`depth`, `path_prefix`), `get_intended_architecture`, `get_upstream_call_flow` / `get_downstream_call_flow`, `get_references`, `get_type_hierarchy`. Dependency check: `check_dependency` (`purl`; refuse `malicious`, block BLOCKER/HIGH). Navigation covers Java, C#, JS, TS, Python, and Rust.
- **Verify:** `run_advanced_code_analysis` (`projectKey`, `branch`, `filePath`, `fileScope` of `MAIN` or `TEST`) after every file edit.
- **Solve:** `show_rule` (for example `python:S7608`), then fix only findings on touched lines, then re-run until clean, then show findings to the user verbatim. Wider context comes from `search_sonar_issues_in_projects`, `search_dependency_risks`, and `get_project_quality_gate_status`.

**Agent plugin install.** Each path ends with the plugin's integrate skill, which installs the CLI, authenticates, starts the MCP server, and configures Vortex and secrets detection:

```bash
/plugin install sonarqube@claude-plugins-official      # Claude Code
codex plugin marketplace add SonarSource/sonarqube-agent-plugins && codex plugin add sonarqube@sonar
/plugin install sonarqube@awesome-copilot             # GitHub Copilot CLI
agy plugin install https://github.com/SonarSource/sonarqube-agent-plugins   # Antigravity
/add-plugin sonarqube                                 # Cursor
/sonarqube:sonar-integrate                            # then, in the agent (Codex: sonar integrate codex)

brew install sonarqube-cli    # or: mise use -g sonarqube-cli@latest
```

## When to use

Use Sonar when you already run SonarQube, or want auditable, deterministic quality and security gates, and need coding agents held to the same standards as humans. Vortex and the MCP server put those gates inside the agent's loop, so issues get fixed before a PR exists and CI stays green. They also save tokens that agents would otherwise spend exploring the codebase. The Remediation Agent fits large legacy backlogs where you want verified PRs instead of tickets. Hunter fits teams whose pentests are infrequent and who need access-control and business-logic coverage. Gitar is the LLM PR-review layer if you want review, CI triage, and fix-until-green from one vendor. Note that Vortex requires prior CI analysis and a sales contact. The Cloud-hosted MCP endpoint is the easiest to set up but exposes only a subset of tools and cannot run Vortex.

## Ecosystem

The integrations named are Claude Code, Cursor, Codex, GitHub Copilot, Antigravity, Devin, Gemini CLI, Windsurf, Zed, Kiro (through a "SonarQube Power"), Amazon Q, and the JetBrains and Visual Studio IDEs. Gitar connects to GitHub, GitLab, Bitbucket, Azure DevOps, the major CI systems, Jira, Linear, and Slack. Public repos referenced are `SonarSource/sonarqube-agent-plugins` (the plugin marketplace) and `SonarSource/sonarqube-cli`. In this wiki, Gitar competes directly with the LLM PR reviewers [[coderabbit.ai]] and [[greptile.com]]; Sonar's own FAQ compares Gitar with CodeRabbit and Qodo. The Vortex in-loop gate is closest in spirit to [[openqodex-openqodex]], which runs deterministic scanners plus a separate reviewer agent before push.

## Documentation

`docs.sonarsource.com` is published on GitBook. It has an `llms.txt` index, a `.md` version of every page, and an `?ask=&goal=` query endpoint for agents. Sections cover SonarQube Cloud, Server LTA versions (2026.5, 2026.1, 2025.4), Community Build, AC/DC (with per-agent Vortex install guides for Claude Code, Codex, Cursor, Copilot CLI, Antigravity, Kiro, and generic MCP), the Hunter and Remediation agents, the SonarQube CLI, the MCP Server, and IDE plugins for VS Code, IntelliJ, Visual Studio, and Eclipse. The marketing site publishes its own `llms.txt` (products, solutions, industries, and learn pages) plus `llms-full.txt`.
