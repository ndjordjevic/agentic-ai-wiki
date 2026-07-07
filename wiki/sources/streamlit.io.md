---
type: source
source_url: https://streamlit.io/
companion_urls:
  - https://github.com/streamlit/streamlit
raw_files:
  - ../../raw/web/streamlit.io.md
  - ../../raw/github/streamlit-streamlit.md
tags:
  - python-framework
  - data-apps
  - interactive-dashboards
  - llm-chat-ui
  - session-state
  - community-cloud
  - client-server
  - open-source
related:
  - render.com
  - huggingface.co
  - pydantic.dev
  - retool.com
  - lovable.dev
product: streamlit
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

Streamlit is an open-source Python framework (45K+ GitHub stars, Apache 2.0, owned by Snowflake) for turning data scripts into interactive web apps in minutes — dashboards, reports, and LLM chat UIs without HTML/CSS/JS. Its scripting model reruns the top-level script on every widget interaction, with Session State, caching (`st.cache_data` / `st.cache_resource`), forms, fragments, and multipage navigation handling state and performance. Deploy via free **Community Cloud** (GitHub-connected, one-click) or **Streamlit in Snowflake** for enterprise. For agentic workflows it is a common choice for rapid agent/LLM demo UIs and internal tools — compare full-stack app builders [[lovable.dev]], enterprise internal-app platforms [[retool.com]], and PaaS deploy targets like [[render.com]] that explicitly support Streamlit hosting.

_All claims below are sourced from ../../raw/web/streamlit.io.md unless otherwise noted._

## What it does

Streamlit transforms Python scripts into shareable browser apps. Install with `pip install streamlit`, run `streamlit hello` to verify, then `streamlit run your_app.py` to serve locally. The API is declarative: widgets like `st.slider`, `st.text_input`, and `st.button` map directly to Python variables; `st.write` and "magic" syntax display dataframes, charts, and markdown without explicit render calls. The framework targets data scientists and AI/ML engineers who need interactive prototypes and production demos without front-end engineering.

## Key features

- **Scripting-first development** — Apps are plain `.py` files; saving triggers live reload during development
- **Rich widget and display library** — DataFrames, charts (Altair, Plotly, Matplotlib, Vega-Lite, PyDeck maps), chat UI (`st.chat_message`, `st.chat_input`, `st.write_stream` for LLM token streaming), layout primitives (`st.columns`, `st.tabs`, `st.expander`, `st.fragment` for partial reruns)
- **Session State and forms** — Per-session state across reruns; `st.form` batches widget input to prevent rerun storms; callbacks via `on_change`/`on_click`
- **Caching** — `@st.cache_data` for serializable computation results; `@st.cache_resource` for shared ML models and DB connections (../../raw/github/streamlit-streamlit.md)
- **Multipage apps** — `st.navigation`, `st.Page`, hidden pages, URL query-parameter widget binding (new in 1.58+)
- **Streamlit Components** — Community and custom React components extend beyond built-in widgets
- **App gallery** — Curated examples including dedicated LLM/chatbot category
- **Deployment paths** — Community Cloud (free, public apps, GitHub push-to-deploy), Snowflake-hosted Streamlit (private/enterprise), or self-host on any Python-capable platform

## Architecture

Streamlit uses a **client-server model**: `streamlit run` starts a Python/Tornado server; each browser tab is a client connected via WebSockets for real-time push updates. (../../raw/github/streamlit-streamlit.md) The monorepo splits `lib/` (Python backend), `frontend/` (React/TypeScript UI), and `proto/` (protobuf definitions). Reruns execute the script top-to-bottom on each interaction — Session State and caching are the primary tools for persistence and performance. In replicated deployments, session affinity ("stickiness") is required for media files and uploads because HTTP media requests may land on a different replica than the user's WebSocket session.

## Installation

```bash
pip install streamlit
streamlit hello
streamlit run streamlit_app.py
```

Minimum example from the README: (../../raw/github/streamlit-streamlit.md)

```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Docs cover Windows/macOS/Linux installation, GitHub Codespaces, and Streamlit in Snowflake as browser-based alternatives to local setup.

## Example usage

LLM chat streaming pattern (from API reference):

```python
import streamlit as st
st.write_stream(my_llm_stream)
```

Session State counter pattern:

```python
import streamlit as st
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button('Increment'):
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)
```

Deploy to Community Cloud: sign in with GitHub → select repo, branch, and entry file → click Deploy; subsequent `git push` updates the live app automatically.

## When to use

Reach for Streamlit when you need a **Python-native interactive UI** fast — ML model demos, data exploration dashboards, internal analytics tools, or LLM chat prototypes — and the team is comfortable with Python but not front-end frameworks. It excels at single-page and small multipage apps where the rerun model is acceptable. Prefer [[retool.com]] or [[lovable.dev]] for governed enterprise internal apps or full product UIs; prefer dedicated agent frameworks when you need orchestration, tool loops, or durable workflows rather than a display layer. [[render.com]] and similar PaaS platforms offer one-click Streamlit deployment for teams that want managed hosting without Community Cloud or Snowflake.

## Maintenance status

Actively maintained under Snowflake; default branch `develop`. (../../raw/github/streamlit-streamlit.md)
- Stars: 45,160; forks: 4,306; primary language: Python
- Latest release: 1.59.0 (2026-07-06); v1.58 added parallel fragments, `st.pagination`, and `streamlit skills` CLI
- License: Apache 2.0
- Trusted by 90%+ of Fortune 50 companies (marketing claim, 2024-11-15)

## Ecosystem

- **Community Cloud** (`share.streamlit.io`) — Free GitHub-connected hosting with viewer allow-lists, logs, reboot, and Codespaces editing
- **Streamlit in Snowflake** — Enterprise deployment with Snowflake security and data proximity
- **Streamlit Components** (`streamlit.io/components`) — Third-party and custom React extensions
- **Forum** (`discuss.streamlit.io`), **blog**, **30 Days of Streamlit** challenge, and **Playground** for browser-based trials
- **Agent instruction files** — `AGENTS.md` and `CLAUDE.md` in the repo for AI coding tool integration (../../raw/github/streamlit-streamlit.md)
- Overlaps with [[huggingface.co]] Spaces (Gradio/Streamlit demos) and [[pydantic.dev]]-based Python stacks for typed agent backends behind a Streamlit front end

## Documentation

Docs at `docs.streamlit.io` organized into Get Started (installation, fundamentals, first steps), Develop (API reference by activity type, architecture concepts — caching, session state, forms, widgets), Deploy (Community Cloud, Snowflake), and Knowledge Base (tutorials, FAQ). API reference covers display elements, input widgets, execution flow, connections/secrets, configuration, and multipage apps.
