---
# === CORE IDENTIFICATION ===
concept: Clippy
slug: clippy

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "01-getting-started"
chapter_number: 1
pdf_page: null
section: "Installation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rust-clippy"
  - "clippy linter"
  - "Rust linter"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - cargo-clippy
  - clippy-lint-levels
  - clippy-lint-groups
  - clippy-configuration
  - clippy-ci
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Clippy?"
  - "How do I install Clippy?"
  - "Is Clippy included with rustup by default?"
  - "How do I install Clippy from source?"
  - "What is the relationship between Clippy and rustc?"
---

# Quick Definition

Clippy is the official Rust linter tool that provides a collection of lints to catch common mistakes, improve code style, enforce best practices, and optimize performance in Rust programs.

# Core Definition

Clippy is a lint tool for the Rust programming language, distributed as a component of the Rust toolchain via `rustup`. It analyzes Rust source code and emits warnings or errors for patterns that are likely bugs, unnecessarily complex, non-idiomatic, or suboptimal.

If you installed Rust using `rustup` with the default profile, Clippy is usually already installed. If you used the `minimal` profile, Clippy is not automatically included and must be added manually.

Clippy can be used in two ways: as a `cargo` subcommand (`cargo clippy`) or directly via the `clippy-driver` binary (a drop-in replacement for `rustc` with lint checking).

# Prerequisites

None -- Clippy is a foundational Rust development tool. It requires only a Rust toolchain installed via `rustup`.

# Key Properties

1. Clippy is distributed as a `rustup` component, making installation trivial for most Rust developers
2. It provides hundreds of lints organized into groups by category (style, correctness, complexity, performance, etc.)
3. Clippy lints are prefixed with `clippy::` to distinguish them from built-in `rustc` lints
4. It can automatically fix many of the issues it detects via `cargo clippy --fix`
5. Lint severity can be configured at multiple levels: command line, source code attributes, `Cargo.toml`, and `clippy.toml`
6. Clippy is designed to be used with a generous sprinkling of `#[allow(..)]` attributes -- not every lint applies to every codebase

# Construction / Recognition

## To Install Clippy:
1. If using `rustup` with the default profile, Clippy is already installed
2. If not installed, run: `rustup component add clippy`
3. To install for a specific toolchain: `rustup component add clippy --toolchain=<name>`
4. To build from source, follow the developer guide's Basics chapter

## To Verify Installation:
1. Run `cargo clippy --version` to check if Clippy is available
2. If the command is not found, install the component via `rustup`

# Context & Application

Clippy is a standard part of the Rust development workflow. Most Rust projects run Clippy as part of their CI pipeline to catch issues before code is merged. It complements the compiler's built-in warnings with hundreds of additional checks specific to Rust idioms and best practices.

Clippy is intended to help developers write more idiomatic Rust, but it is explicitly designed so that not all lints will apply to every project. The documentation encourages selectively allowing or denying lints to match project needs.

# Examples

**Example 1**: Installing Clippy via rustup:
```bash
rustup component add clippy
```

**Example 2**: Installing Clippy for a specific toolchain:
```bash
rustup component add clippy --toolchain=nightly
```

**Example 3**: Running Clippy on a project:
```bash
cargo clippy
```

# Relationships

## Enables
- **cargo-clippy** -- The primary interface for running Clippy on cargo-based projects
- **clippy-driver** -- The alternative interface for running Clippy without cargo
- **clippy-lint-levels** -- Configuring how severely Clippy reports issues
- **clippy-lint-groups** -- Organizing lints by category
- **clippy-configuration** -- Fine-tuning Clippy behavior via configuration files

## Related
- **clippy-ci** -- Running Clippy as part of continuous integration
- **clippy-fix** -- Automatic application of Clippy suggestions

# Common Errors

- **Error**: Running `cargo clippy` and getting "error: no such subcommand: clippy".
  **Correction**: Clippy is not installed. Run `rustup component add clippy` to install it.

- **Error**: Clippy not available after installing a toolchain with the `minimal` profile.
  **Correction**: The `minimal` profile does not include Clippy. Explicitly add it with `rustup component add clippy`.

# Common Confusions

- **Confusion**: Thinking Clippy lints replace `rustc` warnings.
  **Clarification**: Clippy provides additional lints on top of `rustc`'s built-in warnings. Both sets of warnings can appear together, and they use different prefixes (`clippy::` vs. no prefix for `rustc` lints).

- **Confusion**: Believing every Clippy lint should be fixed.
  **Clarification**: Clippy is designed to be used with selective `#[allow(..)]` attributes. Some lints are intentionally opinionated, and disabling them for parts of code or the whole project is expected.

# Source Reference

Chapter 1 (Getting Started), "Installation" section. Installation instructions from lines 1-25 of 01-getting-started.md. General Clippy description and usage overview from the "Usage" section starting at line 29.

# Verification Notes

- Definition: Synthesized from the Installation and Usage sections of the Getting Started chapter
- Installation methods: Directly from source -- `rustup component add clippy` with optional `--toolchain` flag
- Minimal profile note: Directly stated in the source documentation
- Two usage modes: Explicitly described -- cargo subcommand and clippy-driver
- Confidence: HIGH -- core tool description directly from official documentation
- Cross-references: All slugs verified against planned extractions
