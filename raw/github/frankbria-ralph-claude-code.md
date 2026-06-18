# frankbria/ralph-claude-code

## Metadata
- Stars: 9,380
- Forks: 720
- Primary language: Shell
- Default branch: main
- Latest release: none (v0.11.5 in README/badges, no formal release tags)
- License: MIT
- Homepage: (none)
- Fetched: 2026-06-18
- Final URL: https://github.com/frankbria/ralph-claude-code

## Description
Autonomous AI development loop for Claude Code with intelligent exit detection

## README

# Ralph for Claude Code

> **Autonomous AI development loop with intelligent exit detection and rate limiting**

Ralph is an implementation of the Geoffrey Huntley's technique for Claude Code that enables continuous autonomous development cycles he named after Ralph Wiggum. It enables continuous autonomous development cycles where Claude Code iteratively improves your project until completion, with built-in safeguards to prevent infinite loops and API overuse.

**Install once, use everywhere** - Ralph becomes a global command available in any directory.

## Project Status

**Version**: v0.11.5 - Active Development
**Core Features**: Working and tested
**Test Coverage**: 784 tests, 100% pass rate

### What's Working Now
- Autonomous development loops with intelligent exit detection
- **Dual-condition exit gate**: Requires BOTH completion indicators AND explicit EXIT_SIGNAL
- Rate limiting with hourly reset (100 calls/hour, configurable)
- Circuit breaker with advanced error detection (prevents runaway loops)
- Response analyzer with semantic understanding and two-stage error filtering
- **JSON output format support with automatic fallback to text parsing**
- **Session continuity with `--resume` flag for context preservation (no session hijacking)**
- **Session expiration with configurable timeout (default: 24 hours)**
- **Modern CLI flags: `--output-format`, `--allowed-tools`, `--no-continue`**
- **Interactive project enablement with `ralph-enable` wizard**
- **`.ralphrc` configuration file for project settings**
- **Live streaming output with `--live` flag for real-time Claude Code visibility**
- **Log rotation: `ralph.log` rotates at 10MB, keeping 4 archived files**
- **Dry-run mode (`--dry-run`) to simulate loops without API calls**
- **Metrics tracking with `ralph-stats` analytics command (JSON Lines per-loop metrics)**
- **Desktop notifications (`--notify`) for key loop events (macOS/Linux/terminal-bell)**
- **Automatic git backup branches (`--backup`) with `--rollback` restore**
- Multi-line error matching for accurate stuck loop detection
- 5-hour API limit handling with user prompts
- tmux integration for live monitoring
- PRD import functionality
- **GitHub issue import: `ralph-import --github-issue` plus metadata filters**
- **CI/CD pipeline with GitHub Actions**
- **Dedicated uninstall script for clean removal**

### In Progress
- Expanding test coverage
- [Multi-provider agent abstraction](docs/adr/0001-multi-provider-agent-abstraction.md) — decoupling Ralph from `claude` so any headless coding CLI (Codex, Gemini, OpenCode, Droid, Kilocode, Copilot) can drive the loop

## Features

- **Autonomous Development Loop** - Continuously executes Claude Code with your project requirements
- **Intelligent Exit Detection** - Dual-condition check requiring BOTH completion indicators AND explicit EXIT_SIGNAL
- **Session Continuity** - Preserves context across loop iterations with automatic session management
- **Session Expiration** - Configurable timeout (default: 24 hours) with automatic session reset
- **Rate Limiting** - Built-in API call management with hourly limits and countdown timers
- **5-Hour API Limit Handling** - Three-layer detection (timeout guard, JSON parsing, filtered text) with auto-wait for unattended mode
- **Live Monitoring** - Real-time dashboard showing loop status, progress, and logs
- **Task Management** - Structured approach with prioritized task lists and progress tracking
- **Project Templates** - Quick setup for new projects with best-practice structure
- **Interactive Project Setup** - `ralph-enable` wizard for existing projects with task import
- **Configuration Files** - `.ralphrc` for project-specific settings and tool permissions
- **Comprehensive Logging** - Detailed execution logs with timestamps and status tracking
- **Configurable Timeouts** - Set execution timeout for Claude Code operations (1-120 minutes)
- **Verbose Progress Mode** - Optional detailed progress updates during execution
- **Response Analyzer** - AI-powered analysis of Claude Code responses with semantic understanding
- **Circuit Breaker** - Advanced error detection with two-stage filtering, multi-line error matching, and automatic recovery
- **CI/CD Integration** - GitHub Actions workflow with automated testing
- **Clean Uninstall** - Dedicated uninstall script for complete removal
- **Live Streaming Output** - Real-time visibility into Claude Code execution with `--live` flag
- **Docker Sandbox Execution** - Run Claude Code in an isolated container with `--sandbox docker`
- **E2B Cloud Sandbox Execution** - Run Claude Code in an E2B cloud sandbox with `--sandbox e2b`

## Quick Start

Two phases: **one-time installation** and **per-project setup**.

### Phase 1: Install Ralph (One Time Only)

```bash
git clone https://github.com/frankbria/ralph-claude-code.git
cd ralph-claude-code
./install.sh
```

Adds `ralph`, `ralph-monitor`, `ralph-setup`, `ralph-import`, `ralph-queue`, `ralph-migrate`, `ralph-enable`, and `ralph-enable-ci` to PATH.

### Phase 2: Initialize Projects (Per Project)

**Option A: Enable Ralph in Existing Project (Recommended)**
```bash
cd my-existing-project
ralph-enable
ralph --monitor
```

**Option B: Import Existing PRD/Specifications**
```bash
ralph-import my-requirements.md my-project
cd my-project
ralph --monitor
```

**Option C: Create New Project from Scratch**
```bash
ralph-setup my-awesome-project
cd my-awesome-project
# Edit .ralph/PROMPT.md and .ralph/fix_plan.md
ralph --monitor
```

## Understanding Ralph Files

| File | Auto-Generated? | You Should... |
|------|-----------------|---------------|
| `.ralph/PROMPT.md` | Yes (smart defaults) | **Review & customize** project goals and principles |
| `.ralph/fix_plan.md` | Yes (can import tasks) | **Add/modify** specific implementation tasks |
| `.ralph/AGENT.md` | Yes (detects build commands) | Rarely edit (auto-maintained by Ralph) |
| `.ralph/specs/` | Empty directory | Add files when PROMPT.md isn't detailed enough |
| `.ralphrc` | Yes (project-aware) | Rarely edit (sensible defaults) |

## How It Works

Ralph operates on a simple but powerful cycle:

1. **Read Instructions** - Loads `PROMPT.md` with your project requirements
2. **Execute Claude Code** - Runs Claude Code with current context and priorities
3. **Track Progress** - Updates task lists and logs execution results
4. **Evaluate Completion** - Checks for exit conditions and project completion signals
5. **Repeat** - Continues until project is complete or limits are reached

### Intelligent Exit Detection

Ralph uses a **dual-condition check** to prevent premature exits:

**Exit requires BOTH conditions:**
1. `completion_indicators >= 2` (heuristic detection from natural language patterns)
2. Claude's explicit `EXIT_SIGNAL: true` in the RALPH_STATUS block

| completion_indicators | EXIT_SIGNAL | Result |
|-----------------------|-------------|--------|
| >= 2 | `true` | **Exit** ("project_complete") |
| >= 2 | `false` | **Continue** (Claude still working) |
| >= 2 | missing | **Continue** (defaults to false) |
| < 2 | `true` | **Continue** (threshold not met) |

**Other exit conditions:**
- All tasks in `.ralph/fix_plan.md` marked complete
- Multiple consecutive "done" signals from Claude Code
- Too many test-focused loops (indicating feature completeness)
- Claude API 5-hour usage limit reached

### Optional Sections in fix_plan.md

Put low-priority items under `## Optional`, `## Future`, `## Future Enhancements`, or `## Nice to Have` headings — these do not block exit:

```markdown
## High Priority
- [x] Core feature

## Optional
- [ ] Frontend integration   # does NOT block exit
```

## Configuration

### .ralphrc Settings

```bash
PROJECT_NAME="my-project"
PROJECT_TYPE="typescript"
MAX_CALLS_PER_HOUR=100
CLAUDE_TIMEOUT_MINUTES=15
CLAUDE_OUTPUT_FORMAT="json"
ALLOWED_TOOLS="Write,Read,Edit,Bash(git *),Bash(npm *),Bash(pytest)"
SESSION_CONTINUITY=true
SESSION_EXPIRY_HOURS=24
CB_NO_PROGRESS_THRESHOLD=3
CB_SAME_ERROR_THRESHOLD=5
```

### Rate Limiting & Circuit Breaker

- Default: 100 calls per hour, 0 tokens/hour (disabled)
- Circuit breaker opens after 3 loops with no progress or 5 loops with same errors
- Auto-recovers after 30-minute cooldown (OPEN → HALF_OPEN → CLOSED)

### Docker Sandbox

```bash
ralph --sandbox docker                          # Default image, 4g RAM, 2 CPUs, bridge network
ralph --sandbox docker --sandbox-memory 8g --sandbox-cpus 4
ralph --sandbox docker --sandbox-network none   # Full network isolation
```

### E2B Cloud Sandbox

```bash
pip install e2b
export E2B_API_KEY="e2b_..."
ralph --sandbox e2b
ralph --sandbox e2b --sandbox-max-cost 5.00
```

## Importing from GitHub Issues

```bash
# Import a specific issue by number
ralph-import --github-issue 42

# Import the oldest open issue matching a search
ralph-import --github-search "fix login timeout"

# Import with metadata filters
ralph-import --github-label "sprint-1" --github-assignee @me --select interactive

# Dry-run preview
ralph-import --github-label bug --dry-run
```

**Completeness assessment**: Ralph scores issues 0–100 for implementation readiness. Issues below 60 get an implementation plan generated by Claude Code before conversion.

## GitHub Issue Lifecycle

```bash
# Post progress comments every 5 loops, close on completion, create PR
ralph --github-issue 69 --comment-progress --create-pr --link-issue --auto-close

# Open PR as draft for manual review
ralph --github-issue 69 --create-pr --draft-pr
```

## Batch Processing

```bash
ralph-queue add --github-label "bug,P0"
ralph-queue add --github-milestone "v1.0"
ralph-queue status
ralph --process-queue
ralph --resume-queue
```

## CLI Reference

```bash
ralph [OPTIONS]
  -c, --calls NUM         Set max calls per hour (default: 100)
  -p, --prompt FILE       Set prompt file (default: .ralph/PROMPT.md)
  -s, --status            Show current status and exit
  -m, --monitor           Start with tmux session and live monitor
  -v, --verbose           Show detailed progress updates
  -l, --live              Enable live streaming output
  -t, --timeout MIN       Set execution timeout (1-120, default: 15)
  --dry-run               Simulate without API calls
  -n, --notify            Desktop notifications for key events
  -b, --backup            Git backup branch before each loop
  --rollback [BRANCH]     Roll back to a backup branch
  --output-format FORMAT  json (default) or text
  --allowed-tools TOOLS   Set allowed Claude tools
  --no-continue           Disable session continuity
  --reset-circuit         Reset the circuit breaker
  --auto-reset-circuit    Auto-reset circuit breaker on startup
  --process-queue         Process pending queued issues sequentially
  --resume-queue          Resume processing the remaining pending issues
  --sandbox PROVIDER      docker | e2b
  --sandbox-memory SIZE   Docker memory limit (default: 4g)
  --sandbox-cpus N        Docker CPU limit (default: 2)
  --sandbox-max-cost USD  E2B cost cap
```

## System Requirements

- **Bash 4.0+**
- **Claude Code CLI** — `npm install -g @anthropic-ai/claude-code`
- **tmux** — for integrated monitoring
- **jq** — JSON processing
- **Git** — version control
- **GNU coreutils** — `timeout` command (macOS: `brew install coreutils`)

## Testing

```bash
npm install -g bats bats-support bats-assert
npm test            # 771 unit + integration tests
npm run test:e2e    # 13 E2E tests (full ralph_loop.sh subprocess runs)
```

**784 tests across 34 test files**, 100% pass rate.

## Docs

### Top-level Docs (`docs/`)
- `CLI_OPTIONS.md` — full CLI flags reference
- `DOCKER_SANDBOX.md` — Docker sandbox guide
- `E2B_SANDBOX.md` — E2B cloud sandbox guide
- `QUEUE_MANAGEMENT.md` — batch queue management guide
- `SANDBOX_SYNC.md` — file sync filtering

### ADRs (`docs/adr/`)
- `0001-multi-provider-agent-abstraction.md` — planned abstraction to decouple Ralph from `claude` CLI
- `0002-agent-adapter-contract.md` — agent adapter contract design

### User Guide (`docs/user-guide/`)
- `01-quick-start.md`
- `02-understanding-ralph-files.md`
- `03-writing-requirements.md`

## Top-level structure

```
frankbria/ralph-claude-code/
├── .github/          # CI/CD (GitHub Actions test workflow)
├── CLAUDE.md         # Claude Code agent instructions for Ralph projects
├── CONTRIBUTING.md   # Contributor guide (100% test pass rate required)
├── Dockerfile        # Docker sandbox image definition
├── IMPLEMENTATION_PLAN.md    # Roadmap to v1.0
├── IMPLEMENTATION_STATUS.md  # Detailed progress tracking
├── LICENSE           # MIT
├── README.md         # Comprehensive user guide (primary source)
├── SPECIFICATION_WORKSHOP.md
├── TESTING.md        # Per-suite test breakdown
├── create_files.sh   # File creation helper
├── docs/             # CLI reference, ADRs, sandbox guides, user guide
├── examples/         # rest-api/, simple-cli-tool/ (example project configs)
├── install.sh        # Global installation script
├── lib/              # Shared library components (enable_core.sh, wizard_utils.sh, task_sources.sh)
├── logs/             # Runtime logs (gitignored)
├── migrate_to_ralph_folder.sh  # Migration helper for .ralph/ subfolder transition
├── package.json      # npm scripts for BATS test runner
├── ralph-stats.sh    # Metrics analytics command
├── ralph_enable.sh   # Interactive wizard for existing projects
├── ralph_enable_ci.sh # Non-interactive CI version
├── ralph_import.sh   # PRD/GitHub issue import
├── ralph_loop.sh     # Core autonomous loop (main entrypoint)
├── ralph_monitor.sh  # Live monitoring dashboard
├── ralph_queue.sh    # Batch queue management
├── sample-prd.md     # Example PRD document
├── setup.sh          # Per-project setup
├── specs/            # Project specifications
├── src/              # Source code
├── templates/        # Project templates
├── tests/            # 34 test files: unit/, integration/, e2e/, test_error_detection.sh
├── tools/            # Developer tooling
└── uninstall.sh      # Clean removal script
```

Key agent instruction files: `CLAUDE.md` (project-level Claude Code instructions), no top-level `AGENTS.md` (each Ralph project generates its own `.ralph/AGENT.md`).
