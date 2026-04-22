---
concept: Newtype Pattern
slug: newtype-pattern
category: behavioural-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Behavioural Patterns"
extraction_confidence: high
aliases:
  - "newtype"
  - "newtype wrapper"
  - "opaque wrapper"
prerequisites:
  - default-trait
extends: []
related:
  - builder-pattern
  - deref-polymorphism
contrasts_with:
  - deref-polymorphism
answers_questions:
  - "How do I create a type-safe wrapper around an existing type in Rust?"
  - "What is the difference between a newtype and a type alias?"
  - "How can I override trait implementations for foreign types?"
  - "Is the newtype pattern zero-cost?"
---

# Quick Definition

The Newtype pattern uses a tuple struct with a single field to create an opaque wrapper for a type, providing type safety, encapsulation, and the ability to implement traits on foreign types. It is a zero-cost abstraction with no runtime overhead.

# Core Definition

"Use a tuple struct with a single field to make an opaque wrapper for a type. This creates a new type, rather than an alias to a type (`type` items)." The primary motivation is "abstraction. It allows you to share implementation details between types while precisely controlling the interface. By using a newtype rather than exposing the implementation type as part of an API, it allows you to change implementation backwards compatibly." (Rust Design Patterns, Ch. 2: Behavioural Patterns, "Newtype")

# Prerequisites

- **Default trait** -- newtypes often derive or implement `Default` and other standard traits; understanding trait implementation patterns is essential

# Key Properties

1. Uses a tuple struct with a single field: `struct Password(String)`
2. Creates a genuinely new type, not just an alias (unlike `type` items)
3. The wrapped and wrapper types are not type-compatible -- users can never confuse them
4. Zero-cost abstraction: there is no runtime overhead
5. The privacy system ensures users cannot access the wrapped type (fields are private by default)
6. Enables implementing traits on foreign types (e.g., custom `Display` for `String`)
7. Allows restricting functionality (reducing exposed functions or implemented traits)
8. Can make a copy-semantics type have move semantics
9. Hides internal types behind a simpler public API (e.g., `pub struct Foo(Bar<T1, T2>)`)

# Construction / Recognition

## To Create a Newtype:
1. Define a tuple struct with a single field: `struct Wrapper(InnerType)`
2. Implement desired traits on the wrapper (e.g., `Display`, `From`, `Deref`)
3. Provide pass-through methods for any inner type methods that should be exposed
4. Keep the inner field private (default) to enforce encapsulation

## To Recognize the Pattern:
1. Look for tuple structs with exactly one field
2. Check if the struct exists primarily to provide type safety or trait implementations
3. Look for pass-through method delegation to the inner type
4. Check if the struct overrides or restricts trait implementations compared to the inner type

# Context & Application

The source motivates the pattern with a security example: wrapping `String` as `Password` to override `Display` so passwords are never accidentally printed. The `Password` type's `Display` implementation always outputs `"****************"` regardless of the actual password content.

Newtypes are "very common in Rust code." The source lists several use cases: abstraction (the primary use), representing units (e.g., wrapping `f64` for `Miles` and `Kilometres`), restricting functionality, converting copy semantics to move semantics, and hiding internal generic types behind a simpler public API.

The main downside is boilerplate: "You need a 'pass through' method for every method you want to expose on the wrapped type, and an impl for every trait you want to also be implemented for the wrapper type." The `derive_more` crate is mentioned as a mitigation for this boilerplate.

# Examples

**Example 1** (Ch. 2, "Newtype" -- Password Wrapper): A `Password(String)` newtype overrides `Display` to print `"****************"` instead of the actual string. This demonstrates implementing a foreign trait differently for a wrapped type: `println!("secured_password: {secured_password}")` outputs asterisks while the underlying `String` would print the plaintext.

**Example 2** (Ch. 2, "Newtype" -- Hiding Internal Types): `pub struct Foo(Bar<T1, T2>)` where `Bar` is a public generic type and `T1`, `T2` are internal types. "Users of our module shouldn't know that we implement `Foo` by using a `Bar`, but what we're really hiding here is the types `T1` and `T2`, and how they are used with `Bar`."

# Relationships

## Builds Upon
- None explicitly

## Enables
- None explicitly

## Related
- **builder-pattern** -- builders construct complex types; newtypes wrap existing types for type safety. Both are common Rust construction patterns
- **deref-polymorphism** -- implementing `Deref` on a newtype to access inner methods is tempting but considered an anti-pattern

## Contrasts With
- **deref-polymorphism** -- using `Deref` to make a newtype behave like its inner type subverts the purpose of the newtype (type safety and encapsulation). The newtype pattern deliberately restricts the interface; deref polymorphism re-exposes it

# Common Errors

- **Error**: Using a type alias (`type Password = String`) instead of a newtype when type safety is needed.
  **Correction**: Type aliases create an alias, not a new type. The wrapped and wrapper are type-compatible, so users can confuse them. Use a tuple struct newtype for genuine type safety.

- **Error**: Making the inner field public, defeating encapsulation.
  **Correction**: Keep the field private (the default). "The privacy system ensures that users cannot access the wrapped type (if the field is private, which it is by default)."

# Common Confusions

- **Confusion**: Thinking newtypes have runtime overhead.
  **Clarification**: "Newtypes are a zero-cost abstraction -- there is no runtime overhead." The wrapper is erased at compile time.

- **Confusion**: Thinking the boilerplate problem has no solution.
  **Clarification**: The source recommends the `derive_more` crate "for deriving many builtin traits on newtypes," significantly reducing the pass-through boilerplate.

# Source Reference

Chapter 2: Design Patterns, "Newtype" section under Behavioural Patterns. Includes the Password example, a discussion of advantages and disadvantages, and references to the Rust Book's "Advanced Types" chapter, Haskell's Newtype, type aliases documentation, and the `derive_more` crate.

# Verification Notes

- Definition source: Direct quotation from the "Description" and "Motivation" subsections of "Newtype"
- Key Properties: Derived from the "Advantages," "Disadvantages," and "Discussion" subsections
- Confidence rationale: HIGH -- the source provides a clear example, explicit advantages/disadvantages, and multiple use cases
- Uncertainties: None for the pattern itself
- Cross-reference status: default-trait is from Agent 1 (idioms); builder-pattern is from Agent 4 (creational/structural); deref-polymorphism is from Agent 5 (anti-patterns)
