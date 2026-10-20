# stablyai/orca

## Metadata
- Stars: 98679
- Primary language: TypeScript
- Default branch: main
- Latest release: v1.4.232
- License: MIT License
- Homepage: https://orca.dev
- Pushed: 2026-10-20T06:58:33Z
- Fetched: 2026-10-20
- Final URL: https://github.com/stablyai/orca

## Description
Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.

## README
<h1 align="center">
  <a href="https://onOrca.dev"><img src="resources/build/icon.png" alt="Orca" width="64" valign="middle" /></a> Orca
</h1>

<p align="center">
  <a href="https://github.com/stablyai/orca"><img src="https://img.shields.io/github/stars/stablyai/orca?style=flat&amp;label=%E2%98%85&amp;color=08C" alt="GitHub stars" /></a>
  <a href="https://github.com/stablyai/orca/releases"><img src="docs/assets/readme-downloads.svg" alt="Total downloads across all releases" /></a>
  <img src="https://img.shields.io/badge/license-MIT-08C?style=flat" alt="License: MIT" />
  <a href="https://discord.gg/fzjDKHxv8Q"><img src="https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white" alt="Join the Orca Discord" /></a>
  <a href="https://x.com/orca_build"><img src="https://img.shields.io/badge/X-000000?logo=x&logoColor=white" alt="Follow Orca on X" /></a>
  <img src="https://img.shields.io/badge/macOS%20%7C%20Windows%20%7C%20Linux-4493F8?style=flat-square" alt="Supported platforms: macOS, Windows, and Linux" />
</p>

<p align="center">
  <sub><a href="docs/readme/README.zh-CN.md">中文</a> · <a href="docs/readme/README.ja.md">日本語</a> · <a href="docs/readme/README.ko.md">한국어</a> · <a href="docs/readme/README.es.md">Español</a> · <a href="docs/readme/README.fr.md">Français</a> · <a href="docs/readme/README.pt.md">Português</a></sub>
</p>

<p align="center">
  <strong>The AI Orchestrator for 100x builders.</strong><br/>
  Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.
</p>

<h3 align="center"><a href="https://onorca.dev/download"><ins>Download Orca</ins></a></h3>

<p align="center">
  <img src="docs/assets/readme-hero.jpg" alt="Orca desktop app running agents in parallel worktrees, with the Orca mobile companion app in the corner" width="960" />
</p>

## Features

<table>
<tr>
<td width="50%" valign="middle">

### Mobile Companion

Monitor and steer your agents from your phone — get notified when an agent finishes and send follow-ups from anywhere.

[iOS App Store](https://apps.apple.com/us/app/orca-ide/id6766130217) · [Android APK](https://www.onorca.dev/download/android) · [Docs →](https://www.onorca.dev/docs/mobile)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/mobile"><picture><source srcset="docs/assets/feature-wall/mobile-companion-app-showcase.gif" type="image/gif"><img src="docs/assets/feature-wall/mobile-companion-app-showcase.jpg" alt="Orca desktop with the mobile companion app" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Parallel Worktrees

Fan one prompt across five agents, each in its own isolated git worktree — compare the results and merge the winner.

[Docs →](https://www.onorca.dev/docs/model/worktrees)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/model/worktrees"><picture><source srcset="docs/site/public/docs/tab-split.gif" type="image/gif"><img src="docs/site/public/docs/posters/tab-split.jpg" alt="Parallel worktree orchestration" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Terminal Splits

Ghostty-class terminals with WebGL rendering, infinite splits, and scrollback that survives restarts.

[Docs →](https://www.onorca.dev/docs/terminal)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/terminal"><picture><source srcset="resources/onboarding/feature-wall/tile-02.webp" type="image/webp"><img src="resources/onboarding/feature-wall/tile-02.poster.jpg" alt="Terminal splits" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Design Mode

Click any UI element in a real Chromium window to send its HTML, CSS, and a cropped screenshot straight into your agent's prompt.

[Docs →](https://www.onorca.dev/docs/browser/design-mode)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/browser/design-mode"><picture><source srcset="docs/site/public/docs/orca-design-mode.gif" type="image/gif"><img src="resources/onboarding/feature-wall/tile-05.poster.jpg" alt="Embedded browser and Design Mode" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### GitHub &amp; Linear, Native

Browse PRs, issues, and project boards in-app — open a worktree from any task and review without a context switch.

[Docs →](https://www.onorca.dev/docs/review/linear)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/review/linear"><picture><source srcset="resources/onboarding/feature-wall/tile-03.webp" type="image/webp"><img src="resources/onboarding/feature-wall/tile-03.poster.jpg" alt="GitHub and Linear task workflows in Orca" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### SSH Worktrees

Run agents on a beefy remote box with full file editing, git, and terminals — auto-reconnect and port forwarding included.

[Docs →](https://www.onorca.dev/docs/ssh)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/ssh"><picture><source srcset="resources/onboarding/feature-wall/tile-06.webp" type="image/webp"><img src="resources/onboarding/feature-wall/tile-06.poster.jpg" alt="Remote worktrees over SSH" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Annotate AI Diffs

Drop comments on any diff line and ship them back to the agent — review, edit, and commit without leaving Orca.

[Docs →](https://www.onorca.dev/docs/review/annotate-ai-diff)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/review/annotate-ai-diff"><picture><source srcset="docs/site/public/docs/annotate-ai-diff.gif" type="image/gif"><img src="resources/onboarding/feature-wall/tile-08.poster.jpg" alt="Annotate AI-generated diffs" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Drag Files to Agents

VS Code's editor with autosave everywhere — drag files or images straight into an agent prompt.

[Docs →](https://www.onorca.dev/docs/editing/file-explorer)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/editing/file-explorer"><picture><source srcset="resources/onboarding/feature-wall/tile-07.gif" type="image/gif"><img src="resources/onboarding/feature-wall/tile-07.poster.jpg" alt="Drag files and images into an agent prompt" width="100%" /></picture></a>
</td>
</tr>
<tr>
<td width="50%" valign="middle">

### Orca CLI

Agents drive Orca too — script every workflow with `orca worktree create`, `snapshot`, `click`, and `fill`.

[Docs →](https://www.onorca.dev/docs/cli/overview)

</td>
<td width="50%">
  <a href="https://www.onorca.dev/docs/cli/overview"><picture><source srcset="resources/onboarding/feature-wall/tile-09.webp" type="image/webp"><img src="resources/onboarding/feature-wall/tile-09.poster.jpg" alt="Script Orca from the CLI" width="100%" /></picture></a>
</td>
</tr>
</table>

**Also in the box:**

- **[Quick open](https://www.onorca.dev/docs/model/quick-open)** — Search across worktrees, files, agents, commands, and repo context without leaving your flow.
- **[Account switcher &amp; usage tracking](https://www.onorca.dev/docs/agents/usage-tracking)** — See Claude and Codex usage and rate-limit resets, and hot-swap accounts without re-logging in.
- **[Rich repo previews](https://www.onorca.dev/docs/editing/markdown)** — Preview Markdown, images, PDFs, and repo docs in the workspace.
- **[Computer Use](https://www.onorca.dev/docs/cli/computer-use)** — Let agents operate desktop apps and visible UI when a workflow needs real interaction.
- **[Notifications and unread state](https://www.onorca.dev/docs/notifications)** — Know when an agent finishes or needs attention, then mark threads unread to come back later.
- **And many, many more** — we ship daily, so this list is perpetually behind. The [changelog](https://github.com/stablyai/orca/releases) is the real feature list.

---

## Supported Agents

Works with **any CLI agent** — if it runs in a terminal, it runs in Orca.

<p>
  <a href="https://docs.anthropic.com/claude/docs/claude-code"><kbd><img src="docs/assets/claude-logo.svg" alt="Claude Code logo" width="16" valign="middle" /> Claude Code</kbd></a> &nbsp;
  <a href="https://github.com/openai/codex"><kbd><img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" alt="Codex logo" width="16" valign="middle" /> Codex</kbd></a> &nbsp;
  <a href="https://x.ai/cli"><kbd><img src="https://www.google.com/s2/favicons?domain=x.ai&sz=64" alt="Grok logo" width="16" valign="middle" /> Grok</kbd></a> &nbsp;
  <a href="https://cursor.com/cli"><kbd><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" alt="Cursor logo" width="16" valign="middle" /> Cursor</kbd></a> &nbsp;
  <a href="https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli"><kbd><img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" alt="GitHub Copilot logo" width="16" valign="middle" /> GitHub Copilot</kbd></a> &nbsp;
  <a href="https://dev.meta.ai/docs/muse-code"><kbd><img src="src/shared/agent-icons/muse.png" alt="Muse logo" width="16" valign="middle" /> Muse</kbd></a> &nbsp;
  <a href="https://deepseek-harness.github.io/deepseek-harness/"><kbd><img src="src/shared/agent-icons/dsh.png" alt="DeepSeek Harness logo" width="16" valign="middle" /> DeepSeek Harness</kbd></a> &nbsp;
  <a href="https://zcode.z.ai/en/docs"><kbd><img src="src/shared/agent-icons/zcode.png" alt="ZCode logo" width="16" valign="middle" /> ZCode</kbd></a> &nbsp;
  <a href="https://opencode.ai/docs/cli/"><kbd><img src="https://www.google.com/s2/favicons?domain=opencode.ai&sz=64" alt="OpenCode logo" width="16" valign="middle" /> OpenCode</kbd></a> &nbsp;
  <a href="https://mimo.xiaomi.com/coder"><kbd><img src="https://www.google.com/s2/favicons?domain=mimo.xiaomi.com&sz=64" alt="MiMo Code logo" width="16" valign="middle" /> MiMo Code</kbd></a> &nbsp;
  <a href="https://ampcode.com/manual#install"><kbd><img src="https://www.google.com/s2/favicons?domain=ampcode.com&sz=64" alt="Amp logo" width="16" valign="middle" /> Amp</kbd></a> &nbsp;
  <a href="https://openclaude.gitlawb.com/"><kbd><img src="resources/openclaude-logo.png" alt="OpenClaude logo" width="16" valign="middle" /> OpenClaude</kbd></a> &nbsp;
  <a href="https://antigravity.google/docs/cli-overview"><kbd><img src="https://www.google.com/s2/favicons?domain=antigravity.google&sz=64" alt="Antigravity logo" width="16" valign="middle" /> Antigravity</kbd></a> &nbsp;
  <a href="https://pi.dev"><kbd><img src="https://pi.dev/favicon.svg" alt="Pi logo" width="16" valign="middle" /> Pi</kbd></a> &nbsp;
  <a href="https://omp.sh"><kbd><img src="https://omp.sh/favicon.svg" alt="oh-my-pi logo" width="16" valign="middle" /> oh-my-pi</kbd></a> &nbsp;
  <a href="https://hermes-agent.nousresearch.com/docs/"><kbd><img src="https://www.google.com/s2/favicons?domain=nousresearch.com&sz=64" alt="Hermes Agent logo" width="16" valign="middle" /> Hermes Agent</kbd></a> &nbsp;
  <a href="https://devin.ai/cli"><kbd><img src="https://www.google.com/s2/favicons?domain=devin.ai&sz=64" alt="Devin logo" width="16" valign="middle" /> Devin</kbd></a> &nbsp;
  <a href="https://block.github.io/goose/docs/quickstart/"><kbd><img src="https://www.google.com/s2/favicons?domain=goose-docs.ai&sz=64" alt="Goose logo" width="16" valign="middle" /> Goose</kbd></a> &nbsp;
  <a href="https://docs.augmentcode.com/cli/overview"><kbd><img src="https://www.google.com/s2/favicons?domain=augmentcode.com&sz=64" alt="Auggie logo" width="16" valign="middle" /> Auggie</kbd></a> &nbsp;
  <a href="https://github.com/autohandai/code-cli"><kbd><img src="https://www.google.com/s2/favicons?domain=autohand.ai&sz=64" alt="Autohand Code logo" width="16" valign="middle" /> Autohand Code</kbd></a> &nbsp;
  <a href="https://github.com/charmbracelet/crush"><kbd><img src="https://www.google.com/s2/favicons?domain=charm.sh&sz=64" alt="Charm logo" width="16" valign="middle" /> Charm</kbd></a> &nbsp;
  <a href="https://docs.cline.bot/cline-cli/overview"><kbd><img src="https://www.google.com/s2/favicons?domain=cline.bot&sz=64" alt="Cline logo" width="16" valign="middle" /> Cline</kbd></a> &nbsp;
  <a href="https://www.codebuddy.ai/cli"><kbd><img src="https://www.google.com/s2/favicons?domain=codebuddy.ai&sz=64" alt="CodeBuddy logo" width="16" valign="middle" /> CodeBuddy</kbd></a> &nbsp;
  <a href="https://www.codebuff.com/docs/help/quick-start"><kbd><img src="https://www.google.com/s2/favicons?domain=codebuff.com&sz=64" alt="Codebuff logo" width="16" valign="middle" /> Codebuff</kbd></a> &nbsp;
  <a href="https://freebuff.com"><kbd><img src="src/shared/agent-icons/freebuff.png" alt="Freebuff logo" width="16" valign="middle" /> Freebuff</kbd></a> &nbsp;
  <a href="https://commandcode.ai/docs/quickstart"><kbd><img src="https://www.google.com/s2/favicons?domain=commandcode.ai&sz=64" alt="Command Code logo" width="16" valign="middle" /> Command Code</kbd></a> &nbsp;
  <a href="https://docs.continue.dev/guides/cli"><kbd><img src="https://www.google.com/s2/favicons?domain=continue.dev&sz=64" alt="Continue logo" width="16" valign="middle" /> Continue</kbd></a> &nbsp;
  <a href="https://docs.factory.ai/cli/getting-started/quickstart"><kbd><img src="docs/assets/droid-logo.svg" alt="Droid logo" width="16" valign="middle" /> Droid</kbd></a> &nbsp;
  <a href="https://kilo.ai/docs/cli"><kbd><img src="https://raw.githubusercontent.com/Kilo-Org/kilocode/main/packages/kilo-vscode/assets/icons/kilo-light.svg" alt="Kilocode logo" width="16" valign="middle" /> Kilocode</kbd></a> &nbsp;
  <a href="https://www.kimi.com/code/docs/en/kimi-code-cli/getting-started.html"><kbd><img src="https://www.google.com/s2/favicons?domain=moonshot.cn&sz=64" alt="Kimi logo" width="16" valign="middle" /> Kimi</kbd></a> &nbsp;
  <a href="https://kiro.dev/docs/cli/"><kbd><img src="https://www.google.com/s2/favicons?domain=kiro.dev&sz=64" alt="Kiro logo" width="16" valign="middle" /> Kiro</kbd></a> &nbsp;
  <a href="https://github.com/mistralai/mistral-vibe"><kbd><img src="https://www.google.com/s2/favicons?domain=mistral.ai&sz=64" alt="Mistral Vibe logo" width="16" valign="middle" /> Mistral Vibe</kbd></a> &nbsp;
  <a href="https://github.com/QwenLM/qwen-code"><kbd><img src="https://www.google.com/s2/favicons?domain=qwenlm.github.io&sz=64" alt="Qwen Code logo" width="16" valign="middle" /> Qwen Code</kbd></a> &nbsp;
  <a href="https://support.atlassian.com/rovo/docs/install-and-run-rovo-dev-cli-on-your-device/"><kbd><img src="https://www.google.com/s2/favicons?domain=atlassian.com&sz=64" alt="Rovo Dev logo" width="16" valign="middle" /> Rovo Dev</kbd></a> &nbsp;
  <kbd>+ any CLI agent</kbd>
</p>

---

## Install

### Desktop — macOS, Windows, Linux

- **[Download from onOrca.dev](https://onorca.dev/download)**
- Or grab a build directly: [macOS Apple Silicon](https://github.com/stablyai/orca/releases/latest/download/orca-macos-arm64.dmg) · [macOS Intel](https://github.com/stablyai/orca/releases/latest/download/orca-macos-x64.dmg) · [Windows (.exe)](https://github.com/stablyai/orca/releases/latest/download/orca-windows-setup.exe) · [Linux AppImage](https://github.com/stablyai/orca/releases/latest/download/orca-linux.AppImage) · [All builds](https://github.com/stablyai/orca/releases/latest)

_Or via a package manager:_

```bash
# macOS (Homebrew)
brew install --cask stablyai/orca/orca

# Arch Linux (AUR) — or stably-orca-git to build from source
yay -S stably-orca-bin
```

### Mobile Companion — iOS, Android

Pair with your desktop app to monitor and steer your agents from your phone.

- **iOS:** [Download on the App Store](https://apps.apple.com/us/app/orca-ide/id6766130217)
- **Android:** [Download APK](https://www.onorca.dev/download/android) · [Install guide](https://www.onorca.dev/docs/android-apk)

---

## Community &amp; Support

- **Discord:** Join the community on **[Discord](https://discord.gg/fzjDKHxv8Q)**.
- **Twitter / X:** Follow **[@orca_build](https://x.com/orca_build)** for updates and announcements.
- **WeChat:** Group 11 is full. Scan to join the Orca community WeChat group 12.

  <img src="docs/assets/wechat-qr-group12.jpg" alt="WeChat group 12 QR code for the Orca community" width="160" />

- **Feedback &amp; Ideas:** We ship fast. Missing something? [Request a new feature](https://github.com/stablyai/orca/issues).
- **Privacy:** See the [privacy &amp; telemetry docs](https://www.onorca.dev/docs/telemetry) for what anonymous usage data Orca collects and how to opt out.
- **Show Support:** [Star](https://github.com/stablyai/orca) this repo to follow along with our daily ships.

---

## Developing

Want to contribute or run locally? See our [CONTRIBUTING.md](.github/CONTRIBUTING.md) guide.

The relay that pairs the mobile app with a desktop host is also in this repository under
[`cloud/`](cloud/README.md), with a separate pnpm workspace and setup guide.

<a href="https://github.com/stablyai/orca/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=stablyai/orca" alt="Orca contributors" />
</a>

<p align="center">
  <img src="docs/assets/star-history.png" alt="GitHub star history chart for stablyai/orca" width="880" />
</p>

## Signed Builds

Windows code signing sponored/provided by [SignPath.io](https://signpath.io), certificate by [SignPath Foundation](https://signpath.org).

## License

Orca is free and open source under the [MIT License](LICENSE).

## Docs
### docs/ listing
```
file	STYLEGUIDE.md
file	agent-skill-sharing-implementation-checklist.md
dir	assets
dir	audits
file	automated-setup-tab-astra-review.md
file	automated-setup-tab-design.md
dir	bug-reproductions
file	native-chat-setup-provisioning-design.md
file	native-chat-setup-provisioning-review.md
dir	readme
dir	reference
dir	relay-region-correction
dir	site
```

### docs/STYLEGUIDE.md
```
# Orca UI Style Guide

This is the **UI/visual design** doc for Orca — color tokens, typography, component selection, and UX rules. It is _not_ an architecture doc; for system-level design see code and inline comments. Token values live in `src/renderer/src/assets/main.css` (canonical); this file documents the _roles and rules_ for using them.

## Overview

Orca is an Electron desktop app for orchestrating coding agents across git worktrees. The visual identity is **monochrome and quiet** — neutral grays carry the chrome, color is reserved for state (selection ring, destructive, git decorations). The product spends most of its time hosting other people's tools (Monaco, xterm, Markdown previews), so Orca's own UI should recede and frame.

When in doubt:

- Reach for **muted/accent/border** before reaching for color.
- Reach for **CSS variables** before hardcoding hex.
- Match the nearest **shadcn primitive** before writing custom CSS.

## Source of truth

| Concern                                       | Canonical location                                    |
| --------------------------------------------- | ----------------------------------------------------- |
| Color tokens                                  | `src/renderer/src/assets/main.css` (`:root`, `.dark`) |
| Tailwind theme bindings                       | Same file, `@theme inline { … }` block                |
| Component primitives                          | `src/renderer/src/components/ui/` (shadcn-style)      |
| App typography / scrollbars / titlebar chrome | Same `main.css`                                       |

Never hardcode a hex value in component code if a variable already covers it. If a new token is needed, add it to `main.css` (both `:root` and `.dark`), expose it in the `@theme inline` block, then use it.

## Color roles

Tokens come in pairs: a **surface** and a **foreground** that meets contrast on it. Always use them together.

| Role                                     | Use it for                                                  | Don't use it for                                    |
| ---------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| `background` / `foreground`              | App canvas, default text                                    | Cards, popovers, sidebar (have their own)           |
| `card` / `card-foreground`               | Panels lifted off the canvas                                | The canvas itself                                   |
| `popover` / `popover-foreground`         | Floating menus, dropdowns, hovercards                       | Inline UI                                           |
| `primary` / `primary-foreground`         | The single affirmative action in a flow (Save, Confirm)     | Decorative accents; hover states; secondary actions |
| `secondary` / `secondary-foreground`     | Lower-emphasis actions next to a primary                    | The affirmative action                              |
| `muted` / `muted-foreground`             | De-emphasized text, captions, placeholders, disabled chrome | Body copy; primary actions                          |
| `accent` / `accent-foreground`           | Hover/active backgrounds for ghost buttons and list rows    | Solid filled buttons (use `secondary` instead)      |
| `destructive` / `destructive-foreground` | Delete, discard, irreversible-action buttons; error states  | Cancel buttons (Cancel is not destructive)          |
| `border`                                 | All hairlines: dividers, input outlines, card edges         | Heavy emphasis; that's `ring`                       |
| `input`                                  | Form field background only                                  | Anywhere outside form fields                        |
| `ring`                                   | Focus-visible outlines, active selection halos              | Persistent decoration                               |
| `sidebar` (+ variants)                   | The worktree sidebar and its children                       | Other panels                                        |
| `editor-surface`                         | Background of Monaco / markdown editor panes                | App chrome                                          |

The `sidebar` family expands into `--sidebar`, `--sidebar-foreground`, `--sidebar-primary`, `--sidebar-primary-foreground`, `--sidebar-accent`, `--sidebar-accent-foreground`, `--sidebar-border`, and `--sidebar-ring` — use them inside the worktree sidebar so its hover/selected/focus states stay consistent and don't bleed into other panels. `editor-surface` is its own token (not just `background`) because Monaco and the markdown editor have a slightly darker surface in dark mode to match VS Code conventions; reach for it whenever you're rendering an editor pane.

### Git decoration colors

For diff status, file-tree decorations, and the changes view, use the git decoration tokens (mirroring VS Code's palette so users transferring from VS Code aren't surprised):

| Token                        | State          |
| ---------------------------- | -------------- |
| `--git-decoration-added`     | Added / new    |
| `--git-decoration-modified`  | Modified       |
| `--git-decoration-deleted`   | Deleted        |
| `--git-decoration-renamed`   | Renamed        |
| `--git-decoration-untracked` | Untracked      |
| `--git-decoration-copied`    | Copied         |
| `--git-decoration-ignored`   | Ignored by git |

Use these _only_ for git status. Don't reuse them for unrelated state colors — that breaks the convention.

### List rows: hover, selected, current

A common point of drift. Use these conventions for any list-style row (worktrees, command palette items, settings nav):

- **Idle:** transparent background.
- **Hover:** `bg-accent` (in the worktree sidebar, `bg-sidebar-accent`).
- **Keyboard-selected (cmdk highlight):** do **not** rely on flat `bg-accent` alone on light popover/dialog surfaces — `--accent` (#f5f5f5) is nearly identical to `--background` (#fff), so the cursor vanishes. Use the jump-palette recipe in `main.css` (`.jump-palette-item[data-selected='true']`): `color-mix` foreground into background (~12%) plus an inset ring. Expose the mix as `--jump-palette-selection-surface` when nested cutouts (status pips) must match. The `data-selected` attribute is set by `cmdk` automatically.
- **Persistent "current" / "active" row** (e.g. the worktree the user is viewing): also `bg-accent`, _plus_ a `data-current="true"` attribute so CSS or future styling can distinguish it from the cmdk highlight.
- **Don't:** hardcode `bg-[#ededed]` / `bg-[#333333]` or invent a "selected" color. Mix from existing tokens (`foreground`/`background`/`accent`) so light/dark stay aligned.

### Color mixing

When you need a tint (e.g. a 12% primary wash on hover), use `color-mix` against the existing token, not a new hex:

```css
background: color-mix(in srgb, var(--primary) 12%, var(--background));
```

This keeps light/dark parity automatic.

## Typography

- **Family:** `Geist` is loaded as a single variable woff2 (weight range 100–900). Always reach for `Geist` for sans, never `Inter` or system sans.
- **Mono:** `var(--font-mono)` — used for paths, terminal-adjacent UI, code, and anywhere monospace conveys "this is literal."
- **Body letter-spacing:** `0.01em` (set globally on `body`). Don't override per component.
- **Sizes:** Tailwind's default scale. Common sizes in this repo:
  - 11px (uppercase meta, sidebar headers, captions) — pair with `font-weight: 600` and `text-transform: uppercase` and `letter-spacing: 0.05em` for category labels.
  - 12px (sub-text, paths, secondary content)
  - 13px (sidebar items, dense list rows)
  - 14px (default body, button text in `default` size)
- **Named small steps:** `text-2xs` (11px) and `text-3xs` (10px) are theme steps in `main.css`. Use them instead of `text-[11px]` / `text-[10px]`.

### Chat type scale

The native chat uses four steps and no others. Never write an arbitrary size (`text-[13px]`) inside `components/native-chat/`. `pnpm lint` enforces this, along with the softened-foreground and focus-ring rules below (`config/oxlint-plugins/native-chat-design-tokens.mjs`).

| Step             | Default | Use it for                                                                                                 |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `text-sm`        | 14px    | Anything the user reads: message prose, tool and agent activity rows, card titles and bodies, the composer |
| `text-xs`        | 12px    | Labels, timestamps, counters, secondary lines under a row                                                  |
| `text-2xs`       | 11px    | Captions, attribution, uppercase category labels                                                           |
| `text-3xs`       | 10px    | Badges and mono pills                                                                                      |
| `text-chat-code` | 12px    | Code blocks, diffs, commands and tool output                                                               |

The chat root (`.native-chat-appearance`) redefines these steps as ratios of the Text size setting, so every tier scales together; `text-chat-code` follows the Code text size setting. The chat root also ties the spacing unit to the text size (4px at the default 14px), so icons, gaps, padding and row heights grow with the text. Use spacing-scale utilities (`size-3.5`, `min-h-6.5`, `pl-3.25`), not pixel lengths (`min-h-[26px]`), or the element stays fixed while the rest scales. Size an element with one of these utilities only: a CSS rule that sets `font-size` outside a layer silently overrides them.

### Chat text colour, hover and focus

- **Primary text on the chat canvas** uses `text-chat-foreground`, and `text-chat-foreground-strong` for titles and emphasis; both follow the Contrast setting. Don't soften `text-foreground` by hand (`text-foreground/85`). `text-foreground` is for text on a lifted surface inside the chat.
- **Secondary text on the chat canvas** (transcript rows, notices, labels between messages) uses `text-chat-foreground-faint`. `text-muted-foreground` is for text on a lifted surface inside the chat: cards, menus, popovers and the docks above the composer.
- **Row hover** in the transcript is `hover:bg-accent/20`. Buttons, menu items and card controls use `hover:bg-accent`.
- **Focus rings:** full-width transcript rows use the inset ring (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-ring`) so it isn't clipped by the scroll container; standalone controls use `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring`. Inside the chat `--ring` is `--chat-focus-ring`, which clears 3:1 on the canvas; don't lower its opacity.
- **State colours in the chat:** warnings use `text-chat-warning`; diff lines use `text-chat-diff-added` / `text-chat-diff-removed`; what the reader has not seen yet uses `text-chat-unread`. They are mixed toward the foreground so they pass text contrast in light and dark. Don't use raw palette colours (`text-yellow-500`) or the git decoration tokens for text on a tinted row.

## Radius

`--radius: 0.625rem` (10px) is the base; the rest are computed (`--radius-sm` = 0.6×, `--radius-md` = 0.8×, `--radius-lg` = 1×, `--radius-xl` = 1.4×, etc.). Buttons and inputs use `rounded-md`; the `Card` primitive uses `rounded-xl`; badges use `rounded-full`. Match the existing primitive's radius rather than introducing a new one.

## Elevation & shadows

Orca uses shadows sparingly. Three levels in practice:

1. **Inset hairline** — `border` + `border` token. The default. Almost everything sits at this level.
2. **Subtle lift** — `shadow-xs` + a single-token border. Outline buttons, embedded cards.
3. **Floating** — `shadow-floating` (`0 10px 24px rgba(0, 0, 0, 0.18)`). Popovers, popups that escape the editor surface. Reserved.

Don't add a fourth level. If something needs more emphasis than "floating," you're probably reaching for the focus `ring` instead.

## Components

Use the shadcn primitives in `src/renderer/src/components/ui/` before writing anything custom. The shadcn-style wrappers in this folder follow a consistent pattern:

- Most carry a `data-slot="<name>"` attribute on their root for CSS targeting — do not strip it. (The non-shadcn helpers in this folder — `sonner` and `repo-multi-combobox` — don't follow this pattern and shouldn't be modeled when adding new primitives that should.)
- Use `cn()` for class merging. Pass user `className` last so callers can override.
- Use `class-variance-authority` (CVA) for variants when there are multiple.

### Buttons (`button.tsx`)

Variants in priority order:

| Variant       | Use case                                                           |
| ------------- | ------------------------------------------------------------------ |
| `default`     | The single affirmative action in a flow.                           |
| `secondary`   | Lower-emphasis sibling next to a `default`.                        |
| `outline`     | Toolbar / standalone actions where a filled button feels heavy.    |
| `ghost`       | Icon buttons, list-row triggers, anywhere chrome should disappear. |
| `link`        | Inline text actions inside paragraphs.                             |
| `destructive` | Delete, discard, irreversible. Never for Cancel.                   |

Sizes: `default` (36px), `sm` (32px), `xs` (24px), `lg` (40px), plus `icon`, `icon-xs`, `icon-sm`, `icon-lg`. Match the size to the surrounding row height — don't drop a `default` button into a 28px toolbar.

### Other primitives in this repo

Browse `src/renderer/src/components/ui/` for the full list. Most wrap a Radix UI primitive — exceptions are `command` (wraps `cmdk`), `sonner` (wraps `sonner`), and the visual-only wrappers (`badge`, `button-group`, `card`, `input`) which apply tokens and Tailwind utilities directly. Never reimplement headless behavior; extend the existing wrapper.

Use `DialogContent surface="security"` for every dialog that asks the user to trust, approve, run or remove code, including plugin provenance and approval, so plugin themes cannot change the trust surface's tokens. Use its `scrollable` prop when the whole dialog scrolls. Wrap a trust decision outside a dialog, such as an agent approval card or a certificate override, in `SecuritySurface`.

### Picking the right primitive

When a control has multiple plausible primitives, use this fork:

| You want…                                                    | Reach for                                  | Don't use                             |
| ------------------------------------------------------------ | ------------------------------------------ | ------------------------------------- |
| Hover-only label on an icon-only button                      | `Tooltip`                                  | `HoverCard` (too heavy), title attr   |
| Hover preview of richer content (avatar + summary)           | `HoverCard`                                | `Tooltip` (no rich content)           |
| Click-revealed menu with actions                             | `DropdownMenu`                             | `Popover` with hand-rolled list       |
| Right-click contextual actions                               | `ContextMenu`                              | `DropdownMenu` (different invocation) |
| Click-revealed surface with arbitrary content (form, picker) | `Popover`                                  | `Dialog` (it traps focus and dims)    |
| Modal that demands a decision before you continue            | `Dialog`                                   | `Popover`, inline overlay             |
| Drawer / panel sliding in from an edge                       | `Sheet`                                    | `Dialog` centered                     |
| Single choice from a known list                              | `Select`                                   | Custom listbox                        |
| Single choice with search / fuzzy filtering                  | `Command` inside `Popover`                 | `Select` (no search)                  |
| Multi-select with search                                     | `repo-multi-combobox` (mirror its pattern) | Roll a new one                        |
| Transient confirmation ("Saved", "Copied")                   | `sonner` toast                             | `Dialog`, inline banner               |
| Persistent inline status ("3 errors")                        | inline text + `Badge`                      | toast (toasts disappear)              |

If you find yourself styling around a primitive (`<Popover>` to act like a `<Dialog>`, or vice versa), stop and reconsider — the focus-management semantics differ and a future contributor will be misled by the mismatch.

### Tooltips

Tooltips exist to _name_ a control whose meaning isn't obvious from its appearance. They are not the place to teach, persuade, or warn — anything users need to read while acting belongs in the visible UI.

- **Use a tooltip when:** an icon-only button or compact chip needs a label. Toolbar icons, badges with abbreviations, truncated paths.
- **Don't use a tooltip when:** the control already has a visible label, the content is interactive (links, buttons), or the message is critical (errors, blocking warnings — those go inline).
- **Mounting:** the global `<TooltipProvider delayDuration={400}>` lives at the App root. Don't nest a second `TooltipProvider` unless you need a different delay for a tightly-scoped surface.
- **Trigger pattern:** wrap the trigger element with `<TooltipTrigger asChild>` so the tooltip's accessibility props attach to the button (not a wrapper span). This is required for keyboard focus to surface the tooltip.
- **Placement:** default `side="top" sideOffset={4}` — match the toolbar pattern in `sidebar/SidebarToolbar.tsx`. Pick a different side only when the default would clip against the viewport.
- **Shortcut chips inside tooltips:** if the action has a keyboard shortcut, append `<ShortcutKeyCombo />` rather than baking the keys into the label string. The chips render correctly per platform; baked-in strings drift.

```tsx
<Tooltip>
  <TooltipTrigger asChild>
    <Button variant="ghost" size="icon-sm" onClick={openSettings}>
      <Settings />
    </Button>
  </TooltipTrigger>
  <TooltipContent side="top" sideOffset={4}>
    Settings
  </TooltipContent>
</Tooltip>
```

### Icons

Icons come from **`lucide-react`**. Don't import a second icon library.

- **Default size:** `size-4` (16px). `Button` auto-applies this to any `<svg>` it contains via `[&_svg:not([class*='size-'])]:size-4`, so most call sites don't need to set a size on the icon.
- **`size-3` / `size-3.5`:** for metadata, captions, and dense list rows where 16px is too loud.
- **`size-7`+:** for featured/empty-state hero icons only.
- **Stroke width:** lucide's default 2px. Don't override per-icon.
- **Color:** inherit from surrounding text — `text-muted-foreground` for secondary, `text-destructive` for destructive, etc. Don't apply a token to the SVG directly when the parent already carries the right color.
- **Spinner:** the canonical loading icon is `<Loader2 className="size-4 animate-spin" />`. For 3s+ multi-step work, prefer a label that names the stage ("Cloning…" → "Installing…") over an unlabeled spinner. See _UX rule 1_.

### Keyboard shortcut chips

Use **`<ShortcutKeyCombo />`** from `src/renderer/src/components/ShortcutKeyCombo.tsx`. It renders a consistent key-cap style and inserts a `+` separator on Windows/Linux (Mac shows adjacent glyphs, no separator). It does **not** transform key strings — the _caller_ picks the platform-appropriate labels and passes them in:

```tsx
const isMac = navigator.userAgent.includes('Mac')
const mod = isMac ? '⌘' : 'Ctrl'
const shift = isMac ? '⇧' : 'Shift'
<ShortcutKeyCombo keys={[mod, shift, 'N']} />
```

See `Landing.tsx` for the canonical pattern. Don't roll a one-off `<kbd>` — kbd chips drift in shape and color across the app fast if everyone styles their own.

**Where shortcuts surface in the UI:**

- **Tooltips on icon buttons** — append the chip after the label, trailing.
- **Dropdown / context-menu items** — use `<DropdownMenuShortcut>` (or its context-menu equivalent) for the right-aligned chip; don't position one yourself.
- **Never on Cancel, Dismiss, or `link`-variant inline actions** — see _UX rule 3_.

**The label MUST match the actual binding for the platform.** If the keyboard handler reads `metaKey` on Mac and `ctrlKey` elsewhere, the chip must show `⌘` on Mac and `Ctrl` elsewhere. Mismatched chips are worse than no chip.

### Form anatomy

The pattern in `src/renderer/src/components/settings/SettingsFormControls.tsx` is the house style for any label + control + helper text. Match it for new forms:

- **Outer stack:** `space-y-3` for full-section forms (`ThemePicker`); `space-y-2` for compact single-control fields (`ColorField`, `NumberField`). Pick by density, not preference.
- **Label group:** `space-y-1` containing `<Label>` and a description in `text-xs text-muted-foreground`.
- **Control:** the shadcn primitive (`<Input>`, `<Select>`, etc.). Errors surface via `aria-invalid`; the input primitive already maps that to a destructive ring — don't paint your own.
- **Trailing metadata:** `text-[11px] text-muted-foreground` below the control (e.g., "Current: 14px · Default: 13px"), not next to the label.

### Scrollbars

Three scrollbar classes are defined globally in `main.css`:

- **`.scrollbar-sleek`** — the default thin, neutral scrollbar for sidebars, lists, popovers. Pair with `.scrollbar-sleek-parent` on a hover-target ancestor if you want the thumb to fade in only on parent hover.
- **`.scrollbar-editor`** — slightly heavier, used inside Monaco-adjacent surfaces.
- **`.worktree-sidebar-scrollbar`** — no reserved gutter: paired with `overflow-y-auto`, the scrollbar (and its width) exists only while content actually overflows, so a short list stays flush with the fixed header controls and classic-scrollbar Windows shows no arrow buttons on empty lists. The thumb stays invisible until the parent (`.scrollbar-sleek-parent`) is hovered. Used only in the worktree sidebar.

Apply one of these to overflow containers; don't write a fourth style.

## UX rules

These are the rules a contributor will most often get wrong if they're working in isolation. They apply to every UI change.

**UI copy must not overclaim.** Never imply the app has taken an action, made a decision, or observed a fact unless the code has real state or result data to support it. Use neutral process language while work is pending, and reserve result verbs like "skipped", "protected", "found", "verified", or "deleted" for actual results.

### Screen UX review rubric

Use this rubric when reviewing any Orca IDE screen, screenshot, or prototype. A good review should name the highest-impact friction first, then give concrete changes the implementer can make.

#### Review output format

1. **Top fixes:** the 3 changes that would most improve the screen.
2. **Friction notes:** specific clutter, alignment, copy, focus, or flow issues, with the affected UI element named.
3. **Suggested changes:** exact changes to layout, hierarchy, controls, copy, empty/error states, and disclosure.
4. **Keyboard and speed check:** whether the primary workflow can be completed in 1-2 actions where appropriate, with good default focus and Enter/Esc behavior.
5. **Follow-up links or states:** missing external links, acquisition actions, or persistent errors the user needs to recover.

#### What to judge

- **Progressive disclosure:** keep high-frequency actions visible and prominent. Move low-frequency actions out of the common pointer path into menus, overflow controls, detail drawers, or advanced sections. Do not make menus so long that the user has to scan unrelated actions; group or split them when they grow.
- **Action hierarchy:** the primary action must be obvious through placement, size, and `default` button styling. Put high-frequency actions at the top of menus and in the most reachable toolbar positions. Secondary and rare actions should not compete with the primary action.
- **Click count:** remove unnecessary intermediate steps. Common workflows should complete in 1-2 actions when the app already has enough information to proceed.
- **Default focus:** dialogs, popovers, and command surfaces should focus the field or primary action the user is most likely to use. If Enter submits, focus must land where Enter triggers the intended primary action. Esc should back out without adding visual noise to Cancel/Dismiss.
- **Keyboard navigation:** prefer searchable command surfaces for long option lists. Add search fields when users need to find repositories, branches, worktrees, agents, commands, settings, files, or providers from a list.
- **Shortcut labels:** show shortcut chips only for shortcuts that are actually implemented and useful at that location. Labels must match the platform binding. If a shortcut strategy is undecided, do not expose a placeholder label in product UI.
- **Alignment:** rows and columns must line up to a visible grid. Left-align text and labels for scanability; right-align numbers, counts, shortcuts, and trailing metadata when comparison matters; center-align only compact icon controls, empty states, and table cells where symmetry is the clearest read.
- **Copy quality:** displayed text must be typo-free, concise, and specific. Prefer direct verbs and concrete nouns. Remove filler like "please", "simply", "just", "you can", and generic success language that is not backed by state.
- **Dialogs and overlays:** choose a dialog size that matches the amount of input. Short confirmations stay compact; forms with multi-line text, path pickers, provider setup, or review content need a larger dialog or sheet. Floating surfaces must use the documented shadow/elevation and background treatment so they read as above the page.
- **Empty and error states:** when data is missing, show a direct action to acquire or configure that data. Use toasts for transient failures or confirmations; persist errors inline when the user needs to read, retry, copy, or act on the message.
- **External links:** add direct links when the user may need provider docs, token settings, billing/setup pages, Git provider resources, or troubleshooting context. Put links near the relevant empty state, error, helper text, or setup step instead of burying them in a generic menu.
- **Affordance:** users should be able to discover available features without intrusive education. Use familiar icons, visible hover/focus states, clear labels where needed, and tooltips for icon-only controls. Prefer simple lucide icons already used nearby over obscure alternatives.
- **Layout density:** avoid jamming controls together. Preserve breathing room around the primary workflow, reduce competing buttons, and keep toolbar groups visually distinct. Dense screens are acceptable only when grouping, alignment, and hierarchy make scanning faster.
- **Cards and containers:** cards must be visually distinct from their parent surface through the existing `card`/`border` treatment. Avoid nesting cards inside cards. If a section is not a repeated item, modal, or framed tool, consider an unframed layout or full-width band instead.
- **Side-by-side layouts:** default to row-by-row layouts for complex workflows because they are easier to align and scan. Use side-by-side layouts only when space is constrained or comparison is the point, then polish column widths, baselines, and wrapping states carefully.
- **Animation:** use subtle animation to soften expanding/collapsing content and prevent jumpy layout changes. Animation should clarify continuity, not decorate. Respect reduced motion element by element: turn movement off with `motion-reduce:` (slides, rotations, size changes); give spinners, pulses and progress indicators a still state that still says "working" (`LoadingSpinner` does this for spinners) instead of freezing them; short opacity fades can stay. Scripted scrolls ignore CSS, so pass them through `motionSafeScrollBehavior()`.
- **SSH and latency:** assume actions may run remotely. Disable submit controls immediately, delay visible loading feedback when appropriate, and keep focus stable while remote data arrives.

### 1. Match in-flight feedback to perceived duration

The right question isn't _"should this control change while it's working?"_ — it's _"how long does the action take, and what does the user need to know during that time?"_

| Duration           | Feedback                                      |
| ------------------ | --------------------------------------------- |
| 0–100 ms           | None. Anything visible reads as a glitch.     |
| 100 ms–1 s         | Disabled state only.                          |
| 1 s–3 s            | Disabled + spinner or label swap.             |
| 3 s+ or multi-step | Stage labels, progress, optional reassurance. |

Two corollaries:

- **Pre-reserve any space you'll later occupy.** If a control may swap to a longer label or grow an icon, fix its footprint up front (use `width`, not `min-width`). A control that resizes mid-action looks broken even when the action succeeded.
- **Don't pick worst-case feedback for everyone.** If the action is fast locally and slow remotely (SSH), defer the visible loading state by ~200ms. Local users see nothing; remote users get appropriate feedback. Bind the _disabled_ state immediately (so double-clicks don't double-submit) and the _visible_ state on a timer.

### 2. Look for sibling components before designing in isolation

If your component has a sibling — same domain, overlapping behavior, often visible at adjacent moments in the same flow — the two should read as one design. Same icons, same shortcut conventions, same submit semantics. A user moving between them shouldn't perceive a seam.

This is _not_ "match every existing pattern." Some repo patterns are debt and copying them spreads the debt. The narrower claim is about _adjacent_ components. Diverging from a sibling needs a reason: either the sibling is wrong (fix both) or the new component has a real difference in role (commit to it).

When there's no sibling, match the surrounding chrome — button sizes, icon weights, copy tone — and don't manufacture a sibling from a screen the user will never correlate with this one.

### 3. Don't overload the back-out path

`destructive` is for actions that lose data or can't be undone. **Cancel, Dismiss, Close, and Discard are not destructive** — they back the user out of an in-progress action and should stay quiet (default ghost button, no color, no keyboard chip, no animated affordance). Save the visual weight for the affirmative action so the two don't compete. Keyboard handlers can still honor Esc; the visible decoration is what stays minimal.

## Cross-platform

Orca runs on macOS, Linux, and Windows. Every UI change must hold up on all three, in both light and dark mode.

- **Modifier keys:** Never hardcode `e.metaKey`. Use `navigator.userAgent.includes('Mac')` to choose `metaKey` on Mac and `ctrlKey` on Linux/Windows. Electron menu accelerators should use `CmdOrCtrl`.
- **Shortcut labels:** Display `⌘` / `⇧` on Mac; display `Ctrl+` / `Shift+` on other platforms. The label must reflect the actual binding for that platform.
- **Window chrome:** macOS shows traffic lights; the titlebar reserves an 80px gutter (`titlebar-traffic-light-pad`) so they don't overlap content. Don't put hit targets in that band on Mac.
- **SSH:** Many users run Orca on a remote machine. Loading states, focus management, and animations must hold up under 50–200 ms of extra latency. Test under simulated latency (or actual SSH) — local-only verification isn't enough. See _UX rules → 1_.

## When this guide is silent

If you have a UI question this doc doesn't answer:

1. Look at adjacent code in `src/renderer/src/components/` for the closest sibling, and follow its lead.
2. Check `src/renderer/src/components/ui/` for a primitive that already encodes the pattern.
3. If it's a token question, `main.css` is canonical — use what's there, or add a new one in both light and dark.
4. If none of those resolve it, ask the user before inventing.
```

### docs/agent-skill-sharing-implementation-checklist.md
```
# Agent skill sharing implementation checklist

Status: implementation and validation in progress.

Last updated: 2026-08-12.

Implementation baselines captured by this checklist update:

- Orca implementation: `skills-share` through `607e31dd04`; no PR.
- Orca Cloud: bundle smoke PR `#329` merged as `eddb144afe`; generation-aware recovery PR `#330`
  merged as `8045c85dad`; encrypted physical-host credential PR `#336` merged as `8fce3298ef`;
  kill-switch discovery PR `#342` merged as `c2bef2ff20fb`.
  Windows device-name validation PR `#343` merged as `dbb14a658cbc`; explicit disabled production
  bootstrap PR `#352` merged as `2a23f6ace5`; publisher-identity omission PR `#355` merged as
  `b3213bd34d1b224d8a3b11527eceaac883965400`; production enablement PR `#357`, bounded OIDC smoke
  PR `#358`, monitor IAM PR `#359`, and monitor release-ownership PRs `#360`/`#361` are merged
  through `d8605edde72229c5d00d22c8bd6853a13c1a4aaa`.

Validated so far:

- Current release hardening cancels bundle extraction after partial bytes exist and removes the
  extraction directory, durable journal, and managed-install state. Four repeated focused runs and
  the real SIGKILL recovery test passed. Signed GCS uploads use the earlier of signed-policy expiry
  and a 15-minute cap, including their archive read stream, so slow valid uploads can finish while
  stalled uploads remain bounded.
- Local and headless managed-skill operations now wait for the one startup transaction-recovery
  promise before reading or changing install state. Codex uses its documented global
  `~/.agents/skills` root, and provider removal derives allowed roots from the registry so aliases
  remain removable after an agent is no longer detected. The combined focused suite passed 74
  tests across 12 files, including fake-timer slow-upload and controlled-recovery regressions.
- The reported desktop install failure was a strict main-process IPC schema rejecting the
  renderer's additive `providers` selection before bundle verification. All four install schemas
  now accept the bounded field, and focused schema/provider tests pass. The original production
  link resolves as a valid one-skill bundle and returns a fresh same-version local download grant;
  the signed URL and private metadata were not logged or printed during verification.
- The final reliability hardening at `607e31dd04` adds a 60-second Cloud request deadline;
  cancellable, journaled bundle extraction; bounded package creation, verification, and preview
  fanout; atomic share-preparation admission and abandoned-archive cleanup; process-owned download
  staging; SSH startup recovery; and additive paired-client cancellation-result negotiation. The
  focused suite passed 78 ordinary tests plus a real process-death recovery test. Full Node, CLI,
  and web typechecks, repository lint and reliability gates, changed-file formatting, and diff
  checks passed. Mobile-facing wire changes remain additive, and no mobile app surface changed.
- A final performance and React lifecycle review found one stale-response race in managed-install
  inventory: a slower previous machine could overwrite the newly selected machine's list. The
  generation fence and regression test now preserve destination ownership; bundle busy state also
  reaches the parent close guard in the initiating event instead of a mirror effect. The complete
  renderer skill/settings slice passed 122 tests across 18 files, all Node/CLI/web typechecks,
  focused Oxlint, changed-code quality, max-lines, diff, and localization gates.
- The final local readiness pass at `9fcd72e327` passed 489 skill-domain tests across 73 files
  with 11 intentional platform skips, all Node/CLI/web typechecks, localization catalog,
  extraction and coverage, max-lines, changed-code quality, React Doctor, formatting, and diff
  checks. No new P0, P1, or P2 finding was proven by the crash/retry, security, performance,
  functional, mobile-backcompat, or Windows/Linux review.
- Multi-select sharing now preserves hidden selections, reconciles changed discovery scans,
  visibly explains ineligible skills, and blocks duplicate names before review. Exact complete
  managed bundles publish a new immutable version to their existing package; ambiguous or partial
  selections safely create a new package. Managed bundles with an active link can reopen the
  destination-aware installer for another machine; the final renderer slice passed 114 tests.
- The mobile/backcompat review found no persisted mobile keys, routes, deep links, or required
  legacy fields changed. Skill RPC methods and capabilities are additive and capability-gated;
  the cross-platform review found production paths use host path APIs and platform checks, with
  POSIX-only literals confined to tests or WSL guest execution.
- Final bearer-link changes pass 143 Orca Cloud API tests with one opt-in skip; 58 focused Orca
  tests; four mixed-version wire tests; desktop/node/web typecheck; localization catalog,
  extraction, and coverage; changed-code quality; max-lines; and diff checks.
- The final Cloud change passed PR run `31564069382` and merged-`main` run `31564235724`, including
  the full monorepo build, lint, typecheck, tests, Terraform format, and Terraform validation.
- The opt-in desktop staging harness now publishes a bearer share without retired audience fields;
  Node typecheck and Playwright test discovery pass without starting Orca or a browser login flow.
- Local Node and web typechecks, changed-code quality gates, 94 skill-domain files with 770 tests
  passed and 3 skipped, 134 Orca Cloud API tests with one opt-in integration skip, the full Cloud
  monorepo test/typecheck/lint/build gates, and isolated Terraform formatting and validation.
- Final Orca validation passed repository-wide lint, all Node/CLI/web typechecks, the production
  desktop/native build, the Node 18 Relay bundle contract, 78 focused skill files with 557 tests
  passed and 10 platform skips, and the mixed-version wire suite. The full repository run passed
  49,977 tests with 112 skips; its three environment/timeout failures passed as a 124-test rerun
  after removing Orca-injected Git config variables and rerunning the slow macOS PTY case.
- Skill sharing and installation renderer copy now passes the localization catalog, extraction,
  and coverage gates without a max-lines exception.
- Remote upload sessions actively expire abandoned bytes after their bounded idle lifetime, and
  begin/chunk/commit retries resume from the host-acknowledged offset under one stable transfer ID.
- Paired skill install and upload cancellation now reaches queued calls, capability probes,
  one-shot sockets, cached request sockets, and shared-control requests instead of waiting for the
  five-minute transfer timeout. Focused coverage proves queued work never starts, pending request
  admission is released, late responses are ignored, one-shot sockets close, and unrelated cached
  or shared-control requests survive; 84 transport/service tests and Node typecheck passed.
- Standalone and bundled package names reject Windows reserved device names in both Orca and Cloud,
  preventing a package published on macOS/Linux from failing only when installed on Windows.
- Identical archives are deduplicated only within an owner tenant. PostgreSQL object identity and
  tenant-hashed GCS keys prevent cross-tenant existence or finalization-timing disclosure.
- Native Windows package/install/recovery/copy-fallback tests and Node typecheck on `windows 2`;
  the current slice passed 284 tests with 21 intentional platform skips across 43 files.
- The final combined physical `windows 2` run at `44d1266641` enabled native-Windows, real-process,
  and Ubuntu 24.04 WSL coverage together: 67 files passed, 449 tests passed, and 17 intentional
  platform skips remained. Commit `97b831dd17` made Windows recovery assertions path-semantic and
  time-deterministic. Commit `44d1266641` fixed WSL alias reconciliation after proving native UNC
  `lstat` can miss an existing distro symlink; WSL now inspects the alias in-distro and creates new
  aliases with `ln -sT`. The checkout remained clean and no `orca-skill-*` directory remained in
  WSL `/tmp`.
- Native Windows transaction validation passed all 21 cases at `6d3ce582aa`, including a real
  canonical install beyond `MAX_PATH` while the host's `LongPathsEnabled` policy remained disabled.
- Real Ubuntu 24.04 WSL global, guest-workspace, and `/mnt/c` workspace transactions, including
  alias placement, interrupted update recovery, conflict preservation, update, and removal.
- Real Ubuntu 24.04 WSL provider detection and POSIX semantics, including case-sensitive names,
  `0600` regular files, and `0700` executable files.
- Exact portable package digest and archive SHA-256 goldens passed on macOS and native Windows
  despite different bundled zlib versions (`1.2.12` and `1.3.1`).
- The focused deterministic package suite passed 26/26 tests in Debian Bullseye/glibc 2.31 on
  native Linux ARM64 and emulated Linux x64, plus the real Ubuntu 24.04 WSL distro on `windows 2`;
  every host produced the same package digest and archive SHA-256 golden.
- The same 26/26 portable package suite passed at `109272dab1` on a disposable native x86_64
  Ubuntu 22.04 GCE host using Linux 6.8 and Node 24.18. The VM had no service account or scopes;
  its boot disk, uploaded Git bundle, and temporary project SSH metadata were removed afterward.
- The exact x64 Electron directory package at `f1dccb4f42` passed its after-pack ABI scan for all
  18 bundled native binaries, then loaded packaged `node-pty` and spawned `/bin/sh` inside an
  Ubuntu 20.04/glibc 2.31 container. The physical run corrected the gate to use Linux's actual
  `orca-ide` executable and `resources/node_modules` layout. A native ARM64 package built from
  exact commit `abe92d565b` on an isolated `aarch64` GCE host then passed the same 18-binary
  Ubuntu 20.04/glibc 2.31 ABI gate and packaged `node-pty` load/spawn smoke. The ARM64 VM had no
  service account or scopes; its auto-delete boot disk was verified absent, and its local Git
  bundle was moved to Trash after the clean-checkout proof.
- Real native Windows global, linked Git-worktree, and plain folder installs with spaces and
  non-ASCII paths, plus privacy-safe install diagnostics and owner-private staging tests.
- Docker-backed SSH relay installation from the real Electron client passed global, remote Git
  worktree, and remote plain-folder scopes, including client-mediated upload, unchanged preview,
  managed-install listing, safe removal, and remote-target Cloud authorization.
- Real paired-runtime installation passed from an isolated Electron client to both a headed
  desktop host and headless `orca serve` host. The host owned global and Git-worktree installs;
  the headed host also owned a plain-folder install. The client's home remained untouched.
- A fresh post-resilience E2E run passed all three headed paired-runtime, headless `orca serve`,
  and Docker SSH journeys. Focused failure injection also proves invalid gzip classification,
  old-version preservation after `EACCES` and `ENOSPC`, bounded recovery from a lost final install
  response, and validated structured SSH failure data without arbitrary error-data disclosure.
- Isolated staging bucket, IAM, `orca_skills` database and principal, enabled secret version, 11
  log metrics, four alerts, and one dashboard in `onorca-cloud-staging`. The complete targeted
  skill-infrastructure plan is zero-diff at Cloud `41ef335`.
- PostgreSQL migration startup is serialized by a transaction-scoped advisory lock. Transactional
  DDL rollback and eight concurrent startup callers passed against ephemeral PostgreSQL 16 and 17,
  with exactly one recorded schema version.
- Cloud PR `#349` merged as `6a812c5e11` after proving an older API migration runner preserves a
  newer additive column/table and continues using its existing SQL. Build, lint, typecheck, tests,
  Terraform initialization, and validation passed; no service or infrastructure was deployed.
- Cloud PR `#350` merged as `c22007384a` and added a required disposable PostgreSQL 16/17 drill.
  Real old and future-additive Node processes coexist and write against one database, the database
  is dumped and restored, and both processes write again after restoration. PR run `31624484826`
  and merged-main run `31624717796` passed every code, Terraform, and database job; no staging or
  production resource was accessed or deployed.
- The immutable API deploy path stamps every artifact and skill literal variable plus exactly one
  approved skill-database secret, and rejects secret, Cloud SQL, service-account, scaling, CPU,
  memory, volume, mount, probe, or unexpected-environment drift before traffic promotion.
  Staging intentionally carries all four skill controls as `true`; production remains `false`.
- The route-disabled baseline, API revision `orca-cloud-api-staging-00039-rek`, first proved the
  database-ready startup and anonymous `401`/`404` boundaries with zero revision errors.
- Cloud PR `#313` passed run `31533988351`, merged as `d0bf926`, and passed `main` run
  `31534229437`. Guarded wake run `31534564230` restored exactly the two configured Relay cells.
- Auth deploy run `31535179937` promoted revision `orca-cloud-auth-staging-00017-dug` at 100%
  traffic. Health, JWKS, exact GitHub OIDC claim constraints, and zero deployment-window errors
  passed.
- The historical ACL-era API deploy run `31535438327` promoted revision
  `orca-cloud-api-staging-00042-hef` at 100%
  traffic with `authenticatedSmoke: true` and `skillSmoke: true`. The smoke covered artifact
  lifecycle; skill upload/finalize/download; two immutable versions; recipient and outsider
  authorization; local and remote grants; rollback selection; expiry; revocation; package
  deletion; and signed-object cleanup.
- Cloud PR `#317` passed both required checks and merged as `be00db10`. Its historical ACL-era
  deploy run `31546194596`
  promoted revision `orca-cloud-api-staging-00048-xom` at 100% traffic with
  `authenticatedSmoke: true` and `skillSmoke: true`; canonical health and the immutable image
  digest independently matched after promotion.
- The signed-in macOS desktop staging journey reached upload, finalize, durable share creation,
  and global install after replacing an invalid colon in the audience-derived idempotency key.
  The retry test now requires a stable path-safe key, and the live test records the package ID
  before publication so a failed share can still clean up its finalized package. Its update phase
  uncovered same-name discovery ambiguity; the harness now selects the exact workspace source
  directory instead of the first same-named global skill. A final full live rerun remains open.
- The serving API has all four controls `true`, zero revision errors, and privacy-safe structured
  request logs. The log field inventory contains no principals, credentials, signed URLs, object
  paths, or private contents; a sensitive-value scan returned zero matches.
- Cloud PR `#314` removed deploy-owned Auth release metadata from Terraform ownership, passed run
  `31536141357`, merged as `4e91cf9`, and passed `main` run `31536329459`. The targeted Auth/API
  plan then reported zero intended changes. Known SQL and artifact-bucket drift was excluded and
  never applied.
- Cloud PR `#320` passed both required checks and merged as `0579cc1a71`. Targeted Terraform added
  only `google_logging_project_exclusion.skill_share_bearer_request_urls` in staging: one addition,
  zero changes, and zero deletions. This prevents per-link Cloud Run request URLs from entering
  log storage while retaining route-template application telemetry.
- Guarded wake run `31564370807` prepared the reviewed staging topology. Deploy run `31564803943`
  promoted `orca-cloud-api-staging-00051-yoq` at 100% traffic with immutable image digest
  `sha256:511c0196511d2079bd9138092ad3cf065304b46a089b02d8df9318e0ae2e656a` and reported
  `authenticatedSmoke: true` and `skillSmoke: true`.
- Candidate and canonical smoke produced 60 privacy-safe route-template events covering owner
  upload/finalize/share creation/inventory/revocation and anonymous pinned/latest preview,
  local/remote download grants, version selection, expiry, uniform unavailable responses,
  package deletion, and object cleanup. Anonymous requests with no Authorization header and an
  invalid header both returned the same `404 skill_share_not_found` response with `no-store`.
  The serving revision had zero error logs and Cloud Logging retained zero per-link platform
  request logs.
- Guarded sleep run `31546908228` stopped all three Relay cells after the physical staging work.
  Independent GCP reads verified Cloud SQL policy `NEVER`, every MIG target at zero, and both
  managed Cloud Run minimums at zero.
- Final guarded sleep run `31565009141` restored the same low-cost state after the bearer rollout;
  independent reads found Cloud SQL `NEVER`/`STOPPED` and C1, C2, and C3 at target size zero.
- Cloud PR `#329` passed required checks, merged as `eddb144afe`, and passed merged-main run
  `31569732482`. Browser-free desktop run `31569902499` then passed bundle publish v1, install,
  local modification preservation, v2 update, rollback, revoke, installed-copy preservation, local
  removal, and Cloud package deletion without opening a login page.
- Cloud PR `#330` passed required run `31578720429`, merged as `8045c85dad`, and passed merged-main
  run `31578942857`. Guarded wake `31579195133` brought SQL and all three Terraform-owned cells up;
  deploy `31579844413` promoted `orca-cloud-api-staging-00057-kat` at 100% traffic with immutable
  digest `sha256:f61745b21d00b111087620ab1108c9a96e9863ec9e902a424aaad01e9e945605`.
- Recovery smoke `31580071168` published an isolated bundle, soft-deleted the exact published GCS
  generation, restored it with `ifGenerationMatch=0`, verified immutable metadata, transactionally
  repointed every matching database reference, verified the unlisted bearer download, and deleted
  the probe. No ephemeral recovery job or live probe object remained.
- Guarded sleep `31580339694` returned staging to low cost. Independent reads verified Cloud SQL
  `NEVER`/`STOPPED`, C1/C2/C3 target size zero and stable, and API/Auth min scale zero. Production
  was not touched.
- Cloud PRs `#332` through `#335` added the staging-only 12-by-30 finalization load gate, narrowly
  authorized its OIDC identity, fixed deterministic fixture ordering, and made retry settlement
  cleanup-safe. Their merge commits were `ac85d0690e`, `53559bd644`, `7e1d50a84b`, and
  `bb8bf8b9ac`; merged-main verification passed through run `31586525326`.
- Auth deploy `31584318896` promoted `orca-cloud-auth-staging-00021-tuq` with digest
  `sha256:e17075d69dca36df427f02fa515481f359c8f67397c5ab16de9759f7f949c6be`; candidate and
  canonical smoke passed with one 100%-traffic revision and no remaining candidate tag.
- Load run `31585710645` exercised 12 concurrent bundles with 30 skills and 3,949,317 extracted
  bytes each. Two finalized immediately and ten returned explicit saturation; client p95 was
  1,514 ms. Aggregate utilization stayed bounded: request p95 1,401.06 ms, API CPU 8.95%, API
  memory 26.95%, one API instance, database CPU 10.89%, database memory 25.59%, and seven
  connections. A saved, exact one-add Terraform plan restored the declared
  `roles/monitoring.viewer` binding for the staging deploy identity before those aggregate metrics
  were read; it changed no service, traffic, SQL, storage, Relay, or production resource.
- Cleanup run `31586684354` removed the exact failed-wave package set through normal package DELETE
  routes. The two remaining quarantine archives were manifest-proven as 30-skill fixtures for
  suffix `013756ec4740` and deleted with exact GCS generation preconditions; no live object from
  that run window remained. GCS soft delete keeps the operation recoverable.
- Guarded sleep `31587083752` returned staging to low cost. Independent reads verified Cloud SQL
  `NEVER`/`STOPPED`, C1/C2/C3 target size zero and stable with no current actions, and API, Auth,
  and Relay active-revision minimums at zero. Production was not touched.
- Cloud PR `#336` added a browser-free physical-host credential handoff restricted to the exact
  `main`-branch staging workflow identity. It encrypts only the ten-minute owner token to a
  one-time RSA-3072 key, grants no GCP permissions, retains ciphertext for at most one day, and
  passed PR run `31588982191` plus merged-main run `31589194501` as merge `8fce3298ef`.
- Guarded wake `31589384191` restored SQL and the two configured Relay cells without waking C3.
  Auth deploy `31589963244` promoted `orca-cloud-auth-staging-00025-zuz` at 100% traffic with
  immutable digest `sha256:2b5cb04060a871f372298786dbed681054a076f5cf75966ea5e2130403db7254`.
- The physical `windows 2` staging journey passed in 27.6 seconds using credential run
  `31591275227`. It installed v1 into the Windows-owned global path with the published digest and
  no macOS fallback, updated only that host to v2, preserved independent local version selection,
  rolled Windows back to v1, proved revocation left its installed copy intact, removed both host
  and local installs, and deleted the Cloud package. The encrypted artifact and local one-time key
  material were deleted immediately after use.
- The staging skill bucket independently reports the exact age-one-day Delete lifecycle restricted
  to `uploads/`, seven-day soft deletion, uniform bucket access, and public-access prevention. Its
  oldest live quarantine object was created at `2026-08-11T22:49:34Z`, so lifecycle execution—not
  configuration—is still time-gated.
- Guarded sleep `31592709817` completed at Cloud `8fce3298ef`. Independent reads verified SQL
  `NEVER`/`STOPPED`, all three Relay MIGs stable at target zero with no active actions, and API,
  Auth, and Relay active-service minimums at zero.
- Real process-death recovery now kills the transaction process after partial extraction and
  immediately before and after every durable install/removal journal transition. All 17 macOS
  cases passed, including extraction cleanup, dead-lock reclamation, receipt/filesystem agreement,
  and absence of transaction debris; the release workflow requires the same suite on macOS,
  native Windows, and Ubuntu 20.04/glibc 2.31.
- Guarded wake `31603249983` restored only the two configured staging cells. A disposable
  no-service-account Ubuntu 20.04/glibc 2.31 VM then passed the browser-free SSH staging lifecycle
  in 31.3 seconds: publish v1, host-owned install with exact digest, v2 update, managed-install
  verification, rollback, revocation with installed-copy preservation, local removal, and Cloud
  package deletion. The remote install, Orca SSH target, encrypted credential artifact, one-time
  keys, and VM were removed. Guarded sleep `31604391897` passed; independent reads verified SQL
  `NEVER`/`STOPPED` and C1/C2/C3 target zero, stable, and reached. Production was untouched.
- Guarded wake `31634214856` restored the two configured cells at Cloud `dfb8359ff5`. An isolated
  native `Darwin arm64` OpenSSH target with a separate temporary home then passed the full staging
  lifecycle in 20.1 seconds: publish v1, SSH-owned install, v2 update, managed-version checks,
  rollback, revocation with installed-copy preservation, removal, and Cloud package deletion.
  This corrected the staging oracle to accept absolute POSIX homes outside `/home`. The GitHub
  ciphertext artifact was deleted immediately; the SSH service, relay, install, temporary home,
  and one-time keys were removed. Guarded sleep `31635145830` passed; independent reads verified
  SQL `NEVER`/`STOPPED`, all three MIGs stable and reached at zero with no active actions, and
  API/Auth/Relay minimum scale zero. Production was untouched.
- Guarded wake `31605729090` restored the same configured topology. An isolated headless Orca host
  with a separate home/profile then passed the full paired-runtime staging lifecycle in 12.5
  seconds, proving host-owned install, update, managed-install state, rollback, revocation
  preservation, removal, and Cloud deletion without local fallback. The paired environment,
  install, package, encrypted credential artifact, and one-time keys were removed. Guarded sleep
  `31606600532` passed; independent reads again verified SQL `NEVER`/`STOPPED` and all MIGs at
  stable, reached target zero.
- Guarded wake retry `31630802215` succeeded at Cloud `dfb8359ff5`; the additional physical WSL
  Cloud journey was then waived as duplicate release evidence. The first guarded sleep attempt
  `31631288043` failed closed during Terraform provider initialization on a transient upstream
  `503`, before the mutation step. Retry `31631379891` succeeded. Independent reads verified SQL
  `NEVER`/`STOPPED`, all three MIGs stable and reached at target zero with no active actions, and
  the API, Auth, and Relay active-revision minimums at zero. Production was untouched.
- Cloud PR `#355` removed internal publisher and organization identifiers from anonymous skill
  responses, passed every code, Terraform, and PostgreSQL 16/17 check, and merged as
  `b3213bd34d1b224d8a3b11527eceaac883965400`. Guarded wake `31639920301` prepared staging. Deploy
  `31640677572` promoted `orca-cloud-api-staging-00060-qay` at 100% traffic with immutable digest
  `sha256:31cb0a91a7abf1f82e4de08bd31e98fbd71519adc731a005fc95f60480658f73`; authenticated and skill
  candidate/canonical smoke passed. The unrelated post-promotion storage-monitor image update
  lacked `iam.serviceAccounts.actAs`; the unchanged prior monitor image remains serving, and the
  API promotion and verification completed successfully. Guarded sleep `31640935616` passed in
  8m51s. Independent reads verified SQL `NEVER`/`STOPPED`, C1/C2/C3 stable and reached at target
  zero, and the API at minimum scale zero with revision `00060-qay` retaining 100% traffic.
  Production was untouched.

Rollout gate: staging infrastructure, OIDC owner identity exchange, anonymous bearer lifecycle,
owner management, browser-free desktop bundle lifecycle, privacy-safe logging, published-object
recovery, bounded finalization load, and guarded rollback-capable deployment passed. Production
infrastructure and the unlisted-link API are live with all four controls enabled after successful
authenticated candidate and canonical lifecycle smoke. Native Windows, real Ubuntu 24.04 WSL
filesystems, physical Ubuntu 20.04 and
macOS ARM64 SSH, and paired non-Windows staging passed. On 2026-08-12, the owner accepted the
remaining live WSL-to-staging journey as duplicate evidence after the combined 449-test physical
Windows/WSL run and native-Windows staging lifecycle; this does not treat WSL semantics as
identical to macOS. The user-driven signed-in desktop and real-host production journey, supported
Windows SSH, and the quarantine lifecycle deletion remain. The shared staging data plane is asleep.

This checklist turns the architecture plan into ordered implementation and release work. A checked
item means evidence exists in code, tests, reviewed infrastructure, or release documentation; it
does not mean the surrounding phase is complete.

## Definition of done

- [x] A user can select one or many private local skills, publish one immutable Skill Bundle, and
      receive one durable Orca share URL.
- [x] Anyone with an active unlisted link can inspect a bundle without signing in, choose all or a
      subset of its skills, and install them globally or into a Git worktree or plain folder
      workspace.
- [x] Installation works on local macOS, Linux, native Windows, WSL, paired Orca runtimes, and
      supported SSH targets.
- [x] The portable archive root conforms to Agent Plugins 1.0.0 for skills-only packages and keeps
      Orca integrity metadata in `dev.orca.skill-sharing/manifest.json`.
- [x] One canonical `.agents/skills/<skill-name>` copy is installed for each selected skill;
      provider-specific placements are reconciled for explicitly selected agents, defaulting to
      detected agents when no selection is supplied.
- [x] Install, update, rollback, and removal preserve modified or unowned local content unless the
      user explicitly approves replacement.
- [x] Package ingestion rejects unsafe archives before any destination mutation.
- [x] Interrupted operations recover to a complete previous or requested version.
- [x] Private package bytes remain access-controlled, published versions persist until deletion,
      and incomplete uploads expire automatically.
- [x] Mixed-version clients and remote hosts fail safely through capability negotiation.
- [x] Cloud resources are Terraform-owned, monitored, recoverable, and protected by independent
      upload, download, and remote-install kill switches. Targeted Terraform is zero-diff; staged
      generation recovery passed; dashboards, alerts, and runbooks cover the data plane; and Cloud
      PR `#342` proves all three mutation controls can be disabled independently while unlisted
      preview remains available.
- [x] The existing Skills page supports multi-select sharing, selective installation, per-skill
      conflicts/results, and installed-bundle management; Settings → Share Skills provides the
      authenticated owner inventory for copying and revoking active links.

## 0. Confirm scope and ownership

### Product and legal decisions

- [x] Record `vercel-labs/skills` as a behavioral reference only.
- [x] Record upstream baseline commit `c6f69c631292444cc541ac6d91e2226b0ff247da`.
- [x] Decide not to copy upstream source, tests, fixtures, registry data, or path tables.
- [x] Decide Orca will not depend on the upstream CLI or an unsupported programmatic API.
- [x] Decide V1 accepts Orca package sources only; Git, npm, and community registries remain with
      existing tools.
- [x] Decide every Skill Bundle share is unlisted and reachable only through its durable link; do
      not add search, browsing, organization-library, marketplace, or contained-skill indexes.
- [x] Record Agent Plugins 1.0.0 commit `bd383552095128f6effe895b9257cfd580a6d179`
      as the portable-format reference.
- [x] Decide to implement from the specification without copying its CC BY prose or vendoring its
      Apache-licensed schemas.
- [x] Treat the archive as a Skill Bundle, not an Orca plugin product or executable plugin runtime.
- [x] Limit V1 bundles to skills; exclude MCP servers, hooks, processes, connectors, and
      permissions.
- [ ] Review the architecture decision record covering the reference-only boundary with
      engineering and legal owners.
- [x] Add a review check that flags any proposed copied or mechanically translated upstream
      material so attribution and licensing can be reconsidered before merge.
- [ ] Assign desktop, runtime, Cloud API, Terraform, security, design, and release owners.
- [ ] Confirm the first release ends after WSL and SSH support; keep team reconciliation as a later
      product milestone.

### Product semantics

- [x] Confirm private means unlisted and protected by an unpredictable revocable bearer link, not
      end-to-end encryption from Orca Cloud operators.
- [x] Confirm a published immutable version persists until package or version deletion; it has no
      age-based object expiry.
- [x] Confirm an unfinished upload grant expires after 15 minutes and its quarantine object is
      deleted after one day.
- [x] Confirm a durable share URL contains a bearer credential for a revocable authorization
      record, not a GCS object or permanent blob grant.
- [x] Confirm a signed download grant lasts five minutes and is the maximum share-revocation lag.
- [x] Confirm updates create immutable versions and never mutate existing package objects.
- [x] Confirm rollback installs a selected prior immutable version.
- [x] Confirm revoking or deleting a Cloud share does not silently remove existing local installs.
- [x] Confirm sharing and updating use an artifact-like flow—preview, upload, unlisted durable
      link, update, revoke/delete—while retaining skill-specific version, trust, and install
      semantics.
- [x] Confirm recipients do not sign in; publishing and managing owned links still require sign-in.
- [x] Confirm revocation blocks future resolution/download grants but does not remove installed
      copies.
- [x] Add a Settings section named **Share Skills**, parallel to **Artifacts**, without adding any
      index or discoverability surface.
- [x] Treat the authenticated owner-only active-link inventory as management, not recipient
      discoverability; never expose it anonymously or through browse/search APIs.
- [x] Confirm V1 has no checked-in workspace desired-state lockfile and no automatic fleet-wide
      installation.
- [x] Confirm one skill is a one-item bundle and a bundle may contain large selections such as 30
      skills behind one durable link.
- [x] Keep bundle identity, access, versions, transport, update/rollback, revocation, and deletion
      at bundle scope.
- [x] Keep installation selection, conflicts, provenance, modification protection, and outcomes at
      skill scope.
- [x] Keep loose-skill installation as the universal/default path and treat provider-native plugin
      adapters as optional compatibility outputs.

### Existing-code and provider research

- [x] Inventory current skill discovery, `observeSkillPackage`, package identity, topology, and
      freshness code; record reusable contracts and missing behavior.
- [x] Inventory plugin staging, provenance, lock serialization, and Windows rename retry designs;
      extract only primitives that both domains can name and test accurately.
- [x] Inventory current desktop IPC and remote skill RPC registration.
- [x] Inventory existing SSH execution and file-transfer providers and identify the host-side
      installer entry point.
- [x] Research official documentation for every initially supported agent's global and project
      skill directories.
- [ ] Verify each provider path with a real installation on every supported platform.
- [x] Record whether each provider reads `.agents/skills` directly, how it is detected, and which
      alias mechanisms it supports.
- [x] Add a normal reviewed maintenance process for provider registry changes; do not create an
      upstream synchronization job.

## 1. Define package and install contracts

### Bundle contract replacement

- [x] Replace the unpublished single-skill envelope with root `plugin.json`, `skills/<name>/`, and
      `dev.orca.skill-sharing/manifest.json`; do not add an outer `bundle/` directory.
- [x] Define `SkillBundleManifestV1` with stable package/version identity, bundle metadata, ordered
      skill entries, per-skill identity and file lists, globally unique archive paths, and a bundle
      digest.
- [x] Validate Agent Plugins 1.0.0 `plugin.json` fields from independently authored local rules;
      never fetch a schema during loading.
- [x] Create fresh staging roots and reject unknown, malformed, or conflicting imported
      `dev.orca.skill-sharing` namespaces without overwriting them. The extractor now exclusively
      creates its staging root, preserves a pre-existing namespace on conflict, rejects unknown
      top-level extension entries, and removes only staging it created.
- [x] Keep the detailed manifest inside the archive for export, remote/SSH transport, and offline
      validation; keep GCS metadata compact and PostgreSQL limited to exact link/ownership lookup.
- [x] Add selected skill IDs and per-skill conflict choices to preview/install requests.
- [x] Return aggregate status plus ordered installed, unchanged, kept-local, and failed per-skill
      outcomes; support retrying failed items only.
- [x] Add `skills.install.bundle.v1` and additive bundle RPC methods so mixed-version peers fail
      before transfer.
- [x] Decide to dispose of the unpublished staging-only single-skill records before changing the
      Cloud schema; there
      is no production compatibility commitment to the unpublished single-skill format.

### Shared package manifest

- [x] Add `src/shared/skill-package-manifest.ts`.
- [x] Define the original single-skill `SkillPackageManifestV1` prototype with schema version,
      stable package ID, immutable version ID, name, description, creation time, file identities,
      and package digest.
- [x] Normalize manifest paths to `/` while keeping filesystem conversion host-owned.
- [x] Define the canonical digest algorithm over normalized paths, file identity, executable state,
      and classification.
- [x] Require `skill/SKILL.md`, valid frontmatter, and agreement between skill and package names.
- [x] Specify deterministic serialization so identical inputs produce identical identities across
      macOS, Linux, Windows, and WSL.
- [x] Version the schema and require additive changes or a new schema version.
- [x] Reject unknown schema versions with a stable error category.

### Package limits and file policy

- [x] Enforce maximum path depth 16.
- [x] Enforce maximum 2,048 archive entries.
- [x] Enforce maximum 512 regular files.
- [x] Enforce maximum 4 MiB per file.
- [x] Enforce maximum 32 MiB total extracted bytes.
- [x] Enforce maximum 40 MiB compressed bytes.
- [x] Reject absolute, parent-traversal, NUL-containing, and Windows drive-prefixed paths.
- [x] Reject duplicate normalized paths and Unicode or case-fold collisions.
- [x] Reject symlinks, hardlinks, devices, FIFOs, sockets, encrypted entries, and other special
      files in V1.
- [x] Preserve executable modes represented by the package manifest.
- [x] Document that install never executes package scripts.

### Install request, preview, and result

- [x] Add `src/shared/skill-install-contract.ts`.
- [x] Define requests with operation ID, immutable package identity, ingress kind, destination, and
      optional conflict resolution.
- [x] Support download-grant, staged-upload, and trusted in-process local-file ingress.
- [x] Ensure arbitrary remote RPC callers cannot supply a local filesystem path.
- [x] Model global, Git worktree, and folder-workspace destinations without assuming Git exists.
- [x] Define preview output for destination, current state, provider coverage, conflicts, and trust
      metadata.
- [x] Define structured installed, updated, unchanged, conflict, partial, and failed results.
- [x] Define stable error categories for admission, transport, archive, filesystem, conflict,
      recovery, provider placement, and compatibility failures.
- [x] Ensure responses never include grants, credentials, ACL membership, or private package
      contents.

### Capability and wire compatibility

- [x] Add `src/shared/skill-install-capability.ts` with `skills.install.v1` and an update-required
      compatibility message.
- [x] Read and apply `docs/reference/remote-wire-compatibility.md` before changing RPC contracts.
- [x] Add new methods without changing existing discovery behavior.
- [x] Keep new request and response fields optional until all supported peers understand them.
- [x] Do not add a terminal stream opcode for skill installation.
- [x] Define behavior for new client/old host, old client/new host, and capability loss during an
      operation.

### Phase 1 contract gate

- [x] Review package, ingress, conflict, result, and capability contracts. Shared schema, runtime
      method, Relay handler, ingress, planner, and stable-failure suites now form the release-gated
      contract evidence; no existing discovery method or stream opcode changed.
- [x] Freeze stable V1 error categories used by desktop, runtime, SSH, and Cloud tests.

## 2. Build and validate packages

### Package creation

- [x] Add `src/main/skills/skill-package-creation.ts`.
- [x] Accept a specific skill directory rather than an arbitrary parent tree.
- [x] Observe and validate the source before staging.
- [x] Copy the source into an owner-private staging directory.
- [x] Observe the staged copy again and fail if its identity differs from the source snapshot.
- [x] Generate a deterministic tar archive with `manifest.json` and a `skill/` envelope.
- [x] Include only `skill/` contents in the eventual installed directory.
- [x] Bind the user-visible share preview to the final staged digest.
- [x] Clean staging files on success, cancellation, source drift, and error.
- [x] Accept a non-empty ordered selection of skill directories and support at least 30 within the
      global entry/file/byte limits. Focused local creation/extraction now covers one 30-skill
      archive; staging load run `31585710645` finalized the same maximum selection through Cloud.
- [x] Reject duplicate normalized skill names and preserve selection across search/filter changes
      in the caller. The picker keeps hidden selections, unions explicit filtered selection, and
      disables a second same-name source before review.
- [x] Generate deterministic `plugin.json`, `skills/`, and Orca extension metadata.
- [x] Bind the share review to every staged skill digest and the final bundle digest.

### Bounded extraction

- [x] Add `src/main/skills/skill-package-extraction.ts`.
- [x] Stream archive inspection and extraction without buffering the entire package.
- [x] Validate `manifest.json` before trusting archive file metadata.
- [x] Enforce compressed, extracted, entry, file, depth, and per-file limits during extraction,
      not only after it.
- [x] Create extraction staging on the same filesystem as the canonical destination.
- [x] Convert manifest paths with the destination runtime's path APIs.
- [x] Re-observe extracted `skill/` and compare every file identity and package digest.
- [x] Delete partial extraction bytes on cancellation or failure.
- [x] Validate the portable root, Orca extension namespace, bundle manifest, and every selected
      `skills/<name>` subtree before destination mutation.
- [x] Extract selected skill subtrees without requiring installation of unselected skills.

### Package tests

- [x] Test deterministic manifests, archives, and digests on macOS and native Windows. The exact
      golden passed on both hosts at `8be7275d0d` after replacing zlib-dependent streaming output
      with bounded deterministic stored DEFLATE blocks.
- [x] Repeat the portable package golden on native Linux and inside WSL.
      The focused golden passed in Debian Bullseye/glibc 2.31 containers on native ARM64 and
      emulated x64, and inside the real Ubuntu 24.04 WSL distro, at `92c8c6a4c6`. The same 26/26
      suite passed at `109272dab1` on a disposable native x86_64 Ubuntu 22.04 GCE host; the VM,
      boot disk, uploaded bundle, and temporary SSH metadata were removed after validation.
- [x] Test source changes during packaging.
- [x] Test CRLF/LF behavior explicitly and document whether byte identity changes.
- [x] Test executable-mode preservation and Windows's mode limitations.
- [x] Test missing, malformed, and identity-mismatched `SKILL.md` files.
- [x] Test every size, count, and depth boundary at limit, one below, and one above.
- [x] Test traversal, absolute paths, drive paths, Unicode/case collisions, duplicate paths, all
      rejected link and special-file types, and encrypted entries.
- [x] Test truncated archives and invalid tar and content checksums.
- [x] Test invalid gzip bytes and map zlib-specific errors to the stable non-retryable archive
      category.
- [x] Fuzz archive path normalization and envelope parsing with bounded resources.

### Phase 2 package gate

- [x] Prove invalid archive classes fail before destination mutation.
- [x] Prove the same source bytes produce the same digest on macOS, Linux, native Windows, and WSL.
- [x] Prove package creation and extraction require no `npx`, external Node installation, or
      upstream CLI runtime.

## 3. Implement the local installer transaction

### Destination resolution

- [x] Add `src/main/skills/skill-install-destinations.ts`.
- [x] Resolve global canonical roots as `<host-home>/.agents/skills/<skill-name>` on the executing
      host.
- [x] Resolve workspace canonical roots from runtime-owned worktree or folder-workspace identity.
- [x] Reject client-supplied remote paths that do not resolve to the selected workspace identity.
- [x] Resolve WSL home, paths, and target distro inside the selected distro.
- [x] Keep all path joins platform-native and reject destination escapes after realpath-aware
      containment checks.
- [x] Support long Windows paths and case-insensitive destination collision checks.

### Admission, locking, and ingress

- [x] Add `src/main/skills/skill-package-download.ts`.
- [x] Add `src/main/skills/skill-install-service.ts`.
- [x] Validate request shape, schema, capability, package identity, scope, destination, and policy
      before download or mutation.
- [x] Recover prior journals for the same destination before planning a new operation.
- [x] Acquire a filesystem-backed cross-process lock keyed by canonical destination.
- [x] Bound lock wait time and return a retryable busy result.
- [x] Stream ingress to an owner-private bounded temporary file and hash it while downloading.
- [x] Require HTTPS whenever the configured Cloud endpoint uses HTTPS.
- [x] Allow only configured Orca skill-bucket origins and reject credential-bearing cross-host
      redirects.
- [x] Check expected compressed bytes, archive SHA-256, package digest, cancellation, grant expiry,
      and disconnects.
- [x] Delete partial ingress bytes on every incomplete path.

### Planning and conflict handling

- [x] Add `src/main/skills/skill-install-planner.ts`.
- [x] Classify missing canonical destinations as installable.
- [x] Classify an identical requested digest as unchanged and continue placement repair.
- [x] Permit clean updates only when installed bytes still match Orca provenance.
- [x] Return a modified conflict when installed bytes drift from their receipt.
- [x] Return an unowned conflict when a destination exists without Orca provenance.
- [x] Return topology conflicts for files, external links, broken links, and name collisions.
- [x] Classify every requested provider placement independently.
- [x] Repeat current-state inspection immediately before commit and invalidate stale previews.
- [x] Require explicit confirmation before discarding local modifications or unowned content.

### Durable commit and recovery

- [x] Add `src/main/skills/skill-install-transaction.ts`.
- [x] Copy extracted bytes into a hidden sibling staging directory and verify the digest again.
- [x] Preserve executable modes where the host supports them.
- [x] Keep staging, replacement, and backup on the destination filesystem.
- [x] Write and durably flush a versioned transaction journal before moving the current
      destination.
- [x] Move an approved existing destination to a journal-owned backup.
- [x] Rename verified staging into the canonical path.
- [x] Add bounded retries for Windows `EPERM`, `EACCES`, and `EBUSY` rename races caused by
      antivirus or indexing.
- [x] Observe the committed destination and require the requested digest.
- [x] Restore the backup after failed commit and retain sufficient journal state after a crash.
- [x] Never remove a path based only on a filename pattern; require journal ownership,
      containment, and expected identities.
- [x] Run bounded recovery at startup and before later operations for the destination.
      Startup scans at most 64 install and 64 removal journals, bounds each read to 4 MiB,
      validates the journal filename against the canonical-path state key, and recovers removal
      before install under the destination lock. Dead-PID locks are reclaimed immediately after a
      killed runtime; malformed locks retain the bounded stale-age safeguard. Corrupt or conflicting
      journals are preserved and reported by path-free failure code for manual recovery.

### Provenance

- [x] Add `src/main/skills/skill-install-provenance.ts`.
- [x] Store versioned receipts outside installed skill directories.
- [x] Record package/version IDs, digest, scope, destination identity, canonical identity,
      placements, previous version, timestamp, and runtime identity.
- [x] Exclude credentials, grants, share values, manifests, and package contents.
- [x] Serialize receipt updates across processes.
- [x] Write receipt updates through durable temporary-file replacement.
- [x] Support aggregate-index reconstruction from bounded per-install receipts.
- [x] Mark the journal complete only after receipt publication, then remove transaction backups and
      staging.

### Verification and discovery

- [x] Re-run skill discovery on the destination after commit.
- [x] Verify the canonical skill and successful provider placements are observable.
- [x] Determine success from installed bytes and discovery, not process exit alone.
- [x] Invalidate renderer skill caches and refresh the Skills page.
- [x] Return canonical success with `partial` when an optional provider placement fails.

## 4. Implement provider placements

### Provider registry

- [x] Add `src/main/skills/skill-provider-destinations.ts`.
- [x] Add data-only records for Orca agent ID, canonical-root support, global/project resolvers,
      detection evidence, and platform alias support.
- [x] Populate only provider paths independently verified from official documentation and real
      installations.
- [x] Detect an agent before creating its provider-specific configuration root.
- [x] Avoid modifying roots for agents that consume `.agents/skills` directly.
- [x] Keep loose-skill placement as the universal/default installation path.
- [x] Do not add Cursor-specific placement in V1; keep the Agent Plugins-compatible root as the
      portabl
```

### docs/automated-setup-tab-astra-review.md
```
# Independent review: automated Setup tab

## Current review verdict

Reviewed product source head `d96ae2ca6afdca919b4d7f8d85308363abe8b28b`, based on the merged PR 1 commit `7f9b51cf5cc1de8769baa646b40c0c93af76be81`, then the documentation-only head and CI corrections described in Rounds 6–8. **P0: none found. P1: none unresolved. Design and actual source diff have converged, with concrete existing paths and no known smaller adequate implementation.** Review only; this report is my only edited file. The numbered rounds below are historical checkpoints, including questions and pending checks that were subsequently resolved.

The implementation retains the existing Setup-tab creation paths and removes only automated setup split placement and its unreachable state. It retires the setting through the existing settings stripper, accepts old-host layouts, preserves manual/issue splits and generic lifecycle behavior, and leaves PR 1's native-chat provisioning change intact. No publication, sibling reattachment, generalized retry, or ownership repair was added.

Product-behavior local validation is complete. Lead's consolidated post-rebase run reports 34 Node suites / 1816 passing tests, two retained expected-failure cases, and two skips on the reviewed source; node/web typechecks and the changed-code gate passed. Rebuilt hidden paired probes passed setup output, independent Setup tab placement, background selection, manual splitting, actual native-chat surface creation, fixture terminal-agent output, and hidden/unfocused host/client windows. I inspected the proof assertions and before/after/native-chat screenshots; I did not independently rerun tests under the lead's exclusive runtime lease. The E2E typecheck comparison reports 261 baseline and 261 final errors, with no new or removed file/error-code pairs; that project remains non-clean. CI subsequently found a fixture-naming ratchet failure; its reviewed correction changes no product behavior, and lead reports both affected ratchets, 23 focused consumer suites (187 passing tests plus two retained expected failures), repeated node/web typechecks and the changed-code gate all passed.

Accepted **P2** limitations: automatic side-by-side setup placement is removed by design; old hosts can still return splits; the conditional ownership fixture does not prove the incident root cause or a publication/reattachment fix; native-chat proof submits no prompt, the terminal agent is a fixture CLI, and platform construction tests do not prove Windows/WSL/SSH execution. The generated English catalog conservatively retains 20 removed-callsite strings (1,136 uncompressed bytes), without restoring settings/search UI. Its remaining nonnative preflight checks passed per the Round 7 receipt. No unresolved source-review question or local correction-validation item remains. The correction commit, exact-head full PR workflow aggregate, and parent merge decision remain separate gates; this report is not merge authorization. Worker settlement awaits the lead's explicit request.

The latest CI correction changes only a stale counterfactual listener-count expectation: the actual 15-listener budget already passed and remains unchanged. The lead reproduced the failing arithmetic under the CI Bun test path, then all four tests and the changed-code gate passed after correction. Round 8 records the independent code/history evidence; no product behavior or performance limit was changed.

## Round 1 — historical design and control-flow review

Reviewed 2026-10-16 in this worktree at `54bb885bbd391642adecdaef262e87c3424f46e6`. Review only; this report is my only owned file. Implementation/final-diff approval is outstanding. Tests and native builds were not run: the coordinator explicitly reserves the shared native-runtime lease for PR 1.

**P0: none found. P1: no demonstrated unresolved design defect in the scoped tab-only approach.** This is not approval of an implementation or proof of the incident's cause. The changes below need concrete checks after PR 1 is merged and this branch is rebased onto that baseline.

### Evidence and scope

- `src/shared/worktree-first-surface.ts:11–17` explicitly seeds a primary shell for either split setting, even with `callerProvidesSurface`. Removing these two conditions removes a real split-anchor dependency without changing startup or issue-command requirements.
- Existing tab implementations are sufficient: renderer `worktree-setup-issue-command-queue.ts:27–45`, host `runtime-worktree-terminal-provisioning.ts:155–197`, and IPC `worktree-remote.ts:368–411`. Keep these command/env/wrapper/handle paths; do not invent a coordinator, ownership store, or retry mechanism.
- The IPC function is actually `spawnLocalStartupAndSetupTerminals` (`worktree-remote.ts:298`), not `spawnCreatedWorktreeStartup`. It is invoked in the local worktree flow at line 1697 despite the filename. Its no-startup/default-tabs early return at lines 308–310 matters when asserting reachability. Label this surface accurately in the design.
- Host success suppresses fallback: `runtime-local-worktree-terminal-startup.ts:203–214` omits returned setup after provisioning, while `worktree-remote.ts:1741–1749` returns only unconsumed setup. Preserving this control flow is smaller and safer than command deduplication. A failed wrapped setup retains `command` at `worktree-remote.ts:421–428`; the renderer prioritizes it at `worktree-setup-issue-command-queue.ts:28–32`.
- `setup-split-activation-single-owner.test.ts:13–18` describes a conditional reconstruction, and its host fixture deliberately returns no session tabs at lines 103–114 while terminal census returns two orphan records at 117–123. That establishes behavior under those premises, not the original missing-binding cause. Keep manual/saved or old-host split coverage without advertising this policy change as a binding/publication repair.

### Native-chat reachability: do not inflate the first-terminal concern

The desktop structured route sets `backendStartup` to undefined (`worktree-creation-flow-execute.ts:63–68`), routes explicit setup through the background seeding branch (`244–269`), and only then launches structured chat (`289–302`). IPC's early return above therefore returns setup for renderer execution. On the ordinary local route, `resolveWorkspaceTerminalHostAuthority` returns `none` (`workspace-terminal-host-authority.ts:124–127`), so it does **not** enter the first-terminal wait at `worktree-initial-terminal-seeding.ts:136–169`. It can use the existing null-primary Setup-tab branch at lines 172–196.

The host-authority branch really does couple returned setup to a first terminal. However, the host native-chat route normally consumes setup (`runtime-local-worktree-terminal-startup.ts:174–187,203–214`), and the paired `agent.launch` test already exercises a real request (`worktree-agent-first-surface.test.ts:155–180`). A P1 claim needs a request that actually returns fallback setup while host authority is live and no terminal will arrive. A constructed `ensureWorktreeHasInitialTerminal` call alone is insufficient. Keep generic delayed delivery unchanged in PR 2 unless PR 1's actual merged route demonstrates that necessity; ask the parent to resolve any overlap first.

### Settings compatibility

Delete the live setting and type; add only a retired-key entry/destructure to `stripRetiredGlobalSettings` (`terminal-settings-migrations.ts:59–91`). The existing function covers loading (`normalize-loaded-global-settings.ts:68`), updates (`settings-update.ts:62`), and serialization (`state-serialization-secret-handling.ts:262`). A separate settings migration/normalization layer has no demonstrated need.

Current paired read/write types omit this key (`runtime-client-settings-shape.ts:7–40,52–75`), and strict RPC `SettingsUpdate` omits it (`client-settings-params.ts:87–131`). Independent bounded named-path history found:

1. `b1973657ea6` introduces `SettingsUpdate` in `src/main/runtime/rpc/methods/client-ui.ts` on 2026-05-21. Its explicit strict allowlist and `getClientSettings`/`updateClientSettings` projection in `orca-runtime.ts:1142–1193` exclude setup location; the same revision uses setup location privately in host provisioning at lines 7006–7009.
2. `c84007c541d^` predates the generated RPC parameter move. `rpc/methods/client-settings-schemas.ts:81–129` remains a strict allowlist without the key, and the then-inline types/projection in `runtime-client-settings.ts` omit it.
3. Targeted `git log -SsetupScriptLaunchMode` over the current/previous schema and client-settings paths found no introduction of the key into those schemas. Historical matches in `orca-runtime.ts` are host provisioning uses, not paired settings fields.

This supports removal without an ignored paired field or wire-schema relaxation. Old hosts still own their placement: accept their returned split layouts without replay, flattening, migration, or interpreting a missing new preference as proof of unexecuted setup.

### Explicit P2 items and acceptance details

- **P2 product tradeoff:** automatic side-by-side placement disappears. Manual and issue splits remain. Users of old hosts can still receive split layouts until that host updates.
- **P2 design precision:** fix the IPC function name and distinguish local IPC from actual remote-host ownership. Replace the missing Electron-skill claim with the coordinator's discovered `agent-browser skills get core` / `electron` capability and pending hidden-CDP validation.
- **P2 coverage retention:** do not delete generic remount/restore/purge/PTY ownership assertions just because their fixtures mention setup. Convert them to manual/issue/old-host splits. Preserve startup identity consumption. Remove only setup-specific geometry gating (`terminal-pane-mount-preparation.ts:222–225`, `pty-resize-geometry.ts:219–226,242–244`); the visible startup-grid settle at lines 211–218 and 228 onward is broader than setup.
- **P2 selection precision:** renderer Setup creation restores the primary only when activation is allowed (`worktree-setup-issue-command-queue.ts:35–43`). Host `createTerminal` does not default to focused: `orca-runtime-core.ts:240–251` and `terminal/launch/terminal-create.ts:252–279` distinguish focus from selection-if-empty. Missing `activate:false` in the host's existing tab branch is not itself proof of focus theft. Assert primary/background selection through the real route instead of changing generic focus machinery.
- **P2 setup-only/templates:** simplify the mode predicate in both `worktree-creation-flow-execute.ts:173–177` and `runtime-worktree-terminal-provisioning.ts:129–138`, while preserving explicit `setupOnly` intent and no-setup fallback. Do not suppress templates for ordinary blank/native-chat creation. The existing failure fallback at provisioning lines 204–221 remains necessary when Setup was the only owed surface.

### Smaller alternatives and convergence

A default-only change is already inadequate: the default is already `new-tab`, while persisted split values still enter three separate branches and create an anchor shell. Ignoring the setting but retaining queues and geometry leaves dead lifecycle state and fails the requested removal. Replacing the three setup placement branches with their existing tab arm, removing only now-unreachable setup plumbing, and retiring the setting through the existing stripper is the smallest adequate design found.

Before declaring design convergence, lead should confirm the corrected route labels, the historical-settings evidence above, and that no first-terminal or publication/reattach work will slip into PR 2 without actual post-PR-1 reachability evidence. No unresolved P0/P1 is currently demonstrated. Final convergence remains conditional on reviewing actual code and meaningful tests, including old-host no-replay, remount one-shot execution, setup-only/defaults, native-chat/terminal/background routes, sequencing failure fallback, and preserved manual/issue splits. Windows/WSL/SSH command tests establish construction behavior only; do not claim those platforms were executed unless they were.

## Round 2 — design convergence

Re-read the revised design after durable message `msg_bf91c03835ff`. The lead incorporated the correct local-IPC function/route, historical paired-schema evidence, first-terminal reachability qualification, and the PR 1/publication/reattachment boundaries. The design retains generic startup-grid settling and requires retargeting generic split fixtures. The Electron capability statement now identifies the installed specialization and keeps validation pending.

**Design converged: no unresolved P0/P1, concrete implementation paths identified, and no known smaller adequate design.** The P2 product tradeoff and old-host behavior are explicit and accepted within scope. This permits scoped source implementation; it does not approve unreviewed code, tests, or merging. Re-evaluate against PR 1's exact merged baseline before final review.

## Implementation review

At this historical checkpoint, lead revision, PR 1 baseline, actual final diff and test results were pending; their resolution appears in the later rounds and current verdict above. Do not interpret this report as a merge authorization.

### Interim fixture review

At the lead's request (`msg_76639d99e47e`), inspected the retargeted delayed-primary/sibling-fallback test in `pty-connection-split-spawn.spec.ts:235–338`. Its CWD promise is a real generic delay (`run-deferred-connect.ts:74–103`), but then it waits for visible startup-grid settling; 20 shared animation callbacks are not necessarily 12 primary settle ticks when the sibling has its own resize callbacks. Recommended making both explicit-startup panes hidden, retaining the CWD gate and shared transport registry, then asserting sibling-first ownership before resolving the primary CWD. Existing `pty-connection-deliberate-sleep-guard.spec.ts:183–213` demonstrates this hidden CWD gate. This preserves the ownership regression purpose without changing production reattachment or restoring removed setup geometry. Lead must verify the proposed fixture correction; reviewer did not run tests or edit source.

### Round 3 — implementation review before PR 1 rebase

Reviewed the restored working diff after `msg_065efb1f75ff` (base remains `54bb885bbd391642adecdaef262e87c3424f46e6`). **No production P0/P1 found.** A final post-PR-1-baseline verdict remains outstanding.

- All three placement changes retain the existing tab arm. Runtime retains completion-token registration, default-tab dressing, explicit setup-only suppression and failed-Setup fallback. IPC retains its wrapper, platform/shell builder, env, inactive/background options, and consumed-result behavior. No setup execution authority or retry mechanism was introduced.
- The removed state is setup-specific. Issue-command queues/consumption remain; `terminal-pane-mount-bootstrap.test.ts` checks the surviving primary-anchor split, env, focus policy and one-shot command clearing. `terminal-pane-pane-created.ts` still passes the captured raw startup identity to `createQueuedStartupConsumer` after removal of the setup-wait copy.
- `terminal-startup-grid-settle.ts` removes only the now-unused readiness predicate and its frame counter. With no predicate, old `readyFrame` and `frame` advanced together, and `usesReadinessGate` was false; the remaining algorithm therefore preserves the former generic branch. Grid stability/cap/cancellation tests and hidden-window start tests remain.
- Compared old and new PTY test-case names: only the obsolete setup-geometry case was deleted; delayed-primary was retargeted, and remount, resize/mobile locks, hidden startup, and replay cases remain. The final hidden-CWD delayed-primary fixture explicitly proves sibling ownership before release and then asserts a distinct primary PTY; lead reports 78/78 passing.
- Existing old-host first-activation reconstruction retains its layout/ownership assertions and now asserts an empty pending-startup map. Its expected-failure branch remains an acknowledged existing limitation, not a claimed fix. Purge/sleep tests retain issue-queue and generic startup coverage while removing only the deleted map's assertions.
- Stale settings are removed on load, update and save/reload by meaningful persistence tests; remaining setup-location references are deliberate stale-profile test input or the stripper. No paired RPC schema change or saved-layout migration was introduced.
- Inspected `setup-before.png` and `setup-after.png` directly in `.bench-fixtures/setup-split-removal-proof`: before has a split inside one terminal tab, after has Terminal 1 and Setup tabs with one visible Setup pane; both display the setup completion marker. Screenshots alone do not prove hidden/focus state; the proof's explicit BrowserWindow assertions and lead's execution receipt cover that separately.

**P2 correction requested (`msg_ce3248db323b`):** `host-split-and-sleep-journeys.ts:56` calls public `terminal.split`, whose RPC handler (`terminal-lifecycle-methods.ts:96–101`) does not forward inactive options; `terminal-split-surface.ts:129,169` defaults activation to true. Thus the renamed `host-split-first-activation` journey can activate during fixture creation and overstates its coverage. Preserve inactive-first-open through an existing internal test seam, or explicitly navigate away and label this a reactivation fixture, retaining genuine old-host first-open coverage in the unit test. Do not broaden production RPC for the fixture. Also asked the lead to format/check the new proof spec and replace its unchecked result cast.

Validation reported by lead: 34 Node files / 1799 tests with two existing expected-fail cases and two skipped; a separate 78-test PTY fixture run; node/web typechecks; changed-file quality gate. Reviewer has not independently executed these under the lead's exclusive native lease. Final logs/results, E2E typecheck baseline comparison, corrected P2 fixture, PR 1 merged-base adaptation, and exact-head workflow gates remain to be assessed.

Round 3 follow-up: verified the P2 fixture correction after `msg_b7784f689bca`: `host-split-and-sleep-journeys.ts:57` returns to the seeded workspace and the oracle scenario is now `host-split-reactivation`. The old-host first-activation unit assertions remain. This resolves the misleading-coverage finding without broadening production scope. The lead will keep the one-off before/after probe under ignored proof artifacts, not in the PR. Lead also reports both hidden before/after probes passed output, tab/pane count, retained manual split, background-selection and hidden/unfocused-window assertions. No unresolved P0/P1 in the currently reviewed PR 2 diff; post-PR-1 review is still required.

### Round 4 — exact PR 1 merged baseline

Verified locally that `merge-base(64fbb53d8a4c92e17c5aa19a8aa86cd1869979bc, 7f9b51cf5cc1de8769baa646b40c0c93af76be81)` is the exact PR 1 merge `7f9b51cf5cc1de8769baa646b40c0c93af76be81`. The PR 2 diff does not modify PR 1's production `runtime-local-worktree-terminal-startup.ts`: its shared `callerProvidesInitialSurface` predicate still supplies the host's background agent ownership decision, and host success still suppresses returned setup at lines 202–209.

Reviewed the only uncommitted overlap adaptation, `src/main/runtime/orca-runtime-tests/worktree-native-chat-setup.spec.ts`. It retains renderer payload construction → strict RPC parse → runtime argument builder → actual managed-worktree create (lines 72–91), and expands the Claude/Codex setup-only-host assertion across both stale split values, new-tab, and absent settings (95–113). It checks command/env, running setup receipt, consumed setup and absence of an invented startup terminal. Former split-anchor controls now request a real startup and verify distinct startup/Setup tab identities (132–143). Blank, activating attribution, run-hooks, skipped setup and default-command controls remain. The stale field is fixture-only and no deleted live type remains.

**Post-rebase semantic review: no unresolved P0/P1, no duplicated PR 1 production change, and no smaller adequate alternative identified.** The accepted P2 product/old-host limitations remain as documented. Final post-rebase checks/proof and the eventual exact-head CI/merge authorization are still separate gates; reviewer is awaiting their receipts and the lead's explicit settlement request.

### Round 5 — committed-head confirmation

Verified the clean tracked worktree at `d96ae2ca6afdca919b4d7f8d85308363abe8b28b`. Its only change from the Round 4 checkpoint is the already-reviewed native-chat setup test adaptation above; no additional production changes were introduced. **P0: none found. P1: none unresolved. The actual PR 2 diff has converged, with no known smaller adequate implementation.**

Post-rebase validation receipt from lead (`msg_87e2f64711ef`): 1443 focused/runtime tests passed with one existing skip; node/web typechecks and the changed-code gate passed; the rebuilt paired hidden placement proof passed two tabs/one Setup pane, actual setup output, retained background selection, manual splitting, and hidden/unfocused BrowserWindow assertions. These are lead-executed results under the exclusive runtime lease, not independently rerun tests. The extra native-chat `agent.launch` probe and final E2E typecheck comparison remain pending and must not be described as passed yet.

Accepted P2 limitations remain: automatic side-by-side setup placement is intentionally removed; old hosts may still publish split layouts; the preserved conditional ownership fixture is not incident root-cause proof or a publication/reattachment fix; Windows/WSL/SSH construction tests do not establish execution on those platforms. The E2E typecheck has a reported baseline of 261 pre-existing file/code failures, with the final comparison still outstanding. This confirms source review on the named head, not exact-head CI or merge authorization. Worker settlement remains pending the lead's explicit request.

Round 5 validation follow-up (`msg_b865b628c0e7`): lead reports the additional final-baseline hidden probe passed. Independently read its actual paired `agent.launch` calls and assertions: background Claude creates a structured chat, the rendered workspace contains exactly one agent-session and one terminal, and the terminal-agent route creates two terminal tabs and displays the fixture CLI marker. Directly inspected `native-chat-after.png`, which shows Setup and Claude Chat with an empty composer. This proves native-chat surface creation, not a model turn; no prompt was submitted. The terminal-agent check uses a fixture CLI, not a real Codex session. The probe asserts every host/client BrowserWindow is hidden and unfocused.

Read `e2e-typecheck-comparison.json`: baseline and final each have 261 errors, with empty new/removed file-and-TypeScript-code lists. Thus no new errors were found by that comparison, while the E2E project itself is not typecheck-clean. These receipts resolve the two pending validation items above. **Final source-review verdict on `d96ae2ca6afdca919b4d7f8d85308363abe8b28b`: no unresolved P0/P1; accepted P2 limitations are explicit; no known smaller adequate design.** Awaiting explicit settlement or any CI-driven source revision.

Final consolidated receipt (`msg_6734645deb90`): the lead reran all 34 selected Node suites after rebasing, reporting 1816 passing tests, two retained expected failures and two skips on the same source head. This supersedes the earlier focused-test counts as the final consolidated local result. All requested local validation items are resolved with the limitations stated in the current verdict; exact-head PR CI and parent merge approval remain outstanding.

### Round 6 — CI fixture classification correction

Verified documentation-only head `c6cdb67aaaf1cc7e0a2b5befa7e6e8b7cbb8cab2` preserved the reviewed product source. CI then rejected two fixture calls to `getDefaultSettings` under the focus-read ratchet. These calls replaced incomplete asserted settings during the setup preference removal; they did not add production execution-host routing.

Independently inspected both fixtures and all repository references before and after the staged correction. Both modules import Vitest, and every discovered consumer is a `.test.ts` file. `check-focus-read-ratchet.mjs:357–359` already excludes `.test-fixture.ts`, with direct coverage at `check-focus-read-ratchet.test.mjs:244`. Renaming to `worktree-activation-created-agent.test-fixture.ts` and `worktree-activation.test-fixture.ts` therefore applies the existing test/product distinction. The staged renames are 100% content-identical; every import edit is test-only. The existing layout detector also excludes fixtures (`check-layout-writer-ratchets.mjs:161–165`), so the correction deletes the one obsolete 21-writer baseline row for the old filename. Neither detector nor any allowance was expanded.

**No new P0/P1/P2 finding in this correction; prior accepted P2 limitations remain.** Conventional fixture naming is smaller and more accurate than a detector change, a suppression, duplicating defaults, restoring unchecked settings casts, or adding baseline allowances. Final correction receipt (`msg_b98097cf4ff3`): both ratchets passed, 23 focused consumer suites passed 187 tests with two retained expected failures, node/web typechecks passed, and the changed-code gate against the exact PR 1 baseline passed. Existing product-behavior and rendered proof receipts remain applicable; a hidden-app rebuild is unnecessary for content-identical fixture renames and test import changes. No local correction-validation item remains pending. Fresh exact-head full PR CI and parent merge approval are still required.

### Round 7 — generated English catalog correction

Verified clean committed fixture-correction head `fe855b8c97ddf90c0d2ad273f1355cf711ee5d8e` exactly matched Round 6. CI then failed catalog verification: removing the Setup UI/search callsites leaves English catalog entries without literal defaults. The existing `collectRuntimeRequiredKeys` contract (`generate-runtime-required-english-catalog.mjs:45–82`) conservatively retains such entries because they may be dynamically referenced; it does not attempt dead-key reachability analysis. The verifier prescribes the existing `sync:localization-runtime-catalog` generator.

Independently compared flattened JSON before/after generation and the deleted callsites: exactly 20 added entries, zero removed or changed entries, all 20 keys present in the removed setup UI/search code. The uncompressed generated file grows by 1,136 bytes. There is no unrelated generator churn and no restored UI or search registration. Regenerating this single derived catalog is the smallest conservative correction; pruning locale translations requires a broader dynamic-key/locale audit, and changing the verifier would weaken an unrelated contract.

**No new P0/P1; accepted P2:** some obsolete English text remains in the boot catalog under its existing conservative policy. This does not restore setup split behavior. Lead's final receipt (`msg_83f4e9157231`) reports the remaining nonnative gates passed: localization catalogs/extraction/coverage using the CI Bun commands, feature-wall budget, macOS entitlements, and preload/shared declaration guard. The unit-plan script completed its local full-reference fallback, which is not itself proof of the CI plan; lead separately reports the actual CI plan and all static steps preceding catalog verification, including Typecheck, had passed. No local correction-validation item remains pending. Fresh exact-head full PR CI and parent merge approval remain required after the correction commit.

### Round 8 — stale listener-savings arithmetic

Verified committed catalog head `35f132ba2547422cb6e11e00d1b631528fdab424` matched Round 7. A required unit shard then failed `terminal-pane-store-subscription-budget.test.tsx`. Independently traced the exact assertions: the live per-pane budget remains 15 and its assertion passes; the failure is the later equation `45 - 15 = actionKeys.length + 6`, where the action list is now 23, making the right side 29 rather than 30. It is not a measured increase to 30 live subscriptions.

PR 2 removed `consumeTabSetupSplit` from the stable `useMemo`/`getState` action binding and removed a `useState` initializer that reads `pendingSetupSplitByTabId` through `getState`. Neither opened a subscription. The `PRE_FOLD_LISTENERS_PER_PANE` comment defines a counterfactual current mount with one listener per bound action, not an immutable historical observation. Bounded history corroborates its intended updates: `3e25fe70f6b` lowered 46 to 45 for removal of `readTerminalPaneOnInput`; `93baa828be9` lowered 50 to 46 for four removed actions. Both retained the actual live budget.

The reviewed correction changes only `PRE_FOLD_LISTENERS_PER_PANE` from 45 to 44 and makes the stale action-count comment count-neutral. The exact 15-listener assertion, linear scaling, zero-listener stable-action binding and action identity assertions remain unchanged. This is smaller than introducing a retired-action offset or changing the test model, and does not loosen any live performance limit. **No new P0/P1/P2; prior accepted P2 limitations remain.**

Lead's receipt (`msg_278eaae4e38e`): the exact Bun path reproduced one savings-equation failure with three tests passing before the change; all four passed afterward, and the changed-code gate against the exact PR 1 baseline passed. No product source changed. Existing product validation remains applicable; fresh exact-head full CI and parent merge approval remain separate pending gates.
```

### docs/automated-setup-tab-design.md
```
# Automated workspace setup: dedicated Setup tab

Status: design converged; implementation, local validation, and independent source review complete. Exact-head CI and merge authorization are tracked by [PR #29819](https://github.com/stablyai/orca/pull/29819).

## Decision and boundary

Run terminal-backed automated workspace setup in its own **Setup** tab using the existing new-tab path. Remove automated setup split placement, its preference/control, and its one-shot split/geometry state. Keep manual splits, issue-command splits, generic startup consumption, saved layouts, default-tab policy, and setup-to-agent sequencing.

This is PR 2. [PR 1 (#29810)](https://github.com/stablyai/orca/pull/29810) separately fixed background native-chat setup provisioning and merged first as `7f9b51cf5cc1de8769baa646b40c0c93af76be81`. This branch was rebased onto that exact merge before final review and relevant checks. Parent chat-publication and sibling-reattachment fixes, broad terminal ownership, corrupt saved-binding repair, and retries are outside this PR.

## Evidence and severity

* Confirmed pre-change mechanism: `shouldSeedWorktreePrimaryTerminal` treated split setup as a reason to create a shell even when the caller supplies native chat. Renderer `queueSetupAndIssueCommands`, runtime `provisionWorktreeTerminals`, and `spawnLocalStartupAndSetupTerminals` in `worktree-remote.ts` each branched on setup location. This PR reuses their existing dedicated-tab arms.
* The supplied incident investigation observed two leaves bound to one PTY and an independent equal-count chat-publication failure. This worktree does not establish the original missing-binding cause or two setup executions. Removing placement complexity is the user-requested product policy; it is not proof of fixing every frozen terminal.
* No demonstrated P0. P1 acceptance risks are replaying setup after host provisioning, losing requested startup/setup sequencing, or changing primary selection/background workspace selection. The validation below exercises actual creation routes and the preserved one-shot startup mechanisms.
* P2 tradeoff: automatic side-by-side setup placement disappears; manual splitting remains. Older execution hosts can still return existing split layouts, which updated clients must accept without moving/replaying setup.
* The first-terminal delayed delivery coupling exists in `ensureWorktreeHasInitialTerminal` for runtime-owned fallback commands. Ordinary desktop structured creation passes no backend startup and returns setup through local IPC, then uses host authority `none`, so its null-primary Setup path is already independent. The host native-chat route normally consumes setup before returning. Keep delayed delivery unchanged: no actual request proves the alleged native-chat P1. The post-PR-1 semantic review found no reason to expand this scope. The conditional STA-9417 expected-failure fixture does not establish the original incident's cause.

## Surfaces and selection

| Intent | Surfaces owed by this create with setup |
| --- | --- |
| Native chat | Requested chat plus Setup, without a split-anchor shell. |
| Terminal agent | Requested agent terminal plus Setup. |
| Plain terminal | Normal primary terminal plus Setup. |
| Setup only | Setup alone; preserve current suppression of default tabs. |
| Explicit default tabs | Existing template allocation/commands/title/color policy plus Setup. |
| No setup | Existing behavior. |

Issue automation retains its independent split from the normal primary pane, command/env, one-shot behavior, and focus policy. Setup stays unselected when another primary surface exists. Setup-only can select Setup when creation is still in view. Background creates/navigation away preserve workspace/tab selection and never reveal/focus a native window.

## Small existing mechanisms

1. Renderer: always create Setup with `pendingStartup`, title it through `setTabCustomTitle`, and preserve active primary/background options. Remove the location input from primary-shell and setup-only decisions. Retain host-spawn-result handling: `runtime-local-worktree-terminal-startup.ts` and local IPC omit consumed setup from fallback results, and remount restores its existing surface.
2. Runtime host: always `createTerminal` titled Setup; retain command construction, env, completion token/returned handle, fallback surface, `surfaceOwner`, and default-tab dressing. Remove setup's use of `splitTerminal` without changing generic split APIs.
3. Local IPC creation (`spawnLocalStartupAndSetupTerminals` in `worktree-remote.ts`): always use the existing new-tab branch; preserve platform runner/shell selection, sequencing wrapper, `activate: false`, and host authority. Accept old-host startup/layout evidence as authoritative.
4. Delete `pendingSetupSplitByTabId`, queue/consume actions, setup props/captured refs/bootstrap branch, setup-only geometry waits. Preserve generic geometry/resize functions used elsewhere and startup identity consumption. Do not remove regression purpose when updating fixtures: use manual/saved or issue-command splits for generic restore, purge, remount, and PTY ownership coverage.
5. Remove the Setup Script Location section and search registration. No new style/token/component is needed; follow `docs/STYLEGUIDE.md`.

## Settings and mixed versions

The implementation deletes `setupScriptLaunchMode` from live `GlobalSettings`, defaults, and launch types, and adds it to existing `stripRetiredGlobalSettings` so stale load/update/save keys are dropped. Remaining setting inputs are deliberate legacy-profile regression fixtures. There is no dead normalization or shared type retained for an unproven peer requirement.

Current `SettingsUpdate` is a strict explicit client-settings allowlist without this key; `RuntimeClientSettings` and `RuntimeClientSettingsUpdate` also omit it. Independent bounded history confirms the initial paired schema/projection at `b1973657ea6` (2026-05-21) and the pre-generated schema/types at `c84007c541d^` omit it; targeted key-history finds no paired-field introduction (see the Astra report for paths). Retire through the existing stripper, which already covers load, update and serialization; do not add a new normalization layer. Hosts own placement: an updated host ignores retired settings, and an old host may still produce a split. Updated clients accept returned layouts without replay or migration. Removing a client setting cannot force old hosts to adopt the new policy.

No protocol field/opcode, live-layout migration, scheduler, ownership store, command-string deduplication, or retry machinery is proposed. Runner arguments/env/cwd, Windows batch/shebang, WSL/SSH paths, and setup completion remain with existing functions.

## Alternatives

Changing only the default retains legacy split behavior and lifecycle complexity. Keeping the setting while ignoring it retains an unused contract unless actual old-peer evidence requires it. Moving all setup provisioning into a new service duplicates existing working paths and crosses PR 1. General binding enforcement and saved-layout repair solve broader problems and need separate evidence/design. Independent design and actual-diff review found no known smaller adequate approach; this is a scoped engineering judgment, not a mathematical optimality claim.

## Validation and review gates

Before implementation: Astra round 1 found no demonstrated unresolved P0/P1 in this scoped design, with concrete route/settings evidence and no known smaller adequate approach. Round 2 confirms the corrected local-IPC label, historical settings evidence, unchanged first-terminal delivery and strict PR 1/publication/reattachment boundary. The independent report is `docs/automated-setup-tab-astra-review.md`; implementation review remains separate.

Meaningful automated coverage: renderer/native-chat/terminal/setup-only/default-tab/background actual requests, host/remote no-split command/env preservation, sequencing/failure fallback, old-host returned layout/no replay, remount one-shot startup, issue-command/manual split/restore/purge regression intent. Run relevant tests with `ORCA_BACKGROUND_LAUNCH=1`, node/web typechecks, changed-file code-quality and format checks. Preserve platform-specific runner tests; report platforms actually exercised.

Rendered checks require rebuilt hidden Electron plus Playwright CDP; inspect tab count/selection/setup output and retained manual splits, with before/after evidence. The installed agent-browser CLI provides the version-matched Electron skill (`agent-browser skills get core`, then `agent-browser skills get electron`), now read; use it alongside Playwright CDP. The coordinator serialized the shared native-runtime lease after an initial local rebuild failure; the supported rebuilt hidden-app checks subsequently passed.

After implementation: Astra reviews actual final diff/tests and semantic overlap after PR 1 rebase. No merge until PR 1 confirmation, exact-head full `.github/workflows/pr.yml` successful aggregate `verify` / PR checks passed and all required checks, and parent approval through the mandatory blocking merge-gate ask. Use `--match-head-commit` and confirm the merge.


## Implemented validation record

Reviewed source head: `d96ae2ca6afdca919b4d7f8d85308363abe8b28b`, based on the exact PR 1 merge above. The follow-up documentation commit changes no source behavior. The independent review records no unresolved P0/P1 and explicit P2 tradeoffs.

- **Node tests:** final consolidated post-rebase selection passed 34 suites and 1,816 tests; two existing conditional expected-failure cases and two skips remain visible. The selection includes composed native-chat create payload/RPC/host routes for Claude and Codex, retired locations, setup-only/default tabs, wrapper/env/shell construction, failure fallback, one-shot startup, old-host layouts, manual/issue splits, remount, restore, sleep and purge behavior.
- **Types and static checks:** node/web typechecks, changed-file code-quality gate and staged Oxlint/format checks passed. The extra e2e project still reports 261 baseline diagnostics; baseline/final comparison by file and TypeScript error code found none added. This is not a clean e2e-project typecheck. A Bun `node:sqlite` suite-loader failure was avoided by executing the complete selected suites with the supported `test:node` command; no test-routing refactor is included.
- **Real rendered before/after:** rebuilt e2e-mode Electron host and paired client, both hidden, legacy vertical-split preference. Before: one terminal tab and two panes. After: Terminal 1 and Setup tabs, one Setup pane. Both displayed the real setup completion marker, retained background tasks selection, and supported another manual split. Post-rebase after-proof passed again. Screenshots are attached to the PR outside the source diff.
- **Rendered agent surfaces:** actual paired `agent.launch` created Claude native chat plus Setup with no shell anchor; the empty chat composer rendered and no prompt/model turn was submitted. A terminal-agent fixture CLI launched separately beside Setup and displayed its marker. Every native window was asserted hidden and unfocused.
- **Coverage retention:** the public `terminal.split` API activates by design, so its host layout fixture explicitly navigates away and tests reactivation. Genuine conditional old-host first-activation ownership/no-replay assertions remain in the unit fixture. Its expected-failure reconstruction is not presented as incident-cause proof.
- **Platforms actually executed:** macOS local Electron host plus paired desktop client. Windows/WSL command construction is tested, while live Linux, Windows, WSL and SSH execution were not performed. Existing saved layouts remain intact, and old execution hosts can still publish split layouts until upgraded.

Design/Astra artifacts are intentionally preserved in this PR. One-off probe sources and raw local logs live under ignored `.bench-fixtures/setup-split-removal-proof`; no images, profiles, auth data, or temporary test spec are committed. Merge still requires the exact current head's full PR workflow aggregate and all required checks, then the parent's mandatory blocking merge-gate approval.
```

### docs/native-chat-setup-provisioning-design.md
```
# Native-chat background setup provisioning

## Problem and evidence

A structured native-chat creation deliberately omits terminal startup in `worktree-creation-flow-execute.ts`, while passing the selected agent as `createdWithAgent`. `buildRuntimeWorktreeCreateParams` and the RPC `buildManagedWorktreeCreateArgs` preserve that agent and leave activation false when startup is absent. The execution host therefore handles this as background creation, even when the renderer later opens the chat.

The host already treats a submitted agent as a caller-provided surface for background creation without setup. With setup/default tabs, `provisionArgs` instead recognizes only the internal `promisedAgentChat` flag. In new-tab setup mode this inconsistency creates an idle shell before Setup. Renderer-only tests returning unprovisioned setup do not exercise that host decision.

## Proposed policy

Use one host-local caller-surface predicate for terminal provisioning and fallback shell seeding: explicit `promisedAgentChat` always counts; submitted `createdWithAgent` counts only when neither `activate` nor `runHooks` is true. These are transient inputs to this create, not persisted workspace metadata. Apply the same predicate whether or not setup/default tabs exist.

Continue using `shouldSeedWorktreePrimaryTerminal`: a real startup, issue work, existing default terminal, setup-only choice, and split setup anchors retain their existing precedence. Activated attribution-only requests still owe a primary terminal; attribution must not become an activation promise. Preserve every setup split mode and current setup sequencing, surfacing, completion, and failure behavior.

## Scope and compatibility

Change only the host startup policy and regression coverage. No new RPC field, surface store, ownership/retry redesign, split removal, process command change, or UI styling. Renderer and RPC already transmit enough information for the existing background policy; a new wire intent would duplicate that policy and leave older clients unfixed. Old clients benefit when connected to the updated execution host; updated clients connected to old hosts retain the old behavior. Nothing changes execution-host ownership or introduces client-local SSH fallback.

Folder creation has its own matching no-setup background policy and no automated setup provisioning path; retain it and cover its existing contract. The shared host policy is platform independent and leaves macOS/Linux/Windows/WSL runner construction unchanged. Manual splits, explicit commands, issue automation, default tabs, and startup failures remain owned by their existing mechanisms.

Background attribution-only callers intentionally inherit their established no-setup policy. The pre-existing conditional issue-only/first-terminal coupling and asynchronous setup failure reporting are P2 follow-ups outside this change; successful setup/default provisioning still supplies the terminal used for queued issue work. Independent Astra design review accepted this scope with no P0/P1 before implementation.

## Verification

Add coverage that feeds actual structured renderer creation arguments through the production payload builder, RPC schema/argument mapping, host startup, and real terminal provisioner, recording created terminals. New-tab setup should create Setup alone for background native chat, while blank/background creation still receives its shell. Cover both agents, activated attribution-only creation, run-hooks, promised chat, explicit startup, default tabs, split anchors, and setup-only/failure behavior using existing tests where adequate.

Demonstrate the regression failing against the original policy and passing after the change. Run relevant renderer/runtime/RPC/provisioning/folder tests, node and web typechecks, and changed-file format/lint checks with `ORCA_BACKGROUND_LAUNCH=1`. No platform or rendered UI result is claimed without an actual run. Independent Astra review must converge before implementation and review the final diff with no unresolved P0/P1; record P2 dispositions in the review report.

## Results

The original policy failed both agent regressions by spawning an undefined-command shell before Setup; nine controls passed. With the fix, seven selected suites passed 1,451 tests with one existing skip; 15 focused route/promised-chat controls and four first-surface tests also passed. Node/web typechecks, changed-file lint, formatting, and the Electron e2e build passed on macOS ARM64.

A temporary Playwright probe used isolated hidden host/client apps, the production renderer create action with `createdWithAgent: codex` and no startup, real RPC/PTY provisioning, host terminal inventory, and DOM tab-strip assertions. The baseline host rendered two terminal tabs; the fixed host rendered Setup alone. Both runs passed hidden/unfocused-window assertions and captured CDP screenshots. This verifies the terminal provisioning behavior, without claiming a real structured-agent launch or live SSH/Windows/Linux/WSL run. Probe source, logs, and screenshots are retained locally under `.bench-fixtures/native-chat-setup-proof/`; screenshots are attached to the PR, not committed. Final source was restored and rebuilt after the baseline capture.
```

### examples/ listing
```
dir	plugins
```


### CLAUDE.md
```
@AGENTS.md
```

### AGENTS.md
```
# Design System

All UI work — layout, color, typography, spacing, component selection, UX behavior — must follow [`docs/STYLEGUIDE.md`](./docs/STYLEGUIDE.md). Most of it is linted: `pnpm run check:code-quality:changed` fails on new restyles of a `components/ui/` primitive, raw palette colors, and computed `className` strings; `pnpm lint` fails on any class Tailwind cannot generate. See the Enforcement section of the style guide before suppressing either. Use the tokens defined in `src/renderer/src/assets/main.css` (the canonical source) and the shadcn primitives in `src/renderer/src/components/ui/`. Don't invent new color values, font sizes, or shadow tiers when a documented one already covers the role. When STYLEGUIDE.md is silent, follow the resolution order in its final section. In `components/native-chat/`, the "Chat type scale" and "Chat text colour, hover and focus" sections are binding, and `pnpm lint` fails on arbitrary font sizes, softened `text-foreground`, and weakened focus rings there.

## Electron UI Validation

Always run tests and agent-launched apps in the background with `ORCA_BACKGROUND_LAUNCH=1`.
Never steal monitor focus or reveal test windows: no `show()`, `showInactive()`, `bringToFront()`,
`app.focus()`, or OS activation. Use CDP screenshots of hidden renderers. Keep native-focus and
visible-window tests paused on the user's desktop; run them on an isolated display or CI.
Rebuild modified launch-policy code before running an app; stale build wrappers are not safe.

Use the `$electron` skill and Playwright CDP for rendered Orca UI checks. Do not use computer-use for Orca UI validation.

# Style

## Reuse Before Reimplementing

Before writing new logic at any scale — a function, component, IPC channel, state store, or whole subsystem/flow — check whether an existing implementation already does the job (or nearly does). Extend or generalize it instead of building a parallel version; only write from scratch when nothing fits. Keep the check proportionate: a quick search for trivial code, a real one before building anything substantial.

## Concise/Brief Non-obvious Comments ONLY

- DO NOT: be verbose, explain the obvious, walk through the code ("WHY not HOW")
- BE CONCISE. 1 LINE if possible

## Lint Rules: Do Not Disable Max Lines

NEVER add a `max-lines` disable (`eslint-disable max-lines`, `oxlint-disable max-lines`, or line-specific variants), and never add a per-file `max-lines` bump in `mobile/.oxlintrc.json`.

## File and Module Naming

Never use vague names like `helpers`, `utils`, `common`, `misc`, or `shared-stuff` for files, folders, or modules. They carry zero info and tend to become dumping grounds. Name files after what they _actually_ contain — prefer the concrete domain concept (e.g. `tab-group-state.ts`, `terminal-orphan-cleanup.ts`) over the generic role (`tabs-helpers.ts`, `terminal-utils.ts`). If you find yourself reaching for `helpers`, the file probably has more than one responsibility and should be split, or there's a better name hiding in the code that describes what the functions operate on.

## Type Declarations: Prefer `.ts` Over `.d.ts`

## Type Assertions: Prefer Checked Types

Avoid type assertions except `as const`. Unavoidable casts need a line-specific `SAFETY:` explanation:

```ts
// oxlint-disable-next-line typescript/consistent-type-assertions -- SAFETY: Explain the verified invariant here.
```

# Verifying Changes

- **Typecheck**: `pnpm tc` (or `tc:node` / `tc:cli` / `tc:web`)
- **Test**: `pnpm test [path/to/file.test.ts]`
- **Lint**: `oxlint`, or `pnpm run check:code-quality:changed` for changed files (full `pnpm lint` is slow); format with `pnpm format`
- **Design system**: `pnpm run lint:design-system` for the full renderer report (not a gate); the changed-lines gate above is what CI enforces
- **Real Claude CLI**: when you change Claude structured-session code (`src/main/claude/claude-structured-*`), run `ORCA_REAL_CLAUDE_CLI_TEST=1 pnpm test src/main/claude/claude-structured-real-cli.test.ts src/main/claude/claude-structured-real-cli-fold.test.ts`; it uses your real Claude login

# Writing Pull Requests

Fill in [`.github/pull_request_template.md`](./.github/pull_request_template.md), written for a reviewer who has never seen this code:

- No jargon — plain language, no internal shorthand.
- The before and after as the user experiences it.
- The mechanism you changed, not just the symptom.
- Why this approach over the alternatives you considered.

Cover all four concisely. Don't pad or walk the diff.

## Merging Pull Requests

Before merging, verify that the required checks and aggregate gate in the full PR workflow have passed for the exact current PR commit. For GitHub, identify the `.github/workflows/pr.yml` run and its aggregate `PR checks passed` (job ID `verify`); Mobile Checks is separate and never substitutes for it. Check workflow identity as well as the displayed job name. If the head changes, repeat the check for the new head.

Pending, failed, cancelled, or missing required checks block agent merges even when repository settings allow them. `gh pr merge --auto` is not proof that CI passed: GitHub may merge immediately when checks are optional. Never use `--admin` or disable protection to bypass a failed check. An explicit user instruction to make an emergency exception overrides this default; otherwise fix the failure or wait. Use `--match-head-commit` to prevent merging a different commit after validation.

CI changes must exercise the affected checks in the PR. Required check names must be unique across workflows, and workflow changes must preserve the full aggregate's failure handling and conditional job requirements.

# Considerations

## Worktree Safety

Always use the primary working directory (the worktree) for all file reads and edits. Never follow absolute paths from subagent results that point to the main repo.

## Cross-Platform Support

Orca targets macOS, Linux, and Windows. Keep all platform-dependent behavior behind runtime checks:

- **Keyboard shortcuts**: Never hardcode `e.metaKey`. Use a platform check (`navigator.userAgent.includes('Mac')`) to pick `metaKey` on Mac and `ctrlKey` on Linux/Windows. Electron menu accelerators should use `CmdOrCtrl`.
- **Shortcut labels in UI**: Display `⌘` / `⇧` on Mac and `Ctrl+` / `Shift+` on other platforms.
- **File paths**: Use `path.join` or Electron/Node path utilities — never assume `/` or `\`.
- **Windows terminal shells**: `--shell` picks the shell a terminal _is_; `--command` is typed into whatever shell the host spawned, so a shell choice routed through `command` silently becomes a child process.
- **Windows setup scripts**: the setup/issue-command runner is a `.cmd` batch file unless the script starts with a `#!` line — never derive that from the user's terminal-shell preference, and never launch a `.cmd` runner with a bare `cmd.exe /c` from a Git Bash pane (MSYS rewrites the `/c`).
- **Windows child processes**: start them through `runProcess`/`spawnProcess` from `@orca/process-host` — never `child_process` directly. It pins `windowsHide`, refuses `shell: true`, and encodes `.cmd`/`.bat` arguments so neither `CommandLineToArgvW` nor `cmd.exe` mangles them. Recognised npm/pnpm `.cmd` shims are resolved to their real target so the spawn skips `cmd.exe` entirely.
- **Ripgrep**: Orca bundles `rg` for every platform, WSL, and SSH remotes. Spawn it through `spawnBundledRipgrep` (main) or `resolveRelayRipgrepCommand` (relay), never a bare `'rg'` — Windows resolves a bare name in the spawn cwd before PATH. Don't add git/readdir fallbacks locally; the relay's chain exists only for hosts an upload never reached.
- **Windows process enumeration**: read the table through `src/main/windows/windows-process-table.ts`, never by forking `powershell.exe`.
- **Windows MSYS/Git Bash panes**: their children break away from the per-PTY job unless it is created without `JOB_OBJECT_LIMIT_BREAKAWAY_OK`, and a `conpty.node` built before that fix passes every existing gate.
- **Windows daemon-host relocation**: the terminal daemon runs from a copy of the app runtime under `%LOCALAPPDATA%`, which is what survives an auto-update.
- **macOS daemon launch**: packaged macOS runs the terminal daemon from a copy of the signed terminal host helper through launchd, so an update cannot sever its privacy grants. Before touching that copy, its cleanup, or the fork fallback, read [`docs/reference/macos-daemon-tcc-attribution.md`](./docs/reference/macos-daemon-tcc-attribution.md).
- **Windows EDR signal**: don't add `-ExecutionPolicy Bypass`, `-EncodedCommand`, `cmd.exe /c` with escaped free text, per-operation interpreter spawning, or runtime `Add-Type` compilation without reviewing the EDR impact first — behavioural EDR scores each of those, and being signed does not clear them.
- **WSL commands**: build argv with `buildWslExecArgs` (always `--exec` — under `--`, `wsl.exe` expands `$name` in every argument and silently rewrites the script), and fence anything whose stdout you parse with `buildWslCapturedLoginShellCommand`, because the interactive login shell prints the distro banner to stdout.
- **Linux native modules**: keep the glibc floor at Ubuntu 20.04 / glibc 2.31. A module compiled from source on a newer runner can reference symbol versions absent on the floor and crash the app on startup. Packaging fails if a bundled native binary needs newer glibc.

## Native Dependency Installs

Ordinary `pnpm install` covers the host OS and CPU only. Before packaging for another architecture — including `pnpm build:mac`, which builds x64 and arm64 by default — run `pnpm install:release`. electron-builder only warns on a missing `extraResources` source, so the `beforePack` guard is what turns a thin install into a build failure instead of a silently broken artifact.

## SSH Use Case

All changes must consider the SSH use case. Don't assume local-only execution. Before changing anything that reports on, stops, or lists remote work, the execution host owns everything that touches execution, and loss of contact is never evidence of process death — the verdict vocabulary is `live` / `unverifiable` / `exited`, with no synonyms.

## Folder Workspace Use Case

All changes must consider folder workspaces as well as git worktrees. Don't assume every workspace is a git worktree.

## Agent Status

The execution host owns agent status in one store, the hook server's, and every reader (sidebar, `worktree ps`, mobile, dashboard) subscribes to it. New producers write into that store, and readers keep only presentation policy.

## Agent Terminal Screens

A rule that reads what an agent CLI paints on a terminal — readiness, blocked prompts, idle — must be written against a captured transcript, not a remembered screen. Use `config/scripts/capture-agent-pty-transcript.mjs` to keep escapes and wrapping intact and scrub account identifiers before they reach git.

## Remote Wire Compatibility

Clients and remote Orca servers update independently, so mixed versions are the normal state. Before changing anything a paired client and host exchange — RPC params, stream frames, or the content either side publishes over them — preserve compatibility with older peers. A new optional field is safe; a new stream opcode must be capability-negotiated because decoders drop unknown opcodes silently; and changing what the host publishes reaches old clients even with no wire change.

## Git Binary Compatibility

Orca runs the user's Git binary on native, WSL, and SSH hosts, which may all have different versions. Treat Git 2.25 as the core-workflow baseline.

When adding or changing a Git command:

- Check when every subcommand and option was introduced. For newer behavior, keep a baseline-compatible fallback or degrade safely.
- Use `GitCapabilityCache` with a narrow unsupported-error predicate so recurring operations do not retry a known-invalid command. Do not rely only on `git --version`; wrappers such as `simple-git` do not remove host-version differences.
- Scope capability state to the host that executes Git: native, WSL distro, SSH provider, or relay connection. Cover the first fallback, later cached calls, concurrent probes, and relevant host isolation in tests.
- Keep the real-binary compatibility contract in PR CI current. When adopting a newer Git feature, add its version boundary so the preferred command and fallback both run against representative Git releases.
- Preserve commands that begin with global Git options such as `-c` before the subcommand, including auto-maintenance suppression used by worktree-create fetches.

## Git Scan Safety

- Never enumerate every ref and then run `git ls-tree -r` or `git show` once per ref. That ref × tree fan-out can retain gigabytes of output before a downstream `sort -u` or search can make progress.
- Prefer `rg` over the checked-out files for source searches. For history or refs, use a named ref, an explicit namespace/path, `--max-count`, and a bounded output; do not use an unqualified `--all` scan as a first diagnostic.
- Keep repository-wide commands targeted to the current repository and worktree. If an unbounded scan is genuinely required, measure the ref count first, explain the cost, and get confirmation before running it.

## Git Provider Compatibility

Source-control and review changes must consider GitLab and other supported git providers, not only GitHub. Keep provider-specific behavior behind explicit checks, and avoid GitHub-only naming for generic review concepts.

## GitHub CLI Usage

Be mindful of the user's `gh` CLI API rate limit — batch requests where possible and avoid unnecessary calls. All code, commands, and scripts must be compatible with macOS, Linux, and Windows.
```


## Top-level structure
```
file	.gitattributes	.gitattributes
dir	.github	.github
file	.gitignore	.gitignore
dir	.husky	.husky
file	.oxfmtrc.json	.oxfmtrc.json
file	.oxlintrc.json	.oxlintrc.json
file	AGENTS.md	AGENTS.md
file	CLAUDE.md	CLAUDE.md
dir	Casks	Casks
file	LICENSE	LICENSE
file	README.md	README.md
dir	cloud	cloud
file	components.json	components.json
dir	config	config
dir	docs	docs
file	electron.vite.config.ts	electron.vite.config.ts
dir	examples	examples
dir	mobile	mobile
dir	native	native
file	opencode.json	opencode.json
file	orca.yaml	orca.yaml
file	package.json	package.json
file	pnpm-lock.yaml	pnpm-lock.yaml
file	pnpm-workspace.yaml	pnpm-workspace.yaml
dir	resources	resources
dir	skill-guides	skill-guides
dir	skill-stubs	skill-stubs
dir	skills	skills
dir	src	src
dir	tests	tests
file	tsconfig.json	tsconfig.json
file	vite.web.config.ts	vite.web.config.ts
```
