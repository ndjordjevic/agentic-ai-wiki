# docker-sandboxes

## Fetch log
- Inbox URL: https://www.docker.com/products/docker-sandboxes/
- Final URL: https://www.docker.com/products/docker-sandboxes/
- Fetched: 2026-07-28
- Pages: 2
- Mode: standard

**Note:** `docker.com/llms.txt` returned an HTML error/404 page rather than a plain-text catalog — treated as absent per protocol.

## Landing page — https://www.docker.com/products/docker-sandboxes/

# Docker Sandboxes | Sandboxes for Coding Agents | Docker

## Products nav (AI and Agents section)
- Docker Sandboxes New — Isolated environments for coding agents
- AI Governance New — Govern agents and Claws across every team
- Gordon New — Your AI Agent across Docker
- Docker Model Runner — Local-first LLM inference made easy
- Docker MCP Catalog and Toolkit — Connect and manage MCP tools

## Products nav (Application Security section)
- Docker Hardened Images — Ship with secure, enterprise-ready images
- Docker Scout — Simplify the software supply chain

## Products nav (Application Development section)
- Docker Desktop — Containerize your applications
- Docker Hub — Discover and share container images
- Docker Offload — Break free of local constraints

## Docker Sandboxes

**Run AI agents safely in local sandboxes.**

Disposable, isolated sandboxes for AI agents like **Claude Code, Gemini CLI, Copilot CLI, Codex, OpenCode,** and **Kiro** that need safe, unattended execution.

**macOS:** `$ brew trust docker/tap && brew install docker/tap/sbx`
**Windows:** `> winget install Docker.sbx`

## See it in action

Watch an agent install packages, run Docker, modify configs, and execute unattended. Then dispose of the sandbox in one command.

## Why sandboxes

Give agents the autonomy they need to get work done, safely. Agents do their best work when they have freedom. Sandboxes let them run fast without running wild, so speed and safety stop being a tradeoff. Controls shown: Filesystem, Network, Credentials.

Need to enforce these controls across your whole team? → That's Docker AI Governance (/products/ai-governance/)

## Capabilities

**YOLO mode, safely.** Each agent runs inside a dedicated microVM with your dev environment and only your project workspace mounted in. Agents can install packages, modify configs, and spin up their own Docker containers. Your host stays untouched. No manual review, no permission prompts, no supervision required.

- **Customizable Safe Execution** — Network and filesystem controls you define. Enforceable org-wide with Docker AI Governance.
- **MicroVM Isolation** — Hard security boundary from the host.
- **Fast to Spin Up, Easy to Tear Down** — Disposable by default. Faster than VMs.
- **Agents Can Use Docker Too** — Agents can spin up containers within Sandboxes.
- **Real Dev Environment** — Install packages, run services, work unattended.
- **One Sandbox for All Your Coding Agents** — Claude Code, Gemini CLI, Copilot CLI, Codex, Kiro, OpenCode.

Default `--dangerously-skip-permissions`: "Use permissive modes with confidence. In fact, that's the default."

## Works with leading coding agents

Quote — Gavriel Cohen, Creator of NanoClaw: "Every team is about to have their own team of AI agents doing real work for them. The question is whether it can happen safely. NanoClaw was built on the principle that you don't trust agents with security, you build walls around them. Docker has been ahead of the curve on exactly this. Docker Sandboxes is what that looks like at the infrastructure level, making it possible for organizations to get the full value from agents without compromising on security."

Quote — Ben Navetta, Engineering Lead, Warp: "Docker Sandboxes let agents have the autonomy to do long-running tasks without compromising safety. We're excited to integrate Sandboxes into Warp so that developers can run agents freely with a consistent environment, regardless of whether agents are running locally or in the cloud."

## FAQ

**What is a sandbox for AI coding agents?** A sandbox is a microVM isolated environment that protects your filesystem and network from agents running inside it.

**Which coding agents are supported?** Out of the box we support Claude Code, Gemini CLI, Copilot CLI, Codex, OpenCode, Kiro. You can also create your own.

**What does "YOLO mode" mean, and is it safe?** YOLO mode (`--dangerously-skip-permissions`) gives agents autonomy with no approval prompts. Essential for speed, but risky without guardrails. Sandboxes make it safe by isolating each agent inside a dedicated microVM.

**How is a sandbox different from a VM?** Sandboxes run fully isolated in microVMs, giving more isolation without paying the full cost of running a VM. This lets them do things that need more permissions safely, like running additional Docker containers.

**What safety controls can I configure?** To define these once and enforce them on every developer's machine, see Docker AI Governance.

**Do I need Docker Desktop to use sandboxes?** No.

**What if I need additional admin controls?** Installing Sandboxes covers core functionality. For centralized controls across a team such as network policies, filesystem rules, MCP governance: Docker AI Governance.

## Need More Control Over Your Sandboxes?

With Docker Sandboxes, your developers get isolated environments to run agents freely and safely. When your team needs to go further with network access restrictions, filesystem policies, and centralized admin controls: Docker AI Governance adds network access policies, filesystem controls, and org-wide MCP governance — defined once, enforced everywhere. Talk to us about: network access policies for sandbox environments; filesystem access controls and restrictions; admin-level configuration for your team.

**Notable hyperlinks captured on this page:** https://docs.docker.com/ai/sandboxes/ (docs entry point), https://www.docker.com/products/ai-governance/, https://www.docker.com/products/gordon/, https://www.docker.com/products/model-runner/, https://www.docker.com/products/mcp-catalog-and-toolkit/, https://www.docker.com/products/hardened-images/, https://www.docker.com/products/docker-scout/, https://www.docker.com/products/docker-desktop/, https://www.docker.com/products/docker-hub/, https://www.docker.com/products/docker-offload/, https://app.docker.com/signup, https://docs.docker.com/.

## Docs — https://docs.docker.com/ai/sandboxes/

# Docker Sandboxes

Docker Sandboxes run AI coding agents in isolated microVM sandboxes. Each sandbox gets its own Docker daemon, filesystem, and network — the agent can build containers, install packages, and modify files without touching your host system.

> Note: The `sbx` CLI is free to use, including for commercial work. Only organization governance requires a separate paid subscription.

Organization admins can centrally manage sandbox network and filesystem policies, so the same rules apply uniformly across every developer's machine. Available on a separate paid subscription.

## Get started

Install the `sbx` CLI and sign in:

**macOS**
```console
$ brew trust docker/tap
$ brew install docker/tap/sbx
$ sbx login
```

**Windows**
```powershell
> winget install -h Docker.sbx
> sbx login
```

**Linux (Ubuntu)**
```console
$ curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh
$ sudo apt-get install docker-sbx
$ sudo usermod -aG kvm $USER
$ newgrp kvm
$ sbx login
```

Then launch an agent in a sandbox:
```console
$ cd ~/my-project
$ sbx run claude
```

## Learn more

- Agents — supported agents and per-agent configuration
- Integrations — connect editors and apps like VS Code and Cursor to a sandbox over SSH
- Customize — reusable templates and declarative kits for extending or tailoring sandboxes
- Architecture — microVM isolation, workspace mounting, networking
- Security — isolation model, credential handling, and network policies
- CLI reference — full list of `sbx` commands and options
- Troubleshooting — common issues and fixes
- FAQ — login requirements, telemetry, etc

## Feedback

Your feedback shapes what gets built next. If you run into a bug, hit a missing feature, or have a suggestion, open an issue at github.com/docker/sbx-releases/issues.

## Architecture — https://docs.docker.com/ai/sandboxes/architecture/

# Architecture

This page explains how Docker Sandboxes work under the hood.

## Workspace mounting

Your workspace is mounted directly into the sandbox through a filesystem passthrough. The sandbox sees your actual host files, so changes in either direction are instant with no sync process involved. Your workspace is mounted at the same absolute path as on your host, which reduces confusion when debugging or reviewing changes.

> Warning: Avoid mounting network-attached or remote storage (network drives, SMB/NFS shares, or cloud-synced folders) as a workspace — every file read and write goes over the network, adding latency and slowing agent performance.

## Storage and persistence

When you create a sandbox, everything inside it persists until you remove it: Docker images and containers built or pulled by the agent, installed packages, agent state and history, and workspace changes. Each sandbox maintains its own Docker daemon state, image cache, and package installations — multiple sandboxes don't share images or layers, except for a shared agent skills store that supported agents mount read-write by default (opt-out available).

Virtiofs caching is enabled by default on all operating systems, reducing round-trips for read-heavy workloads such as `git status`. Opt out via `DOCKER_SANDBOXES_ENABLE_VIRTIOFS_CACHE=0`.

## Networking

All outbound traffic from the sandbox routes through an HTTP/HTTPS proxy on your host, which enforces network access policies and handles credential injection. The host-side proxy respects the host's own upstream proxy configuration (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`), and a separate `DOCKER_SANDBOXES_PROXY` variable can route only sandbox traffic through a different proxy (supports `http://`, `https://`, `socks5://`, `socks5h://`). `DOCKER_SANDBOXES_NO_PROXY` excludes destinations from that sandbox-specific proxy. Proxy auto-configuration files (`proxy.pac`) are not supported.

## Lifecycle

`sbx run` initializes a VM with a workspace for a specified agent and starts the agent; stopping and restarting preserves installed packages and Docker images. `sbx rm` deletes the sandbox, its VM, and all contents (and removes the `sandbox-<name>` Git remote if `--clone` mode was used).

## Comparison to alternatives

| Approach | Isolation | Docker access | Use case |
|---|---|---|---|
| Sandboxes (microVMs) | Full (hypervisor) | Isolated daemon | Autonomous agents |
| Container with socket mount | Partial (namespaces) | Shared host daemon | Trusted tools |
| Docker-in-Docker | Partial (privileged) | Nested daemon | CI/CD pipelines |
| Host execution | None | Host daemon | Manual development |

Sandboxes trade higher resource overhead (a VM plus its own daemon) for complete isolation. Use containers when you need lightweight packaging without Docker access. Use sandboxes when you need to give something autonomous full Docker capabilities without trusting it with your host environment.
