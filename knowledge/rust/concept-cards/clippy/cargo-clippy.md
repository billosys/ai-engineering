---
# === CORE IDENTIFICATION ===
concept: cargo clippy
slug: cargo-clippy

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
section: "Usage"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo clippy"
  - "cargo-clippy subcommand"
  - "running clippy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
extends: []
related:
  - clippy-lint-levels
  - clippy-lint-groups
  - clippy-fix
  - clippy-driver
contrasts_with:
  - clippy-driver

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run Clippy on my project?"
  - "How do I pass lint flags to Clippy via cargo?"
  - "How do I run Clippy on a specific workspace member?"
  - "What does the -- separator do in cargo clippy commands?"
  - "How do I run Clippy on only one crate without its dependencies?"
---

# Quick Definition

`cargo clippy` is the primary command for running Clippy as a cargo subcommand, analyzing Rust code for lint violations and reporting warnings or errors based on the configured lint levels and groups.

# Core Definition

`cargo clippy` is the easiest and most common way to run the Clippy linter. It works like `cargo check` but additionally runs Clippy's lint passes over the code. By default, it runs the `clippy::all` lint group, which includes all warn-by-default lints.

Lint-specific flags are passed after a `--` separator, which tells cargo to forward the remaining arguments to the Clippy driver rather than interpreting them itself. The flags use the format `-A` (allow), `-W` (warn), and `-D` (deny) followed by a lint or lint group name.

For workspaces, all the usual cargo workspace options apply. The `-p` flag targets a specific crate, and `--no-deps` restricts linting to only the specified crate without its workspace dependencies.

# Prerequisites

- **clippy** -- Clippy must be installed as a rustup component before `cargo clippy` is available.

# Key Properties

1. Runs Clippy's lint collection on cargo-managed Rust projects
2. By default, applies the `clippy::all` lint group (all warn-by-default lints)
3. Lint flags are passed after the `--` separator: `cargo clippy -- -Wclippy::pedantic`
4. Supports all standard cargo options: `--release`, `--all-targets`, `--all-features`, `-p <crate>`, etc.
5. The `-D warnings` flag elevates all warnings to errors, causing a non-zero exit code on lint violations
6. The `--no-deps` option restricts linting to only the target crate, excluding workspace path dependencies
7. Multiple lint flags can be combined: `cargo clippy -- -Aclippy::style -Wclippy::box_default -Dclippy::perf`

# Construction / Recognition

## To Run Clippy:
1. Basic run with defaults: `cargo clippy`
2. With specific lint configuration: `cargo clippy -- -Wclippy::pedantic`
3. Deny all warnings (for CI): `cargo clippy -- -Dwarnings`
4. On a specific workspace member: `cargo clippy -p example`
5. On one crate only (no deps): `cargo clippy -p example -- --no-deps`
6. Allow all, then selectively warn: `cargo clippy -- -A clippy::all -W clippy::useless_format`

## To Recognize cargo clippy Usage:
1. The command always starts with `cargo clippy`
2. Flags before `--` are cargo flags (targets, features, package selection)
3. Flags after `--` are Clippy/rustc lint flags (-A, -W, -D followed by lint names)

# Context & Application

`cargo clippy` is the standard entry point for linting Rust code and is used both during local development and in CI pipelines. It integrates seamlessly with cargo's project model, understanding workspaces, feature flags, and build targets.

The `--` separator pattern is consistent with how cargo forwards flags to `rustc`, making it familiar to Rust developers. The command can be thought of as `cargo check` with additional lint analysis.

**Common workflow patterns:**
- During development: `cargo clippy` with defaults for quick feedback
- Before committing: `cargo clippy -- -Wclippy::pedantic` for stricter checks
- In CI: `cargo clippy --all-targets --all-features -- -Dwarnings` to catch everything

# Examples

**Example 1**: Basic Clippy run with default lints:
```bash
cargo clippy
```

**Example 2**: Configuring multiple lint levels on the command line:
```bash
cargo clippy -- -Aclippy::style -Wclippy::box_default -Dclippy::perf
```

**Example 3**: Denying all warnings (typical CI usage):
```bash
cargo clippy -- -Dwarnings
```

**Example 4**: Running on a specific workspace crate without dependencies:
```bash
cargo clippy -p example -- --no-deps
```

**Example 5**: Allowing all lints and selectively enabling specific ones:
```bash
cargo clippy -- -A clippy::all -W clippy::useless_format -W clippy::needless_return
```

# Relationships

## Builds Upon
- **clippy** -- `cargo clippy` is the cargo interface to the Clippy tool

## Enables
- **clippy-lint-levels** -- Lint levels are configured via flags passed after `--`
- **clippy-fix** -- Adding `--fix` to `cargo clippy` enables automatic suggestions

## Contrasts With
- **clippy-driver** -- `clippy-driver` is the alternative way to run Clippy without cargo, using rustc-style invocation

## Related
- **clippy-lint-groups** -- The default lint group (`clippy::all`) is what `cargo clippy` runs without additional flags
- **clippy-ci** -- CI pipelines invoke `cargo clippy` with `-Dwarnings` to fail builds on lint violations

# Common Errors

- **Error**: Passing lint flags before the `--` separator, e.g., `cargo clippy -Dwarnings`.
  **Correction**: Lint flags must come after `--`: `cargo clippy -- -Dwarnings`. Flags before `--` are interpreted by cargo, not Clippy.

- **Error**: Using `-D warnings` and being surprised that non-Clippy rustc warnings also cause failures.
  **Correction**: `-D warnings` affects all warnings, including `rustc` built-in warnings like `dead_code`. This is by design but may surprise users who only intended to enforce Clippy lints.

# Common Confusions

- **Confusion**: Thinking `cargo clippy` only checks the current crate in a workspace.
  **Clarification**: Like `cargo check`, `cargo clippy` includes workspace path dependencies. Use `--no-deps` to restrict to only the specified crate.

- **Confusion**: Believing `cargo clippy` and `cargo check` are interchangeable.
  **Clarification**: `cargo clippy` does everything `cargo check` does (type checking, borrow checking) plus runs Clippy's additional lints. It is a superset of `cargo check`.

# Source Reference

Chapter 1 (Getting Started), "Usage" section, subsection "Cargo subcommand" starting at line 37 of 01-getting-started.md. Lint configuration via CLI at lines 47-80. Workspace support at lines 147-163.

# Verification Notes

- Definition: Directly from the source -- "The easiest and most common way to run Clippy is through cargo"
- Default lint group: Stated as `clippy::all` in the source
- CLI flag syntax: All examples taken directly from the documentation
- Workspace behavior: Described in the "Workspaces" subsection with `-p` and `--no-deps` examples
- Confidence: HIGH -- all content directly from source documentation
- Cross-references: All slugs verified against planned extractions
