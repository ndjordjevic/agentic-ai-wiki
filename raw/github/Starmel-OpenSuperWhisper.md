# starmel/OpenSuperWhisper

## Metadata
- Stars: 1959
- Primary language: Swift
- Default branch: master
- Latest release: 0.1.0 (2026-03-03)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-08
- Final URL: https://github.com/Starmel/OpenSuperWhisper

## Description
macOS dictation app

## README
# OpenSuperWhisper

OpenSuperWhisper is a macOS application that provides real-time audio transcription using the Whisper model. It offers a seamless way to record and transcribe audio with customizable settings and keyboard shortcuts.

<p align="center">
<img src="docs/image.png" width="400" /> <img src="docs/image_indicator.png" width="400" />
</p>

## Features

- 🎙️ Real-time audio recording and transcription
- 🧠 Two transcription engines: [Whisper](https://github.com/ggerganov/whisper.cpp) and [Parakeet](https://github.com/AntinomyCollective/FluidAudio) — download models directly from the app
- ⌨️ Global keyboard shortcuts — key combination or single modifier key (e.g. Left ⌘, Right ⌥, Fn)
- 🖱️ Mouse button trigger — bind the middle or an extra (thumb) mouse button to start/stop recording
- ✊ Hold-to-record mode — hold the shortcut, modifier key or mouse button to record, release to stop
- 📁 Drag & drop audio files for transcription with queue processing
- 🎤 Microphone selection — switch between built-in, external, Bluetooth and iPhone (Apple Continuity) mics from the menu bar
- 🌍 Support for multiple languages with auto-detection
- 🇯🇵🇨🇳🇰🇷 Asian language autocorrect ([autocorrect](https://github.com/huacnlee/autocorrect))

## Installation

```shell
brew update # Optional
brew install opensuperwhisper
```

Or from [GitHub releases page](https://github.com/Starmel/OpenSuperWhisper/releases).

## Requirements

- macOS (Apple Silicon/ARM64)

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues in the repository
2. Create a new issue with detailed information about your problem
3. Include system information and logs when reporting bugs

## Building locally

To build locally, you'll need:

    git clone git@github.com:Starmel/OpenSuperWhisper.git
    cd OpenSuperWhisper
    git submodule update --init --recursive
    brew install cmake libomp rust ruby
    gem install xcpretty
    ./run.sh build

In case of problems, consult `.github/workflows/build.yml` which is our CI workflow
where the app gets built automatically on GitHub's CI.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

### Contribution TODO list

- [ ] Streaming transcription
- [ ] Custom dictionary / keyword boosting ([#19](https://github.com/Starmel/OpenSuperWhisper/issues/19))
- [ ] Intel macOS compatibility ([#15](https://github.com/Starmel/OpenSuperWhisper/issues/15))
- [ ] Agent mode ([#14](https://github.com/Starmel/OpenSuperWhisper/issues/14))
- [x] Background app ([#8](https://github.com/Starmel/OpenSuperWhisper/issues/8))
- [x] Support long-press single key audio recording ([#18](https://github.com/Starmel/OpenSuperWhisper/issues/18))

## License

OpenSuperWhisper is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Whisper Models

You can download Whisper model files (`.bin`) from the [Whisper.cpp Hugging Face repository](https://huggingface.co/ggerganov/whisper.cpp/tree/main). Place the downloaded `.bin` files in the app's models directory. On first launch, the app will attempt to copy a default model automatically, but you can add more models manually.

### Hebrew (ivrit.ai)

For Hebrew transcription, download the **"Turbo V3 Hebrew"** model from Settings → Model. It is [ivrit.ai](https://www.ivrit.ai/)'s Hebrew fine-tune of `whisper-large-v3-turbo` ([whisper-large-v3-turbo-ggml](https://huggingface.co/ivrit-ai/whisper-large-v3-turbo-ggml)) — the same base model as the other "Turbo V3" entries, but tuned for Hebrew. Selecting it automatically sets the input language to Hebrew, which these models require to be set explicitly.

## Docs

### docs/build_whisper.md
TBD

build .a static lib, move lib and headers to project. Include c++ std and other libs to the project linking.

```curl
cd ../.. && rm -rf build && mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_CXX_STANDARD=11 -DCMAKE_CXX_FLAGS="-fvisibility=hidden" -DWHISPER_BUILD_EXAMPLES=OFF -DWHISPER_BUILD_TESTS=OFF ..

make -j$(sysctl -n hw.ncpu)
```

### docs/release_build.md
## Release build

```shell
./notarize_app.sh $CODE_SIGN_IDENTITY 
```

Example:
```shell
./notarize_app.sh "Developer ID Application: AAAA BBBB (XXXXX)" 
```

## Top-level structure
- `.github/` — CI workflows (build.yml builds the app; boilerplate, not fetched)
- `.swiftpm/` — Swift Package Manager metadata
- `Bridge.h` — Objective-C/Swift bridging header
- `OpenSuperWhisper.xcodeproj/` — Xcode project
- `OpenSuperWhisper/` — main Swift app source: `AudioRecorder.swift`, `ContentView.swift`, `Engines/` (Whisper/Parakeet transcription engines), `Indicator/`, `MicrophoneService.swift`, `Models/`, `ModifierKeyMonitor.swift`, `MouseButtonMonitor.swift`, `Onboarding/`, `PermissionsManager.swift`, `Settings.swift`, `ShortcutManager.swift`, `TranscriptionQueue.swift`, `TranscriptionService.swift`, `Utils/`, `Whis/`, `WhisperModelManager.swift`
- `OpenSuperWhisperTests/`, `OpenSuperWhisperUITests/` — test targets
- `Scripts/` — build/support scripts
- `agent/` — **maintainer-side autonomous coding agent** (not part of the shipped app): `issue_agent.py` (interactive CLI: lists open GitHub issues, lets maintainer pick one), `builder.py` (drives Xcode builds, retries build fixes), `coder.py` (wraps [Aider](https://github.com/Aider-AI/aider) via OpenRouter, model `openrouter/deepseek/deepseek-v4-flash`, to implement the issue or fix failing builds), `gitops.py` (branch/stash management, git worktree safety checks), `github.py` (issue listing via GitHub API), `config.py` (config: base branch `master`, upstream repo public / fork repo private, `MAX_BUILD_FIX_ATTEMPTS=3`)
- `docs/` — `build_whisper.md`, `release_build.md` (both minimal/TBD), plus screenshots
- `libwhisper/` — whisper.cpp integration (git submodule)
- `asian-autocorrect` — submodule/dependency for CJK autocorrect
- `run.sh`, `make_release.sh`, `notarize_app.sh` — build/release scripts
- `ggml-tiny.en.bin`, `ggml-silero-v5.1.2.bin`, `jfk.wav` — bundled model/sample assets
