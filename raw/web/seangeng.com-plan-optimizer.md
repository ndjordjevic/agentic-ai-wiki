# seangeng.com-plan-optimizer

## Fetch log
- Inbox URL: https://seangeng.com-plan-optimizer/freebies/plan-optimizer
- Final URL: https://seangeng.com-plan-optimizer/freebies/plan-optimizer
- Fetched: 2026-06-12
- Pages: 4
- Mode: standard

## llms.txt — https://seangeng.com-plan-optimizer/llms.txt
# Sean Geng

> Frontend components, rendering experiments, and short writeups by Sean Geng — co-founder & CTO at B3. The good parts, left out in the open.

Sean Geng is co-founder & CTO at B3 (building a crypto agent and decentralized inference), previously an engineering leader at Coinbase. This site collects production-grade frontend components, short technical writeups, and free copy-paste tools.

Every writeup is available as Markdown at https://seangeng.com-plan-optimizer/writing/<slug>.md, and all of them concatenated at https://seangeng.com-plan-optimizer/llms-full.txt.

## Writing
- [A skill that iterates on a plan until it stops improving](https://seangeng.com-plan-optimizer/writing/iterate-a-plan-until-it-stops-improving): Treat planning as a search problem: generate a plan, score it against a rubric, critique it, rewrite it, keep the best, and stop when the score plateaus. A downloadable Claude Code skill that hardens any plan — project, code migration, research — and tells you when more iteration is just noise.
- [Building a liquid-metal UI kit for React](https://seangeng.com-plan-optimizer/writing/building-a-liquid-metal-ui-kit): Argent is Glacé's metal sibling: chrome, gold, and gunmetal surfaces that ripple like mercury. Why CSS couldn't fake this one, how a WebGL shader becomes a component kit, the browser's secret WebGL context cap, and writing my own shader to escape a license.
- [Building a liquid-glass UI kit for the web](https://seangeng.com-plan-optimizer/writing/building-a-liquid-glass-ui-kit): Glacé is a small React kit where the glass actually refracts — the edges bend the backdrop like a real lens, not just blur it. Here's the technique (displacement maps, per-element filters, edge profiles), the bugs along the way, and the honest caveats.
- [Building agents that live in your messages](https://seangeng.com-plan-optimizer/writing/building-agents-that-live-in-your-messages): Agents feel best inside the apps you already text in — iMessage, Telegram, WhatsApp, Slack. But iMessage gives you no buttons, and a Slack bot has to juggle many users and orgs at once. Two very different engineering problems, one goal: make the agent feel like a person. How to architect both, with the gotchas.
- [The honest guide to LLM model routing](https://seangeng.com-plan-optimizer/writing/the-honest-guide-to-llm-routing): Auto-routing picks a cheap model for easy prompts and a frontier model for hard ones — automatically. The papers claim 85–98% savings. An independent benchmark found a commercial router doing worse than no routing at all. The real number is ~20–25%, and here's exactly why.
- [Turning WebGL into ASCII, every frame](https://seangeng.com-plan-optimizer/writing/ascii-text-from-webgl): A three.js plane rendered to a hidden canvas, then read pixel-by-pixel and rewritten as ASCII characters in a <pre>. The trick is sampling the render at one pixel per glyph. From B3's ai-arena.
- [A loading bar that lurches like a real one](https://seangeng.com-plan-optimizer/writing/a-laser-beam-loading-bar): Real loads stutter — a burst, a pause, a crawl at the end. This pure-CSS laser beam fakes that with a hand-tuned width track and two offset flickering glows. No JS. Pulled from basement.fun.
- [A game cartridge card, in flat CSS](https://seangeng.com-plan-optimizer/writing/a-2d-cartridge-card): A 2D cartridge card with molded-plastic edges, built from one clip-path polygon stacked four times. No 3D, no canvas — just layered shapes, a noise texture, and a luminance-aware accent. Pulled from basement.fun.
- [Read the recon list as a defense checklist](https://seangeng.com-plan-optimizer/writing/what-your-email-reveals): A list of email and social OSINT tools made the rounds framed for phishing. Flip it: the same tools are what an attacker runs before a targeted email, so run them on yourself first. What your address leaks, and how to shut it down.
- [Ordered dithering and a CRT mask, on a canvas](https://seangeng.com-plan-optimizer/writing/ordered-dithering-and-a-crt-mask): A Bayer 4×4 ordered dither that fakes more shades than you have, plus an animated CRT subpixel mask for the shimmering-phosphor look. Both are small canvas passes, no shaders. Pulled out of ai-arena.
- [Restyling someone's WebGL terrain into night mode](https://seangeng.com-plan-optimizer/writing/night-infinite-terrain): mesq shipped a gorgeous open-source infinite-terrain scene in r3f. I didn't rebuild it — I reskinned it. A new theme palette and moonlit lighting turn a sunny field into a midnight one. Same shaders, different mood.
- [Switch to cubic-bezier over ease and linear](https://seangeng.com-plan-optimizer/writing/better-css-easing-with-cubic-bezier): A one-line upgrade for CSS animations: trade the default ease and linear for cubic-bezier(0.6, 0.6, 0, 1). It starts fast and settles slow, which reads as smooth. Push the curve past 1 and you get a bounce.
- [An isometric cube from one color and three divs](https://seangeng.com-plan-optimizer/writing/an-isometric-cube-in-css): A 3D cube in pure CSS transforms — three faces pushed out with translateZ, shaded from a single hex by nudging HSL lightness. No canvas, no library, optional logo and spin.
- [A sparkly backdrop from one div and mask-composite](https://seangeng.com-plan-optimizer/writing/a-sparkle-field-with-mask-composite): jhey's CSS trick: intersect a grid-of-dots mask with a Perlin-noise mask using mask-composite, then animate mask-position. The dots twinkle, and it's a single element instead of thousands of animated nodes.
- [A glossy squircle app icon](https://seangeng.com-plan-optimizer/writing/a-glossy-squircle-app-icon): Why app icons use squircles and not rounded rectangles, and how to make one in the browser: an SVG squircle clip, a top sheen, an inset rim, and a glare that sweeps across on hover.
- [A blocks grid you can play snake on](https://seangeng.com-plan-optimizer/writing/a-blocks-grid-you-can-play-snake-on): The explorer.b3.fun hero is a grid of live blocks, and you can play snake on it where the blocks are the food. Here's that idea pulled out into a standalone, dependency-free toy.
- [A draggable 3D game cartridge in pure CSS](https://seangeng.com-plan-optimizer/writing/a-3d-cartridge-in-css): No WebGL. A preserve-3d box with six faces, a drag that writes one rotation variable, and a drop-shadow trick that recolors a transparent PNG so one shell works for any accent. Pulled out of basement.fun.
- [One line of JavaScript for a real share sheet](https://seangeng.com-plan-optimizer/writing/the-web-share-api): The Web Share API hands a title, text, and URL to the operating system and opens the same native share sheet every app uses. Here's a share button that uses it, with a graceful fallback for desktop.
- [Recording the screen with two browser APIs](https://seangeng.com-plan-optimizer/writing/recording-the-screen-in-the-browser): getDisplayMedia grabs a stream of the screen, window, or tab; MediaRecorder captures it to a webm you can play back and download. A full screen recorder, no libraries, nothing uploaded.
- [Reading the battery in the browser](https://seangeng.com-plan-optimizer/writing/reading-the-battery-in-the-browser): The Battery Status API gives you charge level, charging state, and time-to-full from JavaScript, and pushes events when they change. Here's a battery widget built on it, with a fallback for the browsers that dropped it.
- [Knowing when the user goes offline](https://seangeng.com-plan-optimizer/writing/detecting-online-offline-status): navigator.onLine plus the online and offline events give you reactive connectivity in a few lines. Here's a status pill and a slide-in toast built on them, with the one caveat worth knowing.
- [An image pixelator in two drawImage calls](https://seangeng.com-plan-optimizer/writing/an-image-pixelator): Drop a picture, pick a block size, export a pixel-art PNG. The whole effect is drawing the image tiny, then scaling it back up with image smoothing turned off.
- [Progressive blur: ramping a marquee's edges into a haze](https://seangeng.com-plan-optimizer/writing/progressive-blur-marquee): A single backdrop-filter blurs uniformly with a hard edge. Stack a few blur layers, mask each to an overlapping gradient band, and the blur ramps smoothly — perfect for fading the ends of a marquee.
- [A pixel grid that breathes, in one canvas loop](https://seangeng.com-plan-optimizer/writing/a-dynamic-pixel-grid): Alex Krasikau's dynamic pixel grid, ported to a themeable canvas component. A field of pixels flickers random opacities inside a circle whose radius pulses on a sine wave.
- [A liquid-glass button, and the @property trick behind it](https://seangeng.com-plan-optimizer/writing/a-liquid-glass-button): Petr Knoll's frosted glass button, ported to a component. backdrop-filter for the frost, layered inset rims, and an animated conic-gradient border + sheen powered by @property angle interpolation.
- [The galaxy button: orbiting stars and a 3D ring in CSS](https://seangeng.com-plan-optimizer/writing/the-galaxy-button): jh3y's glowy CTA, ported to a React component. Orbiting stars, a conic spark sweep, and a star ring tipped into 3D with transform-style: preserve-3d, all driven by one --active variable.
- [A neumorphic toggle from two inset shadows](https://seangeng.com-plan-optimizer/writing/a-neumorphic-toggle): Recreating a soft, pressed-in segmented toggle from a Sketch recipe: a gradient pill, two opposing inset shadows for the depth, and a raised thumb that slides between sun and moon. Pure CSS.
- [A prompt to make AI write like a human](https://seangeng.com-plan-optimizer/writing/write-like-a-human): A system prompt that strips the AI tells out of generated writing — conversational tone, varied rhythm, real emotional context, and a hard list of things to avoid. Drop it in before you ask for any copy.
- [Boil the ocean: an agent prompt worth stealing](https://seangeng.com-plan-optimizer/writing/boil-the-ocean): Garry Tan's SOUL.md entry that tells your coding agent to ship the complete thing, not a plan to build it. Drop it into your agent's system prompt / SOUL.md / CLAUDE.md.
- [A sticky navbar that morphs when it sticks, no JS](https://seangeng.com-plan-optimizer/writing/sticky-navbar-that-morphs-on-scroll): scroll-state container queries let the browser tell you when a sticky element is stuck, so you can restyle it on scroll with pure CSS. No scroll listeners, no animation library. Chromium-only for now.
- [Two lines so anchor links don't hide under your header](https://seangeng.com-plan-optimizer/writing/anchor-links-that-dont-hide): Smooth in-page scrolling plus scroll-margin-top, so jumping to a heading lands it below your sticky header instead of tucked behind it. The fix everyone forgets until a link feels broken.
- [Use tabular-nums for any number that changes](https://seangeng.com-plan-optimizer/writing/tabular-nums-for-changing-numbers): Timers, counters, prices, scores, live data. If a number updates in place, give it tabular figures so it stops jittering. One CSS property: font-variant-numeric: tabular-nums.
- [A production button: gradient fill + inner-light rim](https://seangeng.com-plan-optimizer/writing/a-production-button): The button I actually ship: a class-variance-authority component whose depth comes from two pseudo-element layers (gradient fill, inner-light rim) and a color-matched shadow. Eight variants, four sizes, asChild.
- [Block disposable emails at signup](https://seangeng.com-plan-optimizer/writing/block-disposable-emails): Throwaway inboxes are how spam, trial-abuse, and fake accounts get in. Checking the email domain against a maintained disposable-domains list at signup takes minutes and pairs well with Cloudflare Turnstile.
- [How to be an engineer in the AI era](https://seangeng.com-plan-optimizer/writing/how-to-be-an-engineer-in-the-ai-era): A workshop I gave my team: intelligence got commoditized, the engineering value stack flipped, and the job is now shepherding products and orchestrating agents. The talk, the deck, and what I'd tell anyone trying to stay ahead of it.
- [Block scanners at the edge with one Cloudflare rule](https://seangeng.com-plan-optimizer/writing/block-scanners-at-the-edge): Bots hammer every site for /.env, /.git, /wp-login and a hundred other 'leaky paths'. Here's a single Cloudflare WAF custom rule that blocks them before they ever reach your origin, plus a generator and a Claude Code skill to apply it.
- [Skeletons that don't shift: build the skeleton from the real content](https://seangeng.com-plan-optimizer/writing/skeletons-that-dont-shift): Most loading skeletons are hand-sized grey boxes that don't quite match the content, so the page jumps when data lands. Keep the real content mounted, shimmer it in place, and wipe it in with a mask. Zero layout shift, pure CSS.
- [Faking an aurora glow with nothing but inset shadows](https://seangeng.com-plan-optimizer/writing/faking-a-glow-with-inset-shadows): How to make a dark tile look lit from within, with a colored glow rising off the bottom edge, using four stacked inset box-shadows and one outer bloom. No gradients-on-gradients, no images, no blur filters.
- [Elevation in dark mode: when drop shadows stop working](https://seangeng.com-plan-optimizer/writing/dark-mode-elevation): A single drop shadow vanishes on a dark background. Here's the layered box-shadow system that reads as real depth in dark UIs: a top light line, an inner hairline, an edge ring, and ambient shadows that double with negative spread.
- [A realistic hardware button in pure CSS](https://seangeng.com-plan-optimizer/writing/a-realistic-hardware-button-in-css): Recreating a physical, illuminated push-button in CSS: a gunmetal bezel, a recessed lit-glass panel, a glossy sheen, and a colored light bloom. Three nested layers, layered gradients, inset shadows. No images.
- [The candy button: a glossy 3D CTA from four shadows](https://seangeng.com-plan-optimizer/writing/the-candy-button): How to puff a flat blue rectangle into a tactile, pressable call-to-action using nothing but layered box-shadows: drop, ring, inset stroke, and a top sheen, plus hover and press states. Tailwind and plain-CSS versions.
- [Buttons with real depth: stacked gradients + layered shadows](https://seangeng.com-plan-optimizer/writing/buttons-with-real-depth): How a flat rectangle becomes a tactile, pressable button: two clipped gradients for fill and stroke, a three-part box-shadow, and hover/press states that actually move. Tailwind and plain-CSS versions.
- [Freeze any hover state with one line of JavaScript](https://seangeng.com-plan-optimizer/writing/freeze-hover-states-in-devtools): The setTimeout(debugger) trick: pause the page mid-hover so you can finally inspect tooltips, dropdowns, and other hover-only elements in the Elements panel. Comes with a bookmarklet to do it in one click.
- [Building a pixel-dissolve marquee](https://seangeng.com-plan-optimizer/writing/building-a-pixel-dissolve-marquee): Why I replaced the soft gradient fade on a logo marquee with edges that disintegrate into graduated pixel blocks: bigger, blurrier, and fainter the further out they go.

## Components
- [ASCII Text](https://seangeng.com-plan-optimizer/components/ascii-text): 3D text rendered to a wavy three.js plane, then re-sampled every frame into live ASCII characters that shimmer and follow your cursor. From B3's ai-arena.
- [Compact Cartridge](https://seangeng.com-plan-optimizer/components/compact-cartridge): A 2D game-cartridge card: a clip-path cartridge silhouette with layered noisy borders, an inset media well, a label tab, and a vertical Game NFT stamp. From basement.fun.
- [Loading Beam](https://seangeng.com-plan-optimizer/components/loading-beam): A laser-beam loading bar: a fill that races to 100% on an eased, jittery curve with a flickering glow and a blurred light at the leading edge. Pure CSS. From basement.fun.
- [Infinite Terrain](https://seangeng.com-plan-optimizer/components/infinite-terrain): An endless procedural WebGL scene — streamed grass, trees, and wind lines with a physics ball you steer — that you can reskin live across six moods: night, aurora, synthwave, sakura, ember, noir. Restyled from mesq's MIT r3f original.
- [Isometric Cube](https://seangeng.com-plan-optimizer/components/cube): An isometric 3D cube in pure CSS transforms — three faces tinted from one base color (lighter top, base front, darker right), optional logo on top, optional slow spin. Extracted from explorer.b3.fun.
- [App Icon](https://seangeng.com-plan-optimizer/components/app-icon): A glossy iOS-style squircle app icon: SVG squircle clip, a top sheen, an inset rim, and a glare that sweeps on hover. Extracted from explorer.b3.fun.
- [Block Snake](https://seangeng.com-plan-optimizer/components/block-snake): A grid of streaming blocks that's also a playable snake game — the blocks are the food. Arrow keys / WASD / touch pad, wrap-around walls, grows on eat. Rebuilt from the explorer.b3.fun hero.
- [Dither](https://seangeng.com-plan-optimizer/components/dither): Bayer 4×4 ordered dithering on any image — 1-bit mono or per-channel to N levels — with an optional animated CRT subpixel mask. Canvas 2D, no deps. Extracted from ai-arena.
- [3D Cartridge](https://seangeng.com-plan-optimizer/components/cartridge-3d): A draggable 3D game cartridge in pure CSS 3D transforms: spin it with a drag or swipe, snap to front/back, with the body color cast from an accent drop-shadow. Extracted from basement.fun.
- [Sparkle Field](https://seangeng.com-plan-optimizer/components/sparkle-field): A shimmering field of dots in a single element: a repeated dot mask intersected with an animated Perlin-noise mask via mask-composite, so the dots twinkle. No JS, no canvas.
- [Screen Recorder](https://seangeng.com-plan-optimizer/components/screen-recorder): Record your screen, a window, or a tab right in the browser with getDisplayMedia + MediaRecorder: live preview, a running timer, playback, and a webm download. Nothing leaves the device.
- [Network Status](https://seangeng.com-plan-optimizer/components/network-status): An online/offline indicator on navigator.onLine and the online/offline events: a live pill plus a toast that slides in on every change and auto-dismisses.
- [Battery Status](https://seangeng.com-plan-optimizer/components/battery-status): A live battery readout on the Battery Status API: animated fill, color by charge, a charging bolt, and time-to-full. Falls back to a simulation where the API is missing.
- [Share Button](https://seangeng.com-plan-optimizer/components/share-button): A share button on the Web Share API: opens the native share sheet where supported, and falls back to a copy-link + social-intents menu everywhere else.
- [Image Pixelator](https://seangeng.com-plan-optimizer/components/pixelator): Drop an image and pixelate it — drawn tiny then scaled back up with smoothing off, so it renders as crisp blocks. Block-size presets, full-res PNG export, transparency kept.
- [Progressive Blur](https://seangeng.com-plan-optimizer/components/progressive-blur): A graduated blur — stacked backdrop-filter layers, each masked to an overlapping gradient band, so the blur ramps smoothly instead of stepping. Shown fading the edges of a marquee.
- [Dynamic Pixel Grid](https://seangeng.com-plan-optimizer/components/pixel-grid): A canvas grid of pixels that flicker random opacities inside a sine-pulsing circle — a breathing field of static. Themeable, DPR-crisp, reduced-motion aware. Based on Alex Krasikau.
- [Liquid Glass Button](https://seangeng.com-plan-optimizer/components/glass-button): A frosted backdrop-blur button with layered inset highlights, an animated conic-gradient border, a moving specular sheen, and a shadow that tilts on press. Ported from Petr Knoll.
- [Galaxy Button](https://seangeng.com-plan-optimizer/components/galaxy-button): A glowy CTA with orbiting stars, a conic spark sweep, and a 3D star ring built on transform-style: preserve-3d. Lights up on hover. Ported from jh3y.
- [Neumorphic Toggle](https://seangeng.com-plan-optimizer/components/neu-toggle): A soft, pressed-in segmented toggle — a gradient pill with two opposing inset shadows and a raised thumb that slides between sun and moon. Pure CSS.
- [Button](https://seangeng.com-plan-optimizer/components/button): A layered gradient button — fill, inner-light rim, and a color-matched shadow on stacked pseudo-elements. Brightens on hover, presses on click. Eight variants, four sizes.
- [Skeleton Reveal](https://seangeng.com-plan-optimizer/components/skeleton-reveal): A loading skeleton built from the real content — so it's sized exactly right and nothing shifts on load — that wipes the content in with an animated mask. Pure CSS.
- [Hardware Button](https://seangeng.com-plan-optimizer/components/hardware-button): A realistic physical button — a gunmetal bezel housing a recessed, illuminated glass panel with embossed text and a colored light bloom. Pure CSS; presses into its housing.
- [Glow Tile](https://seangeng.com-plan-optimizer/components/glow-tile): A near-black app-icon tile with an aurora glow rising from the bottom — four stacked inset shadows plus an outer bloom. Recolors from one variable; scales to any size.
- [Dark Elevation](https://seangeng.com-plan-optimizer/components/dm-elevation): A dark-mode elevation scale — five layered box-shadow tokens with a top light line, inner hairline, edge ring, and doubling ambient shadows. From resting card to floating bar.
- [Candy Button](https://seangeng.com-plan-optimizer/components/candy-button): A glossy, puffed-up 3D call-to-action — drop shadow, blue edge ring, inset white stroke, and a top sheen. Lifts on hover, presses in on click.
- [Glossy Button](https://seangeng.com-plan-optimizer/components/gloss-button): A tactile gradient button — stacked fill + hairline gradients with a three-part shadow for real depth. Dark and light variants, elegant hover/press states.
- [Pixelated Marquee](https://seangeng.com-plan-optimizer/components/pixelated-marquee): An infinite logo/content scroller whose edges disintegrate into graduated pixel blocks — ramping pixel size, opacity, and backdrop blur instead of a flat fade.

## Freebies
- [Freebies](https://seangeng.com-plan-optimizer/freebies): free copy-paste tools — disposable-email blocker, Cloudflare WAF leaky-path rule generator, DevTools freeze bookmarklet, and a downloadable Claude Code skill.

## About
- [About](https://seangeng.com-plan-optimizer/about): background, current work, and links.

## Landing page — https://seangeng.com-plan-optimizer/freebies/plan-optimizer

Plan-Optimizer Skill for Claude Code by Sean Geng. A Claude Code skill that automates plan improvement through iterative refinement. Works by establishing a scoring rubric, generating an initial plan, then cycling through critique-and-rewrite steps until performance plateaus.

### Core mechanism
The skill implements a feedback loop that scores plans numerically against weighted criteria, identifies weaknesses, rewrites targeted improvements, and stops when scores stop climbing meaningfully.

### When to deploy
Use it for any plan requiring maximum quality — project launches, code migrations, research initiatives, strategy documents, and similar high-stakes planning.

### Installation
A single curl command installs it to `~/.claude/skills/plan-optimizer/`.

### Process Overview
The workflow emphasizes building the rubric first — described as "the ceiling" that determines how high quality the final plan can reach. The approach separates scoring from writing to prevent blind iteration.

Search strategies include:
- Hill-climbing (incremental improvements each round)
- Best-of-N (generating multiple structural variants when stuck)

### Output Deliverables
The final result includes the optimized plan itself, its numerical score with per-criterion breakdown, the score trajectory showing improvement over rounds, and an explanation of substantive changes made.

The skill explicitly warns against "reward hacking" — gaming metrics without genuine improvement — and emphasizes respecting plateaus to avoid wasting effort on noise iterations.

## Freebies index — https://seangeng.com-plan-optimizer/freebies

Sean Geng's free copy-paste tools ("free to steal"):

1. Plan-optimizer skill — Scores plans against rubrics, critiques and rewrites them iteratively. Available as a Claude Code skill with installation instructions.
2. "Boil the ocean" agent prompt — A system prompt by Garry Tan designed to make coding agents "ship the complete thing, not a plan."
3. "Write like a human" prompt — A system prompt removing AI-like qualities from generated text, focusing on conversational tone and authentic language.
4. Disposable email blocker — Checks signup domains against a maintained list to reject throwaway inboxes, with a live checker tool.
5. Cloudflare leaky-path blocker — Blocks scanner traffic for paths like .env, .git, wp-login at Cloudflare's edge with a WAF rule generator.
6. DevTools freeze bookmarklet — A browser bookmarklet that freezes hover states for inspecting tooltips and dropdowns.
7. Cloudflare leaky-paths skill (.zip) — The WAF rule as a downloadable Claude Code skill.

## Writing — https://seangeng.com-plan-optimizer/writing/iterate-a-plan-until-it-stops-improving

A skill that iterates on a plan until it stops improving. Sean Geng describes a Claude Code skill that treats plan creation as an iterative search process rather than a one-time writing task.

### Core Mechanism
Four key components:
1. Rubric-driven evaluation: Establishing weighted criteria upfront determines what "good" means and sets the ceiling for improvement.
2. Critique-then-rewrite cycle: Rather than vague improvement requests, the system identifies specific weaknesses against the rubric, ordered by impact.
3. Margin-based acceptance: New versions only become the best when they exceed the previous score by a meaningful threshold, preventing noise-driven false improvements.
4. Plateau detection: The loop terminates when scores stop advancing beyond the margin threshold.

### Advanced Technique
When hill-climbing stalls in local optima, the skill switches to best-of-N generation — producing structurally different plan variants simultaneously rather than incremental edits. Using a more capable model here provides the biggest leverage, as it both proposes better alternatives and perceives flaws weaker scorers miss.

### Installation
The skill installs via one command into Claude Code's skills directory and activates whenever users ask to improve, harden, or stress-test plans.
