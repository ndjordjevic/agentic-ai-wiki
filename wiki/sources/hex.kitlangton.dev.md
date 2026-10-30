---
type: source
category: "Media, voice & content"
source_url: https://hex.kitlangton.dev
companion_urls:
  - https://github.com/anomalyco/hex
raw_files:
  - ../../raw/web/hex.kitlangton.dev.md
  - ../../raw/github/anomalyco-hex.md
tags:
  - local-voice-dictation
  - on-device-asr
  - rust-desktop
  - annotate-to-agent
  - opencode-optional
  - cross-platform
related:
  - wisprflow.ai
  - Starmel-OpenSuperWhisper
  - focusee.imobie.com
  - parakeet-ai.com
product: hex.kitlangton.dev
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

Hex (anomalyco/hex, ~1.1k★, MIT, app v2.3.1) is local-first voice dictation for Mac/Windows/Linux: hold a shortcut, speak, on-device ASR pastes at the cursor — with optional OpenCode post-processing, Annotate (screen+draw+talk → agent), CLI history, and a TypeScript SDK.

_All claims below are sourced from ../../raw/web/hex.kitlangton.dev.md unless otherwise noted._

## What it does

Hex downloads a local speech model at setup and transcribes without a cloud ASR dependency for ordinary dictation. Hold Option (configurable) to record; release to paste. Modes apply corrections and optional rewriting. Annotate captures screen + ink + speech for agent handoff. Marketing site redirects hex.kitlangton.dev → hex.kitlangton.com / anoma.ly/hex downloads.

## Key features

- On-device models (menu-bar model/language switch); no OpenCode required for basic dictation
- Double-tap Option for continuous record; Escape cancel; Option-Shift-V re-paste last
- Optional OpenCode V2 post-processing (app/site-aware rewriting)
- Annotate (macOS/Linux): Option-Shift-S / F9 → clipboard contact sheet + Send to OpenCode sessions
- `~/.config/hex/hex.config.ts` transformations + `npx skills add anomalyco/hex --skill hex-personal-commands`
- Transcript CLI (`hex history`, `meetings`, `annotate`) while app runs (../../raw/github/anomalyco-hex.md)

## Architecture

Native Rust desktop app (default branch `dev`) with platform packs under `macos/`, `app/`, `native/`, `crates/`. Local models via Hugging Face hosts; updates from Anomaly release service (`anoma.ly`). Optional Vulkan GPU path on Windows. TypeScript SDK under `sdk/typescript` for embedding local transcription in other apps. (../../raw/github/anomalyco-hex.md)

## Installation

Mac: DMG from downloads.hex.kitlangton.com or `brew install --cask anomalyco/tap/hex` (Apple silicon, macOS 15+). Windows: Setup.exe x64/ARM64 (Vulkan). Linux: install script or .deb/.rpm / `yay -S hex-bin`. GitHub release `app-v2.3.1` mirrors signed binaries. (../../raw/github/anomalyco-hex.md)

## Example usage

```sh
brew install --cask anomalyco/tap/hex
# Hold Option, speak, release → text pastes into focused app
npx skills add anomalyco/hex --skill hex-personal-commands
```
(../../raw/github/anomalyco-hex.md)

## When to use

- Developers who want offline dictation into Claude/IDEs (vs. cloud dictation like [[wisprflow.ai]])
- Agent workflows needing spoken Annotate bundles into OpenCode sessions
- Privacy-sensitive local ASR with optional LLM rewrite only when enabled

## Maintenance status

~1,105 stars, MIT, latest app release `app-v2.3.1` (2026-10-21), active `dev` branch (2026-10-30). Separate TypeScript SDK release tags. Org Anomaly / Kit Langton. (../../raw/github/anomalyco-hex.md)

## Ecosystem

llms.txt points at GitHub README/docs/SDK. Competes/complements [[wisprflow.ai]] and open ASR tools like [[Starmel-OpenSuperWhisper]]. Skill install via [[skills.sh]]-compatible `npx skills`.
