# openqodex/openqodex

## Metadata
- Stars: 706
- Forks: 56
- Primary language: TypeScript
- Default branch: main
- Latest release: openqodex@0.12.0 (2026-10-10)
- License: Apache-2.0
- Homepage: https://qodex.ai/openqodex
- Last pushed: 2026-10-15
- Fetched: 2026-10-15
- Final URL: https://github.com/openqodex/openqodex

## Description
Open source code review that runs in your coding agent before you push. Scanners plus a separate AI reviewer, on your own login, no key.

## README
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openqodex/openqodex/main/.github/assets/readme-banner-dark.png">
  <img alt="OpenQodex" src="https://raw.githubusercontent.com/openqodex/openqodex/main/.github/assets/readme-banner-light.png" width="1280">
</picture>

# OpenQodex

[![npm version](https://img.shields.io/npm/v/openqodex)](https://www.npmjs.com/package/openqodex)
[![licence](https://img.shields.io/badge/licence-Apache--2.0-blue)](https://github.com/openqodex/openqodex/blob/main/LICENSE)
[![CI](https://github.com/openqodex/openqodex/actions/workflows/ci.yml/badge.svg)](https://github.com/openqodex/openqodex/actions/workflows/ci.yml)
[![Discussions](https://img.shields.io/github/discussions/openqodex/openqodex)](https://github.com/openqodex/openqodex/discussions)

AI agents: read the [agent guide](https://github.com/openqodex/openqodex/blob/main/docs/for-agents.md). After the install, `~/.openqodex/bin/openqodex guide for-agents` prints the guide for the installed version.

OpenQodex reviews your code change before you push it. Your change is the commits you have not pushed plus everything uncommitted. OpenQodex runs on your machine, from your coding agent or your terminal.

First, OpenQodex runs the scanners that fit the files you changed. A scanner is a program that checks code without a model, such as gitleaks or semgrep. A finding is one problem at one place in the code, with a severity. OpenQodex keeps the scanner findings on the lines you changed. It drops findings in test fixtures and in rules you switched off.

Then OpenQodex starts a reviewer: a separate Claude Code or Codex process on your own login. By default, the agent that wrote the code does not review it. The reviewer must raise or drop each scanner finding, with a reason. Scripts check that it answered every scanner finding. They also check that it was given every changed line. Then you choose which findings your agent fixes.

## Where it runs

| Coding agent | Starts a review | Can be the reviewer | Push gate |
|---|---|---|---|
| Claude Code | yes | yes | yes |
| Codex CLI | yes | yes | yes, after you trust the hook in Codex |
| Cursor | yes | no | no, a rule asks Cursor to review |
| Cline | yes | no | no, a rule asks Cline to review |

In Cursor and Cline, the review needs Claude Code or Codex installed as the reviewer. A push gate is a hook that looks for a review before your agent runs `git push`.

## Requirements

- Node 22 or newer, and git.
- macOS or Linux. CI runs the gate on Node 22, on macOS and on Ubuntu Linux. No test runs on Windows or WSL.
- For a full review: Claude Code or Codex, installed and logged in. OpenQodex needs no account or API key of its own.
- Some scanners need a language runtime that OpenQodex does not install. brakeman and rubocop need Ruby. golangci-lint needs Go. cargo-deny needs Cargo.

## Install

For people, in your terminal:

```
npx openqodex init
```

In a terminal, `init` finds Claude Code, Cursor, Codex CLI and Cline on your machine. It lists the files it will write. It asks you once. It starts the scanner downloads that your repository needs. Then it reviews your current change when a reviewer can start.

After the install, say to your agent: "review my change with openqodex". In your own terminal, run `~/.openqodex/bin/openqodex review`. That path is the launcher, a small script that `init` writes. An `npx` install puts no `openqodex` on your `PATH`.

For agents, the same install with no question:

```
npx -y openqodex@0.12.0 init --yes --agent <host>
```

`<host>` is `claude-code`, `codex`, `cursor` or `cline`. In its default sandbox mode, Codex gives commands no network. From Codex, run this line in your own terminal. The [quickstart](https://github.com/openqodex/openqodex/blob/main/docs/quickstart.md) has a prompt to paste into your agent.

To install only the skill, run `npx skills add openqodex/openqodex -g`. That installs no push gate and downloads no scanner. A later `init` replaces that skill with the skill that `init` installs.

OpenQodex itself collects no usage data. The built-in scanners, as OpenQodex runs them, send no code. The reviewer sends your change to the model service of your Claude Code or Codex login. The [privacy page](https://github.com/openqodex/openqodex/blob/main/docs/privacy.md) lists each network use of this version.

<!-- recording: added before launch -->

## What it does today

- `openqodex review` reviews your change in one command.
- It writes `report.html`, `report.md`, `report.json` and `report.sarif`. SARIF is a standard JSON format for scanner results.
- At the end, it prints a receipt. The receipt holds the verdict, one line per finding and the path of `report.html`. Here is an [example report](https://github.com/openqodex/openqodex/blob/main/tests/golden/expected/claude/run/report.md).
- The skill tells your agent to show you the receipt. It tells the agent to ask "Fix all, or tell me which?". It tells the agent to fix only the findings you name.
- `review --all` reviews every file of the repository, less the paths that `review.paths.exclude` leaves out.
- `review <branch>` reviews a branch. `review '#42'` reviews a pull request.
- A review is complete only when every stage ran. Otherwise, `review` prints "Review incomplete" with what is missing. Then it exits 2.
- The push gate inside your agent looks for a review of your current work. It does not know what a push sends. For a plain `git push`, it asks whether your current work has a passing review. For any other push command, it says it cannot tell. The git pre-push hook that `init` adds checks the exact commits a push sends, for each `git push` that runs git hooks. `git push --no-verify` skips that hook.
- Both warn by default. They block only when `.openqodex/config.yaml` sets `review.block_on_severity`. Severities run from `critical` through `major`, `minor` and `nitpick` to `info`. A finding at or above the set severity blocks the push.
- The GitHub Action runs the full review on a pull request when the workflow gives it an Anthropic API key. Without a key, it runs the scanners only. The pre-commit hook also runs the scanners only.
- `openqodex graph` answers questions about the code, such as who calls a function. An MCP server is a local tool server that your agent starts. `init` gives your agent the graph questions through an MCP server. For the Cline VS Code extension, `init` prints the entry for you to add.
- `--offline` skips semgrep, osv-scanner, kubeconform and cargo-deny, the built-in scanners that use the network. It also stops scanner downloads. The reviewer still sends your change to its model service. An approved custom scanner still runs its own command.
- `npx openqodex demo` builds a small repository with planted bugs. Then it scans that repository.

## What it does not do yet

- No reviewer other than Claude Code or Codex. Cursor cannot be the reviewer. `cursor-agent` 2025.09.18 offered no way to limit it to reading.
- Without a reviewer, `review` prints "Full review unavailable" and exits 2. It saves the scanner findings, unchecked, to `unchecked-candidates.json`. It also names a fallback command, `review --agent`. In that fallback, your coding agent reviews its own change.
- Inside the Codex sandbox, a second Codex process does not start. So Codex cannot be the reviewer there. OpenQodex tested this with codex-cli 0.160.0 on macOS.
- No review on your own API key, except in the GitHub Action.
- No Homebrew formula, no install script and no Docker image in this version. Install through npm.
- No offline copy of the vulnerability databases. osv-scanner asks osv.dev. cargo-deny downloads the RustSec advisory database.
- No review finds every problem. The report names each stage that did not run.

<!-- benchmark-results:start -->
## Benchmark

| Reviewer | Model | Cases | Issue recall | Precision | Clean rate | Cost per review |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Code (claude-graph-on) | claude-opus-5-5 | Planted bugs, dev split | 129/153 (84.3%) | 142/146 (97.3%) to 146/146 (100.0%) | 6/6 (100.0%) | $0.0870 |
| Codex (codex-graph-on) | gpt-6.1-sol | Planted bugs, dev split | 115/153 (75.2%) | 125/146 (85.6%) to 146/146 (100.0%) | 6/6 (100.0%) | not measured |
| Scanner only (scan) | no model | Planted bugs, dev split | 32/51 (62.7%) | 35/45 (77.8%) to 40/45 (88.9%) | 1/2 (50.0%) | not measured |

[Full results and how to read them](https://github.com/openqodex/openqodex/blob/main/docs/benchmark-results.md)
<!-- benchmark-results:end -->

## Built-in scanners

OpenQodex has 22 built-in scanners. A scanner runs only when your change holds a file it reads. Some scanners also read the project or folder around a changed file. Each scanner that needs a download gets it on first use. OpenQodex pins each download to one version.

| What it checks | Built-in scanners |
|---|---|
| Secrets in code | 1 |
| Security problems in code | 3 |
| Dependencies with known vulnerabilities | 2 |
| Lint | 5 |
| GitHub Actions workflows | 2 |
| Dockerfiles, Terraform, Kubernetes and CloudFormation | 6 |
| SQL and database migrations | 3 |

The [scanner list](https://github.com/openqodex/openqodex/blob/main/docs/scanners.md) gives each scanner, its version, the files it reads and what it does not check.

## Add a scanner from GitHub

You or your agent can configure a compatible scanner from GitHub. Then you approve it before it runs.

1. Add the scanner to `.openqodex/config.yaml` in your repository:

   ```yaml
   scanners:
     custom:
       - source: https://github.com/Bearer/bearer
         run: bearer scan {target} --format sarif --output {report} --quiet --disable-version-check
         target: repo
   ```

2. Run `npx openqodex trust`. It downloads the release asset into a quarantine folder. Then it shows what will run and asks yes or no.
3. Run `npx openqodex scan --only custom:bearer` to see it work. The next review includes it.

To use your agent, say: "add https://github.com/Bearer/bearer to OpenQodex as a custom scanner". The agent writes the entry. The skill tells it never to run `openqodex trust` without asking you first.

A compatible scanner meets these limits:

- It writes SARIF, or one JSON document that a `map` block in the configuration turns into findings.
- It installs from a release asset for your system, an exact npm or PyPI version, or your `PATH`.
- OpenQodex runs it only when `~/.openqodex/trust.json` on that machine holds your approval of that exact entry. A fresh GitHub-hosted runner holds none, so the GitHub Action skips it there.

Bearer CLI is under the Elastic License 2.0, which is not an open source licence. The [custom scanner guide](https://github.com/openqodex/openqodex/blob/main/docs/custom-scanners.md) explains every key.

## Packages

| Package | What it is |
|---|---|
| [`openqodex`](https://www.npmjs.com/package/openqodex) | The CLI as one bundled file, with the skill, the agent templates, the docs and the demo beside it. |

The CLI has no runtime dependencies. You can also import `openqodex` as a [Node library](https://github.com/openqodex/openqodex/blob/main/docs/library.md). The build bundles the workspace packages under `packages/` into it. This repository does not publish them to npm.

## Documentation

The docs ship inside the package. `npx openqodex guide <topic>` prints one page in your terminal.

- [Quickstart](https://github.com/openqodex/openqodex/blob/main/docs/quickstart.md)
- [Agent guide](https://github.com/openqodex/openqodex/blob/main/docs/for-agents.md)
- [Commands](https://github.com/openqodex/openqodex/blob/main/docs/cli.md)
- [Configuration](https://github.com/openqodex/openqodex/blob/main/docs/config.md)
- [What init writes for each agent](https://github.com/openqodex/openqodex/blob/main/docs/agents.md)
- [GitHub Action](https://github.com/openqodex/openqodex/blob/main/docs/github-action.md)
- [Security](https://github.com/openqodex/openqodex/blob/main/docs/security.md)
- [All pages](https://github.com/openqodex/openqodex/blob/main/docs/index.md)

## Made by Qodex

[![Made by Qodex](https://raw.githubusercontent.com/openqodex/openqodex/main/.github/assets/made-by-qodex.svg)](https://qodex.ai?utm_source=openqodex&utm_medium=readme)

[Qodex](https://qodex.ai?utm_source=openqodex&utm_medium=readme) makes OpenQodex. Qodex also runs a hosted review service for pull requests.

## Telemetry

OpenQodex sends no telemetry. OpenQodex starts semgrep with its metrics switched off. The [telemetry page](https://github.com/openqodex/openqodex/blob/main/docs/telemetry.md) says more.

## Security

Report a vulnerability through GitHub's private vulnerability reporting, as the [security policy](https://github.com/openqodex/openqodex/blob/main/SECURITY.md) says. Never open a public issue for one.

## Status

OpenQodex is on the way to 1.0. Commands, flags and the configuration file can change between minor releases. The [changelog](https://github.com/openqodex/openqodex/blob/main/packages/cli/CHANGELOG.md) lists the changes in each release.

Licensed under [Apache 2.0](https://github.com/openqodex/openqodex/blob/main/LICENSE). The [NOTICE](https://github.com/openqodex/openqodex/blob/main/NOTICE) file gives the scanners' licences.

## Docs

### AGENTS.md (repo root)

# Working in this repo

To install or use OpenQodex in another repository, read `docs/for-agents.md`. This file is for work on OpenQodex itself.

OpenQodex is open source AI code review for Claude Code and Codex. It runs before you push, from your coding agent or your terminal. This file tells a coding agent how the repo is built and tested.

## Setup

- Node 22 or newer. The published package must work on Node 22, so test on 22 even if your machine has a newer default.
- pnpm 9 (the version is pinned in `package.json` under `packageManager`).
- `pnpm install`, then `pnpm build`.

## Commands

- `pnpm build`: builds `@openqodex/core`, `@openqodex/scanners`, `@openqodex/graph`, `@openqodex/review` and `@openqodex/mcp`, then the `openqodex` CLI, then copies the shipped assets beside the bundle.
- `pnpm typecheck`, `pnpm lint`, `pnpm test` (unit), `pnpm test:e2e` (runs the built CLI as a real subprocess).
- `pnpm gate`: every check in order, stopping at the first failure. It must be green before any push. CI (`.github/workflows/ci.yml`) runs the same steps: on Linux for a pull request, and on Linux and macOS in the merge queue and on main.
- `pnpm changeset`: add a changeset to any pull request with a change a user can see.
- `pnpm docs:index`: regenerates `docs/llms.txt`. The gate checks it with `--check`, and checks the README's facts with `scripts/docs-facts.mjs`.

## Where things live

- `packages/cli`: the `openqodex` binary. It is published as one bundled file, `dist/bin.js`, with no runtime dependencies; every library it uses is a dev dependency that the bundler inlines.
- `packages/core`: the change source, the config parser, the lenses, the review brief, the renderers.
- `packages/scanners`: the scanner adapters, the changed-line filter and the pinned scanner table (`toolchain.json`).
- `packages/graph`: the code graph. `packages/review`: the review engine the library uses. `packages/mcp`: the code graph's MCP server.
- `skills/openqodex/`: the agent skill. `plugins/claude-code/` and `plugins/codex/`: the Claude Code and Codex plugins. `docs/`: the docs, shipped in the package. `examples/demo-repo/`: the sample repo with planted bugs.
- Assets that ship beside the bundle (lenses, docs, skill, templates, toolchain table, demo) are found at run time relative to the installed package through `assetPath()` in `packages/cli/src/assets.ts`, never from the current directory. `scripts/copy-assets.mjs` copies them into `packages/cli` after the build; the copies are gitignored.

## Pull requests and the merge queue

- A pull request runs one check: the gate on Linux. The macOS gate and the scanner-only benchmark show as skipped.
- When the pull request is ready, a maintainer adds it to the merge queue. The queue merges it with main and with every pull request ahead of it in the queue. Then it runs the full gate on that result: the gate on Linux, the gate on macOS and the scanner-only benchmark.
- When the full gate passes, the queue merges the pull request into main. When it fails, the queue removes the pull request and main does not change. Fix the branch and add it to the queue again.
- To run the full gate before the queue, for example on a scanner or installer change, add the label `full-ci` to the pull request.
- Each push to main runs the full gate again, and the release workflow.

## Exit codes

0 clean or warnings only, 1 a finding at or above the block threshold, 2 the tool itself failed.

## Tests

- No test fakes a module that lives in this repo or a binary on this machine. The only fake allowed is a model provider.
- End-to-end first: a feature is proved by running the real CLI on a real repo and reading the saved report.
- A piece that must be tested alone gets its list of failure cases written before its code. Do not add unit tests after the code to raise coverage.

## Writing

Plain English, sentence case, no emoji, no exclamation marks, no em dash character anywhere (prose, code comments, commit messages, changelog). Define a term the first time it appears. `scripts/scrub.mjs` fails the gate on private material and on the em dash.

### docs/index.md

# OpenQodex docs

OpenQodex is open source AI code review for Claude Code and Codex. It runs before you push, from your coding agent or your terminal.

These pages ship inside the npm package. `npx openqodex guide <topic>` prints one in your terminal, offline. The topic is the file name without `.md`.

## Words used in these pages

- Change: the commits not yet pushed plus everything uncommitted, untracked files included.
- Changed lines: the lines the change adds or edits. Context lines around them do not count.
- Scanner: a program that checks code without a model, such as gitleaks or semgrep.
- Finding: one problem at one place in the code, with a severity.
- Candidate: a scanner finding on a changed line, waiting for the agent to verify it.
- Brief: the text `openqodex review` gives its reviewer to review from.
- Report: the result of a scan or a review, written as `report.md`, `report.json` and `report.sarif`, and for a review also as `report.html`, a page that shows each finding under its line of code.
- Receipt: what `review` prints when it ends: the verdict, one line per finding and the absolute paths of `report.html` and `report.md`.
- Verdict: `passed` or `blocked`.

## Pages

- `for-agents`: for an AI agent: install, configure, add a custom scanner, and what each message means.
- `quickstart`: install OpenQodex and run the first review.
- `claude-code-review`: code review in Claude Code, from install to report.
- `cli`: every command, flag and exit code.
- `config`: every key of `.openqodex/config.yaml`.
- `scanners`: the twenty-two built-in scanners.
- `graph`: the code graph: what it answers, what it cannot see, its folder, its commands and its MCP server for agents.
- `custom-scanners`: add any scanner by its GitHub link.
- `agents`: what `init` writes for each coding agent.
- `github-action`: run the scan on pull requests.
- `library`: review a change with your own model (`reviewChange`), preinstall the scanners for a server image, and import the scanners, the code graph, the lenses, the config parser and the renderers into a Node program.
- `security`: what runs, what is sent where, and where files go.
- `telemetry`: there is none.
- `privacy`: the privacy policy: what OpenQodex collects (nothing) and every network call it makes.
- `plumbing`: the hidden commands that hooks, the skill and the Action call.
- `internal-reviewer-drivers`: how the Claude Code and Codex reviewers are started and held to reading.
- `faq`: short answers.
- `benchmark`: how review quality is measured, from a clone of the repository, and the rule that a claim about it cites a saved run.
- `benchmark-results`: the accepted benchmark numbers, written by a script from the results index.

### docs/quickstart.md

# Quickstart

## Paste this prompt into your agent

```
Install OpenQodex for yourself with `npx -y openqodex@0.12.0 init --yes --agent <host>`. Use the agent you are as <host>: claude-code, codex, cursor or cline. Run the command from this repository. Run it in the background and wait until it exits. It ends with a review of my current change when a reviewer can start. Tell me the verdict and the findings. If there was no review, tell me what its last lines say is missing.
```

The agent runs `init` for itself: the same install as the steps below, the push gate included, with no question (`--yes`). Then `init` reviews your change and the agent tells you the result. The steps below do the same by hand.

Codex runs commands in a sandbox that by default cannot write outside the project or reach the network: from Codex, run the line in your own terminal instead.

The skill alone, with no push gate, launcher or scanner download: `npx skills add openqodex/openqodex -g`. A later `init` replaces it with the skill it keeps up to date.

## Before you start

- Node 22 or newer, and git.
- Claude Code or Codex, installed and logged in. It is the reviewer OpenQodex starts. Without either, `review` runs the scanners, says "Full review unavailable", and names the command with which the agent you are in reviews the change itself.
- macOS or Linux. On Windows, use WSL.
- A git repository with a change in it.

## 1. Install into your agent

In your own terminal:

```
npx openqodex init
```

From inside an agent, the line is `npx -y openqodex@0.12.0 init --yes --agent <host>`, as in the prompt above.

`init` finds Claude Code, Cursor, Codex CLI and Cline on your machine. It prints each file it will write, for you and for the team, then asks once: "Write these files?". `--yes` skips the question. `agents` lists every file for each agent.

Inside a repository, `init` also:

- adds the git pre-push hook, so every push from that repository is checked for a review, from an agent or by hand. `--hook none` leaves it out.
- adds one line to each agent's global instruction file, such as `~/.claude/CLAUDE.md` for Claude Code: before any push, review the change with the openqodex skill. It prints the line before writing it.
- adds a review section to the repository's `CLAUDE.md` and `AGENTS.md`, so a teammate's agent reviews before it pushes too. `--no-repo` leaves it out.
- creates `.openqodex/config.yaml` and `.openqodex/custom-instructions.md`. Commit both. Write in `custom-instructions.md` what a reviewer of your repository must know: conventions, what never to flag, what always to check. The review brief carries it word for word. You can also choose [convention files](config.md#convention-files) for the brief.

After writing, `init` lists what it wrote for you, with the command that undoes it (`init --uninstall` through the launcher), and what it wrote for the team, to commit. `init --project` instead puts the agent files inside the repository, for the team to commit; the scanners and the record of what `init` wrote stay in `~/.openqodex` on your machine.

`init` also starts the scanner downloads that your repo needs, in the background: the ones its files call for, tracked or untracked, less the paths `review.paths.exclude` leaves out and any scanner `scanners.disable` switches off. It prints one line per scanner saying why, such as `oxlint: JavaScript or TypeScript files, such as app/index.tsx`. `init --dry-run` prints those lines and downloads nothing. Running it outside the agent matters: some agents run commands in a sandbox that cannot download.

Then `init` checks the reviewers: it prints "Reviewer ready" with the Claude Code or Codex it found, or "No reviewer can start yet" with what to fix for each.

Last, `init` reviews, when a reviewer can start: when the repository has a change, it runs `openqodex review` and prints its receipt. When it has none, it asks what to review: the whole repository, a pull request, a branch, or not now. With `--yes` or without a terminal it prints the three commands instead of asking. `--no-review` skips this step. The review waits up to two minutes for a scanner its change needs that is still downloading, names any still going after that, and never fails `init`. One line says how it ended: `First review: finished`, `incomplete`, `skipped` or `unavailable`.

Codex only: open Codex, run `/hooks` and trust the OpenQodex hook. Codex runs a new hook only after you trust it.

## 2. Ask for a review

Say to your agent:

```
review my change with openqodex
```

The agent runs `openqodex review` and shows you the receipt it prints. That one command works out the change, copies it to a temporary folder, runs the scanners and the code graph, and starts its own reviewer: a separate Claude Code or Codex process that reads that copy. Scripts then check that the reviewer answered every scanner finding and was given every changed line. OpenQodex writes the report and prints the receipt. The review uses your Claude Code or Codex plan. It can take minutes. On the 2026-10-09 benchmark run, a review of a small change took about two minutes with Claude Code. In your terminal, run it by the full path `init` prints, `~/.openqodex/bin/openqodex review`: an npx install puts no `openqodex` on your `PATH`, and `init` never edits your shell profile.

To review the whole repository instead of one change, say:

```
review my whole repo with openqodex
```

The agent runs `openqodex review --all`. The scanners check every file, and the brief tells the reviewer where to start: the most-called functions and the files with the most scanner hits. See `docs/cli.md` for the details.

To review a teammate's branch or a pull request before it merges, without leaving your own work, say:

```
review the branch feature/login with openqodex
review pull request #42 with openqodex
```

The agent runs `openqodex review feature/login` or `openqodex review '#42'`. OpenQodex fetches the branch or the pull request, checks it out in a temporary folder and reviews what it added since it left its base. Your working folder is not touched. See "Reviewing a branch or a pull request" in `docs/cli.md`.

## 3. Read the report, then choose what to fix

The agent shows you the receipt as OpenQodex printed it: the verdict, the reviewer's summary, one line per finding (its number, severity, category, title, file and line), and the absolute paths of `report.html` and `report.md`. Then it asks: "Fix all, or tell me which?"

Open `report.html` in a browser. It shows each changed file as a diff with each finding under its line: the problem, why it matters, the fix and its source. Below are the coverage, the scanners and the blast radius. The page runs no script and loads nothing. Then answer the agent by number, such as "fix 1 and 3", or say "fix all". The agent fixes only the findings you name, runs the review again and shows you the new receipt.

A complete review means every stage ran, every scanner finding was checked and every changed line was put in front of the reviewer; anything not covered is named. It does not mean nothing was missed. The report is in `.openqodex/reviews/<time>-<id>/` in your repo. `.openqodex/.gitignore` keeps the reports out of git; `git status` shows only the two files above and that `.gitignore`, the first time.

The verdict is `passed` unless `.openqodex/config.yaml` sets `review.block_on_severity` and a finding meets it. With no config, OpenQodex warns and never blocks.

## Try it on the demo repo

```
npx openqodex demo /tmp/openqodex-demo
```

`demo` builds a small repo with 15 planted bugs. Among them are a secret, a SQL injection, Dockerfile problems, a vulnerable lockfile, shell bugs, a workflow injection, a risky database migration, Terraform open to the internet and a privileged Kubernetes container. It scans the change and prints the scanner report. Two of the bugs need the reviewer: no scanner can see them. Then run `openqodex review` in that folder, or open it in your agent and ask for a review.

## Without an agent

Run the review yourself:

```
npx openqodex review
```

`openqodex scan` runs the scanners only and prints their findings unchecked. It is the check the pre-commit hook runs, and the GitHub Action without an Anthropic API key; it is not a review.

## First run

Scanners download on first use into `~/.openqodex/tools/`. A review downloads only the scanners its changed files call for. A scanner still installing after 45 seconds keeps going in the background. The report lists it as installing. It joins the next run.

One measured first run, on 2026-10-02, when the demo needed eight scanners: an Apple Silicon Mac, an empty tool folder, a line of 2 MB per second. The first `demo` printed its report in under a minute. That report held the scanners that had finished installing and listed the rest as installing. The next `scan` included all eight. On 2026-10-12, the 16 scanners that the demo now downloads took 1,018 MiB on an Apple Silicon Mac, with the shared Python. That is the sum of `du -sk` over their folders in `~/.openqodex/tools`. `scanners` gives the size of each one.

To download what this repository needs now, run this inside it:

```
npx openqodex doctor --install
```

`--all-scanners` downloads every scanner.

## Next

- `config`: block pushes at a severity, exclude paths, switch scanners off.
- `custom-scanners`: add any scanner by its GitHub link.
- `security`: what runs and what is sent where.

### docs/benchmark-results.md

# Benchmark results

Generated by `node scripts/benchmark-results.mjs` from `benchmark/index`. Do not edit this page by hand.

## How to read this

- A group is one configuration on one set of cases under one version of the scoring rules. Each row is the run a person accepted for its group.
- Library is the Node library's reviewChange function. It reviews with the model in the row, as a server would.
- Planted bugs are small changes with bugs put in on purpose. The suite also has clean changes with no bug.
- AACR-Bench is an outside benchmark of real pull requests. Its known issues are the review comments that the dataset marks as accepted.
- Issue recall is the share of known issues that the reviews found. Each count adds up every repeat of the run.
- The brackets give the 95% interval for issue recall. The true recall is likely inside that range.
- On AACR-Bench, a finding counts toward issue recall only after a person rules it the same issue as a reference comment.
- Not yet ruled means every finding of the run still waits for a person's ruling. Its issue recall is unknown until then.
- Location recall is the share of known issues with a finding within one line, whatever the finding says.
- Precision is the share of reported findings that are correct. An unresolved finding is one the case does not list and no person has ruled on.
- The precision lower bound counts every unresolved finding as wrong. The upper bound counts every unresolved finding as correct.
- Clean rate is the share of reviews of clean changes that report no finding.
- Cost and time are the mean per review. Not measured means the run did not record that number.
- An A/A twin runs the same build on the same cases a second time. Its noise is the difference in issues found between the two runs.
- A gap between two rows that is smaller than the A/A noise can be chance.
- Board numbers come from AACR-Bench's own evaluator. Line numbers match a finding to a reference comment by file and lines.
- Semantic numbers also need the evaluator's judge to agree that the two say the same thing. F1 combines precision and recall in one number.
- Noise rate is the share of findings that match no reference comment. Board numbers never decide whether a run is accepted.
- A subset, such as dev-smoke, covers only the cases it names. Compare two rows only when they ran the same cases.
- The README shows an AACR-Bench row only once it has board numbers or a ruled hit. This page shows every row.

## AACR-Bench

| Reviewer | Model | Group | Repeats | Issue recall | Location recall | Precision lower bound | Precision upper bound | Clean rate | Cost per review | Time per review | Run | Accepted date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | claude-opus-5-5 | claude-graph-on, dev split, dev-laptop subset, review mode, laptop path, rules 8, split hash edf0f4863eb8 | 3 | not yet ruled | 82/768 (10.7%) | 0/137 (0.0%) | 137/137 (100.0%) | not measured | $0.3383 | 41.5 s | [2026-10-13-b43b25b-aacr-claude](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-13-b43b25b-aacr-claude.tar.gz) | 2026-10-13 |
| Codex | gpt-6.1-sol | codex-graph-on, dev split, dev-laptop subset, review mode, laptop path, rules 8, split hash edf0f4863eb8 | 3 | not yet ruled | 88/768 (11.5%) | 0/180 (0.0%) | 180/180 (100.0%) | not measured | not measured | 65.0 s | [2026-10-13-b43b25b-aacr-codex](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-13-b43b25b-aacr-codex.tar.gz) | 2026-10-13 |
| Library | gpt-6.1-sol | model-gpt-6.1-sol-graph-on, dev split, dev-laptop subset, review mode, server path, rules 7, split hash edf0f4863eb8 | 3 | not yet ruled | 87/768 (11.3%) | 0/176 (0.0%) | 176/176 (100.0%) | not measured | $0.0839 | 58.4 s | [2026-10-12-b43b25b-aacr-gpt61](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-aacr-gpt61.tar.gz) | 2026-10-13 |
| Scanner only | no model | scan, dev split, dev-smoke subset, scan mode, laptop path, rules 1, split hash edf0f4863eb8 | 1 | 0/16 (0.0%) [interval not available] | 0/16 (0.0%) | not measured | not measured | not measured | not measured | 7.8 s | [2026-10-12-eee3d15-aacr-dev-smoke-scan-ci](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-eee3d15-aacr-dev-smoke-scan-ci.tar.gz) | 2026-10-12 |

### Board scores

[2026-10-13-b43b25b-aacr-claude](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-13-b43b25b-aacr-claude.tar.gz), claude-graph-on: not yet board-scored.

[2026-10-13-b43b25b-aacr-codex](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-13-b43b25b-aacr-codex.tar.gz), codex-graph-on: not yet board-scored.

[2026-10-12-b43b25b-aacr-gpt61](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-aacr-gpt61.tar.gz), model-gpt-6.1-sol-graph-on: not yet board-scored.

[2026-10-12-eee3d15-aacr-dev-smoke-scan-ci](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-eee3d15-aacr-dev-smoke-scan-ci.tar.gz), scan: not yet board-scored.

## Planted bugs

| Reviewer | Model | Group | Repeats | Issue recall | Location recall | Precision lower bound | Precision upper bound | Clean rate | Cost per review | Time per review | Run | Accepted date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | claude-opus-5-5 | claude-graph-on, dev split, review mode, laptop path, rules 7 | 3 | 129/153 (84.3%) [72.9%, 98.0%] | 133/153 (86.9%) | 142/146 (97.3%) | 146/146 (100.0%) | 6/6 (100.0%) | $0.0870 | 26.4 s | [2026-10-12-b43b25b-go126-claude](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-go126-claude.tar.gz) | 2026-10-12 |
| Codex | gpt-6.1-sol | codex-graph-on, dev split, review mode, laptop path, rules 7 | 3 | 115/153 (75.2%) [62.8%, 92.8%] | 120/153 (78.4%) | 125/146 (85.6%) | 146/146 (100.0%) | 6/6 (100.0%) | not measured | 47.1 s | [2026-10-12-b43b25b-go126-codex](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-go126-codex.tar.gz) | 2026-10-12 |
| Scanner only | no model | scan, dev split, scan mode, laptop path, rules 1 | 1 | 32/51 (62.7%) [38.9%, 77.4%] | 34/51 (66.7%) | 35/45 (77.8%) | 40/45 (88.9%) | 1/2 (50.0%) | not measured | 8.7 s | [2026-10-11-adab00c-planted-scan-ci](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-11-adab00c-planted-scan-ci.tar.gz) | 2026-10-11 |

A/A noise for claude-graph-on: [2026-10-12-b43b25b-go126-claude](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-go126-claude.tar.gz) found 129 issues, and its twin [2026-10-12-b43b25b-go126-claude-aa](https://github.com/openqodex/openqodex/releases/download/benchmark-data/2026-10-12-b43b25b-go126-claude-aa.tar.gz) found 136. The difference is 7 issues across 3 repeats, or 2.33 per repeat.

[Benchmark methods](benchmark.md)

## Top-level structure

- `packages/` — pnpm workspace packages bundled into the single `openqodex` CLI:
  - `cli/` — the `openqodex` binary (`dist/bin.js`, no runtime deps), templates, CHANGELOG
  - `core/` — change source, config parser, lenses, review brief, renderers
  - `scanners/` — scanner adapters, changed-line filter, pinned `toolchain.json`, locks
  - `graph/` — code graph (corpus, scripts)
  - `review/` — review engine used by the Node library
  - `mcp/` — MCP server exposing the code graph
- `plugins/claude-code/` — Claude Code plugin (`.claude-plugin`, `.mcp.json`, hooks, skills)
- `plugins/codex/` — Codex plugin (`.codex-plugin`, skills)
- `skills/openqodex/SKILL.md` — the agent skill
- `.claude-plugin/marketplace.json`, `.cursor-plugin/plugin.json` — marketplace/plugin manifests
- `docs/` — shipped docs (agents, benchmark, benchmark-results, claude-code-review, cli, config, custom-scanners, faq, for-agents, github-action, graph, index, internal-reviewer-drivers, library, llms.txt, plumbing, privacy, quickstart, scanners, security, telemetry)
- `examples/demo-repo/` — sample repo with planted bugs (baseline, planted, expected.json)
- `benchmark/` — benchmark harness (cases, suites, splits, judge/score/run scripts, review-queue)
- `tests/` — e2e and golden tests
- `scripts/` — build/docs/scrub scripts
- `action.yml` — GitHub Action
- `.pre-commit-hooks.yaml` — pre-commit hook (scanners only)
- `.openqodex.yaml`, `.semgrepignore`, `.snyk`, `.aikido` — self-review/scanner config
- `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `NOTICE`, `LICENSE`
- `.changeset/`, `.github/`, `assets/`, `.playwright-mcp/` — release tooling, CI, assets
