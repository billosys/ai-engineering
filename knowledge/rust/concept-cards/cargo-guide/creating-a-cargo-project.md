---
# === CORE IDENTIFICATION ===
concept: Creating a Cargo Project
slug: creating-a-cargo-project

# === CLASSIFICATION ===
category: build-system
subcategory: project-setup
tier: foundational

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "02-creating-a-new-project"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo new workflow"
  - "creating a new package"
  - "starting a Rust project"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - why-cargo-exists
extends: []
related:
  - cargo-new
  - cargo-build
  - cargo-run
  - cargo-project-layout
  - cargo-toml-vs-cargo-lock
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the full workflow for creating and building a new Cargo project?"
  - "What does cargo new generate and what do the files contain?"
  - "How do I work on an existing Cargo project someone else created?"
  - "What is the difference between debug and release builds?"
  - "What does the generated Cargo.toml look like?"
  - "Where does the compiled binary end up?"
---

# Quick Definition

Creating a Cargo project starts with `cargo new`, which generates a `Cargo.toml` manifest and a `src/main.rs` (or `src/lib.rs`) starter file. The project is immediately buildable with `cargo build` and runnable with `cargo run`. For existing projects, cloning and running `cargo build` fetches all dependencies and compiles everything automatically.

# Core Definition

The source demonstrates the complete workflow for starting a new Rust project: "To start a new package with Cargo, use `cargo new`" (Ch. 2). The command generates a directory containing a `Cargo.toml` manifest written in TOML format and a `src/main.rs` with a "hello world" program. The manifest is described as containing "all of the metadata that Cargo needs to compile your package." Building is accomplished with `cargo build`, which places output in `target/debug/`, and `cargo run` combines compilation and execution in one step.

The source also covers working on existing projects (Ch. 3): "If you download an existing package that uses Cargo, it's really easy to get going." The workflow is simply to clone the repository and run `cargo build`, which "will fetch all of the dependencies and then build them, along with the package." This demonstrates Cargo's promise that building any Cargo-based project follows the same pattern.

# Prerequisites

- **Why Cargo Exists** -- understanding the motivation for Cargo's package abstraction and build system

# Key Properties

1. **cargo new --bin**: Creates a binary package (the default); `--lib` creates a library
2. **Git initialization**: `cargo new` initializes a git repository by default; `--vcs none` disables this
3. **Generated Cargo.toml**: Contains `[package]` with name, version, and edition, plus an empty `[dependencies]` section
4. **Generated src/main.rs**: Contains a minimal "Hello, world!" program
5. **Debug vs release builds**: `cargo build` produces a debug build in `target/debug/`; `cargo build --release` produces an optimized build in `target/release/`
6. **Cargo.lock generation**: First build creates `Cargo.lock` to track exact dependency versions
7. **Existing project workflow**: `git clone` followed by `cargo build` is sufficient to build any Cargo project

# Construction / Recognition

## Creating a New Binary Project:
```console
$ cargo new hello_world --bin
$ cd hello_world
$ tree .
.
├── Cargo.toml
└── src
    └── main.rs
```

## The Generated Cargo.toml:
```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2024"

[dependencies]

```

## Building and Running:
```console
$ cargo build
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
$ ./target/debug/hello_world
Hello, world!
$ cargo run
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
     Running `target/debug/hello_world`
Hello, world!
```

## Working on an Existing Project (Ch. 3):
```console
$ git clone https://github.com/rust-lang/regex.git
$ cd regex
$ cargo build
   Compiling regex v1.5.0 (file:///path/to/package/regex)
```

# Context & Application

This card covers the complete project creation and onboarding workflow from the Cargo Guide. While the cargo-getting-started cards cover `cargo new`, `cargo build`, and `cargo run` as individual command definitions, this card focuses on the guide-level narrative: the end-to-end workflow from project creation through first build and run, including the content of generated files, the distinction between debug and release modes, and the equally simple workflow for joining an existing project. The guide's emphasis is that the workflow is the same whether creating a new project or onboarding to an existing one.

# Examples

**Example 1** (Ch. 2): The generated `src/main.rs`:
```rust
fn main() {
    println!("Hello, world!");
}
```
The source notes: "Cargo generated a 'hello world' program for you, otherwise known as a binary crate."

**Example 2** (Ch. 2): Release builds:
```console
$ cargo build --release
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
```
> "`cargo build --release` puts the resulting binary in `target/release` instead of `target/debug`."

**Example 3** (Ch. 2): Debug vs release tradeoff:
> "Compiling in debug mode is the default for development. Compilation time is shorter since the compiler doesn't do optimizations, but the code will run slower. Release mode takes longer to compile, but the code will run faster."

**Example 4** (Ch. 3): Building an existing project fetches dependencies automatically:
> "This will fetch all of the dependencies and then build them, along with the package."

# Relationships

## Builds Upon
- **Why Cargo Exists** -- the motivation for using Cargo over raw `rustc` invocations

## Enables
- **cargo-dependencies** -- once a project is created, you add dependencies to it
- **cargo-project-layout** -- the generated structure follows Cargo's conventional layout
- **cargo-toml-vs-cargo-lock** -- the first build generates `Cargo.lock` alongside `Cargo.toml`

## Related
- **cargo-new** -- the cargo-getting-started card covering the `cargo new` command definition
- **cargo-build** -- the cargo-getting-started card covering the `cargo build` command definition
- **cargo-run** -- the cargo-getting-started card covering the `cargo run` command definition

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting to `cd` into the new directory before running `cargo build` or `cargo run`.
  **Correction**: `cargo new hello_world` creates a subdirectory; you must enter it before building.

- **Error**: Expecting the binary at `target/hello_world` rather than `target/debug/hello_world`.
  **Correction**: Debug builds go to `target/debug/`; release builds go to `target/release/`.

- **Error**: Running `cargo build --release` for development iteration.
  **Correction**: Use plain `cargo build` for development (faster compilation); use `--release` only when building for deployment or benchmarking.

# Common Confusions

- **Confusion**: Thinking `cargo run` skips compilation.
  **Clarification**: `cargo run` compiles *and* runs. As the source notes, "You won't see the `Compiling` line if you have not made any changes since you last compiled."

- **Confusion**: Thinking `--bin` is required when creating a binary project.
  **Clarification**: `--bin` is the default. You only need to specify `--lib` explicitly if you want a library crate.

- **Confusion**: Thinking you need special setup to work on an existing Cargo project.
  **Clarification**: As stated in Ch. 3, simply cloning the repository and running `cargo build` is sufficient -- Cargo fetches all dependencies automatically.

# Source Reference

Chapter 2: Creating a New Package, and Chapter 3: Working on an Existing Cargo Package. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 2 -- "To start a new package with Cargo, use `cargo new`"
- Confidence rationale: HIGH -- the source provides step-by-step examples with exact command output
- Uncertainties: None for the workflows shown; advanced `cargo new` flags are not covered
- Cross-reference status: cargo-new, cargo-build, cargo-run reference cargo-getting-started cards; other slugs are within this extraction set
