# Einsia/agent-git

## Metadata
- Stars: 414
- Forks: 37
- Primary language: Rust
- Default branch: main
- Latest release: agit-v0.2.28 (2026-10-27)
- License: MIT License
- Homepage: https://agent-git.com
- Pushed at: 2026-10-28T06:39:09Z
- Fetched: 2026-10-28
- Final URL: https://github.com/Einsia/agent-git

## Description
Code is cheap, show me the talk: version control for agent sessions

## README
# agit

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-orange?logo=rust&logoColor=white)](https://www.rust-lang.org)

Lossless version control for every agent session: publishable, resumable.
Works with Claude Code, Codex, OpenCode, and Cursor.

On disk, sessions are just JSONL files that get overwritten, compacted, and
cleaned up at any moment. `agit` puts snapshots and versions on top of them,
so "that conversation last Wednesday that finally cracked the bug" becomes
something you can find, continue, and hand to a teammate.

```text
agit                              choose a session to continue
agit new                          choose a repo and name a fresh conversation
agit import                       choose an existing runtime conversation to adopt
agit log                          choose a session and browse its history
agit push                         choose a saved session to publish
agit share                        choose a session and review link settings
agit run owner/repo@ref           open a saved source, forking when needed
```

These bare commands open their interfaces in a human terminal. `agit resume`
continues the same session and never forks; `agit run` can start a new writable
session from a tag, historical point or another author's source.

Inside an adopted agent session, `agit commit` saves completed turns and
`agit push` publishes that session. For scripts, pass the target explicitly,
for example `agit push owner/repo@branch --json`. Directory branch pins do not
choose targets for `commit`, `push` or `share`.

On user-facing startup, `agit` checks for a newer release at most once a day and prints a
reminder to stderr; it never upgrades automatically. JSON/quiet/CI and internal hook/MCP paths
skip this reminder.

Adopting and recording the first version are one command — the in-between
state ("linked, but unversioned") means nothing to anyone. To mark a session
without versioning it (e.g. offline), pass `--link-only`.

Use a full native session ID and an explicit runtime and destination for lineage discovery.
The terminal offers verified local bases, independent import, or cancellation. Noninteractive
calls return choices without writing; pass `--onto <ref>` or `--independent` to select a path.
`--propose-lineage` prints a read-only report without adopting the session.
Inspecting lineage in an existing repository requires NUL-framed Git worktree output,
normally available in Git 2.36 or newer. An unsupported Git reports `git_worktree_format`;
explicit `--onto`, `--independent`, and `--link-only` imports retain their ordinary checks.

`agit clone` fetches repository history locally. Use `agit run` or `agit resume`
to start a runtime. A clone is **read-only by default** on the Hub: nothing is
created in your name and `origin` points at the source. `agit clone --mine`
creates your copy, repoints `origin` and remembers the source as `upstream`.

The full command list is in `agit --help`.

## Install

### Users: npm

```sh
npx -y create-agit@latest          # one-shot: installs agit + wires skills/hooks/MCP
# or as a global package:
npm install -g @einsia/agent-git   # pnpm add -g @einsia/agent-git works too
agit --version
```

Both routes install a prebuilt binary — no Rust toolchain required. npm
picks the platform sub-package matching your `os`/`cpu`; on platforms with no
prebuilt binary (e.g. FreeBSD) running `agit` prints the source-build recipe.
Details and environment variables: [`npm/README.md`](npm/README.md).

Windows x64 packages include the native peer RC daemon. On Windows, Linux and macOS, run
`agit login` followed by `agit rc start --detach` to register the device and allow your own
account to control it from Workspaces. Windows owner RPC uses a local named pipe restricted
to the current user. RC state requires a private, user-owned directory.

pnpm (v10+) does not run dependency install scripts by default, so the
automatic `agit setup` is skipped there — run `agit setup` once yourself
after installing.

The Linux artifact is **musl static-linked**, so no minimum glibc — the
release pipeline runs every Linux binary inside an Alpine / Amazon Linux /
Debian / Ubuntu container matrix before publishing.

Prebuilt binaries include Git and Git LFS, extracted into a private cache on first
use. Your shell PATH and global Git configuration stay unchanged. Source builds
use system Git; `AGIT_USE_SYSTEM_GIT=1` selects it in a prebuilt binary too.
See [runtime configuration and source prerequisites](docs/01_setup.md).

> Do not install `@einsia/agentgit` (no hyphen) — that is the pre-rewrite
> CLI; its protocol does not match this branch and it will not work.

### Contributors / eager users: from source

```sh
git clone https://github.com/Einsia/agent-git
cd agent-git
./setup.sh
```

`setup.sh` checks the toolchain (rustc, a C compiler), builds, and installs
the binary to `~/.local/bin/agit`. Common flags:

```sh
./setup.sh --debug      # no LTO, much faster while hacking
./setup.sh --test       # run cargo test --lib before installing
./setup.sh --help
```

To build a binary whose built-in hub is the staging deployment, set the build-time default
explicitly. Runtime `AGIT_HUB_URL` and `agit config hub.url ...` still take precedence:

```sh
AGIT_DEFAULT_HUB_URL=https://staging.agent-git.com cargo build --release --locked
```

Internal GitLab pipelines package commit-addressed `dev` and `staging` builds with this setting
embedded. Their `agit --version` output includes the channel and source commit, and `agit upgrade`
is disabled for them so an acceptance-test binary cannot silently turn into the public release.
Only an existing GitHub `agit-v*` tag produces the `prod` channel. The tag push runs the Release
workflow automatically; operators may also select the same reviewed tag through the workflow's
manual production input to retry a failed release without creating a different artifact identity.

Requires **rustc >= 1.88** and a C compiler (`rusqlite` uses the `bundled`
feature, so sqlite's C sources are compiled during the build). The reason for
the toolchain floor is in [`docs/01_setup.md`](docs/01_setup.md).

Both paths install the same binary. npm is for "users who don't want to touch
Rust"; `setup.sh` is for "people changing the code" and "people running
unreleased versions".

## Docs

| Goal                                    | Where                                                         |
| --------------------------------------- | ------------------------------------------------------------- |
| Build, run the backend, sign in, debug  | [`docs/01_setup.md`](docs/01_setup.md)                        |
| How sessions are stored locally         | [`docs/02_session_store.md`](docs/02_session_store.md)        |
| The terminal interface for humans       | [`docs/07_tui.md`](docs/07_tui.md)                            |
| Login / token mechanics                 | [`docs/commands/auth.md`](docs/commands/auth.md)              |
| Local low-entropy secret filtering      | [`docs/05_global_secret_filter.md`](docs/05_global_secret_filter.md) |
| Reversible repository secret placeholders | [`docs/06_repository_secret_dictionary.md`](docs/06_repository_secret_dictionary.md) |
| Probed storage formats of each runtime  | [`docs/mechanism-probing/`](docs/mechanism-probing/)          |
| npm package behavior and env vars       | [`npm/README.md`](npm/README.md)                              |
| Release artifact naming contract        | [`.github/RELEASE_ARTIFACTS.md`](.github/RELEASE_ARTIFACTS.md) |
| What changed in each release            | [`CHANGELOG.md`](CHANGELOG.md)                                |

The server (**AgentGit**) is a separate repository, deployed on its own.

## Release

`Cargo.toml` is the single source of the version; every npm manifest must
agree with it (`node scripts/check-version.js` — run in CI and before
`npm pack`). To move the version, change every spot in one shot:

```sh
node scripts/bump-version.mjs 0.1.0    # Cargo.toml + Cargo.lock + all npm manifests
```

Release notes live in [`CHANGELOG.md`](CHANGELOG.md), and they come first: write the
version's `## [x.y.z]` section, then bump. `bump-version.mjs` refuses to touch a file for
a version that has no section, and `check-version.js` refuses one in CI and before `npm pack`.
The section becomes the GitHub Release body (`scripts/release-notes.mjs` extracts it in
`release.yml`, with repository-relative links pinned to the release tag) and ships inside
the `@einsia/agent-git` package.

After the source release commit passes CI, merge it into GitLab `main`. Wait for
that pipeline's development builds and `mirror:github`, then run its manual
`release:github-tag` job. CI verifies the recorded source-to-mirror mapping and
creates `agit-v<version>` on the public mirror commit. Release tags are immutable;
a stale pipeline cannot publish after either `main` moves.

The mirror rewrites commit IDs, so the source SHA is not the release SHA. Do not
push release tags directly to GitHub. The CI-created tag starts the GitHub Release
workflow, which builds the binaries and then triggers npm publication.

Distribution to users runs through the npm registry: each target ships as a
platform sub-package (`@einsia/agent-git-linux-x64` and friends, gated by
`os`/`cpu` — npm installs only the matching one), and the main
`@einsia/agent-git` pulls them in via `optionalDependencies`. The GitHub
Release holds the canonical tarballs plus `SHA256SUMS`
([contract](.github/RELEASE_ARTIFACTS.md)).

Publishing to npm is the **npm publish** workflow. It runs automatically
once the Release workflow finishes green (and can be dispatched manually —
Actions → npm publish — for retries, `next` dist-tag trials, or a `dry_run`).
It publishes the whole family in dependency order — platform packages →
`@einsia/agent-git` → `create-agit` — with a real global install of the main
tarball as a preflight in between, authenticating via npm trusted publishing
(OIDC, no stored token). The equivalent local fallback:

```sh
gh release download agit-v0.1.0 -p 'agit-*.tar.gz' -D /tmp/agit-dist
node npm/publish.mjs /tmp/agit-dist        # platform packages → main → create-agit
```

`npm/create-agit/` is the one-shot installer behind `npx -y create-agit@latest` — it
depends on the main package and turns the npx cache copy into a durable
`~/.local/bin/agit`, then wires skills/hooks/MCP via `agit setup`. There is
deliberately no unscoped alias package: `agit` on npm belongs to an unrelated
project, and npm's typosquat rule blocks `agent-git` for being one punctuation
mark away from a third party's `agentgit`.

The version oracle (`GET /api/cli/version` on the hub) and `agit upgrade`
both read the npm registry; integrity verification uses the registry's
SRI (sha512). Self-hosted hubs that pin an internal fork set
`AGIT_BACKEND_CLI_REPO` and the whole chain reverts to the GitHub path.

`@einsia/agent-git` is a fresh package name with no existing users, so the
first release goes straight to `latest` — no need to hide in `next` first.
(The old `@einsia/agentgit` stays put; it points at the pre-rewrite CLI.)


## Docs

### AGENTS.md


<!-- agit:begin -->
## Session version control (agit)

Use these rules when the user requests an AgentGit operation or `AGIT_SESSION` or
`AGIT_MERGE_TX` identifies the current managed session. Otherwise continue the
user's task without agit checks, transcript discovery, or session adoption.
The working directory and this file alone do not activate AgentGit.

- Inspect `agit status --json` when the requested operation needs session or workspace state. An adopted session still needs an explicit `<owner/repo>@<branch>` or `AGIT_SESSION`; directory bindings and native runtime IDs do not select it.
- Settle completed phases with `agit commit <owner/repo>@<branch> --milestone "<summary>"` (add `--code` when relevant). Publish with `agit push` only when the user asks to; never push on your own. Importing a session does not set `AGIT_SESSION` in the calling process.
- If resumed as a merge agent, follow the `AGIT_MERGE_TX` protocol in the agit skill.
- Never rebase or force-push AgentGit history; remove context with `agit revert <owner/repo>@<branch>#n.k`. `@` requires `AGIT_SESSION`.
<!-- agit:end -->

## Everything here is written in English

This repository is mirrored publicly and read by people and agents who share no language with
whoever wrote a given line. A comment in a language the reader does not have is worse than no
comment at all: it still occupies the line where the explanation belongs, so the file reads as
if the explanation is there.

Rules:

- **Code and files are English.** Identifiers, comments, doc-comments, assertion messages,
  Markdown under `docs/`, skill documents, shell and CI scripts, and every string that reaches
  a terminal. Quote with `"..."`, never `「...」`, and use no other fullwidth punctuation —
  the em dash, `→`, `…` and `·` are this repository's own typography and stay.
- **Commit messages and merge request titles are English**, bodies included.

The exception is text that is data rather than prose: lexical tables the search index depends
on, character classes that match another script, fixtures that exist to exercise CJK width or
segmentation, and captured transcript evidence quoted verbatim. Those keep their original
language, and the comment beside them says which of these it is.

## Comments state invariants, not history

A comment outlives the situation that produced it. A measurement is about the machine that
produced it, and "the previous version missed this" means nothing once that version is
gone — but both keep being read as if still true, which is worse than no comment at all.

Rules for comments in this repository:

- State the rule and what breaks if it is broken, in the present tense and conditionally
  ("if the budget is one counter, links get billed at the dirent rate"), not as a report of
  something that already happened ("the first version wrote it as one counter").
- No measurements with units, no ratios like "7 of 8 runs", no counts of tests or of table
  entries. If a number is load-bearing, it belongs in a benchmark or an assertion, where it
  is checked; a number in prose is checked by nobody.
- No references to a previous revision, a review round, or a fix. Keep the failure *shape*
  when it explains the rule; drop the fact that it once occurred.
- A test's doc says which property it pins and how a plausible wrong implementation would
  escape it — not how the test was arrived at.
- **If a sentence is already in the commit message, it does not belong in a comment.**
  Commit messages are where the history goes; they are read against the diff that produced
  them, and they never drift.

The test to apply: would this sentence still be true and useful after the machine is
replaced, the traversal is rewritten, or the pool is reconfigured? If not, it is a lab note.

`scripts/check-comment-invariants.mjs` is available as an optional local review aid. It scans
the comment lines a branch adds relative to its merge base and flags numbers with units,
ratios, counts of tests or table entries, and phrasing that points at another version or
review round. It judges shapes; deciding what a sentence was trying to say, and rewriting it
as the invariant, is still yours. It is not a CI gate.

## Tests must justify their continued existence

- Every maintained test must have an explicit purpose: name the user-visible behavior,
  protocol contract, or failure boundary it protects and what a materially wrong
  implementation would do. Use a clear test name and a short contract comment where needed.
- A bug fix, a feature removal, or "preventing regression" is not by itself a reason to add
  a test. Do not add one test for every fix or removed feature.
- Before adding a test, identify the distinct contract that existing coverage cannot
  establish. Prefer updating or consolidating an existing test. If no distinct maintained
  contract is missing, do not add a test.
- Remove tests for deleted behavior, duplicate assertions of the same contract, and tests
  that merely mirror implementation details. Do not retain obsolete fixtures or helpers.
- Prefer a representative end-to-end check over repeated fixtures and broad combinations
  that exercise the same path. Keep focused unit tests only for independently meaningful
  boundaries that such a check cannot establish.
- Keep CI fast: run the smallest relevant targets, avoid redundant builds and matrices,
  and do not add nonessential required checks. Exploratory measurements can remain outside CI.


### docs/00_usage.md (excerpt)
# Using agit

A guide for users, organized by **what you want to do** rather than as a command table. Every
section can be typed as written.

Written against `agit 0.9.0` (`agit --version` tells you which one you have). The full flag list
is in `agit <command> --help`; this document covers only the part you reach for most.

## 1. The mental model first

```
agent   = a git repo       lives in ~/.agit/repos/<owner>/<name>
branch  = one session      once a session occupies a branch, that branch never changes hands
commit  = one user turn    you ask, the agent finishes answering: that is one commit
main    = the file line    AGENTS.md, memory/, skills/ — what sessions share
```

This is not a metaphor; underneath it is a real git repo. `agit log` is the history from the
session's point of view, `agit repo path` prints the repo path, and `git log` inside it shows the
same commits.

Two words recur below:

- **settle**: cut "the conversation added since the last record" into turn commits. The command is
  `agit commit`.
- **VIEW**: the context the agent really sees on the next resume. It is derived — when
  `agit revert` takes something out of it, the original record (the log) does not move a byte.

### Select a repository and ref

Use a full target such as `alice/payments@work`, or set
`AGIT_SESSION=alice/payments@work` before using a local ref such as `work` or `main`.
A workspace binding does not select an existing session for these commands.

For an ordinary explicit ref, a missing local branch can resolve to a single matching
remote-tracking branch. Several remotes carrying that name are ambiguous; a local branch
keeps its identity even when its remote counterpart has advanced. A same-named tag or
another matching object can still make an ordinary explicit ref ambiguous.

`@` selects the exact local session branch in `AGIT_SESSION`. If that local branch is missing,
it refuses instead of selecting a tag, remote-tracking ref, or checkout HEAD. Historical
selectors such as `@#2` are applied after capturing that local branch's tip.

Human command results begin with the verified target and how it was selected:

```text
target: alice/payments@work (via AGIT_SESSION)
```

Fully qualified arguments report `explicit arguments`; a local ref whose repository comes
from the environment reports `explicit arguments + AGIT_SESSION`. An explicit picker choice
reports `interactive selection`. Changing directories with `-C` does not select a session.
An unresolved target never receives a notice. Startup diagnostics and
acquisition progress can appear on stderr before the result.

| Output | Target notice |
| --- | --- |
| `commit`, ordinary `log`/`show`/`view`, tag creation, `fork`/`run`/`resume`, memory status/sync | Verified session, branch, native session identity, or immutable history point |
| Branch and tag lists, `log --branches`/`--graph`, selected-repository fetch, repository-wide pull, `scan` | Repository scope; scan covers the repository publish surface even when refs were supplied |
| Branch/tag mutations, selected-branch push/pull | Actual selected refs; push labels the local source refs |
| `diff`, `merge`, `cherry-pick`, `revert` | Labeled endpoints or target and sources on the same line; transaction sources are identified as recorded state |
| `memory distill`, `distill` | Validated source branch and `main` destination |
| File export, PR creation | Validated source; exported bytes and the remote request remain separate from the human result |

JSON envelopes, quiet mode, active full-screen interfaces, hooks and MCP do not receive a new
human target notice. The existing byte outputs of `show --raw`, `show ref:path`, `show ref#n.k`,
stdout export, `diff --files`, working-state `diff`, `memory diff`, and `repo path` stay unchanged.
Global listings, status, search, `fetch --all`, repository administration, and creation/adoption
commands have their own scope or identity reports rather than an implicit session notice.
For merge transaction controls, `recorded-from` describes the source stored in that transaction;
`commit:<sha>` means its repository namespace was not recorded and is not inferred.

## 2. Getting started

### 2.1 Install

```sh
npm install -g @einsia/agent-git     # prebuilt binary, no Rust toolchain required
agit --version
```

People changing the code install from source:
`git clone https://github.com/Einsia/agent-git && cd agent-git && ./setup.sh`. Both paths install
the same binary.

You also need **git >= 2.28** (repo init uses `git init --initial-branch`). The rest of the
details (musl static linking on Linux, environment variables, platform sub-packages) are in
[`01_setup.md`](01_setup.md) and [`../npm/README.md`](../npm/README.md).

> Do not install `@einsia/agentgit` (no hyphen) — that is the pre-rewrite CLI; its protocol does
> not match.

### 2.2 Sign in

```sh
agit login
```

On a TTY it asks whether to authorize in the browser or use a device code. Where there is no TTY
but someone is watching the output — a container, say — `agit login --device` skips the menu and
goes straight to the device code (it prints a short code you confirm on another device). Fully
unattended CI and agent subprocesses have one path:

```sh
agit login --with-token < token.txt
```

Signing in is not only for push. **Settlement needs an account name**: the commit author and the
`<owner>/` of the repo path both come from the credentials, and neither can be filled in
afterwards. Without a sign-in, `agit commit` refuses outright.

To mark a session offline first, use the `--link-only` of 3.1 below.

### 2.3 Wire up the runtimes (once; after that, forget it)

```sh
agit setup
```

It configures the following integrations. Repeating setup updates existing managed entries:

| What        | Where                                              | Effect                                                       |
| ----------- | -------------------------------------------------- | ------------------------------------------------------------ |
| hooks       | `~/.claude/settings.json`, `$CODEX_HOME/hooks.json` | SessionStart registers the session, Stop settles a turn automatically |
| skill       | `~/.claude/skills/agit/`, `$CODEX_HOME/skills/agit/`, and so on | teaches the agent the `agit commit --milestone` discipline |
| MCP         | each runtime's MCP config                          | the agent can `search` / `show` other people's sessions directly |
| AGENTS.md   | the current project                                | the project-level rules block                                |

Name the one runtime you use, so no config is written for tools you do not have:

```sh
agit setup --runtime claude-code
agit setup --runtime codex --hooks
cd ~/Projects/payments && agit setup --agents-md     # install just the project-level block
```

With hooks installed, Claude Code and a hook-capable Codex **settle once every time a turn
completes**, and day to day you never type `agit commit`. Manual settlement stays useful — see the
milestones in 3.2.

Codex hook installation is capability-gated by `codex features list`; unsupported installations
are left untouched. Codex treats user hooks as untrusted until they are reviewed, so it may ask for
approval before first use or after the installed command changes. OpenCode and Cursor have no
equivalent "turn finished" callback; the skill above injects the settlement discipline into the
agent, and the agent types `agit commit` itself at the right moment.

`agit setup --agents-md` refreshes the managed section and normalizes nested AgentGit markers,
preserving the text around that section. An unchanged repeat does not append another marker pair.

### 2.4 Create an agent repo inside a project

```sh
cd ~/Projects/payments
agit init payments
```

At a terminal, bare `agit init` opens the same operation as a full-screen wizard: type the repo
name, choose whether to bind this directory, and optionally review seed assets. Seed choices start
empty and the screen closes before the existing init path writes anything. Explicit arguments,
pipes, CI and agent sessions keep the command-line behavior.

```
✓ repo created: alice/payments (main is the file line; scaffolding in ~/.agit/repos/alice/payments)
  bound to this directory. Next:
    agit import          adopt a running session (settles on import)
    agit new -b <name>   start a fresh session (inherits memory/skills)
```

`--seed` finds the AGENTS.md / CLAUDE.md / `.claude/skills/` already in the project and collects
them into main **after asking you item by item**. With no TTY it collects nothing (personal memory
can hold private material, and it is never collected silently); `-y` takes everything.

**`agit init` writes no file into your code repo.** The binding between the directory and the
agent is recorded under `~/.agit/workspaces/`. (The only things that touch project files are the
AGENTS.md block from `agit setup`, and the `agit commit --code` you ask for explicitly in 3.2.)

## 3. The everyday path

A fictional project `payments` ties the rest together. The output fragments are real runs.

### 3.1 Put a running session under version control

The most common starting point: you have done a stretch of work in Claude Code and want that
conversation to have a history.

```sh
cd ~/Projects/payments
agit import                       # no argument: lists the unadopted sessions in this directory
```

At a terminal, the zero-argument form opens a full-screen candidate list. Pick a session, choose
the destination repo with `Tab`, type a new branch, or press `l` for the offline `--link-only`
path. The screen closes before lineage selection or the ordinary import command writes anything.
Pipes, CI and agent sessions list explicit choices and leave local state unchanged.

With a full native ID, runtime and destination, inspect and choose the lineage:

```sh
agit import 7f3a1c2e-1111-4a4a-8b8b-000000000001 --from claude-code --into alice/payments@ratelimit
```

The terminal offers verified local prefix candidates, an independent import, and cancellation.
A single candidate still requires a choice. Noninteractive calls return the choices and exit
without adopting; `--onto <ref>` selects a base and `--independent` explicitly starts a separate
line. `--propose-lineage` prints the same local evidence without applying a choice. Semantic
comparison is unavailable, so a missing verified prefix does not prove unrelated history.

After accepting an independent import, the session's turns are recorded:

```
✓ adopted claude-code 7f3a1c2e-111
working dir  unknown (filled in when a version is recorded)
link         ~/.agit/store/claude-code/7f3a1c2e-1111-4a4a-8b8b-000000000001.json

#1 a37029959 add a per-user_id rate limit to payments
#2 21d8a51ff add a test for it

✓ settled 2 turns → alice/payments @ ratelimit
```

Select that branch explicitly for subsequent commands in this terminal:

```sh
export AGIT_SESSION=alice/payments@ratelimit
```

`agit import` cannot change its parent shell's environment. Keep this selection while following
the commands below, or supply `alice/payments@ratelimit` directly to each session command.

Adopting and recording the first version are **one command** — the in-between state ("linked, but
unversioned") means nothing to anyone.

A fresh claim needs an explicit destination repo and session branch. Use
`--into alice/payments@ratelimit`, or `--repo alice/payments -b ratelimit`.
The compatibility `-n <agent>` form names a repo for an explicit independent/base import and
still needs `-b <branch>`; read-only lineage discovery requires the qualified destination.
Session turns cannot land on `main`, which is the file line. Use `--from codex` or
`--from claude-code` to name the source runtime; the option is named `--from`, not `--runtime`.

import **does not copy** the transcript; it writes a link. The original session keeps growing and
the link keeps pointing at it.

**Offline** (on a plane, not signed in yet):

```sh
agit import 7f3a1c2e --link-only    # mark it only, record no version
# back online: choose lineage before recording the first version
agit import 7f3a1c2e-1111-4a4a-8b8b-000000000001 --from claude-code --into alice/payments@ratelimit
```

The offline link has no repository owner or branch claim. The explicit import target establishes
that identity before recording; `agit commit` cannot infer it from the account you sign in to.

**To show it to outsiders**, redact first: `--privacy` adopts a washed copy (secrets become
`[redacted:<rule>]`; home directory, user name and host name become stable pseudonyms), and not
one byte of the original enters history. claude-code only; other runtimes use
`agit export --redact`.

The copy is **frozen** and carries its own new session id: the original session keeps growing, the
copy does not follow. To publish later conversation, run
`agit import <id> --privacy --into alice/payments@<new-branch> --independent` again — every run is a new frozen copy, and the old
branch, already taken by the old copy, is never refreshed.

### 3.2 Settle: get new conversation into history

With hooks installed this step is automatic. Three occasions call for typing it by hand.

**a. Land it every so often**

```sh
agit commit
```

```
target: alice/payments@ratelimit (via AGIT_SESSION)
#3 6b2bb67d8 make the rate-limit threshold configurable

✓ settled 1 turns → alice/payments @ ratelimit
  next: agit push to publish · agit log to read history
```

One turn is one commit, and the message is that turn's user prompt (squashed to one line,
truncated when too long). A trailing turn that has not ended stays for next time — the question is
there but the agent has not answered, or a tool call the agent made has not returned yet (when the
agent runs `agit commit` from inside a turn, that call is the open one). It says so:
`the current turn is still in flight`. The turn lands on the next `agit commit` after the turn
ends (the Stop hook does this), and another `agit push` is what puts it on the Hub. With nothing
new it prints `nothing new since ...` and exits normally; that is not an error.

**b. A phase is done: mark a milestone**

```sh
agit commit --milestone "rate limiting done, tests pass" --tag ms-ratelimit --code
```

- `--milestone` writes a one-line phase summary into the last turn commit; `agit log` shows it
  as ★.
- `--tag` tags it while you are there.
- `--code` also commits in the **code repo** of the directory you run it in (not the directory
  the session was started from), on whatever branch that checkout has checked out, and writes the
  `origin@sha` cross anchor into this turn. It stages tracked changes only, plus whatever you have
  already staged; it really commits only when that leaves something to commit, and on a clean
  tree it records the current HEAD as the anchor. If the checkout has untracked files, it refuses
  and lists them: `git add` the ones that belong to the work, remove or ignore the rest, and run
  it again. The code repo must already have an `origin` remote; when cwd is not a Git repo,
  `--code` warns and skips the code-side commit, and the session turn still settles normally.

This one is for "whoever reads the log later and wants to know how far it got". Automatic
settlement does not write it for you.

One precondition: all three flags **attach only to the new turns this settlement produces**. With
no new turn pending, the whole command is a no-op (it prints `nothing new since ...`, exits
normally, and lands neither the ★ nor the tag nor the anchor). So with hooks installed, have the
agent type this inside the session — while the Stop hook has not settled that turn yet; typing it
in the terminal afterwards cannot catch up.

**c. Only shared files changed**

```sh
cd $(agit repo path)          # into the agent repo's main checkout (the main file line): edit memory/ skills/ AGENTS.md directly
                              # a session branch's copy lives in its own worktree: agit repo path <owner/repo>@<branch>
cd -                          # back to the project directory to settle: context resolves against the project directory, never inside the agent repo
agit commit -m "memory: conclusions on the refund path"
```

`-m` is a file-only commit, legal only when **no new conversation is pending settlement**. With
new turns it refuses; run `agit commit` first.

### 3.3 Look back

```sh
agit log
```

**Typed in front of a terminal, this opens the full-screen interface**, not the text below: a
timeline ordered by turn, `Tab` switches to the branch view, Enter reads that turn's conversation.
In a pipe, in CI and inside an agent session it stays text; to get text in a terminal too, add
`--no-tui`. The tests and the other screens are in [`docs/07_tui.md`](07_tui.md).

Here is the text form:

```
#  1 acdd8307e [file ] agit: init (main file line)
#  2 82eb408cb [file ] agit: claim session line ratelimit
#  1 a37029959 [turn ] add a per-user_id rate limit to payments
#  2 21d8a51ff [turn ] add a test for it
#  3 6b2bb67d8 [turn ] make the rate-limit threshold configurable
#  4 2f5f1a3a6 [turn ] make the error code configurable too  ⌂ ms-ratelimit
      code https://github.com/alice/payments.git@3d0fac3
      ★ rate limiting done, tests pass
```

That last turn is what the settlement in 3.2b produced: `⌂` is the tag, `★` is the milestone, and
`code` is the code anchor `--code` recorded.

Common combinations:

```sh
agit log --oneline -n 50            # one line per turn
agit log --kind turn                # conversation only, without file commits like repo creation and claims
agit log --grep rate --since 7d     # message substring + time
agit log --graph                    # the structure when there are several branches
agit log -- memory/notes.md         # only commits that touched this shared file
```

**Read the conversation itself**:

```sh
agit show                                   # the branch explicitly selected by AGIT_SESSION
agit show 7f3a                              # by session id prefix — this one is exact
agit show alice/payments@ratelimit          # the VIEW of one branch of one repo (the world resume sees)
agit show 'ratelimit#5.1'                   # the 1st event the 5th commit added, raw JSON
agit show 'ratelimit:AGENTS.md'             # a shared file's contents at that point
agit show --agent alice/payments --tui      # full-screen browsing
```

Mind the quotes: `#` starts a comment in the shell, so always quote a reference carrying a `#`.

**Compare two points**:

```sh
agit diff main..ratelimit                   # fork point + which turns each side added (the default)
agit diff --view 'ratelimit#3..ratelimit'   # insertions / deletions in the VIEW sequence
agit diff --files v0.1..ratelimit           # text diff of the shared files
agit diff                                   # no range: what is still unsettled in the workspace
```

With unrelated Git histories, `diff --turns` and merge reconnaissance also report a
**semantic prefix** and each side's remaining normalized LOG turns. This comparison
uses the full saved LOG even when VIEW has been compacted or edited. Its turn ordinals
are content positions, not `#n` commit selectors. A semantic hash is never a Git merge
base, and it does not change merge parents or the endpoints used by `--view` and `--files`.

Semantic comparison uses the shared runtime IR: it excludes timestamps, runtime identity,
path metadata, tool results, compaction and unmodeled content. Tool details depend on what
the native adapter represents. Matching hashes therefore do not establish complete
transcript equality. An endpoint without comparable user turns is reported as unavailable.

**See what the VIEW is made of** (the scouting command before a merge):

```sh
agit view ratelimit
```

```
  VIEW @ ratelimit (8 events)
     0    log#0 user           488B this branch            add a per-user_id rate limit to payme

### docs/01_setup.md
# Build and run

The backend is a pure JSON API with no web interface — `GET /` is a 404. Check
its state with curl or `agit doctor`.

## Install the CLI

Several paths, the same binary either way:

| Who                      | How                                                          | Notes                                               |
| ------------------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| Users (one-shot)         | `npx -y create-agit@latest`                                  | one-shot install to `~/.local/bin/agit`, then setup |
| Users (global)           | `npm install -g @einsia/agent-git`                           | prebuilt binary, no Rust toolchain needed           |
| People changing the code | `./setup.sh`                                                 | builds from source, installs to `~/.local/bin/agit` |

pnpm (since v10) does not run a dependency's install
scripts by default, so the automatic `agit setup` is skipped — run it once by
hand after installing. What the npm package itself does is in
[`../npm/README.md`](../npm/README.md).

Do not install `@einsia/agentgit` (no hyphen) — that is a different CLI from
before the rewrite, and its protocol does not match this branch.

Prebuilt distribution binaries include Git and Git LFS. The CLI extracts its private
runtime under `$AGIT_HOME/git-runtime` (by default `~/.agit/git-runtime`) on first
use, without downloading additional files. Your shell PATH and global Git profile
are unchanged. User and repository Git configuration still apply; AgentGit's own
repository settings continue to control its internal commits and LFS filters.

Source builds use system Git by default and require **Git >= 2.28**; lineage
inspection needs Git >= 2.36 and LFS operations need **Git LFS >= 3.7.1**.
`AGIT_USE_SYSTEM_GIT=1` also selects system Git in a distribution build, including
when a custom credential helper or extension requires your local Git installation.
Run `agit doctor` to see the selected Git and LFS versions. See
[the bundled runtime guide](bundled-git.md) for packaging and cache details.

### The Linux artifact is musl-static

On Linux the npm path downloads `*-unknown-linux-musl`, not gnu. The reason is a
real incident: a gnu artifact turns the **build machine's** glibc version into a
runtime floor, and the user gets `libc.so.6: version 'GLIBC_2.38' not found`
straight after installing. GitHub's ubuntu-latest is now 24.04 (glibc 2.39), and
the gnu artifact built there starts on none of Debian 12, Ubuntu 22.04,
Debian 11, Amazon Linux 2.

The musl artifact is static-pie with no glibc floor: every environment above
plus Alpine runs it. Before building the Release, the release pipeline puts
every Linux artifact into an alpine / amazonlinux / debian / ubuntu container
matrix and actually runs it there (the smoke-test step of `release.yml`).

The embedded Linux Git runtime carries its own musl loader and shared libraries.
It invokes that loader explicitly and uses the host's `/bin/sh`, so Git does not
introduce a host glibc requirement into the static CLI distribution.

`setup.sh` checks the toolchain before building; when something is missing it
tells you which command to type instead of an error from deep inside cargo. For
manual control, read on.

## Build

Needs **`cargo >= 1.88`** and a C compiler.

The two floors come from different places and are not the same number: edition
2024 itself only needs 1.85, but in the committed `Cargo.lock`, `darling 0.23`
and `instability 0.3.12` (a ratatui dependency) declare `rust-version = 1.88`,
so the real floor is 1.88. (1.78 is wrong — edition 2024 does not compile on it
at all.) The C compiler is what `rusqlite`'s `bundled` feature needs: it
compiles sqlite's C source into the binary, so the target machine does not need
sqlite installed.

rustup installs into `~/.cargo/bin`; when that is not on PATH, `source
~/.cargo/env` first.

```bash
(pushd AgentGit-backend && cargo build --release && popd)   # agentgit-backend + agentgit-admin
(pushd agent-git        && cargo build --release && popd)   # agit
```

Run the tests: `cargo test` (69 in the backend), `cargo test --lib` (166 in the
CLI). Without `--lib` the CLI suite times out on this NFS machine.

## Run the backend

Zero configuration:

```bash
./AgentGit-backend/target/release/agentgit-backend
# INFO AgentGit backend started addr=127.0.0.1:8177 root=~/.agentgit-backend
```

The sqlite database and the bare git repos both live in `~/.agentgit-backend`
(0700), and the tables are created at startup. `AGIT_BACKEND_ROOT` /
`AGIT_BACKEND_PORT` change the location and the port.

```bash
curl -s http://127.0.0.1:8177/api/health
# {"status":"ok","version":"0.1.0"}
```

Binding a non-loopback address is refused unless `--insecure` is passed
explicitly — this backend holds every session transcript the team has, and
without TLS both tokens and transcripts cross the network in the clear. In
production, put a reverse proxy in front to terminate TLS.

## Create an account

Self-service registration is open by default: `/signup` in the web interface
creates an account, or call the API directly:

```bash
curl -s -X POST http://127.0.0.1:8177/api/auth/register \
  -H 'content-type: application/json' \
  -d '{"username":"alice","password":"your-long-password"}'
# returns a token pair; registering signs you in
```

On an instance with self-service registration off
(`AGIT_BACKEND_OPEN_REGISTRATION=false`), an administrator creates the accounts.
The password is read from the terminal, never from argv:

```bash
./AgentGit-backend/target/release/agentgit-admin user-add alice
# set a password:
# repeat it:
# created account alice

./AgentGit-backend/target/release/agentgit-admin user-list
```

The only password rule is length ≥10.

With no tty (`docker exec -i`, a pipe) it prints `stty: Inappropriate ioctl for
device`. That is noise; the account is still created correctly. In a script,
pipe the password in twice:

```bash
printf 'your-long-password\nyour-long-password\n' \
  | ./target/release/agentgit-admin user-add alice 2>/dev/null
```

## login / logout

The CLI connects to the public hub `https://agent-git.com` by default, so `agit
login` works as soon as it is installed.

This document covers a self-hosted instance, so point every example below at the
one you started yourself first:

```bash
export AGIT_HUB_URL=http://127.0.0.1:8177
```

For an acceptance binary that defaults to staging without depending on a runtime
environment variable:

```bash
AGIT_DEFAULT_HUB_URL=https://staging.agent-git.com cargo build --release --locked
```

Credentials are stored per address, so the public hub and a self-hosted instance
each stay signed in; switching the environment variable switches identity.

```bash
agit login              # authorize through the browser or choose device code

agit doctor --check-backend
#   [✓] sign-in          alice @ http://127.0.0.1:8177
#   [✓] backend          ok @ http://127.0.0.1:8177 (version 0.1.0)

agit logout             # revokes the server session + deletes local credentials, not the store
```

Signing in returns a token pair, stored under `$AGIT_HOME/credentials/` (default
`~/.agit/credentials/`). The CLI chooses the filename and binds its contents to
the selected Hub authority. Unix files are private to their owner; Windows
files use the current user's private access control list. The credential scope,
refresh behavior, and compatibility rules are in
[`commands/auth.md`](commands/auth.md).

CI uses a PAT supplied through stdin. Save the PAT as a secret file in the CI
runner, then let the CLI validate and store the session:

```bash
export AGIT_HOME=/tmp/agit-ci AGIT_HUB_URL=http://127.0.0.1:8177
agit login --with-token < token.txt
agit whoami --check
```

Do not construct credential filenames or hand-write token JSON. Records without
a valid Hub address cannot establish which destination may receive their tokens.

## Troubleshooting

For owner-controlled-state or ancestor-permission failures after using a shared
shell umask, see [bounded local permission recovery](state-permissions.md).

| Symptom | Cause |
|---|---|
| `cannot connect to the backend ...` | the backend is not running, or `AGIT_HUB_URL` has the wrong port |
| `the backend refused authentication (401)` | the refresh token expired too (thirty days); log in again |
| `wrong account or password` | wrong password, or no such account — the wording deliberately does not distinguish, to block account enumeration |
| `GET /` returns 404 | expected; there is no web interface |
| `stty: Inappropriate ioctl` | noise; the account is still created |

```bash
agentgit-admin doctor        # account / agent / session counts + repo disk use
agentgit-admin audit -n 20   # audit records
```

An unauthenticated `/api/agents` returns 200 and an empty list rather than 401:
an anonymous caller can see public agents. A private agent the caller cannot
reach returns 404 rather than 403; otherwise agent names could be enumerated.


### docs/02_session_store.md (excerpt)
# Sessions, snapshots, versions

The mechanism told along one complete use: install the CLI → sign in → adopt a
session → record a version → publish → someone else picks it up.

## 1. `agit login`

The only prerequisite step, and a hard precondition for recording a
version — `agit import` and `agit commit` both count.

```bash
agit login
```

It puts a token pair in `~/.agit/credentials/<authority-key>.json` (0600): access lasts an hour,
refresh lasts thirty days. Once access expires the client swaps in a new one and
retries, so one sign-in lasts a month.

Recording a version requires signing in first, because a commit records **who
recorded it** (git's `user.name` / `user.email`, taken from the sign-in
credentials), and the agent repo path is `~/.agit/repos/<owner>/<name>/` — both
need the account name, and neither can be filled in afterwards.

`agit import` records the first version by default, so it needs a sign-in too.
To mark a session down where there is no network, use
`agit import <session> --link-only`: that path writes only the link, stays
usable offline. After sign-in, `agit import <session> --into <owner/repo>@<branch>`
records the opening version with explicit ownership. `log` / `show` /
`status` / `doctor` stay offline as always.

There is no other installation step. agit writes nothing into
`~/.claude/settings.json` or `~/.codex/config.toml`, installs no hooks and runs
nothing in the background — it works only while you are typing a command.

The cost is that **adoption is explicit**: a finished session does not enter
version control by itself; `agit import` has to name it.

## 2. Disk layout

The default storage root is `~/.agit`; `AGIT_HOME` can select another root.
Credential filenames are derived from the normalized Hub authority. They are
opaque keys, and each credential record is bound to that Hub. Use `agit login`
and `agit logout` to manage them rather than copying a token file between Hubs.

```text
~/.agit/
  credentials/<authority-key>.json     token pair and account identity, per Hub (0600)
  store/<runtime>/<session-id>.json    the local session link
  repos/<owner>/<name>/               the Agent repository
```

Two levels, not three. A middle level `drafts/<agent>/` — `agit commit`
materializing the content there, `agit push` copying it into the repo and then
**deleting the draft** — produces two bugs: the next commit loses its comparison
baseline, and the hint "rerun agit push if the tag did not get pushed" cannot be
carried out, because what has to be re-pushed is already deleted. `commit`
writes straight into the agent repo and makes one git commit, `push` is
`git push`, and both bugs are structurally impossible.

### store: links only

One session corresponds to one concrete rollout entry in the runtime:

| Runtime | Transcript file | Reverse lookup |
|---|---|---|
| Codex | `~/.codex/sessions/YYYY/MM/DD/rollout-<ISO>-<uuid>.jsonl` | the `threads` table of `~/.codex/state_<N>.sqlite`, 0.40 ms |
| Claude Code | `~/.claude/projects/<cwd-slug>/<uuid>.jsonl` | one glob level, `projects/*/<id>.jsonl`, 2.2 ms |

`agit import <session-id> --from claude-code --into nana/opd@topic` adopts the
native session and records its initial version. Its local link lives at:

```text
~/.agit/store/claude-code/db57fdab-….json
```

```json
{
  "cwd": "/Users/nana/Projects/OpenPad",
  "agent": "opd",
  "owner": "nana",
  "branch": "topic"
}
```

This example shows the local route. The runtime and session id come from the
path and are not repeated in the JSON body; absent optional fields are omitted.

* `cwd` records the native session's project directory.
* `owner`, `agent` and `branch` identify its local repository claim. A session
  adopted with `--link-only` can remain unclaimed. Ordinary commands select an
  existing session through explicit arguments or `AGIT_SESSION`; a saved link
  does not authorize guessing a command target.
* Materialization and settlement can also persist `baseline_bytes`,
  `baseline_hash` and `materialized_from` to distinguish saved context from
  later native work. Supersession, merge-archive roles and naming state have
  separate optional fields; superseded or archive links are not active claims.

Import adopts an existing runtime session; resume/run and a resumed fork can
record a newly materialized instance, and commit updates its settlement state.
Clone only fetches repository history and optionally binds the workspace. It
does not create a runtime session link. These instance records remain local;
the repository's Git history carries the shared lineage.

The store keeps no copy of the transcript. Transcript files do not disappear
(observed over the 18779 `rollout_path` rows of the `threads` table, with the
most recent 400 and the oldest 200 sampled and none missing), while copies would
cost 11.2 GB (18858 sessions on this machine).

One file per session rather than a single `links.json`: writes can fire
concurrently (two sessions open at once), and one file per session removes the
read-modify-write race.

### An operation that scales with the session count must not open transcripts

Reading session state = opening the transcript + parsing the whole JSON. Parsing
one 3 MB session takes 6.8 ms and listing 18810 sessions takes 390 ms — **the
cost is in the multiplication by the session count, not in one parse**. The rule
is drawn there:

| Command | Reads transcripts | Count depends on |
|---|---|---|
| `agit log` / `status` | no | the number of adopted sessions |
| `agit import` finding candidates | no | the number of sessions under this directory |
| `agit commit` | **yes, once** | one |
| `agit import -n <agent>` recording the first version | **yes, once** | one (the same code as above) |
| `agit log <session>` | yes | the one the user named |
| `agit doctor` | yes | every agent repo on this machine + the adopted live transcripts |

The rule is not "session state is read in full only at `agit commit`, so
`import` never touches a transcript". The first half holds — recording one
version is one read; the second half attaches the reason to the wrong object:
what `import` parses after the selection is **that one** session, the same cost
as `commit` parsing it, and it does not change with 18858 sessions on disk or
with 3. So that cost is affordable and worth paying — the user wants "this
session is in version control", not "half of it is".

The one exception is `agit import`'s interactive list: Claude Code has no index
of the opening prompt, and showing it means reading the file. The scope is
pinned to "unadopted candidates under the current directory", and with a single
candidate there is nothing to ask and so nothing to read.

## 3. Snapshot = version

**Recording a version is an explicit action.** It covers everything in the
transcript at that moment. The first version is recorded by `agit import` along
the way, every later one by `agit commit`:

```bash
agit import db57fdab -n opd     # adopt + first version
agit commit opd                 # after more work, record another
```

```
✓ adopted claude-code db57fdab-2f3
  cwd      ~/Projects/OpenPad
  link     ~/.agit/store/claude-code/db57fdab-….json

✓ recorded db57fdab-2f3 → nana/pad
  version  agit-21fc4fdc111ed596a78771f54f45f7a6004d9d5d
  session  agit-a1b2c3d4… (this branch's first snapshot claimed it)
  turns    3
  code     git@github.com:nana/OpenPad.git@1839e61
  repo     ~/.agit/repos/nana/pad
  created the local repo for nana/pad; `agit push` creates it on the hub

  `agit push opd` publishes
```

Why the name has to be given: an automatically chosen agent name silently
decides which lineage this memory lands on, and that kind of mistake is not
noticed right away. A missing name is therefore an error, not "pick one at
random" — the error message carries a suggestion computed from the working
directory name, but typing it stays the user's own step.

### id

```text
snapshot id = "agit-" + <the git commit SHA-1 of this snapshot>
```

A git commit hash is already a content address: it covers the whole
parent → tree → blobs tree, any changed byte yields another id, and the id is
the git tag, which cannot be edited. No second hash layer is
needed — `SHA256(parent ‖ cwd ‖ transcript bytes)` only repeats what git already
does.

The `agit-` prefix has two uses: telling one from a bare git SHA at a glance;
and in `agit clone x/y@Z` a `Z` that starts with it is a version, otherwise a
branch name (so a branch name must not start with `agit-`; an agent name is not
in that position and is not restricted). A hyphen, not an underscore — `agit_`
+ 64 hex hits the backend secret rule `\bagit_[0-9a-f]{64}\b`.

The id exists only after the commit, so the commit message does not contain it;
the tag is applied after the commit, so its name is right by construction.

### Why a version is not taken from the last closed turn

Under the rule "a version = the hash of the last **closed** turn", a turn closes
only when the person speaks again. The last turn — often exactly the most
valuable stretch of work — then never reaches a version. Codex barely holds it
up with `event_msg/task_complete`; **Claude Code has no equivalent signal at
all** (its `system/turn_duration` does not line up with the human turn count:
22 turns against 48 records, 33 turns against 27, and it fires for interrupts
and system turns too).

The root cause is binding the version to the session structure. Bound to the
author instead, the open-turn / closed-turn distinction and everything built to
work around that asymmetry are gone together. `EventKind::TurnEnd` stays in the
IR (rendering skips it, and activity statistics must not count it as a reply),
but it decides nothing about a version.

### session/meta.json

Under `session/`, **one per git commit, overwritten in place** — git stores the
history, and accumulating would only produce two records that can disagree. The
only place that produces it is `meta::write`.

```json
{
  "line":    "session",
  "session": "agit-a1b2c3d4…",
  "runtime": "claude-code",
  "cwd":     "/Users/nana/Projects/OpenPad",
  "code":    "git@github.com:nana/OpenPad.git@1839e61",
  "kind":    "turn",
  "turn":    3
}
```

`line` is the **branch form**, fixed at birth and never converted: a `session`
line is bound to one session for life, a `file` line never claims a session (it
takes only shared-file commits). It is written down, not inferred from "does the
tree have session files" — the inference has a fatal overlap: a session line
just created, with its first turn not yet settled, equally "has commits and no
session files", and is rejected as a file line.

Every invariant is guarded by `meta::validate` (the persist path and the
tree-building path share it):

* A file line carrying `session` contradicts its own form; refused outright.
* A session line's `session` may be empty — that is the **birth state**: the
  identity takes `hash(cwd + transcript bytes)` to compute, and creating the
  branch precedes settling the first turn.
* Once the identity is claimed, `runtime` is mandatory: the envelope's `_source`
  and the VIEW slicing (§4) both resolve through it, and once it is empty
  nothing else can supply it.

`code` exists only when the cwd is a git repo, shaped `<origin>@<short-sha>`;
`cwd_state` is a bounded workspace summary collected at the same moment, for
example:

```json
{
  "origin": "git@github.com:nana/OpenPad.git",
  "head": "1839e61…",
  "branch": "main",
  "worktree": "dirty",
  "staged": 1,
  "unstaged": 2,
  "untracked": 1,
  "conflicted": 0,
  "status_digest": "…"
}
```

It contains no paths, no diffs and no file contents, so the size of the state
body does not grow with the number of files in the workspace; with no origin,
HEAD or branch the corresponding fields are empty, and `worktree` is `unknown`
when the status check cannot be run safely. `cwd_state` is an optional extension
field; a `code_state` written by an older version is read as the same field,
while new writes uniformly use `cwd_state`: an old commit without it is still
read under the original schema and no history migration is required. The backend
parses only the known fields the binding needs and ignores unknown ones, so
adding it changes neither the HTTP interface nor the push protocol.

When one settlement lands several turns at once, only the last turn carries the
`cwd_state` collected during that settlement; earlier turns cannot have the
state at the time they actually happened inferred back from the current
workspace, so they keep the default value rather than passing the current state
off as a historical fact.

`kind` is the kind of this commit (`turn` / `merge` / `view` / `file` / `archive`), and
`turn` is the turn ordinal. Empty fields are never serialized — making "no
identity" look like "the identity is the empty string" gives downstream one more
state to tell apart.

An `archive` snapshot retains additional native evidence in LOG without changing VIEW,
shared files, the logical session identity, or the completed-turn ordinal. It is a
session-line operation, never a file-line operation. Archive entries have no `#n`
turn label and remain selectable by their commit ID. Reader support alone does not
make a runtime produce these snapshots.

The `archive` kind extends a closed metadata enum. CLI releases whose readers do
not recognize it cannot read a history containing it and must be upgraded; adding
the reader does not rewrite any existing snapshot or change the storage layout.
The legacy `snapshot.json` format does not acquire this kind.

`session` is this branch's session identity (one session per branch, see
`docs/03_branch_model.md`): the root snapshot claims it with a content hash —

```text
session = "agit-" + hex(SHA-256(cwd ‖ 0x00 ‖ transcript bytes))[..40]
```

The root snapshot's own commit SHA cannot be computed before the commit (the
tree it covers contains `session/meta.json` itself), and the claim has to be
finished at the moment the file is written, so this value — stable over the same
content — stands in first. Later snapshots inherit from the tip and never
recompute; when the two disagree, HEAD's blob wins — the binding lives in the
history, and the workspace copy is only a mirror.

Fields deliberately **absent**:

| Dropped | Why |
|---|---|
| `parent` | a git commit records its parent itself; a snapshot does not repeat that layer |
| `signer` / `key` / `sig` | the signing mechanism is gone entirely — the id is the commit SHA, content integrity is git's guarantee; the author is recorded by git's `user.name` / `user.email` |
| `version` | that is the snapshot id (= the commit SHA), self-referential |
| `captured_at` / `signed_at` | an unverifiable self-report; for time, ask the git commit |
| the runtime's local session id | a local identifier for "this machine, this installation"; recording it only tempts someone to use it as a durable identity |

**The id is not written in either**: it is the SHA of the commit around it.
Validation = whether the tag name equals the SHA of the commit it points
at — this is how the server-side gate ④·layout judges it (see
`docs/03_branch_model.md` §4). The local half takes another shape: the commit
SHA is itself the content address, so doctor needs no machine tag to prove it
(§8, check 1).

## 4. Envelopes and the v1 LOG / VIEW sequences

Current snapshots declare `"layout": "v1"` in `session/meta.json`. The physical
paths are defined by `domain::meta`; `domain::storage` materializes their logical
envelope streams for readers:

```text
session/meta.json          session metadata and the storage layout declaration
LOG                        full ordered sequence of event ids, one id per line
VIEW                       ordered resume selection of event ids, one id per line
events/a/b/c/d/<event-id>   one canonical envelope and its trailing LF
```

An event id is a lowercase hex content address of the complete envelope,
including its source, session identity and trailing LF. Its first characters
select the shard directories; the complete id remains the filename. It is
distinct from `_object_hash`, which addresses only the envelope's `content`.
The managed `.gitattributes` rules preserve the bytes of `LOG`, `VIEW` and
`events/**`. Shared `AGENTS.md`, `memory/` and `skills/` remain separate content.

Historical **v0** snapshots instead store complete envelope JSONL in
`session/log.jsonl` and `session/VIEW`. A missing `layout` field means v0;
readers use the metadata declaration rather than guessing from filenames.
Those paths remain compatibility inputs for history and migration, not the
physical layout written by current snapshots.

`VIEW` has no extension because it is an ordered selection, not a second
transcript. The capture discussion below describes the logical envelope
streams after materialization, independently of their v0 or v1 storage.

### Event objects materialize into envelope lines

```json
{"_source":"claude-code","_session_id":"agit-…","_object_hash":"…","content":{…the original line…}}
```

Four keys, and **the field declaration order is the wire byte order** (serde
serializes in declaration order; the test `envelope_wire_shape_is_stable` pins
it, and moving one breaks the wire format):

* `_source`: the normalized runtime id (`codex` / `claude-code`).
* `_session_id`: this branch's session claim, taken from `session` in
  `session/meta.json` and carried into the envelope unchanged, **never
  recomputed from content** — the `sessionId` inside content belongs to that
  recording, which is a different thing from the branch identity.
* `_object_hash`: the content address of this line's `content`; the algorithm's
  only implementation site is `transcript::object_hash`:

  ```text
  _object_hash = hex(SHA256(serde_json::to_string(&content)))[..40]
  ```

  Its canonicity (independent of key insertion order, `{"n":1e0}` normalized to
  `1.0`) rests entirely on serde_json's default features: objects go through
  BTreeMap (keys sorted), numbers through f64. A comment in Cargo.toml pins the
  ban on adding `preserve_order` / `arbitrary_precision`, and the
  `object_hash_*` tripwire tests fail loudly on the day someone adds one.

**The skip rule**: empty lines and lines that fail to parse (a truncated tail,
for one) never enter the repo; once the tail is complete it is accounted for by
the next commit. The envelope sequence therefore aligns with the **parseable
lines** of the live text, not with physical line numbers — a bad line occupies a
physical line number, and such a number must never index the packed envelope
sequence (coordinate discipline: cut the window on the raw live lines first,
then pack the slice).

**Unwrapping** has two settings: `unwrap_strict` requires every line to be a
valid envelope (its error message carries a 1-based line number);
`unwrap_lossy` skips bad lines and counts them, for reading a repo that "an
older tool may have written badly". The lines that come back are **canonically
serialized** — key order is rearranged by BTreeMap, the semantics are equal to
the letter, and the bytes do not follow the source file; downstream comparison
always goes through Value/hash, never raw bytes.

### VIEW = the resume selection

The full saved event sequence is `LOG`; the selected resume sequence is `VIEW`.
Repository-backed `agit show` reads `VIEW` by default and `LOG` with
`--log-only`. Resume materializes `VIEW` into envelopes and unwraps the native
records before installation. For ordinary capture, the selection runs from the
last compact boundary (inclusive) to the end; without compaction it contains
the whole captured transcript.

Both forms of compact boundary count (`EventKind::is_compact`): in Claude Code a
user line carrying `"isCompactSummary":true`, in Codex a
`{"type":"compacted",…}` line. The slice is cut on **raw live lines** by
physical line (`view_of_live`), and only then packed into envelopes by
`wrap_lines`.

The logical VIEW is rebuilt from live content when a turn is captured; v1
persists the resulting event-id sequence rather than a second envelope file.
Session enumeration does not count `VIEW` as another session: `session::list_in`
recognizes root `LOG` or the legacy v0 log together with claimed metadata.

**Current v1 self-consistency:** every event id in `VIEW` must resolve to its
canonical object and occur in `LOG`, including synthetic merge/cherry-pick
events. Paired operation markers must also be valid. Historical v0 handling
has compatibility rules for synthetic VIEW records; that exception must not be
used to admit an orphan event into a v1 sequence.

### The write path: commit / import -n

Both commands run the same code and produce byte-identical snapshots. Recording
one version:

1. **The continuity check**, against the committed HEAD blob and not the
   workspace file: the committed envelope hash sequence must be a **prefix** of
   the hash sequence of live's parseable lines (`transcript::continuity`). Three
   verdicts —
   * `Noop`: nothing grew, a no-op (printing "nothing new since agit-…").
     A last line written halfway (non-empty but not parseable as JSON) is not
     accounted for under the skip rule, and the output says it was skipped.
   * `Append`: pure append; carry on.
   * `Diverged`: something in the middle changed — this branch is already taken
     by another session, and it is refused before anything touches the disk:

     ```
     the current branch of alice/photo is already taken by another session.
       this branch's session is agit-…, and 019fb2… does not continue it
       → record it elsewhere: agit commit 019fb2… -n <another agent name>
     ```

     Native installation is a separate resume/run step (§7); clone itself
     does not create a native session. The storage layout does not replace the
     continuation checks for an installed instance.
2. Pass the logical LOG and VIEW envelope streams to `storage::write_snapshot`.
   It writes canonical event objects under `events/`, reuses identical existing
   objects, and writes the root `LOG` / `VIEW` event-id sequences. A conflicting
   body under an existing event id is refused.
3. Overwrite session/meta.json: `session` is inherited from the tip, and only a
   branch's first snapshot claims it by content.
4. git commit (message shaped `agit: 3 turns`; the author comes from the account
   name and email in the sign-in credentials), tag `agit-<40hex>` on the commit
   SHA, and the ownership written back to the store link — the next
   `agit commit <agent>` finds it through that.

### The read path: show / clone / resume

| Command | Which content it reads | How |
|---|---|---|
| Repository-backed `agit show` | selected `VIEW` | Materializes the selected point's sequence into envelopes for parsing/rendering; `--raw` strictly unwraps native records |
| Repository-backed `agit show --log-only` | full `LOG` | Uses the same layout-aware materializer for the complete saved sequence |
| `agit clone` | Git history and repository metadata | Fetches, creates the local checkout/branches and optionally binds the workspace; it does not install or launch a runtime |
| Repository-backed `agit resume` | selected branch head's `VIEW` | The slow path materializes and unwraps the VIEW, restores required native bootstrap metadata when available, then installs it; an eligible existing native instance can use the fast path |
| `agit show` selecting a native transcript or store link | the runtime's live transcript | Reads native content directly, with no repository envelope unwrapping |

A missing or unreadable required `VIEW` or event object is an incomplete
checkout. Materialization refuses instead of substituting the full `LOG`.
Recover the saved content with clone/fetch before retrying the selected session.
The selected branch/ref determines the saved VIEW, not an unrelated checked-out
branch.

### Historical layouts

| Generation | Physical shape | Current distinction |
|---|---|---|
| v0 | `session/meta.json`, `session/log.jsonl`, `session/VIEW` | Layout-aware readers retain historical compatibility; migration writes v1 without changing old commits |
| Earlier multi-session design | `sessions/<runtime>/<id>.jsonl` | Historical design, not the current v0/v1 session layout |
| Earlier root triplet | `snapshot.json`, `transcript.jsonl`, `view.jsonl` | Historical design, not the current root `LOG` / `VIEW` event-id format |

The earlier layouts must not be confused with v0 merely because their files
contain transcripts. Current v0/v1 interpretation is selected by
`session/meta.json`; valid v0 history remains readable and has a dedicated
storage migration path.

## 5. Turns

**A turn = from the person speaking to just before the person speaks again**,
including every tool round trip in between.

A turn boundary lands only at a real user prompt. Both runtimes stuff a grea

### docs/03_branch_model.md (excerpt)
# One branch, one session

## 1. The model

```
agent    = repo
branch   = session
commit   = a snapshot of that session
```

Once a session occupies a branch, that branch never changes hands. To change direction, open a
new branch; the old one stays.

Precisely: a branch has **two forms**, fixed the moment it is born and never convertible (the
`line` field of `session/meta.json`). A **session line** is bound to one session for life and
takes turn / merge / view / file / archive commits; a **file line** never claims a session, takes only commits of
the shared files (memory, skills, AGENTS.md), cannot be resumed, and serves only as the starting
point of a fork / new. The `main` that `agit init` creates is a file line, and sessions each sit
on their own session line — so "how many sessions an agent has" counts session branches, not
whether HEAD carries a transcript (§6).

This is not an invented structure — it already exists in the data, only without a branch to name
it. Committing two sessions alternately inside one agent grows two snapshot chains out of a
common ancestor anyway. All this does is let a git branch carry that, instead of interleaving two
unrelated histories on one `main`.

## 2. Session identity = the value this branch's root snapshot claims

**The runtime session id cannot be used.** `install::mint_id()` mints a new UUID on every
install, so the same agent cloned onto two machines necessarily has two different runtime ids.
Bind on that, and a commit from machine B onto the same branch is judged a change of session. A
runtime id identifies "this install on this machine", not a durable identity — so it does not
enter `session/meta.json` either.

**Fast-forward alone is not enough** either. FF only requires the new commit to be a descendant
of the old tip, and a descendant commit can replace every file. The binding has to be at the
content layer.

A snapshot id is the SHA of the git commit (with an `agit-` prefix) — but the commit SHA of the
root snapshot cannot be computed before the commit (the tree it covers contains
`session/meta.json` itself), so the root snapshot claims the branch with a **content hash**:

```text
session = "agit-" + hex(SHA-256(cwd ‖ 0x00 ‖ transcript bytes))[..40]
```

Computable before the commit, stable across machines, and it introduces no new id space. It
carries no parent (that is the git commit's business) and no session of its own (which would be
circular).

- Later snapshots on the same branch inherit `session` from the tip and never recompute it; the
  tip is whatever HEAD's blob says — the binding lives in the history, and the copy in the
  working tree is only a mirror.
- Only a place that "has no session identity yet" is claimed: the root snapshot of a new agent;
  or a cloned repo where `session/meta.json` cannot be read (pushed up by plain git), where the
  next commit treats it as the start of a new chain, claims by content, and says so rather than
  doing it silently.
- A branch cut off an existing tip with git is **born carrying the tip's identity** (the client
  only continues it), and it is claimed under that identity the first time it appears on the
  server (§4). What the gate locks is "an existing branch must not switch to another identity",
  not "one identity may appear on only one branch".

Lineage itself is the business of the git commit chain and is not written into
`session/meta.json`.

## 3. Repository layout

With one branch per session, a directory level split by runtime has no meaning. The main
checkout (`~/.agit/repos/<owner>/<name>`) stays on the `main` file line; each session branch
gets its own linked worktree the first time it needs a checkout
(`~/.agit/worktrees/<owner>/<name>/<branch>`, which `agit repo path <owner>/<name>@<branch>`
prints and creates on demand). In any checkout, the session content of that branch is these
three files under `session/`:

```
session/meta.json   session metadata (branch form, session identity, runtime, cwd)
session/log.jsonl   the full history, one envelope per line, append-only
session/VIEW        the resume VIEW, a derived file rewritten whole on every commit
```

All three names are fixed constants (`FILE` / `LOG_FILE` / `VIEW_FILE` in
`agit::domain::meta`, and a same-named set on the server side in `gitsync::provenance`), so no
path is recorded in meta — one less place that can disagree with the facts. They sit under
`session/` rather than spread over the repo root because the root also carries the shared files
(memory / skills / AGENTS.md): mixed together, "which bytes belong to this session" has no
path-level answer, and the gate, doctor and the read paths all judge by that boundary.

The envelope format, the write path and the read path are in `docs/02_session_store.md` §4;
`git log <branch>` is this session's version history, and `git show <tag>:session/log.jsonl`
gets that version (in envelope form — the envelope is unwrapped back to raw lines before
rendering or installing).

`session/meta.json`:

```json
{
  "line":     "session",
  "session":  "agit-7f3a…",
  "runtime":  "claude-code",
  "cwd":      "/Users/nana/Projects/OpenPad",
  "code":     "git@github.com:nana/OpenPad.git@1839e61",
  "kind":     "turn",
  "turn":     3
}
```

`line` is the branch form (§1), written down explicitly instead of inferred from "does the tree
carry session files": a session line just created, with its first turn not yet settled, equally
"has commits and no session files", and the inference would take it for a file line and refuse
it. `session` is what the binding rests on (the content hash claimed in §2); a file line never
has it, and a session line does not have it either until the first turn is settled. Once an
identity is claimed, `runtime` is required — the envelope's `_source` and the VIEW slicing both
parse with it, and nothing else can supply it when it is missing.

There is no `parent`, and no `signer`/`key`/`sig` — the commit author comes from git's own
`user.name` / `user.email` (supplied by the sign-in credentials).

Snapshot id = the commit SHA (with an `agit-` prefix); no hash of its own is computed, because
git's commit hash already covers the whole parent → tree → blobs tree.

The agent name (`repo::valid_name`): non-empty, alphanumerics and `-` / `_` only — the name has
to serve as both a directory name (`~/.agit/repos/<owner>/<name>/`) and a URL path segment. It
**may** start with `agit-`: a repo name always sits in the `owner/<name>` position, never mixed
in with a ref, so there is no ambiguity to resolve; the hub allows it too, and derives one from
the directory name (binding `~/Code/agit-web` gives `alice/agit-web`).

The branch name (`repo::valid_branch_name`): non-empty, and must not start with `agit-` — that
prefix belongs to snapshot ids, otherwise `agit clone x/y@Z` has no way to tell whether Z is a
version or a branch. The character set is governed by git's own refname rules.

## 4. How the binding is guarded

Two layers — the client blocks first, the server is the backstop — and on both sides the test is
content, not the shape of a ref.

**Client: a continuity check before anything touches the disk.** `agit commit` requires the
committed envelope hash sequence to be a prefix of the live parsable-line hash sequence (see
`docs/02_session_store.md` §4). Anything but a prefix means another session wants to occupy this
branch — reject, history unchanged, not one byte moved:

```
the current branch of alice/photo is already occupied by another session.
  this branch's session is agit-…, and 019fb2… is not its continuation
  → record it elsewhere: agit commit 019fb2… -n <another agent name>
```

The copy `agit clone` installs into a runtime is minted with a new session id — content that is
nearly identical line by line is judged a divergence here as well. That is the cost of a
content-level test, and it is what the test is for.

**Server: one binding check inside the push gate.** A push passes **seven gates** (backend
`gitsync::routes::receive_pack`):

| # | Gate | What it tests |
|---|---|---|
| ① | Authentication | an anonymous push has no subject for the question "who pushed this" |
| ② | Authorization | whether there is write permission on this agent |
| ③ | ref movement rules | published history is immutable: non-fast-forward / deleting a published ref / repointing an `agit-*` tag |
| ④ | provenance | **two halves**: layout (`session/meta.json` is valid, the log is in the tree, tag name = commit sha) + VIEW self-consistency (every event the VIEW references is reachable, merge markers close in pairs) |
| ⑤ | session binding | the one this section describes |
| ⑥ | secret scanning | **public agents only**, see below |
| ⑦ | quota | only private agents have a hard cap |

Any gate that fails rolls back **every** ref (not only HEAD: a version ID is a tag, and a tag can
point at a commit that is not on the default branch).

The order is by **cost**: ① and ② decide before the request body arrives, and someone with no
write permission must not be able to make the server unpack a pack for them; ③ only compares
shas; ④ reads a few small blobs; ⑥ reads every newly reachable object in full. A push that is
certain to be rejected belongs at the cheapest gate that can stop it. The two halves of ④ are
split along the same line: the layout half sits right after ③, while the VIEW self-consistency
half, which reads the log and the VIEW of every session branch end to end, sits after ⑤.

**⑥ branches on visibility.** What it guards is "the hub is not a distribution channel for
leaked credentials", not "the hub keeps your secrets for you":

- push to a **private** agent → the server does not scan. The content goes into the author's own
  storage and nothing is distributed; and the server-side gate honors no inline annotation, so
  one false positive wedges the author's own work **with no way out**. The client-side scan
  before push still runs, and on the private path it is the only one.
- push to a **public** agent → scan. This push is itself the publication.
- private → **public** → scan the whole repo.
- a PR moving into a **public** target → scan.

All four routes pass through the same choke point, `gitsync::routes::expose()` — sharing one
choke point is what makes the next sentence an invariant rather than a coincidence: **every byte
is scanned in full by this rule set before it is readable by a third party.** History accumulated
while private is scanned end to end at the moment it turns public. The scan surface is
"everything outside the exclusion list" (`agit::domain::secrets::in_publish_surface`, plus
`session/meta.json`) — that is, everything except `.git/`.

The test at the session-binding gate (`check_session_binding`):

> The `session` in the pushed `session/meta.json` must equal the value on that branch's tip.

The four cases:

1. **The branch does not exist** → the first snapshot claims it. This is how a new branch is
   normally born.
2. **The tip carries no metadata** (an empty repo, a commit the hub bootstrapped itself), or
   **the tip is a legacy layout** (the new form does not parse, there is no session identity to
   guard) → allow. This is the grandfather clause: published history is not rewritten by the
   tooling, and the first new snapshot on a legacy branch claims it from then on.
3. **The tip has metadata but the server cannot read it** (over the read cap, read failure) →
   **reject**. Allowing this case too would turn case 2 into a two-step bypass: first inflate or
   corrupt the meta, then push under another identity. "The content itself says there is no
   identity" and "I cannot read the content" are two different things, and only the first
   deserves the grandfather clause.
4. **Both sides have an identity** → they must be equal; unequal is a rejection.

Tags fall outside this gate: a tag is the name of a single snapshot, with 

### docs/07_tui.md (excerpt)
# The side people use: the terminal interface

The earlier documents are all about the model: how a session is stored, how
branches split into lines, how a workspace is decoupled. This one is about **how
a person uses it** — what belongs on screen when a command is typed with no
arguments.

agit's main user is an agent: agents settle through hooks, learn who they are
from environment variables, and their output is read by programs. A person
sitting at the terminal needs something else: to **see what is there before
deciding what to do**. `agit resume` wants a branch name first and `agit new`
wants a repo name first — and remembering those two is exactly what opening the
terminal was for.

The interface solves that one thing. It adds no capability and changes no
existing output.

## 1. When it opens

Four tests, all required:

1. the command's **key argument is empty** (each command defines its own key
   argument);
2. stdin **and** stdout are both terminals;
3. **not inside an agent session**;
4. not explicitly turned off
   (`--no-tui` / `AGIT_TUI=0` / `--json` / `-q` / `-y`).

`--tui` overrides test 3, **but not test 4**. `--json` asks for machine-readable
output, `-q` asks for quiet, `-y` asks not to be prompted — none of the three is
compatible with "pop up a full-screen interface". Letting one flag silently
override another only manufactures "why was this run different" questions.

### Why test 3 speaks up and the other two do not

The three ways of not opening are nothing alike:

* **not a tty** (a pipe, CI): nobody is watching that side, and a line of
  explanation only pollutes stderr;
* **turned off by the user**: they just typed `--no-tui`; saying it back is
  noise;
* **inside an agent session**: they typed the bare command expecting a list and
  got a screen of plain text.

The third one has to be said, and it has to say which test blocked it and how to
get around it:

```text
note not opening the TUI: this looks like an agent session
     (AGIT_SESSION=nana/payments@refund-fix). use `agit --tui` to open it anyway.
```

Drop any one of those parts and the user is left guessing. The note goes to
stderr, so stdout is still consumable by a pipe.

### The tests are not a config key

There is no `tui.enabled` key. "When it opens" is a property of **this call** —
whether anyone is watching, who this output goes to — while configuration is
state that persists across calls. Make it configuration and, on one machine, the
behavior inside a pipe and the behavior in a terminal are decided by a file that
has nothing to do with either.

## 2. The handoff: the through-line

The interface does not exist for "a good-looking list"; it exists to **put the
user inside Claude Code's or Codex's own interface**.

Once a session is picked:

```text
agit's interface suspends  →  the terminal goes to the runtime  →  the runtime exits  →  agit takes it back  →  rescan, back to the list
```

**No nested interface.** The agent's TUI wants the same alt screen and the same
raw mode, and agit does not wrap another frame around it — that would wreck both
renderings at once. So terminal state is four actions (take over, suspend,
resume, give back), not two.

### The one invariant: entries and exits balance

The terminal is state that lives **outside the process**. One restore too few
leaves the user with a shell that has no echo and no cursor, and they do not
connect that to agit — they conclude the terminal is broken. One restore too
many is just as harmful: leaving the alt screen again when it has already been
left wipes out what is in their scrollback.

The invariant holds for **any** sequence of actions, including a panic partway
through, an early return, and a child process crashing while suspended. So the
state machine is independent of execution and can be tested exhaustively;
restoration goes through `Drop`, not through "remember to call it at the end of
the function".

### Results stay in the scrollback

Once the interface closes, the terminal shows what just happened, the same as
after an ordinary command. So everything that is read afterwards — which repo
was picked, which branch was created, which files were materialized — prints on
the **normal screen**, not in the alt screen. What is written in the alt screen
is gone the moment it exits, and that stretch turns blank.

`agit new` is therefore "pick the repo full-screen, type the name on the normal
screen": the name is this session's identity in version control, and it and its
result both leave a trace.

## 3. The screens

### 3.1 Bare `agit` / `agit resume` — which one to continue

`resume` continues an existing local session and never creates a fork. To start
from a tag, historical point or another author's source, use `agit run <ref>`;
it continues a writable session head when possible and otherwise creates a new
writable session.

```text
┌ agit ── nana @ agent-git.com ── rc: online ── ⚠ 2 unnamed ───────────┐
│  sessions                          │  refund-fix                      │
│ ─────────────────────────────────  │ ──────────────────────────────── │
│ ▸ ● here    payments/refund-fix    │  repo     nana/payments          │
│   ○ same-repo  infra/deploy-v2     │  runtime  claude-code            │
│   ⚠ unnamed  claude-code a3f9c1…   │  active   6m ago                 │
└───────────────────────────────────────────────────────────────────────┘
 ↑↓ move  enter continue  / filter  q quit
```

Sources and project badges:

| Badge | Meaning |
|---|---|
| `here` | a session adopted in this directory |
| `same-repo` | a branch in the same code repo |
| `unnamed` | a session that exists in the runtime but is not managed yet |
| `elsewhere` | an adopted session in another project, shown only in all-project scope |

All three sources share one recency axis; on an exact tie an adopted session
comes first. The status bar keeps the number of `unnamed` sessions visible
without letting the badge split the list into a second ordering rule.

Import and resume start with an explicit runtime scope when candidates span multiple
recognized runtimes; a single-runtime list needs no additional step. The scope can
include all available runtimes to preserve the combined recency view. Tab or arrow
keys change this preselection and Enter opens candidates; Esc cancels without adopting.

`a` toggles current-project and all-project candidates. Current scope retains the
same-repo discovery signal for adopted branches. Every row carries its recorded
project directory; missing directories remain `unknown`, never decoded from a slug.
In the resume list, Tab cycles runtime scope. Import's existing stage navigation and
the naming inbox keep their Tab meaning; `r` returns to runtime preselection there.
Scope keys do not intercept filter input or branch-name editing. They change the
visible candidates, never the selected command identity.

Discovery reads runtime indexes and local claims. Missing opening prompts and paths
use a bounded opening window on the leading unmanaged candidates, with a cached
window for a newly highlighted import candidate. Cursor's project is recovered only
when that candidate is highlighted, using the native body/path convention. An
unreadable or incomplete window displays an unavailable preview; it does not open
the rest of a transcript or materialize a runtime export. Enter still delegates to
ordinary import/resume, which revalidates the explicitly selected identity.

Every screen also carries one bounded snapshot of `agit rc status`. The probe
runs before the alternate screen is entered and is refreshed after a runtime
handoff, s

### npm/README.md
# @einsia/agent-git (npm distribution)

This package ships the prebuilt **`agit`** CLI — no Rust toolchain needed.

```sh
npx -y create-agit@latest          # one-shot install: binary + skills/hooks/MCP
# or as a global package:
npm install -g @einsia/agent-git   # pnpm add -g @einsia/agent-git — same CLI
agit --help
```

Two package names, one CLI:

| Package             | Role                                                        |
| ------------------- | ----------------------------------------------------------- |
| `@einsia/agent-git` | the real package — shim, postinstall, platform sub-packages |
| `create-agit`       | `npx` one-shot installer, lands `agit` in `~/.local/bin`    |

> The old package `@einsia/agentgit` (no hyphen) is the pre-rewrite CLI. This
> package is its successor, not a new version of it; there is no upgrade path
> between the two.

`agit` is a native Rust binary. This package is a thin wrapper: npm installs
the platform sub-package matching your `os`/`cpu` via `optionalDependencies`
(`@einsia/agent-git-linux-x64` and friends), the `agit` bin is a Node shim
that execs that binary with argv/stdio/exit-code forwarded, and `postinstall`
runs `agit setup` once to wire skills, hooks, MCP and AGENTS.md.

The executable contains Git and Git LFS. On first use it extracts them under
`$AGIT_HOME/git-runtime` (default `~/.agit/git-runtime`), with no runtime download.
Only AgentGit's child processes use that private runtime; your shell PATH and
global Git configuration are unchanged. Copying or upgrading the single executable
also carries its Git runtime. External credential helpers and extensions may still
need your local tools; `AGIT_USE_SYSTEM_GIT=1` uses your system Git installation.

pnpm (v10+) blocks dependency install scripts unless approved, so under pnpm
the automatic `agit setup` does not run — run it once yourself after
installing (or `pnpm approve-builds -g` and reinstall).

The hub (**AgentGit**) is not in this package; it deploys separately.

## Platforms with prebuilt binaries

| OS    | Arch          | Platform package                  |
| ----- | ------------- | --------------------------------- |
| Linux | x86_64        | `@einsia/agent-git-linux-x64`     |
| Linux | aarch64/arm64 | `@einsia/agent-git-linux-arm64`   |
| macOS | x86_64        | `@einsia/agent-git-darwin-x64`    |
| macOS | arm64         | `@einsia/agent-git-darwin-arm64`  |
| Windows | x86_64      | `@einsia/agent-git-win32-x64`    |

**Linux binaries are musl static-linked — no glibc floor.** Verified on Alpine,
Amazon Linux 2 (glibc 2.26), Debian 11/12, Ubuntu 20.04–24.04, x86_64 and
arm64. No more `libc.so.6: version 'GLIBC_2.xx' not found`.

On macOS, if Node runs under Rosetta (it reports itself as x64) the installer
detects it and installs the arm64 build.

Unsupported operating system and architecture pairs get no prebuilt binary: running
`agit` prints build-from-source instructions. On WSL, the Linux binary works.

## Failure behavior

- Unsupported platform → the shim explains and exits 127 with the source-build
  recipe.
- `agit setup` failing in postinstall never blocks the install — the CLI is on
  disk; re-run `agit setup` any time.
- If npm suppresses postinstall, the next invocation of a globally installed
  `agit` schedules a guarded RC daemon reconciliation in the background.
  npm cannot run the daemon handoff at install time when it suppresses scripts.

## Environment variables

| Variable         | Effect                                                              |
| ---------------- | ------------------------------------------------------------------- |
| `AGIT_BINARY`    | Point at an existing `agit` binary; shim and postinstall honor it.  |
| `AGIT_SKIP_SETUP`| Skip the postinstall `agit setup` (CI, managed environments).       |
| `AGIT_FORCE_INSTALL` | Also run postinstall inside the source checkout (CI smoke tests). |
| `AGIT_HUB_URL`   | Point the CLI at another hub (default `https://agent-git.com`).  |
| `AGIT_NPM_REGISTRY` | Registry `agit upgrade` downloads platform packages from.        |
| `AGIT_USE_SYSTEM_GIT` | Set to `1` to use system Git and Git LFS instead of the bundled runtime. |

## Upgrading

`agit upgrade` asks the hub for the latest CLI version and downloads the
platform package tarball straight from the npm registry, verified against the
registry's SRI (sha512) before anything is replaced.

Windows packages contain `agit.exe`. The `create-agit` installer writes it to
`%USERPROFILE%\.local\bin`; add that directory to your user PATH if the installer
reports that it is missing. Windows source builds need Rust and the MSVC C/C++
toolchain. The local RC daemon uses a current-user Windows named pipe and private
RC state. It refuses shared or redirected RC paths instead of changing their permissions.


## Top-level structure
- `AGENTS.md` — agent instructions including agit session-control block
- `CHANGELOG.md` — release notes (source of GitHub Release bodies)
- `Cargo.toml` / `Cargo.lock` / `rust-toolchain.toml` — Rust workspace; package `agit` **v0.2.28**, rust-version 1.88, edition 2024
- `setup.sh` — contributor build/install to `~/.local/bin/agit`
- `src/` — CLI binary: `adapter`, `commands`, `domain`, `hub`, `infra`, `protocol`, `rc`, `telemetry`, `tui`, `ui`
- `crates/` — `agit-controller`, `agit-peer`, `agit-tunnel` (workspace members)
- `apps/macos-menubar/` — macOS menubar app
- `docs/` — extensive docs (usage, setup, session store, branch model, workspaces, TUI, secret filters, RC/peer RFCs, privacy, telemetry, mechanism-probing per runtime)
- `npm/` — `@einsia/agent-git` + platform packages + `create-agit` one-shot installer
- `examples/`, `benches/`, `tests/`, `scripts/`, `memory/`
- `.github/` — Release / npm publish workflows; `RELEASE_ARTIFACTS.md`
- Note: Hub/server (**AgentGit** backend) is a **separate repository**; this repo is the CLI
