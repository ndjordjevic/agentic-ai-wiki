# streamlit.io

## Fetch log
- Inbox URL: https://streamlit.io/
- Final URL: https://streamlit.io/
- Fetched: 2026-07-07
- Pages: 9
- Mode: standard

## Landing page — https://streamlit.io/

🎈 New in 1.58: Introducing parallel fragments, st.pagination, streamlit skills CLI and more!

### A faster way to build and share data apps

Turn your data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.

Get started | Try the live playground!

Trusted by over 90% of Fortune 50 companies (As of 2024-11-15)

### Get started in under a minute

Streamlit is an open-source app framework that is a breeze to get started with:

```
pip install streamlit
streamlit hello
```

Or skip local installation:
- Try a live playground in your browser
- Build in public with Streamlit Community Cloud — public apps only, totally free, GitHub account required
- Build like a pro on Snowflake — unlimited private apps, enterprise-grade reliability and security

### Three simple principles

**Embrace scripting** — Build an app in a few lines of code with a magically simple API. See it automatically update as you iteratively save the source file.

Example:
```python
import streamlit as st
import pandas as pd
st.write("""
# My first app
Hello *world!*
""")
df = pd.read_csv("my_data.csv")
st.line_chart(df)
```

**Weave in interaction** — Adding a widget is the same as declaring a variable. No need to write a backend, define routes, handle HTTP requests, connect a frontend, write HTML, CSS, JavaScript.

**Deploy instantly** — Show off public apps for free on Streamlit Community Cloud, go with Snowflake for enterprise-grade deployment, or pick something else entirely.

### Build powerful apps

Used in the world's top data science groups (Google X, Stitch Fix, Insight Data Science, Vega-Lite, Yelp, Uber, and more).

### Compatible with basically everything

And even more, with Streamlit Components! Build your own, share with the community.

### Deploy on enterprise

Try Streamlit in Snowflake. Code in the browser, collaborate with Git, deploy in one click. With the security and reliability of Snowflake.

**Navigation:** Playground | Gallery | Components | Cloud | Community | Docs (docs.streamlit.io) | GitHub (github.com/streamlit/streamlit)

## Docs — https://docs.streamlit.io/

Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. Build and deploy powerful data apps in minutes.

**Setup and installation** — Get set up to start working with Streamlit.
**API reference** — Learn about our APIs, with actionable explanations of specific functions and features.
**App gallery** — Try out awesome apps created by our users.

### How to use our docs

- **Get started** — Set up your development environment and learn fundamental concepts.
- **Develop** — API reference explains each Streamlit function with examples. Conceptual guides. Step-by-step tutorials.
- **Deploy** — Streamlit Community Cloud (free platform for deploying and sharing apps). Streamlit in Snowflake (enterprise-class solution).
- **Knowledge base** — Tips, tricks, and articles for creating and deploying Streamlit apps.

### What's new (1.58+)

- **Dynamic containers** — `st.tabs`, `st.expander`, `st.popover` can track open/closed state and trigger reruns with `on_change`.
- **Widget binding** — Most non-trigger widgets have a `bind` parameter to sync widget state with URL query parameters.
- **Clickable images** — `st.image` has a `link` parameter for HTTP/HTTPS URLs.
- **Hidden pages** — `st.Page` has a `visibility` parameter to hide pages in navigation while keeping them routable.
- **CSS colors in Markdown** — Markdown supports arbitrary CSS colors for text foreground and background.
- **Metric delta descriptions** — `st.metric` has a `delta_description` parameter.

## Get started with Streamlit — https://docs.streamlit.io/get-started

This Get Started guide explains how Streamlit works, how to install Streamlit on your preferred operating system, and how to create your first Streamlit app.

- **Installation** — Windows, macOS, Linux. Or code in browser with GitHub Codespaces or Streamlit in Snowflake.
- **Fundamentals** — Streamlit's data model and development flow: display and style data, draw charts and maps, add interactive widgets, customize app layouts, cache computation, define themes.
- **First steps** — Fetch and cache data, draw charts, plot on a map, use interactive widgets to filter results.
- **30 Days of Streamlit 🎈** — Free, self-paced 30 day challenge to build and deploy data apps.

## Working with Streamlit's execution model — https://docs.streamlit.io/develop/concepts/architecture

- **Run your app** — Understand how to start your Streamlit app.
- **Streamlit's architecture** — Client-server architecture and related considerations.
- **The app chrome** — Widgets in the top right for development and user help.
- **Caching** — Cache results to avoid unnecessary recomputation with each rerun.
- **Session State** — Manage app statefulness.
- **Forms** — Isolate user input and prevent unnecessary app reruns.
- **Widget behavior** — How widgets work in detail.

## Understanding Streamlit's client-server architecture — https://docs.streamlit.io/develop/concepts/architecture/architecture

Streamlit apps have a client-server structure. The Python backend is the server; the browser frontend is the client.

**Python backend (server)** — `streamlit run your_app.py` starts a Streamlit server that performs computations for all users. The server runs on the host machine.

**Browser frontend (client)** — Each browser tab is a separate session. When users view over a network, client and server run on different machines.

**Server-client impact on app design:**
- Host must be sized for concurrent users.
- App cannot access user's local files/OS — only uploaded files via widgets like `st.file_uploader`.
- Peripheral devices accessed through browser via Streamlit commands or custom components.
- External programs run on the server, not the user's machine.
- Load balancing/replication requires session affinity for some features.

**WebSockets and session management** — Built on Tornado; WebSockets maintain persistent two-way communication. Each browser tab creates its own WebSocket connection and session. In replicated deployments, media file requests may route to different servers — use session affinity, Base64 data URIs, or external storage (S3).

## Caching overview — https://docs.streamlit.io/develop/concepts/architecture/caching

Streamlit runs your script from top to bottom at every user interaction or code change. Caching stores results of slow function calls so they only need to run once.

Two caching decorators:
- **`st.cache_data`** — Cache computations that return data (DataFrames, arrays, API results). Creates a new copy at each call — safe against mutations. Default choice.
- **`st.cache_resource`** — Cache global resources like ML models or database connections — unserializable objects shared across reruns/sessions. Mutations affect the cached object directly.

Cached values are available to all users. For session-scoped persistence, use Session State instead.

## Add statefulness to apps — https://docs.streamlit.io/develop/concepts/architecture/session-state

A browser tab session is a Streamlit session. Each rerun starts from a blank slate unless Session State is used.

Session State shares variables between reruns per user session. Persists across pages in multipage apps. Supports callbacks (`on_change`, `on_click`, `args`, `kwargs`).

Widget state is unified with Session State via the `key` argument. Cannot set state for `st.button` and `st.file_uploader` via Session State API.

`runner.enforceSerializableSessionState = true` in `.streamlit/config.toml` restricts Session State to pickle-serializable objects.

Limitations: Session State exists only while tab is connected; not persisted across server crashes.

## API reference — https://docs.streamlit.io/develop/api-reference

API organized by activity type. Key categories:

**Display almost anything**
- `st.write`, `st.write_stream` (generators/LLM streams with typewriter effect), Magic (auto-write literals on their own line)
- Text: `st.markdown`, `st.title`, `st.header`, `st.subheader`, `st.caption`, `st.text`, `st.latex`, `st.code`
- Data: `st.dataframe`, `st.data_editor`, `st.column_config`, `st.table`, `st.metric`, `st.json`
- Charts: `st.line_chart`, `st.area_chart`, `st.bar_chart`, `st.scatter_chart`, `st.altair_chart`, `st.vega_lite_chart`, `st.plotly_chart`, `st.pyplot`, `st.bokeh_chart`, `st.graphviz_chart`, `st.map`, `st.pydeck_chart`
- Media: `st.image`, `st.audio`, `st.video`, `st.logo`, `st.pdf`
- Layout: `st.columns`, `st.container`, `st.expander`, `st.popover`, `st.tabs`, `st.sidebar`, `st.empty`, `st.status`, `st.fragment`
- Chat: `st.chat_message`, `st.chat_input`
- Status: `st.success`, `st.info`, `st.warning`, `st.error`, `st.exception`, `st.toast`, `st.progress`, `st.spinner`

**Input widgets**
- `st.button`, `st.download_button`, `st.link_button`, `st.page_link`
- `st.checkbox`, `st.toggle`, `st.radio`, `st.selectbox`, `st.multiselect`, `st.slider`, `st.select_slider`, `st.text_input`, `st.text_area`, `st.number_input`, `st.date_input`, `st.time_input`, `st.datetime_input`, `st.color_picker`, `st.file_uploader`, `st.camera_input`, `st.audio_input`
- `st.feedback`, `st.pills`, `st.segmented_control`

**Execution flow**
- `st.form`, `st.form_submit_button`
- `st.rerun`, `st.stop`, `st.switch_page`
- `st.fragment` (partial reruns)
- `st.pagination`

**Connections and secrets**
- `st.connection` (SQL, Snowflake, etc.)
- `st.secrets`

**Configuration**
- `st.set_page_config`, `st.get_option`, `st.set_option`
- Theming via `config.toml`

**Multipage apps**
- `st.navigation`, `st.Page`, `st.switch_page`

## Streamlit Community Cloud — https://docs.streamlit.io/deploy/streamlit-community-cloud

With Streamlit Community Cloud, create, deploy, and manage Streamlit apps for free. Share apps with the world and build a customized profile page. Account connects directly to GitHub repositories (public or private). Most apps launch in minutes. Community Cloud handles containerization.

- **Get started** — Create account
- **Deploy your app** — Step-by-step deployment guide
- **Manage your app** — Logs, reboot, favorites, GitHub Codespaces editing
- **Share your app** — Share or embed
- **Manage your account** — Email, connections, deletion

Can configure GitHub Codespaces to develop in the cloud without local setup.

## Community Cloud marketing page — https://streamlit.io/cloud

Share your apps with the whole world. Explore and fork community apps. Craft your profile. Totally free.

**Deploy in 3 steps:**
1. Sign in with GitHub
2. Pick a repo, branch, and file
3. Click Deploy — app updates on every `git push`

**Features:** Deploy in one click | Keep code in your repo | Live updates | Securely connect to data | Restrict access with per-app viewer allow-lists | Connect with the community

**Enterprise:** Streamlit in Snowflake — code in browser, collaborate with Git, deploy in one click with Snowflake security and reliability.
