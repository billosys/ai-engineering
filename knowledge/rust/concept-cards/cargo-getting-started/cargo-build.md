---
# === CORE IDENTIFICATION ===
concept: Cargo Build
slug: cargo-build

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
  - "cargo build"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-package
  - cargo-manifest
extends: []
related:
  - crate
  - binary-crate
contrasts_with:
  - cargo-run

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build a Cargo project?"
  - "What is the difference between `cargo build` and `cargo run`?"
---

# Quick Definition

`cargo build` is the Cargo CLI command that compiles a package's crate(s) into output artifacts. For binary crates, it produces an executable in the `target/debug/` directory.

# Core Definition

The source demonstrates `cargo build` as the command to compile a Cargo package: "Let's compile it: `cargo build`" (Ch. 2: First Steps with Cargo). The command reads the `Cargo.toml` manifest and compiles the crate within the package. The compiled output for a binary crate is placed in `target/debug/<name>`, and the resulting executable can then be run directly.

# Prerequisites

- **Cargo Package** -- a package must exist (created via `cargo new`) before it can be built.
- **Cargo Manifest** -- `cargo build` reads the manifest to determine how to compile.

# Key Properties

1. Compiles the crate(s) within a package
2. Reads configuration from `Cargo.toml`
3. Outputs compiled artifacts to `target/debug/` by default
4. For binary crates, produces an executable named after the package
5. Only compiles -- does not run the resulting program
6. Reports compilation progress to the console

# Construction / Recognition

## To Build a Cargo Package:
1. Navigate to the package directory (where `Cargo.toml` is located)
2. Run `cargo build`
3. The compiled binary appears at `target/debug/<package_name>`

## To Run the Built Binary Manually:
1. After `cargo build`, execute `./target/debug/<package_name>`

# Context & Application

`cargo build` is one of the most frequently used Cargo commands. It compiles code without running it, which is useful when you want to check that code compiles successfully or when you need to produce the binary for deployment or testing separately from execution. The Getting Started guide presents `cargo build` as the first step in the build-then-run workflow, before introducing `cargo run` as a shortcut.

# Examples

**Example 1** (Ch 2): Compiling the hello_world package:
```console
$ cargo build
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
```

**Example 2** (Ch 2): Running the compiled binary directly after building:
```console
$ ./target/debug/hello_world
Hello, world!
```

# Relationships

## Builds Upon
- **Cargo Package** -- `cargo build` operates on a package
- **Cargo Manifest** -- `cargo build` reads the manifest for compilation metadata

## Enables
- Running the compiled binary manually from `target/debug/`

## Related
- **Crate** -- `cargo build` compiles the crate(s) within the package
- **Binary Crate** -- the primary example in the Getting Started guide

## Contrasts With
- **Cargo Run** -- `cargo build` only compiles; `cargo run` compiles AND runs in one step

# Common Errors

- **Error**: Running `cargo build` outside the package directory (where there is no `Cargo.toml`).
  **Correction**: Navigate to the directory containing `Cargo.toml` before running `cargo build`.

- **Error**: Looking for the compiled binary in the package root instead of `target/debug/`.
  **Correction**: The compiled output is placed in `target/debug/<package_name>`.

# Common Confusions

- **Confusion**: Thinking `cargo build` also runs the program.
  **Clarification**: `cargo build` only compiles. To compile and run in one step, use `cargo run`. To run after building, manually execute `./target/debug/<name>`.

- **Confusion**: Expecting `cargo build` to produce an optimized release binary.
  **Clarification**: By default, `cargo build` produces a debug build in `target/debug/`. Release builds require `cargo build --release` (not covered in this source).

# Source Reference

Chapter 2: First Steps with Cargo. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 2 -- "Let's compile it" followed by the `cargo build` command and output
- Confidence rationale: HIGH -- the source demonstrates the command with explicit input, output, and the subsequent manual execution of the resulting binary
- Uncertainties: The source shows only the default debug build; release builds, build profiles, and flags are not covered
- Cross-reference status: All slugs reference cards in this extraction set
