---
concept: Match Ergonomics Reservations 2024
slug: match-ergonomics-2024
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: "Match ergonomics reservations"
extraction_confidence: high
aliases:
  - "match ergonomics 2024"
  - "default binding mode restrictions"
  - "rust_2024_incompatible_pat"
  - "pattern ergonomics restrictions"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What changed about match ergonomics in Rust 2024?"
  - "Why can't I use mut in patterns with match ergonomics in Rust 2024?"
  - "What is the default binding mode in Rust pattern matching?"
  - "What does rust_2024_incompatible_pat mean?"
---

# Quick Definition

Rust 2024 restricts three pattern constructs when match ergonomics is active (i.e., when the default binding mode is not `move`): `mut` on bindings, `ref`/`ref mut` on bindings, and reference patterns (`&`/`&mut`). These restrictions "reserve design space" for future improvements to match ergonomics by disallowing currently surprising or redundant behavior.

# Core Definition

Match ergonomics (RFC 2005) allows patterns to elide reference matching. When a pattern passes a reference in the scrutinee without explicitly mentioning it, the *default binding mode* switches from `move` to `ref` or `ref mut`. In Rust 2024, three restrictions apply when the default binding mode is not `move`:

**1. `mut` restriction:** In 2021, writing `mut` on a binding when the default binding mode is not `move` resets the binding mode to `move`, which changes the type. This is surprising -- mutability should not affect the type. In 2024, this is an error.

```rust
// 2021: allowed but surprising
let [x, mut y] = &[(), ()]; // x: &(), mut y: ()

// 2024: error -- mut not allowed when default binding mode is ref
// Fix: make the pattern fully explicit
let &[ref x, mut y] = &[(), ()]; // x: &(), mut y: ()
```

**2. `ref`/`ref mut` restriction:** In 2021, writing `ref` on a binding when match ergonomics already set the binding mode to `ref` is redundant. In 2024, explicit binding modes are disallowed where they are redundant.

```rust
// 2021: allowed but redundant
let [ref x] = &[()]; // x: &()

// 2024: error -- ref is redundant, match ergonomics already provides it
// Fix: rely on match ergonomics
let [x] = &[()]; // x: &()
```

**3. Reference patterns restriction:** In 2021, `&` in a pattern when the default binding mode is not `move` both matches the reference AND resets the binding mode, causing a larger-than-expected type change. In 2024, `&`/`&mut` can only appear when the pattern is fully explicit (default binding mode is `move`).

```rust
// 2021: allowed but surprising
let [&x, y] = &[&(), &()]; // x: (), y: &&()

// 2024: error -- & not allowed when default binding mode is ref
// Fix: make the pattern fully explicit
let &[&x, ref y] = &[&(), &()];
```

# Prerequisites

- **Rust editions** -- understanding edition-gated restrictions

# Key Properties

1. These are *restrictions*, not new capabilities -- they remove currently-allowed but surprising patterns
2. The restrictions only apply when the default binding mode is not `move` (i.e., when match ergonomics is active)
3. Fully explicit patterns (where all references are matched with `&`) are unaffected
4. The purpose is to "leave space" for future improvements to match ergonomics behavior
5. The `rust_2024_incompatible_pat` lint auto-converts affected patterns to fully explicit forms
6. The fully explicit forms work correctly in all editions
7. `mut` restriction prevents mutability from silently changing the type
8. `ref`/`ref mut` restriction removes redundancy
9. `&`/`&mut` restriction prevents surprising double-reference stripping

# Construction / Recognition

## Identifying Affected Patterns:

A pattern is affected when it:
- Uses match ergonomics (passes references without `&` in the pattern) AND
- Contains `mut`, `ref`, `ref mut`, `&`, or `&mut` deeper in the pattern

## Auto-Fix Behavior:

`cargo fix --edition` converts to fully explicit patterns:

```rust
// Before (2021):
let [x, mut y] = &[(), ()];
let [ref x] = &[()];
let [&x, y] = &[&(), &()];

// After (all editions):
let &[ref x, mut y] = &[(), ()];
let &[ref x] = &[()];
let &[&x, ref y] = &[&(), &()];
```

## Understanding Default Binding Mode:

- Starts as `move`
- Changes to `ref` when the pattern passes a `&` in the scrutinee
- Changes to `ref mut` when the pattern passes a `&mut` in the scrutinee
- In 2024, once the mode is not `move`, you cannot write `mut`, `ref`, `ref mut`, `&`, or `&mut`

# Context & Application

These restrictions are described as "reservations" because they leave design space for future changes to how match ergonomics interacts with these constructs. The current behavior of `mut` resetting the binding mode is considered a design mistake -- mutability and borrowing should be orthogonal. Similarly, `&` resetting the binding mode while also matching a reference is confusing because a single `&` in the pattern causes two layers of references to be removed.

By making these patterns errors now, the Rust team can later assign them new, more intuitive semantics without breaking existing code. This is the "reserve now, define later" approach that editions enable.

The auto-fix converts to fully explicit patterns which are always correct in all editions. After migration, you may want to simplify some patterns by removing unnecessary `ref` bindings, since match ergonomics can infer them.

# Examples

**Example 1** (`mut` restriction): `let [x, mut y] = &[(), ()];` gives `x: &()` and `mut y: ()` in 2021 because `mut` resets the binding mode. In 2024, this is an error. Fix: `let &[ref x, mut y] = &[(), ()];`

**Example 2** (redundant `ref`): `let [ref x] = &[()];` is redundant in 2021 because match ergonomics already binds `x` by reference. In 2024, this is an error. Fix: `let [x] = &[()];`

**Example 3** (`&` restriction): `let [&x, y] = &[&(), &()];` gives `x: ()` and `y: &&()` in 2021 because `&` both matches the reference and resets the binding mode. In 2024, this is an error. Fix: `let &[&x, ref y] = &[&(), &()];`

# Relationships

## Related
- **rust-2024-edition** -- these restrictions are part of the 2024 edition's language changes

# Common Errors

- **Error**: Manually fixing patterns by removing `ref` without checking that match ergonomics provides the correct binding mode.
  **Correction**: Use `cargo fix --edition` which correctly converts to fully explicit patterns. Then optionally simplify.

- **Error**: Assuming all patterns with `ref` are affected.
  **Correction**: Only patterns where the default binding mode is already `ref` (because match ergonomics kicked in) are affected. `let ref x = ();` (no match ergonomics) is still fine.

# Common Confusions

- **Confusion**: Thinking match ergonomics itself is being removed or restricted.
  **Clarification**: Match ergonomics (RFC 2005) is fully intact. The restriction only applies to mixing explicit binding modes with implicit match ergonomics in the same pattern.

- **Confusion**: Thinking the fully explicit auto-fix patterns are the recommended style going forward.
  **Clarification**: The auto-fix errs on the side of correctness. In many cases, you can simplify by removing the now-unnecessary explicit `ref` bindings and relying on match ergonomics, which is the idiomatic Rust style.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024, "Match ergonomics reservations" section. Covers background on match ergonomics (RFC 2005), the `mut` restriction, `ref`/`ref mut` restriction, reference patterns restriction, and migration via the `rust_2024_incompatible_pat` lint.

# Verification Notes

- All three restrictions and their examples: directly from the source "Details" section
- Background on default binding mode: from the "Background" subsection
- Auto-fix behavior: from the "Migration" section
- "Reserve design space" rationale: stated in the section headers ("To leave space to fix this" / "To leave space for other language possibilities")
- Confidence: HIGH -- the source provides clear before/after examples for each restriction
- Cross-references: slugs verified against this extraction set
