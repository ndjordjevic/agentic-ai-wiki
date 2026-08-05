---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/block/buzz
tags: [nostr-relay, human-agent-collaboration, acp, mcp, event-sourcing, self-hosted, rust, yaml-workflows]
related: [aaif-goose-goose]
product: buzz
detail_level: standard
created: 2026-08-05
updated: 2026-08-05
---

Buzz is Block's self-hostable team workspace (22,660 stars, Apache-2.0, Rust) where humans and AI agents are members of the same rooms, built on a Nostr relay: every message, reaction, workflow step, review approval, and git event is a cryptographically signed event in one log, whether the author is a person or a process. It matters for this wiki because it inverts the usual agent-integration pattern — instead of bolting a bot into a chat product, Buzz gives agents their own keypairs, channel memberships, audit trails, and the same surface area as a human teammate (create channels, edit canvases, send patches, run workflows, join voice huddles), with an agent-first CLI and an ACP harness that plugs Goose, Codex, and Claude Code straight into the relay.

_All claims below are sourced from ../../raw/github/block-buzz.md unless otherwise noted._

## What it does

Buzz is a self-hosted communication substrate built on the Nostr protocol (NIP-01 wire format), where the relay is the single source of truth: all reads and writes flow through it, with no peer-to-peer exchange, gossip, or replication. Every action is a JSON event with six fields (`id`, `pubkey`, `kind`, `tags`, `content`, `sig`), and the `kind` integer is the only dispatch switch — adding a feature means defining a new kind number, so existing clients see nothing and break nothing. `buzz-core` currently registers 127 kinds, using standard Nostr ranges (kind 7 reactions, kind 9 group-chat messages) plus a custom 40000+ range for Buzz-specific events such as `KIND_JOB_REQUEST` (43001), forum posts (45001/45003), workflow execution events (46001–46012), and canvases (40100).

A Buzz **community** is the workspace a user reaches by URL — the relay URL selects exactly one community in the single-relay setup that ships today. A hosted operator can serve many communities behind different domains; the server resolves a `TenantContext` from the request host before any AUTH, EVENT, REQ, REST, media, git, search, workflow, or pub/sub handling, unknown hosts fail closed, and client-supplied tags cannot override the host-derived community.

The project is explicit about maturity. Working today: relay, channels, threads, DMs, canvases, media, search, audit log; the Tauri + React desktop app; `buzz-cli` plus the ACP harness; YAML workflows with message/reaction/schedule/webhook triggers; NIP-34 git events and a git hosting backend. Being wired up: Flutter mobile clients, workflow approval gates, huddle lifecycle events. Still just opinions: cross-relay web-of-trust reputation, push notifications.

## Installation

Packaged desktop builds are published on the releases page for macOS (Apple Silicon `.dmg` and Intel `.dmg`), Linux (`.AppImage` / `.deb`), and Windows (unsigned `.exe`, so SmartScreen prompts on first launch). The app connects to `ws://localhost:3000` by default; point it elsewhere with `BUZZ_RELAY_URL` or switch relays in-app. A one-click Railway template exists for teams who want a hosted relay without managing servers.

From source you need Docker plus Hermit (or Rust 1.88+, Node 24+, pnpm 10+, `just`):

```bash
git clone https://github.com/block/buzz.git && cd buzz
. ./bin/activate-hermit   # pinned toolchain
just setup && just build
just dev                  # relay + desktop app together
```

`just setup` copies `.env.example` to `.env`, downloads tools via Hermit, and starts Docker services and migrations. For a VPS/single-node relay, `deploy/compose/` carries the production Compose bundle (Postgres, Redis, MinIO, optional Caddy/TLS); the root `docker-compose.yml` is dev-only. On Windows, the agent shell tool needs a bash — Git for Windows is resolved at runtime, or point `BUZZ_SHELL` at another bash-compatible shell.

## Key features

**Agents as members, not bots.** Agents are added to channels the way people are, hold their own keys and channel memberships, and are scoped by identity rather than permission flags. Their actions land in the same signed event log and the same hash-chained audit trail as human actions.

**Agent-first CLI.** `buzz-cli` is JSON in, JSON out, designed for LLM tool calls, authenticated by `BUZZ_PRIVATE_KEY` via NIP-98 Schnorr-signed requests, with structured exit codes (0 ok, 1 user error, 2 network, 3 auth, 4 other, 5 write conflict). It covers messages (send, edit, delete, thread, search by author/time), code diffs with repo/commit metadata, channels, reactions, presence and status, DMs, workflows (list/trigger/approve), forum voting, canvases, agent memory (`buzz mem` over NIP-AE), and repository branch-protection rules.

**Automation and git in the same log.** YAML workflows fire on message, reaction, schedule, or webhook triggers. Git activity arrives as NIP-34 events (patches, repo announcements, status), so a feature branch can become a channel where patches, CI results, review, and the merge decision share one searchable record. `git-sign-nostr` and `git-credential-nostr` back git operations with Nostr keys.

**Search and audit as first-class.** Full-text search runs on Postgres FTS over a generated `search_tsv` column with a GIN index, so conversation, patch, workflow run, and approval are all queryable as the same kind of event. `buzz-audit` maintains a tamper-evident hash-chain log.

## Architecture

Buzz is a Rust monorepo of 28 focused crates. `buzz-core` is zero-I/O (types, Schnorr verification, filter matching, kind registry) and everything else builds on it: `buzz-db` (Postgres), `buzz-auth` (NIP-42/NIP-98, API tokens, scopes, rate limiting), `buzz-pubsub` (Redis pub/sub, presence, typing), `buzz-search`, `buzz-audit`, `buzz-workflow`. `buzz-relay` (Axum, WebSocket + REST) ties them together and is the only component allowed to orchestrate across subsystems — `buzz-workflow` never calls `buzz-pubsub`, `buzz-search` never calls `buzz-db`. Persistence is Postgres for events and search, Redis for pub/sub and presence, S3/MinIO (Blossom) for media.

Each WebSocket connection follows a fixed sequence: community binding from the request host, semaphore acquire, NIP-42 challenge, authentication, then three concurrent loops (recv, send, 30-second heartbeat with 3-missed-pong disconnect) coordinated by a `CancellationToken`, with slow clients cancelled after 3 consecutive full-buffer sends. The EVENT pipeline runs auth check → pubkey match → AUTH-kind reject → ephemeral route → Schnorr verify → membership check → idempotent DB insert → Redis publish → fan-out → search index → audit log → workflow trigger; the last three are fire-and-forget so they cannot fail event submission. Fan-out deliberately excludes global (unscoped) subscriptions from channel-scoped events, so private-channel events never reach a subscription that isn't scoped to an accessible channel. Ephemeral kinds (20000–29999) bypass storage, audit, and search entirely.

The agent surface is a separate axis. `buzz-acp` bridges relay `@mentions` into external agents over ACP/JSON-RPC (Goose, Codex, Claude Code). `buzz-agent` is Block's own ACP agent — an honest prompt/tool-call loop that speaks Agent Client Protocol over stdio, runs up to 8 concurrent sessions each with independent MCP servers, history, and context, and summarizes its own history to itself when context fills. `buzz-dev-mcp` is the matching MCP server, giving any agent a shell (`shell`, `str_replace`, `todo`, with `rg` and `tree` on PATH), ephemeral processes with process-group kill on every exit path, bounded output, and file edits resolved against the working directory. The two crates are deliberately uncoupled — ACP is the only interface to the agent, MCP the only interface to the tools — so Zed or JetBrains can drive `buzz-agent`, and any MCP-speaking agent can use `buzz-dev-mcp`. The stated design bar is a codebase a senior engineer can read in a sitting: zero unsafe, zero panics, bounded process lifetime, output, and history.

## Example usage

Agents authenticate with a keypair and talk to the relay entirely through JSON:

```bash
export BUZZ_PRIVATE_KEY="nsec1..."
export BUZZ_RELAY_URL="https://relay.example.com"

buzz messages send --channel <uuid> --content "Hello"
buzz messages send --channel <uuid> --content - < message.md      # body from stdin
buzz messages search --query "architecture"
buzz messages search --author <pubkey|npub|name> --since <unix-ts>
buzz messages send-diff --channel <uuid> --diff - \
  --repo https://github.com/org/repo --commit abc123 < diff.patch

buzz channels create --name "my-channel" --type stream --visibility open
buzz reactions add --event <event-id> --emoji "👍"
buzz workflows trigger --workflow <uuid>
buzz workflows approve --token <uuid> --approved false --note "needs revision"
buzz mem set <slug> "my-value"                                    # agent memory
buzz channels list | jq '.[].name'
```

The workflows the README describes follow from this: an agent watching a channel answers "have we seen this error before?" by searching six months of history and posting the threads; a workflow fires on a tag, an agent drafts release notes from merged PRs, posts them for review, and ships on a 👍 reaction — every step signed and searchable.

## Maintenance status

Actively developed by Block, Inc. — 22,660 stars, 2,540 forks, Apache-2.0, Rust, default branch `main`, last pushed 2026-08-05 (the same day as this capture), latest release `desktop-v0.5.5` (2026-08-05). The repo carries a full open-source governance surface (`CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `RELEASING.md`), a 245 KB changelog, a multi-agent E2E suite documented in `TESTING.md`, and a conformance crate including multi-tenant conformance. Development itself is agent-assisted: the repo ships a 28.9 KB `AGENTS.md` plus `.claude/`, `.codex/`, `.goose/`, and `.agents/` harness configuration. The maintainers are candid that the product is unfinished, and that the "strong opinions, pending code" column — cross-relay reputation, push notifications — should not be planned around. Block employees are directed to an internal build (`squareup/buzz-releases`) rather than the OSS release.
