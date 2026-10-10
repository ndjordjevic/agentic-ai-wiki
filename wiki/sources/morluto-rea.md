---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/morluto/rea
tags:
  - reverse-engineering
  - mcp-server
  - binary-analysis
  - ghidra-hopper-ida
  - electron-javascript-analysis
  - evidence-provenance
  - agent-setup-cli
  - local-first-analysis
related:
  - integuru.com
  - mukul975-anthropic-cybersecurity-skills
  - SnailSploit-Claude-Red
product: rea
detail_level: standard
created: 2026-10-10
updated: 2026-10-10
---

REA ("Reverse Engineer Anything", `rea-agents` on npm) is an MIT-licensed TypeScript MCP server and matching CLI (58K+ stars, v6.3.0) that lets a coding agent reverse-engineer software it has no source for — native binaries, JavaScript/Electron apps, .NET assemblies, Android APKs, firmware, EVM bytecode, websites and live process behavior — and return findings together with the evidence, limitations and unknowns behind each conclusion. Its pitch is feature-level: "see a feature you like, understand how it works, down to the binary level," then have the agent build a similar version in your own project. It matters for this wiki as a large, agent-first example of wrapping heavyweight expert tooling (Hopper, Ghidra, IDA, JADX, Binwalk) behind one provider-neutral MCP surface with strict evidence contracts.

_All claims below are sourced from ../../raw/github/morluto-rea.md unless otherwise noted._

## What it does

REA connects an agent (or a terminal user) to local analysis tools. The agent calls REA through MCP to inspect a target and trace relevant code; REA returns findings with their evidence, and the agent uses them to ask follow-up questions, explain behavior, or write and test an implementation. CLI commands run the same workflows. All analysis is local — REA does not upload targets, though the agent's model provider sees the tool results.

What it returns depends on the target:

| Target | Returns | Requirements |
|---|---|---|
| Native binaries | Pseudocode, assembly, strings, symbols, calls, references | Hopper, Ghidra or IDA |
| Offline ELF layout / recorded Linux crashes | Sections, segments, relocations, mitigations; registers/signals per thread | Caller-supplied pwntools (optional GDB/pwndbg) |
| EVM bytecode | Dispatch selectors, inferred arguments and mutability | Local raw/hex input |
| JavaScript / Electron | Modules, imports, source maps, routes, IPC, native add-on links | Node.js and npm only |
| Websites / saved network captures | Page structure, scripts, network observations, screenshots; HAR requests/responses | Chrome-family browser; mitmdump on Linux |
| .NET assemblies | Metadata, CIL, native dependencies, build comparisons | None (static) |
| Android APKs | Manifest, classes, decompiled methods, references | Headless JADX + JDK |
| Firmware | Regions, extraction results, handoffs to native analysis | Binwalk / Unblob on Linux |
| Process behavior | Terminal output, interactions, exit/filesystem observations, run comparisons | Linux/macOS native PTY |

Static JavaScript and .NET inspection never run the target; runtime capture runs or interacts with it under the user's permissions.

## Installation

Requires Node.js 22.x (≥22.19), 24.x (≥24.11) or 26+, plus npm. One command registers the MCP server and installs matching workflow instructions (a skill) for chosen agents, showing planned changes and backing up existing config before writing:

```bash
npx rea-agents setup
```

Supported setup targets include Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, Windsurf, Devin, OpenCode, Antigravity, GitHub Copilot CLI, Qwen Code, VS Code, Grok Build, Pi, Hermes and others; any local-MCP client can register manually (REA also ships an MCP Registry `server.json`). For regular CLI use: `npm install --global rea-agents`, then `rea update` to stay current. The `reverse-engineer-anything` skill is also published on skills.sh, but skill-only installation does not register the MCP server.

Native analysis needs a provider: setup can install Hopper after approval; Ghidra and IDA are bring-your-own. Setup is additive and idempotent and never installs unrelated software (Homebrew, Node, Java, Ghidra).

## Key features

- **One MCP for many formats** — native, managed, JS/Electron, Android, firmware, EVM, web and process targets behind provider-neutral tool names, with per-provider coverage reported rather than hidden.
- **Evidence-first results** — every result carries artifact/provider identity, source locations, Evidence references, confidence and limitations inline; observations, derivations, inferences and unknowns are kept distinct, and "missing coverage is unknown, not absence."
- **Six guided MCP prompts** — `investigate_feature`, `compare_application_versions`, `verify_reconstruction`, `trace_crash`, `audit_residual_unknowns`, `prepare_bounded_process_capture` — optional starting points that never invoke tools themselves; arguments are treated as untrusted data.
- **Session-aware completion** — MCP `completion/complete` suggests live documents, procedures, providers, Evidence IDs and residual unknowns from the current session.
- **Deterministic provider selection** — with several native providers available REA requires an explicit `--provider` / `provider_id` (or `REA_ANALYSIS_PROVIDER`) and never falls back silently.
- **Read-only engine usage** — Ghidra uses ephemeral databases without modifying bytes; IDA analysis is read-only and never saves an attached GUI database.
- **Large-evidence views** — complete JS application Evidence can reach hundreds of MB (334 MB for Obsidian); `inspect-analysis-view` projects a ~10 KB summary, module page or single module from saved Evidence.

## Architecture

Layered with dependencies flowing inward: pure `src/domain/` (evidence, comparisons, application graphs) → `src/contracts/` (caller-visible schemas, shared error algebra) → provider adapters → shared `src/application/` workflows → thin CLI (`src/cli.ts`) and MCP stdio server (`src/main.ts`, `src/server/`) adapters, both dispatched from `scripts/rea.mjs`. A `SessionProviderRouter` binds one immutable deep provider per target, and an `EvidenceLedger` owns retained Evidence and residual unknowns per session.

Provider adapters include `src/hopper/` (launch + Unix-socket protocol to `bridge/hopper_bridge.py` running inside Hopper), `src/ghidra/` (packaged headless Java bridge), `src/ida/` (adapting the external `ida-pro-mcp`), `src/browser/` (CDP/Playwright capture), `src/inspector/` (passive V8 Inspector), `src/dotnet/`, `src/android/` (pinned headless JADX), `src/firmware/` (Binwalk/Unblob), `src/evm/` (EVMole in a bounded worker) and `src/native/pwntools|pwndbg`. A shared `src/process/` layer owns process groups, private roots, deadlines and cleanup; `native/windows/` adds a Node-API module for Job Objects and DACLs. Upstream engines live unmodified as submodules in `third_party/`, and REA never downloads engines during an analysis operation.

The repo's tool-design guide shapes the MCP surface: design around the analyst question, choose among task shapes (`inspect`, `search`/`list`, `trace`, `compare`, `workflow`, `observe`/`capture`), prefer reusable primitives and compose workflows only when repeated use demonstrates the need, return complete evidence inline, and add limits only for real format, protocol, authority or measured resource constraints — "an assumed agent budget is insufficient justification for a limit."

## Example usage

Ask the agent in natural language:

```text
Understand how search works in the Notes app, show me the evidence, and build a
similar feature for my project.
```

From the terminal:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
rea analyze /absolute/path/to/program --provider ghidra --json
rea decompile /absolute/path/to/program 0x1000 --provider ghidra --json
rea trace /absolute/path/to/program "search" --provider ghidra --json
rea providers --json
```

Published showcases include reconstructing DX-Ball's sound-pan calculation into C (passing 3,205 original-x86 cases and reproducing all 63 compiled function bytes), tracing Notion's Electron clipboard bridge from renderer through preload/IPC to the main process, and recovering a 16-bit PC-98 bullet-ring calculation in TH04.

## Maintenance status

Very active: 58,387 stars, 11,518 forks, latest release `rea-agents-6.3.0` (2026-10-09), last push 2026-10-10, MIT license, release-please-driven releases with a ~285 KB changelog, README in 18 languages, and a Discord community. Roadmap priorities: broader native architecture/type/indirect-call verification, linking static findings with runtime observations, obfuscated managed-code comparisons, and extended process/protocol coverage; new capabilities must pass real-provider verification lanes. The project disclaims illegal or unauthorized use and states it has issued no cryptocurrency token.
