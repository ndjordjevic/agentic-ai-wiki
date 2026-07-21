# rtk-ai/rtk

## Metadata
- Stars: 72152
- Primary language: Rust
- Default branch: develop
- Latest release: dev-0.44.0-rc.323 (2026-07-20)
- License: Apache License 2.0
- Homepage: https://www.rtk-ai.app
- Fetched: 2026-07-21
- Final URL: https://github.com/rtk-ai/rtk

## Description
CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

## README
<p align="center">
  <img src="https://avatars.githubusercontent.com/u/258253854?v=4" alt="RTK - Rust Token Killer" width="500">
</p>

<p align="center">
  <strong>High-performance CLI proxy that reduces LLM token consumption by 60-90%</strong>
</p>

<p align="center">
  <a href="https://github.com/rtk-ai/rtk/actions"><img src="https://github.com/rtk-ai/rtk/workflows/Security%20Check/badge.svg" alt="CI"></a>
  <a href="https://github.com/rtk-ai/rtk/releases"><img src="https://img.shields.io/github/v/release/rtk-ai/rtk" alt="Release"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://discord.gg/RySmvNF5kF"><img src="https://img.shields.io/discord/1470188214710046894?label=Discord&logo=discord" alt="Discord"></a>
  <a href="https://formulae.brew.sh/formula/rtk"><img src="https://img.shields.io/homebrew/v/rtk" alt="Homebrew"></a>
</p>

<p align="center">
  <a href="https://www.rtk-ai.app">Website</a> &bull;
  <a href="#installation">Install</a> &bull;
  <a href="https://www.rtk-ai.app/guide/troubleshooting">Troubleshooting</a> &bull;
  <a href="docs/contributing/ARCHITECTURE.md">Architecture</a> &bull;
  <a href="https://discord.gg/RySmvNF5kF">Discord</a>
</p>

<p align="center">
  <a href="README.md">English</a> &bull;
  <a href="README_fr.md">Francais</a> &bull;
  <a href="README_zh.md">中文</a> &bull;
  <a href="README_ja.md">日本語</a> &bull;
  <a href="README_ko.md">한국어</a> &bull;
  <a href="README_es.md">Espanol</a> &bull;
  <a href="README_pt.md">Português</a>
</p>

---

rtk filters and compresses command outputs before they reach your LLM context. Single Rust binary, 100+ supported commands, <10ms overhead.

## Token Savings (30-min Claude Code Session)

| Operation | Frequency | Standard | rtk | Savings |
|-----------|-----------|----------|-----|---------|
| `ls` / `tree` | 10x | 2,000 | 400 | -80% |
| `cat` / `read` | 20x | 40,000 | 12,000 | -70% |
| `grep` / `rg` | 8x | 16,000 | 3,200 | -80% |
| `git status` | 10x | 3,000 | 600 | -80% |
| `git diff` | 5x | 10,000 | 2,500 | -75% |
| `git log` | 5x | 2,500 | 500 | -80% |
| `git add/commit/push` | 8x | 1,600 | 120 | -92% |
| `cargo test` / `npm test` | 5x | 25,000 | 2,500 | -90% |
| `ruff check` | 3x | 3,000 | 600 | -80% |
| `pytest` | 4x | 8,000 | 800 | -90% |
| `go test` | 3x | 6,000 | 600 | -90% |
| `docker ps` | 3x | 900 | 180 | -80% |
| **Total** | | **~118,000** | **~23,900** | **-80%** |

> Estimates based on medium-sized TypeScript/Rust projects. Actual savings vary by project size.

## Installation

### Homebrew (recommended)

```bash
brew install rtk
```

### Quick Install (Linux/macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

> Installs to `~/.local/bin`. Add to PATH if needed:
> ```bash
> echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc
> ```

### Cargo

```bash
cargo install --git https://github.com/rtk-ai/rtk
```

### Pre-built Binaries

Download from [releases](https://github.com/rtk-ai/rtk/releases):
- macOS: `rtk-x86_64-apple-darwin.tar.gz` / `rtk-aarch64-apple-darwin.tar.gz`
- Linux: `rtk-x86_64-unknown-linux-musl.tar.gz` / `rtk-aarch64-unknown-linux-gnu.tar.gz`
- Windows: `rtk-x86_64-pc-windows-msvc.zip`

> **Windows users**: Extract the zip and place `rtk.exe` somewhere in your PATH (e.g. `C:\Users\<you>\.local\bin`). Run RTK from **Command Prompt**, **PowerShell**, or **Windows Terminal** — do not double-click the `.exe` (it will flash and close). The full hook system works natively on Windows (and in [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)). See [Windows setup](#windows) below for details.

### Verify Installation

```bash
rtk --version   # Should show "rtk 0.28.2"
rtk gain        # Should show token savings stats
```

> **Name collision warning**: Another project named "rtk" (Rust Type Kit) exists on crates.io. If `rtk gain` fails, you have the wrong package. Use `cargo install --git` above instead.

## Quick Start

```bash
# 1. Install for your AI tool
rtk init -g                     # Claude Code / Copilot (default)
rtk init -g --gemini            # Gemini CLI
rtk init -g --codex             # Codex (OpenAI)
rtk init -g --agent cursor      # Cursor
rtk init -g --agent windsurf    # Windsurf
rtk init --agent cline          # Cline / Roo Code
rtk init --agent kilocode       # Kilo Code
rtk init --agent antigravity    # Google Antigravity
rtk init --agent kimi           # Kimi AI
rtk init -g --agent pi          # Pi
rtk init --agent hermes         # Hermes
rtk init -g --agent droid       # Factory Droid

# 2. Restart your AI tool, then test
git status  # Automatically rewritten to rtk git status
```

Hook-based agents rewrite Bash commands (e.g., `git status` -> `rtk git status`) before execution. Plugin-based agents, including Hermes, use their plugin API to rewrite commands before execution. The agent receives compact output without needing to call `rtk` explicitly.

**Important:** the hook only runs on Bash tool calls. Claude Code built-in tools like `Read`, `Grep`, and `Glob` do not pass through the Bash hook, so they are not auto-rewritten. To get RTK's compact output for those workflows, use shell commands (`cat`/`head`/`tail`, `rg`/`grep`, `find`) or call `rtk read`, `rtk grep`, or `rtk find` directly.

## How It Works

```
  Without rtk:                                    With rtk:

  Claude  --git status-->  shell  -->  git         Claude  --git status-->  RTK  -->  git
    ^                                   |            ^                      |          |
    |        ~2,000 tokens (raw)        |            |   ~200 tokens        | filter   |
    +-----------------------------------+            +------- (filtered) ---+----------+
```

Four strategies applied per command type:

1. **Smart Filtering** - Removes noise (comments, whitespace, boilerplate)
2. **Grouping** - Aggregates similar items (files by directory, errors by type)
3. **Truncation** - Keeps relevant context, cuts redundancy
4. **Deduplication** - Collapses repeated log lines with counts

## Commands

### Files
```bash
rtk ls .                        # Token-optimized directory tree
rtk read file.rs                # Smart file reading
rtk read file.rs -l aggressive  # Signatures only (strips bodies)
rtk smart file.rs               # 2-line heuristic code summary
rtk find "*.rs" .               # Compact find results
rtk grep "pattern" .            # Grouped search results
rtk diff file1 file2            # Condensed diff (exit 1 if files differ)
```

### Git
```bash
rtk git status                  # Compact status
rtk git log -n 10               # One-line commits
rtk git diff                    # Condensed diff
rtk git add                     # -> "ok"
rtk git commit -m "msg"         # -> "ok abc1234"
rtk git push                    # -> "ok main"
rtk git pull                    # -> "ok 3 files +10 -2"
```

### GitHub CLI
```bash
rtk gh pr list                  # Compact PR listing
rtk gh pr view 42               # PR details + checks
rtk gh issue list               # Compact issue listing
rtk gh run list                 # Workflow run status
```

### Test Runners
```bash
rtk jest                        # Jest compact (failures only)
rtk vitest                      # Vitest compact (failures only)
rtk playwright test             # E2E results (failures only)
rtk pytest                      # Python tests (-90%)
rtk go test                     # Go tests (NDJSON, -90%)
rtk cargo test                  # Cargo tests (-90%)
rtk rake test                   # Ruby minitest (-90%)
rtk rspec                       # RSpec tests (JSON, -60%+)
rtk err <cmd>                   # Filter errors only from any command
rtk test <cmd>                  # Generic test wrapper - failures only (-90%)
```

### Build & Lint
```bash
rtk lint                        # ESLint grouped by rule/file
rtk lint biome                  # Supports other linters
rtk tsc                         # TypeScript errors grouped by file
rtk next build                  # Next.js build compact
rtk prettier --check .          # Files needing formatting
rtk cargo build                 # Cargo build (-80%)
rtk cargo clippy                # Cargo clippy (-80%)
rtk ruff check                  # Python linting (JSON, -80%)
rtk golangci-lint run           # Go linting (JSON, -85%)
rtk rubocop                     # Ruby linting (JSON, -60%+)
```

### Package Managers
```bash
rtk pnpm list                   # Compact dependency tree
rtk uv run pytest               # Preserve uv env, errors only
rtk pip list                    # Python packages (auto-detect uv)
rtk pip outdated                # Outdated packages
rtk bundle install              # Ruby gems (strip Using lines)
rtk prisma generate             # Schema generation (no ASCII art)
```

### AWS
```bash
rtk aws sts get-caller-identity # One-line identity
rtk aws ec2 describe-instances  # Compact instance list
rtk aws lambda list-functions   # Name/runtime/memory (strips secrets)
rtk aws logs get-log-events     # Timestamped messages only
rtk aws cloudformation describe-stack-events  # Failures first
rtk aws dynamodb scan           # Unwraps type annotations
rtk aws iam list-roles          # Strips policy documents
rtk aws s3 ls                   # Truncated with tee recovery
```

### Containers
```bash
rtk docker ps                   # Compact container list
rtk docker images               # Compact image list
rtk docker logs <container>     # Deduplicated logs
rtk docker compose ps           # Compose services
rtk kubectl pods                # Compact pod list
rtk kubectl logs <pod>          # Deduplicated logs
rtk kubectl services            # Compact service list
rtk oc get pods                 # OpenShift pod summary
rtk oc get services             # OpenShift service list
rtk oc logs <pod>               # Deduplicated logs
```

### Infrastructure as Code
```bash
rtk pulumi preview              # Strip header/URL/duration noise
rtk pulumi up                   # Compact apply output
rtk pulumi destroy              # Compact destroy output
rtk pulumi refresh              # Drift summary
rtk pulumi stack                # Stack metadata (strips owner/timestamps)
```

### Data & Analytics
```bash
rtk json config.json            # Structure without values
rtk deps                        # Dependencies summary
rtk env -f AWS                  # Filtered env vars
rtk log app.log                 # Deduplicated logs
rtk curl <url>                  # Truncate + save full output
rtk wget <url>                  # Download, strip progress bars
rtk summary <long command>      # Heuristic summary
rtk proxy <command>             # Raw passthrough + tracking
```

### Token Savings Analytics
```bash
rtk gain                        # Summary stats
rtk gain --graph                # ASCII graph (last 30 days)
rtk gain --history              # Recent command history
rtk gain --daily                # Day-by-day breakdown
rtk gain --all --format json    # JSON export for dashboards

rtk discover                    # Find missed savings opportunities
rtk discover --all --since 7    # All projects, last 7 days

rtk session                     # Show RTK adoption across recent sessions
```

## Global Flags

```bash
-u, --ultra-compact    # ASCII icons, inline format (extra token savings)
-v, --verbose          # Increase verbosity (-v, -vv, -vvv)
```

## Examples

**Directory listing:**
```
# ls -la (45 lines, ~800 tokens)        # rtk ls (12 lines, ~150 tokens)
drwxr-xr-x  15 user staff 480 ...       my-project/
-rw-r--r--   1 user staff 1234 ...       +-- src/ (8 files)
...                                      |   +-- main.rs
                                         +-- Cargo.toml
```

**Git operations:**
```
# git push (15 lines, ~200 tokens)       # rtk git push (1 line, ~10 tokens)
Enumerating objects: 5, done.             ok main
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
...
```

**Test output:**
```
# cargo test (200+ lines on failure)     # rtk test cargo test (~20 lines)
running 15 tests                          FAILED: 2/15 tests
test utils::test_parse ... ok               test_edge_case: assertion failed
test utils::test_format ... ok              test_overflow: panic at utils.rs:18
...
```

## Auto-Rewrite Hook

The most effective way to use rtk. The hook transparently intercepts Bash commands and rewrites them to rtk equivalents before execution.

**Result**: 100% rtk adoption across all conversations and subagents, zero token overhead.

**Scope note:** this only applies to Bash tool calls. Claude Code built-in tools such as `Read`, `Grep`, and `Glob` bypass the hook, so use shell commands or explicit `rtk` commands when you want RTK filtering there.

### Setup

```bash
rtk init -g                 # Install hook + RTK.md (recommended)
rtk init -g --opencode      # OpenCode plugin (instead of Claude Code)
rtk init -g --auto-patch    # Non-interactive (CI/CD)
rtk init -g --hook-only     # Hook only, no RTK.md
rtk init --show             # Verify installation
```

After install, **restart Claude Code**.

## Windows

RTK works fully on native Windows. Since **v0.37.2** the auto-rewrite hook runs as a **native binary command** (`rtk hook claude`) — no Unix shell, bash, or jq required — so commands are rewritten transparently on Command Prompt, PowerShell, and Windows Terminal, just like on Linux and macOS.

### Native Windows

```powershell
# 1. Download and extract rtk-x86_64-pc-windows-msvc.zip from releases
# 2. Add rtk.exe to your PATH (e.g. C:\Users\<you>\.local\bin)
# 3. Initialize — installs the native binary hook
rtk init -g
```

**Upgrading from an older install?** If you set RTK up before v0.37.2 you may still have the legacy `rtk-rewrite.sh` shell hook (which does need a Unix shell). Re-run `rtk init -g` to migrate to the native binary hook.

**Prerequisites**: some filters shell out to [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`). Install it and keep it on your PATH (e.g. `winget install BurntSushi.ripgrep.MSVC`) to avoid `Binary 'rg' not found on PATH` warnings.

**Important**: Do not double-click `rtk.exe` — it is a CLI tool that prints usage and exits immediately. Always run it from a terminal (Command Prompt, PowerShell, or Windows Terminal).

### WSL

[WSL](https://learn.microsoft.com/en-us/windows/wsl/install) also works and behaves exactly like Linux:

```bash
# Inside WSL
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
rtk init -g
```

| Feature | Native Windows | WSL |
|---------|----------------|-----|
| Filters (cargo, git, etc.) | Full | Full |
| Auto-rewrite hook | Yes (native binary) | Yes |
| `rtk init -g` | Hook mode | Hook mode |
| `rtk gain` / analytics | Full | Full |

## Supported AI Tools

RTK supports 15 AI coding tools. Each integration rewrites shell commands to `rtk` equivalents for 60-90% token savings where the agent supports command interception.

| Tool | Install | Method |
|------|---------|--------|
| **Claude Code** | `rtk init -g` | PreToolUse hook (native binary) |
| **GitHub Copilot (VS Code)** | `rtk init -g --copilot` | PreToolUse hook — transparent rewrite |
| **GitHub Copilot CLI** | `rtk init -g --copilot` | PreToolUse deny-with-suggestion (CLI limitation) |
| **Cursor** | `rtk init -g --agent cursor` | preToolUse hook (hooks.json) |
| **Gemini CLI** | `rtk init -g --gemini` | BeforeTool hook |
| **Codex** | `rtk init -g --codex` | AGENTS.md + RTK.md instructions |
| **Windsurf** | `rtk init -g --agent windsurf` | .windsurfrules (project-scoped) |
| **Cline / Roo Code** | `rtk init --agent cline` | .clinerules (project-scoped) |
| **OpenCode** | `rtk init -g --opencode` | Plugin TS (tool.execute.before) |
| **OpenClaw** | `openclaw plugins install ./openclaw` | Plugin TS (before_tool_call) |
| **Pi** | `rtk init -g --agent pi` (global) | TypeScript extension (tool_call) |
| **Hermes** | `rtk init --agent hermes` | Python plugin adapter (terminal command mutation via `rtk rewrite`) |
| **Mistral Vibe** | Planned ([#800](https://github.com/rtk-ai/rtk/issues/800)) | Blocked on upstream |
| **Kilo Code** | `rtk init --agent kilocode` | .kilocode/rules/rtk-rules.md (project-scoped) |
| **Google Antigravity** | `rtk init --agent antigravity` | .agents/rules/antigravity-rtk-rules.md (project-scoped) |
| **Kimi AI** | `rtk init --agent kimi` | AGENTS.md (project-scoped) |
| **Factory Droid** | `rtk init -g --agent droid` (or per-project) | PreToolUse hook in `~/.factory/hooks.json` (matcher `Execute`) |

For per-agent setup details, override controls, and graceful degradation, see the [Supported Agents guide](https://www.rtk-ai.app/guide/getting-started/supported-agents). The Hermes plugin source and tests live in `hooks/hermes/`; installed Hermes runtime files still live under `~/.hermes/plugins/rtk-rewrite/`.

## Configuration

`~/.config/rtk/config.toml` (macOS: `~/Library/Application Support/rtk/config.toml`):

```toml
[hooks]
exclude_commands = ["curl", "playwright"]  # skip rewrite for these

[tee]
enabled = true          # save raw output on failure (default: true)
mode = "failures"       # "failures", "always", or "never"
```

When a command fails, RTK saves the full unfiltered output so the LLM can read it without re-executing:

```
FAILED: 2/15 tests
[full output: ~/.local/share/rtk/tee/1707753600_cargo_test.log]
```

For the full config reference (all sections, env vars, per-project filters), see the [Configuration guide](https://www.rtk-ai.app/guide/getting-started/configuration).

### Uninstall

```bash
rtk init -g --uninstall     # Remove hook, RTK.md, settings.json entry
cargo uninstall rtk          # Remove binary
brew uninstall rtk           # If installed via Homebrew
```

## Documentation

- **[rtk-ai.app/guide](https://www.rtk-ai.app/guide)** — full user guide (installation, supported agents, what gets optimized, analytics, configuration, troubleshooting)
- **[INSTALL.md](INSTALL.md)** — detailed installation reference
- **[ARCHITECTURE.md](docs/contributing/ARCHITECTURE.md)** — system design and technical decisions
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — contribution guide
- **[SECURITY.md](SECURITY.md)** — security policy

## Privacy & Telemetry

RTK can collect **anonymous, aggregate usage metrics** once per day. Telemetry is **disabled by default** and requires **explicit opt-in consent** (GDPR Art. 6, 7) during `rtk init` or via `rtk telemetry enable`. This data helps us build a better product: identifying which commands need filters, which filters need improvement, and how much value RTK delivers. For the full list of fields, data handling, and contributor guidelines, see **[docs/TELEMETRY.md](docs/TELEMETRY.md)**.

**What is collected and why:**

| Category | Data | Why |
|----------|------|-----|
| Identity | Salted device hash (SHA-256, not reversible) | Count unique installations without tracking individuals |
| Environment | RTK version, OS, architecture, install method | Know which platforms to support and test |
| Usage volume | Command count (24h), total commands, tokens saved (24h/30d/total) | Measure adoption and value delivered |
| Quality | Top 5 passthrough commands (0% savings), parse failure count, commands with <30% savings | Identify missing filters and weak ones to improve |
| Ecosystem | Command category distribution (e.g. git 45%, cargo 20%, js 15%) | Prioritize filter development for popular ecosystems |
| Retention | Days since first use, active days in last 30 | Understand engagement and detect churn |
| Adoption | AI agent hook type (claude/gemini/codex), custom TOML filter count | Track integration coverage and DSL adoption |
| Configuration | Whether config.toml exists, number of excluded commands, project count | Understand user maturity and customization patterns |
| Features | Usage counts for meta-commands (gain, discover, proxy, verify) | Know which RTK features are valued vs unused |
| Economics | Estimated USD savings (based on API token pricing) | Quantify the value RTK provides to users |

All data is **aggregate counts or anonymized command names** (first 3 words, no arguments). Top commands report only tool names (e.g. "git", "cargo"), never full command lines.

**What is NOT collected:** source code, file paths, command arguments, secrets, environment variables, personal data, or repository contents.

**Manage telemetry:**
```bash
rtk telemetry status     # Check current consent state
rtk telemetry enable     # Give consent (interactive prompt)
rtk telemetry disable    # Withdraw consent — stops all collection immediately
rtk telemetry forget     # Withdraw consent + delete all local data + request server-side erasure
```

**Override via environment:**
```bash
export RTK_TELEMETRY_DISABLED=1   # Blocks telemetry regardless of consent
```

## Star History

<a href="https://www.star-history.com/?repos=rtk-ai%2Frtk&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&legend=top-left" />
 </picture>
</a>

## StarMapper

<a href="https://starmapper.bruniaux.com/rtk-ai/rtk">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://starmapper.bruniaux.com/api/map-image/rtk-ai/rtk?theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://starmapper.bruniaux.com/api/map-image/rtk-ai/rtk?theme=light" />
    <img alt="StarMapper" src="https://starmapper.bruniaux.com/api/map-image/rtk-ai/rtk" />
  </picture>
</a>

## Core team

- **Patrick Szymkowiak** — Founder
  [GitHub](https://github.com/pszymkowiak) · [LinkedIn](https://www.linkedin.com/in/patrick-szymkowiak/)
- **Florian Bruniaux** — Core contributor
  [GitHub](https://github.com/FlorianBruniaux) · [LinkedIn](https://www.linkedin.com/in/florian-bruniaux-43408b83/)
- **Adrien Eppling** — Core contributor
  [GitHub](https://github.com/aeppling) · [LinkedIn](https://www.linkedin.com/in/adrien-eppling/)
- **Nicolas Le Cam** — Core contributor
  [Github](https://github.com/kush) · [LinkedIn](https://www.linkedin.com/in/nicolas-le-cam-386387160/)
- **Takayuki Maeda** — Core contributor
  [GitHub](https://github.com/TaKO8Ki) · [LinkedIn](https://www.linkedin.com/in/tako8ki/)

## Contributing

Contributions welcome! Please open an issue or PR on [GitHub](https://github.com/rtk-ai/rtk).

Join the community on [Discord](https://discord.gg/RySmvNF5kF).

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md).

## Docs

### docs/contributing/ARCHITECTURE.md (excerpt: System Overview, Command Lifecycle, Module Organization, Filtering Strategies)

# rtk Architecture Documentation

> **Deep reference** for RTK's system design, filtering taxonomy, performance characteristics, and architecture decisions. For a guided tour of the end-to-end flow, start with [TECHNICAL.md](TECHNICAL.md).

**rtk (Rust Token Killer)** is a high-performance CLI proxy that minimizes LLM token consumption through intelligent output filtering and compression.

## System Overview

### Design Principles

1. **Single Responsibility**: Each module handles one command type
2. **Minimal Overhead**: ~5-15ms proxy overhead per command
3. **Exit Code Preservation**: CI/CD reliability through proper exit code propagation
4. **Fail-Safe**: If filtering fails, fall back to original output
5. **Transparent**: Users can always see raw output with `-v` flags

### Hook Architecture (v0.9.5+)

Two hook strategies:

```
Auto-Rewrite (default)              Suggest (non-intrusive)
─────────────────────               ────────────────────────
Hook intercepts command             Hook emits systemMessage hint
Rewrites before execution           Claude decides autonomously
100% adoption                       ~70-85% adoption
Zero context overhead               Minimal context overhead
Best for: production                Best for: learning / auditing
```

## Command Lifecycle

### Six-Phase Execution Flow

```
Phase 1: PARSE — Clap Parser extracts command, args, flags
Phase 2: ROUTE — main.rs matches Commands::Git { args, .. } -> git::run(args, verbose)
Phase 3: EXECUTE — std::process::Command::new("git").args([...]).output()
Phase 4: FILTER — git::format_git_output(stdout, "log", verbose); e.g. Stats Extraction
  strategy compresses "5 commits, +142/-89" (96% reduction)
Phase 5: PRINT — verbose levels control debug/raw echo; filtered output goes to stdout
Phase 6: TRACK — tracking::track(original_cmd, rtk_cmd, input, output) writes a
  SQLite row (input_tokens, output_tokens, savings_pct, timestamp) to
  ~/.local/share/rtk/history.db
```

### Verbosity Levels

```
-v   (Level 1): Show debug messages
-vv  (Level 2): Show command being executed
-vvv (Level 3): Show raw output before filtering
```

## Module Organization

**Token savings by ecosystem:**

```
GIT (cmds/git/)          85-99%    status, diff, log, gh, gt
JS/TS (cmds/js/)         70-99%    lint, tsc, next, prettier, playwright, prisma, vitest, pnpm
PYTHON (cmds/python/)    70-90%    ruff, pytest, mypy, pip
GO (cmds/go/)            75-90%    go test/build/vet, golangci-lint
RUBY (cmds/ruby/)        60-90%    rake, rspec, rubocop
DOTNET (cmds/dotnet/)    70-85%    dotnet build/test, binlog
CLOUD (cmds/cloud/)      60-80%    aws, docker/kubectl, curl, wget, psql
SYSTEM (cmds/system/)    50-90%    ls, tree, read, grep, find, json, log, env, deps
RUST (cmds/rust/)        60-99%    cargo test/build/clippy, err
```

**Total: 64 modules** (42 command modules + 22 infrastructure modules)

- **Command Modules**: `src/cmds/` — organized by ecosystem (git, rust, js, python, go, dotnet, cloud, system, ruby)
- **Core Infrastructure**: `src/core/` — utils, filter, tracking, tee, config, toml_filter, display_helpers, telemetry
- **Hook System**: `src/hooks/` — init, rewrite, permissions, hook_cmd, hook_check, hook_audit, verify, trust, integrity
- **Analytics**: `src/analytics/` — gain, cc_economics, ccusage, session_cmd

## Filtering Strategies

Twelve named strategies, each mapped to the modules that use it:

1. **Stats Extraction** — count/aggregate, drop details (90-99%) — `git status/log/diff`, `pnpm list`
2. **Error Only** — stderr only, drop stdout (60-80%) — `err` mode, test failures
3. **Grouping by Pattern** — group by rule/file (80-90%) — `lint`, `tsc`, `grep`
4. **Deduplication** — unique + count (70-85%) — `log` command
5. **Structure Only** — keys + types, strip values (80-95%) — `json` command
6. **Code Filtering** — language-aware level: none (0%) / minimal strips comments (20-40%) / aggressive strips bodies (60-90%) — `read`, `smart` (via `src/core/filter.rs`; languages: Rust, Python, JavaScript, TypeScript, Go, C, C++, Java; extension-based detection)
7. **Failure Focus** — failures only, hide passing (94-99%) — `vitest`, `playwright`, test runner
8. **Tree Compression** — flat list to tree hierarchy (50-70%) — `ls`
9. **Progress Filtering** — strip ANSI progress bars, keep final result (85-95%) — `wget`, `pnpm install`
10. **JSON/Text Dual Mode** — JSON when available, text fallback (80%+) — `ruff`, `pip`
11. **State Machine Parsing** — track test state, extract failures (90%+) — `pytest`
12. **NDJSON Streaming** — parse line-by-line JSON events, aggregate (90%+) — `go test`

## Top-level structure
- `.claude/` — Claude Code project config for this repo
- `.github/` — CI workflows (Security Check workflow referenced in README badges)
- `.rtk/` — project-local rtk config/state
- `CLAUDE.md` — agent instructions for working in this repo (repo dogfoods its own AI-tool integration)
- `CONTRIBUTING.md`, `SECURITY.md`, `DISCLAIMER.md`, `CHANGELOG.md`, `INSTALL.md` — project docs
- `Cargo.toml` / `Cargo.lock` — Rust package manifest (single binary, per README "zero dependencies" framing)
- `Formula/` — Homebrew formula
- `README.md` + `README_{es,fr,ja,ko,pt,zh}.md` — localized READMEs
- `build.rs` — Rust build script
- `docs/` — `TELEMETRY.md` plus `contributing/` (ARCHITECTURE.md, CODING_PRACTICES.md, TECHNICAL.md), `guide/`, `maintainers/`, `usage/`
- `hooks/` — per-agent hook integrations (includes `hooks/hermes/` per README)
- `install.sh` — POSIX install script (curl | sh)
- `openclaw/` — OpenClaw plugin source
- `scripts/` — repo maintenance scripts
- `src/` — Rust source: `main.rs` plus `analytics/`, `cmds/` (per-ecosystem command modules), `core/` (shared infra), `discover/`, `filters/`, `hooks/`, `learn/`, `parser/`
- `tests/` — test suite
