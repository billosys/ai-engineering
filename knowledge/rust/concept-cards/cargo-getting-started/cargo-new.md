---
# === CORE IDENTIFICATION ===
concept: Cargo New
slug: cargo-new

# === CLASSIFICATION ===
category: tooling
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
  - "cargo new"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustup
extends: []
related:
  - cargo-package
  - cargo-manifest
  - binary-crate
  - library-crate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a new Cargo package?"
  - "What is the difference between a binary crate and a library crate?"
---

# Quick Definition

`cargo new` is the Cargo CLI command that generates a new package with a standard directory structure, a `Cargo.toml` manifest, and a starter source file. It defaults to creating a binary crate but can create a library crate with the `--lib` flag.

# Core Definition

The `cargo new` command creates a new Cargo package. As described in the source: "To start a new package with Cargo, use `cargo new`" (Ch. 2: First Steps with Cargo). The command generates a directory containing a `Cargo.toml` manifest and a `src/` directory with an appropriate starter file. By default, it creates a binary program (`--bin`); passing `--lib` creates a library instead.

# Prerequisites

- **Rustup** -- Rust and Cargo must be installed (via rustup) before the `cargo new` command is available.

# Key Properties

1. Creates a new directory named after the package
2. Generates a `Cargo.toml` manifest file with package metadata
3. Creates a `src/` directory with a starter source file (`main.rs` for binary, `lib.rs` for library)
4. Defaults to `--bin` (binary crate)
5. Accepts `--lib` flag to create a library crate instead
6. The generated binary includes a "Hello, world!" program

# Construction / Recognition

## To Create a New Binary Package:
1. Run `cargo new <package_name>`
2. A directory named `<package_name>` is created
3. Inside it: `Cargo.toml` and `src/main.rs`

## To Create a New Library Package:
1. Run `cargo new --lib <package_name>`
2. A directory named `<package_name>` is created
3. Inside it: `Cargo.toml` and `src/lib.rs`

# Context & Application

`cargo new` is the standard way to start any new Rust project. It establishes the conventional directory layout that all Cargo tooling expects and pre-populates the manifest with sensible defaults. The generated structure is minimal but complete enough to immediately build and run.

# Examples

**Example 1** (Ch 2): Creating a new binary package:
```console
$ cargo new hello_world
```

**Example 2** (Ch 2): The generated directory structure:
```
.
├── Cargo.toml
└── src
    └── main.rs
```

**Example 3** (Ch 2): The generated `src/main.rs` content:
```rust
fn main() {
    println!("Hello, world!");
}
```

**Example 4** (Ch 2): Creating a library crate instead:
> "Cargo defaults to `--bin` to make a binary program. To make a library, we would pass `--lib`, instead."

# Relationships

## Builds Upon
- **Rustup** -- Cargo must be installed before `cargo new` can be used

## Enables
- **cargo-package** -- `cargo new` is how packages are created
- **cargo-manifest** -- `cargo new` generates the initial `Cargo.toml`
- **binary-crate** -- default output of `cargo new`
- **library-crate** -- output of `cargo new --lib`
- **cargo-build** -- the generated package can be built immediately
- **cargo-run** -- the generated binary package can be run immediately

## Related
- **cargo-package** -- `cargo new` creates a new package
- **cargo-manifest** -- `cargo new` generates the manifest file

## Contrasts With
- None within this source

# Common Errors

- **Error**: Running `cargo new` with a package name that contains invalid characters (e.g., hyphens that conflict with Rust identifier rules).
  **Correction**: Use underscores in package names (e.g., `hello_world`), as shown in the source example.

- **Error**: Trying to run `cargo build` or `cargo run` without first navigating into the created package directory.
  **Correction**: `cd` into the directory created by `cargo new` before running other Cargo commands.

# Common Confusions

- **Confusion**: Thinking `cargo new` only creates binary projects.
  **Clarification**: `cargo new` defaults to `--bin` (binary) but supports `--lib` for library creation.

- **Confusion**: Believing you need to manually create `Cargo.toml` and the directory structure.
  **Clarification**: `cargo new` generates the complete initial structure automatically.

# Source Reference

Chapter 2: First Steps with Cargo. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 2 -- "To start a new package with Cargo, use `cargo new`"
- Confidence rationale: HIGH -- the source demonstrates the command with explicit examples and output
- Uncertainties: None for core functionality; the source does not cover all `cargo new` flags or options
- Cross-reference status: All slugs reference cards in this extraction set
