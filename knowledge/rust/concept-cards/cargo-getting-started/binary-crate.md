---
# === CORE IDENTIFICATION ===
concept: Binary Crate
slug: binary-crate

# === CLASSIFICATION ===
category: package-management
subcategory: crate-types
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
  - binary program
  - bin crate

# === TYPED RELATIONSHIPS ===
prerequisites:
  - crate
extends:
  - crate
related:
  - cargo-package
  - cargo-new
  - cargo-run
contrasts_with:
  - library-crate

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binary crate?"
  - "What is the difference between a binary crate and a library crate?"
---

# Quick Definition

A binary crate is a crate that compiles to an executable program. It is the default crate type created by `cargo new` and is identified by having a `src/main.rs` entry point.

# Core Definition

The source explicitly identifies a binary crate when describing the output of `cargo new`: "Cargo generated a 'hello world' program for us, otherwise known as a binary crate" (Ch. 2: First Steps with Cargo). A binary crate produces a runnable executable. The source further clarifies that binary is the default: "Cargo defaults to `--bin` to make a binary program. To make a library, we would pass `--lib`, instead."

# Prerequisites

- **Crate** -- A binary crate is a specific type of crate; understanding the general crate concept is needed first.

# Key Properties

1. Compiles to an executable program
2. Entry point is `src/main.rs`
3. Contains a `fn main()` function
4. Is the default crate type created by `cargo new` (via `--bin`)
5. Can be run with `cargo run` or directly from the `target/` directory
6. The compiled binary is placed in `target/debug/` by default

# Construction / Recognition

## To Create a Binary Crate:
1. Run `cargo new <name>` (defaults to `--bin`)
2. Or explicitly: `cargo new --bin <name>`
3. The generated `src/main.rs` contains the binary entry point

## To Recognize a Binary Crate:
1. Check for `src/main.rs` in the package
2. Verify it contains a `fn main()` function
3. The compiled output will be an executable in `target/debug/<name>`

# Context & Application

Binary crates are the most common starting point for new Rust developers. They produce programs that can be executed directly. The Getting Started guide uses a binary crate exclusively for its tutorial, demonstrating the create-build-run workflow. Binary crates are distinguished from library crates, which provide reusable code but no executable entry point.

# Examples

**Example 1** (Ch 2): The generated binary crate source (`src/main.rs`):
```rust
fn main() {
    println!("Hello, world!");
}
```

**Example 2** (Ch 2): Running the compiled binary directly:
```console
$ ./target/debug/hello_world
Hello, world!
```

**Example 3** (Ch 2): The source explicitly labels the generated code:
> "Cargo generated a 'hello world' program for us, otherwise known as a binary crate."

# Relationships

## Builds Upon
- **Crate** -- a binary crate is a specialization of the crate concept

## Enables
- **cargo-run** -- `cargo run` is specifically useful for binary crates (library crates have no executable to run)

## Related
- **cargo-new** -- creates binary crates by default
- **cargo-package** -- a binary crate lives within a package
- **cargo-build** -- compiles the binary crate to an executable

## Contrasts With
- **Library Crate** -- a library crate provides reusable code but no executable; a binary crate produces a runnable program

# Common Errors

- **Error**: Removing or renaming the `fn main()` function in `src/main.rs`.
  **Correction**: Binary crates require a `fn main()` function as the program entry point.

- **Error**: Trying to run a library crate with `cargo run`.
  **Correction**: Only binary crates can be run. Library crates have no `main()` entry point.

# Common Confusions

- **Confusion**: Thinking that a binary crate cannot also depend on library crates.
  **Clarification**: Binary crates commonly depend on library crates listed in the `[dependencies]` section of `Cargo.toml`.

- **Confusion**: Believing "binary" means the output is in binary format as opposed to text.
  **Clarification**: "Binary" here means "executable program" -- a compiled application that can be run.

# Source Reference

Chapter 2: First Steps with Cargo. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 2 -- "otherwise known as a binary crate" and "Cargo defaults to `--bin` to make a binary program"
- Confidence rationale: HIGH -- the source explicitly uses the term "binary crate" and describes what it is and how it is created
- Uncertainties: None for the core concept; the source does not cover advanced binary crate features (multiple binaries, etc.)
- Cross-reference status: All slugs reference cards in this extraction set
