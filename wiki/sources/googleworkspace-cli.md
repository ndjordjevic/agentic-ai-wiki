---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/googleworkspace/cli
tags:
  - google-workspace
  - discovery-service
  - dynamic-cli
  - agent-skills
  - oauth2
  - structured-json-output
  - gemini-cli-extension
  - model-armor
related:
  - voltagent-awesome-agent-skills
  - davila7-claude-code-templates
  - notebooklm.google
product: gws
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

`gws` is a Rust CLI that exposes the entire Google Workspace API surface (Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more) by reading Google's Discovery Service at runtime rather than shipping a static command list — new API methods appear automatically. It ships 100+ bundled Agent Skills (`SKILL.md` files, one per API plus curated workflow recipes), making it a dual-purpose tool: a human-friendly Workspace CLI and a ready-made action layer for AI agents. See [[davila7-claude-code-templates]] and [[voltagent-awesome-agent-skills]] for other large Agent Skills catalogs.

_All claims below are sourced from ../../raw/github/googleworkspace-cli.md unless otherwise noted._

## What it does

`gws` uses a two-phase parsing strategy: it reads the requested service name (e.g. `drive`), fetches that service's Discovery Document (cached 24h), builds a `clap::Command` tree from its resources and methods, then re-parses the remaining arguments and executes the HTTP request. Every response — success, error, download metadata — is structured JSON, which is what makes it agent-friendly: an LLM can call `gws drive files list --params '{"pageSize": 10}'` and get machine-parseable output without custom API glue.

## Installation

Recommended install is a pre-built binary from GitHub Releases, or `npm install -g @googleworkspace/cli`, `cargo install --git https://github.com/googleworkspace/cli --locked`, `nix run github:googleworkspace/cli`, or `brew install googleworkspace-cli`.

## Key features

- **Dynamic command surface** — built from Google's Discovery Service, so it tracks new Workspace API endpoints automatically instead of requiring a version bump.
- **100+ Agent Skills** — one `SKILL.md` per supported API plus 50 curated recipes (Gmail, Drive, Docs, Calendar, Sheets), installable individually or in bulk via `npx skills add`.
- **`+`-prefixed helper commands** — hand-written shortcuts (`+send`, `+reply`, `+triage`, `+standup-report`, `+meeting-prep`, `+weekly-digest`, `+email-to-task`, etc.) layered on top of the auto-generated Discovery surface; never collide with Discovery method names.
- **Timezone-aware helpers** — `+agenda`, `+standup-report`, `+weekly-digest`, `+meeting-prep` fetch the user's Google account timezone from the Calendar Settings API (cached 24h) rather than assuming the local machine's timezone.
- **Model Armor integration** — can route API responses through Google Cloud Model Armor to scan for prompt injection before an agent sees them (`--sanitize`, `warn`/`block` modes).
- **Structured exit codes** — 0 success, 1 API error, 2 auth error, 3 validation error, 4 discovery error, 5 internal error — lets scripts and agents branch on failure type without parsing stderr text.

## Architecture

Two-phase argument parsing (service identification → Discovery Document fetch/cache → dynamic subcommand tree → execution) is the core design. Credentials are encrypted at rest (AES-256-GCM) with the key in the OS keyring by default, or a file-based key when `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND=file` is set.

## Example usage

```bash
gws auth setup
gws drive files list --params '{"pageSize": 10}'
gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'
gws schema drive.files.list
gws drive files list --params '{"pageSize": 100}' --page-all | jq -r '.files[].name'
```

## Maintenance status

29,674 stars, 1,724 forks, Apache-2.0 license, latest release v0.22.5 (2026-03-31), pushed 2026-07-01. Explicitly labeled "under active development" with expected breaking changes before v1.0. Not an officially supported Google product — maintained under the `googleworkspace` GitHub org but explicitly disclaimed as unofficial. Installs as a Gemini CLI extension (`gemini extensions install https://github.com/googleworkspace/cli`), inheriting the terminal's existing `gws` credentials; skills install via `npx skills add` (the [Agent Skills](https://agentskills.io) ecosystem) or manual symlink for OpenClaw.
