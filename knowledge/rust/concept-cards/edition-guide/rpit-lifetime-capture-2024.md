---
concept: RPIT Lifetime Capture Rules 2024
slug: rpit-lifetime-capture-2024
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: "RPIT lifetime capture rules"
extraction_confidence: high
aliases:
  - "lifetime capture rules 2024"
  - "RPIT capture 2024"
  - "precise capturing"
  - "use<> bound"
  - "impl Trait lifetime capture"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What changed about RPIT lifetime capture in Rust 2024?"
  - "What is the use<> bound in Rust?"
  - "How do I control which lifetimes an impl Trait type captures?"
  - "What is precise capturing in Rust?"
  - "How do I migrate RPIT code to Rust 2024?"
---

# Quick Definition

In Rust 2024, return-position `impl Trait` (RPIT) opaque types implicitly capture all in-scope generic parameters, including lifetime parameters. The `use<..>` bound syntax (introduced in Rust 1.82) enables precise control over which parameters are captured, and replaces the older `Captures` and outlives tricks.

# Core Definition

*Capturing* a generic parameter in an RPIT opaque type allows that parameter to be used in the corresponding hidden type. In Rust 2021 and earlier, RPIT opaque types in bare functions and inherent impl methods only captured lifetime parameters when they appeared syntactically in a bound. In Rust 2024, all in-scope generic lifetime parameters are unconditionally captured when no `use<..>` bound is present.

This change is defined by RFC 3498 (lifetime capture rules) and RFC 3617 (precise capturing with `use<..>` bounds). The `use<..>` bound syntax looks like: `fn f<'a, T>(x: &'a (), y: T) -> impl Sized + use<'a, T>`, which explicitly states which generic parameters the opaque type captures.

The edition-specific difference is:

```rust
fn f_implicit(_: &()) -> impl Sized {}
// In Rust 2021: equivalent to impl Sized + use<>       (no lifetime captured)
// In Rust 2024: equivalent to impl Sized + use<'_>     (lifetime captured)
```

This makes bare function RPIT behavior consistent with RPIT in trait impls, RPITIT, and `async fn`, all of which already captured all in-scope lifetimes in all editions.

# Prerequisites

- **Rust editions** -- understanding that edition boundaries enable breaking changes to default behavior

# Key Properties

1. In all editions, type and const generic parameters are always implicitly captured by RPIT
2. In Rust 2024, lifetime parameters are also unconditionally captured (when no `use<..>` bound is present)
3. The `use<..>` bound (stable since Rust 1.82) provides explicit control over capturing in all editions
4. `use<>` (empty) captures no lifetimes; `use<'a, T>` captures specific parameters
5. Captured parameters affect how the opaque type can be used (e.g., captured lifetimes prevent `'static` bounds)
6. APIT (argument position impl Trait) anonymous parameters are considered in scope and captured
7. Generic parameters from outer `impl` blocks are in scope and captured
8. Higher-ranked `for<..>` binder lifetimes are in scope (though capturing them in nested opaques is not yet supported)

# Construction / Recognition

## To Use Precise Capturing (all editions):

```rust
fn capture<'a, T>(x: &'a (), y: T) -> impl Sized + use<'a, T> {
    (x, y)  // Hidden type (&'a (), T) uses both captured parameters
}
```

## To Opt Out of Lifetime Capture in 2024:

```rust
fn no_capture<'a>(x: &'a ()) -> impl Sized + use<> {
    *x  // Hidden type must not use 'a
}
```

## To Migrate from the Captures Trick:

```rust
// Old (all editions): using Captures trait trick
// fn f<'a, T>(x: &'a (), y: T) -> impl Sized + Captures<(&'a (), T)>

// New (all editions): precise capturing
fn f<'a, T>(x: &'a (), y: T) -> impl Sized + use<'a, T> { (x, y) }

// In Rust 2024, can often omit use<..> entirely:
fn f_2024<'a, T>(x: &'a (), y: T) -> impl Sized { (x, y) }
```

## To Migrate from the Outlives Trick:

```rust
// Old: fn f<'a, T: 'a>(x: &'a (), y: T) -> impl Sized + 'a
// The T: 'a bound was unnecessarily restrictive.

// New (2024): no trick needed
fn f<T>(x: &(), y: T) -> impl Sized { (x, y) }
```

# Context & Application

This is the single biggest language change in the 2024 Edition. The previous behavior was inconsistent: RPIT in trait impls and `async fn` already captured all lifetimes, but bare functions and inherent impl methods did not. This inconsistency forced workarounds like the `Captures` trick (a dummy trait bound) and the outlives trick (adding unnecessary `T: 'a` bounds). Both were error-prone and confusing.

The change is especially impactful for code that returns `impl Trait` from functions with lifetime parameters. Code that relied on lifetimes NOT being captured may break and will need `use<..>` bounds to preserve the old behavior.

Migration via `cargo fix --edition` uses the `impl_trait_overcaptures` lint to automatically insert `use<..>` bounds where needed. However, cases involving APIT require manual intervention because the anonymous type parameter must be given a name to appear in the `use<..>` bound.

# Examples

**Example 1** (automatic migration): `fn f<'a>(x: &'a ()) -> impl Sized { *x }` is migrated to `fn f<'a>(x: &'a ()) -> impl Sized + use<> { *x }` to preserve 2021 behavior of not capturing `'a`.

**Example 2** (APIT requiring manual fix): `fn f<'a>(x: &'a (), y: impl Sized) -> impl Sized { (*x, y) }` cannot be auto-fixed because the APIT parameter needs a name. Manual fix: `fn f<'a, T: Sized>(x: &'a (), y: T) -> impl Sized + use<T> { (*x, y) }`.

**Example 3** (outer impl parameters): Generic parameters from an outer `impl` are in scope: `impl<T, const C: usize> S<T, C> { fn f<U>() -> impl Sized {} }` is equivalent to `impl Sized + use<T, U, C>` in all editions.

# Relationships

## Builds Upon
- **rust-editions** -- this change is gated on the 2024 edition boundary

## Related
- **rust-2024-edition** -- this is the most significant language change in the 2024 edition

# Common Errors

- **Error**: Forgetting to add `use<..>` bounds during migration when a function returns `impl Trait` and callers rely on the return type being `'static`.
  **Correction**: Run `cargo fix --edition` which will automatically insert `use<..>` bounds. For APIT cases, name the type parameter and add it to the `use<..>` bound.

- **Error**: Assuming the `Captures` trick is no longer needed without updating edition.
  **Correction**: The `Captures` trick still works in 2024 but is unnecessary. Replace with `use<..>` bounds or remove entirely if the 2024 default capture is desired.

# Common Confusions

- **Confusion**: Thinking `use<..>` bounds are only available in Rust 2024.
  **Clarification**: `use<..>` bounds are available in all editions since Rust 1.82. The edition change is about the default behavior when no `use<..>` bound is present.

- **Confusion**: Thinking this change affects RPIT in trait impls or `async fn`.
  **Clarification**: Those already captured all in-scope lifetimes in all editions. The 2024 change only affects bare functions and inherent impl methods, making them consistent with trait impls and `async fn`.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024, "RPIT lifetime capture rules" section. Based on RFC 3498 (lifetime capture rules) and RFC 3617 (precise capturing). Covers the capturing concept, edition-specific rules, outer generic parameters, higher-ranked binders, APIT, and migration strategies including the Captures trick and outlives trick.

# Verification Notes

- Definition: Directly from the "Summary" and "Details" sections
- Key properties: All derived from explicit statements in the source
- Migration strategies: Directly from the "Migration" subsections
- Code examples: Adapted from the source's examples
- Confidence: HIGH -- the source provides detailed explanations with extensive code examples
- Cross-references: slug references checked against this extraction set
