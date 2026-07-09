---
type: source
source_url: https://determinate.systems/nix-installer/
companion_urls:
  - https://github.com/DeterminateSystems/nix-installer
raw_files:
  - ../../raw/web/determinate.systems.md
  - ../../raw/github/DeterminateSystems-nix-installer.md
tags: [nix, nix-installer, flakes, reproducible-builds, devops, ci-cd, package-management, supply-chain]
related: [kunchenguid-dotfiles]
product: determinate-nix-installer
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

Determinate Nix Installer is the industry-standard way to install Nix and enable flakes across macOS, Linux, WSL, containers, and CI pipelines. Maintained by Determinate Systems, it backs their commercial Determinate Nix platform and has completed over 7 million installs. The installer is written in Rust, uses a planner-based architecture for predictable configuration, and ships a single-command uninstaller — making it the safest, most reversible way to adopt Nix in any environment.

_All claims below are sourced from ../../raw/web/determinate.systems.md unless otherwise noted._

## What it does

Determinate Nix Installer bootstraps a fully functional Nix environment on the host system with flakes enabled by default. A single curl one-liner handles installation on any supported platform:

```shell
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

On macOS, a graphical PKG installer is also available. The installer creates the `/nix` store, sets up the Nix daemon with multi-user mode via systemd (where applicable), configures shell profiles, and on macOS enables Nix to survive system upgrades through "Nix Survival Mode."

## Key features

- **Cross-platform stability**: macOS (Intel and Apple Silicon), Linux (`x86_64`/`aarch64`), WSL2, Valve Steam Deck, Podman, Docker — all at stable maturity.
- **Flakes first**: installs Determinate Nix with flakes and the `nix` command enabled by default; Determinate Systems guarantees forward compatibility for any flake that works today. (../../raw/github/DeterminateSystems-nix-installer.md)
- **Single-command uninstall**: `/nix/nix-installer uninstall` — a safe, thorough removal, unlike official Nix which lacks a supported uninstaller.
- **macOS upgrade survival**: Nix Survival Mode keeps Nix functional across macOS major upgrades.
- **GitHub Actions support**: `DeterminateSystems/determinate-nix-action@v3` installs and configures Nix in a workflow in one step, tagged per Determinate release for pinning. (../../raw/github/DeterminateSystems-nix-installer.md)
- **GitLab and Docker CI**: supports `--init none` for root-only installs in Docker-based runners.
- **Planner architecture**: installation follows a _plan_ made by a _planner_ (linux, darwin, etc.), each configurable via environment variables or CLI flags. (../../raw/github/DeterminateSystems-nix-installer.md)
- **Upgrading via Determinate Nixd**: `sudo determinate-nixd upgrade` upgrades Determinate Nix in place without reinstalling. (../../raw/github/DeterminateSystems-nix-installer.md)

## Architecture

Determinate Nix Installer is a Rust binary that compiles to a single static artifact. It implements a planner pattern: each planner (linux, darwin, ostree, etc.) determines the correct sequence of actions for the target platform. Actions are individually reversible, which is what makes the uninstaller reliable. (../../raw/github/DeterminateSystems-nix-installer.md)

The installer itself is hosted at `install.determinate.systems` and delivered via a shell wrapper (`nix-installer.sh`). After download, the binary is placed at `/nix/nix-installer` and left on disk so that `uninstall` can later undo every action the installer took.

The companion **Determinate Nix** runtime (installed by the installer) is extended upstream Nix: same command surface, but with parallel evaluation, lazy trees, WebAssembly builtins, provenance, and flake schemas layered on top. Upgrades are handled independently by `determinate-nixd`.

## Installation

```shell
# Standard install (recommended)
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install

# With custom build group
NIX_BUILD_GROUP_NAME=nixbuilder ./nix-installer install --nix-build-group-id 4000

# Linux without systemd (Docker, GitLab CI, root-only)
./nix-installer install linux --init none

# NixOS (via flake module)
# inputs.determinate.url = "https://flakehub.com/f/DeterminateSystems/determinate/*";
# Then add determinate.nixosModules.default to your NixOS modules.
```
(../../raw/github/DeterminateSystems-nix-installer.md)

## Example usage

**GitHub Actions:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DeterminateSystems/determinate-nix-action@v3
      - run: nix build .
```

**GitLab CI:**

```yaml
test:
  script:
    - curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install linux --no-confirm --init none
    - . /nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh
    - nix run nixpkgs#hello
```

**Docker:**

```dockerfile
FROM ubuntu:latest
RUN apt update -y && apt install curl -y
RUN curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install linux \
  --extra-conf "sandbox = false" --init none --no-confirm
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
RUN nix run nixpkgs#hello
```
(../../raw/github/DeterminateSystems-nix-installer.md)

## When to use

Determinate Nix Installer is the right choice whenever you want to adopt Nix with minimal friction and maximal reversibility. Use it when:

- You want flakes enabled from day one without manual `nix.conf` edits.
- You need a reliable path to uninstall or upgrade Nix later.
- You run CI on GitHub Actions, GitLab, or Docker-based pipelines.
- You're on macOS and need Nix to survive OS upgrades.
- Your team is evaluating the broader Determinate platform (FlakeHub, FlakeHub Cache, Secure Packages).

The official upstream Nix installer remains an option for those who prefer stock Nix without Determinate's additions, though it lacks a supported uninstaller.

## Maintenance status

Active and well-maintained. 3,640 GitHub stars, 7 million+ installs, tens of thousands per day. Latest release: v3.21.5 (2026-07-08). Licensed under GNU LGPLv2.1. SOC 2 Type II compliant (Determinate Systems). (../../raw/github/DeterminateSystems-nix-installer.md)

## Ecosystem

Determinate Nix Installer is the entry point to the Determinate platform:

- **Determinate Nix** — extended Nix runtime with flakes, parallel eval, lazy trees, Wasm builtins, and provenance.
- **Determinate Nixd** — daemon that handles upgrades, FlakeHub authentication (`determinate-nixd login`), and post-build events.
- **FlakeHub** — SemVer-based registry for publishing and discovering Nix flakes, with private flake support.
- **FlakeHub Cache** — binary cache with federated JWT authentication; `flakehub-push` GitHub Action publishes store paths automatically.
- **Determinate Secure Packages** — curated, vulnerability-scanned Nixpkgs snapshots for enterprise use.
- **Zero to Nix** — Determinate's flake-centric Nix learning resource at https://zero-to-nix.com.
- **FlakeHub CLI (`fh`)** — command-line tool for FlakeHub operations (init, publish, fetch, search).
