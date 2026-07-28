---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://www.docker.com/products/docker-sandboxes/
companion_urls:
  - https://github.com/docker/sbx-releases
raw_files:
  - ../../raw/web/docker-sandboxes.md
  - ../../raw/github/docker-sbx-releases.md
tags:
  - coding-agent-sandbox
  - microvm-isolation
  - dangerously-skip-permissions
  - filesystem-passthrough
  - network-proxy-policy
  - docker-in-docker
  - agent-governance
  - disposable-environments
related:
  - vercel.com
  - browserbase.com
  - warp.dev
  - eve.dev
  - cognition.ai
  - developers.openai.com
product: docker-sandboxes
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

Docker Sandboxes is Docker's product for running coding agents (Claude Code, Gemini CLI, Copilot CLI, Codex, OpenCode, Kiro) inside disposable, isolated microVMs, giving each agent its own Docker daemon, filesystem, and network so it can operate in permissive "YOLO mode" (`--dangerously-skip-permissions`) without risking the host machine. It's Docker's answer to the same "give agents autonomy safely" problem this wiki has seen from Vercel Sandbox ([[vercel.com]]) and browser-focused sandboxing tools like [[browserbase.com]], applied specifically to full local dev environments with real Docker access inside the sandbox itself.

_All claims below are sourced from ../../raw/web/docker-sandboxes.md unless otherwise noted._

## What it does

Each sandbox is a dedicated microVM with the user's dev environment and only the current project workspace mounted in — the agent can install packages, modify configs, and spin up its own nested Docker containers, while the host stays untouched. Setup is a single install (`brew install docker/tap/sbx` on macOS, `winget install Docker.sbx` on Windows, or an APT install on Ubuntu) followed by `sbx login` and `sbx run <agent>` to launch an agent inside a sandbox from the current project directory.

## Key features

- **MicroVM isolation**: a hard security boundary from the host via hypervisor-level virtualization, not just container namespaces.
- **Filesystem passthrough**: the workspace is mounted at the same absolute path inside the sandbox as on the host, so file changes are instant in both directions with no sync process, and error messages/paths remain directly usable for debugging. Virtiofs caching is on by default for read performance (opt-out via `DOCKER_SANDBOXES_ENABLE_VIRTIOFS_CACHE=0`). (../../raw/github/docker-sbx-releases.md)
- **Network proxy enforcement**: all outbound sandbox traffic routes through an HTTP/HTTPS proxy on the host, which enforces network access policies and handles credential injection; sandbox-specific proxying is configurable independently of the host's own `HTTP_PROXY`/`HTTPS_PROXY` via `DOCKER_SANDBOXES_PROXY` (supports `http://`, `https://`, `socks5://`, `socks5h://`).
- **Agents can use Docker too**: each sandbox runs its own private Docker daemon, letting the agent build images and spin up test containers inside the sandbox without touching the host's Docker.
- **Disposable lifecycle**: `sbx run` creates and starts a sandbox; stopping/restarting preserves installed packages and images; `sbx rm` deletes the VM and all contents (and any `sandbox-<name>` git remote created via `--clone` mode).
- **Shared agent skills store**: supported agents mount a shared, host-side skills store read-write by default across sandboxes (opt-out available), so Agent Skills persist across disposable sandbox instances. (../../raw/github/docker-sbx-releases.md)
- **Org-wide governance (paid add-on)**: Docker AI Governance layers centrally managed network-access and filesystem policies on top of Sandboxes, enforced uniformly across every developer's machine — separate from the free `sbx` CLI.

## Architecture

Sandboxes are compared explicitly against three alternatives on Docker's own architecture page: a plain container with a Docker socket mount (partial namespace isolation, shared host daemon — "trusted tools"), Docker-in-Docker (partial, privileged, nested daemon — CI/CD pipelines), and raw host execution (no isolation — manual development). Sandboxes trade the highest resource overhead (a full VM plus its own Docker daemon) for complete hypervisor-level isolation, explicitly positioned for "autonomous agents" rather than trusted tooling or CI. (../../raw/github/docker-sbx-releases.md)

## Installation

```bash
# macOS
brew trust docker/tap && brew install docker/tap/sbx
sbx login

# Windows
winget install -h Docker.sbx
sbx login

# Linux (Ubuntu)
curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh
sudo apt-get install docker-sbx
sudo usermod -aG kvm $USER
newgrp kvm
sbx login
```

## Example usage

```console
$ cd ~/my-project
$ sbx run claude
```

This launches Claude Code (or another supported agent) inside a fresh sandbox scoped to the current project directory, with `--dangerously-skip-permissions`-style autonomy enabled by default within the isolated microVM.

## When to use

Docker Sandboxes fits teams that want to run coding agents in fully permissive/autonomous mode locally — without individually reviewing every file or network action — while still containing the blast radius of a misbehaving or compromised agent to a disposable VM. It's a stronger isolation model than a plain container-based sandbox (agents get a private Docker daemon and true VM-level separation) at the cost of more resource overhead than lightweight container sandboxes. Teams that need centralized policy enforcement across a whole engineering org (rather than per-developer opt-in) are the target audience for the paid Docker AI Governance layer on top.

## Maintenance status

Actively developed: latest stable release v0.37.0 (2026-07-24), with a nightly pre-release build pushed 2026-07-28 and an rc4 pre-release also recent — indicating a fast release cadence typical of a young product line (labeled "New" in Docker's own product navigation). 252 stars on the `docker/sbx-releases` distribution repo, which hosts only install artifacts and the issue tracker, not application source — the `sbx` CLI itself is closed-source. Free for individual/commercial use; only organization-wide governance requires a paid subscription. (../../raw/github/docker-sbx-releases.md)

## Ecosystem

Docker Sandboxes launched alongside several other Docker "AI and Agents" products referenced in the same navigation section: **Docker AI Governance** (org-wide policy enforcement), **Gordon** (Docker's own AI agent), **Docker Model Runner** (local-first LLM inference), and **Docker MCP Catalog and Toolkit** (MCP tool management) — together forming Docker's answer to the agent-infrastructure stack also addressed by [[vercel.com]] (Sandbox, AI Gateway, Workflows) and [[eve.dev]]. Named integration partners include Warp (terminal) and NanoClaw, both quoted endorsing the microVM isolation model for giving agents autonomy without host risk.
