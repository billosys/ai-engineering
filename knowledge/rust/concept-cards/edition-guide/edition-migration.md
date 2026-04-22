---
# === CORE IDENTIFICATION ===
concept: Edition Migration
slug: edition-migration

# === CLASSIFICATION ===
category: edition-system
subcategory: migration
tier: foundational

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "What Are Editions"
chapter_number: 1
pdf_page: null
section: "Transitioning an existing project to a new edition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo fix --edition"
  - "edition upgrade"
  - "edition transition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
extends: []
related:
  - edition-interoperability
  - rust-2018-edition
  - rust-2021-edition
  - rust-2024-edition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I migrate my Rust project to a new edition?"
  - "What does cargo fix --edition do?"
  - "What are the steps to upgrade from one Rust edition to another?"
  - "How does cargo fix handle automatic migration?"
  - "What do I do when cargo fix can't automatically fix something?"
  - "How do I migrate a large workspace incrementally?"
  - "How do I handle macros during edition migration?"
---

# Quick Definition

Edition migration is the process of updating a Rust crate from one edition to another, primarily using `cargo fix --edition` to automatically apply source code transformations, followed by updating the `edition` field in `Cargo.toml`. The process is designed to be largely automated, with manual intervention needed only for edge cases like macros and generated code.

# Core Definition

Rust provides automated tooling to migrate between editions. As described in the source: "Rust aims to make upgrading to a new edition an easy process. When a new edition releases, crate authors may use automatic migration tooling within `cargo` to migrate." (Ch. 1: What Are Editions). The `cargo fix --edition` command works by running `cargo check` with special edition-compatibility lints enabled, detecting code that may not compile in the next edition, and automatically applying fixes to the source code. The process is iterative -- Cargo may run `cargo check` multiple times as one set of fixes can trigger new warnings requiring further fixes.

# Prerequisites

- **rust-editions** -- Understanding what editions are and why migration is needed

# Key Properties

1. **Five-step process**: Update dependencies, run `cargo fix --edition`, update `Cargo.toml`, build/test, reformat
2. **Lint-driven**: Migration uses edition-specific lint groups (e.g., `rust-2021-compatibility`) to detect incompatible code
3. **Safe rollback**: If fixes fail, `cargo fix` automatically backs out changes and displays a warning
4. **Iterative**: `cargo fix` may run multiple passes as fixes can trigger new warnings
5. **Incremental**: Large projects can be migrated one package or one target at a time
6. **Idiomatic upgrades**: `cargo fix --edition-idioms` can additionally update code to use newer idiomatic patterns

# Construction / Recognition

## Standard Migration Steps:
1. Run `cargo update` to update dependencies to latest versions
2. Run `cargo fix --edition` to automatically transform source code
3. Edit `Cargo.toml` and set the `edition` field to the next edition (e.g., `edition = "2024"`)
4. Run `cargo build` or `cargo test` to verify the fixes worked
5. Run `cargo fmt` to reformat the project

## Advanced Migration Strategies:
- **Multiple configurations**: Run `cargo fix` with `--target` for different platforms or `--all-features` for feature-gated code
- **Large workspaces**: Migrate one package at a time; within a package, use target selection flags
- **Broken code**: Use `--broken-code` to keep partial fixes and manually resolve remaining issues
- **Individual lints**: Apply individual migration lints one at a time using `#![warn(lint_name)]`
- **Per-target editions**: Set `edition` on individual `[[bin]]` targets in `Cargo.toml` for incremental migration

# Context & Application

Edition migration is the primary mechanism by which Rust projects adopt new language features that require backwards-incompatible syntax changes. The automated tooling handles the vast majority of cases, but manual intervention may be required for proc macros, `macro_rules!` macros (due to edition hygiene), documentation tests, and build-script-generated code. The migration is designed to produce code that is valid on both the old and new editions, allowing incremental adoption.

# Examples

**Example 1** (Ch 1): Migrating anonymous trait parameters from 2015 to 2018:

Before (`src/lib.rs`):
```rust
trait Foo {
    fn foo(&self, i32);
}
```

After running `cargo fix --edition`:
```rust
trait Foo {
    fn foo(&self, _: i32);
}
```

**Example 2** (Ch 1): Handling keyword conflicts during migration:
> "When migrating to Rust 2018, anything named `async` will now use the equivalent raw identifier syntax: `r#async`."

**Example 3** (Ch 1): Removing idiomatic 2015 patterns:
```rust
// Before (Rust 2015 idiom):
extern crate rand;

// After running cargo fix --edition-idioms:
// The extern crate line is removed entirely
```

**Example 4** (Ch 1): Migrating a macro that uses `dyn` as identifier:
```rust
#[macro_export]
macro_rules! foo {
    () => {
        let dyn = 1;
        println!("it is {}", dyn);
    };
}
```
> This macro cannot be automatically fixed by `cargo fix --edition`. When the crate moves to 2018, `dyn` becomes a keyword, and the macro will fail when called from any crate. Manual intervention is required.

**Example 5** (Ch 1): Migrating to an unstable (nightly) edition:
```console
$ rustup update nightly
$ cargo +nightly fix --edition
# Edit Cargo.toml: add cargo-features = ["edition20xx"] at top
# Edit Cargo.toml: set edition = "20xx"
$ cargo +nightly check
```

# Relationships

## Builds Upon
- **rust-editions** -- migration moves a crate from one edition to another

## Enables
- **rust-2018-edition** -- migration is how projects adopt the 2018 edition
- **rust-2021-edition** -- migration is how projects adopt the 2021 edition
- **rust-2024-edition** -- migration is how projects adopt the 2024 edition

## Related
- **edition-interoperability** -- migration is not required for crates to interoperate across editions
- **path-module-changes-2018** -- one of the changes that requires migration tooling

## Contrasts With
- None within this source

# Common Errors

- **Error**: Running `cargo fix --edition` but forgetting to update the `edition` field in `Cargo.toml`.
  **Correction**: After running `cargo fix --edition`, you must manually change the `edition` value in `Cargo.toml` to the target edition.

- **Error**: Assuming `cargo fix --edition` will fix documentation tests.
  **Correction**: "At this time, `cargo fix` is not able to update documentation tests." Run `cargo test` after migration and fix doctests manually.

- **Error**: Expecting `cargo fix --edition` to handle all `#[cfg]` configurations in one pass.
  **Correction**: Run `cargo fix` multiple times with different `--target` and `--features` flags to cover all conditional compilation paths.

# Common Confusions

- **Confusion**: Thinking `cargo fix --edition` and `cargo fix --edition-idioms` are the same.
  **Clarification**: `--edition` fixes backwards-incompatible changes required for the new edition. `--edition-idioms` additionally updates old idiomatic patterns to newer ones (e.g., removing `extern crate` lines). The idiom lints are known to have issues and may produce incorrect suggestions.

- **Confusion**: Believing macro code is always automatically migrated.
  **Clarification**: Macros use "edition hygiene" where tokens are tagged with their source edition. Proc macros generally cannot be automatically fixed, and `macro_rules!` macros may need manual updates, especially if they contain tokens that change meaning across editions (like `dyn` becoming a keyword).

- **Confusion**: Thinking you must migrate all crates in a workspace simultaneously.
  **Clarification**: "In a Cargo workspace, each package defines its own edition, so the process naturally involves migrating one package at a time."

# Source Reference

Chapter 1: What Are Editions; sections "Transitioning an existing project to a new edition" and "Advanced migration strategies." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 1 -- "Rust aims to make upgrading to a new edition an easy process."
- Confidence rationale: HIGH -- the source provides detailed step-by-step instructions with examples, edge cases, and troubleshooting
- Uncertainties: The `--edition-idioms` flag is noted as having known bugs in the source itself
- Cross-reference status: rust-editions, edition-interoperability are in this extraction set; rust-2021-edition, rust-2024-edition from other agents
