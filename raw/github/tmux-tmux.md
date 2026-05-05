# tmux/tmux

## Metadata
- Stars: 45,066
- Primary language: C
- Default branch: master
- Latest release: 3.6a (about 4 months ago)
- License: ISC License
- Homepage: (none)
- Fetched: 2026-05-02
- Final URL: https://github.com/tmux/tmux

## Description
tmux source code — a terminal multiplexer that enables multiple terminals to be created, accessed, and controlled from a single screen.

## README
# Welcome to tmux!

tmux is a terminal multiplexer: it enables a number of terminals to be created,
accessed, and controlled from a single screen. tmux may be detached from a
screen and continue running in the background, then later reattached.

This release runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS and Solaris.

### Dependencies

tmux depends on [libevent](https://libevent.org) 2.x, available from [this
page](https://github.com/libevent/libevent/releases/latest).

It also depends on [ncurses](https://www.gnu.org/software/ncurses/), available
from [this page](https://invisible-mirror.net/archives/ncurses/).

To build tmux, a C compiler (for example gcc or clang), make, pkg-config and a
suitable yacc (yacc or bison) are needed.

### Installation

#### Binary packages

Some platforms provide binary packages for tmux, although these are sometimes
out of date. Examples are listed on
[this page](https://github.com/tmux/tmux/wiki/Installing).

#### From release tarball

To build and install tmux from a release tarball, use:

```bash
./configure && make
sudo make install
```

tmux can use the utempter library to update utmp(5), if it is installed - run
configure with `--enable-utempter` to enable this.

#### From version control

To get and build the latest from version control - note that this requires
`autoconf`, `automake` and `pkg-config`:

```bash
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure && make
```

### Contributing

Bug reports, feature suggestions and especially code contributions are most
welcome. Please send by email to:

tmux-users@googlegroups.com

Or open a GitHub issue or pull request. Please read CONTRIBUTING.md before opening an issue.

There is [a list of suggestions for contributions](https://github.com/tmux/tmux/wiki/Contributing).

### Documentation

For documentation on using tmux, see the tmux.1 manpage. View it from the
source tree with:

```bash
nroff -mdoc tmux.1|less
```

A small example configuration is in `example_tmux.conf`.

For debugging, run tmux with `-v` or `-vv` to generate server and client log
files in the current directory.

### Support

The tmux mailing list for general discussion and bug reports is:

https://groups.google.com/forum/#!forum/tmux-users

## Top-level structure
- `.github/` — CI workflows and issue templates
- `compat/` — platform compatibility headers and OS-specific shims
- `fuzz/` — fuzz testing harnesses
- `logo/` — project logos
- `presentations/` — conference slide decks
- `regress/` — regression test suite
- `tools/` — build and helper scripts
- `tmux.c` — main entry point
- `server.c` / `server-client.c` / `server-fn.c` / `server-acl.c` — server process and client handling
- `client.c` — client process
- `cmd-*.c` — ~50 individual command implementations (new-session, new-window, split-window, select-pane, send-keys, copy-mode, etc.)
- `window-*.c` — window mode implementations (copy, tree, buffer, client, clock, customize)
- `tty-*.c` — terminal type detection, key handling, drawing
- `osdep-*.c` — OS-specific code for Linux, macOS, OpenBSD, FreeBSD, NetBSD, Solaris, Cygwin, AIX, Haiku
- `format.c` / `format-draw.c` — format string evaluation for status lines
- `grid.c` / `grid-view.c` / `grid-reader.c` — terminal grid model
- `input.c` / `input-keys.c` — VT input parsing
- `options-table.c` / `options.c` — configuration options system
- `key-bindings.c` / `key-string.c` — key binding system
- `paste.c` — paste buffers
- `popup.c` — popup window support
- `status.c` — status bar rendering
- `style.c` — colour and attribute styles
- `tmux.h` — main header file
- `tmux.1` — man page (authoritative documentation)
- `example_tmux.conf` — example configuration
- `CHANGES` — changelog
