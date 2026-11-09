# stageshow

## Fetch log
- Inbox URL: https://github.com/benjitaylor/skills/tree/main/stageshow
- Final URL: https://github.com/benjitaylor/skills/tree/main/stageshow
- Fetched: 2026-11-09
- Pages: 1
- Mode: single-page

## Page — https://github.com/benjitaylor/skills/tree/main/stageshow
# stageshow (benjitaylor/skills)

Captured from GitHub directory page https://github.com/benjitaylor/skills/tree/main/stageshow

## Parent repository
- Repo: benjitaylor/skills
- Description: Skills for AI coding agents.
- Stars: 2759
- License (repo): None
- Pushed: 2026-11-05T03:34:26Z
- Skill subdirectory license: MIT (stageshow/LICENSE)

## Directory listing
- `LICENSE` (file, 1069 bytes)
- `NOTICE.md` (file, 1776 bytes)
- `README.md` (file, 3026 bytes)
- `SKILL.md` (file, 19469 bytes)
- `assets` (dir, 0 bytes)
- `examples` (dir, 0 bytes)
- `kit` (dir, 0 bytes)
- `package-lock.json` (file, 64304 bytes)
- `package.json` (file, 930 bytes)
- `playground` (dir, 0 bytes)
- `references` (dir, 0 bytes)
- `scripts` (dir, 0 bytes)
- `teaching` (dir, 0 bytes)


## package.json
```json
{
  "name": "stageshow",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "description": "The self-contained Stageshow skill, React kit, examples, and playground.",
  "license": "MIT",
  "engines": {
    "node": ">=20.19"
  },
  "scripts": {
    "dev": "node scripts/dev.mjs",
    "typecheck": "tsc --noEmit -p playground",
    "build": "vite build playground --config playground/vite.config.ts",
    "check:css": "node scripts/class-clash.mjs --bundle teaching --bundle examples/looks examples teaching"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "lucide-react": "0.468.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.1",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.7.0",
    "vite": "^6.4.5",
    "typescript": "^5.6.3",
    "playwright-core": "~1.48.2",
    "postcss": "^8.5.6"
  },
  "optionalDependencies": {
    "portless": "^0.4.1"
  }
}

```

## NOTICE.md
# Notices

Stageshow source is MIT licensed; see `LICENSE`.

Product and operating-system names, familiar device geometry, app icons, and
illustrated interfaces are used as examples. Those names and marks remain
with their owners; the Stageshow license does not grant trademark rights or
imply endorsement. Adapt examples to the product you are illustrating.

The Radix-inspired look uses publicly documented color and spacing values;
its source is identified in `examples/looks/radix.css`. The app icons in `assets/app-icons.ts` are artwork from their respective app
bundles, as identified in that file; they are not covered by the Stageshow MIT
license. They remain illustrative references to those products. The Wikipedia
study includes two local photographs dedicated under CC0 1.0 (also used
in the Finder, Telegram and annotation studies); their authors,
original source pages and modifications are recorded in
[`examples/wikipedia/PHOTOS.md`](examples/wikipedia/PHOTOS.md). Other scenes
use CSS and vector illustrations. No third-party fonts are bundled, and the
playground does not fetch fonts or photographs from external services at runtime.

The local brand registry in `kit/brands/` includes SVG artwork from SVGL (MIT), payment-icons (Apache 2.0), Cryptocurrency Icons (CC0 1.0), and official Linear, American Express and Circle assets. Per-file sources, hashes and license files are listed in [`kit/brands/SOURCES.md`](kit/brands/SOURCES.md). The original artwork and brand usage terms remain with their respective owners.

`Phone frame="photo"` is optional. Supply your own permitted bezel image via
`--ss-phone-photo-light: url(...)` and optionally `--ss-phone-photo-dark`.
Without it, the kit uses its CSS-drawn `pro` frame. No bezel photographs are
bundled.


## SKILL.md
---
name: stageshow
description: Build faux product UI that looks like a real product, as a still illustration or an animated demo with a cursor. Browser and app windows, dashboards, phones, notifications, terminals, bento grids and cursor walkthroughs, framed, masked and cropped the way a marketing page, feature card or docs hero needs them. Use whenever someone wants a fake or mocked UI, a product demo or walkthrough animation, a hero or feature-card illustration of an app, a product shot in the style of a polished marketing site, or an animated cursor doing things in an interface, even if they never say "faux UI". React and plain CSS.
metadata:
  version: 1.1.1
---

# Stageshow

Miniature product UI: a believable interface, framed in its space, as one still or a short animation in which one thing happens. The viewer recognizes the screen and sees the thing happen.

## The one idea

**It reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause.**

Five ways it fails:

- **Too much.** Real text in every row, numbers everywhere, everything packed. The more detail, the more it looks generated.
- **Wireframe.** Two gray blobs and a button. Built too small, or stripped of what made it recognizable.
- **Boxed.** A whole window shrunk into a card with even margins: a screenshot pasted in, not a product shot.
- **Flat.** Every object the same weight in the same bordered card. The eye has nowhere to land.
- **Bland.** A gray window with a cursor, whatever the brief said. The brief's look and energy (a blueprint, glass over color, a Dynamic Island, a mascot) are the point; take what it asks for and build it to the rules, as `examples/hero-demo` does with its typed popup and terminal satellite (a satellite is a smaller second object, a receipt, phone or detail card, straddling the hero's edge).

The fix: a full, structured screen in quiet grays, real words only on what the story is about, placeholder lines for the rest, room to breathe, a crop that puts the eye where the story is. Simplify the words, not the context. An empty corner, a void under a list, rows spread to fill a pane, a window floating on a plate (a backdrop or tinted field behind it): unfinished, not calm.

These are authored illustrations, not browser automation: `a.click()` draws the cursor pressing, `a.set()` changes the scene.

## How hard to press

Build it the way a product designer builds a launch page they will be judged on. The gold examples in `examples/` are the bar, not a reference: if yours is the emptier, flatter or smaller one beside the closest gold, that is the first fix. Then look at the frame the way the most exacting designer you know would, the one who screenshots the one wrong thing and sends it back with "what is this?": a dot off its avatar, a unit on its own line, a grabber under the island, copy touching a card. If you can picture that screenshot, you have found the next fix.

## Workflow

Most of the quality is decided before any code. Write the plan first: where it sits, the focal object, the action, the payoff, what can be left out.

1. **Medium and place.** Still or animation (loop, once in view, or hover). The page, its ground, its width. Design at the size it will be seen, about 720 × 340 for a hero beside copy (`hero-demo`), 900 to 1100 wide for a full-width hero (`linear`), 400 × 300 for a card, shown at 1:1; never under about 320 wide for a demo, though a bento tile or a satellite card may be smaller. Every demo that can sit in a phone column ships a `compact` design at the column's width (358), a redesign not a squeeze (`references/framing.md`, Small formats and the page). A grid of tiles is one set: plan it with `references/bento.md`.
2. **Look.** With the product's code or site at hand, map its tokens to the kit's (`references/looks.md`); if the developer asks for their own components, use them inside the stage instead of the kit's small parts. Otherwise a theme (light, dark, blueprint, glass), a palette (accent, mono) and a fidelity: `minimal` is all bars, `standard` is words where they carry meaning and bars elsewhere, `realistic` is real content everywhere. Default light, accent, standard; go realistic at hero scale, for a named real product, or a still whose subject is a list or page. Write filler once with `Text filler` and the fidelity decides. The product's own icons, its real chrome, the content that makes it recognizable. A brief with a style (kawaii, paper, a poster color) gets that style in full, still built to these rules.
3. **The story.** Its shape (`references/motion.md`, Story): how it feels to use, a flow, or what the system does. Three to five beats and a payoff, 10 to 16 seconds. No cursor move you can't explain. Data never rewinds in view without a cause. Between a richer story and a calmer frame, choose the frame.
4. **Start from an example.** Find the closest gold example (the Gold table below) and film it (`node scripts/film.mjs "<preview>/?capture=<gold>" --select '#example' --still --out gold.png`; `npm run dev` serves the preview). Copy its folder into your project as the starting point; don't rewrite it from a glance. The quickest loop: copy it to `examples/<yours>/` here, where the preview picks it up and `?capture=<yours>` films it, then move it into the host when it passes and fix its kit import path. Keep its structure: the stage size, the crop and bleed, row and type sizes, spacing, the script's beats, the kit parts. Now read `references/craft.md` in full: it is short, and it holds the still-frame rules the gold can't show you, the cases your gold doesn't happen to contain. Then replace its look and content with the brief's product: the tokens from step 2, the product's own icons, chrome and words. A copy that only changes the name is not done: it should read as the brief's product, not the gold's. If no gold tells your story, choose in two parts: the layout first (pick it from the table in `references/framing.md`; each layout names its example), and copy that example even though its story differs; then borrow the motion for your beats from the example whose story is closest, and build what neither has in the same style. Then frame it: crop to the panel the story happens in, judged in the final visible crop (`references/framing.md` has the rules and the layout table). The short form: one gutter, a full one or well past; only filler bleeds; what opens stays in; windows keep their shape; the page is the ground, so no plate under a hero on a white or dark page and no window whole with air on four sides; `unframed` only when the developer asks; no dead corners. Film one still at both widths beside the gold's; if yours is emptier, flatter or more boxed, fix the frame before any motion.
5. **The screen.** Count the real strings, usually 3 to 7 (`references/craft.md`, Restraint): a budget for words, not elements. Build with the kit's tokens, `Bar`, `Text` and `Row`. Fit every control's text before it moves. Mark what the cursor touches with `data-target` and `data-cursor`; measure with `rect()`, never hard-code.
6. **Choreograph.** The `Act` API. Keep what appears mounted and toggle it so exits animate (`Bubble` and `Fly` hand off explicitly). Animate the relationship, not just the object: a new row carries the rows below it, a surface that resizes never stretches its text. Beats overlap, groups stagger, the payoff holds, the loop ends where it began or resets with a visible cause.
7. **Rehearse.** Set `poster` first: most people see only that frame (a thumbnail, reduced motion, a screenshot), so it is the beat that tells the story on its own, never one caught mid-change, with the result left on screen rather than tidied away (`references/motion.md`, Story). Then film the loop, not just a still, and always with `--gate`: it is the same contact sheet plus the verdict, so it costs nothing extra. Film the contact sheet at the shown width and at 390, and step through every press, menu, morph and the loop seam (`references/rehearse.md`). A still can't show a pop. Read every frame, fix the largest visible fault first (framing, then hierarchy, then motion, then polish), re-film. Then hold it next to the closest gold and answer the whole-composition and style pairs in `references/teaching.md` as questions about your still (what does the eye land on first, and is it the result? is one window, tile or device clearly leading?); any no is the largest fault. Don't hand over until the loop's `--gate` ends `rehearsal passed`: every line it prints is a fault a viewer will see, even when the contact sheet looks smooth. Short on time or tool calls, fixing its lines comes before more stills, the review and the notes. Passing is necessary, not sufficient. Then run the last pass in `references/rehearse.md`: a fresh-eye review (`references/review.md`) and `REHEARSAL.md` beside the component (template in `references/verify.md`, Hand over): the gold you copied, what you changed, what you did not check.

Faults that come back every round, each with its rule; check them before handing over:

- **Content that swaps** instead of moving (`references/motion.md`, Changing text and values).
- **Gray bars where the eye lands;** filler belongs at the edges (`references/craft.md`, Restraint).
- **A plate behind the window, or a window floating** with air on four sides; the window or phone fills at least two thirds of the stage and runs off an edge (`references/framing.md`, rule 5 and Small formats and the page).
- **Empty bands, cut controls and shadows** (`references/craft.md`, Restraint; `references/framing.md`, rule 4).
- **Stock AI and made-up logos:** sparkles, purple, a letter in a colored square (`references/craft.md`, Icons and logos).
- **Busy rows and uneven insets** (`references/craft.md`, Restraint and Spacing and alignment).
- **Long holds and a reset with no cause** (`references/motion.md`, Loops).
- **A selection that isn't under the I-beam** (`references/motion.md`, Drags and selection).
- **A status bar or home indicator drawn by hand;** the Phone draws both (`references/craft.md`, Chrome and devices).
- **A centered amount centered with its sign** (`references/craft.md`, Spacing and alignment).

## Examples

Film the closest one before you start (step 4). The gold examples are the quality bar; product studies are for borrowing an interaction, never another product's identity; specimen sheets are catalogs, not compositions. Run everything with `npm install` and `npm run dev`. `teaching/` holds bad/good pairs (`references/teaching.md`) for diagnosing a problem; the bad halves are never starting points.

### Gold

| Need | Example | What to learn |
|---|---|---|
| Still or feature card | `static-card` | Quiet hierarchy, a hard crop, one satellite, real words only on the selected customer, its neighbors and the total |
| Dark still | `dark-bento` | One signal said once; album art keeps it a music app |
| Animated hero, a gesture | `hero-demo` | Five beats, named targets, an annotation, a terminal coming forward |
| Choreography, no cursor | `payout-flow` | Slow overlapping arrivals, reading time, a payoff that holds |
| Content changing in place | `choreography` | Retained tracks, soft masks, dependent timing |
| AI answer | `ai-chat` | The question sent, Thinking, the answer streaming in with its height, sources last; no sparkles, no purple |
| AI with cards | `ai-cards` | A multiple-choice card answered and kept as the record, a card of options opening in the thread, booked from its own button |
| Form validation | `form-error` | An error on the field that caused it, cleared by fixing it, then the button confirms on itself |
| Drag to reorder | `reorder` | A row lifted by its grip, the others making room, dropped into place |
| Chart scrub | `chart-scrub` | A hairline and dot that follow the pointer, the headline value rolling to the day under it |
| Edit in a table | `table-edit` | A cell edited in place, then the total it feeds rolls a beat later |
| Loading to content | `loading` | A skeleton at the content's own geometry, rows resolving top to bottom, real chrome throughout |
| Dark hero | `dark-hero` | Depth from surface steps on black, one lit color, a status that changes on its own pill |
| Live collaborators | `presence` | Each person one color everywhere, names riding their cursors, work shown in the doc's own marks |
| System story | `subscriptions` | A chip flies into a row, MRR rolls, a second scene is the reset |
| Close-up | `close-up` | One control at 1.4x with its window's chrome, the row whole, a large cursor to match |
| Many of one | `many-of-one` | A grid of one thing off every edge, one tile in focus by depth, the only one with words |
| Fade crop | `fade-crop` | A window fading out at its foot, over filler, instead of running off an edge |
| Panel over product | `panel-annotation` | A settings panel over the product's margin, one leader from the setting to what it changed |
| Overlapping windows | `overlap` | A card in front of a window, its edge on the window's sidebar line |
| Stacked cards | `stacked-cards` | Two components at one width, a small gap, the lower one off the bottom |
| Opposite corners | `opposite-corners` | A bento tile: copy bottom-left, the product hung from the top-right corner |
| Tilted stack | `tilted-stack` | A loose pile of paper, small alternating angles, only the top card has words |
| Corner chip | `corner-chip` | A small chip centered on a window's corner, half outside |
| Monochrome | `monochrome` | Other companies' products in a row, grayscale, faded at the foot |
| Row of windows | `window-row` | Sessions side by side at one height: focus by depth, neighbors cut by the stage, only filler cropped |
| Window and phone | `device-pair` | A dashboard and a lock screen telling one event; the phone straddles over margin, never over the figure |
| Related objects | `story` | An invoice, a plan, a connector, rolling totals |
| Calendar drag | `calendar` | A populated week, one focal event, a measured pickup |
| Free dragging | `freeform-drag` | Grab offset, a measured grid, a drop slot that snaps |
| Phone app | `phone-touch` | A card opens into its screen as one object, and the loop folds back |
| Dynamic Island | `dynamic-island` | One black shape, its content a separate layer |
| Messages | `messages` | Composer, typing, receipts, a bubble's lifetime |
| Cursors | `cursors`, `cursor-morph`, `cursor-resize` | Five styles, element-driven kinds, resize edges and corners, no cursor at all |
| Annotations | `annotations` | Leaders, dimensions, flows and a moving target; `references/annotations.md` |
| Feature grid | `bento` | One hero, one window, a stat, an object, a diagram |
| Dark ruled grid | `ruled-bento` | Shared rules and technical imagery |
| Consumer grid | `staggered-bento` | Offset tiles, graphic art, physical objects |
| Image-led hero grid | `hero-grid` | Different grounds and materials composed as one picture |
| Upload | `upload` | A file dragged in from the desktop, an upload row with progress that settles as a file row |
| Share | `share` | A share popover over a document: an email becomes a chip, a role menu, a person added to the list |
| Swipe | `swipe` | A phone swipe to archive: press, swipe, a throw at the finger's speed, the gap closes |

### Product studies

Recognizable products (Figma, Linear, Slack, Raycast, Finder, Spotify, Notion, Gmail, Google's apps, Office, Wikipedia, Telegram, iMessage): read `references/products.md` first. Borrow the interaction, not another product's identity.

| Need | Example | What to learn |
|---|---|---|
| Design tool | `figma` | Canvas selection, a color picker, a second cursor |
| Issue tracker | `linear` | Command menu and assignment |
| Chat | `slack` | Messages, a reaction, a thread reply |
| Launcher | `raycast` | Search and clipboard history over a blurred desktop |
| Files | `finder`, `finder-glass` | Quick Look over a file list; a file moved into a folder; the same window in frosted glass |
| Music, dark | `spotify` | A dark desktop app with album art |
| Docs and editors | `notion`, `google-docs` | A slash command; a comment and its reply |
| Email | `gmail` | Hover actions, archive, an undo toast |
| Calendar, real app | `google-calendar` | Drag to create an event, the quick-create popup |
| Office | `powerpoint`, `excel` | Slide editing; AutoSum and a chart |
| Browser page | `wikipedia` | Search suggestions in a browser |
| Phone conversations | `telegram`, `imessage` | Native chat apps on an iPhone |

### Specimen and reference sheets

Catalogs of parts and grounds, described in `references/kit.md` (Specimen sheets). Look up a part here; compose from a gold example.

| Need | Example | What to learn |
|---|---|---|
| Kit specimens | `chrome`, `phones`, `controls`, `buttons`, `cards`, `parts`, `kit-extras` | Every frame and part |
| Glass | `glass` | Frosted surfaces over a color field |
| Backgrounds | `backgrounds` | One interface over twenty grounds; `references/backgrounds.md` |
| Logos | `brand-marks` | Real marks, optically sized, on light and dark; `references/brands.md` |
| A product's look | `looks` | Type, shape and color working together |

## The kit

Copy `kit/` into the project and import from `kit/index.ts`. React, react-dom and lucide-react (for `Icon`, which `Field` and `Chip` use); each part brings its own CSS. It does the parts that are hard to get right by hand and leaves the product's look to you. `references/kit.md` has every part's props and rules; read the entries for the parts you use.

- **The stage.** `Stage`: design size and scale-to-fit, `compact`, scene state, playback, the look, the cursor. The script gets an `Act` (`set`, `wait`, `move`, `click`, `type` and the rest: `references/kit.md`, Act).
- **Frames.** `Window`, `Phone` with `LockScreen` and `Notification`, `Keyboard`, `Thread` with `Bubble`, `Stamp`, `Receipt`. Real geometry; never draw a window, device or bubble by hand.
- **Motion.** `Collapse`, `Roll`, `Swap`, `Count`, `Connector`, `Fly`, `Follow`, `States`, `Stream`, `Popover`, `Scroll`, `Camera`, `Expand`. They handle the frames a cold hand gets wrong.
- **Small parts.** `Bar`, `Text`, `Row` (every list is made of it), `Card`, `Divider`, `Avatar`, `Pin`, `Icon`, `Menu`, `Field`, `Draft`, `Button`, `Segmented`, `Toggle`, `Tabs`, `Badge`, `Chip`, `Kbd`, `BrandMark`, `Code`, `Chart`, `Toast`. Quiet starting points; restyle to the product, never reshape a kit part's geometry from outside.
- **Use the kit part, never a lookalike.** Before writing a class for a button, card, tab, avatar, field, toast, badge or shortcut, check this list: a hand-built one is where uneven padding, squeezed labels and unsized text come from. Restyle the kit part with its props and tokens instead. When a button's label or icon changes, change it on the same `Button`, which animates it; never swap in a second element (`references/motion.md`, Story).
- **`stageshow.css`**: tokens, looks, edge fades, chrome, phones, keycaps.

## The references

`references/framing.md`: the framing rules and the layout table. `references/craft.md`: the still frame (restraint, type, spacing, icons, color, chrome). `references/motion.md`: story, loops, pace, the cursor and drags. `references/verify.md`: the checklist with a you-see / you-do table. `references/rehearse.md`: how to film, and the film lines that are never intentional.


## references/
- `annotations.md`
- `backgrounds.md`
- `bento.md`
- `brands.md`
- `choreography.md`
- `craft.md`
- `framing.md`
- `kit.md`
- `looks.md`
- `motion.md`
- `products.md`
- `rehearse.md`
- `review.md`
- `teaching.md`
- `verify.md`


### references/framing.md (excerpt)
# Framing

How the screen sits in its space decides whether it reads as a product shot or a screenshot in a box. Decide the framing before building the screen: a crop needs nothing past the crop, and it sets how big the type must be. SKILL.md has the summary; the numbers are here.

## The rules

1. **One hero object, at most one or two satellites** (a receipt, a phone, a detail card) that carry the point (`examples/static-card`).
2. **Keep what identifies the product:** a title, the real chrome, the rows that give the action a reason. Logo and nav are not required; crop around the story.
3. **The medium picks the first layout:** corner bleed for a hero beside copy, pinned bottom bleed for a card or tile, a phone pinned from the top. If it doesn't hold, try a second from the table below.
4. **Crop only filler.** The payoff, the action, what the cursor touches and every real word stay whole; a list, diff or terminal may run one line off a bled bottom edge. A placeholder action the crop would slice is removed, not sliced; if the story does not fit, change the stage size or the layout. A button, chip or shadow sliced by the stage edge is the usual fault.
5. **Crop 10 to 40% of the hero off stage.** The window or phone fills at least two thirds of the stage's width and runs off an edge. Labeled controls stay whole. Shapes that read when cut (a card, a slider track, a row of avatars) run off by a third or more.
6. **The stage masks everything** (`overflow: hidden`); one rounded corner per edge. Fades are for sliding tracks, stacks and charts, and for one crop: a window fading out at its foot.
7. **Satellites straddle the hero's edge, about half outside,** never fully inside or floating apart; fully outside, tie it back with a 1px leader ending in a dot.
8. **Distinct depth:** `--ss-shadow-satellite` on a satellite sitting on the hero, `--ss-shadow-ground` for a lone surface; a hairline on light edges; the shadow on the outlined shape, never a wrapper (`examples/story`).
9. **Start flat and frontal; earn a tilt** by comparing with the straight version at final size. Depth from shadow, z-order, scale and opacity; perspective only when asked.
10. **One gutter, measured in the final crop after any wrapper.** The gutter is the hero's inset from the stage edge (the layout table gives it per layout); every other edge distance in the frame matches it. The exception is a satellite straddling in the wider column; a phone counts as a satellite.
11. **A full gutter or well 

### references/kit.md (excerpt)
# The kit, piece by piece

The reference for every part in `kit/`. SKILL.md has the map; read the entries for the parts a demo uses.

The kit is four tiers, and they are not equal:

- **The stage** (`stage.tsx`, `cursors.tsx`): the canvas, the script, the cursor, measuring and playback. Every demo is built on it.
- **Frames** (`window.tsx`, `phone.tsx`, `ios.tsx`, `messages.tsx`): windows, devices and system surfaces drawn from real geometry. Never draw these by hand: no hand-built window, phone, bubble, notification, status bar or home indicator.
- **Motion** (`motion/`): behaviors that have to hold up frame by frame. They bring motion, not a look; style what's inside them as the product does.
- **Small parts** (`parts/`, `controls/`, `code.tsx`, `chart.tsx`): quiet starting points. Restyle them to the product, or build the product's own when they don't match it.

## Specimen sheets

Catalogs of how each part behaves, one per tile, not compositions to copy. Use the scenes in SKILL.md for composition ideas, and look at any reference at the intended width before borrowing from it.

- `examples/controls/`: Field, Segmented, Toggle, Tabs, Code, Chart, a card dragged between columns with `Slot`, `Scroll`, a `Camera` push-in, and the `arrow` cursor with ripple clicks.
- `examples/glass/`: the glass theme on a window, a chip and a popover.
- `examples/brand-marks/`: the bundled payment and app artwork on light and dark surfaces; sources and licenses are in `kit/brands/SOURCES.md`.
- `examples/buttons/`: every Button variant and size, label and icon changes beside neighbors, a button in a narrow row.
- `examples/cards/`: Card padding and nested radius, a flush sectioned card, a sunken group, Divider in a card and a toolbar, Kbd in a field and a menu.
- `examples/kit-extras/`: Chip, Swap, Avatar rings, Meter tones, Menu hover, Expand, solid glyphs, BrandMark.
- `examples/parts/`: the newer parts (States, Check pending, Meter, Stream, Connector arrows, Popover and Menu, the satellite lock screen).
- `examples/looks/`: nine style studies: three invitation identities, then console, finance, canvas, conversation, research and a dimensional transfer receipt.
- `examples/chrome/` and `examples/phones/`: every window chrome and phone frame in the kit.

## The stage

### `Stage`

The canvas.

- **Size.** Design size and scale-to-fit. `compact`: a second design for narrow containers (the composition rule is in `framing.md`, Small formats and the page). A host wrapper marke

### references/rehearse.md (excerpt)
# Rehearse

A dress rehearsal: run the whole demo at real speed and watch it as the audience will, before anyone does. Read every image you make, and confirm the page you filmed runs the code you wrote. The rules the film lines enforce are in `framing.md`, `craft.md` and `motion.md`; this file is how to film and what to watch.

## Prove the still before choreography

Render the opening and the payoff at both shipping widths beside the gold at shown size; the reduced-motion poster is not the opening, and it has to work as the only frame (`motion.md`, Story). Ask the still questions in `verify.md` (Framing, Hierarchy and density), then:

- Can the viewer find the focal object and what changes before any branding or copy?
- Compare the quality (hierarchy, density, spacing, crop, material) against the gold, separately from whether every object in the brief is present.
- Do the same for the busiest mid-story frame and every resting state that changed. A clean tool report does not close a composition question.

## The host's own controls

A demo lives in a page with a picker, playback buttons and labels, and those get judged too. `scripts/layout.mjs` checks ordinary UI outside a Stage, including a bento tile's inner crop (`nested-composition-crop`):

```sh
node scripts/layout.mjs "<url>/?example=hero-demo" --select .pg --width 390 --report shots/host-layout.json --screenshot shots/host-layout.png --strict
```

Run it on the viewer page, the direct scene route and the real destination page at its real width. Moving geometry is reported as incomplete, not passed. Watch each control at rest, hover in and out, pressed, focused, label changed and interrupted mid-transition; geometry cannot vouch for text rendering, focus styling or a filtered silhouette.

## Film

`scripts/film.mjs` opens a page in headless Chrome and shoots the stage at a fixed interval into one contact sheet at true size. It prints console and `[stageshow]` warnings (loop seams, missing targets); `--help` li

## scripts/
- `browser.mjs`
- `class-clash-core.mjs`
- `class-clash.mjs`
- `dev.mjs`
- `film-checks.mjs`
- `film.mjs`
- `jumps-core.mjs`
- `jumps.mjs`
- `layout-core.mjs`
- `layout.mjs`
- `motion-watch.mjs`
- `verification.mjs`


## kit/
- `act.ts` (file)
- `brands` (dir)
- `chart.css` (file)
- `chart.tsx` (file)
- `clock.ts` (file)
- `code.css` (file)
- `code.tsx` (file)
- `controls` (dir)
- `cursor.css` (file)
- `cursor.tsx` (file)
- `cursors.tsx` (file)
- `ease.ts` (file)
- `index.ts` (file)
- `ios.css` (file)
- `ios.tsx` (file)
- `keys.css` (file)
- `keys.tsx` (file)
- `looks.ts` (file)
- `measure.ts` (file)
- `messages.css` (file)
- `messages.tsx` (file)
- `motion` (dir)
- `parts` (dir)
- `phone.css` (file)
- `phone.tsx` (file)
- `reduced-motion.ts` (file)
- `stage.css` (file)
- `stage.tsx` (file)
- `stageshow.css` (file)
- `util.ts` (file)
- `window.css` (file)
- `window.tsx` (file)


## examples/ (names)
- ai-cards
- ai-chat
- annotations
- backgrounds
- bento
- brand-marks
- buttons
- calendar
- cards
- chart-scrub
- choreography
- chrome
- close-up
- controls
- corner-chip
- cursor-morph
- cursor-resize
- cursors
- dark-bento
- dark-hero
- device-pair
- dynamic-island
- excel
- fade-crop
- figma
- finder-glass
- finder
- form-error
- freeform-drag
- glass
- gmail
- google-calendar
- google-docs
- hero-demo
- hero-grid
- imessage
- kit-extras
- linear
- loading
- looks
- many-of-one
- messages
- monochrome
- notion
- opposite-corners
- overlap
- panel-annotation
- parts
- payout-flow
- phone-touch
- phones
- powerpoint
- presence
- raycast
- reorder
- ruled-bento
- share
- slack
- spotify
- stacked-cards
- staggered-bento
- static-card
- story
- subscriptions
- swipe
- table-edit
- telegram
- tilted-stack
- upload
- wikipedia
- window-row

