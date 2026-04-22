---
# === CORE IDENTIFICATION ===
concept: Building the Rust Compiler
slug: building-rustc

# === CLASSIFICATION ===
category: compiler-development
subcategory: build-system
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "How to Build and Run the Compiler"
chapter_number: 1
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "x.py"
  - "bootstrap"
  - "building rustc"
  - "bootstrap.toml"
  - "x build"
  - "x check"
  - "rustc build system"
  - "compiler bootstrap"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-guide-overview
extends: []
related:
  - compiler-testing
  - compiler-debugging
  - contributing-to-rustc
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build the Rust compiler from source?"
  - "What is x.py and how do I use it?"
  - "What is bootstrap.toml and how do I configure it?"
  - "What are the different build stages (stage 0, 1, 2)?"
  - "How do I create a rustup toolchain from my local build?"
  - "How much disk space and RAM do I need to build rustc?"
  - "How do I speed up rebuilds during development?"
  - "How do I set up rust-analyzer for compiler development?"
  - "How do I cross-compile the compiler for other targets?"
  - "How do I optimize the compiler build (LTO, PGO, jemalloc)?"
---

# Quick Definition

The Rust compiler is built using `x.py` (invoked as `./x`), a Python-based build tool that orchestrates the multi-stage bootstrap process. Configuration is done through `bootstrap.toml`, which can be auto-generated via `./x setup`. The typical development workflow uses `./x check` for fast type-checking, `./x build library` for a usable stage 1 compiler, and `./x test` for running the test suite. Building requires 30GB+ disk space, 8GB+ RAM, and benefits greatly from multiple CPU cores.

# Core Definition

The build system uses a staged bootstrap architecture:

- **Stage 0**: A pre-built compiler (downloaded automatically) used to build the initial version of the new compiler
- **Stage 1**: The compiler built by stage 0, paired with a standard library built by that stage 1 compiler. This is the workhorse for most development work.
- **Stage 2**: The compiler rebuilt by the stage 1 compiler (a "full bootstrap"). Almost never needed for development.

The primary build command `./x build library` performs three steps:
1. Builds rustc using the stage 0 compiler and stage 0 std
2. Builds the standard library with the stage 1 compiler
3. Assembles a working stage 1 sysroot (stage 1 compiler + stage 1 standard libraries)

Configuration is managed through `bootstrap.toml` (generated via `./x setup`). Key settings include the build profile (`compiler`, `library`, `tools`), debug options, LLVM configuration, and optimization levels. The file `bootstrap.example.toml` documents all available settings.

The four most common `x` commands are:
- `./x check` -- quick compilation check; rust-analyzer can run this automatically
- `./x build` -- builds rustc, std, and rustdoc
- `./x test` -- runs all tests
- `./x fmt` -- formats all code

# Prerequisites

- Python 3 (required to run x.py)
- Git
- A C compiler/linker
- Internet connection (for downloading the stage 0 compiler and submodules)
- 30GB+ free disk space (full builds can use up to ~100GB)
- 8GB+ RAM
- 2+ CPU cores (more is significantly better)

# Key Properties

1. **`./x` preferred over `./x.py`**: The `./x` wrapper handles Python version detection cross-platform and is the recommended invocation form
2. **Path suffixes work for convenience**: `x test tidy` works instead of `x test src/tools/tidy`; `x build std` works instead of `x build library/std`
3. **`./x setup` creates initial configuration**: Running `./x setup` with the `compiler` profile creates a `bootstrap.toml` with reasonable defaults for compiler development
4. **`--keep-stage-std=1` speeds up rebuilds**: Skips rebuilding the standard library when only the compiler has changed; can produce incorrect results if metadata-affecting changes were made
5. **`download-rustc` avoids building the compiler tree**: When working only on the standard library or tools, setting `download-rustc` uses a pre-built nightly compiler for stage > 0 steps
6. **Incremental compilation is available but off by default**: Enable with `--incremental` flag or `rust.incremental = true` in `bootstrap.toml`; uses more disk space
7. **Separate build directories avoid lock conflicts with rust-analyzer**: Add `--build-dir=build-rust-analyzer` to rust-analyzer's custom commands to prevent competing builds
8. **Git worktrees for parallel branches**: Multiple working trees share the same Git database, avoiding duplicate clones; submodules are not shared
9. **Optimized builds use LTO, jemalloc, PGO, and BOLT**: Production builds of rustc use Thin-LTO (up to 10% speedup on Linux), jemalloc allocator, profile-guided optimization (up to 15% speedup), and post-link optimization
10. **Partial cloning reduces initial clone time**: `git clone --filter='blob:none'` avoids downloading full file history upfront

# Construction / Recognition

## Quickstart for Compiler Development:

```sh
git clone https://github.com/rust-lang/rust.git
cd rust
./x setup            # select "compiler" profile
./x build library    # build stage 1 compiler + std
rustup toolchain link stage1 build/host/stage1
rustc +stage1 -vV    # verify: version should end in "-dev"
```

## Creating a Rustup Toolchain:

```bash
rustup toolchain link stage1 build/host/stage1
rustup toolchain link stage2 build/host/stage2
```

The toolchain updates automatically when `x build` or `x test` run. The built toolchain does not include `cargo`; rustup falls back to the installed nightly/beta/stable cargo.

## Cross-Compilation Setup:

```bash
./x build --target x86_64-unknown-linux-gnu,wasm32-wasip1
```

Or configure permanently in `bootstrap.toml`:
```toml
build.target = ["x86_64-unknown-linux-gnu", "wasm32-wasip1"]
```

## Fast Rebuild Workflow:

```bash
# Initial build
./x build library
# Subsequent builds (skips std rebuild)
./x build library --keep-stage-std=1
```

# Context & Application

- **Compiler contributors**: The primary audience; need to build, test, and iterate on compiler changes
- **Standard library contributors**: Use `--stage 0 library/std` or `--stage 1 library` with the `library` profile
- **Tool developers**: Working on rustdoc, clippy, or other tools shipped with Rust
- **Distribution builders**: Use `./x dist` and `./x install` for creating distribution artifacts
- **Performance engineers**: Use optimized build configurations (LTO, PGO, BOLT) for benchmarking and release builds

# Examples

**Example 1**: Building and checking with the stage 1 compiler:
```bash
./x check compiler    # fast check for compile errors in compiler crate
./x build library     # full stage 1 build for running tests
./x test tests/ui     # run the UI test suite
```

**Example 2**: Configuration for faster development builds in `bootstrap.toml`:
```toml
[rust]
incremental = true
```

**Example 3**: Setting up rust-analyzer for compiler development -- `./x setup editor` prompts for editor-specific configuration (VS Code, Neovim, Emacs, Helix, Zed). The recommended settings configure rust-analyzer to use `./x check` for on-save checking and the stage 0 rustfmt for formatting.

**Example 4**: Optimized compiler build configuration:
```toml
rust.lto = "thin"           # Thin-LTO (up to 10% speedup, Linux/x86_64 only)
rust.jemalloc = true        # jemalloc allocator (Linux/macOS only)
rust.codegen-units = 1      # fewer codegen units for better optimization
```

**Example 5**: Building documentation:
```bash
./x doc library           # build standard library docs
./x doc compiler library  # build compiler + library docs
./x doc --stage 1         # build with current rustdoc (matches CI output)
```

# Relationships

## Builds Upon
- **compiler-guide-overview** -- understanding what the guide covers and where to get help

## Enables
- **compiler-testing** -- tests require a built compiler to run
- **compiler-debugging** -- debugging requires a compiler built with debug info

## Related
- **contributing-to-rustc** -- the contribution workflow that uses these build tools

## Contrasts With
- None within this source

# Common Errors

- **Error**: Running `./x test` without arguments, triggering the full test suite.
  **Correction**: "Running the entire test collection is almost never what you want to do during local development because it takes a really long time." Use `./x test tests/ui` or a more specific subset.

- **Error**: Editing LLVM-related settings without cleaning.
  **Correction**: "If you have already built rustc and you change settings related to LLVM, then you may have to execute `./x clean --all` for subsequent configuration changes to take effect."

- **Error**: Using `rm -rf build` to clean and losing cached LLVM.
  **Correction**: Prefer `./x clean` which preserves the LLVM build. "rm -rf build works too, but then you have to rebuild LLVM, which can take a long time even on fast computers."

- **Error**: Benchmarking with debug builds.
  **Correction**: Use `cargo build --release` and the stage 2 compiler for performance measurement.

# Common Confusions

- **Confusion**: A stage 2 build is needed for development.
  **Clarification**: "You almost never need to do this." A stage 1 build (`./x build library`) is sufficient for the vast majority of compiler development work.

- **Confusion**: `./x check` is the same as `./x build`.
  **Clarification**: `./x check` only verifies that the code compiles without producing a full binary. It is "much faster" and "often that is all you need (e.g., when renaming a method)."

- **Confusion**: The `--keep-stage-std=1` flag is always safe to use.
  **Clarification**: It assumes the old standard library is reusable. If you changed compiler metadata, MIR definitions, or type encoding, you may get "weird behavior" including ICEs. Remove the flag and rebuild if this happens.

- **Confusion**: Nix users can build without special configuration.
  **Clarification**: On non-NixOS distributions, "it may be necessary to set `build.patch-binaries-for-nix = true` in `bootstrap.toml`."

# Source Reference

Chapter 1 (1652 lines) covering: How to Build and Run the Compiler, Quickstart, Prerequisites, Suggested Workflows, Build Distribution Artifacts, Building Documentation, Rustdoc Overview, Adding a New Target, Optimized Build of the Compiler, and crates.io Dependencies. The chapter is heavily practical, focused on the build system mechanics and developer workflow optimization.

# Verification Notes

- Definition source: Direct content from Chapter 1 build documentation
- Key Properties: All items directly supported by source text with specific commands and flags
- Confidence rationale: HIGH -- this is practical, procedural documentation with concrete commands and configurations
- Uncertainties: Some version-specific details (disk space estimates, LLVM versions) may drift over time
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
