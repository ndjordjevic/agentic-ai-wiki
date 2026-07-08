# neondatabase/neon

## Metadata
- Stars: 22501
- Primary language: Rust
- Default branch: main
- Latest release: release-proxy-8853 (2025-07-29)
- License: Apache License 2.0
- Homepage: https://neon.tech
- Fetched: 2026-07-08
- Final URL: https://github.com/neondatabase/neon

## Description
Neon: Serverless Postgres. We separated storage and compute to offer autoscaling, code-like database branching, and scale to zero.

## README

[![Neon](https://github.com/user-attachments/assets/fd91da5f-44a9-41c7-9075-36a5b5608083)](https://neon.com)

# Neon

Neon is an open-source serverless Postgres database platform. It separates storage and compute and substitutes the PostgreSQL storage layer by redistributing data across a cluster of nodes.

## Quick start
Try the [Neon Free Tier](https://neon.com/signup) to create a serverless Postgres instance. Then connect to it with your preferred Postgres client (psql, dbeaver, etc) or use the online [SQL Editor](https://neon.com/docs/get-started-with-neon/query-with-neon-sql-editor/). See [Connect from any application](https://neon.com/docs/connect/connect-from-any-app/) for connection instructions.

Alternatively, compile and run the project [locally](#running-local-installation).

## Architecture overview

A Neon installation consists of compute nodes and the Neon storage engine. Compute nodes are stateless PostgreSQL nodes backed by the Neon storage engine.

The Neon storage engine consists of two major components:
- Pageserver: Scalable storage backend for the compute nodes.
- Safekeepers: The safekeepers form a redundant WAL service that received WAL from the compute node, and stores it durably until it has been processed by the pageserver and uploaded to cloud storage.

See developer documentation in [SUMMARY.md](/docs/SUMMARY.md) for more information.

## Running a local development environment

Neon can be run on a workstation for small experiments and to test code changes, by following these instructions.

#### Building on Linux

```bash
git clone --recursive https://github.com/neondatabase/neon.git
cd neon
make -j`nproc` -s
```

#### Running neon database

```sh
cargo neon init
cargo neon start
cargo neon tenant create --set-default
cargo neon endpoint create main
cargo neon endpoint start main
cargo neon endpoint list
```

```text
psql -p 55432 -h 127.0.0.1 -U cloud_admin postgres
postgres=# CREATE TABLE t(key int primary key, value text);
```

#### Branching locally

```sh
cargo neon timeline branch --branch-name migration_check
cargo neon endpoint create migration_check --branch-name migration_check
cargo neon endpoint start migration_check
```

## Running tests

```sh
CARGO_BUILD_FLAGS="--features=testing" make
./scripts/pytest
```

## Documentation

[docs](/docs) Contains a top-level overview of all available markdown documentation.

- [sourcetree.md](/docs/sourcetree.md) contains overview of source tree layout.

Other resources:
- [Architecture decisions in Neon](https://neon.com/blog/architecture-decisions-in-neon/)
- [Neon glossary](/docs/glossary.md)

## Join the development

- Read [CONTRIBUTING.md](/CONTRIBUTING.md) to learn about project code style and practices.
- To get familiar with a source tree layout, use [sourcetree.md](/docs/sourcetree.md).

## Top-level structure

| Type | Name | Notes |
|---|---|---|
| dir | compute | PostgreSQL compute node code |
| dir | pageserver | Scalable storage backend |
| dir | safekeeper | Redundant WAL service |
| dir | proxy | Connection proxy |
| dir | control_plane | Local development control plane (`neon_local`) |
| dir | docs | Developer architecture documentation |
| dir | libs | Shared Rust libraries |
| dir | endpoint_storage | Endpoint storage service |
| dir | build-tools | Build tooling |
| dir | docker-compose | Local docker compose configs |
| file | Cargo.toml | Rust workspace root |
| file | Makefile | Build orchestration |
| file | README.md | Project overview and local dev guide |
