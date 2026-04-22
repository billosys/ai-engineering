---
# === CORE IDENTIFICATION ===
concept: Library Crate
slug: library-crate

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
extraction_confidence: low

# === VARIANTS (authority control) ===
aliases:
  - library
  - lib crate

# === TYPED RELATIONSHIPS ===
prerequisites:
  - crate
extends:
  - crate
related:
  - cargo-new
  - cargo-package
contrasts_with:
  - binary-crate

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a library crate?"
  - "What is the difference between a binary crate and a library crate?"
---

# Quick Definition

A library crate is a crate that provides reusable code for other crates to depend on, rather than compiling to an executable program. It is created with `cargo new --lib`.

# Core Definition

The Cargo Getting Started guide mentions library crates only in contrast to binary crates: "Cargo defaults to `--bin` to make a binary program. To make a library, we would pass `--lib`, instead" (Ch. 2: First Steps with Cargo). The source does not elaborate on library crate structure or usage beyond this single reference.

# Prerequisites

- **Crate** -- A library crate is a specific type of crate; understanding the general crate concept is needed first.

# Key Properties

1. Created by passing `--lib` to `cargo new`
2. Provides reusable code rather than an executable program
3. Entry point is `src/lib.rs` (not `src/main.rs`)
4. Cannot be run with `cargo run` (no executable output)
5. Contrasts with binary crates, which are the default

# Construction / Recognition

## To Create a Library Crate:
1. Run `cargo new --lib <name>`
2. The generated package will contain `src/lib.rs` instead of `src/main.rs`

## To Recognize a Library Crate:
1. Check for `src/lib.rs` in the package (instead of `src/main.rs`)
2. There is no `fn main()` function

# Context & Application

Library crates are fundamental to code reuse in the Rust ecosystem. While the Getting Started guide focuses on binary crates, it acknowledges the existence of library crates as an alternative. Libraries are what get published to crates.io for other developers to use as dependencies. The full treatment of library crates is deferred to later sections of the Cargo documentation.

# Examples

**Example 1** (Ch 2): The source's only mention of library creation:
> "Cargo defaults to `--bin` to make a binary program. To make a library, we would pass `--lib`, instead."

# Relationships

## Builds Upon
- **Crate** -- a library crate is a specialization of the crate concept

## Enables
- Code reuse across packages (not detailed in this source)

## Related
- **cargo-new** -- creates library crates when passed `--lib`
- **cargo-package** -- a library crate lives within a package

## Contrasts With
- **Binary Crate** -- a binary crate compiles to an executable; a library crate provides reusable code with no executable output

# Common Errors

- **Error**: Trying to run a library crate with `cargo run`.
  **Correction**: Library crates produce no executable. Use `cargo build` to compile, or add a binary crate that depends on the library.

# Common Confusions

- **Confusion**: Thinking a package must contain either a binary or a library, but not both.
  **Clarification**: A package can contain both a binary crate (`src/main.rs`) and a library crate (`src/lib.rs`), though this is not discussed in the Getting Started guide.

- **Confusion**: Believing `--lib` is the default for `cargo new`.
  **Clarification**: The default is `--bin` (binary). You must explicitly pass `--lib` to create a library.

# Source Reference

Chapter 2: First Steps with Cargo. Single sentence reference. No page numbers (online documentation source).

# Verification Notes

- Definition source: The source provides only a single sentence contrasting library creation with binary creation; no standalone definition is given
- Confidence rationale: LOW -- the source mentions library crates only once, in a single sentence, with no examples, structure details, or further elaboration
- Uncertainties: Almost all properties beyond the `--lib` flag are inferred from general Rust ecosystem knowledge rather than stated in this source
- Cross-reference status: All slugs reference cards in this extraction set
