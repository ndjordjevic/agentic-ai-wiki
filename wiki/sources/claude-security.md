---
type: source
category: "Security"
source_url: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-security
tags:
  - claude-code-plugin
  - vulnerability-scanning
  - sarif-reporting
  - patch-suggestions
  - multi-agent-verification
  - appsec
  - trusted-code-model
  - anthropic
related:
  - mukul975-anthropic-cybersecurity-skills
  - openqodex-openqodex
  - usestrix-strix
  - nvidia-skillspector
  - SnailSploit-Claude-Red
product: claude-security
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

claude-security is Anthropic’s official Claude Code plugin (v0.12.0) that runs a multi-agent vulnerability scan and optional patch-suggestion workflow entirely inside the user’s Claude Code session—the in-session counterpart to the hosted Claude Security product—with every finding challenged by independent verifiers before it reaches the report.

_All claims below are sourced from ../../raw/web/claude-security.md unless otherwise noted._

## What it does

Install from `claude-plugins-official`, then `/claude-security` (or plain-language / argument shortcuts) offers three jobs: **Scan codebase** (whole repo or scoped part), **Scan changes** (branch, PR diff with branch checked out, or one commit), and **Suggest patches** (turn a report’s findings into reviewable patch files). Scans and fixes run under the user’s session permissions with no plugin-owned isolation; recommended models are Claude Opus 5.5 or Fable 5.1. For untrusted third-party trees, Anthropic suggests running the whole session inside [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime).

## Key features

- **Effort and scope negotiation** — reads repo size, code directories, branch, and diff before asking; states cost; every question includes an “I don’t know” default; confirms plan before work starts.
- **Verified findings only** — candidates go to independent verifier agents whose job is to disprove them from the code; survivors get CVSS-v4-aligned severity (CRITICAL/HIGH/MEDIUM/LOW), confidence capped by verification, and an outcome-focused recommendation.
- **Timestamped report directory** — `CLAUDE-SECURITY-<timestamp>/` with Markdown report, JSONL (stable `claudeSecurityPluginFindingId`), SARIF 2.1.0, and revision stamp (`CLAUDE-SECURITY-REVISION-<sha12>.json`, `-dirty` if uncommitted changes); credential values redacted to `[REDACTED]` after write; directory carries `.gitignore` so reports are not accidentally committed.
- **Suggest patches** — develops each fix in a scratch copy (never touches the working tree/index), panel-reviews for single-finding fix / no new vuln / no behavior change, writes `patches/F<n>.patch` plus notes; never auto-applies, commits, or pushes.
- **Coverage accounting** — whole-repo scans must account for every top-level directory (scanned or explicitly set aside with reason); Coverage section names what was left out.

## Architecture and concepts

Plugin layout: `.claude-plugin/plugin.json`, `skills/claude-security/` (front-desk `SKILL.md`, job recipes `scan-codebase` / `scan-changes` / `suggest-patches`, `role.md`, report/patch specs), specialist agents (`scan-inventory`, `scan-researcher`, `scan-verifier`, `scan-loader`, `scan-redactor`, `patch-generator`, `patch-verifier`, `explore`, plus `claude-security`), `hooks/`, Python helpers under `scripts/` (report render, save result, scan meta, patch artifacts, CWE/SARIF/finding libs), and `workflows/scan.js`. Trust model: scanned code is trusted; repo contents (code, comments, `CLAUDE.md`) are treated as data under review, not instructions. Verification thoroughness is computed in code, not asserted by the finding model. Scans are nondeterministic and complement (do not replace) SAST, dependency scanning, and human review.

## Main APIs

User-facing entry is `/claude-security` (menu or direct job args such as `/claude-security scan my branch at high`). Skill-allowed tools include Read/Write/Edit/Glob/Grep, AskUserQuestion, Workflow(`claude-security:scan`), named Agent subtypes, constrained Bash (`git`, date/ls/wc/mkdir, plugin Python scripts, `keep-waiting.sh`). Install: `/plugin install claude-security@claude-plugins-official` then `/reload-plugins` (add marketplace `anthropics/claude-plugins-official` first if missing). Requirements: Claude Code + plugin, Python 3.9+ on `PATH`; git checkout needed for change scans and patch suggestions (whole-repo scan can run without). Telemetry opt-out via Claude Code `DISABLE_TELEMETRY=1` / `DO_NOT_TRACK=1` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`; tip suppress with `CLAUDE_SECURITY_SCAN_TIP=off`.

## When to use

Use on repositories you control when you want session-local deep vulnerability hunting with adversarial verification and optional patch drafts you apply yourself—especially branch/PR change reviews at `high` effort—rather than a separate daemon or hosted-only Claude Security run. Prefer sandbox-runtime when the tree is untrusted.

## Ecosystem

Shipped in Anthropic’s official `anthropics/claude-plugins-official` marketplace alongside other Claude Code plugins. In-session product of [Claude Security](https://claude.com/product/claude-security). Plugin vulnerabilities go through Anthropic’s responsible disclosure program (not public GitHub issues); security fixes land only on the latest released version. License: SEE LICENSE IN LICENSE.
