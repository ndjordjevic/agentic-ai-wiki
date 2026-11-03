---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/justrach/nanoui
tags:
  - zig-desktop-framework
  - native-gpu-ui
  - webview-ipc
  - agent-ergonomics
  - headless-ui-testing
  - nui-cli
  - liquid-glass
  - gpui-inspired
related:
  - composio-community-open-dot
  - felix-forever-hermes-agent-desktop
  - x.com-ericzakariasson-building-clis-for-agents
  - must-have-clis-2026
product: nanoui
detail_level: standard
created: 2026-11-03
updated: 2026-11-03
---

nanoui (690★, MIT, Zig 0.17, v0.11.0) is a desktop-app framework: each window is either a **native UI** drawn by nanoui on the GPU/CPU (no HTML/webview) or a **system webview** page with typed Zig↔TypeScript IPC. It matters to this wiki because it is explicitly built for coding agents as well as humans — `nui` scaffolds/tests/snapshots apps with `--json`, ships a detailed `AGENTS.md` (headless-only verification, 600-line file cap), and powers apps like **nanoterm** (terminal + coding agent) and **nanomon**.

_All claims below are sourced from ../../raw/github/justrach-nanoui.md unless otherwise noted._

## What it does

nanoui ports and extends the mygo/GPUI style of fast desktop UI into Zig: immediate-mode views, flexbox layout, Metal/OpenGL/CPU renderers, Liquid Glass, `ui.motion`, and a GPUI-Kit-inspired `nanoui.kit` component set — or, alternatively, WKWebView/WebView2 pages that call Zig through a generated `nanoui.js` / `nanoui.d.ts` client. Apps are small single binaries (~0.7 MB release); idle apps use no CPU (nothing polls). Cross-compile targets include macOS, Linux (GTK 3), Windows, iOS, and Android.

## Installation

```sh
git clone --recursive https://github.com/justrach/nanoui
cd nanoui
zig build run-gallery    # native UI tour
zig build run-hello      # webview example
zig build test
# or scaffold a new app (people + agents):
zig build nui && zig-out/bin/nui start my-app
# dependency in your project:
zig fetch --save git+https://github.com/justrach/nanoui#v0.11.0
```

Requires Zig 0.17.0; macOS needs Xcode/CLT; Linux needs GTK 3 at runtime.

## Key features

- **Dual content modes** — native GPU UI (Metal/CoreText on macOS; OpenGL/CPU elsewhere) or system webview with comptime-generated typed JS/TS bridge.
- **`nui` CLI** — non-interactive `start` / `test` / `snapshot` / `run` / `doctor` with `--json`; writes `AGENTS.md` into new apps so agents know how to verify look (`nui snapshot`) and behavior (`ui.Tester`).
- **Headless verification** — `ui.Tester` offscreen clicks/screenshots; app flags `--nanoui-snapshot`, `--nanoui-script`, `--nanoui-eval`, `--nanoui-wait` (no real-screen driving).
- **Agent hard rules** — every file ≤600 lines (`zig build lines`); never show windows on the developer’s screen while working; never synthesize OS-level input against the real desktop.
- **Kit + motion** — buttons/overlays/forms after GPUI Kit; springs, presence, layout animation, shared elements via `ui.motion`.
- **Platforms** — macOS, Linux, Windows, iOS, Android; release self-update from GitHub on macOS (`nanoui.Updater`).
- **Showcase apps** (submodules) — nanoterm, nanomon, nanomail, nanolight, nanostudio, nanofly, stageshow.

## Architecture

Public API lives in `src/nanoui.zig`. Native UI is `src/ui/` (context, flex layout, paint, Metal/OpenGL/raster, glass, motion, tester). Web content uses `page.zig` + platform webviews (`page_webkit`, `page_webview2`) and `tsgen.zig`/`bridge.js` for IPC. OS backends under `linux/`, `windows/`, `ios/`, `android/` with no C shims (`@cImport` forbidden — ObjC/Win32/GTK/JNI via comptime/`extern`/`dlopen`). `AGENTS.md` is the operating contract for contributors and coding agents.

## Example usage

```zig
const Counter = struct {
    n: i64 = 0,
    fn view(s: *Counter, c: *ui.Context) void {
        const col = ui.div(c).column().sizeFull().center().gap(16);
        defer col.end();
        ui.textf(c, .{ .size = 56, .weight = .bold }, "{d}", .{s.n});
        if (ui.button(c, "Increment", .{ .variant = .primary }).clicked) s.n += 1;
    }
};
// App.create → newWindow(.{ .content = .{ .view = .init(&state, Counter.view) } }) → run
```

Headless check: `zig-out/bin/gallery --nanoui-snapshot=shot.png --nanoui-script="click:Tasks"`.

## Maintenance status

690 stars, 29 forks, MIT, Zig primary language, default branch `main`, latest release **v0.11.0** (2026-11-03), actively pushed the same day. Inspired by / credits mygo, Zed GPUI, gpui-motion, and GPUI Kit (notices in `THIRD_PARTY_NOTICES.md`).
