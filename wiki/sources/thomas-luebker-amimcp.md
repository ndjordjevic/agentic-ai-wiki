---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/thomas-luebker/amimcp
tags:
  - mcp-server
  - amiga
  - remote-desktop
  - screen-capture
  - semantic-ui-tree
  - arexx
  - stdio-mcp
  - retro-hardware
related:
  - microsoft-playwright-mcp
  - sequentialthinking-mcp
  - INSANE0777-Awwwards-mcp
  - responsively-org-responsively-app
product: amimcp
detail_level: standard
created: 2026-11-09
updated: 2026-11-09
studied: true

---

amimcp (26★, Apache-2.0, C + Python stdlib, amiagent v0.15.0) is an MCP server that gives Claude (or any stdio MCP client) hands on a real Amiga: AmigaDOS shell, files, screenshots, mouse/keyboard, semantic Intuition gadget clicks, menus, and ARexx app scripting over a tiny TCP daemon on the machine.

_All claims below are sourced from ../../raw/github/thomas-luebker-amimcp.md unless otherwise noted._

## What it does

Two halves talk over a framed TCP protocol on port 7846 (optional AmiSSL TLS): **`amimcp`** is a pure-stdlib Python stdio MCP server on the host; **`amiagent`** is an ~85 KB AmigaOS 2.04+ 68000 daemon needing only `bsdsocket.library`. Together they expose shell, filesystem, system info, planar/RTG screen capture, pointer/click/drag/type, a semantic UI tree for Intuition/GadTools gadgets, menu enumeration/selection, and ARexx ports — enough to diagnose, fix, and drive a real Amiga (or a fake_agent sandbox) from an agent session.

## Installation

On the Amiga: unpack `amiagent-0.15.0.lha` from releases (or `amipkg install amiagent`, or cross-compile `agent/` with m68k-amigaos-gcc), start TCP/IP, then `amiagent TOKEN=pickasecret` (or Workbench tool types / `S:User-Startup`). On the host: `./install.sh <amiga-ip> <token>` registers Claude Code, or configure any MCP client to run `python3 server/amimcp.py` with `AMIGA_HOST` / `AMIGA_TOKEN` (optional `AMIGA_TLS=on`). Probe without an LLM via `python3 server/amimcp.py --probe`.

## Key features

- Broad MCP tool surface: shell, read/write/list, system info, screenshot/screens/pointer/region hash, click/drag/type/key/break.
- Semantic GUI layer (`amiga_ui_tree`, `amiga_ui_click`, menus) so agents click by label/role instead of pixels on standard Intuition UIs.
- ARexx scripting both ways: drive Directory Opus/editors/etc., and apps can drive `AMIAGENT` for local input injection.
- Optional TLS via AmiSSL; token-gated plain TCP by default — README stresses LAN-only, never port-forward.
- Companion tools: `amimon`/`amimon-mui` status monitors, `amifleet` macOS fleet console, `amibench` CPU/memory benchmark, `tests/fake_agent.py` for host-side development.

## Architecture

MCP JSON-RPC over stdio → Python `amimcp`/`amiga.py` → framed `"AMI0"` request/response over TCP (one request per connection) → `amiagent` on AmigaOS. Wire format and command codes (`EXEC`, `GET`/`PUT`, `SHOT`, `INPUT`, `UITREE`, `UIACT`, `MENUS`, `AUTH`, …) are documented in `PROTOCOL.md`. Screenshots use native planar capture, CyberGraphX for RTG, or SGrab fallback; input injection must use relative mouse for SDL/games that ignore Intuition pointer warps.

## Example usage

```sh
./install.sh 192.168.1.42 pickasecret
# or
claude mcp add amiga \
  --env AMIGA_HOST=192.168.1.42 \
  --env AMIGA_TOKEN=pickasecret \
  -- python3 /path/to/amimcp/server/amimcp.py
```

Then ask the agent to inspect Kickstart/volumes, fix `Startup-Sequence`, push a cross-compiled binary, or click a Workbench gadget by name. Host-only tests: `python3 tests/fake_agent.py --port 7846 --root /tmp/fakeamiga` then `./run_tests.sh`.

## Maintenance status

26 stars, 2 forks, default branch `master`, latest release `v0.15.0` (2026-11-08), Apache-2.0 (vendored CyberGraphX terms noted in NOTICE). Verified by the author on A4000/060 AmigaOS 3.2.3 with Picasso96; actively pushed as of fetch date.
