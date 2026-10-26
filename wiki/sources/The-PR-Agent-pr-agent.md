---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/The-PR-Agent/pr-agent
tags:
  - open-source-pr-review
  - multi-git-provider
  - litellm
  - github-action
  - agent-skills
  - self-hosted
  - code-suggestions
  - compression-strategy
related:
  - coderabbit.ai
  - greptile.com
  - agent-field-pr-af
  - openqodex-openqodex
  - sonarsource.com
  - litellm.ai
product: pr-agent
detail_level: standard
created: 2026-10-26
updated: 2026-10-26
---

PR-Agent is the original open-source AI pull-request reviewer (13,611 stars, MIT, Python, latest release v0.49.0). Qodo donated the project to the community; it now lives in the `The-PR-Agent` GitHub org, with docs at docs.pr-agent.ai and a homepage at pr-agent.ai. The README states that this repository is the community-maintained legacy project and is distinct from Qodo's hosted AI code-review product (and from Qodo's free tier for open-source projects). Each main tool (`/review`, `/improve`, `/ask`) is designed as a single LLM call, about 30 seconds and low cost, and the same commands run as a PR comment, a CLI, a GitHub Action, or a self-hosted webhook. For this wiki it is the self-hosted, multi-forge counterpart to hosted reviewers such as [[coderabbit.ai]] and [[greptile.com]], and to local pre-push review in [[openqodex-openqodex]].

_All claims below are sourced from ../../raw/github/The-PR-Agent-pr-agent.md unless otherwise noted._

## What it does

PR-Agent reads a pull request (or, for `/similar_issue`, an issue), builds prompt context from the diff plus surrounding code, calls a configured model, and publishes the result back through the git provider. Tools cover description, review, code suggestions, free-text Q&A, documentation generation, custom labels, similar-issue search, help, and changelog updates. `/help_docs` has been disabled since v0.36.1 pending a credential-exposure fix (issue #2445).

Invocation is local CLI, a comment on the PR, or automatic runs when a PR opens or a branch is pushed. Supported forges in the platform matrix are GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea, plus registered Gerrit and CodeCommit providers. Deployment options are CLI, GitHub Action, Docker, self-hosted webhooks, and polling.

## Installation

Recommended path in the README is a GitHub Action on `pull_request` `opened` and `synchronize`, using `the-pr-agent/pr-agent@main` with `OPENAI_KEY` and `GITHUB_TOKEN`.

Local CLI:

```bash
pip install "pr-agent[github]"
export OPENAI_KEY=your_key_here
pr-agent --pr_url https://github.com/owner/repo/pull/123 review
```

Git-provider SDKs are extras (`github`, `gitlab`, `bitbucket`, `azure`, `codecommit`, `gitea`); `pr-agent[all]` installs every integration. Docker uses the `pragent/pr-agent` image (releases 0.34.2 and later; older images stay on the frozen `codiumai/pr-agent` namespace):

```bash
docker run --rm -it \
  -e OPENAI__KEY=<your_openai_key> \
  -e GITHUB__USER_TOKEN=<your_github_token> \
  pragent/pr-agent:latest --pr_url <pr_url> review
```

From source: `git clone`, `uv sync` (Python ≥ 3.12), copy `pr_agent/settings/.secrets_template.toml` to `.secrets.toml`, then `uv run pr-agent --pr_url <pr_url> review`. The `similar_issue` extra is `uv sync --group similar-issue`.

Webhook servers for GitHub, GitLab, Gitea, and Bitbucket Server run under gunicorn. The default worker cap is 4; importing the app costs about 250MB, and the docs suggest starting near 1Gi for four workers. GitHub polling only accepts mention notifications from host-configured `github.polling_repositories` and caps child workers at 10.

## Key features

- **Command tools** — `/describe` (title, type, summary, walkthrough, labels), `/review` (issues, security, tests, review effort), `/improve` (actionable suggestions), `/ask`, `/add_docs`, `/generate_labels`, `/similar_issue` (issue-scoped), `/help`, `/update_changelog`. Describe, review, improve, ask, and add-docs are supported on the five main forges. Similar issues is GitHub-only. Generate-labels and changelog updates fall back to a comment (💬) where the provider cannot set labels or push files.
- **Single-call cost model** — `/review`, `/improve`, and `/ask` each use one LLM call. Describe output is reused as metadata for later review and improve calls so the chain-of-thought does not require extra API calls.
- **Compression** — small PRs fit in one prompt with three lines of context around each hunk. Large PRs drop binary and non-code files, prefer the repo's main languages, keep additions over deletion-only hunks, and pack patches with tiktoken until a token buffer, listing the rest as `other modified files`.
- **Dynamic context** — more lines before a change than after, extended up to an enclosing function or class (`max_extra_lines_before_dynamic_context = 8` by default) so the model sees structure without a full-file dump.
- **Self-reflection** — a follow-up call scores `/improve` suggestions 0–10, drops zeros, re-ranks, and can filter below `suggestions_score_threshold`. Suggestions are shown hierarchically (category, one-line summary, expandable snippet).
- **Agent skills** — optional host-level `SKILL.md` libraries injected into review, improve, describe, and ask. Disabled by default, capped by `max_skills_tokens` (8000). `skills.paths` is host-only so a repo `.pr_agent.toml` cannot point the scanner at host files. Scripts and assets are skipped because calls are single-shot, with no tool-use loop.
- **Repo context** — `AGENTS.md` and similar per-repo context files are a documented core ability on the main forges. Organization `extra_instructions` and best practices can be injected with the diff, commit history, and full contents of modified files.
- **Models** — OpenAI, Anthropic Claude, Gemini, DeepSeek, Mistral, and any LiteLLM route (Azure OpenAI, Bedrock, Vertex, Databricks, OpenRouter, Ollama, and others) via `pr_agent/algo/ai_handlers/litellm_ai_handler.py`.

## Architecture

Dispatch is `pr_agent/agent/pr_agent.py` → `command2class` → a tool class under `pr_agent/tools/` with `async def run(self)`. A tool loads a `GitProvider`, gathers PR context, fills a `self.vars` dict, renders Jinja2 prompts (`StrictUndefined`) through `TokenHandler`, calls the model handler, and publishes via the provider. Prompts live as TOML under `pr_agent/settings/` and must be listed in `config_loader.py` or they are not loaded.

Settings use Dynaconf (`get_settings()`). Defaults are `configuration.toml`. Per-repo `.pr_agent.toml` is applied by `apply_repo_settings` before dispatch. `config_security.py` drops host-only keys that a repository tries to set. Environment variables override files (`SECTION__KEY`). Secrets stay in env vars or gitignored `.secrets.toml`, with optional AWS Secrets Manager.

Providers implement `pr_agent/git_providers/git_provider.py` and are selected with `config.git_provider`. Built-in ids include `github`, `gitlab`, `bitbucket`, `bitbucket_server`, `azure`, `codecommit`, `local`, `gerrit`, `gitea`, and `plain-diff`. Extra packages can `register_git_provider` before resolution. Capability checks (`provider.is_supported("feature")`) gate behavior; Gerrit and CodeCommit lack `gfm_markdown`, so `/describe` omits some sections there.

`pr_agent/servers/` turns webhook and polling events into `PRAgent.handle_request`. The CLI is `pr_agent/cli.py` (`pr-agent`). `algo/` holds patch fitting, token budgets, skills loading, review merge, and the LiteLLM handler. Tests default to `tests/unittest` via `PYTHONPATH=. uv run pytest`; e2e tests need provider credentials.

## Example usage

Comment on a PR, or run the CLI:

```bash
/describe
/review
/improve
/ask "What does this PR change?"

pr-agent --pr_url <PR_URL> review
pr-agent --issue_url <ISSUE_URL> similar_issue
```

From a checkout, the same tools are `uv run pr-agent --pr_url <pr_url> review` (and `describe`, `improve`, `ask`, `add_docs`, `generate_labels`). Quoted CLI overrides share the automation parser, for example `/review --pr_reviewer.extra_instructions='be concise please'`.

## Maintenance status

Active community project: 13,611 stars, 1,996 forks, default branch `main`, pushed 2026-10-26, latest release v0.49.0 on 2026-10-25. License is MIT. Primary language is Python (≥ 3.12). First external maintainer is Naor (@naorpeled); the README says the project is in the process of being donated to an open-source foundation, with development supported by sponsors (Qodo is the listed gold sponsor). Versioned GitHub release tags and Docker version tags are immutable; rolling tags (`latest`, `github_action`, and the per-service tags) move on every release. Docs are the Docusaurus site in `docs/`, and self-hosted usage keeps the model API key between the operator and the provider. It sits next to [[agent-field-pr-af]] (longer multi-agent PR audits) and [[sonarsource.com]] (deterministic quality gates), and it calls models through [[litellm.ai]].
