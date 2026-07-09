# DeterminateSystems/nix-installer

## Metadata
- Stars: 3,640
- Primary language: Rust
- Default branch: main
- Latest release: v3.21.5 (2026-07-08)
- License: GNU LGPLv2.1
- Homepage: https://determinate.systems
- Fetched: 2026-07-09
- Final URL: https://github.com/DeterminateSystems/nix-installer

## Description
Install Nix and flakes with the fast and reliable Determinate Nix Installer, with over 7 million installs.

## README
# Determinate Nix Installer

**Determinate Nix Installer** is the easiest and most reliable way to install Determinate Nix. The installer works across a wide range of environments, including macOS, Linux, Windows Subsystem for Linux (WSL), SELinux, the Valve Steam Deck, and more. It offers support for seamlessly uninstalling Nix, enables Nix to survive macOS upgrades, and offers a range of features that make it the industry standard for installing Nix.

By default, it installs Determinate Nix, which enables flakes and offers a variety of industry-leading features and improvements.

## Install Determinate Nix

This one-liner installs Determinate Nix on just about any supported system:

```shell
curl -fsSL https://install.determinate.systems/nix | sh -s -- install
```

The best way to get started with Determinate Nix on macOS is to use the macOS package (https://install.determinate.systems/determinate-pkg/stable/Universal), which uses Determinate Nix Installer behind the scenes but provides a highly intuitive graphical UI.

Determinate Nix Installer successfully completes **tens of thousands** of installs every day in a number of environments:

| Platform | Multi user? | `root` only | Maturity |
|---|---|---|---|
| Linux (`x86_64` and `aarch64`) | ✓ (via systemd) | ✓ | Stable |
| macOS (Apple Silicon / `aarch64`) | ✓ | | Stable |
| Valve Steam Deck (SteamOS) | ✓ | | Stable |
| WSL2 (`x86_64` and `aarch64`) | ✓ (via systemd) | ✓ | Stable |
| Podman Linux containers | ✓ (via systemd) | ✓ | Stable |
| Docker containers | | ✓ | Stable |

## As a GitHub Action

You can install Determinate Nix on GitHub Actions using `determinate-nix-action`. Example:

```yaml
on:
  pull_request:
  push:
    branches: [main]

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DeterminateSystems/determinate-nix-action@v3
      - name: Run `nix build`
        run: nix build .
```

The action is updated and tagged for every Determinate release. `DeterminateSystems/determinate-nix-action@v3` installs the most recent release in the `v3.x.y` series.

## Planners

Determinate Nix Installer installs Nix by following a _plan_ made by a _planner_. To review the available planners:

```shell
/nix/nix-installer install --help
```

You can configure planners using environment variables or command arguments:

```shell
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  NIX_BUILD_GROUP_NAME=nixbuilder sh -s -- install --nix-build-group-id 4000
```

## Upgrading Determinate Nix

If you've installed Determinate Nix, you can upgrade it using Determinate Nixd:

```shell
sudo determinate-nixd upgrade
```

## Uninstalling

```shell
/nix/nix-installer uninstall
```

## On GitLab

GitLab CI runners are typically Docker-based and run as `root`, so `systemd` is not present. Pass `--init none`:

```yaml
test:
  script:
    - curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install linux --no-confirm --init none
    - . /nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh
    - nix run nixpkgs#hello
```

## Without systemd (Linux only)

When `--init none` is used, _only_ `root` or users who can elevate to `root` can run Nix.

```shell
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  sh -s -- install linux --init none
```

## In a container (Docker/Podman)

```dockerfile
FROM ubuntu:latest
RUN apt update -y
RUN apt install curl -y
RUN curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install linux \
  --extra-conf "sandbox = false" \
  --init none \
  --no-confirm
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
RUN nix run nixpkgs#hello
```

## Top-level structure
- `.cargo/` — Cargo workspace config
- `.github/` — CI workflows (ci.yml, release)
- `src/` — Rust source (planner logic, action implementations)
- `nix/` — Nix build support
- `docs/` — Troubleshooting guide and additional docs
- `tests/` — Integration test suite
- `flake.nix` — Nix flake definition
- `Cargo.toml` — Workspace manifest
- `nix-installer.sh` — Shell wrapper script
- `README.md` — Full documentation
