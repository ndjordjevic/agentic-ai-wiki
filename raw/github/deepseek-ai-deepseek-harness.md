# deepseek-ai/deepseek-harness

## Metadata
- Stars: 189,060
- Primary language: TypeScript
- Default branch: master
- Latest release: v0.1.1-rc.2 (2026-08-21)
- License: MIT
- Homepage: https://deepseek.com/harness
- Fetched: 2026-08-24
- Final URL: https://github.com/deepseek-ai/deepseek-harness

## Description
DeepSeek Harness: Everything is a Plugin.

## README

# DeepSeek Harness

English | [中文](README.zh.md)

DeepSeek Harness (`dsh`) is an open-source agent harness developed by [DeepSeek AI](https://deepseek.com).

It uses an architecture where **everything is a plugin**, and is powered by [Cordis](https://github.com/cordiverse/cordis), whose design is described in [_A Programming Paradigm for Spatiotemporal Composability_](https://github.com/cordiverse/paper).

## Developer preview

DeepSeek Harness is currently in _developer preview_ and is iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.**

## Run

### Run from `npm`

Install `Node.js`, then run:

```sh
npx @deepseek-ai/dsh web
```

The command starts the Web UI at `http://127.0.0.1:3080` by default and opens it in the default browser for a local launch. An SSH launch only prints the host URL because the SSH client or editor owns the local forwarded address. Pass `--no-open` to run the server without opening a browser. See [Web UI guide](docs/user/guide/index.md).

### Run from source

To run from a repository checkout:

```sh
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

`pnpm run build` prepares the repository artifacts. `pnpm dsh web` uses those built artifacts without rebuilding.

## Community and support

- Feel free to submit feedback or bug reports through [GitHub Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions).
- Add the [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic to your plugin repository for discoverability.
- Join the DeepSeek Harness Discord community.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Development

Start with the [development guide](docs/development.md) and [architecture documentation](docs/architecture.md).

For agents, follow [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)

## Docs

### Architecture

# DeepSeek Harness Architecture

Read this before changing anything under `packages/`. It assumes you know Cordis; if you do not, start with the primer or the tutorial.

## Cordis

Cordis is the framework under dsh: plugins contribute services, typed events, and reversible effects to a shared context. Every part of the product is a plugin, including the model adapter, the tool registry, the session log, and the agent loop itself, so every part is replaceable from configuration.

There is no privileged core to patch: you extend dsh by mounting a plugin beside the others, and registrations are effects that unwind when their plugin unloads.

## Profiles and bundles

A running `dsh` is a plugin tree composed at boot from ordered layers.

A **profile** is a named composition stored in the Harness home. It lists the bundles it stacks, holds any out-of-tree plugins it installs, and keeps the user's own `cordis.patch.yml`. `web` and `headless` ship as templates.

A **bundle** is a distribution format for Cordis config rows and the code they mount, so whatever it inserts stays patchable by the layers above it.

Each declares itself in its own `package.json` under a `dsh` field: `dsh.profile` lists a profile's bundles, and `dsh.bundle` points at a bundle's patch file.

`dsh-base` is the first layer of every profile: model adapters, tools, persistence, sandbox and approval policy, settings, credentials, telemetry. `dsh-web-app` adds the browser application; `dsh-headless` adds a one-shot runner with no server at all.

Layers apply to an empty entry list in this order: each bundle in the profile's listed order, then the profile's `cordis.patch.yml`, then the home-level one, then any `--patch` overlay. A patch targets a row by id and replaces its whole config, or inserts new rows.

To see the tree your machine actually boots:

```sh
dsh --profile web --dump-config
```

## Core packages

| Package | Owns | `ctx` key |
|---|---|---|
| `core/session` | Append-only `SessionEvent` log and in-memory store | `ctx.sessions` |
| `core/system-prompt` | Prompt-section and tool-schema assembly | `ctx.systemPrompt` |
| `core/tools` | Scoped tool registry and guarded execution pipeline | `ctx.tools` |
| `core/agent` | The `Agent` interface, live registry, and `agent/*` events | `ctx.agents` |
| `core/agent-loop` | Default driver implementing that interface | `ctx.agentLoop` |
| `core/scope` | Per-agent scoped-registration primitive | library, no key |
| `llm/llm` | Message and stream vocabulary plus the adapter seam | `ctx.llm` |

## Events

Events are the extension points, and picking the right domain is the first decision in most changes.

- **Session events** are durable facts appended to the log and broadcast through `session/event`. Use one when the fact must survive a reload.
- **Agent events** (`agent/*`) carry a live `Agent`: inbox, step, status, request, validation, continuation. Use one to observe or intercept work in flight.
- **Capability events** attach policy and adapters to a seam (`fs/*`, `tools/*`, `telemetry/*`) without importing the loop.

## Turn flow

```
turn/start
  claim next-step input plus one queued message
  assemble prompt sections + tool schemas
  -> agent/pre-step                   reject | enter(messages)
     step/start
     append entered messages as user/message
     derive model history from the log
     agent/request -> llm/stream -> assistant/chunk* -> assistant/message
     tool/call* -> tools/pre-execute -> tools/execute -> tools/post-execute -> tool/result*
     step/end
  -> agent/turn-stopping
turn/end
```

## Capability seams

A **seam** is a swappable capability with three roles: a **Service Definition** declaring the interface, a **Service Provider** implementing it, and a **Consumer** using it, commonly a model-facing tool. A package may combine roles, but one role alone is not a seam; adding a capability means designing all three.

Seams are why one provider swap changes the whole product. Filesystem and subprocess providers share one execution world, so pointing them at a remote sandbox moves Bash, PTY, and LSP with them, with no provider forks.

## Where new behavior goes

| Goal | Mechanism |
|---|---|
| Add a model provider | register its adapter on `ctx.llm` |
| Add a model-facing capability | register on `ctx.tools`; its schema joins prompt assembly |
| Give one session a different capability set | compose an agent preset; a service row there needs an `isolate` realm |
| Add shell execution | register a `ctx.shell` backend; the local one spawns through `ctx.subprocess` |
| Add persistent terminal execution | register a `ctx.terminals` backend plus `dsh-tool-terminal` |
| Add a human command | register on `ctx.commands`; it dispatches without a model turn |
| Add background work | register on `ctx.jobs`; `job_*` tools collect or stop it |
| Add filesystem access or policy | register a `ctx.fs` provider or listen to `fs/*` events |
| Confine spawned processes | use a `ctx.sandbox` backend; consumers wrap argv before spawning |
| Intercept a request, tool, or turn | use its `agent/*` or `tools/*` event |
| Add model-facing context | call `agent.inject()`; it lands in the next admitted request |
| Add UI or editor integration | drive `ctx.agents` and render from `session/event` |
| Add durable session state | extend `SessionEventMap`; render and replay from the log |
| Fork a live session | `ctx.sessions.fork(source, boundary?, childSessionId?)` |

### Cordis Primer (excerpt)

Cordis is the vendored plugin framework underneath DeepSeek Harness.

**Five ideas:**
- A plugin is an object that implements Service — a function with optional `inject` and `apply(ctx)` fields, or a `Service` subclass.
- A context is a repository of services claiming a stable `ctx.<key>`.
- Declare service dependency via `inject` — a plugin waits until required services exist.
- Typed events for communication — `emit`, `waterfall`, `parallel`, or `serial`.
- Registrations are reversible effects — installed through `ctx.effect()` or `ctx.on()` so reload and teardown unwind them predictably.

**Dispatch modes:**
| Mode | Awaited? | Dispatch Order | Has Return Value? |
|---|---|---|---|
| `emit` | No | listeners in registration order | No |
| `waterfall` | No | listeners in registration order | Yes |
| `parallel` | Yes | all listeners in parallel | No |
| `serial` | Yes | listeners in registration order | Yes |

### Tool catalog (selected tools)

Model-facing tools contributed by shipped plugins. The full generated catalog is in `docs/tool-catalog.md`.

Key tools: `bash`, `pwsh`, `str_replace_editor`, `edit/read/read_image/write`, `glob/grep`, `web_search/web_fetch`, `subagent`, `subagent_fork`, `workflow`, `skill`, `ask_user_question`, `todo_write`, `exit_plan_mode`, `lsp`, `run_code`, `cordis_define/inspect/run` (experimental), `schedule_create/delete/list`, `terminal_open/send/read/close`, `job_kill/list/output`, `session_event_read/search`.

## Top-level structure

```
vendor/      Vendored Cordis source
packages/    @deepseek-ai/dsh-<pkg> workspaces
  core/        product API spine: session, system-prompt, tools, agent, agent-loop
  api/         Remote BFF assembly and Typert RPC gateway
  typert/      type graph generator, loader, and runtime registry
  llm/         LLM capability: Service Definition/Consumer + DeepSeek providers
  e2b/         E2B POC: sandbox + FS/subprocess adapters
  shell/       bash capability: providers + shell Consumers
  subprocess/  subprocess capability + local process-tree provider
  terminal/    persistent sessions
  fs/          filesystem capability + policy
  lsp/         language-server capability
  skill/       skill provider registry + local impl + catalog/loader tool
  web/         web capability: Service Definition + search/fetch providers + tool Consumer
  compaction/  compaction capability + basic provider
  context/     request-context plugins
  subagent/    subagent capability: Service Definition + providers + delegation Consumers
  bundle/      installable dsh --profile patch-layer bundles
  workflow/    workflow capability + worker-thread provider + tool Consumer
  todo/        todo_write tool
  plan/        plan mode as logged state
  preset/      per-session agent composition from preset cordis.yml files
  guard/       loop-hygiene + tool-timeout plugins
  self-modification/  the agent inspects/mounts its own plugins
  hooks/       Claude Code/Codex hook bridges + wire-protocol library
  session/     durable session data: persistence, projection, titles, telemetry
  credentials/ credential/authorization capabilities + env/.env provider
  acp/         automation-only Agent Client Protocol server
  sdk/         JSON-RPC protocol, server, and TypeScript client
  experimental/ private prototypes excluded from official releases
python/      Python SDK and bundled runtime
native/      @deepseek-ai/node-addon-landlock-run source
examples/    Runnable cordis.yml leaves: acp-agent, headless-agent, jsonrpc-agent, mcp-memory, web-cordis, web-schedule
docs/        architecture, generated catalogs, postmortems, cookbook
  subsystems/    per-core-package subsystem docs
  cookbook/      extension cookbook: packages, tools, LLM adapters, Chat nodes, settings cards
  cordis-tutorial/  hands-on Cordis walkthrough
scripts/     repo gates and generators
website/     VitePress projection of bilingual docs
AGENTS.md    Agent contributor guide (repo layout, commands, conventions)
CLAUDE.md    Same content (Claude Code entry point)
```
