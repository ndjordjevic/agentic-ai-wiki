# morluto/rea

## Metadata
- Stars: 254870
- Forks: 64040
- Primary language: TypeScript
- Default branch: main
- Latest release: rea-agents-6.5.0 (2026-10-14)
- License: MIT
- Homepage: https://rea.tools
- Last pushed: 2026-10-15
- Fetched: 2026-10-15
- Final URL: https://github.com/morluto/rea

## Description
Reverse engineer anything with agents, from app behavior down to native binaries.

## README
<div align="center">

**English** · [简体中文](docs/readme/README_zh.md) · [繁體中文](docs/readme/README_zh-TW.md) · [日本語](docs/readme/README_ja.md) · [한국어](docs/readme/README_ko.md) · [Türkçe](docs/readme/README_tr.md) · [Русский](docs/readme/README_ru.md) · [Tiếng Việt](docs/readme/README_vi.md) · [ไทย](docs/readme/README_th.md) · [Deutsch](docs/readme/README_de.md) · [Español](docs/readme/README_es.md) · [Français](docs/readme/README_fr.md) · [Українська](docs/readme/README_uk.md) · [Polski](docs/readme/README_pl.md) · [Português (Brasil)](docs/readme/README_pt-BR.md) · [العربية](docs/readme/README_ar.md) · [فارسی](docs/readme/README_fa.md) · [Bahasa Indonesia](docs/readme/README_id.md) · [Italiano](docs/readme/README_it.md)
· [Ελληνικά](docs/readme/README_el.md)

# REA: Reverse Engineer Anything

### One MCP for reverse engineering across binaries, applications, and runtime behavior.

**See a feature you like. Understand how it works, down to the binary level.**

[![npm version](https://img.shields.io/npm/v/rea-agents?style=flat-square&color=cb3837)](https://www.npmjs.com/package/rea-agents)
[![MCP tool catalog](https://img.shields.io/badge/MCP-tool_catalog-5c4ee5?style=flat-square)](docs/mcp-contracts.md#generated-catalog)
[![Node.js requirements](https://img.shields.io/badge/Node.js-requirements-339933?style=flat-square&logo=nodedotjs&logoColor=white)](#what-you-can-analyze)
[![skills.sh](https://skills.sh/b/morluto/rea?style=flat-square)](https://skills.sh/morluto/rea/reverse-engineer-anything)
[![MIT license](https://img.shields.io/badge/license-MIT-f4c430?style=flat-square)](LICENSE)
[![Discord](https://img.shields.io/discord/1556595354999332884?logo=discord&logoColor=white&label=Discord&color=5865F2)](https://discord.gg/GkcryMnJDM)

<a href="https://trendshift.io/repositories/82054?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-82054" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/82054" alt="morluto%2Frea | Trendshift" width="250" height="55"/></a>

**[Website](https://rea.tools/) · [Guides](https://rea.tools/guides/) · [Showcases](https://rea.tools/showcase/)**

[Quick start](#quick-start) · [How REA works](#how-rea-works) · [What you can analyze](#what-you-can-analyze) · [Showcases](#showcases) · [FAQ](#faq) · [Documentation](#documentation)

<code>npx rea-agents setup</code>

</div>

> [!IMPORTANT]
> Get REA from [morluto/rea](https://github.com/morluto/rea),
> [rea.tools](https://rea.tools/), or the [rea-agents npm package](https://www.npmjs.com/package/rea-agents).
> Follow the installation and release links from these official sources. A similar
> repository name or copied README does not establish that a download is official.

<div align="center">

<br />

<img src="docs/assets/rea-hopper-analysis.png" alt="REA launching its analysis bridge inside Hopper while inspecting a native binary" width="1200" />

<br /><br />

<table aria-label="REA community">
<tr>
<td align="center" width="360">
  <a href="https://discord.gg/GkcryMnJDM">
    <img src="docs/assets/discord.svg" height="42" alt="Discord" /><br />
    <strong>Join the Reverse Engineering Community</strong>
  </a><br />
  <sub>Discord · Q&amp;A · Show and Tell</sub>
</td>
</tr>
</table>

<br />

</div>

---

See a feature in an app that you want in your own product? Ask your agent to investigate it with REA. It can inspect the app without its source code, explain how the feature works, show the evidence, and build a version for your project.

REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites. You can also use the same tools from your terminal. Analysis runs locally, and results include the evidence and limitations behind each conclusion.

Setup registers REA with your agent and installs matching workflow instructions. Native analysis can use an existing Hopper, Ghidra, or IDA installation; setup can optionally install Hopper with approval. Static JavaScript analysis needs no native analysis engine.

> **[Visit the REA website](https://rea.tools/)** for setup instructions, illustrated guides, and real case studies.

## Quick start

On Linux, Ghidra, JADX, firmware tool launches and static JavaScript/Electron
analysis require a procps-compatible `ps` on REA's `PATH` for process ownership
checks. Recovery steps are in `docs/installation.md` under
"Linux owned-process prerequisite".

### Set up your agent

With Node.js and npm installed, run:

```bash
npx rea-agents setup
```

Choose your agents, review the proposed changes, and approve them. Setup adds
REA's MCP server and matching workflow instructions, with backups of existing
configuration. Restart your agent afterward.

Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and
[other agents](docs/installation.md#supported-agents). See
[installation and setup](docs/installation.md) for provider configuration and
manual MCP registration.

### Ask your agent

```text
Understand how search works in the Notes app, show me the evidence, and build a
similar feature for my project.
```

Replace Notes with your target app and the feature you want to understand.

### Use the terminal

Inspect an extracted JavaScript/Electron app directory or ASAR:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

The result includes modules, imports, Electron boundaries and their evidence.
Replace the path with your target, such as `"D:/apps/example"` on Windows.

To install the `rea` command for regular use:

```bash
npm install --global rea-agents
rea --help
```

For native analysis, configure a provider first. See the
[CLI and Evidence guide](docs/cli.md) for native commands, provider selection,
snapshots and scripting.

### Update REA

REA changes quickly, and new releases include frequent bug fixes. Keep your
installation up to date.

For a CLI installed with `npm install --global` or `bun add --global`:

```bash
rea update
```

Bun global updates require Bun 1.2.17 or later. With an older Bun release,
upgrade Bun manually before running `rea update`.

To refresh your agent registrations and skill, run the setup command printed
by the update.

If you use `npx`, update your agent setup with:

```bash
npx rea-agents@latest setup
```

Review the setup changes and restart your agent. For one-off CLI commands,
use `npx rea-agents@latest` followed by the command. With Bun, use
`bunx rea-agents@latest` in place of `npx rea-agents@latest`.

## How REA works

Your agent calls REA through MCP to inspect the target and trace relevant code.
REA returns findings with their evidence. The agent uses them to ask follow-up
questions, explain the behavior, or write and test an implementation.
CLI commands use the same workflows.

![REA investigation flow: your agent asks about a local target, REA inspects and traces it using analysis tools, and the agent uses the returned code, references and unknowns to explain, implement and test.](website/public/assets/figures/rea-investigation-flow.svg)

[Open the full-size figure](website/public/assets/figures/rea-investigation-flow.svg).

<a id="current-status"></a>

## What you can analyze

REA requires Node.js 22.x (>=22.19), 24.x (>=24.11), or 26+, plus npm.
Additional tools and host support depend on the target:

| Target                 | What REA returns                                                                     | Requirements and guide                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Native binaries        | Pseudocode, assembly, strings, symbols, calls and references                         | Hopper, Ghidra or IDA; [native analysis](docs/native-investigation.md)                                                                |
| Offline ELF layout     | Sections, segments, original symbols/relocations and static mitigation candidates    | Caller-supplied pwntools on Linux x64; [binary diagnostics](docs/binary-diagnostics.md)                                               |
| Go binaries            | Embedded compiler version, modules, replacements and build settings                  | Built-in static ELF/PE/thin Mach-O inspection; no Go installation required                                                            |
| Rust binaries          | Embedded cargo-auditable crate names, versions, sources and dependency edges         | Built-in static ELF/PE/thin Mach-O inspection; [Rust binaries](docs/rust-binaries.md)                                                 |
| WASM artifact          | Validation, sections, exact import/export WAT forms and decoded WAT                  | Caller-supplied WABT 1.0.42; `inspect_wasm_artifact`                                                                                  |
| EVM bytecode           | Dispatch selectors, byte offsets, inferred arguments and mutability                  | Local raw/hex carrier on Linux x64; [offline EVM guide](docs/evm-bytecode.md)                                                         |
| SQLite databases       | Tables, columns, indexes, views, triggers and selected ordinary-table rows           | Local database/WAL snapshot; Node.js 24.x >=24.15 or 26+ with native SQLite limits                                                    |
| Recorded Linux crashes | Raw notes, every recorded thread's registers/signals and optional mapping candidates | Caller-supplied pwntools on Linux x64; optional GDB/pwndbg; [recorded crashes](docs/recorded-crashes.md)                              |
| JavaScript / Electron  | Modules, imports, source maps, routes, IPC and native add-on relationships           | Node.js and npm; Linux: procps-compatible `ps`; [application analysis](docs/javascript-application-workflows.md)                      |
| Websites               | Page structure, scripts, network observations and requested screenshots              | A Chrome-family browser; [browser analysis](docs/browser-observation.md)                                                              |
| Saved network captures | Requests, responses, exposed payloads and source locations                           | HAR or Fiddler Everywhere SAZ; mitmdump on Linux for native mitmproxy; [capture guide](docs/web-network-captures.md)                  |
| .NET assemblies        | Metadata, CIL instructions, declared native dependencies and build comparisons       | None (static only); [managed-code guide](docs/managed-code-analysis.md)                                                               |
| Android APKs           | Manifest declarations, classes, decompiled methods and references                    | Headless JADX and a full JDK on Linux/macOS/Windows x64; [Android guide](docs/android-analysis.md)                                    |
| Android devices        | Devices, packages, processes, logs, dumps, screen captures, and APK/file transfers   | Caller-supplied adb (emulator or hardware); [ADB guide](docs/adb-device-analysis.md)                                                  |
| JEB projects           | Engine-backed project units, artifact digests and type/method pseudo-code            | A caller-started JEB client serving MCP, selected with REA_JEB_MCP_URL; [JEB guide](docs/jeb-analysis.md)                             |
| Android resources      | Decoded manifest, string tables, locales and version facts                           | Caller-supplied Apktool launcher; [resource guide](docs/apktool-resource-analysis.md)                                                 |
| Flutter apps           | Dart snapshot hash, per-ABI library digests and engine build provenance              | None (static APK parsing); [Flutter guide](docs/flutter-analysis.md)                                                                  |
| Firmware               | Regions, extraction results and native-analysis handoffs                             | Binwalk / Unblob on Linux; [firmware guide](docs/firmware-analysis.md)                                                                |
| Recorded packets       | Selected fields, repeated values, filters and decode-as rules                        | Linux: TShark 4.x + prlimit; [capture guide](docs/packet-captures.md)                                                                 |
| Packet summaries       | Endpoints, DNS, TLS SNI, protocol distribution and HTTP requests                     | Caller-supplied tshark and capinfos (Linux-verified); [pcap guide](docs/pcap-analysis.md)                                             |
| Recorded logic signals | Decoder annotations, sample ranges and diagnostics                                   | Linux: sigrok-cli 0.7.2 + prlimit; [signal recordings](docs/signal-recordings.md)                                                     |
| Packages and resources | File inventories, digests, plists, Apple bundle anatomy and extracted resources      | [Artifact and JavaScript guide](docs/javascript-artifact-reconstruction.md), [Apple applications](docs/apple-application-analysis.md) |
| Process behavior       | Terminal output, interactions, exit and filesystem observations, and run comparisons | Linux/macOS with a native PTY; [process capture](docs/process-capture.md)                                                             |

Static JavaScript and .NET inspection read the supplied files without running
the application. Runtime capture runs or interacts with the selected target
using your user permissions; each runtime guide describes its effects.

For offline native-binary inspection, REA also supports caller-supplied GNU
objdump and Rizin. See the [reverse-engineering tools guide](docs/reverse-engineering-tools.md)
for provider setup, CLI commands, and Evidence limitations. REA does not install
or update either provider.

<a id="choosing-a-deep-analysis-provider"></a>

Native formats and host support vary by provider. See
[Hopper and Ghidra setup](docs/installation.md#hopper), the
[IDA guide](docs/ida-provider.md) (including an optional native MCP bridge), the
[Kuna decompiler guide](docs/kuna-provider.md), and
[experimental Windows Ghidra support](docs/windows-ghidra-p0.md).
Ghidra also supports [16-bit DOS analysis](docs/ghidra-dos.md).
For large binaries, raise the provider's startup deadline with
`REA_GHIDRA_STARTUP_TIMEOUT_MS` or `REA_HOPPER_STARTUP_TIMEOUT_MS`.
For provider selection, see the [CLI guide](docs/cli.md#choose-a-provider).
Check [release availability](docs/installation.md#released-package-and-main)
for features added since the latest npm release.

## Showcases

[![Illustrations of the DX-Ball sound-pan, Notion clipboard-bridge, and TH04 bullet-ring showcases](docs/assets/rea-showcases.png)](https://rea.tools/showcase/)

### DX-Ball: reconstruct a sound-pan calculation

Follow a sound call into its position-to-pan helper, inspect the instructions,
and turn incomplete pseudocode into C. The reconstruction passes 3,205
original-x86 cases and reproduces all 63 compiled function bytes.

[Read the case study](https://rea.tools/showcase/dx-ball/) ·
[Reconstruction repository](https://github.com/N0zoM1z0/dx-ball)

### Notion: trace the Electron clipboard bridge

Find the renderer's clipboard API, follow it through preload and IPC into the
main process, and inspect the rich clipboard format.

[Read the case study](https://rea.tools/showcase/notion/)

### TH04: recover a DOS bullet-ring calculation

Inspect the original PC-98 game's 16-bit instructions, recover the fixed and
aimed angle calculations, and compare the reconstructed C++ with the
historical compiler output.

[Read the case study](https://rea.tools/showcase/th04/) ·
[Reconstruction repository](https://github.com/N0zoM1z0/th04)

If you've used REA on something interesting, we'd love to see it. Share your
case in an [issue](https://github.com/morluto/rea/issues) or a
[pull request](https://github.com/morluto/rea/pulls), including the target,
your question, how REA helped, and what you found.

## FAQ

<details>
<summary><strong>Which agents can use REA?</strong></summary>

Any agent that supports local MCP servers. Setup configures the
[supported agents](docs/installation.md#supported-agents); other clients can use
[manual MCP registration](docs/installation.md#mcp-registry).

</details>

<details>
<summary><strong>Do I need Hopper, Ghidra or IDA?</strong></summary>

Deep native analysis uses one of them. Static JavaScript and .NET inspection
work without a native analysis engine. Setup can install Hopper after approval;
Ghidra and IDA use your existing installations. See [provider setup](docs/installation.md#hopper).

</details>

<details>
<summary><strong>Do I need to start Hopper first?</strong></summary>

REA starts Hopper when an operation needs it. On macOS, a first-run dialog may
ask you to choose demo mode or activate your license. Complete that prompt in the
same user session before your first CLI/MCP operation or unattended job. Open
Hopper manually if needed. See
[Hopper startup and troubleshooting](docs/installation.md#launcher-paths-and-troubleshooting).

</details>

<details>
<summary><strong>What does installing the skill from skills.sh do?</strong></summary>

The skill supplies investigation instructions for your agent. Use `npx rea-agents setup`
to register REA's MCP server and install the matching instructions, then restart
your agent. See [skill-only installation](docs/installation.md#skill-only-installation).

</details>

<details>
<summary><strong>What code does REA return?</strong></summary>

Native analysis returns pseudocode and assembly. JavaScript/Electron analysis
recovers modules and their relationships. Your agent uses these findings to
write and test an implementation; the [showcases](#showcases) give worked examples.

</details>

<details>
<summary><strong>Does REA upload my app?</strong></summary>

REA analyzes targets locally. Your agent receives the tool results, and its
model provider has its own data policy.

</details>

<details>
<summary><strong>What should I do if I hit a bug?</strong></summary>

Update first; a recent release may already fix it.

For a CLI installed with `npm install --global` or `bun add --global`:

```bash
rea update
```

For agent setup through `npx`:

```bash
npx rea-agents@latest setup
```

If you're using an agent, complete the [setup refresh](#update-rea) and restart
it. Retry the same task. If the problem persists, [open an issue](https://github.com/morluto/rea/issues)
with your REA version, target type, steps to reproduce and error output.

</details>

## Documentation

Start with the website's [worked guides](https://rea.tools/guides/).
For exact options, prerequisites and result contracts:

- [Installation and setup](docs/installation.md): agent registration, provider configuration, updates and uninstall.
- [Readiness and troubleshooting](docs/installation.md#check-readiness-for-your-task): diagnose one agent or analysis engine.
- [CLI and Evidence](docs/cli.md): commands, provider selection, snapshots, import/export and exit statuses.
- [MCP contracts](docs/mcp-contracts.md) and [agent prompts](docs/mcp-prompts.md): tool results, sessions and guided investigations.
- [Tool catalog](docs/mcp-contracts.md#generated-catalog): generated inventory of tools, providers and CLI commands.
- [Roadmap](docs/roadmap.md): planned work and capability trackers.

Report vulnerabilities through [SECURITY.md](SECURITY.md).

## Star history

🎉 **250,000 GitHub stars — thank you!**

Thanks to everyone using REA, reporting bugs, requesting features, testing builds, and contributing fixes.

<a href="https://www.star-history.com/?repos=morluto%2Frea&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=morluto/rea&amp;type=date&amp;theme=dark&amp;legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=morluto/rea&amp;type=date" />
    <img alt="REA GitHub star history" src="https://api.star-history.com/chart?repos=morluto/rea&amp;type=date" />
  </picture>
</a>

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md) for responsible-use guidance.

The project's position on illegal or unauthorized use covers all REA versions,
distribution channels, and platforms; each copy retains its applicable licenses.

REA is for lawful research, education, interoperability, software preservation,
and analysis of software you own or are authorized to examine.

## Contributing

We'd love your help with REA! [Open an issue](https://github.com/morluto/rea/issues) to
report a bug or suggest a feature, or [send a pull request](https://github.com/morluto/rea/pulls)
to improve the code or docs.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and checks,
[testing](docs/testing.md) for verification lanes, and the
[architecture map](docs/architecture.mermaid) for the project structure.

## License

[MIT](LICENSE)

REA-authored code is licensed under MIT. Third-party material retains its own
licenses and copyright notices; see
[Third-party notices](THIRD_PARTY_NOTICES.md) for the dependency inventory,
preserved license texts, and external-tool terms.

**You must legally obtain and be authorized to use commercial tools**, including
IDA Pro / Hex-Rays decompilers, Hopper, and JEB, under their applicable
licenses. REA grants no tool license, key, or activation entitlement. Trials and
demos remain subject to vendor terms, including user, feature, automation, and
output sharing restrictions. Cracked copies, stolen keys, unauthorized key
sharing, and bypassing license restrictions are not authorized. This guidance
does not amend MIT or third-party licenses.

## Docs

### docs/index.md

---
layout: home

hero:
  name: REA
  text: Reverse Engineer Anything
  tagline: Understand binaries, applications, and runtime behavior with one CLI and MCP server.
  actions:
    - theme: brand
      text: Get started
      link: /installation
    - theme: alt
      text: View on GitHub
      link: https://github.com/morluto/rea

features:
  - title: Investigate with your agent
    details: Connect REA to your coding agent, describe the app or feature you want to understand, and follow the evidence.
    link: /mcp-prompts
  - title: Inspect across formats
    details: Explore native binaries, JavaScript and Electron apps, .NET assemblies, Android packages, firmware, and websites.
    link: /installation
  - title: Keep the evidence
    details: Analysis runs locally and returns observations, limitations, and unknowns through the CLI and MCP.
    link: /mcp-contracts
---

## Start with one command

```bash
npx rea-agents setup
```

Choose your agent, review the planned changes, and approve setup. Native binary
analysis can use an existing Hopper, Ghidra, or IDA installation; static
JavaScript analysis needs no native analysis engine.

For a first result from an extracted JavaScript application or ASAR:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

See [installation and setup](./installation.md) for requirements and configuration.

For runtime instrumentation, see the [Frida guide](./frida-instrumentation.md).

## Choose a guide

| Task                                                | Guides                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inspect native functions, references, or types      | [Native binaries](native-investigation.md), [Go metadata](go-binaries.md), [Rust dependencies](rust-binaries.md), [offline ELF layout](binary-diagnostics.md), [recorded crashes](recorded-crashes.md)                                                                                                                      |
| Select a native provider or import format           | [Ghidra semantics](ghidra-provider.md), [Windows](windows-ghidra-p0.md), [DOS](ghidra-dos.md), [raw bytes](raw-binary.md), [MIPS](ghidra-mips.md), [PSP](ghidra-psp.md), [NativeAOT](ghidra-nativeaot.md), [IDA](ida-provider.md), [Kuna](kuna-provider.md), [JEB](jeb-analysis.md)                                         |
| Analyze JavaScript or Electron artifacts            | [Static analysis](javascript-artifact-reconstruction.md), [tracing and comparisons](javascript-application-workflows.md), [application graph](javascript-application-graph.md), [source recovery](javascript-recovery.md)                                                                                                   |
| Compare static JavaScript with runtime observations | [Runtime attribution](javascript-runtime-observation.md), [reconciliation](javascript-runtime-reconciliation.md), [Electron observation](electron-observation.md), [Electron fuses](electron-fuses.md)                                                                                                                      |
| Inspect assemblies, packages, or firmware           | [.NET](managed-code-analysis.md), [Android](android-analysis.md), [Apktool resources](apktool-resource-analysis.md), [ADB acquisition](adb-device-analysis.md), [Apple](apple-application-analysis.md), [Harmony](harmony-analysis.md), [firmware](firmware-analysis.md), [WASM](wasm-artifacts.md), [EVM](evm-bytecode.md) |
| Observe or compare a browser scenario               | [CDP observation](browser-observation.md), [scenarios](browser-scenario-contract.md), [runtime evidence](web-runtime.md), [historical captures](web-network-captures.md)                                                                                                                                                    |
| Trace captured website source                       | [Source locations](web-source-location.md), [module traces](website-module-trace.md), [script export](website-script-export.md)                                                                                                                                                                                             |
| Capture and compare a command                       | [Process capture](process-capture.md)                                                                                                                                                                                                                                                                                       |
| Use CLI/MCP and retain evidence                     | [CLI](cli.md), [MCP contracts](mcp-contracts.md), [agent prompts](mcp-prompts.md), [obligation ledgers](reconstruction-obligation-ledgers.md)                                                                                                                                                                               |

For development, use [testing](testing.md), [client verification](client-verification.md),
[tool design](tool-design.md), and [releasing](releasing.md).
[Reconstruction readiness](reconstruction-readiness.md) describes a development
conformance verifier. [The 6.2 migration](migration-6.2.md) records that release's
compatibility changes; [the roadmap](roadmap.md) tracks future work.

![REA inspecting a native binary in Hopper](./assets/rea-hopper-analysis.png)

### docs/cli.md

# CLI and Evidence

Use the CLI for a direct inspection or a script. It uses the same application
workflows and evidence contracts as REA's MCP server. Each CLI invocation is a
separate process; save results when you want to use them in a later command.

## Run a command

After [installing REA](installation.md), use `rea`. You can also run a command
without a global installation:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

Use an extracted application directory or an ASAR as the target. Static
JavaScript analysis returns the application graph and Evidence directly.
Generic `rea analyze PATH` selects this workflow for directories and `.asar`
files when neither `--provider` nor `--snapshot` is supplied. See
[JavaScript artifact reconstruction](javascript-artifact-reconstruction.md)
for results, integrity checks and coverage.

The complete application Evidence can be hundreds of megabytes for a real
application. When an agent or a person reads the result, save it to a file and
project a summary, a module page or one module from the saved Evidence:

```bash
rea analyze-javascript-application /absolute/path/to/app --json > app-evidence.json
jq -c '{source: {kind: "inline", evidence: .}, view: {kind: "summary"}}' app-evidence.json > app-view.json
rea inspect-analysis-view app-view.json
```

For example, a 334 MB Obsidian application Evidence file yields a summary view
of about 10 KB. Replace the view with
`{"kind": "page", "collection": "modules", "offset": 0, "limit": 32}` for a
module page. See
[JavaScript application workflows](javascript-application-workflows.md) for
views, feature traces and comparisons that take the same saved Evidence.

## Managed assemblies (.NET)

For a .NET PE/CLI assembly, inspect its identity and deployment form before
inspecting members. These commands read metadata and Common Intermediate
Language (CIL) without loading or executing the assembly and require no native
analysis engine:

```bash
rea inspect-managed-artifact /absolute/path/Assembly.dll --json
rea inspect-managed-members /absolute/path/Assembly.dll --json
rea inspect-managed-members /absolute/path/Assembly.dll --type Example.Parser --json
```

Replace `Example.Parser` with an exact `full_name` from the member inspection,
or a declaring type name you already know. Omit `--type` to inspect all members,
or repeat it to select several types.
Selection limits decoding to the selected types; member references remain an
assembly-wide inventory, so the output can still be large.

Choose the workflow from the artifact's contents rather than its `.exe` or
`.dll` extension. The managed parser requires PE/CLI metadata; it does not
unpack .NET single-file hosts or decode IL2CPP metadata. NativeAOT method bodies
require native analysis. See the [managed-code guide](managed-code-analysis.md)
for supported deployment forms, selection semantics, and coverage limits.

## SQLite snapshots

For a local database snapshot, use `rea inspect-sqlite-database PATH --json`.
Add `--table NAME --row-limit 20` to read a bounded sample from an ordinary
table. This command does not require a native analysis provider. See
[SQLite database snapshots](sqlite-databases.md) for database/WAL identity,
source-file handling and row-value semantics.

## Native analysis

Inspect embedded Go build metadata without installing Go or configuring a
disassembler:

```bash
rea inspect-go-binary /absolute/path/to/program --json
```

The shared CLI/MCP workflow reports compiler version, modules, replacements,
build settings, original bytes and SHA-256. See [Go binaries](go-binaries.md)
for supported containers and absent or malformed metadata.

Inspect an embedded cargo-auditable Rust dependency list without installing
Rust or configuring a disassembler:

```bash
rea inspect-rust-binary /absolute/path/to/program --json
```

The same workflow reports package names, versions, sources, the root package,
dependency edges, and the section's file range. A missing `.dep-v0` section is
null metadata, not proof that the binary has no dependencies. See
[Rust binaries](rust-binaries.md).

Configure [Hopper or Ghidra](installation.md#hopper), the
[IDA adapter](ida-provider.md), or [Kuna](kuna-provider.md) before analyzing a
native target. Substitute
your target, search text and function name or address in these examples:

```bash
rea analyze /absolute/path/to/program --provider ghidra --json
rea search /absolute/path/to/program "search" --provider ghidra --json
rea function /absolute/path/to/program main --provider ghidra --json
rea decompile /absolute/path/to/program 0x1000 --provider ghidra --json
rea xrefs /absolute/path/to/program 0x1000 --provider ghidra --json
rea trace /absolute/path/to/program "search" --provider ghidra --json
```

`analyze` and `inspect` share the native overview workflow. `function` returns
a function dossier; `decompile` returns pseudocode. For assembly instructions
alone, use `rea instructions`. A macOS `.app` bundle can be supplied directly.

Run `rea --help` or a command's `--help` for arguments and output options.
The [generated catalog](mcp-contracts.md#generated-catalog) lists all CLI commands and MCP
tools. Provider-specific target support is described in the
[native guide](native-investigation.md), [DOS guide](ghidra-dos.md),
[raw binary guide](raw-binary.md), and
[Windows Ghidra guide](windows-ghidra-p0.md).

## Choose a provider

List the available providers and their supported operations:

```bash
rea providers --json
rea capabilities --json
```

These commands describe binary-session providers and auxiliary capabilities.
For the complete MCP surface, use the connected server's tool list and the
session's advertised availability; individual guides describe prerequisites.

With automatic selection, REA uses the single available provider that supports
the target. When several providers support it, select one explicitly:

```bash
rea analyze /absolute/path/to/program --provider hopper
```

Set `REA_ANALYSIS_PROVIDER` for a standing preference. An explicit `--provider`
overrides it. In MCP, pass `provider_id` to `open_binary`:

```json
{
  "path": "/absolute/path/to/program",
  "provider_id": "hopper"
}
```

The selected provider remains bound to the session until an explicit switch
or close. Provider failures are returned with their original reason. For an
`ambiguous` selection error, choose from `details.candidate_ids`; for
`provider_unavailable`, follow `message`, `remediation.action`, and the original
reasons in `details.rejections`. For Hopper, Ghidra, IDA, and JADX, run
`rea doctor --provider ID --json` to diagnose the selected engine. Other adapters,
such as `pwntools-elf`, report their configuration requirements directly and are
not accepted by `doctor --provider`. See
[task readiness](installation.md#check-readiness-for-your-task) and
[provider selection](mcp-contracts.md#identity-and-discovery).

The session reports work still in progress through `analysis_activity`.
A client timeout can end its wait while the provider continues analyzing.
`cleanup_incomplete` identifies resources whose shutdown or removal could not
be verified. See [MCP contracts](mcp-contracts.md) for session lifecycle and
[Ghidra first-query deadlines](mcp-contracts.md#ghidra-first-query-deadlines-and-recovery)
for import, client timeouts and recovery.

## Save and reuse analysis snapshots

A snapshot retains successful analysis results for later queries. REA reuses
an exact result when the target bytes, operation, parameters, provider and
settings match. Mutations and cursor-dependent calls are excluded from the
cache. Snapshot files are local and use owner-only permissions.

Dispatching a metadata write invalidates the active session's snapshot cache,
even if its reply fails: the provider may already have applied the write.
Close and reopen the target before importing or saving another snapshot.

Snapshots retain eligible target-scoped question histories in full, including
mutation Evidence recorded while another target was active. Observations and
related questions must still belong to the saved target. If those dependencies
cannot be retained, the entire history is excluded instead of reverting the
question to an earlier revision or disposition.

```bash
rea analyze /absolute/path/to/program --provider ghidra --snapshot /absolute/path/to/analysis/program.json
# Repeat the same query to reuse its saved result.
rea analyze /absolute/path/to/program --provider ghidra --snapshot /absolute/path/to/analysis/program.json
```

An exact CLI cache hit is normally read before starting a provider process.
On Windows, Ghidra first admits the selected source through its native snapshot
owner, so replay can start that provider.
In MCP, `open_binary` accepts `snapshot_path` to import a snapshot atomically
for its matching target; an MCP provider may still start before returning a
cached result. `close_binary` accepts `snapshot_path` and optional
`overwrite: true` to save before releasing provider resources. A failed save
leaves the session open so the caller can resolve the output failure.

The MCP save receipt reports `primitive_entries`, `workflow_entries`, and
`evidence_records` separately. Zero primitive bindings can still accompany retained workflow
results and Evidence. These are cached observations, not a saved provider
database: only eligible exact queries can reuse a result, and new or live
queries can still require provider startup. The CLI uses the same snapshot
format and preserves these records when loading and updating it.

## Import, export and compare Evidence

Evidence records retain artifact identity, source locations, observations,
inferences and unresolved findings. Validate an existing bundle, export its
canonical form, or compare two supplied bundles:

```bash
rea evidence-import /absolute/path/to/evidence/bundle.json
rea evidence-export /absolute/path/to/evidence/bundle.json /absolute/path/to/evidence/canonical.json
rea compare /absolute/path/to/evidence/left.json /absolute/path/to/evidence/right.json
```

Exports preserve an existing destination unless `--overwrite` is explicit.
For application traces and version comparisons, see
[JavaScript application workflows](javascript-application-workflows.md).
MCP [retained Evidence references](mcp-contracts.md#retained-application-evidence-inputs)
belong to one connection. Separate CLI calls consume full saved records.

## Import historical source

Import an older source tree to compare with the current artifact:

```bash
rea import-reference-source /absolute/path/to/source
rea import-reference-source /absolute/path/to/source --detail summary --outline-depth 2 --json
```

The default (`--detail full`) returns the complete `HistoricalSourceGraph`.
Choose `--detail summary` for a `HistoricalSourceSummary` of that same committed
inventory: its `HistoricalSourceManifest` contains the full graph and root
digests, with provenance, VCS facts, languages, manifest paths, entry and
relationship counts, parse-failure counts, file/directory states, exclusions
and limitations. The summary is a presentation view, not a graph accepted by
source-to-bundle comparison; keep the full output for that workflow.

`--outline-depth` requires `--detail summary` and accepts a nonnegative safe
integer. Depth 1 shows root children, depth 2 (the default) also shows their
children, and depth 0 omits all outline entries. Paths retain canonical Unicode
code-point order. `outline.omitted_entry_count` counts only inventoried entries
hidden by the chosen depth; it does not count unexamined children of excluded or
unreadable directories, or change `inventory_state`. Exclusions and source
limitations remain separate from this presentation omission.

`file_sizes.known_bytes` is the exact sum of known inventoried file sizes as
decimal text, so large sums cannot lose integer precision. Unknown sizes count
in `file_sizes.unknown_file_count`; excluded or unexamined paths are not included
in that total. A zero known-byte sum therefore does not establish an empty source
tree. Full output retains individual file hashes, relationships and parse-failure
diagnostics. Summary mode performs the same import and cleanup, then projects
the committed result without rereading source files. It reduces the selected
output, not the amount of source examined. A shallow tree or many exclusions can
still produce a large summary; depth 0 removes the outline but preserves the
other facts. No fixed output-size or runtime improvement is promised.

The import records hashes and metadata for the supplied files, separately
from observations of the current app. For a directory inside a Git checkout,
it records the HEAD of the nearest enclosing repository; whether the working
tree matches that commit remains unknown. It honors the source tree's `.gitignore`
and applies default exclusions for common generated and dependency paths such
as `node_modules/`, `dist/`, and `*.log`. Pattern-based exclusions record the
matched pattern and whether it came from project, default, caller, or sensitive
path policy. Links into excluded paths retain their internal target metadata;
the exclusion explains why the target has no inventory entry, and the inventory
remains partial. Exclusions record `entry_kind` when the importer observed it;
older saved exclusions without that field have unknown kind. An excluded
ancestor proves an internal descendant only when its kind is `directory`.
Set `REA_REFERENCE_SECRET_PATTERNS_JSON` to a JSON array of ignore
patterns when you want to mark selected paths as sensitive; those patterns are
reported separately as configured-secret exclusions.

Re-import saved graphs whose pattern-based exclusions lack `pattern` before
using them in source-to-bundle comparisons.

JavaScript and TypeScript import parsing requires valid UTF-8. Malformed source
bytes retain their original hashes and sizes with a decoding diagnostic; REA
does not infer module targets from replacement characters.

Historical-source import requires safe no-follow file opens on Linux or
macOS. Native Windows returns `unsupported_host`; use Linux REA inside WSL
or another supported host. See
[source-to-bundle comparison](javascript-application-workflows.md#historical-source-to-bundle-comparison)
for mapping identities, inferences and unknowns.

## Capture runtime behavior

Choose the guide for the target and intended interaction:

- [Browser observation](browser-observation.md): inspect a selected page through CDP.
- [Browser scenarios](browser-scenario-contract.md): run declared interactions and capture their results.
- [Electron observation](electron-observation.md): inspect an Electron renderer or capture an application scenario.
- [Electron fuses](electron-fuses.md): read packaged fuse bytes before expecting `--inspect` to reach an Electron main process.
- [Node/Electron Inspector](javascript-runtime-observation.md): record script locations and execution contexts.
- [Process capture](process-capture.md): run an executable and compare terminal, exit and filesystem observations.

Runtime requests name the target and actions. Launched targets run with your
user permissions; consult the chosen guide for host requirements and effects.

## Output and exit status

`rea mcp doctor --json` checks production MCP startup and reports child logs in
`diagnostics`. It drains stderr while retaining at most its first 64 KiB of raw
bytes as text, omitting a final UTF-8 code point if it crosses that byte limit.
`stderr_bytes` counts all observed bytes, including omitted output;
`stderr_truncated` indicates that output exceeded the retention limit. The same
diagnostics appear inside the report when `--full-output` is selected. Log
truncation alone does not change the diagnostic health or exit status.

The default terminal format is TOON. Use `--json` when saving results for a
JSON consumer. Valued output flags (`--format`, `--filter-output`,
`--token-limit`, `--token-offset`) accept `--flag value` or `--flag=value`; a
missing value fails with `MISSING_OUTPUT_VALUE` before the command runs. `--json` is indented on a terminal and compact when piped or
redirected, which keeps large results smaller for agents and scripts; pipe
through `jq .` for indented files. Output selection and formatting do not change
operation status.

For `cutter-command`, `--json-output` requests command-specific JSON from
Cutter when available. This is separate from `--format json`, which selects the
CLI result representation; the global `--json` flag selects that same CLI
representation.

Cutter still accepts deprecated `--json=true` and `--json=false` compatibility
values. When both forms are present, `--json-output` takes precedence in either
argument order. Bare `--json` retains its global meaning of selecting JSON CLI
output formatting.

| Status    | Meaning                                                                                                                                                                                                                                                                                                                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`       | The operation completed. Its result may include partial evidence, warnings or unresolved questions.                                                                                                                                                                                                                                                                                    |
| `1`       | The operation could not complete. Structured output identifies invalid input, permissions, cancellation, timeouts or another failure when available.                                                                                                                                                                                                                                   |
| `128 + N` | Signal-derived status. An unhandled signal may have ended the process, with the shell or runtime preserving the conventional status; a command may instead have handled the signal, waited for its operation and cleanup to settle, and assigned the same status (`130` for SIGINT, `143` for SIGTERM). In the handled case, it may also have printed a structured `cancelled` result. |

A `cancelled` result does not by itself determine the exit status; it depends on
the command's signal handling. Commands routed through the shared
`withCommandCancellation` handler in the CLI set status `130` for SIGINT or
`143` for SIGTERM after their operation settles. Current source registrations
use that handler for process capture and comparison (`capture-process`,
`compare-process-captures`), JavaScript application analysis (`analyze` when it
selects the JavaScript lane, and `analyze-javascript-application`), selected
browser, web and Electron commands (including `analyze-web-bundle`,
`observe-web-execution`, `capture-browser-scenario` and
`capture-electron-scenario`), and the platform and provider command families
for Android/ADB, Apktool/JEB/Flutter, firmware, PCAP and signal analysis,
WASM/EVM, Go/Rust and binary diagnostics, Frida instrumentation, the Cutter
command, objdump, Rizin and GDB. In these paths, a returned structured
`cancelled` result can be printed before the wrapper assigns the
signal-derived status. This describes the current source routing; it is not a
claim that every command or provider runtime has been independently exercised.

When the reader of piped output closes early, as `rea ... | head` does, the
CLI stops writing, prints no error and exits `141` (`128 + 13`, the status of a
SIGPIPE-terminated writer). The operation itself may have completed; only its
output was declined.

`inspect-artifact` also returns a structured cancelled result, but its direct
analysis cancellation path does not set a signal-derived exit status, so it
exits `1`. Setup has its own contract: cancellation exits `0`. Treat the
structured result and process status as separate signals when scripting
cancellation.

`setup --dry-run` returns `planned` and exits `0`; a cancelled setup also exits
`0`. Setup returns `1` for `needs_confirmation` or `needs_human`.
`doctor` returns `1` when required checks in its selected readiness scope fail;
unavailable optional providers remain informational for unrelated tasks.

Enable `pipefail` in a supporting shell so a downstream formatter preserves
REA's failure status:

```bash
set -o pipefail
rea inspect-artifact ./app.asar --json | jq . > inspection.json
```

### docs/mcp-prompts.md

# Guided MCP prompts and completion

REA exposes six provider-neutral investigation workflows through the MCP
`prompts` capability. They complement the generated tool catalog; they do not add, remove, or
invoke tools by themselves.

## Prompt inventory

| Prompt                            | Purpose                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| `investigate_feature`             | Trace a feature from discovery into relevant function evidence.                      |
| `compare_application_versions`    | Compare two shipped artifacts, with optional static and runtime follow-up.           |
| `verify_reconstruction`           | Evaluate a finite reconstruction specification against retained comparison Evidence. |
| `trace_crash`                     | Correlate a crash symptom with static paths and optional process capture evidence.   |
| `audit_residual_unknowns`         | Audit current residual-unknown heads and evidence-qualified resolution.              |
| `prepare_bounded_process_capture` | Design a bounded controlled process experiment before execution.                     |

Every rendered prompt provides optional starting points using current REA tool
names. Agents can call tools directly, skip irrelevant suggestions, and inspect
provider or target state only when it helps answer the request or a tool
requires it. The prompts also ask agents to keep observations, inferences, and
unknowns distinct. Requested prompt arguments and completion choices are
rendered as untrusted selection data, not instructions or authorization.
Tool results include their Evidence inline. Prompts do not require a bundle or
resource fetch to read a result; an Evidence ID is only a reference when a
prompt argument or tool explicitly accepts one.

For a JavaScript/Electron application directory, `investigate_feature` points
directly to `analyze_javascript_application` with `input_path`; it does not
require `open_binary`. When that Evidence, or `inspect_binary_layout` Evidence,
is already retained, it suggests `inspect_analysis_view` before tracing a
feature seed. The CLI equivalent is `rea analyze <directory>`.
`open_binary` and the doctor target check admit files and macOS app bundles.
A directory outside that opening route is reported with an available analysis
action; this does not establish support for every directory format.

For target paths in `compare_application_versions`, the prompt suggests
opening each target before calling `inspect_artifact`; inspection operates on
the active target and returns the graph and findings together inline.

Use standard MCP discovery and retrieval:

```json
{ "method": "prompts/list", "params": {} }
```

```json
{
  "method": "prompts/get",
  "params": {
    "name": "investigate_feature",
    "arguments": {
      "feature": "offline search",
      "document": "Notes"
    }
  }
}
```

The server advertises `listChanged: true`. Updating a registered guided prompt
emits `notifications/prompts/list_changed`, allowing clients to refresh their
cached prompt catalog.

## Session-aware completion

MCP `completion/complete` completes guided-prompt arguments; it does not define
completion for arbitrary tool-call arguments. REA attaches completion to
optional prompt arguments that accept a session value. Suggestions provide
identifiers only; they do not retrieve or replace the inline Evidence result.

```json
{
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "investigate_feature"
    },
    "argument": {
      "name": "procedure",
      "value": "0x10"
    },
    "context": {
      "arguments": {
        "document": "Notes"
      }
    }
  }
}
```

Completion sources are live projections of the current session:

Document and procedure completion in a binary session reads an already-ready
provider; it does not start analysis. A cold provider, a target transition, or
unavailable inventory can return no suggestions. Run an analysis query first
when you need inventory from a provider that supplies it. An empty completion
list does not establish that the target has no procedures.

| Argument family     | Source and filtering                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Document            | Current provider `list_documents` result.                                                                                                            |
| Procedure           | The complete `list_procedures` inventory; all procedure addresses and uniquely named procedures are offered. Optional document context is forwarded. |
| Provider            | `auto` plus sorted deep candidates from the current binary session; target-free completion does not start them.                                      |
| Evidence            | Evidence IDs retained in the current session ledger, offered only for prompt arguments that accept Evidence references.                              |
| Process capture     | IDs for retained Evidence whose operation and validated result identify process capture.                                                             |
| Artifact manifest   | Manifest IDs from schema-valid retained artifact inventories.                                                                                        |
| Artifact occurrence | Occurrence IDs present in schema-valid retained artifact inventory pages.                                                                            |
| Residual unknown    | Current non-resolved unknown heads only.                                                                                                             |

Suggestions are Unicode-normalized, case-insensitive prefix matches. The server
deduplicates them and sorts by code point for deterministic results. Procedure
completion derives candidates from the complete inventory, so a name is offered
only when it identifies one address in that inventory. Completion returns all
matching values; it does not expose paging controls.

## Lifecycle and safety

Completion has no cache in REA. Opening or switching a target changes document
and procedure suggestions on the next request. Closing the binary clears its
Evidence ledger and residual-unknown registry, so identifiers from the closed
session are no longer suggested. Provider errors, unsupported operations, and
malformed provider output produce an empty completion list rather than an
unverified identifier.

Suggestions are starting points, not tool calls. A tool acts on the target,
operation, and lifecycle fields in its own request; selecting a suggestion does
not execute it or broaden those fields.

### docs/tool-design.md

# MCP tool design

## Decide whether to add a tool

Design around the analyst question. Inspect the current canonical contracts,
provider capabilities, and nearest existing tool before changing the surface.
Extend a tool when intent and result contract match; add one for a distinct
outcome or materially different authority. Public names and semantics remain
provider-neutral, with exact coverage reported per provider.

Keep the catalog complete; report capability/session availability instead of
truncating schemas. Serialized bytes alone do not establish agent usability.

## Choose the tool shape

| Shape                 | Use it for                                  | Result                                                                    |
| --------------------- | ------------------------------------------- | ------------------------------------------------------------------------- |
| `inspect`             | Facts about one target, object, or resource | Relevant fields, locations, and facet availability                        |
| `search` / `list`     | Candidate discovery                         | Stable ordering and context; pagination when the query or format needs it |
| `trace`               | Relationships across evidence               | Typed edges, supporting facts, and unresolved paths                       |
| `compare`             | Explicitly paired artifacts or observations | Identity, comparable coverage, and supported deltas                       |
| `workflow`            | A recurring outcome needing composition     | Inline answer, contributing evidence, and partial facets                  |
| `observe` / `capture` | Runtime behavior                            | Authority, launch/attach effects, lifecycle, and cleanup status           |

These are task shapes, not mandatory prefixes. Name tools for the action and
object callers reason about. Avoid unrelated discovery/execution/mutation modes
inside one tool.

## Prefer primitives; compose workflows

A primitive reports a reusable fact about an identified object or relationship.
A format-specific decoder qualifies; one application's business interpretation
belongs outside the general contract. Expose provider APIs when they add a
useful capability that existing tools cannot express.

Compose a workflow when repeated use demonstrates a multi-source outcome REA
can join without hiding caller choices or uncertainty. Batch homogeneous reads
when that removes repeated work while preserving per-item outcomes. Keep prompts
optional and avoid prescribing call sequences that a direct tool can replace.

Agents can compose experiments with ordinary commands, scripts, and local
fixture servers. Custom orchestration languages, replay engines, or separate
prepare/execute plans need an observed requirement those primitives cannot
satisfy. A plan without execution does not establish runtime behavior.

## Define the contract

- Use strict inputs with explicit target identity and required fields. Preserve
  meaningful target, action, capture, and output choices; remove ignored options
  and repeated permission declarations.
- Return the requested facts inline with artifact/provider identity, source
  locations, Evidence references, coverage, and relevant confidence and
  limitations. Use supported selection, summaries or views when they answer
  the question; preserve access to complete source Evidence and honor existing
  contracts and requested detail. Missing coverage is unknown, not absence.
  Avoid extra lookups solely to understand the answer or its provenance.
- Keep observed, derived, and inferred relationships distinct. Preserve
  unresolved edges and partial provider facts instead of requiring every
  provider to supply the same metadata.
- For caller/callee reads, `relationship_coverage` describes only the
  provider-observed direct relationship set. `complete` means that set was
  returned without a known read limit; it does not claim every possible runtime
  edge. Provider and execution caveats stay in `limitations` and do not imply
  incomplete relationship coverage. Missing coverage remains `unknown`.
- Declare process, filesystem, network, UI, and mutation effects truthfully;
  enforce the requested target and lifecycle.
- Add limits only for real format, protocol, authority, or measured resource
  constraints. Report pagination, truncation, cancellation, and partial failure.
  An assumed agent budget is insufficient justification for a limit.

## Implement and evaluate

Put provider protocols/parsing in adapters and shared CLI/MCP workflows in the
application layer. Share Evidence provenance, unknown projection, and session
retention semantics; matching payloads alone do not establish parity.

Measure the resource before choosing a budget and enforce it before the costly
step. Account for value alternatives, trace-frame products, retained records,
serialization expansion, and temporary-file growth separately. Derive facet
completeness from examined records and exhaustiveness, rather than diagnostic
prose or an empty failure list. Preserve observations independently of cleanup
success.

Update canonical contracts, output schemas, examples, generated artifacts, and
relevant docs together. Verify converted advertised schemas and success,
malformed, unavailable, cancellation, and partial outcomes through affected
consumers. Real-engine claims require the matching provider lane; see
[testing.md](testing.md).

For fixed tuples in public contracts, use `src/domain/fixedTupleSchema.ts`:
Zod's tuple projection omits implicit length bounds and Draft 2020-12 `items`,
which some clients require even alongside `prefixItems`. Tuples with a rest
schema also need explicit minimum lengths. Check parser/schema parity for empty,
short, overlong, and malformed values in both input and output projections.

When discoverability changes, evaluate representative broad, direct, and negative
tasks on the intended host. Record host/model/catalog, selected tools, arguments,
errors, retries, and task outcomes. Schema validity and keyword heuristics do not
establish successful tool selection. See [mcp-contracts.md](mcp-contracts.md) for
shipped runtime behavior.

### docs/roadmap.md

# REA roadmap

The [platform tracker](https://github.com/morluto/rea/issues/32),
[process/Hopper tracker](https://github.com/morluto/rea/issues/48), and
[browser tracker](https://github.com/morluto/rea/issues/39) track capability and
verification work. Available tools and setup are documented in the
[investigation guides](https://rea.tools/guides/),
[installation guide](installation.md), and
[generated catalog](mcp-contracts.md#generated-catalog).

## Priorities

- Expand native architecture, type, and indirect-call verification.
- Connect static findings and runtime observations across application layers.
- Improve obfuscated managed-code comparisons and verified native links.
- Extend process, protocol, filesystem, reconnect, and build-comparison coverage.
- Evaluate additional providers and targets when an analyst workflow demonstrates
  a capability gap.

## Admission criteria

New capabilities must return useful evidence through shared CLI/MCP workflows,
preserve observations and unknowns, and declare actual authority and lifecycle
constraints. Agents compose experiments using ordinary commands, scripts, and
fixture servers; custom orchestration needs a demonstrated requirement.

Provider and platform claims require their corresponding
[real verification lanes](testing.md#real-toolchain-verification-lanes).
See [tool design](tool-design.md) for choosing a tool boundary and
[Ghidra semantics](ghidra-provider.md) for the existing deep-provider contract.

Setup remains additive, reuses existing tools, and requires approval for disclosed
configuration and Hopper installation changes. Additional installer choices need
an implemented toolchain and explicit scope; setup does not install or upgrade
unrelated runtimes or dependencies.

### docs/architecture.mermaid

graph TD
    subgraph "Entry Points"
        CLI["src/cli.ts + src/cli/<br/>One-shot CLI adapter<br/>setup, diagnostics, analysis, decompilation"]
        MAIN["src/main.ts + src/main/<br/>MCP stdio server adapter<br/>config, session, process lifetime"]
        DISPATCH["scripts/rea.mjs<br/>Executable dispatcher<br/>routes mcp / one-shot"]
    end

    subgraph "Production Composition"
        COMPOSITION["src/composition/<br/>fresh typed provider and session factories<br/>one-shot binding and independent optional loading<br/>static WASM/EVM descriptors: named contracts, factories, retryable lifetimes"]
    end

    subgraph "Adapters"
        SERVER["src/server/<br/>MCP request translation<br/>createServer, tool registration, toolResult"]
        HOPPER_BRIDGE["bridge/hopper_bridge.py<br/>Runs inside Hopper<br/>adapts operations to Hopper Python API"]
        GHIDRA_BRIDGE["bridge/ghidra/ReaGhidraBridge.java<br/>Packaged HeadlessScript<br/>inventory, decompiler, references, CFG"]
        INSTALL["src/cli/ + src/application/Setup*<br/>Host installation adapters<br/>macOS: verified vendor DMG to ~/Applications<br/>Linux: verified vendor package + apt/dnf/pacman"]
    end

    subgraph "Application Layer"
        APP["src/application/<br/>Shared CLI/MCP workflows<br/>enhanced analysis and investigations"]
        SESSION["SessionProviderRouter + BinarySession<br/>one immutable deep binding per target<br/>disjoint auxiliary routing"]
        REGISTRY["AnalysisProviderRegistry<br/>sorted deep candidates<br/>deterministic selection, no fallback"]
        RECORDS["src/application/investigation/<br/>composed InvestigationRecords + narrow ports<br/>EvidenceLedger and Unknown ownership"]
        SNAPSHOT["BinarySessionRecords + AnalysisSnapshotCache<br/>binary target/profile snapshots<br/>compatibility facade and post-commit notifications"]
        JS_RECON["src/application/javascript/ + src/artifacts/javascript/<br/>JavaScript artifact reconstruction<br/>directory/ASAR reads<br/>AST-only bundle projection"]
    end

    subgraph "Provider Layers"
        PWNTOOLS["src/native/pwntools/ + src/native/pwndbg/<br/>BYO offline ELF/core adapters<br/>owned snapshots/Python and optional core-only GDB<br/>unchanged upstream parsers, ABI structures and mapping API"]
        WASM["src/wasm/<br/>caller-supplied WABT; immutable artifact inspection<br/>owned process supervision and retryable workspace cleanup"]
        EVM["src/evm/<br/>unchanged EVMole/WASM in bounded owned worker<br/>explicit carrier parsing and inferred interface adapter"]
        HOPPER["src/hopper/<br/>Hopper launch & Unix-socket protocol<br/>BridgeLauncher, HopperClient, protocol"]
        GHIDRA["src/ghidra/<br/>Ghidra discovery, profile & function analysis<br/>snapshot, Unix/Windows transport, bounded lifecycle"]
        IDA["src/ida/<br/>Upstream MCP contract adaptation<br/>live GUI binding or owned headless database"]
        IDA_MCP["External ida-pro-mcp<br/>GUI proxy or database supervisor<br/>upstream installation and engine lifecycle"]
        AUX["src/artifacts/ + src/native/<br/>artifact inventory and extraction<br/>format readers and native capabilities"]
        BROWSER["src/browser/<br/>CDP / Playwright capture<br/>captured scripts and native module resolution<br/>execution/: coverage, listener and source attribution"]
        JS_CODEC["src/javascript/sourceMaps/<br/>pinned upstream map codec<br/>owned heap-limited Node process, complete point evidence"]
        INSPECTOR["src/inspector/<br/>passive V8 Inspector discovery and capture<br/>script and target locations"]
        DOTNET["src/dotnet/<br/>Managed static metadata provider<br/>PE/CLI metadata inventory, members, IL"]
        OBJDUMP["src/objdump/<br/>GNU objdump command profile"]
        RIZIN["src/rizin/<br/>Static command profile and persistent debugger sessions"]
        GDB["src/gdb/<br/>Persistent GDB/MI sessions<br/>owned process lifecycle and target state"]

        FIRMWARE["src/firmware/<br/>Binwalk / Unblob adapters<br/>owned processes, report normalization, private extraction"]
        ANDROID["src/android/<br/>Static APK adapter<br/>owned SDK stdio, pinned headless JADX, normalization"]
        REFERENCE["src/reference/<br/>Filesystem reference-source reader<br/>bounded traversal, validation, errors"]
    end

    subgraph "Provider Process Foundation"
        PROCESS["src/process/<br/>owned process groups, private roots<br/>deadlines, bounded file reads and diagnostics, cleanup"]
        WINDOWS["src/windows/<br/>Windows host boundary adapters<br/>package loader, opaque handles, owned jobs and private runtimes"]
        WINDOWS_NATIVE["native/windows/src/<br/>Node-API implementation<br/>NTFS admission, protected DACLs and atomic Job Object assignment"]
    end

    subgraph "Contracts Layer"
        CONTRACTS["src/contracts/<br/>Caller-visible schemas for analysis, reverse engineering, managed, browser, Electron, application, and session tools"]
        ERRORS["src/contracts/errorSchemas.ts<br/>Shared analysis error schemas<br/>CLI diagnostics, generated error catalog"]
    end

    subgraph "Domain Layer"
        DOMAIN["src/domain/<br/>Pure side-effect-free modules<br/>evidence, comparisons, application graphs"]
    end

    subgraph "Configuration"
        CONFIG["src/config/<br/>Zod-validated env parsing<br/>provider settings and origins"]
    end

    subgraph "Tests"
        TESTS["tests/<br/>Vitest suite<br/>fixtures/ holds fake launcher, bridge, and CDP seams"]
    end

    subgraph "Evaluation"
        EVALUATION["src/evaluation/<br/>Agent release evaluation<br/>session transcript scoring"]
    end

    DISPATCH --> CLI
    DISPATCH --> MAIN
    MAIN --> CONFIG
    MAIN --> SERVER
    MAIN --> APP
    CLI --> APP
    MAIN --> COMPOSITION
    CLI --> COMPOSITION
    SERVER --> COMPOSITION
    COMPOSITION --> SESSION
    APP --> FIRMWARE
    FIRMWARE --> PROCESS
    FIRMWARE --> CONTRACTS
    APP --> ANDROID
    ANDROID --> PROCESS
    ANDROID --> CONTRACTS
    ANDROID --> DOMAIN
    CLI --> ERRORS
    APP --> SESSION
    SESSION --> REGISTRY
    SESSION --> SNAPSHOT
    SNAPSHOT --> RECORDS
    APP -->|record callbacks| RECORDS
    SERVER -->|narrow record ports| RECORDS
    RECORDS --> DOMAIN
    COMPOSITION --> WASM
    WASM --> PROCESS
    WASM --> DOMAIN
    COMPOSITION --> PWNTOOLS
    PWNTOOLS --> PROCESS
    PWNTOOLS --> DOMAIN
    COMPOSITION --> HOPPER
    COMPOSITION --> GHIDRA
    COMPOSITION --> IDA
    COMPOSITION --> AUX
    IDA --> IDA_MCP
    IDA --> CONTRACTS
    IDA --> DOMAIN
    SESSION --> AUX
    APP --> JS_RECON
    APP --> INSTALL
    SERVER --> CONTRACTS
    SERVER --> APP
    APP --> BROWSER
    APP -->|source-map codec port| JS_CODEC
    JS_CODEC --> PROCESS
    JS_CODEC --> DOMAIN
    APP -->|runtime observation port| INSPECTOR
    INSPECTOR -->|shared CDP and file-location helpers| BROWSER
    INSPECTOR --> DOMAIN
    APP --> DOTNET
    DOTNET --> DOMAIN
    COMPOSITION --> OBJDUMP
    OBJDUMP --> DOMAIN
    COMPOSITION --> RIZIN
    RIZIN --> DOMAIN
    CLI --> GDB
    SERVER --> GDB
    GDB --> PROCESS
    GDB --> DOMAIN
    HOPPER --> HOPPER_BRIDGE
    GHIDRA --> GHIDRA_BRIDGE
    HOPPER --> PROCESS
    GHIDRA --> PROCESS
    GHIDRA --> WINDOWS
    PROCESS --> WINDOWS
    WINDOWS --> WINDOWS_NATIVE
    APP --> PROCESS
    APP --> DOMAIN
    JS_RECON --> AUX
    JS_RECON --> DOMAIN
    APP --> REFERENCE
    REFERENCE --> DOMAIN
    CONTRACTS --> DOMAIN
    HOPPER --> DOMAIN
    GHIDRA --> DOMAIN
    AUX --> DOMAIN
    BROWSER --> DOMAIN
    PROCESS --> DOMAIN
    TESTS -.-> MAIN
    TESTS -.-> HOPPER
    TESTS -.-> GHIDRA
    TESTS -.-> IDA
    TESTS -.-> PROCESS
    TESTS -.-> BROWSER
    TESTS -.-> EVALUATION
    TESTS -.-> ERRORS

    COMPOSITION --> EVM
    APP -->|EVM interface port| EVM
    EVM --> PROCESS
    EVM --> DOMAIN

### docs/ (directory listing)

- .vitepress
- adb-device-analysis.md
- android-analysis.md
- apktool-resource-analysis.md
- apple-application-analysis.md
- architecture.mermaid
- assets
- binary-diagnostics.md
- browser-observation.md
- browser-scenario-contract.md
- cli.md
- client-configuration.md
- client-verification.md
- electron-fuses.md
- electron-observation.md
- error-contract.schema.json
- evm-bytecode.md
- firmware-analysis.md
- flutter-analysis.md
- frida-instrumentation.md
- ghidra-dos.md
- ghidra-mips.md
- ghidra-nativeaot.md
- ghidra-ppc.md
- ghidra-provider.md
- ghidra-psp.md
- ghidra-riscv.md
- go-binaries.md
- harmony-analysis.md
- http3-capture-lab.md
- ida-provider.md
- index.md
- installation.md
- javascript-application-graph.md
- javascript-application-workflows.md
- javascript-artifact-reconstruction.md
- javascript-recovery.md
- javascript-runtime-observation.md
- javascript-runtime-reconciliation.md
- jeb-analysis.md
- kuna-provider.md
- managed-code-analysis.md
- mcp-contracts.md
- mcp-prompts.md
- migration-6.2.md
- native-investigation.md
- packet-captures.md
- pcap-analysis.md
- process-capture.md
- raw-binary.md
- readme
- reconstruction-obligation-ledgers.md
- reconstruction-readiness.md
- recorded-crashes.md
- releases
- releasing.md
- reverse-engineering-tools.md
- roadmap.md
- rust-binaries.md
- signal-recordings.md
- specs
- sqlite-databases.md
- testing.md
- tool-design.md
- user-visible-errors.csv
- wasm-artifacts.md
- web-network-captures.md
- web-runtime.md
- web-source-location.md
- website-module-trace.md
- website-script-export.md
- windows-ghidra-p0.md

### AGENTS.md (repo agent instructions)

# Repository Guidelines

## Product and Authority

REA is a local-only reverse-engineering tool with shared CLI/MCP workflows. Distinguish observations, derivations, inferences, and unknowns; preserve Evidence provenance and session semantics through both adapters. Provider support and setup live in [README.md](README.md#choosing-a-deep-analysis-provider) and its linked guides.

Follow the [contribution scope and fail-closed integration rule](CONTRIBUTING.md#contribution-scope). Do not integrate capabilities while material scope, authority, side-effect, or required verification questions remain unresolved. For new providers or capabilities involving target execution, injection, mutation, or protection recovery, seek the required maintainer scope decision before substantial implementation for integration. Welcome early proposals, small exploratory prototypes, and draft PRs that help resolve questions; they do not authorize integration.

Ghidra uses ephemeral databases without modifying executable bytes or controlling a GUI; Windows Ghidra P0 has no mutation authority. IDA analysis is read-only; never save or close an attached GUI database.

Configuration changes must be additive and idempotent, with backups. Installers must not install or upgrade unrelated software, including Homebrew, Node.js, npm, Java, or Ghidra. Ghidra and IDA are bring-your-own. `rea setup` must show its planned changes and require approval before writing files or installing Hopper.

Preserve caller-selected inputs and local evidence, including output, URLs, paths, digests, and metadata. Redact transport authentication credentials and explicitly marked sensitive values; do not infer secrecy from names or text patterns. Do not persist the ambient environment merely because a child inherits it.

## Architecture and Cleanup

Dependencies flow inward: domain semantics and contracts, provider adapters, shared application workflows, then CLI/MCP adapters. Keep engine protocols and provider-specific code out of domain/application layers. See [docs/architecture.mermaid](docs/architecture.mermaid) when changing composition.

Give each interpretation and resource a clear owner. Consumers must use that owner's parsed facts rather than reinterpret raw source. Preserve identity, omission, uncertainty, and source evidence across boundaries. Retain ownership of resources whose cleanup failed. Reuse `src/process/` supervision and identity primitives; a PID and executable path alone do not establish ownership after exit or reuse.

Keep proof of ownership separate from validity, editability, and readiness. Malformed owned data may still be safely removable. Unresolved identity or applicability must remain unknown rather than be treated as absent, foreign, or aligned.

Assess brittleness in touched code during implementation, debugging, review, and maintenance. Fix the producing representation or ownership rule before adding downstream repairs. Normalize once at the owning boundary using format-aware parsers. Remove superseded representations, aliases, wrappers, and redundant tests after verifying affected consumers. Introduce abstractions only when they remove observed complexity.

When fixing a bug, inspect the producing boundary and affected consumers for duplicated interpretation or unclear ownership. Complete any directly related refactor in the same change and remove superseded code. Passing regression tests alone does not establish that the brittleness is resolved. If related cleanup remains, explain what remains and why.

When addressing a review thread, inspect the producing boundary and affected consumers for brittleness. Complete directly related refactoring in the same change. Before resolving the thread, explain the root cause, structural fix, validation, and any remaining cleanup.

Parse unknown boundary values and model expected failures with the tagged error algebra and `Result`. Preserve partial facts and meaningful failure reasons. Keep identity and lookup values separate from display formatting; preserve source values and explicit unknowns when normalization loses information. Absolute paths, file URLs, and HTTP paths have different semantics.

Validate advertised JSON Schemas after SDK conversion against their declared dialect and actual clients. Bind handlers to named contracts with exact types; catalog ordering must never select an operation or schema.

## Performance

Design analysis workflows and agent interfaces for efficiency from the first
implementation. Correctness, useful answers, Evidence provenance, caller choices,
compatibility and safe resource bounds remain required.

Optimize in this order:

1. Agent tokens and context. Return the smallest sufficient answer with
   necessary provenance, coverage and limitations. Use task selection,
   summaries, paging and retained Evidence where supported; honor requested
   detail and keep complete Evidence accessible. Count the whole task,
   including schemas, extra calls and retries.
2. Analysis time. Reuse validated results and shared work. Cache keys must
   cover result-affecting inputs; define invalidation and lifetime. Validate
   freshness before reporting cached live state as current.
3. CPU and memory. Avoid unnecessary work and copies; bound concurrency,
   retained state and serialization growth.

For changes affecting these costs, measure representative completed tasks and
compare equivalent workflows before and after where available. Report token
usage, elapsed time, CPU time and peak process-family memory. Separate cold
and warm runs, label estimates, and state unmeasured costs. Fewer bytes alone
do not establish fewer tokens or faster analysis.

## Development

Use [.nvmrc](.nvmrc) and `package.json#packageManager` for the pinned toolchain. Cursor Cloud may place older Node.js first on `PATH`; environment setup installs the pinned toolchain under `/usr/local/bin`.

- `npm ci`: install locked dependencies.
- `npm run build:cached`: build the runtime and packaged skill.
- `npm run test:local -- PATH...`: source tests without building.
- `npm run test:focused -- PATH...`: exact tests with their required artifacts.
- `npm run check:fast`: cached typecheck/lint and the pre-push check.
- `npm run docs:check`: validate generated documentation.

Use relevant checks for the change. The complete local gate, `npm run check:pr`, is optional for broad changes or CI diagnosis. See [CONTRIBUTING.md](CONTRIBUTING.md) for development, generated-file ownership, and release conventions.

`docs/public/product-catalog.json`, `docs/verification/managed-conformance-*.json`, and `skills/` are ignored outputs. Edit source contracts and `.agents/skills/reverse-engineer-anything/`, then regenerate as needed. `.cache/mcp-tool-catalog.json` is test metadata; runtime builds and source checking do not consume it. Never commit binaries, provider project documents, credentials, `dist/`, `node_modules/`, or local planning artifacts.

## Tool and Test Changes

For tool design, follow [docs/tool-design.md](docs/tool-design.md): start from the analyst question, reuse existing contracts, preserve caller choices, and return useful evidence inline. Limits must follow real format, protocol, authority, or resource constraints. Account for representation expansion before allocation; derive completeness from examined coverage.

For test changes or provider claims, use [docs/testing.md](docs/testing.md). Prefer real public CLI/MCP workflows, then production-boundary integration, then producer goldens. Keep module tests for distinct semantics stronger workflows cannot reliably reproduce. Preserve malformed-input, cancellation, cleanup, permission, capacity, and target-identity coverage when pruning. Report unverified coverage explicitly; simulated providers do not establish real-provider behavior.

Use Conventional Commit subjects and PR titles. Mark breaking changes with `!` or a `BREAKING CHANGE:` footer. Describe behavior changes, relevant validation, and real-provider verification scope.

## Issue Reports

Follow [issue reporting guidance](CONTRIBUTING.md#reporting-issues) and the matching
issue form. Keep reports concise and cite the smallest useful evidence.
Distinguish observed results, source-derived reasoning, hypotheses, and proposed
checks. Never claim runtime reproduction or measurements you did not perform.
Use `NOT_ENOUGH_INFO` with an explanation for missing narrative answers or evidence.
Incomplete reports, source-only findings, and early feature or design ideas are
welcome when their limitations are explicit; a completed diagnosis or fix is not
required to open an issue.

## Pull Request Readiness

Follow [human ownership and readiness](CONTRIBUTING.md#pull-request-ownership-and-readiness)
when preparing a PR. AI-assisted contributions are welcome; a human must review
and own the final diff, check the validation evidence and its limitations, and
explicitly declare the PR ready for initial maintainer review.

Keep the PR body concise and current, with the concrete problem, observable
outcome, approach, and evidence. Report only checks that actually ran as executed;
distinguish source-derived conclusions, proposed checks, and unavailable coverage.
Address actionable automated review findings and explain disagreements.

Leave the template's **Author readiness** declarations unchecked for the human
owner to complete. Never attest to human review on their behalf. Keep the PR in
draft until the human declares the PR initially ready. Later pushes do not
invalidate that declaration or require another human sign-off. Keep the PR body
and affected validation current as work changes. The readiness check validates
the filled declaration; CI and automated review results do not establish that
human review occurred, maintainer scope approval, or merge permission.

<!-- BEGIN:turborepo-agent-rules -->

# This is NOT the Turborepo you know

Turborepo configuration, task behavior, and CLI commands can vary between installed versions and may differ from your training data. Resolve the `turbo` package from this file's directory or relevant workspace; in monorepos, it may not be visible from the repository root. For example, run `node -p "require.resolve('turbo/package.json')"` from a workspace that depends on `turbo`.

Read `docs/README.md` inside that installed package first, then read the relevant pages from its `docs/` directory before changing Turborepo configuration or commands. Heed deprecation notices. These bundled docs match the installed package version and are available without network access.

This block is written and re-added by `turbo` before repository-scoped commands when an AI agent is detected. In the Turborepo source repository, its template is defined in `crates/turborepo-cli/src/cli/agent_guidance.rs`. Removing the managed block while updates are enabled means a later qualifying invocation will add it again. Set `"agentGuidance": false` in the root `turbo.json` or `turbo.jsonc` to opt out; this does not remove an existing block. Keep the block committed with your work to avoid an uncommitted change on the next agent invocation.
<!-- END:turborepo-agent-rules -->

## Top-level structure
- `src/` — TypeScript runtime: CLI adapter, MCP stdio server, shared workflows, composition, contracts, domain, config and provider adapters
- `bridge/` — engine-side bridges (Hopper, Ghidra, Android, mitmproxy, native, process, pwndbg, pwntools)
- `native/` — native host implementation (Windows Node-API host)
- `docs/` — guides and contracts (see listing above), `readme/` translations (19 languages), `releases/`, `specs/`, `.vitepress/` site config
- `.agents/` — agent skills source (packaged REA investigation skill)
- `website/` — rea.tools site source
- `experiments/` — experimental work
- `tests/` — Vitest suites
- `scripts/` — build/verify/generate scripts (`rea.mjs` dispatcher)
- `third_party/` — upstream engines as submodules
- `licenses/`, `LICENSE`, `THIRD_PARTY_NOTICES.md`, `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `AGENTS.md`
- Root config: `package.json`, `turbo.json`, `vitest*.config.ts`, `stryker*.config.mjs` (mutation testing), `knip.json`, `server.json` (MCP Registry manifest), `install.sh`, `release-please-config.json`
