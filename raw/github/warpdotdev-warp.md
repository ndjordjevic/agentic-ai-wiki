# warpdotdev/warp

## Metadata
- Stars: 62646
- Primary language: Rust
- Default branch: master
- Latest release: v0.2026.06.09.19.54.dev_00 (2026-06-09)
- License: GNU Affero General Public License v3.0 (AGPL-3.0); UI framework crates also available under MIT
- Homepage: https://warp.dev
- Fetched: 2026-07-01
- Final URL: https://github.com/warpdotdev/warp

## Description
Warp is an agentic development environment, born out of the terminal.

## README

[Warp](https://www.warp.dev) is an agentic development environment, born out of the terminal. Use Warp's built-in coding agent, or bring your own CLI agent (Claude Code, Codex, Gemini CLI, and others).

You can [download Warp](https://www.warp.dev/download) and [read the docs](https://docs.warp.dev/) for platform-specific instructions.

> **Note:** OpenAI is the founding sponsor of the new, open-source Warp repository, and the new agentic management workflows are powered by GPT models.

### Warp Contributions Overview Dashboard

Explore [build.warp.dev](https://build.warp.dev) to:
- Watch thousands of Oz agents triage issues, write specs, implement changes, and review PRs
- View top contributors and in-flight features
- Track your own issues with GitHub sign-in
- Click into active agent sessions in a web-compiled Warp terminal

### Oz for OSS

Maintaining a popular open-source project? [Apply for Oz credits](https://tally.so/r/LZWxqG) to explore [Oz for OSS](https://github.com/warpdotdev/oz-for-oss).

Oz for OSS is a partner program for bringing the same agentic open-source management workflows used in this repository to select partner repositories. Workflows include issue triage, PR review, community management, and contributor coordination.

### Licensing

Warp's UI framework (the `warpui_core` and `warpui` crates) are licensed under the MIT license.

The rest of the code in this repository is licensed under AGPL v3.

### Open Source & Contributing

Warp's client codebase is open source and lives in this repository. Community contributions are welcome via a lightweight contribution workflow. For the full contribution flow, see [CONTRIBUTING.md](CONTRIBUTING.md).

**Chat with contributors and the Warp team** in the [`#oss-contributors`](https://warpcommunity.slack.com/archives/C0B0LM8N4DB) Slack channel.

### Issue to PR Workflow

1. Search existing issues for the bug or feature request.
2. If nothing exists, file an issue using templates.
3. A maintainer reviews and may apply readiness labels:
   - `ready-to-spec` — design is open for contributors to spec out
   - `ready-to-implement` — design is settled and code PRs are welcome
4. Anyone can pick up a labeled issue.

### Building the Repo Locally

```bash
./script/bootstrap   # platform-specific setup
./script/run         # build and run Warp
./script/presubmit   # fmt, clippy, and tests
```

See [AGENTS.md](AGENTS.md) for the full engineering guide, including coding style, testing, and platform-specific notes.

### Open Source Dependencies

Key dependencies include: Tokio, NuShell, Fig Completion Specs, Warp Server Framework, Alacritty, Hyper HTTP library, FontKit, Core-foundation, Smol.

## Top-level structure

```
.agents/          — agent configuration files
.claude/          — Claude coding agent configuration
AGENTS.md         — full engineering guide (coding style, testing, platform notes)
CONTRIBUTING.md   — contribution workflow
FAQ.md            — frequently asked questions
LICENSE-AGPL      — AGPL v3 license
LICENSE-MIT       — MIT license (UI framework crates)
README.md         — project overview
SECURITY.md       — security policy
app/              — Warp application source
crates/           — Rust crate workspace
docker/           — Docker configuration
resources/        — application resources
script/           — build and setup scripts
skills-lock.json  — agent skills lockfile
specs/            — technical specifications
```
