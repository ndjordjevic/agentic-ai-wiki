# anomalyco/hex

## Metadata
- Stars: 1105
- Primary language: Rust
- Default branch: dev
- Latest release: app-v2.3.1 (2026-10-21)
- License: MIT
- Homepage: https://anoma.ly/hex
- Fetched: 2026-10-30
- Final URL: https://github.com/anomalyco/hex

## Description
Local-first voice dictation for macOS. Hold a shortcut, speak, and paste into any app. Native Rust, on-device speech recognition, and a Linux beta.

## README
<p align="center">
  <img src=".github/assets/hex-icon.png" width="96" height="96" alt="Hex app icon" />
</p>

<h1 align="center">Hex</h1>

<p align="center">
  <strong>Speak. It appears.</strong><br />
  Local-first voice dictation, built in Rust.
</p>

<p align="center">
  <a href="https://anoma.ly/hex/"><strong>Download for Mac, Windows, or Linux</strong></a>
  · <a href="docs/windows.md">Windows beta</a>
  · <a href="docs/linux.md">Linux beta</a>
  · <a href="sdk/typescript/README.md">TypeScript SDK</a>
  · <a href="CONTRIBUTING.md">Contributing</a>
</p>

Hex is local-first voice dictation for Apple silicon Macs running macOS 15 or
newer. Hold a shortcut, speak, and release. Hex transcribes on your Mac and
pastes the result into the app you are using.

- **On-device transcription.** Download a local speech model during setup;
  ordinary dictation does not require OpenCode or a cloud transcription service.
- **Your words, your way.** Choose a shortcut, language, and model. Use Modes for
  corrections, application-specific behavior, and optional text processing.

The macOS app is available now. The [Windows beta](#windows-beta) covers x64 and
ARM64 PCs, and the [Linux beta](#linux-beta) covers x86_64 X11 and compatible
wlroots Wayland compositors. See [Privacy and local data](#privacy-and-local-data)
for what stays on your device and what optional features send to a provider.

## Install Hex

### Downloads

Each link serves the current release: the newest dev build (published on
every change to `dev`, and updating itself from the Dev channel) until Hex's
first stable release, then the stable release.

| Platform | Download |
| --- | --- |
| macOS (Apple silicon) | [DMG](https://anoma.ly/hex/download/macos-arm64-dmg) |
| Windows x64 | [Installer](https://anoma.ly/hex/download/windows-x64-setup) |
| Windows ARM64 | [Installer](https://anoma.ly/hex/download/windows-arm64-setup) |
| Linux x86_64 | [Executable](https://anoma.ly/hex/download/linux-x64) |
| Linux x86_64 (Debian, Ubuntu) | [.deb](https://anoma.ly/hex/download/linux-x64-deb) |
| Linux x86_64 (Fedora, openSUSE) | [.rpm](https://anoma.ly/hex/download/linux-x64-rpm) |
| Linux ARM64 | [Executable](https://anoma.ly/hex/download/linux-arm64) |
| Linux ARM64 (Debian, Ubuntu) | [.deb](https://anoma.ly/hex/download/linux-arm64-deb) |
| Linux ARM64 (Fedora, openSUSE) | [.rpm](https://anoma.ly/hex/download/linux-arm64-rpm) |

Updater files: [macOS ZIP](https://anoma.ly/release/hex/desktop/dev/macos-arm64),
[Windows x64 EXE](https://anoma.ly/release/hex/desktop/dev/windows-x64),
[Windows ARM64 EXE](https://anoma.ly/release/hex/desktop/dev/windows-arm64).
Windows links work once Windows signing is configured. On Linux you can also
use `yay -S hex-bin` or the install script below.

With Homebrew:

```sh
brew install --cask anomalyco/tap/hex
```

Then launch Hex from Applications and complete setup.

The cask installs the same signed app and keeps its built-in updater. Existing
DMG installations can keep using **Check for Updates**; Homebrew does not migrate
or forcibly replace another app already named `Hex.app`.

Or install manually:

1. [Download the signed DMG](https://anoma.ly/hex/download/macos-arm64-dmg) and open it.
2. Drag `Hex.app` into Applications, then launch it.
3. Complete the permission and model steps in setup.

- **Microphone** lets Hex record while you dictate.
- **Accessibility** lets Hex notice its shortcut in every app and paste into the foreground app. Drag the Hex tile into the list. Hex does not need Input Monitoring.
- **Transcription model** downloads the speech model that runs locally.

Hex checks for signed updates automatically. Use **Hex > Check for Updates…**
to check immediately.

Organizations that manage app versions themselves can turn off in-app updates,
including manual checks, with the `DisableUpdates` Boolean in the
`anomaly.hex` preference domain. Deploy it in a configuration profile
(payload type `anomaly.hex`, key `DisableUpdates`, value `true`), or for a
single Mac run `defaults write anomaly.hex DisableUpdates -bool true`. On
Windows, set the DWORD `DisableUpdates` to `1` under
`HKLM\SOFTWARE\Policies\Anomaly\Hex` (Group Policy) or the same path in HKCU.
Relaunch Hex to apply it. Model downloads still work. Releases through 2.3.1
used the `com.kitlangton.hex2` domain; profiles for those keep applying only to them.

**Download blocked?** Each app release on [GitHub Releases](https://github.com/anomalyco/hex/releases)
has the identical signed files. App releases use `v…` tags (`app-v…` through
2.3.1); the repository also publishes separate TypeScript SDK releases.
If an older installation cannot check for updates on your network, install the
DMG manually over the existing Rust app.

On managed networks, ask IT to allow `anoma.ly`: Hex downloads and updates
from the Anomaly release service at `https://anoma.ly/release` (releases up to
2.3.1 use `https://anoma.ly/hex/files`). Local model setup separately needs `huggingface.co` and its model
download CDN. A successful
app download does not establish that those model hosts are reachable. After
restoring access, retry model preparation in Settings.

Coming from the original Swift app? Install the new app manually and complete
setup. Settings and history are not transferred. Quit the old app before
dictating in the new one so their shortcuts do not compete.

## Dictate Anywhere

Hold **Option**, speak, then release. Hex transcribes and pastes at the current
focus.

- Double-tap Option to keep recording; press Option again to finish.
- Press Escape to cancel. While recording, Escape discards the recording; after
  you release, it cancels the newest dictation that is still transcribing, so
  nothing is pasted for it.
- Press Option-Shift-V to paste the last completed dictation again.

Settings let you change the shortcut, microphone, language, local model,
recording behavior, feedback volume, launch-at-login behavior, and Dock
visibility. Corrections in Modes fix names and preferred spellings before text
is pasted; modes can also apply optional rewriting and text transformations.

Use **menu bar > Transcription Model** to switch between downloaded models without
opening Settings. Each model remembers its last selected language and, for
Whisper, recognition hints. Choose the language in Settings once, then switch
between combinations such as English with Parakeet and French with Whisper from
the menu. **Manage Models…** opens the full picker for downloads and language changes.

## Optional OpenCode Features

[OpenCode V2 beta](https://v2.opencode.ai/) (`opencode2`) is optional. Ordinary
dictation does not require it.

- **Post-processing:** enable OpenCode in Modes to rewrite a transcript before
  paste. Hex sends the transcript, foreground application, and Brave website
  hostname to the configured model provider. Modes can target applications and
  websites in Brave Browser.

If OpenCode rewriting fails, Hex keeps the corrected local transcript and still
runs any selected text transformations. If that transformation stage fails, Hex
keeps the text from before the stage, not partial transformation results.

## Annotate

Annotate records your screen while you draw on it and talk, then hands the
recording to an agent: its keyframes, your drawing, and a transcript of what
you said. It is on by default on macOS and Linux (Settings › Annotate; not on
Windows yet). Nothing is recorded, and no screen permission is asked for,
until you first use it.

- **One key:** **Option-Shift-S** on macOS, **F9** on Linux. Tap it to start
  and tap again to stop. While it records, hold it and move the pointer to
  draw, no click needed; let go and the mouse is the app's again. macOS asks
  for Screen Recording the first time; Linux asks through the desktop's
  screen-sharing dialog once, then remembers the screen. While it records,
  the dictation shortcut does nothing.
- **The bar:** the recording bar at the top shows the timer, a pen (click it
  to draw until you click it again; Esc stops drawing), stop, and ✕ to
  discard. On macOS, holding Shift draws too. Ink fades from the screen
  after about a second but stays in the recording.
- **Paste or send:** when it stops, the annotation is on your clipboard and
  the capsule offers **Paste** (the contact sheet, then the summary) and
  **Inspect**. With OpenCode running, **Send to…** lists its sessions (macOS
  also opens its suggestions by itself): click one to send it there, and Undo
  takes it back for a few seconds. A send carries the transcript and the
  pictures inline, so it works with an OpenCode server on another machine.
- `hex annotate list|show|send` (also `hex capture …`) reads and sends from the
  terminal.

## Custom Transformations

Advanced users can create `~/.config/hex/hex.config.ts` for deterministic
dictation transformations, written in TypeScript or JavaScript. Hex runs the
config itself in an embedded JavaScript engine and reloads it on save; nothing
else needs installing. `hex commands init` creates the starter workspace, and
`hex commands check` reports what the config registers or why it fails.

Config scripts get no filesystem, network, or process access.

To teach a coding agent how to configure personal transformations,
install the official Hex skill:

```sh
npx skills add anomalyco/hex --skill hex-personal-commands
```

The skill targets current Hex: dev builds now, and the next stable release.
On Hex 2.3.1, install the matching skill with
`npx skills add anomalyco/hex#app-v2.3.1 --skill hex-personal-commands`, or
[switch to the dev build](https://github.com/anomalyco/hex#install-hex).

## Read Transcripts From The CLI

The macOS release binary provides read-only queries while the app runs:

```sh
/Applications/Hex.app/Contents/MacOS/hex history --since 3d --app 'OpenCode Beta' --grep problems --json
/Applications/Hex.app/Contents/MacOS/hex meetings list --since 7d --json
/Applications/Hex.app/Contents/MacOS/hex meetings show latest --md
/Applications/Hex.app/Contents/MacOS/hex meetings search 'release schedule'
```

History supports `--until`, `--limit`, `--raw`, and `--oldest-first`; queries
respect the saved retention window. Meetings share the read-only MCP query
layer. No microphone, GUI, model, or app service starts.
See [flags and the versioned JSON schema](docs/transcript-cli.md).

## Privacy And Local Data

- Speech transcription runs locally.
- Hex does not save dictation audio by default.
- History retains successfully pasted dictation text
  for seven days by default, including the local transcript, final text, and
  limited application and timing metadata. It never stores audio, full browser
  URLs, or window titles. Every retention choice is capped at 10,000 entries and
  16 MiB of raw plus final text, with oldest entries evicted first.
- Use **History > Keep: Off** to stop adding entries, or **Clear all** to remove
  existing history. Turning retention off does not delete existing entries or
  disable diagnostic logging.
- An explicit `HEX_RETAIN_DICTATION_AUDIO` diagnostic setting can retain a
  bounded number of owner-only WAV files.
- Local diagnostic logs can contain transcript text, recognized command speech,
  foreground application names, and Brave URLs. Hex does not upload these logs.
- OpenCode features send the data described above to your configured model
  provider.
- Model installation and software updates require network access.

Review and redact diagnostics before sharing them.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Hex appears to disappear | Open Hex from its menu-bar hexagon. If the status item could not start, Hex keeps its Dock icon visible. |
| The shortcut does nothing | Open Hex and verify Microphone and Accessibility access. |
| Recording works but text does not paste | Verify Accessibility access. |
| Transcription does not start | Confirm that the selected local model is installed. |
| OpenCode features fail | Verify the separate OpenCode installation and model provider. |
| Website context does not match | Website-aware modes currently require Brave Browser. |

Permission changes may require quitting and reopening Hex.

Still stuck? [Report a bug](https://github.com/anomalyco/hex/issues/new?template=bug_report.yml)
with your Hex version, operating system, and steps to reproduce. Review and
redact any attachments; do not upload private dictation, recordings, or full logs.

Diagnostics are stored at:

- macOS: `~/Library/Application Support/hex/logs/`
- Windows: `%APPDATA%\hex\logs\`
- Linux: `~/.local/share/hex/logs/`, or under `XDG_DATA_HOME`

## Windows Beta

The Windows beta runs on Windows 10 and 11, x64 and ARM64. It covers hotkey
dictation (Hold or Toggle, `Ctrl+Space` by default), Modes,
History, a tray icon, and signed self-updates. On x64 with a Vulkan graphics
driver, Parakeet Unified English streams while you speak, so text arrives within
about 100 ms of release even after minutes of talking; ARM64 transcribes on the
CPU. Meetings and the local transcription API are not included.
Download the installer for
[x64](https://anoma.ly/hex/download/windows-x64-setup) or
[ARM64](https://anoma.ly/hex/download/windows-arm64-setup)
and run it; it installs for your user without administrator rights. It is not
code-signed yet, so SmartScreen may warn: choose **More info**, then **Run
anyway**. See the [Windows guide](docs/windows.md) for details or to build from
source.

## Linux Beta

The Linux beta targets x86_64 Linux on i3/X11 and compatible wlroots Wayland
compositors. It supports local hotkey dictation, Modes, History,
the Hex window, and signed updates for direct installs. With a Vulkan graphics driver, dictation
streams while you speak, as on macOS and Windows. Native Wayland requires
compositor support for clipboard and layer-shell protocols; paste uses `wtype`
with the virtual keyboard protocol, or the desktop's RemoteDesktop portal (KDE,
GNOME).
Shortcuts come from the desktop's GlobalShortcuts portal, or you bind
`hex dictation start` / `stop` / `toggle` in your compositor; see the
[Linux guide](docs/linux.md#shortcuts). Meetings are not
included.

Install the signed release on x86_64 Arch Linux (glibc 2.44 or later) with:

```sh
curl -fsSL https://anoma.ly/hex/files/install-linux.sh | sh
```

Until Hex has a stable release on the release service, this installs the
newest dev build, which keeps updating from the Dev channel
(`HEX_INSTALL_CHANNEL=stable` or `=dev` picks one explicitly).

From the next release on, Arch users can instead install the AUR package
`hex-bin` (for example `yay -S hex-bin`), which pacman updates; it is not on the
AUR yet.

The [Linux installation guide](docs/linux.md) covers inspecting the installer
first, uninstalling, and building from source. It also describes
requirements and limitations.
For Nix/NixOS packaging and per-user autostart, see the [Nix guide](docs/nix.md).

## Testing Builds

Every push to `dev` produces unsigned test builds for macOS, Windows, and
Linux in the [Test builds](https://github.com/anomalyco/hex/actions/workflows/test-builds.yml)
workflow. Open the latest green run and download from its summary. The
[test build guide](docs/test-builds.md) explains how to install and remove each
one without disturbing an installed Hex.

## Build With Hex

[`@kitlangton/hex`](sdk/typescript/README.md) brings local transcription to your
own application through Promise and optional Effect APIs. Your app supplies the
recorded audio; Hex handles model preparation and transcription.

The SDK is published on [npm](https://www.npmjs.com/package/@kitlangton/hex), but
a bundled native helper is not yet published. You must supply a compatible Hex
executable. Follow the [SDK guide](sdk/typescript/README.md) for requirements and
examples.

## Contributing

Issues are welcome, including detailed diagnoses and proposed fixes. Hex's team
writes every change, so pull requests from outside the team aren't accepted; we
credit your analysis in the pull request that fixes it. See
[`CONTRIBUTING.md`](CONTRIBUTING.md).

Architecture, development commands, active plans, and historical research are
indexed in [`docs/README.md`](docs/README.md), with development rules in
[`AGENTS.md`](AGENTS.md). Report vulnerabilities through the process in
[`SECURITY.md`](SECURITY.md).

Hex is available under the [MIT License](LICENSE).
Vendored icon licenses are listed in [Third-Party Notices](THIRD_PARTY_NOTICES.md).


## Docs

### docs/windows.md
# Windows Beta

The Windows port is a beta with a Rune desktop app (a tray process; see
[The app](#the-app)), WASAPI capture,
local `transcribe.cpp` transcription, a global shortcut, and generation-safe
automatic paste. Its daily-use surface includes live microphone, model, and
shortcut settings, Hold or Toggle shortcut modes, double-tap lock, Paste Last
Dictation, recording tones, a click-through HUD, retained History, text
replacements, a resident system tray, and per-user Launch at login. Global and
contextual Modes can rewrite completed dictation through the same
deadline-bounded OpenCode processing policy as macOS, then run ordered built-in
or user-defined TypeScript transformations.

The default shortcut is `Ctrl+Space`. In **Hold** mode, hold both keys while
speaking and release Space to transcribe and paste. In **Toggle** mode, press
`Ctrl+Space` to start and again to finish. Only Escape cancels; holding a
modifier on its own does nothing. Hex consumes the chord while it matches, so
applications and input methods no longer see `Ctrl+Space`; rebind it in Settings
if you rely on that chord elsewhere. To let another app use the same key, such as
a Discord push-to-talk key, turn on **Share dictation shortcut with other apps**
under Advanced: Hex still reacts to it but passes its key-down and key-up on,
which can also trigger that binding in other apps. In Hold mode, tap the shortcut twice within
300 ms to lock recording, then press it again to finish. Paste Last defaults to
`Ctrl+Alt+V`. Settings changes apply live or through an automatic listener
restart.

The Settings card reads **Enabled** when the shortcut works system-wide in every
app and **Disabled** when it does nothing.

## Install

Download and run the installer for your PC:

- x64: [`HexSetup.exe`](https://anoma.ly/hex/download/windows-x64-setup)
- ARM64: [`HexSetup.exe`](https://anoma.ly/hex/download/windows-arm64-setup)

Until Hex's first stable release these are the newest dev build, which keeps
updating itself from the Dev channel; afterwards, the stable release.

[anoma.ly/hex](https://anoma.ly/hex/) picks the right one. The
installer needs no administrator rights: it installs for the current user,
adds Hex to the Start menu and to **Settings › Apps** for uninstalling, and
opens Hex, whose first run downloads a speech model. Releases built once
Anomaly's Azure Artifact Signing is configured are Authenticode-signed
([windows-signing.md](windows-signing.md)). Until then, and while a new
publisher builds SmartScreen reputation, SmartScreen may say it protected your
PC; choose **More info**, then **Run anyway**.

**x64** decodes on the GPU through Vulkan and needs a current NVIDIA, AMD, or
Intel graphics driver (it supplies `vulkan-1.dll`); the installer stops with an
explanation when it is missing. **ARM64** decodes on the CPU. Both are
self-contained: no Visual C++ Redistributable is required. Hex then keeps
itself current through the signed update feed. Uninstalling removes every
installed version, the shortcut, and Launch at login, and keeps settings, logs,
history, and models in `%APPDATA%\hex`.

The installer and the script below create the same managed layout, so either
can replace the other. For a scripted install:

```powershell
powershell -ExecutionPolicy Bypass -Command "iwr https://anoma.ly/hex/files/install-windows.ps1 -OutFile install-windows.ps1; ./install-windows.ps1"
```

Uninstall a script install with `install-windows.ps1 -Uninstall`.

## Known Issues

**Discord shows "Playing HEX: Shards of Fate"**
([#445](https://github.com/anomalyco/hex/issues/445)). With game activity
detection on, Discord Desktop matches the running `hex.exe` to the verified game
*HEX: Shards of Fate*. It then shows that game on your profile for as long as
Hex runs. The reporter's local test suggests Discord matches on the executable
name. Hex keeps the name `hex.exe` because the installer, updater, Start Menu
shortcut, and Launch at login all use the managed
`%APPDATA%\hex\versions\<version>\hex.exe` path. The problem has been reported
to Discord. Until Discord fixes its game list, open Discord's
**Settings › Registered Games** (or **Activity Privacy**) and hide the detected
entry, or turn off activity sharing there. Hex works the same either way.

## Streaming Dictation

With Parakeet Unified English on a GPU, Hex streams audio into the model while
the shortcut is held, so release only decodes the last one to two seconds. The
same engine streams on macOS (Metal) and Linux (Vulkan). Each dictation logs
`source=stream` or `source=fallback` in `logs\process.log`; a stream that fails,
stalls past its deadline, or returns nothing falls back to transcribing the
whole clip. CPU devices (including ARM64) always use the whole-clip path. Set
`HEX_STREAMING=0` to force the whole-clip path. See
[dictation](features/dictation.md#streaming-finish).

## Requirements For Source Builds

- 64-bit Windows 10 or 11, x64 or ARM64.
- PowerShell 7 or Windows PowerShell 5.1.
- `winget` from Microsoft App Installer.
- Visual Studio C++ Build Tools, CMake, and the stable MSVC Rust toolchain.
- x64: the Vulkan SDK (`VULKAN_SDK` set), for the GPU backend.
- ARM64: Visual Studio's clang-cl and Ninja; ggml's ARM CPU backend refuses
  MSVC. Build with `CC=clang-cl`, `CXX=clang-cl`, `CMAKE_GENERATOR=Ninja`, and
  `TRANSCRIBE_CMAKE_ARGS=-DGGML_NATIVE=OFF -DGGML_OPENMP=OFF`, as
  `.github/workflows/check-windows.yml` does.

`.cargo/config.toml` links the C and C++ runtimes statically. Distributed builds
also set `TRANSCRIBE_CMAKE_ARGS=-DGGML_NATIVE=OFF`; without it ggml tunes its
CPU kernels to the build machine and the binary can crash on older CPUs.

Run the checked-in setup script from the repository root. It keeps an existing
compatible Visual Studio installation and installs only missing prerequisites.

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-windows.ps1
```

The script also installs `rustfmt`, Clippy, and rust-analyzer, fetches Cargo
dependencies, and runs `cargo check --all-targets`.

## Smoke Test

List WASAPI inputs and the compute backends visible to `transcribe.cpp`:

```powershell
cargo run -- devices
cargo run -- model devices
```

Install the default English model, load it, and transcribe a WAV file:

```powershell
cargo run -- model install
cargo run -- model check
cargo run -- model transcribe .\sample.wav
```

For Polish, select the multilingual Parakeet model explicitly:

```powershell
cargo run -- model install --model parakeet_v3 --language pl
cargo run -- model check --model parakeet_v3 --language pl
cargo run -- capture --model parakeet_v3 --language pl --copy
```

Open the desktop application after the model is installed:

```powershell
cargo run -- app
```

The Settings card reads **Enabled** when the shortcut works system-wide in every
app and **Disabled** when it does nothing; its button and the tray's
**Enable / Disable Hex** switch between them. Hex enables itself on launch by
default (**Enable on launch**). The microphone records only while you dictate.
Changing the
transcription model, microphone, dictation shortcut, double-tap behavior, or
Paste Last setting automatically restarts the listener; you do not need to
stop it first. Text replacements and feedback volume apply without a model
reload. Mode rules, OpenCode profiles, and ordered transformations are
snapshotted by the output worker and apply to the next completed dictation
without restarting capture. The command-line listener uses the settings saved
by the app:

```powershell
cargo run -- listen --model parakeet_v3 --language pl
```

`capture` prewarms the selected model and opens the microphone before prompting.
Press Enter once to start, then again to stop. Captures shorter than 300 ms are
discarded. `--device` accepts a case-insensitive fragment from `devices`.

Runtime data is stored under `%APPDATA%\hex`. Observations are in
`logs\live.ndjson`, and native/runtime diagnostics are in `logs\process.log`,
including every panic with its thread and backtrace. A worker that stops
unexpectedly leaves its cause there. The app detaches from its console at
launch, so it has no stdout or stderr.
Successful pasted dictations are retained, subject to the selected retention
window and hard size limits, in `history.json`. Captured audio is never retained
by default.

## Custom Transformations

The Transformations card in Modes always offers the built-in transformations.
Choose **Set up** there to create `~/.config/hex/hex.config.ts` and load any
transformations registered by that config. Hex runs the config in its embedded
JavaScript engine (QuickJS), so nothing else needs installing.

Transformations run in the displayed order after mode corrections and the
optional OpenCode rewrite. Reordering, adding, or removing them persists in the
global or contextual mode and applies to the next output job. Each
transformation call is limited to one second and the engine to 64 MiB; a
failed step preserves the previous pipeline output. Saving the config reloads
it; a config that fails to load keeps the previous one and shows its error in
the card.

## The App

`hex app` (`--hidden` for a login launch) runs the tray app on Rune. Snapshot
fixtures without starting anything: `hex app -- --snap out.png --scene modes`.

```ts
hex app
├── named event already held -> signal it (the running app shows its window) -> exit
└── becomes the app                                   // windows_rune::open
    ├── runtime thread: WindowsDesktopHost (listener, model preparation, OpenCode, transformations, updater), publishes every 250 ms
    ├── main thread: rune::App's winit loop and the window; rune::Tray runs on its own thread
    ├── --hidden -> windowless start; close -> hide (keep_running)
    ├── tray Show or a relaunch -> AppHandle::open (shows and focuses)
    └── tray Quit / Ctrl-C / restart into an update -> AppHandle::quit -> runtime stops the listener
```

- Quit Hex in the window or the tray stops the listener and ends the app;
  closing the window only hides it.
- The window uses the shared Rune panes (General, Modes,
  History, the transcription picker, first-run setup) with Windows rows:
  Launch at login (the current-user Run key), no terminal-paste row. The
  sidebar footer holds Check for updates, and Download update for unmanaged
  installs. Shortcuts are recorded by
  polling the keyboard with the listener's hook suspended, because modifier-only chords never reach the window as key events.
- Models are prepared in-process through `transcription_preparation`; the
  runtime saves the selection when it is ready and restarts the listener.
- Enable on launch waits until first-run setup has recorded completion.
- The dictation HUD is a Rune overlay (`rune_hud.rs`, shared with Linux): a
  HUD thread steps the shared indicator model and Dot scope, and the
  overlay's compositor draws each frame on the GPU with `rune_hud.wgsl`; Rune shows it in a topmost tool window
  with `WS_EX_NOACTIVATE|WS_EX_TRANSPARENT|WS_EX_LAYERED`, shown with
  `SW_SHOWNOACTIVATE`, 12 pt from the top or 24 pt above the taskbar. The
  same model, shaders, and overlay run on Linux; on Windows it is only
  type-checked.
- The window gets the executable's icon from Rune's `App::on_window` hook
  (its HWND through `WindowHandle::with_raw_handle`) for the taskbar,
  Alt-Tab, and the caption. The native title bar keeps its icon and title,
  blended into the window: DWM paints the caption the theme's `bg_deep`
  (`DWMWA_CAPTION_COLOR`, Windows 11; Windows 10 keeps its own caption
  color). The view repaints it when the system theme switches.
- Without a tray (creation failed) closing the window quits Hex.
  See the [single-process plan](plans/single-process.md#windows-under-rune).

**This app has never run on Windows.** Earlier releases shipped a GPUI app
that a person did run; that app is gone, and the Rune app replaces it in the
next release, so a person must run it on Windows (x64 and ARM64) before that
release. It is type-checked by cross-compiling on Linux with
[cargo-xwin](https://github.com/rust-cross/cargo-xwin):

```sh
rustup target add x86_64-pc-windows-msvc && cargo install cargo-xwin
# clang-cl, lld-link, and llvm-lib must be on PATH (llvm-lib can be a
# symlink to rustup's llvm-tools llvm-ar).
mkdir -p /tmp/no-transcribe/lib
echo '{"libraries":[],"shared":false}' > /tmp/no-transcribe/lib/transcribe-link.json
# TRANSCRIBE_DIR skips the transcribe.cpp/Vulkan CMake build; nothing links in check.
TRANSCRIBE_DIR=/tmp/no-transcribe cargo xwin clippy --target x86_64-pc-windows-msvc \
  --all-targets -- -D warnings
```

For ARM64, add the `aarch64-pc-windows-msvc` target and set
`XWIN_CROSS_COMPILER=clang`: ring's aarch64 build forces the GNU-style
`clang` driver, which rejects the clang-cl `/imsvc` flags cargo-xwin passes
by default. Also set `CARGO_FEATURE_NO_NEON=1`: blake3 (through Rune) builds
NEON C that the xwin sysroot's `arm64_neon.h` macros break under that driver.

That checks every Rust path, including Rune, wgpu's DX12 and Vulkan
backends, and the Windows modules; it compiles C build scripts (ring) for
the target but never links, builds transcribe.cpp, or runs anything.

## Local Transcription Service

Not available on Windows in this build. The `windows-shell` branch generalized
the authenticated local API (`service` and `service --embedded`) across
platforms, but `dev` has since reshaped it for macOS; porting it onto that
version is follow-up work.

## macOS Parity

The target is product and visual parity with macOS, using native Windows
adapters where the operating-system APIs differ. A direct copy of AppKit,
CoreAudio event taps, Metal, `SMAppService`, Accessibility, or
ScreenCaptureKit code would not run on Windows; the Windows implementation must
preserve the same user contract through Win32, WASAPI, Rune (wgpu), the
current-user startup registry, UI Automation, and Windows capture APIs.

| Area | Windows status |
| --- | --- |
| Local hold-to-dictate, Toggle mode, timestamped boundaries, Escape, paste | Implemented |
| Live model, shortcut, and microphone selection | Implemented |
| Double-tap lock and Paste Last Dictation | Implemented |
| Clipboard preservation and generation-safe restoration | Implemented |
| Recording tones and click-through recording/processing HUD | Implemented; a CPU port of the macOS Metal shader drawn in a Rune overlay, never run on Windows |
| History retention, list, detail, search, copy, delete, and clear | Implemented |
| Text replacements | Implemented in the Windows Modes pane using the shared phrase-boundary replacement engine |
| Application picker in Modes | Implemented; lists Start menu shortcuts, App Paths, and apps with an open window, with each executable's icon; "Choose a file…" opens the native dialog through `rune::FileDialogs` |
| Interface language | Implemented on every OS; English, Polish, Chinese, Japanese, German, Spanish, and Ukrainian |
| Resident tray and Launch at login | Implemented |
| Application modes with per-mode corrections, OpenCode rewriting, and transformations | Implemented on the shared ordered processing policy; global and contextual profiles persist their own corrections, model, reasoning variant, deadline, and ordered built-in/TypeScript transformations, while modes match by application name — physical end-to-end paste/UI validation remains |
| Recognition hints for Whisper-family models | Implemented |
| Release microphone while idle | Implemented; mutually exclusive with audio pre-roll, as documented in Settings |
| While-dictating audio control (mute other apps or pause media) | Implemented via WASAPI session volumes and GSMTC |
| Signed automatic self-update for managed installs | Implemented for x64 and ARM64; the same ed25519 key and `https://anoma.ly/hex/files` origin as Linux, one feed per architecture, activating into a user-local versions directory. Checks 10 s after launch and every 6 h (or Check for updates); a staged update shows Restart to update in the tray menu and the window's sidebar footer, and the tray tooltip says an update is available. Source builds keep the GitHub release link (Download update); CI test builds never check |
| Web-domain mode rules and browser context via UI Automation | Implemented; the page URL comes from the browser's UIA document element, bounded so a hung provider degrades to application-only context |
| Managed installer with Start Menu integration and clean uninstall | Implemented as `.github/release/install-windows.ps1`; it creates the self-updating versions layout, and updates retarget the managed shortcut and Launch-at-login entry |
| First-run onboarding | Implemented; a fresh install picks a dictation language, downloads its recommended model with live progress, and starts listening only once setup is recorded — the shared Rune tour |
| Activity pane with the live session and recent transcripts | Implemented in developer builds; the shared read-only pane |
| Developer Meetings, live drafts, and meeting paste | Missing |
| Local transcription API and public TypeScript SDK host lifecycle on Windows | Missing; see Local Transcription Service |
| Streaming finish with whole-clip fallback | Implemented on GPU devices with Parakeet Unified English |

Settings live in `%APPDATA%\hex\settings.json`, the same file macOS and
Linux use.

The Windows window uses the shared design system
([design-system.md](design-system.md)): the same Rune panes as macOS and
Linux under the native title bar. Mode processing, OpenCode rewriting, and transformations run
through the same `dictation_processor` and `personal_commands` modules as
macOS; Windows reaches OpenCode through the `opencode2 api` CLI. Like macOS,
an unset OpenCode model tries the ranked recommended models before the
OpenCode default.
Remaining panes should be added only with their complete Windows behavior;
empty look-alike screens do not count as parity.

## Current Port Boundary

The Windows listener preserves physical press/release timestamps, keeps audio
capture off the transcription and paste worker, and restores the previous
clipboard only when no newer clipboard change supersedes it.
`check-windows` builds and tests the optimized MSVC release for x64 and ARM64
on every pull request. The remaining code
parity slice is the developer-only Meetings surface after the physical matrix
is green. Shared
first-run onboarding, complete OpenCode mode rewriting controls, and the bounded
TypeScript transformation host already ship. Windows releases are built for
x64 and ARM64 by
[`release.yml`](../.github/workflows/release.yml) with
[`scripts/build-windows.sh`](../scripts/build-windows.sh), Authenticode-signed,
and published to the Anomaly release service with the other platforms
(`docs/releasing.md`); [`.github/release/install-windows.ps1`](../.github/release/install-windows.ps1)
installs from its stable manifest. Users install
with the command under [Install](#install).


### docs/linux.md
# Install The Linux Beta

The Linux beta targets x86_64 and ARM64 (aarch64) Linux: i3/X11 and compatible wlroots-based Wayland
compositors such as Hyprland or Sway. Audio uses ALSA, including PipeWire systems
with ALSA compatibility. Inference uses Vulkan when available and can fall back
to the CPU. The window still needs a Vulkan driver, even with CPU
inference; `vulkan-icd-loader` alone is not a driver. Install a driver for your GPU
or a software Vulkan driver. See the Wayland requirements below.

Linux opens the same window as macOS and Windows: Settings, Modes,
and History. Website mode rules and meetings are macOS-only.
Paste on Wayland uses `wtype` where the compositor offers the virtual keyboard
protocol (wlroots compositors, niri) and the desktop's RemoteDesktop portal
elsewhere (KDE, GNOME). Shortcuts are general: the desktop's GlobalShortcuts portal when it has one, otherwise
your desktop's own keybindings running `hex` commands (see
[Shortcuts](#shortcuts)).

For Nix/NixOS, use the [Nix guide](nix.md). Nix owns updates to that installation;
Hex's signed updater owns only the direct-install layout below.

## One Hex Process

Hex on Linux is **one process per user** (and per data directory), not a
system-wide/root daemon. It owns the microphone, shortcuts, model downloads and
workers, sounds, paste, History, the recording pill, and the window. The window
is optional: closing it stops neither dictation nor a model download, and
launching Hex again opens it. When the desktop has a tray (a
StatusNotifierItem host, such as Waybar, KDE, or Omarchy's bar), Hex shows a
tray icon: click it to open the window, or use its menu's **Show Hex** and
**Quit Hex**. Without a tray, quit with **Quit Hex** at the bottom of the
window's sidebar, the launcher's **Quit Hex** action, or `hex quit`.

The window opens at 980×760 logical pixels and floats on tiling window
managers with no window rule: it maps with its minimum size equal to its
maximum, which sway, Hyprland, niri, and X11 managers such as i3 float, then
drops the maximum so you can resize it down to 860×560 or up to any size.
macOS and Windows open the same resizable window.

Settings live in `settings.json` in Hex's data directory, the same file macOS
and Windows use.

```sh
hex                             # open the window, starting Hex if needed
hex start                       # start Hex in the background; no window
hex status                      # query the running Hex, not an old log entry
hex quit                        # finish accepted work, release the microphone, exit
hex restart                     # restart the systemd unit in this desktop's environment
                                # (over SSH: the one it last ran in)
journalctl --user -u hex.service # diagnostics of the supervised process
```

`hex app` is the same as `hex`, `hex app --hidden` the same as `hex start`, and
`hex stop` the same as `hex quit`; older desktop and autostart entries keep
working after an update replaces only the executable.

A launch first asks the running Hex over its socket. If one answers, it
forwards `Activate` with the launcher's `XDG_ACTIVATION_TOKEN` or
`DESKTOP_STARTUP_ID` and exits 0; the running process opens or focuses its
window. If none runs and the installer's (or Home Manager's) `hex.service` user
unit is loaded, the launch writes an owner-only `session.env` and starts the
unit, which reports readiness to systemd (`Type=notify`) once its socket
answers, then forwards `Activate`. Otherwise (a custom data directory,
`cargo run`, a desktop without systemd) the launching process becomes Hex
itself. Two racing launches produce one Hex; the loser forwards and exits 0.

`session.env` holds the display and session variables, the cursor theme and
input method (`XCURSOR_THEME`, `XCURSOR_SIZE`, `XMODIFIERS`, `GTK_IM_MODULE`,
`QT_IM_MODULE`), and, when set, `XDG_DATA_DIRS` and the locale (`LANG`,
`LANGUAGE`, `LC_ALL`, `LC_CTYPE`, `LC_MESSAGES`). Missing display variables
explicitly clear stale Wayland/X11 values inherited by the user manager; missing
locale and data-directory variables are left to the user manager. No
permissions are granted. The unit is `PartOf=graphical-session.target`;
desktops managing a custom session target must bind its lifetime to their
login/logout lifecycle. Systemd restarts a crashed Hex (`Restart=on-failure`)
without a window; after **Update**, the restarted Hex reopens the window.
There is one Hex per user: a launch from another desktop session restarts the
supervised unit in the new session, and refuses to take over an unsupervised
one (quit it first).

The socket is owner-only in Hex's data directory, with same-user peer
credentials, versioned bounded frames, bounded queues, and I/O deadlines. It is
not a network API or the macOS embedded transcription SDK service. It carries
only `Activate`, the shortcut commands, `Status`, and `Quit`; shortcut commands
go straight from the socket to the listener, never through the window.

For development, run `cargo run --release`. `hex dictate` remains an explicit
foreground diagnostic listener without the window or HUD and cannot coexist
with Hex's listener. With
`HEX_APPLICATION_SUPPORT_DIR` set, launches never start, stop, or restart the
installed user unit; they forward to the Hex using that data directory or
become it. `HEX_SYSTEMD_UNIT` names another unit for isolated tests.
`hex status --lines 40` retains the explicit diagnostic-log view.

The window runs on Rune's app lifetime (`rune::App`): Hex starts it without a
window, each `Activate` opens or focuses it with the forwarded token (on
Wayland through `xdg_activation_v1`; without a token most compositors only
mark it urgent), and closing it keeps the window's state for the next open.

## Install A Published Build

Published builds exist for x86_64 and ARM64, as a bare executable, a `.deb`,
and an `.rpm`. They are built on Ubuntu 24.04 and need glibc 2.39 or later:
Ubuntu 24.04, Debian 13, Fedora 40, current Arch, or newer. ARM64 builds use
Vulkan like x64 and fall back to the CPU.

### Install script

The script installs the bare executable for your architecture into a
user-local layout (`~/.local/share/hex`) that updates itself. It installs the
stable release, or the newest dev build (on the Dev update channel) while
there is no stable release yet; set `HEX_INSTALL_CHANNEL=stable` or `=dev` to
choose:

```sh
curl -fsSL https://anoma.ly/hex/files/install-linux.sh | sh
```

If a runtime library is missing, the installer names the packages to install
(with Arch names). Then open Hex from your application launcher, or run
`~/.local/bin/hex`; its first run downloads a speech model.

To install the dependencies up front, or to inspect the installer before
running it:

```sh
sudo pacman -S --needed alsa-lib curl jq \
  libxkbcommon libxkbcommon-x11 libx11 libxcb openblas openssl util-linux \
  vulkan-icd-loader wl-clipboard wtype xxd
curl --proto '=https' --tlsv1.2 -fsSLO \
  https://anoma.ly/hex/files/install-linux.sh
less install-linux.sh
sh install-linux.sh
~/.local/bin/hex model install
~/.local/bin/hex
```

The installer verifies the signed release feed, exact artifact size, and
SHA-256 before installing. It uses no root access. It creates the managed
version layout, `~/.local/bin/hex`, a desktop launcher, and an XDG autostart
entry and a `hex.service` user unit. It does not start recording during installation.

Remove the application while preserving logs and settings with:

```sh
sh install-linux.sh uninstall
```

### Upgrading from 2.3.1

HEX 2.3.1 read every `/dev/input` device on Wayland, so it needed the `input`
group. Current builds don't: they use the GlobalShortcuts portal or `hex`
commands bound in your desktop (see [Shortcuts](#shortcuts)). Don't grant input
access; install the new build instead.

The new build is a separate install in `~/.local/share/hex` and imports
nothing from 2.3.1's `~/.local/share/voice-control`, so set up the model and
settings again. The installer refuses to replace 2.3.1's files, so remove them
first (the paths below assume the default XDG directories):

```sh
systemctl --user disable --now hex.service
rm -f ~/.config/systemd/user/hex.service ~/.local/bin/hex \
  ~/.local/share/applications/hex.desktop ~/.config/autostart/HEX.desktop
systemctl --user daemon-reload
rm -rf ~/.local/share/voice-control   # optional: 2.3.1's settings, logs, and models
curl -fsSL https://anoma.ly/hex/files/install-linux.sh | sh
~/.local/bin/hex model install
~/.local/bin/hex
```

On Hyprland, bind the shortcut in your config as described in
[Shortcuts](#shortcuts).

### Debian, Ubuntu, Fedora, and openSUSE

The `hex` package installs `/usr/bin/hex`, the desktop entry, and the systemd
user unit `hex.service` (the same files as the AUR package below). Download
it for your architecture from <https://anoma.ly/hex/download/linux-x64-deb>
(`linux-arm64-deb`, `linux-x64-rpm`, `linux-arm64-rpm`), then:

```sh
sudo apt install ./hex.deb            # Debian, Ubuntu
sudo dnf install ./hex.rpm            # Fedora (zypper install on openSUSE)
systemctl --user enable hex.service   # optional: start Hex at login
```

There is no apt or dnf repository yet. Hex never replaces a package-installed
executable: when a new stable release is out, Settings shows the command that
downloads and installs its package. Package installs follow the stable channel,
so a package from the dev channel learns of the next stable release only.

### AUR

From the next release on, the AUR package `hex-bin` installs `/usr/bin/hex`,
the desktop entry, and the systemd user unit `hex.service`, from the same
release executable, for `x86_64` and `aarch64`. It is not on the AUR yet. With
an AUR helper:

```sh
yay -S hex-bin
systemctl --user enable hex.service   # optional: start Hex at login
```

pacman updates it; Hex never replaces a package-installed executable, and
Settings says "Updated by your package manager". It is unrelated to the
official `hex` package (a hex dump tool that installs `/usr/bin/hx`).

## Install From Source

Install the native dependencies and, for a source build, the Rust toolchain:

```sh
sudo pacman -S --needed base-devel git rustup python alsa-lib curl jq openssl xxd \
  util-linux libxkbcommon libxkbcommon-x11 libx11 libxcb openblas \
  vulkan-headers vulkan-icd-loader \
  shaderc spirv-headers clang cmake pkgconf wl-clipboard wtype
rustup default stable
```

Build and install Hex as your desktop user:

```sh
git clone https://github.com/anomalyco/hex.git
cd hex
./scripts/install-linux.sh
~/.local/bin/hex model install
~/.local/bin/hex
```

Do not run the installer as root. It installs a user-local binary, desktop
launcher, and autostart entry in the same layout as published builds, and
marks the version as a source build (`source-build` beside the executable).
The in-app updater never replaces a source build; Settings shows "Updated from
your source checkout", and you update by pulling and running the installer
again. Installing a published release over it switches back to signed
updates. With a custom
`HEX_APPLICATION_SUPPORT_DIR`, `cargo run --release` runs an
unmanaged development Hex instead; without one it forwards to the installed Hex.

## Dictate

Hold **Alt-Space**, speak, then release. Double-tap the shortcut to keep
recording, press the same chord again to finish, or press Escape to cancel the
active recording. **Double-tap only** waits for two complete taps before
recording, and **Toggle** mode starts and stops with single presses.
**Ctrl-Alt-V** pastes the last dictation again. Settings shows listener state,
Start/Stop, and operational errors. Changing a shortcut or a setting the
listener reads at start temporarily stops listening and restores the previous
running state after the edit.

Modes apply corrections, OpenCode rewriting, and transformations per
application. On X11, Hex reads the frontmost application from the active
window's process name (`code`, `firefox`); the application picker lists
`.desktop` entries. Wayland doesn't report the focused window,
so the Global mode applies there. Completed dictations are kept in History.

**Microphone mode** can release the microphone between dictations; it then opens
on the shortcut press without pre-roll. **While dictating** can mute the default
output through `wpctl` (PipeWire) or `pactl` (PulseAudio), or pause playing
MPRIS media players over D-Bus, once the hold passes 300 ms, so shortcut chords
and short taps never do; Hex restores only what it changed.
Cancelling shortcut capture preserves the old binding unless the new binding
has already been saved; listening resumes only if it was previously running.

## Shortcuts

Hex gets its shortcuts one of three ways, and all of them drive the same
dictation rules:

- **X11:** Hex grabs the shortcuts Settings records.
- **Wayland with the GlobalShortcuts portal** (for example niri with
  `xdg-desktop-portal-gnome`, GNOME, or KDE): Hex asks the desktop for the
  shortcuts Settings records. The desktop decides: it may grant them, assign
  another key, or refuse one that it or another binding already uses. Settings
  lists what the desktop granted under **Desktop shortcuts**, with an error for
  any it refused. A desktop may keep an older binding when you record a new
  shortcut (KDE does); where its portal supports it, **Desktop shortcuts >
  Open** shows the desktop's own dialog for Hex's shortcuts, and Settings
  follows what you choose there. The portal identifies Hex by its installed
  `hex.desktop` entry and by inspecting the Hex process. A downloaded
  executable has no entry, so Hex writes a minimal
  `~/.local/share/applications/hex.desktop` that runs it (a managed install
  replaces it); if the portal still can't find it, restart the portal with
  `systemctl --user restart xdg-desktop-portal`. Run `hex service` directly:
  a setgid wrapper such as `newgrp`, once used to grant input-device access,
  makes the portal refuse Hex. The desktop delivers the keys to Hex, not to the
  focused application.
- **Hyprland** has the portal but takes every shortcut without a key, so
  nothing happens until you bind one in your config, and the key Settings
  records is not used. Hex can't tell whether your config binds it. Prefer
  keys without modifiers, because Hyprland adds every modifier you still hold
  to Hex's paste (see [Native Wayland Requirements](#native-wayland-requirements)). For example:

```lua
hl.bind("End", hl.dsp.global("hex:dictation"))
hl.bind("F9", hl.dsp.global("hex:paste-last"))
```

  Older Hyprland configs write `bind = , End, global, hex:dictation`.
  Escape-cancel can't be bound this way; bind `hex dictation cancel` to a key
  instead. Hyprland 0.56's Lua binds send no release when the modifier comes
  up before the key (Alt before Z); 0.57 fixes this. On 0.56, Toggle is
  unaffected: the next press still finishes. In Hold, recording continues
  until the next press and release, so lift the key first or use Toggle.
- **Wayland without the portal** (for example Sway): nothing registers global
  shortcuts. Settings lists these commands; bind them in your desktop's own
  keyboard configuration:

```sh
hex dictation start     # bind to a key's press: start recording
hex dictation stop      # bind to the same key's release: stop and transcribe
hex dictation toggle    # one key: start, then stop and transcribe
hex dictation cancel    # discard the recording
hex paste-last          # paste the last dictation again
```

For example, hold-to-dictate on F9 in Sway, and a toggle in any desktop that
runs commands on key presses only:

```sh
bindsym F9 exec hex dictation start
bindsym --release F9 exec hex dictation stop
bindsym Ctrl+Alt+d exec hex dictation toggle
```

`hex dictation stop --print` stops the same way, then waits up to 60 s and
writes the transcript to stdout instead of pasting it, after the same
processing a paste gets. Only that command waits; the listener stops
recording at once, so a following `start` isn't blocked. No speech exits 4
and prints nothing; a failure, cancel, or timeout prints nothing, exits 1,
and never pastes. History keeps the text as Printed, and Paste Last skips it.
See `docs/cli.md`.

The commands are safe to bind anywhere, including X11 beside the grabs. They
talk to the running Hex and never start it: without one, or while Hex is
not listening, they print a one-line error and exit non-zero. Starting while recording,
stopping while idle, and cancelling while idle do nothing, so key repeat is
harmless. Start and stop bypass Hold, Toggle, and double-tap: start records,
stop finishes. A shortcut press also finishes a recording a command started.

Escape cancels only while something records. On Wayland with the portal, Hex
binds Escape, and Escape with the recording shortcut's modifiers, only for the
length of the recording; the desktop then keeps that Escape from the focused
application. Without the portal, bind `hex dictation cancel` instead.

Shortcuts need a non-modifier key. Modifier-only shortcuts, such as Super
alone, are not supported on Linux.

On X11, Hex first grabs Escape with any modifiers. If another application owns
a modified Escape shortcut, Hex falls back to plain Escape with Caps/Num Lock
variants; release other modifiers before cancelling. If plain Escape also
conflicts, dictation continues and Settings and `hex status` show
`Escape cancel unavailable: another application holds Escape`. Finish with the
dictation shortcut instead. Hex logs once per conflict episode and retries on
the next capture; a successful grab clears the warning.

Recording sounds are enabled at 50% volume by default, including when upgrading
older settings. A start sound is queued immediately when the shortcut starts capture,
a stop sound marks the end of a retained recording (not completed transcription
or paste), and a cancel sound acknowledges cancellation of an active capture.
Brief taps still play the start sound, but recordings shorter than 300 ms remain
discarded and do not play the stop sound. **Sound volume** in Settings
offers Off, 25%, 50%, 75%, and 100%; changes save immediately without restarting
the listener and preview the start sound unless set to Off. `hex dictate` uses
the same saved volume. Playback uses the default audio output through a bounded
background worker; unavailable audio output does not prevent dictation.

Closing the window leaves Hex running on both X11 and Wayland. The
recording/processing pill never takes focus or intercepts clicks, with or
without the window open: a Rune overlay that is a layer-shell surface on
Wayland and an override-redirect window on X11. It needs the window's event
loop, so it is unavailable when the window cannot start (no display or GPU)
and in `hex dictate`. **Recording indicator** places it at the top or bottom of the
screen, or turns it off.

Insertion uses the clipboard and **Ctrl-V** for new installations. Enable
**Terminal paste shortcut** in Settings for targets that require **Ctrl-Shift-V**.
Existing X11 settings retain their previous Ctrl-Shift-V behavior until changed.
The target application must accept the selected binding.

After a paste, Hex puts the previous clipboard back, as on macOS
([#391](https://github.com/anomalyco/hex/issues/391)). Before writing the
transcript it reads every format the clipboard offers (text, rich text, images),
up to 32 MiB within one second, and 500 ms after the paste shortcut serves them
again from Hex until something else copies. It restores only if nothing newer
replaced the transcript in the meantime: a later dictation, a copy, or another
application. An empty clipboard stays empty. A larger or unreadable clipboard
is left holding the transcript, and Hex's log says why. When automatic paste
fails, the transcript stays on the clipboard for Ctrl+V. Nothing confirms the
target read the paste, so a target stalled past the delay can paste the
restored clipboard instead (see [#24](https://github.com/anomaly

## Top-level structure
- app/, macos/, native/, crates/, src/ — Rust app and crates
- docs/ — windows, linux, cli, features, releasing, …
- sdk/typescript/ — local transcription SDK for other apps
- skills/ — Agent Skills (e.g. hex-personal-commands)
- site/ — marketing site sources
- packaging/, nix/, flake.nix — packaging
- AGENTS.md, ROADMAP.md, SECURITY.md
