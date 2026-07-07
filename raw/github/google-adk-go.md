# google/adk-go

## Metadata
- Stars: 8403
- Primary language: Go
- Default branch: main
- Latest release: v2.0.0 (2026-06-30)
- License: Apache License 2.0
- Homepage: https://google.github.io/adk-docs/
- Fetched: 2026-07-07
- Final URL: https://github.com/google/adk-go

## Description
An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

## README
# Agent Development Kit (ADK) for Go

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Go Doc](https://img.shields.io/badge/Go%20Package-Doc-blue.svg)](https://pkg.go.dev/google.golang.org/adk/v2)
[![Nightly Check](https://github.com/google/adk-go/actions/workflows/nightly.yml/badge.svg)](https://github.com/google/adk-go/actions/workflows/nightly.yml)
[![r/agentdevelopmentkit](https://img.shields.io/badge/Reddit-r%2Fagentdevelopmentkit-FF4500?style=flat&logo=reddit&logoColor=white)](https://www.reddit.com/r/agentdevelopmentkit/)
[![View Code Wiki](https://www.gstatic.com/_/boq-sdlc-agents-ui/_/r/YUi5dj2UWvE.svg)](https://codewiki.google/github.com/google/adk-go)

Agent Development Kit (ADK) is a flexible and modular framework that applies software development principles to AI agent creation. It is designed to simplify building, deploying, and orchestrating agent workflows, from simple tasks to complex systems. While optimized for Gemini, ADK is model-agnostic, deployment-agnostic, and compatible with other frameworks.

This Go version of ADK is ideal for developers building cloud-native agent applications, leveraging Go's strengths in concurrency and performance.

---

## ✨ Key Features

*   **Idiomatic Go:** Designed to feel natural and leverage the power of Go.
*   **Rich Tool Ecosystem:** Utilize pre-built tools, custom functions, or integrate existing tools to give agents diverse capabilities.
*   **Code-First Development:** Define agent logic, tools, and orchestration directly in Go for ultimate flexibility, testability, and versioning.
*   **Modular Multi-Agent Systems:** Design scalable applications by composing multiple specialized agents.
*   **Deploy Anywhere:** Easily containerize and deploy agents, with strong support for cloud-native environments like Google Cloud Run.

## 🚀 Installation

To add ADK Go to your project, run:

```bash
go get google.golang.org/adk/v2
```

## 📄 License

This project is licensed under the Apache 2.0 License - see the
[LICENSE](LICENSE) file for details.

The exception is internal/httprr - see its [LICENSE file](internal/httprr/LICENSE).

## Docs

### AGENTS.md (agent instructions for contributors)

ADK Go (`google.golang.org/adk/v2`) is an open-source, code-first Go toolkit for building, evaluating, and deploying AI agents. It is model-agnostic but optimized for Gemini, and is one of three ADK implementations — Go, Python, and Java — that share a conceptual model but are independent codebases. Requires Go 1.25+.

**Repository layout:**
- `agent/`     Agent interface + types (`llmagent`, `workflowagent(s)`, `remoteagent`)
- `runner/`    Execution engine that drives the run loop
- `workflow/`  Node/graph-based workflow engine for multi-agent apps
- `model/`     LLM abstraction (`gemini`, `apigee`)
- `tool/`      Tool/Toolset interface + built-in tools (incl. `skilltoolset/`, `mcptoolset/`)
- `session/`   Conversation state + events
- `memory/`, `artifact/`   Long-term memory and file/data services
- `plugin/`    Cross-cutting lifecycle hooks
- `server/`    HTTP servers (`adkrest` is primary; `adka2a`, `agentengine`)
- `cmd/`       CLI (`adkgo`) and server launchers
- `telemetry/`, `util/`   Public helper packages
- `platform/`  Overridable seams for time & UUID generation (deterministic tests)
- `internal/`  Private packages — NOT public API; `internal/httprr` is vendored
- `examples/`  Runnable example agents (quickstart, tools, a2a, skills, …)

**Conventions:**
- Streaming: agent runs return `iter.Seq2[*session.Event, error]`; consume with `for event, err := range … {}`.
- Interface-first: public packages expose interfaces (`Agent`, `Tool`, `Toolset`, `Service`).
- Callbacks over subclassing (`Before*`/`After*` for Agent/Model/Tool); returning non-nil from a `Before` callback short-circuits execution.
- Tests run offline by default via `testdata/*.httprr` HTTP replay.

**Minimal example:**
```go
model, err := gemini.NewModel(ctx, "gemini-2.5-flash",
    &genai.ClientConfig{APIKey: os.Getenv("GOOGLE_API_KEY")})
a, err := llmagent.New(llmagent.Config{
    Name:        "assistant",
    Model:       model,
    Instruction: "You are a helpful assistant.",
    Tools:       []tool.Tool{ /* ... */ },
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

**Extending the framework:**
- Add a tool: `functiontool.New[Args, Results](cfg, handler)` or implement `tool.Tool`.
- Add a toolset: implement `tool.Toolset`.
- Add cross-cutting behavior: register `plugin.New(plugin.Config{...})` hooks.

**Alignment:** adk-python is the source of truth for feature behavior; Go port checks parity with Python.

### README-v2.md (v2.0 breaking changes excerpt)

- `session.NewEvent` now requires `context.Context` as first argument for deterministic, replay-safe events via `platform.WithTimeProvider` / `platform.WithUUIDProvider`.
- ToolContext and CallbackContext merged into unified `agent.Context`; mocks should embed `agent.StrictContextMock`.

### examples/README.md

Examples are minimal, feature-focused samples (distinct from `google/adk-samples` e2e repo). Many use `full.NewLauncher()` supporting console, REST API, A2A, and web UI launch modes. `prod.NewLauncher()` builds in REST API and A2A only.

## Top-level structure

| Path | Type | Notes |
|---|---|---|
| `.github/` | dir | CI workflows (nightly check badge) |
| `agent/` | dir | Agent interface, `llmagent`, `workflowagents`, `remoteagent`, context types |
| `artifact/` | dir | File/data artifact services |
| `cmd/` | dir | CLI (`adkgo`) and server launchers |
| `examples/` | dir | Runnable samples: quickstart, tools, a2a, mcp, multiagent, workflow, skills, vertexai, web, rest, telemetry, bidi, agentengine, toolconfirmation, workflowagents |
| `internal/` | dir | Private packages; `httprr` vendored HTTP replay for tests |
| `memory/` | dir | Long-term memory services |
| `model/` | dir | LLM abstraction (`gemini`, `apigee`) |
| `platform/` | dir | Overridable time/UUID providers for deterministic tests |
| `plugin/` | dir | Cross-cutting lifecycle hooks |
| `runner/` | dir | Execution engine driving the agent run loop |
| `scripts/` | dir | Build/utility scripts (`adk-web`) |
| `server/` | dir | HTTP servers: `adkrest` (primary), `adka2a`, `agentengine` |
| `session/` | dir | Conversation state and events |
| `telemetry/` | dir | OpenTelemetry integration |
| `tool/` | dir | Tool/Toolset interfaces; `functiontool`, `mcptoolset`, `skilltoolset`, `agenttool`, `geminitool`, etc. |
| `util/` | dir | Public helper packages |
| `workflow/` | dir | Graph-based workflow engine: nodes, edges, branches, joins, retries, HITL, dynamic scheduling |
| `AGENTS.md` | file | AI agent contributor instructions |
| `CLAUDE.md` | file | Claude Code context |
| `GEMINI.md` | file | Gemini CLI context |
| `CONTRIBUTING.md` | file | Human contributor guide |
| `README.md` | file | Project overview |
| `README-v2.md` | file | v2.0 migration notes |
| `go.mod` | file | Module `google.golang.org/adk/v2`, Go 1.25.0 |
| `LICENSE` | file | Apache 2.0 |

**Key dependencies (go.mod):** `google.golang.org/genai`, `github.com/modelcontextprotocol/go-sdk`, `github.com/a2aproject/a2a-go`, OpenTelemetry exporters, GCP (`cloud.google.com/go/aiplatform`, storage), SQLite (`glebarez/sqlite`).

**Related ADK implementations:** [Python ADK](https://github.com/google/adk-python), [Java ADK](https://github.com/google/adk-java), [ADK Web](https://github.com/google/adk-web). Docs: https://google.github.io/adk-docs/
