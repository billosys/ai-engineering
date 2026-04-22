---
# === CORE IDENTIFICATION ===
concept: Rust 2018 Edition
slug: rust-2018-edition

# === CLASSIFICATION ===
category: edition-2018
subcategory: edition-overview
tier: intermediate

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "Rust 2018"
chapter_number: 3
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust 2018"
  - "edition 2018"
  - "the productivity edition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
extends:
  - rust-2015-edition
related:
  - edition-migration
  - edition-interoperability
  - path-module-changes-2018
  - async-await-keywords-2018
  - rust-2021-edition
contrasts_with:
  - rust-2015-edition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Rust 2018 edition?"
  - "What changes were introduced in Rust 2018?"
  - "What was the theme of Rust 2018?"
  - "When was Rust 2018 released?"
  - "What are anonymous trait parameters and why were they deprecated?"
  - "What Cargo changes were made in Rust 2018?"
---

# Quick Definition

Rust 2018, released with Rust 1.31.0 (December 2018), was the first edition created alongside the edition system itself (RFC #2052). Its theme is "productivity," and it introduced the overhauled module/path system, new keywords (`dyn`, `async`, `await`, `try`), deprecation of anonymous trait function parameters, method dispatch changes for raw pointers, and Cargo behavior changes.

# Core Definition

As described in the source: "The edition system was created for the release of Rust 2018. The release of the Rust 2018 edition coincided with a number of other features all coordinated around the theme of productivity." (Ch. 3: Rust 2018). The majority of features released alongside Rust 2018 were backwards compatible and are available on all editions. However, several changes required the edition mechanism, most notably the module system overhaul.

The edition-specific changes in Rust 2018 include:
1. **Path and module system changes** -- simplified and unified path resolution, removed need for `extern crate`, allowed `foo.rs` alongside `foo/` directory
2. **New keywords** -- `dyn` (strict), `async`/`await` (strict), `try` (reserved)
3. **Anonymous trait function parameters deprecated** -- `fn foo(&self, u8)` must become `fn foo(&self, _: u8)`
4. **Method dispatch for raw pointers** -- the `tyvar_behind_raw_pointer` lint became a hard error
5. **Cargo changes** -- target discovery and `cargo install` behavior changes

# Prerequisites

- **rust-editions** -- Understanding the edition system to contextualize what Rust 2018 is

# Key Properties

1. **Theme: productivity** -- all changes aimed at making Rust easier and more ergonomic to use
2. **First "designed" edition**: The edition system was created specifically for this release
3. **Released with Rust 1.31.0** (December 6, 2018)
4. **RFC #2052**: The RFC that proposed both the edition system and the 2018 edition
5. **Module system overhaul**: The most significant change, simplifying path and import resolution
6. **New keyword reservations**: Enabled future language features (async/await, dyn Trait, try blocks)

# Construction / Recognition

## Identifying Rust 2018 Features:
- No `extern crate` declarations (except sysroot crates)
- `crate::` prefix for current crate references
- `dyn Trait` syntax for trait objects
- Named parameters in trait function declarations
- `foo.rs` alongside `foo/` directory (instead of `foo/mod.rs`)

## Edition-Specific vs. Edition-Independent:
Many features released around the same time as Rust 2018 do not require the edition:
- Only the module system changes, keyword reservations, anonymous parameter deprecation, and method dispatch changes are edition-gated
- Features like `impl Trait` in argument/return position, NLL (Non-Lexical Lifetimes), and many others were made available on all editions

# Context & Application

Rust 2018 was a landmark release that demonstrated the viability of the edition system. It showed that Rust could make significant ergonomic improvements (particularly the module system simplification) without fragmenting the ecosystem. The "productivity" theme reflected the Rust community's focus on reducing friction in everyday Rust programming after the "stability" foundation of 2015 was established.

# Examples

**Example 1** (Ch 3): Anonymous trait parameters deprecated:
```rust
// Rust 2015 -- allowed
trait Foo {
    fn foo(&self, u8);
}

// Rust 2018 -- parameter must be named
trait Foo {
    fn foo(&self, baz: u8);
}
```

**Example 2** (Ch 3): Method dispatch hard error:
> The `tyvar_behind_raw_pointer` lint is now a hard error in Rust 2018.

**Example 3** (Ch 3): Cargo behavior changes:
- If there is a target definition in `Cargo.toml`, it no longer automatically disables automatic discovery of other targets
- Target paths of the form `src/{target_name}.rs` are no longer inferred for targets where the `path` field is not set
- `cargo install` for the current directory is no longer allowed; you must specify `cargo install --path .`

**Example 4** (Ch 3): The `dyn Trait` syntax:
```rust
// Rust 2015
fn function1() -> Box<Trait> { ... }

// Rust 2018
fn function2() -> Box<dyn Trait> { ... }
```

**Example 5** (Ch 3): Edition metadata:
| Info | |
| --- | --- |
| RFC | #2052 (which also proposed the Edition system) |
| Release version | 1.31.0 |

# Relationships

## Builds Upon
- **rust-editions** -- 2018 is an edition within the edition system
- **rust-2015-edition** -- 2018 changes are defined relative to 2015 behavior

## Enables
- **rust-2021-edition** -- the next edition after 2018

## Related
- **path-module-changes-2018** -- the major module system overhaul (detailed card)
- **async-await-keywords-2018** -- new keyword reservations (detailed card)
- **edition-migration** -- automated tooling supports migrating to 2018
- **edition-interoperability** -- 2018 crates interoperate with all other editions

## Contrasts With
- **rust-2015-edition** -- 2018 replaced many 2015-era patterns and syntax

# Common Errors

- **Error**: Using anonymous parameters in trait function declarations in Rust 2018.
  **Correction**: All parameters must have names in 2018. Use `_: type` for unused parameters: `fn foo(&self, _: u8)`.

- **Error**: Running `cargo install` in the current directory without `--path .` in Rust 2018+.
  **Correction**: Use `cargo install --path .` to install the current package.

# Common Confusions

- **Confusion**: Thinking all features released alongside Rust 2018 require the 2018 edition.
  **Clarification**: "The majority of those features were backwards compatible and are now available on all editions; however, some of those changes required the edition mechanism." Only path/module changes, keywords, anonymous parameters, and method dispatch are edition-gated.

- **Confusion**: Assuming Rust 2018 was the first edition.
  **Clarification**: Rust 2015 is the first edition (retroactively designated). Rust 2018 was the first edition designed alongside the edition system.

- **Confusion**: Thinking the `async`/`await` feature was usable in Rust 1.31.0 (the 2018 release).
  **Clarification**: The keywords were reserved in 1.31.0, but the async/await feature was stabilized later in Rust 1.39.0.

# Source Reference

Chapter 3: Rust 2018; all sections (overview, path changes, anonymous parameters, new keywords, method dispatch, Cargo changes). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 3 -- "The edition system was created for the release of Rust 2018. The release of the Rust 2018 edition coincided with a number of other features all coordinated around the theme of productivity."
- Confidence rationale: HIGH -- the source provides comprehensive documentation of all 2018 edition changes
- Uncertainties: The `try` keyword feature remains unstabilized; some Cargo changes may have evolved since the source was written
- Cross-reference status: rust-editions, rust-2015-edition, path-module-changes-2018, async-await-keywords-2018, edition-migration, edition-interoperability are in this extraction set; rust-2021-edition from Agent B
