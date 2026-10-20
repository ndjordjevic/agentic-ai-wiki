# Kevin-Liu-01/Claude-of-Tanks

## Metadata
- Stars: 489
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://cot.kevinliu.studio
- Pushed: 2026-10-20T06:56:16Z
- Fetched: 2026-10-20
- Final URL: https://github.com/Kevin-Liu-01/Claude-of-Tanks

## Description
A World of Tanks-style armored combat simulator built directly with Three.js and Vite: 220 vehicles, 33 destructible battlefields, and 13 modes, with plate-level armor, ballistics, modules, spotting, and physics. Play in your browser on desktop or mobile. Built end-to-end by a multi-agent Claude/Codex pipeline.

## README
<p align="center">
  <a href="https://cot.kevinliu.studio">
    <img src="public/brand/og-image.png" alt="Claude of Tanks armored battle with the crest badge and wordmark">
  </a>
</p>

<h1 align="center">CLAUDE OF TANKS</h1>

<p align="center">
<!-- product-summary:start -->
A World of Tanks-style armored combat simulator built directly with Three.js and Vite: 220 vehicles, 33 destructible battlefields, and 13 modes, with plate-level armor, ballistics, modules, spotting, and physics. Play in your browser on desktop or mobile. Built end-to-end by a multi-agent Claude/Codex pipeline.
<!-- product-summary:end -->
</p>

<table width="100%" align="center">
<tr>
<td width="20%" align="center" valign="middle" bgcolor="#05080b"><a href="https://cot.kevinliu.studio/"><img src="public/brand/features/play.svg" height="58" alt="Play armored combat"><br><strong>PLAY</strong></a></td>
<td width="20%" align="center" valign="middle" bgcolor="#05080b"><a href="https://cot.kevinliu.studio/docs"><img src="public/brand/nav/docs.svg" height="58" alt="Open the armored vehicle field manual"><br><strong>FIELD MANUAL</strong></a></td>
<td width="20%" align="center" valign="middle" bgcolor="#05080b"><a href="https://cot.kevinliu.studio/gallery"><img src="public/brand/nav/tank-gallery.svg" height="58" alt="Open Tank Gallery"><br><strong>TANK GALLERY</strong></a></td>
<td width="20%" align="center" valign="middle" bgcolor="#05080b"><a href="https://cot.kevinliu.studio/studio"><img src="public/brand/nav/studio.svg" height="58" alt="Open Scene Studio"><br><strong>SCENE STUDIO</strong></a></td>
<td width="20%" align="center" valign="middle" bgcolor="#05080b"><a href="docs/INDEX.md"><img src="public/brand/features/modules.svg" height="58" alt="Open the engineering documentation"><br><strong>ENGINEERING DOCS</strong></a></td>
</tr>
</table>

<table>
<tr>
<td width="50%"><img src="public/media/site50-r14/stills/s07-lake-shellfire.webp" alt="A Stridsvagn 122 crosses the frozen lake through shellfire"></td>
<td width="50%"><img src="public/media/site50-r14/stills/s23-village-crossroads.webp" alt="A T-80U Husarz and a PL-01 hold the village crossroads"></td>
</tr>
<tr>
<td width="50%"><img src="public/media/site50-r14/stills/s39-lakeside-village.webp" alt="A Chieftain Mk 10 fires across the village at Highland Reservoir"></td>
<td width="50%"><img src="public/media/site50-r14/stills/s20-road-return-fire.webp" alt="A Challenger 2 leads a Ukrainian column returning fire across the fields at sunset"></td>
</tr>
</table>

These are deterministic scenes staged in Scene Studio and rendered at 4K in the game engine—not concept art. The
[visual archive](public/media/site50-r14/archive.json) holds the fifty frames and the key moment and close portrait of each of
the site's takes. The [landing selection](public/media/landing-r1/manifest.json) records the 12 hero frames, the 22
screenshots of the rail, the feature reel, the four camera-path loops, the destruction loop, the 12 versus stills, the
3 trailers, the 24-shot mosaic and the Scene Studio loop published on the site.

## Fight, inspect, and direct

<p>
  <img src="public/brand/features/live-combat.svg" width="52" alt="Live tank combat icon" title="Fight">
  <img src="public/brand/features/armor.svg" width="52" alt="Armor inspection icon" title="Inspect">
  <img src="public/brand/nav/studio.svg" width="72" alt="Scene Studio icon" title="Direct">
</p>

- **Fight:** enter Standard Battle, Capture the Flag, Zone Control, armed low-gravity Turbo Ball, Gravity Mode, cooperative
  Endless Horde, the six-operation Frontline Assault campaign, Juggernaut, Infected, Realistic, Gun Game, Drone, or AC-130 in solo or multiplayer, with physical shell travel, armor geometry, component damage, spotting,
  terrain, collision, destructible structures, persistent wrecks, mode-specific respawns, and authority-owned results.
- **Inspect:** open any vehicle in Tank Gallery, articulate the live rig, isolate armor or internal anatomy, and export an
  exact-surface review packet from the same specification used in combat.
- **Direct:** stage any roster vehicle on any battlefield in Scene Studio, animate actors and cameras, schedule game FX,
  and capture stills or video from reproducible scene data.

## Current release

| | Current runtime |
| --- | --- |
| Fleet | **220** first-party procedural vehicles in production and local development; **0** GLB-sourced playables |
| Worlds | **33** authored battlefields with shared structures, wrecks, utility networks, loose props, placement, collision, and destruction |
| Authority | Fixed **60 Hz** movement, ballistics, armor, damage, spotting, bots, destructibles, and result |
| Presentation | Direct Three.js/WebGL renderer with a measured **120 FPS** test path, adaptive quality, stable shadows, SMAA/FSR, and GPU recovery |
| Play | **13 battle modes**, solo bots, browser-hosted private rooms, LAN rooms, room chat, spectators, respawns, and rematches |
| Platforms | Mouse/keyboard and complete touch controls with safe-area layout and device-adaptive rendering |
| Languages | English and Simplified Chinese across the game, Garage, Studio, Gallery, and public docs; local reviewed catalogs managed with General Translation |
| Tools | Scene Studio, Tank Gallery, exact-surface review, deterministic capture, vehicle anatomy, and release gates |

Language selection lives under **Settings → Language → Language**. See the
[localization guide](docs/LOCALIZATION.md) for coverage, intentional exclusions,
the General Translation workflow, and release gates.

The provenance gate currently reports **220 first-party procedural battle playables and 0 GLB-sourced playables**. Comparison inputs are never a playable loading path and are stripped from public builds.

## Field footage

<p>
  <img src="public/brand/features/screenshots.svg" width="52" alt="In-engine battle screenshot icon" title="In-engine footage">
  <img src="public/brand/features/camera-paths.svg" width="52" alt="Camera path icon" title="Camera rails">
</p>

Each frame below opens a looping WebM recorded from the game. The camera rails use live vehicles, maps, ballistics,
recoil, impacts, sparks, smoke, debris, and destruction effects.

<table>
<tr>
<td width="50%"><a href="public/media/site50-r14/loops/s05-barn-advance.webm"><img src="public/media/site50-r14/loops/s05-barn-advance.jpg" alt="Open the T-14 Armata past the barns take"></a><br><sub><b>T-14 Armata past the barns:</b> A T-14 Armata advances past the barns of Verdant Fields.</sub></td>
<td width="50%"><a href="public/media/site50-r14/loops/s07-lake-shellfire.webm"><img src="public/media/site50-r14/loops/s07-lake-shellfire.jpg" alt="Open the Strv 122 on the frozen lake take"></a><br><sub><b>Strv 122 on the frozen lake:</b> A Stridsvagn 122 crosses the frozen lake through shellfire.</sub></td>
</tr>
<tr>
<td width="50%"><a href="public/media/site50-r14/loops/s18-street-knockout.webm"><img src="public/media/site50-r14/loops/s18-street-knockout.jpg" alt="Open the T-90A knocked out at night take"></a><br><sub><b>T-90A knocked out at night:</b> A T-90A is knocked out at the end of a Steinburg street at night.</sub></td>
<td width="50%"><a href="public/media/site50-r14/loops/s26-minaret-fire.webm"><img src="public/media/site50-r14/loops/s26-minaret-fire.jpg" alt="Open the Merkava Mk 3D fires take"></a><br><sub><b>Merkava Mk 3D fires:</b> A Merkava Mk 3D fires at Sunscar Oasis.</sub></td>
</tr>
</table>

<p align="center">
  <a href="https://cot.kevinliu.studio/home"><strong>OPEN THE FULL LANDING SHOWCASE</strong></a>
</p>

## Vehicle-specific mechanics

<p>
  <img src="public/brand/features/vehicle.svg" width="52" alt="Procedural vehicle icon" title="Vehicle-specific systems">
  <img src="public/brand/features/missile.svg" width="52" alt="Guided missile icon" title="Guided weapons">
  <img src="public/brand/features/modules.svg" width="52" alt="Internal tank modules icon" title="Internal anatomy and autoloaders">
</p>

The fleet does not reduce every vehicle to the same gun and movement model. Specifications can add their own loading,
guidance, suspension, ammunition, anatomy, and control behavior while remaining inside the fixed-step authority.

<table>
<tr>
<td width="50%"><img src="public/media/feature-evidence-r2/mechanic-strv-suspension.webp" alt="Stridsvagn 103 using hydropneumatic suspension to aim on a slope"><br><sub><b>Swedish siege suspension:</b> the Strv 103A, Strv 103B, and UDES 03 aim their fixed guns by pitching the physical hull. Wheels and both loaded track runs reshape around the solved pose.</sub></td>
<td width="50%"><img src="public/media/feature-evidence-r2/mechanic-mbt70-missile.webp" alt="MBT-70 firing a guided Shillelagh missile"><br><sub><b>Guided weapons:</b> the MBT-70 fires the Shillelagh as its primary round. IFVs carry vehicle-specific TOW, MILAN, Spike, Konkurs, Arkan, and Jyu-MAT launchers.</sub></td>
</tr>
<tr>
<td width="50%"><img src="public/media/showcase-r2/13_gallery_modules.webp" alt="Leclerc SXXI internal modules and crew shown in the current Tank Gallery"><br><sub><b>Internal anatomy:</b> the Gallery shows crew, gun, turret ring, engine, fuel, ammunition, tracks, optics, radio, and vehicle-specific feed or missile systems.</sub></td>
<td width="50%"><img src="public/media/showcase-r2/01_garage_verdant.webp" alt="Current Claude of Tanks Garage displaying a K2 in Verdant Motor Pool"><br><sub><b>One shared fleet:</b> battle, garage, Gallery, Studio, bots, icons, diagrams, and technical dossiers read the same vehicle specifications—220 in production and local development.</sub></td>
</tr>
</table>

- **Magazine autoloaders** track ready rounds, intra-magazine cycle time, full replenishment, manual magazine reloads,
  shell changes, and damage to the loading mechanism. The Leclerc, Type 90, PL-01, and four-round PL-01 105 each carry
  their own magazine timings.
- **Guided missiles** travel at visible weapon-specific speeds and steer toward the authority-owned aim point. Launcher
  damage, rack damage, ammunition count, reload state, guidance, impact, and presentation all remain synchronized.
- **Hydropneumatic aim** uses the same canonical pose for armor, muzzle, collision, wheels, tracks, remote snapshots, and
  the camera; there is no separate visual-only tank tilt.
- **Free look** keeps the sight and turret on target while the camera moves. Hold `Shift` on keyboard, `RB` on a standard
  controller, or assign another binding in settings.

## Combat systems

<p>
  <img src="public/brand/features/live-combat.svg" width="52" alt="Live combat icon" title="Physical combat">
  <img src="public/brand/features/armor.svg" width="52" alt="Armor inspection icon" title="Plate-level armor">
  <img src="public/brand/features/modules.svg" width="52" alt="Internal modules icon" title="Internal damage">
</p>

<table>
<tr>
<td width="50%"><img src="public/media/showcase-r2/17_live_player_hud.webp" alt="Current production battle HUD during live armored combat in a K2"><br><sub><b>Battle HUD:</b> dual reticle, ammunition, modules, teams, minimap, chat, performance, and authority-owned combat feedback.</sub></td>
<td width="50%"><img src="public/media/showcase-r2/25_live_killcam_xray.webp" alt="Current X-ray killcam showing the resolved shell path through armor and modules"><br><sub><b>X-ray killcam:</b> the resolved shell path, struck plate, effective protection, penetration result, damaged modules, and crew.</sub></td>
</tr>
<tr>
<td width="50%"><img src="public/media/presentation-r1/ui_combat_firing.webp" alt="Tank firing with current muzzle flash and recoil"><br><sub><b>Physical gunnery:</b> finite world aim, bore convergence, resolved muzzle transform, visible recoil, dispersion, travel time, and gravity.</sub></td>
<td width="50%"><img src="public/media/site50-r14/stills/s29-fjord-road-kill.webp" alt="A T-90 burns on the road above the fjord"><br><sub><b>Destruction:</b> fire, sparks, smoke, detached remnants, persistent wreck state, and pooled effects driven by the completed hit.</sub></td>
</tr>
</table>

- **Plate-level armor** resolves the actual plate, slope, impact angle, normalization, ricochet, overmatch, spaced armor,
  composites, ERA, and separate kinetic/chemical protection.
- **Five ammunition families** model muzzle velocity, gravity, penetration loss, ricochet, and damage differently.
- **Internal anatomy** tracks crew, ammunition racks, engine, fuel, gun, turret ring, optics, radio, and tracks.
- **Tank-specific mobility** combines drivetrain, terrain resistance, per-wheel support, suspension-damped hull attitude,
  flexible terrain-following tracks, collision, ramming, and crushable cover.
- **Real battlefield knowledge** combines view range, concealment, movement/firing bloom, foliage, radio sharing, and the
  15 m bush rule. Multiplayer authority filters hidden enemies before serializing a snapshot.

## Worlds and vehicle design

<p>
  <img src="public/brand/features/battlefield.svg" width="52" alt="Battlefield icon" title="Authored battlefields">
  <img src="public/brand/features/vehicle.svg" width="52" alt="Procedural tank icon" title="First-party procedural vehicles">
  <img src="public/brand/nav/tank-gallery.svg" width="72" alt="Tank Gallery icon" title="Tank Gallery">
</p>

<table>
<tr>
<td width="50%"><img src="public/media/site50-r14/stills/s26-minaret-fire.webp" alt="A Merkava Mk 3D fires at Sunscar Oasis"><br><sub><b>Thirty worlds:</b> terrain, roads, structures, foliage, fog, sky, lighting, cover, collision, minimap, and dedicated-server descriptors.</sub></td>
<td width="50%"><img src="public/media/site50-r14/stills/s19-roof-tiles.webp" alt="Roof tiles rain down as a PL-01 fires up the street"><br><sub><b>Shared world kit:</b> destructible buildings, camps, wreck families, debris, utility lines, loose physical props, and narrow hitboxes.</sub></td>
</tr>
<tr>
<td width="50%"><img src="public/media/showcase-r2/11_gallery_hero.webp" alt="Current Tank Gallery showing a T-90M Proryv and technical dossier"><br><sub><b>Tank Gallery:</b> search 220 production vehicles, orbit and articulate the current vehicle rig, inspect armor, modules, and crew, and export exact-surface review packets.</sub></td>
<td width="50%"><img src="public/media/presentation-r1/ui_tank_closeup_modern.webp" alt="Close inspection of a first-party procedural modern tank"><br><sub><b>Shared vehicle specification:</b> geometry, armor, modules, gun limits, ammunition, mobility, garage cards, bots, icons, diagrams, Gallery, and Studio.</sub></td>
</tr>
</table>

Every playable hull, turret, gun, fitting, suspension, road wheel, and track run is assembled by the repository's
first-party vehicle pipeline. Vehicle changes pass combat-anatomy receipts, generated technical diagrams, geometry
checks, visual fingerprints, and a targeted release gate.

### Ten Garage environments

<p align="center">
  <a href="public/media/showcase-r2/process/review-01.webp"><img src="public/media/showcase-r2/process/review-01.webp" alt="All ten Claude of Tanks Garage environments shown with a varied non-Abrams fleet and the current Garage interface"></a>
</p>

The Garage is its own authored presentation system. Verdant retains the enclosed Motor Pool; the other nine locations
use lightweight scene packs derived from a real battlefield's terrain, structures, PBR materials, detailed trees,
approach route, horizon, sky, and atmosphere without loading that battlefield. One immutable hero pose keeps the tank
and camera comparable across the complete set, while connected maintenance stations, heavy-lift equipment, real fleet
exhibits, and full-detail tank parts establish a distinct service story around every platform.

The release gate reviews every location from four orbit angles and responsive layouts, rejects unsupported or floating
parts, certifies geometry-derived structure collision, and requires a score of at least 90/100 with bounded draw calls,
triangles, transitions, cache residency, and repeated-cycle memory. See the
[Garage environments guide](docs/GARAGE-ENVIRONMENTS.md) for the complete visual, lifecycle, and verification contract.

## Renderer, drivers, and performance

<p>
  <img src="public/brand/features/gpu.svg" width="52" alt="GPU renderer icon" title="GPU-aware renderer">
</p>

The renderer treats quality as a device contract instead of a single desktop preset. It selects a GPU/driver-aware
profile, caps pixel density, prewarms shader paths, adapts costly effects, and can recover from a black frame or WebGL
context loss. The current presentation path combines:

- four quality-scaled, stable texel-anchored shadow cascades with articulation-aware tank shadow hulls;
- fused output grading, anti-aliasing, adaptive render scale, fog/atmosphere, and bounded transparent depth work;
- instance/batch paths for repeated world objects, pooled particles, and explicit GPU resource disposal;
- reusable hot-loop scratch state, fixed-step simulation, render interpolation, and high-refresh presentation;
- an in-game diagnostics surface for FPS, ping, frame timing, draw calls, triangles, memory, network telemetry, quality,
  and renderer/driver identity.

The renderer reached **120 FPS on the certified test hardware**. Actual performance depends on refresh rate, browser,
thermal limits, GPU and driver, resolution, and quality level. Combat rules remain fixed at 60 Hz at every render rate.

<table>
<tr>
<td width="50%"><img src="public/media/showcase-r2/19_live_sniper.webp" alt="Current Leclerc XLR precision sight rendered through the production post-processing path"><br><sub><b>Presentation:</b> high-resolution scope, stable shadowing, post AA, bounded depth copies, and readable combat overlays.</sub></td>
<td width="50%"><img src="public/maps/foundry.webp" alt="Ironworks battlefield overview rendered by the current game"><br><sub><b>World rendering:</b> authored layouts and detailed environments use adaptive quality, instancing, culling, and streaming.</sub></td>
</tr>
</table>

## Multiplayer

<p>
  <img src="public/brand/features/multiplayer.svg" width="52" alt="Multiplayer tanks icon" title="Authoritative multiplayer">
</p>

LAN and private rooms run their match in the host commander's browser over WebRTC and use the shared renderer-free movement and combat rules. No database or dedicated game server is required; Internet rooms meet through a small rooms Worker (seats, signaling, host migration), and restricted networks may need TURN relay. See [Multiplayer v2](docs/MULTIPLAYER-V2.md).
Clients send intent, never trusted hits or damage. Snapshot filtering, local prediction/reconciliation, bounded remote
interpolation, reliable fire edges, reconnectable room state, and separate control/chat delivery keep a moving and firing
7v7 battle responsive without giving the client authority.

<p align="center">
  <img src="public/media/multiplayer-r1/dual-perspective.webp" alt="Side-by-side live browser multiplayer screens showing an M1A1 Abrams HC and a T-90AM facing each other from opposing player perspectives">
</p>
<p align="center"><sub><b>Two screens, opposing sights:</b> paired live 1v1 captures preserve the real battle HUD, authoritative simulation, filtered snapshots, and each commander's view.</sub></p>

### Controls at a glance

| Action | Keyboard and mouse | Standard controller |
| --- | --- | --- |
| Drive and steer | `WASD` or arrow keys | Left stick |
| Aim and fire | Mouse + `LMB` | Right stick + `RT` |
| Precision sight | Hold `RMB` by default; wheel in also enters | `LT` |
| Free look without moving the turret | Hold `Shift` or `Left Alt` | `RB` |
| Select ammunition | `1` / `2` / `3` | D-pad |
| Vehicle-specific action | `E` | `LB` |
| Reload a partial magazine | `C` | Remappable |
| Consumables | `4` / `5` / `6` | Remappable |
| Handbrake | `Space` | `A` |
| Shot log / performance / menu | `L` / `F8` / `Esc` | Interface controls |

Every desktop action is remappable. `RMB` can use hold-to-aim, toggle-aim, or classic free-look behavior. Touch devices
receive dedicated movement, aim, scope, fire, ammunition, equipment, and special-action controls rather than a scaled
desktop HUD.

## Production tools

For procedural vehicle creation, use the [tank-generation handbook](docs/tank-generation/README.md):
source-file and Gallery-markup intake, measured geometry and negative space,
independent review gates, reusable agent briefs, and handoff templates.

<p>
  <img src="public/brand/nav/studio.svg" width="72" alt="Scene Studio icon" title="Scene Studio">
  <img src="public/brand/features/camera-paths.svg" width="52" alt="Camera path icon" title="Camera direction">
  <img src="public/brand/features/screenshots.svg" width="52" alt="Capture icon" title="Deterministic capture">
</p>

<table>
<tr>
<td width="50%"><img src="public/media/showcase-r2/15_studio_workspace.webp" alt="Current Scene Studio composing a multi-tank action shot"><br><sub><b>Scene Studio:</b> place any roster vehicle on any map, conform it to terrain, set its pose within physical limits, schedule game effects on a deterministic timeline, and capture the current renderer.</sub></td>
<td width="50%"><a href="public/media/landing-r1/studio-leclerc-knockout.mp4"><img src="public/media/landing-r1/studio-leclerc-knockout.jpg" alt="Open the Scene Studio film of a Strv 122 firing on and destroying a Leclerc"></a><br><sub><b>Directed destruction:</b> this 1080p timeline moves both actors, fires the Strv 122, resolves impacts, detaches the Leclerc track, and triggers its ammunition-rack blast.</sub></td>
</tr>
</table>

Scene Studio works with the runtime rather than a separate cinematic renderer. Vehicles, camouflage, camera, lighting,
recoil, tracers, explosions, sparks, smoke, debris, wreck state, and timeline events remain scene data. A saved scene can
be replayed, scrubbed, edited, exported as JSON, captured as a high-resolution still, or recorded as a video.

Regenerate the current public archive:

```bash
npm run shots:battle:generate
npm run shots:battle:grade -- --root shots/marketing-battles-r3
npm run studio:action:render
npm run showcase:publish
npm run showcase:check
npm run landing:media:publish
```

The capture harness serializes concurrent jobs, starts a clean local game, verifies the requested state, and records
current rendering diagnostics. `public/media/site50-r14/archive.json` is the source archive (the fifty frames and every take's two stills);
`public/media/landing-r1/manifest.json` records the public hero, rail, mosaic, and Studio selections with their actor,
effect, duration, dimensions, and byte receipts.

The same run is reviewed in contact sheets before any frame becomes a 4K master. These collection views make weak
silhouettes, obstructed cameras, repeated compositions, and overpowered effects obvious before automated grading.

<table>
<tr>
<td width="50%"><a href="public/media/site50-r14/frames/sheet-1.webp"><img src="public/media/site50-r14/frames/sheet-1.webp" alt="Contact sheet 1 of the fifty frames, frames 1 through 10"></a><br><sub><b>Review sheet 1:</b> ten of the fifty frames, each a 4K render of a moving scene with its motion blur.</sub></td>
<td width="50%"><a href="public/media/site50-r14/frames/sheet-2.webp"><img src="public/media/site50-r14/frames/sheet-2.webp" alt="Contact sheet 2 of the fifty frames, frames 11 through 20"></a><br><sub><b>Review sheet 2:</b> the next ten, as the manual shows them beside the battle takes.</sub></td>
</tr>
</table>

The manual shows all five sheets; [docs/SHOWCASE-LIBRARY.md](docs/SHOWCASE-LIBRARY.md) records the library and how it is built.

## Selected field frames

The landing page publishes a larger responsive mosaic. This smaller wall samples the site fifty's key moments and close portraits
without repeating the hero's frames.

<table>
<tr>
<td width="25%"><img src="public/media/site50-r14/stills/s05-barn-advance.webp" alt="A T-14 Armata advances past the barns of Verdant Fields"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s20-road-return-fire.webp" alt="A Challenger 2 leads a Ukrainian column returning fire across the fields at sunset"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s21-fields-assault.webp" alt="A T-90SM wedge assaults through the burning fields"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s27-caravanserai-kill.webp" alt="A T-62MV-1 is knocked out by the caravanserai"></td>
</tr>
<tr>
<td width="25%"><img src="public/media/site50-r14/stills/s34-furnace-salvo.webp" alt="TOS-1A launchers fire a rippling salvo in the Ironworks yard at night"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s06-farm-charge.webp" alt="A KF51 Panther charges past the farmhouse through artillery"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s23-village-crossroads.webp" alt="A T-80U Husarz and a PL-01 hold the village crossroads"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s24-ice-duel.webp" alt="A duel on the frozen lake: a T-80U takes the hit"></td>
</tr>
<tr>
<td width="25%"><img src="public/media/site50-r14/stills/s33-water-tower-close.webp" alt="The line advances past the burning water tower at night"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s38-church-knockout-close.webp" alt="A Leopard 2A6 is knocked out beside the onion-domed church at night"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s18-street-knockout-close.webp" alt="A T-90A is knocked out at the end of a Steinburg street at night"></td>
<td width="25%"><img src="public/media/site50-r14/stills/s19-roof-tiles-close.webp" alt="Roof tiles rain down as a PL-01 fires up the street"></td>
</tr>
</table>

[Browse the full archive](public/media/site50-r14/archive.json),
[open the public Tank Gallery](https://cot.kevinliu.studio/gallery), or
[build a new shot in Scene Studio](https://cot.kevinliu.studio/studio).

## Architecture

```text
controls ──► deterministic authority ──► filtered state + reliable events ──► presentation
                 │                                                           │
                 ├─ movement / terrain / collision                            ├─ procedural vehicles
                 ├─ aim / ballistics / armor / anatomy                        ├─ tracks / suspension / FX
                 ├─ spotting / concealment / bots                             ├─ HUD / audio / killcam
                 └─ destructibles / match result                              └─ Three.js / post / Studio
```

```text
src/engine/    renderer, camera, lighting, post, quality, telemetry, GPU recovery
src/world/     thirty-one maps, terrain, vegetation, props, collision, destruction
src/vehicles/  specs, procedural geometry, materials, profiles, asset verification
src/sim/       DOM-free movement, aiming, ballistics, armor, damage, spotting
src/game/      local composition, bots, input, profile, killcam, Scene Studio
src/mp/        rooms, the wire, transports, the match client, the browser host, sessions
src/ui/        garage, battle HUD, reports, settings, diagnostics, touch controls
server/        the match actor, the LAN room helper, collision manifests, ICE, telemetry
```

Start with [Technical overview](docs/TECHNICAL-OVERVIEW.md), [Product features](docs/FEATURES.md),
[How it works](docs/HOW-IT-WORKS.md), [Multiplayer v2](docs/MULTIPLAYER-V2.md),
[Performance](docs/PERFORMANCE.md), [Scene Studio](docs/STUDIO.md), and [Tank Gallery](docs/GALLERY.md).

## Develop and verify

```bash
npm install
npx vite
npm test
npm run test:net:v2:p2p
npm run tank:native:check
npm run build
npm run build:private
```

The public build strips quarantined comparison assets. Simulation, networking, browser multiplayer, maps, collision,
destruction, rendering policy, UI, mobile controls, vehicle provenance, anatomy, generated assets, and both build variants
have executable checks.

## Deploying

Production (`cot.kevinliu.studio`) is deployed **once per round, by hand**, never per commit. Git
auto-deploys are disabled in `vercel.json` for every branch, so pushing never builds on
Vercel; the release path is the prebuilt CLI deploy documented in [`docs/DEPLOYS.md`](docs/DEPLOYS.md)
(`vercel pull --yes --environment=production` → `vercel build --prod` → `vercel deploy --prebuilt --prod`),
run after the release gate is green. There is no CI deploy.

## Credits and licensing

**Kevin B. Liu** created, designed, and directed the project. Claude and Codex assisted with research, vehicle authoring,
simulation, networking, design, performance, quality assurance, documentation, and deployment. They are development
tools, not co-authors or copyright holders.

All gameplay code and every selectable procedural vehicle model are original first-party work by Kevin B. Liu. The
repository is MIT-licensed by default, with procedural vehicle and battlefield source, fleet and map data, generated game
assets, capture recipes, authored media, and first-party branding expressly excluded as proprietary Reserved Content.
Earlier public revisions remain available under the MIT terms under which they were released. See [`LICENSE`](LICENSE), [`LICENSE-POLICY.md`](LICENSE-POLICY.md),
[`NOTICE.md`](NOTICE.md), and [`docs/ATTRIBUTION.md`](docs/ATTRIBUTION.md) before reusing any file. External models may be
retained only as quarantined research references; they are never loaded as playable geometry.

## Docs
### docs/ listing
```
file	ARCHITECTURE.md
file	ASSET-PROVENANCE.md
file	ATTRIBUTION.md
file	AUDIO.md
file	AUTUMN-LEAF-SPRAYS.md
file	BATTLE-UI-QA.md
file	BATTLE-WEATHER-AND-DAMAGE.md
file	BIRCH-CROWN-FORM.md
file	BOT-TACTICS.md
file	BUILD-STANDARD.md
file	BUILDING-DETAIL.md
file	CAMOUFLAGE-ART-PASS-2026-09-24.md
file	CLEANUP-2026-09-22.md
file	CLEANUP-2026-09-23-structure.md
file	DECISIONS.md
file	DECORATIONS.md
file	DEPLOYS.md
file	DESIGN.md
file	DESTRUCTION.md
file	DEV-PERF-TRACE.md
file	DEVELOPMENT.md
file	ENTRY-RESILIENCE.md
file	ENVIRONMENT-PASS.md
file	ENVIRONMENT-RECOVERY.md
file	FEATURES.md
file	FLEET-FREEZE-CURRENT.json
file	FOUNDRY-SERVICE-COURT.md
file	GALLERY.md
file	GAME-MODES.md
file	GARAGE-ENVIRONMENTS.md
file	GEOMETRY-GATE.md
file	GROUND-MATERIAL-OWNERSHIP.md
file	GUNNERY-CAMERA-SPEC.md
file	HORIZON-ENVELOPE.md
file	HORIZON-FOCUSED-CAPTURE.md
file	HOW-IT-WORKS.md
file	INDEX.md
file	JEV-COMMANDER.md
file	LESSONS.md
file	LOCALIZATION.md
file	MAP-BEAUTIFICATION.md
file	MAP-LAYOUT-BRIEF.md
file	MAP-RENDER-FOUNDATIONS.md
file	MARKETING-BATTLE-CAMPAIGN.md
file	MEDIA-PRODUCTION-CAMPAIGNS.md
file	MEDIA-PRODUCTION.md
file	MODULES.md
file	MULTIPLAYER-V2.md
file	PERFORMANCE.md
file	POSTMORTEM-RUNNING-GEAR-REGRESSION-2026-08-13.md
file	REGIONAL-LANDFORM-PASS.md
file	REGIONAL-MAP-IDENTITIES.md
file	REPOSITORY-LAYOUT.md
file	ROAD-SETTLEMENT-REVIEW.md
file	SCREENSHOT_CONTRACT.md
file	SHADOW-CLOUD-REVIEW-20260929.md
file	SHALLOW-WATER-CONTACT.md
file	SHORELINE-REGRESSION-RECONCILIATION.md
file	SHOWCASE-LIBRARY.md
file	STUDIO.md
file	SYSTEMS.md
file	TANK-ASSET-PIPELINE.md
file	TECHNICAL-OVERVIEW.md
file	VEHICLE-CONTROLS.md
file	VEHICLE-FIELD-UPGRADES-2026-10-07.md
file	VEHICLE-ROSTER.md
file	WOT-ENVIRONMENT-REFERENCE.md
dir	audio-generation
dir	balance
dir	geometry-gate
dir	history
dir	licenses
dir	performance
dir	qa
dir	references
dir	tank-generation
```

### docs/ARCHITECTURE.md
```
# ARCHITECTURE.md — original implementation contract

> Historical document. This was the locked nine-module plan used during the
> original parallel implementation. It is retained as build provenance, but it
> is not the current runtime architecture. Use [SYSTEMS.md](SYSTEMS.md) for
> current ownership and data flow, [MULTIPLAYER-V2.md](MULTIPLAYER-V2.md)
> for network behavior, and [DEVELOPMENT.md](DEVELOPMENT.md) for verification.

Nine builder agents implement the modules below **in parallel, without talking to each
other**. This document is the ONLY shared truth. If something here conflicts with a
research doc, THIS FILE WINS. If something is not specified here or in the research
docs, pick the simplest option that satisfies the interface — never invent a new
cross-module dependency.

Module ownership (file paths are FIXED):

| Builder | Files |
|---|---|
| engine   | `src/engine/renderer.ts`, `src/engine/lighting.ts`, `src/engine/post.ts`, `src/engine/sky.ts`, `src/engine/cameraRig.ts` |
| world    | `src/world/terrain.ts`, `src/world/vegetation.ts`, `src/world/props.ts`, `src/world/map.ts` |
| vehicles | `src/vehicles/specs.ts`, `src/vehicles/fleetFactory.ts`, `src/vehicles/factoryGeometry.ts`, `src/vehicles/tankFactoryCore.ts`, `src/vehicles/materials.ts` |
| movement | `src/sim/movement.ts` |
| combat   | `src/sim/ballistics.ts`, `src/sim/armor.ts`, `src/sim/damage.ts`, `src/sim/combat.selftest.mjs` |
| ai       | `src/game/ai.ts` |
| hud      | `src/ui/hud.ts`, `src/ui/garage.ts`, `src/ui/damagePanel.ts` |
| fx       | `src/fx/effects.ts`, `src/fx/particles.ts` |
| audio    | `src/audio/audioEngine.ts` |
| integration | `src/main.ts`, `src/game/state.ts` |

Research docs each builder MUST read: `docs/history/research/graphics-aaa.md` (engine, world,
fx), `docs/history/research/movement-physics.md` (engine cameraRig, movement, vehicles specs),
`docs/history/research/armor-penetration.md` + `docs/history/research/shells-ballistics.md` (combat,
vehicles specs, ai), `docs/history/research/tank-roster.md` (vehicles, hud garage),
`docs/SCREENSHOT_CONTRACT.md` (everyone).

---

## 1. Global conventions (binding on every module)

### 1.1 Units & coordinates
- **Meters, seconds, radians** for ALL runtime state and ALL function arguments/returns,
  unless the field name carries a unit suffix (see 1.2). World is three.js standard:
  right-handed, **+Y up**. Map spans x,z ∈ [-512, +512] (1024 m square), y = terrain height.
- **Tank local frame**: origin at the **ground-contact center** of the hull (bottom of
  tracks, centered in plan). **Local forward = +Z**, +Y up. Locked axis formulas:
  `forwardAxis(yaw) = [sin(yaw), 0, cos(yaw)]`, `rightAxis(yaw) = [cos(yaw), 0, -sin(yaw)]`.
  `yaw = 0` faces world +Z; positive yaw turns the nose toward +X.
  Hull attitude mapping to the visual root is locked as: `root.rotation.order = 'YXZ'`;
  `rotation.y = yaw`, `rotation.x = -visualPitch` (positive pitch = nose up),
  `rotation.z = visualRoll` (positive roll = right side down). Only tankFactory's
  `syncFromState` and armor.ts's inverse transform implement this mapping; everyone else
  treats `yaw/pitch/roll` as plain numbers.
- **turretYaw** is hull-relative, radians, 0 = gun forward, same sign sense as hull yaw.
- **gunPitch** is relative to the hull plane, radians, **positive = muzzle up**.
- `dt` is **seconds**. Fixed sim step = `1/60` s. Render step is variable.
- Positions passed across module boundaries are `THREE.Vector3` where the signature says
  `Vector3`, and plain `[x,y,z]` arrays where it says `vec3` (event payloads use `vec3`
  so events are JSON-serializable).

### 1.2 Unit-suffix convention for spec/stat fields
Static spec data (`specs.ts`) keeps the research docs' human units, flagged by field-name
suffix — consumers convert at point of use:
`...Kmh` (km/h, `mps = kmh/3.6`), `...DegS` (deg/s), `...Deg` (degrees), `...Mm` (mm),
`...M` (meters), `...S` (seconds), `...Hp` (horsepower), `...Tons` (metric tons).
No suffix ⇒ SI/radians. Never store radians in specs; never pass degrees at runtime.

### 1.3 Module hygiene (screenshot contract depends on this)
- **Zero top-level side effects.** No DOM/WebGL/AudioContext access at import time. Only
  pure data and function definitions at module top level. All setup happens inside the
  exported `create*/init*` functions. This makes every module importable under plain
  node and keeps the load path error-free.
- **ES modules everywhere.** `package.json` has `"type": "module"` (already set — do not
  change it). Imports: `three` and `three/examples/jsm/...` only. No other packages, no
  CDN, no fetch of any asset.
- `src/sim/*`, `src/vehicles/specs.ts`, and `src/game/ai.ts` are **pure-logic modules**:
  they may import `three` **for math classes only** (Vector3/Matrix4/Quaternion/Ray/Box3)
  — never anything that touches WebGL or DOM — so they run under plain node.
- **Import rules**: any module may import the pure-logic modules above. Nothing else may
  be imported across builder boundaries. All stateful/scene objects arrive as function
  parameters wired by integration.
- No `console.error`/`console.warn` on any reachable path. Guard every shader-string
  `.replace()` injection by asserting the string changed; if it didn't, `throw` at init
  (loud, catchable) — never limp along.
- No per-frame allocation in update loops (reuse scratch Vector3s, module-scope).

### 1.4 Determinism & RNG
- Canonical PRNG — copy this verbatim into any module that needs randomness (do NOT
  create a shared file for it):
  ```js
  export function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);
    t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
  ```
- An `rng` parameter always means `() => number in [0,1)`.
- **Never call `Math.random()`, `Date.now()`, or `performance.now()` inside sim, fx,
  world, or vehicles code.** Time arrives as a parameter; randomness arrives as `rng` or
  a `seed` option. Fixed seeds: terrain `1337`, vegetation `2001`, props `2002`, textures
  `3000 + layerIndex`, per-tank camo `4000 + spawnIndex`, fx `5000`, combat per-battle
  `6000` (integration passes these; defaults inside modules must equal these values).

### 1.5 Event bus (injected, not imported)
Integration constructs the bus and passes it to modules that need it. Reference
implementation (integration owns it; builders may copy it into selftests only):

```js
function createBus(){ const m=new Map(); return {
  on(ev,fn){ (m.get(ev)??m.set(ev,[]).get(ev)).push(fn); return ()=>this.off(ev,fn); },
  off(ev,fn){ const a=m.get(ev); if(a){ const i=a.indexOf(fn); if(i>=0)a.splice(i,1);} },
  emit(ev,payload){ const a=m.get(ev); if(a) for(const fn of a.slice()) fn(payload); },
};}
```

**Event names and payloads (complete list — do not invent new ones):**

| event | payload | emitted by |
|---|---|---|
| `shell:fired` | `{ shellId, shooterId, isPlayer, shellType, caliberMm, muzzlePos:vec3, dir:vec3 }` | integration (after `createShell`) |
| `shell:hit` | `HitEvent` (§2.6) | integration (from damage.ts return) |
| `shell:expired` | `{ shellId, pos:vec3, hitTerrain:boolean }` | integration |
| `tank:destroyed` | `{ id, specId, pos:vec3, killerId, cause:'shot'|'fire'|'ammorack' }` | integration |
| `tank:fire` | `{ id, burning:boolean }` | integration |
| `module:state` | `{ id, module:ModuleName, state:'ok'|'yellow'|'red' }` | integration |
| `player:reload` | `{ t, total }` (every sim tick while reloading) | integration |
| `ui:shellSelect` | `{ slot:0|1|2 }` | hud |
| `ui:magazineReload` | `{}` | input/hud |
| `ui:battleStart` | `{ specId }` | garage |
| `ui:click` | `{}` | hud/garage (any button press) |

FX and audio each expose `bindBus(bus)` for subsystem reactions. The typed
`combatFeedbackRuntime.ts` owner bridges discrete hit/ERA/camera-recoil,
destructible-prop, and Garage-residency presentation reactions without placing
them in the simulation or composition root. HUD and other presentation owners
receive the bus through their constructors; authoritative state never imports a
browser presentation consumer.

---

## 2. Shared data structures (exact shapes)

### 2.1 `TankId` and roster constants

`specs.ts` owns stable vehicle IDs and registered records.
`rosterPolicy.ts` derives the production, development, and reference
projections; `fleetOrder.ts` then makes each related native family contiguous
in historical/design progression. Registration order is never a UI or
matchmaking contract.

### 2.2 `TankSpec` (exported by `src/vehicles/specs.ts`)
```js
TankSpec = {
  id: TankId, name: string, nation: string,
  era: 'interwar'|'ww2'|'cold-war'|'modern'|'next-generation',
  role: 'light'|'medium'|'heavy'|'td'|'mbt'|'ifv'|'spg', // simulation-only
  hp: number,                                  // locked table §3.3.1
  // --- mobility (schema of movement-physics.md §1) ---
  enginePowerHp, weightTons, topSpeedKmh, reverseSpeedKmh: number,
  hullTraverseDegS: number,
  terrainResistance: { hard, medium, soft },   // dimensionless
  trackTraction?: number,                      // optional running-gear grip multiplier
  pivotStyle: 'pivot'|'neutral',
  // --- turret & gun kinematics ---
  turretTraverseDegS, gunPitchDegS, gunElevationDeg, gunDepressionDeg: number, // depression positive
  // --- gun ---
  gun: {
    caliberMm: number, reloadS: number,
    autoloader?: {
      magazineSize: number,      // ready rounds at battle start/full reload
      intraClipS: number,        // delay between shots in one magazine
      fullReloadS: number,       // all-or-nothing magazine replenishment
    },
    baseAccuracy: number,        // meters dispersion @100 m, fully aimed (2σ)
    aimTimeS: number,
    bloom: { move, hullRot, turret, afterShot }, // movement doc §1 semantics
    shells: [ShellSpec, ShellSpec, ShellSpec],   // slot 0 = standard, 1 = special, 2 = HE
  },
  dims: { hullLengthM, overallLengthM, widthM, heightM },
  armor: ArmorModel,             // §2.3
  visual: object,                // OPAQUE — tankFactory-internal (camo colors, detail flags)
}

ShellSpec = {
  name: string,
  type: 'AP'|'APCR'|'HEAT'|'HE'|'APFSDS',   // roster APHE/APCBC/APBC ⇒ 'AP'
  caliberMm: number,             // copy of gun caliber
  pen100Mm: number, pen1000Mm: number,      // linear interp 100→1000 m, clamped outside
  dmg: number,                   // avg HP damage (roster values)
  velocityMps: number,           // real-ish muzzle velocity (shells doc §1)
  moduleDmg: number,             // default = caliberMm
  tracer: 'AP'|'APCR'|'HEAT'|'HE'|'APFSDS', // fx preset key (shells doc §10)
  reloadS?: number,              // PER-SHELL reload (IFV autocannon belt vs. ATGM
                                 // rail) — governs this slot in startReload;
                                 // absent ⇒ gun.reloadS. Conventional shells
                                 // share the gun channel; guided launchers keep
                                 // independent background reload channels.
  count?: number,                // rounds carried — overrides the type-level
                                 // default loadout (belts vs. missile racks)
}
```
Modern roster pens are quoted @2 km: encode as `pen1000Mm = quoted2kmPen / (1 - lossPer100m*10) `
inverse-solved so that the shells-doc falloff table §4 reproduces the quoted value at
2 km — vehicles builder does this arithmetic; consumers only ever read pen100/pen1000.

### 2.3 `ArmorModel` (data-only, inside `TankSpec.armor`)
Combat raycasts against this. The fleet finalizer derives a closed, low-complexity
collision shell from the actual first-party procedural armor mesh; authored zones
remain the source of thickness/material behavior, but no playable vehicle relies on
disconnected broad quads or AABBs as its main silhouette.
```js
ArmorModel = {
  boundingRadiusM: number,          // broadphase sphere around tank origin
  turretPivot: [x,y,z],             // hull-local position of turret rotation center
  gunPivot: [x,y,z],                // TURRET-local position of gun trunnion
  gunBarrel: { lengthM, radiusM },  // cylinder along +Z from gunPivot (external module 'gun')
  hullPlates:   Plate[],            // hull-local frame
  turretPlates: Plate[],            // turret-local frame (rotates with turretYaw; mantlet
                                    //  plates may set gunFollow:true → also pitch with gun)
  collisionShells: {                // generated from actual procedural geometry
    hull: ConvexCell[],              // closed longitudinal union in hull-local frame
    turret: ConvexCell[],            // closed union in turret-local frame
  },
  modules: ModuleVolume[],          // hull-local (turretLocal:true ⇒ turret frame)
  crew:    CrewVolume[],
}
Plate = {
  name: string,                     // 'upper_glacis', 'turret_cheek_L', ...
  verts: [[x,y,z],[x,y,z],[x,y,z],[x,y,z]],  // planar convex quad, CCW seen from OUTSIDE
                                    // (outward normal = normalize(cross(v1-v0, v3-v0)))
  physicalMm: number,               // for ricochet/overmatch geometry
  keMm: number, ceMm: number,       // RHAe (WWII steel: keMm = ceMm = physicalMm)
  kind: 'main'|'spaced'|'era'|'external',   // external = tracks/stowage screens
  era: null | { keReduction:number, ceFlatMm:number },   // kind==='era' only
  moduleLink: null | ModuleName,    // e.g. track plates link 'trackL'
  gunFollow: boolean,               // turret plates only (mantlet)
}
ConvexCell = {
  min:[x,y,z], max:[x,y,z],       // broadphase only
  vertices:[[x,y,z], ...],
  faces:[{ indices:[i0,i1,i2], normal:[x,y,z], constant:number,
           plate:Plate, internal:boolean }],
}
SmoothShape =
  | { kind:'ellipsoid', center:[x,y,z], radii:[x,y,z] }
  | { kind:'capsule', a:[x,y,z], b:[x,y,z], radius:number }
  | { kind:'ellipticCylinder', center:[x,y,z], axis:0|1|2,
      halfLength:number, radii:[r0,r1] }
ModuleVolume = { module: ModuleName, min:[x,y,z], max:[x,y,z],
                 turretLocal:boolean, shapes:SmoothShape[] }
CrewVolume   = { crew: CrewName, min:[x,y,z], max:[x,y,z],
                 turretLocal:boolean, shapes:SmoothShape[] }
ModuleName = 'engine'|'fuelTank'|'ammoRack'|'gun'|'turretRing'|'radio'|'optics'|'trackL'|'trackR'
CrewName   = 'commander'|'gunner'|'driver'|'loader'   // 3-crew tanks (t34_85 pre-85? no —
             // t90am has no loader; omit absent crew members from the array entirely
```
The generated shell is sliced only along vehicle-local Z and convex-hulled from
clipped source triangles, so adjacent components share closed boundaries while the
bow, shoulders, cheeks, bustle, cupolas and hatches retain their changing section.
Every face maps back to a canonical `Plate`; ERA, spaced screens, external tracks and
gun-follow mantlets remain separately ordered layers. Internal authoring bounds are
converted to ellipsoids, capsules or elliptic cylinders, split across shell cells when
necessary, and seated fully inside the closed armor before combat begins.

**trackShapes addendum (2026-08-06, fleet-wide).** Track hitboxes are no
longer per-tank rectangle stacks: `attachTrackShapes` (specs.ts) derives one
convex prism per side from each profile's `trackLoopPoints` at spec time, and
`tankFactory.trackHitboxHull` mirrors the same derivation for the visual
debug hull, so the killcam and combat agree by construction. Combat raycasts
enter through `intersectTrackPrism` (src/sim/armor.ts) before the plate walk
(`moduleLink 'trackL'/'trackR'` semantics unchanged); the killcam renders the
true trapezoid + loop-following slats via `addTrackPrism`. The prisms are
derived data — never hand-author them; fix the gear loop instead. Hash/gate
neutrality was proven at the fleet landing (101/101 profiles, combat suite
253 checks).

### 2.4 `TankEntity`, `TankState`, `CombatState`
Integration composes entities; each sub-object has exactly one owner module.
```js
TankEntity = {
  id: string, specId: TankId, spec: TankSpec,
  team: 'player'|'enemy', isPlayer: boolean,
  state: TankState,        // owned by movement.ts
  combat: CombatState,     // owned by damage.ts
  input: TankInput,        // written by integration (player) or ai.ts
  visual: TankVisual|null, // owned by tankFactory (null in headless tests)
  ai: object|null,         // opaque, owned by ai.ts
}

TankState = {              // movement.createTankState(spec, pos:Vector3, yaw) builds this
  pos: THREE.Vector3,      // authoritative root; Y may be above support in flight
  yaw: number, speed: number /* horizontal m/s signed */, yawRate: number /* rad/s */,
  verticalSpeed: number, grounded: boolean, landingImpactMps: number,
  visualPitch: number, visualRoll: number,        // spring outputs, radians
  turretYaw: number, gunPitch: number,            // radians (conventions §1.1)
  turretYawRate: number,                          // rad/s (for bloom)
  aimPoint: THREE.Vector3,                        // world target the gun chases
  bloomF: number,                                 // dispersion multiplier ≥ 1
  trackScroll: { l: number, r: number },          // cumulative meters per track
  atGunLimit: boolean,                            // gun pinned at elevation/depression
  _spring: object, _prevSpeed: number,            // movement-internal
}

TankInput = {
  throttle: number /* -1..1 */, steer: number /* -1..1 */, brake: boolean,
  fire: boolean, aimPoint: THREE.Vector3, shellSlot: 0|1|2,
}

CombatState = {            // damage.createCombatState(spec) builds this
  hp: number, maxHp: number, destroyed: boolean,
  modules: { [ModuleName]: { hp, maxHp, state:'ok'|'yellow'|'red', repairT:number } },
  crew:    { [CrewName]: boolean },               // alive?
  fire: { burning: boolean, tickTimer: number, ticksLeft: number },
  eraSpent: Set<string>,                          // Plate.name of detonated ERA tiles
  reload: {
    t: number, totalS: number,
    kind: 'ready'|'shell'|'intraClip'|'magazine',
  },                                              // t counts down to 0 = ready
  magazine: null|{ rounds: number, capacity: number },
  launcherSalvoShots?: number,                    // guided shots fired in the current rack salvo group
  magazineIndicator?: null|{ rounds, capacity, launcher: boolean }, // NETWORK MIRROR ONLY — see below
  shellSlot: 0|1|2,
}
```
Ammo selection preserves magazine rounds, salvo position, and every reload timer.
Types fired through the same gun share its cycle; separate cannon and launcher
channels advance concurrently, including while deselected. Selecting or reselecting
an ammo key never reloads a clip. Only a successful shot or the explicit magazine
reload control starts a cycle. Solo and network firing check the selected weapon's
timer, and an empty-slot request cannot fire a different fallback weapon.
Shells with the same explicit `reloadGroup` share a secondary weapon's cycle:
the BMP-3's 100 mm HE and gun-launched missile use one timer, independent of its
30 mm autocannon. Secondary weapons do not consume the main gun's magazine.

The reticle's multi-round indicator is never read from `magazine` directly: `sim/magazineIndicator.ts`
derives it once (the cannon magazine, or — with a guided round loaded on a `gun.launcherSalvo` rack —
the rounds left in the current salvo group, 0 while the rack runs its own 'shell' reload) for the solo
aim frame, the authoritative snapshot's `magazineRounds/Capacity` and the `player:reload` event. The
client bridge decodes those snapshot fields into `magazineIndicator` and fills `magazine` only for a
cannon magazine, so the manual magazine-reload rules keep reading the cannon alone.
Effects of module/crew state on gameplay (movement & integration read these — locked):
`engine` yellow ⇒ `enginePowerHp × 0.5`, red ⇒ immobile; `trackL|trackR` red ⇒ immobile;
`gun` yellow ⇒ σ×2 & no aim shrink below f=2, red ⇒ cannot fire; `turretRing` yellow ⇒
turret traverse ×0.5, red ⇒ ×0.2; `loader` dead ⇒ reload ×1.5; `gunner` dead ⇒ aimTime
×1.5; `driver` dead ⇒ accel & traverse ×0.7; ammoRack red ⇒ instant destruction.
Red modules auto-repair to yellow (hp=50%) after `repairT = 10 s`.

### 2.5 `ShellEntity` (owned by ballistics.ts)
```js
ShellEntity = {
  id: number, shooterId: string, isPlayer: boolean,
  spec: ShellSpec,
  pos: THREE.Vector3, prevPos: THREE.Vector3, vel: THREE.Vector3,
  ageS: number, dead: boolean,
  penRollDone: boolean, remainingPenMm: number,   // set by damage.ts during resolution
  bounces: number,
}
```

### 2.6 `HitEvent` (returned by damage.ts, emitted as `shell:hit`)
```js
HitEvent = {
  kind: 'pen'|'nonpen'|'ricochet'|'spaced_absorb'|'era'|'he_pen'|'he_splash'|'terrain',
  shellId: number, shellType: string, caliberMm: number,
  attackerId: string, targetId: string|null,      // null for terrain
  pos: vec3, normal: vec3,
  impactAngleDeg: number, effectiveMm: number, penRollMm: number,
  damage: number, targetHpAfter: number,
  modulesHit: [{ module: ModuleName, newState:'ok'|'yellow'|'red' }],
  crewHit: CrewName[],
  fireStarted: boolean, ammoRacked: boolean, destroyed: boolean,
  eraPlate: string|null,                          // Plate.name popped, for fx/visual strip
}
```

### 2.7 `HeightField` and `World` (owned by world builder)
```js
// terrain.js — PURE part, node-runnable, no three-scene code:
createHeightField(seed = 1337) => HeightField
HeightField = {
  getHeightAt(x, z) => number,          // meters; defined for all x,z (flat beyond map)
  getNormalAt(x, z) => THREE.Vector3,   // fresh or scratch — treat as read-only, copy if kept
  getGroundType(x, z) => 'hard'|'medium'|'soft',   // roads hard, fields medium, marsh soft
  size: 1024, minY: number, maxY: number,
}

// map.ts — composes terrain meshes + vegetation + props into a scene:
createMap(engineCtx, { seed = 1337 } = {}) => World       // engineCtx: §3.1.6
World = {
  heightField: HeightField,
  raycast(origin: Vector3, dir: Vector3, maxDist: number) => null |
      { point: Vector3, normal: Vector3, dist: number, kind: 'terrain'|'prop' },
  getObstacles() => [{ min:[x,y,z], max:[x,y,z] }],        // static AABBs (props, buildings)
  spawnPoints: { player: {pos:[x,y,z], yaw}, enemies: [{pos, yaw} × ≥7] },
  getMinimapFeatures() => { roads: [[ [x,z], ... ]], buildings: [{x,z,w,d,rot}],
                            treeClusters: [{x,z,r}], waterOrSoft: [{x,z,r}] },
  update(dt, cameraPos: Vector3),       // LOD, wind time accumulate
  setWindTime(t: number),               // freeze hook for screenshots
  group: THREE.Group,                   // already added to scene by createMap
}
```
`raycast` must be cheap (heightfield ray-march at 0.5–2 m steps + prop AABB tests) —
it is called a few dozen times per frame (camera, aim, AI LOS).

### 2.8 `EngineCtx` — the render-side dependency bundle
Created by integration from engine's exports and passed to world / vehicles / fx:
```js
EngineCtx = {
  renderer: THREE.WebGLRenderer, scene: THREE.Scene, camera: THREE.PerspectiveCamera,
  setupShadowMaterial(mat, extraOnBeforeCompile = null) => mat,  // lighting.ts §3.1.2
  anisotropy: number,                    // min(8, renderer max)
  quality: 'high'|'low',
}
```

---

## 3. Module contracts

### 3.1 engine — `src/engine/`

#### 3.1.1 `renderer.ts`
```js
export function createRenderer(container /* HTMLElement */) => THREE.WebGLRenderer
// exactly per graphics-aaa §1: antialias:false, stencil:false, high-performance,
// pixelRatio ≤ 1.5, SRGBColorSpace, ACESFilmic, PCFSoftShadowMap. Appends canvas.
export function onResize(renderer, camera) // sets size + camera aspect + updateProjectionMatrix
```

`viewportRuntime.ts` composes that renderer policy with post-target sizing and
CSM frustum refresh. It owns the sole window listener and a temporary 0x0 boot
recovery observer/interval; the first positive layout disconnects the recovery
work, while ordinary boots never create it.

`frameLoopScheduler.ts` owns browser frame delivery, including one queued-rAF
latch, context-restoration restart, and bounded hidden-pane recovery. Every
delivery path enters the same frame callback; hidden input or timer rescue can
never stack a second render loop when animation frames resume.

#### 3.1.2 `lighting.ts`
```js
export function createLighting(scene, camera, sunDir /* Vector3, unit, FROM origin TOWARD sun */)
  => Lighting
Lighting = {
  csm,                                   // the CSM instance (graphics doc §3 config)
  setupShadowMaterial(mat, extraHook = null) => mat,
     // csm.setupMaterial(mat) THEN wraps onBeforeCompile with extraHook (doc §3 pattern)
  update(),                              // per-frame csm.update()
  updateFrustums(),                      // on resize / fov change
  setSunIntensity(i), hemi: THREE.HemisphereLight,
}
```
Construct CSM **before** any material is compiled (integration guarantees call order;
lighting must not lazily defer CSM construction).

The four cascade maps are sized by the active graphics tier. Their five-tap
PCF rotation is anchored to shadow-map texels rather than screen pixels, so a
stationary world surface does not hatch or crawl as the camera moves. A minimum
filter footprint prevents low-resolution tiers from falling below an
anti-aliased texel. Procedural vehicles disable their thousands of detailed
shadow submissions and instead provide at most three articulation-aware convex
support hulls derived from the authored hull, turret, and gun meshes. Terrain,
buildings, poles, near vegetation, and dedicated wreck proxies remain regular
casters; distant decorative foliage stays intentionally non-casting.

#### 3.1.3 `sky.ts`
```js
export function createSky(scene, renderer) => SkyRig
SkyRig = {
  sunDir: THREE.Vector3,                 // fixed: elevation 35°, azimuth 140° (doc §5)
  bakeEnvironment(),                     // PMREM bake per doc §2.3; sets scene.environment
  horizonColor: THREE.Color,             // sampled/hand-tuned per doc §5(a)/(b)
  applyFog(scene),                       // scene.fog = Fog(horizonColor, 150, 1200)
}
```
Night sky (round 22, 2026-09-18): the dome shader adds a deterministic starfield, a galactic band and a
moon after its intensity multiply whenever the preset dims the dome (`nightAmount`), and the preset knobs
`nightSky` / `galaxy` / `nebulaHex` / `planetDeg` / `planetHex` let a map ask for a galaxy sky. The cloud
decks erode thin fringes with their own alpha field (`uEdgeDetail`).
Physically based atmosphere (round 65, 2026-09-24): on the desktop tier the visible dome, the environment bake, the
fog colour, the hemisphere light's hue and the post aerial pass's scatter-in target all derive from
`engine/atmosphere.ts` — Hillaire 2020's transmittance, multiple-scattering and sky-view LUTs rendered as fragment
passes only when the sun or a map's parameters change, plus an 8 × 1 summary readback; `skyPresetToAtmosphere` maps
every map's authored sky preset onto the model, the Preetham dome remains the mobile tier's path and the fallback,
and the terrain material never samples a LUT (it holds its sixteen texture units).
Light effects (round 69, 2026-09-24): on the desktop tier `engine/postLightFxPolicy.ts` resolves four levers per
preset (`?fx=off` / `?fx=names` for QA) — screen-space contact shadows marched inside the aerial pass against the
resolved depth and blended into the CSM visibility the opaque lit materials write into the scene target's alpha
(`engine/contactShadows.ts`), an analytic energy-conserved ground bounce added to the lit materials' indirect diffuse
through the CSM shader patch (`engine/groundBounce.ts`), and quarter-resolution sun shafts and a lens flare
(`engine/sunShafts.ts`, `engine/lensFlare.ts`) written into one light target the grade adds before its tonemap; the
pass order above is unchanged and no full-resolution pass was added.
Vehicle form in shade (2026-10-02): the vehicle readability floors (`vehicles/materials.ts`) aim a shaded plate's
fill by its world orientation — sky-facing plates most, the sun's bearing a little, a 0.28 lens share kept for
readability — rather than by how squarely it faces the lens; indirect light falls toward the ground along each
vehicle's own up axis (× 0.66 at the hull bottom, back to 1 at 1.75 m) through one shared ground reference that every
vehicle mesh points at its root before it draws (`tankFactoryCore.ts`); and a fifth light lever, `vehicleOcclusion`
(`engine/vehicleOcclusion.ts`, ultra/high/medium, `?fx=cavity`), adds a vehicle-only cavity occlusion inside the aerial
pass — fixed horizon taps against the resolved depth on pixels whose alpha carries the vehicle tag, scaling only the
ambient share — for bustles, skirts and wheel bays. Scene-wide GTAO stays off. The deep-shade floor lifts the light a
plate receives, not its output: each texel lands in proportion to its own paint against the map's mean tone (its last
mip), so a camouflage keeps its light/dark contrast on shaded sides and under canopy (the old lift brought every texel
to one luminance along its hue, and a desert scheme's dark patches vanished into the base tan).
Volumetric clouds (round 68, 2026-09-24): on the desktop tier `engine/volumetricClouds.ts` raymarches a per-map cloud
slab (its layer derived by `engine/cloudPresets.ts` from the map's authored sky block, its noise volumes baked by
`engine/cloudNoise.ts` in a worker) at one sixteenth of a half-resolution history with a 4 × 4 slot cycle and
reprojection, lit by the atmosphere's sun transmittance and sky irradiance, composited premultiplied through a
depth-tested dome behind the aerial pass's haze law; per-cascade alpha-tested planes on the shadow-only layer carry
the cloud shadows through the CSM, `post.ts` owns the single per-frame hook, and `?clouds=off` keeps the baked decks.
Round 71 (2026-09-25, still opt-in behind `?clouds=volumetric`): every map config authors a `clouds` block (a regime
from `engine/cloudscapes.ts` and any knob; main.ts carries it on the sky preset as `cloudscape`, Mars on its shared
preset) that `cloudPresets.ts` resolves through the regime rows; the trace reads a multi-scale weather field with a
type channel and a street / anvil / cirrus companion field in the wind frame, type height profiles, a rigid wind lean,
curl-warped erosion, the Hillaire multiple-scattering octaves under a dual-lobe phase with Beer–powder toward the sun,
a far stratocumulus band and a cirrus sheet behind the slab; the shadow gobos discard by the same fields through a
custom depth material, and the baked cirrus veil hides while the layer shows.
The layered sky (2026-10-01): `engine/cloudWeatherLayers.ts` adds to the same trace the weather beyond the slab — a
sea fog bank and rain shafts / virga in front of it; distant cumulonimbus cells with anvils and rain, the far band and
a 2.5D mid-level layer (altocumulus, altostratus, cirrocumulus, lenticular) behind it, sorted by distance; contrails on
the cirrus sheet — placed deterministically per map from the `clouds` block, with lightning in a night storm drawn in
the composite. `cloudPresets.ts` resolves the block for the battle's time of day (the diurnal law of convective cloud,
per-time knobs, a neutral albedo at sunset and night, the moonlight's hue, a town's glow on the bases).
The owner's cloud bar (2026-10-13): Verdant's fair-weather cumulus is the reference; the broken stratocumulus deck
("no more of the cloud type depicted in fjord") is retired from the regime vocabulary, Fjord, Polders and Copper Mesa
carry fair-weather cumulus tuned to their place, and `engine/cloudsBan.selftest.mjs` keeps the deck out of every map,
time of day, weather variant, Studio plan, Garage sky and phone deck.
Clouds 2.0 (2026-10-06, after the clouds package of Takram's three-geospatial; MIT, the port recorded in
docs/ATTRIBUTION.md): the slab is a layered medium. `engine/cloudLayers.ts` turns the map's resolved preset into up to
four altitude lanes (the regime's main layer and the layer aloft the meteorology puts over it), each a coverage of the
local weather (`cloudNoise.ts` `bakeCloudLocalWeather`: cumulus fields with clearings, the elements aloft, the decks'
stratiform field and cells, equalised, on a 48 km tile) shaped by a height function (a dome over a flat base, a deck
flat on both faces, an anvil) into a shell that a 3.2 km Perlin–Worley shape volume and a detail volume
(`cloudVolumeNoise.ts`, baked on the GPU at load) carve under a density profile (`cloudShaders.ts`). The shells curve
with a parabolic Earth so the field converges at the horizon; the march (36 km on High) strides by the footprint and
refines on entering a cloud. Each sample's optical depth to the sun is a short secondary march plus a Beer shadow map —
two toroidal, world-anchored cascades (12 km about the camera and 40 km about the camera's point at the stack's
middle height carried down the sun) of the same medium marched along the sun by lanes and altitude slices, a band a
frame, read as the four texels' depths blended as transmittances —
under the multiple-scattering octaves, a dual-lobe phase, the powder term, the sky and ground light and a deck's
diffusion (by the vertical depth over the point — in a deck, the column over it in its own cell, so a thick core is dark
beside a thin seam); the trace writes its depth, and the resolve reprojects by it and clips to its neighbourhood's
variance. The clouds' sun is the light model's colour (`scene.userData.lightModel`) times the air between the ground and
the cloud, and under a closing deck the ground light the bases see is what the deck passes down (`cloudGroundLight`). The
near cascade's column depth is the cloud shade the lit materials read (`cloudShadeMap.ts`, the contract unchanged), and
its mean over the battlefield is published as `scene.userData.cloudSunMean` for the light model. The dome composite,
the history the lens flare / sun shafts / horizon panorama read and the sky beyond the medium (rain, fog bank, cirrus,
contrails, lightning) are unchanged; the far band is gone (the curved shells carry the field to the horizon).

Horizon ring — vista pass (round 24, 2026-09-19; owner: "the stuff around the map like mountains needs to
be so much better … consider this a triple AAA pass"). `world/maps/horizon.ts` now builds a 431-column
ring whose row ladder is subdivided on every span (18 rows on the rolling / mesa / escarpment styles, 36 on
alpine) with ridged relief (spurs and gullies about 260 m and 90 m apart) instead of two smooth octaves,
seats its buried anchor and first exterior row on the battlefield's own edge height and gradient
(`seatHorizonSkirtOnGround`; Autumn and Redrock keep their own seams), and stands the first authored ridge
at 700–720 m so the foothill band behind the rim is a real hillside. The tableland maps bound every cap
rise at 1.25:1 (`reshapeFiniteTableCaps`, authored-row driven). On the desktop tier the ring's fragment
program is the layered vista material in `world/horizonVista.ts`: five tileable colour tiles (meadow,
canopy, rock, scree, snow) sampled triplanar in world space, weights from slope / altitude / three
world-anchored noise fields, strata beds and seams, a screen-derivative bump normal lit by the map sun plus
a hemispherical sky term, and per-fragment aerial haze toward the fog tint (the vertex bake is tone-only
there; mobile keeps the older per-vertex programs). The rows up to the first ridge render with the
terrain's own splat material (`terrain.ts` `bindAutumnHorizonGround` generalised to every map, columns
and bands from `mesh.userData.horizonRing`, meadow tint refreshed from the ground albedo mean), with the
splat mask faded outside the playable square so no road or dirt streak climbs the ring. `buildHorizonForest`
scatters an instanced forest where the fragment program paints stands (the JS twin of its stand function
over the shared detail noise): species and crown palettes follow the map's `vegetation.rimMix` /
`palettes` (pine / spruce / fir / cedar are conifers), the rim band keeps three quarters of the 8000-instance
budget thinned uniformly around the perimeter, the band trees nearest the edge form a rich shadow-casting
near class, and the ranges beyond get a two-tier class; the crowns carry the canopy tile's mottle, rim
darkening and the ring's haze curve per fragment. The forest material joins the cascade through
`engineCtx.setupShadowMaterial(material, hook)` — the hook must be passed as the extra hook, since the
cascade setup replaces `onBeforeCompile`.

#### 3.1.4 `post.ts`
```js
export function createPost(renderer, scene, camera) => Post
Post = {
  composer,
  render(dt),                            // composer.render() — the ONLY render call
  setSize(w, h),
  bloom, gtao,                           // passes, for quality toggles
  setQuality(level /* 'high'|'low' */),  // low: gtao.enabled=false
}
// Chain locked (graphics doc §4): RenderPass → GTAOPass → UnrealBloomPass(0.35,0.55,0.85)
// → SMAAPass → OutputPass. HalfFloat target with DepthTexture.
```

#### 3.1.5 `cameraRig.ts`
```js
export function createCameraRig(camera, deps) => Rig
// deps = { heightField, raycast /* World.raycast */, getPlayer: () => TankEntity }
Rig = {
  mode: 'ARCADE'|'SNIPER',
  zoom: number,                          // sniper zoom step value (2|4|8|16|25)
  aimPoint: THREE.Vector3,               // server-aim raycast result, updated each frame
  aimDist: number,
  update(dt, camInput),                  // camInput = { mouseDX, mouseDY, wheel:-1|0|1,
                                         //   rmb:boolean /* generic free-look hold */,
                                         //   shiftPressed:boolean }
  addTrauma(x),                          // 0..1, shake per graphics doc §11
  enterSniper(), exitSniper(),
  getAimRay(outOrigin: Vector3, outDir: Vector3),
  // --- screenshot hooks ---
  setExternalPose(pos: Vector3, lookAt: Vector3, fovDeg = 50),  // suspends rig control
  snapArcade(step /* 0..5 */, orbitYaw, orbitPitch),            // deterministic arcade pose
  snapSniper(zoom, aimYaw, aimPitch),
  release(),                             // resume normal control
}
```
Behavior per movement-physics doc §9 verbatim: orbit steps `[24,18,13,9,6,4]`, sniper
zooms `[2,4,8]` (+16/25 flagged), pivot 2.5 m above turret, pitch clamp [-65°,+15°],
collision pull-in, FOV 60/zoom, hide player visual in sniper
(`player.visual.root.visible = false` — rig does this itself via `getPlayer()`).
Rig writes `getPlayer().input.aimPoint.copy(rig.aimPoint)` every update.

#### 3.1.6 Engine assembly note
Integration builds `EngineCtx` (§2.8) from these pieces. Engine files may import each
other freely (single builder).

### 3.2 world — `src/world/`
Exports locked in §2.7. Additional requirements:
- Browser integration imports `map.ts` dynamically on first battlefield use.
  `worldBuildCoordinator.ts` owns in-flight joins, background promotion,
  cancellation, residency, and eviction. A cold debug/capture switch is
  asynchronous; production battle and Studio entry await the same cached
  `ensureWorld` promise.
- `terrain.js` also exports `buildTerrainMeshes(heightField, engineCtx) => THREE.Group`
  (chunked LOD meshes + splat material per graphics doc §6–7; uses
  `engineCtx.setupShadowMaterial(mat, splatHook)`); `map.ts` calls it.
- `vegetation.ts`: `createVegetation(heightField, engineCtx, seed = 2001) =>
  { group, update(dt, camPos), setWindTime(t), treeObstacles: AABB[] }` — instanced
  grass + trees + wind per doc §8.
- `props.ts`: `createProps(heightField, engineCtx, seed = 2002) =>
  { group, obstacles: AABB[], colliders /* for raycast */, features /* minimap */ }` —
  rocks, ~10-building village, walls/cover, roads are terrain-material features
  (getGroundType returns 'hard' on them).
- Water: `shallowWater.ts` owns the translucent sea / lake sheet over the admitted wet cells and its apron past
  the square; `waterRipples.ts` the world-anchored GPU shallow-water field it reads for wakes and splashes; and (round
  66) `oceanSpectrum.ts` + `oceanFft.ts` the FFT ocean — a per-map spectrum (`ocean` block on the map config) turned
  into displacement / slope / foam maps by fragment-shader butterfly passes every frame — that the sheet displaces
  and shades with. The in-square sea colour and the marine ring faces stay the terrain material's; nothing here
  adds a terrain sampler.
- Small obstacle contact: street rubble, steel hedgehogs, and loose surface rocks
  (scatter scale 1.25–1.8, at most half embedded) crush immediately under a moving
  tank, including crawling/reversing, without an impact slowdown or track damage.
  Large rocks, authored tactical outcrops, and rubble repurposed as Reservoir
  waterworks remain solid cover. `crushableClutter.ts` keeps debris visible by
  flattening its existing batched vertices or rock instance; it adds no meshes,
  draw calls, or steady-frame work. All three hedgehog beams share one appended
  prop identity. Movement, shell collision, authoritative destruction events, and
  late-join state use that identity together; cached-world rematches restore exact
  original geometry and collision. Server shards must be recaptured after changes
  to this policy. `crushableClutter.selftest.mjs` exercises native collision shapes,
  light/heavy forward/reverse contact, track health and replication;
  `tools/crushable-clutter.browser.mjs` verifies live map geometry and resets.
- Building authoring has two performance contracts. Landmark geometry and its
  connected exterior fixtures merge into existing material buckets before GPU
  upload. Repeated destructible structures keep one intact and one broken
  `InstancedMesh` family, never one object/material per placement. Every
  individual landmark part must be connected within the authoring tolerance.
  `structureConnectivity.ts` owns the typed support-graph invariant and the
  structure selftests construct all 38 heavyweight/site builders with two
  deterministic variants before release. The 28 additional structure families
  retain 16 destructible families and their persistent broken-state pools.
  `structureInstanceAppearance.ts` owns deterministic per-instance diffuse
  variation; intact and packed broken slots must resolve the same tint without
  cloning a material or adding a live update.
- `destructibleRenderPolicy.ts` is the single cascaded-shadow classifier for
  destructible families. Buildings, cover, walls, fences, large silhouettes,
  and toppling actors keep dynamic shadows. Sub-meter grounded clutter can rely
  on direct lighting, GTAO, and received world shadows rather than multiplying
  a tiny silhouette through every cascade. Visible geometry and collisions are
  not changed by this policy.
- Building PBR fallbacks carry color, normal, and one packed linear surface map
  (AO in red, roughness in green). CC0 sourced replacements mutate those same
  texture objects asynchronously. Renderer-owned ACES tone mapping, PMREM,
  bloom and cascaded shadows must not be duplicated inside world builders.
- Map layout: village near center (≈ x -60..+80, z -40..+120), two roads crossing it,
  spawnPoints.player south edge of village, 7 enemy spawns spread N/NE/NW at 150–400 m.
  Terrain must be drivable (slope ≤ 35°) between all spawn points and the village.
- Determinism: same seed ⇒ identical world, byte-for-byte heights.

### 3.3 vehicles — `src/vehicles/`

#### 3.3.1 `specs.ts` (PURE data + pure functions; **no three import at all** here)
```js
export const TANK_IDS;                       // §2.1 locked order
export const TANK_SPECS: { [TankId]: TankSpec };
export function getSpec(id) => TankSpec      // throws on unknown id
```
`specHelpers.ts` is the registry-free typed constructor boundary for armor
quads, shells, internal module/crew boxes, and shared armor envelopes. It uses
meter-space three-value tuples and millimeter resistance values and must remain
free of DOM, Three.js, builder, and registry imports.
Locked stat values (transcribe the rest from tank-roster.md; these resolve ambiguity):

| id | hp | hullTraverseDegS | turretTraverseDegS | baseAccuracy | aimTimeS | terrainResistance | pivotStyle | reloadS |
|---|---|---|---|---|---|---|---|---|
| m1a1_abrams_hc     | 2600 | 44 | 40 | 0.30 | 1.8 | 0.7/0.8/1.5 | neutral | 6.0 |
| t90am     | 2000 | 42 | 38 | 0.35 | 2.2 | 0.7/0.8/1.5 | neutral | 7.5 |

(The m4a3e8, tiger1, t34_85, is2, panther_g and leo2a7 rows retired with the
hidden fleet on 2026-09-23; the Leopard 2A7 row lives on as the unregistered
donor template in `src/vehicles/donorSpecs.ts`.)

`gunPitchDegS = 0.8 × turretTraverseDegS` (round to int). Bloom: WWII
`{move:0.20, hullRot:0.20, turret:0.12, afterShot:4}`, modern (stabilized)
`{move:0.06, hullRot:0.08, turret:0.06, afterShot:3}`. Elevation/depression, weights,
engine hp, speeds, shell pens/dmg: from the roster tables verbatim. Shell velocities
(m/s, locked): m1a1_abrams_hc 1670/1400/1000; t90am 1750/905/850. (slots:
standard/special/HE.)

#### 3.3.2 `fleetFactory.ts` / `factoryGeometry.ts` / `tankFactoryCore.ts`
```ts
export function ensureTankBuilder(specId: string): Promise<void>
export function ensureTankBuilders(specIds: readonly string[]): Promise<void>
export function createTank(specId: string, engineCtx, opts = {}): TankVisual
// opts = { camoSeed = 4000, quality = 'high' }
TankVisual = {
  root: THREE.Group,                     // NOT added to scene — integration adds it
  specId,
  syncFromState(state: TankState),       // applies pos/yaw/visualPitch/visualRoll to root,
                                         // turretYaw/gunPitch to sub-groups, wheel spin +
                                         // track scroll from state.trackScroll & speed,
                                         // suspension bob hooks
  gunMuzzleWorld(out: Vector3) => out,   // world-space muzzle tip
  gunPivotWorld(out: Vector3) => out,
  turretTopWorld(out: Vector3) => out,   // for camera pivot / HP bar anchor
  recoilKick(ageS=0, impulseScale=1),    // barrel slide-back anim (visual only, self-timed
                                         //   via dt accumulated in syncFromState)
  stripEra(plateName),                   // remove ERA brick cluster visual (t90am)
  setDestroyed(),                        // burnt: dark material, drooped gun, decapitated
                                         //   turret optional; idempotent
  setVisible(v), dispose(),
  dims: { lengthM, widthM, heightM }, boundingRadiusM,
}
```
Browser consumers must await the builder gate before the first synchronous
`createTank` for an id. The strict import-free `fleetManifest.ts` owns the
id-to-family mapping; the loader table must cover every family at compile time,
and concurrent requests share one retryable promise. A missing gate throws
instead of silently constructing a legacy fallback. `tankFactory.ts` remains
the eager facade for Node audits and release tools that intentionally sweep the
whole roster. Geometry-derived combat-anatomy and vehicle-marking receipts use
the same demand boundary through `combatAnatomyCalibrationLoader.ts` and
`vehicleMarkingSeatLoader.ts`. Their typed registries validate each generated
record before publication; grouped payloads remain generator-owned TypeScript
and are never imported directly by browser feature code.
Geometry bar: per tank-roster.md §*.5 visual specs — composed BufferGeometries
(mergeGeometries), correct silhouettes, road wheels + sprocket/idler + track band,
signature details per Appendix B. ~8–15k tris full LOD; build a `THREE.LOD` with a
~3k mid LOD if time allows (optional). Track scroll: scroll a texture offset or slide
instanced links — builder's choice, must respond to `state.trackScroll`.
`wheelQuality.ts` is the release-facing receipt boundary for wheel families,
suspension linkage, inboard clearance, end-wheel construction, and working-gear
paint roles. Keep this audit out of player-frame work and run its fleet sweep
after shared running-gear changes.
All materials through `materials.ts`; every lit material passes through
`engineCtx.setupShadowMaterial`.

Final color-pass meshes receive deterministic semantic coplanar depth layers
after decoration, static batching and battle-detail grouping. This resolves
equal-depth seams between objects that must stay separate for materials,
articulation or damage ownership; shadow-pass materials are never offset.
Incorrect broad overlays must still be fixed geometrically. The fleet-wide
invariant is `npm run tank:surface-overlap:check`, which must report zero
unresolved positive-area, same-facing exterior overlaps.

#### 3.3.3 `materials.ts` (vehicles-internal; exact API is the builder's choice, but:)
```ts
export function createTankMaterials(spec, engineCtx, camoSeed) {
  return { hull, tracks, wheels, detail /* ... */ };
}
```
Procedural camo per roster paint notes (canvas textures, sRGB albedo, subtle normal/
roughness). MeshStandardMaterial only.

`appearanceAudit.ts` owns semantic material roles and the fixed neutral
running-gear palette. Builders may tag roles, but must not duplicate or bypass
its normalization and release-audit rules; painted armor and working gear are
separate even when they share a visual hierarchy.

### 3.4 movement — `src/sim/movement.ts` (pure logic)
```js
export function createTankState(spec, pos /* Vector3 */, yaw) => TankState        // §2.4
export function resetTankVerticalState(state, y, verticalSpeed = 0, grounded = true) => void
export function updateTank(entity /* {spec, state, input, combat} */, heightField, dt,
                           collide = null) => void
// collide: null | (pos: Vector3, radiusM: number, outPush: Vector3) => boolean
//   (integration provides tank-vs-tank + tank-vs-obstacle circle pushback; movement
//    adds outPush to pos after integration when
```

### docs/ASSET-PROVENANCE.md
```
# First-party asset provenance

Kevin B. Liu's creator credit is now attached to each procedural vehicle's
`root.userData.provenance`. It includes a stable vehicle ID, copyright, license
and attribution pointers. Three.js preserves serializable `userData` in its
JSON representation and exports it as glTF node `extras`. This is inspectable
metadata, not hidden instructions, geometry perturbation, DRM or telemetry.
It adds no meshes, draw calls, textures or per-frame work.

Every public build writes `dist/asset-provenance.json`: SHA-256 fingerprints of
tracked vehicle/world source, the world collision manifests, and first-party
icon, map, minimap, field-guide, FX, audio and site media files, together with
the license policy, notices and attribution record. The receipt records
the source revision and a digest of the ordered file inventory. File hashes
describe the actual build checkout; the revision alone does not assert it was
clean. References, downloaded models, fonts and partner branding are
outside this reviewed scope. Existing embedded and third-party notices always
take precedence; the receipt does not relicense anything.

## Generate and verify

From the repository root:

```sh
node tools/asset-provenance.mjs --write=dist/asset-provenance.json
node tools/asset-provenance.mjs --check=dist/asset-provenance.json
```

Verification compares the complete current tracked inventory and bytes, so
edits, additions, deletions and changes to the license/attribution documents
fail. Preserve a release receipt with its matching source revision. Stage new
intended content before generating a release receipt; untracked work is not a
release input. Ordinary builds generate **unsigned** receipts: their hashes
detect differences against a trusted copy, but anyone can regenerate them.

For a signed release, provide an independently managed Ed25519 key stored
outside the repository:

```sh
node tools/asset-provenance.mjs --write=dist/asset-provenance.json --sign-key=/absolute/private/key.pem
node tools/asset-provenance.mjs --check=dist/asset-provenance.json --public-key=/absolute/trusted/public.pem
```

Signing covers the entire receipt, including creator, revision and file hashes.
Verification requires the trusted public key separately; it never trusts a key
supplied inside the receipt. No key is generated, committed or shipped by this
implementation. Keep an independent signed release archive and public-key
fingerprint if you use this path.

## Limits and research

Metadata can be stripped and unsigned hashes can be replaced. A signature proves
that a key signed specific bytes, not that its holder originated the work. None
of this guarantees legal ownership, prevents copying, or makes a watermark
undetectable by agents.

The [glTF asset schema](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/schema/asset.schema.json)
provides an explicit copyright field; node extras can carry project metadata.
[C2PA](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html)
provides a stronger interoperable framework for signed media provenance and
distinguishes verifiable assertions from judgments about authorship. This small
source receipt is **not C2PA**, and does not claim certification or trusted
timestamping. Use a proper C2PA signing pipeline if exported photos/video need
interoperable Content Credentials.

Regression: `node tools/asset-provenance.selftest.mjs` exercises changed content,
forged credits, wrong keys, inventory drift, path traversal and symlinks.
```

### docs/ATTRIBUTION.md
```
# Project and Asset Attribution

## Project authorship

**Claude of Tanks was created, designed, and directed by Kevin B. Liu.**
Claude and Codex were development tools, not co-authors or copyright holders.
Unless a row below, an embedded notice, or a license record identifies another
author, every original repository file and asset is Copyright © 2026 Kevin B.
Liu. First-party material is covered by the root MIT License unless
[`LICENSE-POLICY.md`](../LICENSE-POLICY.md) identifies it as proprietary
Reserved Content. Reserved Content includes procedural vehicle and battlefield
source, fleet and map data, generated game assets, capture recipes, authored
media, and first-party branding.

Every selectable runtime vehicle model is original procedural geometry created
by Kevin B. Liu. Downloaded vehicle models are quarantined comparison/research
inputs, never playable geometry, and retain the attribution recorded below.

Third-party exceptions take precedence over the repository-wide Kevin B. Liu
notice. Neither project license relicenses third-party fonts, marks, shader
code, reference models, props, or other sourced work. See [`NOTICE.md`](../NOTICE.md)
for the concise repository coverage rule.

Every downloaded asset committed to this repo is recorded here (name, author,
source, license, file path). Runtime stays fully self-contained: all files are
served locally from `public/`, no CDN or network fetches in game code.

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| ABC Monument Grotesk (Regular/Medium/Bold, woff2 converted from the owner's OTF cut with fontTools, otherwise unmodified). OWNER-DIRECTED CHOICE (fonts r4, 2026-08-04) replacing Inter as the UI face — the owner supplied their own Dinamo cut; ABC Monument Grotesk is a COMMERCIAL typeface and is used here under the owner's own Dinamo license terms, NOT under this repo's asset licenses. It must not be copied out of this repo for reuse. Weight mapping via @font-face ranges: 100-400 Regular, 500-600 Medium, 700-900 Bold (UI usage floor stays 500). | Dinamo Typefaces | https://abcdinamo.com/typefaces/monument-grotesk | Commercial (Dinamo EULA, owner-held) — all rights reserved by Dinamo; not covered by the licenses in this file. | `public/fonts/abc-monument-grotesk/ABCMonumentGrotesk-{Regular,Medium,Bold}.woff2` |
| Inter variable font v4.1 — RETIRED from the live UI (fonts r4 swap to ABC Monument Grotesk, 2026-08-04; previously the UI face per the r3 owner-directed swap from Archivo, which had replaced the unobtainable Klim "Die Grotesk"). InterVariable.woff2 itself is removed from public/; Inter survives ONLY as the two ~1.5 KB wordmark subsets embedded in the brand lockups (see the brand row below), so the OFL license file stays committed. | Rasmus Andersson (The Inter Project Authors) | https://rsms.me/inter/ (release: https://github.com/rsms/inter/releases/tag/v4.1) | SIL Open Font License 1.1 | license: `public/fonts/inter/OFL.txt` (font file removed; subsets embedded in `public/brand/logo-full.svg` + `logo-full-metal.svg`) |

## Embedded open-source shader code

| Software | Author | Source | License | Files |
|---|---|---|---|---|
| FidelityFX Super Resolution 1 spatial upscaler (EASU + RCAS), adapted to Three.js `ShaderMaterial`/`EffectComposer` conventions. | Advanced Micro Devices, Inc. | https://github.com/GPUOpen-Effects/FidelityFX-FSR | MIT | `src/engine/post.ts` (copyright and MIT notice retained inline) |
| Volumetric cloud techniques ported from the clouds package of three-geospatial (2026-10-06, Clouds 2.0): the shape-altering function, the weather and media sampling (the shape and detail remaps, the density profile), the Beer shadow map's accumulation and lookup with its optical-depth tail, the multiple-scattering octaves, the powder term and the variance clipping, adapted to this project's layer uniforms, first-party weather and noise, a parabolic Earth and its own march, reprojection and shade. The noise volumes are first-party (`cloudVolumeNoise.ts`). | Shota Matsuda (Takram) | https://github.com/takram-design-engineering/three-geospatial/tree/main/packages/clouds | MIT | `src/engine/cloudShaders.ts` (copyright and MIT notice retained inline; the ported functions are marked `[ported]`) |

## Generated runtime declarations

| Software | Author | Source | License | Files |
|---|---|---|---|---|
| Cloudflare Workers runtime declarations, generated locally by `wrangler types` inside each Worker's `typecheck` and `test` scripts and gitignored since 2026-10-01 (no copy is tracked; the signaling Worker left the tree on 2026-09-29). Embedded upstream notices stay in each generated file. | Cloudflare and Microsoft Corporation | https://github.com/cloudflare/workerd/tree/main/types / https://developers.cloudflare.com/workers/wrangler/commands/#types | Apache License 2.0; copy at `LICENSES/Apache-2.0.txt` | `cloudflare/rooms/worker-configuration.d.ts`, `cloudflare/telemetry/worker-configuration.d.ts` (generated, untracked) |

This third-party license applies to the generated declarations, not to the
project's first-party code or Reserved Content.

## Open-source UI assets

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| National and territory flags (selective 4x3 SVG imports; the build includes only roster nations rather than the complete catalog). | Panayiotis Lipiridis and flag-icons contributors | https://flagicons.lipis.dev/ / https://github.com/lipis/flag-icons | MIT | npm package `flag-icons`; mapping/render adapter in `src/ui/{flagCodes,flags}.js` |
| Three.js logo mark (official icon geometry, presented in the landing-page engine credit through a CSS color mask). | three.js authors | https://github.com/mrdoob/three.js/blob/072dcccba979a47a44a44769c051793ebe800d67/files/icon.svg | MIT | `public/brand/threejs-mark.svg` |
| General Translation GT mark (official 96 px transparent export, presented only in the language-switcher attribution). | General Translation, Inc. | https://generaltranslation.com/brand/no-bg-gt-logo-dark-96.png | General Translation trademark/branding; not covered by the project license. | `public/brand/partners/general-translation.png` |

## Brand / logo set (public/brand/) — added 2026-07-31

The game logo is a hand-authored original flat-vector composition (stylized
modern MBT, side profile, original art — not based on any specific real
vehicle or third-party tank art) with the **Claude Code mascot** seated in the
commander's hatch wearing a tanker helmet. v5 (2026-08-31, owner-directed)
retains the approved v3 chamfer-top crest shield while cleaning the vehicle
into a balanced, fully contained modern-MBT silhouette: the hull is shifted
right, the bow and track loop are closed, and the vehicle uses restrained,
small-size-safe component detailing. The exposed hull side has recessed access
plates and fasteners; the turret uses an articulated cheek, roof facet, and
integrated raised bustle; and the gun is a coherent stepped assembly. The
tapered side skirt overlays the lower hull seam while remaining entirely below
the upper glacis and retaining visible road-wheel arcs. The antenna and raised,
finished flag mast terminate in visible deck mounts. It ships in
three treatments —
`logo-mark.svg` is the COLORED PRIMARY used by all game surfaces (dark steel
field #151f29, steel-blue two-tone tank, mascot #D97757, amber #f5b64b
pinstripe/pennant/dashes), `logo-mark-bw.svg` is the black-and-white sticker
treatment, and `logo-mark-metal.svg` is the embossed brushed-steel/gunmetal
badge (the only variant using gradients). `favicon.svg` is synchronized from
the metal crest; `logo-mark-simple.svg` remains the archived fat-shape
16–32 px simplification (amber band, helmet-dome commander).
The v1 steel-blue set is archived under `public/brand/v1/`, the v2 B/W
roundel set under `public/brand/v2-roundel/`.
Only the mascot glyph is a sourced asset; everything else in `public/brand/`
is first-party:

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| Claude Code mascot icon (pristine 24×24 path; `color.svg` and `default.svg` on the source CDN are byte-identical, fill `#D97757`). Used verbatim inside the brand marks via `translate(...) scale(...)` with the legs clipped below the hatch ring — the glyph geometry itself is unmodified; the helmet/goggles are drawn as separate first-party shapes layered on top. | Anthropic (Claude Code branding; icon page curated by theSVG) | https://thesvg.org/icon/claude-code (file: https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/claude-code/color.svg) | Anthropic trademark/branding, © Anthropic. Not covered by either project license; no endorsement is implied and no reuse permission is granted. Any use must comply with Anthropic's then-current trademark and brand terms. | pristine source: `public/brand/claude-code-source.svg`; composed into the v5 crest masters `public/brand/logo-mark.svg`, `logo-mark-bw.svg`, and `logo-mark-metal.svg`; synchronized into `favicon.svg`, `logo-full.svg`, `logo-full-metal.svg`, and the `index.html` boot splash by `tools/sync-brand-marks.mjs`; raster exports are `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`, `og-logo.png`, and `og-logo-transparent.png`, plus the site-root `public/favicon.ico` (16/32/48 px) and `public/apple-touch-icon.png` (180 px), both exported from `favicon.svg`; historical v1/v2/v3 sets remain archived. |
| Inter wordmark subsets inside `logo-full.svg` / `logo-full-metal.svg` (two static instances of the repo's Inter variable font — wght 800 and 700 at opsz 32 — subset to the 13 glyphs of "CLAUDE OF TANKS" with fontTools and embedded as ~1.5 KB woff2 data URIs so the lockup renders correctly standalone). | Rasmus Andersson (The Inter Project Authors) | derived from `public/fonts/inter/InterVariable.woff2` (see Inter row above) | SIL OFL 1.1 — modification/subsetting and embedding permitted; license at `public/fonts/inter/OFL.txt` | embedded in `public/brand/logo-full.svg`, `public/brand/logo-full-metal.svg` |
| Claude spark mark (verbatim 24×24 path) used as an in-game camouflage print motif — the `spark` pattern (camo r4, owner ask) stamps it across hull textures; the Claude Code mark above is likewise stamped by the `claude` pattern (camo r5: the creature IS that pattern's whole print). The Anthropic logogram briefly shipped as an `anthropic` pattern in camo r4 and was removed the same day (camo r5, owner ask). Geometry unmodified; only fill color/scale/rotation vary. | Anthropic (brand marks; paths as published by the simple-icons project) | https://github.com/simple-icons/simple-icons (`icons/claude.svg`) | Anthropic trademark/branding, © Anthropic. Same terms as the mascot row above: not covered by either project license; no reuse permission is granted, and any use must comply with Anthropic's then-current trademark and brand terms. | inline path constants `CLAUDE_SPARK_MARK` / `CLAUDE_CODE_MARK` in `src/vehicles/materials.ts` (hull painters + `src/ui/garage.ts` picker swatches) |

PNG exports are produced by `tools/brand-render.mjs` (export mode; `favicon.ico`
by its ico mode) and the og composition script; regenerate any raster from its
SVG master rather than editing pixels.

## Optional logo camouflage marks — 2026-09-20

OpenAI, X, and Gemini camouflage uses the complete official vector marks.
These trademarks belong to OpenAI, X Corp., and Google respectively and are
not licensed as first-party project artwork. Their use does not imply
endorsement. The independent Mono, Carbon, and Prism finishes are original
unbranded paint designs.

| Asset | Official source | Runtime and retained evidence |
| --- | --- | --- |
| OpenAI Blossom | [OpenAI brand guidelines](https://openai.com/brand/) | Exact black Blossom path in `src/vehicles/brandCamoMarks.ts`; official guideline SVG and SHA-256 in [brand-asset provenance](references/brand-assets/README.md). |
| X logo | [X brand toolkit](https://about.x.com/en/who-we-are/brand-toolkit) | Exact `logo.svg` path in `src/vehicles/brandCamoMarks.ts`; original vector and SHA-256 in [brand-asset provenance](references/brand-assets/README.md). The saved camo ID remains `xai` for compatibility. |
| Gemini sparkle v002 | [Google-hosted Gemini SVG](https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg) | Exact vector path and published gradient in `src/vehicles/brandCamoMarks.ts` / `brandCamoPainter.ts`; source bytes and SHA-256 in [brand-asset provenance](references/brand-assets/README.md). |

## Vehicles (public/models/tanks/) — comparison/reference assets

All playable tank geometry is authored procedurally in this repository. The
files listed below are retained only as isolated comparison inputs and license
records; no `MODEL_SOURCE` runtime row points at them, and public builds strip
candidate/reference paths.

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| Abrams M1A2 SEPv3 | dannzjs | https://sketchfab.com/3d-models/abrams-m1a2-sepv3-eb6f5560198740269507e9948376414c (obtained without login via public GitHub mirror DhruvBhargava007/Morv_AI @ Dhruv) | CC-BY-4.0 — "This work is based on \"Abrams M1A2 SEPv3\" (https://sketchfab.com/3d-models/abrams-m1a2-sepv3-eb6f5560198740269507e9948376414c) by dannzjs (https://sketchfab.com/dannzjs) licensed under CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/)" | `public/models/tanks/m1a2_sepv3_dannzjs.glb` (offline preprocess: textures downscaled 1K/512 + WebP, TurretPivot/GunPivot articulation grouping baked in; original license.txt + Sketchfab API license record + geometry notes preserved in `docs/licenses/m1a2_sepv3_dannzjs/`) |

> **Identity correction (2026-08-03):** the dannzjs asset above is a mislabeled **Leopard 2A5**, not an Abrams (owner-identified from parity renders). Authorship and CC-BY-4.0 license stand as recorded; the file remains on disk but no tank registers it — `m1a1_abrams_hc` now measures against the recovered SEPv2 drop (local-only quarantine, not this table's concern).
| Leopard 2 A6 comparison print | buh | https://sketchfab.com/buh-late (user-supplied download, batch user-drops 2026-07-28; refreshed owner GLB 2026-08-11) | CC-BY 4.0 | `public/models/tanks/leo2a6_buh.glb` — critic/reference use only. The retired source-geometry module and bake script were deleted; the playable uses `buildLeo2A6` in `src/vehicles/profiles/leopard.ts`. |

Integration verdict (harness renders `tank_closeup_modern`, `garage`,
`player_view`, `combat_firing`, icons): the sourced model decisively beats the
procedural M1A2 — recognizable SEPv3 (CROWS, CITV, bustle rack, 7 road wheels,
side skirts), turret yaw / gun pitch / recoil / camo tint / killcam all work
through `modelLoader.js`'s re-parenting path.

The per-tank source-of-truth switch is `MODEL_SOURCE` in
`src/vehicles/specs.ts`. Battle playables must resolve to `procedural`; the
GLB ingestion path in `src/vehicles/modelLoader.js` exists for isolated review
and non-battle presentation tooling, not fleet geometry.

### Evaluation record — vehicle model scouting (2026-07-27)

Allowed sources searched: poly.pizza (site search API; terms: tiger, t-34,
sherman, abrams, panther, leopard 2, t-90, is-2, panzer, ww2/military/battle
tank, mbt), kenney.nl, opengameart.org (3D art search), GitHub repo/code
search. Candidates downloaded for judging were **rejected and deleted**:

- "Tank" by Zsky — https://poly.pizza/m/7GG1xDtc8l — CC-BY 3.0 — single fused
  mesh (`Super_Tank`), no articulable turret node; stylized flat-shaded low
  poly, not recognizable as any roster tank. Trial-rendered in
  `tank_closeup_modern`; lost to the procedural M1A2.
- "Tank" by KolosStudios — https://poly.pizza/m/egcLMSGiuA — CC-BY 3.0 —
  single fused mesh (`Cube.002`), generic modern MBT shape.
- "Tank" by SomeoneUnknown — https://poly.pizza/m/1jJ50vLGCk — CC-BY 3.0 —
  single fused mesh (`Cube`), untextured toy shape. Trial-rendered in
  `tank_closeup_ww2`; lost to the procedural Tiger I.

Other findings: kenney.nl has no realistic tank packs ("Tanks" is 2D
top-down). opengameart.org's only specific real-tank assets — "tank (panzer
tiger)" by Federx (CC-BY 3.0, placeholder-textured .blend), "t-34/85" by
Lotnik (CC0, .blend), "Abrams tank" by Sketlux (CC0, Freeciv-derived .blend) —
are .blend files, not loadable by GLTFLoader and with no Blender toolchain
available for a build-time convert. GitHub searches surfaced only
World-of-Tanks model rippers (forbidden: ripped game assets).

Verdict: **procedural wins for all 8 tanks** — no candidate was recognizable
as the specific vehicle, and none had a separable turret (automatic loss).

## Environment props (public/models/props/) — downloaded 2026-07-27

All sourced from [poly.pizza](https://poly.pizza); license verified on each
asset page at download time. The original source files were baked to
vertex-colored geometry in `src/world/props-models.json`, then packed without
loss into `src/world/props-models.bin.gz` for runtime use and retired from
tracked assets on 2026-08-26. The game fetches no external model file at
runtime, and public builds no longer copy those redundant source binaries.

CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/ ·
CC-BY 3.0: https://creativecommons.org/licenses/by/3.0/ (attribution below)

| Asset | Author | Source | License | File |
|---|---|---|---|---|
| Sandbags | J-Toastie | https://poly.pizza/m/xClPIEQJdX | CC-BY 3.0 | baked runtime geometry retained; source binary retired 2026-08-26 |
| Sack Trench | Quaternius | https://poly.pizza/m/LW3jwpPfiN | CC0 1.0 | baked runtime geometry retained; source binary retired 2026-08-26 |
| Sack Trench Small | Quaternius | https://poly.pizza/m/iHyRewQQcN | CC0 1.0 | baked runtime geometry retained; source binary retired 2026-08-26 |
| Tank | Poly by Google | https://poly.pizza/m/4t0RMXCl_Ud | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Light Tank | Zsky | https://poly.pizza/m/S1jUTRmAjD | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Tank | Quaternius | https://poly.pizza/m/Dc4k4CooN3 | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Barrel | Quaternius | https://poly.pizza/m/MraIiFnpAY | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Oil Drum | Zsky | https://poly.pizza/m/TLsXd9efLC | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Hay | Quaternius | https://poly.pizza/m/Yu8TOERkpw | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Haystack | Poly by Google | https://poly.pizza/m/6LeCqyw00RK | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Fence | Quaternius | https://poly.pizza/m/U7g0Wxpt63 | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Fence | Quaternius | https://poly.pizza/m/UXmKfG81fG | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Telephone pole | Poly by Google | https://poly.pizza/m/7YIloiV4cAt | CC-BY 3.0 | baked runtime geometry retained; source binary retired 2026-08-26 |
| Barn | CreativeTrio | https://poly.pizza/m/A6UkPq33aZ | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Big Barn | Quaternius | https://poly.pizza/m/q1N3xn2SpC | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Church | CreativeTrio | https://poly.pizza/m/GHzPfvoyzX | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Church | Poly by Google | https://poly.pizza/m/6vzTphxL9w4 | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Bridge | Poly by Google | https://poly.pizza/m/9oToSb_rBKY | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Rock Large | Quaternius | https://poly.pizza/m/54jZKTAt5p | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Boulder | Poly by Google | https://poly.pizza/m/3jql0qtape- | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Pine | Quaternius | https://poly.pizza/m/igSu0cPoBz | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Pine Tree | Danni Bittman | https://poly.pizza/m/2Qo-fmVKuSG | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Dead Tree | Quaternius | https://poly.pizza/m/Mcd2zYqyww | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| WW2 Ammo box | Carwyn Pelley | https://poly.pizza/m/4QQwW16WZZT | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Debris Pile | Quaternius | https://poly.pizza/m/WrIiMMxyEP | CC0 1.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| Ruin | nha pham | https://poly.pizza/m/6eGK7_Kbswf | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |
| M939 Truck | J-Toastie | https://poly.pizza/m/y8lBpvMlim | CC-BY 3.0 | (provenance record — file removed at judging cleanup 2026-07-27) |

(Judging record appended below once the per-category screenshot verdicts are in.)

### Judging record — environment props (2026-07-27)

Method: side-by-side rendered screenshots (reference vs authored procedural) via the
screenshot harness plus custom close-up camera poses; per-category verdicts.

**KEPT (winners, files above remain in repo):**
- **Telephone pole** (Poly by Google, CC-BY 3.0) — crossarms, insulators and
  wire spans beat the plain procedural cylinder poles. Placed via
  InstancedMesh along road A (`SOURCED.poles` in src/world/props.ts).
- **Sandbag emplacements** — "Sack Trench" + "Sack Trench Small" (Quaternius,
  CC0) and "Sandbags" (J-Toastie, CC-BY 3.0). No procedural equivalent
  existed; tan bags sit naturally in the palette. InstancedMesh clusters along
  the main road and at the village plaza (`SOURCED.sandbags`).

**REJECTED after trial (procedural won; GLBs deleted from the repo, rows in
the table above record the original download for provenance):** big barn +
church (bright toy-farm palette clashed with the weathered plaster/stone
village), ruin (white fantasy colonnade, wrong material language), rocks
(red-brown palette fought the mossy-gray terrain), fence (garden-picket look
and brick-red tint), hay bale / haystack (procedural straw cones and cylinders
read better), barrels + WW2 ammo box (navy-blue / bright tints, clutter value
below procedural crates), tank wrecks + M939 truck + debris pile (intact
cartoon silhouettes never read as destroyed vehicles next to the detailed
procedural tanks), pine trees (snow-covered model, wrong biome; procedural
card trees with wind win outright), and the two broken files (Poly tank —
corrupt transforms; oil drum — off-center multi-part). Bridge segments were
sourced but never placed: the map has no water gap to justify one.

Pipeline note: winners are baked at build time to vertex-colored geometry
(`node tools/bake-props-models.mjs` → `src/world/props-models.json`,
then `node tools/pack-prop-models.mjs` → `src/world/props-models.bin.gz`). The
attributed JSON is the authoring source; the exact packed streams load only on
Battle intent and the JSON is a demand-loaded compatibility fallback.

### Evaluation record — Tiger I & Panther Ausf. G model hunt (2026-07-27, Blender pipeline available)

Candidate kept as **strong maybe** (not integrated; procedural remains source of truth):

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| tank (panzer tiger) | Federx | https://opengameart.org/content/tank-panzer-tiger | CC-BY 3.0 (stated on asset page; quoted in docs/licenses/panzer-tiger-federx-LICENSE-RECORD.txt) | candidate files DELETED at integrate cleanup 2026-07-27 (procedural Tiger stays; license record kept) |

- **Tiger I — verdict: procedural stays.** The Federx model is recognizably a
  Tiger and its running gear (interleaved road wheels, sculpted track links,
  drive sprockets, rear exhaust pair) clearly beats the procedural cylinders.
  But the hull front is a wedge-shaped prow (Tiger I is stepped/vertical), the
  upper hull carries zero greebles, and it has no usable textures — the
  distributed placeholder texture was a third-party magazine color-profile
  scan (Tiger "243", s.Pz.Abt. 503), NOT covered by Federx's CC-BY, so it was
  deleted and the kept GLB re-exported with materials stripped. Fails the
  "equal-or-better surface detail" gate vs `shots/tank_closeup_ww2.png`. Kept
  because the suspension geometry + clean 3-bone rig (bodyTank>turret>cannon
  skin joints) make it a viable donor/upgrade base if re-materialed.
- **Panther Ausf. G — verdict: procedural stays; no downloadable candidate
  exists on any account-free permissive source.** Searched: opengameart
  (panther/panzer/wehrmacht/ww2 — only the Federx Tiger exists; "Tanks and
  Trucks" by chabull is 2D PSD/PNG), poly.pizza (panther → animals only;
  panzer/tiger → same generic cartoon tanks rejected in the earlier sweep —
  MirVR `/m/5rqAPFRwLMh`, PabloLuna57 `/m/CAZeAFrhC7`, Nico `/m/41Tq_Kf0Tui`
  triaged by poster render: stylized toys, single-color, not Panthers),
  itch.io (only pack with German WW2 3D tanks, "Lowpoly Tank Pack 01", states
  no license and is $5/account-gated; no Panther anyway), GitHub repo+code
  search (no permissively-licensed Tiger/Panther meshes). Good Sketchfab
  CC-BY candidates exist but are account-gated — see report wishlist.

## Textures & HDRIs — downloaded 2026-07-27, integrated 2026-07-27

All CC0; license verified on each asset page at download time. Winners ship
from `public/textures/terrain/` (splat layers, wired via
`src/world/sourcedTextures.ts` + `src/world/terrain.ts`) and
`public/textures/buildings/` (village materials via `src/world/props.ts`).
The procedural painters remain the synchronous fallback behind the
`USE_SOURCED_*` flags in `src/world/sourcedTextures.ts`. Only the 1K
Color/NormalGL/Roughness/AmbientOcclusion maps are kept; preview PNGs and the
losing candidates were deleted.

- ambientCG asset pages each state: "Creative Commons CC0 license, making
  them free to use without attribution - even in commercial circumstances."
  (quoted from https://ambientcg.com/view?id=<AssetID> for every asset below)
- Poly Haven license page (https://polyhaven.com/license) states all assets
  are CC0 — "CC0 means absolute freedom."

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| Grass 004 (1K JPG PBR set) | ambientCG (Lennart Demes) | https://ambientcg.com/view?id=Grass004 | CC0 1.0 | public/textures/terrain/Grass004_1K-JPG_*.jpg |
| Withered Grass (1K JPG maps) | Charlotte Baglioni / Poly Haven | https://polyhaven.com/a/withered_grass | CC0 1.0 | public/textures/terrain/withered_grass_*_1k.jpg |
| Ground 071 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Ground071 | CC0 1.0 | public/textures/terrain/Ground071_1K-JPG_*.jpg |
| Ground 093C (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Ground093C | CC0 1.0 | public/textures/terrain/Ground093C_1K-JPG_*.jpg |
| Snow 010A (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Snow010A | CC0 1.0 | public/textures/terrain/Snow010A_1K-JPG_*.jpg |
| Paving Stones 046 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=PavingStones046 | CC0 1.0 | public/textures/terrain/PavingStones046_1K-JPG_*.jpg |
| Rock 058 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Rock058 | CC0 1.0 | public/textures/terrain/Rock058_1K-JPG_*.jpg |
| Rock 063 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Rock063 | CC0 1.0 | public/textures/terrain/Rock063_1K-JPG_*.jpg |
| Bricks 097 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Bricks097 | CC0 1.0 | public/textures/buildings/Bricks097_1K-JPG_*.jpg |
| Plaster 007 (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Plaster007 | CC0 1.0 | public/textures/buildings/Plaster007_1K-JPG_*.jpg (the `NormalGL-smooth` map is a first-party derivative of its normal map, 2026-10-06: the rows of blocky losses removed by periodic FFT filtering, the tile's own quiet relief in their place; the game loads it instead of `NormalGL`. The `Color-even` map is a first-party derivative of its colour map, 2026-10-07: 70 % of the broad luminance blotching taken out by a periodic FFT high-pass and the chroma pulled 80 % toward the tile's mean, its fine grain kept; the game loads it instead of `Color`) |
| Roofing Tiles 012A (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=RoofingTiles012A | CC0 1.0 | public/textures/buildings/RoofingTiles012A_1K-JPG_*.jpg |
| Planks 023A (1K JPG PBR set) | ambientCG | https://ambientcg.com/view?id=Planks023A | CC0 1.0 | public/textures/buildings/Planks023A_1K-JPG_*.jpg |
| Kloofendal 43D Clear (Pure Sky) 2K HDR | Greg Zaal / Poly Haven | https://polyhaven.com/a/kloofendal_43d_clear_puresky | CC0 1.0 | REJECTED after in-engine A/B — deleted |
| Kloofendal Overcast (Pure Sky) 2K HDR | Greg Zaal / Poly Haven | https://polyhaven.com/a/kloofendal_overcast_puresky | CC0 1.0 | REJECTED (untested runner-up) — deleted |
| Snow Field (Pure Sky) 2K HDR | Jarod Guest, Sergej Majboroda / Poly Haven | https://polyhaven.com/a/snow_field_puresky | CC0 1.0 | REJECTED (untested runner-up) — deleted |

### Judging record — texture/HDRI scouting (2026-07-27)

Judged by reading each albedo/normal at full res next to the current
procedural reference shots (shots/battlefield.png, player_view.png,
battlefield_winter.png, battlefield_urban.png). Downloaded-then-rejected
(deleted from repo): Ground 092C (dirt-mud — blurry beige albedo, lost to
Ground 071's stick-strewn brown dirt), Ground 080 (sand — trampled-beach
lumps, wrong for dunes), Plaster 002 (too clean, barely beats procedural
flat color), Roofing Tiles 013A (anthracite black, clashes with the game's
red-clay roofs), Wood Siding 009 (pale painted siding, wrong for brown
barns). Unavailable without payment (ambientCG supporter early-access, CC0
once public): Ground 102, Ground 095C.

### Integration verdict — textures & HDRIs (2026-07-27, in-engine A/B)

Judged with before/after harness renders (`battlefield`, `player_view`,
`battlefield_winter`, `battlefield_urban`, `battlefield_desert`).

- **Terrain splat layers — SOURCED KEPT** on all 4 maps (per-map layer plan in
  `src/world/sourcedTextures.ts`: verdant grass/dirt/rock, desert
  withered-grass/sand/rock63, winter snow/dirt/rock, urban
  grass/dirt/paving-stones; the mud/marsh layer stays procedural everywhere —
  its puddle/ice gloss response drives `uMarshGloss`). Near-field turf, dirt
  roads and dune grain clearly beat the painted canvases; AO is baked into
  albedo RGB and roughness packed into albedo alpha per the splat contract.
- **Building materials — SOURCED KEPT**: Plaster 007 (plaster walls), Roofing
  Tiles 012A (roofs), Planks 023A (wood barns) on all maps, Bricks 097
  replacing the fieldstone bucket on urban only. Fieldstone stays procedural
  elsewhere (the coursing painter reads better on the low village walls).
- **HDRI environment — REJECTED, procedural PMREM bake stays.** Kloofendal
  43D Clear tested live as `scene.environment` (flag machinery kept in
  `src/engine/sky.ts`): its baked-in sun cannot track the per-map sun
  azimuth/elevation that drives the CSM shadows — wrong-azimuth specular
  sheen on verdant, warm tint fighting the winter overcast preset. All three
  .hdr files deleted; the download records above stand for provenance.

### Evaluation record — WW2 roster re-scout with Blender pipeline (2026-07-27, second pass)

Targets: M4A3E8 Sherman, T-34-85, IS-2. With the Blender 5.2 headless
converter now available (`tools/blend2glb.sh`), the previously unloadable
.blend leads were converted and judged standalone (neutral 3-point-light
GLB viewer + puppeteer, same 3/4 orbit as `shots/tank_closeup_*.png`,
procedural tanks rendered in the identical harness for A/B). Candidates
judged and **rejected/deleted**:

- "T-34/85" (Rudy) by Lotnik — https://opengameart.org/content/t-3485 —
  CC0 (license line on asset page: "CC0") — converted OK (41 separable
  meshes, turret re-parentable). Upper hull/turret silhouette is genuinely
  good (hexagonal turret, cupola, ball MG), BUT the running gear is
  unmodeled — hollow track loops with a single road wheel + idler per
  side — and the export has zero materials/textures. From the dominant
  in-game side/3-4 view it loses decisively to the procedural T-34-85
  (full road wheels, textured tracks, camo, decals).
- "Tank1" by hubahuba — https://opengameart.org/content/tank1 — CC0 —
  fictional cartoon APC-like vehicle with stub mortar; not any roster
  tank. Instant loss.

Exhaustive source sweep (no viable free-direct-download candidates found):
opengameart.org keyword sweep via search scrape (tank p1+p2, sherman, m4,
t-34, t34, is-2, kv, soviet, panzer, ww2, world war) — only other
real-tank hits are CC-BY-SA/GPL ("American Tank"/"Enhanced" — license
excluded); poly.pizza (sherman: none; tank: all stylized toys, already
judged first pass); itch.io (realistic WW2 packs are paid and/or have no
stated license — forbidden; free ones are 2D/voxel); GitHub code+repo
search (only irrelevant hits / WoT rippers); BlendSwap (403 to
anonymous scraping, downloads account-gated); Kenney (no realistic
tanks). Sketchfab was NOT downloaded from (account-gated by policy);
strong CC-BY candidates recorded in the scouting report for the user.

Verdict: **procedural stays the winner for M4A3E8 Sherman, T-34-85 and
IS-2**. No files kept in `public/models/candidates/` from this pass.

### Evaluation record — modern MBT scouting pass (2026-07-27, M1A2/T-90M/Leopard 2A7)

**KEPT (winner candidate, pending integration):**

| Asset | Author | Source | License | Files |
|---|---|---|---|---|
| Abrams M1A2 SEPv3 (256.8k tris, full PBR texture set) | dannzjs | https://sketchfab.com/3d-models/abrams-m1a2-sepv3-eb6f5560198740269507e9948376414c (license re-verified live on the asset page + Sketchfab API on 2026-07-27; files obtained WITHOUT login from the public GitHub mirror DhruvBhargava007/Morv_AI @ Dhruv, which preserves the Sketchfab download bundle incl. its license.txt) | CC-BY-4.0 — attribution line required, recorded in `docs/licenses/m1a2_sepv3_dannzjs/NOTES.md` | INTEGRATED → `public/models/tanks/m1a2_sepv3_dannzjs.glb` (raw 175 MB candidate bundle deleted after the offline preprocess; license records in `docs/licenses/m1a2_sepv3_dannzjs/`) |

Judged in the standalone GLB harness against `shots/tank_closeup_modern.png`:
recognizable M1A2 SEPv3 (CROWS RWS, CITV, 7 road wheels, woodland camo),
surface detail far above procedural; turret+gun proven articulable by
mesh-name re-parenting (40° yaw proof render kept with the candidate).
Caveat for the integrate step: ~160 MB of textures must be downscaled and
the 256k-tri mesh ideally decimated.

Candidates judged and **rejected/deleted** this pass:

- "Abrams tank" by Sketlux — https://opengameart.org/content/abrams-tank —
  CC0 — Blender 2.79 file converted fine via tools/blend2glb.sh (plus
  removal of a rogue 2x2x3.6 m `Cube.003`), but all Blender-Internal
  materials export white, the barrel is comically fat, hierarchy is flat
  with unnamed parts. Loses clearly to the procedural M1A2.
- "Leopard 2A4 OTCO" by Jeyhun1985 (Sketchfab, CC-BY label, mirrored in
  ryanbourdais/Bour-Engine) — REJECTED ON PROVENANCE: model description
  says "Leopard 2A4 OTCO from War Thunder"; identical face count to a
  known WT-extraction upload. Ripped game asset — forbidden. Deleted.
- "Uralvagonzavod T-90AM" by nazidefenseforceofficial (Sketchfab, CC-BY
  label, mirrored in pratiksharan/AstraSense) — REJECTED ON PROVENANCE:
  hash-named `*_dds` game-engine textures, internal node
  "T-90M_Main_Battle_Tank.obj"; the same author's other MBTs carry
  ripper-tool texture names (`Tex_0673_0.dds`) and several pages are now
  deleted. Treated as game rips — forbidden. Deleted. (T-90MS by
  Cloostyyyk: Sketchfab page deleted, license unverifiable — skipped.)
- rtcoder/tanks-game GLTFs (21 named tanks incl. m1-abrams, leopard-2a6)
  — repo has NO license ("project-owned generated geometry" per its
  SOURCE.txt) — forbidden without a visible license; also procedural.

Source sweep for T-90M / Leopard 2A7 (exhaustive, no clean downloadable
hit): opengameart (t-90/t90/leopard/m1a2/m1a1/mbt/abrams/battle tank —
only the Sketlux Abrams and generic packs), poly.pizza API search (t-90,
leopard tank, main battle tank, military/modern tank — only stylized
generics already judged), itch.io free tag-tank (stylized/WWII only),
GitHub code search (all real hits were the rips above or unlicensed),
Kenney (none). Sketchfab downloads are account-gated by policy — best
CC-BY candidates recorded in the scouting report wishlist instead.

Verdict: **sourced wins for M1A2 Abrams (pending integration); procedural
stays the winner for T-90M and Leopard 2A7.**

## Community vehicles (public/models/tanks/community/) — 17 playable sourced tanks

Community-crawl winners (2026-07-27), integrated as PLAYABLE vehicles: garage
carousel and stats card (each carries the author credit line — CC-BY
attribution requirement), AI-drivable, random enemy rosters may include
them. Every license was verified ON the asset page at download time; the
quoted license line for each asset is preserved in
`docs/licenses/community/<slug>.LICENSE-RECORD.txt`.

| In-game vehicle (spec id) | Asset | Author | Source | License | File |
|---|---|---|---|---|---|
| Stridsvagn 103 (`strv103b`) | Stridsvagn 103 | Lukasz Wesiora (canisferus) | https://opengameart.org/content/stridsvagn-103 | CC-BY 3.0 (bundled License.txt: "CC-By 3.0 license... Copyrights Lukasz Wesiora.") | `public/models/tanks/community/strv103_wesiora.glb` (materials rebuilt as Principled BSDF from the 2012 pre-nodes .blend; textures 4096→2048 JPEG; integrated as fixed-gun casemate TD) |

Retired 2026-09-22 (repository cleanup): the Wei He T-34-85 CAD study
(`t34_85_cad`) and the Newc42 Tiger I / Panzer III Ausf. J studies
(`newc_tiger`, `newc_pziii`) left the saved fleet with their icons, anchors,
fill records, geometry packets and reference certificates. Their licence
records stay in `docs/licenses/community/` as provenance history.

Retired 2026-09-23 (hidden-fleet cleanup; owner 2026-09-22 "we shouldn't have
any hidden tanks"): the 36 remaining development-only records — the archived
WWII core hulls (`m4a3e8`, `tiger1`, `t34_85`, `is2`, `panther_g`), the
`m1a2_legacy` and `leo2a7` donors, the community study hulls (`is3`,
`pziii_konserwa`, `leichttraktor`, `tiger2`, `sherman_jumbo`, `jagdtiger`,
`jpz_e100`, `sturmtiger`, `t95`, `t30`, `is7`, `object279`, `is6b`, `is1`,
`is3_bergman`, `isu152`, `isu122s`, `comet`, `challenger_cruiser`,
`charioteer`, `m26_pershing`, `m45_patton`, `t44`, `t54`, `t72b_1987`,
`t72b3`, `merkava4`) and the two reference placeholders (`recon_tank`,
`q_heavy`) — left the saved fleet with their icons, anchors, anatomy and
marking-seat receipts, fill records, geometry packets and reference
certificates. Their licence records stay in `docs/licenses/community/` as
provenance history; the `leo2a7`, `t72b3`, `merkava4`, `jpz_e100` and
`t72b_1987` combat rows survive as unregistered donor templates in
`src/vehicles/donorSpecs.ts` for the live vehicles cloned from them.

Deleted 2026-09-25 (owner: delete the archived WWII / casemate tanks that are
not in production): the builder code of `jagdtiger`, `jpz_e100`, `sturmtiger`,
`t95`, `isu152`, `isu122s`, `m4a3e8`, `t34_85`, `is2`, `panther_g`, `tiger1`,
`tiger2`, `t30`, `sherman_jumbo`, `pziii_konserwa`, `leichttraktor` and
`q_heavy` left `src/vehicles/profiles/casemate.ts`, `profiles/ww2.ts`
(removed) and `tankFactoryCore.ts`, together with the retired ids' local-only
oracle rows in `tools/procedural-fidelity.html` and
`tools/visual-evaluator-page.html`. No tracked third-party file changed: the
licence records above stay as provenance history, and the `jpz_e100` donor
template remains the combat row `jpz_e100` is cloned from.

Integration path: `MODEL_SOURCE` community entries in `src/vehicles/specs.ts`
(parametric class-template armor/stats), generalized GLB ingestion in
`src/vehicles/modelLoader.js` (fixed-gun casemates, sibling gun nodes,
bone-rigged turrets, auto-derived yaw/pitch pivots, untextured-asset camo
painting). Icons under `public/icons/<spec id>_*.png` are DERIVATIVE RENDERS
of the models above (the CC-BY rows' attribution covers them).

Losing crawl candidates (all other `public/models/community-candidates/`
downloads) were deleted after judging; the two duplicate Stridsvagn 103
downloads were consolidated into the wesiora re-export above.

### Community wave 2 (print-model crawl, integrated 2026-07-28) — 8 more playables

Second sourcing wave (Sketchfab-mirror + Thingiverse/Printables print models,
panel-judged on re-materialed renders). Same integration rules: garage
carousel + stats credit cards, AI rosters may draw them,
license lines verified on the asset/mirror page at download time and preserved
in `docs/licenses/community/<slug>.LICENSE-RECORD.txt` (Sketchfab assets also
keep the original `license.txt` / API license snapshot alongside). Fused
single-mesh print models ship as fixed-gun TD-class vehicles.

| In-game vehicle (spec id) | Asset | Author | Source | License | File |
|---|---|---|---|---|---|
| KV-2 (`kv2`) | KV-2 heavy tank 1940 | Comrade1280 (https://sketchfab.com/comrade1280) | https://sketchfab.com/3d-models/kv-2-heavy-tank-1940-ba8b84d78c0a42038cf2eaa4210ef296 (via GitHub mirror Tsukimi125/Kaiser-Ray-Tracer, full bundle with original license.txt) | CC-BY 4.0 | `public/models/tanks/community/kv2-full-comrade1280.glb` (583k→150k tris, textures capped 2K/1K; named hull/turret/tracks/wheels nodes — turret yaw articulates) |

Wave-2 losing candidates (all other wave-2
`public/models/community-candidates/` downloads) were deleted after judging.
Notable near-miss: a CC-BY T28 by AtomicArdvark (thingiverse thing:3223947)
ships as an unassembled print plate and was dropped in favor of the T95.

### Community wave 3 (IS-series hunt, integrated 2026-07-28) — 4 more playables

Targeted Soviet heavy-line hunt (Thingiverse via archive.org mirrors +
Printables public API). Same integration rules as wave 2; print STLs were
re-assembled/normalized offline in Blender (turrets auto-seated on rings,
Hull/Turret articulation nodes preserved, re-materialed — the sources are
untextured print models — and camo-painted at load). Full provenance and
license verification per model in
`docs/licenses/community/<slug>.LICENSE-RECORD.txt`.

| In-game vehicle (spec id) | Asset | Author | Source | License | File |
|---|---|---|---|---|---|

Wave-3 losing candidates (`is2-aarontmg`, `is6-wotturret-lawrenceft`) were
deleted after judging along with the rest of
`public/models/community-candidates/`.

## Variant vehicles (public/models/tanks/community/variants/) — CC-BY 4.0 derivatives

Historical modified versions of on-disk CC-BY 4.0 base models ("variant"
sourcing route, docs/history/research/modern-roster.md Part 0). Each file is an offline
Blender re-export of the base with the modifications listed below — recorded
here per CC-BY 4.0 §3(a)(1)(B). The files are comparison candidates only;
playable combat data is registered by `src/vehicles/combatVariantSpecs.ts` and
all three live visuals are first-party procedural builds.

| In-game vehicle (spec id) | Base asset | Author | Source | License | File + modifications |
|---|---|---|---|---|---|
| M1A1 Abrams (`m1a1`) | Abrams M1A2 SEPv3 | dannzjs | https://sketchfab.com/3d-models/abrams-m1a2-sepv3-eb6f5560198740269507e9948376414c | CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/) — original license records in `docs/licenses/m1a2_sepv3_dannzjs/` | `public/models/tanks/community/variants/m1a1_dannzjs_variant.glb` — MODIFIED: SEP kit stripped (both RWS bodies incl. CROWS, mast/fin, bustle-rack extension carved; no CITV), manual cupola ring + pintle M2 .50 added; the shipped m1a1_abrams_hc's runtime fidelity fixes baked in (stovepipe/headlight-tower carves, DU cheek plates, roofline caps, GPS doghouse, deck grille panels, bore evacuator + MRS collar, fender lights, whip antennas shortened). Attribution line: "This work is based on \"Abrams M1A2 SEPv3\" by dannzjs, licensed under CC-BY-4.0 — modified (SEP kit removed, M1A1 kit added)." |
| M1A2 Abrams TUSK (`m1a1_abrams_sa`) | Abrams M1A2 SEPv3 | dannzjs | (same as above) | CC-BY 4.0 | `public/models/tanks/community/variants/m1a2_tusk_dannzjs_variant.glb` — MODIFIED: TUSK kit added (2 stacked ARAT-1 ERA tile rows on both skirts + ARAT-2 wedges forward, loader's three-sided shield with smoked-glass top, CITV pedestal, Tank Infantry Phone box, rear slat cage, belly appliqué plate) over the same baked fidelity fixes; CROWS retained. Attribution line: "…by dannzjs, licensed under CC-BY-4.0 — modified (TUSK kit added)." |
| T-90A (`t90a_2004`) | T-90 | alexxx_xarchenko | https://sketchfab.com/3d-models/t-90-9bb8af8876a6478aa92089eff058d4db (license verified via Sketchfab API record 2026-07-28: "CC Attribution", creativecommons.org/licenses/by/4.0) | CC-BY 4.0 | `public/models/tanks/community/variants/t90a_xarchenko_variant.glb` — MODIFIED: decimated 304k→148k tris, scale/ground normalized (9.53 m overall, front −Y→glTF +Z), merged by-material meshes split into hull / running-gear / turret / gun with authored TurretPivot→GunPivot articulation nodes, whip antennas compressed, untextured clay re-materialed (mid-green paint + dark gear; camo-canvas painted at runtime via `paintUntextured`). Attribution line: "This work is based on \"T-90\" by alexxx_xarchenko, licensed under CC-BY-4.0 — modified (decimated, re-materialed, turret/gun articulation split)." |

Derivative renders (icons `public/icons/m1a1_*`, `t90a_*`, `m1a2_tusk_*`,
generated 2026-07-28 by tools/genIcons.mjs) are covered by the rows above.
All three ids remain registered playables, but none loads these files or
exposes source-credit metadata as part of its runtime spec. Attribution and
the required modification indication live in this document; authoring tools
may use the files for isolated visual comparison.

### Evaluation record — Type 74 variant (2026-07-28): built, NOT shipped

The roster plans Type 74 (#24) as a variant of `stb1_haphazard` ("STB-1" by
Haphazard0587, https://www.thingiverse.com/thing:2626560, CC-BY label). The
variant WAS built (IR searchlight + .50 cal kit, turret/gun split) but is
withheld from the repo on provenance: the thing's own description presents it
as the tank "from the game World of Tanks" — the same wording that failed the
Maus recovery (thing:2329090, rejected 2026-07-28 as a WoT game rip;
CC-BY label treated as invalid). This conflicts with the earlier wave-2
clearance of the same author's T30/T95/Jagdpanzer E 100 deposits ("original
print-oriented CAD, no game-rip topology" — see
`docs/licenses/community/t30_haphazard.LICENSE-RECORD.txt`). Until the
round verifier reconciles the Haphazard0587 provenance question, no
Haphazard0587 model is used as a variant base. No STB-1-derived file ships in
`public/`; the build script + artifacts remain in the session scratchpad only.
UPDATE 2026-07-28: the Japan roster is now filled by a DIFFERENT model — the
NullOps Type 74 user drop (quarantine, see "User drops" section
and the quarantine table) — the STB-1 rejection above stands unchanged.

## User drops (integrated 2026-07-28) — 3 winners from user-supplied Sketchfab downloads

Source archives were hand-delivered by the user (batch `user-drops`,
normalized GLBs + judging renders retained under
`public/models/community-candidates/user-drops/<slug>/`). Textures
recompressed to WebP at <=2k for the shipped copies.

| Vehicle (spec id) | Author | Source | License | Shipped file | Role |
|---|---|---|---|---|---|
| Leopard 2 A6 (`leo2a4`) | buh | https://sketchfab.com/buh-late (user-supplied download) | CC-BY 4.0 | `public/models/tanks/leo2a6_buh.glb` | Retained local comparison print only. The playable is our native procedural Leopard builder; no source mesh or generated source geometry is used at runtime. |
| Type 74 (`type74`) | NullOps | https://sketchfab.com/nullops (user-supplied download) | Sketchfab Standard — QUARANTINE (below) | `public/models/tanks/community/quarantine/type74-nullops.glb` | NEW Japan tier-VIII playable (the STB-1 print base stays rejected — see the evaluation record above). Skinned rig: Tower_9 yaw / Gun_7 pitch bones. |
| C1 Ariete (`c1_ariete_preserie`) | DustyMojito | https://sketchfab.com/DustyMojito (user-supplied download) | Sketchfab Standard — QUARANTINE (below) | `public/models/tanks/community/ariete-dustymojito.glb` (retained local oracle only) | RETIRED model swap. Since 2026-08-11 the playable is an original procedural rebuild; the quarantined GLB is never registered or shipped as the vehicle. |

Other `user-drops` candidates (`m1a2-abrams`, `bergman-pack`) were not part
of this integration round — the m1a2-abrams CC-BY-NC-ND candidate is tabled
in the quarantine section below; the rest stay in `community-candidates/`
pending their own integration decisions.

REMOVED (critique round 3, content_breadth audit): the `abrams-x` candidate
directory (`abrams-x.glb` + `RENDER.png`) was deleted from the repo. It was
the one committed public/ asset with no ATTRIBUTION row and no
LICENSE-RECORD.txt: the re-exported GLB embeds no provenance (Blender I/O
generator only), no source archive remains, and the decimated mesh cannot be
face-count-matched to a Sketchfab source hone
```

### docs/AUDIO.md
```
# Audio: the sound engine and how its sounds were made

Claude of Tanks' sound is a sample-driven engine (`src/audio/`) playing
first-party sound effects and national crew radio packs that were generated
offline with ElevenLabs and then measured, selected and mastered by the tools
in `tools/audio/`. Nothing calls ElevenLabs at runtime: only the mastered
WebM/Opus files and two generated manifests ship.

This document covers the runtime design, the generation pipeline end to end,
the feedback rounds that shaped it, and how to change or extend it. Module
contracts are summarised in [ARCHITECTURE.md §3.9](ARCHITECTURE.md); provenance
and the voice cast are in [ATTRIBUTION.md](ATTRIBUTION.md#audio-publicaudio--generated-for-this-project-with-elevenlabs-no-sampled-third-party-recordings).

## What ships

| Payload | Where | Size | Loaded |
|---|---|---|---|
| 479 sound-effect assets, 851 variant files | `public/audio/sfx/<group>/<id>_<n>.webm` | 23.5 MB | per battle: the battle set at the battle phase edge, the aircraft set on first sight of an aircraft, everything else on first use |
| 13 crew radio packs × 119 lines × 1–4 takes | `public/audio/voice/<lang>/<line>_<n>.webm` | ~1.6 MB per language | only the crew's pack (every pack carries every line; nothing stands in for a missing take) |
| SFX manifest | `src/audio/sfxManifest.generated.ts` | | bundled in the lazy audio chunk |
| Voice manifest | `src/audio/voiceManifest.generated.ts` | | bundled in the lazy audio chunk |

Every sound is one of these recordings (2026-10-03). Nothing is synthesized:
no oscillator, rendered buffer or noise burst is ever heard, and a cue whose
asset is still decoding, or that the browser cannot decode (Safari before 17.4
has no WebM/Opus), is silent rather than replaced by a stand-in.
`soundAssets.selftest.mjs` fails on any `createOscillator` in `src/audio/` or
the HUD. The only generated signal left is the reverb's impulse response,
which is never heard on its own.

## Runtime

### Boot and loading

`src/audio/lazyAudio.ts` keeps the engine out of the boot bundle. The
AudioContext is created in the first user gesture; until then every call is a
no-op, so headless captures never touch audio hardware. The first click or key
press anywhere also loads the engine, so the garage's hangar and its controls
are heard before any battle (until 2026-10-02 the engine waited for the Battle
button, and the garage was silent on a first visit). The engine
(`audioEngine.ts`, a 160 kB / 52 kB gzipped lazy chunk including the manifests)
arrives after the first paint.

`assetLibrary.ts` reads the manifest, probes WebM/Opus decode with a 650-byte
embedded file, and decodes each asset on an `OfflineAudioContext` at the rate
the build chose (24 kHz for assets with almost no energy above 12 kHz, else
48 kHz; mobile caps everything at 24 kHz and keeps one variant per asset).
Crew packs decode on their own lane so the first radio call never waits behind
a battle's worth of sound effects. Sound effects share six decode slots in two
lanes: the front lane is served first, and an asset joins it when it is loaded
`{ front: true }` or the first time something asks to play it before it has
decoded (a rig's loop, an ambience bed, a report), so a sound wanted now never
waits behind banks queued for later.

At every battle phase edge, and when it is adopted after that edge has passed, the engine warms and **pins** its battle set: every
weapon report bank, the combat, occupied-hull, interface and mode sets, the
map's scene, running gear, and the roster's powertrains (the solo loader also
awaits this, bounded to 3.5 s, before the reveal; a network round passes its
lobby roster as it starts loading, and every later warm of the battle keeps the
roster it was given). Its **presence set** decodes first, in the front lane:
each powertrain's start-up and idle, the map's beds, the running gear, the
other engine bands, every loop a rig can start, then the count's tick, the
mode's opener, the hatch and the horn, so the countdown is heard from its first
frame (on Verdant with six tanks: 44 assets, 45 files, 2.1 MB of the about 670
files a cold entry queues; our idle used to decode 638th, now 7th). Each roster
hull's powertrain is resolved from its whole spec (`getVehicleSpec`, the
fleet's `getSpec`), as its rig will be: a family turns on role and weight too,
and by id alone every IFV warmed another family's bank
(`presenceFamilies.selftest.mjs` checks all 220 vehicles). Pinned
assets and live loops
are never evicted; the decoded budget (200 MB desktop, 96 MB mobile) only caps
the unpinned extras. One battle's working set is about 120–140 MB decoded on
desktop and 65–80 MB on mobile.

### Placing a sound: the voice pool

Every sample plays through `voicePool.ts`, which applies the asset's cue
profile from `soundCues.ts` (per manifest group, with per-asset overrides):

- **Space**: `world` (positioned), `hull` (attached to the occupied tank) or
  `flat` (interface, radio, beds).
- **Distance law**: `distanceAttenuationDb(distance, refM, rolloff)` plus 6 dB/km
  of excess loss. Gunfire, impacts and explosions use a compressed game-mix
  curve (weapons: reference 35 m, rolloff 0.55, so a cannon at 100 m is 5 dB
  down instead of 19, and at 400 m 12 dB instead of 33). Small clutter is
  short-ranged: props 260 m, other hulls' brakes, gears and suspension
  140–150 m, bullet impacts 120–180 m.
- **Air and terrain**: an ISO 9613 air-absorption lowpass, terrain occlusion
  from seven height samples on the line of sight (up to 9 dB and a strong
  lowpass), speed-of-sound delay beyond 18 m (Earth 343 m/s, Mars 240 m/s and
  14 dB thinner; vacuum on the Moon).
- **Own hits**: a round fired by the listener's tank (the occupied one, or the
  one being watched) is heard landing under `OWN_HIT_FOCUS`: three times the
  cue's reference distance, rolloff at most 0.55, at least 2.6 km of range and
  no HDR culling. It still arrives at the speed of sound, darkened by the air,
  from the target's bearing.
- **HDR window**: the loudest recent event sets the window top (instant attack,
  12 dB/s release). A new voice more than 18 dB below it is trimmed by half the
  excess (at most 12 dB); one more than 50 dB below is not started. The loudest
  sound always plays in full.
- **Budgets**: 32 voices on desktop, 16 on mobile, with per-asset instance caps
  and re-trigger cooldowns. When the budget is full the lowest-priority
  one-shot is stolen; loops (beds, fires) are never stolen.

### The mix

`mixer.ts` builds this graph (levels in `mixPolicy.ts`):

```
weapons, impacts, environment, vehicles ─→ world sum → snapshot lowpass/level → voice duck ─┐
own (hull engine, mechanisms), ownCombat (hull gun, interior hits) → snapshot lowpass/level ─┤
interior, cinematic, ambience (ducked under radio) ───────────────────────────────────────────┼→ body → concussion → ┐
ui, music, voice, alarm ──────────────────────────────────────────────────────────────────────────────────────────────┴→ glue → limiter → soft clip → master
```

- Gunfire and our own tank lead. Weapons (1.5) and the occupied hull's gun
  (1.6) carry a +3 dB low shelf at 110 Hz and impacts (1.3) +4 dB; our own
  engine and running gear (0.36) and the loading and turret machinery inside
  it (0.95) sit above other tanks' engines (0.31); ambience (0.18, beds
  mastered at −21 LUFS and high-passed at 90 Hz on the bus) and the interface
  (0.6, with a high-shelf cut) sit underneath. The crew radio (0.24) is heard
  over the battle: while a line plays the beds drop 10 dB and the world 4. A
  gun's echo tail sits 12 dB under its report (14 under our own), its distant
  bank 3 dB under in the crossfade, and its punch 6 dB under a cannon's
  report, 16 under an autocannon's and 19 under a machine gun's.
- The levels are measured on the master by `tools/audio-mix-balance.mjs`. Its
  first run, on deploy 169's louder engine and ambience (0.8 and 0.65), put
  the idle battle bed at −22 dBFS with a cannon at 15 m only 11.6 dB above it.
  The bed was 79 % below 200 Hz: loudness-normalised (K-weighted) beds carry
  far more rumble than they sound like, and the near cannon cannot get louder
  (the glue compressor and soft clip hold its short-term level near −10
  dBFS). Four runs later — the ambience bus high-pass, idling engines quieter
  than loaded ones, cannons keeping their close report to about 150 m, and
  the trims of the time — the bed was −27.7 dBFS, a cannon stood 17.9, 11.1
  and 7.9 dB above it at 15, 150 and 400 m, and the radio 8.4 dB under a near
  cannon.
- Then the guns became cracks (2026-10-02/03), and six more measurements
  rebuilt the mix around them. A crack is judged on its loudest 100 ms (a
  400 ms window rewards a long boom), its peak and its decay, from its arrival
  over the bed. A near crack is bounded by the master's ceiling, and its
  100 ms sits its crest (about 11 dB) under that peak, so more gun level only
  squashes it: each louder step took a near cannon's decay (its loudest 50 ms
  in the first 100 ms against 250–700 ms) from 7.1 dB to 1.5 dB, because the
  limiter flattened the crack while the echo tail, unchanged while the reports
  became peak-mastered and about 8 dB lower in loudness, passed under its
  threshold at nearly the shot's level: half a second within 2–9 dB of the
  peak is a blast. The tails came down 10 dB, the blast 4, the gun shelves 3,
  the limiter learned to release slowly, the cannon reports were re-shaped to
  decay a third faster, and the guns came back down until the limiter only
  trims the top of a near crack (the probe reads its gain reduction), with
  the bed about 4 dB lower to keep them dominant. Gates: a near
  cannon 12 dB over the bed on its loudest 100 ms with its crack peaking at
  least 22 dB over it and decaying at least 8 dB; 10 and 4 dB at 150 and
  400 m; our own gun 14 dB with a 22 dB crack; at most 40 samples at the soft
  clip's knee; the radio 6 dB under a near cannon. The final measurement (d52e45620): the bed −32.0 dBFS; a near cannon 13.6 dB over it on its loudest 100 ms, its crack peaking 24.1 dB over it and decaying 10.6 dB, held down 2.3 dB by the limiter with nothing at the clip's knee; 10.7 and 6.2 dB at 150 and 400 m; our own gun 17.2 dB with a 28.0 dB crack (3.3 dB of limiting); the radio 7.4 dB under a near cannon; the garage −31.3 dBFS.
- The glue compressor has a 12 ms attack and 2.5:1 ratio so cannon transients
  reach the limiter after it (−2.6 dBFS, 20:1, 2 ms attack, 250 ms release):
  the compressor's built-in look-ahead lets it take a crack's peak down
  smoothly, and the tanh soft clip behind it is only the last resort. A Web
  Audio compressor adds its own makeup gain ((1 / curve(0 dBFS))^0.6, +1.5 dB
  here) that cannot be switched off; a trim after the limiter takes it back
  out, or the limiter would raise everything, the bed included. Before the
  limiter the cracking guns rode the clip (a near cannon put 111 samples at
  its knee, our own gun 254), which squares a crack off into old-film grit.
- Settings channels from the Sound tab (`cot.settings.v1`, live via
  `ui:volumes`) scale the buses: master, engine, gunfire (combat), ambience,
  interface, voice. The occupied gun answers to the gunfire slider.
- Snapshots: battle, scoped (the occupied gun and engine move to an
  interior/headset spectrum, the world dulls), paused, kill-cam (live world
  ducked, cinematic bus up), spectating, garage. Pause and kill-cam end with the
  battle.
- Concussion: a heavy round through the occupied hull, or an HE burst or
  vehicle explosion within a bore-scaled radius (9 m per 100 mm, at most 16 m),
  muffles the mix and recovers over 4.5 s, with tinnitus on the strongest. The
  crew's own gun never triggers it, and a settings toggle turns it off.

### Vehicles

`vehicleAudioProfiles.ts` resolves each spec to a powertrain family —
`turbine_agt` (Abrams), `turbine_gtd` (T-80), `diesel_v12_soviet`,
`diesel_two_stroke` (Leopard 1/Chieftain/T-64 lineage), `diesel_v12_modern`,
`diesel_aircooled` (M48/M60/Merkava 1–3), `diesel_ifv`, `gasoline_v12` — plus
modifiers (turbo whistle, turbine auxiliaries, hybrid-electric drive, turret
drive type, loader kind, mass class).

`vehicleAudioModel.ts` turns speed, throttle, slope and module health into RPM,
load and gear. Manual and automatic gearboxes shift near the governor and hold
0.6–1.1 s between shifts, with a downshift band well below the lower gear's top
so a tank crawling at a shift point never hunts; turbines spool instead of
shifting. It also derives track speed (with yaw scrub), braking, skids,
landings, bumps, stalls and restarts.

`vehicleRig.ts` plays the result: idle/low/mid/high engine bands crossfaded and
pitched by RPM (an idling engine at about a third of its full-load level),
start and wind-down, light/heavy track sets per surface (earth,
hard, mud, sand, snow; water runs the mud set under a wading loop) at slow/fast
speed, squeal, skid and damaged-engine knock loops, and shift, brake,
suspension and stall one-shots. The occupied hull adds turret drive, elevation
servo, cabin hum and rattle. Remote rigs use levels of detail: own, near
(within 140–165 m, five on desktop) and far (to 900–1000 m, eight). A rig's
range hysteresis never makes a nearby tank read as our own: until 2026-10-02 an
existing rig within 25 m was promoted to the own perspective (full level,
centred, with the cabin extras).

### Weapons

`weaponAudio.ts` classifies every gun into one of eighteen report classes:
rifle and heavy machine guns, 20/25/30/40/50 mm autocannons,
90/105/120/125/130/152 mm cannons, ATGM and heavy rocket launchers, and the
AC-130's autocannon, howitzer and missiles (sound profiles refine the trim,
e.g. the BMP-3's low-pressure 100 mm, or name a class outright, as the
gunship's shells do). Each class has a close bank and a distant bank
crossfaded by range (a cannon keeps its close report to about 150 m), a gun
tail matched to the map (open, forest, urban, mountain; a machine-gun burst
gets it once per 0.22 s beat, not once per round), and for the occupied gun
in the sight an interior report. Our own gun has a dedicated report per bore
(`gun_own_medium` for 90–105 mm, `gun_own_large` for 120–125 mm,
`gun_own_heavy` for 130–152 mm, and `missile_launch_own` for launchers),
fuller and more detailed than anyone else's, as World of Tanks keeps the
player's shot apart, with the breech's recoil and run-out (`gun_recoil_mech`)
under it.

A gun report is a crack: the close reports were regenerated on 2026-10-02 and
measure 13–22 dB of crest, their loudest millisecond 4–41 ms after the onset
and at most 22 % of their body below 100 Hz (see Sound effects below). Under
each one, within the close range, plays the punch of the muzzle blast: a
recorded slam of air with the air rushing back behind it (`blast_punch_light`
under machine guns, `blast_punch_medium` under autocannons,
`blast_punch_heavy` under guns), pitched lower as the bore grows and cut after
0.22, 0.32 and 0.5 s so it weights the attack without blurring the decay. It
sits 6 dB under a cannon's report, 16 under an autocannon's and 19 under a
machine gun's (2 dB higher for our own gun); air absorption leaves only a
thud at range. Until 2026-10-03 the punch was rendered (a Friedlander pressure
pulse per bore); before that a synthesized sine sweep from about 78 to 26 Hz
sat under every cannon within 700 m, and 0.5–0.8 s of falling sine is a
trailer boom that made gunfire read as explosions. HE bursts, vehicle
explosions and penetrations of the occupied hull carry their weight in
recorded, low-passed layers (`blast_sub`, `hull_thud_sub`). Shell flybys and
near-miss cracks are timed from the shell's closest approach and muzzle
velocity.

### Your own tank: loading and machinery

Reloads play the loader's choreography (`resolveReloadCuePlan`) at the matching
reload progress, close-miked in the turret on the interior bus:

| Loader | Sequence |
|---|---|
| Manual | breech drops open, the case is thrown out, the ready-rack door slides open, a round comes out, the door shuts, the round is rammed home (a separate charge for 152 mm), the breech closes |
| Carousel autoloader | the stub is kicked out, the carousel turns, the cassette lifts, the chain rammer drives the projectile and then the charge, the breech closes |
| Bustle autoloader | the case is ejected, the next round indexes, the ram, the breech closes |
| Drum magazine | the drum turns to its first empty chamber, four rounds are fed in one by one, the drum indexes, the breech closes; between rounds of a clip, the drum turns and a round is rammed |
| Autocannon | the box latches into the feed, the belt and bolt clatter, the latch |
| Missile | the canister slides into the tube, the second one, the launcher arm swings up, the latch |

Every cycle ends in the lock that says the gun is ready. The turret drive has
a start when a real slew begins (never on a servo flicker), its electric or
hydraulic loop, and a braking clunk; the elevation servo hums. At the end of
its elevation travel the gun gives a soft strain through the mount, never more
than once in 2.5 s and with no crew call (the old "Can't depress further" was
dropped as corny).

### Hits and misses

There is no interface hit marker. A hit is confirmed the way a crew
experiences it:

- **The impact at the target.** Armour hits crossfade by range from the close
  banks (tearing metal, a heavy clang, a dull thud) into distant banks (a
  crack, knock or clang with an outdoor echo) between about 140 and 620 m, for
  every shooter. HE and HEAT add their blasts, ERA its cassettes. Our own
  rounds carry under the own-hit law above, so a penetration at 700 m is a
  distant crack two seconds after the shell lands.
- **The target going up.** A kill is the destruction itself (blast, sub-bass,
  debris, turret, cook-off), carried like our hits, with the far explosion
  layer beyond 600 m.
- **The gunner's call.** Every main-gun result is called about half a second
  after it lands, the time it takes to see it: "Penetration", "Ricochet", "No
  penetration", module and crew effects, "Target destroyed". Autocannon and
  machine-gun hits are called now and then. A main-gun miss is called too:
  "Short. Adjusting." when the round came down before the enemy it was laid on
  (the live enemy nearest the line of fire), a plain "Miss." otherwise; the
  radio can ask for a line's take by index for that.

### Aircraft and mode sounds

`aerialRig.ts` plays the aircraft of the Drone and AC-130 modes: one moving
loop placed in the listener frame (distance law, air absorption, pan, Doppler),
or an own perspective for the pilot or crew.

- **Drone.** FPV drones fly as shells, so the live shell list reaches the audio
  update. An enemy drone buzzes where it flies (loud close, gone within about
  500 m) and pitches up as it closes in. Our own spins up as it lifts off, and
  while it flies the listener rides it (`player-drone` in
  `listenerPoseRuntime.ts`): the battle is heard from the drone, our tank is
  one more vehicle heard from outside, the hull's machinery is not heard, and a
  hit on the hull is felt 10 dB down and muffled under the feed. The drone's
  motors lead (−1 dB on the own bus): a hover hum crossfades into the
  full-throttle buzz as the motors work harder (speed, climbing, correcting),
  pitched by that load, spooling up over the 2.4 s launch and sagging over the
  battery's last ten seconds; wind rises with the square of speed (high-passed
  at 150 Hz), and the link's hiss rises toward the 850 m range limit and the
  last ten seconds of battery. It cuts out in a burst of static when it
  strikes, is recalled or dies; a strike is heard up close, then the listener
  is back in the tank. Until 2026-10-02 the listener stayed in the tank, so a
  flying drone sounded like the tank's own engine with a quiet, muffled buzz
  under it.
- **AC-130.** A gunship is a roster tank pinned to its orbit; it never gets a
  tank rig. The ground hears four turboprops circling overhead, the 30 mm
  thumping (`gunship_30mm_far`) and the howitzer booming (`gunship_howitzer_far`)
  from the sky. Its crew hears the cabin: the turboprops with the airframe
  rattling and wind at the gun ports under them (`gunship_cabin_rattle_loop`),
  the 30 mm, the howitzer and the missile leaving the wing pylon inside the
  fuselage (`gunship_30mm_own`, `gunship_howitzer_own`, `gunship_missile_own`),
  the howitzer's hot case clanging onto the deck 0.45 s after each shot, the
  crew loading the howitzer by hand (breech open, `gunship_round_load`, breech
  closed; missiles arm on the pylon) and the selector arming each gun
  (`gunship_weapon_select`). The gunship's shells carry `gunship-*` sound
  profiles in `matchRuleset.ts`; until 2026-10-02 they had none, so the crew
  heard tank reports from a commander's hatch, the 180 mm guided missile played
  as a 152 mm cannon and howitzer reloads ran the hull's autoloader.
- **Mode openers.** Each mode opens on its own field sound at roll-out
  (`MODE_OPENER`, read through the `getGameMode` getter): an air-raid siren for
  the Endless Horde, a distant preparatory barrage for the Frontline Assault, a
  vault door slamming for the Juggernaut, broken radio for Infected, a foghorn
  for Turbo Ball, an armory for Gun Game and the gunship passing overhead for
  the AC-130; Realistic opens on silence and the rest on the battle horn. The
  Horde's waves come on the siren with the all-clear after them, the
  Frontline's counter-attacks and advances under the barrage, and a cache lands
  with a thud where it arrives (`cache_drop`). The Juggernaut itself (found by
  its hull, at least three times anyone else's) runs its engine bank 14 %
  deeper, lands and rams with a superheavy's mass, and its gun reports carry
  2.5 dB further, a little deeper. Gravity mode's Olympus Basin has Mars
  acoustics (sound at 240 m/s, 14 dB thinner, nothing above 3.2 kHz).
- **Gun Game.** Advancing a stage plays the weapon changeover (breech, ram or
  missile tube, latch) and the loader's call for the new round. **Infected.**
  Being turned plays a grave sting and radio interference. The drone switch
  clicks.

The aircraft set decodes on first sight of an aircraft; the Infected sting
rides every battle set.

### Environment

`environmentScenes.ts` gives each of the 33 maps a scene: a stereo bed, an
optional water or machinery layer, weighted spot sounds placed 40–380 m away at
random bearings (birds higher; mostly crows, hawks, gulls, wind, rubble and
machinery, with songbirds, bees and a distant siren among them where they
belong, and no breaking glass or car alarms; bells ring only from a map's own
towers, below), a distant-war bed in
battle, the gun tail and a procedural reverb. The beds were regenerated on
2026-10-02 without songbirds, bees, sirens or radio tones (those come as
spots), selected for an
even level across the loop seam and for body under the hiss. The garage is a
working hangar: an audible room tone (+7 dB) with tools, impact wrenches, a
hammer on a track pin, the crane chain, an air compressor, a diesel being run
up and the big door 3–14 m away.

Every control in the garage and the menus sounds (`interfaceSounds.ts`): one
delegated click listener classifies the pressed element — a tab, a tank card
(which lifts its tank into place), another list option, a toggle, a back or
close button, the primary action, any other button — and a range input sounds
on change. An element can name its sound or opt out with `data-ui-sound`. In
battle only menus and dialogs sound, and a control's own `ui:click` never
doubles the delegated sound.
Atmosphere events (artillery, flak, AA, flyovers) and destructible props
have their own assets. A flyover sounds of its era (`scene.flyovers`): the
Second World War maps fly piston fighters and twin-engine bombers
(`flyover_piston`, `flyover_bomber`: Prokhorovka's Il-2s, Shanghai's G3Ms, the
Saar's Thunderbolts and Marauders), the later ones jets; an event that names its
`aircraft` type plays that type's sound (`FLYOVER_BY_AIRCRAFT`).

**Props.** `propSounds.ts` names every kind the world builds (the inhabiting
and scenery kits, the light buildings, the sandbag stacks, the telegraph poles,
the front's AA guns, the trees) with the layers it plays at the prop, and
`propSounds.selftest.mjs` fails on a world kind it does not name. A toppled
telegraph pole cracks at the foot (`pole_snap`), its wires whip as it goes over
(`pole_wires`, 0.3 s) and it lands (`pole_fall`) 0.8 s after the crush, when the
props' hinge topple reaches the ground; lamp posts, road signs, wayside crosses
and the wind pump land on the same beat. Carts splinter (`cart_break`), straw
crunches (`straw_crush`), tents and stalls tear down (`tent_collapse`), clay jars
shatter (`pottery_smash`), the red fuel drum explodes (`fuel_drum_blast`) and a
loose drum, churn, bin, bucket, jerrycan or gas bottle a hull shoves clangs and
rolls (`can_knock`, at most once per 0.3 s). Only a plastic traffic cone is
silent, by name. The world reports these through the destructibles seam
(`prop:destroyed`): the poles' topples as `utility_pole` and the loose dressing's
knocks with `loose: true` (`props.ts` `crushProp`, `kickLooseRecord`). Until
2026-10-06 a regex chose: a haycart crushed as a car ("cart" matched /car/),
sedans, bales and tents broke as wooden crates, a steel guard post as a wooden
fence, a wooden barrel as a steel drum, and the poles and the loose dressing made
no sound at all.

**Bells.** On the six maps whose towers ring (`scene.bells`: Verdant's Orthodox
village church, Frontier's and Steinburg's churches, Glacier Pass's hospice and
chapel, the Podhale's wooden churches and belfry, Saltwind's campanile) the
ambience director tolls the nearest tower within 1.6 km every 110–240 s (the
first after 25–75 s), only after the battle has rolled out (the countdown, and
every probe that holds a battle in its pre-battle, never tolls) and only once
the HDR window has stayed under 118 dB for 25 s: a cannon within a kilometre or
two, an explosion or our own gun holds the bells. The towers come from the world's feature list (a planned building's plan
id, `church`, `onionchurch`, `chapel`, or a set piece's `landmark`, `church`,
`belfry`, `campanile`) through the `getLandmarks` option, read once per scene
when the first toll falls due. A Western toll is one to three strokes of
`bell_toll` 3.4–4.2 s apart; an Orthodox tower rings `bell_orthodox` once (the
great bell's stroke, and in one take the small bells' rhythm over its hum). The
size of the tower's bell sets its pitch (`BELL_TOWERS`): the campanile's great
bell lowest (0.78), a church 0.93, a chapel or belfry higher. Bells ride the
ambience bus, under the radio and the ambience slider.

### Crew radio

`voiceLines.ts` defines 119 lines with priority (0–4), per-line and per-group
cooldowns and staleness; `crewRadio.ts` schedules them with radio discipline:
one transmission at a time, a 0.8 s gap, a two-line queue, stale calls dropped
rather than played late. Survival calls cut anything below them, decisive
events cut situational calls, and reports (what our round did, what our
equipment just did) cut the loader's flavour, so "Penetration" never goes stale
behind "Firing". Every main-gun result is called; only flavour (firing, reload
done, allies' kills, near misses, autocannon and machine-gun results) is
probability-gated, and spot calls are throttled to one per five seconds unless
several contacts appear at once. The team's count (last tank, last enemy,
outnumbered) waits out the kill call that usually comes with it. It counts the
whole field, never what a seat can see: a solo battle's list is the field; a
network seat is sent only the hulls its team spots, so it counts the lobby
roster with the authority's deaths (`getTeamRoster`, the roster the HUD's team
tally reads; every seat is sent every destroyed hull), and only where a death is
final (`deathsAreFinal` in `src/sim/matchRuleset.ts`: no respawn, no waves). In
a respawn or wave mode, or with no roster wired, a network battle (its hulls
carry `networkVisible`) calls no side counts at all.

What the crew says for the tank's own systems and the modes (2026-10-04):

| Moment | Heard | Crew |
|---|---|---|
| Smoke volley (`auxiliary:smokeScreens`, ours within 4 m) | launcher, burst | "Smoke out" |
| Roof gun on / off (the sim's auxiliary state) | weapon-station servo / switch | "Roof gun active" (on) |
| Lights on / off | headlight relay / switch | — |
| Hydropneumatic aim engaged | suspension | "Suspension set" |
| Our drone lifts off / its battery or link gives out | spin-up / feed cut | "Drone up" / "Lost the drone" (not on a recall, a hit or our death) |
| Drone pressed while recharging | refusal | — |
| Magazine reload accepted / refused | magazine swap / refusal | "Reloading" (only when it happens) |
| Special action or an empty round refused | refusal | "Out of that type" (empty round) |
| Sensor view changed (tank sight, drone, gunship) | sight ratchet | — |
| Our gunship's weapon selected | selector | "Thirty mike-mike" / "Howitzer" / "Missile selected" |
| Our gunship's supply drop (`mode_pickup_spawned` with `by`) | cache | "Ammo crate away" / "Repair crate away" |
| Enemy on a point we hold (`mode_zone_contested`) | — | "They're contesting the point" |
| Respawn | respawn | "Back in the fight" (and the one-per-life calls re-armed) |
| Countdown (3, 2, 1, never while PREPARING holds it) | a tick each second | — |
| Rollout (once a battle; a network battle joined after its count rolls out with no cues) | mode opener, hatch, horn | "All crews, advance" |
| A reasoning medal (`service:medal` Chain of Thought or Let Me Think Step by Step), or 3 % of first shots | — | "Let me think step by step." then the gunner: "Step one: aim. Step two: fire." |

The reasoning exchange (2026-10-05, the Claude of Tanks / chain-of-thought
joke) is once a battle and never costs a real call. Both lines are priority-0
flavour that `yields`: any call of priority 1 or more cuts them. A request
waits up to 8 s for a quiet net (the radio's `quiet`: nothing queued, the last
line and its gap over), so the kill call that earned the medal goes first; the
gunner's answer is never queued — the engine speaks it only when the net is
quiet again and the commander's line was the last thing said, so an
interruption drops the punchline instead of leaving it to follow a damage
call. Both lines also keep a ten-minute cooldown on the net, and the 3 %
first-shot chance draws from its own seeded stream.

A network battle reaches the same handlers: the presentation maps the
authority's `tank_spotted` and `tank_autoflip` to solo's `tank:spotted` (the
spotting side as the viewer sees it), `player:spotted` and `tank:autoflip`, and
emits `player:reload` from the viewer's row, so spot calls, the sixth sense,
the self-right and the loading machinery work there too.

A hull's crew speaks its operating nation's language by default (en-US,
en-GB, de, ru, uk, zh, fr, sv, ja, ko, it, pl, he). **Settings → Sound →
Crew voices** offers **National crews**, or one nation's existing pack for
every tank. The shared nation dropdown shows flags and localized nation
names. Choosing a crew applies immediately and persists in the `crewVoice`
field of `cot.settings.v1` as `national` or a pack ID; resetting Sound restores
`national`. `crewVoice.ts` owns validation, resolution and legacy migration:
`english` becomes `en-US`, and `interface` becomes the currently resolved
interface-language pack once (English if unsupported). Later UI locale changes
do not change that fixed crew choice.

The engine resolves the choice at first audio initialization, on live
`ui:volumes` changes, and when the player's entity or operating nation changes
(including vehicle replacement on the same entity). Switching language stops
the old transmission and clears queued calls. While a chosen pack decodes,
the radio waits. No crew stands in for another: a take a pack lacked would be
silent, and the radio selftest fails unless every pack carries every line.
Every line runs through a live intercom chain — a 24 dB/oct 320 Hz–3.4 kHz
band, a 1.9 kHz presence peak, compression, a tanh drive, a 4.6 kHz headset
speaker roll-off, and the recorded net static (`radio_static_loop`) gated
with the line between the recorded key-up and release (`radio_key_in`,
`radio_key_out`) — measured on the live output at 77–93 % of the energy inside
300–3400 Hz and under 0.1 % above 6 kHz in every language. The release does
not chirp: the synthesized squelch it replaced let a tone fall from 1250 to
900 Hz after every line, a little boing. A damaged radio module narrows the
band, adds drive and drops syllables.

### Settings and debugging

The Sound tab (`src/ui/settings.ts`) has the six volume sliders, the crew
voices (National crews / one nation's pack), the concussion toggle and the
critical-damage heartbeat. After resume, `window.__COT_AUDIO` exposes the
context, a master PCM tap (`startTap` / `stopTap` / `readTapB64`), the sound-route
log, the sfx log (asset, start, gain, rate, distance, bus), the voice log,
the crew request log (`sayLog`: every line asked for and whether the net took
it, beside `voiceLog`, the lines actually spoken), library stats, listener, rig
and aircraft state, effective bus levels, and test hooks (`play`, `preload`,
`sayVoice`, `setEngineProbeSolo`, `forceCrewLanguage`).

## How generation worked

The hands-on guide (prompt cookbook, take scoring and failure modes, costs,
recipes) is the [audio-generation handbook](audio-generation/README.md); this
section is the record of how the shipped set was made.

Everything was generated on the owner's paid ElevenLabs Creator plan on
2026-10-02 (paid plans license generated output for commercial use under
ElevenLabs' terms). The API key is read from `ELEVENLABS_API_KEY` or a file named
by `ELEVENLABS_API_KEY_FILE` and is never written to the repository.

`tools/audio/elevenlabs.mjs` is a small client for the sound-generation,
text-to-speech, speech-to-text and Voice Library endpoints. Every response is
cached content-addressed under `~/.cache/cot-elevenlabs/{sfx,tts,stt}` (keyed by
the full request), every billed call is appended to
`~/.cache/cot-elevenlabs/ledger.jsonl` with the API's own `character-cost`, and
re-running any step with unchanged inputs spends nothing.

### Sound effects

```
sfx-catalog.mjs ──→ generate-sfx.mjs ──→ sfx-qa.mjs (measure) ──→ build-sfx.mjs (score, pick, master) ──→ public/audio/sfx + manifest
   398 entries        ~1,100 raw takes      onsets, decay, seams,     master.mjs presets, picks override
   prompt, dur,       eleven_text_to_       spectral bands,
   takes, variants    sound_v2, pcm_48000   clipping
```

1. **Catalog** (`tools/audio/sfx-catalog.mjs`). One entry per asset: id, group
   (the output directory and the runtime cue group), an original prompt, a
   duration, prompt influence, loop flag, how many raw takes to generate, how
   many variants to ship, and a mastering preset.
2. **Generation** (`generate-sfx.mjs`). Each take is a separate call to
   `eleven_text_to_sound_v2` at `pcm_48000` (stereo, 16-bit). The model has no
   seed, so the take number is part of the cache key; a run replaces an asset's
   take list in `~/.cache/cot-elevenlabs/sfx-index.json`. `--ids`, `--groups`,
   `--budget` and `--dry` control a run.
3. **Measurement** (`sfx-qa.mjs`). Per take: peak and RMS, onset count and first
   onset, decay time, spectral band shares (20–150 Hz, 150–800 Hz, 0.8–4 kHz,
   4–20 kHz), loop-seam level step and spectral match, and clipped runs. It also
   renders spectrogram contact sheets for review (`--sheets`).
4. **Selection** (`build-sfx.mjs`). Takes are scored: level, clipping, a hard
   first onset for punchy presets, exactly one onset for single-shot assets (MG
   and autocannon close reports, bullets, the radio key), loop seams for loops,
   dead-air rejection, transient anatomy for gun reports (below), low-end
   weight for distant reports and blasts (reward 20–150 Hz, penalise harsh
   highs), darkness for the interface and stingers, weight
   plus a clean steel transient for the loading machinery (and one event per
   clunk, not a rattle of them), body under the hiss for ambience beds, and
   for the punch and low layers an instant slam over within 200 ms and no
   pitched tone in the low band: a take whose 25–250 Hz content holds a
   regular pitch for 60 ms while it glides 12 % (or for 150 ms at all) is a
   falling sine, a cartoon boing, and loses (`lowToneGlide` in `pcm.mjs`). The best `variants` takes ship; an optional
   `tools/audio/sfx-picks.json` (`{ "<id>": [take, …] }`) pins specific takes. Single-shot assets are truncated after the first
   shot.
5. **Mastering** (`master.mjs`). Per preset: mono fold without phase
   cancellation, high-pass, trim, fades, a loudness target, a true-peak ceiling
   and the Opus bitrate. Loops are repaired at the seam and wrap-padded
   (`[last 4096 samples | body | first 4096]`) so `loopStart`/`loopEnd` from the
   manifest never click. Gun reports (the `gunshot` preset) are normalised on
   their true peak (−1.5 dBTP, the limiter left above it) and shaped by the
   transient designer below, and so are the punches under them (`punch`); the
   low layers under blasts (`sub`) keep only what passes a two-stage 190 Hz
   low-pass and are normalised on their peak; other close weapon sounds land at −9 LUFS
   momentary max, impacts −10, foley −14, the interface −16, ambience beds −21
   LUFS integrated.
   Assets with almost no energy above 12 kHz are stored at 24 kHz.
6. **Manifest**. `build-sfx.mjs` writes `src/audio/sfxManifest.generated.ts`
   (group, variant count, durations, channels, rate, loop points, size) and the
   incremental state `tools/audio/.sfx-manifest.json`.

**Gun reports** (2026-10-02). The owner heard firing as old film or gamey
blasts, and the files agreed: the cannon reports swelled to their loudest
60–320 ms after the shot with 25–96 % of their body below 100 Hz, several
machine-gun takes were clipped, selection rewarded exactly that low end, and
mastering normalised each crack to −9 LUFS momentary and limited it back,
squaring the peak. Now:
- range-recording prompts with a crack per calibre (below), 6–8 takes each;
- `transientAnatomy` (`pcm.mjs`) on every take: the rise to its loudest
  millisecond, the energy in its first 10 ms, its crest, its body below 100 Hz;
  `build-sfx.mjs` scores an instant rise, early energy and crest up and a late
  swell, low boom and any clipping down;
- a single-shot take that was really a burst is cut at its second report only
  when that report is within 8 dB of the first (a quieter onset is its own
  echo), and a cut that leaves under 0.25 s is skipped (fewer variants ship
  rather than a click);
- the `gunshot` preset normalises on the true peak, and a transient designer
  (`shapeTransient`, the entry's `shape: [holdMs, tauMs, floorDb]`) follows the
  take's envelope and pulls a sustained blast body down onto a decaying target
  (25–35 ms for machine guns, 30–55 ms for autocannons, 90–150 ms for tank guns,
  floors 15–26 dB under the peak) while the crack and the echo pass untouched.

**Prompt lessons.**
- Short machine-gun and autocannon prompts produced bursts. "Gunshot sound
  effect: one single…" framing, longer durations, single-shot scoring and
  first-shot truncation fixed them.
- Every prompt ends with "no music, no voices"; impacts add "very loud, with an
  immediate hard attack".
- Asked for a "deep concussive low-frequency punch … rolling outdoor echo",
  the model returns cinematic explosions that swell to their peak a tenth of a
  second or more after the shot. Range-recording prompts return cracks: "at a
  military range, recorded 30 metres beside it: instantaneous, … muzzle-blast
  crack, a hard concussive punch as the pressure wave slaps off the ground,
  then a dry echo rolling off distant hills. Realistic documentary field
  recording, not cinematic, no explosion, no rumble swell, no debris". A prompt
  may be at most 450 characters.
- Words like "ding", "chime", "beep", "bright" or "triumphant" produce exactly
  the light, jingly sounds a serious war game should not have. The interface is
  described as heavy hardware ("a heavy armoured-vehicle console push button…
  a short dull mechanical clunk with no ring") and the stingers as grave
  war-film brass and timpani with "no fanfare".

### Crew radio voices

```
crew-lines.json ─┐                    crew-voices.json
 119 lines,      ├──→ build-voices.mjs ──→ eleven_v4 TTS ──→ scribe_v2 STT check ──→ master 'voice' ──→ public/audio/voice + manifest
 13 languages,   │    (per language,       [delivery] text,     best of up to 3        −18 LUFS, 24 kHz
 deliveries ─────┘     per line, per take) stability 0.6        attempts               mono Opus
```

1. **Script** (`tools/audio/crew-lines.json`). Each line has a speaking role
   (the commander's voice, or the shared gunner/loader/driver voice), an English
   delivery direction, the American English master and one rendering per
   language. Renderings follow what each army's armoured crews actually say over
   the intercom, not literal translation: German "Brand!" for a vehicle fire
   because "Feuer" is the firing order, British "Contact, wait out", Russian
   nominative ammunition calls ("Бронебойный"), IDF clock-position contact calls,
   spelled-out numbers and no Latin acronyms where a speech engine would misread
   them.
2. **Casting** (`voice-casting.mjs`, `voice-audition.mjs`). The Voice Library is
   searched per language for native male voices without live moderation or a
   credit multiplier, and candidates are ranked toward serious, mature profiles
   (deep, calm, authoritative, narration) and away from upbeat, energetic,
   social-media or young ones. Each candidate then reads two working-register
   calls; takes are round-tripped through speech-to-text and measured for pitch
   and spectral centroid. The cast (`tools/audio/crew-voices.json`) takes the
   deepest, most authoritative clean voice as commander and a distinct, equally
   serious voice as crew.
3. **Synthesis** (`build-voices.mjs`). Every take is `eleven_v4` speech in the
   crew language with the line's delivery as a bracketed audio tag (e.g.
   `[calm, clipped] Contact front.`), stability 0.6, similarity 0.8.
4. **Verification**. Each take is transcribed with `scribe_v2` and compared to
   the script (normalised Levenshtein similarity). A transcript that repeats
   the call back to back ("HE. HE.", a stuttered restart) is held under the
   bar, since by edit distance alone a doubled short call scores 0.5. Below
   0.62 (0.34 for calls of four characters or fewer) a take is regenerated —
   three attempts by default, and because earlier attempts come from the
   cache, `--attempts 10` on the flagged lines pays only for the new ones — and
   the best is kept, a clean attempt before a repeated one. The model says a
   one- or two-word call twice on nearly every attempt, so when none passes,
   each attempt is cut at its pauses and a cut is kept when its own transcript
   reads as the script (0.75, stricter than the take bar, so a fragment of a
   longer call never passes). Takes still under 0.34 are reported for review; most
   are exact homophones the transcriber spells differently (Japanese
   装填 / 争点, 徹甲弾 / 鉄鋼弾, 奪取 / ダッシュ), which no text comparison can
   separate.
5. **Mastering**. The `voice` preset: trim, fades, −18 LUFS integrated, 24 kHz
   mono Opus at 32 kbps. The radio character is not baked in: it is the live
   intercom chain, so it can degrade with the radio module.

### Rounds

- **2026-10-02, first round.** The synthesized engine and its 111 baked files
  were replaced: 347 assets, 13 crew packs, the new engine, the Sound tab
  settings. Deployed as deploy 166.
- **2026-10-02, feedback round.** The owner reported gamey voices, too much
  sound at once, guns that were hard to hear and not bassy, inaudible garage
  ambience, and light, jingly sounds. Causes and fixes:
  - Gunfire followed a realistic inverse-distance law against constant engine,
    radio and ambience layers, and a global HDR duck lowered the whole world
    (including the cannon that triggered it) by up to 11 dB. Now a compressed
    distance curve, a per-voice HDR trim, the crew's own gun on the gunfire
    channel at full level, lower constant layers, a low shelf and a sub-bass
    layer.
  - Entry paths that skipped the solo loader left the battle set cold, so first
    shots fell back to synthesized reports; the engine now warms and pins its
    own battle set at the phase edge.
  - Density: a 32/16 voice budget, short ranges for clutter, a 0.8 s radio gap,
    probability gates on chatter, a spot-call throttle, no hover ticks, sparser
    ambient spots, and fixes for gear hunting and turret-stop / gun-limit
    clunks firing on every servo flicker.
  - The script was rewritten into a terse procedure register in all 13
    languages and recast with serious voices; the interface, stingers and light
    foley were regenerated as heavy, low, mechanical sounds, the cannon and
    blast takes re-picked for low end, and the light ambient spots (cowbells,
    buoy bells, songbirds, skylarks, tropical birds, breaking glass, car alarms)
    replaced by darker ones.
  - The garage scene got an audible room tone and indoor spot placement.
  - The speech model often doubled very short calls ("Loading. Loading",
    発射、発射) on every attempt; the voice build now detects repeats, prefers
    clean attempts and cuts takes at their pauses (36 flagged takes became 2).
- **2026-10-02, the crew's own tank.** The owner asked for a beautiful firing
  sound, the machinery inside the tank, reload, shell insertion, autoloader,
  missile, rotation and clanging sounds on the model of World of Tanks, louder
  own-tank sound and firing, better and louder ambience, garage ambience and
  interface sounds, and an end to the corny limit sounds. Generated: dedicated
  own-gun reports, the recoil and run-out, a re-prompted loading set (breech,
  case, rack, ram, charge, ammunition doors, carousel, cassette, chain rammer,
  bustle, drum rotation and drum loading, autocannon feed, missile tube,
  launcher arm, ready lock), the turret drive's start, loops and stop, the
  elevation servo, a quieter limit strain, all 24 battlefield beds and the
  garage bed, and six hangar sounds; the seven light spots no scene played
  were removed. Two bugs found by the production check of deploy 168 were
  fixed: an engine adopted after the battle phase edge never warmed its battle
  set, and an existing rig within 25 m was promoted to our own perspective.
- **2026-10-02, hit realism and the new modes.** The owner asked for hits to
  sound far more realistic, and six modes had landed on main. The interface
  hit markers were removed in favour of the impact at the target (new distant
  armour-hit banks, the own-hit law), the target's destruction and the gunner's
  calls including misses; the drone, gunship, Gun Game and Infected sounds
  were generated and wired as above.
- **2026-10-02, the drone's own sound.** The owner heard the tank's engine while
  flying the drone: the listener stayed in the hull, so the tank played as our
  own vehicle at full level with the drone's buzz 12 dB under it behind a feed
  filter. The listener now rides the drone, the tank is heard from outside, and
  the drone's motors lead with a new hover loop and wind.
- **2026-10-02, guns that crack.** The owner heard firing as old film or gamey
  blasts. Measured, the reports were explosions (above); all 16 close reports
  were regenerated and picked by transient anatomy, mastered on the true peak
  and shaped, a procedural muzzle blast went under every gun, the firing sub
  sweep was removed and a look-ahead limiter went in ahead of the soft clip.
- **2026-10-03, the AC-130 and every mode.** The owner asked for many AC-130
  sounds and custom sounds for every mode: the gunship's crew cabin, its guns
  inside and from the sky, its hand-loaded howitzer and selector, and an opener
  per mode with the Horde's siren, the Frontline's barrage and the caches.
- **2026-10-03, nothing synthesized.** The owner heard a little boing all
  through battles and found it on a listening page: the impact fallback, a
  triangle wave sweeping from about 1.2 to 2.8 kHz that played at a fixed level,
  unplaced, on every hit whose recorded impact had been culled for distance or
  by the HDR window. Every synthesized sound went with it. The fallbacks
  (shots, explosions, impacts, clicks, the engine, the loading rumble) are
  gone, and the radio's key-up, release and static, the punch under the guns,
  the low end under blasts and hull hits, the cabin alarms, the heartbeat, the
  drivetrain whines, the loading bed and the sixth-sense lamp are recordings:
  13 new assets and a release regenerated without its chirp (1,806 credits). The
  same round put the crew over the battle, added the incoming-drone call,
  silenced calls that were wrong while standing still and opened up the sight.
- **2026-10-04, the crew on top of the tank, and no stand-ins.** The owner asked
  for 
```

### docs/AUTUMN-LEAF-SPRAYS.md
```
# Autumn birch/aspen leaf sprays

Baseline `c4b3c14ac`; runtime checkpoint `99ea0b24f`. Only Autumn opts into
leaf-bearing birch/aspen atlases. Other maps retain the existing bare-twig
painter. The detailed Garage grove uses the same palette selector.

Eleven irregular branch sprays carry attached leaves with open gaps. They
replace winter twig scratches and translucent circular haze, using the same
256×256 straight-alpha RGBA storage, texture owner, mip policy, alpha cutoff,
material and shader. Near/far geometry, wind, placements, collision and
concealment records are unchanged. No new frame-loop work is introduced.

## Verification

`autumnLeafSprays.selftest.mjs` executes the actual species registry, Canvas
painters, near/far/Garage builders and material constructors. It covers exact
twig output and painter RNG for 29 opt-out maps, 12 seeded target raster pairs,
20 near/far geometry pairs, two Garage species and existing owner counts.
Geometry RNG and every attribute/index remain exact. Painter RNG intentionally
differs and is independently seeded; it does not drive tree placement.

The old seasonal-palette test still checks byte-exact alpha and RNG for its
pigment-only comparison. It removes the new leaf flag from fixture copies;
the leaf test separately covers the intentional silhouette change.

Tested cutoff coverage is 9.93–14.65% through box-averaged 16px samples, inside
a 6–18% regression envelope. Empty, solid, near-solid-with-holes, old-twig
and moved-geometry mutations fail. These CPU samples are not GPU mip readbacks.
At the production atlas seeds, mean alpha decreases from .123 to .113 for
birch and .120 to .105 for aspen; cutoff coverage can increase locally.

Eight focused tests, native TypeScript 7, strict complexity, changed-scope
Doctor and public build pass. The strengthened density-envelope test and
Doctor were repeated after its test-only change. No scanner suppression.

## Native art and cost evidence

Evidence root: `/Users/kevinliu/.codex/visualizations/2026/environment-recovery-20260907/`.
`autumn-leaf-sprays-r1.CCGXNj/native.json` records six native Metal 1440×900
High screenshots at three matched cameras: near, reverse lighting, and wide.
Root and an independent reviewer inspected all six. Recognizable leaves
replace the scribbly crowns without new rectangular edges; accepted as a
leaf-identity improvement, not a complete tree redesign. Long bare spear-like
leaders and disconnected crown clumps remain visible and need a later pass.

Only the two authenticated atlas RGBA/alpha hashes differ. Observed foliage
stays at 42 geometries, 11 materials, 7 textures, 42 instance owners,
6,243,912 attribute/instance-view bytes and 8,865,352 typed backing bytes.
Scene renderer counts match per camera: 669/674/677 geometries, 211 textures,
209 programs. All views retain 42 observed foliage submissions per frame and
the same submitted triangles. These callbacks exclude shadow paths that
bypass them; the postprocess counter is not a complete-frame draw count.

The first sequential sample has slower candidate submission-wall medians
(near 2.9→4.4ms, reverse 4.3→6.6ms, wide 3.4→7.7ms). These include driver and
scheduling time, not completed GPU time. A warmed candidate/baseline/baseline/
candidate repeat (`autumn-leaf-cost-r1.TqxMHb`) returned 6.8/3.1/6.4/6.4ms
medians. The unchanged baseline itself more than doubled, so cross-context
submission wall is unstable here. All four delivered-frame medians remain
16.7ms (p95 17.0–17.5ms). This does not prove the atlas is free to render.

A final diagnostic swapped only the two observed baseline/candidate RGBA
contents in the same candidate scene, retaining the existing ImageData,
Texture, Material, geometry and instance owners. Each balanced block excluded
120 warm-up frames after upload before observing 120 normal renders, then
restored the production candidate pixels. This deliberately controlled
override is separate from unmodified-production art/ownership evidence.

The first pixel-swap attempt (`autumn-leaf-pixel-cost-r1.6q2Yaf`) stopped at
the browser command's argument-size guard before any cost block. It retained
the source-pinned baseline and candidate RGBA captures and closed its browser
and preview. The second attempt (`autumn-leaf-pixel-cost-r2.vPV1xs`) used stdin
for lossless pixel transfer, authenticated both atlas byte hashes and completed
without errors. Source/build pins stayed unchanged, candidate pixels and full
inventory were restored, and its browser and preview closed.

The eight same-context blocks used order C/B/B/C/B/C/C/B at the same near
camera. Interpret four neighboring balanced pairs, not 960 independent runs:

| Pair | C / B submission median (ms) | C / B submission p95 (ms) | C / B frame-interval p95 (ms) |
| --- | --- | --- | --- |
| 1 | 2.8 / 2.9 | 3.0 / 3.2 | 17.5 / 17.6 |
| 2 | 3.05 / 3.0 | 7.3 / 3.9 | 19.5 / 17.5 |
| 3 | 3.0 / 2.9 | 4.2 / 3.1 | 17.4 / 17.4 |
| 4 | 7.45 / 7.7 | 8.2 / 8.4 | 17.4 / 17.0 |

The paired median differences are −0.10/+0.05/+0.10/−0.25ms, without a consistent
candidate penalty; the late slowdown persists after switching back to baseline.
Candidate pair 2 still has a worse tail. That is retained as uncertainty, not
discarded or presented as a zero-cost guarantee. This narrow texture change
has accepted art and unchanged storage/draw budgets; the sampled evidence
does not establish a repeatable median regression attributable to its pixels.

No physical mobile/Safari, forced-GC heap, whole-game FPS or global
no-performance-regression certificate is claimed by this packet.

## Integration

Preserved newer remote UI/performance commits through `85aa932da` in an isolated
merge. The shared test-suite manifest merged without conflicts; foliage runtime
and map configuration did not overlap. `autumn-leaf-integration-r1.3x6Zdd`
records passing leaf, seasonal-palette and new shot-schematic self-tests,
TypeScript 7 and a fresh public build on the integrated tree. The art and
pixel-cost captures above precede this unrelated UI merge; they were not
recaptured or relabeled as post-merge measurements.
```



### CLAUDE.md
```
# Shared project instructions

@AGENTS.md

Before integrating or publishing work, follow
[the shared-main procedure](docs/DEVELOPMENT.md#publishing-to-shared-main).
Codex and Claude use the same procedure and deployment owner.
```

### AGENTS.md
```
# claude-of-tanks - Agent Index

> Pointer index for agents working in this repo. Keep this file lean: load linked
> files on demand, prune no-op instructions, and keep generated facts inside
> `agent-docs:auto` blocks.

## Overview
<!-- agent-docs:fill:overview -->
Browser-native Three.js armored combat game. The runtime combines a fixed-step
60 Hz simulation, procedural first-party vehicle fleet, thirty battlefields,
garage/showroom presentation, bots, armor/ballistics/modules, and mobile input.
Treat current `origin/main` as active shared work: isolate broad changes in a
worktree and never stage generated tank work wholesale.

## Architecture Pointers
<!-- agent-docs:fill:architecture -->
- `docs/DEVELOPMENT.md#publishing-to-shared-main` — shared Codex/Claude integration,
  overlap review and preflight; read before integrating or publishing changes.
- `docs/ARCHITECTURE.md` — original module contracts and simulation invariants.
- `docs/AUDIO.md` — the sound engine and how its sounds were generated (ElevenLabs
  catalog, takes, selection, mastering, crew script and cast); read before changing
  `src/audio/` or regenerating sounds.
- `docs/audio-generation/README.md` — the audio-generation handbook: pipeline and
  files, the prompt cookbook (what worked and failed), take scoring and failure
  modes, costs and recipes. Begin with
  [`docs/audio-generation/SKILL.md`](docs/audio-generation/SKILL.md) before
  generating or repairing any sound or crew line.
- `docs/MULTIPLAYER-V2.md` — the peer-to-peer multiplayer: rooms Worker, wire, host, client, the cutover (§13.10).
- `docs/tank-generation/README.md` — source/markup intake, measured construction,
  prompts, quality gates and resumable tank-generation handoffs. Read before
  new source-backed tanks, family rebuilds or exact-surface geometry repairs.
  Begin with [`docs/tank-generation/SKILL.md`](docs/tank-generation/SKILL.md);
  this documentation-only directory is not discovered by the source-code index.
- `docs/tank-generation/fleet-style-performance-priority.md` — urgent open
  fleet-wide primitive/cost, switching, roller/track, chassis-closure and
  material-role work; read before adding further tank micro-detail.
- `src/main.ts` — strict typed boot, scene composition, UI flow, and render-loop
  wiring across extracted lifecycle owners; keep changes surgical.
- `src/game/stateCore.ts` — dependency-free typed session shell, event bus,
  and deterministic integration RNG.
- `src/game/state.ts` — battle roster and authoritative simulation integration.
- `src/sim/` — movement, armor, damage, spotting, and ballistics logic.
- `src/mp/` — rooms, the binary wire, transports, the match client, the browser host and the session owner.

## Stack
<!-- agent-docs:auto:stack start -->
- **Name:** claude-of-tanks
- **Package manager:** npm
- **Languages:** typescript
- **Framework:** vite
<!-- agent-docs:auto:stack end -->

## Commands
<!-- agent-docs:auto:commands start -->
- Package scripts detected: 122. Use `package.json` as the exhaustive source.
- `npm run build` - VITE_PUBLIC_BUILD=1 vite build && node tools/strip-nc-assets.mjs
- `npm run test` - node tools/run-selftests.mjs core
- `npm test` runs the pre → core → post receipt groups; a receipt whose observable inputs are
  byte-identical to its last PASS is skipped with a SKIP line (`COT_SELFTEST_CACHE=0 npm test`
  runs everything), every failure in a group is reported in one run (`COT_SELFTEST_FAIL_FAST=1`
  stops at the first), and `tank:release:check` runs its fleet probes beside the suite and the
  build after the serial scoring steps. See docs/DEVELOPMENT.md "Fast checks".
- `npm run typecheck` - node node_modules/typescript/bin/tsc -p tsconfig.json --noEmit && node tools/core-unused-check.mjs
- `npm run agent-docs` - node scripts/run-agent-docs.ts
- Keep this block compact. Put full command catalogs in a generated command index, not in AGENTS.md.
<!-- agent-docs:auto:commands end -->

## Directory index
<!-- agent-docs:auto:dirmap start -->
| Directory | Skill | Purpose |
|---|---|---|
| `api/` | [`api/SKILL.md`](api/SKILL.md) | Maintain the deprecated STUN-only ICE answer, telemetry, Jev proxy and public GitHub-count HTTP entrypoints. |
| `server/` | [`server/SKILL.md`](server/SKILL.md) | Implement and operate the match actor, the LAN room helper, collision manifests, ICE and telemetry services. |
| `src/` | [`src/SKILL.md`](src/SKILL.md) | Navigate browser boot and shared source contracts while preserving subsystem and bundle boundaries. |
| `src/app/` | [`src/app/SKILL.md`](src/app/SKILL.md) | Maintain typed application composition, lazy owner access, frame wiring, and combat warm lifecycle. |
| `src/audio/` | [`src/audio/SKILL.md`](src/audio/SKILL.md) | Work on event-driven spatial audio, radio voices, engines, weapons, ambience, and mix state. |
| `src/dev/` | [`src/dev/SKILL.md`](src/dev/SKILL.md) | Maintain opt-in diagnostics, bounded traces, deterministic shot controls, and capture readiness gates. |
| `src/docs/` | [`src/docs/SKILL.md`](src/docs/SKILL.md) | Maintain the public field manual, indexed topic pages, typed icons, and battle-reel interactions. |
| `src/engine/` | [`src/engine/SKILL.md`](src/engine/SKILL.md) | Work on renderer, lighting, camera, postprocessing, device quality, and frame diagnostics. |
| `src/fx/` | [`src/fx/SKILL.md`](src/fx/SKILL.md) | Work on pooled particles, impacts, destruction effects, decals, and shared FX time. |
| `src/gallery/` | [`src/gallery/SKILL.md`](src/gallery/SKILL.md) | Build and verify the public Tank Gallery, its technical dossiers, diagnostic overlays, and exact-surface markup review packets. |
| `src/game/` | [`src/game/SKILL.md`](src/game/SKILL.md) | Work on battle integration, bots, input, garage dressing, progression, replays, and studio state. |
| `src/presentation/` | [`src/presentation/SKILL.md`](src/presentation/SKILL.md) | Maintain lightweight public navigation, media loading, archive presentation, and public-site contracts. |
| `src/sim/` | [`src/sim/SKILL.md`](src/sim/SKILL.md) | Work on deterministic movement, armor, ballistics, damage, and spotting simulation. |
| `src/ui/` | [`src/ui/SKILL.md`](src/ui/SKILL.md) | Work on garage, HUD, settings, mobile controls, transitions, and battle presentation UI. |
| `src/vehicles/` | [`src/vehicles/SKILL.md`](src/vehicles/SKILL.md) | Work on first-party procedural tank specs, builders, materials, profiles, ordering, and asset provenance. |
| `src/world/` | [`src/world/SKILL.md`](src/world/SKILL.md) | Work on terrain, maps, collision, vegetation, props, destructibles, and world streaming. |
| `tools/` | [`tools/SKILL.md`](tools/SKILL.md) | Maintain deterministic performance, screenshot, fleet, geometry, asset, and release verification tools. |
| `tools/marketing-shots/` | [`tools/marketing-shots/SKILL.md`](tools/marketing-shots/SKILL.md) | Generate deterministic branded marketing screenshots from staged game states. |
<!-- agent-docs:auto:dirmap end -->

## Repo graph sidecar (Graphify)
<!-- agent-docs:auto:repo-graph start -->
- Use Graphify for repo topology, path/explain/affected questions, PR risk, and unfamiliar codebase orientation.
- Use `rg` for exact strings; use Kevin-Wiki `qmd` for people, tools, decisions, and compiled wiki knowledge.
- Use `agent-browser` for browser/UI work; use Playwright only for committed regression tests.
- Runtime memories (Hermes/Hindsight/Honcho) are not project truth until written back to AGENTS.md, SKILL.md, or the wiki.
- Status: `cd ~/Documents/GitHub/kevin-wiki && npm run graphify:sidecar -- status --run outputs/graphify/claude-of-tanks`
- Build from this repo: `PROJECT_ROOT="$(pwd)" && cd ~/Documents/GitHub/kevin-wiki && npm run graphify:sidecar -- build "$PROJECT_ROOT" --run outputs/graphify/claude-of-tanks --no-viz`
- Query after build: `cd ~/Documents/GitHub/kevin-wiki && npm run graphify:sidecar -- query "what should I inspect first?" --run outputs/graphify/claude-of-tanks`
- Never run Graphify installers/hooks or commit generated `graphify-out/` artifacts.
<!-- agent-docs:auto:repo-graph end -->

## Environment variables (names only)
<!-- agent-docs:auto:env start -->
- `VITE_COT_DEV_FLEET_KEY`
- `VITE_ROOMS_URL`
<!-- agent-docs:auto:env end -->

## Conventions & invariants
<!-- agent-docs:fill:conventions -->
- Runtime units are meters, seconds, and radians; tank forward is local `+Z`.
- Simulation advances at `SIM_DT = 1/60`; rendering may be variable-rate.
- Simulation randomness is seeded/injected. Do not use wall-clock time or
  `Math.random()` in authoritative logic.
- Keep simulation and network modules Node-runnable and free of DOM/WebGL.
- No per-frame allocation in established hot loops; reuse scratch state.
- All playable tanks are first-party procedural runtime models. Source GLBs
  are comparison/authoring inputs, never a playable loading path.
- Every first-party file and asset is attributed to Kevin B. Liu by
  `NOTICE.md`; every playable spec inherits the named authorship record from
  `src/authorship.ts`. Record third-party exceptions in `docs/ATTRIBUTION.md`
  and run `npm run attribution:check`.
- Every game-mode rule (gravity, speed, hull, damage, reload, ammunition, equipment,
  consumables, respawn, clock, roster split, assault escalation, score targets) lives in
  `src/sim/matchRuleset.ts`; the mode controller, `state.ts`, the authority, the HUD and the
  rule cards read that table. Never add a mode literal elsewhere.
- Both sides deploy through one function: `src/sim/deployment.ts` (each bravo slot the 180° rotation of
  its alpha slot about the anchors' midpoint), resolved on the world by `sim/matchPlacement.ts`
  `deploymentSlot`, which the authority, the browser host and the solo sim all call; the world keeps
  its spawn clearings round those slots (`deploymentClearings`). Never seat a side anywhere else.
- Objective markers (spawns, flags, zones, sectors, goals, caches) come from one derivation,
  `src/ui/minimapObjectives.ts`, and one glyph set, `src/ui/objectiveGlyphs.ts`; the HUD
  minimap and `src/game/matchModeWorldPresentation.ts` both consume them. A new objective
  gets a marker kind and a glyph there, never an ad-hoc drawing in the HUD or the world.
- Export only what another file imports: `node tools/unused-exports.mjs` lists the
  exports nothing else mentions and drives the periodic un-export passes;
  `npm run typecheck` runs the unused-locals check on the core owners. Leave
  hash-pinned sources (vehicle profiles, terrain, sky, impact decals, the authority,
  match placement) to their receipts.
- Add focused `*.selftest.mjs` coverage and include it in `npm test`.
- Any playable tank addition or geometry/profile change must run the complete
  combat-anatomy procedure: `npm run tank:anatomy:update`,
  `npm run tank:anatomy:check`, then the targeted
  `npm run tank:release:check -- --ids=<ids> --gate`. The update deliberately
  refreshes armor/module/crew receipts and all fleet technical diagrams. After
  the fleet geometry ledger rows move, re-measure the gun lines of those ids:
  `node tools/gun-junction-census.mjs --ledger=docs/geometry-gate/gun-junction.json --update --ids=<ids>`.

## Gotchas / never-do-X
<!-- agent-docs:fill:gotchas -->
- Never modify or clean the shared dirty checkout to integrate unrelated work.
- Never equate a player/entity ID with a vehicle spec ID; duplicate tank picks
  are valid in multiplayer.
- Never send hidden enemy coordinates to a client and rely on rendering to hide
  them; spotting filters snapshots before serialization.
- Never make a client authoritative for hits, damage, reloads, or match result.
- Do not import full fleet builders into a new boot-critical module.
- Do not add multicrew roles or multiple player seats inside one vehicle.
- Never deploy per commit. Git auto-deploys are disabled in `vercel.json`
  (`git.deploymentEnabled: false`, every branch); production changes
  only through the once-per-round prebuilt CLI deploy in `docs/DEPLOYS.md`
  (`vercel pull --yes --environment=production && vercel build --prod &&
  node tools/vercel-output-immutable.mjs && vercel deploy --prebuilt --prod`,
  scope `kl01s-projects`) after a green
  gate. Do not add a second gate (Ignored Build Step) or a CI deploy.

## Extending this project's agent system
<!-- agent-docs:fill:extending -->
The `agent-docs:auto` blocks come from the Agent-Docs kit in the owner's
Kevin-Wiki checkout, which is outside this repo and optional: with one,
`KEVIN_WIKI_ROOT=<checkout> npm run agent-docs -- scaffold .` refreshes them
and `-- doctor --json` checks them; without it the command exits 2 and can be
skipped. The Graphify commands above need the same checkout (read
`~/Documents/GitHub/kevin-wiki` as `$KEVIN_WIKI_ROOT`). Edit prose only below
`agent-docs:fill` markers; generated auto blocks are owned by the scaffold
command.

When a generated block lags, `package.json` wins. The Commands block predates
the current scripts: `npm test` runs `tools/run-selftests.mjs all`;
`npm run build` adds `tools/generate-localized-pages.mjs` between the Vite
build and `tools/strip-nc-assets.mjs` (after the `i18n:validate` prebuild);
`npm run typecheck` runs TypeScript 7 native (`@typescript/native`), then
`tools/core-unused-check.mjs`.
```


## Top-level structure
```
dir	.agent-docs	.agent-docs
dir	.agents	.agents
file	.env.example	.env.example
dir	.github	.github
file	.gitignore	.gitignore
file	.nvmrc	.nvmrc
file	.vercelignore	.vercelignore
file	404.html	404.html
file	AGENTS.md	AGENTS.md
file	CLAUDE.md	CLAUDE.md
file	LICENSE	LICENSE
file	LICENSE-POLICY.md	LICENSE-POLICY.md
dir	LICENSES	LICENSES
file	NOTICE.md	NOTICE.md
file	README.md	README.md
file	SKILL.md	SKILL.md
dir	api	api
dir	cloudflare	cloudflare
dir	docs	docs
file	gt-lock.json	gt-lock.json
file	gt.config.json	gt.config.json
file	index.html	index.html
file	middleware.ts	middleware.ts
file	package-lock.json	package-lock.json
file	package.json	package.json
dir	public	public
dir	scripts	scripts
dir	server	server
dir	site	site
file	skills-lock.json	skills-lock.json
dir	src	src
dir	tools	tools
file	tsconfig.json	tsconfig.json
file	vercel.json	vercel.json
file	vite.config.ts	vite.config.ts
```
