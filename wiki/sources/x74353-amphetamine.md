---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/x74353/Amphetamine
tags:
  - macos
  - keep-awake
  - closed-display-mode
  - applescript
  - power-management
  - system-utility
related:
  - tmux-tmux
  - wezterm.org
product: amphetamine
detail_level: standard
created: 2026-08-20
updated: 2026-08-20
---

This repo provides supplementary resources for Amphetamine, a popular free macOS app (distributed on the Mac App Store) that prevents a Mac from sleeping, locking the screen, or activating a screensaver. The GitHub repo itself is not the app's source — it hosts the **Power Protect** add-on: an AppleScript + sudoers configuration bundle that fixes a regression on Apple Silicon MacBooks where Amphetamine's Closed-Display Mode (clamshell mode) breaks when the laptop is connected or disconnected from external power. The fix requires manual installation because Apple's sandboxing restrictions prevent Amphetamine from doing it autonomously.

_All claims below are sourced from ../../raw/github/x74353-amphetamine.md unless otherwise noted._

## What it does

Amphetamine is a macOS menu-bar utility that keeps a Mac awake on demand — preventing sleep, screen lock, or screensaver activation during long-running tasks such as overnight AI agent runs, builds, downloads, or media playback. The supplementary repository addresses one specific failure mode: on Apple Silicon MacBooks, Closed-Display Mode (running the Mac with the lid closed, connected to an external display) stops functioning reliably when the power source changes. The Power Protect add-on monitors these power-source transition events with a background AppleScript and re-asserts the correct display-management state automatically.

## Key features

- **Power Protect script**: an AppleScript (`.scpt`) installed in Amphetamine's application-scripts sandbox path that monitors `NSWorkspace` power-change notifications and re-applies Closed-Display Mode after every power-source transition.
- **Sudoers configuration**: a `sudoers.d` entry (`PowerProtect_Configuration`) that grants passwordless privilege for the specific system call the script needs — required because privilege escalation dialogs cannot be displayed in clamshell mode.
- **Opt-in activation**: once files are installed, a single `defaults write` Terminal command enables the feature inside Amphetamine — explicit user intent required.
- **Apple Silicon targeting**: the fix targets the class of hardware (M-series MacBooks) and macOS versions where Apple's display-management API changed behavior; Intel-based Macs are unaffected.
- **MIT-licensed**: all scripts and configuration in the repo are available under the MIT License.

## Architecture

The repo is a minimal two-component add-on:

1. **AppleScript component** (`Files/powerProtect.scpt`) — runs inside Amphetamine's application-scripts directory (`~/Library/Application Scripts/com.if.Amphetamine/`). The script leverages the Apple Script `NSWorkspace` bridge to observe power-source changes and calls back into Amphetamine to re-assert its keep-awake state. No compiled binary or background daemon is installed separately; the script is invoked by Amphetamine itself.
2. **Sudoers component** (`Files/PowerProtect_Configuration`) — a minimal `sudoers.d` snippet installed at `/private/etc/sudoers.d/`. It grants passwordless `sudo` privilege for the one specific command the script needs, scoped to the current user, following least-privilege conventions.

The repo also ships compiled artifacts (`amphetamine_PowerProtect`) and localization strings but the only user-facing operational files are the two above.

## Installation

```bash
# 1. Install the AppleScript
cp ~/Downloads/PowerProtect_Script/powerProtect.scpt \
   ~/Library/Application\ Scripts/com.if.Amphetamine/

# 2. Install the sudoers config (requires admin password)
sudo cp ~/Downloads/PowerProtect_Configuration/amphetamine_PowerProtect \
   /private/etc/sudoers.d/

# 3. Enable the feature in Amphetamine
defaults write com.if.Amphetamine 'Enable Power Protect Install' -bool TRUE
```

## Example usage

Once installed and enabled, no further interaction is required. When Amphetamine is running in Closed-Display Mode and you plug in or unplug a power adapter or powered display, the Power Protect script fires automatically, re-asserts the keep-awake state, and logs the event. Long-running agentic AI workloads on Apple Silicon MacBooks — overnight code-generation runs, batch-ingest pipelines, model fine-tuning jobs — benefit from the combination of Amphetamine (staying awake) and Power Protect (surviving power-source changes without dropping clamshell mode).

## Maintenance status

- **Stars**: 119
- **Latest release**: none (resource-only repo; the app itself is distributed through the Mac App Store)
- **Last pushed**: 2023-10-24 (stable; the Power Protect mechanism has not needed updates since the Apple Silicon regression was addressed)
- **License**: MIT
- **Primary language**: AppleScript
