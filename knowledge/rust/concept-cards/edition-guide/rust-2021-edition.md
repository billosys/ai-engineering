---
concept: Rust 2021 Edition
slug: rust-2021-edition
category: edition-2021
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "edition 2021"
  - "2021 edition"
  - "Rust 1.56 edition"
prerequisites:
  - rust-editions
extends:
  - rust-editions
related:
  - prelude-2021
  - cargo-feature-resolver-v2
  - into-iterator-arrays
  - disjoint-capture-closures
  - panic-macro-consistency
  - c-string-literals
  - edition-migration
  - edition-interoperability
  - rust-2024-edition
contrasts_with: []
answers_questions:
  - "What changed in the Rust 2021 edition?"
  - "What is RFC 3085?"
  - "Which Rust release introduced the 2021 edition?"
  - "How do I migrate to Rust 2021?"
  - "What syntax was reserved in Rust 2021?"
  - "What warnings became errors in Rust 2021?"
---

# Quick Definition

The Rust 2021 Edition, released with Rust 1.56.0 (RFC 3085), introduces several changes that bring new capabilities and more consistency to the language: additions to the prelude, default Cargo feature resolver v2, `IntoIterator` for arrays, disjoint capture in closures, panic macro consistency, reserved syntax for future expansion, raw lifetimes, promotion of two warnings to errors, or patterns in macro-rules, and C-string literals.

# Core Definition

"The Rust 2021 Edition contains several changes that bring new capabilities and more consistency to the language, and opens up room for expansion in the future." (Edition Guide, Ch. 4: Rust 2021, introduction)

The major changes are:

1. **Prelude additions** -- `TryInto`, `TryFrom`, and `FromIterator` are added to the prelude (see `prelude-2021`)
2. **Default Cargo feature resolver** -- `edition = "2021"` implies `resolver = "2"` in `Cargo.toml` (see `cargo-feature-resolver-v2`)
3. **IntoIterator for arrays** -- `array.into_iter()` now iterates by value instead of by reference (see `into-iterator-arrays`)
4. **Disjoint capture in closures** -- closures capture individual fields instead of whole variables (see `disjoint-capture-closures`)
5. **Panic macro consistency** -- `panic!()` always processes its first argument as a format string (see `panic-macro-consistency`)
6. **Reserved syntax** -- `ident#`, `ident"..."`, `ident'...'` are reserved for future use
7. **Raw lifetimes** -- `'r#ident_or_keyword` is now allowed as a single lifetime token
8. **Warnings promoted to errors** -- `bare_trait_objects` and `ellipsis_inclusive_range_patterns` become hard errors
9. **Or patterns in macro-rules** -- `:pat` now matches `|` in patterns; `:pat_param` preserves old behavior
10. **C-string literals** -- `c"..."` and `cr"..."` syntax for `&CStr` values (see `c-string-literals`)

# Prerequisites

- **Rust editions** (`rust-editions`) -- understanding what editions are, how they work, and how code using different editions can interoperate is essential context for understanding any specific edition's changes

# Key Properties

1. Released with Rust 1.56.0
2. Activated by setting `edition = "2021"` in `Cargo.toml`
3. Migration is supported by `cargo fix --edition`
4. Editions are per-crate; different crates in a workspace can use different editions
5. Reserved syntax (`prefix#ident`, `prefix"string"`, `prefix'c'`) enables future language expansion without edition boundaries
6. Raw lifetimes (`'r#ident`) are parsed as a single token (previously three tokens: `'r`, `#`, `ident`)
7. `bare_trait_objects` lint becomes a hard error: `&MyTrait` must be written as `&dyn MyTrait`
8. `ellipsis_inclusive_range_patterns` lint becomes a hard error: `0...100` must be written as `0..=100`
9. `:pat` fragment specifier in `macro_rules!` now matches `|` (e.g., `A | B`); `:pat_param` retains old behavior
10. The edition of a macro's definition crate (not the calling crate) determines `:pat` behavior

# Construction / Recognition

## To Migrate a Crate to Rust 2021:
1. Ensure your code compiles without warnings on the current edition
2. Run `cargo fix --edition` to automatically apply migration fixes
3. Update `edition = "2018"` to `edition = "2021"` in `Cargo.toml`
4. Build and test to verify everything works correctly
5. Review any "dummy let" insertions in closures for possible removal

## To Recognize Rust 2021 Code:
1. `edition = "2021"` in `Cargo.toml`
2. Uses `TryInto`/`TryFrom`/`FromIterator` without explicit imports
3. Uses `array.into_iter()` to iterate by value
4. Closures that rely on capturing individual fields of structs
5. Uses `c"..."` or `cr"..."` C-string literals
6. Uses `dyn` keyword with all trait objects (required, not optional)
7. Uses `..=` for inclusive ranges in patterns (required, not optional)

# Context & Application

The Rust 2021 edition focuses on incremental improvements and consistency rather than headline features. The biggest behavioral change is disjoint capture in closures, which changes what closures capture and can affect drop order and trait implementations. The prelude additions address a long-standing ergonomic issue where `TryInto` required an explicit `use` statement. The reserved syntax changes are forward-looking, making room for future features like format string shorthands (`f"hello {name}"`) and string-typed literals (`s"hello"`) without needing another edition boundary.

The warnings-to-errors changes (`bare_trait_objects` and `ellipsis_inclusive_range_patterns`) enforce patterns that have been recommended since earlier editions, making the language more consistent. Similarly, the panic macro changes unify `core::panic!()` and `std::panic!()` and make `panic!()` behave consistently with `println!()`.

# Examples

**Example 1** (Reserved Syntax): The reserved prefix syntax enables future expansion. For instance, `z"hey"` was previously tokenized as `z` followed by `"hey"` in macros. In Rust 2021, this is a tokenization error. The fix is to insert a space: `z "hey"`. This reservation may eventually allow syntax like `f"hello {name}"` for format strings or `s"hello"` for `String` literals.

**Example 2** (Raw Lifetimes): Raw lifetimes support migration to newer editions that introduce new keywords. For example, the 2024 edition introduced the `gen` keyword. Code using a lifetime `'gen` can be migrated to `'r#gen` in Rust 2021, analogous to raw identifiers (`r#keyword`) for regular identifiers.

**Example 3** (Warnings to Errors): In Rust 2021, `&MyTrait` must be written as `&dyn MyTrait`, and `0...100` in patterns must be written as `0..=100`:

```rust
// Rust 2021 -- these are errors, not warnings:
// pub fn my_function(_: &MyTrait) {}   // Error: use &dyn MyTrait
// matches!(n, 0...100)                  // Error: use 0..=100

pub fn my_function(_: &dyn MyTrait) {}   // Correct
matches!(n, 0..=100)                      // Correct
```

**Example 4** (Or Patterns in Macros): The `:pat` fragment specifier now matches `|`:

```rust
// In Rust 2021, $x:pat matches "1 | 2" as a single pattern.
// To get the old behavior (not matching top-level |), use :pat_param:
macro_rules! my_macro {
    ($x:pat_param | $y:pat) => { /* ... */ }
}
my_macro!(1 | 2);
```

# Relationships

## Builds Upon
- **rust-editions** -- Rust 2021 is one instance of the edition mechanism

## Enables
- **prelude-2021** -- the new prelude additions
- **cargo-feature-resolver-v2** -- default resolver v2
- **into-iterator-arrays** -- changed `array.into_iter()` semantics
- **disjoint-capture-closures** -- precise closure captures
- **panic-macro-consistency** -- consistent panic formatting
- **c-string-literals** -- C-string literal syntax

## Related
- **edition-migration** -- the process for migrating between editions
- **edition-interoperability** -- how different editions work together
- **rust-2024-edition** -- the next edition after 2021

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Assuming `cargo fix --edition` handles all migration automatically.
  **Correction**: Some changes (especially Cargo feature resolver differences) have no automated fix. Run `cargo fix --edition` first, then manually review build failures, particularly around dependencies that relied on unified features.

- **Error**: Forgetting that the edition of a `macro_rules!` definition determines `:pat` behavior, not the edition of the calling crate.
  **Correction**: If your macro is defined in a 2021-edition crate, `:pat` will match `|` regardless of what edition the caller uses. Use `:pat_param` if you need the old behavior.

# Common Confusions

- **Confusion**: Thinking reserved syntax (`prefix"string"`) has a specific meaning in Rust 2021.
  **Clarification**: The reservation only makes these token patterns into errors. No prefix has been assigned a meaning in 2021 -- specific meanings (like `c"..."` for C-strings) are assigned by later stabilizations. The reservation ensures those future assignments do not require an edition boundary.

- **Confusion**: Thinking `bare_trait_objects` and `ellipsis_inclusive_range_patterns` are new lints in 2021.
  **Clarification**: These lints have been warnings since much earlier editions. Rust 2021 only promotes them to hard errors. If your code is already warning-free, no migration is needed for these changes.

- **Confusion**: Thinking all changes in the 2021 edition only apply in 2021 edition crates.
  **Clarification**: Some changes, like `IntoIterator` for arrays, were added to all editions. Only the `.into_iter()` method call syntax change is edition-gated. Similarly, `:pat_param` is available in all editions.

# Source Reference

Chapter 4: Rust 2021, all sections. The overview is from the chapter introduction. Individual changes are detailed in dedicated sections: "Additions to the prelude," "Default Cargo feature resolver," "IntoIterator for arrays," "Disjoint capture in closures," "Panic macro consistency," "Reserved syntax," "Raw lifetimes," "Warnings promoted to errors," "Or patterns in macro-rules," and "C-string literals." RFC 3085 governs the edition.

# Verification Notes

- Definition source: Direct quotation from Ch. 4 introduction
- Key Properties: Synthesized from all sections of Ch. 4
- Confidence rationale: HIGH -- this is an overview card compiling explicitly documented changes from the official Edition Guide
- Uncertainties: None for the content; all changes are well-documented
- Cross-reference status: All slugs reference cards in this extraction set or from other agents' extraction sets (rust-editions, edition-migration, edition-interoperability from Agent A; rust-2024-edition, prelude-2024 from Agent C)
