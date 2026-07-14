# bradautomates/claude-video

## Metadata
- Stars: 8256
- Primary language: Python
- Default branch: main
- Latest release: v0.2.0 (2026-07-01)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-14
- Final URL: https://github.com/bradautomates/claude-video

## Description
Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude.

## README

# /watch

**Give Claude the ability to watch any video.**

Claude Code (recommended — auto-updates via marketplace):
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

Codex, Cursor, Copilot, Gemini CLI, or any of 50+ Agent Skills hosts:
```bash
npx skills add bradautomates/claude-video -g
```
(`-g` installs globally for your user, available across all projects. Drop it to scope per-project.)

Zero config to start — `yt-dlp` and `ffmpeg` install on first run via `brew` on macOS (Linux/Windows print exact commands). Captions cover most public videos for free. Whisper API key is only needed when a video has no captions.

Claude can read a webpage, run a script, browse a repo. What it can't do, out of the box, is *watch a video*. You paste a YouTube link and it has to either guess from the title or pull a transcript that's missing 90% of what's on screen.

With Claude Video `/watch` you can paste a URL or a local path, ask a question, and Claude fetches captions first, downloads only what it needs, extracts frames (scene-aware, or fast keyframes at `efficient` detail), pulls a timestamped transcript (free captions when available, Whisper API as fallback), and `Read`s every frame as an image. By the time it answers, it has *seen* the video and *heard* the audio.

```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
```

### What people actually use it for

**Analyze someone else's content.** `/watch https://youtu.be/<viral-video> what hook did they open with?` Claude looks at the first frames, reads the opening transcript, breaks down the structure. Same for ad creative, competitor launches, podcast intros, anything where the *how* matters as much as the *what*.

**Diagnose a bug from a video.** Someone sends you a screen recording of something broken. `/watch bug-repro.mov what's going wrong?` Claude watches the recording, finds the frame where the issue appears, describes what's on screen, often catches the cause without you ever opening the file.

**Summarize a video.** `/watch https://youtu.be/<long-thing> summarize this` pulls the structure, the key moments, what was actually said and shown. Faster than watching at 2x.

**Cut the hype out of an update video.** `/watch https://youtu.be/<launch-video> what's actually new — skip the hype` strips a "game-changer" feature drop down to the few things that matter.

**Turn a playlist into notes.** `/watch https://youtu.be/<video> summarize this to a note` — run it across a series and file a per-video summary, so a channel or course becomes a searchable set of notes.

### How it works

1. **You paste a video and a question.** URL (anything yt-dlp supports — YouTube, Loom, TikTok, X, Instagram, plus a few hundred more) or a local path (`.mp4`, `.mov`, `.mkv`, `.webm`).
2. **`yt-dlp` checks captions first.** At `transcript` detail, captioned URLs return without downloading video. Otherwise, or when Whisper needs audio, it downloads only what the run needs.
3. **`ffmpeg` extracts frames at the chosen detail.** `efficient` decodes keyframes only (near-instant); `balanced`/`token-burner` prefer scene-change frames and fall back to the duration-aware uniform sampler when they under-produce. JPEGs are 512px wide by default and clamped to 1998px tall for Claude Read compatibility.
4. **The transcript comes from one of two places.** First try: `yt-dlp` pulls native captions (manual or auto-generated) from the source. Free, instant, accurate-ish. Fallback: extract a mono 16 kHz 64 kbps mp3 audio clip (~480 kB/min) and ship it to Whisper — Groq's `whisper-large-v3` (preferred — cheaper and faster) or OpenAI's `whisper-1`.
5. **Frames + transcript are handed to Claude.** The script prints frame paths with `t=MM:SS` markers and the transcript with timestamps. Claude `Read`s each frame in parallel — JPEGs render directly as images in its context.
6. **Claude answers grounded in what's actually on screen and in the audio.** Not "based on the description" — it saw the frames and heard the transcript.
7. **Cleanup.** The script prints a working directory at the end. If you're not asking follow-ups, Claude removes it.

### Frame budget — why it matters

Token cost is dominated by frames. Every frame is an image; image tokens add up fast. The script's auto-fps logic exists so you don't blow your context budget on a sparse scan of a 30-minute video that would have been better answered by a focused 30-second window.

| Duration | Default frame budget | What you get |
|----------|---------------------|--------------|
| ≤30 s | ~30 frames | Dense — basically every key moment |
| 30 s - 1 min | ~40 frames | Still dense |
| 1 - 3 min | ~60 frames | Comfortable |
| 3 - 10 min | ~80 frames | Sparse but workable |
| > 10 min | 100 frames (capped modes) | "Sparse scan" warning — re-run focused, or `--detail token-burner` for full uncapped coverage |

When the user names a moment ("around 2:30", "the last 30 seconds", "from 0:45 to 1:00"), pass `--start` / `--end`. Focused mode gets denser per-second budgets, capped at 2 fps.

### Frame deduplication

Frame selection can still surface near-identical frames: a screen recording that holds one slide for 90 seconds produces a dozen, each billed as a separate image. A dedup pass drops them before frames reach Claude, running by default on every frame mode (`--no-dedup` turns it off):

1. One `ffmpeg` call scales each extracted JPEG to a 16×16 grayscale thumbnail. Everything after is pure-stdlib Python — no image libraries.
2. For each frame, compute the **mean absolute difference** against the *last frame that was kept* (average per-pixel brightness change, 0–255 scale).
3. If that difference is at or below the threshold (`2.0`), the frame is a near-duplicate and is dropped. Otherwise it's kept and becomes the new reference.
4. The frame-budget cap applies *after* dedup, so the budget is spent on distinct frames.

Comparing against the last *kept* frame (not the previous one) catches slow fades that never trip a frame-to-frame threshold. The **Frames** line reports what was collapsed, e.g. `6 selected from 14 candidates (8 near-duplicates dropped)`.

### Detail modes — measured

The `--detail` dial trades speed and token cost for visual fidelity. Numbers below are from a real run against a **49:08** YouTube video (1280×720, English auto-captions) — a long, mostly-static screen recording. Extraction times are local CPU against a pre-downloaded copy; the one-time download was **~37 s** / 76 MB, shared by the three frame modes.

| Mode | Engine | Frames | Cap | Extraction time | Temporal coverage | Est. image tokens |
|------|--------|--------|-----|-----------------|-------------------|-------------------|
| `transcript` | none (captions) | 0 | — | **~4.5 s** (one yt-dlp call, no download) | full (text) | 0 (≈26.6k text tokens) |
| `efficient` | keyframe (`-skip_frame nokey`) | 50 | 50 | **~0.5 s** | 0:00 → 49:04 (full) | **~9.8k** |
| `balanced` | scene-change | 100 | 100 | **~20.9 s** | 0:00 → 48:38 (full) | **~19.7k** |
| `token-burner` | scene-change | 116 | uncapped | **~21.0 s** | 0:00 → 48:38 (full) | **~22.8k** |

- **Image tokens** use Anthropic's `(width × height) / 750` — at the default 512px width these 720p frames are 512×288, **≈197 tokens/frame**; `--resolution 1024` roughly 4×s that. The transcript is surfaced in every captioned mode and on long videos is often the larger cost.
- **One sampling rule across frame modes.** Each detects all candidates across the full range, then even-samples (first + last always kept) down to its cap. The modes differ only in candidate *source* (keyframes vs. scene cuts) and cap, never in how coverage is spread.
- **`efficient` is the speed tier** (~0.5 s) — it only reconstructs keyframes, so it's ~40× faster than the scene modes, which decode every frame to find cuts. It can also return *more* frames than `balanced` on low-motion footage.
- **`token-burner` only diverges from `balanced` past the cap.** This clip had 116 cuts, so `balanced` sampled 100 and `token-burner` kept all 116.

### Install

| Surface | Install |
|---------|---------|
| **Claude Code** | `/plugin marketplace add bradautomates/claude-video` then `/plugin install watch@claude-video` |
| **Codex, Cursor, Copilot, Gemini CLI, +50 more** | `npx skills add bradautomates/claude-video -g` |
| **claude.ai** (web) | Download `watch.skill` from the latest release → Settings → Capabilities → Skills → `+` |
| **Manual / dev** | `git clone` then symlink `skills/watch` into your host's skills dir |

The [Agent Skills](https://agentskills.io) CLI (`npx skills add bradautomates/claude-video -g`) installs the skill into whatever agents it detects; `-g` installs globally (`~/.codex/skills`, `~/.cursor/skills`, etc.), drop it for per-project. Useful flags: `-a, --agent <names…>` (target specific hosts), `-l, --list`, `--copy` (copy instead of symlink). The CLI discovers the skill from `skills/watch/SKILL.md` and copies the whole folder — `SKILL.md` plus its `scripts/` runtime — as a self-contained unit, resolving scripts relative to wherever it was installed so it works the same on every host.

For claude.ai web: enable "Code execution and file creation" under Capabilities first — the skill shells out to `ffmpeg` and `yt-dlp`.

Manual/dev: `git clone https://github.com/bradautomates/claude-video.git` then `ln -s "$(pwd)/claude-video/skills/watch" ~/.claude/skills/watch`. Build the claude.ai bundle with `bash skills/watch/scripts/build-skill.sh` → `dist/watch.skill`.

### First run

On the first `/watch` call, the skill runs `scripts/setup.py --check`. If `ffmpeg` / `yt-dlp` aren't on PATH, or no Whisper API key is set, it walks through fixing it: macOS auto-runs `brew install ffmpeg yt-dlp`; Linux prints exact `apt`/`dnf`/`pipx` commands; Windows prints `winget`/`pip` commands; it scaffolds `~/.config/watch/.env` (mode `0600`) with placeholders for `GROQ_API_KEY` (preferred) and `OPENAI_API_KEY`. After setup, preflight is a sub-100ms lookup on subsequent runs.

### Bring your own keys

| Capability | What you need | Cost |
|------------|---------------|------|
| Download + native captions | `yt-dlp` + `ffmpeg` | Free |
| Whisper fallback (preferred) | Groq API key — `whisper-large-v3` | Cheap, fast |
| Whisper fallback (alt) | OpenAI API key — `whisper-1` | Standard pricing |
| Disable Whisper entirely | `--no-whisper` | Free, frames-only when no captions |

Whisper fallback only kicks in when a video genuinely has no caption track — typically local files, TikToks, some Vimeos, and the occasional caption-less YouTube upload.

### Usage

```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
/watch https://www.tiktok.com/@user/video/123 summarize this
/watch ~/Movies/screen-recording.mp4 when does the UI break?
/watch https://vimeo.com/123 what tools does she mention?
```

Focused on a specific section:
```
/watch https://youtu.be/abc --start 2:15 --end 2:45
/watch video.mp4 --start 50 --end 60
/watch "$URL" --start 1:12:00            # from 1h12m to end
```

Other flags (passed to `scripts/watch.py`): `--detail transcript|efficient|balanced|token-burner`, `--timestamps T1,T2,…` (grab a frame at each absolute timestamp), `--max-frames N`, `--resolution W` (bump to 1024px for on-screen text), `--fps F` (capped at 2 fps), `--whisper groq|openai`, `--no-whisper`, `--no-dedup`, `--out-dir DIR`.

### Limits

- **Long-video accuracy depends on the detail mode.** On capped modes (`efficient`, default `balanced`), coverage thins out past ~10 minutes — the script prints a "sparse scan" warning; re-run focused with `--start`/`--end`, or use `--detail token-burner` to lift the cap and keep every scene-change frame (at the cost of more image tokens).
- **Detail is one dial.** Defaults: scene-aware frames, 2 fps max, 100-frame cap. `WATCH_DETAIL` in `~/.config/watch/.env` changes the default.

### Structure

```
.
├── skills/watch/                 # self-contained skill — copied as a unit by every installer
│   ├── SKILL.md                  # skill contract — the source of truth across all surfaces
│   └── scripts/
│       ├── watch.py              # entry point — orchestrates download → frames → transcript
│       ├── download.py           # yt-dlp wrapper
│       ├── frames.py             # ffmpeg frame extraction + auto-fps logic
│       ├── transcribe.py         # VTT parsing + dedupe + Whisper orchestration
│       ├── whisper.py            # Groq / OpenAI clients (pure stdlib)
│       ├── config.py             # shared config (~/.config/watch/.env)
│       ├── setup.py              # preflight + installer
│       └── build-skill.sh        # build dist/watch.skill for claude.ai upload (dev-only)
├── hooks/                        # SessionStart status hook (Claude Code only)
├── .claude-plugin/                # plugin.json + marketplace.json (Claude Code)
├── .codex-plugin/                 # plugin.json — Codex/agents manifest ("skills": "./skills/")
├── .agents/plugins/                # marketplace.json — Agent Skills marketplace listing
├── AGENTS.md → CLAUDE.md          # generic-agent entry point
├── tests/                          # pytest suite (ffmpeg-synthesized clips, no network)
└── .github/workflows/               # release.yml — auto-builds watch.skill on tag push
```

### Develop

```bash
python3 -m pytest -q                          # test suite (ffmpeg required for frame tests)
bash skills/watch/scripts/build-skill.sh      # → dist/watch.skill
```

Releasing: tag `vX.Y.Z`, push the tag. The workflow builds `dist/watch.skill` and attaches it to the GitHub release. Keep the version in sync across `skills/watch/SKILL.md`, `.claude-plugin/plugin.json`, and `.codex-plugin/plugin.json`.

### Open source

MIT license. Built on `yt-dlp`, `ffmpeg`, and Claude's multimodal `Read` tool. Whisper transcription via Groq or OpenAI.

Built by Brad Bonanno — content about building with AI on YouTube (@bradbonanno), and AI operating systems for businesses at Solaris Automation.

## Top-level structure

- `skills/watch/` — the self-contained skill: `SKILL.md` (contract, source of truth across all surfaces) plus `scripts/` (`watch.py` entry point, `download.py`, `frames.py`, `transcribe.py`, `whisper.py`, `config.py`, `setup.py`, `build-skill.sh`)
- `hooks/` — SessionStart status hook (Claude Code only)
- `.claude-plugin/` — `plugin.json` + `marketplace.json` for Claude Code plugin distribution
- `.codex-plugin/` — Codex/agents manifest (`"skills": "./skills/"`)
- `.agents/plugins/` — Agent Skills marketplace listing (`marketplace.json`)
- `AGENTS.md` → `CLAUDE.md` — generic-agent entry point
- `tests/` — pytest suite using ffmpeg-synthesized clips, no network required
- `.github/workflows/` — `release.yml`, auto-builds `watch.skill` on tag push
- `CHANGELOG.md`, `LICENSE` (MIT)
