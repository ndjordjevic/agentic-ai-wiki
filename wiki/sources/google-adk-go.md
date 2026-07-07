---
type: source
source_url: https://github.com/google/adk-go
tags:
  - adk
  - google-adk
  - go-sdk
  - multi-agent
  - graph-workflows
  - gemini
  - mcp
  - a2a-protocol
  - cloud-native
related:
  - adk.dev
  - langchain.com-langgraph
  - strandsagents.com
  - microsoft-agent-framework
  - crewai.com
  - pydantic.dev
  - agents-cli
  - trigger.dev
  - microsoft-autogen
product: adk
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

**ADK Go** (`google.golang.org/adk/v2`) is Google's open-source, code-first Go implementation of the Agent Development Kit — a modular framework for building, evaluating, and deploying production AI agents with idiomatic Go patterns, strong concurrency, and cloud-native deployment (notably Google Cloud Run). v2.0.0 (June 2026) ships a graph-based workflow engine, unified agent context, MCP and A2A integrations, and parity-oriented alignment with the Python ADK. It complements the canonical docs and Python runtime documented in [[adk.dev]].

_All claims below are sourced from ../../raw/github/google-adk-go.md unless otherwise noted._

## What it does

ADK Go applies software-engineering principles to agent development: agents, tools, sessions, memory, artifacts, plugins, and a `runner` execution loop are composed in Go for testability and versioning. Agent runs stream `iter.Seq2[*session.Event, error]` events; the `runner` drives the reasoning→tool→response loop. A separate `workflow` package provides graph-based orchestration (nodes, edges, branches, joins, retries, human-in-the-loop, dynamic scheduling) for multi-agent systems. While optimized for Gemini via `model/gemini`, the framework is model-agnostic and deployment-agnostic.

## Key features

- **Idiomatic Go** — interface-first design (`Agent`, `Tool`, `Toolset`, `Service`); callbacks over subclassing (`Before*`/`After*` hooks short-circuit execution).
- **Rich tool ecosystem** — `functiontool.New[Args, Results]` wraps Go functions; built-in toolsets include `mcptoolset/` (MCP), `skilltoolset/`, `agenttool`, `geminitool`, memory/artifact loaders.
- **Graph workflow engine** (`workflow/`) — agent nodes, function nodes, tool nodes, branch/join, retry loops, parallel workers, HITL, dynamic nodes, persistence.
- **Multi-agent patterns** — `workflowagents/` and `examples/multiagent`, `examples/workflowagents`; A2A support via `server/adka2a` and `examples/a2a`.
- **MCP integration** — `tool/mcptoolset` using `github.com/modelcontextprotocol/go-sdk`.
- **Session & memory** — `session/` for conversation state/events; `memory/` and `artifact/` for long-term recall and file services.
- **Server surfaces** — `server/adkrest` (primary REST), `adka2a` (Agent-to-Agent), `agentengine`; `cmd/adkgo` CLI.
- **Observability** — OpenTelemetry in `telemetry/` with OTLP exporters.
- **Offline-first tests** — HTTP replay via vendored `internal/httprr`; no live LLM calls in CI.
- **Launcher pattern** — examples use `full.NewLauncher()` (console, REST, A2A, web UI) or `prod.NewLauncher()` (REST + A2A).

## Architecture

Package layout mirrors ADK's conceptual model across languages:

| Package | Role |
|---|---|
| `agent/` | Core `Agent` interface; `llmagent`, `workflowagents`, `remoteagent`; unified `Context` |
| `runner/` | Execution engine — drives the agent run loop, agent nodes, HITL integration |
| `workflow/` | Graph engine — `Workflow`, nodes (`agent_node`, `function_node`, `tool_node`, `join_node`), scheduler, branch isolation, retry, state persistence |
| `model/` | LLM abstraction — `gemini`, `apigee` adapters atop `google.golang.org/genai` |
| `tool/` | Tool interfaces and implementations — function tools, MCP, skills, confirmations |
| `session/` | Events, conversation state; v2 requires `context.Context` in `NewEvent` for replay-safe IDs/timestamps via `platform/` |
| `memory/`, `artifact/` | Long-term memory search and file artifact services |
| `plugin/` | Cross-cutting lifecycle hooks across run/agent/model/tool |
| `server/` | HTTP serving layers for REST, A2A, and Agent Engine deployment |
| `platform/` | Injectable time/UUID providers for deterministic tests and workflow replay |

Streaming is the default consumption pattern — collect events with `for event, err := range r.Run(...)` rather than buffering slices. Python ADK is the behavioral source of truth; Go ports validate parity.

## Installation

```bash
go get google.golang.org/adk/v2
```

Requires Go 1.25+. Set `GOOGLE_API_KEY` (or Vertex AI credentials) for Gemini model access.

## Example usage

```go
model, err := gemini.NewModel(ctx, "gemini-2.5-flash",
    &genai.ClientConfig{APIKey: os.Getenv("GOOGLE_API_KEY")})
a, err := llmagent.New(llmagent.Config{
    Name:        "assistant",
    Model:       model,
    Instruction: "You are a helpful assistant.",
    Tools:       []tool.Tool{ /* functiontool or mcptoolset tools */ },
})
r, err := runner.New(runner.Config{
    AppName:           "my-app",
    Agent:             a,
    SessionService:    session.InMemoryService(),
    AutoCreateSession: true,
})
msg := genai.NewContentFromText("Hello", genai.RoleUser)
for event, err := range r.Run(ctx, userID, sessionID, msg, agent.RunConfig{}) {
    // handle err; read event.LLMResponse.Content
}
```

See `examples/quickstart` for a runnable program. Run `go run ./examples/quickstart/main.go help` for launcher options (console, REST API, A2A, web UI).

## Maintenance status

- **8,403 stars**, 733 forks (fetched 2026-07-07)
- **Latest release:** v2.0.0 (2026-06-30)
- **License:** Apache 2.0 (exception: `internal/httprr`)
- **Default branch:** `main`
- **Docs:** https://google.github.io/adk-docs/
- **Sibling implementations:** Python, Java, ADK Web — independent codebases sharing conceptual model
- **Community:** r/agentdevelopmentkit subreddit; Code Wiki at codewiki.google
