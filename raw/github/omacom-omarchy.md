# omacom/omarchy

## Metadata
- Stars: 45279
- Primary language: Shell
- Default branch: quattro
- Latest release: v4.0.6
- License: MIT License
- Homepage: https://omarchy.org
- Pushed: 2026-10-20T06:45:26Z
- Fetched: 2026-10-20
- Final URL: https://github.com/omacom/omarchy

## Description
Beautiful, Modern & Opinionated Linux

## README
# Omarchy

Omarchy is a beautiful, fun & agentic Linux distribution by DHH.

Read more at [omarchy.org](https://omarchy.org).

## The Omarchy Manual

The manual lives in [`manual/`](manual/), which is its authoritative source.

- [Welcome to Omarchy!](manual/01-welcome-to-omarchy.md)

**The Basics**

- [Getting Started](manual/02-getting-started.md)
- [Coming From Mac or Windows](manual/03-coming-from-mac-or-windows.md)
- [Navigation](manual/04-navigation.md)
- [The top bar](manual/05-the-top-bar.md)
- [Themes](manual/06-themes.md)
- [Hotkeys](manual/07-hotkeys.md)
- [Unified Clipboard & History](manual/08-unified-clipboard-history.md)
- [Reminders](manual/09-reminders.md)
- [Notices](manual/10-notices.md)
- [Text Extraction & Dictation](manual/11-text-extraction-dictation.md)
- [Screenshots & Recording](manual/12-screenshots-recording.md)
- [Toggles, idle & screensaver](manual/13-toggles-idle-screensaver.md)
- [Omarchy CLI](manual/14-omarchy-cli.md)

**The Applications**

- [Terminal](manual/15-terminal.md)
- [Neovim](manual/16-neovim.md)
- [AI](manual/17-ai.md)
- [Development Tools](manual/18-development-tools.md)
- [Shell Tools](manual/19-shell-tools.md)
- [Shell Functions](manual/20-shell-functions.md)
- [TUIs](manual/21-tuis.md)
- [GUIs](manual/22-guis.md)
- [Browsers](manual/23-browsers.md)
- [Commercial apps/services](manual/24-commercial-apps-services.md)
- [Web Apps](manual/25-web-apps.md)
- [Gaming](manual/26-gaming.md)
- [Filling out PDFs](manual/27-filling-out-pdfs.md)
- [Windows VM](manual/28-windows-vm.md)
- [Other Packages](manual/29-other-packages.md)

**Configuration**

- [Updates](manual/30-updates.md)
- [Dotfiles](manual/31-dotfiles.md)
- [Shell plugins](manual/32-shell-plugins.md)
- [Monitors](manual/33-monitors.md)
- [Keyboard, Mouse, Trackpad](manual/34-keyboard-mouse-trackpad.md)
- [Networking](manual/35-networking.md)
- [System sleep](manual/36-system-sleep.md)
- [Hardware authentication](manual/37-hardware-authentication.md)
- [Fonts](manual/38-fonts.md)
- [Backgrounds](manual/39-backgrounds.md)
- [Prompt](manual/40-prompt.md)
- [Branding](manual/41-branding.md)
- [Common tweaks](manual/42-common-tweaks.md)
- [Making your own theme](manual/43-making-your-own-theme.md)

**The Rest**

- [Mac support](manual/44-mac-support.md)
- [Troubleshooting](manual/45-troubleshooting.md)
- [FAQ](manual/46-faq.md)
- [System snapshots](manual/47-system-snapshots.md)
- [Security](manual/48-security.md)
- [Omarchy on...](manual/49-omarchy-on.md)
- [Dual Boot Install](manual/50-dual-boot-install.md)
- [Unattended Installs](manual/51-unattended-installs.md)

## License

Omarchy is released under the [MIT License](https://opensource.org/licenses/MIT).

## Docs
### docs/ listing
```
file	audio-tuning.md
file	cli-router.md
file	elsewhen.md
file	file-layout.md
file	i18n.md
file	input-methods.md
file	lifecycle-dispatch.md
file	menu.md
file	notifications.md
file	omarchy-shell.md
file	passwordless-sudo.md
file	testing.md
file	theming.md
file	update-process.md
```

### docs/audio-tuning.md
```
# Speaker tunings

Laptop speakers ship voiced by the vendor's Windows DSP layer, which Linux does
not get. A tuning restores that as a PipeWire filter-chain in front of the
internal speaker sink: a declarative graph hosted by a small PipeWire client, with
no GUI app and no binary blob.

```
default/audio/tunings/<vendor>-<model>/
├── tuning.conf        # description, match, provenance, measurements
└── filter-chain.conf  # the graph, with @SPEAKER_SINK@ substituted on install
```

`on` renders the graph into `~/.config/pipewire/omarchy-speaker-tuning.conf.d/`
(plus the shared host config `omarchy-speaker-tuning.conf`, from
`default/audio/filter-chain-host.conf`) and runs it as its own PipeWire client via
`omarchy-speaker-tuning.service`, rather than
loading it into the audio daemon. The daemon only reads its own config at startup,
so a daemon-loaded tuning could only be switched by restarting PipeWire — which
drops every PulseAudio client's connection, and applications that do not reconnect
(Spotify) then have to be restarted by hand. Hosting it separately makes switching
a start/stop of one small process, and contains failure: a malformed tuning breaks
only that service instead of stopping PipeWire from starting at all.

Tunings apply automatically: `install/hardware/speaker-tuning.sh` installs the
LV2 dependency and `install/user/first-run/audio-tuning.sh` applies the tuning,
both gated on the match. Machines without a matching tuning are untouched.

Switching it on happens at first-run, not at finalize-user time, because finalize-user
also runs in the ISO chroot where there is no audio server: the sink a tuning has
to target does not exist there, so nothing could be written — and nothing would
retry, since the finalizer marks all shipped migrations complete on a fresh
install. Matching itself deliberately does not consult the audio graph, so the
LV2 dependency is still installed in the chroot.

```bash
omarchy audio tuning on        # install the matching tuning
omarchy audio tuning off       # remove it, back to raw speakers
omarchy audio tuning status    # installed? in use? what matches?
```

`match` and `fronted-sink` are also accepted; they exist for the install hooks
and the sink-listing scripts rather than for daily use.

`on` verifies its own work: it waits for the tuning sink to appear and confirms
its output linked to the expected physical sink, and uninstalls everything again
on either failure — so a broken tuning cannot be left half-applied. It also
switches the default sink to the tuning and moves existing app streams onto it
(`off` reverses both). When everything is already installed and linked, `on` is
a no-op; pass `--force` when iterating on a tuning in place.

## Adding a tuning

Add a directory with a `tuning.conf` and a `filter-chain.conf`. No new command is
needed: matching is data. A tuning declares how to recognise its hardware, plus the
`sink_pattern` its graph targets:

| Key | Matches on | Notes |
|---|---|---|
| `match_sku` | DMI product SKU, whole value | Most precise. Vendors key speaker firmware on it, so it identifies the hardware rather than a marketing name |
| `match_dmi` | DMI product name or family, substring | Convenient, but a short string widens fast — `product_family` here is `Dell Laptops` |
| `match_command` | Any predicate you name | For hardware needing a sharper test than either |

`match_sku` and `match_dmi` are lists, so one tuning can cover several models it has
been validated on:

```bash
match_sku=("0DB9" "0DBA")   # XPS 14 and XPS 16
```

Only the first *defined* key is consulted, in the order `match_command`,
`match_sku`, `match_dmi` — keys below a defined one are ignored, and a tuning
defining none never matches.

`sink_pattern` is required whichever method you use, since the graph's target sink
is substituted from it. The graph must also keep two fixed properties: the sink
node is named `omarchy_speaker_tuning` (the install checks for that exact name,
so renaming it silently fails verification), and its output stream sets
`node.dont-fallback` alongside `node.dont-move`, so WirePlumber cannot link it
somewhere else when the target sink is absent at host start.

Gate narrowly and widen as models are validated; a tuning aimed at the wrong
drivers can sound worse than none and can stress them. When a tuning covers a model
it was not measured on, say so in `tuning.conf` — the provenance fields are there to
keep that distinction visible rather than implied.

Two hard requirements:

- **End in a limiter.** Peaks must stay under 0 dBFS with headroom.
- **Do not boost what the drivers cannot deliver.** The XPS 14 tuning
  deliberately *cuts* 40 Hz by around 18 dB. Excursion down there buys nothing
  and costs distortion.

## Building one

Measuring a laptop and fitting a filter-chain to it is a separate job with its own
tools, in [omarchy-audio-tuner](https://github.com/omacom-io/omarchy-audio-tuner).
It is not installed by default — almost nobody authoring a tuning, and it needs
python, ffmpeg and mpv.

```bash
omarchy pkg add omarchy-audio-tuner
```

Its README is the walkthrough, and covers both cases: copying a reference that
already sounds right (how the XPS 14 tuning was made, no microphone needed), and
designing from scratch, which needs a *calibrated* measurement mic and a target
curve that measurement alone cannot give you.

## What a tuning must report

A tuning is not reviewable on "sounds better to me". Record these, measured, in
`tuning.conf`:

| Field | What it is |
|---|---|
| `magnitude_rms_db` | Deviation from the reference or target it was fitted to |
| `bass_group_delay_swing_ms` | Max minus min group delay, 30–300 Hz |
| `limiter_headroom_db` | Worst-case peak against the limiter threshold |
| `dynamic_range_delta_lu` | LRA change against the reference |

Measure electrically by capturing the physical speaker sink's monitor, which sits
upstream of the volume control, so results are independent of listening level.

## How this fits the audio graph

Two things about the surrounding system are worth knowing, because both caused
real bugs:

- **Volume lives downstream of the tuning.** A tuning is a virtual sink that
  becomes the default output, and changing *its* volume would alter the level
  going into the processing — moving the display while the speakers stay put, and
  changing the tone of anything with a compressor or limiter in it.
  `omarchy-audio-output-sink` is the single definition of "which sink does this
  output's volume really use": it resolves a sink through any DSP sink to the
  physical one, and with no argument resolves the current default output. The
  volume keys, the output switcher's OSD and the audio panel all use it, so they
  cannot disagree. Resolving the *current default* rather than "whatever a tuning
  fronts" is what keeps it correct when headphones or HDMI are selected while a
  tuning still exists.
- **The fronted sink is hidden.** The tuning and the physical speakers both exist
  in the graph, and selecting the physical one would only bypass the tuning. So
  `omarchy-audio-sink-availability` reports it unavailable and
  `omarchy-audio-output-switch` skips it, leaving one speaker entry in the panel.
  A WirePlumber smart filter would remove the need for both — it leaves the real
  device as the default output — but on PipeWire 1.6.8 / WirePlumber 0.5.15 the
  graph loads and links correctly as a smart filter and then passes audio through
  unprocessed. Revisit when that is understood.
- **EasyEffects cannot coexist with a tuning.** It moves any stream that follows
  the default sink to its own sink, so it would grab audio back from a
  filter-chain. `on` refuses while it is running rather than installing a graph
  that would be bypassed.
- **The tuning's own output must not be moved.** A filter-chain's output is a
  playback stream like any other, so anything rerouting "all streams" to a newly
  selected output would drag the processing with it — onto headphones, or into the
  tuning's own sink, which is a cycle. The tuning sets `node.dont-move`, and
  `omarchy-audio-output-set-default` moves only streams that carry an
  `application.name`.
```

### docs/cli-router.md
```
# The Omarchy CLI router

`bin/omarchy` maps spaced commands onto the flat `bin/omarchy-*` namespace:
`omarchy theme set foo` becomes `exec bin/omarchy-theme-set foo`. There is no
registry to maintain — every executable `bin/omarchy-*` file is a command, and
its filename is its default route. Metadata comments in the file header refine
how it presents and routes; the keys are documented in
[`agents/skills/command-metadata.md`](../agents/skills/command-metadata.md).
This document covers what that guide does not: how resolution and dispatch
actually work.

## How a binary becomes routes

The stem after `omarchy-` splits at the first hyphen: `omarchy-theme-set` gets
group `theme` and name `set`, with remaining hyphens becoming spaces
(`omarchy-hw-asus-rog` → group `hw`, name `asus rog`). A single-segment stem
(`omarchy-update`) is the root command of its own group, with an empty name.

Every command registers two routes: the canonical route `omarchy <group>
<name>` after metadata overrides, and the filename route with *all* hyphens
turned to spaces. When metadata moves nothing, they are the same route. When it
does, both keep working — `# omarchy:name=gaming xbox-cloud` on
`omarchy-install-gaming-xbox-cloud` keeps the hyphen inside the name, so
`omarchy install gaming xbox-cloud` is canonical while the filename route
`omarchy install gaming xbox cloud` still resolves. An explicitly *empty* `#
omarchy:name=` makes a command the root of its group: `omarchy-menu-share` sets
`group=share` and an empty name, so its canonical route is `omarchy share`
while `omarchy menu share` remains as the filename route. Alias routes register
the same way but are flagged, so listings show them as aliases rather than
commands.

Two routes claiming different binaries is a collision: the first registration
wins, dispatch is unaffected, and the conflict is recorded for `omarchy
commands --check` to report. Hidden commands (`# omarchy:hidden=true`) still
register and dispatch normally — hiding only removes them from listings, which
is how install-time plumbing like `omarchy apply hardware` stays callable
without being browsable.

Metadata is read from the comment header only: the first 80 lines, stopping at
the first non-comment line, so metadata-shaped comments after code never take
effect. Malformed `omarchy:` lines and unknown keys are ignored rather than
fatal — a typo degrades a command to its filename route instead of breaking the
router. The first plain comment line doubles as a fallback summary, and a
command with no comments at all still gets a generated one, though `--check`
demands the explicit form (below).

## Dispatch

Resolution is longest-prefix: the router tries the full argument list as a
route, then drops trailing words until something matches. Whatever it drops is
passed to the binary as arguments. This runs in two passes.

The fast path joins argument prefixes with hyphens and checks for an
executable file: `omarchy theme set foo` probes `omarchy-theme-set-foo`, then
`omarchy-theme-set`, which exists — resolved without reading a single metadata
header. This exists because plain dispatch is the hot path: parsing the
headers of several hundred binaries on every invocation is measurable
latency (`omarchy dev benchmark cli` tracks it), and a filename probe is a few
stat calls. Metadata loads lazily, only for the resolved command when help is
needed.

When no filename matches — metadata-moved routes like `omarchy share`, and aliases like `omarchy screenshot` — the router first loads only the commands that could own a route under the first word: those whose filename starts with it, and those whose header names it as their group or in an alias. If that resolves a route that runs its command, it dispatches from there, about as fast as a filename route. Help output, a route that needs arguments it wasn't given, and anything still unresolved fall back to loading all metadata and resolving against the full route table, with the same longest-prefix rule, since help lists related commands from the whole table.

Both paths intercept `--help`/`-h` *anywhere* in the leftover arguments, not
just the first one. Resolution can succeed with unresolved words still ahead of
the flag — `omarchy update aur --help` resolves `update` with leftovers `aur
--help` — and checking only the first leftover once let that invocation start a
real update. A `--` ends the scan: everything after it belongs to the command,
so `omarchy foo run -- --help` forwards the flag. `--json` alongside `--help`
switches the help output to the command's JSON record; `--json` alone is just
an argument for the command.

Bare invocations are also guarded. If a command declares required arguments
(its `args` metadata, minus `[bracketed]` optional parts, is non-empty) and
none were given, the router shows help instead of executing — `omarchy theme
set` prints usage rather than running an interactive setter. A bare group name
with child commands shows the group help.

Dispatch is `exec`: the router process is replaced, the binary sees only the
leftover arguments, and the exit code is the binary's own. The router itself
exits 127 for unknown routes or missing binaries.

When nothing resolves, the router tries a prefix listing — `omarchy hw asus`
prints every command whose usage starts with that prefix — and otherwise
errors with a "did you mean" suggestion (a known route extending the first
word) and a pointer to `omarchy commands --all`.

## Groups and the top-level listing

Group help is synthesized from metadata, not written anywhere. A command
belongs to a group when either its metadata group or its filename group
matches, listed under the route that fits the group being viewed: `omarchy
menu --help` shows `omarchy-menu-share` as `omarchy menu share`, while its
canonical `omarchy share` stands alone. On the fast path, group help loads
only that group's filename-prefixed binaries rather than everything.

The top-level `omarchy` listing is driven entirely by the hand-curated
`GROUP_DESCRIPTIONS` table in `bin/omarchy`, which also titles each group's
help. An entry there advertises the group even when every command in it is
hidden — which is exactly why `apply` and `provision` have none: they route,
but a listing entry would put install-time plumbing back in front of users
(see the Command Naming section of `AGENTS.md`). Adding a browsable command
group means adding its `GROUP_DESCRIPTIONS` entry; adding hidden plumbing
means deliberately not doing so.

## Introspection

`omarchy commands` prints every non-hidden command with its summary, plus an
alias table. `--all` includes hidden commands, `--markdown` emits a table, and
`--json` emits full records: route, binary, group, name, summary, flags, args,
examples, aliases, `filename_route`, and `routes` (the union of everything
that resolves to the binary). Per-command JSON comes from `omarchy <route>
--help --json`.

`omarchy commands --check` is the metadata lint, run by `test/cli`. It fails
on:

- route collisions between binaries
- a missing explicit `# omarchy:summary=` — a plain-comment fallback renders
  in help but does not satisfy the check
- invalid boolean metadata: `hidden` and `requires-sudo` must be `true` or
  omitted, never `false`
- a registered command whose binary is missing or not executable

When debugging a routing surprise, `omarchy <route> --help` shows the resolved
binary and, when it differs, the filename route; `omarchy commands --all
--json` shows every route the router knows.
```

### docs/elsewhen.md
```
# Elsewhen

A world clock for the Omarchy shell: a globe in the bar that opens a panel of clocks, one row per city, with a spinnable globe behind it. It lives in `shell/plugins/panels/elsewhen/` under the plugin id `omarchy.elsewhen`, and file names below are relative to that directory. Its checks live in `test/shell.d/elsewhen/` and run as part of `./test/shell` through `test/shell.d/elsewhen-test.sh`.

Everything it needs is already on an Omarchy install: `date` and `timedatectl` for zone offsets, `curl` for weather and places, and `jq` for reading GitHub profiles. The network is touched for three things only: [Open-Meteo](https://open-meteo.com) geocoding and forecasts, without an API key, and the public GitHub profile of anyone added to a city by handle. The globe's coastlines are [Natural Earth](https://www.naturalearthdata.com) 110m (public domain), shipped as `world.json`. Settings live inline on the widget's `shell.json` entry; see [Settings](#settings).

## Why it shells out to `date`

Qt's QML engine has no `Intl`, so JavaScript cannot be asked for the time in an arbitrary IANA zone. Instead a single `date` probe reports each zone's current UTC offset and abbreviation, and the rows tick locally against those offsets. Offsets only move at a DST boundary, so the probe re-runs whenever the panel opens and every five minutes while it stays open.

## Reordering

Grab the body of a row and drag it up or down. The row lifts and follows the pointer while the ones it passes step aside by exactly one row; the new order is written to `shell.json` on release.

Three things make it feel solid:

**The pointer is measured in the Column, not in the row.** The grab area sits inside the row, and the row is translated as it is dragged - so reading `mouse.y` directly is a feedback loop: the local frame slides out from under a stationary pointer, the offset chases itself, and the row stutters. `mapToItem` into the (never-moving) Column gives a stable reading.

**The target slot has hysteresis.** Recomputing it freely means a pointer resting near a boundary flips between two slots on sub-pixel movement. The target only changes once the pointer is 0.6 of a row past the current slot, so jitter at a midpoint holds steady.

**The drop is animated.** On release the row glides the remaining distance into its slot and the reorder commits when it arrives, rather than the row vanishing from under the pointer. Rows making room ease aside too - but the dragged row itself is excluded from that easing, or it lags the cursor.

The list itself is **not** touched while the pointer moves - rows are displaced with a `Translate` transform, which is purely visual and leaves the Column's layout alone. Reordering the model mid-drag would replace the array the Repeater is built from, rebuild every delegate, and drop the gesture half-way through.

Rows are not all one height - a city with people in it carries an extra line - so the gesture measures each row it passes by that row's own height, taken from the rows themselves when the grab starts. The rows stepping aside still move by the dragged row's height, which is the space it leaves.

The grab area stops above the daylight strip, so vertical reordering never competes with the strip's horizontal scrub, and it is declared before the remove button so that keeps its taps. A few pixels of slack are required before a drag arms, so a click is never a reorder.

## The first run

A fresh install has no configuration and asks for none. The first time the panel opens it writes its own starting list: **the city you are in, plus four well-known destinations spread round the clock from it** - five rows, so it looks like a world clock immediately rather than an empty box with an "add a city" button.

The four are chosen **relative to home**. A fixed list would hand someone in Paris a second Paris, and would give a reader in Tokyo a spread that is really a spread around California. From Los Angeles the list comes out as New York, London, Dubai, Tokyo; from Copenhagen as Delhi, Tokyo, Los Angeles, New York.

Candidates are taken in order of how well known they are, and one is kept only if it is at least three hours from home *and* from every city already picked - so the gap does the spreading rather than a rule about spacing. Spacing four cities evenly round the dial and taking whoever is nearest each mark gives a tidier spread but a stranger list: from Los Angeles it produces Sao Paulo, Cairo, Bangkok and Auckland, which is even but reads like a lottery. If somewhere has too little of the world far enough away - the Pacific, mostly - the three-hour gap relaxes rather than returning a short list. The result is sorted eastward, so the list walks round the world.

It costs one process: the same `date` probe that reads the local zone also prices the candidate cities on that first run, and never again. The local zone is emitted twice in that probe - once as the `LOCAL` marker and once as an ordinary row - so home's own offset is available like any other city's, which the picker needs and cannot ask for in advance.

Everything is written to `shell.json` as a normal list, so the first thing anyone can do is delete or reorder it. `test/shell.d/elsewhen-model-test.sh` runs the whole thing from fifteen different home cities, including UTC, Kathmandu's forty-five-minute offset, and the Pacific.

## Adding and removing cities

`+ Add a city` opens an inline search over the system's zone list. Clicking a result adds it; hovering a row reveals a `×` in its top-right corner to remove it. The last row cannot be removed. Changes are written straight back to this widget's entry in `~/.config/omarchy/shell.json`, so they survive a restart.

The search is driven from the keyboard: type, walk the results with the up and down arrows, Return adds the highlighted one, Escape closes. The selection starts on the first match, so the common case - type three letters, press Return - never needs an arrow at all, and it wraps at both ends because the list is six long and entirely on screen. A changed query puts the selection back on the first row: the list under it has been replaced, and Return should not add a city nobody looked at.

Both lists name the zone and say where it is: `Asia/Kathmandu  UTC+5:45`. The name alone does not settle it - half a dozen entries share `America/Los_Angeles`, and `Asia/Kolkata` tells you nothing about India being half an hour off the hour until it says `UTC+5:30`. The offset is absolute rather than relative to you, unlike the `+9h` on a tracked row: a city you have not added yet has no relationship to you yet.

Search results are not covered by the probe that feeds the rows - that one only knows the cities you track - so the offsets come from a second `date` call over whatever the list is currently showing, coalesced while one is in flight. The answers are merged into what is already known rather than replacing it, so the column does not blank on every keystroke. Its command is set when it starts rather than bound to the list: the probe is started from the list's own change handler, which can run before a binding on that same list has caught up, and then it probes the list before last.

### Searching places, not just zones

The zone list only knows the tz database's representative cities, and most towns are not one. Someone in Fort Lauderdale could pick New York or Miami, and either way the row geocoded and fetched the weather for somewhere they are not.

So the search also asks the geocoder. Open-Meteo's geocoding answers with each place's name, region, coordinates and - the part that makes this work - the IANA zone it keeps, which is everything a row needs. It is the same keyless service the weather already uses, so nothing new is trusted.

The zone matches come first and are there on the first keystroke; the places join underneath once three letters have been typed and the typing has paused for 300 ms. One lookup runs at a time and the latest query wins, and every answer is kept for the session, so backspacing never asks twice. A failed lookup is kept as no places, so the list stops saying it is searching.

Keeping the offline matches first means the old keyboard flow is untouched: three letters and Return pick what they always did. A city both lists know is shown once, and the offline entry takes the geocoder's region and coordinates, so "Portland" reads `Portland  Oregon, US` and adding it never geocodes again. A place's row shows its region in place of the zone name - "Florida, US" says where it is better than `America/New_York` does, and the offset beside it still says what time it keeps.

A place added from the search brings its coordinates with it, and a row with coordinates is never geocoded by name. That stops a city's weather depending on the geocoder guessing right a second time, and it is what lets two Springfields be told apart: Springfield, Illinois and Springfield, Missouri both keep Central time, are listed separately, and the second one added is named `Springfield (Missouri)`, since a row is known by its name and zone. A place already on the list is left out of the results, recognised by where it is.

A weather reading remembers the point it was taken for, so a city whose coordinates move - a better pick for here, say - gets fresh weather rather than its old spot's for the rest of twenty minutes.

The geocoder's answer is network input and is read as such: only a real list, and no more entries than were asked for, so a malformed answer cannot hold the shell's UI thread in a loop. The globe's jump box searches places too, and a session city found that way flies to the exact spot. The globe holds one city per name, so a jump is matched by where the town is: Springfield, Missouri after Springfield, Illinois goes to Missouri, joining as `Springfield (Missouri)`, and the globe sets off for the picked coordinates without waiting for it to land.

The globe's own **jump box** works the same way - arrows, Return, Escape, selection on the first match, wrapping over five results. Its results grow upward out of the field rather than down from it, but the first match is still at the top of them, so Down moves down the screen and down the list at once.

**A zone is not a city.** Six of the picker's entries share `America/Los_Angeles`; the name is the only thing telling Oakland from Las Vegas from Los Angeles. Committing a choice passes the label alongside the zone, so picking Oakland puts "Oakland" on the list rather than "Los Angeles".

The `×` is placed from the corner rather than centered in its target, so how tucked-in it reads does not depend on how big the target is. The target itself is anchored flush into the corner and is larger than the mark, because a corner is the easiest place on a row to hit.

The search is rendered inline rather than in a dropdown popup: the shared `SearchableDropdown` only ever opens downward, and this panel hangs off a vertical bar low on the screen, so its list would run off the bottom edge.

Inline, the list grows the panel instead - but only up to the card's cap, the screen's height or `space(680)`, whichever is smaller. Past that the content is clipped to the card and scrolls, and while the search is open the panel follows the results down so the last one is not left clipped against the bottom edge.

Scrolling is the wheel only. The rows own the pointer - drag-to-reorder and the scrub strip are `MouseArea`s with `preventStealing` - so an interactive `Flickable` would be fighting them for every gesture.

### City aliases

The tz database ships one representative city per zone, so most places people actually search for are missing — there is no `Miami`, only `America/New_York`. `CITY_ALIASES` in `Model.js` adds extra search entries pointing at the zone that governs them. Adding a city is a one-line change; the only rule is that the zone must be the one that place actually observes, DST rules included.

Two cities may share a zone (Miami and Boca Raton are both `America/New_York`), so a row is identified by its label and zone together, and removal is by position.

The aliases are the offline floor - they work with no network and on the first keystroke - but they no longer need to grow, since the place search finds the rest.

## The stored list

The list is `cities` on the widget's `shell.json` entry, one object per row:

```json
"cities": [
  { "name": "Fort Lauderdale", "zone": "America/New_York", "lat": 26.12231, "lon": -80.14338, "region": "Florida, US" },
  { "name": "Cincinnati", "zone": "America/New_York", "people": ["Ann", "@octocat"] },
  { "name": "Tokyo", "zone": "Asia/Tokyo" }
]
```

`lat` and `lon` come as a pair or not at all, and only a city found by the place search has them; the rest are geocoded by name as before. `people` is optional.

It replaced a `zones` string, `"Label|Zone, Label|Zone"`, which had no room for coordinates (a comma was its separator) or for people. There is no migration: a config with no `cities` is read from `zones`, and the first change writes `cities` and removes `zones`. A config nobody touches keeps working as it was.

## The daylight strip

Each row carries a 24-hour bar, midnight to midnight in that city's own clock, with the daylight lit and a marker at now. Read down the column and you can see who is awake: markers inside the lit band are in daylight, markers out at the dark ends are not. Rows are also filled by phase, lightest at midday and darkest at night.

The lit band is the city's real day, from the coordinates the weather lookup already geocodes. Reykjavik's four-hour December day and Auckland's long January one are different shapes, and that difference is most of what a daylight bar is worth looking at. A city the geocoder has not placed yet gets a fixed 06:00-18:00 band until its coordinates arrive.

The marker turns gold while it is inside the lit band and stays white outside it. That is decided geometrically, from the same span the band draws, not from the phase name - so the sun can never be painted sitting in the dark half of its own bar. The gold is a literal color rather than a theme role, because several themes map the palette name `yellow` to something that isn't yellow.

`Sun.js` computes the day, built on the globe's own `subsolarPoint` rather than a second copy of the astronomy. Declination comes straight off that function and the equation of time is recovered from it - `subsolarPoint` builds its meridian as `lon = -15 * (utcHours - 12) - eot`, so running that relation backwards hands the correction back with nothing new to keep in step. Local solar noon is found by iterating: the subsolar meridian sweeps west at a steady 15 degrees an hour, so the gap between where the sun is and where you want it converts straight into a time correction, and three passes put the residual under a second.

`test/shell.d/elsewhen-sun-test.sh` checks it against Open-Meteo's published sunrise and sunset for thirteen cities - both hemispheres, both solstices, the equator, and Kashgar, which runs on Beijing time and sees the sun rise at 08:23 by the clock. The reference rows are held in the test verbatim so it stays offline.

It is inside a minute at mid-latitudes, and about four minutes at Nuuk and Anadyr, both a little past 64 degrees north. That is the shared low-precision solar position doing what it says: it is good to a fraction of a degree, and near the poles the sun crosses the horizon at such a shallow angle that a fraction of a degree is minutes of time. The two high-latitude cities are in the test with the tolerance they actually need rather than left out.

A bar can be lit at both ends, and that is not a drawing fault. Reykjavik on the June solstice sets four minutes after midnight, so the first four minutes of the same day are lit too - by the sun that rose the morning before. The day is drawn where it falls and again a day either side, and only the parts that land on the bar survive.

The arrows do not wrap with it. A sunset at 00:04 belongs to the next bar along, and a mark pinned to this one's edge would claim the sun set at midnight.

Above the Arctic circle there is no sunrise to plot, and that is a real answer rather than an error: `kind` comes back as `midnightSun` or `polarNight`, the band is the whole bar or none of it, and no arrows are drawn. Longyearbyen in June and in December are both in the test.

### The arrows

An up arrow just before the band and a down arrow just after it, shown while the pointer is on that row and outside the lit part rather than on its edge - a mark sitting on the boundary reads as part of the band and gets lost in it. The band already says how long the day is; the arrows say which end is which. They keep off the resting state: five rows each carrying two arrows all the time is a lot of furniture for something looked up rarely.

They are tucked in close to the band. The tap target is finger-sized and the glyph sits in the middle of it, so a box placed flush against the crossing would leave the arrow half a box away. A nudge closes most of that without letting the glyph touch the band.

Sunrise sits two pixels high and sunset two pixels low. The glyphs are the same height and the same shape reversed, which is the pair the eye is worst at telling apart at this size. The offset gives a second, coarser cue that needs no reading: the one above the line is the one going up.

Click one and it prints `Sunrise 6:16 AM` in a small dark chip above the bar - named, not just numbered, because a bare time floating over a row that already has a clock on it has to be worked out from which arrow was clicked. One at a time, and it clears when the pointer leaves the row.

Above and not below, because below is where the pointer is. The chip floats over the date line, which is why it has a ground of its own, and its colors are inverted in every theme the way a tooltip is. The arrows carry `z: 1` so the chip paints over the row's time block, which is declared after them.

They are declared after the strip's scrub `MouseArea`. That one covers the whole bar to drag time, and an earlier sibling would never see a press - the same later-sibling rule the remove button relies on.

An arrow hides while the marker is standing on it. Two things drawn at the same point read as a printing fault, and the arrow is the one that can be spared: it marks a boundary that is not going anywhere, while the marker is the only thing on the bar that says when now is. It follows `nowMarker.x` and not the row's progress, so the arrow comes back exactly as the sun clears it - the marker's motion is eased, and progress is where it is going, not where it is. Hidden rather than faded, because invisible is also untappable: a click on the sun should scrub time the way it does everywhere else on the bar. If the marker covers an arrow whose time is open, the chip closes with it.

Clicking the marker itself does not name the moon's phase: the marker is also the scrub handle, so aiming at a ten-pixel dot to read a label would nudge the whole list off the hour on every miss. Shift-clicking the moon runs the phase animation instead, which is a deliberate gesture rather than one you land on by aiming badly.

Clicking anywhere else on the row puts the chip away. A tooltip that can only be dismissed by hitting the same few pixels that opened it is a trap.

A click on an arrow stops at the arrow: the scrub bar and the row's reorder grab underneath record no press at all, so the scrub bar needs no guard against the arrows drawn on top of it. That is measured rather than reasoned - see [Testing what the pointer does](#testing-what-the-pointer-does).

A press on the row body does still reach the grab, which dismisses, so the two decisions can meet on one click. Neither rule reads the live value; both are answered from what was showing when the press began, which is the same number whichever runs first. The two rules are `Model.chipAfterTap` and `Model.chipAfterRelease`, and `test/shell.d/elsewhen-model-test.sh` plays a click through both delivery orders across every case: opening, closing, swapping one chip for another, and a release that must not undo a chip opened during the same press.

## Weather

Each row shows the current temperature beside the city name, and one glyph beside it: sun, partly cloudy, cloud, rain, or snow. The glyph sits with the temperature because the two are the same fact about being outside.

Open-Meteo reports WMO present-weather codes - nearly a hundred of them, separating drizzle from freezing drizzle from rain showers. `Model.weatherKind` collapses them to those five, which is all a row has space for; fog joins cloud rather than getting a symbol nobody could read at this size. The code travels with the temperature in the same reading, so the two cannot disagree.

The sun is `white-balance-sunny`, not `weather-sunny`. The obvious one is a hollow ring inside a six-point burst, which at eleven pixels reads as a snowflake - sitting directly beside an actual snowflake. The one in use is a solid disc with short rays, which cannot be mistaken for anything else in the set.

`Number(null)` is `0`, and `0` is the WMO code for *clear sky* - so a missing reading would quietly render a sun. Absent values are rejected before the conversion; `test/shell.d/elsewhen-model-test.sh` covers it.

The panel fetches it with `curl`, in two steps: one geocoding request per city it has no coordinates for yet, then one batched forecast for every city. Both results live in memory as `facts`, keyed `label|zone`. Geocodes last the session (a city does not move) and weather twenty minutes (the resolution the source offers), so opening the panel again soon does no network at all. Nothing here is fatal - a failed fetch keeps the previous value, and failing that the row simply renders without it.

Cities are geocoded by their **label**, not their zone, which matters for aliases: Miami and Boca Raton share `America/New_York` but resolve to their own Florida coordinates and report genuinely different temperatures. Where a label cannot be geocoded, the zone's representative coordinates from `/usr/share/zoneinfo/zone1970.tab` are the fallback; after a network failure that fallback is used for now and the geocode retried on the next refresh.

## The hour's greeting

Point at a row and its date line turns into what people there would actually be saying to each other at that moment: Tokyo at midday says こんにちは, at eight in the evening こんばんは, at three in the morning おやすみ. The pronunciation follows it in grey, because a greeting you cannot say out loud is only a decoration.

The number is the one thing about a time zone that does not travel. "18:40" is the same symbol in every city on the list and says nothing about what 18:40 *is* there. The greeting is the hour as the people in it experience it.

The table is three levels deep - a zone belongs to a country, a country is greeted in a language, and a handful of cities override their country - and it is baked into `Greetings.js` and never fetched. Greetings do not change, and nothing the panel draws on hover should need the network.

Two decisions inside it are judgement calls, and are meant to be:

**It picks the language you would hear, not the one on the paperwork.** Brussels is French, Dublin is Irish, Hong Kong is Cantonese rather than Mandarin, Nairobi is Swahili. An official-languages list would have made several of these duller and one or two of them wrong.

**It does not invent an hourly split where a language has none.** Burmese greets you with မင်္ဂလာပါ at any hour and Thai barely moves, so those tables are one and two bands long. A short table is a fact about the language, not a gap in the data.

The boundaries are where the language moves rather than where a clock does, and the same language disagrees with itself: Spanish in Madrid is still saying *buenas tardes* at 20:00, while Spanish in Lima gave it up an hour earlier. Vienna gets *Grüß Gott* and Zurich *Grüezi* where Berlin gets *Guten Tag*. Indonesian has five bands where English has four - *siang* and *sore* split an afternoon English keeps whole.

The panel's own monospace family carries none of these scripts. Fontconfig substitutes per character, so a Japanese greeting is set in whatever the system has for Japanese and only the Latin ones stay monospaced; Arabic sits right-to-left with its pronunciation in a separate item beside it, which is what keeps the two from being reordered into each other.

**Every zone the picker offers is covered.** The picker offers every zone `timedatectl list-timezones` returns - 598 of them, not just the 74 in `cities.json` - so the table is built from the system's own `zone.tab`. English is checked at the source rather than in the result: a zone may only be greeted in English because some country asked for English, and a zone missing from the table is a failure rather than a silent fall-through to English.

The overrides earn their place by being few. Honolulu is Hawaiian though the United States is English, Montreal is French though Canada is not, and that is nearly the whole list - the country is the right answer almost everywhere.

`test/shell.d/elsewhen-greetings-test.sh` checks everything around the words - that every zone the picker can offer maps to a language, that no hour of any day falls into a gap, that adjacent bands actually differ, and that every non-Latin greeting carries a pronunciation while no Latin one does. The words themselves are the one thing here with no independent reference on this machine, and they want a speaker's eye rather than a test.

### The legacy aliases

The zone table matches each zone's *compiled* zoneinfo file against the ones in `zone.tab`. That is exact for real zones and wrong for the legacy aliases, because an alias shares its rules with whatever zone the tz database linked it to - chosen for keeping identical time, not for being anywhere near it. `Iceland` keeps Abidjan's clock all year, so it would match Burkina Faso and say *Bonjour*; `NZ` would match Antarctica, `Asia/Rangoon` the Cocos Islands, `Africa/Asmera` Djibouti.

Following the tz link table instead does not help: that returns the country of the *canonical* zone, which for `Iceland` is Côte d'Ivoire and for `Pacific/Truk` is Papua New Guinea. There is no rule available here, only places, so the fifteen are named by hand in `ALIAS_COUNTRY` and `countryFor` reads that first.

Two that look like mistakes and are not: `Antarctica/South_Pole` really is in Antarctica and `Pacific/Ponape` really is in Micronesia, whatever zones they share their rules with. `Europe/Simferopol` stays Ukrainian, which is a choice rather than a lookup.

The test checks each alias against the canonical zone for the *same place* - `Iceland` against `Atlantic/Reykjavik`, `Pacific/Truk` against `Pacific/Chuuk` - which is an answer that does not come from the table being tested.

## Time scrubber

Drag any row's daylight strip and **every** clock moves together, so you can ask "if I propose 3pm, what am I doing to Auckland?" and see the answer rather than compute it. The header shows the shifted time in the accent color with the offset from now (`+3h`), so a scrubbed clock can never be mistaken for the real one. Release and it holds for a couple of seconds - long enough to read - then returns to the present. Closing the panel also returns it.

The drag maps *absolutely*: the pointer's position across the strip is a local time-of-day for that city, measured against the unscrubbed present, so a drag cannot accumulate drift. It resolves to the nearest occurrence of that time, so dragging slightly left means an hour ago, never twenty-three hours on.

The rows are modelled on the zone list rather than on the computed clock rows. The clock rows are a binding on the scrubbable, ticking time, so using them as the model would rebuild every delegate on every tick and destroy the `MouseArea` mid-gesture, turning every drag into a single click.

`test/shell.d/elsewhen-model-test.sh` covers the scrub arithmetic, including scrub direction and the short way round midnight.

## Globe mode

Tapping the globe in the header does not swap one view for another: the globe **grows out of the little circle** and shoves the rows aside, and the panel opens out around it. Tapping the cross that takes its place in the circle reverses the whole thing.

One number, `zoom`, runs from 0 (the list) to 1 (the globe). Everything is a function of it - the stage's height, each row's displacement, the globe's scale and position, the cross in the header, the globe's own footer and search bar - so no part of the transition can fall out of step with any other. The animation is on `zoom` alone: 800ms `OutQuart` opening, which spends its speed early and then settles, and a brisker 500ms `InOutCubic` coming back.

**Hold Shift while clicking** to run the whole thing at a third speed - the gesture macOS uses for slow-motion window animations, and free here because every Hyprland binding is SUPER-prefixed. Because one number drives everything, slowing that number slows the rows, the fades and the globe's chrome with it.

The duration and easing are set *before* `globeMode` is flipped, never derived from it. Deriving them from `globeMode` inside the animation is a race - it is the very property whose change starts the animation - and losing that race means an opening transition runs with the closing duration. Every path into globe mode goes through `setGlobeMode` for that reason.

The globe is scaled about **the center of its own disc**, not the center of its box, so it grows from where it is drawn; the translation then carries that center between the little circle and the middle of the stage. The two globes trade places with a quick crossfade while they are still the same size and in the same spot, so there is never a moment with two of them on screen.

Rows are shoved in sequence rather than together - each waits its turn, then covers the rest of the distance - so it reads as something arriving from above rather than the list simply leaving. They tilt, shrink, and are thrown a long way sideways in alternating directions.

They do not fade at all: they fall **clear off the bottom of the panel**. The distance is measured from the list at rest plus a margin, so even the topmost row - which has the whole list below it to fall past - is gone by the end. The fall is squared against the zoom so it accelerates rather than easing out, the way a dropped thing does.

Everything involved is **opaque**. The globe's ocean and the row cards mix their tones against the panel background and return a color with no alpha, rather than painting low-alpha foreground over it. That looks identical at rest and correct in motion: the globe arrives as a solid object in front of the list rather than as a tinted pane the rows show through.

The **stage is not clipped**, because at the start of the flight the globe is still up in the header above it and clipping would cut it in half exactly when it is meant to look like the little circle. The rows are clipped instead, by a separate item, so they slide out of the panel rather than piling up past its edge. The globe is **loaded on hover**, not on click, so reading its two data files never lands in the middle of the animation.

### What it shows

A spinnable orthographic globe: coastlines, a graticule, the day/night terminator, and a major city for every time zone. Drag to spin (it keeps going and eases to a stop), drag vertically to tilt, and tap a city to read its local time in the footer. Tapping the hero globe again returns to the list, and closing the panel returns to it too - the list stays the way in.

City names are drawn **in two tones**: light over the sea, dark over the land. They are painted twice - once light over everything, then again dark through a clip of the continents - so a name straddling a coastline comes out dark on its land half and light on its sea half, and every part of it sits against something it contrasts with. An outline cannot do this; it only fattens the letters and dulls both halves. Tracked and home cities keep their distinction through weight and their dot rings rather than label color.

Names are placed to the left of their dot when placing them to the right would run off the panel, so nothing is truncated at the edge.

On each row's daylight strip the marker is **gold by day and the moon by night** - not a plain pale dot, but tonight's actual phase, with the unlit part bitten out of it. Sun and moon are the same size: they are the same marker in the same place meaning the same thing, so only their content differs. The whole disc is always drawn faintly underneath, so the marker never disappears at new moon.

**Shift-click a moon** to walk it through a full lunation and back - the moon is nearly always somewhere unremarkable, so without this there is no way to see that the marker really is drawing a phase. It runs about five seconds, tweening between eight stops, then drops straight back to the real phase (the tween is disabled for that last step, or it would run the month backwards on the way).

It is one element carrying two facts rather than a new thing on the row, which is the only reason it earns its place. The phase follows the scrubber too, so dragging time walks the moon through its month.

`GlobeModel.moonPhase` is the mean synodic month against a known new moon - enough to draw a phase, not enough to predict an eclipse. It drifts from the true lunation by up to about half a day, which is under 6% of illumination and sub-pixel on a marker this size. `test/shell.d/elsewhen-globe-test.sh` pins it against five eclipses, which are the one thing that fixes a lunation to a wall clock: a solar eclipse can only happen at new moon and a lunar eclipse only at full. The drawn shape is checked by rasterising it and counting lit pixels against the illumination formula.

City dots on the globe use the same rule as the list: gold in daylight, pale at night.

**The city you are in is always on the globe**, always labelled, and drawn the way the panel globe draws it - the dot in the accent color, a dark edge so it does not vanish into the land, and a halo. It is merged in ahead of everything else, so a built-in or a tracked row of the same name cannot shadow it.

**Cities the list is tracking** get an accent ring around the dot, and first claim on a label slot so they are always named. Matching is by city name, not zone - tracking Miami does not light up New York, because they are different cities that happen to share `America/New_York`. A tracked city that is not one of the globe's own built-ins is merged in using the coordinates the weather script already geocoded, so a city in the list can never be missing from the globe.

Dots are thinned in screen space before anything is drawn: candidates are offered in priority order and one is kept only if it clears the others by a minimum distance, so a dense region like western Europe shows a few legible cities instead of a smear of overlapping dots. Tracked cities and the current selection are exempt and always survive. The survivors change as the globe turns or the panel resizes, since the test is in pixels rather than degrees.

Labels are then placed greedily over the survivors with collision avoidance, so names appear and disappear as the globe turns rather than piling up.

**A city's label is part of its click target.** A two-pixel dot is a hard thing to hit, so label boxes are tested first - before dots - because a label sits beside its own dot and would otherwise lose the proximity test to a neighbouring city.

**A moving globe is drawn with less in it.** A full paint measures about 14ms - already over a 120Hz frame at 8.3ms - and every frame of movement repaints the whole canvas, because the projection changes, whether the globe is riding the zoom, being dragged, or coasting after a throw.

Two things dominate that paint: the city names, which cost a layout pass and two passes of text, one of them through a clip built from every coastline ring; and the graticule, 17 stroked polylines. Both are dropped while the globe is in motion and come back the moment it settles, which roughly halves the cost. Nothing is lost that could be read - names on a turning globe are a smear, and mid-zoom the whole thing is a few dozen pixels across.

Below half size the coastline is drawn at half its vertices as well. That one is tied to how big the globe is being drawn rather than to whether it is transitioning, because the zoom's ease-out spends its slow tail near full size, where the missing islands would be visible and would then snap back in.

Measured over the open transition, with `smoothMotion` off and on: average paint 11.6ms to 7ms, and the worst gap between frames 105ms to 45ms. Set `smoothMotion` to `false` to draw everything, always.

**Everything drawn scales with the shell.** Stroke widths and marker radii go through `GlobeModel.scalePx` rather than being pixel literals, because the globe's radius and its labels already follow the shell's base font size, and literal widths would read as proportionally thinner as that size grows. The small globe derives its widths from its own radius, which the large globe cannot do, its radius being hundreds of pixels rather than tens. Widths are floored at one pixel, below which a stroke stops reading as a thin line and starts dropping out of the raster.

Nothing here touches the network at runtime. The coastlines are Natural Earth 110m, simplified with Douglas-Peucker to 68 rings and 1337 points (14 KB), and the cities were geocoded once at build time - both are plain data files in the plugin. Zone offsets come from the same `date` probe the list uses.

`test/shell.d/elsewhen-globe-test.sh` covers the projection and solar maths, including a check of the terminator against Open-Meteo's `is_day` for every city.

### One selection, two views

The list and the globe are two views of the same choice, so they hold it together. Clicking a row and then opening the globe lands on that city rather than resetting to home, and picking a city on the globe moves the list's focus so the header and the small globe are already on it when the globe closes.

Picking a city on the globe also brings it round to face you, as opening the globe does for home and the jump box does for what it finds - a city chosen near the limb would otherwise sit where the projection is most foreshortened. Only a hit turns the globe: a tap on open ocean clears the selection and leaves the view alone.

The pick is `pickAt(x, y)` on the globe's root rather than a body inside the `MouseArea`, so the same code the pointer runs can be driven from a test or over IPC. This desktop cannot inject a pointer at all, and a copy of the logic in a test would be free to drift from the one the mouse actually reaches.

A globe city the list does not track is the ordinary case - the globe draws every zone's main city, the list holds the handful you chose - and it leaves the list where it was. There is no row to focus, and sending the list home would move it somewhere nobody asked to go. Clicking empty ocean is the same story from the other side: it clears the globe's selection, but the globe's "no city" and the list's "home" are different states and forwarding one as the other would be a lie.

The list's own focus is held the same way. `focusKey` is the city's `label|zone` and the row number is derived from it, because `zones` is a binding too - replaced wholesale on a reorder or a removal - so a stored index would silently come to mean a different city. Deriving the index means a reorder carries the focus with the city and removing the focused city drops it back to home.

The crossing is made on `label|zone`, not on an index. The two views index different things - a row is an index into the settings list, the globe's selection is an index into its own catalogue of everything it draws - and that catalogue is a binding, rebuilt whenever the home row, a tracked city's coordinates or a session city lands. A key survives the rebuild. `test/shell.d/elsewhen-model-test.sh` covers the crossing, including the untracked city and the case where both fields have to agree.

### Jumping to a city

The bar at the bottom searches the whole zone catalogue - every IANA city plus the aliases - and turns the globe to whatever is picked, centering it by setting the spin to the city's longitude and `viewLat` to its latitude, taking the short way round.

A city already on the globe is flown to immediately. One that is not is added **for this session only**: the panel geocodes it, and the globe flies there once the coordinates arrive. Nothing is written to `shell.json`, so there is no saved list to delete from, order, or migrate. Want it again, type it again.

Results are drawn over the globe rather than growing the panel, so the globe does not resize under the pointer while a search is being typed.

### Turning it off

Set `globeEnabled` to `false` on the widget's `shell.json` entry. The hero stops being a button and the globe's Loader never activates; nothing else changes.

### The footer under the globe

Two lines: the city with its time, and under it the zone with its offset. Opening the globe selects home, so the footer is never empty under a marker sitting plainly on a city.

A mark sits against the city's name, the same one the rows carry on their strips: a lit dot by day, tonight's moon by night. It is judged by this globe's own daylight, so it agrees with the dot drawn on that same city an inch above it.

It is sized off the name it stands next to rather than set in pixels, and it stands on the same baseline, so it occupies exactly the band the capital does - never above the cap, never below the letters. `tightBoundingRect` on a capital M gives the ink of the glyph; the mark is one pixel under that, which rasterises to the same 14 device pixels, because a circle's antialiased edge reads a pixel wider than a glyph's stem. Any smaller and the moon reads as a bullet point; a crescent needs room to be a crescent.

It is not placed with `anchors.baseline`: inside a Row, anchoring to a sibling whose own position depends on the Row's height is a loop, and QML settles it by dropping the dot onto the line below. A Row leaves `y` alone, so both items start at its top and the dot's underside is placed on the baseline directly - `Text.baselineOffset` is the ascent of its first line, the same number the glyph itself is drawn from.

The mark and the name are their own Row inside the line, so the gap between them can be tighter than the gaps after them - the mark belongs to the name, not to the row of facts.

There is no "daylight" or "night" word after the time: the city markers and the terminator already say it in the picture. The line cannot fit on one row - "Johannesburg Africa/Johannesburg UTC+2 7:50 PM" runs off the end of the panel - so it is two caption lines, which the footer's reserved height already holds.

The parts of that line are anchored to a named `footer` id rather than reached through `parent.parent`, because QML resolves a chain that falls a step short to `undefined` in silence.

## The hero globe

The globe in the header is drawn, not a glyph, by `MiniGlobe.qml`. A glyph cannot spin: rotating a flat image about the vertical axis squashes it to a line and flips it, which reads as a coin. A sphere keeps its circular outline and moves only its surface across it - so the disc is constant and the graticule and coastlines are re-projected as the spin advances, using the same orthographic projection as globe mode and the same `world.json`.

Landmasses are filled rather than outlined, and only rings above a size threshold are drawn: at icon size an outline is a scribble and an island is a speck of dirt on the lens. The rim is stroked last so nothing spills over it.

Both globes fill their continents from the same clipping code in `GlobeModel.js`. Neither strokes a coastline over the fill: the fill's own edge *is* the coastline, and a second pass over every ring is the expensive half. Measured on the large globe, per repaint: outlines only 8.1ms, fill plus outline 13.4ms, **fill alone 9.1ms** - so the filled look costs about 1ms over outlines, against a 16.7ms frame budget.

Filling means labels and city dots cross light land as often as dark ocean, so labels are outlined and every dot carries a dark edge.

Clipping a coastline to the visible hemisphere has to produce **one** polygon per ring. Keeping each visible run and closing it makes self-intersecting shapes whose area jumps whenever a run splits, and that is visible: continents morph and pulse at the limb, worst as the spin slows. Sutherland-Hodgman against the hemisphere keeps the ring whole, and walking the limb between an exit and the next entry (rather than cutting straight across) makes the silhouette continuous. Measured over a full rotation, the worst area change per quarter-degree of spin goes from 356 px^2 (split runs) to 278 (whole ring, chords) to **3.5** (whole ring, limb arcs) on a 2463 px^2 disc. `test/shell.d/elsewhen-globe-test.sh` holds it there.

The globe leans by `GlobeModel.AXIAL_TILT` - 23.44 degrees, the real obliquity, and the same constant the subsolar calculation uses.

It is drawn at full strength and oversized rather than sitting at text weight: as the centerpiece a dimmed thin globe just reads as washed out.

A marker shows the city you are in, in the accent color. It carries a dark edge: the marker can be nearly the same lightness as the filled continents, and without one the dot dissolves into whichever landmass it is sitting on.

**The globe opens on the city you are in.** It flies there as the panel zooms out, so the two motions - growing out of the header and turning round to home - land together rather than one after the other. If your coordinates have not arrived yet, which happens on a cold geocode cache, the request is held and runs the moment they do.

**Clicking a city row turns the globe to it** and marks it - so a tap on Tokyo swings the globe round and drops the marker on Japan. It takes the shortest way round rather than always turning forward: Los Angeles to Tokyo is 102 degrees west, not 258 east.

While the globe is showing somewhere else, clicking the header line brings it home. The whole line is the target, not just the name. Once it is home, the same click asks where here is - see [Where "here" is](#where-here-is) - so the line is never a dead click target. In globe mode it is only live while the globe is away. Reopening the panel also returns it home.

The opening spin **lands on home** - the animation runs from `homeLon - 1080` to `homeLon`, three whole turns that finish with your own meridian facing you. At rest a `Binding` holds the globe there, standing down while the animation is writing the property. Until the weather script has geocoded your city the marker is hidden and it rests on Greenwich.

`Easing.OutQuart` over 1250ms puts most of the rotation in the first third and lets the rest coast out, which is what a globe flicked by hand does rather than a motor driving it at a constant rate.

## Where "here" is

The header reads "It's 10:28 AM here in Los Angeles." rather than a bare "here", which names your own city without spending a row on it. The zone comes from the same `date` probe the rows use - one extra `LOCAL|<zone>` line, from `timedatectl` - so it costs no additional process and follows a time-zone change on the next refresh.

The city name starts as the zone's last segment, and the tz database names zones after a *representative* city: someone in Fort Lauderdale reads "here in New York", gets New York's weather on the first row, and a home pin a thousand miles north.

**Click the header line to say where you are.** It opens a search titled "Where are you?" over every place the city search knows - the zone cities, the aliases, and whatever the geocoder finds. While the list's focus is on another city the first click brings it home, as it always did, and the next one asks. `w` opens the same search from the keyboard.

Picking a place on this machine's own zone moves everything that meant here together. It is stored as `here`, with its coordinates; the header names it; the globe's home pin and the opening spin land on it; and **the row that stood for the old here is renamed in place**, keeping its position, its people, and gaining the new coordinates, so the first row's weather is your weather. The first run's own home row is that row. A row is only renamed into a city the list does not already hold, and no row is added if none stood for here.

**A place on another zone moves the machine's clock there.** Land in Nashville, pick it, and the system time zone becomes `America/Chicago` - the bar clock, every app, and the header along with it. It goes through the same passwordless `sudo timedatectl set-timezone` rule the timezone menu uses (`etc/sudoers.d/omarchy-tzupdate`), with `sudo -n`, so where that rule is missing the change fails instead of waiting on a password prompt nobody can see. Here only moves once the clock has: a refused change leaves the header, the list and the setting as they were, and says so in a notification. Only here waits on the clock - an edit made to the list in the meantime stands. A successful one says where you are and which zone the clock is on.

That move leaves the list alone. The row that stands for home stays where it is, now an hour ahead, because the point of being away is that home is somewhere else; renaming it to Nashville would lose it. Picking home again on the way back moves the clock back.

`here` is remembered with its zone and only counts while the machine is on that zone. If the clock moves some other way - the timezone menu,
```

### docs/file-layout.md
```
# File layout

How `omarchy/` is organized and where everything ends up on an installed
system.

## Mental model

Two Arch packages are built from this one repo (PKGBUILDs live in the
separate `omarchy-pkgs` repository, under `pkgbuilds/`):

- **`omarchy`** — runtime binaries (`bin/`, including `bin/omarchy-dev-*`),
  install/finalize scripts (`install/`), migrations, themes, and the
  Quickshell desktop (`shell/`). Depends on `omarchy-settings`.
- **`omarchy-settings`** — everything that has to be on the target *before*
  the omarchy package installs (specifically before `useradd -m` and the
  limine bootloader install): all `/etc/skel/**`, `/etc/` drop-ins,
  package-owned system files under `/usr/share` and `/usr/lib`, fonts,
  plymouth theme, sddm theme, branding, plus the limine/snapper configs
  (mkinitcpio hooks, limine-entry-tool drop-ins, snapper template, the
  `default/limine/` and `default/snapper/` trees, and the boot/snapshot
  story end-to-end). Also ships the three debug binaries
  (`omarchy-debug`, `omarchy-debug-idle`, `omarchy-upload-log`) needed by
  the live ISO env.

Two other packages live in `omarchy-pkgs` but stand alone:
`omarchy-keyring` (GPG keys for pacman) and `omarchy-nvim` (the Neovim
setup; independently seeds `/etc/skel`).

Some trees ship in neither package and exist only in the repo: `manual/`
(user manual chapters), `agents/skills/` (contributor task guides), `docs/`,
`test/`, and `plans/`.

Three layers populate `$HOME`:

1. **Seed** — `omarchy-settings` ships static defaults to `/etc/skel/`.
   Arch's `useradd -m` copies that tree into a new user's `$HOME` at user
   creation. This is the only mechanism that touches a brand-new user's home
   for these files.
2. **Finalize** — `omarchy-provision-user` (routed as `omarchy finalize
   user`) runs once per user and handles the things `/etc/skel` can't do
   because they need `$HOME` expansion, the live `$OMARCHY_PATH`, or runtime
   detection of system state.
3. **Resync** — `omarchy-reinstall-configs` is the explicit, destructive
   command for an existing user to clobber their configs back to shipped
   defaults.

`/etc/skel` only fires at user creation. Existing users picking up new
defaults must use the resync command.

Deferred-provisioning installs (`omarchy-apply-system --defer-provisioning`)
create no user at all: the ISO leaves `/var/lib/omarchy/provisioning/pending`
behind, which arms `omarchy-provision-owner.service` (shipped from
`install/provisioning/`, alongside the factory-reset finish unit and
`setup-form.sh`). On first boot `bin/omarchy-provision-owner` creates the
user on tty1 and runs the finalize step itself.

On an encrypted install `omarchy-provision-owner` then re-keys LUKS from the staged install key to the owner's password through `install/provisioning/luks-rekey.sh`, which journals each step (phase and slot numbers, never keys) in `/var/lib/omarchy/provisioning/luks-rekey.state` so an interrupted first boot resumes. Setup finishes only once the staged key opens nothing, and removes the journal with `pending`, so a retry after the staged key is retired must use the password the disk holds. On a platform whose boot package owns the boot chain, the check before the owner form, the boot-time unlock and the record of the kept key slot go through `omarchy-lifecycle-dispatch`. See [lifecycle-dispatch.md](lifecycle-dispatch.md).

`omarchy-drive-password` reuses those journal helpers when the owner changes the password of the disk holding `/`: it changes the LUKS key and confirms the new key opens the disk and the old one no longer does. The login and root passwords are left alone. `~/.local/state/omarchy/drive-password.state` records the disk's UUID, the key slots and the phase (never a password) until the change is confirmed and its slot recorded, and the next run finishes an interrupted change with whichever of the old or new password the disk opens with.

Prebuilt images are set up away from the machine they will run on, so their hardware setup waits for that machine. The builder writes a root-owned manifest, `/var/lib/omarchy/image/target` (`format=1`, `platform=<omarchy-hw-platform value>`), before `omarchy-apply-system`. While it exists, `omarchy-apply-hardware` runs no hardware leaf: it queues each one in `/var/lib/omarchy/image/deferred-steps` and arms `omarchy-provision-hardware.service` (shipped from `install/provisioning/`). On the machine's first boot, before owner setup and the login screen, `bin/omarchy-provision-hardware` renames the manifest to `target.booted` and runs the queue in order, dropping each step that succeeds. Before the first step it makes the machine's own pacman keyring when the build asked for one (`/var/lib/omarchy/image/pacman-keyring`, which install finalization writes on aarch64 platforms other than Apple Silicon instead of running `pacman-key --init`, so no two machines share a master key). A failed step stays queued for the next boot. It refreshes no package databases: the image carries its sync databases and every package its queued steps install, so the queue runs offline (the image build checks that it carries them; a step whose package is missing stays queued). Once the queue is empty it rebuilds the initramfs if a step changed its inputs (the mkinitcpio configuration, module options in `/etc/modprobe.d/` and `/usr/lib/modprobe.d/`, or the kernel command line in `/etc/default/limine` and `/etc/limine-entry-tool.d/`) or asked for the rebuild (`/var/lib/omarchy/image/boot-rebuild`), and disables the service; the unit file stays, so a start job already queued is skipped on the emptied queue rather than failed. A platform's own first boot may run `omarchy-provision-hardware` itself: runs are serialised, and it exits 75 when a step or the keyring failed and stays queued, and 1 when it refused to run (an untrusted manifest or queue) or the final rebuild failed, which the next run retries. Steps know they run on an image's first boot from `OMARCHY_IMAGE_DEFERRED_HARDWARE=1` (Bluetooth starts its service there, since boot already brought up its target). `install/helpers/image-target.sh` holds the contract. Root always uses these fixed paths; no environment variable turns a live system into an image build.

Current generated theme state lives under
`~/.local/state/omarchy/current/`. Keep `~/.config/omarchy/` for files a user
may intentionally version in a dotfile manager, such as user themes, hooks,
shell layout, plugins, and themed template overrides.

## Build-time map (repo → installed paths)

```
omarchy/                            built into          installed at
─────────────────────────           ──────────────      ────────────────────────────────────

bin/omarchy-*                  ──►  omarchy             /usr/bin/omarchy-*
                                                        (and symlinks in /usr/share/omarchy/bin/)
bin/omarchy-debug,
bin/omarchy-debug-idle,
bin/omarchy-upload-log         ──►  omarchy-settings    /usr/bin/  (needed before omarchy is installed)

default/libalpm/hooks/*.hook
                                ──►  omarchy             /usr/share/libalpm/hooks/*.hook

install/**                     ──►  omarchy             /usr/share/omarchy/install/
migrations/**                  ──►  omarchy             /usr/share/omarchy/migrations/
themes/**                      ──►  omarchy             /usr/share/omarchy/themes/
shell/**                       ──►  omarchy             /usr/share/omarchy/shell/
version                        ──►  omarchy             /usr/share/omarchy/version
                                                        + /etc/skel/.local/state/omarchy/migrations/*

config/**                      ──►  omarchy-settings    /etc/skel/.config/**         (seeds new users)
                                                        /usr/share/omarchy/config/** (resync source)
etc/fastfetch/config.jsonc     ──►  omarchy-settings    /etc/fastfetch/config.jsonc
etc/xdg/kitty/kitty.conf       ──►  omarchy-settings    /etc/xdg/kitty/kitty.conf
etc/mpv/mpv.conf               ──►  omarchy-settings    /etc/mpv/mpv.conf            (hardware decoding; ~/.config/mpv wins)
etc/xkb/{rules/evdev,symbols/omarchy}
                               ──►  omarchy-settings    /etc/xkb/                    (Shift + Caps Lock compose option)

applications/*.desktop         ──►  omarchy-settings    /etc/skel/.local/share/applications/
                                                        /usr/share/omarchy/applications/
default/applications/*.desktop
                                ──►  omarchy-settings    /usr/share/omarchy/default/applications/
                                                        (optional and legacy launcher templates)
applications/icons/*           ──►  omarchy-settings    /usr/share/icons/hicolor/{48,256,scalable}/apps/

etc/**                         ──►  omarchy-settings    /etc/**           (drop-ins we own outright)
  ├─ mkinitcpio.conf.d/{00-omarchy-hooks,omarchy_hooks,thunderbolt_module}.conf
  ├─ limine-entry-tool.d/{omarchy-defaults,omarchy-uki}.conf
  ├─ mise/conf.d/{omarchy,omarchy-tools,omarchy-agent-accounts}.toml
  ├─ NetworkManager/, sudoers.d/, sysctl.d/, tmpfiles.d/,
  │  profile.d/omarchy.sh, …                            (a summary — `ls etc/` for the full ~17-entry tree)
  └─ security/faillock.conf, nsswitch.conf,
     cups/cups-browsed.conf, plymouth/plymouthd.conf    /usr/share/omarchy/etc-overrides/
                                                          → /etc/* (post_install cp -f, see below)

default/limine/limine.conf     ──►  omarchy-settings    /usr/share/omarchy/default/limine/limine.conf
default/limine/default.conf    ──►  omarchy-settings    /usr/share/omarchy/default/limine/default.conf
                                                        (template; ISO substitutes @@CMDLINE@@ → /etc/default/limine)
default/snapper/root           ──►  omarchy-settings    /etc/snapper/config-templates/omarchy
                                                        (+ /usr/share/omarchy/default/snapper/root)

default/**                     ──►  omarchy-settings    /usr/share/omarchy/default/
  ├─ bash/env-bootstrap                                 /usr/share/omarchy/default/bash/env-bootstrap
  │                                                       (sourced by every shell/session entry point; see "Env bootstrap")
  ├─ bashrc                                             /usr/share/omarchy/etc-overrides/dot.bashrc
  │                                                       → /etc/skel/.bashrc (post_install cp -f)
  ├─ hypr/toggles/*.lua (flags,
  │    single-window-aspect-ratio, window-no-gaps)      /etc/skel/.local/state/omarchy/toggles/hypr/
  ├─ nautilus-python/extensions/*.py                    /etc/skel/.local/share/nautilus-python/extensions/
  ├─ uwsm/env.d/10-omarchy                              /usr/share/uwsm/env.d/
  ├─ environment.d/*.conf                               /usr/lib/environment.d/
  ├─ fontconfig/conf.avail/50-omarchy.conf              /usr/share/fontconfig/conf.avail/
  │                                                       + symlink /etc/fonts/conf.d/50-omarchy.conf
  ├─ xdg-terminal-exec/*.list                           /usr/share/xdg-terminal-exec/
  ├─ applications/mimeapps.list                         /usr/share/applications/mimeapps.list
  ├─ systemd/user/*.service                             /usr/lib/systemd/user/
  ├─ systemd/user/app.slice.d/10-oomd.conf              /usr/lib/systemd/user/app.slice.d/
  ├─ systemd/system-sleep/unmount-fuse                  /usr/lib/systemd/system-sleep/
  ├─ systemd/zram-generator.conf.d/90-omarchy.conf      /usr/lib/systemd/zram-generator.conf.d/
  ├─ fonts/omarchy/omarchy.ttf                          /usr/share/fonts/omarchy/
  ├─ sddm/omarchy/                                      /usr/share/sddm/themes/omarchy/
  ├─ sddm/hyprland.lua                                  /usr/share/sddm/hyprland.lua
  ├─ wayland-sessions/omarchy.desktop                   /usr/local/share/wayland-sessions/
  └─ plymouth/                                          /usr/share/plymouth/themes/omarchy/

logo.{txt,svg}, icon.{txt,png}  ──► omarchy-settings    /usr/share/omarchy/  (resync source)
                                                        /usr/share/pixmaps/omarchy.png
                                                        /usr/share/icons/hicolor/256x256/apps/omarchy.png
                                                        /etc/skel/.config/omarchy/branding/{about,screensaver}.txt
```

The hardware-conditional `force-igpu` and `keyboard-backlight` sources also live under `default/systemd/system-sleep/`, but their setup commands publish root-owned copies only on machines that need them; they are not installed by `omarchy-settings`.

### Platform root

A platform's runtime package (omarchy-mac on Apple Silicon, say) adds its desktop files under a fixed root that only the one installed platform package owns. Omarchy ships nothing there, and a missing root or file means no platform additions. No environment variable moves it; tests reach fixtures through test-only seams, never through a desktop session's environment.

```
/usr/share/omarchy-platform/
  displays.conf                backlight and DDC hints for the display commands (below)
  key-names                    "<keysym> <name>" lines the keybindings menu shows in place of keysyms
  display-cutouts.json         camera cutouts the top bar keeps out of (see omarchy-shell.md)
  keyrings                     signing keyring packages of the repositories the platform adds, one per line
  audio.json                   audio processing nodes the audio panel and microphone widget leave out (below)
  fingerprint-readers          readers the kernel drives without USB, and the file that shows each one is usable (below)
```

See [lifecycle-dispatch.md](lifecycle-dispatch.md#platform-files).

`omarchy-update-keyring` refreshes each installed package `keyrings` names (`#` comments and blank lines skipped, and a line that isn't a `*-keyring` package name skipped with a warning) along with Arch's, before the system upgrade, installing any newer version the repository has, so a key rotation in the platform's own repository never fails that upgrade's signature checks. On Apple Silicon, omarchy-mac names `asahi-alarm-keyring` there.

#### Display hints (`displays.conf`)

`omarchy-hw-display` picks the built-in panel's backlight by name (`gmux_backlight`, then `amdgpu_bl*`, `intel_backlight`, `acpi_video*`, else the first one listed, never a T2 Touch Bar's `appletb_backlight`), and `omarchy-brightness-display` probes every external monitor over DDC. Where a platform's names or display driver differ, its platform package says so in `/usr/share/omarchy-platform/displays.conf`; Omarchy ships none, and without it both behave as above. One directive per line, whitespace-separated; blank lines, whole-line `#` comments, unknown directives, and lines with a wrong word count or a name that is `.`, `..` or has a `/` are ignored:

- `backlight-skip <glob>`: a `/sys/class/backlight` name (a shell glob) that never drives the built-in panel, such as a Touch Bar's. It is never picked, not even when a later directive or the built-in order names it.
- `backlight-prefer <name>`: the built-in panel's backlight, a literal name, tried after `gmux_backlight` and before the GPU and ACPI ones, in file order.
- `ddc-require-connector-ddc`: the display driver registers no DDC channel, so a probe would only walk unrelated I2C buses. An external monitor (other than an Apple Studio or XDR Display, which `omarchy-brightness-display-apple` drives with asdcontrol) is probed only when its DRM connector has a `ddc` node (`/sys/class/drm/card*-<connector>/ddc`); otherwise it gets no DDC or backlight control, and the built-in panel is never dimmed in its place.

No environment variable moves the file: these commands also run under `sudo` and from the brightness keys. Their tests (`test/shell.d/hw-display-test.sh`, `test/shell.d/brightness-display-test.sh`) run a copy rewritten to read a fixture in its place.

#### Fingerprint readers (`fingerprint-readers`)

`omarchy-hw-fingerprint` finds USB readers by their product string or vendor. A reader the kernel drives some other way (a Mac's Touch ID sensor, behind its Secure Enclave) is named by the platform package in `/usr/share/omarchy-platform/fingerprint-readers`; Omarchy ships none. Each line is an absolute path, a shell glob, then the value that file reads once the reader is usable; the reader is present when any file the glob matches reads that value. The value must be the file's whole content, not part of it (Touch ID reads `not-ready` before it reads `ready`). Three details decide a match: the file's trailing newlines are dropped before comparing (sysfs ends every value with one), fields are split on whitespace (so neither the glob nor the value can contain a space), and the file is read as the user running the check, the session user, so it must be readable by that user and not only by root. Blank lines, whole-line `#` comments, relative paths and lines with a missing or extra word are ignored. A platform file never hides a USB reader: when no platform-named file matches, the USB scan still runs. On Apple Silicon, omarchy-mac names `/sys/bus/platform/drivers/apple_sep/*/diag/touchid ready`. That file is `0444 root:root`, so the session user can read it. The line follows the kernel's names for the Secure Enclave driver (`apple_sep`) and its `diag/touchid` attribute: if a kernel renames either, the reader and the first-run invitation quietly stop appearing, so the platform package changes the line along with its kernel.

The rest of the fingerprint path is the same for every reader: the setup's first-run invitation follows `omarchy-hw-fingerprint`, so it reaches a machine once its platform's reader is usable, and `omarchy-setup-security-fingerprint` installs `libfprint-git`. Setup can only enroll a platform's reader once that package carries its driver; for a Mac's Touch ID that is the aarch64 build from omacom/omarchy-pkgs#806. `test/shell.d/hw-fingerprint-test.sh` runs a copy rewritten to read a fixture in place of the file.

#### Audio hints (`audio.json`)

The audio panel lists every output, input and playback stream PipeWire has, and the microphone widget counts every recording as the microphone in use (the shell's own level meters never count). A platform whose audio runs through its own processing (DSP filter graphs in front of raw devices, say) has nodes that are neither devices nor apps, and its platform package names them in `/usr/share/omarchy-platform/audio.json`; Omarchy ships none, and without it nothing is left out.

```json
{
  "hidden": ["<pattern>", "..."],
  "replaced": [{ "node": "<pattern>", "by": "<pattern>" }]
}
```

A pattern is a JavaScript regular expression matched against a whole `node.name`. A `hidden` node is never listed as an output, an input or an app stream, unless it is the current default output or input (so the panel always shows what's in use), and never lights the microphone widget; a `replaced` node is left out only while a node matching `by` exists (a mono processed microphone behind a stereo copy of it, say). Missing or malformed JSON means no hints, and an invalid pattern or entry is skipped. The shell reads the file at that fixed path, which no environment variable moves (`shell/Commons/AudioNodes.qml`), and `test/shell.d/audio-test.sh` covers the parsing.

A virtual source (an `Audio/Source/Virtual`, such as EasyEffects' or a platform's microphone mapping) needs no hint: Quickshell leaves it untyped, so the panel and widget set its volume and mute through `wpctl` (`shell/Commons/UntypedInput.qml`, one `pactl subscribe` for the whole shell), shows no level meter for it (Quickshell's peak monitor takes typed nodes only), and the panel lists it because PulseAudio does (`omarchy-audio-sink-availability sources`).

### Why `etc-overrides/` exists

Some files under `/etc/` (`.bashrc` in `/etc/skel`, `nsswitch.conf`,
`security/faillock.conf`, `cups/cups-browsed.conf`, `plymouth/plymouthd.conf`)
are owned by upstream Arch packages, so we can't install over them via pacman
without a file conflict. Instead their sources (under `etc/` in the repo;
`.bashrc` from `default/bashrc`) ship at
`/usr/share/omarchy/etc-overrides/` and the `omarchy-settings` `post_install`
/ `post_upgrade` scriptlet `cp -f`'s them into place.

Tradeoff: user edits to those files get clobbered on every `omarchy-settings`
upgrade. This is documented in the PKGBUILD.

## Locate indexing

`default/systemd/system/plocate-updatedb.service.d/10-omarchy.conf` ships through `omarchy-settings` to `/usr/lib/systemd/system/plocate-updatedb.service.d/10-omarchy.conf`. It replaces the existing service's `ExecStart` with `updatedb --prune-bind-mounts=no --add-prunepaths=/.snapshots`, keeping Btrfs subvolume mounts searchable and excluding Snapper snapshots. The upstream service retains its timer, resource limits, and sandbox; Omarchy's existing AC-power condition still applies.

`/etc/updatedb.conf` remains owned by plocate and is never rewritten by Omarchy. The command-line options override bind-mount pruning and add to the administrator's existing path exclusions. Installer and AUR package refreshes pass the same options directly because installation may run without systemd and an explicitly requested refresh should work on battery.

Arch's systemd package hook reloads units when the vendor drop-in is installed or upgraded. The settings package containing the drop-in must ship alongside the runtime package that removes the old configuration helper and migration. Pacman removes those retired files; no new state migration is needed. A running indexer finishes with its original options, and subsequent service starts use the drop-in. For an immediate local test after installing the packages, restart `plocate-updatedb.service` while connected to AC power.

## Env bootstrap (`default/bash/env-bootstrap`)

Single source of truth for `OMARCHY_PATH` and dev-link-aware `PATH`. It:

- Sources `/etc/omarchy.conf` (written by `omarchy-dev-link`, reset to the
  package path by `omarchy-dev-unlink`) if present; otherwise forces
  `OMARCHY_PATH=/usr/share/omarchy` so a stale inherited value can't survive
  an `omarchy-dev-unlink`.
- Prepends `$OMARCHY_PATH/bin` to `PATH` **only when** `OMARCHY_PATH` is
  not `/usr/share/omarchy`. On a production install the binaries are
  already on `PATH` as `/usr/bin/omarchy-*` via the `omarchy` package.
- Prepends mise's `command-wrappers/bin` so subscription account dispatch runs before inherited tool binaries, then appends `~/.local/share/mise/shims` and `~/.local/bin` so login shells and the uwsm session find mise-managed tools. The existing mise tool shims also dispatch these wrappers for SSH commands that run no shell setup; the PAM path needs no additional entry. `etc/mise/conf.d/omarchy-agent-accounts.toml` declares the Claude, Codex, and Grok wrappers; `mise reshim` builds them during user setup and migration. Each invocation resolves the selected account through `omarchy-agent-account-exec`, while an explicit provider home takes precedence. Credentials and running sessions remain in their original account homes.

Sourced by every entry point that needs the env set:

```
/etc/profile.d/omarchy.sh                      (system login shells)
/etc/skel/.bashrc                              (interactive shells)
/usr/share/uwsm/env.d/10-omarchy               (Hyprland session via uwsm)
/usr/share/omarchy/default/bash/envs           (SSH / non-login bash)
```

Idempotent — safe to source more than once in the same shell.

`PATH` covers everything the user runs, but not `sudo`, which resolves command
names against `secure_path` from `/etc/sudoers`. So `omarchy-dev-link` also
writes `/etc/sudoers.d/omarchy-dev-path`:

```
Defaults secure_path="<checkout>/bin:/usr/local/sbin:/usr/local/bin:/usr/bin"
```

Without it, `sudo omarchy-*` fails for a command the package has not shipped
yet and silently runs the packaged copy of one it has. The drop-in is validated
with `visudo -c` before install and removed by `omarchy-dev-unlink`; unlike
`/etc/omarchy.conf`, it takes effect without a reboot.

Factory reset is an exception: it always self-elevates through `/usr/bin/omarchy-system-factory-reset` and refuses a checkout copy that differs from the installed command, including when invoked with `sudo`. Install the matching package before resetting so a newer checkout cannot silently hand off to older account-scrubbing code.

## Runtime finalization (`omarchy-provision-user`)

Runs once per user. It does **not** copy `~/.config/**`, `~/.bashrc`,
`flags.lua`, or the nautilus extensions — `/etc/skel` already seeded those.
It only does the things `/etc/skel` can't:

- Skill symlinks into `~/.agents/skills/<name>`, `~/.claude/skills/<name>`, `~/.codex/skills/<name>`, `~/.pi/agent/skills/<name>`, `~/.gemini/config/skills/<name>` (Antigravity), `~/.hermes/skills/<name>`, and each existing `~/.hermes/profiles/*/skills/<name>` → `$OMARCHY_PATH/default/agents/skills/<name>`, looping over every skill directory there (currently `omarchy` and `diagnose-crash`) so new skills need no edit. Symlinks (not copies) so `omarchy dev link` against a dev checkout repoints them correctly. Hermes profile dirs are only linked when they already exist — provision does not create Hermes profiles.
- `xdg-user-dirs-update` (Templates/Public/Desktop folded back into `$HOME`)
  and `~/.config/gtk-3.0/bookmarks` (needs `$HOME` expansion).
- Hyprland's package-owned default input reads `XKBLAYOUT` / `XKBVARIANT`
  from `/etc/vconsole.conf`; no per-user Hyprland config rewrite is needed.
- `xdg-settings set default-web-browser chromium.desktop` and
  `xdg-mime default HEY.desktop x-scheme-handler/mailto` (XDG-aware paths).
- `omarchy-refresh-applications` (composes generated `.desktop` launchers).
- Sources `install/user/all.sh` — theme, chromium, git, xcompose, mise,
  keyring, per-user hardware quirks (asus mic/mixer, framework f13 audio, …).
- On `--first-install`, marks every shipped user migration as already applied
  for the freshly-created user.

Idempotency marker: `~/.local/state/omarchy/done/finalize-user`, managed
by `omarchy-done`.

The ISO calls it as `omarchy-provision-user --force --first-install` in the
target chroot as the install user, after `omarchy-apply-system` has finished
the root-side work. `omarchy-provision-owner` makes the same call (with
`OMARCHY_SETUP_CONTEXT=provision-owner`) when it creates the user during
deferred first-boot provisioning.

## Migrations (`omarchy-migrate`)

See [`migrations.md`](../agents/skills/migrations.md) for the full migration model, authoring
guidelines, and troubleshooting notes.

Omarchy migrations live in `migrations/*.sh` and run per-user through
`omarchy-migrate`. Completion state lives in
`~/.local/state/omarchy/migrations/`, so every user gets a chance to run every
migration. Migrations run as the user; privileged work should invoke the
appropriate helper or privilege prompt. Migrations must be idempotent;
machine-wide repairs should no-op when another user already applied them.

Each graphical user has `omarchy-migrate-notify.service`, started once per login
through `WantedBy=graphical-session.target` and ordered after that target so
notification actions can safely launch through UWSM. The `omarchy-pkgs`
PKGBUILD has shipped `omarchy-update-user-notify.service` as a symlink onto
it, so users enabled under the old unit name keep working before they reach
migration `1785095882`.
It runs `omarchy-migrate-notify` as
that user, which checks `omarchy-migrate --pending`. If this user has missing
migration state, it shows a notification that opens a terminal for
`omarchy-migrate`. The notifier never runs migrations in the background.

Login is the only trigger. Nothing watches the packaged migration directory: a
watcher cannot tell a bypassed `pacman -Syu` from the package transaction inside
a normal `omarchy update`, so it notified about migrations that `omarchy-migrate`
was already applying in the visible update terminal.

`omarchy-migrate` waits for any active pacman transaction to finish, then runs
pending migrations. It does not need `--force`; migrations happen when state
files are missing. `omarchy update` runs `omarchy-migrate` after the package
transaction in the already-visible update terminal, then runs
`omarchy-hook post-update`.

## First-run (`omarchy-provision-first-run`)

Runs once on first interactive login, after the user manager is live. It
first runs `omarchy-provision-user || true` so finalize catches up if it
never ran, then handles the steps that need a running graphical session
and/or a working user systemd instance:

- `omarchy-hook-install post-update` for the two shipped hooks
  (`setup-fingerprint.hook`, `setup-agent.hook`).
- `install/user/first-run/enable-user-units.sh` — daemon-reload, then
  `systemctl --user enable --now` the shipped user units (`bt-agent`,
  `omarchy-sleep-lock`, `omarchy-recover-internal-monitor`,
  `omarchy-migrate-notify.service`, `omarchy-fcitx5.service`,
  `omarchy-crash-watch.service`) so they run in the first session too.
  Done here, not at finalize, because
  the user manager isn't reachable from the ISO chroot; `ConditionPath*`
  in the unit files keeps services inert when they don't apply.
- `omarchy-lifecycle-dispatch setup-user` — the platform's own user setup,
  now with the session up (a no-op where the platform registers none; see
  [lifecycle-dispatch.md](lifecycle-dispatch.md)).
- `install/user/first-run/gnome-theme.sh`,
  `install/user/first-run/gtk-primary-paste.sh` — GNOME/GTK settings that
  need the dconf daemon.
- `install/user/first-run/audio-tuning.sh` — apply speaker tuning.
- `install/user/first-run/welcome.sh` — keybindings toast that greets the
  first login and opens the cheatsheet when clicked. The caller runs
  `omarchy-notification-wait` once before this and the Wi-Fi step, so both
  toasts land on a live notification server.
- `install/user/first-run/wifi.sh` — Wi-Fi/update toasts (waits detached on
  `nm-online` so the update prompt only lands once there is a connection).

The entire sequence has one idempotency marker:
`~/.local/state/omarchy/done/first-run-user`, managed by `omarchy-done`.
Completed users exit before any first-run step. On failure the marker is not
written and the sequence retries next login.

Completion markers live under `~/.local/state/omarchy/done/`. Use
`omarchy-done check <name>` to check one and `omarchy-done mark <name>` to record it.
Use `omarchy-done ensure <name>` as a conditional when the guarded work should
run only once; it records completion before returning success.
The Quattro upgrade completes graphical first-run for upgraded users and moves
the legacy finalization marker from `~/.local/state/omarchy/` into `done/`.

## Root-side install orchestration

`omarchy-apply-system` (root, in chroot) runs target-side setup at ISO
finalization. It sources:

- `install/config/all.sh` — theme links, lockout limits, lockscreen PAM,
  powerprofilesctl shebang fix, SSH command path and keepalive, docker setup,
  Snapper retention, locate index tuning, service enablement, firewall.
- `install/hardware/all.sh` via `omarchy-apply-hardware` — vendor- and
  device-specific kernel modules, udev rules, microcode, wireless regdom,
  ASUS / Framework / Intel / Apple / Lenovo quirks.
- `install/login/all.sh` — SDDM theme/session config.
- `install/post-install/all.sh` — final pacman/udev/localdb passes.

Logging goes to `/var/log/omarchy-install.log` via
`install/helpers/logging.sh`.

Platform-specific setup asks `omarchy-hw-platform`, which prints `x86`, `aarch64`, `aarch64-apple`, `aarch64-qualcomm`, `aarch64-n1x` or `aarch64-gb10` (the naming standard is in AGENTS.md under Platforms). It reads the vendor prefix of each token in the device tree's root `compatible` (`apple,` or `qcom,`, from `/proc/device-tree` or `/sys/firmware/devicetree/base`) and the CPU architecture, and fails when they contradict each other. A Snapdragon laptop's `qcom,` tree is `aarch64-qualcomm`. The NVIDIA N1x boots with ACPI and no device tree; it is `aarch64-n1x` when its MediaTek I2C controllers (ACPI `NVDA0200`) or its GPU (PCI `10de:2e06`) are present, and a device tree naming Apple or Qualcomm alongside them is a contradiction. An NVIDIA GB10 desktop, such as the DGX Spark, also boots with ACPI; it is `aarch64-gb10` when its GPU (PCI `10de:2e12`) is present, with the same contradictions, and an N1x signature alongside it is one too. A manifest written by an older image builder may still say `apple-silicon`, `generic-aarch64`, `generic` or `qualcomm`, which read as `aarch64-apple`, `aarch64`, `x86` and `aarch64-qualcomm`.

An image built away from the machine it will run on names its target in a root-owned manifest, `/var/lib/omarchy/image/target` (`format=1`, `platform=<omarchy-hw-platform value>`, unknown keys ignored). While the root is being built rather than booted, the detector answers from the manifest and never reads the build host's device tree. The root counts as built when it shows it: no `/run/systemd/system`, PID 1's root is another one (a chroot), or PID 1 is not systemd (a PID namespace). A booted system always answers from its hardware, even with a manifest left behind, so no unit that asks the detector may use `PrivatePIDs=`. As root the detector restarts in an empty environment and ignores the fixture variables its tests use.

The package lists the ISO pacstraps live at `install/omarchy-base.packages`
and `install/omarchy-other.packages`; the ISO builder also reads them when
constructing its offline mirror.

A platform's default package set is the base list, then its architecture's additions, then its own: `install/omarchy-aarch64.packages` on every aarch64 platform, then `install/omarchy-<platform>.packages` when that platform has one (`install/omarchy-aarch64-apple.packages` on Apple Silicon, `install/omarchy-aarch64-qualcomm.packages` on Snapdragon, `install/omarchy-aarch64-n1x.packages` on the N1x, `install/omarchy-aarch64-gb10.packages` on the GB10). x86 installs the base list alone. `omarchy-pkg-defaults [platform]` prints the composed set, for the running machine by default (via `omarchy-hw-platform`, so an image build gets its target's set), and `omarchy-reinstall-pkgs` installs it.

## Platform display hints (`/usr/share/omarchy-platform/displays.conf`)

`omarchy-hw-display` picks the built-in panel's backlight by name (`gmux_backlight`, then `amdgpu_bl*`, `intel_backlight`, `acpi_video*`, else the first one listed, never a T2 Touch Bar's `appletb_backlight`), and `omarchy-brightness-display` probes every external monitor over DDC. Where a platform's names or display driver differ, its platform package says so in `/usr/share/omarchy-platform/displays.conf`; Omarchy ships none, and without it both behave as above. One directive per line, whitespace-separated; blank lines, whole-line `#` comments, unknown directives, and lines with a wrong word count or a name that is `.`, `..` or has a `/` are ignored:

- `backlight-skip <glob>`: a `/sys/class/backlight` name (a shell glob) that never drives the built-in panel, such as a Touch Bar's. It is never picked, not even when a later directive or the built-in order names it.
- `backlight-prefer <name>`: the built-in panel's backlight, a literal name, tried after `gmux_backlight` and before the GPU and ACPI ones, in file order.
- `ddc-require-connector-ddc`: the display driver registers no DDC channel, so a probe would only walk unrelated I2C buses. An external monitor (other than an Apple Studio or XDR Display, which `omarchy-brightness-display-apple` drives with asdcontrol) is probed only when its DRM connector has a `ddc` node (`/sys/class/drm/card*-<connector>/ddc`); otherwise it gets no DDC or backlight control, and the built-in panel is never dimmed in its place.

No environment variable moves the file: these commands also run under `sudo` and from the brightness keys. Their tests (`test/shell.d/hw-display-test.sh`, `test/shell.d/brightness-display-test.sh`) run a copy rewritten to read a fixture in its place.

## Explicit resync (`omarchy-reinstall-configs`)

When an existing user wants to reset to shipped defaults:

```
~/  ←  cp -af /etc/skel/.
```

Replaying `/etc/skel` over `$HOME` is exactly what `useradd -m` does for a
brand-new user, so this one copy resyncs `.bashrc`, `.config/**`,
`.local/share/applications/`, the nautilus-python extensions, hypr toggles,
branding files, and the shipped migration markers in a single pass.

Then it runs `omarchy-refresh-limine`, `omarchy-refresh-plymouth`, and the
nvim refresh. Destructive: existing user files copied from `/etc/skel` are
clobbered without backup. Fastfetch is package-owned at
`/etc/fastfetch/config.jsonc`; delete `~/.config/fastfetch/config.jsonc` to
return to the packaged default.

## Quick reference: where does X live?

| Goal | Touch |
| --- | --- |
| Default file at `~/.config/foo/` | `config/foo/` |
| `/etc/` drop-in we own outright | `etc/` |
| `/etc/` file owned by an upstream package | `etc/` (see `etc/security/faillock.conf`), then add to `etc-overrides` in `omarchy-settings` PKGBUILD + scriptlet |
| Package-owned system file (e.g. systemd user service in `/usr/lib`) | `default/`, then add the `install -Dm644` line in `omarchy-settings` PKGBUILD |
| Per-user file that's static but lives outside `~/.config` | `default/`, then add `install -Dm644 ... $pkgdir/etc/skel/...` in `omarchy-settings` PKGBUILD |
| Runtime tweak that needs `$HOME` or live system state | extend `omarchy-provision-user`, or add a per-user leaf under `install/user/` and wire into `install/user/all.sh` |
| One-time root-side setup step | `install/config/*.sh` or `install/hardware/*.sh`, wire into `install/config/all.sh` or `install/hardware/all.sh` |
| One-time fix for existing installs | `migrations/<unix-timestamp>.sh` |
| Package-owned path something else may already write | Prefer a path nothing else writes, such as a vendor drop-in under `/usr/lib`. Otherwise the `--overwrite` entry in `bin/omarchy-update-system-pkgs` has to ship a release before the file |
| User-facing `omarchy-*` command | `bin/omarchy-<group>-<verb>` — see `GROUP_DESCRIPTIONS` in `bin/omarchy` |
| New stock theme | `themes/<name>/` (+ matching templates under `default/themed/` if they need theme colors) |
| User-installed theme | `~/.config/omarchy/themes/<name>/` |
| Generated current theme/background state | `~/.local/state/omarchy/current/` |

## Kitty defaults and user overrides

Kitty loads `/etc/xdg/kitty/kitty.conf` before `~/.config/kitty/kitty.conf`. The `omarchy-settings` package owns the system file; the user template contains only the active theme include and commented examples for personal overrides. Keeping the theme include in the user file lets users remove it without changing the packaged defaults. Individual inherited keybindings can be unmapped with an empty `map <shortcut>` directive, or all inherited bindings can be cleared with `clear_all_shortcuts yes`.

The system default uses `allow_remote_control socket-only` so Omarchy can query the active terminal directory over its Unix socket while Kitty rejects remote-control requests arriving through terminal output. Changing this setting requires restarting Kitty. The migration refreshes the exact previous stock config with a backup; customized configs retain their settings and ordering, with only explicit unrestricted `yes`, `y`, or `true` remote-control settings commented out.
```

### docs/i18n.md
```
# Omarchy in 50 languages

Omarchy ships in the same 50 languages as omarchy.org: English plus 49 translations, chosen under **Setup > Language** in the menu. English is the default and the fallback for every string a translation has not covered yet. Picking a language translates the Omarchy menu, the Quickshell desktop, and Omarchy's own notifications, and sets the session's `LANG` to match, so other applications follow as they are opened: `LANG` goes to `~/.config/uwsm/env.d/50-omarchy-language`, which uwsm exports at every login, and into the running session. `uwsm app` runs an app in a scope, which keeps the environment of whatever launched it (Hyprland for bindings, the shell for the launcher), so the running session takes it in two steps: `hl.env("LANG", …, true)` sets it in Hyprland and passes it on to the systemd and D-Bus activation environments services start from, and the shell is then restarted from Hyprland to inherit it. Apps already open keep the language they started with until restarted, and the system locale in `/etc/locale.conf` (the console, the login screen) is left alone. A `LANG` the user sets in a later uwsm env file, or an `LC_ALL`, `LC_MESSAGES` or `LANGUAGE` they export, still takes precedence. The Omarchy interface re-renders live from the language file, so the shell restart is only there to hand the new `LANG` to the apps it launches. Japanese, Korean, and Chinese also bring their input method and CJK glyph forms, unless the user already has an input method or chose the forms (see `docs/input-methods.md`).

## Where things live

- `default/i18n/locales.json` — the 50-language registry: code, native name, English name, BCP 47 format locale, glibc locale, and text direction where it is not left-to-right. The roster mirrors `src/i18n/locales.json` on the omarchy-site `fifty-languages` branch (56 site editions collapse to 50 languages because the regional English editions share English text).
- `default/i18n/en/menu.json`, `shell.json`, `cli.json` — the English source catalogs. Every other language mirrors their keys exactly in `default/i18n/<code>/`.
- `manual/*.md` — the English manual. Translations live in `manual/<code>/` under the same file names.
- `~/.config/omarchy/language` — the user's choice, one registry code. A missing or unknown code means English.
- `bin/omarchy-language` — shows or sets the language and the session's `LANG`. With no argument it prints the current code; `list` prints the picker rows; `omarchy language da` switches. Only generating a locale that isn't generated yet needs root, as one elevated script with a single password prompt: `sudo` in a terminal, `pkexec` when picked from the menu. Switching between generated locales prompts for nothing. The choice is persisted only after that succeeds, so a cancelled prompt leaves everything as it was.
- `default/i18n/<code>/keybindings.json` — the descriptions in the keybindings menu (Super+K), keyed by their English text. The English catalog is generated from the bind calls in `default/hypr/bindings/*.lua` by `scripts/i18n-sync.py` (a description built with `..` becomes a `%1` pattern such as `Switch to workspace %1`), and `omarchy-menu-keybindings` swaps each row's description for the current language's as it shows the menu, after ordering the rows in English. A description a user wrote shows as written.
- `bin/omarchy-i18n` — prints one `cli.json` string in the current language: `omarchy-i18n battery.lowBody 12`. Catalog entries carry `%1`-style tokens, substituted from the extra arguments, so translations may reorder them freely.
- `shell/Commons/I18n.qml` — the shell singleton. QML reads `I18n.t("common.search")` (or `Commons.I18n.t(...)` with a qualified import), with `.arg(...)` filling `%1` holes. It layers the current language's `shell.json` over the English one and re-renders live when the language file changes. It also exposes `formatLocale` from the registry. Shell code that prints day or month names formats with `Qt.locale(I18n.formatLocale)` rather than `Qt.formatDate` or a bare `Qt.locale()`, which follow the `LANG` the shell inherited rather than the language file. Qt's `MMMM` is the genitive month (right in "14 октября", wrong in a heading), so a month on its own uses `standaloneMonthName`, and date patterns that vary by language (`clock.dayMonthFormat`, `clock.monthYear`) live in the catalog.
- `shell/plugins/menu/MenuModel.js` — `applyTranslations` retitles the shipped menu rows from `menu.json` before the user's menu extension merges on top, so user rows and retitles always win. The English label moves into the row's search-only terms, which keeps English search working in every language without making English words routable menu commands. The injected root row ("Go") has no JSONC entry, so its label comes from the catalog's `root` entry.
- `test/shell.d/i18n-test.sh` — holds the whole arrangement honest: registry shape, English menu catalog freshness against `omarchy-menu.jsonc`, exact key and placeholder parity for all 49 languages, every catalog key referenced and every referenced key present, complete per-language manuals, and `omarchy-language` / `omarchy-i18n` behavior against stubbed locale files.

## Adding or changing a string

English changes first, translations follow. For a menu label, edit `default/omarchy/omarchy-menu.jsonc` and mirror the change in `default/i18n/en/menu.json` (the test fails until they agree). For a shell string, add the key to `default/i18n/en/shell.json` and read it with `I18n.t(...)`; plain-JS models take an optional `tr(key, english)` argument defaulting to the English text, which the Node tests assert. For a notification or other user-facing CLI string, add the key to `default/i18n/en/cli.json` and print it with `omarchy-i18n`. Terminal output, usage text, and diagnostics stay English, as does the developer gallery; plugin manifest names and descriptions are not translated yet.

A few habits keep a translated string correct. Keep each sentence whole in one key with `%1`-style placeholders, never glued from translated pieces, since other languages reorder words; where English branches on a count, use a `…One` key for exactly one beside the general key. Translate at the point of display: a value that is stored, compared, or answered over IPC stays English, and a line that must keep an English literal carries an `// i18n: ignore` comment so the extractor passes it. Keep `I18n.t()` inside bindings so a language switch re-renders it; text assembled once when something happens keeps the old language until rebuilt. A QML `Text` whose text becomes an `I18n.t()` binding needs an explicit `textFormat` (`qml-text-format-test.sh`). Day and month names come from `Qt.locale(I18n.formatLocale)` (`standaloneMonthName` for a month on its own), never `Qt.formatDate` or a bare `Qt.locale()`; in `bin/`, run `date` with `LC_TIME="$(omarchy-language locale)"`. Date patterns that vary by language, like `clock.dayMonthFormat`, live in the catalog as Qt patterns.

Third-party shell plugins ship their own catalogs and read them through `Commons.Translations` (`shell/Commons/Translations.qml`), and Omarchy-style apps follow the language with a small JSON-backed `QTranslator`; the `omarchy` skill's `plugins.md` and the `omarchy-app` skill describe both for the agents that build them.

Until a translation catches up, the missing key simply renders in English. The site keeps its manual in English for now (`manual: false` in its registry); the translated manuals in this repo are ahead of it and can be picked up there later.

## Keeping translations in sync

Individual pull requests only ever add the English side: the string in code plus its English catalog entry (or the English manual chapter). The `i18n-check` workflow validates structure on pull requests — catalogs well-formed, placeholders intact, English menu catalog fresh, and no user-facing English literals embedded directly in `bin/` or `shell/` — but deliberately does not require translations. The extractor flags any QML property whose name ends like display text (`text`, `tooltipText`, `activeTooltipText`, `leftLabel`, `placeholderText`, …), every literal on such a line, and bare string-list items such as hero phrases; in `bin/`, literals on `omarchy-notification-send` and menu prompt lines. A handful of intentional literals (brand names and fixed phrases) live in `default/i18n/extract-allowlist.json`; for one line rather than one string everywhere, use the `// i18n: ignore` marker.

The `Sync translations` workflow does the converging, modeled on omarchy-site's translate workflow. It runs on pushes to `quattro` that touch English sources, daily, and on demand. `scripts/i18n-sync.py` computes what is pending from `default/i18n/translation-manifest.json`, which records the hash of the English source every catalog key and manual chapter was translated from; a unit is pending when its translation is missing or its English changed since. The workflow first extracts any English that was embedded directly in code — on a credential-less runner that only produces a patch, which another credential-less job applies and validates (the checks load the extracted code, so nothing there may hold a token), and a trusted job path-checks and publishes without running any repository code — then runs one credential-less Muse runner per pending language, collects and validates their patches under per-language path allowlists without credentials, updates the manifest, and lands everything through a final trusted job, again only git and gh, as a single pull request from the `i18n-sync` branch with auto-merge enabled, so it merges itself once `i18n-check` passes. The one exception: when extraction changed executable code under `bin/` or `shell/`, auto-merge is turned off, even if an earlier run enabled it, and the pull request waits for a human review. Failed languages simply stay pending and are retried on the next run; English is never blocked. The same script works locally: `python3 scripts/i18n-sync.py pending` shows the queue and `translate --locale da` fills one language.

Repository settings this needs: the `MUSE_API_KEY` Actions secret (optional `MUSE_MODEL` variable), an `I18N_SYNC_TOKEN` secret holding a fine-grained PAT with contents and pull-requests write on this repository (pull requests created with the default `GITHUB_TOKEN` do not trigger workflow runs, so their required check would never report; without the PAT the sync pull request still opens but needs a human nudge), "Allow auto-merge" enabled, and `i18n-check` as a required status check on `quattro` so auto-merge actually waits for validation.

## Translator brief

Translate like the interface was written in your language: short, natural, and in the register of consumer desktop software. Menu labels are one or two words where the language allows it. Keep the following exactly as they are: product and brand names (Omarchy, Hyprland, Neovim, Chromium, application names, agent names, font names), technical tokens (DNS, DHCP, AUR, TUI, VM, QR, GPU, SSH, PATH), commands, file paths, URLs, keyboard key names (Super, Alt, Ctrl, Home, F9), and placeholders (`%1`, `%2`, … in both catalogs) — a translation must carry the same placeholders as its English source, though it may reorder them. Clock-format preview labels translate the weekday and month words only; times and digits stay. ALL-CAPS section headers stay capitalized where that is natural for the script. In the manual, preserve Markdown structure, headings, links, code blocks, commands, and file names verbatim, translate link text and prose, and keep the author's voice — the manual is opinionated on purpose.

Regional notes: `pt` is European Portuguese as written in Portugal (`estar a fazer`, `equipa`, `ecrã`, `ficheiro`, `utilizador`); `pt-BR` is Brazilian Portuguese. `es-MX` is Mexican Spanish. `zh-CN` is Simplified Chinese and `zh-TW` Traditional Chinese in Taiwan usage. `no` is Norwegian Bokmål. `sr` is Serbian in Cyrillic. The stock `noto-fonts` and `noto-fonts-cjk` packages already cover every script in the roster, so no language needs extra fonts.

A plural entry is an object of CLDR categories rather than a string: English writes `{"one": "%1 device", "other": "%1 devices"}`, and each translation supplies exactly the categories its language's counts reach — Russian `one`, `few`, `many`, `other`; Arabic all six; Japanese only `other` — always keeping every placeholder in `other`, and dropping the count from a form only where the language says the number with a word.

## Plurals, numbers, and direction

Plural rules live twice, in `shell/Commons/Plural.js` for the shell and `default/i18n/plural.jq` for `omarchy-i18n`, and `i18n-test.sh` checks the two agree for every language. The sync script asks `plural.jq` which categories a language needs, so translations come back complete. In QML, `I18n.tn("key", count)` picks the form (`.arg()` still fills the holes); in bash, `omarchy-i18n --count "$n" key "$n"`; a plain-JS model takes an optional `tn` the way it takes `tr`. A string that only abbreviates a unit (`%1h`, `%1 min`) is not a plural.

Numbers follow the language too: the registry's `decimal` and `zeroDigit` (taken from Qt, so they match the dates it writes) give Danish `13,1` and Persian `۱۳٫۵`. Shell code formats displayed numbers with `I18n.formatNumber(value, decimals)` (`shell/Commons/Numbers.js`), never `toFixed` or `toLocaleString`; `omarchy-i18n` localizes any argument that is a plain number, so commands pass numbers as their own arguments with the unit in the catalog string, and `omarchy-i18n --number` writes one number for text outside a catalog. Numbers are not grouped, so a year or a port never grows a separator.

Arabic, Hebrew, Persian, and Urdu are marked `"direction": "rtl"` in the registry, and `I18n.rightToLeft` mirrors every panel, menu, notification, and dialog with Qt's `LayoutMirroring` (set in `KeyboardPanel`, `PopupCard`, `OverlayWindow`, and the standalone windows); the bar keeps the sections the user arranged. Anchors, rows, layouts, and text alignment flip on their own. Anything placed by explicit `x` arithmetic follows `LayoutMirroring.enabled` itself, as `PanelSlider` does; glyphs that mean back or forward swap with `I18n.rightToLeft`; and Left/Right key handling goes through `Util.readingKey(event)`, so Left moves forward along a right-to-left row.
```



### CLAUDE.md
```
@AGENTS.md
```

### AGENTS.md
```
# Task Guides

Deeper instructions for specific kinds of work live in `agents/skills/`. Read the
matching guide before starting:

- [`agents/skills/command-metadata.md`](agents/skills/command-metadata.md) - adding or changing commands in `bin/`
- [`agents/skills/install-scripts.md`](agents/skills/install-scripts.md) - working under `install/` or on system/user setup commands
- [`agents/skills/mise-tools.md`](agents/skills/mise-tools.md) - adding or changing mise-managed tools
- [`agents/skills/shell-dev.md`](agents/skills/shell-dev.md) - editing the Quickshell desktop under `shell/`
- [`agents/skills/icon-font.md`](agents/skills/icon-font.md) - adding branded glyphs to `default/fonts/omarchy/omarchy.ttf`
- [`agents/skills/acceptance-tests.md`](agents/skills/acceptance-tests.md) - writing or running graphical acceptance tests under `test/acceptance.d/`
- [`agents/skills/visual-verification.md`](agents/skills/visual-verification.md) - verifying any change with a visual effect in the running UI
- [`agents/skills/migrations.md`](agents/skills/migrations.md) - creating or changing migrations under `migrations/`

# Documentation Layout

Three documentation trees, split by genre and audience:

- `agents/skills/` - task procedure ("do this when doing X"), for anyone working on the codebase
- `docs/` - reference on how the system is shaped (file layout, update pipeline, theming, shell architecture), for anyone working on the codebase; skills link here for depth
- `manual/` - end-user documentation for using Omarchy, published; never codebase internals

# Style

- In markdown documents (`plans/`, `docs/`, `manual/`), write full lines — no hard wrapping at 80 columns; break only at structural boundaries like headings and list items
- Two spaces for indentation, no tabs
- Use bash 5 conditionals: use `[[ ]]` for string/file tests and `(( ))` for numeric tests
- In `[[ ]]`, don't quote variables, but do quote string literals when comparing values (e.g., `[[ $branch == "dev" ]]`)
- Prefer `(( ))` over numeric operators inside `[[ ]]` (e.g., `(( count < 50 ))`, not `[[ $count -lt 50 ]]`)
- Prefer a full `if`/`else` conditional for simple two-path control flow; don't rely on `exec` or `exit` in one branch to make following statements unreachable
- For strings/paths with spaces, quote them instead of escaping spaces with `\ ` (e.g., `"$APP_DIR/Disk Usage.desktop"`, not `$APP_DIR/Disk\ Usage.desktop`)
- Shebangs must use `#!/bin/bash` consistently (never `#!/usr/bin/env bash`). A security-sensitive entrypoint may use the exact `#!/bin/bash -p` form only when it must suppress `BASH_ENV` and exported-function startup injection before its first command; that exception must be explained at the boundary and covered by a regression that rejects an ordinary Bash launch with a decoy `-p` argument.
- Scripts under `install/` and `migrations/` may be sourced and intentionally omit shebangs

# Command Naming

All commands start with `omarchy-`. Prefixes indicate purpose.

The authoritative list of user-facing command groups lives in `bin/omarchy` in `GROUP_DESCRIPTIONS`. Keep `GROUP_DESCRIPTIONS` updated when adding a new command prefix users are meant to browse to.

A group whose commands are all `# omarchy:hidden=true` gets no entry. That table drives the top-level group listing on its own, so an entry there advertises the group even when every command in it is hidden. `apply-` and `provision-` are deliberately absent for that reason; both still route, and `omarchy <group>` still prints a group header without one.

Common prefixes include:

- `cmd-` - check if commands exist, misc utility commands
- `capture-` - screenshots, screen recordings, and other capture tools
- `pkg-` - package management helpers
- `hw-` - hardware detection (return exit codes for use in conditionals)
- `refresh-` - copy default config to user's `~/.config/`
- `restart-` - restart a component
- `launch-` - open applications
- `install-` - install optional software
- `setup-` - interactive setup wizards
- `toggle-` - toggle features on/off
- `theme-` - theme management
- `update-` - update components

Do not maintain a second exhaustive prefix list here. Consult
`GROUP_DESCRIPTIONS` when selecting or checking a command group so this
guidance does not drift from the router.

# Runtime Environment

- `$OMARCHY_PATH` is set at the top level by the uwsm session environment and is always available to Omarchy runtime code.
- Commands in `bin/` and Quickshell QML should rely on `$OMARCHY_PATH` / `Quickshell.env("OMARCHY_PATH")`; do not derive fallback paths from `HOME`, `Quickshell.shellDir`, or re-export/default `OMARCHY_PATH` manually.

# Platforms

Omarchy runs on x86 and aarch64 (ARM). A platform name is the CPU architecture, then a hardware family only when that family needs handling of its own:

- `x86` - every x86_64 machine
- `aarch64` - every ARM machine without a family of its own (Raspberry Pis and ARM VMs today)
- `aarch64-apple` - Apple Silicon Macs
- `aarch64-qualcomm` - Snapdragon laptops
- `aarch64-n1x` - NVIDIA N1x laptops
- `aarch64-gb10` - NVIDIA GB10 desktops (DGX Spark, ASUS Ascent GX10)

A new family is named `aarch64-<family>` (e.g. `aarch64-qualcomm`, `aarch64-n1x`) and is added only once it needs code of its own, so `aarch64*` always means ARM. `omarchy-hw-platform` prints the most specific name. Use these exact names wherever a platform is named: package lists, pacman template directories, image manifests, dispatch registration, tests and docs. Never introduce `generic`, `arm64`, `apple-silicon` or other spellings; the old `apple-silicon`, `generic-aarch64` and `generic` are read only for compatibility with older image builders.

Ask a helper; don't read `uname -m` or the device tree in feature code:

- `omarchy-hw-x86` / `omarchy-hw-aarch64` - the CPU architecture. Use them for binary and ABI availability: a package with no aarch64 build, an x86 guest VM, multilib.
- `omarchy-hw-aarch64-apple`, `omarchy-hw-aarch64-qualcomm`, `omarchy-hw-aarch64-n1x`, `omarchy-hw-aarch64-gb10` (one per family) - built on `omarchy-hw-platform`, image-build aware. Use them for hardware behaviour that the whole family shares; a single model's quirks stay behind `omarchy-hw-match` on its DMI name, or behind `omarchy-hw-match-device-tree` on its device-tree compatible string where models share a DMI name. `omarchy-hw-apple-silicon` and `omarchy-hw-n1x` are hidden aliases kept for the omarchy-mac packages and older N1x images; don't use them in new code.

Where platform code lives:

- Packages: `install/omarchy-base.packages` for everyone, `install/omarchy-aarch64.packages` for every ARM machine, `install/omarchy-<platform>.packages` for one family, and base packages with no aarch64 build in `install/omarchy-x86_64-only.packages`. `omarchy-pkg-defaults` composes them.
- Pacman templates: `default/pacman/` for x86, `default/pacman/<platform>/` for each ARM platform.
- Hardware setup: `install/hardware/<vendor-or-family>/`, gated by a predicate. `install/hardware/apple/` holds Intel Mac quirks; Apple Silicon's own setup ships in the omarchy-mac packages.
- Boot chains Omarchy can't drive generically: a platform package behind `omarchy-lifecycle-dispatch` ([`docs/lifecycle-dispatch.md`](docs/lifecycle-dispatch.md)). Platforms that boot Limine with UKIs like x86 keep the generic path.

The experience should be the same on every platform. When a package or feature is missing or broken on one, the default is to get it fixed upstream (an aarch64 build, a bug report, a patch to the maintainer) and leave the gap visible meanwhile, not to paper over it. When asked for a platform workaround, say so and propose the upstream fix first. Hiding a menu entry or skipping a package is fine only for things that can't exist there (an x86 guest VM, an x86-only proprietary binary). Alternative packages and platform-only replacements are a last resort, used only when upstream can't or won't fix it, with the reason written next to the code.

# Privileged Commands

- Follow the "Privilege Escalation" section of `default/agents/skills/omarchy/SKILL.md`. It draws the
  `sudo`/`pkexec` line by whether the caller has a terminal to enter a password in, and the repo's
  own scripts follow it.

# Git

- Commits should be atomic: include only one coherent change or fix, and do not mix unrelated work.
- Commit messages should be succinct and describe the change being made.

# Helper Commands

Use these instead of raw shell commands:

- `omarchy-cmd-missing` / `omarchy-cmd-present` - check for commands
- `omarchy-pkg-missing` / `omarchy-pkg-present` - check for packages (don't use these if you can just use `omarchy-pkg-add`/`omarchy-pkg-drop`)
- `omarchy-pkg-add` - install packages from the configured pacman repos, Omarchy's included; use `omarchy-pkg-aur-add` for AUR packages
- `omarchy-pkg-drop` - remove packages; use this instead of raw `pacman -R*`
- `omarchy-notification-send` - send desktop notifications; do not call `notify-send` directly
- `omarchy-hw-asus-rog` - detect ASUS ROG hardware (and similar `hw-*` commands)

Commands installed by Omarchy's default package set are runtime invariants. Invoke them directly; do not add defensive `omarchy-cmd-present` / `omarchy-cmd-missing` checks around them. Use command-presence helpers only for genuinely optional dependencies or code that can run before the default package set is installed.

Exceptions are allowed for migration and package-helper scripts where the helper may not be available yet, where the helper itself is being implemented, or where direct package-manager behavior is required.

# Background Work

- Long-running code (the shell, daemons, watchers) reacts to events instead of polling with a timer. Polling is the last resort, for state with no change signal; [`agents/skills/shell-dev.md`](agents/skills/shell-dev.md) lists the event sources and the push-refresh pattern.
- `test/shell.d/shell-idle-spawn-test.sh` fails when an idle shell starts any process, and other tests hold the router, menu guards and theme switch to budgets; see "Performance guards" in [`docs/testing.md`](docs/testing.md).

# Menu

- The menu definition lives in `default/omarchy/omarchy-menu.jsonc`;
  [`docs/menu.md`](docs/menu.md) covers the schema, guards, and providers.
- Do not add `aliases` to new menu entries. Aliases are reserved for
  established alternate names users already type, kept for compatibility.

# Config Structure

- `config/` - default configs copied to `~/.config/`
- `default/themed/*.tpl` - templates with `{{ variable }}` placeholders for theme colors
- `themes/*/colors.toml` - theme color definitions (accent, background, foreground, red/green/yellow/blue/magenta/cyan and bright_* variants)

# Tests

Run focused automated tests for the area you changed;
[`docs/testing.md`](docs/testing.md) covers how the suites are shaped. Current
test entry points:

- `./test/all` - aggregate runner for CLI and shell tests; it intentionally does not run graphical acceptance tests
- `./test/cli` - CLI routing, command metadata, theme helpers, and safe dispatch coverage
- `./test/shell` - all Omarchy shell tests under `test/shell.d/`

New Omarchy shell tests should live in `test/shell.d/*-test.sh` so `./test/shell` picks them up automatically. Source `test/shell.d/base-test.sh` for shared root-path discovery, assertions, and Node test helpers.

The graphical acceptance suite runs in a disposable VM, not in the active
development session; see [`agents/skills/acceptance-tests.md`](agents/skills/acceptance-tests.md).

Visual changes must be verified in the running UI in addition to automated
tests; follow [`agents/skills/visual-verification.md`](agents/skills/visual-verification.md).

# Refresh Pattern

To copy a default config to user config with automatic backup:

```bash
omarchy-refresh-config hypr/hyprland.lua
```

This copies `$OMARCHY_PATH/config/hypr/hyprland.lua` to `~/.config/hypr/hyprland.lua`. The argument
is interpolated into both paths and only checked with `[[ -e ]]`, so pass a plain relative path: a
name containing `..` resolves and copies, landing outside `~/.config` rather than being rejected.
```


## Top-level structure
```
file	.editorconfig	.editorconfig
dir	.github	.github
file	.gitignore	.gitignore
dir	.greptile	.greptile
file	.luarc.json	.luarc.json
file	AGENTS.md	AGENTS.md
file	CLAUDE.md	CLAUDE.md
file	LICENSE	LICENSE
file	README.md	README.md
dir	agents	agents
dir	applications	applications
dir	bin	bin
dir	config	config
dir	default	default
dir	docs	docs
dir	etc	etc
file	icon.png	icon.png
file	icon.txt	icon.txt
dir	install	install
file	logo.svg	logo.svg
file	logo.txt	logo.txt
dir	manual	manual
dir	migrations	migrations
dir	plans	plans
dir	scripts	scripts
dir	shell	shell
dir	test	test
dir	themes	themes
file	version	version
```
