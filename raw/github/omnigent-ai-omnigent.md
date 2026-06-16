# omnigent-ai/omnigent

## Metadata
- Stars: 2073
- Primary language: Python
- Default branch: main
- Latest release: none found (no GitHub Releases published)
- License: Apache License 2.0
- Homepage: https://omnigent.ai
- Fetched: 2026-06-16
- Final URL: https://github.com/omnigent-ai/omnigent

## Description
A meta-harness for all your AI agents. Omnigent provides a common layer over Claude Code, Codex, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, keep them in check with policies and sandboxing, and collaborate in real time on the same live session, from any device.

## README

<div align="center">

# Omnigent

### A meta-harness for all your AI agents

Omnigent provides a common layer over Claude Code, Codex, Cursor, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, keep them in check with policies and sandboxing, and collaborate in real time on the same live session, from any device.

[omnigent.ai](https://omnigent.ai) · Download the macOS desktop app

</div>

## Why Omnigent?

Omnigent lets you:

- **Work with agents from any device, including your phone.** Sessions follow you: start in your terminal, continue in the browser, pick it up on your phone. Messages, sub-agents, terminals, and files stay in sync.
- **Supervise multiple agents.** Use Claude Code, Codex, Pi, and custom agents (defined in YAML) together in the same session. Ask one agent to review another's work, or split a task across agents that are each good at different things.
- **Use any model.** A first-party API key, a Claude/ChatGPT subscription, or any compatible gateway. All first-class.
- **Collaborate.** Share a session so teammates can chat with your agent and watch it work live, co-drive it on your machine, or fork the conversation to continue on their own.
- **Run agents in cloud sandboxes.** No laptop required: run sessions in disposable Modal, Daytona, or Islo sandboxes, launched from the CLI or provisioned by the server per session (*managed hosts*).
- **Govern your agents.** Create policies to pause for your approval before risky actions, cap spend, or limit which tools an agent reaches. They apply to the whole server, one agent, or a single chat.

## Quick start

### 1. Install

```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
```

Omnigent needs Python 3.12+. Install the `omnigent` package via `uv tool install omnigent` (or `pip install "omnigent"`), Homebrew (`brew install omnigent-ai/tap/omnigent`), or straight from the repo (`uv tool install -q --python 3.12 git+https://github.com/omnigent-ai/omnigent.git`).

Toolchain prerequisites: `uv` (required), `git` (required), Node.js 22 LTS+ with `npm` (for the Claude, Codex, and Pi coding harnesses — `omnigent run` installs the harness CLI you pick), `tmux` (required by the native `omnigent claude` / `omnigent codex` wrappers), `bubblewrap` (`bwrap`, Linux only — the native Claude/Codex/Pi harnesses wrap each agent terminal in a `bwrap` OS-sandbox; macOS uses the built-in `seatbelt` sandbox). Databricks workspace support is an optional extra (`uv tool install "omnigent[databricks]"`).

Updating: `omni upgrade` detects how you installed, drains and stops the local server, then runs the matching upgrade command; `omni upgrade --check` reports whether a newer release is available. Source checkouts update with `git pull`. The update check honors `UV_INDEX_URL` / `PIP_INDEX_URL` and `uv.toml` / `pip.conf`; override with `OMNIGENT_INDEX_URL`. Silence with `OMNIGENT_NO_UPDATE_CHECK=1`.

### 2. Start your first agent

`omnigent` (alias `omni`) picks a model with you and starts a session in your terminal, and also launches a local web UI at `http://localhost:6767` showing the same session in the browser or on a phone on your network. The desktop app wraps that same UI in a native window with OS notifications and a dock badge.

On first run, Omnigent picks up model credentials already in the environment (`ANTHROPIC_API_KEY` / `OPENAI_API_KEY`, or a `claude` / `codex` CLI you're logged into) and offers one as the default.

```bash
omnigent
omnigent claude                      # Claude Code, in a session your team can join
omnigent codex                       # Codex
omnigent run path/to/agent.yaml      # your own agent
```

Two example agents ship with the repo:

- **Polly** — a multi-agent coding orchestrator who writes no code herself. She plans, delegates work to coding sub-agents (Claude Code, Codex, or Pi) in parallel git worktrees, then routes each diff to a reviewer from a different vendor than the one that wrote it. You merge.
- **Debby** — a brainstorming partner with two heads, one Claude and one GPT. Every question goes to both heads, laid out side by side; `/debate` makes the heads critique each other for a few rounds before converging. Needs both a Claude and an OpenAI credential.

```bash
omnigent run examples/polly/
omnigent run examples/debby/
omnigent run examples/polly/ --harness pi
omnigent run examples/debby/ --harness openai-agents
omnigent run examples/polly/ --harness cursor  # needs cursor-agent + CURSOR_API_KEY
```

Browser-first alternative:

```bash
omnigent server start   # start the local server and web UI in the background
omnigent host           # (separate terminal) register this machine as a host
```

In the web UI: **New Chat** → pick your machine → go. `omnigent server status` checks status; `omnigent stop` stops everything.

### 3. Choose & switch models

```bash
omnigent setup
```

Four credential kinds, grouped by agent: **API key** (first-party vendor key for Anthropic, OpenAI, etc.), **Subscription** (Claude Pro/Max or ChatGPT plan via the official `claude` / `codex` CLIs), **Gateway** (any OpenAI- or Anthropic-compatible `base_url` + key — OpenRouter, LiteLLM, Ollama, vLLM, Azure), **Databricks** (a Databricks workspace profile, requires the `databricks` extra). Defaults are per agent, so a Claude default and a Codex default coexist; `/model` switches mid-session.

Gateway base URLs: OpenRouter for Claude Code uses `https://openrouter.ai/api`; OpenRouter for Codex / OpenAI agents uses `https://openrouter.ai/api/v1`; local Ollama for Codex / OpenAI agents uses `http://localhost:11434/v1` (key value ignored).

### 4. Deploy a server (and use it from your phone)

Running Omnigent on a server with a stable URL makes sessions reachable from anywhere, including a phone — same chat, sub-agents, terminals, and files, in sync with the laptop. `docker compose up` runs the server on any host; Render deploys with one click; Fly.io, Railway, Hugging Face Spaces, and Modal are also covered (full guide: `deploy/README.md`). The server can also provision a cloud sandbox per session (*managed hosts*), so no laptop has to stay online.

```bash
omnigent login https://your-host    # sign in once; run / attach / host reuse the token
omnigent host  https://your-host    # new sessions can now run on this machine
```

On a LAN, no deploy is needed — open the machine's LAN address on a phone (e.g. `http://192.168.x.x:6767`).

### 5. Collaborate with your team

Multi-user accounts, controlled by one environment variable:

```bash
OMNIGENT_AUTH_ENABLED=1 omnigent server start
```

The Docker deploy turns this on by default. Sign in as `admin` (first run prints the password and saves it locally) and use **Admin → Members → Invite** to create a single-use invite link — no email server needed; signup is invite-only.

Collaboration features:
- **Share a live session** — Hit Share in the web UI; teammates watch the agent work and chat with it in real time.
- **Co-drive** — A teammate co-attaches to a running session; their messages execute on the host's machine. Good for pairing or handing the keyboard to a domain expert mid-investigation: `omnigent attach <session_id>`.
- **Fork** — Clone a conversation onto another machine and continue independently from the fork point: `omnigent run --fork <session_id>`.

SSO: setting `OMNIGENT_OIDC_ISSUER` plus a client ID/secret on the deployed server enables sign-in via Google, GitHub, Okta, or Microsoft logins (plus a proxy-only `header` auth mode) — see `deploy/README.md#auth`.

### 6. Govern your agents with policies

Policies decide what an agent may do — run shell commands, edit files, spend tokens. They check every action and either allow it, block it, or pause to ask the user first.

- In the web UI: open a session's info panel to browse available policies and toggle them.
- In chat: ask directly, e.g. *"Add a policy that asks me before running shell commands."* The agent configures it.

Server-wide or per-agent defaults are set in server config or agent YAML:

```yaml
policies:
  approve_shell:
    type: function
    handler: omnigent.policies.builtins.safety.ask_on_os_tools   # ask before shell / file writes
  cap_calls:
    type: function
    handler: omnigent.policies.builtins.safety.max_tool_calls_per_session
    factory_params:
      limit: 50                    # cap how many tools one session can call
  budget:
    type: function
    handler: omnigent.policies.builtins.cost.cost_budget
    factory_params:
      max_cost_usd: 5.00           # hard spend cap...
      ask_thresholds_usd: [3.00]   # ...with a soft warning on the way
```

Policies stack across three levels — server-wide (admin), per-agent (developer), and per-session (you) — with stricter session rules checked first. Spend caps and access limits ship as builtins. Full catalog and trust model: `docs/POLICIES.md`.

## Write your own agent

An agent is a short YAML file: prompt, tools, and optional helper sub-agents a supervisor can delegate to. Agents can author agent YAML for you — describe the agent you want in any Omnigent chat.

```yaml
name: my_agent
prompt: You are a helpful data analyst.

executor:
  harness: claude-sdk          # or: codex, codex-native, claude-native, cursor, openai-agents, pi, antigravity

tools:
  word_count:
    type: function
    callable: mypackage.mymodule.word_count

  researcher:
    type: agent
    prompt: Search for relevant information and summarize it.
    tools:
      word_count: inherit
```

```bash
omnigent run path/to/my_agent.yaml
```

The same file can declare sub-agents and reviewers — see Polly at `examples/polly/` and the full schema in `docs/AGENT_YAML_SPEC.md`.

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for environment setup, checks, and the PR process.

## Docs

### docs/AGENT_YAML_SPEC.md (excerpt)

Omnigent can run an agent from a single YAML file (`omnigent run path/to/agent.yaml`), choosing the harness/model, writing the system prompt, and declaring tools, sub-agents, OS access, and policies.

Minimal agent:

```yaml
name: hello_agent
prompt: |
  You are a concise assistant. Answer directly and ask a follow-up question when
  the request is ambiguous.

executor:
  harness: claude-sdk
  model: databricks-claude-sonnet-4-6
  auth:
    type: databricks
    profile: oss
```

`prompt` may be replaced by `instructions: AGENTS.md`; relative paths resolve from the YAML file's directory.

Common top-level fields: `name` (stable identifier), `prompt` / `instructions` (system prompt, instructions takes precedence), `executor` (harness/model/auth), `tools` (MCP tools, Python function tools, sub-agents, handoffs, inherited tools), `policies` (guardrails), `params` (typed user parameters), `os_env` (enables local OS tools — file reads/writes/edits, shell), `terminals` (named interactive terminal environments), `async` (async work tools, default `true`), `cancellable` (default `true`), `timers` (default `false`).

Executor harnesses: `claude-sdk`, `openai-agents`, `codex`, `cursor`, `pi`, `antigravity`, and more. The `cursor` harness talks only to Cursor's own backend (no Databricks gateway path) — authenticate with `CURSOR_API_KEY` or `cursor-agent login`. `antigravity` runs through Google's Antigravity SDK (`pip install "omnigent[antigravity]"`), defaults to Gemini 3.5 Flash, and can also drive Claude / GPT-OSS; it is Gemini-native with no OpenAI-compatible gateway / Databricks path.

Local OS access is declared under `os_env`:

```yaml
os_env:
  type: caller_process
  cwd: .
  sandbox:
    type: linux_bwrap
    write_paths:
      - .
    allow_network: true
```

Omitting `sandbox.type` lets Omnigent pick the platform default (`linux_bwrap` on Linux, `darwin_seatbelt` on macOS) so the same YAML works cross-platform; `sandbox.type: none` is available for trusted local development.

Tools are declared under `tools` by name: MCP servers (local command or remote `url`), Python function tools (`callable` + JSON-schema `parameters`, or `runtime: client` for client-provided tools), and sub-agent tools (`type: agent` with its own `executor`, `os_env: inherit`, `pass_history`, `max_sessions`) — each sub-agent can pick its own harness/model, so an orchestrator can mix harnesses by role (e.g. a `cursor` coder reviewed by a `claude-sdk` reviewer).

### docs/POLICIES.md (excerpt)

Policies are declarative gates that enforce rules on agent behavior, evaluated at specific enforcement points, returning one of three verdicts: **ALLOW** (proceed), **DENY** (blocked, agent gets an error), **ASK** (paused for user approval — approved becomes ALLOW, refused becomes DENY). Policies compose: multiple can be active at once, evaluated in declaration order; a DENY from any policy short-circuits the rest.

Three configuration levels, each a different persona: **Server-wide** (admin, via `policies` in server config YAML or REST API, evaluated last), **Agent spec** (developer, via `policies` in agent YAML, evaluated middle), **Session** (end user, via session settings panel in the UI, evaluated first and can short-circuit/DENY before spec or admin policies run).

Server admins register custom policy modules via `policy_modules` in server config, then declare `policies` with `type: function`, a dotted `handler` import path, and optional `factory_params`:

```yaml
# server_config.yaml
policies:
  session_budget:
    type: function
    handler: omnigent.policies.builtins.cost.cost_budget
    factory_params:
      max_cost_usd: 10.00
      ask_thresholds_usd: [5.00]
  global_rate_limit:
    type: function
    handler: omnigent.policies.builtins.safety.max_tool_calls_per_session
    factory_params:
      limit: 200
```

Agent developers add the same `policies` block at the top level of an agent's YAML (e.g. capping tool calls, scoping GitHub write access to specific repos/branches via `omnigent.policies.builtins.github.github_policy`, or scoping Google Drive access via `omnigent.policies.builtins.google.gdrive_policy`). Session users add policies through the UI's information window, or just by asking the agent in chat — Omnigent exposes a built-in `sys_add_policy` tool the agent uses to configure the policy on the user's behalf.

## Top-level structure

- `omnigent/` — main Python package (core harness, sandboxing, policy engine, builtins)
- `ap-web/` — web UI frontend (the browser/phone session interface)
- `deploy/` — deployment guide and configs (Docker, Render, Fly.io, Railway, Hugging Face Spaces, Modal)
- `designs/` — design docs (e.g. `docs/omni-upgrade-design.md` referenced from docs/)
- `dev/` — development tooling/scripts
- `docs/` — `AGENT_YAML_SPEC.md`, `POLICIES.md`, `omni-upgrade-design.md`, `images/`
- `examples/` — example agents: `polly/` (multi-harness coding orchestrator), `debby/` (dual-model brainstorming partner)
- `scripts/` — install scripts (`install_oss.sh`) and utilities
- `sdks/` — client SDKs
- `tests/` — test suite
- `.claude/`, `.github/` — agent instruction / CI config (boilerplate, not fetched)
- Root config: `pyproject.toml`, `setup.py`, `uv.lock`, `uv.toml`, `pyrefly.toml`, `railway.toml`, `render.yaml`, `openapi.json`, `LICENSE` (Apache-2.0), `NOTICE`, `SECURITY.md`, `CONTRIBUTING.md`
