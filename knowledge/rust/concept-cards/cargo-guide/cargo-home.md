---
# === CORE IDENTIFICATION ===
concept: Cargo Home
slug: cargo-home

# === CLASSIFICATION ===
category: build-system
subcategory: tooling-internals
tier: intermediate

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "10-cargo-home"
chapter_number: 10
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "~/.cargo"
  - "CARGO_HOME"
  - "Cargo home directory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-dependencies
extends: []
related:
  - cargo-ci
  - cargo-publishing
  - cargo-build-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cargo home directory and where is it located?"
  - "What files and directories does ~/.cargo contain?"
  - "How do I change the location of the Cargo home?"
  - "What should I cache from the Cargo home in CI?"
  - "How does Cargo cache downloaded dependencies?"
  - "What is the difference between registry/cache and registry/src?"
  - "How do I clear the Cargo cache?"
  - "How does Cargo store Git dependencies?"
---

# Quick Definition

The Cargo home (defaulting to `$HOME/.cargo/`) is the download and source cache directory that stores configuration (`config.toml`), credentials (`credentials.toml`), installed binaries (`bin/`), Git dependency clones (`git/`), and registry data (`registry/`). Its location can be changed via the `CARGO_HOME` environment variable. The internal structure is not stabilized.

# Core Definition

The source states: "The 'Cargo home' functions as a download and source cache. When building a crate, Cargo stores downloaded build dependencies in the Cargo home." (Ch. 10). By default it is located at `$HOME/.cargo/` and can be relocated via the `CARGO_HOME` environment variable.

The directory contains files (`config.toml` for global configuration, `credentials.toml` for registry login tokens, `.crates.toml` and `.crates2.json` for installed crate metadata) and directories (`bin/` for installed executables, `git/db/` and `git/checkouts/` for Git dependency management, `registry/index/`, `registry/cache/`, and `registry/src/` for registry-based dependencies).

The source explicitly warns: "the internal structure of the Cargo home is not stabilized and may be subject to change at any time."

# Prerequisites

- **Cargo Dependencies** -- understanding how dependencies are fetched and stored

# Key Properties

1. **Default location**: `$HOME/.cargo/`, configurable via `CARGO_HOME` environment variable
2. **config.toml**: Global Cargo configuration
3. **credentials.toml**: Private login credentials from `cargo login`
4. **bin/**: Executables installed via `cargo install` or `rustup`
5. **git/db/**: Bare Git repository clones for Git dependencies
6. **git/checkouts/**: Specific commit checkouts from bare repos for the compiler
7. **registry/index/**: Bare Git repository with metadata (versions, dependencies) for all crates in a registry
8. **registry/cache/**: Compressed `.crate` archives of downloaded dependencies
9. **registry/src/**: Extracted source files from `.crate` archives for compilation
10. **Unstabilized structure**: The internal layout may change at any time
11. **Self-healing cache**: Any part can be removed and Cargo will redownload or re-extract as needed

# Construction / Recognition

## Cargo Home Structure:
```
$HOME/.cargo/
├── config.toml          # Global configuration
├── credentials.toml     # Registry login credentials
├── .crates.toml         # Installed crate metadata (do not edit)
├── .crates2.json        # Installed crate metadata (do not edit)
├── bin/                 # Installed executables
├── git/
│   ├── db/              # Bare Git repo clones
│   └── checkouts/       # Specific commit checkouts
└── registry/
    ├── index/           # Registry metadata (bare git repo)
    ├── cache/           # Compressed .crate archives
    └── src/             # Extracted source files
```

## Efficient CI Caching (recommended subset):
```
.crates.toml
.crates2.json
bin/
registry/index/
registry/cache/
git/db/
```

# Context & Application

Understanding the Cargo home is important for CI optimization, disk space management, and troubleshooting dependency issues. The source's CI caching guidance is particularly practical: caching the entire `$CARGO_HOME` is inefficient because it stores downloaded sources twice (compressed in `registry/cache/` and extracted in `registry/src/`). The recommended subset avoids this redundancy. The `cargo vendor` subcommand provides an alternative for projects that need all dependencies vendored locally. The cache is self-healing: "you can always remove any part of the cache and Cargo will do its best to restore sources."

# Examples

**Example 1** (Ch. 10): Credentials storage:
> "Private login credentials from `cargo login` in order to log in to a registry."

**Example 2** (Ch. 10): Git dependency storage mechanism:
> "When a crate depends on a git repository, Cargo clones the repo as a bare repo into this directory and updates it if necessary."
> "The required commit of the repo is checked out from the bare repo inside `git/db` into this directory."
> "Multiple checkouts of different commits of the same repo are possible."

**Example 3** (Ch. 10): Why not to cache everything in CI:
> "If we depend on a crate such as `serde 1.0.92` and cache the entire `$CARGO_HOME` we would actually cache the sources twice, the `serde-1.0.92.crate` inside `registry/cache` and the extracted `.rs` files of serde inside `registry/src`. That can unnecessarily slow down the build."

**Example 4** (Ch. 10): Cache self-healing:
> "In theory, you can always remove any part of the cache and Cargo will do its best to restore sources if a crate needs them either by reextracting an archive or checking out a bare repo or by simply redownloading the sources from the web."

# Relationships

## Builds Upon
- **Cargo Dependencies** -- the Cargo home is where fetched dependencies are stored

## Enables
- Efficient CI caching strategies
- Understanding of how Git and registry dependencies are stored and managed

## Related
- **cargo-ci** -- CI pipelines benefit from caching the right parts of the Cargo home
- **cargo-publishing** -- `credentials.toml` in the Cargo home stores the crates.io API token
- **cargo-build-performance** -- cache management affects build performance

## Contrasts With
- None within this source

# Common Errors

- **Error**: Manually editing `.crates.toml` or `.crates2.json`.
  **Correction**: The source warns: "Do NOT edit by hand!" These files are managed by `cargo install`.

- **Error**: Caching the entire `$CARGO_HOME` directory in CI.
  **Correction**: Cache only the recommended subset (`.crates.toml`, `.crates2.json`, `bin/`, `registry/index/`, `registry/cache/`, `git/db/`). Caching `registry/src/` duplicates data already in `registry/cache/`.

- **Error**: Sharing or committing `credentials.toml` to version control.
  **Correction**: This file contains secret API tokens. It lives in the Cargo home and should never be shared.

# Common Confusions

- **Confusion**: Thinking the Cargo home structure is a stable API.
  **Clarification**: "The internal structure of the Cargo home is not stabilized and may be subject to change at any time."

- **Confusion**: Thinking deleted cache files will cause permanent build failures.
  **Clarification**: The cache is self-healing. Cargo will redownload, re-extract, or re-checkout as needed.

- **Confusion**: Thinking `registry/cache/` and `registry/src/` contain different crates.
  **Clarification**: They contain the same crates in different forms: `cache/` has compressed `.crate` archives, `src/` has the extracted source files. This is why caching both in CI is redundant.

# Source Reference

Chapter 10: Cargo Home -- sections "Files," "Directories," "Caching the Cargo home in CI," "Vendoring all dependencies of a project," and "Clearing the cache." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 10 -- "The 'Cargo home' functions as a download and source cache."
- Confidence rationale: HIGH -- the source provides a complete directory listing with explanations
- Uncertainties: The internal structure is explicitly marked as unstable and subject to change
- Cross-reference status: All slugs reference cards within this extraction set
