# agents-cli

## Fetch log
- Inbox URL: https://google.github.io/agents-cli/
- Final URL: https://google.github.io/agents-cli/
- Fetched: 2026-06-30
- Pages: 10
- Mode: standard

## Landing page — https://google.github.io/agents-cli/
agents-cli

CLI and skills for building agents on Google Cloud.

Get Started → View on GitHub

Works with your coding agent

Antigravity CLI Claude Code Codex & more

# install the cli + skills

$ uvx google-agents-cli setup

# now ask your coding agent to build

> an agent that triages incidents

## Docs — https://google.github.io/agents-cli/guide/getting-started/


## Getting Started — https://google.github.io/agents-cli/guide/getting-started/

# Getting Started

**Agents CLI in Agent Platform** is a CLI and skills package for building, evaluating, and deploying AI agents on Google Cloud. Agents are built with Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) — Agents CLI handles everything around it: scaffolding, evaluation, deployment, and observability.

It works two ways:

1. **With a coding agent** — install skills into Antigravity CLI, Claude Code, Codex, or others. Your coding agent uses them to make the right decisions at every step.
2. **Without a coding agent** — run CLI commands directly from your terminal. Every command works standalone.

Agents CLI bundles **7 skills** that give your coding agent deep knowledge across the full ADK lifecycle:

| Skill | What your coding agent learns |
|-------|-------------------------------|
| `google-agents-cli-workflow` | Development lifecycle, code preservation, model selection |
| `google-agents-cli-adk-code` | ADK Python API — agents, tools, orchestration, callbacks |
| `google-agents-cli-scaffold` | Project scaffolding — `create`, `enhance`, `upgrade` |
| `google-agents-cli-eval` | Evaluation lifecycle — datasets, metrics, generate/grade, compare, analyze, optimize |
| `google-agents-cli-deploy` | Deployment — Agent Runtime, Cloud Run, GKE, CI/CD |
| `google-agents-cli-publish` | Gemini Enterprise registration |
| `google-agents-cli-observability` | Cloud Trace, logging, third-party integrations |

---

## Prerequisites

**Required:** [Python 3.11+](https://www.python.org/downloads/), [uv](https://docs.astral.sh/uv/getting-started/installation/), [Node.js](https://nodejs.org/en/download) (for skills installation)

**Optional (for deployment):** [Google Cloud SDK](https://cloud.google.com/sdk/docs/install), [Terraform](https://developer.hashicorp.com/terraform/downloads)

---

## Install

```bash
uvx google-agents-cli setup
```

This installs the CLI and context-aware skills for your coding agent.

??? info "Alternative installation methods"
    **pipx:** `pipx install google-agents-cli && agents-cli setup`

    **venv + pip:** `pip install google-agents-cli && agents-cli setup`

    **Skills only:** `npx skills add google/agents-cli`

**Platform support:** macOS, Linux, and Windows (WSL 2). Native Windows is not officially supported.

---

## Authenticate

If you're already authenticated with `gcloud`, it just works — Agents CLI picks up your Application Default Credentials automatically.

Otherwise, the quickest option is a Gemini API key from [AI Studio](https://aistudio.google.com/apikey):

```bash
export GEMINI_API_KEY="your-key-here"
```

See [Authentication](authentication.md) for full details.

---

## Start Building with Your Coding Agent

=== "Antigravity CLI"

    1. **Open Antigravity CLI**

        Launch Antigravity from your IDE or terminal.

    2. **Verify skills are installed**

        Check that Agents CLI skills are available in your environment.

    3. **Ask it to build something**

        ```
        Build a support agent that answers questions from our docs
        ```

        Antigravity will use the installed skills to scaffold, build, and evaluate your agent.

=== "Claude Code"

    1. **Open Claude Code**

        ```bash
        claude
        ```

    2. **Verify skills are installed**

        ```
        /skills
        ```

        You should see `google-agents-cli-workflow` and other Agents CLI skills listed.

    3. **Ask it to build something**

        ```
        Build a support agent that answers questions from our docs
        ```

        Claude will use the installed skills to scaffold, build, and evaluate your agent.

=== "Codex"

    1. **Open Codex**

        ```bash
        codex
        ```

    2. **Verify skills are installed**

        Check that Agents CLI skills are available in your environment.

    3. **Ask it to build something**

        ```
        Build a support agent that answers questions from our docs
        ```

        Codex will use the installed skills to scaffold, build, and evaluate your agent.

=== "Any Other Agent"

    Agents CLI works with any coding agent that supports [skills](https://agentskills.io/what-are-skills).

    1. **Install skills**

        ```bash
        uvx google-agents-cli setup
        ```

    2. **Verify skills are visible**

        Check that your agent can see `google-agents-cli-workflow` and other Agents CLI skills. Most agents expose this via a `/skills` command or settings panel.

    3. **Ask it to build something**

        ```
        Build a support agent that answers questions from our docs
        ```

        As long as the skills are installed and visible, your agent will use them automatically.

---

## Prefer to Type Commands Yourself?

You can drive the entire workflow from your terminal — no coding agent needed.

```bash
# Create a minimal agent project
agents-cli create my-agent --prototype --yes

# Install dependencies and start the dev playground
cd my-agent
agents-cli install
agents-cli playground
```

This starts the ADK web playground at `http://localhost:8080` with hot reload.

For a full walkthrough, see the [Manual Workflow Tutorial](hands-on-tutorial.md).

---

## Demo

<div align="center">
  <iframe width="100%" height="450" src="https://www.youtube.com/embed/ECYKo70pPNc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## Next Steps

- [Tutorial: Build Your First Agent](quickstart-tutorial.md) — build, evaluate, and deploy with your coding agent
- [Tutorial: Manual Workflow](hands-on-tutorial.md) — type every command yourself
- [Use Cases](use-cases.md) — get inspired by real agent patterns people build
- [Project Structure](project-structure.md) — understand what each generated file does
- [Agent Templates](templates.md) — choose the right template (`adk`, `agentic_rag`)
- [Development Guide](development.md) — full development workflow
- [CLI Reference](../cli/index.md) — all commands and flags

---

!!! tip "Coming from Agent Starter Pack?"
    See the [migration guide](../reference/from-agent-starter-pack.md).

!!! note "Share what you build"
    Built something interesting with Agents CLI? We'd love to hear about it! Share your project at [agents-cli@google.com](mailto:agents-cli@google.com).

## The Lifecycle — https://google.github.io/agents-cli/guide/lifecycle/

# The Lifecycle

Agents CLI is opinionated about one thing: the loop between **"looks good in a notebook"** and **"live in production."** This page is the map.



## Watch a single investigation

Imagine an outage-recovery agent. It's been live for a week. A pager fires:

<div id="lifecycle-anim-transcript" class="lifecycle-anim" aria-label="Auto-playing transcript of an outage investigation"></div>

That investigation took **4.3 seconds**. Nothing about *the agent itself* is unusual — most agent frameworks could express it. What's unusual is everything around it: the eval rubric that wouldn't have let it ship if it recommended a destructive remediation, the CI check that would have caught the runbook search returning the wrong section, the trace that lets you replay this exact investigation when something goes sideways tomorrow.

That's the loop.

## Four CLI verbs on rotation

<div id="lifecycle-anim-loop" class="lifecycle-anim" aria-label="The four CLI verbs in a continuous loop"></div>

`scaffold`, `eval`, `deploy`, observe — on a rotation, forever. You write the spec; the loop catches what would have shipped, ships what passes, and shows you what happens next so the next iteration is smarter.

## What goes wrong without it

Most agent demos stop at the prompt. You write a clever instruction, the model returns something that looks great in a notebook, and you screenshot it for the team. However, deploying to production brings real-world challenges.

| | Without the loop | With Agents CLI |
|---|---|---|
| **Hallucinated remediation** | Discovered customer-side, after the fact | Eval rubric blocks the PR before merge |
| **Tool API change** | 2 AM page, agent silently broken | CI integration test catches the schema drift |
| **Production misuse** | No replay, no telemetry | Cloud Trace + BigQuery analytics surface it within the hour |
| **Cost spike from a chatty tool** | Next month's bill is the alert | Per-tool span counts surface the loop in hours |

## The eight phases

The loop expands to eight phases when you walk through it slowly. Each phase has an opinion encoded in a [skill](../reference/skills.md) so your coding agent picks the right answer for you.

| # | Phase | What it does | CLI verb | Skill | Deep-dive |
|---|---|---|---|---|---|
| 0 | **Spec** | Write a `.agents-cli-spec.md`. The other phases derive from this. | — | `google-agents-cli-workflow` | [Development Guide](development.md) |
| 1 | **Scaffold** | Turn the spec into a production-shaped project (~72 files). | `scaffold create` | `google-agents-cli-scaffold` | [Templates](templates.md) |
| 2 | **Build** | Write the agent body — model, instruction, tools, `App` wrapper. | — | `google-agents-cli-adk-code` | [Project Structure](project-structure.md) |
| 3 | **Orchestrate** | Compose specialists when one agent grows into a team. | — | `google-agents-cli-adk-code` | [Project Structure](project-structure.md) |
| 4 | **Evaluate** | Score the agent against a dataset before every deploy. | `eval generate`, `eval grade`, plus `eval dataset synthesize`, `eval compare`, `eval analyze`, `eval metric list`, and `eval optimize` | `google-agents-cli-eval` | [Evaluation](evaluation.md) |
| 5 | **Deploy** | Ship to Agent Runtime, Cloud Run, or GKE. | `deploy` | `google-agents-cli-deploy` | [Deployment](deployment.md) |
| 6 | **Publish** | Register with Gemini Enterprise so other agents can find this one. | `publish` | `google-agents-cli-publish` | [CI/CD](cicd.md) |
| 7 | **Observe** | Cloud Trace + BigQuery analytics; production data feeds tomorrow's dataset. | — | `google-agents-cli-observability` | [Observability](observability/index.md) |

### 0 · Spec

A `.agents-cli-spec.md` names the agent's tools, constraints, and success criteria. The whole rest of the lifecycle reads from it: the scaffold flags, the eval rubrics, the safety guardrails, the trace attributes you'll watch in production. Don't start from blank — browse [Agent Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden) for an existing template close to what you want, then customize.

A typical spec is one screen of markdown:

```markdown
# .agents-cli-spec.md — outage-recovery-bot

## Tools

| Tool                                    | Backing service       |
| --------------------------------------- | --------------------- |
| `query_logs(service, severity)`         | Cloud Logging         |
| `check_metrics(service, metric)`        | Cloud Monitoring      |
| `search_runbook(query)`                 | Vector Search         |

## Constraints

1. Always cite the runbook section consulted.
2. Never recommend a destructive remediation unless the runbook
   explicitly sanctions it for the observed symptom.

## Success criteria

- ≥ 80% of incidents get a diagnosis whose root cause matches ground truth
- 100% of recommendations cite a runbook section
- 0 destructive recommendations without runbook sanction
```

### 1 · Scaffold

One command takes the spec and emits the project: agent code, tests, eval boilerplate, Terraform, CI/CD workflows, deployment manifests. The flags aren't gratuitous — each one expands or contracts the scaffold to match the lifecycle you've signed up for.

<div id="lifecycle-anim-scaffold" class="lifecycle-anim" aria-label="Scaffold wizard — toggle flags, watch the command and file count update"></div>

The full setup ships **~72 files** across agent code, eval boilerplate, Terraform, GitHub Actions workflows, and deploy manifests. Trim it down by skipping pieces you don't need. See [Templates](templates.md) for the full list.

### 2 · Build

Every ADK agent boils down to four ingredients: a model, an instruction, a list of tools, and an `App` that wraps them. The body is barely 30 lines of meaningful code — the interesting work happens inside the tools.

```python
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini

root_agent = Agent(
    name="root_agent",
    model=Gemini(model="gemini-flash-latest"),
    instruction="You are an SRE outage-recovery assistant...",
    tools=[query_logs, check_metrics, search_runbook],
)

app = App(root_agent=root_agent, name="app")
```

You're not locked to Gemini — swap the model line for any provider supported by ADK ([Model Garden](https://cloud.google.com/model-garden) covers Anthropic Claude, OpenAI GPT, and others). The rest of the lifecycle behaves the same regardless.

Stateful agents reach for two more pieces of Agent Platform:

- **Managed session storage** for conversation state that survives restarts and scales horizontally — pick it at scaffold time via `--session-type agent_platform_sessions` instead of the in-memory default.
- **[Memory Bank](https://cloud.google.com/agent-builder/docs/memory)** for *long-term* memory across sessions (the SRE bot recognizing "this looks like that incident from last quarter"). Wire it in via `from google.adk.memory import VertexAiMemoryBankService` and the agent gets a persistent store keyed to user, session, or app.

For workflows that don't fit in a single HTTP request — long investigations, multi-step batch jobs — Agent Runtime persists the agent's state so a deploy or restart doesn't lose progress.

<div id="lifecycle-anim-models" class="lifecycle-anim" aria-label="Same prompt, three model providers — illustrative side-by-side"></div>

Here's the same agent body answering a different incident, end-to-end:

<div id="lifecycle-anim-playground" class="lifecycle-anim" aria-label="Inline playground — payments triage scenario, click to step through"></div>

### 3 · Orchestrate

The single-agent body works while the problem is small. Real production agents grow into **teams** — an orchestrator that routes work to a handful of specialists, each with its own narrow tool surface.

<div id="lifecycle-anim-team" class="lifecycle-anim" aria-label="Team diagram — orchestrator routes work to investigator, diagnoser, and remediator"></div>

Splitting helps for three reasons that show up in eval, deploy, and observe: smaller prompts make each agent more reliable, separate tool surfaces let you apply per-agent guardrails, and the trace tells you exactly which sub-agent took the bad turn.

When the team needs to span processes — or call agents your team doesn't own — use the **[A2A protocol](https://a2a-protocol.org/)** as the wire format. A2A is built into every ADK agent, so just scaffold normally (`--agent adk`): any A2A-compatible agent (built with Agents CLI or not) can call yours, and yours can call theirs.

### 4 · Evaluate

This is the phase most agent demos skip. `agents-cli eval generate` followed by `agents-cli eval grade` can execute your dataset against the live agent, ask an LLM judge to score each response against a rubric, and give you a number you can defend.

<div id="lifecycle-anim-eval" class="lifecycle-anim" aria-label="Eval-fix loop — click 'apply fix' to see one case flip from failing to passing"></div>

Expect 5–10+ iterations of the `agents-cli eval grade` loop. Every fix nudges the score, you re-run, you ship when it crosses the threshold. Below: the four failure modes the rubrics catch most often.

<div id="lifecycle-anim-failures" class="lifecycle-anim" aria-label="Common agent failures and the eval rubric that catches each"></div>

See the [Evaluation Guide](evaluation.md) for metrics, dataset schemas, and the full methodology.

### 5 · Deploy

The same agent code can land in three different places. `agents-cli deploy` dispatches based on the target you scaffolded with. **Pick one to see what `--dry-run` would print and the steps that would follow:**

<div id="lifecycle-anim-deploy" class="lifecycle-anim" aria-label="Deploy target picker — choose a runtime to see the dry-run + pipeline"></div>

```bash
agents-cli deploy --dry-run        # preview the pipeline
agents-cli deploy                  # ship it
agents-cli deploy --no-wait        # return immediately; check later with --status
```

Each target inherits the surrounding production primitives:

- **Per-agent service account** — opt in with `agents-cli deploy --agent-identity`, and the deployed agent runs as its own GCP identity. Scope what it can actually call (which BigQuery datasets, which buckets, which APIs) with normal IAM. The eval rubrics that block destructive remediations have a fallback: the agent literally can't `kubectl delete` if its identity isn't allowed to.
- **[Identity-Aware Proxy (IAP)](https://cloud.google.com/iap)** — gate a Cloud Run deploy behind your Google Workspace SSO with the `--iap` flag. Internal-only agents stop being a public-internet concern.
- **[Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)** — the scaffolded `pr_checks.yaml` authenticates GitHub Actions to GCP via WIF, so no service-account keys live in your repo.

See [Deployment](deployment.md) for full per-target walkthroughs.

### 6 · Publish

Deploying the agent makes it reachable at a URL. Publishing is the separate step that lists it in Gemini Enterprise so other agents (or humans browsing the catalog) can actually find it.

<div id="lifecycle-anim-publish" class="lifecycle-anim" aria-label="The agent's listing in Gemini Enterprise after publish"></div>

Two registration modes: **ADK** (publishes a deployed Agent Runtime instance) and **[A2A](https://a2a-protocol.org/)** (publishes an A2A-compatible HTTP endpoint, no ADK required — works with agents built on any framework).

### 7 · Observe

Once the agent is live, every invocation emits a Cloud Trace span. Every tool call, model generation, and sub-agent handoff is visible. **Hover any span below to see its attributes.**

<div id="lifecycle-anim-trace" class="lifecycle-anim" aria-label="Trace waterfall — bars draw in left-to-right showing the orchestrator and its sub-agents; hover to inspect"></div>

Observability is essential for any agent running in production, as it helps you catch regressions your evaluation might have missed, cost spikes from chatty tools, or cases where users bypass safety prompts. With `--bq-analytics` turned on at scaffold time, every prompt and response also lands in BigQuery for offline analysis.

The same data closes the loop: production traffic feeds tomorrow's dataset. Eval scores get re-computed continuously, so regressions surface in days, not months.

<div id="lifecycle-anim-rolling" class="lifecycle-anim" aria-label="Rolling production eval score over the last ten days, with annotated regression and deploy events"></div>

See [Observability](observability/index.md) for the full setup.

## Two ways to drive it

<div class="lc-tabs-bare" markdown>

=== "Ask your coding agent"

    The canonical path. Your coding agent reads the skills and picks the right CLI command at the right phase.

    ```
    Build me an outage-recovery agent. It should investigate incidents
    using logs, metrics, and runbooks, and recommend remediations
    that cite a runbook section. Deploy it to Agent Runtime.
    ```

    Your coding agent will:

    1. Write a `.agents-cli-spec.md` describing the tools and constraints
    2. Run `agents-cli scaffold create … --agent agentic_rag --deployment-target agent_runtime`
    3. Author the agent body and tools
    4. Write dataset cases
    5. Run `agents-cli eval generate` followed by `agents-cli eval grade` and iterate with `eval grade` until the score crosses threshold
    6. Run `agents-cli deploy`
    7. Wire up trace + analytics, hand you the URL

=== "Drive the CLI yourself"

    Every command works standalone. Skip the coding agent entirely if you'd rather type.

    ```bash
    # Phase 1: scaffold
    agents-cli scaffold create outage-recovery-bot \
      --agent agentic_rag \
      --datastore agent_platform_vector_search \
      --deployment-target agent_runtime \
      --cicd-runner github_actions \
      --bq-analytics
    cd outage-recovery-bot && agents-cli install

    # Phase 2-3: build & orchestrate (edit app/agent.py)
    agents-cli playground       # local web playground at :8080

    # Phase 4: evaluate
    agents-cli eval dataset synthesize --count 10  # optional: cold-start a dataset
    agents-cli eval generate
    agents-cli eval grade                          # repeat until eval score crosses threshold
    agents-cli eval compare prev.json latest.json  # confirm fixes actually helped
    agents-cli eval analyze --eval-result latest.json  # cluster remaining failures
    agents-cli eval optimize                       # optional: auto-tune prompts using eval data

    # Phase 5: deploy
    agents-cli deploy --dry-run
    agents-cli deploy

    # Phase 6: publish (optional)
    agents-cli publish gemini-enterprise
    ```

    See the [Manual Workflow Tutorial](hands-on-tutorial.md) for the full end-to-end walkthrough.

</div>

## Where to dig deeper

- [Templates](templates.md) — full list of scaffold templates (`adk`, `agentic_rag`, …)
- [Project Structure](project-structure.md) — what each generated file does
- [Development Guide](development.md) — day-to-day workflow
- [Evaluation Guide](evaluation.md) — dataset schema, the eval-fix loop
- [Deployment](deployment.md) — per-target walkthroughs
- [CI/CD & Production](cicd.md) — the full PR-to-prod path
- [Observability](observability/index.md) — Cloud Trace, BigQuery analytics, third-party tools
- [CLI Reference](../cli/index.md) — every command and flag

## Use Cases — https://google.github.io/agents-cli/guide/use-cases/

# Use Cases

Agents CLI scaffolds, evaluates, and deploys agents from the descriptions you provide to your coding agent. Use it to build:

- **Scheduled bots.** Fetch data from RSS feeds, summarize the results with an LLM, and publish to Google Chat or email on a Cloud Scheduler trigger.
- **Investigation agents.** Read logs, trace deployments, and correlate findings with past incidents to produce a root-cause analysis.
- **Knowledge agents.** Index conversations, email, and design documents so that prior decisions are retrievable when topics recur.
- **A2A multi-agent systems.** Coordinate specialist agents across incident response, code migrations, or audits.

---

## Pick a Pattern

<table class="use-case-grid">
<tr>
<td align="center" width="33%"><h3><a href="#daily-news-bot">Daily News Bot</a></h3></td>
<td align="center" width="33%"><h3><a href="#industry-watch">Industry Watch</a></h3></td>
<td align="center" width="33%"><h3><a href="#self-tuning-support">Self-Tuning Support</a></h3></td>
</tr>
<tr>
<td align="center"><h3><a href="#technical-investigation">Technical Investigation</a></h3></td>
<td align="center"><h3><a href="#regression-detector">Regression Detector</a></h3></td>
<td align="center"><h3><a href="#organizational-memory">Organizational Memory</a></h3></td>
</tr>
<tr>
<td align="center"><h3><a href="#institutional-memory-navigator">Institutional Memory</a></h3></td>
<td align="center"><h3><a href="#due-diligence">Due Diligence</a></h3></td>
<td align="center"><h3><a href="#security-audit">Security Audit</a></h3></td>
</tr>
<tr>
<td align="center"><h3><a href="#rfp-response-generator">RFP Generator</a></h3></td>
<td align="center"><h3><a href="#incident-response-coordination">Incident Response</a></h3></td>
<td align="center"><h3><a href="#distributed-code-migration">Code Migration</a></h3></td>
</tr>
</table>

!!! note "Not yet supported"

    - **Real-time voice and video**
    - **Non-Python agents** (Go, Java, TypeScript)
    - **Multi-cloud deployments** — focused on Google Cloud; interaction with other clouds may require custom infrastructure and skills

---

## Beginner

Single-agent patterns with no inter-agent coordination. Suitable as first projects.

### Daily News Bot

*Beginner · `adk`*

Fetch headlines from a configured set of RSS feeds, select the most relevant items with an LLM, and publish to Google Chat or email. Schedule with Cloud Scheduler.

```
Build me a daily news bot that pulls these RSS feeds, summarizes the top 5 stories, and posts to Google Chat every morning.
```

For scheduling and rollout, see [Deployment](deployment.md) and [CI/CD](cicd.md).

### Industry Watch

*Beginner · `adk`*

Track public release notes, documentation updates, job postings, and conference talks across your industry. Surface shipped features and hiring trends. Persist findings to a queryable store for week-over-week review.

```
Track these companies' public docs, releases, and job postings daily. Surface shipped features and hiring trends.
```

---

## Intermediate

A single agent paired with a feedback loop, retrieval-augmented generation, or substantial tool integration.

### Self-Tuning Support

*Intermediate · `adk`*

Run evaluation after each conversation, identify gaps in knowledge or behavior, and draft new evaluation cases for weak responses. Coverage adapts to the questions customers actually ask.

```
Build a support agent that runs eval after each conversation, drafts new eval cases for weak answers, and surfaces documentation gaps.
```

The [Evaluation Guide](evaluation.md) describes the eval-and-fix loop. Pair with [observability](observability/index.md) to replay production traces.

### Technical Investigation

*Intermediate · `adk`*

Accept a question such as "Why did latency increase in the payments service last month?" Read logs, trace deployments, and correlate with past incidents. Produce a timeline and root-cause analysis.

```
Build an investigation agent. I ask questions like "why did X break last week" and it pulls from logs, deploy history, and past incidents to produce a writeup.
```

### Regression Detector

*Intermediate · `adk`*

Compare current metrics and log patterns against historical pre-incident signatures. File preventive issues when current behavior matches a known regression pattern. Run on a nightly schedule.

```
Build an agent that runs nightly, looks for metric/log patterns that match historical pre-incident signatures, and files preventive bugs.
```

### Organizational Memory

*Intermediate · `agentic_rag`*

Index Google Chat, email, design documents, and meeting notes for decision records. When a proposal recurs (for example, "use Redis for sessions"), surface the original thread and the decision the team reached.

```
Build a RAG agent that indexes Google Chat, email, and design docs nightly. Surface past decisions when someone proposes something we've already discussed.
```

The [`agentic_rag` template](templates.md) provides retrieval out of the box. See [Project Structure](project-structure.md) for ingestion code locations.

### Institutional Memory Navigator

*Intermediate · `agentic_rag` · Gemini Enterprise*

Deploy in Gemini Enterprise with permissioned access to Drive, Google Chat, and email. Respond to questions such as "How do I get production database access?" with both the documented process and the current operational reality.

```
Build a RAG agent for new-hire questions that knows both official docs and how things actually work. Publish it to Gemini Enterprise.
```

See the [`google-agents-cli-publish`](../reference/skills.md) skill for registration details.

---

## Advanced

Long-running workflows or multi-agent coordination. Requires dedicated infrastructure and extended development.

### Due Diligence

*Advanced · `agentic_rag`*

Index a target codebase of approximately 500,000 lines. Analyze technical debt, security vulnerabilities, license compliance, and deployment complexity. Produce a risk report with line numbers, dependency graphs, and CVE references. Multi-day analysis benefits from Agent Runtime's extended sessions and checkpointing.

```
Build a due-diligence agent that indexes a target codebase, runs security and license scans, and produces a risk report with citations.
```

### Security Audit

*Advanced · `adk`*

Map data flows across the codebase to verify GDPR, HIPAA, or SOC2 compliance. Trace sensitive data from ingestion through deletion. Flag gaps such as analytics logs that retain user data beyond the configured retention policy.

```
Build a compliance-audit agent that traces sensitive data flows across our codebase and flags retention/policy gaps with file:line citations.
```

Use [BigQuery agent analytics](observability/bq-agent-analytics.md) to track audit trail completeness.

### RFP Response Generator

*Advanced · `agentic_rag`*

Pull from past project records, current resource availability, and pricing models. Estimate timelines and budgets. Draft a technical approach. Produce a proposal package for human review.

```
Build a RAG agent that drafts RFP responses by pulling from past proposals, current resourcing, and pricing models.
```

### Incident Response Coordination

*Advanced (A2A) · `adk`*

Run specialist agents in parallel during an outage: one bisects recent changes, one correlates errors across services, one searches past incidents, and one drafts customer communications. Parallel investigation reduces time-to-cause compared to sequential troubleshooting.

```
Build an A2A multi-agent system for incident response. Specialists for bisection, error correlation, past-incident lookup, and customer comms — coordinated in parallel.
```

The [`adk` template](templates.md) (A2A built in) exposes the A2A protocol. Each specialist runs as a service, and the coordinator orchestrates execution.

### Distributed Code Migration

*Advanced (A2A) · `adk`*

Run specialist agents for a large framework migration: one handles data models, one handles API contracts, one handles tests, and one handles validation. Specialists coordinate over A2A to share findings about breaking changes. GKE is the recommended runtime when running many concurrent specialist instances.

```
Build A2A specialist agents for a large framework migration: data models, API contracts, tests, validation.
```

---

## Next Steps

- [Tutorial: Build Your First Agent](quickstart-tutorial.md) — build, evaluate, and deploy with your coding agent
- [Project Structure](project-structure.md) — understand what each generated file does
- [Agent Templates](templates.md) — choose the right template (`adk`, `agentic_rag`)
- [Development Guide](development.md) — full development workflow
- [CLI Reference](../cli/index.md) — all commands and flags

## Development Guide — https://google.github.io/agents-cli/guide/development/

# Development Guide

This guide covers the full development workflow — from defining what you're building to monitoring it in production. It follows the same phases your coding agent uses via the `google-agents-cli-workflow` skill.

---

## Phase 0: Understand

Before writing any code, define what you're building.

If you're working with a coding agent, it will ask you these questions automatically. If you're working manually, answer them yourself:

1. **What problem will the agent solve?** — Core purpose and capabilities
2. **External APIs or data sources needed?** — Tools, integrations, auth requirements
3. **Safety constraints?** — What the agent must NOT do
4. **Deployment preference?** — Prototype first, or full deployment (Agent Runtime, Cloud Run, GKE)?

Save your answers to `.agents-cli-spec.md` in the current directory — overview, example use cases, tools required, constraints, success criteria.

---

## Phase 1: Scaffold

Create a new project from a template:

```bash
agents-cli create my-agent
```

Choose your agent template (`adk`, `agentic_rag`) and deployment target during creation. For fast prototyping without infrastructure decisions:

```bash
agents-cli create my-agent --prototype --yes
```

You can add deployment support later with `agents-cli scaffold enhance`.

See [Agent Templates](templates.md) for all options.

---

## Phase 2: Build & Iterate

### With a coding agent

Open your coding agent and activate the workflow skill:

```
/google-agents-cli-workflow
```

Describe what you want to build. Your coding agent uses the installed skills to write agent logic, create tools, and test changes — all following ADK best practices.

### Manually

Edit your agent logic in `app/agent.py` and test with:

- `agents-cli playground` — launches the ADK web playground at `localhost:8080` with hot reload
- `agents-cli run "your prompt"` — quick smoke test from the terminal

### Code Quality

```bash
agents-cli lint                                # Ruff checks and formatting
uv run pytest tests/unit tests/integration     # Run unit and integration tests
```

### Package Management

Add and remove dependencies with [uv](https://docs.astral.sh/uv/):

- `uv add <package>`
- `uv remove <package>`

---

## Phase 3: Evaluate

Run structured evaluations to validate agent behavior. This uses the [GenAI Eval SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) under the hood.

```bash
agents-cli eval generate
agents-cli eval grade
```

Expect **5-10+ iterations** of the eval-fix loop before your agent consistently passes. Start with 1-2 core eval cases, fix failures, then expand coverage.

See the [Evaluation Guide](evaluation.md) for metrics, dataset schemas, and the full methodology.

---

## Phase 4: Deploy

Once evaluation thresholds are met, deploy to Google Cloud.

1. **Add a deployment target** (if you started with `--prototype`):

    ```bash
    agents-cli scaffold enhance --deployment-target cloud_run
    ```

2. **Deploy**:

    ```bash
    agents-cli deploy
    ```

!!! tip
    To enable observability features (prompt-response logging, content logs), run `agents-cli infra single-project` after deploying. See the [Observability Guide](observability/index.md) for details.

For production pipelines with staging, approval gates, and CI/CD, see [Deployment](deployment.md) and [CI/CD & Production](cicd.md).

---

## Phase 5: Publish (optional)

Register your deployed agent with Gemini Enterprise:

```bash
agents-cli publish gemini-enterprise
```

Not all agents need this — only if you're distributing through Gemini Enterprise.

---

## Phase 6: Observe

Monitor your agent in production. Cloud Trace is enabled by default in all deployed agents — no configuration needed.

- **Cloud Trace** — distributed tracing, latency analysis, error visibility
- **BigQuery Agent Analytics** — opt-in advanced analytics for token usage, conversation patterns, and LLM-as-judge scoring

See the [Observability Guide](observability/index.md) for setup and usage.

---

For all commands and flags, see the [CLI Reference](../cli/index.md). For details on the skills your coding agent uses at each phase, see [Skills](../reference/skills.md).

## Evaluation Guide — https://google.github.io/agents-cli/guide/evaluation/

# Evaluation Guide

Run structured evaluations to confirm your agent calls the right tools, produces quality responses, and handles edge cases. Under the hood, evaluation uses the [Gemini Enterprise Agent Platform GenAI Eval SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) to grade evaluations.

!!! note "Upgrading from an older agents-cli?"
    If your project still has `tests/eval/evalsets/*.evalset.json` files from a previous version, see [Migrating Eval Datasets](../reference/eval-dataset-migration.md) for the new format.

---

## Run Your First Evaluation

Your project includes a default dataset at `tests/eval/datasets/basic-dataset.json` and metrics configuration `tests/eval/eval_config.yaml`. Run it:

```bash
agents-cli eval generate
agents-cli eval grade
```

The output shows scores for each eval case against the configured metrics.

```bash
# Run for a custom dataset and different metrics
agents-cli eval generate --dataset tests/eval/datasets/custom-dataset.json --output custom_traces/
agents-cli eval grade --metrics general_quality --traces custom_traces/
```

---

## Writing Eval Cases and Choosing Metrics

For full documentation on eval case schemas and available metrics, see the [Gemini Enterprise Agent Platform Evaluation documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).

### Available Metrics Reference

You can choose from a wide range of built-in metrics depending on your agent's capabilities and the task at hand. To see the full list of available metrics, run:

```bash
agents-cli eval metric list
```

#### Common metrics at a glance

A short reference for the most-used built-in metric IDs. Use `agents-cli eval metric list` for the full set with descriptions.

| Metric ID | What it grades |
|---|---|
| `general_quality` | Overall response quality with auto-generated content-based criteria. Recommended starting point for non-agent eval. |
| `text_quality` | Linguistic aspects: fluency, coherence, grammar. |
| `instruction_following` | How well the response adheres to specific constraints and instructions. |
| `tool_use_quality` | Tool selection, parameter accuracy, and step sequence correctness (single-turn). |
| `multi_turn_tool_use_quality` | Technical and semantic correctness of tool calls across a multi-turn conversation. |
| `multi_turn_trajectory_quality` | Sequential logic, efficiency, and error-recovery robustness across turns. |
| `multi_turn_task_success` | Whether the user's goal was fulfilled across the full multi-turn conversation. |
| `final_response_quality` | Comprehensive evaluation of the final response and intermediate tool usage. |
| `final_response_reference_free` | Final-response quality without a reference answer (requires custom rubrics). |
| `final_response_match` | Compares the agent's final response to a provided golden reference answer. |
| `hallucination` | Segments the response into atomic claims and verifies each against tool-returned context. |
| `grounding` | Factuality and consistency against provided context. |
| `safety` | Compliance against safety policies (PII, hate speech, dangerous content, harassment, sexual). |

### Evaluation Configuration (`eval_config.yaml`)

The `eval_config.yaml` file specifies the metrics to run and defines custom metrics for grading evaluations.

```yaml
metrics_to_run:
  - response_under_500_chars

custom_metrics:
  - name: response_under_500_chars
    custom_function: |
      def evaluate(instance: dict) -> dict:
          response = instance.get("response") or {}
          text = "".join(
              p.get("text", "") for p in (response.get("parts") or []) if p.get("text")
          )
          passed = len(text) <= 500
          return {
              "score": 1.0 if passed else 0.0,
              "explanation": f"Final response is {len(text)} chars (limit 500).",
          }
  - name: response_quality_rubric
    prompt_template: |
      Rate the agent's response 1-5 for helpfulness and accuracy.
      Prompt: {prompt}
      Final response: {response}
      Full trace (for tool-call and reasoning context): {agent_data}
      Return JSON: {"score": <1|2|3|4|5>, "explanation": "<reason>"}
    judge_model: gemini-flash-latest
    judge_model_sampling_count: 3
```

Each custom metric must conform to either the **Code Execution Metric** or **LLM-as-a-Judge Metric** (`LLMMetric`) schema:
- **Code Execution Metric**: Used to run custom Python code for evaluation. Must have a `name` and a `custom_function` (containing a `def evaluate(instance):` signature). By default, the function executes **locally in the CLI process** — no GCP project or region is required, but the user-supplied code runs with the CLI's privileges. Add `"execution": "remote"` to opt into Vertex AI's sandboxed `CodeExecutionMetric` (server-side), which requires a configured GCP project + region.
- **LLM-as-a-Judge Metric**: Used to evaluate responses using an LLM judge. Must have a `name` and a `prompt_template`. Optional fields include `rubric_group_name`, `judge_model` (e.g., `gemini-flash-latest`), and `judge_model_sampling_count` (between `1` and `32`).

### Quick Reference for Common Scenarios

- **Agents with custom function tools** — Use `tool_use_quality` (for single-turn) or `multi_turn_tool_use_quality` + `multi_turn_trajectory_quality` (for multi-turn).
- **RAG agents** — Use `grounding` + `hallucination` + `safety`.
- **Conversational assistants** — Use `general_quality` or `multi_turn_general_quality`.
- **Goal-oriented agents** — Use `multi_turn_task_success`.

---

## The Eval-Fix Loop

Evaluation is iterative. Expect 5-10+ cycles before your agent consistently passes.

1. **Write 1-2 core eval cases** covering the most important behavior.
2. **Run**: `agents-cli eval generate` followed by `agents-cli eval grade`
3. **Read the results** — which cases failed and why.
4. **Fix** — adjust the agent's instruction, tools, or logic.
5. **Re-run**: `agents-cli eval generate` and `agents-cli eval grade`
6. **Expand** — once core cases pass, add edge cases and new scenarios.

---

## Beyond `generate` and `grade`

`generate` and `grade` form the inner loop, but the eval surface has a few more commands worth knowing about. Each is a separate step you reach for as your eval setup matures.

### `agents-cli eval dataset synthesize`

Bootstraps a dataset by inspecting your local ADK agent and generating multi-turn conversation scenarios for it — no input file required. Useful for cold-starting evaluation on a new agent or expanding coverage without writing every case by hand. Each generated case includes a starting user message, a conversation plan, and the full agent trace produced by playing the scenario out against an LLM-backed user simulator.

```bash
agents-cli eval dataset synthesize --count 10
```

Steer what gets generated with `--instruction` (e.g. `"Scenarios where the user changes their mind"`) and `--environment-context` (e.g. `"Today is Monday. Flights to Paris are available."`). The output is a regular `*-dataset.json` file you can edit, commit, and feed back into `eval grade` directly (the trace is already populated, so you can skip `eval generate`).

### `agents-cli eval compare`

Compares two grade results side by side so you can see whether a change actually improved things.

```bash
agents-cli eval compare baseline_results.json candidate_results.json
```

A typical use is comparing a "before fix" run against an "after fix" run during the eval-fix loop.

### `agents-cli eval analyze`

Clusters failure modes from a grade-results file into themes, so you can see *what kinds of things* are going wrong instead of skimming individual cases.

```bash
agents-cli eval analyze --eval-result grade_results.json
```

### `agents-cli eval metric list`

Prints every built-in metric the SDK supports, with a short description for each. The starting point when you want to know what's available beyond the common metrics table above.

### `agents-cli eval optimize`

Once your evals are in place, `eval optimize` uses them to automatically tune your agent's prompts.

```bash
agents-cli eval optimize
```

A run takes anywhere from a few minutes to several hours depending on dataset size and metric complexity, so it's not something to run over and over. Reach for it after simpler approaches (rewriting the prompt yourself, adjusting metrics, fixing failing cases by hand) have run their course.

---

For full documentation on eval case schemas, metrics, and user simulation, see the [Gemini Enterprise Agent Platform Evaluation documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).

## Deployment — https://google.github.io/agents-cli/guide/deployment/

# Deployment

Deploy your agent to a development environment or production with a CI/CD pipeline.

![Prototype to Production](../assets/prototype_to_prod.png)

---

## Infrastructure vs Deployment

**Infrastructure** (`agents-cli infra`) provisions the cloud resources your agent needs — service accounts, IAM bindings, APIs, telemetry buckets, and Terraform state. It sets the stage but doesn't run your agent.

**Deployment** (`agents-cli deploy`) takes your agent code and puts it on the provisioned infrastructure — building a container, pushing it to a registry, and starting the service.

The typical flow: provision infrastructure first, then deploy on top of it.

---

## Deploy to a Dev Environment

The simplest path to a running deployment:

**1. Set your dev project:**

```bash
gcloud config set project YOUR_DEV_PROJECT_ID
```

**2. Deploy the agent:**

```bash
agents-cli deploy
```

The command reads your `deployment_target` from `agents-cli-manifest.yaml` (under `create_params`) and dispatches to the right flow:

| `deployment_target`  | What happens                                  |
|----------------------|-----------------------------------------------|
| `agent_runtime`      | Agent Runtime deployment (fully managed)       |
| `cloud_run`          | `gcloud beta run deploy` (container on Cloud Run) |
| `gke`                | Terraform + Docker build + `kubectl apply`     |

The deployment target is set when you create your project:

```bash
agents-cli create my-agent -d cloud_run    # or agent_runtime, gke
```

To change the deployment target for an existing project, use `scaffold enhance`:

```bash
agents-cli scaffold enhance -d cloud_run
```

Run `agents-cli scaffold enhance --help` to see all available options.

!!! tip
    To enable observability features (prompt-response logging, content logs), run `agents-cli infra single-project` after deploying. Terraform provisions the telemetry resources and updates your service to use them. See the [Observability Guide](observability/index.md) for details.

**Verify it works:**

```bash
agents-cli deploy --list    # List deployments
agents-cli deploy --status  # Check deployment status
```

---

## Deployment Targets

### Agent Runtime

*Selected with `agents-cli create my-agent -d agent_runtime`, or `create_params.deployment_target: agent_runtime` in `agents-cli-manifest.yaml`.*

Fully managed runtime: you provide a `Dockerfile` (scaffolded for you) and Agent Engine builds and runs the container — no cluster or service to operate:

```bash
agents-cli deploy --project my-gcp-project --region us-east1
```

Pass Docker build args or a container port; a prebuilt `--image` is not supported (Agent Runtime always builds from the Dockerfile):

```bash
agents-cli deploy --build-args KEY=VALUE --port 8080
```

Check on an async deployment:

```bash
agents-cli deploy --no-wait     # Start and return immediately
agents-cli deploy --status      # Check progress later
```

### Cloud Run

*Selected with `agents-cli create my-agent -d cloud_run`, or `create_params.deployment_target: cloud_run` in `agents-cli-manifest.yaml`.*

Builds a container from source and deploys as a Cloud Run service:

```bash
agents-cli deploy --project my-gcp-project --region us-east1
```

Override resource limits:

```bash
agents-cli deploy --memory 8Gi --port 8080
```

Deploy a pre-built image instead of building from source:

```bash
agents-cli deploy --image gcr.io/my-project/my-agent:v1
```

!!! tip
    If you need more advanced Cloud Run deployment features not exposed via `agents-cli` flags, use `--dry-run` (or `-n`) to print the full `gcloud` command. You can then copy it and add additional arguments as needed.

### GKE

*Selected with `agents-cli create my-agent -d gke`, or `create_params.deployment_target: gke` in `agents-cli-manifest.yaml`.*

Deploys to a GKE cluster using Terraform and kubectl:

```bash
agents-cli deploy --cluster-name my-cluster --project my-gcp-project
```

---

## Next Steps

- [CI/CD & Production](cicd.md) — set up automated pipelines for staging and production
- [Observability](observability/index.md) — monitor your deployed agent

## Agent Templates — https://google.github.io/agents-cli/guide/templates/

# Agent Templates

`agents-cli` creates projects from agent templates. Each template provides a working agent with the right dependencies, tools, and project structure for its use case.

---

## Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `adk` | ReAct agent using ADK | General-purpose conversational agent with tool use |
| `agentic_rag` | ADK agent with RAG pipeline | Document Q&A with automated data ingestion |

### adk

The default template. Creates a ReAct agent using the [Agent Development Kit](https://google.github.io/adk-docs/) with a sample tool. Start here if you are new to ADK or building a general-purpose agent.

```bash
agents-cli create my-agent --agent adk
```

Every Python ADK agent serves the [Agent-to-Agent (A2A) protocol](https://a2a-protocol.org) out of the box — the A2A routes (agent card + JSON-RPC) are mounted automatically. Use this when your agent needs to interoperate with agents built on other frameworks (LangGraph, CrewAI, etc.) or when building a distributed multi-agent system; no separate template or hand-written A2A code is required.

### agentic_rag

A document Q&A agent with a built-in RAG (Retrieval-Augmented Generation) pipeline. Includes data ingestion infrastructure for indexing documents into a vector store and retrieving them at query time.

```bash
agents-cli create my-agent --agent agentic_rag --datastore agent_platform_search
```

During project creation, choose a datastore backend:

| Datastore | Description |
|-----------|-------------|
| `agent_platform_search` | GCS Data Connector with built-in scheduling and ranking |
| `agent_platform_vector_search` | Kubeflow pipeline with auto-embedding |

After creation, provision the datastore and ingest data:

```bash
agents-cli infra datastore
agents-cli data-ingestion
```

## Project Structure — https://google.github.io/agents-cli/guide/project-structure/

# Project Structure

*For developers who want to understand the layout of a generated agent project.*

When you run `agents-cli create my-agent --prototype --yes`, you get a ready-to-run project. This page explains what each file does.

---

## Directory Layout

```
my-agent/
├── app/                          # Your agent code
│   ├── __init__.py               # Registers the app (exports `app`)
│   ├── agent.py                  # Agent definition — instructions, model, tools
│   └── app_utils/                # Utilities (telemetry, converters)
│       ├── __init__.py
│       ├── telemetry.py          # OpenTelemetry setup for Cloud Trace
│       ├── typing.py             # Request/response Pydantic models
│       └── gcs.py                # GCS utility functions
│
├── tests/
│   ├── eval/                     # Evaluation test cases
│   │   ├── datasets/
│   │   │   └── basic-dataset.json    # Default eval cases
│   │   └── eval_config.yaml          # Evaluation metrics configuration
│   ├── integration/
│   │   └── test_agent.py         # Integration test (runs agent end-to-end)
│   └── unit/
│       └── test_dummy.py         # Placeholder for unit tests
│
├── pyproject.toml                # Project config and dependencies
├── agents-cli-manifest.yaml      # Configuration for agents-cli
├── GEMINI.md                     # Guidance file for coding agents
├── Makefile                      # Shortcut commands (make dev, make eval, etc.)
├── .env                          # Environment variables (project ID, location)
└── uv.lock                       # Locked dependency versions
```

---

## Key Files

### `app/agent.py`

This is where your agent lives. The default template looks like this:

```python title="app/agent.py"
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city."""
    # ... implementation
    return f"The current time is ..."


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="You are a helpful AI assistant.",
    tools=[get_weather, get_current_time],
)

app = App(
    root_agent=root_agent,
    name="app",  # Must match the agent directory name
)
```

The four key parts:

1. **Tool functions** — plain Python functions with docstrings. The docstring tells the LLM when to use the tool.
2. **`Agent`** — combines a model, instruction (system prompt), and tools.
3. **`App`** — wraps the agent for serving. The `name` must match the directory name (`app`).
4. **Model** — defaults to `gemini-flash-latest`. Change it in the `Gemini()` constructor.

### `pyproject.toml`

Contains Python project metadata and dependencies:

```toml title="pyproject.toml"
[project]
name = "my-agent"
version = "0.0.1"
requires-python = ">=3.11"
dependencies = [
    "google-adk[gcp]>=2.0.0,<3.0.0",
    # ... other dependencies
]
```

### `agents-cli-manifest.yaml`

Contains agents-cli project metadata and configuration:

```yaml title="agents-cli-manifest.yaml"
name: my-agent
agent_directory: app
create_params:
  deployment_target: none
  session_type: in_memory
```

- **`agent_directory`** — tells `agents-cli` commands where your agent code is.
- **`create_params`** — records how the project was created. Used by `agents-cli scaffold upgrade` to preserve your configuration.

### `tests/eval/datasets/basic-dataset.json`

Default evaluation cases. Each case defines a user message and the session context for running it. See the [Evaluation Guide](evaluation.md) for the full schema.

### `GEMINI.md`

A guidance file that coding agents (Antigravity CLI, Claude Code, etc.) read automatically. It contains project-specific instructions — ADK patterns, coding conventions, and workflow guidance. You don't need to read or edit this file unless you want to customize how coding agents work with your project.

### `.env`

Environment variables for local development:

```bash title=".env"
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-east1
```

These are read by the agent at runtime. Set them to match your Google Cloud project, or leave them empty if using a Gemini API key.

---

## With Deployment Infrastructure

When you create a project with a deployment target (or add one with `agents-cli scaffold enhance`), additional directories appear:

```
my-agent/
├── deployment/
│   └── terraform/
│       ├── dev/              # Dev environment Terraform
│       ├── staging/          # Staging Terraform
│       ├── prod/             # Production Terraform
│       └── variables.tf      # Shared variables
│
├── .github/                  # GitHub Actions CI/CD (if selected)
│   └── workflows/
│       ├── pr_checks.yaml
│       ├── staging.yaml
│       └── deploy-to-prod.yaml
│
└── .cloudbuild/              # Cloud Build CI/CD (if selected)
    ├── pr_checks.yaml
    ├── staging.yaml
    └── deploy-to-prod.yaml
```

### Adding Infrastructure Later

Start with a prototype and add infrastructure when you need it:

```bash
# Add Cloud Run deployment
agents-cli scaffold enhance --deployment-target cloud_run

# Add a RAG datastore
agents-cli scaffold enhance --datastore agent_platform_search

# Preview changes without applying
agents-cli scaffold enhance --deployment-target cloud_run --dry-run
```

## Observability Overview — https://google.github.io/agents-cli/guide/observability/

# Observability

Every `agents-cli` project ships with OpenTelemetry instrumentation that automatically exports traces to **Cloud Trace**. This gives you:

- **Distributed tracing** — track requests as they flow through LLM calls and tool executions.
- **Latency analysis** — identify performance bottlenecks by analyzing span durations.
- **Error visibility** — traces capture errors, helping pinpoint where failures occur.
- **No configuration required** — works out-of-the-box in all environments.

For ADK-based agents, **prompt-response logging** is also available. It captures model interactions (prompts, responses, tokens) and exports them to GCS, BigQuery, and Cloud Logging. Disabled locally by default, enabled automatically in deployed environments.

### Logging Behavior by Environment

| Environment | Tracing (Cloud Trace) | Prompt-Response Logging |
|---|---|---|
| **Local** (`agents-cli playground`) | Enabled | Disabled (no `LOGS_BUCKET_NAME`) |
| **Deployed** (Terraform) | Enabled | Enabled (`NO_CONTENT` mode — metadata only) |

---

## Cloud Trace

The default observability method. See [Cloud Trace](cloud-trace.md) for setup and usage.

---

## BigQuery Agent Analytics

For advanced analytics — querying patterns across conversations, token usage dashboards, and LLM-as-judge scoring on production traffic. Opt-in via the `--bq-analytics` flag during project creation.

See [BigQuery Agent Analytics](bq-agent-analytics.md) for details.
