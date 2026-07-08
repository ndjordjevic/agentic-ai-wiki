---
type: source
source_url: https://github.com/Starmel/OpenSuperWhisper
tags:
  - macos-dictation
  - whisper-cpp
  - local-transcription
  - open-source
  - issue-fixing-agent
  - aider
related:
  - wisprflow.ai
detail_level: standard
product: opensuperwhisper
created: 2026-07-08
updated: 2026-07-08
---

OpenSuperWhisper is an open-source (MIT, 1,959+ stars) macOS dictation app that runs real-time audio transcription fully locally via whisper.cpp or the Parakeet engine, offering system-wide keyboard/mouse-triggered recording with no cloud dependency — the self-hosted counterpart to hosted voice-to-text products like [[wisprflow.ai]]. Notably, the repo also ships a small maintainer-side autonomous coding agent (`agent/`) that uses [Aider](https://github.com/Aider-AI/aider) over OpenRouter to pick up GitHub issues, implement fixes in the Swift codebase, and iterate on build failures.

_All claims below are sourced from ../../raw/github/Starmel-OpenSuperWhisper.md unless otherwise noted._

## What it does

OpenSuperWhisper records audio and transcribes it in real time on macOS (Apple Silicon), inserting text wherever the user is focused. Two transcription engines are supported — Whisper (whisper.cpp) and Parakeet (FluidAudio) — with models downloadable directly from the app. It targets the same "speak instead of type" niche as commercial products but keeps transcription entirely on-device.

## Installation

```shell
brew update # Optional
brew install opensuperwhisper
```

Or download from the GitHub releases page. Building from source requires `git submodule update --init --recursive`, `cmake`, `libomp`, `rust`, `ruby`, and `xcpretty`, then `./run.sh build`; CI builds are defined in `.github/workflows/build.yml`.

## Key features

- Global keyboard shortcuts, including single-modifier triggers (Left ⌘, Right ⌥, Fn)
- Mouse button trigger (middle button or an extra thumb button) to start/stop recording
- Hold-to-record mode alongside toggle mode
- Drag-and-drop audio files for queued transcription
- Microphone selection across built-in, external, Bluetooth, and iPhone (Apple Continuity) mics from the menu bar
- Multi-language support with auto-detection, plus Asian-language autocorrect for Japanese/Chinese/Korean output
- A dedicated Hebrew fine-tune (ivrit.ai's "Turbo V3 Hebrew," based on `whisper-large-v3-turbo`) selectable from Settings

## Architecture

The Swift app (`OpenSuperWhisper/`) is organized around `AudioRecorder.swift`, `TranscriptionService.swift`, `TranscriptionQueue.swift`, `WhisperModelManager.swift`, and an `Engines/` module abstracting the Whisper/Parakeet backends, with `ShortcutManager.swift`, `ModifierKeyMonitor.swift`, and `MouseButtonMonitor.swift` handling the various trigger inputs and `Indicator/`/`Onboarding/` covering UI. `libwhisper/` vendors the whisper.cpp integration as a git submodule, built as a static lib per `docs/build_whisper.md`. Whisper model `.bin` files are pulled from the Hugging Face whisper.cpp repository at runtime; a small default model ships bundled.

## Maintenance status

Actively maintained: 1,959 stars, 162 forks, MIT license, latest tagged release 0.1.0 (2026-03-03), most recent push 2026-07-06. Roadmap items tracked as a checklist in the README include streaming transcription, custom dictionary/keyword boosting, Intel macOS compatibility, and an "Agent mode" (open feature request, distinct from the maintainer-side `agent/` tooling below); background-app support and long-press single-key recording are already shipped.

## Ecosystem

The repo bundles a maintainer-only autonomous coding agent under `agent/` (not part of the shipped macOS app): `issue_agent.py` is an interactive CLI that lists open GitHub issues and, once one is picked, calls `coder.py` — a thin wrapper around Aider (model `openrouter/deepseek/deepseek-v4-flash` via OpenRouter) — to implement the fix directly in the Swift sources. `builder.py` drives Xcode builds and asks the model to fix compile failures (capped at `MAX_BUILD_FIX_ATTEMPTS = 3`), while `gitops.py` handles branch creation and stash-based worktree safety so tracked changes aren't clobbered. Issues are read from the public upstream repo but work lands on a separate private fork, keeping in-progress fixes out of public view until ready. This is a small but concrete example of an LLM-driven issue-to-PR loop wired directly into a real open-source project's contribution workflow, adjacent to the broader agentic-coding tooling covered elsewhere in this wiki (e.g. [[obra-superpowers]], [[eyaltoledano-claude-task-master]]).
