# xhluca/session-migrate

## Metadata
- Stars: 53
- Primary language: Python
- Default branch: main
- Latest release: v0.8.0 (2026-08-25)
- License: MIT License
- Homepage: https://session-migrate.github.io/
- Fetched: 2026-08-26
- Final URL: https://github.com/xhluca/session-migrate

## Description
Migrate native coding-agent sessions across Claude Code, Codex, Pi, OpenCode, Copilot, Antigravity, Vibe, Muse, Qwen, Kimi, and Cursor.

## README
<p align="center">
  <a href="https://session-migrate.github.io/"><img src="https://raw.githubusercontent.com/xhluca/session-migrate/main/docs/assets/logo-lockup.svg" alt="session-migrate" width="430"></a>
</p>

<p align="center"><strong>Migrate your sessions to any harness.</strong></p>

<p align="center">
  <a href="https://pypi.org/project/session-migrate/"><img src="https://img.shields.io/pypi/v/session-migrate?style=flat-square&color=b8f94a&label=PyPI" alt="PyPI version"></a>
  <a href="https://pypi.org/project/session-migrate/"><img src="https://img.shields.io/pypi/pyversions/session-migrate?style=flat-square" alt="Python versions"></a>
  <a href="https://github.com/xhluca/session-migrate/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-8dbdff?style=flat-square" alt="MIT license"></a>
  <a href="https://session-migrate.github.io/"><img src="https://img.shields.io/badge/website-live-b8f94a?style=flat-square" alt="Project website"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/xhluca/session-migrate/main/docs/assets/demo.gif" alt="A Claude Code session migrated and continued inside the native Pi TUI" width="860">
</p>

<p align="center">
  Move coding agent sessions among <strong>Claude Code</strong>,
  <strong>Codex</strong>, <strong>Pi</strong>, <strong>Oh My Pi</strong>,
  <strong>OpenCode</strong>,
  <strong>GitHub Copilot CLI</strong>, <strong>Antigravity CLI</strong>,
  <strong>Cursor Agent</strong>, <strong>Mistral Vibe</strong>,
  <strong>Muse Code</strong>, <strong>Qwen Code</strong>, and
  <strong>Kimi Code</strong>.
</p>

## Install

```bash
curl -LsSf https://session-migrate.github.io/install.sh | sh
```

Or install with `uv`:

```bash
uv tool install session-migrate
```

`pipx install session-migrate` works too. Python 3.11+ and Linux are currently
supported. The full command is `session-migrate`; `smigrate` is the shorthand.
Already installed? Run `uv tool upgrade session-migrate`.

## Quick start

Inspect any native transcript without printing its conversation:

```bash
smigrate inspect ~/.claude/projects/-work/SESSION.jsonl
```

Move a Claude session into Codex and resume it from the same project directory:

```bash
smigrate transfer SESSION_UUID --from claude --to codex --cwd "$PWD"
codex resume NEW_SESSION_UUID
```

Or find an older session by its native title/name first:

```bash
smigrate catalog refresh
smigrate catalog search "oauth refresh" --format claude
smigrate transfer --title "oauth refresh" --from claude --to pi
```

Search is case-insensitive and every word must match, in any order. It searches
native titles, names, and IDs—not conversation bodies. A few useful patterns:

```bash
# "Fix flaky PostgreSQL timeout" also matches this reversed keyword order.
smigrate catalog search "timeout postgres"

# Find a release conversation among archived Codex sessions from this month.
smigrate catalog search "release notes" --format codex \
  --lifecycle archived --since 2026-08-01T00:00:00Z

# Opt in to matching a project directory when the title is vague.
smigrate catalog search "checkout api" --include-paths
```

`catalog refresh` is exhaustive inside the default, environment-selected,
registered, and explicitly discovered roots. It does not crawl your whole disk.

## Give it to your coding agent

Choose the route on the [project website](https://session-migrate.github.io/),
or replace the three bracketed values yourself:

> Follow https://session-migrate.github.io/llms.txt to migrate a session from
> `[SOURCE]` to `[TARGET]`. Session: `[UUID OR TITLE]`

The linked procedure is sandbox-tested with both Claude Code and Codex. See the
[agent workflow and verification](https://github.com/xhluca/session-migrate/blob/main/docs/coding-agent-instruction.md).

## Compatibility

- Claude Code
- Codex CLI
- Pi
- Oh My Pi (OMP)
- OpenCode
- GitHub Copilot CLI
- Antigravity CLI
- Mistral Vibe
- Muse Code
- Qwen Code
- Kimi Code
- Cursor Agent (experimental, pinned, text only)

Every listed format can be a source or target: 144 ordered routes, including
same-format portable rewrites. Cursor deliberately transfers only ordered
user/assistant text and is pinned to one exact Linux build; it is not a
vendor-supported import API. Same-format migration creates a new independent
session—it is not a byte-for-byte clone or a live sync.

## What survives

| Session data | Result | Notes |
| --- | :---: | --- |
| User and assistant messages | ✓ | Preserved in order on every route |
| Tool calls and results | ✓ / partial | Preserved when both adapters support the native shape |
| Images | ✓ / partial | Supported image blocks move; other media is format-dependent |
| Compaction summaries | ✓ / partial | Recreated where the target has a portable equivalent |
| Readable reasoning | Vibe-only portable rewrite | Vibe keeps its explicit readable field when rewritten to Vibe; other/private/signed traces never move |
| Session name, ID, and picker entry | Recreated | The target gets a new native identity and resume state |
| Branches, forks, and subagents | Not flattened | Cataloged separately where detectable; migrate the parent session |
| Private or signed thinking | No | Model/provider-bound traces are deliberately omitted |
| Auth, hooks, policies, MCP, and runtime config | No | These remain with the source client |

Every omission or transformation is counted in a content-free migration
manifest. The source session is never modified. Cursor intentionally accepts
text only. See
[Pi thinking traces](https://github.com/xhluca/session-migrate/blob/main/docs/pi-thinking-traces.md).

## How it works

```text
native session → validated event timeline → native target → resume
```

Each reader projects a versioned native transcript into a small ordered model.
Each writer then emits only structures verified against the target CLI. This is
session migration, not text export: the target receives a discoverable,
resumable native session.

## More

- [CLI reference](https://github.com/xhluca/session-migrate/blob/main/docs/cli-reference.md)
- [Coding-agent instruction](https://github.com/xhluca/session-migrate/blob/main/docs/coding-agent-instruction.md)
- [Session catalog](https://github.com/xhluca/session-migrate/blob/main/docs/session-catalog.md)
- [Compatibility details](https://github.com/xhluca/session-migrate/blob/main/docs/format-compatibility.md)
- [Troubleshooting](https://github.com/xhluca/session-migrate/blob/main/docs/troubleshooting.md)
- [Format research and validation](https://github.com/xhluca/session-migrate/blob/main/docs/validation-report.md)
- [Data handling and architecture](https://github.com/xhluca/session-migrate/blob/main/docs/architecture.md)
- [Antigravity format](https://github.com/xhluca/session-migrate/blob/main/docs/antigravity-format.md)
- [Oh My Pi format](https://github.com/xhluca/session-migrate/blob/main/docs/omp-format.md)
- [Experimental Cursor format](https://github.com/xhluca/session-migrate/blob/main/docs/cursor-format.md)
- [Mistral Vibe format](https://github.com/xhluca/session-migrate/blob/main/docs/vibe-format.md)
- [Muse, Qwen Code, and Kimi Code formats](https://github.com/xhluca/session-migrate/blob/main/docs/muse-qwen-kimi-formats.md)

The Antigravity and Cursor adapters are clean-room, unofficial, and
version-pinned. Their independently observed formats are published separately:
[Antigravity research](https://github.com/xhluca/antigravity-session-interoperability)
and [Cursor research](https://github.com/xhluca/cursor-session-interoperability).

The demo above uses real native casts recorded with the same tmux + asciinema
approach as agent-talk. Claude diagnoses a boundary bug in a small project; the
migrated session is reopened in Pi, which applies the proposed patch and runs
the regression test. It shows the source TUI, the migration command, the shared
history, and the continued target session. The website plays those casts
directly in JavaScript; the README animation is rendered from that same scene.
The same source session is also continued in
[Claude → Codex](https://raw.githubusercontent.com/xhluca/session-migrate/main/docs/assets/demo-codex.gif).
[Watch the larger-text Pi video](https://github.com/xhluca/session-migrate/raw/main/docs/assets/demo-pi.mp4),
[watch the larger-text Codex video](https://github.com/xhluca/session-migrate/raw/main/docs/assets/demo-codex.mp4),
or [reproduce both](https://github.com/xhluca/session-migrate/blob/main/scripts/render-demo.sh).
The recorder uses disposable credential copies only to drive the native clients;
the published assets contain only the controlled demo project and omit account
status.

## Contributing

```bash
git clone https://github.com/xhluca/session-migrate.git
cd session-migrate
uv sync --dev
uv run pytest
```

See [the development guide](https://github.com/xhluca/session-migrate/blob/main/docs/development.md)
before changing a native
adapter. New formats need sanitized fixtures and a real native-resume oracle.

## License

MIT

## Docs

### docs/architecture.md

# Architecture

`session-migrate` converts native coding-agent histories without treating a
terminal transcript as an interchange format.

```text
native source
    │ bounded parse + identity checks
    ▼
ordered portable event timeline
    │ target-specific projection + loss accounting
    ▼
validated native target + content-free manifest
```

The source is always authoritative and never modified. A target is a new,
independent conversation.

## Layers

| Layer | Responsibility |
| --- | --- |
| `model.py` | Agent/target enums and neutral `Session`/`Event` types |
| `formats/*.py` | One bounded native reader/writer per agent |
| `inspection.py` | Content-free format detection and structural inventory |
| `discovery.py` | Exact native-ID lookup without trusting mutable indexes |
| `catalog.py` | Private multi-root metadata index and title/ID search |
| `conversion.py` | Dispatch, portable rewrite, validation, manifests, installation |
| `cli.py` | User-facing commands and JSON/error contracts |

The neutral event kinds are message, tool call, tool result, thinking,
compaction, context, and opaque. Roles are user, assistant, system, and tool.
Each event retains source record ordinal/type and, where available, source IDs
and block ordinals. The model is intentionally small: it represents portable
conversation history, not an agent's entire runtime.

## Read paths

### JSON and JSONL sources

Claude, Codex, Pi, OMP, Copilot, Vibe, Muse, Qwen, and Kimi messages are bounded
JSON/line streams. Readers cap total
bytes, record bytes, record count, JSON nesting/nodes, and media payloads. They
validate source identity before and after reading so an actively appending,
replaced, or truncated file fails with a retryable error.

- Claude reconstructs the active UUID ancestry selected by `last-prompt`,
  validates compaction back-edges, and excludes inactive branches/meta prompts.
- Codex replays canonical legacy `response_item` history, deduplicates UI
  projections, and rejects paginated/history-base lineage.
- Pi follows the v3 `id`/`parentId` active tree and rejects unsupported schema
  versions.
- OMP follows its v3 active tree after validating the fixed 256-byte title
  slot, honors native reset boundaries, and safely resolves hashed image blobs.
- Copilot validates its schema-v1 event envelope, root agent, assets, and tool
  linkage.
- Vibe snapshots `meta.json` and `messages.jsonl` together, validates the
  documented `LLMMessage` shape, and projects readable reasoning, tools,
  images, compaction, and injected-runtime omissions.
- Muse validates its durable metadata, retained markers, and linked
  intent→run→materialization lifecycle before projecting committed events.
- Qwen follows the active UUID/parent chat graph and counts inactive branches.
- Kimi snapshots `state.json` and the main-agent protocol-`1.5` wire journal
  together before projecting context events.

### OpenCode virtual sources

The catalog reads only native session metadata from `opencode.db`. A selected
source is exported through exact pinned `opencode export`, parsed as an official
bundle, and represented by the virtual path `opencode:<id>`. The migrator never
queries message/part tables or writes OpenCode SQLite.

### SQLite/protobuf sources

Antigravity and Cursor readers make a consistent SQLite backup that includes
committed WAL state. They then validate exact table/index/user-version
contracts and decode protobuf wire structures through independently written,
bounded codecs.

- Antigravity projects user/planner messages and observed generic tool
  steps/results.
- Cursor walks SHA-256-addressed root→turn→user/assistant blobs and projects
  text only. Every unsupported native occurrence becomes a reason-specific
  opaque event so a later target manifest cannot silently claim losslessness.

## Write paths

Writers consume the same ordered event timeline and return `(native_bytes,
loss_counters)`. No writer reads another source format directly.

| Target | Native artifact |
| --- | --- |
| Claude | UUID-linked project JSONL |
| Codex | Legacy rollout JSONL with canonical response items and UI projection |
| Pi | v3 session JSONL tree |
| Oh My Pi | v3 title-slot session JSONL tree |
| OpenCode | Official JSON import bundle |
| Copilot | Schema-v1 event JSONL plus workspace sidecar |
| Antigravity | Complete trajectory SQLite/protobuf DB plus picker summary on install |
| Cursor | Complete content-addressed SQLite/protobuf DB, text only |
| Vibe | Native `meta.json` plus `messages.jsonl` session directory |
| Muse | Date-partitioned durable session event JSONL |
| Qwen | Project-scoped append-only chat graph JSONL |
| Kimi | Native `state.json` plus main-agent `wire.jsonl` session directory |

Every generated artifact is reparsed/validated before publication. Target
required IDs, timestamps, and metadata may be synthesized. Source tool output,
reasoning, or system instructions are never invented. Known transformations
and omissions are counted.

OpenCode IDs and timestamps are made monotonically sortable because its runtime
pages history by `(time_created, id)`. Claude emits a fresh linear parent chain.
Codex emits legacy history rather than synthesizing the more coupled paginated
projection. Cursor groups assistant steps beneath the most recent user turn and
rejects histories with no portable user message.

## Same-format migration

Same-format is not a fast copy. It deliberately runs reader→portable
model→writer, allocates a new target identity, and emits
`same_format_portable_rewrite`. This removes source-only runtime state just as a
cross-format route would. It is useful for moving between homes or normalizing
an older supported transcript, but it is not byte-identical and does not keep
the two sessions synchronized.

## Native installation

Filesystem targets use no-clobber publication. New files are mode `0600`; new
state directories are mode `0700`; existing directory permissions are not
silently changed. The source is never overwritten.

- Claude/Codex/Pi/OMP write one native transcript and one manifest atomically.
- Muse/Qwen write one native transcript and one manifest atomically.
- Kimi reserves a native session directory and publishes its state, wire
  journal, and manifest with rollback guards.
- Vibe reserves a short-ID-safe native directory and atomically publishes its
  metadata, message stream, and manifest.
- Copilot reserves the complete session directory and writes events, workspace
  sidecar, and manifest.
- OpenCode reserves a private external manifest, invokes only the official
  pinned importer, confirms the ID through official listing, then finalizes the
  manifest.
- Antigravity and Cursor reserve the manifest, verify the exact pinned binary,
  invoke their clean-room atomic database installers, validate the installed
  session, then finalize the manifest.

If failure occurs after an external/native installer succeeds, the error says
that the session may already exist. Blind retry is intentionally avoided.

## Version boundaries

Claude/Codex writers are pinned to the local integration image; Pi, OMP, OpenCode,
Copilot, Antigravity, Cursor, Vibe, Muse, Qwen, and Kimi to exact host
builds/releases. A source declaring a
different version produces `unvalidated_source_version`. A
`--target-cli-version` override changes metadata only and produces
`unvalidated_target_version`; it never changes writer architecture.

Automatic OpenCode, Antigravity, and Cursor installation is stricter: metadata
overrides cannot bypass exact runtime version checks. Antigravity verifies its
binary digest. Cursor verifies launcher, main bundle, protobuf-bearing chunk,
bundled Node, sizes, SHA-256 values, and reported version.

Cursor remains experimental because only text history has passed the native
loader/TUI/backend-blob gates and a real authenticated assistant checkpoint
followed by a second resume has not been proven.

## Catalog architecture

The catalog is a derived, private SQLite database. It stores roots, scan runs,
session metadata, and bounded labels—never message/tool/media bodies. Native
files/rows remain authoritative.

Enumeration covers:

- Claude main sessions and nested sidechains;
- Codex active and archived rollouts;
- Pi and OMP workspace buckets, classified by their native heads;
- every OpenCode `session` row, including parents/archives;
- Copilot session directories, including missing event logs;
- Antigravity conversation DBs; and
- Cursor workspace/chat DBs, including missing stores;
- Vibe and Kimi multi-file session directories;
- Muse date-partitioned event streams; and
- Qwen project chat graphs.

JSONL rows use stat identity. Vibe and Kimi fingerprint both native files.
Antigravity/Cursor include DB/WAL/SHM fingerprints.
OpenCode rows use a fingerprint of every indexed metadata field. Unavailable
roots retain prior rows instead of falsely marking everything missing.

Search covers native names/titles and IDs. Paths/CWDs are opt-in. "All sessions"
means all recognized sessions in auto-selected, registered, or explicitly
bounded-discovered roots; arbitrary whole-disk discovery is neither safe nor
honest.

## Manifest semantics

Schema-v2 manifests contain migration/source/target identities, paths, hashes,
versions, structural counts, `dropped_events`, and warning objects. They contain
no message/tool/media bodies. The historical `dropped_events` name includes:

- data that was omitted;
- data that was transformed or grouped; and
- inconsistent records retained with a warning.

Non-empty counters do not necessarily mean a whole event vanished. Operators
should inspect warning keys before resume.

## Data and credential boundary

The project does not read or copy login stores, cookies, API keys, shell state,
pending approvals, processes, MCP connections, memories, or workspace files.
Native validation may use isolated test-only credential copies when a target
technically accepts the same account/provider schema; that is not a migration
feature.

There is no redaction, encryption, or secret scanning. A secret embedded in a
supported message, tool argument/result, or image is copied into the target.
Treat sources, targets, manifests, catalog metadata, and CLI JSON as sensitive
according to their contents.

## Adding a format

A new adapter needs:

1. a sanitized native-shaped fixture;
2. strict bounded parsing and generated-byte validation;
3. explicit loss counters for every unsupported semantic class;
4. conversion, detection, discovery, catalog, and CLI integration;
5. all-routes semantic and loss-accounting tests; and
6. an actual native load/resume oracle at an exact pinned version.

Private-format work must be clean-room and publish only independently observed
descriptions and synthetic generators—not vendor code, binaries, descriptors,
credentials, or real transcripts.

### docs/cli-reference.md

# CLI reference

This page documents `session-migrate` 0.8.0. `smigrate` is an exact shorthand
for the same executable.

## Commands

```text
session-migrate inspect PATH [--format FORMAT] [--json]
session-migrate convert PATH --to TARGET --output PATH [OPTIONS]
session-migrate import PATH --to TARGET [--home PATH] [--dry-run] [OPTIONS]
session-migrate transfer SOURCE_ID --from FORMAT --to TARGET [OPTIONS]
session-migrate transfer --catalog-id ID --to TARGET [OPTIONS]
session-migrate transfer --title TITLE [--from FORMAT] --to TARGET [OPTIONS]
session-migrate catalog refresh [ROOT OPTIONS] [--validate] [--json]
session-migrate catalog roots list|add|remove ...
session-migrate catalog list [FILTERS]
session-migrate catalog search QUERY [FILTERS]
session-migrate catalog show CATALOG_ID [--include-paths] [--json]
```

`FORMAT` and `TARGET` accept:

```text
claude  codex  pi  omp  opencode  copilot  antigravity  cursor  vibe  muse  qwen  kimi
```

All twelve formats are readable and writable. Cursor is an experimental,
text-only adapter pinned to one exact Cursor Agent build. Same-format migration
is supported as a portable rewrite into a new independent session.

## `inspect`

`inspect` reports structural metadata and counts without printing message text,
tool arguments/results, image bytes, or titles.

```bash
smigrate inspect ~/.codex/sessions/2026/08/20/rollout-...jsonl
smigrate inspect ./store.db --format cursor --json
```

It prints the source path, CWD, UUID, timestamps, SHA-256, and structural
counts. Those fields can still be sensitive. Successful inspection means the
container is structurally recognizable; conversion applies stricter semantic
validation.

`--format` bypasses automatic format selection. It does not make an unsupported
schema or version safe.

## `convert`

`convert` writes a standalone target artifact plus a sidecar manifest:

```bash
smigrate convert SOURCE --to codex --output ./rollout.jsonl
```

The manifest is `OUTPUT.session-migrate.json`. `convert` never installs into a
native agent home and never invokes a target CLI. For OpenCode it writes an
official import bundle; for Antigravity and Cursor it writes a complete SQLite
database; for Vibe it writes a validation bundle that `import` publishes as
native `meta.json` plus `messages.jsonl`.

## `import`

`import` converts and installs into a target store:

```bash
smigrate import SOURCE --to pi --cwd "$PWD" --dry-run
smigrate import SOURCE --to pi --cwd "$PWD"
```

The target paths are collision checked and never overwritten. `--dry-run`
performs conversion, native validation, and collision checks but does not
install a session or manifest. OpenCode's official read/list preflight can
initialize its ordinary XDG cache/database metadata during a dry run.

OpenCode import always uses the official pinned CLI and does not accept
`--home`; isolate or select it with normal `HOME`/XDG variables. Antigravity and
Cursor installs verify the exact pinned executable and its published hashes.
Muse and Qwen install one native JSONL; Kimi installs its native `state.json`
and main-agent `wire.jsonl` together.

## `transfer`

Direct lookup uses a native source ID:

```bash
smigrate transfer SOURCE_UUID --from claude --to codex --cwd "$PWD"
smigrate transfer SOURCE_UUID --from omp --source-cwd "$PWD" --to codex
smigrate transfer SOURCE_UUID --from cursor --source-cwd "$PWD" --to claude
smigrate transfer SOURCE_UUID --from vibe --source-cwd "$PWD" --to codex
smigrate transfer SOURCE_UUID --from qwen --source-cwd "$PWD" --to kimi
smigrate transfer session_SOURCE_UUID --from kimi --source-cwd "$PWD" --to muse
smigrate transfer ses_... --from opencode --to pi --source-cli ~/.opencode/bin/opencode
```

Claude, Pi, OMP, Cursor, Vibe, Qwen, and Kimi can use `--source-cwd` to select a
workspace-specific store. OpenCode is virtual: the pinned official CLI exports
the requested ID. All other sources are read from their native files.

Catalog transfer avoids ambiguous paths and duplicate UUIDs:

```bash
smigrate catalog search "parser refactor"
smigrate transfer --catalog-id CATALOG_ID --to copilot
smigrate transfer --title "parser refactor" --from claude --to copilot
```

`SOURCE_ID` selects the source. `--session-id` assigns the new target UUID;
they are deliberately different concepts.

`--title` searches the existing catalog and proceeds only when one session
matches. An exact case-insensitive title wins over partial keyword matches.
Refresh the catalog first; if the title is ambiguous, use `catalog search` and
pass the selected opaque ID with `--catalog-id`.

Without `--to`, only Claude→Codex and Codex→Claude retain their historical
default. Every other source requires an explicit target.

## Conversion options

| Option | Meaning |
| --- | --- |
| `--format FORMAT` | Override source detection for file-based `inspect`, `convert`, or `import` |
| `--session-id UUID` | Assign a new target UUID; generated by default |
| `--cwd PATH` | Target working directory; precedence is option, source CWD, process CWD |
| `--target-cli-version VERSION` | Change emitted metadata only; the writer architecture remains pinned |
| `--target-cli PATH` | Pinned OpenCode, Antigravity, or Cursor executable for native import |
| `--model-provider ID` | Codex, Pi, OMP, OpenCode, or Muse target provider |
| `--model ID` | Claude, Pi, OMP, OpenCode, Copilot, Antigravity, Vibe, Muse, Qwen, or Kimi target model label |
| `--home PATH` | Target native home, except OpenCode |
| `--dry-run` | Validate and collision-check without installing migrator artifacts |

An irrelevant target-specific option may be accepted but has no effect. The
manifest records the target metadata version and warns when it differs from the
validated writer pin. Automatic OpenCode, Antigravity, and Cursor installation
still requires the exact pinned version.

## Home resolution

| Format | Default source/target root |
| --- | --- |
| Claude | `$CLAUDE_CONFIG_DIR`, otherwise `~/.claude` |
| Codex | `$CODEX_HOME`, otherwise `~/.codex` |
| Pi | `$PI_CODING_AGENT_DIR`, otherwise `~/.pi/agent` |
| Oh My Pi | `$PI_CODING_AGENT_DIR`, otherwise `~/.omp/agent` |
| OpenCode | official CLI under its normal XDG data root |
| Copilot | `$COPILOT_HOME`, otherwise `~/.copilot` |
| Antigravity | `~/.gemini/antigravity-cli` |
| Cursor | `$CURSOR_CONFIG_DIR`, `$XDG_CONFIG_HOME/cursor`, otherwise `~/.cursor` |
| Vibe | `$VIBE_HOME`, otherwise `~/.vibe` |
| Muse | `$XDG_DATA_HOME/muse`, otherwise `~/.local/share/muse` |
| Qwen | `$QWEN_HOME`, otherwise `~/.qwen` |
| Kimi | `$KIMI_CODE_HOME`, otherwise `~/.kimi-code` |

Explicit `--home` or `--source-home` wins where supported. All CLI path options
expand `~` consistently.

## Catalog

The private SQLite catalog is at
`$SESSION_MIGRATE_CATALOG`, otherwise
`$XDG_STATE_HOME/session-migrate/catalog.sqlite3`, otherwise
`~/.local/state/session-migrate/catalog.sqlite3`.

Refresh auto-registers existing default, environment-selected, and ancestor
project roots:

```bash
smigrate catalog refresh
smigrate catalog refresh --discover-under ~/dev --validate
```

Additional roots are repeatable:

```text
--claude-root PATH       --codex-root PATH
--pi-root PATH           --omp-root PATH
--opencode-root PATH
--copilot-root PATH      --antigravity-root PATH
--cursor-root PATH       --vibe-root PATH
--muse-root PATH         --qwen-root PATH
--kimi-root PATH
```

`--discover-under` is bounded to the supplied directory, never follows
symlinked directories, and recognizes conventional hidden stores. Arbitrary
custom root names must be registered explicitly. "All sessions" means all
recognized entries in these configured/discovered roots—not a whole-disk scan.

Search is case-insensitive across native title/name metadata and IDs. Multiple
keywords are ANDed and may occur in any order:

```bash
smigrate catalog search "database migration" --format codex
smigrate catalog search "timeout postgres" --lifecycle archived
smigrate catalog list --status candidate --since 2026-08-01T00:00:00Z
```

Paths and CWDs are neither searched nor printed unless `--include-paths` is
passed. The catalog never stores conversation bodies or tool payloads. See the
[catalog guide](session-catalog.md) for statuses and schema behavior.

## Successful JSON output

`convert`, `import`, and `transfer` print one content-free JSON object:

```json
{
  "cwd": "/target/workspace",
  "dropped_events": {"thinking:unsupported": 2},
  "dry_run": true,
  "manifest": "/target/state/session-migrate/manifests/UUID.json",
  "output": "/target/native/session/path",
  "records": 12,
  "session_id": "TARGET_ID",
  "sha256": "TARGET_SHA256",
  "source_format": "claude",
  "target_format": "cursor",
  "warnings": []
}
```

The historical field name `dropped_events` includes omissions,
transformations, and retained inconsistencies that need operator attention.
Non-empty warnings do not mean the command failed. Review them before resume.

Manifests use schema version 2 and include migration version, source/target
identity and hashes, structural counts, warning objects, and the same loss
counters. They never include message/tool/media bodies, but their paths, IDs,
CWDs, timestamps, and hashes are operationally sensitive.

A dry-run conversion is regenerated on apply. A fixed `--session-id` usually
pins native paths, but generated structural IDs/timestamps can change, so do not
expect identical SHA-256 values.

## Exit behavior

- `0`: success, help, or version
- `2`: argument error or expected migration failure

Expected failures are printed to stderr as:

```text
session-migrate: error: MESSAGE
```

There is no overwrite/force mode. Source files are always left untouched. If
manifest finalization fails after an external/native install, the error states
that the target session may already exist so the operator can inspect it before
retrying.

## Top-level structure

- `.claude/` — Claude Code agent instructions for this repo (agent-facing config, not a build artifact)
- `.gitignore`
- `.python-version`
- `CHANGELOG.md`
- `LICENSE` — MIT
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `docs/` — extensive per-format research/design docs (architecture, cli-reference, coding-agent-instruction, per-agent format specs for antigravity/cursor/vibe/muse/qwen/kimi/omp/opencode/copilot, validation-report, troubleshooting, session-catalog, specification, development guide) plus `docs/assets/` (logo, demo GIFs/videos, screenshots)
- `install.sh` — curl-pipe installer script
- `llms.txt` — machine-readable procedure for coding agents to perform a migration
- `pyproject.toml`
- `scripts/` — demo recording and native-format validation scripts (`capture-native-tui-demo.py`, `render-browser-demo.py`, `render-demo.sh`, `validate-*-native.py` / `validate-*-corpus.py` per target, `verify-native-resume.sh`)
- `src/session_migrate/` — package source:
  - `__init__.py`, `__main__.py`
  - `catalog.py` — private SQLite session index (roots, scan runs, metadata, search)
  - `cli.py` — CLI commands and JSON/error contracts
  - `conversion.py` — dispatch, portable rewrite, validation, manifests, installation
  - `discovery.py` — exact native-ID lookup
  - `errors.py`
  - `inspection.py` — content-free format detection and structural inventory
  - `jsonl.py`
  - `model.py` — neutral `Session`/`Event` types and Agent/target enums
  - `formats/` — one bounded reader/writer module per agent: `antigravity.py`, `claude.py`, `codex.py`, `common.py`, `copilot.py`, `cursor.py`, `kimi.py`, `muse.py`, `omp.py`, `opencode.py`, `pi.py`, `qwen.py`, `vibe.py`
- `tests/` — pytest suite: per-format unit + native-resume tests (`test_<format>_format.py` / `test_<format>_native.py` for each of the 12 agents), plus `test_catalog.py`, `test_cli.py`, `test_conversion.py`, `test_discovery.py`, `test_inspection.py`, `test_jsonl.py`, `test_route_matrix.py`, `test_target_integration.py`, and `fixtures/`
- `uv.lock`
- `website/` — project website source (session-migrate.github.io)
