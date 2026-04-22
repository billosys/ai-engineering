---
concept: Never Type Fallback Change 2024
slug: never-type-fallback-2024
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: "Never type fallback change"
extraction_confidence: high
aliases:
  - "never type fallback"
  - "never-to-any coercion fallback"
  - "! fallback change"
  - "bang type fallback"
  - "dependency_on_unit_never_type_fallback"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What is never type fallback in Rust?"
  - "How did the never type fallback change in Rust 2024?"
  - "Why does my code break with never type fallback in Rust 2024?"
  - "What is the dependency_on_unit_never_type_fallback lint?"
---

# Quick Definition

In Rust 2024, when the compiler inserts a never-to-any coercion and cannot infer the target type, it now falls back to `!` (never) instead of `()` (unit). This change, planned to eventually apply to all editions, prevents `!` from spontaneously coercing to `()` in cases where no specific type was required.

# Core Definition

When the compiler encounters a value of type `!` (never) at a coercion site, it inserts an implicit `absurd` coercion to convert it to any target type. If type inference cannot determine the target type, the compiler uses a "fallback type."

Historically, the fallback type was `()`. This caused `!` to spontaneously coerce to `()` even when there was no reason to infer `()`, which was confusing and prevented stabilization of the `!` type. In the 2024 Edition, the fallback type is changed to `!` itself, making the behavior more intuitive: when you pass `!` and there is no reason to coerce it to something else, it stays as `!`.

The compiler effectively does this:

```rust
// When it sees: { panic!() };
// It inserts: { absurd(panic!()) };
// If it can't infer T for absurd::<T>:
//   2021: absurd::<()>(panic!())     -- falls back to ()
//   2024: absurd::<!>(panic!())      -- falls back to !
```

Additionally, the `never_type_fallback_flowing_into_unsafe` lint is elevated from `warn` to `deny` in 2024, catching a specific dangerous interaction between `!` fallback and unsafe code.

# Prerequisites

- **Rust editions** -- understanding the edition migration mechanism

# Key Properties

1. The never type fallback changes from `()` to `!` in the 2024 Edition
2. This change is planned to apply to all editions in a future release
3. The change only affects code where type inference cannot determine a concrete type
4. The most common breakage pattern is `f()?;` where `f` is generic over the `Ok` type
5. Another common pattern is closures that always panic: `run(|| panic!())`
6. There is no automatic fix -- only automatic detection via the `dependency_on_unit_never_type_fallback` lint
7. The fix is to specify the type explicitly so the fallback is not used
8. The `never_type_fallback_flowing_into_unsafe` lint is now `deny` by default

# Construction / Recognition

## Pattern 1: Generic `?` operator

```rust
fn f<T: Default>() -> Result<T, ()> { Ok(T::default()) }

// In 2021: f()? infers T = () via fallback
// In 2024: f()? infers T = ! which may not implement Default

// Fix: specify the type
f::<()>()?;
// or:
() = f()?;
```

## Pattern 2: Panicking closures

```rust
trait Unit {}
impl Unit for () {}

fn run<R: Unit>(f: impl FnOnce() -> R) { f(); }

// In 2021: run(|| panic!()) works because ! coerces to () which implements Unit
// In 2024: ! stays as ! which doesn't implement Unit

// Fix: specify the return type
run(|| -> () { panic!() });
```

## Pattern 3: Never in one branch, unconstrained in another

```rust
// In 2021: infers () for Default::default() because ! from return coerces to ()
if true { Default::default() } else { return };

// In 2024: infers ! for Default::default(), fails because ! doesn't implement Default

// Fix:
() = if true { Default::default() } else { return };
// or:
if true { <() as Default>::default() } else { return };
```

# Context & Application

This change addresses a long-standing design issue that prevented the stabilization of `!` as a proper type. The unit fallback was counterintuitive: writing `{ panic!() };` would silently evaluate to `()`, and generic functions called in diverging contexts would unexpectedly resolve their type parameters to `()`.

The migration challenge is that it can be non-trivial to identify which type needs to be specified, since the fallback only triggers when inference fails. The compiler's `dependency_on_unit_never_type_fallback` lint detects affected code in earlier editions, giving advance warning.

The `never_type_fallback_flowing_into_unsafe` lint addresses a specific safety concern: when the `!` fallback changes, it can alter the type of an expression flowing into unsafe code, potentially causing undefined behavior (e.g., if `mem::zeroed::<T>()` was called where `T` was inferred via the fallback).

# Examples

**Example 1** (common `?` pattern): `f()?;` where `f<T: Default>() -> Result<T, ()>`. Due to the `?` operator desugaring, `T` was inferred as `()` via fallback in 2021. In 2024, `T` is inferred as `!` which may not implement `Default`. Fix: `f::<()>()?;`

**Example 2** (panicking closure): `run(|| panic!())` where `run<R: Unit>`. The `!` from `panic!` coerced to `()` in 2021 (satisfying the `Unit` bound). In 2024, `!` stays as `!` and fails. Fix: `run(|| -> () { panic!() })`.

**Example 3** (branch inference): `if true { Default::default() } else { return };` infers `()` for `Default::default()` in 2021 via `!` coercion from `return`. In 2024, it tries to use `!` which does not implement `Default`.

# Relationships

## Related
- **rust-2024-edition** -- this is one of the language changes requiring manual migration

# Common Errors

- **Error**: Not running the `dependency_on_unit_never_type_fallback` lint before migrating, leading to surprise compilation failures.
  **Correction**: Enable the lint manually with `#![warn(dependency_on_unit_never_type_fallback)]` before upgrading to identify all affected code.

- **Error**: Using `_` as the type annotation (e.g., `f::<_>()?;`) thinking it forces inference.
  **Correction**: `_` still triggers inference and may hit the fallback. Use the concrete type (e.g., `f::<()>()?;`).

# Common Confusions

- **Confusion**: Thinking this change affects all uses of `!` or `panic!`.
  **Clarification**: The change only affects cases where the compiler cannot infer the target type for a never-to-any coercion and must use the fallback. Most code specifies types explicitly enough that the fallback is never used.

- **Confusion**: Thinking the `?` operator is directly involved.
  **Clarification**: The `?` operator is common in affected code because its desugaring introduces a coercion site, but the underlying issue is type inference fallback, not the `?` operator itself.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024, "Never type fallback change" section. Covers the mechanism of never-to-any coercions, the fallback type change from `()` to `!`, the `never_type_fallback_flowing_into_unsafe` lint, and migration patterns for `f()?`, panicking closures, and branch inference scenarios.

# Verification Notes

- Fallback mechanism explanation: directly from the "Details" section
- Common patterns (f()?, closures, branches): all from the "Migration" section with source code examples
- The plan to make this change across all editions: direct statement from source
- Confidence: HIGH -- the source provides detailed explanation of the mechanism and multiple migration examples
- Cross-references: slugs verified against this extraction set
