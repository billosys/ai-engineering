---
concept: Rust 2024 Edition
slug: rust-2024-edition
category: edition-2024
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Edition 2024"
  - "Rust Edition 2024"
  - "2024 Edition"
prerequisites:
  - rust-editions
  - edition-migration
extends:
  - rust-2021-edition
related:
  - rpit-lifetime-capture-2024
  - unsafe-changes-2024
  - if-let-temporary-scope-2024
  - never-type-fallback-2024
  - gen-keyword-reservation
  - prelude-2024
  - match-ergonomics-2024
  - cargo-changes-2024
  - rustfmt-style-edition
contrasts_with:
  - rust-2021-edition
answers_questions:
  - "What changed in the Rust 2024 Edition?"
  - "What is the Rust 2024 Edition?"
  - "How do I migrate to Rust 2024?"
  - "What language changes does Rust 2024 include?"
---

# Quick Definition

The Rust 2024 Edition, released with Rust 1.85.0 (February 2025) via RFC 3501, is the largest edition since 2015. It includes changes across language, standard library, Cargo, Rustdoc, and Rustfmt, with a strong theme of making `unsafe` more explicit and improving lifetime and temporary scope semantics.

# Core Definition

The 2024 Edition encompasses changes in five major areas:

**Language changes:** RPIT lifetime capture rules (all in-scope generic parameters, including lifetimes, are now implicitly captured); `if let` temporary scope changes (temporaries dropped before `else` branch); `let` chains in `if` and `while`; tail expression temporary scope narrowing; match ergonomics reservations (restricting `mut`/`ref`/`ref mut` and reference patterns with match ergonomics); unsafe `extern` blocks; unsafe attributes (`no_mangle`, `export_name`, `link_section`); `unsafe_op_in_unsafe_fn` warning by default; disallowing references to `static mut`; never type fallback changing from `()` to `!`; macro fragment specifier changes (`expr` now matches `const` and `_`); missing macro fragment specifiers becoming a hard error; `gen` keyword reservation; and reserved syntax for guarded strings.

**Standard library:** `Future` and `IntoFuture` added to the prelude; `IntoIterator` for `Box<[T]>` with edition-dependent `.into_iter()` behavior; `set_var`/`remove_var` marked `unsafe`.

**Cargo:** Rust-version aware resolver (`resolver = "3"`); table/key name consistency (removing underscored variants); rejecting unused inherited `default-features`.

**Rustdoc:** Combined doctests into a single binary for performance; nested `include!` path resolution change.

**Rustfmt:** Style edition system allowing per-edition formatting rules; numerous formatting fixes; raw identifier sorting; version sorting.

Migration is performed via `cargo fix --edition`, which runs the `rust-2024-compatibility` lint group to automatically fix most issues.

# Prerequisites

- **Rust editions** -- understanding the edition system and how editions enable backward-incompatible changes
- **Edition migration** -- familiarity with `cargo fix --edition` workflow

# Key Properties

1. Released with Rust 1.85.0 on February 20, 2025
2. Defined by RFC 3501
3. Largest edition since the original 2015 edition, touching language, stdlib, Cargo, Rustdoc, and Rustfmt
4. Strong theme of making `unsafe` more explicit (extern blocks, attributes, `unsafe_op_in_unsafe_fn`, `static mut` references)
5. Significant lifetime and temporary scope changes (RPIT capture, `if let` temporaries, tail expression temporaries)
6. Introduces `resolver = "3"` in Cargo for Rust-version aware dependency resolution
7. Introduces the style edition concept for Rustfmt
8. Reserved `gen` keyword for future generator blocks
9. Never type fallback changes from `()` to `!`
10. Prelude adds `Future` and `IntoFuture`

# Construction / Recognition

## To Migrate to the 2024 Edition:

1. Ensure your project compiles cleanly on the latest stable Rust
2. Run `cargo fix --edition` to apply automatic migrations
3. Change `edition = "2021"` to `edition = "2024"` in `Cargo.toml`
4. Manually review changes flagged by lints that cannot auto-fix (e.g., `tail_expr_drop_order`, never type fallback)
5. Run tests to verify behavior is preserved
6. For virtual workspaces, explicitly set `resolver = "3"` if desired

## Key Lints in `rust-2024-compatibility` Group:

- `impl_trait_overcaptures` -- RPIT lifetime capture changes
- `if_let_rescope` -- `if let` temporary scope
- `tail_expr_drop_order` -- tail expression temporaries (manual review)
- `rust_2024_incompatible_pat` -- match ergonomics
- `missing_unsafe_on_extern` -- unsafe extern blocks
- `unsafe_attr_outside_unsafe` -- unsafe attributes
- `unsafe_op_in_unsafe_fn` -- unsafe operations in unsafe functions
- `static_mut_refs` -- references to `static mut`
- `keyword_idents_2024` -- `gen` keyword conflicts
- `edition_2024_expr_fragment_specifier` -- macro `expr` specifier
- `rust_2024_prelude_collisions` -- prelude trait method ambiguity
- `boxed_slice_into_iter` -- `Box<[T]>::into_iter()` behavior change
- `deprecated_safe_2024` -- newly unsafe stdlib functions

# Context & Application

The 2024 Edition continues Rust's tradition of using editions to make backward-incompatible improvements without breaking existing code. The edition is opt-in per crate, and crates using different editions interoperate seamlessly.

The dominant theme of this edition is safety and correctness: making unsafe operations more visible (`unsafe extern`, `unsafe` attributes, `unsafe_op_in_unsafe_fn`, `static mut` references), fixing surprising lifetime behavior (RPIT capture, `if let` temporaries, tail expression temporaries), and correcting the never type fallback from `()` to `!`.

The Cargo resolver v3 is noteworthy for CI/production environments: it respects `rust-version` when selecting dependencies, preventing silent breakage from dependency updates that require newer Rust versions.

# Examples

**Example 1** (RPIT lifetime capture): In 2021, `fn f<'a>(x: &'a ()) -> impl Sized {}` does not capture `'a`. In 2024, it implicitly captures `'a`. Use `impl Sized + use<>` to opt out.

**Example 2** (`if let` temporary scope): In 2021, `if let Some(x) = *value.read().unwrap() { ... } else { value.write().unwrap(); }` deadlocks because the read lock lives through the `else` block. In 2024, the temporary is dropped before the `else` block.

**Example 3** (unsafe extern): `extern "C" { fn free(p: *mut c_void); }` must become `unsafe extern "C" { ... }` in 2024.

# Relationships

## Builds Upon
- **rust-2021-edition** -- the 2024 edition extends and refines changes from 2021
- **rust-editions** -- the edition mechanism that enables these changes

## Enables
- **gen-keyword-reservation** -- reserves `gen` for future generator blocks
- **rustfmt-style-edition** -- introduces the style edition concept

## Related
- **rpit-lifetime-capture-2024** -- the largest language change in this edition
- **unsafe-changes-2024** -- the cluster of unsafe-related changes
- **prelude-2024** -- prelude additions
- **cargo-changes-2024** -- Cargo tooling changes

## Contrasts With
- **rust-2021-edition** -- the previous edition; 2024 changes several 2021 behaviors

# Common Errors

- **Error**: Running `cargo fix --edition` without reviewing the output, especially for `tail_expr_drop_order` and never type fallback warnings that require manual review.
  **Correction**: Always manually review warnings that `cargo fix` cannot auto-fix; these involve potential behavior changes.

- **Error**: Expecting virtual workspaces to automatically use resolver v3.
  **Correction**: Virtual workspaces require explicitly setting `resolver = "3"` in the `[workspace]` definition.

# Common Confusions

- **Confusion**: Thinking the 2024 edition requires Rust 1.85 or newer to compile crates using it.
  **Clarification**: Correct -- Rust 1.85.0 is the minimum compiler version needed for `edition = "2024"`. Older compilers will reject it.

- **Confusion**: Believing that switching to edition 2024 will break interop with crates on older editions.
  **Clarification**: Crates on different editions interoperate seamlessly. Edition is a per-crate setting.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. RFC 3501 defines the edition. Released with Rust 1.85.0 (February 20, 2025). The chapter covers all changes organized by area: Language, Standard Library, Cargo, Rustdoc, and Rustfmt.

# Verification Notes

- Overview synthesized from the full chapter covering ~3000 lines of source material
- Release version (1.85.0) and RFC (3501) from the chapter header table
- All section summaries drawn from the respective section "Summary" blocks
- Confidence: HIGH -- all information directly from the edition guide
- Cross-references: slugs reference other cards in this extraction set and previously extracted edition cards
