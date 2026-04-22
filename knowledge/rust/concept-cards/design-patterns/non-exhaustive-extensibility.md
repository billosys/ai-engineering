---
# === CORE IDENTIFICATION ===
concept: Non-Exhaustive Extensibility
slug: non-exhaustive-extensibility

# === CLASSIFICATION ===
category: idiom
subcategory: api-design
tier: intermediate

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "#[non_exhaustive] and private fields for extensibility"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "non_exhaustive attribute"
  - "private field extensibility"
  - "backwards compatible structs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - structs-and-enums
  - visibility-rules
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add fields to a public struct without breaking downstream code?"
  - "What does #[non_exhaustive] do and when should I use it?"
  - "How can I prevent exhaustive matching on my enum across crate boundaries?"
  - "What is the private field trick for backwards-compatible structs?"
---

# Quick Definition

Use `#[non_exhaustive]` on structs, enums, and enum variants to allow adding new fields or variants without breaking backwards compatibility across crate boundaries. Alternatively, add a private `_b: ()` field to a struct to force downstream users to use `..` in patterns. Both techniques prevent exhaustive matching and direct construction by external code.

# Core Definition

> "A small set of scenarios exist where a library author may want to add public fields to a public struct or new variants to an enum without breaking backwards compatibility." -- Rust Design Patterns, "#[non_exhaustive] and private fields for extensibility"

Rust offers two solutions: (1) `#[non_exhaustive]` on structs, enums, and enum variants, which prevents exhaustive matching and direct construction across crate boundaries; (2) a private field (e.g., `_b: ()`) which forces `..` in patterns and prevents direct instantiation. The `#[non_exhaustive]` approach is the modern standard; the private field method works within crates where `#[non_exhaustive]` has no effect.

# Prerequisites

- Understanding of Rust structs and enums
- Knowledge of Rust's visibility rules (`pub` vs. private)
- Familiarity with pattern matching and destructuring

# Key Properties

1. **Cross-crate only**: `#[non_exhaustive]` has no effect within the defining crate; only external crates are affected.
2. **Prevents exhaustive matching**: External code must use `..` in struct patterns and `_` in enum matches.
3. **Prevents direct construction**: External code cannot construct the struct with a struct literal.
4. **Applies to variants too**: `#[non_exhaustive]` on an enum variant forces `..` in that variant's pattern.
5. **Private field alternative**: A `_b: ()` field achieves similar goals within the same crate.
6. **Zero runtime overhead**: The `()` private field has no size; `#[non_exhaustive]` is purely a compile-time attribute.

# Construction / Recognition

## To Apply #[non_exhaustive]:
1. Add `#[non_exhaustive]` above the struct, enum, or variant definition
2. Provide constructor functions or `Default` implementation for external creation
3. Document that the type may gain new fields/variants

## To Apply private field:
1. Add a field like `_b: ()` (private, zero-sized)
2. This forces `..` in patterns and prevents direct construction from outside the module

## To Recognize:
- `#[non_exhaustive]` attribute on struct/enum/variant definitions
- Private fields of type `()` with underscore-prefixed names
- `..` in struct destructuring patterns, `_ =>` in enum matches

# Context & Application

This idiom is essential for library authors who want to evolve their public types without issuing semver-major releases. Adding a new field to a struct or variant to an enum normally breaks all exhaustive matches downstream. With `#[non_exhaustive]`, clients are forced to write extensible patterns from the start. However, use this deliberately: it makes the API less ergonomic, and sometimes a major version bump is the better choice.

# Examples

**Example 1 -- non_exhaustive struct and enum:**

```rust
mod a {
    #[non_exhaustive]
    pub struct S {
        pub foo: i32,
    }

    #[non_exhaustive]
    pub enum AdmitMoreVariants {
        VariantA,
        VariantB,
        #[non_exhaustive]
        VariantC { a: String },
    }
}

fn print_matched_variants(s: a::S) {
    // Must use `..` because S is non_exhaustive
    let a::S { foo: _, .. } = s;

    let some_enum = a::AdmitMoreVariants::VariantA;
    match some_enum {
        a::AdmitMoreVariants::VariantA => println!("A"),
        a::AdmitMoreVariants::VariantB => println!("B"),
        a::AdmitMoreVariants::VariantC { a, .. } => println!("C: {a}"),
        _ => println!("new variant"),  // required wildcard
    }
}
```

**Example 2 -- private field alternative:**

```rust
pub struct S {
    pub a: i32,
    // Private field prevents direct instantiation and
    // forces `..` in patterns
    _b: (),
}
```

# Relationships

(No closely related concept cards in this extraction.)

# Common Errors

- **Error**: Using `#[non_exhaustive]` and expecting it to work within the same crate
  **Correction**: `#[non_exhaustive]` only affects external crates; use private fields for intra-crate protection

- **Error**: Applying `#[non_exhaustive]` too broadly, making the API unnecessarily awkward
  **Correction**: Use deliberately; a major version bump may be better for infrequent changes

- **Error**: Clients calling `panic!()` in the wildcard arm of non-exhaustive enum matches
  **Correction**: Design a meaningful fallback; if no good action exists, consider whether `#[non_exhaustive]` was the right choice

# Common Confusions

- **Confusion**: Thinking `#[non_exhaustive]` prevents adding fields internally
  **Clarification**: It only affects external consumers; within the crate, everything works normally

- **Confusion**: Believing `#[non_exhaustive]` is always preferable to a major version bump
  **Clarification**: It reduces ergonomics; use it when evolution is expected and frequent, not as a default

# Source Reference

Chapter 1: Idioms, Section "#[non_exhaustive] and private fields for extensibility".

# Verification Notes

- Definition source: Directly from "#[non_exhaustive] and private fields for extensibility" section
- Confidence rationale: HIGH -- thorough discussion with examples, alternatives, and trade-offs
- Uncertainties: None
- Cross-reference status: References RFC 2008
