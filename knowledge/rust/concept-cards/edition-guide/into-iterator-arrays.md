---
concept: IntoIterator for Arrays
slug: into-iterator-arrays
category: edition-2021
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "IntoIterator for arrays"
extraction_confidence: high
aliases:
  - "array IntoIterator"
  - "array into_iter"
  - "array iteration by value"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - edition-migration
  - edition-interoperability
contrasts_with: []
answers_questions:
  - "How does array.into_iter() behave differently in Rust 2021?"
  - "Why couldn't IntoIterator for arrays be added without an edition?"
  - "What does the array_into_iter lint warn about?"
  - "How do I iterate over an array by value?"
---

# Quick Definition

Starting with Rust 1.53.0, arrays implement `IntoIterator` in all editions, but `array.into_iter()` changes meaning only in Rust 2021: in earlier editions it still resolves to `(&array).into_iter()` (iterating by reference), while in Rust 2021 it iterates by value. Other syntax like `for e in [1, 2, 3]` and `IntoIterator::into_iter([1, 2, 3])` works by value in all editions.

# Core Definition

"Instead, the trait implementation was added in all editions (starting in Rust 1.53.0) but with a small hack to avoid breakage until Rust 2021. In Rust 2015 and 2018 code, the compiler will still resolve `array.into_iter()` to `(&array).into_iter()` like before, as if the trait implementation does not exist. This only applies to the `.into_iter()` method call syntax. It does not affect any other syntax such as `for e in [1, 2, 3]`, `iter.zip([1, 2, 3])` or `IntoIterator::into_iter([1, 2, 3])`. Those will start to work in all editions." (Edition Guide, Ch. 4: Rust 2021, "IntoIterator for arrays")

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- the `.into_iter()` method call behavior change is part of the 2021 edition

# Key Properties

1. Arrays implement `IntoIterator` in all editions starting from Rust 1.53.0
2. Only the `.into_iter()` method call syntax is edition-gated
3. In Rust 2015/2018, `array.into_iter()` resolves to `(&array).into_iter()` (iterates by reference)
4. In Rust 2021, `array.into_iter()` calls the real `IntoIterator::into_iter` (iterates by value)
5. `for e in [1, 2, 3]` works by value in all editions (not affected by the hack)
6. `iter.zip([1, 2, 3])` works by value in all editions
7. `IntoIterator::into_iter([1, 2, 3])` works by value in all editions
8. The `array_into_iter` lint has been a default warning since Rust 1.41
9. The trait implementation could not exist in only one edition because editions can be mixed

# Construction / Recognition

## To Migrate Array Iteration Code:
1. Run `cargo fix --edition` to automatically adjust affected calls
2. If you need by-reference iteration, change `array.into_iter()` to `array.iter()`
3. If you want by-value iteration, keep `array.into_iter()` (it will work as expected in 2021)
4. For fully qualified syntax `IntoIterator::into_iter(array)`, you can optionally simplify to `array.into_iter()` in 2021

## To Identify Affected Code:
1. Look for `array.into_iter()` calls where the array is a fixed-size array type `[T; N]`
2. Check whether the code expects `&T` elements (old behavior) or `T` elements (new behavior)
3. The `array_into_iter` lint flags all affected calls

# Context & Application

This change addresses a long-standing issue (rust-lang/rust#25725): you could iterate over `&[1, 2, 3]` and `&mut [1, 2, 3]`, but not `[1, 2, 3]` directly by value. Simply adding the `IntoIterator` implementation would change the meaning of existing `.into_iter()` calls on arrays, which was deemed too much breakage for a "minor" change.

The solution was a carefully designed compromise: add the trait implementation to all editions (so `for e in array` works everywhere), but use a compiler hack to preserve the old `.into_iter()` method resolution in earlier editions. This keeps the edition difference minimal -- only one specific method call syntax changes behavior.

For migration, the most straightforward approach is to replace `array.into_iter()` with `array.iter()` if you want to keep the by-reference behavior. This works in all editions and makes the intent explicit.

# Examples

**Example 1** (Behavior change, "Details" section):

```rust
fn main() {
    let array = [1u8, 2, 3];
    for x in array.into_iter() {
        // x is a &u8 in Rust 2015 and Rust 2018
        // x is a u8 in Rust 2021
    }
}
```

**Example 2** (Migration to preserve old behavior, "Migration" section):

```rust
fn main() {
    let array = [1u8, 2, 3];
    for x in array.iter() {  // Use .iter() for by-reference iteration
        // x is a &u8 in all editions
    }
}
```

**Example 3** (Syntax that works in all editions, "Details" section):

```rust
fn main() {
    // These iterate by value in ALL editions (not affected by the hack):
    for e in [1, 2, 3] {}                        // for-in loop
    let _ = [1, 2, 3].iter().zip([4, 5, 6]);     // zip with array
    let _ = IntoIterator::into_iter([1, 2, 3]);   // fully qualified call
}
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- the method call behavior change is part of the 2021 edition

## Enables
- No downstream concepts directly

## Related
- **edition-migration** -- `cargo fix --edition` handles the migration
- **edition-interoperability** -- this change demonstrates how editions handle cross-edition trait implementations

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Assuming `for e in array` is edition-dependent.
  **Correction**: `for e in [1, 2, 3]` iterates by value in all editions since Rust 1.53. Only the `.into_iter()` method call syntax is edition-dependent.

- **Error**: Replacing `array.into_iter()` with `array.into_iter()` and expecting the same behavior across editions.
  **Correction**: If you need consistent by-reference behavior, use `array.iter()` explicitly. If you want by-value behavior, use `for e in array` which works in all editions.

# Common Confusions

- **Confusion**: Thinking `IntoIterator` for arrays only exists in Rust 2021.
  **Clarification**: The trait implementation exists in all editions since Rust 1.53. Only the method call syntax `array.into_iter()` has edition-dependent behavior. The compiler uses a "small hack" to make it resolve to `(&array).into_iter()` in pre-2021 editions.

- **Confusion**: Thinking this change affects slices (`&[T]`).
  **Clarification**: This change is about arrays (`[T; N]`), not slices. Slices already had `IntoIterator` via reference. The change allows arrays to be consumed by value during iteration.

- **Confusion**: Wondering why the trait cannot just exist in one edition.
  **Clarification**: "You can't have a trait implementation exist in one edition and not in another, since editions can be mixed." A crate on 2021 and a crate on 2018 may both use the same array type -- the trait impl must exist for both.

# Source Reference

Chapter 4: Rust 2021, "IntoIterator for arrays" section. References rust-lang/rust#25725 (long-standing issue), rust-lang/rust#65819 (adding the trait implementation), and the Rust book section on method syntax. The `array_into_iter` lint has been active since Rust 1.41.

# Verification Notes

- Definition source: Direct quotation from "IntoIterator for arrays" section, "Details" subsection
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides detailed explanation of the edition hack, the rationale, and migration steps
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set or Agent A's set
