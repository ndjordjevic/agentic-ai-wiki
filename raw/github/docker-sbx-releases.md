# docker/sbx-releases

## Metadata
- Stars: 252
- Primary language: none (releases-only distribution repo, no source language detected)
- Default branch: main
- Latest release: v0.37.0 (2026-07-24)
- License: Other
- Homepage: https://docs.docker.com/ai/sandboxes
- Fetched: 2026-07-28
- Final URL: https://github.com/docker/sbx-releases

## Description
(none set on GitHub)

## README
# Docker Sandboxes

Safe environments for agents. Built by Docker.

# What it does

It provides sandboxes with controlled access to your filesystem, network, and tools. This means your agents can work autonomously without putting your machine or data at risk.

# Details

- Docker-native isolation. Same containerization principles trusted by 20M+ developers.
- Vendor-neutral. Works with the models and tools you're already using.

# What you get

- YOLO mode by default: agents work without asking permission
- Private Docker daemon for running test containers
- File access controls between host and sandbox
- Network access control
- Works with Claude Code, Codex, Gemini CLI, OpenCode, and more

# Install

### Homebrew (macOS)

```bash
brew install docker/tap/sbx
```

### WinGet (Windows)

```powershell
winget install -h Docker.sbx
```

### APT (Ubuntu)

```bash
curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh
sudo apt-get install docker-sbx
sudo usermod -aG kvm $USER
newgrp kvm
```

## Manual install from release artifacts

Download the artifacts for your platform from the GitHub Releases page.

## Top-level structure

This repository is a **releases-only distribution repo** — it hosts install instructions, release binaries/artifacts, and the issue tracker for the closed-source `sbx` CLI (Docker Sandboxes). No application source code lives here; `primaryLanguage` is unset on GitHub. Recent activity includes a nightly pre-release build (2026-07-28) alongside the stable v0.37.0 tag (2026-07-24) and an rc4 pre-release, indicating active, frequent releases. The product's actual documentation lives at docs.docker.com/ai/sandboxes/ (captured in raw/web/docker.com.md) rather than in this repo's README.
