---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/karpathy/llm-council
tags:
  - llm-ensemble
  - openrouter-orchestration
  - multi-model-ranking
  - llm-evaluation
  - fastapi-react
  - local-webapp
  - vibe-coding
related:
  - openrouter.ai
  - uditakhourii-adhd
product: llm-council
detail_level: standard
created: 2026-07-20
updated: 2026-07-28
---

LLM Council is Andrej Karpathy's local, two-tier web app for "ensembling" frontier models on a single prompt: it fans out a question to multiple LLMs via OpenRouter, runs a second-pass peer review where each model ranks anonymized answers, and then has a designated chairman model synthesize the final response. It is intentionally positioned as a non-production Saturday hack ("99% vibe coded"), but it is a practical reference implementation for multi-model adjudication loops and side-by-side answer inspection.

_All claims below are sourced from ../../raw/github/karpathy-llm-council.md unless otherwise noted._

## What it does

The app behaves like a local ChatGPT-style interface backed by a three-stage "council" pipeline instead of a single model call. In Stage 1, each configured model independently answers the user's query. In Stage 2, each model receives the other models' outputs with identities anonymized and ranks them for accuracy and insight. In Stage 3, a chairman model consolidates all responses and review signals into one final answer, while the UI still exposes per-model answers in tab form for manual inspection.

## Installation

The repository uses `uv` for Python dependencies and npm for the frontend:

```bash
uv sync
cd frontend
npm install
cd ..
```

Then set `OPENROUTER_API_KEY` in a root `.env` file and run either `./start.sh` or backend/frontend in separate terminals.

## Key features

- **Three-stage council loop**: first opinions, anonymized peer review, chairman synthesis.
- **Multi-model panel**: configurable council model list plus a separately configurable chairman model in `backend/config.py`.
- **OpenRouter-based federation**: one API integration path fans out to multiple providers/models.
- **Inspectable deliberation**: model-specific responses are retained for comparison instead of returning only the merged answer.
- **Simple local persistence**: conversations are stored as JSON under `data/conversations/`.
- **Agent-ready repo instructions**: a top-level `CLAUDE.md` defines contributor workflow guardrails for coding-agent iteration.

## Architecture

The backend is a Python FastAPI service split across `backend/main.py` (HTTP API), `backend/council.py` (multi-stage council orchestration/ranking), `backend/openrouter.py` (provider API wrapper), `backend/config.py` (model roster/chairman settings), and `backend/storage.py` (conversation persistence). The frontend is a React + Vite app under `frontend/` that presents chat UX and per-model tabbed outputs. `start.sh` coordinates local startup of both tiers for development.

## Example usage

```bash
./start.sh
```

After startup, open `http://localhost:5173`, ask a question, and inspect each model's Stage 1 output before reading the chairman's final synthesis.

## Maintenance status

22,918 stars and 4,128 forks, last pushed 2025-11-22, no tagged release, and no detected license metadata via GitHub API. The README explicitly frames the project as unsupported and provided "as is," so it is best treated as a reference pattern for model-council orchestration rather than a maintained framework.
