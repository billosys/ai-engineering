---
# === CORE IDENTIFICATION ===
concept: Installation
slug: installation

# === CLASSIFICATION ===
category: cli
subcategory: setup
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Installation"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "installing Cobalt"
  - "setup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt
extends: []
related:
  - cobalt-init
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install Cobalt?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

Cobalt can be installed on Windows, Linux, and macOS through OS packages, pre-built binaries, `cargo install`, or by building from source (including via Docker).

# Core Definition

The Cobalt documentation describes five installation methods for the Cobalt static site generator. OS packages are available for Arch Linux (`pacman -S cobalt`) and macOS via Homebrew (`brew install cobalt`). Pre-built binaries can be downloaded from the GitHub releases page or installed via a curl script to `~/.cargo/bin`. From source, Cobalt can be installed using `cargo install cobalt-bin` from crates.io, built natively by cloning the repository and running `cargo build --release`, or built using a Docker container with the official Rust image (source: Install doc page).

# Prerequisites

- **Cobalt** -- understanding of what Cobalt is and why you would install it
- For source builds: Rust toolchain (rustup), and on Debian systems: cmake, git, curl, build-essential, libssl-dev
- For Windows with syntax highlighting/sass: Build Tools for Visual Studio and Windows 10 SDK

# Key Properties

1. **Cross-platform** -- "Cobalt supports Windows, Linux, and Mac" (source: Install doc page).
2. **OS Package method** -- Arch Linux via `pacman -S cobalt`; macOS via `brew install cobalt` (source: Install doc page, "OS Package" section).
3. **Pre-built binary method** -- download from GitHub releases or use the gh-install curl script, with no additional requirements (source: Install doc page, "Pre-built Binary" section).
4. **Cargo install method** -- `cargo install cobalt-bin` installs from crates.io, requiring a Rust toolchain (source: Install doc page, "From crates.io" section).
5. **Native build method** -- clone the repository and run `cargo build --release`; optional `--features=sass` flag for Sass support (source: Install doc page, "Building Natively" section).
6. **Docker build method** -- uses `rust:latest` Docker image to compile without a local Rust installation (source: Install doc page, "Building with Docker" section).

# Construction / Recognition

## To Construct/Create:
1. **OS Package (Arch Linux)**: `pacman -S cobalt`
2. **OS Package (macOS)**: `brew install cobalt`
3. **Pre-built binary**: Download from `https://github.com/cobalt-org/cobalt.rs/releases` or run:
   ```
   curl -LSfs https://raw.githubusercontent.com/crate-ci/gh-install/master/v1/install.sh | sh -s -- --git cobalt-org/cobalt.rs --crate cobalt
   ```
4. **From crates.io**: `cargo install cobalt-bin`
5. **Native build**: `git clone https://github.com/cobalt-org/cobalt.rs.git && cargo build --release`
6. **Docker build**: `docker run --rm -it -u $(id -u):$(id -g) -v ${PWD}:/app -w /app rust:latest cargo build --release --features=sass`

## To Identify/Recognize:
1. A successful installation is verified by running `cobalt --help`, which displays available commands.
2. The binary is typically located at `~/.cargo/bin/cobalt` when installed via cargo or the curl script.

# Context & Application

- **Typical contexts**: First step before using any Cobalt functionality; needed once per development environment.
- **Common applications**: Setting up a development machine for Cobalt site authoring, configuring CI/CD pipelines for site building, containerized builds.

# Examples

**Example 1** (source: Getting Started page): Quick install via curl script:
```console
$ curl -LSfs https://raw.githubusercontent.com/crate-ci/gh-install/master/v1/install.sh | sh -s -- --git cobalt-org/cobalt.rs --crate cobalt
```

**Example 2** (source: Install doc page): Installing from crates.io:
```console
$ cargo install cobalt-bin
```

**Example 3** (source: Install doc page): Building with Docker:
```console
$ docker pull rust:latest
$ git clone https://github.com/cobalt-org/cobalt.rs.git
$ cd cobalt.rs
$ docker run --rm -it -u $(id -u):$(id -g) -v ${PWD}:/app -w /app rust:latest cargo build --release --features=sass
```

**Example 4** (source: Install doc page): Debian prerequisites for building from source:
```console
$ sudo apt install cmake git curl build-essential libssl-dev
$ curl https://sh.rustup.rs -sSf | sh
$ source $HOME/.cargo/env
```

# Relationships

## Builds Upon
- **Cobalt** -- installation is the prerequisite step for using Cobalt

## Enables
- **cobalt init** -- after installation, users can initialize a new site
- **cobalt build** -- building requires a working Cobalt installation
- **cobalt serve** -- serving requires a working Cobalt installation

## Related
- **cobalt-init** -- the natural next step after installation

## Contrasts With
- No direct contrasts within scope.

# Common Errors

- **Error**: Running `cargo install cobalt` instead of `cargo install cobalt-bin`.
  **Correction**: The crate name on crates.io is `cobalt-bin`, not `cobalt`. Use `cargo install cobalt-bin`.

- **Error**: On Windows, building with syntax highlighting or Sass support fails with MinGW/MSYS2.
  **Correction**: Use Build Tools for Visual Studio instead of MinGW/MSYS2, install Windows 10 SDK, and run `vcvarsall.bat amd64` before building (source: Install doc page, "Windows" section).

# Common Confusions

- **Confusion**: The crate name `cobalt-bin` vs. the command name `cobalt`.
  **Clarification**: The crate published on crates.io is named `cobalt-bin`, but once installed, the command-line binary is invoked as `cobalt`.

# Source Reference

Installation doc page, all sections (OS Package, Pre-built Binary, From Source, From crates.io, Building Natively, Building with Docker). Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Install doc page
- Confidence rationale: High -- all installation methods are explicitly documented with commands and requirements
- Uncertainties: The Homebrew formula availability may change over time; the documentation shows it but does not specify version constraints
- Cross-reference status: References to cobalt, cobalt-init verified against planned card slugs
