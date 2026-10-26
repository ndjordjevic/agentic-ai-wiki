# The-PR-Agent/pr-agent

## Metadata
- Stars: 13611
- Forks: 1996
- Primary language: Python
- Default branch: main
- Latest release: v0.49.0 (2026-10-25)
- License: MIT License
- Homepage: https://www.pr-agent.ai
- Pushed: 2026-10-26
- Fetched: 2026-10-26
- Final URL: https://github.com/The-PR-Agent/pr-agent

## Description
🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier.

## README


<br />

<div align="center">


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/logo-dark.png" width="330">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/logo-light.png" width="330">
  <img src="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/logo-light.png" alt="logo" width="330">

</picture>
<br>
The Original Open-Source PR Reviewer
<br><br>
<a href="https://github.com/the-pr-agent/pr-agent/commits/main">
<img alt="GitHub" src="https://img.shields.io/github/last-commit/the-pr-agent/pr-agent/main?style=for-the-badge" height="20">
</a>
</div>

---

 This repository contains the open-source PR Agent Project.
 It is not the Qodo offering for open-source projects.

PR-Agent is an open-source, AI-powered code review agent and a community-maintained legacy project of Qodo. It is distinct from Qodo's primary AI code review offering, which provides a feature-rich, context-aware experience. Qodo offers a free version for open-source projects and integrates seamlessly with GitHub, GitLab, Bitbucket, and Azure DevOps for high-quality automated reviews.


## Sponsors

PR-Agent is a community-maintained open-source project, with its ongoing development supported by our sponsors. If you'd like to support the project, consider [becoming a sponsor](https://github.com/sponsors/naorpeled).

<p align="center">
  <h3 align="center">🥇 Gold Sponsor</h3>
</p>

<p align="center">
  <a target="_blank" href="https://www.qodo.ai/">
    <img alt="Qodo — Gold sponsor" src="https://www.qodo.ai/wp-content/uploads/2025/03/qodo-logo.svg" width="150">
  </a>
</p>

<p align="center">
  <a target="_blank" href="https://www.qodo.ai/solutions/open-source/">Free version of Qodo for open-source projects</a>
</p>


## Table of Contents

- [Getting Started](#getting-started)
- [Why Use PR-Agent?](#why-use-pr-agent)
- [Features](#features)
- [See It in Action](#see-it-in-action)
- [How It Works](#how-it-works)
- [Data Privacy](#data-privacy)
- [Contributing](#contributing)

## Getting Started

> [!NOTE]
> **Docker Hub namespace migration.** Releases `0.34.2` and later are published under [`pragent/pr-agent`](https://hub.docker.com/r/pragent/pr-agent). Older releases (up to and including `v0.31`) remain available at the legacy [`codiumai/pr-agent`](https://hub.docker.com/r/codiumai/pr-agent) namespace as a frozen archive — no new images are pushed there. Update any pinned `image:` / `docker pull` / `uses: docker://` references when upgrading to `0.34.2+`.

### 🚀 Quick Start for PR-Agent

#### 1. GitHub Action (Recommended)

Add automated PR reviews to your repository with a simple workflow file:

```yaml
# .github/workflows/pr-agent.yml
name: PR Agent
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  pr_agent_job:
    runs-on: ubuntu-latest
    steps:
    - name: PR Agent action step
      uses: the-pr-agent/pr-agent@main
      env:
        OPENAI_KEY: ${{ secrets.OPENAI_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
[Full GitHub Action setup guide](https://docs.pr-agent.ai/installation/github/#run-as-a-github-action)

#### 2. CLI Usage (Local Development)

Run PR-Agent locally on your repository:

```bash
pip install "pr-agent[github]"
export OPENAI_KEY=your_key_here
pr-agent --pr_url https://github.com/owner/repo/pull/123 review
```
Git provider SDKs are optional extras: install the one for your provider ([list](https://docs.pr-agent.ai/installation/locally/#using-pip-package)), or `pr-agent[all]` for every integration.
[Complete CLI setup guide](https://docs.pr-agent.ai/usage-guide/automations_and_usage/#local-repo-cli)

#### 3. Other Platforms

- [GitLab webhook setup](https://docs.pr-agent.ai/installation/gitlab/)
- [BitBucket app installation](https://docs.pr-agent.ai/installation/bitbucket/)
- [Azure DevOps setup](https://docs.pr-agent.ai/installation/azure/)

## News and Updates

Full notes for every release are on the [Releases page](https://github.com/the-pr-agent/pr-agent/releases).


## Why Use PR-Agent?

### 🎯 Built for Real Development Teams

**Fast & Affordable**: Each tool (`/review`, `/improve`, `/ask`) uses a single LLM call (~30 seconds, low cost)

**Handles Any PR Size**: Our [PR Compression strategy](https://docs.pr-agent.ai/core-abilities/compression_strategy/) effectively processes both small and large PRs

**Highly Customizable**: JSON-based prompting allows easy customization of review categories and behavior via [configuration files](pr_agent/settings/configuration.toml)

**Platform Agnostic**:
- **Git Providers**: GitHub, GitLab, BitBucket, Azure DevOps, Gitea
- **Deployment**: CLI, GitHub Actions, Docker, self-hosted, webhooks
- **AI Models**: OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any other model reachable through LiteLLM (Azure OpenAI, AWS Bedrock, Vertex AI, Databricks, OpenRouter, Ollama, and more) — see [Changing a model](https://docs.pr-agent.ai/usage-guide/changing_a_model/)

**Open Source Benefits**:
- Full control over your data and infrastructure
- Customize prompts and behavior for your team's needs
- No vendor lock-in
- Community-driven development

## Features

<div style="text-align:left;">

See the current [feature and git provider support matrix](https://docs.pr-agent.ai/overview/supported_platforms/) in the PR-Agent documentation.

⚠️ `/help_docs` is temporarily disabled since `v0.36.1` pending a fix for a credential-exposure issue ([#2445](https://github.com/the-pr-agent/pr-agent/issues/2445)).

[//]: # (- Support for additional git providers is described in [here]&#40;./docs/Full_environments.md&#41;)
___

## See It in Action

</div>
<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/describe_new_short_main.png" width="512">
</p>
</div>
<hr>

<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/732#issuecomment-1975099151">/review</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/review_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/the-pr-agent/pr-agent/pull/732#issuecomment-1975099159">/improve</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/improve_new_short_main.png" width="512">
</kbd>
</p>
</div>

<hr>

### Usage Examples

PR-Agent tools run as a comment on a PR or from the CLI. A few common ones:

```bash
# Comment on a PR (GitHub/GitLab/Bitbucket/…):
/describe
/review
/improve
/ask "What does this PR change?" # free-text Q&A about the PR

# Issue-scoped commands run on an issue instead of a PR:
/similar_issue # find similar issues in the repository

# Or locally via the CLI:
pr-agent --pr_url <PR_URL> review
pr-agent --issue_url <ISSUE_URL> similar_issue
```

See the [Tools docs](https://docs.pr-agent.ai/tools/#usage-examples) for the full list of tools with example commands, and each tool's page for screenshots and options.

<hr>

## How It Works

The following diagram illustrates PR-Agent tools and their flow:

![PR-Agent Tools](https://raw.githubusercontent.com/The-PR-Agent/pr-agent/main/docs/static/img/diagram-v0.9.png)

## Data Privacy

### Self-hosted PR-Agent

- If you host PR-Agent with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

## Contributing

To contribute to the project, get started by reading our [Contributing Guide](https://github.com/the-pr-agent/pr-agent/blob/main/CONTRIBUTING.md).

For local verification, run `PYTHONPATH=. uv run pytest` from the repository root; it discovers the unit-test suite under `tests/unittest` by default. End-to-end tests under `tests/e2e_tests` require provider credentials and should be invoked explicitly, for example `PYTHONPATH=. uv run pytest tests/e2e_tests/test_github_app.py`.


## Big News for PR-Agent

PR-Agent has a new home!

After years of building this tool alongside the community, Qodo has donated PR-Agent to the open-source community - and we couldn't be more excited about what comes next.

The project now lives in the PR-Agent org on GitHub, is fully community-owned, and is open for contributions and additional maintainers.

What else changed:
- Docs moved to - [docs.pr-agent.ai](https://docs.pr-agent.ai/)
- Qodo Merge (Qodo 1.0), the hosted URL, which was the enterprise version of PR-Agent, has been rebranded and evolved into Qodo (Qodo 2.0), a full AI code review platform.

## ❤️ Community

This open-source release remains here as a community contribution from Qodo — the origin of modern AI-powered code collaboration. We’re proud to share it and inspire developers worldwide.

The project now has its first external maintainer, Naor ([@naorpeled](https://github.com/naorpeled)), and is currently in the process of being donated to an open-source foundation.

## Docs

Fetched at standard detail: docs landing, platform matrix, privacy, installation index, local install, tools index, core abilities (skills, compression, dynamic context, metadata, self-reflection), usage introduction, extending guide, and root `AGENTS.md`.

Docs tree under `docs/docs/` (not every file inlined): `index.mdx`, `core-abilities/`, `faq/`, `installation/` (azure, bitbucket, gitea, github, gitlab, locally, mosaico_server, index), `overview/` (data_privacy, supported_platforms), `tools/` (add_docs, ask, describe, generate_labels, help, help_docs, improve, review, similar_issues, update_changelog, index), `usage-guide/` (additional_configurations, automations_and_usage, changing_a_model, configuration_options, configuration_reference, custom_ca_and_self_signed_certificates, extending_pr_agent, introduction, local_git_provider, mail_notifications, plain_diff_mode, push_outputs, index). The Docusaurus site also has `docs/docusaurus.config.js`, `docs/sidebars.js`, `docs/src/`, `docs/static/`, and `docs/i18n/`.

### docs/docs/index.mdx

---
title: "Overview"
sidebar_position: 1
description: "Open-source AI agent that reviews, describes and improves pull requests on GitHub, GitLab, Bitbucket, Azure DevOps and Gitea."
hide_title: true
hide_table_of_contents: true
displayed_sidebar: null
custom_edit_url: null
pagination_prev: null
pagination_next: null
---

import Hero from '@site/src/components/Hero';
import MaintainerAvatars from '@site/src/components/MaintainerAvatars';

<Hero />

<div className="pra-landing-body">

## Quick start

Review a pull request from your terminal. All you need is an OpenAI key and a GitHub token.

```bash
docker run --rm -it \
  -e OPENAI__KEY=<your_openai_key> \
  -e GITHUB__USER_TOKEN=<your_github_token> \
  pragent/pr-agent:latest --pr_url <pr_url> review
```

<div className="pra-cta-row">

[Install it on your repositories](./installation/index.md) [Other ways to run it locally](./installation/locally.md)

</div>

Already installed? Comment `/help "your question"` on a pull request and PR-Agent answers from these docs.

## Maintained by

<MaintainerAvatars />

<div className="pra-cta-row">

[Meet the team](/maintainers/)

</div>

</div>

### docs/docs/overview/supported_platforms.md

---
title: "Supported platforms"
sidebar_position: 3
---

Which tools, triggers and core abilities work on each git provider.

|       |    | <span class="pra-provider"><span class="pra-logo pra-logo--github" aria-hidden="true"></span>GitHub</span> | <span class="pra-provider"><span class="pra-logo pra-logo--gitlab" aria-hidden="true"></span>GitLab</span> | <span class="pra-provider"><span class="pra-logo pra-logo--bitbucket" aria-hidden="true"></span>Bitbucket</span> | <span class="pra-provider"><span class="pra-logo pra-logo--azuredevops" aria-hidden="true"></span>Azure DevOps</span> | <span class="pra-provider"><span class="pra-logo pra-logo--gitea" aria-hidden="true"></span>Gitea</span> |
| ----- |---------------------------------------------------------------------------------------|:------:|:------:|:---------:|:------------:|:-----:|
| [TOOLS](../tools/index.md) | [Describe](../tools/describe.md)                                     |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Review](../tools/review.md)                                                           |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Improve](../tools/improve.mdx)                                                         |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Ask](../tools/ask.md)                                                                 |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Ask on code lines](../tools/ask.md#ask-lines)                                         |   ✅   |   ✅   |           |      ✅       |       |
|       | [Add Docs](../tools/add_docs.md)                                                       |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Generate Labels](../tools/generate_labels.md)                                         |   ✅   |   ✅   |   💬    |      ✅       |       |
|       | [Similar Issues](../tools/similar_issues.md)                                           |   ✅   |        |           |              |       |
|       | [Help](../tools/help.md)                                                               |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Help Docs](../tools/help_docs.md) ⚠️                                                   |        |        |           |              |       |
|       | [Update CHANGELOG](../tools/update_changelog.md)                                       |   ✅   |   ✅   |    ✅     |      💬       |  💬  |
|       |                                                                                       |        |        |           |              |       |
| [USAGE](../usage-guide/index.md) | [CLI](../usage-guide/automations_and_usage.md#local-repo-cli)      |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [App / webhook](../usage-guide/automations_and_usage.md#github-app)                    |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Tagging bot](https://github.com/the-pr-agent/pr-agent#try-it-now)                       |   ✅   |        |           |              |       |
|       | [Actions](../installation/github.md#run-as-a-github-action) <br /> [GitLab pipeline](../installation/gitlab.md#run-as-a-gitlab-pipeline) <br /> [Bitbucket pipeline](../installation/bitbucket.md#run-as-a-bitbucket-pipeline) <br /> [Azure DevOps pipeline](../installation/azure.md#azure-devops-pipeline) |   ✅   |   ✅   |    ✅     |      ✅       |       |
|       |                                                                                       |        |        |           |              |       |
| [CORE](../core-abilities/index.md) | [Adaptive and token-aware file patch fitting](../core-abilities/compression_strategy.md) |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Agent skills (`SKILL.md`)](../core-abilities/agent_skills.md)                         |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Repo context files (`AGENTS.md`)](../usage-guide/additional_configurations.md#bringing-per-repo-context-files-to-pr-agent) |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Compression strategy](../core-abilities/compression_strategy.md)                      |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Dynamic context](../core-abilities/dynamic_context.md)                                |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Fetching ticket context](../core-abilities/fetching_ticket_context.md)                |   ✅   |  ✅   |    ✅     |      ✅       |  ✅   |
|       | [Local and global metadata](../core-abilities/metadata.md)                             |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Multiple models support](../usage-guide/changing_a_model.md)                          |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |
|       | [Self reflection](../core-abilities/self_reflection.md)                                |   ✅   |   ✅   |    ✅     |      ✅       |  ✅   |

⚠️ `/help_docs` is temporarily disabled since v0.36.1 pending a fix for a credential-exposure issue ([#2445](https://github.com/The-PR-Agent/pr-agent/issues/2445)); see [Help Docs](../tools/help_docs.md).

Legend: ✅ = supported. 💬 = the tool runs, but its output is posted as a PR comment instead of being applied (Update CHANGELOG where the provider cannot push files, Generate Labels where it cannot set labels). Blank = not supported, or not yet verified (Generate Labels on Gitea).

## Gerrit and CodeCommit

Gerrit and CodeCommit are registered providers but are kept out of the main table to keep it readable. Support is:

|       |    | <span class="pra-provider"><span class="pra-logo pra-logo--gerrit" aria-hidden="true"></span>Gerrit</span> | <span class="pra-provider"><span class="pra-logo pra-logo--codecommit" aria-hidden="true"></span>CodeCommit</span> |
| ----- |---------------------------------------------------------------------------------------|:------:|:----------:|
| [TOOLS](../tools/index.md) | [Describe](../tools/describe.md), [Review](../tools/review.md), [Improve](../tools/improve.mdx), [Ask](../tools/ask.md), [Add Docs](../tools/add_docs.md), [Help](../tools/help.md) |   ✅   |     ✅     |
|       | [Ask on code lines](../tools/ask.md#ask-lines)                                         |        |            |
|       | [Generate Labels](../tools/generate_labels.md)                                         |   💬   |     💬     |
|       | [Update CHANGELOG](../tools/update_changelog.md)                                       |   💬   |     💬     |
|       | [Similar Issues](../tools/similar_issues.md)                                           |        |            |
| [USAGE](../usage-guide/index.md) | [CLI](../usage-guide/automations_and_usage.md#local-repo-cli)                  |   ✅   |     ✅     |
|       | [App / webhook](../usage-guide/automations_and_usage.md#github-app)                    |   ✅   |            |
|       | Tagging bot / Actions and pipelines                                                   |        |            |
| [CORE](../core-abilities/index.md) | [Agent skills (`SKILL.md`)](../core-abilities/agent_skills.md) and other core abilities |   ✅   |     ✅     |
|       | [Repo context files (`AGENTS.md`)](../usage-guide/additional_configurations.md#bringing-per-repo-context-files-to-pr-agent) |        |            |

Gerrit and CodeCommit do not support `gfm_markdown`, so `/describe` omits semantic file types and a few other sections. CodeCommit setup notes currently live in the [GitHub installation page](../installation/github.md); Gerrit has no dedicated installation page yet.

For Gerrit, the changed-file list and reviewed diff both respect `ignore.glob` and `ignore.regex`. Renamed files use their destination path, while deleted files retain their original path. Files with non-UTF-8 content remain in filename-based language detection but are omitted from the model diff.

### docs/docs/overview/data_privacy.md

---
title: "Data Privacy"
sidebar_position: 2
---

## Self-hosted PR-Agent

- If you self-host PR-Agent with your OpenAI (or other LLM provider) API key, it is between you and the provider.

### docs/docs/installation/index.md

---
title: "Installation"
sidebar_position: 1
---

There are several ways to use PR-Agent:

<div class="pra-provider-grid">

- <span class="pra-logo pra-logo--terminal" aria-hidden="true"></span> [Locally](./locally.md)
- <span class="pra-logo pra-logo--github" aria-hidden="true"></span> [GitHub](./github.md)
- <span class="pra-logo pra-logo--gitlab" aria-hidden="true"></span> [GitLab](./gitlab.md)
- <span class="pra-logo pra-logo--bitbucket" aria-hidden="true"></span> [Bitbucket](./bitbucket.md)
- <span class="pra-logo pra-logo--azuredevops" aria-hidden="true"></span> [Azure DevOps](./azure.md)
- <span class="pra-logo pra-logo--gitea" aria-hidden="true"></span> [Gitea](./gitea.md)

</div>

## GitHub polling HTTP requests

When GitHub polling needs to look back through PR comments, it reuses the polling
HTTP session rather than blocking the event loop with a synchronous request.
`github.polling_request_timeout` sets the total timeout for the entire fallback
comment-history scan, including any follow-up page requests
(default: 10 seconds; positive values are capped at 60). Invalid values use the
default with a warning. Set it in the host configuration or through
`GITHUB__POLLING_REQUEST_TIMEOUT`; repository settings do not control this limit.
This does not change the other polling requests or the sequential notification
scan. The fallback now follows the existing aiohttp session's proxy and TLS
behavior, not Requests-specific environment settings.

GitHub polling only processes mention notifications from repositories listed in
`github.polling_repositories` (for example `["org/repo"]`). The list is
host-only; repository settings and comment arguments cannot widen it. The empty
default ignores every polling notification and still marks it as read, so
configure it in the host configuration or through `GITHUB__POLLING_REPOSITORIES`
before enabling polling or upgrading.

## Sizing a self-hosted webhook server

The GitHub, GitLab, Gitea and Bitbucket Server webhook servers (the `github_app`, `gitlab_webhook`, `gitea_app` and `bitbucket_server_webhook` Docker targets) run under gunicorn with multiple worker processes, so that a worker busy handling a request cannot block the health check served by another. The other deployments — Bitbucket Cloud, Azure DevOps, GitHub polling, and the Lambda variants — do not use this gunicorn worker configuration.

| Variable               | Default   | Description                                                                               |
|------------------------|-----------|-------------------------------------------------------------------------------------------|
| `GUNICORN_WORKERS`     | *(unset)* | Pins the worker count exactly. Overrides the derived count and `GUNICORN_MAX_WORKERS`.    |
| `GUNICORN_MAX_WORKERS` | `4`       | Upper bound on the automatically derived worker count.                                    |
| `PORT`                 | `3000`    | Port the server binds to.                                                                 |

When `GUNICORN_WORKERS` is unset, the worker count is derived from the CPUs actually available to the container (cgroup CPU limit, falling back to CPU affinity), clamped to between 2 and `GUNICORN_MAX_WORKERS`. Note that a CPU *request* without a *limit* leaves no cgroup quota to read, so the cap is what bounds the worker count there.

**Sizing memory:** importing the application costs roughly 250MB. The app is imported once in the gunicorn master and workers are forked from it, so they share most of that baseline copy-on-write rather than each paying it in full — total memory grows with worker count, but by noticeably less than 250MB per worker. Start from about 1Gi for the default of 4 workers and adjust against your own metrics.

If the container is OOMKilled during startup, lower the worker count:

```bash
GUNICORN_WORKERS=2
```

## GitHub polling workers

GitHub polling uses one polling process and a separate child process for each
accepted comment. At most 10 of these child workers may be active across all
polling iterations. If an earlier batch still fills the limit, accepted work
waits for a free slot without blocking the event loop. This can delay the next
notification poll under sustained load.

The existing per-batch limit is unchanged: only the first 10 queued comments in
a batch are accepted; excess work is logged and dropped. Waiting work is held in
memory only. Notification acknowledgement is unchanged, so shutdown or startup
failures do not guarantee redelivery. Dispatch interruptions log the remaining
count. A worker startup failure stops polling rather than risking further
dispatch with an untracked child; inspect the failure before restarting.
Completed children are joined without waiting and closed each iteration;
live children are not terminated on cancellation. This is not a durable queue,
a model-call deadline, or a host-wide memory limit.

## Docker image names and version tags

:::note[Docker Hub namespace migration]
Releases **`0.34.2` and later** are published under [`pragent/pr-agent`](https://hub.docker.com/r/pragent/pr-agent). Older releases (up to and including `v0.31`) remain at the legacy [`codiumai/pr-agent`](https://hub.docker.com/r/codiumai/pr-agent) namespace as a frozen archive — no new images are pushed there. The examples on this site reference the new namespace; if you are pinning to a release before `0.34.2`, swap `pragent/pr-agent` for `codiumai/pr-agent` in your `image:` / `docker pull` / `uses: docker://` references.
:::

:::note[Immutable releases and version tags]
**What you pin is what you get.** Version-numbered artifacts can never change after publication:

- **GitHub releases** — the Git tag cannot be moved or deleted, and attached assets cannot be added, replaced, or removed. The protection also survives repository deletion, so a tag from an immutable release can never be reused by a repository recreated under the same name. (Release titles and notes stay editable; immutability covers the tag and the assets.)
- **Docker images** — version tags such as `0.40.0` and `0.40.0-github_app` always resolve to the same image. Once pushed, they cannot be overwritten or repointed.

**Rolling tags stay mutable by design.** `latest`, `github_action`, `github_lambda`, `gitlab_lambda`, `gitlab_webhook`, `gitea_app`, `mosaico_agent` and `bitbucket_server_webhook` move to the newest build on every release. They are convenient for trying things out, but a `docker pull` of the same rolling tag on two different days can give you two different images.

For anything you depend on — CI, production webhooks, pinned Action steps — reference a version tag (or a digest) rather than a rolling one. Upgrading then becomes a deliberate change you make, not something that happens underneath you.
:::

### docs/docs/installation/locally.md

---
title: "Locally"
sidebar_position: 3
---

To run PR-Agent locally, you first need to acquire two keys:

Local execution has two distinct cases: use the hosted-provider examples below for an existing PR/MR URL, or use the [Local Git Provider guide](../usage-guide/local_git_provider.md) for branch comparisons without a hosted PR/MR.

1. An API key for your configured [language model provider](../usage-guide/changing_a_model.md). For OpenAI, create one <a href="https://platform.openai.com/api-keys" target="_blank" rel="noopener noreferrer">here</a>.
2. A personal access token from your Git platform (GitHub, GitLab, BitBucket, Gitea) with repo scope. GitHub token, for example, can be issued from <a href="https://github.com/settings/tokens" target="_blank" rel="noopener noreferrer">here</a>

## Using Docker image

A list of the relevant tools can be found in the [tools guide](../tools/index.md).

To invoke a tool (for example `review`), you can run PR-Agent directly from the Docker image. Here's how:

- For GitHub:

    ```bash
    docker run --rm -it -e OPENAI__KEY=<your_openai_key> -e GITHUB__USER_TOKEN=<your_github_token> pragent/pr-agent:latest --pr_url <pr_url> review
    ```

    If you are using GitHub enterprise server, you need to specify the custom url as variable.
    For example, if your GitHub server is at `https://github.mycompany.com`, add the following to the command:

    ```bash
    -e GITHUB__BASE_URL=https://github.mycompany.com/api/v3
    ```

- For GitLab:

    ```bash
    docker run --rm -it -e OPENAI__KEY=<your key> -e CONFIG__GIT_PROVIDER=gitlab -e GITLAB__PERSONAL_ACCESS_TOKEN=<your token> pragent/pr-agent:latest --pr_url <pr_url> review
    ```

    If you have a dedicated GitLab instance, you need to specify the custom url as variable:

    ```bash
    -e GITLAB__URL=<your gitlab instance url>
    ```

- For BitBucket:

    ```bash
    docker run --rm -it -e CONFIG__GIT_PROVIDER=bitbucket -e OPENAI__KEY=$OPENAI_API_KEY -e BITBUCKET__BEARER_TOKEN=$BITBUCKET_BEARER_TOKEN pragent/pr-agent:latest --pr_url=<pr_url> review
    ```

- For Gitea:

    ```bash
    docker run --rm -it -e OPENAI__KEY=<your key> -e CONFIG__GIT_PROVIDER=gitea -e GITEA__PERSONAL_ACCESS_TOKEN=<your token> pragent/pr-agent:latest --pr_url <pr_url> review
    ```

    If you have a dedicated Gitea instance, you need to specify the custom url as variable:

    ```bash
    -e GITEA__URL=<your gitea instance url>
    ```


For other git providers, update `CONFIG__GIT_PROVIDER` accordingly and check the [`pr_agent/settings/.secrets_template.toml`](https://github.com/the-pr-agent/pr-agent/blob/main/pr_agent/settings/.secrets_template.toml) file for environment variables expected names and values.

### Utilizing environment variables

It is also possible to provide or override the configuration by setting the corresponding environment variables.
You can define the corresponding environment variables by following this convention: `<TABLE>__<KEY>=<VALUE>` or `<TABLE>.<KEY>=<VALUE>`.
The `<TABLE>` refers to a table/section in a configuration file and `<KEY>=<VALUE>` refers to the key/value pair of a setting in the configuration file.

For example, suppose you want to run `pr_agent` that connects to a self-hosted GitLab instance similar to an example above.
You can define the environment variables in a plain text file named `.env` with the following content:

```bash
CONFIG__GIT_PROVIDER="gitlab"
GITLAB__URL="<your url>"
GITLAB__PERSONAL_ACCESS_TOKEN="<your token>"
OPENAI__KEY="<your key>"
```

Then, you can run `pr_agent` using Docker with the following command:

```shell
docker run --rm -it --env-file .env pragent/pr-agent:latest <tool> <tool parameter>
```

---

### I get an error when running the Docker image. What should I do?

If you encounter an error when running the Docker image, it is almost always due to a misconfiguration of api keys or tokens.

Note that litellm, which is used by pr-agent, sometimes returns non-informative error messages such as `APIError: OpenAIException - Connection error.`
Carefully check the api keys and tokens you provided and make sure they are correct.
Adjustments may be needed depending on your llm provider.

For example, for Azure OpenAI, additional keys are [needed](../usage-guide/changing_a_model.md#azure).
Same goes for other providers, make sure to check the [documentation](../usage-guide/changing_a_model.md#changing-a-model-in-pr-agent)

## Using pip package

Install the package:

```bash
pip install "pr-agent[github]"
```

Git provider SDKs are optional extras, so install the one for your provider: `github`, `gitlab`, `bitbucket` (Bitbucket Cloud, Bitbucket Server and Jira), `azure`, `codecommit` or `gitea`.
`google` adds Vertex AI, `mosaico` adds the Mosaico server, and `pr-agent[all]` installs every integration.

Then run the relevant tool with the script below.
<br>
Make sure to fill in the required parameters (`user_token`, `openai_key`, `pr_url`, `command`):

```python
from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    # Fill in the following values
    provider = "github" # github/gitlab/bitbucket/azure_devops
    user_token = "..."  #  user token
    openai_key = "..."  # OpenAI key
    pr_url = "..."      # PR URL, for example 'https://github.com/the-pr-agent/pr-agent/pull/809'
    command = "/review" # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    return cli.run_command(pr_url, command)


if __name__ == '__main__':
    raise SystemExit(main())
```

With `config.propagate_tool_errors` enabled, forwarding the return value through `SystemExit` makes this script exit with status 1 after a propagated tool error. The default remains status 0.

The Python helper accepts quoted arguments, for example
`cli.run_command(pr_url, "/review --pr_reviewer.extra_instructions='be concise please'")`.
It uses the same quoting rules as configured automation commands: explicitly
quoted setting values stay strings, and unquoted values retain their normal
types. For questions containing apostrophes, use double quotes around the
question, such as `command = '/ask "What\'s changed?"'`.
This does not change how interactive PR comments are parsed.

## Run from source

1. Clone this repository:

   ```bash
   git clone https://github.com/the-pr-agent/pr-agent.git
   ```

2. Navigate to the `/pr-agent` folder and install dependencies with [uv](https://docs.astral.sh/uv/) (creates a `.venv` from `uv.lock`):

   ```bash
   uv sync
   ```

   *Note: If you get an error related to Rust in the dependency installation then make sure Rust is installed and in your `PATH`, instructions: https://rustup.rs*

3. Copy the secrets template file and fill in your OpenAI key and your GitHub user token:

   ```bash
   cp pr_agent/settings/.secrets_template.toml pr_agent/settings/.secrets.toml
   chmod 600 pr_agent/settings/.secrets.toml
   # Edit .secrets.toml file
   ```

4. Run the cli.py script:

   ```bash
   uv run pr-agent --pr_url <pr_url> review
   uv run pr-agent --pr_url <pr_url> ask "<your question>"
   uv run pr-agent --pr_url <pr_url> describe
   uv run pr-agent --pr_url <pr_url> improve
   uv run pr-agent --pr_url <pr_url> add_docs
   uv run pr-agent --pr_url <pr_url> generate_labels
   uv run pr-agent --issue_url <issue_url> similar_issue
   ...
   ```

   *Note: the `similar_issue` tool needs extra dependencies that a bare `uv sync` does not install. Install them with `uv sync --group similar-issue` before running it.*

[Optional] Add the pr_agent folder to your PYTHONPATH

```bash
export PYTHONPATH=$PYTHONPATH:<PATH to pr_agent folder>
```

### docs/docs/tools/index.md

---
title: "Tools"
sidebar_position: 1
---

Each PR-Agent tool has a dedicated page that explains its behavior and usage:

| Tool | Description |
|------|-------------|
| **[PR Description (`/describe`)](./describe.md)** | Generate a PR title, type, summary, code walkthrough and labels. |
| **[PR Review (`/review`)](./review.md)** | Generate a PR review with feedback on possible issues, security concerns, tests and review effort. |
| **[Code Suggestions (`/improve`)](./improve.mdx)** | Generate actionable code suggestions for improving the PR. |
| **[Question Answering (`/ask ...`)](./ask.md)** | Answering free-text questions about the PR, or on specific code lines |
| **[Add Documentation (`/add_docs`)](./add_docs.md)** | Generate documentation for code components that are missing it |
| **[Generate Labels (`/generate_labels`)](./generate_labels.md)** | Generate custom labels for the PR based on the code changes |
| **[Similar Issues (`/similar_issue`)](./similar_issues.md)** | Find similar issues in the repository based on the current issue |
| **[Help (`/help`)](./help.md)** | Provides a list of all the available tools |
| **[Help Docs (`/help_docs`)](./help_docs.md)** | Answer a free-text question based on a git documentation folder |
| **[Update Changelog (`/update_changelog`)](./update_changelog.md)** | Automatically updating the CHANGELOG.md file with the PR changes |

## Usage examples

Each tool can be triggered in two ways:

- **As a comment** — write the command (e.g. `/review`) as a comment, and PR-Agent replies. Most tools are commented on a PR; issue-scoped tools such as `similar_issue` are commented on an issue.
- **From the [CLI](../usage-guide/automations_and_usage.md#local-repo-cli)** — run `python -m pr_agent.cli --pr_url=<PR_URL> <tool>`. Issue-scoped tools take `--issue_url=<ISSUE_URL>` instead of `--pr_url`. The module form works only from an environment where the `pr_agent` package is importable (for example, the venv created by `uv sync`). If `pr-agent` is on your `PATH`, run it directly.

Both accept the same tool arguments and [configuration overrides](../usage-guide/configuration_options.md).

| Tool                                     | Comment                          | CLI                                                             |
|------------------------------------------|----------------------------------|----------------------------------------------------------------|
| [Describe](./describe.md)                | `/describe`                      | `python -m pr_agent.cli --pr_url=<PR_URL> describe`             |
| [Review](./review.md)                    | `/review`                        | `python -m pr_agent.cli --pr_url=<PR_URL> review`              |
| [Improve](./improve.mdx)                  | `/improve`                       | `python -m pr_agent.cli --pr_url=<PR_URL> improve`             |
| [Ask](./ask.md)                          | `/ask "How does X work?"`        | `python -m pr_agent.cli --pr_url=<PR_URL> ask "How does X work?"` |
| [Add Docs](./add_docs.md)                | `/add_docs`                      | `python -m pr_agent.cli --pr_url=<PR_URL> add_docs`           |
| [Generate Labels](./generate_labels.md)  | `/generate_labels`               | `python -m pr_agent.cli --pr_url=<PR_URL> generate_labels`     |
| [Similar Issues](./similar_issues.md)    | `/similar_issue`                 | `python -m pr_agent.cli --issue_url=<ISSUE_URL> similar_issue` |
| [Help](./help.md)                        | `/help`                          | `python -m pr_agent.cli --pr_url=<PR_URL> help`                |
| [Update Changelog](./update_changelog.md)| `/update_changelog`              | `python -m pr_agent.cli --pr_url=<PR_URL> update_changelog`    |

`/help_docs` is temporarily disabled (see [#2445](https://github.com/The-PR-Agent/pr-agent/issues/2445)) and is therefore omitted from the table above.

For screenshots, arguments, and a walkthrough of a typical use case, see the **Example usage** section on each tool's page linked above.

### docs/docs/core-abilities/index.md

---
title: "Core Abilities"
sidebar_position: 1
---

PR-Agent utilizes a variety of core abilities to provide a comprehensive and efficient code review experience. These abilities include:

- [Agent skills](./agent_skills.md)
- [Compression strategy](./compression_strategy.md)
- [Dynamic context](./dynamic_context.md)
- [Fetching ticket context](./fetching_ticket_context.md)
- [Local and global metadata](./metadata.md)
- [Self-reflection](./self_reflection.md)

## Blogs

Here are some additional technical blogs from Qodo, that delve deeper into the core capabilities and features of Large Language Models (LLMs) when applied to coding tasks.
These resources provide more comprehensive insights into leveraging LLMs for software development.

### Code Generation and LLMs

- [Effective AI code suggestions: less is more](https://www.qodo.ai/blog/effective-code-suggestions-llms-less-is-more/)
- [State-of-the-art Code Generation with AlphaCodium – From Prompt Engineering to Flow Engineering](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/)
- [RAG for a Codebase with 10k Repos](https://www.qodo.ai/blog/rag-for-large-scale-code-repos/)

### Development Processes

- [Understanding the Challenges and Pain Points of the Pull Request Cycle](https://www.qodo.ai/blog/understanding-the-challenges-and-pain-points-of-the-pull-request-cycle/)
- [Introduction to Code Coverage Testing](https://www.qodo.ai/blog/introduction-to-code-coverage-testing/)

### Cost Optimization

- [Reduce Your Costs by 30% When Using GPT for Python Code](https://www.qodo.ai/blog/reduce-your-costs-by-30-when-using-gpt-3-for-python-code/)

### docs/docs/core-abilities/agent_skills.md

---
title: "Agent Skills"
sidebar_position: 2
---

`Supported Tools: Review, Improve, Describe, Ask`

## Overview

Agent Skills let you distribute curated, reusable review guidance to PR-Agent using the [agent-skills (`SKILL.md`) format](https://github.com/The-PR-Agent/pr-agent/issues/2384). A skill is a directory containing a `SKILL.md` file with YAML frontmatter (`name` + `description`) followed by a markdown body:

```markdown
---
name: terraform-standards
description: Use when reviewing Terraform code — checks state safety and risky deletions.
---

# Terraform Review Guidance

- Flag any resource deletion that is not explicitly called out in the PR description.
- Require `prevent_destroy` on stateful resources.
- ...
```

When enabled, PR-Agent discovers every `SKILL.md` under the configured paths, parses it, and injects the skill's `name`, `description`, and body into the `/review`, `/improve`, `/describe`, and `/ask` prompts (including questions on a specific line) alongside `extra_instructions`. The model applies the guidance it judges relevant to the PR or question, using each skill's `description` as the signal for when the skill applies.

The value proposition is **org-wide, host-level skill libraries**: install one curated set of skills on your PR-Agent deployment and reuse it across many repositories, without checking guidance into each repo.

## Configuration

Skills are **disabled by default** and configured in `configuration.toml` (or any host-level config source):

```toml
[skills]
enabled = false
paths = []                # directories scanned recursively for "*/SKILL.md"; supports ~ and $VAR
max_skills_tokens = 8000  # token budget for the combined skills block
```

- `enabled` — turn the feature on.
- `paths` — a list of directories (scanned recursively for `*/SKILL.md`) or direct paths to a `SKILL.md` file. `~` and `$VAR`/`${VAR}` are expanded. A plain string is read as a single path, with a warning that it should be a list.
- `max_skills_tokens` — caps the combined size of the injected skills block. Skills past the cap are dropped from the end with a warning; if the first skill alone exceeds the budget it is clipped and marked `[truncated]`.

:::warning[`skills.paths` is host-level only]
`skills.paths` **cannot be set from a repository's `.pr_agent.toml`** and is configurable only where the deployment is administered. Because it reads files from the PR-Agent host's filesystem, allowing a repository to set it would let a malicious repo point PR-Agent at sensitive host files (e.g. `~/.ssh/*`) and exfiltrate their contents into the model prompt. A repo-supplied `skills.paths` is ignored with a warning.

A repository *may* set the safe per-repo preferences `skills.enabled` and `skills.max_skills_tokens` in its own `.pr_agent.toml` — e.g. to opt in to (or size) the host's admin-curated skill library for that repo. It can never redirect the filesystem scan.
:::

## Bundled resources

The agent-skills standard supports bundled files alongside `SKILL.md`. PR-Agent inlines the **text** ones:

- All `*.md` files in the skill directory tree (including a `references/` subdirectory) are appended after the `SKILL.md` body. Individual resource files larger than 256&nbsp;KB are skipped with a warning.
- `scripts/` and `assets/` subdirectories are **skipped**: PR-Agent runs single-shot model calls with no tool-use loop, so it cannot execute scripts or load binary assets on demand.
- A nested directory that contains its own `SKILL.md` is treated as a separate skill and not inlined into its parent.

In short, PR-Agent supports **text-only** agent skills.

## Limitations

PR-Agent dispatches single-shot model calls, so the agent-skills standard's *progressive disclosure* model (the model reads `SKILL.md` only after selecting it by `description`, and reads `references/*.md` only on demand) is not implementable on the current architecture — an architecture change to support this is planned for the future. Until then, every enabled skill's text is loaded into every PR's prompt, bounded by `max_skills_tokens`. Skills that depend on script execution or binary assets will not work.

### docs/docs/core-abilities/compression_strategy.md

---
title: "Compression Strategy"
sidebar_position: 3
---

`Supported Git Platforms: GitHub, GitLab, Bitbucket, Azure DevOps, Gitea`


## Overview

There are two scenarios:

1. The PR is small enough to fit in a single prompt (including system and user prompt)
2. The PR is too large to fit in a single prompt (including system and user prompt)

For both scenarios, we first use the following strategy

### Repo language prioritization strategy

We prioritize the languages of the repo based on the following criteria:

1. Exclude binary files and non code files (e.g. images, pdfs, etc)
2. Given the main languages used in the repo
3. We sort the PR files by the most common languages in the repo (in descending order):
   * ```[[file.py, file2.py],[file3.js, file4.jsx],[readme.md]]```

### Small PR

In this case, we can fit the entire PR in a single prompt:

1. Exclude binary files and non code files (e.g. images, pdfs, etc)
2. We Expand the surrounding context of each patch to 3 lines above and below the patch

### Large PR

#### Motivation

Pull Requests can be very long and contain a lot of information with varying degree of relevance to the pr-agent.
We want to be able to pack as much information as possible in a single LMM prompt, while keeping the information relevant to the pr-agent.

#### Compression strategy

We prioritize additions over deletions:

* Combine all deleted files into a single list (`deleted files`)
* File patches are a list of hunks, remove all hunks of type deletion-only from the hunks in the file patch

#### Adaptive and token-aware file patch fitting

We use [tiktoken](https://github.com/openai/tiktoken) to tokenize the patches after the modifications described above, and we use the following strategy to fit the patches into the prompt:

1. Within each language we sort the files by the number of tokens in the file (in descending order):
    * ```[[file2.py, file.py],[file4.jsx, file3.js],[readme.md]]```
2. Iterate through the patches in the order described above
3. Add the patches to the prompt until the prompt reaches a certain buffer from the max token length
4. If there are still patches left, add the remaining patches as a list called `other modified files` to the prompt until the prompt reaches the max token length (hard stop), skip the rest of the patches.
5. If we haven't reached the max token length, add the `deleted files` to the prompt until the prompt reaches the max token length (hard stop), skip the rest of the patches.

#### Example

<img src="/img/git_patch_logic.png" alt="Core Abilities" width="768" />

### docs/docs/core-abilities/dynamic_context.md

---
title: "Dynamic Context"
sidebar_position: 4
---

`Supported Git Platforms: GitHub, GitLab, Bitbucket, Azure DevOps, Gitea`

PR-Agent uses an **asymmetric and dynamic context strategy** to improve AI analysis of code changes in pull requests.
It provides more context before changes than after, and dynamically adjusts the context based on code structure (e.g., enclosing functions or classes).
This approach balances providing sufficient context for accurate analysis, while avoiding needle-in-the-haystack information overload that could degrade AI performance or exceed token limits.

## Introduction

Pull request code changes are retrieved in a unified diff format, showing three lines of context before and after each modified section, with additions marked by '+' and deletions by '-'.

```diff
@@ -12,5 +12,5 @@ def func1():
 code line that already existed in the file...
 code line that already existed in the file...
 code line that already existed in the file....
-code line that was removed in the PR
+new code line added in the PR
 code line that already existed in the file...
 code line that already existed in the file...
 code line that already existed in the file...

@@ -26,2 +26,4 @@ def func2():
...
```

This unified diff format can be challenging for AI models to interpret accurately, as it provides limited context for understanding the full scope of code changes.
The presentation of code using '+', '-', and ' ' symbols to indicate additions, deletions, and unchanged lines respectively also differs from the standard code formatting typically used to train AI models.

## Challenges of expanding the context window

While expanding the context window is technically feasible, it presents a more fundamental trade-off:

Pros:

- Enhanced context allows the model to better comprehend and localize the code changes, results (potentially) in more precise analysis and suggestions. Without enough context, the model may struggle to understand the code changes and provide relevant feedback.

Cons:

- Excessive context may overwhelm the model with extraneous information, creating a "needle in a haystack" scenario where focusing on the relevant details (the code that actually changed) becomes challenging.
LLM quality is known to degrade when the context gets larger.
Pull requests often encompass multiple changes across many files, potentially spanning hundreds of lines of modified code. This complexity presents a genuine risk of overwhelming the model with excessive context.

- Increased context expands the token count, increasing processing time and cost, and may prevent the model from processing the entire pull request in a single pass.

## Asymmetric and dynamic context

To address these challenges, PR-Agent employs an **asymmetric** and **dynamic** context strategy, providing the model with more focused and relevant context information for each code change.

**Asymmetric:**

We start by recognizing that the context preceding a code change is typically more crucial for understanding the modification than the context following it.
Consequently, PR-Agent implements an asymmetric context policy, decoupling the context window into two distinct segments: one for the code before the change and another for the code after.

By independently adjusting each context window, PR-Agent can supply the model with a more tailored and pertinent context for individual code changes.

**Dynamic:**

We also employ a "dynamic" context strategy.
We start by recognizing that the optimal context for a code change often corresponds to its enclosing code component (e.g., function, class), rather than a fixed number of lines.
Consequently, we dynamically adjust the context window based on the code's structure, ensuring the model receives the most pertinent information for each modification.

To prevent overwhelming the model with excessive context, we impose a limit on the number of lines searched when identifying the enclosing component.
This balance allows for comprehensive understanding while maintaining efficiency and limiting context token usage.

## Appendix - relevant configuration options

```toml
[config]
patch_extension_skip_types =[".md",".txt"]  # Skip files with these extensions when trying to extend the context
allow_dynamic_context=true                  # Allow dynamic context extension
max_extra_lines_before_dynamic_context = 8  # will try to include up to X extra lines before the hunk in the patch, until we reach an enclosing function or class
patch_extra_lines_before = 3                # Number of extra lines (+3 default ones) to include before each hunk in the patch
patch_extra_lines_after = 1                 # Number of extra lines (+3 default ones) to include after each hunk in the patch
```

### docs/docs/core-abilities/metadata.md

---
title: "Local and global metadata injection with multi-stage analysis"
sidebar_position: 6
---

`Supported Git Platforms: GitHub, GitLab, Bitbucket, Azure DevOps, Gitea`

1. PR-Agent initially retrieves for each PR the following data:

   - PR title and branch name
   - PR original description
   - Commit messages history
   - PR diff patches, in [hunk diff](https://loicpefferkorn.net/2014/02/diff-files-what-are-hunks-and-how-to-extract-them/) format
   - The entire content of the files that were modified in the PR

   :::note[Tip: Organization-level metadata]
   In addition to the inputs above, PR-Agent can incorporate supplementary preferences provided by the user, like [`extra_instructions` and `organization best practices`](../tools/improve.mdx#extra-instructions-and-best-practices). This information can be used to enhance the PR analysis.
   :::

2. By default, the first command that PR-Agent executes is [`describe`](../tools/describe.md), which generates three types of outputs:

   - PR Type (e.g. bug fix, feature, refactor, etc)
   - PR Description - a bullet point summary of the PR
   - Changes walkthrough - for each modified file, provide a one-line summary followed by a detailed bullet point list of the changes.

   These AI-generated outputs are now considered as part of the PR metadata, and can be used in subsequent commands like `review` and `improve`.
   This effectively enables multi-stage chain-of-thought analysis, without doing any additional API calls which will cost time and money.

   For example, when generating code suggestions for different files, PR-Agent can inject the AI-generated ["Changes walkthrough"](https://github.com/the-pr-agent/pr-agent/pull/1202#issue-2511546839) file summary in the prompt:

   ```diff
   ## File: 'src/file1.py'
   ### AI-generated file summary:
   - edited function `func1` that does X
   - Removed function `func2` that was not used
   - ....

   @@ ... @@ def func1():
   __new hunk__
   11  unchanged code line0
   12  unchanged code line1
   13 +new code line2 added
   14  unchanged code line3
   __old hunk__
    unchanged code line0
    unchanged code line1
   -old code line2 removed
    unchanged code line3

   @@ ... @@ def func2():
   __new hunk__
   ...
   __old hunk__
   ...
   ```

3. The entire PR files that were retrieved are also used to expand and enhance the PR context (see [Dynamic Context](./dynamic_context.md)).

4. All the metadata described above represents several level of cumulative analysis - ranging from hunk level, to file level, to PR level, to organization level.
   This comprehensive approach enables PR-Agent AI models to generate more precise and contextually relevant suggestions and feedback.

### docs/docs/core-abilities/self_reflection.md

---
title: "Self-Reflection"
sidebar_position: 7
---

`Supported Git Platforms: GitHub, GitLab, Bitbucket, Azure DevOps, Gitea`

PR-Agent implements a **self-reflection** process where the AI model reflects, scores, and re-ranks its own suggestions, eliminating irrelevant or incorrect ones.
This approach improves the quality and relevance of suggestions, saving users time and enhancing their experience.
Configuration options allow users to set a score threshold for further filtering out suggestions.

## Introduction - Efficient Review with Hierarchical Presentation

Given that not all generated code suggestions will be relevant, it is crucial to enable users to review them in a fast and efficient way, allowing quick identification and filtering of non-applicable ones.

To achieve this goal, PR-Agent offers a dedicated hierarchical structure when presenting suggestions to users:

- A "category" section groups suggestions by their category, allowing users to quickly dismiss irrelevant suggestions.
- Each suggestion is first described by a one-line summary, which can be expanded to a full description by clicking on a collapsible.
- Upon expanding a suggestion, the user receives a more comprehensive description, and a code snippet demonstrating the recommendation.

:::note[Fast Review]
This hierarchical structure is designed to facilitate rapid review of each suggestion, with users spending an average of ~5-10 seconds per item.
:::

## Self-reflection and Re-ranking

The AI model is initially tasked with generating suggestions, and outputting them in order of importance.
However, in practice we observe that models often struggle to simultaneously generate high-quality code suggestions and rank them well in a single pass.
Furthermore, the initial set of generated suggestions sometimes contains easily identifiable errors.

To address these issues, we implemented a "self-reflection" process that refines suggestion ranking and eliminates irrelevant or incorrect proposals.
This process consists of the following steps:

1. Presenting the generated suggestions to the model in a follow-up call.
2. Instructing the model to score each suggestion on a scale of 0-10 and provide a rationale for the assigned score.
3. Utilizing these scores to re-rank the suggestions and filter out incorrect ones (with a score of 0).
4. Optionally, filtering out all suggestions below a user-defined score threshold.

Note that presenting all generated suggestions simultaneously provides the model with a comprehensive context, enabling it to make more informed decisions compared to evaluating each suggestion individually.

To conclude, the self-reflection process enables PR-Agent to prioritize suggestions based on their importance, eliminate inaccurate or irrelevant proposals, and optionally exclude suggestions that fall below a specified threshold of significance.
This results in a more refined and valuable set of suggestions for the user, saving time and improving the overall experience.

## Example Results

<img src="/img/self_reflection1.png" alt="self_reflection" width="768" />
<img src="/img/self_reflection2.png" alt="self_reflection" width="768" />

## Appendix - Relevant Configuration Options

```toml
[pr_code_suggestions]
suggestions_score_threshold = 0 # Filter out suggestions with a score below this threshold (0-10)
```

### docs/docs/usage-guide/introduction.md

---
title: "Introduction"
sidebar_position: 2
---

After [installation](../installation/index.md), there are three basic ways to invoke PR-Agent:

1. Locally running a CLI command
2. Online usage - by <a href="https://github.com/the-pr-agent/pr-agent/pull/229#issuecomment-1695021901" target="_blank" rel="noopener noreferrer">commenting</a> on a PR
3. Enabling PR-Agent tools to run automatically when a new PR is opened

Specifically, CLI commands can be issued by invoking a pre-built [docker image](../installation/locally.md#using-docker-image), or by invoking a [locally cloned repo](../installation/locally.md#run-from-source).

For online usage, you will need to setup either a [GitHub App](../installation/github.md#run-as-a-github-app) or a [GitHub Action](../installation/github.md#run-as-a-github-action) (GitHub), a [GitLab webhook](../installation/gitlab.md#run-a-gitlab-webhook-server) (GitLab), or a [BitBucket App](../installation/bitbucket.md) (BitBucket).
These platforms also enable to run PR-Agent specific tools automatically when a new PR is opened, or on each push to a branch.

### docs/docs/usage-guide/extending_pr_agent.md

---
title: "Extending PR-Agent"
sidebar_position: 9
---

Contributors extending a model, git provider, or tool start here. To only change
the model, use [Changing a Model](./changing_a_model.md).

## Adding a model

Tool calls go through LiteLLM (`pr_agent/algo/ai_handlers/litellm_ai_handler.py`), the default handler. Most models need only configuration:

```toml
[config]
model="<model-name>"
fallback_models=["<fallback-model-name>"]
```

Set these under `[config]` in `pr_agent/settings/configuration.toml`.
Keep model names in configuration, not in tool code.

Models that behave differently are registered in `pr_agent/algo/__init__.py`:
`CLAUDE_EXTENDED_THINKING_MODELS` for Claude models that
take extended thinking. For Claude models with provider-prefixed aliases
(bare, `anthropic/`, `vertex_ai/`, `bedrock/`), declare the canonical family
in `_CLAUDE_MODEL_FAMILIES` to expand them across registries automatically.
Other models can be added directly to the matching list.

Temperature support is decided at runtime by probing
`litellm.get_supported_openai_params()` for each model (see
`_litellm_supports_temperature` in `pr_agent/algo/ai_handlers/litellm_ai_handler.py`).
Models that must never receive the temperature parameter are listed in
`config.no_temperature_models` in `configuration.toml`; adaptive-thinking Claude
models (Opus 4.7/4.8 and Opus/Sonnet/Fable 5) never receive it.

Context windows are registered in `MAX_TOKENS` in `pr_agent/algo/__init__.py`:
Claude model families declared in `_CLAUDE_MODEL_FAMILIES` populate their
aliases automatically. For other models, add the model name and its
context-window token count to `MAX_TOKENS`, or set `config.custom_model_max_tokens`
in `configuration.toml`. Without either, `get_max_tokens()` raises.

Verify with `PYTHONPATH=. uv run pytest tests/unittest`.

## Adding a git provider

Implement a `GitProvider` subclass and register it:

1. Create `pr_agent/git_providers/<name>_provider.py`, extending the interface in `pr_agent/git_providers/git_provider.py` (`gitlab_provider.py` is the reference).
2. Add the built-in provider to `_BUILTIN_GIT_PROVIDERS` in `pr_agent/git_providers/__init__.py` as a `(module_path, class_name)` pair. Built-ins are imported lazily when selected. Keys already used: `github`, `gitlab`, `bitbucket`, `bitbucket_server`, `azure`, `codecommit`, `local`, `gerrit`, `gitea`, `plain-diff`.
3. Select it via `[config]` → `git_provider="<name>"` in `pr_agent/settings/configuration.toml`.
4. Add `docs/docs/installation/<name>.md` (see [`gitlab.md`](../installation/gitlab.md)) and register it under `Installation` in `docs/sidebars.js`.
5. Select provider-dependent behavior with capability checks like `provider.is_supported("feature")` rather than provider-type checks.
6. Add unit tests under `tests/unittest/test_<name>_provider.py` (see `test_bitbucket_provider.py`) and list the required env vars in `pr_agent/settings/.secrets_template.toml`.

### Registering a provider from another package

A provider does not have to live in this repository. Call `register_git_provider` from your own package before PR-Agent resolves the provider, for example from the module that starts your server or wraps the CLI:

```python
from pr_agent.git_providers import register_git_provider

from my_package.forge_provider import ForgeProvider

register_git_provider("forge", ForgeProvider)
```

Then select it with `git_provider="forge"` under `[config]`. The class must extend `GitProvider`. Registering the same class twice is a no-op, and registering a different class under an id that is already taken raises, so a package cannot silently replace a built-in provider.

## Adding a tool

1. Implement the tool class in `pr_agent/tools/pr_<name>.py` with an `async def run(self)` entry point (see `pr_reviewer.py`).
2. Add a `[pr_<tool>]` section in `pr_agent/settings/configuration.toml` for the option keys the tool reads (`[pr_reviewer]` is the pattern to follow).
3. Add a prompt TOML under `pr_agent/settings/` and register it in the `settings_files=[...]` list in `pr_agent/config_loader.py` — it is not loaded otherwise.
4. Match the TOML section name to the settings key the tool reads: `[pr_review_prompt]` in `pr_reviewer_prompts.toml` ↔ `get_settings().pr_review_prompt` in `pr_reviewer.py`.
5. Register the tool in `command2class` in `pr_agent/agent/pr_agent.py` under a command name, e.g. `"my_tool": PRMyTool`. Then add it to the hardcoded help surfaces, or it will not show up in `/help`: `pr_agent/tools/pr_help_message.py`, `pr_agent/servers/help.py`, and the command list in `pr_agent/cli.py`.
6. Add a row to the tool list in `docs/docs/tools/index.md`, a page `docs/docs/tools/<name>.md` (see [`review.md`](../tools/review.md)), and register the page under `Tools` in `docs/sidebars.js`.
7. Add tests under `tests/unittest/` and verify with `PYTHONPATH=. uv run pytest tests/unittest`.

### AGENTS.md

# Repository Guidelines

This file is the shared source of repository guidance for coding agents. Tool-specific instruction files should import it instead of repeating repository-wide rules.

## Dos and Don’ts

- **Do** match the interpreter requirement declared in `pyproject.toml` (Python ≥ 3.12) and install dependencies with `uv sync` (runtime + dev, from `uv.lock`) before running tools.
- **Do** run tests with `PYTHONPATH=.` set to keep imports functional (for example `PYTHONPATH=. uv run pytest tests/unittest/test_output_models.py -q`).
- **Do** adjust configuration through `.pr_agent.toml` or files under `pr_agent/settings/` instead of hard-coding values.
- **Don’t** commit secrets or access tokens; rely on environment variables as shown in the health and e2e tests.
- **Don’t** reformat or reorder files globally; match existing 120-character lines, import ordering, and docstring style.
- **Don’t** delete or rename configuration, prompt, or workflow files without maintainer approval.

## Project Structure and Module Organization

PR-Agent automates AI-assisted reviews for pull requests across multiple git providers.

- `pr_agent/agent/` orchestrates commands (`review`, `describe`, `improve`, etc.) via `pr_agent/agent/pr_agent.py`.
- `pr_agent/tools/` implements individual capabilities such as reviewers, code suggestions, docs updates, and label generation.
- `pr_agent/algo/` contains shared algorithms, model handlers, prompt/token handling, types, and utilities.
- `pr_agent/git_providers/` handles integrations with GitHub, GitLab, Bitbucket (cloud and server), Azure DevOps, Gitea, Gerrit, CodeCommit, local checkouts, and plain diffs; `pr_agent/identity_providers/` handles identity and `pr_agent/secret_providers/` handles secrets.
- `pr_agent/settings/` stores Dynaconf defaults (prompts, configuration templates, ignore lists) respected at runtime; `.pr_agent.toml` overrides repository-level behavior.
- `pr_agent/servers/` contains webhook and service entrypoints.
- `tests/unittest/`, `tests/e2e_tests/`, and `tests/health_test/` contain pytest-based unit, end-to-end, and smoke checks.
- `docs/` holds the Docusaurus site (`docs/docusaurus.config.js` and `docs/sidebars.js` plus content under `docs/docs/`); theme overrides live in `docs/src/` and static assets in `docs/static/`.
- `.github/workflows/` defines CI pipelines for unit tests, coverage, docs deployment, pre-commit, and PR-agent self-review.
- `docker/` provides build targets for services (`github_app`, `gitlab_webhook`, etc.) and the `test` stage used in CI; the root `Dockerfile.github_action_dockerhub` only wraps the published `github_action` image for `action.yaml`.

## Architecture and Request Flow

PR-Agent is a CLI/server that runs AI-powered tools (`/review`, `/describe`, `/improve`, `/ask`, etc.) against pull requests on supported git providers or local input. The main dispatch flow is `pr_agent/agent/pr_agent.py` → `command2class` → a tool class under `pr_agent/tools/`.

A tool generally obtains the appropriate git provider, gathers pull-request context, prepares prompt variables and templates, calls the configured model handler, and publishes or stores the result through the provider.

### Prompt Building

Prompt-driven tools generally construct a `self.vars` dictionary and pass it with the system/user prompt strings to `TokenHandler`. Prompt rendering uses Jinja2 with `StrictUndefined`, so variables referenced by a template should be present in the corresponding vars dictionary; define optional values explicitly and guard optional sections with Jinja conditionals.

System/user prompt strings live as TOML files under `pr_agent/settings/` and are loaded into `global_settings` by `pr_agent/config_loader.py`. Tool and prompt names normally correspond, for example:

- `pr_reviewer.py` ↔ `pr_reviewer_prompts.toml`
- `pr_description.py` ↔ `pr_description_prompts.toml`
- `pr_code_suggestions.py` ↔ `code_suggestions/pr_code_suggestions_prompts.toml` (plus its related variants)

New prompt files must also be registered in the `settings_files=[...]` list in `pr_agent/config_loader.py` or they will not be loaded into `global_settings`.

### Settings and Runtime Configuration

Use `get_settings()` from `pr_agent/config_loader.py` as the shared settings accessor. It returns the request-scoped Dynaconf object from `starlette_context` when one is present, otherwise the module-level `global_settings` object.

Defaults live in `pr_agent/settings/configuration.toml`. Per-repository overrides come from the repository's `.pr_agent.toml` and are applied by `pr_agent/git_providers/utils.py::apply_repo_settings` before command dispatch. When introducing a configuration section, add its defaults and comments to `configuration.toml` and keep related prompt/config changes synchronized.

`docs/docs/usage-guide/configuration_reference.md` is generated from `configuration.toml` by `python scripts/generate_config_reference.py [output_path]` (run from the repository root), and its header says not to edit it by hand. Write the output to a temporary path and diff it against the page before replacing anything. `tests/unittest/test_config_reference.py` checks that the page matches the generator output, lists exactly the active keys, and asserts a hard-coded active-key count, so update that count when adding or removing keys.

Repository overrides are filtered by `pr_agent/config_security.py`; host-only keys must be supplied through host configuration. Configuration file merges preserve other fields in a section but replace overlapping list/dict values rather than appending or deep-merging; environment variables take precedence.

Sensitive values should stay in environment variables or the gitignored `.secrets.toml` files under `pr_agent/settings/` and `pr_agent/settings_prod/`. `apply_secrets_manager_config()` optionally loads values from AWS Secrets Manager.

### Git Providers

`pr_agent/git_providers/` contains provider implementations that share the `GitProvider` interface in `pr_agent/git_providers/git_provider.py`. Provider-dependent behavior should be selected through capability checks such as `provider.is_supported("feature")` rather than concrete provider-type checks, because individual providers can stub or override capabilities. Some output is gated this way too: semantic file types and several other `/describe` sections are only emitted where `gfm_markdown` is supported.

### Servers and Entrypoints

`pr_agent/servers/` hosts webhook and service entrypoints that translate provider events into `PRAgent.handle_request(...)` calls. The CLI entrypoint is `pr_agent/cli.py`, registered as the `pr-agent` console script.

## Build, Test, and Development Commands

- Install dependencies (runtime + dev) into a project virtualenv from the lockfile with `uv sync` using a uv version that satisfies `tool.uv.required-version` in `pyproject.toml`; `uv run` auto-syncs before each command.
- Run a single unit test (verified): `PYTHONPATH=. uv run pytest tests/unittest/test_output_models.py -q`.
- Run the full unit suite: `PYTHONPATH=. uv run pytest tests/unittest -v`.
- CI also runs `uv run pytest -q tests/packaging/test_help_docs_package.py`; it is outside `testpaths`, so the unit suite does not cover it. The distribution-contract test asserts the exact uv version given by the lower bound of `tool.uv.required-version` in `pyproject.toml`; newer uv versions can fail that assertion.
- Execute the CLI locally once dependencies and API keys are available: `uv run pr-agent --pr_url <https://host/org/repo/pull/123> review`.
- Build the test Docker target mirror of CI when containerizing: `docker build -f docker/Dockerfile --target test .` (loads dev dependencies and copies `tests/`).
- Build the documentation the same way CI does (Node.js 22): `npm ci` then `npm run build` from `docs/`; `npm start` serves a live preview. After building, run `python3 scripts/check_docs_urls.py` from the repository root to check `docs/build` as CI does. The `docs-ci` workflow publishes `docs/build` to GitHub Pages.

## Coding Style and Existing Tooling

Ruff is the single linting tool: `pyproject.toml` configures it and the pre-commit Ruff hook enforces it (Flake8 and the standalone isort hook have been removed).

- Keep Python lines within the 120-character limit declared in `pyproject.toml`.
- `pyproject.toml` configures Ruff rules `E`, `F`, `B`, `I`, `UP` and `FURB`. Within the files touched by the task, fix lint violations rather than adding ignore entries. Remove corresponding ignore entries only when they are no longer needed, and preserve intentional exceptions.
- Before committing, run `uv run ruff check --fix <paths>` on the Python files you touched and fix every issue it reports. Keep fixes mechanical (rename, remove unused imports, sort imports); do not alter program logic while cleaning up — if a lint fix would change behavior, surface it instead of applying it silently.
- `.pre-commit-config.yaml` is the source of truth for enabled pre-commit hooks. Run them on the files you touched with `uvx pre-commit run --files <paths>` and review the automatic edits so unrelated changes are not included. The pre-commit GitHub Actions workflow runs on pull requests, so the hooks are enforced in CI.
- No general-purpose Python formatter is currently enforced (`ruff format` is deliberately not adopted yet). Preserve the surrounding file's formatting and avoid unrelated rewrites or repository-wide formatting.
- Prefer double quotes for Python strings where consistent with the surrounding file.
- Match existing docstring and comment style—concise English comments using imperative phrasing only where necessary.
- Configuration files in `pr_agent/settings/` are TOML; preserve formatting, section order, and comments when editing prompts or defaults.
- Markdown in `docs/` uses Docusaurus conventions: every page starts with YAML front matter (`title`, `sidebar_position`), admonitions use `:::note` fences, collapsible sections use `<details>`, and images live in `docs/static/img/` referenced as `/img/<file>`. Pages stay `.md` (CommonMark) unless they need a JSX component, in which case they are `.mdx`. Register every new page in `docs/sidebars.js`.

## Testing Guidelines

- Pytest is the standard framework; keep new tests under the closest matching directory (`tests/unittest/` for unit logic, `tests/e2e_tests/` for integration flows, `tests/health_test/` for smoke coverage).
- Pytest configuration lives in `pyproject.toml`, including `asyncio_mode = "auto"` and `testpaths = ["tests/unittest"]`. The Docker test image keeps `pyproject.toml` at `/app` (uv installs from it), so CI inherits these settings as well. Plain `PYTHONPATH=. uv run pytest` therefore defaults to the unit suite; invoke end-to-end tests explicitly.
- Prefer focused unit tests that isolate helpers in `pr_agent/algo/`, `pr_agent/tools/`, or provider adapters; use parameterized tests where existing files already do so.
- Set `PYTHONPATH=.` when invoking pytest from the repository root to avoid import errors.
- End-to-end suites require provider credentials and may take several minutes; `TOKEN_GITHUB`, `TOKEN_GITLAB`, `BITBUCKET_USERNAME`, and `BITBUCKET_PASSWORD` are CI secret names, not runtime environment variables (see the mappings in `.github/workflows/e2e_tests.yaml`). These tests create remote branches and pull/merge requests and expect deployed apps/webhooks to process them; run them only when credentials and sandboxes are configured.
- `tests/health_test/main.py` is a manual script for `/describe`, `/review`, and `/improve`; it asserts artifact headers inline, not checked-in artifact files. Update those inline assertions if prompts change meaningfully. CI provider smoke runs `tests/health_test/test_github_smoke.py` instead (`/describe` only, model stubbed, `GITHUB.USER_TOKEN`).

## Review Checklist

- A setting can arrive as a TOML list, a plain string, or an environment value that Dynaconf parses as TOML (`SECTION__KEY=123` arrives as an int). Code that reads it handles each form.
- A fix in one git provider, AI handler or server usually applies to its siblings. Check the same logic in the others and fix them or name them in the PR.
- New or changed regexes run in linear time: no nested or adjacent unbounded quantifiers that can match the same characters, and no unbounded leading quantifier in an unanchored search. User-supplied patterns and globs get a length cap before they are compiled or translated.
- Docs and config comments describe what the branch does. A PR that changes a default or a setting's behavior updates the `configuration.toml` comment and the docs page that state it, and none documents behavior from another PR.

## Commit and Pull Request Guidelines

- Follow `CONTRIBUTING.md`: keep changes focused, add or update tests, and use Conventional Commit-style messages (e.g., `fix: handle missing repo settings gracefully`).
- Target branch names follow `feature/<name>` or `fix/<issue>` patterns for substantial work.
- Reference related issues and update README or docs when user-facing behavior shifts.
- Before requesting review, run the relevant local checks above and make sure the corresponding CI workflows (`build-and-test`, `pre-commit`) pass; coverage is collected and uploaded by `build-and-test`, and `docs-ci` builds the documentation on every pull request that touches `docs/**` (publishing only on pushes to `main` and `add-docs-portal`). That build fails on broken links and anchors, and also runs `scripts/check_docs_urls.py` to confirm the documentation URLs hardcoded in `pr_agent/` and the README still resolve.
- Include screenshots or terminal captures when modifying user-visible output or documentation previews.

## Safety and Permissions

- Ask for confirmation before adding dependencies, renaming files, or changing workflow definitions; many consumers embed these paths and prompts.
- Stay within existing formatting and directory conventions—avoid mass refactors, re-sorting of prompts, or reformatting Markdown beyond the touched sections.
- You may read files, list directories, and run targeted lint/test/doc commands without prior approval; coordinate before launching full Docker builds or e2e suites that rely on external credentials.
- Never commit cached credentials, API keys, or coverage artifacts; CI already handles secrets through GitHub Actions.
- Treat prompt and configuration files as single sources of truth—keep related defaults and prompts under `pr_agent/settings/` synchronized when behavior changes. The root `.pr_agent.toml` is intended for this repository's hosted Qodo reviews, not as a mirror of the packaged defaults; some entries have no open-source implementation.

## Security and Configuration Tips

- Secrets should be supplied through environment variables (see usages in `tests/e2e_tests/test_github_app.py` and `tests/health_test/main.py`); do not persist them in code or configuration files.
- Adjust runtime behavior by overriding keys in `.pr_agent.toml` or by supplying repository-specific Dynaconf files; keep overrides minimal and documented inside the PR description.
- Review `SECURITY.md` before disclosing vulnerabilities and follow its contact instructions for responsible reporting.

## Top-level structure

- `.github/` — CI workflows (unit tests, coverage, docs deployment, pre-commit, PR-agent self-review). Boilerplate workflows directory; not fetched file-by-file.
- `.pr_agent.toml` — repository-level PR-Agent config override for this repo's own reviews.
- `AGENTS.md` — shared coding-agent guidance (Python ≥ 3.12, uv, module map, request flow). Full text in Docs.
- `CHANGELOG.md`, `RELEASE_NOTES.md` — release notes; latest GitHub release is v0.49.0.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` (MIT) — project policy files.
- `Dockerfile.github_action_dockerhub` — thin wrapper around the published `github_action` image for `action.yaml`.
- `action.yaml` — GitHub Action entry (`the-pr-agent/pr-agent`).
- `docker/` — `Dockerfile`, `Dockerfile.lambda`, and `mosaico/` build targets (`github_app`, `gitlab_webhook`, and similar service images; `test` stage used in CI).
- `docs/` — Docusaurus documentation site published toward docs.pr-agent.ai. Key pages fetched above.
- `github_action/` — `entrypoint.sh` for the GitHub Action container.
- `pr_agent/` — Python package.
  - `agent/` — command orchestration (`pr_agent.py` maps commands to tool classes; `request_policy.py`).
  - `algo/` — shared algorithms: `ai_handlers/` (LiteLLM handler), token budget/handler, patch processing, model routing, skills loader, review merge/output.
  - `cli.py`, `cli_pip.py` — CLI entrypoints (`pr-agent` console script).
  - `config_loader.py`, `config_security.py` — Dynaconf settings and host-only key filtering.
  - `git_providers/` — GitHub, GitLab, Bitbucket Cloud and Server, Azure DevOps, Gitea, Gerrit, CodeCommit, local checkout, plain diff.
  - `identity_providers/`, `secret_providers/` — identity and secrets (including optional AWS Secrets Manager).
  - `servers/` — webhook and service entrypoints (GitHub app, GitHub polling, GitHub/GitLab Lambda, GitLab webhook, Gitea, Bitbucket, Azure DevOps, Gerrit).
  - `settings/` — Dynaconf defaults and per-tool prompt TOML (`configuration.toml` plus tool prompt files).
  - `tools/` — one module per command: describe, review, improve/code suggestions, ask, line questions, add docs, generate labels, similar issue, help, help docs, update changelog, config, ticket compliance, progress comment.
  - `doctor.py`, `telemetry/`, `log/`, `mosaico/` — diagnostics, telemetry, logging, Mosaico server extra.
- `pr_compliance_checklist.yaml` — compliance checklist asset.
- `pyproject.toml`, `setup.py`, `uv.lock`, `MANIFEST.in`, `.python-version` — packaging (uv lockfile; Python ≥ 3.12 per AGENTS.md).
- `scripts/` — `check_docs_urls.py`, `generate_config_reference.py`, `set_pyproject_version.py`.
- `tests/` — `unittest/` (default pytest path), `e2e_tests/` (provider credentials), `health_test/` (smoke), `packaging/`.
- `uv.lock` — lockfile; not fetched (large).
