---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/openqodex/openqodex
tags:
  - pre-push-code-review
  - static-analysis-scanners
  - independent-reviewer
  - push-gate-hooks
  - sarif
  - code-graph-mcp
  - claude-code-plugin
  - codex-plugin
related:
  - coderabbit.ai
  - agent-field-pr-af
  - greptile.com
  - openai-codex-plugin-cc
product: openqodex
detail_level: standard
created: 2026-10-15
updated: 2026-10-15
---

OpenQodex is an open-source (Apache-2.0) local code reviewer by Qodex that runs inside your coding agent or terminal *before* you push. It reviews "the change" — unpushed commits plus everything uncommitted — first with deterministic scanners (gitleaks, semgrep, osv-scanner, linters, IaC and SQL checkers — 22 built in), then with a **separate** Claude Code or Codex process running on your own login (no API key, no account). By default the agent that wrote the code does not review it. Scripts verify the reviewer answered every scanner finding and was shown every changed line, and push-gate hooks check for a passing review before `git push`. It matters for this wiki as a concrete pattern for independent, verifiable AI review inside the agent loop rather than as a hosted PR bot.

_All claims below are sourced from ../../raw/github/openqodex-openqodex.md unless otherwise noted._

## What it does

`openqodex review` works out the change, copies it to a temporary folder, runs the scanners that match the changed files, keeps only findings on changed lines (dropping test fixtures and disabled rules), builds a code graph, and starts its own reviewer. The reviewer must **raise or drop each scanner finding ("candidate") with a reason** and may add its own. OpenQodex then writes `report.html`, `report.md`, `report.json` and `report.sarif` under `.openqodex/reviews/<time>-<id>/` and prints a **receipt**: verdict (`passed` / `blocked`), one line per finding, and the report paths. The bundled skill tells the agent to show the receipt, ask "Fix all, or tell me which?", and fix only the findings you name.

A review is "complete" only when every stage ran; otherwise it prints "Review incomplete" and exits 2. Without Claude Code or Codex available, it prints "Full review unavailable", saves unchecked scanner findings, and offers `review --agent` as a fallback in which the coding agent reviews its own change.

| Coding agent | Starts a review | Can be the reviewer | Push gate |
|---|---|---|---|
| Claude Code | yes | yes | yes |
| Codex CLI | yes | yes | yes, after trusting the hook |
| Cursor | yes | no | no (a rule asks Cursor to review) |
| Cline | yes | no | no (a rule asks Cline to review) |

## Installation

Requires Node 22+, git, macOS or Linux, and Claude Code or Codex logged in for full reviews.

```bash
npx openqodex init                                        # interactive, for humans
npx -y openqodex@0.12.0 init --yes --agent <host>         # for agents: claude-code | codex | cursor | cline
npx skills add openqodex/openqodex -g                     # skill only — no push gate, no scanner download
```

`init` detects installed agents, lists the files it will write and asks once. Inside a repo it adds a git pre-push hook, a one-line "review before push" instruction to each agent's global file (e.g. `~/.claude/CLAUDE.md`), a review section in the repo's `CLAUDE.md`/`AGENTS.md`, and `.openqodex/config.yaml` + `.openqodex/custom-instructions.md` (to commit). It starts background scanner downloads into `~/.openqodex/tools/`, checks that a reviewer can start, and runs a first review. It writes a launcher at `~/.openqodex/bin/openqodex` — an npx install puts nothing on `PATH`. Codex users must trust the hook via `/hooks`, and should run `init` outside Codex's default no-network sandbox.

## Key features

- **Two-stage review** — scanners first (no model), then an independent LLM reviewer that must account for every scanner candidate; scripts check coverage of findings and changed lines.
- **22 pinned built-in scanners** — secrets (1), code security (3), dependency vulnerabilities (2), lint (5), GitHub Actions (2), Dockerfile/Terraform/Kubernetes/CloudFormation (6), SQL and migrations (3). A scanner runs only when the change touches a file it reads.
- **Custom scanners from GitHub** — declare any SARIF- or JSON-emitting tool in `.openqodex/config.yaml`; `openqodex trust` quarantines and shows it for explicit approval stored in `~/.openqodex/trust.json`. The skill forbids the agent from running `trust` without asking.
- **Push gates** — an in-agent hook checks for a passing review of current work; the git pre-push hook checks the exact commits being pushed. Both warn by default and block only when `review.block_on_severity` is set (`critical` > `major` > `minor` > `nitpick` > `info`).
- **Review scopes** — current change, `review --all` (whole repo, with the brief pointing at most-called functions and scanner hot spots), `review <branch>`, `review '#42'` (PR, checked out in a temp folder).
- **Code graph + MCP** — `openqodex graph` answers questions such as "who calls this function", exposed to agents through a local MCP server.
- **Privacy** — no telemetry; built-in scanners send no code. `--offline` skips the network-using scanners (semgrep, osv-scanner, kubeconform, cargo-deny); the reviewer still sends the change to its model provider.
- **CI surfaces** — a GitHub Action (full review with an Anthropic API key, scanners only without), and a pre-commit hook (scanners only).

## Architecture

A pnpm monorepo bundled into a single dependency-free `openqodex` CLI (`dist/bin.js`). `packages/core` holds the change source, config parser, review "lenses", review brief and renderers. `packages/scanners` holds the scanner adapters, the changed-line filter and the pinned `toolchain.json`. `packages/graph` is the code graph and `packages/mcp` its MCP server. `packages/review` is the review engine behind the Node library (`reviewChange`, which reviews with a model of your choice, as a server would). Agent integrations live in `skills/openqodex/`, `plugins/claude-code/` (hooks, skills, `.mcp.json`) and `plugins/codex/`, plus a Cursor plugin manifest. Docs ship inside the package and print offline via `openqodex guide <topic>`. Exit codes: 0 clean/warnings, 1 finding at or above the block threshold, 2 the tool itself failed.

The repo's own engineering rules are distinctive: no test may fake an in-repo module or local binary (only the model provider), features are proved end-to-end by running the real CLI on a real repo, and `pnpm gate` (typecheck, lint, unit, e2e, docs-facts checks, a scrub that rejects em dashes and private material) must pass before any push.

## Example usage

```text
review my change with openqodex
review my whole repo with openqodex
review pull request #42 with openqodex
```

```bash
~/.openqodex/bin/openqodex review          # from your own terminal
npx openqodex scan --only custom:bearer    # scanners only, unchecked
npx openqodex demo                         # repo with 15 planted bugs, then scan it
npx openqodex doctor --install             # pre-download scanners this repo needs
```

Custom scanner entry:

```yaml
scanners:
  custom:
    - source: https://github.com/Bearer/bearer
      run: bearer scan {target} --format sarif --output {report} --quiet --disable-version-check
      target: repo
```

## Maintenance status

706 stars, 56 forks, TypeScript, Apache-2.0. Latest release `openqodex@0.12.0` (2026-10-10), last pushed 2026-10-15. Pre-1.0: commands, flags and config may change between minor releases. Published benchmark (planted bugs, dev split, 3 repeats): Claude Code reviewer (claude-opus-5-5) found 84.3% of issues (129/153) at 97.3–100% precision, about $0.087 and 26 s per review. The Codex reviewer (gpt-6.1-sol) found 75.2%, and scanners alone 62.7%. On the external AACR-Bench (real PRs), issue recall is not yet human-ruled, and location recall is about 11%. The repo publishes A/A noise runs and requires that any quality claim cite a saved run.

## Ecosystem

Made by Qodex, which also sells a hosted PR review service. OpenQodex differs from hosted PR reviewers such as [[coderabbit.ai]] and [[greptile.com]] by running locally, before the push, on the developer's existing Claude Code/Codex subscription. Compared with [[agent-field-pr-af]], which runs a long multi-agent PR audit in CI, OpenQodex is an inner-loop check. Its use of a second, separate model process as reviewer mirrors the cross-agent review idea in [[openai-codex-plugin-cc]]. It ships through npm, `npx skills add`, and Claude Code/Codex/Cursor plugin manifests.
