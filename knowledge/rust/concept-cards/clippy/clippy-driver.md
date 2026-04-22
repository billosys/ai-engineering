---
# === CORE IDENTIFICATION ===
concept: clippy-driver
slug: clippy-driver

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: advanced

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
  - "clippy driver"
  - "clippy without cargo"
  - "clippy-driver binary"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
extends: []
related:
  - cargo-clippy
contrasts_with:
  - cargo-clippy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run Clippy without cargo?"
  - "What is clippy-driver?"
  - "Can I use Clippy on non-cargo projects?"
  - "What arguments does clippy-driver accept?"
  - "Why should I not use clippy-driver as a replacement for rustc?"
---

# Quick Definition

`clippy-driver` is a binary that runs Clippy directly without `cargo`, accepting the same arguments as `rustc`. It is designed for projects that do not use cargo as their build system.

# Core Definition

For projects that do not use cargo, Clippy can be invoked via the `clippy-driver` binary. It accepts the same command-line arguments as `rustc`, making it a drop-in replacement for the compiler invocation in non-cargo build systems.

The documentation explicitly warns that `clippy-driver` is designed specifically for running Clippy's lints and should not be used as a general replacement for `rustc`. Artifacts produced by `clippy-driver` may not be optimized as expected, since the tool's purpose is lint analysis, not production compilation.

# Prerequisites

- **clippy** -- `clippy-driver` is installed as part of the Clippy component

# Key Properties

1. Accepts the same arguments as `rustc`
2. Designed for non-cargo build systems
3. Should not be used as a general `rustc` replacement
4. May produce artifacts that are not optimized as expected
5. Runs Clippy's lint passes on the compiled code
6. Installed alongside `cargo clippy` as part of the Clippy component

# Construction / Recognition

## To Use clippy-driver:
1. Invoke `clippy-driver` with the same arguments you would pass to `rustc`
2. Example: `clippy-driver --edition 2018 -Cpanic=abort foo.rs`
3. In a custom build system, replace the `rustc` invocation with `clippy-driver`

## To Recognize clippy-driver Usage:
1. Look for `clippy-driver` in build scripts, Makefiles, or custom build tool configurations
2. It appears in contexts where `rustc` would normally be used, but with Clippy linting enabled

# Context & Application

Most Rust projects use cargo as their build system, making `cargo clippy` the standard way to run Clippy. However, some projects -- particularly those with custom build systems, embedded systems with bespoke toolchains, or projects using alternative build tools like Bazel or Buck -- need to invoke the compiler directly.

`clippy-driver` fills this niche by providing Clippy's lint analysis with `rustc`-compatible command-line arguments. It is the mechanism that `cargo clippy` uses internally; the cargo subcommand sets up the build environment and then invokes `clippy-driver` in place of `rustc`.

# Examples

**Example 1**: Running Clippy on a single file without cargo:
```bash
clippy-driver --edition 2018 -Cpanic=abort foo.rs
```

**Example 2**: Using clippy-driver in a Makefile (hypothetical):
```makefile
RUSTC = clippy-driver
RUSTFLAGS = --edition 2021

%.o: %.rs
	$(RUSTC) $(RUSTFLAGS) $<
```

# Relationships

## Builds Upon
- **clippy** -- `clippy-driver` is the underlying binary that performs Clippy analysis

## Contrasts With
- **cargo-clippy** -- `cargo clippy` is the high-level interface; `clippy-driver` is the low-level binary invoked directly

## Related
- **cargo-clippy** -- `cargo clippy` internally uses `clippy-driver` as the compiler replacement

# Common Errors

- **Error**: Using `clippy-driver` for production builds and getting suboptimal binary output.
  **Correction**: `clippy-driver` is for lint analysis only. Use `rustc` for production compilation. The documentation explicitly warns that artifacts may not be optimized as expected.

- **Error**: Passing cargo-style arguments (like `--all-targets` or `-p`) to `clippy-driver`.
  **Correction**: `clippy-driver` accepts `rustc` arguments, not cargo arguments. Use `rustc`-style flags like `--edition`, `-C`, and source file paths.

# Common Confusions

- **Confusion**: Thinking `clippy-driver` provides additional functionality beyond `cargo clippy`.
  **Clarification**: `clippy-driver` provides the same lint analysis as `cargo clippy` but with a `rustc`-compatible interface. It is a lower-level tool, not a more powerful one.

- **Confusion**: Believing `clippy-driver` is needed for advanced Clippy usage.
  **Clarification**: `clippy-driver` exists solely for non-cargo projects. If your project uses cargo, `cargo clippy` is always the preferred interface.

# Source Reference

Chapter 1 (Getting Started), "Usage" section, subsection "Using Clippy without cargo: clippy-driver" at lines 165-178 of 01-getting-started.md.

# Verification Notes

- Definition: Directly from source -- "Clippy can also be used in projects that do not use cargo"
- Argument compatibility: Directly stated -- "run clippy-driver with the same arguments you use for rustc"
- Warning about optimization: Directly quoted -- "clippy-driver may produce artifacts that are not optimized as expected"
- Warning about general use: Directly stated -- "clippy-driver is designed for running Clippy and should not be used as a general replacement for rustc"
- Example: Directly from source -- `clippy-driver --edition 2018 -Cpanic=abort foo.rs`
- Confidence: HIGH -- all content directly from source documentation
- Cross-references: All slugs verified against planned extractions
