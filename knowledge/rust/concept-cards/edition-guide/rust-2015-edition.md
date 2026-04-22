---
# === CORE IDENTIFICATION ===
concept: Rust 2015 Edition
slug: rust-2015-edition

# === CLASSIFICATION ===
category: edition-system
subcategory: edition-versions
tier: intermediate

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "Rust 2015"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust 2015"
  - "edition 2015"
  - "the stability edition"
  - "default edition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
extends: []
related:
  - edition-migration
  - edition-interoperability
  - rust-2018-edition
contrasts_with:
  - rust-2018-edition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Rust 2015 edition?"
  - "What is the default edition if none is specified?"
  - "What is the theme of Rust 2015?"
  - "Why is 2015 the default edition?"
---

# Quick Definition

Rust 2015 is the first and default Rust edition, coinciding with the release of Rust 1.0 in May 2015. Its theme is "stability" -- it marked the transition from Rust's pre-1.0 era of daily breaking changes to the commitment of backwards compatibility. It is the edition used when no `edition` field is specified in `Cargo.toml`.

# Core Definition

As described in the source: "Rust 2015 has a theme of 'stability'. It commenced with the release of 1.0, and is the 'default edition'." (Ch. 2: Rust 2015). The edition system was conceived in late 2017, but Rust 1.0 was released in May 2015, so 2015 was retroactively designated as the first edition. The source notes: "'Stability' is the theme of Rust 2015 because 1.0 marked a huge change in Rust development. Previous to Rust 1.0, Rust was changing on a daily basis. This made it very difficult to write large software in Rust, and made it difficult to learn."

Rust 2015 serves as the baseline from which all subsequent editions diverge. You never migrate *to* Rust 2015 -- you only migrate *away* from it.

# Prerequisites

- **rust-editions** -- Understanding the edition system to contextualize what Rust 2015 represents

# Key Properties

1. **Default edition**: Used when no `edition` field is present in `Cargo.toml`
2. **Theme of stability**: Represents the commitment to backwards compatibility after Rust 1.0
3. **Retroactive designation**: The edition system was created later (2017); 2015 was applied retroactively
4. **Baseline edition**: All other editions are defined relative to changes from 2015
5. **One-way migration**: You transition away from 2015, never to it
6. **Pre-edition syntax rules**: Uses `extern crate` for imports, `mod.rs` for module files, different `use` path rules

# Construction / Recognition

## Identifying a Rust 2015 Project:
- The `Cargo.toml` has `edition = "2015"`, or
- The `Cargo.toml` has no `edition` field at all (2015 is the implicit default)

## Characteristics of 2015-era Code:
- `extern crate` declarations at the crate root
- `mod.rs` files for modules with submodules
- `::` prefix to reference external crates in submodules
- Trait functions with anonymous parameters (e.g., `fn foo(&self, i32)`)
- `dyn` not required for trait objects (bare `Trait` used in type position)

# Context & Application

Rust 2015 is primarily relevant as the starting point for edition migration. Most actively maintained crates have migrated to newer editions, but the 2015 edition remains supported indefinitely per Rust's stability guarantee. Understanding 2015-era syntax patterns is useful for reading older code and for understanding what the subsequent editions changed and why.

# Examples

**Example 1** (Ch 2): The theme of stability:
> "'Stability' is the theme of Rust 2015 because 1.0 marked a huge change in Rust development. Previous to Rust 1.0, Rust was changing on a daily basis."

**Example 2** (Ch 1): Setting a project to the 2015 edition explicitly:
```toml
[package]
name = "foo"
version = "0.1.0"
edition = "2015"
```

**Example 3** (Ch 1): Default edition behavior:
> "If there's no `edition` key, Cargo will default to Rust 2015."

**Example 4** (Ch 2): One-way migration:
> "Since it's the default edition, there's no way to port your code to Rust 2015; it just is. You'll be transitioning away from 2015, but never really to 2015."

# Relationships

## Builds Upon
- **rust-editions** -- 2015 is the first edition in the system

## Enables
- **edition-migration** -- 2015 is typically the starting point for migration to newer editions
- **path-module-changes-2018** -- the 2018 module changes are defined relative to 2015's module system

## Related
- **edition-interoperability** -- 2015 crates remain fully compatible with crates on any edition
- **edition-migration** -- automated tooling supports migrating from 2015 to 2018 and beyond

## Contrasts With
- **rust-2018-edition** -- 2018 changed many 2015-era patterns (extern crate, module paths, anonymous parameters)

# Common Errors

- **Error**: Creating a new project without specifying an edition and assuming it uses the latest edition.
  **Correction**: While `cargo new` defaults to the latest edition, manually created `Cargo.toml` files without an `edition` field default to 2015.

# Common Confusions

- **Confusion**: Thinking Rust 2015 is deprecated or unsupported.
  **Clarification**: Rust 2015 code continues to compile on the latest Rust compiler. The stability guarantee ensures ongoing support. Migration to newer editions is encouraged but never required.

- **Confusion**: Believing the edition system existed from the start.
  **Clarification**: "The edition system was conceived in late 2017, but Rust 1.0 was released in May of 2015." The 2015 edition was retroactively designated.

# Source Reference

Chapter 2: Rust 2015. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 2 -- "Rust 2015 has a theme of 'stability'. It commenced with the release of 1.0, and is the 'default edition'."
- Confidence rationale: HIGH -- though the source chapter is brief, the content is clear and unambiguous
- Uncertainties: None
- Cross-reference status: rust-editions, edition-migration, edition-interoperability, rust-2018-edition are in this extraction set
