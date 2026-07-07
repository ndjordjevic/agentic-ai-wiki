# streamlit/streamlit

## Metadata
- Stars: 45160
- Primary language: Python
- Default branch: develop
- Latest release: 1.59.0 (2026-07-06)
- License: Apache License 2.0
- Homepage: https://streamlit.io
- Fetched: 2026-07-07
- Final URL: https://github.com/streamlit/streamlit

## Description
Streamlit — A faster way to build and share data apps.

## README

# Welcome to Streamlit 👋

**A faster way to build and share data apps.**

## What is Streamlit?

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you've created an app, you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app.

### Why choose Streamlit?

- **Simple and Pythonic:** Write beautiful, easy-to-read code.
- **Fast, interactive prototyping:** Let others interact with your data and provide feedback quickly.
- **Live editing:** See your app update instantly as you edit your script.
- **Open-source and free:** Join a vibrant community and contribute to Streamlit's future.

## Installation

Open a terminal and run:

```bash
$ pip install streamlit
$ streamlit hello
```

If this opens our sweet _Streamlit Hello_ app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/get-started) for specific installs.

## Quickstart

### A little example

Create a new file named `streamlit_app.py` in your project directory with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Now run it to open the app!
```
$ streamlit run streamlit_app.py
```

### Give me more!

Streamlit comes in with [a ton of additional powerful elements](https://docs.streamlit.io/develop/api-reference) to spice up your data apps and delight your viewers. Some examples:

- Input widgets
- Dataframes
- Charts
- Layout
- Multi-page apps
- Fun

Our vibrant creators community also extends Streamlit capabilities using 🧩 [Streamlit Components](https://streamlit.io/components).

## Get inspired

There's so much you can build with Streamlit:
- 🤖  [LLMs & chatbot apps](https://streamlit.io/gallery?category=llms)
- 🧬  [Science & technology apps](https://streamlit.io/gallery?category=science-technology)
- 💬  [NLP & language apps](https://streamlit.io/gallery?category=nlp-language)
- 🏦  [Finance & business apps](https://streamlit.io/gallery?category=finance-business)
- 🗺  [Geography & society apps](https://streamlit.io/gallery?category=geography-society)

**Check out [our gallery!](https://streamlit.io/gallery)** 🎈

## Community Cloud

Deploy, manage and share your apps for free using our [Community Cloud](https://streamlit.io/cloud)! Sign-up [here](https://share.streamlit.io/signup).

## Resources

- Explore our [docs](https://docs.streamlit.io) to learn how Streamlit works.
- Ask questions and get help in our [community forum](https://discuss.streamlit.io).
- Read our [blog](https://blog.streamlit.io) for tips from developers and creators.
- Extend Streamlit's capabilities by installing or creating your own [Streamlit Components](https://streamlit.io/components).
- Help others find and play with your app by using the Streamlit GitHub badge in your repository:
```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](URL_TO_YOUR_APP)
```

## Contribute

Before contributing, please read our guidelines here: https://github.com/streamlit/streamlit/blob/develop/CONTRIBUTING.md

## License

Streamlit is completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.

## Top-level structure

| Path | Notes |
|---|---|
| `lib/` | Core Python Streamlit library |
| `frontend/` | Browser frontend (React/TypeScript) |
| `proto/` | Protocol buffer definitions for client-server communication |
| `e2e_playwright/` | End-to-end Playwright tests |
| `scripts/` | Build and development scripts |
| `specs/` | Specifications |
| `wiki/` | Internal wiki/docs in repo |
| `pyproject.toml` | Python project configuration |
| `Makefile` | Build targets |
| `AGENTS.md`, `CLAUDE.md` | Agent instruction files for AI coding tools |
| `.github/` | CI/CD workflows |
