# ComposioHQ/composio

## Metadata
- Stars: 30897
- Forks: 4914
- Primary language: TypeScript
- Default branch: next
- Latest release: @composio/cli@0.6.0 (2026-11-01); also CLI beta @composio/cli@0.6.1-beta.533 (2026-11-03)
- License: MIT License
- Homepage: https://docs.composio.dev
- Fetched: 2026-11-03
- Final URL: https://github.com/ComposioHQ/composio

## Description
Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

## README
<p align="center">
  <a href="https://composio.dev">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://brand.composio.dev/logos/Logomark-White.svg">
      <img alt="Composio logo" src="https://brand.composio.dev/logos/Logomark-Black.svg" width="96">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://composio.dev"><b>composio.dev</b></a> •
  <a href="https://docs.composio.dev">Documentation</a> •
  <a href="https://docs.composio.dev/docs/quickstart">Quickstart</a> •
  <a href="https://docs.composio.dev/reference/changelog">Changelog</a>
</p>

<p align="center">
  <a href="https://github.com/ComposioHQ/composio/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ComposioHQ/composio?style=social" /></a>
  <a href="https://www.npmjs.com/package/@composio/core"><img alt="npm" src="https://img.shields.io/npm/v/@composio/core?label=%40composio%2Fcore" /></a>
  <a href="https://pypi.org/project/composio/"><img alt="PyPI" src="https://img.shields.io/pypi/v/composio?label=composio" /></a>
  <a href="https://discord.gg/composio"><img alt="Discord" src="https://img.shields.io/badge/discord-community-5865F2?logo=discord&logoColor=white" /></a>
  <a href="https://hvtracker.net/agents/composio/"><img alt="HVTrust" src="https://hvtracker.net/badge/composio.svg" /></a>
</p>

# Composio

Composio gives your AI agents 1000+ pre-authenticated toolkits, per-user sessions, authentication, triggers, and a sandbox, so you can ship agents that turn intent into action.

This is the Composio SDK monorepo. It contains:

- **[`@composio/core`](ts/packages/core)**: TypeScript SDK
- **[`composio`](python)**: Python SDK
- **[`composio` CLI](ts/packages/cli)**: search, execute, and script tools from your shell
- **Provider adapters** for OpenAI Agents, Claude Agent SDK, Vercel AI SDK, LangChain, and [more](#providers)

## Quickstart

Create a session for a user, hand its tools to your agent, and let the agent take action across 1000+ apps. Grab a `COMPOSIO_API_KEY` from the [dashboard](https://dashboard.composio.dev/settings) first.

### TypeScript

```bash
npm install @composio/core @composio/openai-agents @openai/agents
```

> `@composio/core` intentionally packages its TypeScript source and SDK docs so the installed package is inspectable to coding agents. If you want a smaller install with the same API, use [`@composio/slim`](ts/packages/slim).

```typescript
import { Composio } from "@composio/core";
import { OpenAIAgentsProvider } from "@composio/openai-agents";
import { Agent, run } from "@openai/agents";

const composio = new Composio({ provider: new OpenAIAgentsProvider() });

// Each session is scoped to one of your users
const session = await composio.create("user_123");
const tools = await session.tools();

const agent = new Agent({
  name: "Personal Assistant",
  instructions: "You are a helpful assistant. Use Composio tools to take action.",
  tools,
});

const result = await run(agent, "Summarize my emails from today");
console.log(result.finalOutput);
```

### Python

```bash
pip install composio composio-openai-agents openai-agents
```

```python
from composio import Composio
from composio_openai_agents import OpenAIAgentsProvider
from agents import Agent, Runner

composio = Composio(provider=OpenAIAgentsProvider())

# Each session is scoped to one of your users
session = composio.create(user_id="user_123")
tools = session.tools()

agent = Agent(
    name="Personal Assistant",
    instructions="You are a helpful assistant. Use Composio tools to take action.",
    tools=tools,
)

result = Runner.run_sync(starting_agent=agent, input="Summarize my emails from today")
print(result.final_output)
```

By default a session gets meta tools that discover, authenticate, and execute app tools at runtime, so you don't load hundreds of tool definitions into context. Store `session.session_id` and reuse it with `composio.use()` across turns. See [what a session is](https://docs.composio.dev/docs/how-composio-works) and [configuring sessions](https://docs.composio.dev/docs/configuring-sessions) for restricting toolkits, auth configs, and connected accounts.

**Prefer MCP?** Every session also exposes a hosted MCP endpoint. Pass `mcp: true` to `composio.create()` and point Claude, Cursor, or any MCP client at `session.mcp.url`. See [sessions via MCP](https://docs.composio.dev/docs/sessions-via-mcp).

## CLI

The `composio` CLI runs Composio from your shell and gives coding agents like Claude Code a local tool surface.

```bash
curl -fsSL https://composio.dev/install | sh
```

The installer puts `composio` on your `PATH` for future terminals. Open a new terminal, then run `composio login`. See [INSTALL.md](INSTALL.md) for shell setup overrides, including `COMPOSIO_INSTALL_SHELL=none` for install-only runs.

Use `composio search` to find tools, `composio execute` to run them, `composio link` to connect accounts, and `composio run` to script workflows in TypeScript. See the [CLI docs](https://docs.composio.dev/docs/cli).

## Providers

A provider adapts Composio tools to your agent framework's native tool format:

| Provider | TypeScript | Python |
|----------|:----------:|:------:|
| OpenAI | [`@composio/openai`](ts/packages/providers/openai) | [`composio-openai`](python/providers/openai) |
| OpenAI Agents | [`@composio/openai-agents`](ts/packages/providers/openai-agents) | [`composio-openai-agents`](python/providers/openai_agents) |
| Anthropic | [`@composio/anthropic`](ts/packages/providers/anthropic) | [`composio-anthropic`](python/providers/anthropic) |
| Claude Agent SDK | [`@composio/claude-agent-sdk`](ts/packages/providers/claude-agent-sdk) | [`composio-claude-agent-sdk`](python/providers/claude_agent_sdk) |
| Vercel AI SDK | [`@composio/vercel`](ts/packages/providers/vercel) | — |
| Google GenAI | [`@composio/google`](ts/packages/providers/google) | [`composio-gemini`](python/providers/gemini), [`composio-google`](python/providers/google) |
| Google ADK | — | [`composio-google-adk`](python/providers/google_adk) |
| LangChain | [`@composio/langchain`](ts/packages/providers/langchain) | [`composio-langchain`](python/providers/langchain) |
| LangGraph | via `@composio/langchain` | [`composio-langgraph`](python/providers/langgraph) |
| LlamaIndex | [`@composio/llamaindex`](ts/packages/providers/llamaindex) | [`composio-llamaindex`](python/providers/llamaindex) |
| Mastra | [`@composio/mastra`](ts/packages/providers/mastra) | — |
| Pi | [`@composio/experimental`](ts/packages/experimental)* | — |
| Cloudflare Workers AI | [`@composio/cloudflare`](ts/packages/providers/cloudflare) | — |
| TypeSafe (Jev) | [`@composio/typesafe`](ts/packages/providers/typesafe) | [`composio-typesafe`](python/providers/typesafe) |
| CrewAI | — | [`composio-crewai`](python/providers/crewai) |
| AutoGen | — | [`composio-autogen`](python/providers/autogen) |

\* *The [Pi provider](https://docs.composio.dev/docs/providers/pi) is experimental and ships from `@composio/experimental`.*

Don't see your framework? [Build a custom provider](https://docs.composio.dev/docs/providers/custom-providers), or skip providers entirely and connect over [MCP](https://docs.composio.dev/docs/sessions-via-mcp).

## All packages

Everything published from this repo:

| Package | Description |
|---------|-------------|
| [`@composio/core`](ts/packages/core) | TypeScript SDK |
| [`@composio/slim`](ts/packages/slim) | `@composio/core` without packaged source or docs; same API, smaller install |
| [`composio` CLI](ts/packages/cli) | Standalone CLI binary: `curl -fsSL https://composio.dev/install \| sh` |
| [`@composio/experimental`](ts/packages/experimental) | Experimental integrations, including the Pi provider |
| [`@composio/json-schema-to-zod`](ts/packages/json-schema-to-zod) | JSON Schema to Zod conversion |
| `@composio/*` [provider adapters](#providers) | OpenAI, OpenAI Agents, Anthropic, Claude Agent SDK, Vercel, Google, LangChain, LlamaIndex, Mastra, Cloudflare, TypeSafe |
| [`composio`](python) | Python SDK |
| `composio-*` [provider adapters](#providers) | OpenAI, OpenAI Agents, Anthropic, Claude Agent SDK, Gemini, Google, Google ADK, LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, TypeSafe |

## Repository layout

```text
ts/                TypeScript SDK workspace
  packages/core/       @composio/core
  packages/providers/  Provider adapters
  packages/cli/        Composio CLI
python/            Python SDK and provider packages
docs/              Documentation site (docs.composio.dev)
```

The TypeScript SDK is tested against Node 22+; the Python SDK supports Python 3.11+.

## Development

```bash
mise install    # pinned toolchain (Node, Python, pnpm)
pnpm install
pnpm build
pnpm test
```

Python commands run from `python/`; see [`python/README.md`](python/README.md). We welcome contributions to both SDKs; read the [contribution guidelines](CONTRIBUTING.md) before submitting pull requests.

## Support

- [Documentation](https://docs.composio.dev)
- [Discord community](https://discord.gg/composio)
- [Open an issue](https://github.com/ComposioHQ/composio/issues)
- [support@composio.dev](mailto:support@composio.dev)

## License

MIT. See [LICENSE](LICENSE).


## Docs
### INSTALL.md
# Composio CLI installation

Install the CLI bundle in `~/.composio` and its entry point in `~/.local/bin`:

```bash
curl -fsSL https://composio.dev/install | sh
```

The installer also configures your shell. It infers your login shell from `$SHELL` (`zsh`, `bash`, or `fish`) and writes a managed `# Composio CLI` PATH block so future terminals find `composio`. For `zsh` and `fish`, it updates the matching startup file. For `bash`, it updates `~/.bashrc` plus a login-mode startup file, because a login bash (what macOS Terminal.app starts) never reads `~/.bashrc`: the first existing of `~/.bash_profile` or `~/.bash_login`, or a newly created `~/.bash_profile` when neither exists. A `~/.bash_profile` created this way sources `~/.profile` first, so nothing you already had stops loading; `~/.profile` itself is never modified. Open a new terminal, then run `composio login`.

If your shell is not recognized, or shell setup fails, the binary install still succeeds and the installer prints a runnable command instead. The installer also installs plugins for detected, supported Codex and Claude Code hosts. Set `COMPOSIO_INSTALL_PLUGINS=0` or pass `--no-plugins` to skip plugin setup. Login remains a separate step.

Official releases must pass SHA-256 verification against the release's `checksums.txt`: a missing manifest, a manifest with no entry for your platform's archive, a malformed entry, or a mismatch aborts the install with `Refusing to install`. On systems with no `sha256sum` or `shasum`, the installer warns that verification was skipped and continues.

## Choose or skip shell setup

Set `COMPOSIO_INSTALL_SHELL` to force a specific shell, or to skip shell configuration entirely:

```bash
curl -fsSL https://composio.dev/install | COMPOSIO_INSTALL_SHELL=zsh sh
curl -fsSL https://composio.dev/install | COMPOSIO_INSTALL_SHELL=bash sh
curl -fsSL https://composio.dev/install | COMPOSIO_INSTALL_SHELL=fish sh
curl -fsSL https://composio.dev/install | COMPOSIO_INSTALL_SHELL=none sh
```

Use `none` to leave shell files unchanged. Use it when a dotfile manager owns your startup files. For an install-only run in CI or Docker, also set `COMPOSIO_INSTALL_PLUGINS=0`.

Shell-specific installer variants ([`install/zsh.sh`](install/zsh.sh), [`install/bash.sh`](install/bash.sh), [`install/fish.sh`](install/fish.sh)) pin `COMPOSIO_INSTALL_SHELL` to their shell before delegating to the base installer.

Shell setup is idempotent: repeated installs keep exactly one managed PATH block per startup file and reconcile it when the bin directory changes. Setup delegates to `composio install --shell <shell>` and falls back to writing the same `# Composio CLI` PATH block inline when the installed CLI predates that flag, delegated setup fails, or delegated setup leaves a stale block.

Pin a stable or beta release with `COMPOSIO_INSTALL_VERSION`, or pass the tag as a positional argument:

```bash
curl -fsSL https://composio.dev/install | COMPOSIO_INSTALL_VERSION=0.3.1 sh
curl -fsSL https://composio.dev/install | sh -s -- @composio/cli@0.3.1-beta.329
```

The positional argument takes precedence over `COMPOSIO_INSTALL_VERSION`.

| Variable or argument | Description | Default |
|---|---|---|
| `COMPOSIO_INSTALL_DIR` | Complete CLI bundle directory. | `$HOME/.composio` |
| `COMPOSIO_BIN_DIR` | `composio` entry-point directory. Treat this as trusted input: anyone who can write to this directory can replace commands that future terminals run. | `$HOME/.local/bin` |
| `COMPOSIO_INSTALL_VERSION` | Stable or beta version, with or without the package prefix. | Latest stable release |
| `COMPOSIO_QUIET` | Set to `1` or `true` to hide progress output. Warnings and errors still print. | Unset |
| `COMPOSIO_DEBUG` | Set to `1` or `true` to print installer traces. | Unset |
| `COMPOSIO_INSTALL_HELP` | Set to `0` to hide normal post-install guidance. Shell-setup failures still warn and print a recovery command to stderr. | `1` |
| `COMPOSIO_INSTALL_PLUGINS` | Set to `0` to skip plugin setup for detected agent hosts. | `1` |
| `COMPOSIO_INSTALL_SHELL` | Shell setup mode: `auto` infers your login shell from `$SHELL`, `zsh`, `bash`, or `fish` force a specific shell, and `none` skips shell configuration. | `auto` |
| `--agent` | Log in as a Composio agent after installation. | Off |
| `--no-plugins` | Skip plugin setup, even when `COMPOSIO_INSTALL_PLUGINS=1`. | Off |

## Manual Installation

Download the archive for your platform from [GitHub Releases](https://github.com/ComposioHQ/composio/releases):

- `composio-linux-x64.zip`
- `composio-linux-aarch64.zip`
- `composio-darwin-x64.zip`
- `composio-darwin-aarch64.zip`

Extract and install the complete bundle. The CLI loads support files beside the executable, so do not copy only the nested `composio` file.

```bash
bundle=composio-linux-x64
COMPOSIO_INSTALL_DIR=${COMPOSIO_INSTALL_DIR:-"$HOME/.composio"}
COMPOSIO_BIN_DIR=${COMPOSIO_BIN_DIR:-"$HOME/.local/bin"}

unzip "$bundle.zip"
mkdir -p "$COMPOSIO_INSTALL_DIR"
cp -Rp "$bundle"/. "$COMPOSIO_INSTALL_DIR/"
chmod +x "$COMPOSIO_INSTALL_DIR/composio"
mkdir -p "$COMPOSIO_BIN_DIR"
if [ "$COMPOSIO_BIN_DIR" != "$COMPOSIO_INSTALL_DIR" ]; then
  ln -sf "$COMPOSIO_INSTALL_DIR/composio" "$COMPOSIO_BIN_DIR/composio"
fi
export PATH="$COMPOSIO_BIN_DIR:$PATH"
```

## Verification

```bash
composio --version
which composio
```

## Uninstall

Remove the entry point and release artifacts without deleting credentials, configuration, or caches. The file list below matches the current release layout; if you installed a different version, compare it against the contents of that release's archive.

```bash
install_dir=${COMPOSIO_INSTALL_DIR:-"$HOME/.composio"}
bin_dir=${COMPOSIO_BIN_DIR:-"$HOME/.local/bin"}

rm -f \
  "$bin_dir/composio" \
  "$install_dir/composio" \
  "$install_dir/release-tag.txt" \
  "$install_dir/run-helpers-runtime.mjs" \
  "$install_dir/run-subagent-shared.mjs" \
  "$install_dir/run-subagent-acp.mjs" \
  "$install_dir/run-subagent-legacy.mjs" \
  "$install_dir/run-subagent-output-mcp.mjs" \
  "$install_dir/generation-runtime.mjs" \
  "$install_dir/execute-output-encoder-runtime.mjs"
rm -rf \
  "$install_dir/services" \
  "$install_dir/acp-adapters" \
  "$install_dir/local-tools-binaries"
```

Remove the managed `# Composio CLI` PATH block from `~/.zshrc`, `~/.bashrc`, `~/.bash_profile`, `~/.bash_login`, or `~/.config/fish/config.fish`. Blocks written by older installers contain an extra `export COMPOSIO_INSTALL_DIR=...` (or `set --export COMPOSIO_INSTALL_DIR ...`) line after the marker; remove that line too. If removing the block leaves `~/.bash_profile` with nothing but blank lines, delete the file: the installer creates it on bash systems that had no login startup file, and even an empty `~/.bash_profile` keeps bash from reading `~/.profile`. If you had a `~/.profile` at install time, that created file instead holds a passthrough sourcing it, starts with `# Created by the Composio CLI installer.`, and is left in place; delete it as well to restore bash's default startup-file selection.

To purge credentials, configuration, caches, and every other CLI file, run `rm -rf "${COMPOSIO_INSTALL_DIR:-$HOME/.composio}"`. This is a complete reset and cannot be undone.

## Supported platforms

- Linux x64
- Linux ARM64
- macOS Intel
- macOS Apple Silicon
- Windows: use [WSL](https://learn.microsoft.com/windows/wsl/install) and run the installer inside your WSL distribution


## Top-level structure
- `.agents/`, `.claude/`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT7.md` — agent instruction / skill packaging
- `skills/` — includes official `composio` Agent Skill (`npx skills add ComposioHQ/composio --skill composio`)
- `python/` — Python SDK (`composio` package; not legacy `composio-core`)
- `ts/packages/core`, `ts/packages/cli` — TypeScript SDK and CLI (from README layout)
- `docs/`, `examples-manifest.json`, `harness/`, `install.sh`, `public/`
- Monorepo managed with pnpm workspace; default branch `next`
