# resend/resend-cli

## Metadata
- Stars: 372
- Primary language: TypeScript
- Default branch: main
- Latest release: v2.3.0 (2026-05-28)
- License: MIT
- Homepage: (none)
- Fetched: 2026-06-09
- Final URL: https://github.com/resend/resend-cli

## Description
The official CLI for Resend. Built for humans, AI agents, and CI/CD pipelines.

## README
# Resend CLI

The official CLI for [Resend](https://resend.com).

Built for humans, AI agents, and CI/CD pipelines.

## Install

### cURL

```sh
curl -fsSL https://resend.com/install.sh | bash
```

### Node.js

```sh
npm install -g resend-cli
```

### Homebrew (macOS / Linux)

```sh
brew install resend/cli/resend
```

### PowerShell (Windows)

```sh
irm https://resend.com/install.ps1 | iex
```

Or download the `.exe` directly from the GitHub releases page.

## Quickstart

```bash
# Authenticate
resend login

# Send an email
resend emails send \
  --from "you@example.com" \
  --to delivered@resend.dev \
  --subject "Hello from Resend CLI" \
  --text "Sent from my terminal."

# Check your environment
resend doctor
```

## Agent skills

This CLI ships with an agent skill (`skills/resend-cli/SKILL.md`) that teaches AI coding agents (Cursor, Claude Code, Windsurf, etc.) how to use the Resend CLI effectively, including non-interactive flags, output formats, and common pitfalls.

To install skills for Resend's full platform (API, CLI, React Email, email best practices):

```sh
npx skills add resend/resend-skills
```

## Authentication

The CLI resolves your API key using the following priority chain:

| Priority    | Source                   | How to set                                |
| ----------- | ------------------------ | ----------------------------------------- |
| 1 (highest) | `--api-key` flag         | `resend --api-key re_xxx emails send ...` |
| 2           | `RESEND_API_KEY` env var | `export RESEND_API_KEY=re_xxx`            |
| 3 (lowest)  | Config file              | `resend login`                            |

If no key is found from any source, the CLI errors with code `auth_error`.

## Commands

### `resend login`

Authenticate by storing your API key locally. Interactive: prompts for key if not found. Non-interactive (CI): requires `--key re_xxx` flag.

Switch between profiles: `resend auth switch` or use `--profile <name>` global flag.

### `resend emails send`

Send an email via the Resend API.

```bash
resend emails send \
  --from "Name <sender@example.com>" \
  --to delivered@resend.dev \
  --subject "Subject line" \
  --text "Plain text body"
```

Options: `--from`, `--to` (multiple, space-separated), `--subject`, `--text`, `--html`, `--html-file`, `--cc`, `--bcc`, `--reply-to`.

Supports `--dry-run` to validate inputs without sending: prints `{ "dryRun": true, "request": { ... } }`.

### `resend doctor`

Run environment diagnostics: CLI version check, API key validation, domain verification status, AI agent detection (OpenClaw, Cursor, Claude Desktop, VS Code). Exit `0` when all checks pass or warn; `1` if any fail.

### Webhooks

Full CRUD + live listening:

- `resend webhooks list` — list endpoints
- `resend webhooks create --endpoint <url> --events <events...>` — register HTTPS endpoint; signing secret shown once
- `resend webhooks get <id>` — fetch one webhook
- `resend webhooks update <id>` — update endpoint, events, or status (enabled/disabled)
- `resend webhooks delete <id> --yes` — delete webhook
- `resend webhooks listen --url <tunnel-url>` — local dev: starts HTTP server, registers temp webhook, prints events, cleans up on exit

**Webhook event types:**

| Category | Events |
|---|---|
| Email | `email.sent`, `email.delivered`, `email.delivery_delayed`, `email.bounced`, `email.complained`, `email.opened`, `email.clicked`, `email.failed`, `email.scheduled`, `email.suppressed`, `email.received` |
| Contact | `contact.created`, `contact.updated`, `contact.deleted` |
| Domain | `domain.created`, `domain.updated`, `domain.deleted` |

## Global options

| Flag | Description |
|---|---|
| `--api-key <key>` | Override API key for this invocation |
| `-p, --profile <name>` | Profile to use |
| `--json` | Force JSON output |
| `-q, --quiet` | Suppress spinners and status (implies `--json`) |
| `--version` | Print version |
| `--help` | Show help |

## Output behavior

- **Interactive (TTY):** Formatted text on stdout; spinners, prompts, human-readable errors on stderr
- **Machine (piped/CI/`--json`):** Success JSON on stdout; error JSON on stderr

Errors always exit with code `1`. Error format: `{ "error": { "message": "...", "code": "..." } }`.

## Agent & CI/CD usage

**CI/CD:** Set `RESEND_API_KEY` env var — no `resend login` needed.

**AI agents:** Non-TTY detection automatically activates JSON output. Contract: all required flags must be provided; success JSON on stdout; error JSON on stderr; exit `0` success, `1` error. `resend commands` prints the full command tree as JSON for agent discovery.

## Dry-run

`--dry-run` implemented on `emails send` and `broadcasts create`. Validates inputs and prints the would-be request without sending.

## Configuration

| Item | Path |
|---|---|
| Config directory | `~/.config/resend/` (respects `$XDG_CONFIG_HOME`, `%APPDATA%`) |
| Credentials | `~/.config/resend/credentials.json` (`0600` permissions) |
| Install directory | `~/.resend/bin/` (respects `$RESEND_INSTALL`) |

## Top-level structure
- `.github/` — CI/CD workflows
- `src/` — CLI source code (TypeScript)
- `skills/` — Agent skill files (SKILL.md for resend-cli)
- `skill-evals/` — Skill evaluation test suite
- `tests/` — Unit and integration tests
- `scripts/` — Build/release scripts
- `install.sh` / `install.ps1` — curl/PowerShell installers
- `package.json`, `pnpm-workspace.yaml` — pnpm monorepo workspace
- `tsconfig.json`, `biome.json` — TypeScript + linter config
- `vitest.config.ts`, `vitest.config.e2e.ts` — Vitest test configs
- `LICENSE` — MIT
