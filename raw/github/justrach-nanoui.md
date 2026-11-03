# justrach/nanoui

## Metadata
- Stars: 690
- Forks: 29
- Primary language: Zig
- Default branch: main
- Latest release: v0.11.0 (2026-11-03)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-11-03
- Final URL: https://github.com/justrach/nanoui

## Description
Desktop apps in Zig, with native UI drawn on the GPU or a web frontend

## README
<p align="center">
  <img src="docs/images/nano-transparent.png" alt="Nano, nanoui's field mouse craftsperson, wearing a blue workshop jacket and holding a miniature app window" width="280">
</p>

<h1 align="center">nanoui</h1>

<p align="center">Desktop apps in Zig, with native UI drawn on the GPU or a web frontend.</p>

<p align="center"><sub>Meet Nano. <a href="docs/images/nano-transparent.png">Transparent PNG</a> · <a href="docs/images/nano-paper.png">Original paper illustration</a></sub></p>

<p align="center">Want to see it in use? <a href="https://github.com/justrach/nanoterm"><strong>nanoterm</strong></a> is a terminal with a coding agent, and <a href="https://github.com/justrach/nanomon"><strong>nanomon</strong></a> an activity monitor, both built on nanoui.</p>

<p align="center">
  <img alt="macOS · Linux · Windows" src="https://img.shields.io/badge/macOS%20·%20Linux%20·%20Windows-555">
  <img alt="Apps of about 0.7 MB" src="https://img.shields.io/badge/apps-~0.7%20MB-44cc11">
  <img alt="One dependency, the author's own http-zig, on Linux and Windows only" src="https://img.shields.io/badge/dependencies-1%20(own)-44cc11">
  <img alt="Built in Zig 0.17" src="https://img.shields.io/badge/built%20in-Zig%200.17-f7a41d?logo=zig&logoColor=white">
  <img alt="MIT" src="https://img.shields.io/badge/license-MIT-blue">
</p>

<p align="center">
  <a href="#get-started">Get started</a> ·
  <a href="#native-ui">Native UI</a> ·
  <a href="#web-pages">Web pages</a> ·
  <a href="#testing-without-a-window">Testing</a> ·
  <a href="#platforms">Platforms</a> ·
  <a href="#apps">Apps</a> ·
  <a href="#performance">Performance</a> ·
  <a href="#credits">Credits</a>
</p>

<p align="center">
  <img src="docs/images/nanomon-window.png" alt="nanomon, built on nanoui: the overview in Codegraff Light, with cell graphs of CPU, memory, GPU, disk and network" width="760">
</p>

Each window shows one of two kinds of interface:

- **Native UI**, written in Zig alone and drawn by nanoui: no HTML, no
  JavaScript, no webview. It has flexbox layout, text in a glyph atlas,
  animations, and views you can test without a window. On macOS it draws with
  Metal and CoreText, in one instanced draw call per frame.
- **A web page** in the system webview (WKWebView on macOS, WebView2 on
  Windows). The
  frontend calls Zig through a JavaScript client generated from your Zig
  types, with TypeScript declarations.

Apps are single binaries. Nothing polls, so an idle app uses no CPU.

## Get started

```sh
git clone --recursive https://github.com/justrach/nanoui
cd nanoui
zig build run-gallery    # the native UI tour
zig build run-hello      # the webview example
zig build test           # unit and widget tests
```

You need Zig 0.17.0, plus the macOS SDK on a Mac (Xcode or the Command Line
Tools). Linux apps need GTK 3 at run time and nothing at build time.

`--recursive` also fetches the apps, which live in their own repositories as
submodules under `apps/`. To fetch them after a plain clone, run
`git submodule update --init`.

### A new app: `nui`

`nui` makes an app that builds, and checks it without opening a window,
for people and for coding agents alike. It never asks anything, and every
command takes `--json`.

```sh
nui start my-app          # build.zig, a view, its test and an AGENTS.md; then it builds
cd my-app
nui test                  # the view's tests, rendered offscreen
nui snapshot --out shot.png --script "click:Increment"   # the app as a PNG, no window
nui run                   # its window
nui doctor                # Zig 0.17, and GTK 3 on Linux
```

Each release has `nui` for macOS, Linux and Windows; `zig build nui` builds
it into `zig-out/bin`. `nui start` pins nanoui at the release `nui` came
with (`--nanoui REF` for another, `--local PATH` for a checkout). The app's
`AGENTS.md` tells an agent the commands and rules: check the look with
`nui snapshot`, the behavior with `ui.Tester`.

To add nanoui to a project of your own instead:

```sh
zig fetch --save git+https://github.com/justrach/nanoui#v0.5.0
```

Releases are tagged `vMAJOR.MINOR.PATCH`, as mygo's are, and each is listed
under [Releases](https://github.com/justrach/nanoui/releases) with what
changed. While nanoui is 0.x, a minor release may change the API; a patch
release won't.

## Native UI

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

pub fn main(init: std.process.Init) !void {
    const app = try nanoui.App.create(init, .{ .name = "Counter" });
    defer app.destroy();
    var state: Counter = .{};
    _ = try app.newWindow(.{ .title = "Counter", .content = .{ .view = .init(&state, Counter.view) } });
    try app.run();
}
```

<p align="center">
  <img src="docs/images/gallery-dark.png" alt="The nanoui gallery: buttons, toggles, sliders and a text field, drawn by nanoui" width="640">
  <br><sub>The gallery example, <code>zig build run-gallery</code>.</sub>
</p>

Views are immediate mode: a function of your state, run on every event.
Widgets answer from the previous frame's layout. When an interaction changes
state, the frame is built again before it's drawn, so the screen never lags
the state.

<details>
<summary>What's in the toolkit</summary>

- **Layout:** rows, columns, cards and scroll views, with flexbox grow,
  shrink, absolute placement, and maximum sizes.
- **Elements:** GPUI-style method chains, such as
  `ui.div(c).row().gap(8).bg(...)`.
- **Lists:** a virtualized list (`ui.list`) that builds only the rows in view.
- **Text:** wrapping, monospace, weights and rich spans, with text that can
  be selected and copied like a terminal's; lines too long for their box
  end in an ellipsis or fade out (`.truncate`); fonts an app bundles are
  found by family like installed ones (`ui.registerFont`).
- **Controls:** buttons, checkboxes, toggles, sliders, progress bars,
  segmented controls, badges, and text fields (IME on macOS, iOS and Linux).
- **Images:** pictures decoded once and packed into an atlas.
- **SVG:** icons and marks from SVG files (`ui.svg`), drawn by nanoui at
  the screen's density on every platform and tinted to follow the theme:
  paths, shapes, fills, strokes, transforms and inherited styles.
- **Look:** light and dark themes that follow the system, eased animations,
  Gaussian shadows, and Liquid Glass.
- **Pointer:** hover that follows ancestry as CSS's `:hover` does, double
  clicks, and pointer tracking for graphs (`c.wants_moves`).

</details>

### Liquid Glass

`.glass(.{})` fills a box with Liquid Glass, the material of macOS 26 and
later, in place of a background. Whatever was painted under the box shows
through it: frosted, bent near its edges as through the rim of a lens, and
lit along a hairline rim. That includes content scrolling under a toolbar
placed over it with `absolute()`.

```zig
const bar = ui.div(c).absolute().offset(20, 20).w(420).h(56).row().itemsCenter().px(16).rounded(28).glass(.{});
defer bar.end();
ui.text(c, "On glass", .{ .weight = .semibold });
ui.spacer(c);
// A prominent button: glass tinted with the accent.
const tap = ui.div(c).px(16).py(8).rounded(16).glass(.{ .tint = th.accent }).control();
defer tap.end();
ui.text(c, "Tap", .{ .color = th.accent_text });
```

Regular glass frosts and lightens what shows through, or darkens it in dark
mode, so text on it reads over anything. `.style = .clear` barely frosts it,
for glass over photos and video. nanoui draws the glass itself, after mygo's
glass plugin and its measurements of AppKit's `NSGlassEffectView`. Each pane
averages and blurs what's under it, then shades it on the GPU, and the CPU
renderer computes the same pixels. It looks the same on Linux and Windows,
and a test checks the two renderers agree.

<p align="center">
  <img src="docs/images/gallery-glass.png" alt="A toolbar of Liquid Glass over colored cards, with a tinted button and a pane of clear glass" width="640">
  <br><sub>The gallery's Glass page.</sub>
</p>

### Motion

`ui.motion` animates boxes the way gpui-motion does: every frame, you say
where a box should be, and motion takes it there.

- **Transitions:** a spring, or a tween with an easing.
- **Interruptible:** a target that changes midway is taken from where the box
  is, and a spring keeps its speed.
- **Presence:** boxes enter from `initial`, and leave to `exit` before
  they're removed.
- **Gestures:** `hover` and `press` are targets too.
- **Lists:** items can be staggered.
- **Layout animation:** boxes the layout moves glide to their new place.
- **Shared elements:** boxes that share a key glide across parents (`share`).
- **Drag and snap:** a box follows the pointer, then springs to a point.
- **Scroll-linked values:** a scroller's progress drives another number.
- **Animated text:** letters or words enter, staggered.
- **Keyframes:** they loop, or play there and back.

Motion keeps its state in the frame's context, by box, so there are no
objects to hold. It draws frames only while something moves, and jumps
straight to the end when the system asks for reduced motion.

```zig
const f = ui.motion.frame(c, .{
    .target = .{ .width = if (open) 320 else 180, .background = if (open) th.accent else th.surface },
    .initial = .{ .y = 12, .opacity = 0 },
    .press = .{ .scale = 0.96 },
    .transition = .{ .spring = ui.motion.Spring.bouncy },
});
const card = ui.div(c).p(16).control().motion(f);
defer card.end();
if (card.clicked()) open = !open;

// A toast that comes and goes: drawn while it shows, and while it leaves.
if (ui.motion.present(c, "toast", saved, .{ .initial = .{ .y = 24, .opacity = 0 }, .exit = .{ .opacity = 0 } })) |t| {
    const toast = ui.div(c).px(16).py(12).rounded(12).bg(th.text).motion(t);
    defer toast.end();
    ui.text(c, "Saved", .{ .color = th.background });
}
```

<p align="center">
  <img src="docs/images/gallery-motion.png" alt="The gallery's Motion page: a card, a counter, a staggered list, easings, and a toast" width="640">
  <br><sub>The gallery's Motion page.</sub>
</p>

### Kit

`nanoui.kit` is a set of components after GPUI Kit, drawn by nanoui and
moved by `ui.motion`:

- **Buttons** in its variants (primary, danger, ghost, outline, link, …) and
  sizes, with icons, loading and tooltips.
- **Display:** tags, badges, avatars and stacks of them, alerts, skeletons,
  spinners, progress bars and rings.
- **Overlays:** tooltips, popovers, menus, dialogs, sheets and toasts. They
  open on layers over the page, go where they fit, and close on Escape or a
  click elsewhere.
- **Navigation:** tabs whose marker slides, breadcrumbs, pagination, and
  accordions that open to their content's height.
- **Forms:** radio groups, selects you can move through with the arrow keys,
  number inputs, and labelled fields with hints and errors.

```zig
const kit = nanoui.kit;

if (kit.button(c, "Delete", .{ .variant = .danger, .icon = "trash" }).clicked) confirm = true;
if (kit.dialog(c, "confirm", &confirm, .{ .title = "Delete project?", .ok = "Delete", .ok_variant = .danger })) |d| {
    ui.text(c, "Its files and history go too.", .{});
    if (d.end() == .ok) toaster.push(.{ .status = .danger, .title = "Deleted" });
}
_ = kit.tabs(c, &.{ "Overview", "Activity", "Settings" }, &tab, .{ .variant = .segmented });
toaster.view(c); // last: toasts over everything
```

Overlays are made of two new box properties: `layer` draws a box above the
page and unclipped, and `fixed` places it from the window's corner.
`Context.state` keeps a widget's small state between frames.

<p align="center">
  <img src="docs/images/gallery-kit.png" alt="The gallery's Kit page: buttons in every variant and size, tags, avatars, alerts, progress" width="640">
  <br><sub>The gallery's Kit page.</sub>
</p>

## Web pages

```zig
const Greeter = struct {
    pub const nanoui_params = .{ .greet = .{"name"} };

    pub fn greet(_: *Greeter, call: *nanoui.Call, name: []const u8) ![]const u8 {
        return std.fmt.allocPrint(call.arena, "Hello, {s}!", .{name});
    }
};

const Tick = nanoui.Event("tick", struct { uptime: u64 });

// in main:
try app.bind(&greeter);
try app.registerEvent(Tick);
_ = try app.newWindow(.{ .title = "Hello", .content = .{ .page = .{ .url = "/", .assets = &assets } } });
```

```js
import { Greeter, onTick } from "/nanoui.js"; // generated, served by the app

document.body.textContent = await Greeter.greet("Ada");
onTick(({ uptime }) => console.log(uptime));
```

`zig build gen` writes `nanoui.d.ts`:

```ts
export declare const Greeter: { greet(name: string): Promise<string> };
export declare function onTick(listener: (payload: TickPayload) => void): () => void;
```

Methods may return error unions; an error rejects the page's promise with
the error's name. Assets are served from the `nanoui://localhost/` scheme.
Elements styled `--app-region: drag` move frameless windows.

## Testing without a window

```zig
var t: ui.Tester = undefined;
try t.init(gpa, .init(&state, Counter.view), .{});
defer t.deinit();
try t.clickText("Increment");
try std.testing.expect(t.hasText("1"));
try t.screenshot("/tmp/counter.png"); // rendered offscreen by the Metal renderer
```

The real apps run headless too:

```sh
zig-out/bin/gallery --nanoui-snapshot=shot.png --nanoui-script="click:Tasks;type:Hi;key:enter"
zig-out/bin/hello --nanoui-eval='nanoui.call("Greeter.greet","Ada").then(v => { nanoui.log(v); nanoui.window.close() })'
```

`--nanoui-wait=SECONDS` runs the event loop first, drawing the view as it
goes, so what an app loads as it draws (pictures, a map's tiles, replies)
is there in the snapshot.

## Platforms

nanoui loads what each platform has instead of linking it, so every platform
builds from any machine (iOS from a Mac with Xcode, for its SDK; Android with
Android's SDK and NDK). On a Mac, `zig build -Dtarget=x86_64-linux-gnu` or
`-Dtarget=x86_64-windows-gnu` makes a Linux or Windows binary.

| | macOS | iOS | Android | Linux | Windows |
|---|---|---|---|---|---|
| windows, input, timers | AppKit | UIKit: screens over each other, touch, keyboards | NativeActivity: screens over each other, touch, keyboards, Back | GTK 4, else GTK 3 (loaded with `dlopen`) | Win32 |
| text | CoreText | CoreText | nanoui's TrueType reader, Android's fonts | nanoui's TrueType reader (`src/ui/tt/`) | the same |
| rendering | Metal | Metal | OpenGL ES 3; CPU without it | OpenGL 3.3 in a GtkGLArea; CPU (`src/ui/raster.zig`) without one | CPU, shown by Direct3D 11 (a DXGI flip swap chain; GDI without it) |
| icons | SF Symbols | SF Symbols | line icons drawn by nanoui (`src/ui/icons.zig`) | the same | the same |
| SVG (`ui.svg`) | drawn by nanoui (`src/ui/svg.zig`) | the same | the same | the same | the same |
| pages (webview) | WKWebView | not yet | not yet | not yet | WebView2 |
| menus | the menu bar | a keyboard's shortcuts | a keyboard's shortcuts | accelerators | accelerators |
| HTTP (`nanoui.http`) | NSURLSession | NSURLSession | http-zig, names looked up by Android | [http-zig](https://github.com/justrach/http-zig): HTTP/2 over TLS, a thread per request | the same |
| input methods that compose text | NSTextInputClient: marked text, the text around the caret, the edit menu | UITextInput: marked text (pinyin), autocorrect, ⌘C ⌘X ⌘V | not yet: a software keyboard types keys | GTK's input method, its preedit | not yet: only what arrives as `WM_CHAR` |
| accessibility | VoiceOver: the same tree as iOS (`ui.access`): controls, text, headings, boxes that take clicks, `nanoui.kit`; announcements, Increase Contrast | VoiceOver: controls, text, headings, boxes that take clicks (`ui.access`); Dynamic Type, Increase Contrast | not yet | not yet | not yet |

The CPU renderer matches the Metal one pixel for pixel, and a test compares
them; others compare the OpenGL renderer with the CPU one, with OpenGL 3.3
and with OpenGL ES 3, in a context without a window. `NANOUI_RENDERER=cpu` draws on the CPU where OpenGL is. `zig build test -Dportable=true` runs the Linux and Windows text and
renderer on a Mac. Linux is also tested in a container
(`tools/linux.Dockerfile`: GTK 3 and 4, fonts and a virtual display).

On Linux nanoui loads GTK 4 when it's installed and GTK 3 otherwise;
`NANOUI_GTK=3` asks for GTK 3. Both work the same: GTK 4's event
controllers, draw function, clipboard and dialogs stand in for GTK 3's
event signals and waiting calls (`src/linux/surface_gtk4.zig`). On Windows,
frames reach the screen through a Direct3D 11 device (hardware, else WARP)
and a flip-sequential swap chain, so resizing stays smooth and content
stays anchored (`src/windows/d3d.zig`).

### iOS

<p align="center"><img src="docs/images/ios-gallery.gif" width="300" alt="The gallery example on an iPhone in the iOS Simulator: pages pushed from a list, buttons, toggles, a task list typed into, a 10 000-row list filtered, springs, and Liquid Glass"></p>

The gallery on an iPhone ([MP4](docs/images/ios-gallery.mp4)). It's the same
Zig view as on the Mac. When the window is narrow it shows its pages as a list
and pushes each one in. The app played this itself:

```sh
xcrun simctl launch booted dev.nanoui.gallery "--nanoui-play=tap:Tasks;tap:Something to do;type:Record a demo;tap:Add"
xcrun simctl io booted recordVideo demo.mov
```

`--nanoui-play` takes the same steps as `--nanoui-script` (tap, type, key,
scroll, wait) and plays them in the running app at a person's pace, with a
dot where each finger lands. It works on macOS too. The Simulator can record
its screen but can't tap, so this is how you make demo videos.

Native UI runs on iOS with the Mac's renderer and text, Metal and CoreText;
`src/ios/` puts them on UIKit. The first window fills the screen, and
windows shown after it cover it until they close or hide; a window over
another needs its own way to close (no swipe down). A finger is the
pointer: it presses and drags, and scrolls what it moves up or down over,
flinging as iOS's scroll views do. Two fingers pinch: their spread and
movement come to the view as `input.zoom` and `input.pan` (a trackpad's
pinch does on the Mac). A hardware keyboard's keys and shortcuts work as on
the Mac, and a focused text field brings up the software keyboard. Views
are laid out inside the safe area, clear of the status bar, the home
indicator and the keyboard; a window made with `.full_bleed = true` spans
the screen and keeps its content clear itself with `ui.div(c).safeArea()`.

```sh
zig build $(sh tools/ios/zig-lib.sh) -Dtarget=aarch64-ios-simulator               # zig-out/ios/Counter.app, Gallery.app
zig build $(sh tools/ios/zig-lib.sh) run-gallery -Dtarget=aarch64-ios-simulator   # in the booted Simulator
zig build $(sh tools/ios/zig-lib.sh) run-gallery -Dtarget=aarch64-ios-simulator --watch   # again on every save
```

With `--watch`, each save builds the app, installs it and launches it
again in the Simulator in a few seconds, its output in the same terminal.
A release build (`-Doptimize=ReleaseSmall`) is stripped of its local
symbols as it is bundled: the counter is about 300 KB, the gallery about
500 KB, the renderer, text and widgets in them.

You need Xcode for the iOS SDK. Zig 0.17.0's std can't build programs for
iOS as it ships: it takes iOS for a system that can replace its process
image (`std.process.can_replace`). `tools/ios/zig-lib.sh` makes Zig's lib
folder again out of links to it, with that one line fixed, and prints the
`--zig-lib` flag that uses it (nothing, once Zig is fixed), which goes
first after `zig build`.

`-Dtarget=aarch64-ios` builds for devices: sign the app with your team
(Xcode, or `codesign` and a provisioning profile) and install it with
`xcrun devicectl`. Zig compiles a device's program and Apple's linker
(`xcrun clang`) links it: an iPhone refuses a program Zig 0.17.0 links,
before it runs and without a crash report. An app bundles itself in its
own build.zig:

```zig
const bundle = @import("nanoui").ios.app(b, exe, .{ .name = "Notes", .id = "com.example.notes" });
```

An app that makes its own bundle takes its program from
`ios.executable(b, exe)`.

Zig 0.17 makes iOS 18 the lowest an app runs on unless the target names
one, and the app's Info.plist follows it. nanoui runs on iOS 15 and
later: `-Dtarget=aarch64-ios.15.0` (or `aarch64-ios.15.0-simulator`)
reaches those devices.

Not on iOS yet: pages, the selection's handles and loupe, keys repeating
while held, or iPad multiwindow.

### Android

<p align="center"><img src="docs/images/android-gallery.png" width="720" alt="The gallery example on an Android phone in the emulator: its pages as a list, the task list typed into with the software keyboard up, and the list in dark mode"></p>

Native UI runs on Android with Linux's text and renderer, nanoui's TrueType
reader on Android's fonts and OpenGL ES 3 (or the CPU), on the NDK's
NativeActivity (`src/android/`). There's no Java of nanoui's own: the app's
`main` runs on a thread of its own with a looper, and Java's classes are
called through JNI where Android has no C interface (the clipboard, links,
dialogs, the software keyboard, the insets). As on iOS, the first window
fills the screen and windows shown after it cover it; a finger presses,
scrolls and flings, two pinch, and views are laid out clear of the bars,
the cutout and the keyboard. Back is Escape for the top window's view
first (a menu, a sheet or a page closes), then closes the top window, and
on the last one sends the app to the background. A mouse hovers, clicks
and scrolls; dark mode, rotation and density follow the system.

```sh
zig build -Dtarget=aarch64-linux-android               # zig-out/android/Counter.apk, Gallery.apk
sh tools/android/emulator.sh                           # an emulator without a window
zig build run-gallery -Dtarget=aarch64-linux-android   # installed and run there (or on a phone), its log here
```

What you need, an app's build.zig, and what isn't there yet:
[docs/android.md](docs/android.md).

## Apps

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/justrach/nanoterm"><img src="docs/images/nanoterm-light.png" alt="nanoterm: an agent's answer with a native visual"></a>
      <p><a href="https://github.com/justrach/nanoterm"><strong>nanoterm</strong></a>: a terminal of blocks, in the manner of Warp, with a coding agent (graff or Claude Code) over ACP. It has native visuals, a ⌘P launcher, and SSH sessions where the agent works on the remote host.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/justrach/nanomon"><img src="docs/images/nanomon-dark.png" alt="nanomon: the overview with graff's suggestions"></a>
      <p><a href="https://github.com/justrach/nanomon"><strong>nanomon</strong></a>: an activity monitor in Codegraff colors, with cell graphs of CPU, memory, GPU, disk and network. You can quit several processes at once, and a graff bubble suggests what to quit.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/justrach/nanostudio"><img src="docs/images/nanostudio-dark.png" alt="nanostudio: the editor with a zoom on the timeline"></a>
      <p><a href="https://github.com/justrach/nanostudio"><strong>nanostudio</strong></a>: a screen recorder and editor. It records a display or a window with its sound, then zooms where you clicked. You can trim, speed up and dress the take, and export it. Every frame, preview and export alike, is a nanoui view.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/justrach/nanofly"><img src="docs/images/nanofly.png" alt="nanofly: Singapore to San Francisco over the Pacific, with the weather's radar, and the flight's card in a sheet of glass" width="300"></a>
      <p><a href="https://github.com/justrach/nanofly"><strong>nanofly</strong></a>: flights, live, on a map, for iPhone (and the Mac), after Flighty. It finds a flight's route, follows it from open ADS-B data, and says when it lands by each airport's clock, with the weather there. Its map, drawn by <code>ui.canvas</code>, has the night's side, the weather's radar and the planes around; you can pinch it, and its card is a sheet of Liquid Glass you drag between three heights.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/gstohl/nanomail"><img src="docs/images/nanomail-dark.png" alt="nanomail: a message with links and a picture, shared mailboxes in the sidebar"></a>
      <p><a href="https://github.com/gstohl/nanomail"><strong>nanomail</strong></a>: a JMAP mail client for macOS and iOS. It shows rich mail with links and pictures, loading pictures from the web only when you ask. New mail arrives by push, and mailboxes others share with you appear with what you may do in them. It signs in with a password, a token, or OAuth in the browser.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/justrach/nanolight"><img src="docs/images/nanolight.jpg" alt="Nanolight: its panel has found Safari from &quot;saf&quot;"></a>
      <p><a href="https://github.com/justrach/nanolight"><strong>nanolight</strong></a>: a launcher for the Mac, Windows and Linux. It finds apps as you type (initials and typos too), does math, and completes Google searches inline, showing the results in its own panel. It runs Raycast extensions and script commands, and asks Grok or searches X a row away.</p>
    </td>
  </tr>
</table>

Download them for macOS:
[nanoterm](https://github.com/justrach/nanoterm/releases/latest/download/nanoterm-macos-arm64.dmg) ·
[nanomon](https://github.com/justrach/nanomon/releases/latest/download/nanomon-macos-arm64.dmg) ·
[nanostudio](https://github.com/justrach/nanostudio/releases/latest/download/nanostudio-macos-arm64.dmg) ·
[nanolight](https://github.com/justrach/nanolight/releases/latest/download/nanolight-macos-arm64.dmg).
nanomail builds from source for now (`zig build`; its README has iOS).

They live in `apps/` as submodules, and each also builds on its own, fetching
nanoui pinned by commit. To build one against the nanoui next to it, with
your changes, use `--fork`: `cd apps/nanomon && zig build run --fork=../..`.

## Performance

Performance is measured headless with [`hillclimb/`](hillclimb/README.md):
the same scenes rendered through each framework's own frames and offscreen
Metal renderer, on an Apple M3 Ultra. The figures are medians per frame in
milliseconds; lower is better.

| scene | frame CPU nanoui | frame CPU mygo | GPU nanoui | GPU mygo |
|---|---:|---:|---:|---:|
| boxes (600 shadowed boxes) | 0.061 | 0.301 | 0.140 | 1.616 |
| text (300 changing labels) | 0.108 | 0.418 | 0.065 | 0.056 |
| scroll (1000-row column) | 0.315 | 2.076 | 0.055 | 0.122 |
| list (100 000-row virtual list) | 0.060 | 0.367 | 0.046 | 0.045 |
| dashboard (12 cards) | 0.015 | 0.087 | 0.098 | 0.295 |

Release binaries are about 0.7 MB for nanoui and 11.8 MB for mygo. IPC (5000
sequential calls from the page to native code) took 493 ms with nanoui and
528 ms with mygo.

### Build times

A counter app each, from empty build caches, on the same M3 Ultra
(`sh tools/buildperf.sh` measures it again: mygo's
`examples/counter-native` with Go 1.27.1, nanoui's from `nui start` with
Zig 0.17.0; network fetches aren't timed):

| | mygo | nanoui |
|---|---:|---:|
| cold build | 4.4 s | 6.3 s (a second app, Zig's global cache warm: 4.8 s) |
| rebuild, nothing changed | 0.28 s | 0.12 s |
| rebuild after a one-line edit | 0.55 s | 2.2 s |
| build cache on disk | 182 MB | 97 MB |
| program | 14 MB | 4 MB Debug, 0.7 MB ReleaseFast (11 s), 0.4 MB ReleaseSmall (6.7 s) |

Zig compiles the app and nanoui as one unit, so an edit rebuilds the
whole of it where Go rebuilds one package: that's where mygo is faster.
Cold builds are close, nothing-changed rebuilds faster, and the disk a
project costs is about half.

## Development

```sh
zig build lines                                                       # the 600-line limit, enforced
zig build test-bin -Dtarget=aarch64-linux-gnu --prefix zig-out/linux  # Linux tests, for the container
cd hillclimb && zig build run -- --label "change"                     # benchmarks against mygo and history
sh tools/version.sh 0.2.1                                             # set the version for a release
```

To release, set the version, commit, and push its tag (`git tag v0.2.1 &&
git push origin v0.2.1`). The release workflow checks that the tag matches
`build.zig.zon`, runs the tests, and opens the GitHub release.

Rules for working here, by hand or with an agent, are in
[AGENTS.md](AGENTS.md).

nanoui is a subset of what full frameworks offer. Pages work on macOS and
Windows so far, accessibility is only on iOS and macOS's built-in controls,
there are no notifications, channels or plugins yet, and bundling is only for
iOS and Android. Apps update themselves from GitHub releases on macOS, even
restarting unseen (`nanoui.Updater`). Bound methods run on the main thread.

## License

nanoui is licensed under the [MIT License](LICENSE). Material from mygo (MIT),
GPUI (Apache 2.0), gpui-motion (MIT) and GPUI Kit (Apache 2.0) keeps its own
notices; see [third-party notices](THIRD_PARTY_NOTICES.md).

## Credits

nanoui stands on the shoulders of these projects:

- **[mygo](https://github.com/egoist/mygo)** by [egoist](https://github.com/egoist):
  nanoui began as a port of its core to Zig, and keeps its architecture. That
  means:
  - the Objective-C runtime called directly, with runtime classes for
    delegates;
  - a batched outbox (one evaluation per main-loop turn), held events;
  - a generated, typed client, and native UI drawn by the framework;
  - Liquid Glass drawn by its own renderers, ported from mygo's glass plugin.
- **[GPUI](https://github.com/zed-industries/zed/tree/main/crates/gpui)** by
  [Zed Industries](https://zed.dev). From GPUI, nanoui takes:
  - elements styled by method chains, and the virtualized `uniform_list`;
  - layouts cached across frames, with glyphs rasterized once into an atlas;
  - Gaussian shadows;
  - its general idea of a fast, GPU-drawn native UI.
- **[gpui-motion](https://github.com/1bye/gpui-motion)** by
  [1keep](https://github.com/1bye): `ui.motion` follows its model and API.
  That covers interruptible targets, presence, keyframes, stagger, layout
  animation, its exact springs and its easing curves.
- **[GPUI Kit](https://github.com/longbridge/gpui-component)** by [Longbridge](https://github.com/longbridge): `nanoui.kit` follows its components, their variants and their names.
<p align="center"><sub>Built in Zig 0.17 · <a href="AGENTS.md">AGENTS.md</a> · <a href="hillclimb/README.md">benchmarks</a> · <a href="LICENSE">MIT</a> · <a href="THIRD_PARTY_NOTICES.md">third-party notices</a></sub></p>


## Docs
### AGENTS.md
# AGENTS.md

nanoui is a desktop application framework in Zig 0.17, after
[mygo](https://github.com/egoist/mygo). Windows show either a web page in the
system webview (WKWebView, macOS only for now) with typed Zig ↔ TypeScript
IPC, or native UI that nanoui draws itself, in the manner of GPUI: with Metal
and CoreText on macOS; on Linux (GTK 3, loaded with dlopen) and Windows
(Win32) with nanoui's own TrueType text (`src/ui/tt/`) and CPU renderer
(`src/ui/raster.zig`, tested against Metal); on Linux, OpenGL 3.3 draws
where there is a GPU (`src/ui/opengl.zig`, tested against the CPU
renderer); on iOS (UIKit) with Metal and CoreText as on the Mac; on
Android (NativeActivity, no Java of nanoui's own: Java's classes through
JNI) with nanoui's own text and OpenGL ES 3, or the CPU. Every platform
builds from any machine (`-Dtarget=...`); iOS needs Xcode's SDK and Zig's
lib fixed (`tools/ios/zig-lib.sh`), Android the Android SDK and NDK.

## Hard rules

- **Every file is at most 600 lines.** Source, scripts, shaders, docs: no
  exceptions. When a file would grow past 600 lines, split it by
  responsibility (a widget set, a backend concern, a layout pass) before
  adding to it. `zig build lines` checks it and must pass. The one
  exception: upstream license texts kept verbatim in `third_party/licenses/`,
  which must not be split or edited.
- **Zig 0.17.0.** Use its APIs (`std.process.Init`, `std.Io`, `@Fn`,
  `std.lang.Type`'s `field_names`/`field_types`/`decl_names`), not older idioms.
- **No C shims.** Native code is called directly: the Objective-C runtime
  through `src/objc.zig` (`objc.msg` builds each `objc_msgSend` prototype at
  comptime), C frameworks (CoreText, CoreGraphics, Metal, ImageIO,
  libdispatch) and Win32 through `extern` declarations, GTK through
  `dlopen`/`dlsym` (`src/linux/gtk.zig`), Java through JNI's function
  table (`src/android/jni.zig`). No `@cImport`, no `.c`/`.m`, no `.java`.
- **Every platform keeps building.** After a change, build for Linux and
  Windows too (`zig build -Dtarget=aarch64-linux-gnu --prefix zig-out/linux`,
  `-Dtarget=x86_64-windows-gnu`), iOS
  (`zig build $(sh tools/ios/zig-lib.sh) -Dtarget=aarch64-ios-simulator`) and
  Android (`zig build -Dtarget=aarch64-linux-android`: zig-out/android/*.apk),
  and run the Linux tests in the container (`tools/linux.Dockerfile`, `zig build test-bin`).
- **Never show windows on the developer's screen** while working: no
  running examples or benchmark apps windowed, nothing that activates an
  app or takes focus (nanoterm may be shown when asked). Live apps are
  checked headlessly with `--nanoui-snapshot` and `--nanoui-wait`; on
  iOS in a simulator booted headless, on Android in an emulator without a
  window (`tools/android/emulator.sh`), which adb may drive and capture
  (`adb shell input`, `adb exec-out screencap`). Measure with the headless hill-climb app
  (`hillclimb/`), verify with `ui.Tester` and the `--nanoui-*` flags.
- **Never drive the real screen.** No synthetic mouse or keyboard events
  (CGEventPost, AppleScript clicks), no full-screen captures: the user's
  other windows are theirs. Test native UI with `ui.Tester` (in process,
  rendered offscreen), apps with `--nanoui-snapshot`/`--nanoui-script`, and
  pages with `--nanoui-eval`, all of which keep windows hidden. Tests never
  touch the user's state either: no system clipboard (the Tester has its
  own), no files outside temporary directories, no defaults.
- **Threading.** AppKit, WebKit and the UI run on the main thread. Work from
  other threads reaches it through `objc.dispatchMain`.
- **Nothing polls.** Frames are drawn on input, resize, or while an
  animation runs; an idle app uses no CPU.
- **Objective-C memory:** `alloc`/`new` objects are owned and must be
  released; wrap code that makes temporary objects in `objc.Pool`. Objects
  a callback may still reach after teardown (a scheduled flush or frame)
  free themselves when it runs (`dead` flags in `Page` and `Surface`).
- **Heavy builds:** never build with Zig's self-hosted backend
  (`-fno-llvm`/`-fno-lld`); one heavy build at a time.

## Layout

```
src/nanoui.zig        the public API
src/objc.zig          Objective-C runtime, runtime classes, blocks, libdispatch
src/app.zig           lifecycle, menu bar, trays, services, client generation
src/dev.zig           --nanoui-* flags: generate, snapshot, script, eval, hidden
src/window.zig        NSWindow showing a page or native UI, window controls
src/page.zig          the page's platform-free part: the outbox, held messages, the asset table
src/page_webkit.zig   WKWebView: the view, the scheme handler, the message handler
src/page_webview2.zig WebView2: the view, the resource filter, the message handler
src/page_webview2_profile.zig  WebView2's profile folder
src/windows/webview2.zig  WebView2's COM interfaces, by vtable slot
src/tests_page.zig    the page's platform-free parts, tested
src/ipc.zig           bound services, calls, typed events, page messages
src/tsgen.zig         comptime TypeScript declarations and JS client
src/bridge.js         the page runtime (window.nanoui)
src/menu.zig          menus from templates: roles, accelerators, checkboxes
src/tray.zig          status bar icons
src/dialog.zig        open/save panels, message boxes
src/desktop.zig       clipboard, shell (open, reveal, trash), paths, appearance
src/update.zig        updates from GitHub releases: check, verify, swap the bundle
src/ui/ui.zig         native UI's public API and View
src/ui/context.zig    per-frame box tree, ids, input, hit testing, animation
src/ui/input.zig      keys, shortcuts, text operations, one event's input
src/ui/layout.zig     flexbox: measure, arrange, grow, shrink, absolute, scroll
src/ui/paint.zig      tree → GPU instances, clipping, culling, scrollbars
src/ui/frame.zig      one frame, shared by windows and the Tester; frame stats
src/ui/widgets.zig    boxes, text, icons, buttons, toggles, sliders, …
src/ui/div.zig        GPUI-style elements: ui.div(c).row().gap(8)…
src/ui/list.zig       virtualized list (GPUI's uniform_list)
src/ui/textfield.zig  the text field: selection, composition, clipboard
src/ui/textinput.zig  NSTextInputClient: IME, key bindings → text ops
src/ui/text.zig       fonts, shaping, cached layouts, wrapping
src/ui/shaper.zig     the exact fast path for printable ASCII
src/ui/atlas.zig      the glyph and SF Symbol atlas, growing
src/ui/metal.zig      the renderer: one pipeline, ring of instance buffers
src/ui/shader.metal   rounded rects, borders, glyphs, Gaussian shadows
src/ui/glass.zig      Liquid Glass: the material, backdrop and optics (CPU too)
src/ui/glass.metal    the glass's backdrop kernels and fragment function
src/ui/metal_glass.zig  panes of glass in the Metal renderer
src/ui/surface.zig    the NSView: events, display link, occlusion, resize
src/ui/motion/        ui.motion: springs, tweens, presence, keyframes, layout,
                      drag/snap, scroll-linked values, shared elements, text
src/ui/tester.zig     views without a window: input, time, PNG snapshots
src/ui/tests.zig      widget tests through the Tester
src/ui/text_tt.zig    text where nanoui shapes it itself (Linux, Windows, Android)
src/ui/tt/            TrueType: font files, the installed fonts, outlines to coverage
src/ui/atlas_tt.zig   the glyph atlas in memory; icons.zig: line icons
src/ui/raster.zig     the CPU renderer (same pixels as shader.metal)
src/ui/canvas.zig     a CPU-drawn window's pixels: only what a frame changed is drawn
src/ui/opengl.zig     the OpenGL 3.3 renderer (Linux), and OpenGL ES 3's (Android); shader.glsl: both Metal shaders in GLSL
src/ui/gl.zig         OpenGL's functions, loaded with dlopen
src/ui/images.zig     pictures (ui.image): decoded once, packed in a BGRA atlas
src/ui/png_decode.zig PNG to pixels where ImageIO isn't (Linux, Windows, portable)
src/platform.zig      what differs by OS below the UI (event loop, clipboard)
src/linux/            GTK 3 backend: app, window, surface (GL area or CPU), dialogs, fd watches
src/windows/          Win32 backend: app, window, surface (events, frames) +
                      surface_gpu (paint, D3D11 present), d3d (swap chain),
                      ime (IMM32), win32 (the extern layer), desktop, dialog,
                      fdwatch, loop, tests_*
src/ios/              UIKit backend: app and scenes, windows as stacked screens,
                      surface (Metal view), touch (pointer, scrolling, flings),
                      keys (hardware keys, software keyboard), desktop, dialogs
src/android/          NativeActivity backend: the activity and the app's thread (activity,
                      main, launch, calls), JNI, windows as stacked screens, surface
                      (EGL, or the CPU), touch, keys and the keyboard (ime), bars and
                      insets, desktop, dialogs (AlertDialog), fd watches, Zig std's
                      workarounds for bionic (sigaction, lookup)
src/menu_accel.zig    menus as accelerators (Linux, Windows, iOS, Android)
src/kit/              nanoui.kit: components after GPUI Kit (buttons, overlays, tabs, forms)
tools/*.Dockerfile    Linux (GTK, Xvfb) and Windows (Wine) test images
tools/ios/            app bundles (bundle.zig), the Simulator (sim.sh), Zig's lib fixed (zig-lib.sh)
tools/android/        APKs (apk.zig: the SDK, the manifest, aapt2, pack.zig, apksigner), run.sh, emulator.sh
examples/             hello (webview), counter and gallery (native UI), browser (local and remote pages)
hillclimb/            headless benchmarks against mygo (its own package)
apps/nanoterm/        the first app: a Warp-like terminal with ACP agents
apps/nanomon/         a small activity monitor (libproc, Mach, /proc)
apps/nanomail/        a JMAP mail client for macOS and iOS
site/                 the website (its own repo): Next.js on Cloudflare Workers, a gallery
tools/lines.zig       the 600-line check
tools/version.sh      set or check the version (build.zig.zon) for a release
.github/workflows/    CI (tests on macOS and Linux) and releases from v* tags
```

## Commands

```sh
zig build                 # build every example into zig-out/bin
zig build test            # unit and widget tests (renders offscreen with Metal)
zig build test -Dportable=true   # the same with nanoui's own text and CPU renderer
zig build test-bin -Dtarget=aarch64-linux-gnu --prefix zig-out/linux   # Linux tests, run in the container
zig build lines           # enforce the 600-line limit
zig build run-hello       # webview + typed IPC
zig build run-counter     # native UI
zig build run-gallery     # native UI widgets
zig build gen             # write examples/hello/frontend/nanoui.{js,d.ts}
zig build $(sh tools/ios/zig-lib.sh) run-gallery -Dtarget=aarch64-ios-simulator   # the gallery in a simulator booted headless (xcrun simctl boot)
sh tools/android/emulator.sh   # an Android emulator without a window (stop: sh tools/android/emulator.sh stop)
zig build run-gallery -Dtarget=aarch64-linux-android   # the gallery on it (or a phone), its log here
zig build test-bin -Dtarget=aarch64-linux-android --prefix zig-out/android-tests   # the tests for a device:
adb push zig-out/android-tests/bin/nanoui-tests /data/local/tmp && adb shell /data/local/tmp/nanoui-tests
zig build test-tools      # the Android build tools' own tests (zip writing, the manifest)
sh tools/version.sh 0.2.1 # set the version; commit, push tag v0.2.1 to release
cd hillclimb && zig build run -- --label "change"   # climb: compare with mygo and history
cd apps/nanomon && zig build test --fork=../..     # an app (a submodule) against this nanoui, not its pinned one

# Headless checks of the real apps (no window is shown):
zig-out/bin/gallery --nanoui-snapshot=/tmp/g.png --nanoui-script="click:Tasks;type:Hi;key:enter"
zig-out/bin/hello --nanoui-eval='nanoui.call("Greeter.greet","Ada").then(v=>{nanoui.log(v);nanoui.window.close()})'
```

## Conventions

- New widgets are made of boxes (`Context.open`/`leaf`) styled from the
  theme and animated with `Context.animate`; a widget whose interaction
  changes app state sets `c.changed` so the frame is built again.
- Interactions read the previous frame's layout; keep ids stable with
  `ui.key` for list items.
- Every widget behavior gets a test in `src/ui/tests.zig`; every new IPC
  type mapping gets one in `src/tsgen.zig`.
- Keep `examples/hello/frontend/nanoui.d.ts` current (`zig build gen`).
- Performance work is hill-climbed: run `hillclimb` before and after, keep
  changes that climb, label runs. Never trade correctness for speed: fast
  paths come with tests proving they match the slow path (`shaper.zig`).


### docs/android.md
# Android

How nanoui builds for Android, what an app needs, and what isn't there yet.
The overview is in the [README](../README.md#android).

You need Android's SDK with its NDK, build tools and Android 16's platform
(API 36; Android Studio installs them, and `ANDROID_HOME`, `ANDROID_NDK_HOME`
say where if elsewhere) and Java, to sign. The build links the NDK's C
library, as Zig has none for Android. An app is a library NativeActivity
loads, in an APK signed with the debug key (or `.keystore`):

```zig
const android = @import("nanoui").android;
const lib = android.library(b, .{ .name = "notes", .root_module = mod, .nanoui = nanoui_module });
const apk = android.apk(b, lib, .{ .name = "Notes", .id = "com.example.notes" });
```

Apps run on Android 10 (API 29) and later; `-Dtarget=x86_64-linux-android`
builds for x86 emulators and Chromebooks. A release build of the gallery
(`-Doptimize=ReleaseSmall`) is about 730 KB. Arguments reach a debuggable
build (a debug APK) as the intent's extras (`run-*` passes them, and
`NANOUI_*` variables); a release build ignores them, as any app could send
them, and says so in the log. What it prints goes to `adb logcat -s nanoui`,
and `--nanoui-snapshot` works on a device too, into a path of the app's
(`adb shell run-as` reads it). Zig 0.17.0's std lays out `struct sigaction`
as glibc does and looks host names up in /etc/resolv.conf, neither of which
fits Android: nanoui translates the one and asks Android's resolver instead.

Not yet: pages, file pickers (`dialog.open` answers null), input methods
that compose text (a software keyboard types keys: what Android's key maps
have, no Chinese or Japanese), more than three buttons in a message, and
predictive Back's animation.


### docs/motion.md (excerpt)
# ui.motion

Declarative, interruptible animation for nanoui's native UI. Every frame you
say where a box should be (its target) and how to get there (a spring or a
tween). Motion remembers where it is. A target that changes midway is taken
from there; a spring keeps its speed.

The model follows [gpui-motion](https://github.com/1bye/gpui-motion) (MIT)
and [Motion](https://motion.dev) (ideas only, no copied code): state-driven
targets, closed-form springs, FLIP layout, presence, drag, scroll-linked
values, and staggered text. State lives in the `Context` by box id. Nothing
is allocated per frame on the hot path once the store has its slots, and
frames are requested only while something is moving.

Reduced motion jumps to the target.

## Targets

`x`, `y`, `scale`, `opacity`, `width`, `height`, `radius`, `background`.
What a target leaves null is left alone. `hover` and `press` overlay the
target while the pointer is over or pressing the box.

```zig
const f = ui.motion.frame(c, .{
    .target = .{ .width = if (open) 320 else 180, .background = if (open) th.accent else th.surface },
    .initial = .{ .y = 12, .opacity = 0 },
    .press = .{ .scale = 0.96 },
    .hover = .{ .y = -2 },
    .transition = .{ .spring = ui.motion.Spring.bouncy },
});
const card = ui.div(c).control().motion(f);
```

## Springs and tweens

```zig
.{ .spring = .{ .stiffness = 240, .damping = 26, .mass = 1 } }
.{ .spring = ui.motion.Spring.snappy } // also .gentle, .bouncy
.{ .spring = ui.motion.Spring.visual(0.4, 0.15) } // 90% in 0.4s
.{ .tween = .{ .duration = 0.3, .ease = .ease_out } }
.instant
```

The spring is solved exactly (under-, critically-, and over-damped). A
value at any time is the same however the frames fell.

## Presence

```zig
if (ui.motion.present(c, "toast", show, .{
    .initial = .{ .y = 24, .opacity = 0 },
    .exit = .{ .y = 24, .opacity = 0 },
})) |f| { ... }
```

The box stays drawn until its exit settles, then `present` returns null.

## Layout and shared elements

`.layout = true` glides a box when flexbox moves it (a list shuffle).
`share(c, "chip", show, m)` does the same across parents: one key, one
place it was last drawn, FLIP to where it is now.

## Drag and snap

```zig
const d = ui.motion.drag(c, .{
    .min = .{ 0, 0 },
    .max = .{ 280, 0 },
    .axis = .x,
    .snap = &.{ .{ 0, 0 }, .{ 140, 0 }, .{ 280, 0 } },
    .elasticity = 0.18,
    .momentum = true,
});
const knob = ui.div(c).control().motion(d.frame());
```

While pressed the box follows the pointer (rubber-banded past the edges).
On release it keeps its speed and springs to the nearest snap or grid.

## Scroll-linked values

Every scrolling box records `scroll_max` (not only `follow_end` ones).

```zig
const p = ui.motion.scroll.of(c, scroller_id); // 0..1
const w = ui.motion.scroll.value(c, "bar", scroller_id, .{ 0, 200 }, .instant);
const y = ui.motion.scroll.remap(p, .{ 0, 1 }, .{ 0, 40 }, true);
```

`inView(viewport, item)` is the overlapping fraction of the item.

## 

### docs/linux-perf.md (excerpt)
# Linux performance hill-climb

Headless measurements of nanoui on Linux against itself and other GUI
frameworks. The JSON source of truth is `bench/frameworks.json`.

Host: Ubuntu 24.04, x86_64, **no discrete GPU**. nanoui draws with
`src/ui/raster.zig` through `ui.Tester` (offscreen, 900×640 at 2×).
rustc **1.99.1** (rustup stable). Mesa **lavapipe** (llvmpipe LLVM 20.1.2)
is the Vulkan ICD under `xvfb-run`.

## Method

Scenes: `boxes` (600 moving shadowed rects), `text`, `scroll`, `list`,
`dashboard`, `springs` (2 000 `ui.motion` boxes), `letters`. 30 frames of
warm-up, 20 measured. A change is kept only if a scene improves by more
than 3% and nothing important regresses by more than that.

GPUI 0.2.2 is built with its Linux X11 + Blade backend. A window opens
on Xvfb and `Window::draw` is timed (layout, prepaint, paint, scene).
Blade **present hung** on lavapipe's vsync path, so GPU present is not in
the GPUI times. `TestAppContext` (present discarded) is recorded too and
matches the X11 draw times.

## Results (after climb, with GPUI)

Frame CPU is build + layout + paint (nanoui `Tester.frame` / GPUI
`Window::draw`). Encode is nanoui's CPU raster into pixels.

| scene | nanoui frame | nanoui encode | GPUI frame (X11/Blade) | egui | iced tree | slint | clay |
|---|---:|---:|---:|---:|---:|---:|---:|
| boxes | 0.074 ms | 24.0 ms | 1.444 ms | 0.107 | 0.072* | ≤1.05† | 0.064 |
| text | 0.205 ms | 2.1 ms | 2.285 ms | 0.315 | 0.033* | 17.4 | — |
| scroll | 0.510 ms | 2.0 ms | 14.601 ms | 1.431 | 0.377* | ≤1.14† | — |
| list | 0.057 ms | 2.0 ms | 0.380 ms | — | — | — | — |
| dashboard | 0.044 ms | 12.8 ms | 0.340 ms | — | — | — | — |
| springs | 0.571 ms | 4.7 ms | 5.562 ms | 0.334‡ | 0.281*‡ | ≤1.04†‡ | — |
| letters | 0.081 ms | 0.71 ms | 1.474 ms | — | — | — | — |

\* iced times are widget-tree build only (no layout/present hook).
† Slint 1 ms timer floor except text.
‡ egui/iced/slint "springs" are `sin()` offsets. GPUI and nanoui solve
the same closed-form spring (k=240, c=26, m=1).

nanoui **leads GPUI on every scene's frame CPU** (about 10–30× on
boxes/text/scroll/springs). It leads egui on boxes, text and scroll.
Clay is still slightly ahead on boxes layout (0.064 vs 0.074) and draws
nothing.

The Linux gap vs a live GPUI window is **encode**, not the view tick:
Gaussian shadows on boxes/dashboard are 13–24 ms on the CPU. GPUI's
Blade present was not timed here (hung on lavapipe). A 60 Hz CPU window
would drop on those two scenes; the OpenGL path is the intended live
path when a GPU exists.

`--cheap-shadow` (1 Y-sample instead of Metal's 4) cuts boxes encode
24.0 → 13.5 ms (−44%) and dashboard 12.8 → 7.4 ms (−42%). It does
**not** match the Metal raster tests; default stays Metal's (4 then, 8 now).

ReleaseFast binary: gallery 8.1 MB, counter 6.9 MB. Idle CPU is 0
(nothing polls).

## Steps

### 0. Baseline

Motion API expansion and `scroll_max` on every scroller. First Lin

## Top-level structure

- `src/` — framework: `nanoui.zig` public API, `ui/` native GPU/CPU UI (Metal, OpenGL, raster), `page_*` webviews, `linux/`/`windows/`/`ios/`/`android/` backends, `kit/` GPUI-Kit-style components, `tsgen.zig` / `bridge.js` for typed JS IPC
- `examples/` — hello, gallery, counter, todo, browser, map, board, duo, drop, turn, sgbus, access, basics
- `apps/` — git submodules: nanoterm, nanomon, nanomail, nanolight, nanostudio, nanofly, stageshow
- `docs/` — platform notes (android, linux-perf, motion, windows-ime, windows-pages) + images
- `tools/` — iOS/Android packaging scripts, linux.Dockerfile, version.sh
- `hillclimb/` — headless benchmarks vs mygo / history
- `bench/` — performance benches
- `build.zig` / `build.zig.zon` — Zig 0.17, version 0.11.0; lazy http-zig dep for Linux/Windows
- `AGENTS.md` — hard rules for humans and coding agents (600-line file limit, headless-only testing, no screen driving)
- `.agents/skills/` — agent skills directory present
- `nui` CLI — scaffold/test/snapshot apps for people and coding agents (`zig build nui`)

