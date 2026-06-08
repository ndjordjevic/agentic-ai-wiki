# earendil-works/pi

## Metadata
- Stars: 60792
- Forks: 7304
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.78.1 (2026-06-04)
- License: MIT
- Homepage: (none; see https://pi.dev/)
- Fetched: 2026-06-08
- Final URL: https://github.com/earendil-works/pi

## Description
AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods

## Repository structure (top-level)
```
packages/
  agent/          @earendil-works/pi-agent-core — agent runtime, tool calling, state management
  ai/             @earendil-works/pi-ai — unified multi-provider LLM API
  coding-agent/   @earendil-works/pi-coding-agent — interactive coding agent CLI
  tui/            @earendil-works/pi-tui — terminal UI library with differential rendering
AGENTS.md
CONTRIBUTING.md
LICENSE
SECURITY.md
scripts/
packages/coding-agent/docs/containerization.md
```

## README summary

Monorepo for the Pi agent harness project.

### Packages

| Package | Description |
|---------|-------------|
| @earendil-works/pi-ai | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| @earendil-works/pi-agent-core | Agent runtime with tool calling and state management |
| @earendil-works/pi-coding-agent | Interactive coding agent CLI |
| @earendil-works/pi-tui | Terminal UI library with differential rendering |

Related: [earendil-works/pi-chat](https://github.com/earendil-works/pi-chat) for Slack/chat automation.

### Permissions & Containerization

Pi does not include a built-in permission system. Three containerization patterns:
- **OpenShell**: run the whole `pi` process in a policy-controlled sandbox
- **Gondolin extension**: keep `pi` and provider auth on host; route built-in tools and `!` commands into a local Linux micro-VM
- **Plain Docker**: run `pi` in a local container for simple isolation

### Supply-chain hardening

- Direct external deps pinned to exact versions; `.npmrc` sets `save-exact=true` and `min-release-age=2`
- `package-lock.json` is ground truth; pre-commit blocks accidental lockfile commits
- Published CLI includes `npm-shrinkwrap.json` to pin transitive deps for npm users
- CI uses `npm ci --ignore-scripts`; scheduled `npm audit` and `npm audit signatures` workflow
- Shrinkwrap generation has explicit allowlist for dependency lifecycle scripts

### Development

```bash
npm install --ignore-scripts
npm run build
npm run check     # lint, format, type check
./test.sh         # run tests
./pi-test.sh      # run pi from sources
```

### Latest release: v0.78.1 (2026-06-04)

Key changes:
- Added Ant Ling and NVIDIA NIM provider setup; MiniMax-M3 support
- Extensions can use `ctx.mode` and `ctx.getSystemPromptOptions()` for cross-mode adaptation
- Fixed stored XSS in HTML session exports (sanitized Markdown link/image URLs)
- Fixed SDK embedding in bundled Node apps failing with ENOENT when package.json absent
- Fixed HTTP timeout not being respected for non-Codex providers
- Node.js minimum: v22.19.0
