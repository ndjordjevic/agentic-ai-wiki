# googleworkspace/cli

## Metadata
- Stars: 29674
- Primary language: Rust
- Default branch: main
- Latest release: v0.22.5 (2026-03-31)
- License: Apache License 2.0
- Homepage: https://developers.google.com/workspace
- Fetched: 2026-07-14
- Final URL: https://github.com/googleworkspace/cli

## Description
Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

## README
<h1 align="center">gws</h1>

**One CLI for all of Google Workspace — built for humans and AI agents.**
Drive, Gmail, Calendar, and every Workspace API. Zero boilerplate. Structured JSON output. 40+ agent skills included.

> [!NOTE]
> This is **not** an officially supported Google product.

⬇️ **[Download the latest release for your OS](https://github.com/googleworkspace/cli/releases)**

`gws` doesn't ship a static list of commands. It reads Google's own [Discovery Service](https://developers.google.com/discovery) at runtime and builds its entire command surface dynamically. When Google Workspace adds an API endpoint or method, `gws` picks it up automatically.

> [!IMPORTANT]
> This project is under active development. Expect breaking changes as we march toward v1.0.

## Prerequisites

- **Node.js 18+** — for `npm install` (or download a pre-built binary from GitHub Releases)
- **A Google Cloud project** — required for OAuth credentials. Create one via the Google Cloud Console, the `gcloud` CLI, or the `gws auth setup` command.
- **A Google account** with access to Google Workspace

## Installation

The recommended way to install `gws` is to download the pre-built binary for your OS and architecture from GitHub Releases. Extract the archive and place the `gws` binary in your `$PATH`.

```bash
npm install -g @googleworkspace/cli
```

Or build from source:

```bash
cargo install --git https://github.com/googleworkspace/cli --locked
```

A Nix flake is also available at `github:googleworkspace/cli`:

```bash
nix run github:googleworkspace/cli
```

On macOS and Linux, you can also install via Homebrew:

```bash
brew install googleworkspace-cli
```

## Quick Start

```bash
gws auth setup     # walks you through Google Cloud project config
gws auth login     # subsequent OAuth login
gws drive files list --params '{"pageSize": 5}'
```

## Why gws?

**For humans** — stop writing `curl` calls against REST docs. `gws` gives you `--help` on every resource, `--dry-run` to preview requests, and auto‑pagination.

**For AI agents** — every response is structured JSON. Pair it with the included agent skills and your LLM can manage Workspace without custom tooling.

```bash
# List the 10 most recent files
gws drive files list --params '{"pageSize": 10}'

# Create a spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'

# Send a Chat message
gws chat spaces messages create \
  --params '{"parent": "spaces/xyz"}' \
  --json '{"text": "Deploy complete."}' \
  --dry-run

# Introspect any method's request/response schema
gws schema drive.files.list

# Stream paginated results as NDJSON
gws drive files list --params '{"pageSize": 100}' --page-all | jq -r '.files[].name'
```

## Authentication

The CLI supports multiple auth workflows so it works on your laptop, in CI, and on a server.

### Which setup should I use?

| I have… | Use |
|---|---|
| `gcloud` installed and authenticated | `gws auth setup` (fastest) |
| A GCP project but no `gcloud` | Manual OAuth setup (Google Cloud Console) |
| An existing OAuth access token | `GOOGLE_WORKSPACE_CLI_TOKEN` |
| Existing Credentials | `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` |

### Interactive (local desktop)

Credentials are encrypted at rest (AES-256-GCM) with the key stored in your OS keyring (or `~/.config/gws/.encryption_key` when `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND=file`).

```bash
gws auth setup       # one-time: creates a Cloud project, enables APIs, logs you in
gws auth login       # subsequent scope selection and login
```

> [!WARNING]
> **Scope limits in testing mode:** If your OAuth app is unverified (testing mode), Google limits consent to ~25 scopes. The `recommended` scope preset includes 85+ scopes and **will fail** for unverified apps (especially for `@gmail.com` accounts). Choose individual services instead: `gws auth login -s drive,gmail,sheets`

### Manual OAuth setup (Google Cloud Console)

1. Open the OAuth consent screen and Credentials pages for the target project.
2. Configure OAuth branding: App type **External** (testing mode is fine).
3. Add your account under **Test users**.
4. Create an OAuth client of type **Desktop app**.
5. Download the client JSON to `~/.config/gws/client_secret.json`.

Then run `gws auth login`.

### Browser-assisted auth (human or agent)

- **Human flow**: run `gws auth login`, open the printed URL, approve scopes.
- **Agent-assisted flow**: the agent opens the URL, selects account, handles consent prompts, and returns control once the localhost callback succeeds.

### Headless / CI (export flow)

```bash
gws auth export --unmasked > credentials.json
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/credentials.json
gws drive files list   # just works
```

### Service Account (server-to-server)

```bash
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/service-account.json
gws drive files list
```

### Pre-obtained Access Token

```bash
export GOOGLE_WORKSPACE_CLI_TOKEN=$(gcloud auth print-access-token)
```

### Auth precedence

1. `GOOGLE_WORKSPACE_CLI_TOKEN`
2. `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`
3. Encrypted credentials via `gws auth login`
4. Plaintext `~/.config/gws/credentials.json`

## AI Agent Skills

The repo ships 100+ Agent Skills (`SKILL.md` files) — one for every supported API, plus higher-level helpers for common workflows and 50 curated recipes for Gmail, Drive, Docs, Calendar, and Sheets.

```bash
# Install all skills at once
npx skills add https://github.com/googleworkspace/cli

# Or pick only what you need
npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-drive
npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-gmail
```

OpenClaw setup: symlink `skills/gws-*` into `~/.openclaw/skills/`, or copy specific skills. The `gws-shared` skill includes an `install` block so OpenClaw auto-installs the CLI via `npm` if `gws` isn't on PATH.

## Gemini CLI Extension

```bash
gws auth setup
gemini extensions install https://github.com/googleworkspace/cli
```

Installing this extension gives your Gemini CLI agent direct access to all `gws` commands and Google Workspace agent skills, inheriting your terminal's credentials.

## Advanced Usage

### Multipart Uploads

```bash
gws drive files create --json '{"name": "report.pdf"}' --upload ./report.pdf
```

### Pagination

| Flag | Description | Default |
|---|---|---|
| `--page-all` | Auto-paginate, one JSON line per page (NDJSON) | off |
| `--page-limit <N>` | Max pages to fetch | 10 |
| `--page-delay <MS>` | Delay between pages | 100 ms |

### Helper Commands

Some services ship hand-crafted helper commands alongside the auto-generated Discovery surface, prefixed with `+` so they never collide with Discovery-generated method names. Time-aware helpers (`+agenda`, `+standup-report`, `+weekly-digest`, `+meeting-prep`) automatically use your Google account timezone (fetched from Calendar Settings API, cached 24h).

**Full helper reference:**

| Service | Command | Description |
|---------|---------|-------------|
| `gmail` | `+send` | Send an email |
| `gmail` | `+reply` | Reply to a message (handles threading automatically) |
| `gmail` | `+reply-all` | Reply-all to a message |
| `gmail` | `+forward` | Forward a message to new recipients |
| `gmail` | `+triage` | Show unread inbox summary (sender, subject, date) |
| `gmail` | `+watch` | Watch for new emails and stream them as NDJSON |
| `sheets` | `+append` | Append a row to a spreadsheet |
| `sheets` | `+read` | Read values from a spreadsheet |
| `docs` | `+write` | Append text to a document |
| `chat` | `+send` | Send a message to a space |
| `drive` | `+upload` | Upload a file with automatic metadata |
| `calendar` | `+insert` | Create a new event |
| `calendar` | `+agenda` | Show upcoming events |
| `script` | `+push` | Replace all files in an Apps Script project with local files |
| `workflow` | `+standup-report` | Today's meetings + open tasks as a standup summary |
| `workflow` | `+meeting-prep` | Prepare for your next meeting: agenda, attendees, and linked docs |
| `workflow` | `+email-to-task` | Convert a Gmail message into a Google Tasks entry |
| `workflow` | `+weekly-digest` | Weekly summary: this week's meetings + unread email count |
| `workflow` | `+file-announce` | Announce a Drive file in a Chat space |
| `events` | `+subscribe` | Subscribe to Workspace events and stream them as NDJSON |
| `events` | `+renew` | Renew/reactivate Workspace Events subscriptions |
| `modelarmor` | `+sanitize-prompt` | Sanitize a user prompt through a Model Armor template |
| `modelarmor` | `+sanitize-response` | Sanitize a model response through a Model Armor template |
| `modelarmor` | `+create-template` | Create a new Model Armor template |

### Model Armor (Response Sanitization)

Integrates Google Cloud Model Armor to scan API responses for prompt injection before they reach an agent:

```bash
gws gmail users messages get --params '...' \
  --sanitize "projects/P/locations/L/templates/T"
```

`GOOGLE_WORKSPACE_CLI_SANITIZE_MODE` is `warn` (default) or `block`.

## Environment Variables

All variables are optional (see `.env.example`): `GOOGLE_WORKSPACE_CLI_TOKEN`, `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`, `GOOGLE_WORKSPACE_CLI_CLIENT_ID`/`CLIENT_SECRET`, `GOOGLE_WORKSPACE_CLI_CONFIG_DIR`, `GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE`/`SANITIZE_MODE`, `GOOGLE_WORKSPACE_CLI_LOG`/`LOG_FILE`, `GOOGLE_WORKSPACE_PROJECT_ID`.

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | API error |
| `2` | Auth error |
| `3` | Validation error |
| `4` | Discovery error |
| `5` | Internal error |

## Architecture

`gws` uses a **two-phase parsing** strategy:

1. Read `argv[1]` to identify the service (e.g. `drive`)
2. Fetch the service's Discovery Document (cached 24h)
3. Build a `clap::Command` tree from the document's resources and methods
4. Re-parse the remaining arguments
5. Authenticate, build the HTTP request, execute

All output — success, errors, download metadata — is structured JSON.

## Development

```bash
cargo build                       # dev build
cargo clippy -- -D warnings       # lint
cargo test                        # unit tests
./scripts/coverage.sh             # HTML coverage report → target/llvm-cov/html/
```

## License

Apache-2.0

## Docs

### docs/skills.md — Skills Index (auto-generated)

**Services** — core Google Workspace API skills:

| Skill | Description |
|-------|-------------|
| gws-shared | Shared patterns for authentication, global flags, and output formatting |
| gws-drive | Google Drive: Manage files, folders, and shared drives |
| gws-sheets | Google Sheets: Read and write spreadsheets |
| gws-gmail | Gmail: Send, read, and manage email |
| gws-calendar | Google Calendar: Manage calendars and events |
| gws-admin-reports | Google Workspace Admin SDK: Audit logs and usage reports |
| gws-docs | Read and write Google Docs |
| gws-slides | Google Slides: Read and write presentations |
| gws-tasks | Google Tasks: Manage task lists and tasks |
| gws-people | Google People: Manage contacts and profiles |
| gws-chat | Google Chat: Manage Chat spaces and messages |
| gws-classroom | Google Classroom: Manage classes, rosters, and coursework |
| gws-forms | Read and write Google Forms |
| gws-keep | Manage Google Keep notes |
| gws-meet | Manage Google Meet conferences |
| gws-events | Subscribe to Google Workspace events |
| gws-modelarmor | Google Model Armor: Filter user-generated content for safety |
| gws-workflow | Google Workflow: Cross-service productivity workflows |
| gws-script | Manage Google Apps Script projects |

**Helpers** — shortcut commands for common operations, one per `+`-prefixed helper listed in the README table above (e.g. `gws-drive-upload`, `gws-gmail-send`, `gws-calendar-agenda`, `gws-workflow-standup-report`, etc.), each with its own `SKILL.md`.

## Top-level structure
- `crates/` — Rust workspace source (CLI implementation)
- `skills/` — 100+ `SKILL.md` agent skill definitions (one per API/helper)
- `docs/` — skills index, contributing guide, demo assets
- `npm/` — npm packaging wrapper for binary distribution
- `art/`, `demo.gif` — project media
- `scripts/` — dev scripts (coverage, etc.)
- `.claude/`, `.gemini/`, `.agent/` — agent-harness config directories
- `CLAUDE.md`, `AGENTS.md`, `CONTEXT.md` — agent instruction files
- `gemini-extension.json` — Gemini CLI extension manifest
- `Cargo.toml`/`Cargo.lock` — Rust package manifest
- `flake.nix`/`flake.lock` — Nix packaging
- `deny.toml` — cargo-deny license/security policy
- `lefthook.yml` — git hooks config
