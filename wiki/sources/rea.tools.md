---
type: source
category: "MCP servers & integrations"
source_url: https://rea.tools/
companion_urls:
  - https://github.com/morluto/rea
raw_files:
  - ../../raw/web/rea.tools.md
  - ../../raw/github/morluto-rea.md
tags:
  - reverse-engineering
  - mcp-server
  - feature-reconstruction
  - binary-analysis
  - electron-ipc-tracing
  - browser-runtime-capture
  - evidence-provenance
  - compiler-matching-reconstruction
related:
  - morluto-rea
  - integuru.com
  - mukul975-anthropic-cybersecurity-skills
  - SnailSploit-Claude-Red
product: rea
detail_level: standard
created: 2026-10-15
updated: 2026-10-28
---

rea.tools is the website for REA ("Reverse Engineering for Your Coding Agent"), the open-source MCP server and CLI captured in [[morluto-rea]]. The repo documents the tool surface; the site teaches the workflow. It sends a beginner from a pasted setup prompt to a first investigation, then through worked guides (native binary, Electron app, browser request) and case studies (Aegis APK, a CTF flag checker, DX-Ball, Notion, Touhou TH04) in which an agent reads a program's code and rebuilds one feature with a verifiable check. It also runs a research blog about model capability for agentic reverse engineering. For this wiki it is a clear example of an agent-tool project built around *show, then verify*: each claim on the site comes with the REA output, the recovered code, and the check that confirmed it.

_All claims below are sourced from ../../raw/web/rea.tools.md unless otherwise noted._

## What it does

REA gives a coding agent tools to inspect the code behind a question about an app, game or website. The site describes a three-step loop: **ask about one feature** (give the agent a program or page and a question), **inspect the program** (REA returns code, references and runtime observations), and **explain it, then try a change** (the agent uses the findings to explain or rebuild the feature). Reverse engineering is framed as "learning how software works by inspecting the program itself."

The landing page demonstrates the loop with two interactive examples. In the first, REA reads the running script of Chrome's dinosaur game. It recovers `SPEED: 6`, `ACCELERATION: 0.001`, `MAX_SPEED: 13`, checks the result by calling the original update function 4,000 and 10,000 times, and then rebuilds the rule in a mini-game with a speed slider. In the second, REA reads Windows Calculator's `%` handler from the installed DLL (`CMP EAX, 0x5c` / `0x5b`, `MOV EDX, 0x64`). It recovers the two rules ("after + take a percentage of the first number; after × turn 10% into 0.1"), and the agent cross-checks the branch against Microsoft's public source.

## Key features

- **One-prompt setup** — paste "Install REA and connect it to this coding agent using npx rea-agents@latest setup. Show me the setup plan for approval, then verify the installation." Setup adds the MCP connection and the matching investigation skill, backs up existing config, and asks before applying changes.
- **Broad client support** — setup IDs for Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, Windsurf, Devin, OpenCode, Antigravity, GitHub Copilot CLI, Command Code, Qwen Code, VS Code, Grok Build, OMP, Pi and Hermes. Qoder, Factory Droid, Trae, ZCode and DeepSeek Harness are available on `main`, and Grok Bot connects from its chat via `npx -y rea-agents@6.4.0 mcp`.
- **Pluggable native providers** — Hopper (macOS/Linux; setup can install it), Ghidra 12.1.x with JDK 21+ (macOS/Linux; experimental read-only on Windows x64), or an existing IDA setup registered through an `ida-mcp.json` file (attached GUI or headless supervisor).
- **Many target types** — the site's target table covers JavaScript/Electron, websites, .NET/Flutter packages, Android APKs, devices and resources, JEB projects, firmware, WASM, SQLite, EVM bytecode, ELF crashes, HAR/SAZ/mitmproxy captures, PCAP, logic signals, and PTY process behavior. Each links to a per-target guide in the repo.
- **Evidence-backed answers** — the guides show the actual REA output (instructions, callers, decoded constants, IPC pairing counts, captured requests) next to the agent's interpretation. They state the limits explicitly: an IPC path "is inferred from code; a runtime capture can check what executes", and computed channel names can remain unresolved.
- **Local analysis** — "REA analyzes targets on your machine"; only the results reach the agent's model provider.
- **New in the repo since the earlier capture** — Go and Rust binary metadata, WASM, SQLite, ADB devices, JEB, Apktool resources, Flutter, packet and signal recordings, caller-supplied GNU objdump and Rizin, and a Kuna decompiler provider. (../../raw/github/morluto-rea.md)

## Architecture

REA is a layered TypeScript system. A pure domain layer (evidence, comparisons, application graphs) sits under caller-visible contracts. Provider adapters (Hopper, Ghidra, IDA, browser/CDP, V8 Inspector, .NET, JADX, Binwalk/Unblob, EVM, pwntools/pwndbg) feed shared application workflows, which are exposed through a thin CLI and an MCP stdio server. A session router binds one deep provider per target, and an evidence ledger tracks retained evidence and residual unknowns. Upstream engines are kept unmodified as submodules in `third_party/`. (../../raw/github/morluto-rea.md)

The site's guides show which layer does what. In the Electron guide, REA builds a map of entrypoints, modules and process boundaries, then pairs the literal `ipcRenderer.invoke("notes:export")` with its `ipcMain.handle` (`literal_channels: 1`, `paired_renderer_transmissions: 1`). In the browser guide, REA attaches to an existing Chrome over the remote-debugging port and records requests during an observation window, including their initiating script and JSON response shape. The user keeps control of the page throughout.

## Installation

Requires Node.js 22.19+, 24.11+ or 26+ with npm (or Bun, where `bunx` replaces `npx`). On Windows, use `npx.cmd` if PowerShell blocks scripts.

```bash
npx rea-agents@latest setup                 # interactive: pick client(s), review plan
npx rea-agents@latest setup --client codex  # one specific client
npx -y rea-agents@latest doctor --client codex --json   # expect "healthy": true
npm install --global rea-agents             # optional permanent `rea` command; update with `rea update`
```

Native providers are checked with `doctor --provider hopper|ghidra|ida`. For Ghidra, set `GHIDRA_INSTALL_DIR` and `JAVA_HOME`, then rerun setup. Installing only the skill from [[skills.sh]] is not enough, because setup must register the MCP server. On Linux, Ghidra, JADX, firmware launches and static JS/Electron analysis need a procps-compatible `ps` on `PATH`. The README also warns users to get REA only from the official repo, rea.tools, or the `rea-agents` npm package, because look-alike repositories exist. (../../raw/github/morluto-rea.md)

## Example usage

The site's first investigation is a six-file Electron Notes app with an **Export notes** button:

```text
Download https://rea.tools/examples/notes-example.zip into a new example folder and unpack it.
Use REA to find what happens when I click Export notes. Show where notes.csv is written,
which fields it contains, and the relevant files and lines.
```

The expected answer traces `renderer.js` (`notes.exportCsv()`) to `preload.js` (`notes:export` IPC) to the `main.js` handler, which writes `notes.csv` to Downloads with `id,title` columns. The user then checks a prediction by running the `toCsv` formatter directly (`1,"Hello, ""REA"""`). Terminal equivalents:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/notes-example --json
npx -y rea-agents@latest function /absolute/path/to/program main --provider ghidra --json
npx -y rea-agents@latest list-browser-targets http://127.0.0.1:9222 --json
npx -y rea-agents@latest inspect-web-page http://127.0.0.1:9222 TARGET_ID --observation-ms 10000 --include-json-body-shapes --json
```

(../../raw/github/morluto-rea.md also documents `rea analyze`, `rea decompile`, `rea trace` and `rea providers`.)

## When to use

Use REA when an agent has to answer "how does this shipped software actually do X?" and no source is available: an installed desktop app, a packaged Electron app, an APK, an old game executable, or a live web page. The site recommends one target and one behavior per question ("How is this file parsed?", "Which function handles this menu action?"), then following any unresolved call or value as the next question. Pick it over a browser-automation or API-scraping tool when you need the program's own logic, not just its I/O. Static JavaScript and .NET inspection need no native engine; deep native analysis needs Hopper, Ghidra or IDA.

## Maintenance status

Extremely active: 254,870 stars and 64,040 forks (up from about 58K stars on 2026-10-10), latest release `rea-agents-6.5.0` (2026-10-14), last push 2026-10-15, MIT license with a separate `THIRD_PARTY_NOTICES.md` and `DISCLAIMER.md`. The README now states that commercial tools (IDA Pro/Hex-Rays, Hopper, JEB) must be legally obtained, and that REA grants no tool licenses. Roadmap priorities: broader native architecture/type/indirect-call verification, linking static findings with runtime observations, and wider process/protocol coverage. (../../raw/github/morluto-rea.md)

## Ecosystem

The site lists five worked case studies: Aegis Authenticator's TOTP code recovered from its released APK, an easy DownUnderCTF flag checker solved as equations, DX-Ball's sound-pan function (`pan = (x × 1.5625 − 500.0) × scale`), checked against 3,205 inputs and all 63 compiled bytes, Notion's clipboard bridge traced through packaged JavaScript and IPC, and TH04's 16-bit bullet-ring angle helper. Community support runs through GitHub issues and Discord.

The blog post "Does reverse engineering need a bigger model?" (reviewed 2026-10-13) uses Touhou reconstruction repos (TH04, TH08, TH09, TH095) as evidence. The goal there is exact reconstruction: source code that, built with a pinned historical compiler, reproduces the original machine code. The post shows newer models (GPT-6.1-Sol, GPT-6-Astra, GPT-6-Luna-max) closing matches that earlier sessions had stalled on, by changing temporary lifetimes or the control-flow representation. It argues that retrieval over repo-held compiler lessons may provide much of what a specialist model would, and proposes RL against compile-and-compare oracles. It also warns that a flawed oracle (TH08 comparisons that passed with wrong floating-point constants) would teach the learner the same blind spot. Related wiki sources: [[integuru.com]] reverse-engineers web APIs rather than binaries, and the security skill libraries [[mukul975-anthropic-cybersecurity-skills]] and [[SnailSploit-Claude-Red]] can use REA as an analysis backend.

## Documentation

The site has no `llms.txt` or `/docs`. `sitemap.xml` lists Get started, First investigation, Guides (native, JavaScript, browser), FAQ, Showcase (five case studies), Examples (dino-lab), Blog (two posts) and Contributors, mirrored in 19 locales. Deeper per-target reference material lives in the repo's `docs/` folder (about 70 files, including installation, CLI, MCP contracts/prompts, tool design, and per-target guides), and the site links to it directly.
