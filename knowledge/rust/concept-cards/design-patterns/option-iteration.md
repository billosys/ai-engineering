---
# === CORE IDENTIFICATION ===
concept: Option Iteration
slug: option-iteration

# === CLASSIFICATION ===
category: idiom
subcategory: iterators
tier: foundational

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Iterating over an Option"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Option as iterator"
  - "Option IntoIterator"
  - "iterating over Option"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - option-type
  - iterator-trait
extends: []
related:
  - iterator-chain
  - filter-map
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I treat an Option as an iterator in Rust?"
  - "How do I append an Option's value to a collection using iterator methods?"
  - "When should I use std::iter::once instead of Some(x).into_iter()?"
---

# Quick Definition

`Option<T>` implements `IntoIterator`, making it a zero-or-one element container that works with iterator combinators like `.extend()`, `.chain()`, and `.filter_map()`. Use this to compose `Option` values with iterators without explicit `if let` unwrapping.

# Core Definition

> "`Option` can be viewed as a container that contains either zero or one element. In particular, it implements the `IntoIterator` trait, and as such can be used with generic code that needs such a type." -- Rust Design Patterns, "Iterating over an Option"

Since `Option` implements `IntoIterator`, it can be used anywhere an iterator is expected: as an argument to `.extend()`, chained onto existing iterators with `.chain()`, or iterated directly with a `for` loop (though `if let` is usually preferred for the last case).

# Prerequisites

- Understanding of `Option<T>` (`Some` and `None`)
- Familiarity with the `Iterator` and `IntoIterator` traits

# Key Properties

1. **IntoIterator implementation**: `Option<T>` yields zero elements for `None` and one element for `Some(T)`.
2. **Works with .extend()**: Append an `Option`'s value to a collection without unwrapping.
3. **Works with .chain()**: Tack an `Option` onto the end of an existing iterator.
4. **for loop works but if let is preferred**: `for x in option` is equivalent to `if let Some(x) = option`, but the latter is more idiomatic for simple cases.
5. **std::iter::once for known Some**: When the value is always `Some`, `std::iter::once(value)` is more readable.

# Construction / Recognition

## To Apply:
1. Identify a case where you need to conditionally include a value in an iterator pipeline
2. Use `.extend(option)` to push the value into a collection
3. Use `.chain(option)` or `.chain(option.iter())` to append to an iterator
4. Use `Iterator::filter_map` when mapping functions return `Option`

## To Recognize:
- `.extend(some_option)` calls on collections
- `.chain(some_option)` or `.chain(some_option.iter())` in iterator chains
- `for x in some_option` loops (though `if let` is preferred)

# Context & Application

This idiom leverages Rust's trait system: because `Option` implements `IntoIterator`, it composes naturally with the entire iterator ecosystem. This is particularly useful in generic code where you want to conditionally include values without branching. The `filter_map` combinator is the most common application, filtering and mapping in one step by returning `Option` from the closure.

# Examples

**Example 1 -- extending a collection with an Option:**

```rust
let turing = Some("Turing");
let mut logicians = vec!["Curry", "Kleene", "Markov"];

logicians.extend(turing);

// equivalent to:
if let Some(turing_inner) = turing {
    logicians.push(turing_inner);
}
```

**Example 2 -- chaining an Option onto an iterator:**

```rust
let turing = Some("Turing");
let logicians = vec!["Curry", "Kleene", "Markov"];

for logician in logicians.iter().chain(turing.iter()) {
    println!("{logician} is a logician");
}
```

# Relationships

## Related
- **iterator-chain** -- `.chain()` is the primary combinator for appending Option iterators
- **filter-map** -- `Iterator::filter_map` is a specialized map for functions returning Option

# Common Errors

- **Error**: Using `for x in option` when `if let Some(x) = option` is clearer
  **Correction**: Prefer `if let` for simple conditional access; use iterator methods for composition

- **Error**: Using `Some(value).into_iter()` when the value is always present
  **Correction**: Use `std::iter::once(value)` for clarity

# Common Confusions

- **Confusion**: Thinking `Option` must be unwrapped before use in iterator contexts
  **Clarification**: `Option` implements `IntoIterator` directly; it works as-is with `.extend()`, `.chain()`, etc.

- **Confusion**: Confusing `option.iter()` (borrows) with `option.into_iter()` (consumes)
  **Clarification**: `.iter()` yields `&T`, `.into_iter()` yields `T` by consuming the Option

# Source Reference

Chapter 1: Idioms, Section "Iterating over an Option".

# Verification Notes

- Definition source: Directly from "Iterating over an Option" section
- Confidence rationale: HIGH -- complete with multiple examples and see-also references
- Uncertainties: None
- Cross-reference status: References std::iter::once, Iterator::filter_map, ref_slice crate
