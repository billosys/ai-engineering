---
# === CORE IDENTIFICATION ===
concept: Cargo Project Layout
slug: cargo-project-layout

# === CLASSIFICATION ===
category: project-organization
subcategory: directory-structure
tier: foundational

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "05-project-layout"
chapter_number: 5
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package layout"
  - "Cargo directory structure"
  - "Cargo file placement conventions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
extends: []
related:
  - cargo-toml-vs-cargo-lock
  - cargo-test-command
  - cargo-manifest
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the conventional directory structure for a Cargo package?"
  - "Where does the default library file go?"
  - "Where does the default executable file go?"
  - "How do I add additional binary targets to my package?"
  - "Where do integration tests, benchmarks, and examples go?"
  - "How do I organize a multi-file binary, example, bench, or test?"
  - "What naming conventions do Cargo targets follow?"
---

# Quick Definition

Cargo uses a conventional directory structure where `Cargo.toml` and `Cargo.lock` live at the package root, source code goes in `src/`, integration tests in `tests/`, benchmarks in `benches/`, and examples in `examples/`. The default library file is `src/lib.rs` and the default executable is `src/main.rs`, with additional binaries placed in `src/bin/`.

# Core Definition

The source states: "Cargo uses conventions for file placement to make it easy to dive into a new Cargo package" (Ch. 5). The layout is convention-driven rather than configuration-driven, meaning that placing files in the right directories is sufficient for Cargo to discover and build them as the correct target types. The default library crate root is `src/lib.rs`, the default binary crate root is `src/main.rs`, and additional binary targets can be placed in `src/bin/`. Integration tests go in `tests/`, benchmarks in `benches/`, and examples in `examples/`.

For multi-file targets (binaries, examples, benches, or integration tests), the source specifies: "place a `main.rs` file along with the extra modules within a subdirectory." The directory name becomes the executable name. By convention, target names use `kebab-case` while module names use `snake_case`.

# Prerequisites

- **Creating a Cargo Project** -- you need an understanding of how a project is created before exploring its full layout

# Key Properties

1. **Cargo.toml and Cargo.lock at root**: The manifest and lockfile live at the package root
2. **src/ for source code**: All production source code goes in the `src` directory
3. **src/lib.rs**: Default library crate root
4. **src/main.rs**: Default binary crate root
5. **src/bin/**: Additional binary executables, each `.rs` file or subdirectory is a separate binary
6. **tests/**: Integration tests (must import the crate explicitly)
7. **benches/**: Benchmarks
8. **examples/**: Example programs
9. **Multi-file targets**: Use a subdirectory with a `main.rs` and additional modules
10. **Naming conventions**: Target names in `kebab-case`, module names in `snake_case`
11. **Auto-discovery**: Cargo infers target names from file and directory names without explicit configuration

# Construction / Recognition

## Complete Conventional Layout:
```text
.
├── Cargo.lock
├── Cargo.toml
├── src/
│   ├── lib.rs
│   ├── main.rs
│   └── bin/
│       ├── named-executable.rs
│       ├── another-executable.rs
│       └── multi-file-executable/
│           ├── main.rs
│           └── some_module.rs
├── benches/
│   ├── large-input.rs
│   └── multi-file-bench/
│       ├── main.rs
│       └── bench_module.rs
├── examples/
│   ├── simple.rs
│   └── multi-file-example/
│       ├── main.rs
│       └── ex_module.rs
└── tests/
    ├── some-integration-tests.rs
    └── multi-file-test/
        ├── main.rs
        └── test_module.rs
```

## Key Directory Roles:
- `src/` -- production source code (library and binary crates)
- `src/bin/` -- additional binary executables
- `tests/` -- integration tests
- `benches/` -- benchmarks
- `examples/` -- example programs

# Context & Application

The Cargo project layout is one of the key conventions that makes it possible to "dive into a new Cargo package" easily. Because file placement determines target type, developers rarely need to manually configure targets in `Cargo.toml`. This convention-over-configuration approach is central to Cargo's design philosophy described in Chapter 1. The layout also enables auto-discovery: Cargo automatically recognizes new binaries, tests, examples, and benchmarks when files appear in the correct directories. This card complements the cargo-getting-started cards by presenting the full conventional layout, not just the minimal structure generated by `cargo new`.

# Examples

**Example 1** (Ch. 5): Default library and binary locations:
> "The default library file is `src/lib.rs`."
> "The default executable file is `src/main.rs`."
> "Other executables can be placed in `src/bin/`."

**Example 2** (Ch. 5): Integration tests location:
> "Integration tests go in the `tests` directory."

**Example 3** (Ch. 5): Multi-file target organization:
> "If a binary, example, bench, or integration test consists of multiple source files, place a `main.rs` file along with the extra modules within a subdirectory of the `src/bin`, `examples`, `benches`, or `tests` directory. The name of the executable will be the directory name."

**Example 4** (Ch. 5): Naming convention:
> "By convention, binaries, examples, benches and integration tests follow `kebab-case` naming style... Modules within those targets are `snake_case` following the Rust standard."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- `cargo new` generates the minimal subset of this layout

## Enables
- **cargo-test-command** -- the `tests/` directory is where integration tests expected by `cargo test` live
- **cargo-build-performance** -- understanding the layout helps with workspace organization for build optimization

## Related
- **cargo-toml-vs-cargo-lock** -- both files live at the package root as part of the layout
- **cargo-manifest** -- `Cargo.toml` is the manifest that lives at the root of the layout

## Contrasts With
- None within this source

# Common Errors

- **Error**: Placing integration tests in `src/` instead of `tests/`.
  **Correction**: Tests in `src/` should be unit tests (using `#[cfg(test)]` modules). Integration tests belong in the `tests/` directory and must import the crate.

- **Error**: Creating a `main.rs` directly in `src/bin/` expecting it to be a separate binary.
  **Correction**: Files directly in `src/bin/` become separate binaries named after the file (e.g., `src/bin/tool.rs` becomes a `tool` binary). A `main.rs` in a subdirectory of `src/bin/` is for multi-file binaries.

- **Error**: Using `snake_case` for binary target names.
  **Correction**: By convention, binary, example, bench, and integration test names use `kebab-case`.

# Common Confusions

- **Confusion**: Thinking you must configure every target in `Cargo.toml`.
  **Clarification**: Cargo uses auto-discovery based on file placement. Placing a file in `src/bin/` automatically makes it a binary target without any `Cargo.toml` configuration.

- **Confusion**: Thinking `src/lib.rs` and `src/main.rs` are mutually exclusive.
  **Clarification**: A package can have both -- one library crate and one or more binary crates. The full layout example shows both `lib.rs` and `main.rs` coexisting.

- **Confusion**: Wondering how multi-file binaries work without explicit configuration.
  **Clarification**: A subdirectory in `src/bin/` with a `main.rs` and additional module files becomes a single binary named after the directory. Cargo discovers this automatically.

# Source Reference

Chapter 5: Package Layout. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 5 -- "Cargo uses conventions for file placement to make it easy to dive into a new Cargo package"
- Confidence rationale: HIGH -- the source provides the complete directory tree and explains each convention
- Uncertainties: Manual target configuration (overriding auto-discovery) is referenced but not detailed in this chapter
- Cross-reference status: cargo-manifest references cargo-getting-started cards; other slugs are within this extraction set
