# kunchenguid/lavish-axi

## Metadata
- Stars: 4358
- Primary language: JavaScript
- Default branch: main
- Latest release: lavish-axi-v0.1.96 (2026-10-29)
- License: MIT
- Homepage: 
- Fetched: 2026-10-30
- Final URL: https://github.com/kunchenguid/lavish-axi

## Description
HTML is the new markdown. Lavish is the new editor for your HTML artifacts.

## README
<h1 align="center">lavish-axi</h1>
<p align="center">
  <a href="https://github.com/kunchenguid/lavish-axi/actions/workflows/ci.yml"
    ><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/lavish-axi/ci.yml?style=flat-square&label=ci"
  /></a>
  <a href="https://github.com/kunchenguid/lavish-axi/actions/workflows/release-please.yml"
    ><img alt="Release" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/lavish-axi/release-please.yml?style=flat-square&label=release"
  /></a>
  <a href="https://www.npmjs.com/package/lavish-axi"
    ><img alt="npm" src="https://img.shields.io/npm/v/lavish-axi?style=flat-square"
  /></a>
  <a href="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue?style=flat-square"
    ><img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue?style=flat-square"
  /></a>
  <a href="https://x.com/kunchenguid"
    ><img alt="X" src="https://img.shields.io/badge/X-@kunchenguid-black?style=flat-square"
  /></a>
  <a href="https://discord.gg/Wsy2NpnZDu"
    ><img alt="Discord" src="https://img.shields.io/discord/1439901831038763092?style=flat-square&label=discord"
  /></a>
</p>

<h3 align="center">For when a rich editor is not rich enough.</h3>

<p align="center">
  <img alt="Lavish Editor demo" src="lavish-editor-marketing/renders/lavish-editor-marketing.gif" width="960" />
</p>

HTML is the new markdown. Lavish is the new editor for your HTML artifacts.

Agents are good at producing rich HTML artifacts, but the human-agent collaboration loop on such artifacts is lacking and falls back into screenshots and long responses for “tell me what to change.”
That loses the thing HTML is best at: interactivity.

Lavish Editor opens agent-generated HTML files in a local browser, lets you pinpoint elements and selected text, edit diagrams your agent authored as Mermaid whiteboards, and send feedback to the agent to address.

- **Local-first** - Review local HTML artifacts with a local CLI and no cloud dependency in the core feedback loop; hosted sharing through third-party ht-ml.app is explicit and opt-in.
- **Human-AI collaboration** - Annotate elements and selected text ranges, edit Mermaid whiteboard diagrams, and send messages to the agent without leaving Lavish Editor.
- **Battery included** - Lavish Editor teaches your agent good visualization for common use cases such as product or technical plans, design explorations and more out of the box.

Lavish Editor is an [AXI](https://axi.md), which means -

- It's just a CLI any capable agent can run without setup.
- It's optimized for agent ergonomics. TOON output, long polling, and contextual disclosure making it highly token efficient.
- The skill and hooks below only handle discovery; agents learn to use the AXI by using it.

## Quick Start

Install the Lavish skill in the [Agent Skills](https://agentskills.io) format with [`npx skills`](https://github.com/vercel-labs/skills):

```sh
npx skills add kunchenguid/lavish-axi --skill lavish
```

That is the entire setup - no npm install needed.
The skill teaches your agent to run Lavish through `npx -y lavish-axi`, so the CLI comes along on demand.
It stays a short stub and sends the agent to `npx -y lavish-axi --help`, `reply --help`, `design`, and `playbook` for current instructions, so an installed copy cannot go stale against a newer CLI.
Its frontmatter also includes Hermes Agent metadata, so Hermes-compatible harnesses can categorize and surface it as a first-class productivity skill.
This installs the public `lavish` skill.
The repository also contains an internal `lavish-design` brand skill for maintainers; default `npx skills add ... --list` and skills.sh discovery hide it unless `INSTALL_INTERNAL_SKILLS=1` is set.

Then, in agents that expose skills as slash commands (Claude Code, for example), invoke it directly:

```
/lavish let's discuss our plan here
```

Or just ask for anything that is easier to grasp visually - a plan, comparison, diagram, table, code view, or report - and the agent loads the skill on its own when it recognizes the task.

By default the skill lands in the current project's skills directory (`.claude/skills/`, for example); add `-g` to install it for all projects (`~/.claude/skills/`).

## Other Ways to Use Lavish

The skill is the recommended path, but it is not the only one.

### Zero setup

Lavish is an AXI, so any capable agent can run the CLI directly with nothing installed at all.
Just tell your agent:

```
Use `npx -y lavish-axi` to write a product or technical plan for what we discussed.
```

### Session hook

Want Lavish's ambient context - including your live open sessions - fed into every agent session instead of loading on demand?
Install the CLI globally and opt into the hook:

```sh
npm install -g lavish-axi
lavish-axi setup hooks
```

This installs a `SessionStart` hook for **Claude Code**, **Codex**, **OpenCode**, and **GitHub Copilot CLI** that surfaces open sessions, visualization playbooks, and usage guidance at the start of each session.
Unlike the skill, the hook also shows your live open sessions, so a fresh agent session can resume an in-flight review.
**Restart your agent session after running this** so the new hook takes effect.

### Agent Plugin

Lavish also ships as an [Agent Plugin](https://agent-plugins.org) - the vendor-neutral packaging standard for skills and MCP servers - so clients that speak that format can load it directly.

**No marketplace is involved.** The installed npm package _is_ the plugin: `plugin.json` sits at the package root next to the `skills/` directory, so whatever `npm install` already put on disk is a complete, conformant plugin. Install the CLI, then register it:

```sh
npm install -g lavish-axi
lavish-axi setup plugin
```

That registers the installed package with every supported client it finds - **VS Code**, **Cursor**, and **GitHub Copilot CLI** - and reports which ones were absent. It is opt-in and idempotent, and it repairs the registered path after a reinstall or relocation. Reload each client afterward.

Each client is registered independently: one that cannot be registered is reported with what to do about it, and never blocks the others or fails the command.

To register by hand instead, point any client at the package directory (`npm root -g`/`lavish-axi`):

| Client             | Register with                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| VS Code            | `"chat.pluginLocations": { "<package-dir>": true }` in user settings                                               |
| Cursor             | link the package dir at `~/.cursor/plugins/local/lavish-axi` (`setup plugin` handles Windows link compatibility)   |
| GitHub Copilot CLI | `copilot plugin install <package-dir>` (or `copilot plugin install kunchenguid/lavish-axi` straight from the repo) |

Codex and ChatGPT install plugins only from marketplace sources, so Codex users should use the session hook above instead.
Lavish declares no MCP server - the CLI itself is the agent interface - so a plugin install brings the same `lavish` skill, and the skill and plugin are alternatives rather than a stack.

### From source

```sh
git clone https://github.com/kunchenguid/lavish-axi.git
cd lavish-axi
pnpm install --frozen-lockfile
pnpm run build
pnpm link
```

## How It Works

```
┌───────────────┐
│ Agent writes  │
│ artifact.html │
└───────┬───────┘
        ▼
┌────────────────────────┐
│ lavish-axi <file_path> │
│ opens local browser UI │
└───────┬────────────────┘
        ▼
┌────────────────────────┐
│ Human annotates text   │
│ or elements, sends     │
│ chat, or queues layout │
│ issues from the inbox  │
└───────┬────────────────┘
        ▼
┌────────────────────────┐
│ lavish-axi poll waits  │
│ and returns prompts    │
│ the user queued        │
└────────────────────────┘
```

- **File-path identity** - Sessions are keyed by the canonical HTML file path, so agents do not need opaque IDs.
- **Portable artifacts** - The artifact runs in a sandboxed iframe while Lavish injects a small SDK for annotations, snapshots, feedback controls, and render-time layout checks.
  Author-defined links and popups can open in top-level tabs, while artifact documents remain sandboxed without same-origin access.
  Lavish does not inject any design system, so the saved HTML file renders identically whether you open it through `lavish-axi` or directly in a browser.
  Run `lavish-axi design` for the single source of agent-facing design guidance, including optional CDN snippets and the whiteboard (Mermaid) opt-in snippet.
- **Self-paint warning** - `lavish-axi <html-file>`, `export`, and `share` run a render-free check for artifacts missing an explicit page background and return a one-line `self_paint_warning`.
  The check fails open - any stylesheet link, `@import`, Tailwind runtime script, `color-scheme`, or `html`/`body`/`:root` background signal suppresses it - and it never blocks the open.
- **Open-time layout gate** - The browser chrome masks an artifact only while the real in-iframe audit waits for fonts and final geometry.
  The first completed client-side check reveals the artifact, whatever it found and even if reporting that check to the server fails; the gate never holds the review hostage waiting for a repair or a network round-trip.
  The user can click **Show anyway**, and a bounded safety timeout fails open from every gate state.
  If the review cannot load at all - the chrome's own script never runs, or the server does not answer the artifact's load request after several retries - the mask names the problem and offers **Check and reload** without removing the independent **Show anyway** escape.
  A review already loaded in another browser tab is named the same way, with a **Take over here** button that loads the artifact in the current tab, because Lavish loads an artifact in one tab at a time. The takeover warning reads "Unsent answers stay in the tab or window where you entered them; taking over in another window does not bring them along."
- **Layout issues inbox** - Detection is passive. After fonts and finite animations settle, the injected SDK confirms severe failures from direct rendered evidence such as materially escaped meaningful content or required controls, clipped text fragments, viewport reachability, or near-total semantic occlusion.
  Explicit ellipsis and line clamp, standard visually hidden accessibility text, intentional scrollers or masks, parent overhang, generic element scroll geometry, decorative overlap, and uncertain motion do not produce findings by themselves.
  Proven failures are filed in a **Layout issues** button in the top bar, which is hidden while nothing is unresolved and otherwise shows the unresolved count.
  Its drawer lists each issue with severity, a plain-language explanation, the affected viewport, the target/component identity, when it was last seen, and its lifecycle state, plus per-issue **Reveal** (highlight it in the artifact) and **Dismiss** actions.
  Nothing is selected by default. The user picks issues (or **Select all**) and **Queue selected fixes** turns that whole group into one ordinary queued prompt, tagged `layout-warnings`, that reaches the agent through the normal feedback path when they send.
  Detection never returns `lavish-axi poll` and never wakes an agent; only the user queueing a fix does. The one exception is a fatal `artifact_failures` response, for failures that make the review itself unusable, such as the artifact document or one of its own local assets failing to load.
- **Layout issue lifecycle** - Each issue is identified by a stable fingerprint of the diagnostic rule, the normalized target identity, and the viewport class, so repeat detections update one record instead of inflating the count.
  `Open` means the latest completed check for its viewport still detects it. `Queued for fix` means the user asked for a repair - it stays unresolved and counted, and cannot be queued again while that request is outstanding.
  `Resolved` requires a newer successful artifact load plus a complete check at the same viewport that no longer detects it; it then leaves the count but keeps a bounded history.
  `Still present` (recurring) means a queued issue survived a newer revision, so it is selectable again with its earlier attempt retained. `Unverified` means a reload or check failed or was incomplete, so the prior issue was preserved rather than cleared. `Returned` means a resolved issue came back on a later revision.
  Dismissal applies only to the current artifact revision; a later revision surfaces the issue again if it is still detected. A check at one viewport never clears an issue found at another, and a viewport removed from the configured diagnostic set (`LAVISH_AXI_DIAGNOSTIC_VIEWPORTS`, default all) is marked obsolete with an explicit reason rather than reading as fixed.
- **Revisions legend** - Opt-in. After a round of feedback the agent regenerates the whole file, and a one-sentence edit is invisible on a long artifact. The agent can declare what it changed in the artifact itself: one `<script type="application/json" data-lavish-revisions>` array of `{ id, label, timestamp, summary }` entries, plus `data-lavish-revision="<id>"` on each block it edited or added. Run `lavish-axi design` for the snippet.
  A **Revisions** button then appears in the top bar with a legend listing each round - colour swatch, label, time, and the agent's summary - and **Reveal** steps through that round's changed blocks, flashing them one at a time.
  Each revision's swatch carries a distinct border style and fill pattern as well as a colour, so the rounds stay distinguishable without colour. Artifacts with no registry show no button and are otherwise unaffected, a malformed registry is ignored rather than surfaced as an error, and at most 6 revisions are listed - one per distinguishable swatch.
  Lavish never marks up the artifact for this: the legend lives in the browser chrome, so the served page stays identical to the saved file, and the registry and marks travel with the file through export.
- **Live tab title and icon** - Opt-in. The browser tab adopts the artifact's `<title>` and first `<link rel="icon">` when it loads. A long-lived artifact can keep the tab current afterwards with `window.lavish.setDocumentMeta({ title, icon })`: a string sets the field (a title that is blank after trimming restores the load-time title), `null` restores the load-time value, and an omitted field is left alone. The title is trimmed to 120 characters and shown as `<title> · Lavish`; the icon must be a `data:image/svg+xml` URL of at most 8192 characters. Anything else is ignored. A value stays until the next call or until the tab itself reloads, so call again after each page update. The call is a no-op when the page is not open in Lavish, so feature-detect with `window.lavish?.setDocumentMeta?.(...)`.
- **Local assets** - Copy local images, CSS, fonts, and scripts next to the HTML artifact and reference them with relative paths from that directory; root-prefixed paths such as `/assets/logo.png` will not resolve through Lavish's artifact route.
- **Export and sharing** - `lavish-axi export` writes `<name>.export.html` by inlining local assets only, stripping the annotation SDK, and leaving remote CDN/font references as links that still need network access.
  `lavish-axi share` publishes the same local-inlined HTML to [ht-ml.app](https://ht-ml.app), a third-party hosting service not part of Lavish.
  Publishing sends the artifact to ht-ml.app's servers, public by default, or private and password-protected with `--private` (Lavish generates the password and returns it once, in the command output and in the browser publish dialog) or `--password <pw>` (one you supply, never echoed back). A generated password is a shared secret: give it to whoever should read the page, and expect it to appear in your agent's transcript, because the agent has to relay it. Lavish does not store it.
  The response includes a secret `update_key` shown once. Keep it to republish the same URL later with `--site <site_id> --update-key <key>`, which replaces the HTML in place and leaves the password alone unless you pass `--private` (rotate to a new generated one) or `--password <pw>` (set one). Locking a page that was public is not instant - it can keep answering from ht-ml.app's CDN cache for minutes after the password is set - while a page that was already private has no such cached copy.
  A page's password cannot be removed: ht-ml.app accepts a request to clear one and silently ignores it, so Lavish offers no way to make a private page public rather than telling you it did something the host did not do. Republish as a new page if you need a public URL.
  ht-ml.app has no delete endpoint, so `--unpublish --site <site_id> --update-key <key>` replaces the page with a short placeholder and locks it behind a discarded random password rather than removing it: the URL still resolves and the host still holds what was published. The content swap is immediate, but the lock is not: a page that was public can keep serving the placeholder to uncredentialed visitors from ht-ml.app's CDN cache for minutes afterwards. The `update_key` plus `--private` republishes real content behind a new password you can share.
  Bundling never fetches remote URLs, Lavish itself does not set a CSP, local reads stay confined and size-capped, and absolute `file://` paths outside safe inlined asset references are redacted before output.
  Per-asset and per-bundle inline caps default to 10 MB and 25 MB, overridable with `LAVISH_AXI_EXPORT_MAX_ASSET_BYTES` and `LAVISH_AXI_EXPORT_MAX_BUNDLE_BYTES`.
  Unresolved local assets or export notices such as author-set CSP meta tags and redacted file URLs are surfaced in command or browser output.
  Use `--token` or `LAVISH_AXI_HTML_APP_TOKEN` for an optional bearer token when publishing a new page (a republish or `--unpublish` authorizes with the `update_key` instead and rejects `--token`); set `LAVISH_AXI_HTML_APP_API_URL` to override the ht-ml.app API base and point `share` at a backend you control (see [Self-hosting the share backend](docs/self-hosting-share.md) for the contract it must implement).
- **Live reload** - Lavish watches the HTML artifact file by default and preserves review context across reloads: the artifact iframe scroll position, an open annotation card's unsent text, and answers to `data-lavish-question` controls (application-owned form state is left alone). Supported review state and the unsent queue are saved in that tab's `sessionStorage` and survive a full reload of the review page in the same tab when browser storage is available. They are not shared with another tab or window; closing the owning tab can lose work that has not been sent. While a queued layout-issue batch is outstanding, closely spaced saves coalesce so one batch of fixes costs one refresh. To also reload on sibling asset changes, add `data-lavish-live-reload-root` to the root element or `<meta name="lavish-live-reload" content="root">`.
  If the element an unsent annotation was attached to is gone from the artifact for good, Lavish cannot reopen that card, and if the artifact replaces a queued note while you are editing it, the replacement is kept as the artifact sent it. Either way, Lavish writes your edited text into the conversation panel under **Unsent annotation** - selectable, never written over anything you have typed, and kept there across reloads; no note is ever dropped to make room for a newer one, and a note the browser refuses to store says so where it is shown.
- **Feedback controls** - Native controls (radios, checkboxes, inputs, selects, buttons, labels, disclosure summaries, contenteditable) and custom widgets with an interactive ARIA role (`button`, `checkbox`, `combobox`, `menuitem`, `menuitemcheckbox`, `menuitemradio`, `option`, `radio`, `switch`, `tab`, `treeitem`) are interactive automatically, so they do not need `data-lavish-action`. A link (`<a href>`) stays annotatable when it carries one of these roles or sits inside such a widget.
  Artifacts can start in explore mode with `data-lavish-annotate="off"` on the root `<html>` element so stray clicks do not open annotation cards. Annotation stays on by default (or with `"on"`); unknown values default to on. The toolbar reflects the page default and can override it; the reviewer's choice persists across artifact reloads within that review page. See `lavish-axi playbook input` for author guidance.
  For reversible choices, let option clicks update local state, then queue exactly one final answer from a per-question submit or Queue answer button with `window.lavish.queuePrompt()`.
  If someone may open a decision artifact as a standalone HTML file, `lavish-axi playbook input` provides an optional Copy all answers control they can use to paste their form answers back into chat.
  Mark only custom (non-native) clickable elements with `data-lavish-action` so Lavish does not annotate them, and use `data-lavish-question` or `queueKey` when pre-send updates for the same question should replace each other.
  Everything you send is part of the conversation: a note on an element, a text selection, a table cell, a diagram node, a whiteboard, a layout-issue batch, or a composer message each becomes a bubble on your side of the Conversation panel, with an anchor line naming what it was attached to (the element tag, text selection, table cell, diagram node, whiteboard, or layout issues), a quoted excerpt, and, when available, the selector on hover. A note you have queued but not sent sits at the end of the conversation as a dashed bubble labelled **Queued** with edit and remove controls. Clicking the bubble or its edit control opens its words for editing in place and scrolls the artifact to the element it points at; clicking that element again in annotate mode opens the same note rather than a fresh card. Saving a note with no words and no images removes it, and **Send** delivers an open edit as typed. While its batch is in flight it reads **Sending** and can no longer be edited, and once the server accepts it, it settles in place as a sent bubble in every tab of the session. The panel keeps the newest stored transcript up to 5 MiB; older bubbles drop from view, but an accepted note still settles and is not sent twice. Agent replies render a small Markdown subset - paragraphs, line breaks, headings as bold lead lines, bullet and numbered lists, fenced and inline code, bold, italic, and http(s) links - while tables, images, and raw HTML stay as the text the agent wrote; your own messages keep their line breaks and are never parsed.
  On wider screens, the conversation and the queued notes share one scrollable Conversation panel above a sticky composer, so long feedback queues do not push the text box or send controls off screen. The sidebar button in the top bar hides that panel so the artifact takes the full width, and shows it again; while it is hidden the button counts queued notes or marks an agent reply you have not seen, and the choice is remembered in this browser for every review.
  The browser chrome keeps editing actions in the overflow menu (copy path, reload artifact, copy DOM snapshot, export standalone HTML, publish link, end session), while the composer exposes **Send & End** beside **Send to Agent** to submit queued prompts and user-ended attribution together. Once **Send & End** starts, Lavish pauses new feedback, waits up to 5 seconds for feedback preparation already underway, keeps any open annotation draft intact until delivery succeeds, then holds that exact terminal batch. A completed reservation survives a page reload, including when its prompts were already delivered and only the pending end remains; incomplete preparation is not restored. If preparation times out, Lavish keeps the review open and its existing queue editable with a visible error. A transient delivery failure permits only retrying the same terminal batch through **Send & End** until it succeeds. If a snapshot makes the request too large (HTTP 413), Lavish retries that exact batch once without the optional snapshot. An actionable attachment rejection (HTTP 400), recoverable layout-selection conflict (HTTP 409), or unrecoverable 413 instead cancels the terminal reservation without ending the session, keeps the prompts queued, and restores editing, removal, **Send to Agent**, **Send & End**, and **End session** so the reviewer can revise or remove stale feedback before submitting again.
  Unsent queued notes belong to the tab where you entered them, not to a server-shared draft. Empty **Send to Agent** reports "Nothing queued in this tab." followed by the same message: "Unsent answers stay in the tab or window where you entered them; taking over in another window does not bring them along." Annotate mode alone does not queue a note, so use the annotation card's **Queue** action first. Only feedback accepted by **Send** is stored on the server for delivery to the agent.
  Composer feedback is visibly queued before the text box clears and stays queued until acknowledged. Send waits up to 5 seconds for the artifact's DOM snapshot, then delivers without that optional context if the frame no longer answers; a late snapshot cannot submit the batch twice. A failed or still-unacknowledged POST keeps the queue and shows persistent recovery guidance unless a transcript sync proves the server already accepted that feedback.
- **Reviewing on a phone** - Below 860px wide, the artifact takes the whole screen above a **Conversation** dock, and the conversation opens as a bottom sheet over it: tap the dock, swipe it up, or press the chevron to raise it; tap the dimmed artifact, swipe the sheet down, press the chevron, or press Escape to lower it. The dock reports what matters while the sheet is down - how many prompts are queued, a reply that arrived while you were reading, or whether the agent is listening - and the sheet stays open across a reload of the review page. The sheet sizes itself to the visible viewport and respects safe-area insets; if the keyboard or attachments leave little room, conversation content yields or scrolls while the send actions remain pinned above the bottom edge. In landscape the sheet covers the top bar as well. Wider screens keep the side-by-side layout.
- **Keyboard shortcuts** - In the chrome composer, Enter sends queued prompts and Shift+Enter inserts a newline.
  In the annotation card, Enter queues the annotation, Shift+Enter inserts a newline, and Ctrl+Enter (Cmd+Enter on macOS) queues it and sends all queued prompts immediately. Escape closes the card, same as Cancel, but only while it is empty (no text, no attachment); with unsent text or an attachment present, Escape does nothing rather than risk discarding it.
  While editing a queued note, Enter saves it, Shift+Enter inserts a newline, and Escape discards the edit.
  Cmd+I or Ctrl+I toggles between annotate and explore mode from either the browser chrome or the artifact iframe, including while focus is in a textarea or control.
  In annotate mode a plain click on a link annotates it; Ctrl+click (Cmd+click on macOS) follows the link instead, opening it in a new tab as the browser normally would, without leaving annotate mode. Off macOS, Meta+click (the Windows or Super key) annotates like a plain click.
- **Agent presence** - The browser shows when no agent is listening and keeps human feedback actions available while the agent is working. Feedback accepted by **Send** is queued on the server for the next successful `lavish-axi poll` delivery even across reloads; never-sent notes remain in the originating tab. An agent reply concludes delivered work and returns presence to waiting (see the CLI Reference for reply and poll commands). A supervisor-owned process listener is shown as an external listener rather than an idle captain turn.
- **Delivery receipts** - Every note you have sent carries three emoji under it that light up in turn: 👀 **Seen** when a `lavish-axi poll` takes the note, 🛠️ **Working** when the artifact file changes after that, and ✅ **Done** when the agent replies. A step that has not happened yet is the same emoji greyed out. All three come from what the server observes; the agent does nothing extra. Until 👀 lights, the row says why: no agent is listening, or the agent is busy and the note is delivered on its next poll. A note answered without touching the artifact goes Seen to Done with Working still grey. A reply marks every note the agent has seen as Done, not notes still waiting for a poll. Each emoji names its step and time on hover and to screen readers. Notes sent before receipts existed show no receipt row.
  In a Herdr-managed pane, set `LAVISH_AXI_HERDR_CHIME=1` to show a Herdr request notification and play its chime once an indefinite poll enters the waiting state. Immediate queued feedback and timed debug polls do not trigger a notification. The integration is off unless both `LAVISH_AXI_HERDR_CHIME` and Herdr's `HERDR_ENV` session marker equal `1`; leaving either unset or using any other value opts out. Notification delivery runs without blocking feedback: if Herdr is unavailable, rejects the notification, stalls, or fails, the poll continues unchanged.
  Closing the last review tab while a poll is active starts a reconnect grace period, 10 seconds by default. A reload or quick reconnect keeps an active poll waiting; if every review stays disconnected, the poll returns `browser_disconnected` without ending the resumable session, and the agent asks whether to reopen or end it instead of acting uninvited.
  A phone that locks its screen or backgrounds the tab drops the connection too, so set `LAVISH_AXI_DISCONNECT_GRACE_MS` on the server to a longer millisecond budget, or to `0` or `off` so a disconnect never ends the poll (it then waits for feedback, an end, or its own timeout). Empty or invalid values keep the 10-second default.
  The no-timeout poll always writes an immediate stderr banner so it is visibly not hung; it adds the periodic stderr wait ticks only in an interactive terminal, so when stderr is piped (as under agent harnesses) the captured output carries no tick noise. Stdout always stays reserved for the final response; if the poll is interrupted or times out before feedback arrives, re-run it because feedback remains queued until delivery. Poll delivery consumes the response, so read the complete response before truncating or filtering it.
  Codex-specific guidance keeps that poll attached to the active turn instead of hiding it in a background task, because completed background tasks may not resume the agent.
- **Session end etiquette** - Lavish tracks who ended a session: a human clicking **End session** (or **Send & End**) in the browser is a user-initiated end, while `lavish-axi end <html-file>` is agent-initiated.
  When either side ends the session, every open review tab becomes visibly read-only and disables its feedback controls; feedback submitted after the end is refused instead of being accepted without an agent to receive it.
  A plain `lavish-axi <html-file>` after a user-initiated end refuses to reopen the browser and returns guidance instead; pass `--reopen` only when the user asks for further review or something important needs their visual attention.
  Agent-initiated ends keep reopening normally, same as before.
  `lavish-axi poll`'s `ended` response and the `feedback` response for the final batch before an end both carry `next_step` guidance telling the agent to stop polling and deliver remaining updates in chat instead of reopening.
- **Precise targets** - Text annotations include selected text plus range anchors, and text selections carry those anchors only.
  Clicking an element inside a table also carries the cell's visible row and column names alongside the exact CSS locator, so filtered or sorted rows do not make feedback look misdirected.
  When merged cells make either name ambiguous, Lavish leaves that name out rather than guessing; an explicit `<th scope="row">` remains authoritative even when a `rowspan` makes the row's position ambiguous.
  The CSS locator still points at the exact element you clicked, so an annotation with an omitted name is only less descriptive, never mislabelled.
- **Image attachments** - Attach reference images (PNG, JPEG, WebP) in either the Conversation composer or an annotation card by pasting, drag-dropping, or using its image picker; each image shows a thumbnail chip with upload, remove, retry, and error states. If a sent image is later evicted under the attachment storage limits, its transcript-history thumbnail becomes an **Image expired** placeholder.
  A paste containing both text and images preserves the text while attaching the images (a copied file's own name or path is treated as placeholder and not pasted). Conversation messages may contain text and images together or images only.
  Images are stored under the state dir and the queued prompt carries a server-generated absolute `path` and content-hash `id` (plus mime and dimensions) - never the raw bytes - so `lavish-axi poll` hands the agent a local file path to open.
  Limits are `LAVISH_AXI_MAX_ATTACHMENT_BYTES` (default 10 MiB per image), `LAVISH_AXI_MAX_ATTACHMENTS_PER_PROMPT` (default 4), and `LAVISH_AXI_MAX_PROMPT_ATTACHMENT_BYTES` (default 25 MiB per prompt); if any image is missing or any prompt breaches a count or byte cap, the entire send batch is rejected, the queue is preserved, and the reason is surfaced in the composer rather than silently dropping images.
  As a browser-side abuse guard, each chrome page allows 30 upload attempts per rolling minute, 4 uploads in flight at once, and 256 MiB of attempted image bytes over its lifetime; rejected uploads stay visible for retry or removal.
  Unreferenced attachments expire after `LAVISH_AXI_ATTACHMENT_TTL_MS` (default 7 days; `0`/`off` disables); `LAVISH_AXI_MAX_ATTACHMENT_DISK_MB` (default 512 MiB; `0`/`off` disables) caps total attachment disk and may evict older unreferenced images sooner.
  The cap is enforced when an image is uploaded, not just periodically: the upload first reclaims unreferenced files (oldest first, and never one added within the last hour), and if it still would not fit, that upload is refused with a storage-full error on its chip instead of discarding an image the user is about to send.
- **Mermaid diagrams** - Whiteboards are an opt-in: agents author a diagram as Mermaid only when you ask for an editable whiteboard, and hand-authored inline SVG illustrations are the default figure medium otherwise.
  In the Lavish browser, every rendered Mermaid diagram in a `.mermaid` container becomes an embedded editable Excalidraw whiteboard.
  Click a diagram to unlock editing, and use its Fullscreen action to edit it over the whole viewport.
  Whiteboard scenes autosave locally.
  If a live reload changes the Mermaid source, an unmodified whiteboard silently re-converts to the new diagram. If the reviewer had edited the scene, reopening it lets them re-convert and discard the saved edits or keep editing the saved scene.
  Use **Queue feedback** to add a bounded edit summary plus local `.excalidraw` scene and PNG preview paths to the Conversation panel, then click **Send to Agent** to deliver it.
  The agent updates the artifact's Mermaid source, which remains authoritative.
  Flowchart, sequence, class, ER, and state diagrams convert to editable shapes; other diagram types are images that reviewers can draw and annotate.
  Lavish changes only the browser view, so saved, standalone, and exported artifacts still render plain Mermaid.
- **Whiteboard libraries** - Copy Excalidraw library files (`.excalidrawlib`, for example from [libraries.excalidraw.com](https://libraries.excalidraw.com)) into `~/.lavish-axi/excalidraw-libraries/`, or `LAVISH_AXI_STATE_DIR/excalidraw-libraries/` when set. Every whiteboard's library panel lists their items, and an item you drop on the canvas reaches the agent by name in the edit summary.
  Agents run `lavish-axi libraries` to find item refs and can show a flowchart node as one of those icons by adding a `%% lavish-icon <node-id> <library-id>/<item name>` comment to the Mermaid source. Mermaid ignores the comment, so saved, exported, and shared copies, and whiteboards missing that library, show the plain node.
  Lavish only reads that directory and never downloads libraries. Files over 10 MB, more than 25 MB or 5,000 items in total, and unreadable files are skipped; `lavish-axi libraries` lists each skip with its reason.
  Each library carries its author's terms (AWS Architecture Icons, for example, are covered by AWS's own usage terms), so check them before using one.
- **Server cleanup** - The detached server stops after the last session ends when nothing is connected, or after `LAVISH_AXI_IDLE_TIMEOUT_MS` (default 30 minutes) with no browser or poll connections.
  Set `LAVISH_AXI_IDLE_TIMEOUT_MS=0` or `off` to disable idle self-shutdown.
- **Server upgrades** - One background server serves every session, so upgrading `lavish-axi` while reviews are open makes the next `lavish-axi <html-file>` replace that server. Only a newer CLI replaces an older server: a CLI older than the running server uses it as is, so two installed versions on one machine do not restart each other's server. Releases up to and including 0.1.86 still replace a server of a different version, so this turn-by-turn restart stops only when both installed versions contain this fix. Only the review page for the artifact being opened reloads itself once the replacement answers - and not even that one while you have unsent annotation text open, which gets the same banner instead so the reload is yours to make. Every other open review page keeps working and shows a banner reading "Lavish was updated. This page is running the previous version.", with a Check and reload button and a Dismiss button, so no page you are reading reloads on its own. After `lavish-axi stop` those pages say Lavish was stopped and to reload after you start it again, and a restart that only picks up a local build says that rather than claiming an update. An open review page whose server simply goes away - idle self-shutdown, a crash, a machine that slept - shows that same banner once reconnecting has failed for a few seconds, rather than retrying a dead server silently while looking fine; it clears itself if the server comes back, and dismissing it keeps it dismissed until then.
  A page still using the legacy event stream reloads once when it reconnects to the replacement server, moving itself onto the current transport without retaining an HTTP connection. If unsent annotation text is open, it shows the neutral server-restarted banner instead and waits for you to reload.
  Every **Check and reload** control asks the server whether it is running before it navigates; while nothing answers, the page stays where it is and says so, and a check that gets no answer at all says that instead of guessing.
  In-flight `lavish-axi poll` commands end with an interrupted-poll error and are safe to re-run; server-accepted feedback remains queued until delivery, while never-sent notes and supported annotation drafts survive a same-tab reload as described under **Live reload**.
  A page waits for the replacement rather than reloading into a port nothing is listening on, and tells the user to restart Lavish if it never returns.
- **Local-first state** - Session state stays under `~/.lavish-axi/` by default, or `LAVISH_AXI_STATE_DIR` when set.
- **Diagnostic viewports** - `LAVISH_AXI_DIAGNOSTIC_VIEWPORTS` sets which viewport classes the layout-issue inbox tracks (`mobile`, `compact`, `desktop`; comma-separated, default all). Warnings whose class leaves the set are marked obsolete with an explicit reason instead of silently reading as fixed.
- **Server port** - Set `LAVISH_AXI_PORT` to choose the server port; it defaults to `4387`.
- **Network binding** - With Tailscale running, the review server automatically listens only on loopback (`127.0.0.1`) and this machine's Tailscale IPv4 address - never on `0.0.0.0` or every interface. The generated session link uses the machine's MagicDNS name, so it is the phone-ready URL to open from another device on the same tailnet. When Tailscale is absent or down, Lavish silently falls back to loopback-only and prints no phone URL. If Tailscale is running but MagicDNS is unavailable, Lavish visibly warns that phone access is unavailable and remains loopback-only. Binding beyond loopback exposes an unauthenticated server that can read and serve arbitrary local files to devices that can reach it, so the tailnet should be trusted. Any explicit `LAVISH_AXI_HOST` overrides automatic Tailscale binding; wildcard values are restricted to loopback, while a non-wildcard value selects that concrete bind address, and the server listens on loopback as well so every local CLI finds it whatever its own `LAVISH_AXI_HOST` says. An address that cannot be bound - the tailnet address while another process holds it, while Tailscale restarts, or an explicit hostname that temporarily does not resolve - is reported as `network_warning` in `lavish-axi <file>` output and logged to `server.log`; session links point at loopback meanwhile unless `LAVISH_AXI_LINK_HOST` overrides them, and the server keeps retrying that address in the background and immediately on the next CLI invocation. Once it binds, the warning clears and new session links use it again, with no restart. If no listener can bind, startup fails rather than claiming a reachable server. `LAVISH_AXI_LINK_HOST` controls the link host when automatic Tailscale binding is disabled.
- **One server per port** - Agents on one machine can run with different `LAVISH_AXI_HOST` settings, or none, and still share one server: before starting one, the CLI looks for a running server on its configured host, loopback, and every other local address. A running server that was never asked to listen on the address a CLI's `LAVISH_AXI_HOST` names is replaced once by a server that listens on that address plus every address the old one served, keeping all sessions. Upgrade and network-change restarts keep every address the old server served in the same way, except an address that is no longer on this machine. Switching to an address the running server already serves, including loopback, reuses it, so run `lavish-axi stop` first to drop an address. Another server of the same installation (the same state directory) found on the same port at a different address is shut down through its own shutdown endpoint, after the kept server is made to serve that address too, so review links already handed out there keep working. A server belonging to another state directory that reports its installation identity is never used, replaced, or stopped: when it holds loopback or the configured address, the CLI fails with an error naming its state directory, so pick another `LAVISH_AXI_PORT`. Older servers that cannot report an identity are treated as belonging to this installation only at those control addresses, for upgrade compatibility.
- **Allowed hosts** - To defend against DNS rebinding, the server rejects (`403`) any request whose `Host` header is missing or not one it answers to: loopback names plus the concrete Tailscale IPv4 address and MagicDNS name when the Tailscale listener is successfully bound. If you configure a reverse proxy or another intentional hostname, list it in `LAVISH_AXI_ALLOWED_HOSTS` (whitespace-separated). Behind a reverse proxy, the forwarded `X-Forwarded-Host` is validated against the same list, so add the public hostname there and have the proxy send it together with `X-Forwarded-Proto`. Set `LAVISH_AXI_ALLOWED_HOSTS` to `*` to disable the check entirely, only when the server sits behind your own authentication or proxy. Mutating routes also reject a present foreign `Origin` or `Referer` (`403`); header-less CLI control requests remain allowed where supported.
- **Browser opening** - Set `LAVISH_AXI_NO_OPEN=1`, equivalent to `--no-open`, to create or resume a session without launching a browser window.

## CLI Reference

| Command                         | Description                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lavish-axi`                    | Show current sessions and usage guidance.                                                                                                                                                                                                                                                                                                                 |
| `lavish-axi update`             | Check for or apply the latest npm release through the AXI SDK self-updater.                                                                                                                                                                                                                                                                               |
| `lavish-axi <html-file>`        | Open or resume a Lavish Editor session, with the open-time layout gate enabled by default. Unresolved layout issues from earlier in the session are preserved. Refuses to reopen a session the user explicitly ended from the browser unless `--reopen` is passed.                                                                                        |
| `lavish-axi poll <html-file>`   | Long-poll until the user sends feedback, ends the session, or leaves every review disconnected past the reconnect grace period; detected layout issues arrive only when queued. On `browser_disconnected`, ask before reopening or ending the still-resumable session. On `ended`, stop polling and do not reopen uninvited.                              |
| `lavish-axi reply <html-file>`  | Post an agent reply and exit 0 only after the server accepts it, so the review page stops showing Working. Exits non-zero if the server does not confirm within 10 seconds. Use this when handing a result back without starting a long-poll. `poll --agent-reply` still posts a reply and then waits.                                                    |
| `lavish-axi end <html-file>`    | End a session as the agent; unlike a user-initiated end from the browser, this still allows a plain reopen later.                                                                                                                                                                                                                                         |
| `lavish-axi export <html-file>` | Write a portable copy of the artifact: one HTML file with its local assets inlined, so it opens with no server and no sibling files. Remote CDN/font references are left as links.                                                                                                                                                                        |
| `lavish-axi share <html-file>`  | Publish the artifact (local assets inlined) to [ht-ml.app](https://ht-ml.app), a third-party host not part of Lavish, and print a visitable URL plus a secret update key; shares are public by default, `--private` locks one behind a generated password, and the same command republishes or unpublishes an existing page with `--site`/`--update-key`. |
| `lavish-axi stop`               | Shut down the background server.                                                                                                                                                                                                                                                                                                                          |
| `lavish-axi playbook [id]`      | List focused artifact guidance or show one playbook; agents must open each matching playbook before writing HTML.                                                                                                                                                                                                                                         |
| `lavish-axi libraries`          | List the Excalidraw libraries in the whiteboard library directory; `--search <text>` or `--library <id>` lists item refs for `%% lavish-icon` nodes.                                                                                                                                                                                                      |
| `lavish-axi design`             | Show agent-facing design guidance, including optional CDN snippets and the whiteboard (Mermaid) opt-in snippet.                                                                                                                                                                                                                                           |
| `lavish-axi setup hooks`        | Install or repair optional SessionStart hooks for Claude Code, Codex, OpenCode, and GitHub Copilot CLI; restart the agent session afterward.                                                                                                                                                                                                              |
| `lavish-axi setup plugin`       | Register the installed package as an [Agent Plugin](https://agent-plugins.org) in VS Code, Cursor, and GitHub Copilot CLI; opt-in, idempotent, no marketplace involved. Reload each client afterward.                                                                                                                                                     |
| `lavish-axi server`             | Run the local Lavish Editor server.                                                                                                                                                                                                                                                                                                                       |

Known playbook IDs: `diagram`, `table`, `comparison`, `plan`, `code`, `input`, `explanation`, `slides`.
One artifact often combines several playbooks, such as a plan that includes a comparison and a diagram, so agents must match against each `use_when` trigger and open every matching playbook before writing HTML.
For flows, architecture, state, or sequence diagrams, open the diagram playbook for the recommended tooling and SVG guidance.

### Flags

| Command                  | Flag                        | Description                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lavish-axi <html-file>` | `--no-open`                 | Ensure the server/session exists without opening another browser window.                                                                                                                                                                                                                                                      |
| `lavish-axi <html-file>` | `--no-gate`                 | Skip the open-time layout curtain for this browser open.                                                                                                                                                                                                                                                                      |
| `lavish-axi <html-file>` | `--reopen`                  | Reopen a session the user explicitly ended from the browser; without it, a plain open refuses and explains why instead of reopening uninvited.                                                                                                                                                                                |
| `lavish-axi update`      | `--check`                   | Report current vs latest npm version without installing an update.                                                                                                                                                                                                                                                            |
| `lavish-axi export`      | `--out <path>`              | Write the export to a specific path instead of `<name>.export.html` next to the source.                                                                                                                                                                                                                                       |
| `lavish-axi share`       | `--private`                 | Make the page private behind a password Lavish generates and returns once; hand it to viewers as a shared secret.                                                                                                                                                                                                             |
| `lavish-axi share`       | `--password <pw>`           | Make the third-party ht-ml.app page private with a password you supply; viewers must supply the password. An empty or whitespace-only value (an unquoted `$PW` that is unset) is refused rather than publishing a public page.                                                                                                |
| `lavish-axi share`       | `--site <site_id>`          | Republish an existing page in place (with `--update-key`) instead of creating a new one; the URL does not change.                                                                                                                                                                                                             |
| `lavish-axi share`       | `--update-key <key>`        | The secret returned when the page was published; required to republish or unpublish it.                                                                                                                                                                                                                                       |
| `lavish-axi share`       | `--unpublish`               | Replace a published page with a locked placeholder (ht-ml.app cannot delete); takes `--site` and `--update-key` and no file.                                                                                                                                                                                                  |
| `lavish-axi share`       | `--token <t>`               | Attach an optional bearer token (`LAVISH_AXI_HTML_APP_TOKEN`) when creating a page; never required, and rejected on a republish or `--unpublish`, where the `update_key` is the credential.                                                                                                                                   |
| `lavish-axi poll`        | `--owner <label>`           | Identify the process listening for this session; the non-empty label appears in the home session listing. `none` is reserved for sessions without a listener. A second concurrent poll is refused instead of silently returning `waiting`.                                                                                    |
| `lavish-axi poll`        | `--takeover`                | Explicitly displace the current poll listener. The displaced poll exits with typed `LISTENER_REPLACED`; without this flag, the new poll fails with typed `LISTENER_ACTIVE`.                                                                                                                                                   |
| `lavish-axi poll`        | `--agent-reply "..."`       | Show a concise agent reply in the existing browser chat, conclude delivered work (every note the agent has seen is marked Done), and return presence to waiting before polling again. Keep replies concise by default.                                                                                                        |
| `lavish-axi poll`        | `--agent-reply-file <path>` | When a longer reply is genuinely necessary, read Markdown from a file (`-` for stdin) so newlines survive quoting. Use blank-line paragraphs, `- ` / `1. ` lists, and `## ` headings so the Conversation panel renders it scannably. The Markdown subset is under Feedback controls. Cannot be combined with `--agent-reply`. |
| `lavish-axi poll`        | `--timeout-ms <ms>`         | Test/debug escape hatch only; agents should normally omit it and leave the long poll running.                                                                                                                                                                                                                                 |
| `lavish-axi reply`       | `--agent-reply "..."`       | Concise reply text. Required unless `--agent-reply-file` is set. The command exits 0 only after the server accepts it. Empty text is refused. Prefer this over `poll --agent-reply` when you are not about to long-poll.                                                                                                      |
| `lavish-axi reply`       | `--agent-reply-file <path>` | Read the reply from a file (`-` for stdin) so newlines survive quoting. Cannot be combined with `--agent-reply`. Same Markdown guidance as `poll --agent-reply-file`.                                                                                                                                                         |
| `lavish-axi stop`        | `--port <port>`             | Shut down a server running on a non-default port.                                                                                                                                                                                                                                                                             |
| `lavish-axi server`      | `--verbose`                 | Log session and watcher events to stderr; can also be enabled with `LAVISH_AXI_DEBUG=1`. Detached server output is appended with UTC timestamps to `~/.lavish-axi/server.log` (or `LAVISH_AXI_STATE_DIR/server.log`) for startup, shutdown-cause, and crash diagnostics.                                                      |
| `lavish-axi server`      | `--also-listen <host>`      | Also listen on this concrete address (repeatable). The CLI passes it when it replaces a running server, so the replacement keeps every address the old one served; see One server per port.                                                                                                                                   |

## Telemetry

The npm release sends anonymous usage telemetry to an [Umami](https://umami.is) server at `https://a.kunchenguid.com`. The host and website ID are baked into the published bundle at build time, so telemetry is on by default for `npx -y lavish-axi`.

Each `lavish-axi` run sends two requests, except `lavish-axi --version` (also `-v` and `-V`), which sends none: a page view when the command starts, and a `command` event when it finishes. Both carry:

- the command name (for example `open`, `poll`, or `home` when you run it with no command), but not its arguments, file paths, artifact content, or prompts
- the Lavish version, `process.platform`, and `process.arch`

The `command` event also carries a `status` field: `success`, or `error` only when the CLI itself throws. A command that fails and sets a nonzero exit code is handled by the CLI framework, so it still reports `success`. No user identifier is sent. Requests time out after 1 second, and failures are ignored, so telemetry never changes what a command does.

Set `LAVISH_AXI_TELEMETRY=0` (or `false` or `off`) to turn it off. A build from source sends nothing unless `LAVISH_AXI_UMAMI_WEBSITE_ID` is set, and `LAVISH_AXI_UMAMI_HOST` overrides the host.

## Development

```sh
pnpm run check          # Run all verification commands
pnpm run build          # Bundle the publishable CLI, chrome, and design assets
pnpm run build:skill    # Regenerate the installable lavish skill
pnpm test               # Run node:test tests
pnpm run lint           # Run ESLint
pnpm run format:check   # Check Prettier formatting
pnpm run typecheck      # Run TypeScript checkJs validation
```


## Docs

### AGENTS.md
# AGENTS.md

This file is loaded every session. It keeps only rules that apply to almost every change. Detail lives in the doc that owns it.

- [README.md](README.md) owns the user-facing contract: features, CLI flags, environment variables, keyboard shortcuts, export and share, and session-end etiquette.
- CLI output owns what agents are told while using Lavish: `lavish-axi --help`, `lavish-axi design`, and `lavish-axi playbook <id>` (`src/cli.js`, `src/design-reference.js`, `src/playbooks.js`). The generated skill (`src/skill.js` to `skills/lavish/SKILL.md`) stays a stub that points at those commands. Do not copy CLI-owned instructions into the skill.
- [VISION.md](VISION.md) owns the acceptance policy. Change it only through the author.
- [docs/invariants.md](docs/invariants.md) owns architecture internals, security rationale, and easy-to-reintroduce failure modes. Read the section for the area you are editing before changing it.
- Update the owner when a contract changes. Edit this file only when an every-session rule changes.

## Commands

```sh
pnpm run check          # build, lint, format check, typecheck, tests, and skill freshness
pnpm run build          # bundle dist/cli.mjs and copy chrome/design assets into dist
pnpm run build:skill    # regenerate skills/lavish/SKILL.md from src/skill.js
pnpm test               # node:test runner (test/*.test.js)
pnpm run lint           # ESLint over bin src test scripts
pnpm run format:check   # Prettier check
pnpm run typecheck      # tsc --noEmit (checkJs)
```

One file: `node --test test/server.test.js`. One name: `node --test --test-name-pattern "createOpenOutput" test/cli-output.test.js`.
Opt-in browser suites need `chrome-devtools-axi`: `LAVISH_AXI_BROWSER_E2E=1 node --test test/layout-audit-browser.test.js test/layout-warning-inbox.browser.test.js`.
Seven-tab pool regression: `LAVISH_AXI_BROWSER_E2E=1 node --test test/event-transport.browser.test.js`.
`prepack` and `prepare` both run `build`. `pnpm run check` fails if `skills/lavish/SKILL.md` drifts from `createSkillMarkdown()`, or if root `plugin.json` drifts from `pnpm run build:plugin`. Release-please bumps `plugin.json` through `extra-files`.

## Project conventions

- Node 22+, ESM-only JavaScript (`"type": "module"`). No TypeScript source. `.js` files are validated with `checkJs`.
- Use TDD for bug fixes and new features (see the `test-driven-development` skill).
- Run `pnpm run check` before pushing.
- Treat repo-provided `.agents/` skill content as vendored. Prettier ignores it.
- Do not hand-edit `CHANGELOG.md` or `.release-please-manifest.json`. Release-please owns them.
- Human-authored PRs to `main` go through [no-mistakes](https://github.com/kunchenguid/no-mistakes) >= 1.46.0. [CONTRIBUTING.md](CONTRIBUTING.md) owns the gate, the attestation contract, and the workflow-pin rules.
- Tests that start the server set `LAVISH_AXI_STATE_DIR` and use an ephemeral port.
- `run()` returns on `--version` / `-v` / `-V` before `ensureStateDir` and telemetry (`test/cli-version.test.js`). New startup work goes after that short-circuit.
- `canonicalFile` runs `realpath`. Two paths to the same file are one session.
- `normalizeArgv` must let AXI `RESERVED_COMMANDS` (including `update`) pass through. A bare `lavish-axi update` must not become `open update`.

## Safety and correctness

Each line is the rule. [docs/invariants.md](docs/invariants.md) has the failure mode.

- The session key is the canonical artifact path. It is not a secret. No route may treat key possession as authorization. [Process model](docs/invariants.md#process-model).
- Never signal a listener by port alone. Stop only a Lavish PID bound to that exact address, or `POST /shutdown` on an owned server. [Process model](docs/invariants.md#process-model).
- Adopt, replace, or stop only a server `isOwnedServer` owns. Another installation's server at a control address is a `SERVER_ERROR`, never used, replaced, or stopped. [Process model](docs/invariants.md#process-model).
- Every server replacement passes all previously requested hosts through `inheritedListenHosts` (`--also-listen`), dropping only IPs no longer on a local interface. [Process model](docs/invariants.md#process-model).
- Loopback is always requested. An unresolvable `LAVISH_AXI_HOST` is kept (`keepUnresolved`) and retried, never silently dropped. [Process model](docs/invariants.md#process-model).
- A wildcard listen request becomes loopback, and an alias that resolves to an all-interfaces address is refused. Never open a wildcard listener. [Process model](docs/invariants.md#process-model).
- Health probes use `node:http` and destroy the socket on every exit. Do not use `fetch`. [Process model](docs/invariants.md#process-model).
- Loopback binds first and is the port lock. A failed requested address stays in `pendingBinds` and is retried. Declare request-handler timers before the first bind. [Process model](docs/invariants.md#process-model).
- Host allowlist, then Origin/Referer guard. Header-less CLI control requests must keep working. `*` skips hostname membership and still rejects a malformed forwarded authority. [Process model](docs/invariants.md#process-model).
- Live-event WebSockets keep the ping/pong heartbeat so half-open sockets terminate. Idle self-shutdown keys off tracked live connections, not session status. [Process model](docs/invariants.md#process-model).
- The detached server entrypoint logs `uncaughtException` and exits 1 explicitly. Each listener keeps its `error` handler after `listening`. [Process model](docs/invariants.md#process-model).
- `/api/:key/prompts`, `/share`, whiteboard writes, and attachment upload/delete are same-origin guarded. The key alone must never queue a prompt or publish. [Request flow](docs/invariants.md#request-flow).
- Poll control `GET` and `POST` requests reject a present foreign Origin or Referer while header-less CLI requests keep working. [Request flow](docs/invariants.md#request-flow).
- The chrome page (`/session/:key`) answers `X-Frame-Options: DENY` and `frame-ancestors 'none'`. Keep that header off `/artifact/*` and `/whiteboard-frame`, which are framed. [Request flow](docs/invariants.md#request-flow).
- The artifact route injects only the one SDK `<script>` tag. Served artifact bytes otherwise match the file on disk. [Request flow](docs/invariants.md#request-flow).
- `/api/sessions` refuses a path that is not a regular `.html`/`.htm` file after `realpath`. [Request flow](docs/invariants.md#request-flow).
- Artifact asset serving (`/artifact/:key/<path>`) stays inside that session's HTML-file directory, resolves with `realpath`, and never serves a symlink target outside that tree. [Request flow](docs/invariants.md#request-flow).
- Layout detection never emits `feedback`. Only a user prompt and the narrow fatal artifact-failure path may wake `lavish-axi poll`. [Request flow](docs/invariants.md#request-flow).
- Layout-diagnostics reports are fire-and-forget and never hold the artifact behind a round-trip. Ordinary layout findings are never relabelled fatal. [Request flow](docs/invariants.md#request-flow).
- The chrome mints each queued prompt's `prompt_id` (never from the iframe) and removes a queued note only when the transcript acknowledges that id. Evicted ids stay on `chat_ack_ids`. [Request flow](docs/invariants.md#request-flow).
- Only agent chat entries render as HTML. User entries are always escaped. [Request flow](docs/invariants.md#request-flow).
- A note's Sending state is derived from the existing send bookkeeping, never tracked separately. [Request flow](docs/invariants.md#request-flow).
- `/api/:key/prompts` rejects every new batch for an ended session. Only the internal `restore` replay is exempt. [Request flow](docs/invariants.md#request-flow).
- A session the user ended never reopens without explicit opt-in (`reopen: true`, the CLI's `--reopen`). [Request flow](docs/invariants.md#request-flow).
- Poll ownership is exclusive per session in `activePolls`. Takeover installs the new holder before releasing the old one, and claims, including the reply write, serialize through `pollOwnershipLock`. [Request flow](docs/invariants.md#request-flow).
- Every poll exit path undoes the presence it set and cancels the disconnect grace timer. `/api/poll` subscribes to closure before its first `await`. [Request flow](docs/invariants.md#request-flow).
- Poll stdout is reserved for the final JSON/TOON response. Recurring wait ticks go to stderr only on a TTY, and notification failure never affects the poll. [Request flow](docs/invariants.md#request-flow).
- The chrome never promotes presence to `working` on send. It renders only the state the live stream reports. [Request flow](docs/invariants.md#request-flow).
- Poll feedback field order is `prompts`, `artifact_failures`, `next_step`, then `dom_snapshot`. Never move `next_step` after the snapshot. [Request flow](docs/invariants.md#request-flow).
- `takeFeedback` is destructive. A disconnected poll restores through `queuePrompts` `restore`: prepend, do not re-plan, re-emit `feedback`, and exempt only the request-wide attachment-ref cap. [Request flow](docs/invariants.md#request-flow).
- A disconnected-poll restore never overwrites a newer `dom_snapshot` or `artifact_failures` recorded after the take. [Request flow](docs/invariants.md#request-flow).
- A layout warning clears only on a newer artifact revision plus a complete pass at the same viewport class. Do not emit `feedback` for a detection. [Passive layout-warning inbox](docs/invariants.md#passive-layout-warning-inbox).
- The chrome never decides that a warning went away. Display strings come from `serializeLayoutWarnings`. [Passive layout-warning inbox](docs/invariants.md#passive-layout-warning-inbox).
- The active artifact load is durable in `session.artifact_load`. Only a newer `beginArtifactLoad` retires it, and only an explicit takeover reload replaces a superseded reviewer. [Passive layout-warning inbox](docs/invariants.md#passive-layout-warning-inbox).
- Reload and gate recovery probe `/health` before navigating. Do not call `location.reload()` directly for these recovery actions; the superseded-reviewer takeover card may reload directly after its 409 response. Sticky "Lavish is not running." copy is never cleared by a later successful load. [Live reload](docs/invariants.md#live-reload).
- Every recovery `/health` probe is bounded by an abort timeout, and its caller restores the control whether the probe answers, fails, or times out. [Live reload](docs/invariants.md#live-reload).
- Sticky copy never makes the gate overlay sticky. Every failure card keeps the bounded timeout and the **Show anyway** bypass. [Live reload](docs/invariants.md#live-reload).
- Shutdown banner text must be true for the `reason` that fired. Idle shutdown reloads nothing. [Live reload](docs/invariants.md#live-reload).
- `chrome-outdated` never reloads by itself, and a restart shows the banner instead of reloading while an unsent draft exists. The log-only shutdown `cause` is never widened into `reason`. [Live reload](docs/invariants.md#live-reload).
- Review-state restore sets values directly and dispatches no synthetic `change`/`input` events. [Live reload](docs/invariants.md#live-reload).
- A stored annotation draft is retired only after two artifact revisions report its selector missing. A retired draft is kept verbatim in `lavish-axi:retired-drafts:<key>` and never trimmed. [Live reload](docs/invariants.md#live-reload).
- The whiteboard channel token is not a secret. Trust is session-key binding plus descent from the artifact frame (`isArtifactChildWindow`). [Whiteboard](docs/invariants.md#whiteboard-mermaid-excalidraw).
- `/whiteboard-frame` stays framable by any origin and requires `?key=`. The channel token is signed over the session key. [Whiteboard](docs/invariants.md#whiteboard-mermaid-excalidraw).
- Whiteboard scenes persist in per-diagram sidecars, never in `state.json`. Stale user edits are never silently merged, and `handleInit` goes through `resolveWhiteboardInitAction`. [Whiteboard](docs/invariants.md#whiteboard-mermaid-excalidraw).
- Mermaid source stays authoritative. There is no scene-to-Mermaid reverse conversion. `mermaid` is pinned exactly. Persisted Excalidraw `appState` must not carry `theme` or a dark `viewBackgroundColor`. [Whiteboard](docs/invariants.md#whiteboard-mermaid-excalidraw).
- `/whiteboard-assets/*` keeps `Access-Control-Allow-Origin: *` so fonts load in the opaque-origin frame, plus `Cache-Control: no-cache` and sendFile `dotfiles: "allow"`. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Mermaid skeletons re-materialize after Excalidraw fonts load, saved-scene repair is expansion-only, and `restoreMermaidLabelLineBreaks` runs before `convertToExcalidrawElements`. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Every store mutation takes `store.lock`. `referencedAttachmentIds` stays lock-free. [Image attachments](docs/invariants.md#image-attachments).
- Attachment identity is the content-addressed file. `queuePrompts` re-derives path, mime, bytes, and dimensions from disk. Resolution is all-or-nothing. `boundAttachmentRefs` runs before any filesystem await. [Image attachments](docs/invariants.md#image-attachments).
- Uploads are magic-byte validated and ignore `Content-Type`. Accepted types derive from `ACCEPTED_IMAGE_MIME`, never a second hardcoded list. [Image attachments](docs/invariants.md#image-attachments).
- Upload results bind to the requesting document by `ATTACHMENT_NONCE` plus `event.source === parent`. [Image attachments](docs/invariants.md#image-attachments).
- An oversized file is decided `error` before its bytes are read. [Image attachments](docs/invariants.md#image-attachments).
- The composer notice is derived on every render, paste and drop go through `transferredFiles`, and the chip send gate holds back only the composer's own message and an explicit end. [Image attachments](docs/invariants.md#image-attachments).
- Do not put a body-parser `limit` on the attachment upload route. Drain the body, then 413. The chrome is the confused deputy for iframe uploads and shares one page-wide budget with the composer. [Image attachments](docs/invariants.md#image-attachments).
- Removing a chip never deletes an attachment. Only the reference-aware sweeper and the same-origin `DELETE` route for unreferenced attachments delete. No iframe-driven delete. Cap admission goes through `admitAttachmentCharge` and charges allocated blocks. [Image attachments](docs/invariants.md#image-attachments).
- The sweeper never removes a referenced attachment (references include the delivery grace): TTL cleanup reaps an unreferenced file past the TTL, and disk or object-cap pressure may evict an unreferenced file earlier once it is older than `ATTACHMENT_EVICTION_GRACE_MS`. [Image attachments](docs/invariants.md#image-attachments).
- Attachment admission runs under the store lock and refuses with 507. `maxObjects` derives from the disk budget, and `removeAttachment` deletes the sidecar first. [Image attachments](docs/invariants.md#image-attachments).
- A dedup upload's mtime refresh is never swallowed into success. Env limits floor before the bounds check and require `>= 1`, and only `0`/`off` disables one. [Image attachments](docs/invariants.md#image-attachments).
- Attachment files and dirs are owner-only (`0600`/`0700`), set explicitly at creation and re-asserted by `ensureAttachmentDir`. [Image attachments](docs/invariants.md#image-attachments).
- Export makes no outbound requests. Local reads stay inside the artifact directory after `realpath`. A symlink must not escape. [Export (local-asset inlining)](docs/invariants.md#export-local-asset-inlining).
- Export and share inline confined same-directory resources and redact every other absolute `file://` URL to `about:blank` so local paths never leak. [Export (local-asset inlining)](docs/invariants.md#export-local-asset-inlining).
- Exports strip the injected SDK and escape inlined `</script>`/`</style>`. Hosted shares never include the SDK. [Export (local-asset inlining)](docs/invariants.md#export-local-asset-inlining).
- `--unpublish` is not a deletion. There is no clear-password path. Empty share flag values are refused. A lost create response must not offer a recovery the host cannot perform. Suggested commands never contain a password placeholder. [Hosted sharing (ht-ml.app)](docs/invariants.md#hosted-sharing-ht-mlapp).
- Share passwords are minted only in `src/share-password.js`. Lavish persists neither the password nor `update_key`. [Hosted sharing (ht-ml.app)](docs/invariants.md#hosted-sharing-ht-mlapp).
- The share route echoes a password only when it minted one. [Hosted sharing (ht-ml.app)](docs/invariants.md#hosted-sharing-ht-mlapp).
- Share writes classify failure through `hostRejectedShareWrite`, where only a 4xx proves nothing landed. An echoed `site_id` is untrusted, and recovery commands come only from `republishCommand`/`unpublishCommand`. [Hosted sharing (ht-ml.app)](docs/invariants.md#hosted-sharing-ht-mlapp).
- Every surface reporting a page as newly gated carries the CDN public-to-private caveat. [Hosted sharing (ht-ml.app)](docs/invariants.md#hosted-sharing-ht-mlapp).
- `DESIGN_PRIORITY_RULE` is stated once in `src/design-reference.js`. Do not restate it. Do not hardcode one Mermaid theme. [AXI integration](docs/invariants.md#axi-integration).
- Poll wake-path guidance comes only from `POLL_WAKE_PATH_RULES`. [AXI integration](docs/invariants.md#axi-integration).
- The internal brand skill keeps `metadata.internal: true`. The generated skill omits a `version` frontmatter field. [AXI integration](docs/invariants.md#axi-integration).
- `plugin.json` and `skills/lavish` stay in `package.json` `files`. Skill frontmatter stays inside `validateSkillMarkdown`'s allowed shape. An unlinkable plugin client is reported, never thrown. Do not ship `mcp.json`. [Agent Plugins packaging](docs/invariants.md#agent-plugins-packaging).
- Plugin setup runs only on explicit invocation, drops only locations `isStalePluginLocation` attributes to this plugin, and never rewrites unparseable VS Code settings. [Agent Plugins packaging](docs/invariants.md#agent-plugins-packaging).
- Telemetry is best-effort and must never affect CLI behavior. Users opt out with `LAVISH_AXI_TELEMETRY=0`. [Telemetry](docs/invariants.md#telemetry).
- Every artifact-to-chrome message goes through `postArtifactMessage`. The artifact iframe stays sandboxed without `allow-same-origin`. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Every `/artifact/*` response carries the CSP `sandbox` policy matching the iframe, so an escaped popup stays opaque-origin. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- SDK helpers that the browser must call are exported functions in a module `serializeModuleHelpers` inlines. No module-level constants. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Serialized SDK helper modules export only functions. `serializeModuleHelpers` throws on any other export. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Mermaid pan and zoom touch only the live SVG `viewBox`, never the saved artifact. `normalizeMermaidNodeTarget` strips node targets to their fixed shape. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Table-cell annotations name a row or column only when it is provable and stay silent otherwise. `snapshot()` never computes table targets. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- A text annotation's `prompt.selector` names the container, not the selected range. Never target text by selector alone. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Annotation handlers ignore native controls, editable regions, and `data-lavish-action` elements. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- `resetRevisionLegend()` runs only when `replaceArtifactFrame` actually assigns `frame.src`. Reject over-long revision ids and selectors. Lookups use `Map`/`Set`. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- The revision legend's per-row cap derives from `revisionPalette()` length, never a second number. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- A keyboard shortcut that must work in both chrome and the artifact needs a capture-phase listener in both `src/chrome-client.js` and `src/artifact-sdk.js`, and it requires a modifier. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- `MOBILE_SHEET_MEDIA` matches the CSS phone breakpoint, and the collapsed sheet is a `translateY`, never a height change. The desktop `panel-collapsed` class never applies at phone width. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- `CHROME_BOOT_FAILSAFE_JS` stays inlined before the `<script src="/chrome-client.js">` tag so the gate escape works when the client script hangs. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- A recoverable first artifact load retries through `ARTIFACT_LOAD_RECOVERY_DELAYS_MS` and then surfaces `setLayoutGateFailure`. `superseded` and `out-of-order` never retry. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- Self-paint stays a warning. Never block open and never auto-repair. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- The layout audit fails open. An empty completed pass means repaired. A failed run publishes `complete: false` and no findings. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).
- The layout audit is severe-only. Scroll dimensions alone are never proof, diagram surfaces are excluded, and a finding needs the same severe root in two samples. [Things to know when editing](docs/invariants.md#things-to-know-when-editing).

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.


### VISION.md
# Vision

`lavish-axi` exists so that a person reviewing what an agent rendered can point at it and be understood exactly.
It is operated by the agent and serves the collaboration between that agent and its human user, turning the person's pointing, selecting, drawing, and typing into instructions the agent receives as their own words.
It owns exactly one thing: the review loop between one person and one agent over one local HTML file.

## The artifact stays the author's

The saved HTML file is the source of truth, and serving it adds exactly one script tag and nothing else.
Nothing else is injected, because an artifact must render identically when it is opened directly with Lavish absent.
A rendered Mermaid diagram can be edited as a whiteboard, but the Mermaid source stays authoritative and the edits return as a summary the agent applies to that source.
Export inlines local assets only and makes no outbound request, so exporting can never become fetching.
A change that makes the served artifact differ from the file on disk is refused.

## Interaction beats prose

An artifact earns its format by letting the reader understand and answer through the page itself instead of through a wall of text.
Elements that can be pointed at, diagrams that can be drawn on, and controls that collect an answer are the substance; any one of them, the whiteboard included, is an instance of that and not a feature in its own right.
A page that could have been a paragraph should have been a paragraph.

## An artifact's design is chosen, never defaulted into

An agent picks a design direction deliberately, in a stated priority order, and says which source it used.
The artifact matches the project it is about before it matches anything Lavish would prefer.
Lavish may offer building blocks that are correct by construction, and they stay opt-in, written in by the artifact's author, and reachable when Lavish is not running.
An artifact that arrives styled at random is a defect in Lavish's guidance before it is a defect in the agent.

## Nothing interrupts the human

Time to first interaction is the number that matters, and every check is weighed against the friction it adds for the person waiting.
Detection is passive: Lavish files what it finds where the user can see it, and only the user selecting an issue turns it into work.
No detection wakes the agent, returns a poll, or repairs anything; the single exception is a failure that leaves the human nothing to review, where waiting on them to act is pointless.
Every check fails open, because a false warning on every open costs more than a miss, and a cosmetic finding is never worth a blocked page.
Only a deliberate human action in the browser becomes feedback the agent receives.
A warning is cleared by a fresh artifact load and a check that no longer finds it, never by the user being asked to declare it settled.
A check that blocks the review, edits the artifact, or nags persistently is removed, and machinery that no longer does the job it was built for is deleted rather than kept.

## Every token is spent on purpose

Token efficiency is a first-class concern rather than a later optimization pass.
Output is compact, waiting is a long poll instead of repeated checks, and guidance is disclosed when it is needed rather than all at once.
A surface that costs the agent tokens on every run has to earn them on every run.
Efficiency is never bought with capability: a rule moves behind a command only once agents are shown to follow the pointer, never on the assumption that they will.
Work a capable agent already does is not rebuilt inside Lavish and then explained back to it.

## The instructions are the product

Lavish is a CLI an agent discovers by running it, so its output is an interface and not documentation.
Every behavior contract has exactly one owner surface, and every other surface points at it instead of restating it.
The installable skill is a generated stub that points at the CLI for all actual guidance, and the build fails when that stub drifts from its generator.
When agents behave badly, changing what Lavish tells them is a real fix and is preferred over new machinery.
Guidance steers the agent's judgment and stops short of rigid rules it can satisfy without thinking.
Lavish keeps its own files in its own places and never modifies a file the user or another tool owns without being asked, because that trust is spent once.

## Scope

The review loop runs on the user's machine, and anything that leaves it is opt-in, named, and disclosed at the moment it happens.
Lavish reviews HTML, and it does not adopt Markdown, PDFs, or images by wrapping them in a page that has no saved file behind it.
It is one person and one agent, however many windows or screens that person uses; it is not a place for two people to collaborate with each other.
It is not a hosting service, and publishing goes to a named third party that is never on by default.
It expects to run inside an agent harness, and the long poll is how that harness holds a continuous session; Lavish does not launch, drive, or supervise the agent itself.
It is not an MCP server and it has no marketplace, because the CLI is already the agent interface and an installed copy is already complete.
It does not translate a whiteboard back into Mermaid, and it does not repair artifacts on the user's behalf.

A change aligns when it carries a human's intent to the agent more precisely, when it keeps the artifact portable and the review uninterrupted, and when it lands in the one surface that already owns the contract it touches.
A change should be resisted when it acts on the artifact without the reviewer asking, when it makes the served artifact diverge from the saved file, when it spends the agent's tokens or the human's waiting time without earning them, or when it quietly widens Lavish past one person, one agent, and one local HTML file.


### docs/delivery-acks.md
# Delivery acks: seen, working, done per request

Design note for per-request delivery state in the Conversation panel. [README.md](../README.md) owns
the user-facing wording once this ships; [invariants.md](invariants.md) owns the stamping rules.

## Problem

A reviewer sends a note and cannot tell whether anything picked it up. Today the panel has one
session-wide signal - the `agent-presence` stream (`waiting` / `listening` / `working`) and the
"Working..." bubble - and a sent note looks identical whether it is sitting undelivered in
`state.json`, has been handed to a poll, or was answered an hour ago.

## What Lavish can already observe

Every state below is a fact the server records anyway. None of them asks the agent to do anything new.

| Signal                   | Where it is observed                                                                   | Means                                            |
| ------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `/api/:key/prompts` 200  | `SessionStore.queuePrompts` appends the note to `session.chat`                         | **Sent** - the server holds it for the next poll |
| no poll in `activePolls` | `computePresence` is `waiting`; the chrome already shows "Your agent is not listening" | nobody is there to receive it                    |
| `takeFeedback` succeeded | the store drained the batch for a poll; a poll that closed before the write undoes it  | **Seen** - the batch was handed to a poll        |
| artifact file changed    | chokidar `reload` for the session key after a delivery                                 | **Working** - the agent is editing the artifact  |
| `addAgentReply`          | `lavish-axi reply` / `poll --agent-reply`, or `/api/:key/agent-reply`                  | **Done** - the agent handed something back       |

Two of Wally's three acks ("I saw it", "I'm done") fall straight out of the existing protocol.
"I'm working on it" has no explicit message, but the file watcher sees the agent's saves. A request
that is answered without touching the artifact goes Seen -> Done with Working never ticked, which is
true, not a gap.

## States per request

```
queued ──send──> sent ──poll takes it──> seen ──artifact changes──> working ──agent reply──> done
 (tab)          (server)                 (agent)                    (agent)                  (agent)
```

- **queued**: in the tab only (dashed bubble). Unchanged.
- **sent**: a `role: "user"` chat entry with no `delivered_at`. The bubble says why it has not been
  seen, from the live presence the chrome already holds: "No agent is listening" (`waiting`),
  "Agent is busy; delivered on its next poll" (`working` / external listener), or "Delivering"
  while a poll is attached, which lasts milliseconds.
- **seen**: `delivered_at` set by `takeFeedback`.
- **working**: `working_at` set by the first artifact `reload` after delivery. Optional evidence.
- **done**: `done_at` set by the next agent reply.

## Storage and stamping rules

Stamps live on the chat entry (`session.chat[i]`), which already outlives the delivered prompt and is
what the chrome renders. `serializeChat` spreads the entry, so `initialChat` and `chat-sync` carry
the stamps with no new wire shape.

- **Delivery stamps by position, not by id.** `agentFacingPrompt` strips `prompt_id` from stored
  prompts at queue time, so ids are gone by the time `takeFeedback` runs. A take drains every
  pending prompt, and `queuePrompts` runs under the same store lock, so inside `takeFeedback` the
  set "user entries with no `delivered_at`" is exactly the batch being delivered. Each take increments
  `session.delivery_seq` and writes it as `delivered_seq` on the entries it stamps.
- **A disconnected poll un-stamps its own take only.** `restoreClosedFeedback` passes the take's
  `delivery_seq` back; `queuePrompts` in `restore` mode deletes the stamps on entries carrying that
  sequence (delete, not null - the restore tests assert `chat` deep-equals its pre-take shape). Notes
  queued in the window keep no stamp and are delivered, and stamped, by the next take. A restore that
  is refused (an attachment no longer resolves) cannot put the prompts back, and still takes the
  stamps off: the note is lost, and a Seen left on it would claim a delivery that never happened.
- **Working stamps delivered-and-not-done entries.** `markWorking(key)` runs on the `reload` event. A
  reload with nothing delivered changes nothing and writes nothing.
- **Done stamps delivered-and-not-done entries.** `addAgentReply` does it in the same write as the
  reply. An entry that was sent but never delivered is not marked done: the agent has not seen it.
- **Working and Done stay inside one review round.** Reopening an ended session records the last
  take so far as `session.closed_delivery_seq`, and neither stamp lands on an entry delivered at or
  before it. A note `lavish-axi end` left at Seen stays Seen: a later round's edit or reply is about
  that round's notes.
- **Every stamp change bumps `chat_revision`.** `syncChat` in the chrome accepts a same-revision sync
  only when it contains the displayed entries; a higher revision is what makes it take the
  authoritative replacement.
- `delivery_seq` is a session field, so `#upsertSessionLocked` carries it across a reopen like
  `chat_revision`. Stamps on `chat` entries survive because `chat` is carried verbatim.
- The server publishes `chat-sync` on the success path of a delivery (`finishFeedbackDelivery`) and
  after a restore, never on the destructive take itself, so a tab is not told Seen for a batch that
  is about to be put back.

## UI

Each sent user bubble gets a one-line receipt under its text: the three emoji of the Telegram ack
protocol this mirrors, 👀 Seen, 🛠️ Working, ✅ Done, each lighting up once its stamp exists and
shown greyed and dimmed until then, so the row always shows what is still to come. Every step
carries its label and time (or "not yet") as both `title` and `aria-label`, so hover and screen
readers say the word, not the glyph. Before 👀 lights, the row carries the honest reason from the
presence stream. The session-wide "Working..." bubble and
presence banner are unchanged; the receipt is the per-request view of the same facts.

A presence change rewrites only the undelivered line, the one part of the row that depends on it.
The rest of the bubble is left alone, so a thumbnail already replaced by "Image expired" stays so.

## CLI and API changes

None required for the automatic path. `lavish-axi poll`, `reply`, and the `/api/*` routes keep their
shapes. Two guidance strings gain one sentence each: `reply --help` and the poll `--agent-reply` row
in README say that a reply marks every request delivered to you as Done.

## Transcripts from before receipts

The positional rule is only true for sessions the receipt code has written from the start. An
existing `state.json` holds sessions whose user entries no take ever stamped; read naively, the
first poll after an upgrade would mark months-old notes Seen today and the next reply would mark
them Done. `readState`, the one load path every operation shares, therefore marks every user entry
of a session that has no `delivery_seq` key at all as `receipt: "none"` and persists that at once,
before any take can run. Those entries are skipped by every stamp helper and render no receipt row:
nothing was observed about them, and an empty row would read as "never seen".

## Open issues for Igor

- **A progress reply reads as Done.** `poll --agent-reply "still working on it"` stamps Done on
  every delivered note, exactly as it already clears the session-wide Working state. If a progress
  channel is wanted, it is a reply flag that posts without concluding; not built here.
- **Working means "the file changed", not "the agent is on your note".** An agent editing the
  artifact for an unrelated reason also ticks Working on every delivered, unanswered note. It is the
  honest automatic signal available; an explicit ack would be more precise and more work for agents.
- **`lavish-axi end` leaves notes at Seen.** Ending says the agent is finished with the review, not
  that each note was handled, so Done is not stamped. Say if the board should treat it as Done.

## Alternatives rejected

- **An explicit `lavish-axi ack <file> --working` command.** It is a new duty for every agent and
  harness, and the file watcher already supplies the signal for the common case. The upgrade path, if
  a progress channel is wanted, is a reply flag that posts a message without concluding the round;
  today `poll --agent-reply "still working"` stamps Done, exactly as it already clears Working.
- **Stamping on the poll's HTTP 200.** The take is destructive and the response can fail to write;
  stamping before the write and reverting on restore keeps one source of truth (`state.json`) and
  avoids a second bookkeeping path.
- **Matching delivered prompts to chat entries by `prompt_id`.** Would mean keeping ids on stored
  prompts and stripping at two boundaries plus the restore path; the positional rule under the lock is
  shorter and provably equivalent.
- **Marking Done when the agent ends the session.** `lavish-axi end` says the agent is finished with
  the review, not that it handled each note. Those stay Seen.
- **Session-level only.** That is today's presence stream; it cannot answer "did it see _this_".


### docs/invariants.md
# Implementation invariants

This file owns Lavish's architecture internals, security rationale, and easy-to-reintroduce failure modes.
[AGENTS.md](../AGENTS.md) keeps only the every-session rules and points here.
[README.md](../README.md) owns the user-facing contract. Runtime guidance strings in `src/cli.js`, `src/design-reference.js`, and `src/playbooks.js` own what agents are told while using Lavish.
[VISION.md](../VISION.md) owns the acceptance policy.

When a change touches an invariant below, update this file. When it touches a user-facing contract, update the README instead.

## Architecture

Lavish Editor is a CLI + local HTTP server that opens agent-generated HTML artifacts in a browser, lets the user annotate elements and selected text ranges or edit Mermaid diagrams as whiteboards, and ships that feedback back to the agent over a long-polling API.

### Process model

Tailscale detection (`src/tailscale.js`) resolves each command candidate to an executable regular file before calling `execFile`: absolute paths are checked directly and bare names are resolved through `PATH`. Unresolved candidates are skipped without a launch attempt, because even an attempted launch of a missing binary can trigger managed-device software restrictions. Resolution and probe errors remain non-fatal, and all candidates share one probe timeout budget. `test/tailscale.test.js` covers skipping missing, directory, and non-executable candidates while retaining probes of installed executables.

The CLI (`bin/lavish-axi.js` -> `src/cli.js`) spawns `lavish-axi server` as a **detached** background process (`src/cli.js:startServer`) and waits for `/health`, which returns `{ ok, app, version }`.
Later CLI invocations reuse the running server when its health version is equal to or newer than the current CLI version, and replace it when the version is older, missing before the handshake, or unparseable, or when the local-build force applies. Releases up to and including 0.1.86 still replace a server of a different version. Stale servers are asked to `POST /shutdown`, and a pre-handshake server may be SIGTERM'd only through the PID `lsof` finds listening at its exact address and port whose command is Lavish (`killLavishListener`); other processes can share the port at other addresses, so nothing is ever signalled by port alone, and an unidentifiable listener is reported instead.
Host, port, listener, and link-host resolution lives in `src/paths.js`; the default path detects Tailscale and gives `serve()` separate concrete loopback and Tailscale listeners, and an explicit `LAVISH_AXI_HOST` disables that automatic path but still adds loopback beside the pinned address. Loopback is always requested because it is the one address every CLI probes regardless of its own `LAVISH_AXI_HOST`: agents on one machine run with different settings, and a server pinned to the tailnet address alone was invisible to a client with no host, which then spawned a second daemon on the same port and the same `state.json`. Wildcard requests are reduced to loopback before listening, and aliases are DNS-resolved and rejected if any result is an all-interfaces address. A name that does not resolve right now is kept as the name (`keepUnresolved`) on both sides - the server binds and retries it like any failed address and reports it in `network_warning`, and the CLI still requires it - so a DNS failure never silently drops an explicit `LAVISH_AXI_HOST`. `listenOnce` resolves a name through the same lookup and all-interfaces refusal as startup, and `requested_hosts` reports configured names beside the addresses they resolved to, so a name whose DNS recovers is compared by address and never looks missing to a CLI that resolves it. Loopback binds FIRST and is the port's ownership lock: if it is in use by a Lavish server (probed over `/health`, bounded), startup throws before taking any other address, so two servers started concurrently cannot split one port between them. Every concrete address gets the same bounded bind retry, and the "did anything bind yet" check runs AFTER those retries and after the loopback floor below - ordering it first made both unreachable whenever the first (or only) host failed. When nothing binds and loopback was not among the requested hosts (explicit `hosts` only), `serve()` binds loopback as a floor. At least one listener must be an address the CLI control channel probes (the primary requested host or loopback), otherwise every listener already bound is closed and startup throws. A requested address that still fails is NOT given up on and never marks the server stale: it stays in `pendingBinds`, is retried in the background for the life of the process (`BIND_RECOVERY_DELAYS_MS`, last delay repeating) and immediately on `/health?reconcile_network=1`, and `applyNetworkState` recomputes the link host, Host allowlist, and phone readiness whenever a listener comes up. Restarting could not free a port another process holds and would drop every live review connection. Every surface that reports network health derives its text from `pendingBinds` (`currentNetworkWarning`), so the warning appears and clears with the bind state and is always logged, not only under `--verbose`. Every mutable the request handlers touch (`idleTimer`, `attachmentSweepTimer`, `bindRecoveryTimer`) is declared before the first listener binds: a reconnecting chrome can attach a live-event socket while later addresses are still retrying, and declaring them after the bind loop was a TDZ `ReferenceError` that crashed restarted servers. CLI discovery (`findRunningServer` in `src/cli.js`) probes the configured host, loopback, and every local interface address in parallel, each bounded, and a response whose `app` is `lavish-axi` wins over a foreign `/health`. Both health probes (`fetchHealth` in the CLI, `probeLavishHealth` in the server) use `node:http` with the socket destroyed on every exit path, never `fetch`: an aborted fetch leaves its TCP connect running, and a Tailscale IPv6 address that drops connections to itself kept every CLI invocation alive ~10s after printing; a connection nobody reads likewise holds the other side's `close()` open. `/health` reports `state_id` (hash of the state file path), `state_dir`, bound `hosts`, and `requested_hosts`. Installation identity is `isOwnedServer`: a matching `state_id`, or - for a 0.1.77-or-older server that reports none - an answer at the CLI's configured host or loopback, where replacing it is the upgrade path; one reached only through the interface sweep without a `state_id` is never adopted or stopped, and another installation's server at a control address is a `SERVER_ERROR` naming its state directory, never used, replaced, or stopped. The CLI adopts the first owned server, retires any other owned server on the port over its own `/shutdown` (never by process name or port-wide signal), and replaces the kept server first when it does not request every address a retired duplicate served (`hostsToServe`), so existing review links survive. It also replaces a server whose `requested_hosts` lack the CLI's explicit host, rechecked once in the startup wait loop when another daemon wins the port, so agents with different hosts converge on one daemon instead of trading it; a server still missing that host after the one retry (including after a network restart) is a `SERVER_ERROR` naming the address, never a successful open. Every replacement - missing host, upgrade, or changed network - passes everything the replaced servers requested to the new one (`inheritedListenHosts` -> `--also-listen`), so one agent's restart never drops another agent's address and its review links; only an IP that is no longer on a local interface (`localInterfaceAddresses`) is dropped, so a vanished Tailscale address is not retried forever while a still-live one survives a MagicDNS change even when the replacing agent's explicit host disables Tailscale detection. A Tailscale identity change (address, MagicDNS, up/down) still reports `network_stale` and is replaced by `ensureServer`, at most once per invocation including the replacement performed before the startup wait loop; a version-driven replacement does not consume that network guard. A version-driven replacement happens only when the running server is OLDER than the CLI (`isServerOlderThanCli`, numeric on major.minor.patch): a newer server is adopted, because replacing it in either direction made two installed versions restart each other's server and interrupt every live poll. Releases up to and including 0.1.86 still replace a server of a different version, so this stops only when both installed versions contain this fix. The same test gates the SIGTERM fallback (`shouldKillProcessOnPort`) and the `upgrade` reason. A missing or unparseable version still counts as older, and the local-build force still replaces a server of any version.
Two global middlewares run before every route, in this order: a Host-header allowlist, then a mutating-route Origin/Referer guard. The Host allowlist (`buildAllowedHostnames`/`isAllowedRequestHost`) rejects any request whose `Host` is missing or not one this server answers to - the DNS-rebinding defense, since `isSameOriginRequest` alone does not stop rebinding (a rebound page sends its hostile domain in _both_ `Origin` and `Host`, so they still match). The allowlist is loopback names + every concrete listener + the active link host + explicit `LAVISH_AXI_ALLOWED_HOSTS` extras (`src/paths.js:extraAllowedHosts`), minus wildcard binds; the Tailscale address and MagicDNS name enter it only while the Tailscale listener is usable. A lone `*` (`allowsAllHosts`) disables the guard for operators fronting it with their own auth. When a reverse proxy sits in front, `X-Forwarded-Host`'s outermost value is validated as a complete authority against the same allowlist (an AND check, so a spoofed or malformed forwarded host only narrows access, never bypasses `Host`); the `*` opt-out skips hostname membership but still rejects malformed authorities. README's Allowed hosts bullet owns the user-facing contract. So a specific-interface bind stays rebinding-protected while its own hostname works, rather than the guard switching off outside loopback. The origin guard then 403s non-GET/HEAD/OPTIONS requests whose Origin (else Referer) is present and does not match this server's origin, using the same construction as `isSameOriginRequest` (including forwarded host/proto). Header-less CLI control-channel requests have no Origin and must keep working; the Host allowlist remains their gate. Per-route `isSameOriginRequest` checks stay in place and still reject header-less callers.
README's Network binding bullet owns the user-facing env vars and the non-loopback security warning.
Live-event WebSockets carry an application-level ping/pong (`liveEventHeartbeatMs`) and an unanswered ping terminates the socket, because a slept laptop or a dropped tailnet path leaves a half-open connection that never emits `close` - which otherwise keeps a departed reviewer counted, suppressing idle shutdown and reporting presence wrongly. Every `shutdown()` records a log-only `cause` (never widened into the user-facing `reason`, which would let an internal cause render as a banner line that claims something untrue), and default log lines are UTC-timestamped by `formatServerLogLine` because `server.log` is append-only across restarts. Detached server stdout/stderr are timestamped inside the server process at real line starts so crash diagnostics in `server.log` stay dated after the parent CLI has already exited; an injected `log` still formats its own lines. The detached spawn uses `bin/lavish-axi-server.js` (published as `dist/server.mjs`), which installs that writer before dynamically importing the CLI, so a module-load failure is dated too. Each HTTP listener keeps its `error` handler after `listening`, so a post-listen error is logged instead of becoming a fatal unhandled `EventEmitter` error. The detached entrypoint also logs `uncaughtException` through timestamped stderr and exits 1 explicitly; installing that listener without an explicit exit would suppress Node's default termination and leave a potentially corrupted server alive. Ordinary user-facing commands still start through `bin/lavish-axi.js` / `dist/cli.mjs`. Server self-shutdown keys off tracked live connections (browser WebSockets and agent polls), not session status, so the next `lavish-axi <file>` re-spawns a fresh server and adopts the session from `state.json` when it is still resumable; README's Server cleanup bullet owns the user-facing idle-timeout rules. The retained legacy SSE route is only a one-response migration handoff, not a tracked persistent connection.
State lives at `~/.lavish-axi/state.json` (`LAVISH_AXI_STATE_DIR`), shared across all projects and keyed by a sha256 prefix of the canonicalized file path - the canonical HTML path _is_ the identity, so the CLI never needs opaque session IDs (`src/session-store.js:sessionKey`).
That makes the session key **derived, not secret**: anyone who learns the artifact path (or sees a session URL) knows it, so no route may treat key possession as authorization.

### Request flow

1. `lavish-axi <file.html>` (`openCommand`) -> POST `/api/sessions` -> `SessionStore.upsertSession` -> the CLI opens the returned session URL in the browser.
   `--no-gate` sends `noGate`, returns a one-open URL with `?no-gate=1`, and leaves the stored canonical session URL unchanged.
   Sessions record who ended them: `ended_by: "user"` for browser-initiated ends (including the composer's send-and-end, which posts final prompts and the `endSession` flag to `/api/:key/prompts` atomically) and `ended_by: "agent"` for `lavish-axi end <file>`.
   Idle self-shutdown never calls `endSession` - it only stops the server process, leaving session status untouched in `state.json`, so there is no third `ended_by` case to track.
   `/api/sessions` refuses a path that is not a regular `.html` / `.htm` file after `realpath` (`src/artifact-path.js:resolveAllowedArtifactFile`), matching the CLI, so a caller cannot register `/etc/passwd` (or an HTML symlink to it) and adopt that directory as a serving tree.
   `/api/sessions` refuses to revive a user-ended session unless the request body sets `reopen: true` (the CLI's `--reopen`), returning `{ status: "user-ended" }` without upserting; agent-initiated ends keep reviving on a plain open.
2. `GET /session/:key` serves a chrome page (`createChromeHtml`) whose sandboxed iframe points at `/artifact/:key/index.html`; the chrome client bootstraps from the `lavish-session` JSON script in the page.
   `extractArtifactHead` (`src/server.js`) adopts the artifact's own `<title>` and `<link rel="icon">` for the chrome tab, but only `data:`, `http(s):`, and protocol-relative icon hrefs - artifact-relative hrefs would not resolve against the chrome page - with fallback to the Lavish defaults.
3. The artifact route runs `injectLavishSdk` (`src/html-transform.js`) to append one `<script src="/sdk.js?key=...">` at the end of `<body>`. Nothing else is injected - artifacts stay byte-identical apart from that tag so they remain portable when opened directly without the server.
4. Sibling assets resolve under `/artifact/:key/<path>`, sandboxed to that session's **artifact tree** - the directory of the canonical HTML file - both lexically and by **real-path/symlink resolution**. `resolveArtifactAsset` (shared with `/whiteboard-assets/*`) rejects `..` escapes and, in parity with export's `guardedRead`, a path whose symlink-followed real path leaves the tree, so a symlink placed beside the artifact can't make the route serve an outside file; a nonexistent path (`ENOENT`/`ENOTDIR`) falls back to the lexical check for the caller's 404, and every other realpath failure fails closed. It returns the **resolved** path, so `sendFile` re-opening it cannot be redirected by a link swapped in after the check. `sendFile` still uses `dotfiles: "allow"` so a tree that _lives under_ a dot-directory (`.lavish/artifact.html`) is not 403ed by the absolute path. A stored session whose file is not HTML is refused on `/artifact`, `/session/:key`, export, share, and mermaid-sources before those routes read `session.file`. The packaged Tailwind/DaisyUI assets are still served from `/design/:asset` so older artifacts keep working, but new artifacts are no longer auto-wired to those routes.
5. The injected SDK runs the render-time layout audit and posts each pass - findings plus its own `complete` flag and viewport width - to the chrome. A completed client-side pass releases the visual gate immediately, then the chrome reports it fire-and-forget to `/api/:key/layout-diagnostics`; a failed report must never hold the artifact behind a network round-trip. If a pass loses an artifact-load-token race, the chrome requests a fresh pass instead of silently consuming the cycle.
   Detection is **passive**: that route updates the warning inbox and emits a live `layout-warnings` event, and it deliberately never emits `feedback`, so a diagnostic pass can never make `lavish-axi poll` return or wake an agent. The gate reveals on the first completed pass whatever it found (detection and user-facing behavior: README's Layout issues inbox, Layout issue lifecycle, and Open-time layout gate bullets).
   Cosmetic, intentional, transient, tiny, warning-severity, and uncertain observations fail open and never enter the inbox.
   The narrow **fatal** path is separate and still immediate: `/api/:key/artifact-failures` records only `artifact-unavailable` (the chrome's probe of the artifact route failed) or `artifact-asset-unavailable` (the SDK saw a same-origin subresource `error`), marks the session `feedback`, and `takeFeedback` returns them as `artifact_failures`. Ordinary layout findings must never be relabelled fatal to regain auto-repair.
6. User actions in the iframe `postMessage` to the chrome. Queued prompts live in tab `sessionStorage`; unsent prompts sharing the SDK-internal `_lavishQueueKey` replace each other, and that field is stripped before POSTing collected prompts to `/api/:key/prompts`.
   The chrome assigns each queued prompt a unique `prompt_id` at queue time (never trusting an iframe-supplied value), carries it through `queuePrompts` onto the persisted transcript entry, and removes a queued note solely when that transcript acknowledges the same identity - never by displayed content or only by a successful POST response - so a reload after a lost response recognizes an already-accepted note instead of re-sending it. `queuePrompts` filters acknowledged identities before attachment resolution and layout-warning planning, and reports whether it accepted fresh feedback so an idempotent retry neither conflicts with newer warning state nor wakes an unrelated poll. Visible `session.chat` is bounded to `MAX_CHAT_STORED_BYTES` (5,242,880) of stored JSON on every shared state load and transcript append; legacy overflow is persisted before the session is served. Evicted user entries leave their `prompt_id` on `session.chat_ack_ids`, and both the store's ack filter and the chrome's settlement (`initialChatAckIds` / live `ack_ids`) consult that compact list so eviction cannot reopen duplicate send. `chat_revision` lets the chrome accept an authoritative bounded replacement even when no retained entry overlaps its current view, while rejecting stale syncs.
   Editing a queued note happens only in the chrome: the edit rewrites `prompt` on the same queued object, so its `prompt_id`, anchor, and send bookkeeping (which tracks notes by object identity) are unchanged, and a note that is already Sending cannot be opened. The iframe learns only the selectors of element-anchored queued notes (`lavish:queuedAnchors`), never their text, and asks the chrome to open one with `lavish:editQueuedAnchor`. The artifact is agent-authored, so a design where the SDK held or rewrote note text would let any artifact script read or silently rewrite the reviewer's instructions; the forgeable message can only open one of the user's own notes for editing.
   The conversation transcript is server-owned display state. Every accepted prompt with text or images enters `session.chat` through `chatEntryForPrompt` (`src/chat-messages.js`) as a bounded `{ role: "user", kind, text, anchor, attachments, at, prompt_id }` entry - not only composer messages - and `/api/:key/prompts` answers with the serialized transcript and emits `chat-sync` at accept time, so the sending chrome settles its queued bubbles in place and every other tab shows the sent notes before any poll takes the batch. Rendering is computed server-side by `serializeChat`/`renderChatMarkdown` in that module because `chrome-client.js` is served as a raw file and cannot import modules (the same reason layout-warning display strings and share passwords are): agent entries ship with their rendered `html` and are the only entries the chrome ever sets as html; user entries ship as text with their anchor and are always escaped. The queued log (`#queuedLog`, the last child of `.panel-scroll`) renders the tab's unsent prompts as the same user bubble in its dashed, removable state, and `promptAnchor` in the chrome deliberately duplicates the server's anchor rule for prompts that have not reached the server yet; `test/chrome-client-queue.test.js` pins the two against the same fixtures so a bubble never changes its anchor when it settles. A note's Sending state is derived from the existing send bookkeeping (`snapshotRequests`, `pendingSubmissions`, the active submission, the terminal reservation), never tracked separately, so no failure path can strand a note with its remove control disabled.
   `/api/:key/prompts` is **same-origin guarded** like `/share` and the whiteboard write routes: whatever lands there reaches the agent as the reviewer's own instructions, and the key alone must never buy that. Only this server's own chrome may queue prompts, so any test or tool that posts there has to send a matching `Origin`; behind a reverse proxy, the expected origin is built from the outermost `X-Forwarded-Host`'s validated hostname and port plus the outermost `X-Forwarded-Proto`, only after the forwarded authority passes the same allowlist boundary as `Host` (or strict authority validation under the `*` opt-out).
   The route rejects every new batch for an already-ended session, including a redundant send-and-end batch, because no later poll will deliver it. `SessionStore.queuePrompts` exempts only its internal `restore` replay of a batch that was accepted before a poll disconnected.
   The chrome page (`/session/:key`) also answers `X-Frame-Options: DENY` and `frame-ancestors 'none'`, denying an attacker page both a window handle to the chrome and a clickjacking surface over Send. The header is scoped to that route on purpose - `/artifact/*` is framed by the chrome, and `/whiteboard-frame` is framed by the artifact document (see the whiteboard section).
   Text selection prompts use `tag: "text"` with a `target` of `type: "text-range"` (selected text, `commonAncestorSelector`, start/end boundary anchors).
   Mermaid diagram-node prompts for rendered SVGs outside `.mermaid` containers use `tag: "mermaid-node"` with a `target` carrying `diagramId`, `nodeId`, the rendered `label`, and a `selector`, so the annotation anchors to node identity and survives a re-render that reshuffles the SVG.
   Composer and annotation-card keyboard conventions, button layout, and the conversation panel are user-facing behavior owned by README's Feedback controls and Keyboard shortcuts bullets.
7. `lavish-axi poll <file.html>` (`pollCommand`) hits `GET /api/poll`, or `POST /api/poll` when it atomically publishes an `--agent-reply` before waiting.
   Poll ownership is exclusive per session and lives only in the server's `activePolls` map. A second poll receives typed `LISTENER_ACTIVE` with the holder label and age; `--takeover` installs its holder before releasing the old poll with typed `LISTENER_REPLACED`, so cleanup cannot erase the successor. The in-process map also supplies the listener labels exposed by `/health` for session listings. Claims serialize through `pollOwnershipLock`, including the reply write, so a rejected poll cannot publish or duplicate its reply. Poll control GETs and POSTs reject a present foreign Origin or Referer while preserving header-less CLI access.
   Queued prompts or fatal artifact failures - including prompts queued before an ended session - are returned immediately and mark the session as observed by an agent; otherwise the poll marks the session actively listening and long-polls on an `EventEmitter` until a `feedback` or `ended` event fires.
   A waiting no-timeout response carries `Lavish-Poll-State: listening`; immediate feedback does not. The CLI uses that response signal for the opt-in Herdr chime, so it never announces a review-ready wait when feedback was already queued, and notification failure must never affect the poll.
   A user-queued layout-issue batch arrives here as an ordinary `tag: "layout-warnings"` prompt with a `type: "layout-warnings"` target - indistinguishable from other feedback at the CLI boundary, which is what lets a nonblocking relay consume it without special handling. `layout_warnings` is no longer a poll field.
   A `status: "ended"` response carries `ended_by`; the final `status: "feedback"` batch delivered right before a session ends carries the same signal via `session_ended: true` plus `ended_by`, so that last `next_step` also skips the reopen instruction.
   Default no-timeout polls stream whitespace heartbeat bytes before the final JSON response and always write the one-shot wait banner to stderr - it is the "not hung" signal an agent needs while stdout stays empty - but write the recurring per-minute wait ticks only when stderr is an interactive terminal (`shouldNarratePollWaitTicks`), so agent harnesses with piped, non-TTY stdio get no unbounded tick noise in their merged capture; stdout is always reserved for the final JSON/TOON response, and `--timeout-ms` is a non-streaming test/debug escape hatch.
   Losing the last review WebSocket while a poll is active starts a per-session reconnect grace timer; a reconnect cancels it, while expiry releases the poll with non-terminal `browser_disconnected` and leaves the stored session open. Poll cleanup must cancel that timer so a timeout, feedback, or explicit end cannot leave a stale disconnect event for a later poll. A disabled grace (`resolveBrowserDisconnectGraceMs` returns `null`) must schedule no timer at all, never a `null`/`0` delay, which `setTimeout` would fire almost at once.
   Key order in `createPollOutput`'s feedback object is a contract, not incidental: `prompts`, `artifact_failures`, then `next_step` all come before the unbounded `dom_snapshot`, so an agent that truncates or filters the response still reaches the user's own words and the instruction that continues the review loop (`test/cli-output.test.js` guards the emitted order). Never move `next_step` after the snapshot: it is the only field carrying the reply-and-poll-again directive, the attachment paths, and the session-ended "stop polling" rule. Poll delivery consumes the response - the feedback is gone from the store once returned - which is why the guidance strings say feedback remains queued only _until delivery_ rather than that it is never lost.
   If SIGINT or SIGTERM interrupts a no-timeout poll, the CLI writes re-run guidance to stderr and exits with the conventional signal code; queued feedback persists, so re-running the same poll is safe.
   That durability has to survive the take itself: `takeFeedback` clears the batch before any response is written, so a poll whose client disconnected - during the immediate take OR during the event-driven long-poll `respond()` - puts the prompts, `dom_snapshot`, and `artifact_failures` back through `queuePrompts`'s `restore` mode and leaves delivery unmarked, because nothing was delivered. `restore` replays an already-accepted batch verbatim - it re-plans no layout warnings and re-appends no chat messages - while still re-deriving attachments through the same resolver.
   Everything else about restore exists because the take window is concurrent, and each rule is load-bearing. Restored prompts are PREPENDED, so a `/prompts` that landed in the window keeps its later position and the user's chronological order survives. A newer `dom_snapshot` and newer `artifact_failures` WIN - the restore only fills what the window did not already replace, and the failure merge goes through the same `mergeArtifactFailures` dedupe and `MAX_ARTIFACT_FAILURES` bound as a fresh report, so a failure re-reported inside the window is not handed to the agent twice - including the end the bound trims, because the restore REPLACES that list: keeping its own never-delivered entries over the newer ones would delete failures nothing else holds, recorded in the window and never delivered either. At the bound the restore's own overflow is dropped and reported through the incomplete-restore log. A successful restore must re-emit `feedback`: a second poll can take `waiting` between the destructive take and the restore, and without that wake it long-polls forever over feedback already sitting in `state.json`. And a restore is exempt from the request-wide `MAX_REQUEST_ATTACHMENT_REFS` bound (never from the per-prompt cap or the resolver), because that bound sizes ONE untrusted POST while a delivery accumulates across an unbounded number of them - measuring a restore against it rejects the whole batch and causes exactly the loss restore exists to prevent.
8. The `/events/:key` live-event WebSocket emits server-derived `agent-presence` data. Its state is `waiting` before any poll has attached, `listening` while one is active, and `working` after a poll has delivered feedback and released. Its mode distinguishes `agent-listener`, an owner-labelled `external-listener`, `agent-busy`, and `waiting-on-captain`; the chrome uses external mode to avoid presenting a supervisor-owned listener as an idle captain turn. While the session is open, the chrome keeps feedback actions available because the server queues them for the next poll. An agent reply concludes the working state and returns presence to `waiting`, and a batch delivered with `session_ended` releases it immediately because no later poll or reply can.
   A 200 from `/api/:key/prompts` acknowledges the queue write, not a completed round, so the chrome never promotes itself to `working` on send and renders only the state the stream reports. A successful ownership claim retires the previous round's delivery marker; releasing a poll never does. Presence reconciliation compares state plus mode so a takeover between bare and owner-labelled listeners is visible even when both states remain `listening`.
   Per-note delivery receipts ([docs/delivery-acks.md](delivery-acks.md)) are the same facts stamped on the user's chat entry: `takeFeedback` writes `delivered_at`/`delivered_seq` (Seen), the artifact `reload` event after a delivery writes `working_at` through `markWorking` (Working), and `addAgentReply` writes `done_at` (Done), each only where the previous stamp exists and the next does not. Seen is stamped **by position under the store lock**, not by id: `agentFacingPrompt` strips `prompt_id` from stored prompts at queue time, and because a take drains every pending prompt while `queuePrompts` shares the lock, the user entries with no stamp are exactly the batch being delivered. `session.delivery_seq` numbers takes so a closed-poll restore (`restoreClosedFeedback` passes `delivery_seq` back) removes **only that take's** stamps - deleted, never nulled, because the restore tests assert the entry is byte-identical to its pre-take shape - while a note queued in the window stays unstamped and is delivered by the next take. A refused restore (an attachment no longer resolves) re-queues nothing and still removes that take's stamps and publishes `chat-sync`: a note that reached no agent must not read Seen. Working and Done never cross a reopen: `#upsertSessionLocked` records the last take of an ended session as `closed_delivery_seq`, and `stampWorking`/`stampDone` skip entries delivered at or before it, so a note `lavish-axi end` left at Seen is not marked by a later round's edit or reply. Every stamp change bumps `chat_revision`, which is what makes `syncChat` accept the replacement; `chat-sync` for a delivery is emitted from `finishFeedbackDelivery` (the success path) and again after a restore, never from the destructive take, so no tab is told Seen for a batch about to be put back. `delivery_seq` is stripped from the poll response by `agentFacingFeedback`; agents never see it. A session with no `delivery_seq` key at all predates receipts: `readState` marks its user entries `receipt: "none"` and persists that before any take runs, because the positional rule would otherwise read every one of them as the first post-upgrade batch; marked entries are skipped by every stamp helper and render no receipt row. The chrome derives the receipt row from the entry on every render, and a presence change rewrites only the pre-Seen `receipt-note` line (`refreshUnseenReceipts`), never the bubble, so an "Image expired" placeholder is not rebuilt into a retried image.
   An `ended` live event makes every connected chrome read-only immediately. The channel registers before reading session state, then sends an `ended` snapshot when that state is already terminal; the bootstrapped `initialEnded` state covers pages loaded after the end, and `markSessionEnded()` is idempotent across redundant signals.
   Every poll exit path has to undo the presence it set: `/api/poll` subscribes to request and response closure before its first `await`, re-checks closure and replacement after destructive feedback takes, and reconciles a browser disconnect that occurred before event handlers were armed. This prevents abandoned or displaced polls from stranding ownership, presence, or consumed feedback.
   `--agent-reply` and `--agent-reply-file` publish a chat message through the same atomic poll claim before waiting, rendered in the browser conversation panel via the live stream; README's CLI reference owns when to use each input. `lavish-axi reply` posts that same message to `POST /api/:key/agent-reply` and exits 0 only after the route answers `sent`. The whole receipt request (connect, headers, body) shares one deadline, `AGENT_REPLY_RECEIPT_TIMEOUT_MS`, and a timeout exits non-zero. It must not claim a poll: a poll stays open until feedback arrives, so it cannot be the acceptance receipt.

### Passive layout-warning inbox

`src/layout-warnings.js` is the whole lifecycle, as pure functions over stored records, so it is unit-testable without a browser or a server; `SessionStore` and the routes only persist and serve what it returns.
Identity is `layoutWarningFingerprint` over rule + normalized target + viewport class - **magnitude is deliberately excluded**, so a finding that worsens updates one record instead of inflating the count.
Every observation is stamped with an **artifact revision**: `session.artifact_revision`, incremented by the server-owned `beginArtifactLoad` epoch before navigation. The artifact document route only verifies the current load and serves it. Every transition that needs "a newer successful artifact load" (resolved, recurring, dismissal expiry) keys off the revision.
The reviewer handoff is a server-issued single-reviewer capability. Begin requests return typed `superseded`, `no-handoff`, or `out-of-order` outcomes; the chrome may re-handshake once for `no-handoff`, but only an explicit takeover reload can replace a superseded reviewer.
The active load is **durable**, not process state: `beginArtifactLoad` writes the whole epoch - token, revision, pass fence, and the `request_id`/`request_sequence`/`handoff_token` a later begin is judged against - to `session.artifact_load`, and `SessionStore` restores it (and the handoff that owns it) the first time a process asks for it, because the `upgrade` restart replaces the server under reviewers who did not ask for it. Only a newer `beginArtifactLoad` retires a load - not a restart, and not reopening the session. A stored load the restore cannot read as a whole is treated as none, which degrades to one re-handshake and a fresh epoch. The restart tests in `test/session-store.test.js` and `test/server.test.js` pin all three.
`applyDiagnosticPass` is conservative by construction and each guard is load-bearing: a pass for one viewport class returns other classes untouched; an incomplete pass marks active warnings `unverified` instead of clearing them; absence at a revision the warning was already seen on is not resolution; and re-observing an identical finding on the same revision returns the record unchanged so repeat passes do not rewrite `state.json`.
`queued` is a request, not a fix - it stays in the active count and only `recurring` (a newer revision still found it) makes a warning selectable again.
Display strings are computed server-side (`serializeLayoutWarnings`) because `src/chrome-client.js` is served as a raw file and cannot import modules; the chrome renders what it is given and never decides that a warning went away.
The chrome bootstraps the inbox from `initialLayoutWarnings` in the session JSON and re-syncs over the live-event channel, so the inbox survives a browser refresh or reconnect; only per-chrome drawer selection lives in `sessionStorage`, keyed per session so it cannot leak across artifacts.

### Live reload

While a session has a queued (not yet re-checked) layout-warning batch, the reload debounce widens to `BATCH_RELOAD_DEBOUNCE_MS` so an agent's related saves coalesce into one artifact refresh for that group.
`chokidar` watches the artifact file itself by default - watching the entire parent directory recursively saturated the event loop when artifacts lived inside large trees like `~`.
The opt-in attribute/meta (user-facing contract: README's Live reload bullet) switches the watcher to the artifact's directory, excluding `.git`, `node_modules`, `dist`, `build`, `.lavish-axi`.
Any file change emits a `reload` live event and the chrome reloads the iframe; the SDK reports scroll position with `lavish:scroll` and the chrome replays it with `lavish:restoreScroll` after the iframe loads, because the sandbox prevents direct scroll reads.
The same channel preserves the rest of the in-iframe review context: `lavish:reviewState` carries an open annotation card's unsent text and the values of controls inside a `data-lavish-question` scope, and `lavish:restoreReviewState` replays them after the load. Restoration sets values directly and dispatches **no** synthetic `change`/`input` events, because the artifact's own handlers queue prompts and replaying them would silently re-queue answers. Application-owned form state outside `data-lavish-question` is deliberately left alone.
That reported state is also **persisted** per session (`lavish-axi:review-state:<key>` in `sessionStorage`, beside the queue's own key) and restored on boot, because it is the user's own writing and the chrome's in-memory copy dies with the document: an iframe live-reload replayed it, but a full page reload destroyed it, and a real user lost written notes that way. The SDK reports `card: null` when a card is queued or cancelled, which is what retires the stored draft, so a stale draft can never reappear over a later card. `closeCard` reports only when a card was actually open: a page declaring `data-lavish-annotate="off"` closes at boot, and a `card: null` sent then would overwrite the stored draft before the frame's `load` event replays it (`test/artifact-sdk-bundle.test.js`, "reports no review state at boot").
During version-driven shutdown, the server sends `chrome-reload` to the live-event clients of the ONE session named by `POST /shutdown`'s `reload_key` - the session `lavish-axi <file>` is about to open - and `chrome-outdated` to every other connected chrome; a shutdown that names no key (`lavish-axi stop`, idle self-shutdown) reloads nothing. `chrome-outdated` shows a dismissible banner in the conversation panel and never reloads by itself: a forced reload of a current page the user is reading or writing in is the behavior this replaced. The deliberate migration exception is an old EventSource client reconnecting to the retained legacy route: it receives one neutral `chrome-reload` event and the response ends immediately so the tab moves to WebSocket without occupying the browser's HTTP connection pool. `reloadChromeAfterServerRestart` still shows the banner instead of reloading whenever an unsent annotation draft exists. The same banner also carries the server-unreachable state: after `LIVE_EVENT_UNREACHABLE_FAILURES` consecutive live-socket reconnect failures the chrome raises it with the no-reason copy, because an endless silent retry is indistinguishable from a healthy quiet stream and the user learned nothing until they reloaded into a browser connection error. Only that path may retire a banner it raised - a `chrome-outdated` event means the server really was replaced, which a reconnect does not disprove - and a dismissal sticks until the stream actually recovers.
The banner's line is chosen by the shutdown's own `reason` (`SHUTDOWN_REASONS`: `upgrade` and `local-build` from `ensureServer`, chosen by `serverReplacementReason` from whichever branch of `shouldRestartServer` fired, and `stop` from `lavish-axi stop`), and **every branch must be true where it is shown** - a deliberate stop told the user Lavish had been updated, which was false on both counts. An invalid reason on `/shutdown` is dropped and renders the line that claims neither; the legacy migration deliberately sends the unrecognized `server-restarted` reason because the replacement server cannot know why its predecessor stopped. Idle self-shutdown and `shutdownIfNoLiveSessions` need no branch: both only fire with `liveEventClients.size === 0`. Every recovery control this feature shows probes `/health` before navigating - the banner and both gate cards through `checkServerThenReload`, and the inline boot failsafe (`CHROME_BOOT_FAILSAFE_JS`) through its own copy of the same rule, because it runs where `chrome-client.js` does not exist. Each is raised in a state where nothing may be listening, and each is labelled for the check rather than the navigation. Every one of those probes is bounded by an abort timeout and every caller restores its own control on a path that runs whether the probe answers, fails, or times out - a port that accepts a connection and then says nothing would otherwise leave the user's only recovery button disabled, which is worse than the reload it guards. A new one that calls `location.reload()` directly reintroduces the browser error page this whole path exists to avoid; the `superseded` takeover card is the one exception, because its 409 proves the server answered.
The "Lavish is not running." card's copy is the one failure state only the user retires, so `setLayoutGateFailure` refuses to overwrite it with a non-sticky failure or clear that state. Sticky copy never makes the visual overlay sticky: every failure card retains the shared bounded timeout and independent **Show anyway** bypass.
A draft is retired only on a definite answer, and "definite" is deliberately expensive: the SDK re-queries the anchor after `REVIEW_DRAFT_ANCHOR_SETTLE_MS` before reporting `lavish:reviewDraftUnrestorable` (the load event says the document parsed, not that script-built or Mermaid content has rendered), and the chrome retires the stored draft only when a SECOND artifact revision reports that same selector missing. One miss is recorded, not acted on: the element a user annotates is the one the agent is most likely to be rewriting while they type, and an intermediate save that drops it must not delete their notes. Silence is what left an unrestorable draft to be retried against every later load, but retiring on anything less than two revisions is itself data loss. Opening a card cancels the pending settle re-query outright (`showAnnotationCard` -> `cancelPendingDraftRestore`), and the timer also checks `activeCardContext` when it fires: `showAnnotationCard` closes whatever is on screen before it draws, so restoring there would delete text the user is typing that nothing has carried to the chrome yet, and closing that card reports `card: null`, which retires the stored draft - a restore that fired after it would put text the chrome no longer holds back on screen and back into persistence. Retirement is also not silent - `keepRetiredDraft` writes the text verbatim into the conversation panel and persists it under `lavish-axi:retired-drafts:<key>`, so the user keeps a readable copy of writing Lavish can no longer replay; it overwrites nothing they typed and has no control that could discard it. That list is never trimmed to make room: an entry already handed back may not be dropped for a newer one, and a write browser storage refuses is reported in the note itself rather than resolved by evicting an older one.
`reloadChromeAfterServerRestart` must gate the reload on a healthy `/health` answer, never on a deadline alone: reloading into a port nothing is listening on replaces a recoverable page with the browser's own connection-error page, which no Lavish code can undo. A wait that ends on the deadline rather than a confirmed probe re-probes before deciding, because either stale answer is wrong in its own direction.
The "Lavish is not running." card state is **sticky** (`setLayoutGateFailure(..., { sticky: true })`): a later successful artifact load or diagnostic pass clears the ordinary artifact-load failure state but must never clear this copy, because the page is still running the pre-upgrade client against the replacement server and nothing else would tell the user that. A completed pass, manual bypass, or gate timeout must still reveal the artifact; stickiness governs copy, never visual release.
Hand-edited files in `dist/` won't trigger reloads.
Run `lavish-axi server --verbose` (or set `LAVISH_AXI_DEBUG=1`) to log session and watcher events to stderr when diagnosing wedges; detached server stdout/stderr is also appended to `server.log` in `LAVISH_AXI_STATE_DIR` for startup and crash diagnostics.

<a id="whiteboard-mermaid-excalidraw"></a>

### Whiteboard (Mermaid → Excalidraw)

At view time the SDK replaces each rendered Mermaid diagram inside a `.mermaid` container with an inline whiteboard: a sibling sandboxed iframe (`allow-scripts allow-popups`, no `allow-same-origin`, `data-lavish-ui`) hosting `/whiteboard-frame`, while the hidden container keeps the Mermaid source authoritative - standalone and exported artifacts render plain Mermaid because the SDK is absent.
Inline frames boot locked in view mode behind a click-catcher so embedded canvases never trap page scrolling; a click unlocks editing, and a Fullscreen action reopens the same diagram in the chrome's overlay (the inline frame parks on `about:blank` meanwhile so two editors never autosave one sidecar).
The frame bundle (`src/whiteboard-frame.js`, built by `scripts/build.js` into `dist/whiteboard/` with Excalidraw, the converter, React, and vendored fonts) converts the diagram with `@excalidraw/mermaid-to-excalidraw` and mounts the editor; flowchart, sequence, class, ER, and state diagrams become editable shapes with Mermaid node/edge ids preserved (`regenerateIds: false`), and every other diagram type becomes an image the user draws on (`imageFallback`).
Frames have no server access: each frame gets a signed, short-lived channel token in its HTML, reports directly to `window.top`, and accepts commands only from that top window; the chrome verifies the token at `POST /api/:key/whiteboard-channel`, binds the frame window and token to its diagram index, then fetches sources (`GET /api/:key/mermaid-sources`, extracted from the artifact file on disk by `src/mermaid-source.js` in `.mermaid` document order) and saved scenes, passes them back over postMessage, and performs all writes.
That channel token is **not** a secret and must never be treated as one: `/whiteboard-frame` has to stay framable by any origin - its legitimate parent is the artifact iframe, whose sandbox gives it an opaque origin that no `frame-ancestors` expression can name - and the frame hands its token to whatever window frames it. Two independent guards carry the trust instead, and both are load-bearing.
Binding: the token is signed over the **session key** (`createWhiteboardChannelToken`/`isValidWhiteboardChannelToken`), so it is a capability for one session only, and `/whiteboard-frame` therefore requires `?key=` and 400s without it; signing `${now}.${nonce}` alone let a token minted with no session named at all authenticate any session.
Descent: the chrome accepts inline whiteboard messages **only from windows whose `parent` is the current artifact frame** (`isArtifactChildWindow` in `src/chrome-client.js`) - descent, not token possession, is what proves the sender is ours; without it, any window that can `postMessage` to the chrome (a popup opener, or a page that framed it) could open a channel and queue a fabricated prompt as the reviewer.
Scenes autosave (debounced) through `PUT /api/:key/whiteboard/:index` into per-diagram sidecar files under `<state-dir>/whiteboards/<key>/` (`src/whiteboard-store.js`) - never into `state.json`, which is rewritten wholesale on every store operation; an authenticated `lavish-whiteboard:flush` performs a bounded save before version-driven chrome reloads.
Whiteboard write routes are same-origin guarded and get a 20 MB JSON limit (`isWhiteboardWriteApiPath`); everything else keeps the 2 MB default.
Staleness is hash-based (`mermaidSourceHash`, or `whiteboardSourceHash` for sources with `%% lavish-icon` lines; see below): a live reload that changes the diagram shows a banner in an open whiteboard. Reopening prompts re-convert vs keep-editing only when the saved scene has preservable edits versus its conversion baseline (`resolveWhiteboardInitAction` in `src/whiteboard-core.js`); an unmodified autosave-on-view silently re-converts. Stale user edits are never silently merged.
"Queue feedback" exports the scene and a PNG server-side (`POST .../feedback-files`), then queues a normal prompt with `tag: "whiteboard"` and an `excalidraw-scene` target carrying a bounded edit summary (diffed from the conversion baseline by `summarizeSceneEdits` in `src/whiteboard-core.js` using the stable ids), local `scenePath`/`previewPath`, `sourceHash`, and bounded stats; poll guidance tells the agent to read the summary first and update the Mermaid source, never the scene file.
The Mermaid source in the artifact stays authoritative; there is no scene→Mermaid reverse conversion.
User-supplied Excalidraw libraries live in `<state-dir>/excalidraw-libraries/`, which Lavish only reads (`src/whiteboard-library-store.js`, size and item caps, skips reported by `lavish-axi libraries`). The chrome fetches them on every whiteboard init (never cached per page, so the frame converts with the same libraries the server hashed into that init's source hash) from the same-origin-guarded, read-only `GET /api/whiteboard-libraries` and passes them in `lavish-whiteboard:init`. Each library snapshot has a `version`, reported by `/api/whiteboard-libraries` and, for sources with directives, by `/api/:key/mermaid-sources` as `libraries_version`; a failed fetch or a version mismatch (a library file changed between the two requests) never blocks the whiteboard: init carries `librariesUnavailable: true`, and when the frame converts a source with `%% lavish-icon` directives under it (`conversionUsesUnverifiedLibraries`), every save of that scene (autosave and queued feedback) keeps the full scene but records the source hash with `UNVERIFIED_LIBRARIES_HASH_SUFFIX` (`createWhiteboardPersistencePayload`), so it can never be restored as matching: a later open re-converts it with the right libraries, or offers the keep-or-re-convert choice when it was edited. A restored scene keeps its saved hash, and a diagram without directives is never marked. Frames still have no server access. Unnamed items are named after their largest text with at least two letters or digits. `toExcalidrawLibraryItems` stamps every library element with `customData.lavishLibraryRef` (Excalidraw keeps `customData` when inserting an item) and groups ungrouped multi-element items, so `summarizeSceneEdits` folds a dropped item into one "Added library item <ref>" line, and reports a library item's moves and resizes from its whole bounds (an icon node's icon relative to its node), and as "Edited library item <ref>" its content edits, any part moved, resized, or reshaped beyond what the item's overall move and scale explain, and deleted parts while others remain ("Removed library item <ref>" only once every part is gone). Generated item refs are unique after normalization, bounds account for `angle`, and an unreadable library file is reported as skipped.
A `%% lavish-icon <node-id> <ref>` comment in a flowchart (`parseLibraryIconDirectives`) turns that vertex into an icon node. The swap happens on skeletons, before Excalidraw materializes them (`prepareLibraryIconSkeletons`): the vertex keeps its Mermaid id, label, and bindings, resizes to hug icon and label, turns transparent, and keeps the normal label size even where the converter shrank it to fit a shape (cylinders). Its bound arrows are extended or trimmed to the new edge, because `convertToExcalidrawElements` binds arrows without rerouting them. Every icon scales to `LIBRARY_ICON_HEIGHT` within `LIBRARY_ICON_MAX_WIDTH` (`libraryIconSize`). Icon nodes grow taller, so a diagram that places an icon gets wider Mermaid spacing only along that axis (`rankSpacing` top-down, `nodeSpacing` left-right; `libraryIconMermaidConfig`): enough that neighbours do not overlap, without spreading the rest of the diagram. `placeLibraryIcons` then adds the scaled item with ids derived from the vertex id (`<id>:icon:<n>`), grouped with the vertex. A missing library, item, or vertex leaves the plain node. Mermaid ignores `%%` lines, so export, share, and direct opens are unchanged. For sources with directives only, `/api/:key/mermaid-sources` folds the referenced items into the hash (`whiteboardSourceHash`), so a changed item re-converts an unmodified scene while every other diagram keeps its plain source hash.

### Image attachments

Annotation image attachments (`src/attachment-store.js`) are content-addressed: the id is `<sha256-of-bytes>.<ext>` and the file under `<state-dir>/attachments/<sessionKey>/` _is_ the identity, so the client never dictates a path or id.
The sandboxed artifact iframe can't reach the loopback server (opaque origin), so the SDK annotation card captures the image, reads its bytes, and hands them to the chrome, which performs the same-origin `POST /api/:key/attachments` (raw body, magic-byte validated - a lying Content-Type is ignored) and reports the server-vetted id back to the card. Upload/delete are same-origin guarded like the whiteboard writes.
Two surfaces originate uploads: that relayed card path and the chrome's own Conversation composer, whose controller (`createChatAttachmentsController` in `src/chrome-client.js`) owns its chips, send gate, and notice. They deliberately share the page-wide abuse budget below rather than getting per-surface counters. Three invariants keep the composer honest: its notice is DERIVED from item state on every render (`syncNotice`), because an imperatively stamped "waiting for an upload" string outlived the upload it described once that upload failed; paste/drop resolve their payload through the single `transferredFiles` helper, because several browsers expose a pasted screenshot only through `clipboardData.items` and reading `.files` alone attaches nothing with no error and no chip; and the accepted image types come from `ACCEPTED_IMAGE_MIME` (`src/attachment-store.js`, beside the enforcing `detectImageType`), threaded to the chrome through the session JSON and to the card through `createSdkJs`'s `acceptedImageMime` (`acceptedImageTypes`), so both pickers' `accept` attributes, both paste/drop filters, and the composer's rejection copy are derived - a second hardcoded list would let one surface offer a format the others refuse. Like the annotation card, an over-cap file is decided `error` with no retained `file` and no object URL, so it renders no Retry and its bytes are never read.
Four more composer rules are easy to regress: the chip send gate holds back only the composer's own message and an explicit end - queued annotation prompts still deliver (gating the whole `sendQueued` pipeline made Send and Send & End silently deliver nothing); paste raises no unsupported chips because Office/macOS pastes expose stray non-image file flavors beside their text (the picker and drop still refuse visibly, and a `Files` drag with nothing enumerable gets an explicit refused chip); the cap counts only uploadable chips (mirroring `currentImageCount`) so a size-refused companion cannot eat a valid image's slot and have `syncNotice` clear the cap notice on the same tick; and a document-level `Files`-drag guard keeps a drop that misses the composer from navigating the chrome away, while leaving text drags to the browser. `planClipboardPaste` (shared rule, duplicated as `keepsClipboardText` in the import-less chrome) treats a pasted file's own name or path in `text/plain` as placeholder, not caption.
The upload route reads the request stream itself via `readAttachmentUploadBody` rather than `express.raw({ limit })`: raw-body aborts on a too-large `Content-Length` WITHOUT draining, which leaves the browser's in-flight upload reset mid-stream so the chip hangs on "uploading" instead of getting the 413. The manual reader buffers up to the cap but always drains to end-of-body, then the route sends a clean 413. Belt-and-suspenders, the chrome also pre-checks byte length against `attachmentMaxBytes` (surfaced in the chrome session JSON) and fails the chip locally before uploading. Do not reintroduce a body-parser `limit` on this route.
Because the sandboxed frame's postMessage source proves origin but not a user gesture, the chrome is the **confused-deputy mediation point** for the relayed card path, and its counters are page-wide, so the composer's own user-gesture uploads spend the same budget: it rate-limits (`UPLOAD_RATE_MAX`/`UPLOAD_RATE_WINDOW_MS`), enforces a per-chrome-session cumulative-byte quota (`UPLOAD_SESSION_BYTE_QUOTA`), AND bounds concurrent in-flight uploads (`UPLOAD_MAX_IN_FLIGHT`, D8 - rate + cumulative alone let ~30 large bodies fetch at once before the quota tripped) before any upload reaches the loopback server; over-cap uploads are refused with a retry hint and a settled upload frees a slot. The server keeps a bounded default disk quota (`DEFAULT_MAX_ATTACHMENT_DISK_BYTES`) as the durable backstop.
The **trust boundary** is `SessionStore.queuePrompts`: a queued prompt carries only the client's `id` + display `name`; `resolvePromptAttachments` re-derives every authoritative field (absolute `path`, mime, bytes, dimensions) from disk via the injected resolver, so a crafted `/prompts` POST cannot aim an attachment at an arbitrary file. Repeated content ids remain repeated logical references with their own display names and count separately toward prompt count/byte caps; content-addressed storage deduplicates only the bytes on disk. Resolution is **all-or-nothing** (C4): a malformed field/entry, any unknown id, or a count/byte-cap breach rejects the whole batch (`{ rejected, caps }`, persist nothing → 400), never a silent partial-drop; the chrome keeps its queue on the 400 and surfaces the reason. User-facing limits/env vars and defaults are owned by README's Image attachments bullet.
`boundAttachmentRefs` runs BEFORE the resolver and is why a crafted batch can't wedge the server: the in-resolver cap counts RESOLVED refs, and a well-formed id for a file that doesn't exist never advances it, so thousands of them would each buy a sequential `stat` while the store's single mutex is held, stalling every poll and mutation. Raw per-prompt and request-wide (`MAX_REQUEST_ATTACHMENT_REFS`) counts are rejected up front - except that a closed-poll restore is exempt from the request-wide bound alone, for the reason given in Request flow step 7 - and the reported rejection list is capped (`MAX_REPORTED_ATTACHMENT_REJECTIONS`) so the 400 can't be turned into an amplifier. New pre-resolve validation belongs in that same pure gate - never after the first `await` into the filesystem.
`SessionStore` owns ONE `AsyncMutex` (`src/async-mutex.js`, `store.lock`) covering BOTH concerns. Every `state.json` read-modify-write runs under it - `queuePrompts`, `takeFeedback`, `recordLayoutWarnings`, `upsertSession`, `endSession`, `addAgentReply` - so a poll can't clear prompts in the window `queuePrompts` holds its pre-resolve snapshot and then clobber the take (E1); **any new store mutation must acquire this lock too**. The server routes its attachment disk sections (upload finalize, delete, the sweep) through `store.runExclusive` so they share that same lock, keeping the reference snapshot + delete atomic against `queuePrompts` (D5). `referencedAttachmentIds` is a pure read and must stay lock-free - the server calls it from inside `runExclusive`, so self-locking would deadlock. Delete is **reference-counted** under the lock - a content-addressed file shared by a queued prompt survives a DELETE request (`status: "referenced"`) - and dedup re-upload **refreshes the mtime** so a re-referenced aged file isn't reaped by the next sweep (B3).
Dimensions are persisted at upload in a `<id>.meta` sidecar (D6): `resolveAttachment` reads it instead of re-parsing the whole image, and the thumbnail GET uses `statAttachmentForServe` (one stat + streamed send, mime from the id extension) instead of a second full read. Sidecars are removed with their image on delete/sweep and are excluded from `listAttachments` by `ID_RE`.
The SDK's annotation card gates queuing on BOTH `hasPending()` (R2.4, an in-flight upload) AND `hasErrors()` (W2, a failed/rejected chip) so neither is silently dropped by `collectReady`/`closeCard` - it keeps the card open with a notice so the user can wait, retry, or explicitly remove; that notice line is shared with the card's neutral keyboard hint, so it renders in the error color and is restored (never left stale) once the condition clears. A count-cap rejection remains visible while the card is full and clears only when removing a chip creates capacity. A mixed drop **partial-accepts**: `partitionDroppedFiles` always reports both halves, so the images attach AND every unsupported companion raises its own `UNSUPPORTED_TYPE` chip - reporting the unsupported files only when no image was found is what made a mixed drop swallow them silently. Removing a chip deletes **nothing**: there is deliberately no `lavish:removeAttachment` message and the chrome honors no iframe-driven delete, because the iframe is untrusted and no client can see every live reference (attachments are content-addressed, so another tab's ready-but-unqueued chip shares the id and is invisible from here). Only the reference-aware sweeper and the reference-counted same-origin `DELETE` route remove unreferenced attachments; the chrome never drives the latter, so do not reintroduce an eager delete. Upload results are scoped to the document that asked for them: each document mints an `ATTACHMENT_NONCE`, sends it with every upload, and `isTrustedAttachmentResult` requires both an exact nonce match and `event.source === parent` - chip ids restart at `att-1` on every load, so id alone would let a result in flight across a reload mark a new chip with the previous document's image. The card's per-prompt count cap is NOT a literal: `createSdkJs` threads the server's `maxPerPrompt` into the SDK so the local guard matches `LAVISH_AXI_MAX_ATTACHMENTS_PER_PROMPT` (W1), and an over-cap pick is surfaced instantly rather than swallowed. Queued and sent note bubbles always render at most four thumbnails and collapse every additional attachment into an explicit `+N` badge, independent of that configurable cap (`test/chrome-client-queue.test.js`). The card re-clamps its viewport position after every attachment-row render (W3) so chip rows can't push Queue/Cancel off-frame; the chip list also has a `max-height`/scroll backstop.
Cleanup (`sweepAttachments`, run at server startup + hourly) is **reference-aware** and never removes a file in `SessionStore.referencedAttachmentIds()`. It has two distinct passes: TTL cleanup reaps an unreferenced file once it is past its TTL (`LAVISH_AXI_ATTACHMENT_TTL_MS`, seven days by default), and cap eviction, under disk-cap or object-cap pressure, removes unreferenced files oldest first before their TTL, but only once they are older than `ATTACHMENT_EVICTION_GRACE_MS` (one hour) - so a send-and-end batch's images are never lost before delivery, and orphaned uploads (card cancelled, or `/prompts` never followed) are reaped later.
That reference set is pending-prompt ids **plus** ids delivered within `ATTACHMENT_DELIVERY_GRACE_MS`: `takeFeedback` clears the delivered prompts, so without that window an attachment would become sweepable at the exact moment the agent starts reading the path it was just handed. The grace is a bounded read window, not a second lifetime (the TTL and disk cap must still reclaim delivered bytes eventually), and the retained list is capped (`MAX_DELIVERED_ATTACHMENTS`) because it lives in `state.json`, which is rewritten wholesale on every store operation.
The eviction grace is the symmetric window on the upload side (fixed, not env-tunable): "unreferenced" also describes a **ready chip** - an image sitting in an open annotation card or the Conversation composer that has not queued a prompt yet - so cap eviction with no age floor deletes bytes out from under the imminent Send, which then fails unrecoverably as not-found. It never lets the total exceed the cap, because admission refuses the new write instead.
The disk cap charges **allocated** cost, not logical image bytes: `listAttachments` reports `chargedBytes` = the image rounded up to whole `ATTACHMENT_ALLOC_BLOCK_BYTES` (4096) blocks plus the sidecar's own block, and both of its enforcement points measure `maxDiskBytes` against that accounting. Summing logical `size` let a flood of 12-byte magic-prefix uploads (the smallest `detectImageType` accepts) sit ~683x under the reported total while consuming real disk and inodes.
The periodic sweep is only one of those two points, and it can never hold the cap alone: it refuses to evict referenced or in-grace files, so concurrent chrome pages could each write past `maxDiskBytes` in the window before the next sweep. `admitAttachmentCharge` inside `writeAttachment` is therefore the single **upload-admission chokepoint** every byte-adding write path must route its charge through (today a new image+sidecar and the dedup sidecar repair; the dedup mtime rewrite replaces identical bytes and the sweep only removes): it reclaims toward `cap - newCharge`, measures the true committed allocation with its own tree walk so the undeletable temp/orphan debris a curated survivor set hides is still counted, and refuses with **507** when the write would not fit. Admission must run under the store's lifecycle lock so the reference snapshot, the reclaim, and the write are one critical section; a refused sidecar repair is skipped (the sidecar is only a display cache) rather than failing the dedup upload. The `maxObjects` bound is **derived** from the disk budget (`budget / 2 blocks`), never a separate env var, so it can only agree with the byte cap. The sweep's cap/object eviction keeps **running totals** decremented per removal rather than recomputing over all survivors per candidate: it runs under the store's global mutex, so per-candidate O(n) work would be an E3-class lock hazard. The sweep also reaps files that `ID_RE` hides from every cap: crash-orphaned temp files (D6) - `writeFileAtomically` writes `<name>.<pid>.<n>.tmp` then renames, and a crash in between leaves one, reaped once older than a 5-minute grace (a live write renames within ms) - and orphan `<id>.meta` sidecars whose image is gone (ATTACH-002), reaped with no grace since a live upload writes the image before its sidecar. `removeAttachment`/`removeFile` delete the sidecar FIRST, so a crash between the two removals leaves only the counted image, never an uncounted orphan sidecar. The SDK decides a whole drop in one pass via the pure `classifyAttachmentBatch` (mime / size / count-cap per file) and `addFiles` renders **once** instead of per file (D7 - a large multi-drop was O(N²) DOM rebuilds); `rejectUnsupportedBatch` does the same for unsupported files. The size decision lives in that classifier and still runs **before** `createObjectURL`/`arrayBuffer` (`attachmentSizeError`, threaded from the server via `createSdkJs`'s `maxAttachmentBytes`), so an oversized drop is decided `error` and never read into a buffer or structured-cloned into the chrome; the server still re-checks.
Attachment files and dirs are created **owner-only** (`0600`/`0700`, set explicitly at creation since the umask would otherwise leave 0644 in traversable dirs) and `ensureAttachmentDir` re-asserts the dir modes so an install that uploaded before that hardening doesn't keep its existing screenshots exposed. A dedup upload's mtime refresh is load-bearing (it restarts the TTL clock) and must never be swallowed into a success: `writeAttachment` falls back to an atomic rewrite of the identical bytes and propagates if that fails too. Env limits floor BEFORE the bounds check and require `>= 1`, so a fractional `0.5` falls back instead of flooring to a silent zero cap; only `0`/`off` may disable one.

<a id="export-local-asset-inlining"></a>

### Export (local-asset inlining)

`src/export-bundle.js` (`buildSelfContainedHtml`) inlines only an artifact's **local** assets: local stylesheets/classic scripts become inline `<style>`/`<script>`, and local images/fonts/icons, confined fetchable `file://` refs, and CSS `url(...)`/`@import` become data URIs (recursively, resolved relative to each stylesheet).
Remote references are deliberately left as links; the user-facing contract, including the size-cap env vars and their defaults, lives in README's Export and sharing bullet.
The transform makes **no outbound requests** (no fetching, no SSRF); its only security surface is local file reading, which is confined to the artifact directory both lexically (`confineDir`) and by **real-path/symlink resolution** in the default `readLocalFile` (`guardedRead`), so a symlink inside the directory can't exfiltrate an outside file (e.g. `~/.ssh/id_rsa`) into a shared bundle.
Absolute `file://` paths in non-inlined regions are redacted to `about:blank` so local paths do not leak into exports or hosted shares; the injected Lavish SDK is stripped; in-document fragment refs (`#a`, encoded `%23a`) are left alone; and inlined `</script>`/`</style>` are escaped so they can't break out.
The transform records `warnings` rather than failing, split into unresolved local assets (such as `load-failed`, `outside-root`, `too-large`, or unsupported local references left external) and notices (such as `csp-meta` or `file-url-redacted`).
It is dependency-injectable (`readLocalFile`, `resolveAbsolute`, `confineDir`, size caps) so it is testable without disk; the server passes `resolveAbsolute: resolveDesignAssetPath` to inline legacy `/design/*` references from the packaged assets.
The chrome's **Export standalone HTML** overflow-menu item `GET`s `/api/:key/export`; the CLI exposes the same transform as `lavish-axi export`, server-independently.
Lavish sends two `Content-Security-Policy` headers, and neither restricts which assets artifact content may load: the chrome page answers `frame-ancestors 'none'`, and every `/artifact/*` response carries only the `sandbox` directive matching the iframe's `sandbox` attribute, so an escaped popup stays opaque-origin (see [Things to know when editing](#things-to-know-when-editing)). Exports and hosted shares carry neither header. Author-set CSP meta tags are preserved and reported as export notices because they may still block exported inline assets.

<a id="hosted-sharing-ht-mlapp"></a>

### Hosted sharing (ht-ml.app)

`src/html-app.js` (`publishToHtmlApp`) publishes the local-inlined HTML to the share backend `LAVISH_AXI_HTML_APP_API_URL` names, defaulting to ht-ml.app.
The wire contract - endpoint, request body, required response fields, and the optional bearer token - is owned by [docs/self-hosting-share.md](self-hosting-share.md); do not restate it here.
What matters architecturally is that creating a site needs no account or API key, so the response's secret `update_key` is the only credential the user ever gets and it is returned once.
The user-facing contract - third-party disclosure, public by default, private with a password - lives in README's Export and sharing bullet and the runtime share output.
The browser's **Publish link** flow `POST`s `/api/:key/share`; the route is **same-origin guarded** (`isSameOriginRequest`) because publishing is a state-changing, outward-facing action - a cross-origin page must not drive a publish through the loopback server.
ht-ml.app serves hosted pages with no CSP and no sandbox header, so remote CDN/font references load over the viewer's network; hosted shares never include the annotation SDK.
Share passwords are **generated in one place** (`src/share-password.js`) and reach the browser through the `/api/:key/share` response, because `src/chrome-client.js` is served as a raw file and cannot import modules: a browser-side generator would be a second copy of the alphabet and length rules, free to drift from the CLI's. That route echoes a password only when it minted one - a password the user typed is never sent back - and Lavish persists neither it nor the `update_key` anywhere, so `state.json` never becomes a store of hosting credentials.
The host has **no delete endpoint** (`GET`/`PUT` only on a site), so `--unpublish` is a `PUT` of a placeholder page behind a discarded random password. It is not a deletion, the URL still resolves, and every surface has to say so; a flag or a next_step that claims a published page was removed is a lie the user acts on.
The `PUT` password semantics are **probed against the live host, not inferred**, and the evidence lives in a comment on `createHtmlAppUpdatePayload`: omitting `password` preserves the page's current one and sending a new one rotates it, but sending `""` answers 200 and changes nothing. So there is deliberately **no clear-password path** - the host documents a clear it does not perform, and a surface reporting a page as public while it is still gated is the same class of lie as calling `--unpublish` a deletion. Re-probe before adding one back.
Every request that changes hosted state classifies its own failure through `hostRejectedShareWrite` (`src/html-app.js`, shared by the CLI and the browser `POST /api/:key/share` route): only a 4xx proves the host wrote nothing, so a 5xx, a transport failure, or a timeout must be reported as an outcome that may already have landed. A 200 whose body is missing required fields is neither - the page landed - so `publishToHtmlApp` throws through `htmlAppIncompleteResponseError` carrying whatever fields did arrive, and the caller reports a SUCCESSFUL publish rather than hedging. A site_id the host echoes is untrusted (`echoedSiteId`) and never reaches a suggested command; those interpolate the locally validated id. A republish and `--unpublish` say the change may already be live and name a re-run that converges; a CREATE cannot, and says so - the lost response held the only copy of the update_key, so a page that landed that way can never be republished or unpublished, and re-running mints a second page instead of reclaiming the first. Never offer that path a recovery it does not have. Whether Lavish minted a password is NOT what decides that: a generated password is an extra hint layered onto the indeterminate report (a rejection must never carry it, since it gates nothing), never its trigger. Any new path that changes a published page needs the same split, and every command string those errors suggest is built by `republishCommand`/`unpublishCommand` so a recovery hint cannot drift into a shape `resolveShareRequest` rejects. Those commands must never contain a password placeholder: every other placeholder fails loudly when pasted literally, but any non-empty string is a valid password, so a literal `<pw>` would rotate a live page to a secret nobody was told and the host cannot clear it. Name `--private` (it takes no value) or describe the password in words.
An empty or whitespace-only value for one of share's value flags is **refused**, never treated as absent: the host reads an empty password as none, so `--password "$PW"` with an unset variable would publish a PUBLIC page the caller believes is gated (README's `--password` row and the `share` help own that contract).
Setting a password takes effect at the origin, but the **public -> private transition is not instant at the CDN edge** - a page that was public kept answering uncredentialed requests for minutes afterwards. That is a property of the transition, not of the command performing it, so every surface reporting a page as newly gated carries the caveat (today `createShareUpdateOutput`'s private branch, `createShareUnpublishOutput`, the `share` help, and README's Export and sharing bullet); a page that was already private has no such cached copy. It is deliberately absent from the home/skill guidance, which every run pays for.

### AXI integration

The CLI is built on `axi-sdk-js` (`runAxiCli`).
The `home()` callback returns the rich object shown when the user runs `lavish-axi` with no arguments - the same TOON-serialized output that lands in the agent's optional `SessionStart` hook after `lavish-axi setup hooks`; top-level `--help` returns the same static guidance without dynamic sessions.
Poll execution guidance is shared across home output, help, and `next_step` responses through `POLL_WAKE_PATH_RULES`: every harness gets the same completion-aware wake-path contract, while `detectInvokingAgent` adds an attached-turn warning when `CODEX_SANDBOX` or `CODEX_THREAD_ID` identifies Codex. The installable skill does not restate these rules; it points at `lavish-axi --help`.
Agent-facing design guidance is single-sourced in `src/design-reference.js`: `DESIGN_PRIORITY_RULE` states the design-direction priority order exactly once, and `DESIGN_SYSTEM_HINT`, the `lavish-axi design` summary, and the design command help all embed it - never restate the rule on another surface (README carries only a one-sentence summary). The skill points at `lavish-axi design` instead of embedding the rule.
`src/skill.js` renders the minimal installable Agent Skill, a stub pointing to the CLI commands for live guidance. It retains non-interactive `npx -y lavish-axi ...` invocation and slash-command request handling, omits live session state, and includes Hermes Agent frontmatter metadata for categorization.
The generated skill intentionally omits a `version` frontmatter field because release-please updates `package.json` without regenerating `skills/lavish/SKILL.md`.
`skills/lavish/SKILL.md` is the only public Agent Skill shipped through npm.
The repository-local `.agents/skills/lavish-design/SKILL.md` brand skill is internal and must keep `metadata.internal: true` so `npx skills add ... --list` and skills.sh hide it unless `INSTALL_INTERNAL_SKILLS=1` is set.
The bare-arg form (`lavish-axi some.html`) is normalized into `["open", "some.html"]` by `normalizeArgv`, which must let the SDK's `RESERVED_COMMANDS` (such as the built-in `update` self-updater) pass through untouched; otherwise the bare-arg rewrite turns `lavish-axi update` into `["open", "update"]` and the inherited reserved command never reaches `runAxiCli`.

### Agent Plugins packaging

The published package root **is** the Agent Plugin: `plugin.json` sits beside the `skills/` directory the standard discovers, so an installed copy is a conformant plugin with nothing downloaded and no marketplace involved (README's Agent Plugin bullet owns the user-facing contract). Keeping that true is the invariant - both `plugin.json` and `skills/lavish` must stay in `package.json` `files`, and `resolvePluginRoot` resolves `../` from `src/plugin.js`, which is the package root when bundled and the repo root from source.
Agent Plugins delegates skill validity wholesale to the Agent Skills spec and **silently skips** skills that fail it, so a frontmatter regression removes the skill from the plugin with no error anywhere. `validateSkillMarkdown` (`src/skill.js`) encodes the rules the reference validator enforces: only `ALLOWED_SKILL_FRONTMATTER_KEYS` at the top level, no YAML flow collections (`[a, b]`), and `metadata` limited to one level of string values. That is why `author` and `argument-hint` live under `metadata` and the Hermes fields are flattened rather than nested - moving any of them back to the top level silently invalidates the skill.
Each client registers independently and a client that cannot be registered must be _reported_, never thrown: `linkCursorLocalPlugin` returns `unsupported` instead of raising so one unlinkable client cannot abort the command or the other clients. On Windows it prefers a **junction**, because a directory symlink there needs a privilege an ordinary account lacks (Developer Mode or elevation), then falls back to a directory symlink when the junction is refused, such as across volumes. Tests that assert on a real on-disk link skip when symlink creation is unavailable; the link-creation logic itself stays covered everywhere through injected operations.
`setup plugin` registers only clients that install from a local path (VS Code, Cursor, Copilot CLI); Codex installs from marketplace sources only and is deliberately served by the SessionStart hook instead. Registration follows the same discipline as `setup hooks` - explicit invocation only (issue #43), idempotent, and path-repairing - and `isStalePluginLocation` only ever drops entries it can positively attribute to this plugin, so a user's other plugin locations survive. VS Code settings that fail to parse (they legally allow comments) are reported for manual edit, never rewritten.
No `mcp.json` ships: the CLI itself is the agent interface, and adding one would create a second agent-facing contract to keep in sync.

### Telemetry

`src/telemetry.js` posts anonymous events to an Umami endpoint.
The website ID and host can be baked into the bundle at build time via `LAVISH_AXI_UMAMI_HOST`/`LAVISH_AXI_UMAMI_WEBSITE_ID` env vars (consumed by `scripts/build.js` and inlined as `process.env.LAVISH_AXI_BUILD_UMAMI_*` defines).
The build also inlines `package.json`'s version as `process.env.LAVISH_AXI_BUILD_VERSION` for the CLI/server version handshake, with source runs falling back to reading `package.json`.
Users opt out with `LAVISH_AXI_TELEMETRY=0`.
The client is best-effort and must never affect CLI behavior - all errors are swallowed.

## Things to know when editing

- `run()` short-circuits `--version`/`-v`/`-V` (`isVersionOnlyArgv`) before `ensureStateDir` and `initDefaultTelemetry`, because agent harnesses probe every tool's version at session start and the telemetry drain in the `finally` block costs up to a full second. Any new startup work must go after that short-circuit; `test/cli-version.test.js` guards both the latency budget and the "no telemetry request, no state dir" property.
- `canonicalFile` runs `realpath`, so symlinks resolve to their target before becoming session keys. Two paths that refer to the same file always collapse to one session.
- The SDK injected into artifacts lives in `src/artifact-sdk.js` and is wrapped by `createSdkJs`.
  It executes inside an iframe sandboxed with `allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-downloads` (no `allow-same-origin`), so it cannot read the chrome's DOM - communication is `postMessage` only - and it runs the layout audit in the iframe because the chrome cannot directly inspect the sandboxed document. `allow-popups-to-escape-sandbox` lets popups render as top-level tabs without weakening the artifact iframe. Every `/artifact/*` response also carries the matching CSP `sandbox` policy, so an escaped popup that navigates to an artifact-owned active document remains opaque-origin and cannot become a same-origin application client.
  EVERY artifact→chrome message must go through `postArtifactMessage`, the only send path that stamps the current `artifact_load_token`: the chrome's message listener drops any frame message whose token is not the current load's before dispatch, so a raw `parent.postMessage` is silently discarded (a token-less `lavish:uploadAttachment` shipped exactly this break while every mocked harness stayed green - the chrome harness must therefore send test messages verbatim, never patch the token in).
  Nothing (Tailwind, DaisyUI, Mermaid, layout safety CSS) is auto-injected into artifacts; agents choose a design direction via the single-sourced `DESIGN_PRIORITY_RULE` (see AXI integration above).
  The `lavish-axi design` Mermaid snippet chooses dark or light rendering from the effective artifact page background and re-renders when a page-theme or OS appearance change alters that appearance, so do not hardcode one Mermaid theme.
- For rendered Mermaid SVGs outside `.mermaid` containers, the injected SDK retains dependency-free viewBox pan (drag) and zoom (wheel) in explore mode, then freezes it in annotation mode so a click resolves cleanly to one node instead of panning. It enhances on load and `DOMContentLoaded` and re-runs through a throttled `MutationObserver` because Mermaid renders asynchronously and can re-render. Enhancement touches only the live SVG's `viewBox` and listeners, never the saved artifact, so the diagram still renders identically when opened directly. Node detection, label extraction, and target validation live in `src/mermaid-node.js` so they are unit-testable and shared with the server.
- Any helper `createArtifactSdk` calls must reach the browser through `serializeModuleHelpers` in `createSdkJs`, which turns every export of a shared module (`src/mermaid-node.js`, `src/table-cell.js`, `src/artifact-revisions.js`) into a same-scope `const`. A module-private function called from the SDK closure compiles fine and only `ReferenceError`s on the first click, so put new helpers in one of those wholesale-serialized modules and export them; a helper may then reference only its own arguments, browser globals, or its sibling exports - never a module-level constant, which is not serialized. Those modules must export functions and nothing else: only functions survive `toString()`, so `serializeModuleHelpers` throws on any other export rather than shipping a `Set` or `RegExp` that would arrive as an empty `{}`. `test/artifact-sdk-bundle.test.js` boots the served bundle and drives a real click, which is what catches an unreachable helper; the module-level unit tests cannot.
- Table-cell annotations attach `src/table-cell.js`'s semantic row/column names as `target` only. The clicked element's own `selector`, `tag`, and `text` keep describing that element, because the on-screen highlight outlines exactly what was clicked. Both coordinates stay silent rather than name a row or column they cannot prove, because a confidently wrong name reads as authoritative and is worse than none: a rowspan is clipped to its own row group, so only one starting in an earlier row of that group (including `rowspan="0"`, which runs to the end of it) makes a row's DOM order stop being its rendered order, and that suppresses the row's positional heading - only a declared `scope="row"` heading survives it - while the column label needs the header row unshifted the same way, plus a row whose colspans sum to the header's and a cell that does not straddle a grouped header.
  A grouped header's `<th rowspan="2">` therefore costs the leaf header row its names and leaves every `<tbody>` row nameable.
  Spans come from the browser-parsed `rowSpan`/`colSpan` whenever present, because HTML's integer rules stop at the first non-digit and render `rowspan="2x"` as a real two-row span that `Number` reads as `NaN`. Resolving a cell walks its whole table, so `context()` computes the target only under `{ table: true }`, which the annotation card passes and `snapshot()` - which calls `context()` for every element in the document - deliberately does not.
- Annotation handlers ignore native controls (`button`, `input`, `select`, `textarea`, `option`, `label`, `summary`, editable regions, and elements with an interactive ARIA widget role such as `role="button"` or `role="menuitem"`) and their descendants, so they stay interactive without markup; an `<a href>` stays annotatable when it carries such a role or sits inside such a widget, because a passed-through click would navigate the artifact frame away; `data-lavish-action` opts custom non-native controls out of annotation and gives them a pointer cursor. Artifact-author guidance for input patterns (`data-lavish-question`, `queueKey`, per-question submits) is owned by the input playbook in `src/playbooks.js`.
- For text annotations, `prompt.selector` is the common ancestor/container selector, not the complete identity. Use the `target` range boundaries and snapshot context to locate the exact selected text.
- For non-whiteboard Mermaid diagram nodes, a click annotates the whole rendered `<g>` node - not the sub-shape under the cursor - and hover highlights the same node. `SessionStore.normalizeTarget` routes these targets through `normalizeMermaidNodeTarget`, which strips them to the fixed `type`/`diagramId`/`nodeId`/`label`/`selector` shape, while text-range and other/legacy targets pass through unchanged.
- `SessionStore` re-reads and re-writes the entire `state.json` on every operation - there is no in-memory cache. The single server process is necessary but NOT sufficient for consistency: a method that reads state, `await`s, then writes can still interleave with another method's read-modify-write and lose its update. Every mutation therefore serializes through the store's single `AsyncMutex` (`store.lock`); see the Image attachments section (E1) for the full invariant and the one lock-free exception (`referencedAttachmentIds`).
- Below 860px the conversation panel is a fixed bottom sheet with a persistent dock (the phone block in `src/chrome.css`; README's Reviewing on a phone bullet owns the user-facing behavior), and the chrome's sheet controller in `src/chrome-client.js` owns open/closed intent, `inert` on the hidden half, focus handoff, gestures, visual-viewport synchronization, and the dock summary. `MOBILE_SHEET_MEDIA` there must match the CSS breakpoint. Four rules are easy to break: desktop stays pixel-identical only because `.panel-head`/`.panel-head-row` are `display: contents` outside the breakpoint (the `h2` must remain a direct flex child of `.panel`); the collapsed state is a `translateY`, never a height change, so the chat keeps its layout and the sheet can follow a drag, which is also why the phone panel carries a shadow hairline instead of a border (a 1px border pushes the docked head past the viewport edge); the sheet is sized from `--vv-top`/`--vv-height`, which `syncVisualViewport` keeps equal to the visual viewport, so the iOS keyboard shrinks it instead of covering the composer (Android gets the same through `interactive-widget=resizes-content` in the viewport meta, and `viewport-fit=cover` is what makes the `env(safe-area-inset-*)` padding non-zero); and the mobile composer is its own scrollport with sticky send actions while `.panel-scroll` yields its minimum height first under visual-viewport pressure, keeping the actions reachable even with attachments and a keyboard. Real geometry is pinned by the opt-in `test/mobile-conversation-sheet.browser.test.js`. The desktop panel collapse (`#sidebarToggle`, `body.panel-collapsed`, one viewer-wide `localStorage` key) must never reach the phone layout: its CSS sits under `@media not all and (max-width: 860px)`, the exact complement of the sheet breakpoint, and the client sets the class only while `MOBILE_SHEET_MEDIA` does not match, so a stored collapse cannot hide the dock.
- The chrome and the sandboxed artifact document cannot see each other's keyboard events (no `allow-same-origin`), so any keyboard shortcut that must work regardless of focus needs its own capture-phase `document.addEventListener("keydown", ..., true)` in _both_ `src/chrome-client.js` and `src/artifact-sdk.js`, not just one.
  The annotate/explore mode toggle hotkey (`MODE_TOGGLE_HOTKEY_KEY`, Cmd/Ctrl+I) is the reference implementation: the SDK initializes from `data-lavish-annotate` on the root html element (only `"off"` disables), and reports that default once with token-stamped `lavish:annotationMode`. The chrome accepts one boolean default per artifact load until the reviewer explicitly toggles, then keeps that choice across artifact reloads and reconciles it back to the SDK, including when frame-load replay arrives before the default report. On catching the hotkey the SDK sends `{ type: "lavish:toggleAnnotationMode" }` to the chrome, which drives the exact same `toggleAnnotationMode()` function the on-screen switch's `onclick` calls.
  Requiring a modifier (`metaKey || ctrlKey`) is what lets the listener safely call `preventDefault()` without breaking plain typing (including typing the bound letter itself) in the chat box or an annotation-card textarea.
- Tests use `LAVISH_AXI_STATE_DIR` and ephemeral ports to stay isolated. When adding tests that spin up the server, do the same.
- Circular close buttons (`.queued-remove`, `.share-close`) render an inline SVG x mark with two symmetric strokes, not a text `x`/`&times;` glyph.
  Font metrics put text glyphs off from the geometric center even under flex centering, while the SVG centers via flex plus equal viewBox margins.
  Keep the SVG strokes on `currentColor` so existing hover color rules still apply, and follow this pattern for any new circular icon-only button.
- The in-iframe layout audit (`src/artifact-sdk.js`) is severe-only and fails open on uncertainty; its easy-to-reintroduce failure modes are covered by dedicated and browser-level tests:
  - Scroll dimensions and parent overhang are never proof by themselves. `classifySevereTextOverflow` requires rendered text-range fragments from one semantic text boundary to materially cross that boundary, excludes explicit truncation, masks, and standard visually hidden text, and reports vertical loss only when a line's center leaves its box.
  - Diagram surfaces (`.mermaid`, SVG, and `[data-lavish-ui]`) stay outside the general audit so it does not compete with the separate Mermaid and Excalidraw diagram-label clipping path.
  - Page overflow requires both a material document delta and meaningful text or required-control bounds beyond the usable viewport, producing one `html` root finding instead of descendant geometry noise.
  - Finite animations settle before sampling, findings associated with still-active finite or infinite motion stay silent without hiding independent stable failures, and `findStableLayoutFindings` requires the same severe root in two samples.
  - Overlap reports only near-total coverage by one opaque static sibling; decorative transparent overlap stays silent. Warning-severity input is filtered again by the chrome and by `normalizeFindings` in `src/layout-warnings.js`.
  - The audit reports its own completeness. A failed run must publish `complete: false` with no findings, never an empty completed pass - an empty completed pass is read as evidence of repair, so the distinction is what keeps a crashed audit from silently resolving real warnings.

- The self-paint check (`src/self-paint.js`, surfaced by `open`/`export`/`share` as `self_paint_warning`) is render-free and fails open by design: any stylesheet link, `@import`, Tailwind runtime script, `color-scheme`, or html/body/:root background signal suppresses it, because a false warning on every open is worse than a miss from this intentionally conservative static check. Keep it a warning - never a blocked open, never auto-repair.

- The chrome page ships from `createChromeHtml` with the layout-gate overlay ALREADY covering the artifact area. `CHROME_BOOT_FAILSAFE_JS` is inlined BEFORE the `<script src="/chrome-client.js">` tag (a request that hangs rather than errors blocks parsing, so a failsafe placed after the tag would never be reached), installs the shared gate escape before the client can fail, and handles the script's `onerror` and boot timeout. The client reuses that escape and cancels only the boot-failure timer by setting `window.__lavishChromeReady` at the very end of the file. Keep the placement, timeout, end-of-file cancellation, ended-session guard, bounded gate hold, and network-independent **Show anyway** path: the escape must work even when the client script or server does not.
- The artifact iframe carries only `data-artifact-src` and is navigated exclusively by `replaceArtifactFrame`, so a chrome whose FIRST begin-load fails has no previous frame to preserve - abandoning the load there leaves an empty frame and an `artifact_revision` that never advances, which is what a session reopened across a server restart looked like. Recoverable outcomes (a transport failure past `ARTIFACT_LOAD_BEGIN_RETRY_DELAYS_MS`, or a `no-handoff` whose one re-handshake also failed) must schedule a fresh attempt through `ARTIFACT_LOAD_RECOVERY_DELAYS_MS` and, once that is exhausted with nothing on screen, surface `setLayoutGateFailure` instead of a silent blank. `superseded` and `out-of-order` must NOT retry: another reviewer or a newer request in this same chrome owns the artifact, and a background retry would fight it. A `superseded` chrome that has nothing on screen still has to say so on the gate overlay (`setLayoutGateFailure` with a takeover reload), because the takeover banner lives in the conversation panel, which the overlay covers - without that the page holds the checking spinner for the full gate hold and then reveals an empty frame with its only recovery control hidden the whole time. A `superseded` chrome that already shows an artifact must keep it and use the banner alone.
- The layout-warning inbox's rules are the product contract, not implementation detail - `src/layout-warnings.js` and `test/layout-warnings.test.js` are the authority, and the lifecycle is also restated for users in README and for agents in the poll guidance. Two invariants are easy to break by accident:
  - Nothing may clear a warning except a newer artifact revision plus a **complete** pass at the **same viewport class** that no longer detects it. Not a closed drawer, a checked box, a queued or delivered prompt, an agent reply, a reload in flight, a temporarily absent element, another viewport passing, or a failed diagnostic run.
  - Adding a route or UI action that emits `feedback` for a detection makes the whole feature regress to the auto-repair churn it replaced. Only user actions (`/api/:key/prompts`) and the narrow fatal path may emit it.

- The revision legend (`src/artifact-revisions.js`, README's Revisions legend bullet) reads an agent-declared `data-lavish-revisions` registry and `data-lavish-revision` marks; the SDK is read-only and never marks up the artifact, so the served bytes stay identical to the file on disk. Three invariants are easy to break by accident:
  - `resetRevisionLegend()` in `src/chrome-client.js` must run only right before `replaceArtifactFrame` actually reassigns `frame.src`, never unconditionally at the top of that function. A preserved load (`superseded`, `out-of-order`, an exhausted retry) never reassigns `frame.src`, so clearing the legend there strips it from an artifact that is still on screen and whose SDK will never re-report it.
  - The legend's per-row cap (`entries` in both `revisionLimits()` and the chrome's `REVISION_LIMITS`) must derive from the shared `revisionPalette()` length, not a second hardcoded number - a cap that outgrows the palette hands two revisions the same colour, border, and pattern.
  - The chrome re-validates the postMessage payload as untrusted input from a sandboxed frame: an id or selector over its length limit is rejected outright, never truncated, because a truncated id can collide with another revision's and a truncated selector is still valid CSS pointing somewhere else. `__proto__` is a legal revision id, so lookups use a `Map`/`Set`, never a plain object key.

- The whiteboard has six easy-to-reintroduce failure modes, all covered by tests or explained in comments:
  - Mermaid skeletons must be materialized again after Excalidraw's scene fonts load; the first synchronous materialization uses a narrower browser-serif fallback and stores text bounds that clip the eventual Excalifont glyphs.
    Keep the font-load and second-conversion ordering in `convertExcalidrawSkeletonsAfterFontsLoad`, and keep the versioned saved-scene repair expansion-only so it never overwrites user geometry or content.
    The real-browser regression in `test/whiteboard-render.browser.test.js` covers both paths.
  - Mermaid node labels use `<br>` / `<br/>` and a two-character `\n` as line breaks. `parseMermaidToExcalidraw` copies `vertex.text` onto skeleton `label.text` unchanged, so those markers stay literal characters and Excalidraw concatenates "classify<br>checks" into one line. `restoreMermaidLabelLineBreaks` in `src/whiteboard-core.js` must run on skeletons before `convertToExcalidrawElements` (and again on materialized text with a measure pass) so Excalidraw `text` / `originalText` get real `\n` and the box sizes to the line set. When that pass grows a node-label container (rectangle, ellipse, diamond) from the center, it must also reposition the independently stored bound-text `x`/`y` into the new box; skip labelled arrows, whose labels sit at path midpoints. `convertSource` mounts without `restore()`, so Excalidraw will not re-derive that geometry on first paint. `test/whiteboard-core.test.js` and the clipping browser fixture cover both break forms, the fusion case, bound-text recentering, and labelled-arrow skip.
  - The converter breaks with mermaid >= 11.14.0: its parsers reach into mermaid's rendered DOM/db internals, and newer versions silently degrade class/ER/state diagrams and subgraph flowcharts to image fallbacks. `mermaid` is pinned EXACTLY (independent of the artifact-facing Mermaid CDN version in `src/design-reference.js`), and `test/whiteboard-pins.test.js` fails any unpinning; bumping requires a live re-probe of native conversion.
  - Excalidraw's theme must be passed only through the `<Excalidraw theme>` prop, and persisted `appState` must never carry `theme` or a dark-space `viewBackgroundColor`: dark mode renders through an invert filter, so a dark background value or a second theme application double-inverts into a washed-out canvas (`src/whiteboard-core.js` strips both at the persistence boundary).
  - `/whiteboard-assets/*` must keep `Access-Control-Allow-Origin: *` (the opaque-origin frame's font fetches are CORS-gated), `Cache-Control: no-cache` (an unversioned bundle URL plus memory cache serves stale editors after upgrades), and `dotfiles: "allow"` in sendFile (a checkout under a dot-directory otherwise 403s every asset).
  - A sidecar's presence is not a user edit: `startFromConversion` autosaves on view, including scroll/zoom from fit-to-content. `handleInit` must go through `resolveWhiteboardInitAction` so a Mermaid-source change silently re-converts an unmodified-since-conversion scene and only prompts when `savedSceneHasPreservableEdits` finds preservable edits. Treating "saved scene exists with a different hash" as the prompt condition brings back the phantom re-convert/keep banner on live agent updates.


### docs/self-hosting-share.md
# Self-hosting the share backend

`lavish-axi share` publishes to [ht-ml.app](https://ht-ml.app) by default. Set
`LAVISH_AXI_HTML_APP_API_URL` to point `share` at a backend you control instead.
This page documents the contract that backend must implement.

## Configuration

| Env var                       | Purpose                                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LAVISH_AXI_HTML_APP_API_URL` | Base URL of your share backend. Defaults to `https://api.ht-ml.app`; trailing slashes are stripped.                                                                                                                          |
| `LAVISH_AXI_HTML_APP_TOKEN`   | Optional bearer token for `POST /v1/sites` only, sent as `Authorization: Bearer <token>`. Also settable per call with `--token`. Republishes authorize with the page's `update_key` instead, so `--token` is rejected there. |

## Contract

`share` creates a page with one request, and republishes an existing one with a second:

```
POST {LAVISH_AXI_HTML_APP_API_URL}/v1/sites
Content-Type: application/json
Authorization: Bearer <token>          # only when a token is configured

{
  "html_content": "<full inlined HTML>",
  "password": "<optional>"             # present when --password or --private is used
}
```

The response must be JSON containing at least `url` and `update_key` — `share`
errors if either is missing:

```json
{
  "url": "https://plans.example.com/abc123",
  "update_key": "<secret, shown once>",
  "site_id": "abc123",
  "status": "published"
}
```

- `url` — where the published artifact is viewable. Your backend owns this; it can be any URL on your domain.
- `update_key` — an opaque secret returned to the user for managing the page later.
- `site_id` — optional, but it is what the user passes back as `--site` to republish or unpublish, so a backend that omits it supports creation only. It is interpolated into the `PUT` path, so `share` accepts only `A-Za-z0-9._-` and refuses an all-dots id; pick ids from that set.
- `status` — optional; surfaced if present.

### Republishing

`share --site <site_id> --update-key <key>` (and `--unpublish`, which sends a placeholder page)
replaces an existing page in place:

```
PUT {LAVISH_AXI_HTML_APP_API_URL}/v1/sites/{site_id}
Content-Type: application/json
Authorization: Bearer <update_key>

{
  "html_content": "<full inlined HTML>",
  "password": "<optional>"             # absent on a plain republish; present to set or rotate one
}
```

There is no way to remove a page's password. Lavish never sends an empty `password`, and offers no
flag that would: ht-ml.app answers `200` to a clear and leaves the page gated, so a backend that
implements one cannot be told apart from one that does not, and the CLI would report a page as
public while it is still private.

`Authorization` on this request carries the `update_key`, not the create-time bearer token, so a
backend that gates `POST /v1/sites` with a shared token has to authorize `PUT` by the stored
`update_key` alone. `--token` is rejected on a republish rather than silently dropped, because the
header has no room for both.

The response may repeat `url`, `site_id`, and `status`. Return `url`: when the body omits one,
`share` reports the republish without a URL rather than guessing a host, since the API base is
yours. Reject the request with `401` when the `update_key` does not match: that key is the page's
only credential, so treating a bad one as a no-op silently loses the update.

`share` never issues a `DELETE`. ht-ml.app has no delete endpoint, and `--unpublish` is a `PUT` of a
placeholder page behind a fresh password, so a backend implementing this contract needs no delete
route either.

Both requests time out after 30 seconds.

## Minimal reference (Cloudflare Worker)

```js
export default {
  async fetch(req, env) {
    const { pathname } = new URL(req.url);
    const bearer = (req.headers.get("authorization") || "").replace(/^Bearer /, "");

    if (req.method === "POST" && pathname === "/v1/sites") {
      // Require the bearer token — an open endpoint hosts arbitrary HTML on your domain.
      if (bearer !== env.SHARE_TOKEN) return new Response("Unauthorized", { status: 401 });

      const { html_content, password } = await req.json();
      const id = crypto.randomUUID().slice(0, 8);
      const update_key = crypto.randomUUID();
      await env.SITES.put(id, JSON.stringify({ html_content, password: password || null, update_key }));

      return Response.json({
        url: `https://${env.VIEW_HOST}/${id}`,
        update_key,
        site_id: id,
        status: "published",
      });
    }

    const site = pathname.startsWith("/v1/sites/") && pathname.slice("/v1/sites/".length);
    if (req.method === "PUT" && site && !site.includes("/")) {
      const stored = await env.SITES.get(site, "json");
      // The update_key is the page's only credential — a mismatch must fail, never no-op.
      if (!stored || bearer !== stored.update_key) return new Response("Unauthorized", { status: 401 });

      const { html_content, password } = await req.json();
      // An absent password preserves the stored one; a present one sets or rotates it.
      await env.SITES.put(site, JSON.stringify({ ...stored, html_content, password: password || stored.password }));

      return Response.json({ url: `https://${env.VIEW_HOST}/${site}`, site_id: site, status: "published" });
    }

    return new Response("Not found", { status: 404 });
  },
};
```

Serve the viewer (`GET /:id`) from a **separate origin** so untrusted artifact
JavaScript never runs on your app's origin, and enforce the stored `password`
before returning the HTML.

## Security notes

- **Gate publish with a token.** An unauthenticated `/v1/sites` lets anyone host arbitrary HTML on your domain — a phishing and malware vector wearing your name.
- **Isolate the viewer origin.** Published artifacts run their own JavaScript; serve them from a dedicated host with a restrictive CSP so a script in one artifact can't reach your app's cookies or session.
- **Honor `password`.** When present, require it before serving the artifact.


## Top-level structure
- .agents/ — vendored agent skill content
- .claude/ — Claude Code plugin/config
- .github/ — CI, release-please
- AGENTS.md — every-session agent rules (points to README/VISION/docs owners)
- CLAUDE.md — Claude-specific instructions
- VISION.md — acceptance policy for the review loop
- CONTRIBUTING.md — PR gate via no-mistakes
- bin/ — CLI entry
- docs/ — delivery-acks, invariants, self-hosting-share
- skills/lavish/ — generated Agent Skill stub (points at CLI --help)
- src/ — ESM JS: cli, server, chrome UI, whiteboard/mermaid, layout warnings, export/share, playbooks, skill/plugin generators
- test/ — node:test suite (+ optional browser E2E via chrome-devtools-axi)
- lavish-editor-marketing/ — marketing GIF/assets
- plugin.json — Agent Plugin manifest at package root
- package.json / pnpm workspace — Node 22+ ESM
