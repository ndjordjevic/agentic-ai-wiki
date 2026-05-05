# shareAI-lab/learn-claude-code

## Metadata
- Stars: 58143
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://learn.shareai.run
- Fetched: 2026-05-05
- Final URL: https://github.com/shareAI-lab/learn-claude-code

## Description
Bash is all you need — A nano claude code–like "agent harness", built from 0 to 1

## README
[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)
# Learn Claude Code -- Harness Engineering for Real Agents

## Agency Comes from the Model. An Agent Product = Model + Harness.

Before we talk about code, let's get one thing straight.

**Agency -- the ability to perceive, reason, and act -- comes from model training, not from external code orchestration.** But a working agent product needs both the model and the harness. The model is the driver, the harness is the vehicle. This repo teaches you how to build the vehicle.

### Where Agency Comes From

At the core of every agent is a neural network -- a Transformer, an RNN, a learned function -- that has been trained, through billions of gradient updates on action-sequence data, to perceive an environment, reason about goals, and take actions. Agency is never granted by the surrounding code. It is learned by the model during training.

Humans are the best example. A biological neural network shaped by millions of years of evolutionary training, perceiving the world through senses, reasoning through a brain, acting through a body. When DeepMind, OpenAI, or Anthropic say "agent," the core of what they mean is always the same thing: **a model that has learned to act, plus the infrastructure that lets it operate in a specific environment.**

### The Mind Shift: From "Developing Agents" to Developing Harness

When someone says "I'm developing an agent," they can only mean one of two things:

**1. Training the model.** Adjusting weights through reinforcement learning, fine-tuning, RLHF, or other gradient-based methods.

**2. Building the harness.** Writing the code that gives the model an environment to operate in. This is what most of us do, and it is the focus of this repository.

A harness is everything the agent needs to function in a specific domain:

```
Harness = Tools + Knowledge + Observation + Action Interfaces + Permissions

    Tools:          file I/O, shell, network, database, browser
    Knowledge:      product docs, domain references, API specs, style guides
    Observation:    git diff, error logs, browser state, sensor data
    Action:         CLI commands, API calls, UI interactions
    Permissions:    sandboxing, approval workflows, trust boundaries
```

The model decides. The harness executes. The model reasons. The harness provides context. The model is the driver. The harness is the vehicle.

### What Harness Engineers Actually Do

- **Implement tools.** Give the agent hands. File read/write, shell execution, API calls, browser control, database queries.
- **Curate knowledge.** Give the agent domain expertise. Product documentation, architectural decision records, style guides, regulatory requirements. Load them on-demand (s05), not upfront.
- **Manage context.** Give the agent clean memory. Subagent isolation (s04) prevents noise from leaking. Context compression (s06) prevents history from overwhelming. Task systems (s07) persist goals beyond any single conversation.
- **Control permissions.** Give the agent boundaries. Sandbox file access. Require approval for destructive operations. Enforce trust boundaries between the agent and external systems.
- **Collect task-process data.** Every action sequence the agent executes in your harness is training signal.

### Why Claude Code -- A Masterclass in Harness Engineering

Claude Code is the most elegant and fully-realized agent harness we have seen. Not because of any single clever trick, but because of what it *doesn't* do: it doesn't try to be the agent. It doesn't impose rigid workflows. It doesn't second-guess the model with elaborate decision trees. It provides the model with tools, knowledge, context management, and permission boundaries -- then gets out of the way.

```
Claude Code = one agent loop
            + tools (bash, read, write, edit, glob, grep, browser...)
            + on-demand skill loading
            + context compression
            + subagent spawning
            + task system with dependency graph
            + team coordination with async mailboxes
            + worktree isolation for parallel execution
            + permission governance
```

**12 progressive sessions, from a simple loop to isolated autonomous execution.**
**Each session adds one harness mechanism. Each mechanism has one motto.**

> **s01** "One loop & Bash is all you need" — one tool + one loop = an agent
> **s02** "Adding a tool means adding one handler" — the loop stays the same; new tools register into the dispatch map
> **s03** "An agent without a plan drifts" — list the steps first, then execute; completion doubles
> **s04** "Break big tasks down; each subtask gets a clean context" — subagents use independent messages[], keeping the main conversation clean
> **s05** "Load knowledge when you need it, not upfront" — inject via tool_result, not the system prompt
> **s06** "Context will fill up; you need a way to make room" — three-layer compression strategy for infinite sessions
> **s07** "Break big goals into small tasks, order them, persist to disk" — a file-based task graph with dependencies, laying the foundation for multi-agent collaboration
> **s08** "Run slow operations in the background; the agent keeps thinking" — daemon threads run commands, inject notifications on completion
> **s09** "When the task is too big for one, delegate to teammates" — persistent teammates + async mailboxes
> **s10** "Teammates need shared communication rules" — one request-response pattern drives all negotiation
> **s11** "Teammates scan the board and claim tasks themselves" — no need for the lead to assign each one
> **s12** "Each works in its own directory, no interference" — tasks manage goals, worktrees manage directories, bound by ID

## The Core Pattern

```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS,
        )
        messages.append({"role": "assistant",
                         "content": response.content})

        if response.stop_reason != "tool_use":
            return

        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = TOOL_HANDLERS[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": results})
```

## Quick Start

```sh
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env   # Edit .env with your ANTHROPIC_API_KEY

python agents/s01_agent_loop.py       # Start here
python agents/s12_worktree_task_isolation.py  # Full progression endpoint
python agents/s_full.py               # Capstone: all mechanisms combined
```

### Web Platform

Interactive visualizations, step-through diagrams, source viewer, and documentation.

```sh
cd web && npm install && npm run dev   # http://localhost:3000
```

## Architecture

```
learn-claude-code/
|
|-- agents/                        # Python reference implementations (s01-s12 + s_full capstone)
|-- docs/{en,zh,ja}/               # Mental-model-first documentation (3 languages)
|-- web/                           # Interactive learning platform (Next.js)
|-- skills/                        # Skill files for s05
+-- .github/workflows/ci.yml      # CI: typecheck + build
```

## What's Next

### Kode Agent CLI -- Open-Source Coding Agent CLI

> `npm i -g @shareai-lab/kode`

Skill & LSP support, Windows-ready, pluggable with GLM / MiniMax / DeepSeek and other open models.

GitHub: **[shareAI-lab/Kode-cli](https://github.com/shareAI-lab/Kode-cli)**

### Kode Agent SDK

A standalone library with no per-user process overhead, embeddable in backends, browser extensions, embedded devices, or any runtime.

GitHub: **[shareAI-lab/Kode-agent-sdk](https://github.com/shareAI-lab/Kode-agent-sdk)**

## Sister Repo: claw0

[claw0](https://github.com/shareAI-lab/claw0) deconstructs the "always-on" harness:
- **Heartbeat** — every 30s the harness sends the agent a message to check if there is anything to do.
- **Cron** — the agent can schedule its own future tasks, executed automatically when the time comes.

```
learn-claude-code                   claw0
(agent harness core:                (proactive always-on harness:
 loop, tools, planning,              heartbeat, cron, IM channels,
 teams, worktree isolation)          memory, soul personality)
```

## Docs

### docs/en/s01-the-agent-loop.md
# s01: The Agent Loop

> *"One loop & Bash is all you need"* -- one tool + one loop = an agent.
> **Harness layer**: The loop -- the model's first connection to the real world.

**Problem:** A language model can reason about code, but it can't *touch* the real world -- can't read files, run tests, or check errors. Without a loop, every tool call requires you to manually copy-paste results back.

**Solution:** One exit condition controls the entire flow. The loop runs until the model stops calling tools (`stop_reason != "tool_use"`).

```python
def agent_loop(query):
    messages = [{"role": "user", "content": query}]
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM, messages=messages,
            tools=TOOLS, max_tokens=8000,
        )
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason != "tool_use":
            return
        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = run_bash(block.input["command"])
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": results})
```

That's the entire agent in under 30 lines. Everything else in this course layers on top -- without changing the loop.

### docs/en/s05-skill-loading.md
# s05: Skills

> *"Load knowledge when you need it, not upfront"* -- inject via tool_result, not the system prompt.
> **Harness layer**: On-demand knowledge -- domain expertise, loaded when the model asks.

**Problem:** Putting everything in the system prompt wastes tokens on unused skills. 10 skills at 2000 tokens each = 20,000 tokens, most of which are irrelevant to any given task.

**Solution:**
- Layer 1: skill *names* in system prompt (~100 tokens/skill)
- Layer 2: full *body* via tool_result (on demand, ~2000 tokens)

Each skill is a directory containing a `SKILL.md` with YAML frontmatter. `SkillLoader` scans for `SKILL.md` files. The model learns what skills exist (cheap) and loads them when relevant (expensive).

### docs/en/s07-task-system.md
# s07: Task System

> *"Break big goals into small tasks, order them, persist to disk"* -- a file-based task graph with dependencies.
> **Harness layer**: Persistent tasks -- goals that outlive any single conversation.

**Problem:** s03's TodoManager is a flat checklist in memory: no ordering, no dependencies, no status beyond done-or-not. Real goals have structure — task B depends on task A, tasks C and D can run in parallel.

**Solution:** A file-based task graph (`.tasks/task_N.json`) with `pending` / `in_progress` / `completed` statuses and `blockedBy` dependency edges. Completing a task automatically unblocks dependents by clearing their `blockedBy` list.

```
.tasks/
  task_1.json  {"id":1, "status":"completed"}
  task_2.json  {"id":2, "blockedBy":[1], "status":"pending"}
  task_3.json  {"id":3, "blockedBy":[1], "status":"pending"}
  task_4.json  {"id":4, "blockedBy":[2,3], "status":"pending"}
```

### docs/en/s09-agent-teams.md
# s09: Agent Teams

> *"When the task is too big for one, delegate to teammates"* -- persistent teammates + async mailboxes.
> **Harness layer**: Team mailboxes -- multiple models, coordinated through files.

**Problem:** Subagents (s04) are disposable: spawn, work, return summary, die. Real teamwork needs persistent agents with identity and a communication channel between agents.

**Solution:**
- `TeammateManager` maintains a `config.json` team roster; `spawn()` starts each agent's loop in a thread
- `MessageBus` uses append-only JSONL inboxes: `send()` appends a JSON line; `read_inbox()` reads all and drains
- Each teammate checks its inbox before every LLM call, injecting received messages into context

```
.team/
    config.json           <- team roster + statuses
    inbox/
      alice.jsonl         <- append-only, drain-on-read
      bob.jsonl
      lead.jsonl
```

## Top-level structure

```
learn-claude-code/
├── .env.example          — environment variables template (ANTHROPIC_API_KEY)
├── .github/              — CI workflows (typecheck + build)
├── .gitignore
├── LICENSE               — MIT
├── README.md             — English README (main)
├── README-zh.md          — Chinese README
├── README-ja.md          — Japanese README
├── agents/               — Python reference implementations
│   ├── s01_agent_loop.py      — minimal loop + bash tool
│   ├── s02_tool_use.py        — dispatch map, multiple tools
│   ├── s03_todo_write.py      — in-memory TodoManager
│   ├── s04_subagent.py        — independent messages[] per subagent
│   ├── s05_skill_loading.py   — SKILL.md two-layer loading
│   ├── s06_context_compact.py — three-layer context compression
│   ├── s07_task_system.py     — file-based task graph with deps
│   ├── s08_background_tasks.py— daemon threads + notify queue
│   ├── s09_agent_teams.py     — persistent teammates + JSONL mailboxes
│   ├── s10_team_protocols.py  — request-response FSM
│   ├── s11_autonomous_agents.py— idle cycle + auto-claim
│   ├── s12_worktree_task_isolation.py — worktree + task coordination
│   └── s_full.py              — capstone: all mechanisms combined
├── docs/
│   ├── en/               — English docs (s01-s12, one .md per session)
│   ├── zh/               — Chinese docs
│   └── ja/               — Japanese docs
├── requirements.txt      — Python dependencies (anthropic SDK etc.)
├── skills/               — SKILL.md files for s05 skill loading demo
├── tests/                — test suite
└── web/                  — Next.js interactive learning platform
```
