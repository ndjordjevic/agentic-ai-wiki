---
type: source
category: "Media, voice & content"
source_url: https://github.com/bradautomates/claude-video
tags:
  - agent-skill
  - video-understanding
  - yt-dlp
  - ffmpeg
  - whisper-transcription
  - frame-extraction
  - multimodal-read
  - multi-harness
related:
  - Starmel-OpenSuperWhisper
  - skills.sh
  - davila7-claude-code-templates
product: claude-video
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

`claude-video` (8,256+ stars, MIT) is an Agent Skill (`/watch`) that gives Claude the ability to genuinely watch a video — not guess from a title or a partial transcript — by downloading it, extracting scene-aware frames, pulling a timestamped transcript (free captions first, Whisper as fallback), and handing both to Claude's multimodal `Read` tool. It's a focused, single-purpose skill (one video comprehension pipeline, ~8 Python scripts) rather than a broad toolkit, and ships with measured token/latency numbers for each fidelity tier rather than vague claims.

_All claims below are sourced from ../../raw/github/bradautomates-claude-video.md unless otherwise noted._

## What it does

`/watch <url-or-path> <question>` accepts anything `yt-dlp` supports (YouTube, Loom, TikTok, X, Instagram, and a few hundred more sources) or a local file (`.mp4`, `.mov`, `.mkv`, `.webm`). It fetches native captions first when available (fast, free, no download needed at `transcript` detail), extracts frames at a chosen fidelity, and falls back to Whisper transcription (Groq or OpenAI) only when a video has no caption track. Claude then `Read`s every extracted frame as an image and answers grounded in what it actually saw and heard — the README frames this against the default failure mode of an agent guessing from a video's title or a threadbare auto-transcript. Named use cases: reverse-engineering a viral video's hook/structure, diagnosing a bug from a screen-recording, summarizing a long video, stripping hype from a launch/update video, and turning a playlist into a set of per-video notes.

## Installation

**Claude Code** (recommended, auto-updates via marketplace):
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```
**Codex, Cursor, Copilot, Gemini CLI, and 50+ other hosts** via the [Agent Skills](https://agentskills.io) CLI:
```bash
npx skills add bradautomates/claude-video -g
```
`-g` installs globally (`~/.codex/skills`, `~/.cursor/skills`, etc.); dropped for per-project scope. The CLI discovers the skill from `skills/watch/SKILL.md` and copies the whole self-contained folder (`SKILL.md` + its `scripts/` runtime) as a unit, resolving scripts relative to install location so it behaves identically on every host. **claude.ai (web)** installs via a downloadable `watch.skill` bundle through Settings → Capabilities → Skills (requires "Code execution and file creation" enabled, since the skill shells out to `ffmpeg`/`yt-dlp`). **Manual/dev** installs by cloning and symlinking `skills/watch` into a host's skills directory. First run triggers a preflight check (`scripts/setup.py --check`) that auto-installs `ffmpeg`/`yt-dlp` via `brew` on macOS (prints exact commands on Linux/Windows) and scaffolds a `~/.config/watch/.env` for Whisper API keys. (../../raw/github/bradautomates-claude-video.md)

## Key features

- **Detail-mode dial** — `transcript` (captions only, no frames, ~4.5s), `efficient` (fast keyframe decode, 50-frame cap, ~0.5s extraction), `balanced` (scene-aware, 100-frame cap, default), `token-burner` (scene-aware, uncapped). Every mode uses the same even-sampling rule (first + last frame always kept) so the last frame always lands at the clip's actual end.
- **Auto-fps frame budgeting** by video duration — from ~30 frames for a ≤30s clip up to a 100-frame cap past 10 minutes, with a "sparse scan" warning printed when a long video is being thinned; `--start`/`--end` targets a specific window with a denser per-second budget instead.
- **Frame deduplication** — a pure-stdlib (no image libraries) mean-absolute-brightness-difference pass against the *last kept* frame (not the previous frame, so it catches slow fades) drops near-identical frames — held slides, static screen recordings — before they reach Claude, spending the frame budget on distinct content.
- **`--timestamps` targeting** — grabs a frame at each timestamp a user or transcript cue names ("look here," "as you can see"), layered on top of the detail-mode frames.
- **Measured cost tables in the README itself** — a real 49-minute-video benchmark reports extraction time and estimated image tokens per detail mode (e.g. `efficient`: ~0.5s, ~9.8k tokens vs `token-burner`: ~21.0s, ~22.8k tokens), computed from Anthropic's `(width × height) / 750` image-token formula.

## Architecture

The skill is a single self-contained unit at `skills/watch/` — `SKILL.md` (the cross-host contract) plus a `scripts/` runtime: `watch.py` (entry point orchestrating download → frames → transcript), `download.py` (yt-dlp wrapper), `frames.py` (ffmpeg extraction + auto-fps logic), `transcribe.py` (VTT parsing, dedup, Whisper orchestration), `whisper.py` (pure-stdlib Groq/OpenAI clients), `config.py` (`~/.config/watch/.env`), and `setup.py` (preflight/installer). Distribution is multi-surface by design: `.claude-plugin/` (Claude Code marketplace), `.codex-plugin/` (Codex manifest), `.agents/plugins/` (Agent Skills marketplace listing), and a generic `AGENTS.md` → `CLAUDE.md` symlink for hosts that auto-load that convention. `hooks/` adds a SessionStart status hook for Claude Code only. Releases are tag-triggered: pushing `vX.Y.Z` runs `.github/workflows/release.yml`, which builds `dist/watch.skill` and attaches it to the GitHub release for the claude.ai web install path. (../../raw/github/bradautomates-claude-video.md)

## Example usage

```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
/watch https://www.tiktok.com/@user/video/123 summarize this
/watch ~/Movies/screen-recording.mp4 when does the UI break?
/watch https://youtu.be/abc --start 2:15 --end 2:45
/watch video.mp4 --detail token-burner --resolution 1024
```
(../../raw/github/bradautomates-claude-video.md)

## Maintenance status

8,256 GitHub stars, 905 forks, MIT licensed, default branch `main`, latest release v0.2.0 (2026-07-01), most recent push 2026-07-01. Test suite is pytest-based using ffmpeg-synthesized clips (no network dependency). Built by Brad Bonanno (content creator on YouTube @bradbonanno; also builds AI operating systems at Solaris Automation). (../../raw/github/bradautomates-claude-video.md)

## Ecosystem

A narrow, single-purpose complement to broader skill catalogs like [[davila7-claude-code-templates]] and distribution layers like [[skills.sh]] (installable the same way, via `npx skills add`) — it solves one specific multimodal gap (Claude can't natively watch video) rather than bundling many capabilities. Pairs conceptually with [[Starmel-OpenSuperWhisper]] on the audio side (both lean on Whisper-family transcription, though OpenSuperWhisper is a standalone dictation app rather than an agent skill). Built entirely on existing open-source tooling (`yt-dlp`, `ffmpeg`) plus Groq/OpenAI Whisper APIs and Claude's own multimodal `Read` — no bespoke video-understanding model.
