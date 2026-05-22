# pydantic/pydantic

## Metadata
- Stars: 27,832
- Primary language: Python
- Default branch: main
- Latest release: v2.13.4 (2026-05-06)
- License: MIT License
- Homepage: https://pydantic.dev/docs/validation
- Fetched: 2026-05-22
- Final URL: https://github.com/pydantic/pydantic

## Description
Data validation using Python type hints

## README
# Pydantic Validation

[![CI](https://img.shields.io/github/actions/workflow/status/pydantic/pydantic/ci.yml?branch=main&logo=github&label=CI)](https://github.com/pydantic/pydantic/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![pypi](https://img.shields.io/pypi/v/pydantic.svg)](https://pypi.python.org/pypi/pydantic)
[![downloads](https://static.pepy.tech/badge/pydantic/month)](https://pepy.tech/project/pydantic)
[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](https://github.com/pydantic/pydantic/blob/main/LICENSE)
[![llms.txt](https://img.shields.io/badge/llms.txt-green)](https://docs.pydantic.dev/latest/llms.txt)

Data validation using Python type hints.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.10+; validate it with Pydantic.

## Pydantic Logfire :fire:

We've launched Pydantic Logfire to help you monitor your applications.
[Learn more](https://pydantic.dev/logfire/?utm_source=pydantic_validation)

## Pydantic V1.10 vs. V2

Pydantic V2 is a ground-up rewrite that offers many new features, performance improvements, and some breaking changes compared to Pydantic V1.

If you're using Pydantic V1 you may want to look at the
[pydantic V1.10 Documentation](https://docs.pydantic.dev/) or,
[`1.10.X-fixes` git branch](https://github.com/pydantic/pydantic/tree/1.10.X-fixes). Pydantic V2 also ships with the latest version of Pydantic V1 built in so that you can incrementally upgrade your code base and projects: `from pydantic import v1 as pydantic_v1`.

## Help

See [documentation](https://docs.pydantic.dev/) for more details.

## Installation

Install using `pip install -U pydantic` or `conda install pydantic -c conda-forge`.
For more installation options to make Pydantic even faster,
see the [Install](https://docs.pydantic.dev/install/) section in the documentation.

## A Simple Example

```python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: list[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#> 123
```

## Contributing

For guidance on setting up a development environment and how to make a
contribution to Pydantic, see
[Contributing to Pydantic](https://docs.pydantic.dev/contributing/).

## Reporting a Security Vulnerability

See our [security policy](https://github.com/pydantic/pydantic/security/policy).

## Top-level structure
- `pydantic/` — main library source (Python)
- `pydantic-core/` — Rust-based core validation engine (vendored as submodule)
- `docs/` — documentation source (MkDocs)
- `tests/` — test suite
- `release/` — release tooling and changelogs
- `pyproject.toml` — build configuration
- `HISTORY.md` — full changelog
- `Makefile` — developer workflow shortcuts
- `mkdocs.yml` — documentation site configuration
- `.github/` — CI/CD workflows (GitHub Actions)
