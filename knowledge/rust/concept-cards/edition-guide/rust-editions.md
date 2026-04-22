---
# === CORE IDENTIFICATION ===
concept: Rust Editions
slug: rust-editions

# === CLASSIFICATION ===
category: edition-system
subcategory: core-concepts
tier: foundational

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "What Are Editions"
chapter_number: 1
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "editions"
  - "Rust edition system"
  - "epoch system"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - edition-migration
  - edition-interoperability
  - rust-2015-edition
  - rust-2018-edition
  - rust-2021-edition
  - rust-2024-edition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Rust editions?"
  - "Why does Rust have editions?"
  - "How do editions allow backwards-incompatible changes without breaking existing code?"
  - "How do I set the edition for a Cargo project?"
  - "What editions are available in Rust?"
---

# Quick Definition

Rust editions are opt-in release milestones (2015, 2018, 2021, 2024) that allow backwards-incompatible changes to the language while preserving the "stability without stagnation" guarantee. Each crate independently selects its edition in `Cargo.toml`, and crates on different editions interoperate seamlessly.

# Core Definition

Editions solve the fundamental tension between language evolution and backwards compatibility. As described in the source: "When there are backwards-incompatible changes, they are pushed into the next edition. Since editions are opt-in, existing crates won't use the changes unless they explicitly migrate into the new edition." (Ch. 1: What Are Editions). The edition mechanism was created alongside Rust 2018 (RFC #2052) and retroactively designated Rust 1.0 as the "2015" edition. The valid editions are 2015, 2018, 2021, and 2024.

A key design principle is that edition changes are "skin deep": "All Rust code -- regardless of edition -- will ultimately compile down to the same internal representation within the compiler." This means editions can introduce new keywords (like `async`/`await` in 2018), change path resolution rules, or deprecate syntax, but they cannot fundamentally alter how the compiled code works at the IR level.

# Prerequisites

- None within this source. Editions are a fundamental concept of the Rust language itself.

# Key Properties

1. **Opt-in**: Editions are never forced; crates choose when to migrate
2. **Per-crate granularity**: Each crate (and even individual Cargo targets) specifies its own edition independently
3. **Backwards-compatible compilation**: All editions compile to the same internal representation
4. **Cross-edition interoperability**: Crates on different editions can depend on each other seamlessly
5. **Automated migration**: `cargo fix --edition` provides automated tooling to migrate code between editions
6. **Default edition**: If no edition is specified, Cargo defaults to Rust 2015 for backwards compatibility
7. **Three-year cadence**: New editions are released roughly every three years

# Construction / Recognition

## Setting the Edition for a New Project:
1. Run `cargo new <project_name>` -- defaults to the latest stable edition
2. Or specify explicitly: `cargo new --edition 2018 <project_name>`
3. The edition is recorded in `Cargo.toml` under `[package]`

## Identifying the Current Edition:
- Check the `edition` field in `Cargo.toml`:
  ```toml
  [package]
  name = "foo"
  version = "0.1.0"
  edition = "2024"
  ```
- If no `edition` field is present, the crate uses the 2015 edition by default

## Changing the Edition Manually:
- Edit the `edition` value in `Cargo.toml` to the desired year

# Context & Application

The edition system allows Rust to evolve the language surface (syntax, keywords, module resolution) without breaking the ecosystem. Common backwards-incompatible changes enabled by editions include introducing new keywords (e.g., `async`, `await`, `dyn` becoming strict in 2018), changing module path resolution, and modifying default behaviors. Because the changes are "skin deep," the compiler, standard library, and runtime remain unified across all editions.

# Examples

**Example 1** (Ch 1): Creating a project with the latest edition:
```console
$ cargo new foo
$ cat foo/Cargo.toml
[package]
name = "foo"
version = "0.1.0"
edition = "2024"
```

**Example 2** (Ch 1): Creating a project with a specific edition:
```console
$ cargo new --edition 2018 foo
$ cat foo/Cargo.toml
[package]
name = "foo"
version = "0.1.0"
edition = "2018"
```

**Example 3** (Ch 1): Invalid edition years are rejected:
```console
$ cargo new --edition 2019 foo
error: invalid value '2019' for '--edition <YEAR>'
  [possible values: 2015, 2018, 2021, 2024]
```

**Example 4** (Ch 1): Why editions exist -- introducing `async` as a keyword:
> "Early versions of Rust didn't feature the `async` and `await` keywords. If Rust had suddenly introduced these new keywords, some code would have broken: `let async = 1;` would no longer work."

# Relationships

## Builds Upon
- None -- editions are a foundational concept

## Enables
- **edition-migration** -- the process of moving between editions
- **edition-interoperability** -- crates on different editions working together
- **rust-2015-edition** -- the first (default) edition
- **rust-2018-edition** -- the second edition, introducing path changes and new keywords
- **rust-2021-edition** -- the third edition
- **rust-2024-edition** -- the fourth edition

## Related
- **edition-migration** -- the automated tooling for moving between editions
- **edition-interoperability** -- the guarantee that editions don't split the ecosystem

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming that an absent `edition` field means the latest edition.
  **Correction**: If there's no `edition` key in `Cargo.toml`, Cargo defaults to Rust 2015, not the latest edition.

- **Error**: Using an invalid year like `2019` or `2020` as an edition value.
  **Correction**: Only specific years are valid editions: 2015, 2018, 2021, 2024. Cargo will reject invalid values.

# Common Confusions

- **Confusion**: Thinking that editions are like major version bumps that split the ecosystem.
  **Clarification**: "Crates in one edition must seamlessly interoperate with those compiled with other editions." Editions are per-crate and don't affect dependency compatibility.

- **Confusion**: Believing edition changes affect the compiled output or runtime behavior.
  **Clarification**: "All Rust code -- regardless of edition -- will ultimately compile down to the same internal representation within the compiler." Changes are syntactic/"skin deep."

- **Confusion**: Thinking you must upgrade to a new edition immediately when it releases.
  **Clarification**: Editions are opt-in and permanent. A crate on edition 2015 continues to compile with the latest Rust compiler indefinitely.

# Source Reference

Chapter 1: What Are Editions; "Creating a new project" section. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 1 -- "Rust uses editions to solve this problem. When there are backwards-incompatible changes, they are pushed into the next edition."
- Confidence rationale: HIGH -- the source provides detailed explanation with examples and design rationale
- Uncertainties: None for core concepts
- Cross-reference status: edition-migration, edition-interoperability, rust-2015-edition, rust-2018-edition are in this extraction set; rust-2021-edition and rust-2024-edition are from other agents
