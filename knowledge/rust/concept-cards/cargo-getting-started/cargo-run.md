---
# === CORE IDENTIFICATION ===
concept: Cargo Run
slug: cargo-run

# === CLASSIFICATION ===
category: build-system
subcategory: cli-commands
tier: foundational

# === PROVENANCE ===
source: "Cargo Getting Started"
source_slug: cargo-getting-started
authors: "The Cargo Team"
chapter: "First Steps with Cargo"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo run"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-package
  - cargo-manifest
  - binary-crate
extends:
  - cargo-build
related:
  - crate
contrasts_with:
  - cargo-build

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compile and run a Cargo project in one step?"
  - "What is the difference between `cargo build` and `cargo run`?"
---

# Quick Definition

`cargo run` is the Cargo CLI command that compiles a package's binary crate and immediately runs the resulting executable in one step. It combines the functionality of `cargo build` and manual execution.

# Core Definition

The source introduces `cargo run` as a convenience command: "We can also use `cargo run` to compile and then run it, all in one step" (Ch. 2: First Steps with Cargo). It performs compilation (if needed) and then executes the resulting binary. When the code has already been compiled and is up to date, `cargo run` skips recompilation (showing "Fresh" instead of "Compiling") and runs the existing binary directly.

# Prerequisites

- **Cargo Package** -- a package must exist before it can be run.
- **Cargo Manifest** -- `cargo run` reads the manifest for build configuration.
- **Binary Crate** -- `cargo run` requires a binary crate with a `main()` function to execute.

# Key Properties

1. Compiles the binary crate if source has changed
2. Runs the compiled executable immediately after compilation
3. Combines `cargo build` + manual execution into one command
4. Skips recompilation if the binary is already up to date (shows "Fresh")
5. Only works with binary crates (not library crates)
6. Outputs both compilation status and program output

# Construction / Recognition

## To Compile and Run in One Step:
1. Navigate to the package directory
2. Run `cargo run`
3. Cargo compiles (if needed) and then executes the binary
4. Program output appears in the console

# Context & Application

`cargo run` is the primary command for rapid development iteration. It eliminates the two-step process of building then manually running the binary. The Getting Started guide introduces it as an improvement over the `cargo build` + `./target/debug/<name>` workflow, making it the preferred command during development. It is especially useful in edit-compile-run cycles.

# Examples

**Example 1** (Ch 2): Using `cargo run` after the code has already been built:
```console
$ cargo run
     Fresh hello_world v0.1.0 (file:///path/to/package/hello_world)
   Running `target/hello_world`
Hello, world!
```

Note: The "Fresh" status indicates no recompilation was needed (the binary was already up to date from a previous `cargo build`).

# Relationships

## Builds Upon
- **Cargo Build** -- `cargo run` incorporates `cargo build` functionality as its first step
- **Cargo Package** -- operates on a package
- **Cargo Manifest** -- reads compilation metadata from the manifest
- **Binary Crate** -- requires a binary crate to have something to execute

## Enables
- Rapid development iteration without separate build and run steps

## Related
- **Crate** -- `cargo run` compiles and runs the binary crate

## Contrasts With
- **Cargo Build** -- `cargo build` only compiles; `cargo run` compiles AND runs. `cargo build` works with both binary and library crates; `cargo run` requires a binary crate.

# Common Errors

- **Error**: Using `cargo run` in a library-only package.
  **Correction**: `cargo run` requires a binary crate (`src/main.rs`). It cannot run a library crate.

- **Error**: Expecting `cargo run` to always recompile.
  **Correction**: `cargo run` is smart about recompilation -- it only recompiles when source files have changed. The "Fresh" status in the output indicates no recompilation was needed.

# Common Confusions

- **Confusion**: Thinking `cargo run` always recompiles from scratch.
  **Clarification**: `cargo run` performs incremental compilation. If the source hasn't changed since the last build, it shows "Fresh" and runs the existing binary without recompiling.

- **Confusion**: Believing `cargo run` and `cargo build` produce different binaries.
  **Clarification**: The compilation step in `cargo run` is identical to `cargo build`. The only difference is that `cargo run` also executes the result.

# Source Reference

Chapter 2: First Steps with Cargo. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 2 -- "We can also use `cargo run` to compile and then run it, all in one step"
- Confidence rationale: HIGH -- the source demonstrates the command with explicit output showing both the "Fresh" compilation status and the program output
- Uncertainties: The source does not cover `cargo run` flags or passing arguments to the executed binary
- Cross-reference status: All slugs reference cards in this extraction set
