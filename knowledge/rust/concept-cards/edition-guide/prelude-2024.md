---
concept: Rust 2024 Prelude and Standard Library Changes
slug: prelude-2024
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
  - "prelude 2024"
  - "std prelude 2024"
  - "Future in prelude"
  - "IntoFuture in prelude"
  - "IntoIterator for Box<[T]>"
  - "set_var unsafe"
prerequisites:
  - rust-editions
  - prelude-2021
related:
  - rust-2024-edition
contrasts_with:
  - prelude-2021
extends:
  - prelude-2021
answers_questions:
  - "What was added to the Rust 2024 prelude?"
  - "Why does my poll() method call become ambiguous in Rust 2024?"
  - "How did IntoIterator for Box<[T]> change in Rust 2024?"
  - "Why is set_var unsafe in Rust 2024?"
  - "What standard library functions became unsafe in Rust 2024?"
---

# Quick Definition

The Rust 2024 standard library changes include adding `Future` and `IntoFuture` to the prelude (potentially causing trait method ambiguity), implementing `IntoIterator` for `Box<[T]>` with edition-dependent `.into_iter()` behavior, and marking `std::env::set_var`/`remove_var` as `unsafe` due to thread-safety concerns.

# Core Definition

**Prelude additions:** The 2024 prelude adds `std::future::Future` and `std::future::IntoFuture`. This can cause ambiguity when a trait in scope has a method with the same name as a `Future` method (e.g., `poll`). The compiler prioritizes manually imported items over prelude items, so only glob imports (`use example::*;`) can create ambiguity.

**`IntoIterator` for `Box<[T]>`:** Starting in Rust 1.80, `Box<[T]>` implements `IntoIterator` in all editions. However, calling `.into_iter()` on a boxed slice has edition-dependent behavior:
- Before 2024: `boxed_slice.into_iter()` auto-dereferences to `(&(*boxed_slice)).into_iter()`, yielding `&T` references
- In 2024: `boxed_slice.into_iter()` calls `IntoIterator::into_iter` directly, yielding owned `T` values

Using `for x in boxed_slice` (without `.into_iter()`) yields owned values in all editions since 1.80.

**Unsafe standard library functions:** `std::env::set_var` and `std::env::remove_var` are now `unsafe` because calling them in multithreaded programs is unsound on some platforms. `CommandExt::before_exec` (already deprecated since 1.37) is also marked `unsafe`. The `deprecated_safe_2024` lint wraps calls in `unsafe {}` blocks automatically, but correctness must be verified manually.

# Prerequisites

- **Rust editions** -- understanding edition-gated behavior changes
- **Prelude 2021** -- the previous prelude that this extends

# Key Properties

1. `Future` and `IntoFuture` are the only new traits added to the 2024 prelude
2. Trait method ambiguity from prelude additions is resolved via fully qualified syntax
3. `Box<[T]>` implements `IntoIterator` in all editions (since Rust 1.80)
4. `.into_iter()` on `Box<[T]>` yields `&T` in pre-2024 editions, `T` in 2024
5. `for x in boxed_slice` (without `.into_iter()`) yields `T` in all editions since 1.80
6. `set_var` and `remove_var` are unsafe because process environment APIs are not thread-safe on some platforms
7. The `boxed_slice_into_iter` lint has been warning by default, so most code is already prepared
8. Auto-migration changes `.into_iter()` to `.iter()` to preserve reference behavior

# Construction / Recognition

## Resolving Prelude Trait Ambiguity:

```rust
// Before (2021) -- works because Future is not in prelude:
trait MyPoller { fn poll(&self); }
impl<T> MyPoller for T {}
core::pin::pin!(async {}).poll();  // calls MyPoller::poll

// After (2024) -- ambiguous: Future::poll vs MyPoller::poll
// Fix with fully qualified syntax:
<_ as MyPoller>::poll(&core::pin::pin!(async {}));
```

## Handling `Box<[T]>::into_iter()` Change:

```rust
let my_boxed_slice: Box<[u32]> = vec![1, 2, 3].into_boxed_slice();

// To iterate by reference (preserving pre-2024 behavior):
for x in my_boxed_slice.iter() { /* x: &u32 */ }

// To iterate by value (new 2024 behavior):
for x in my_boxed_slice { /* x: u32 -- works in all editions since 1.80 */ }
```

## Migrating `set_var`/`remove_var`:

```rust
// Before (2021):
std::env::set_var("FOO", "123");

// After (2024):
// SAFETY: ensure this is called only in single-threaded context
unsafe { std::env::set_var("FOO", "123") };
```

# Context & Application

The prelude change follows the same pattern as the 2021 Edition, which added `TryInto`, `TryFrom`, and `FromIterator`. Each addition can break code that has traits with conflicting method names. The 2024 additions (`Future`, `IntoFuture`) primarily affect async code.

The `Box<[T]>` change mirrors how `IntoIterator` for arrays was handled in the 2021 Edition. In both cases, the method-call syntax `.into_iter()` had edition-dependent behavior to avoid breaking existing code that relied on auto-deref to slice.

The `set_var`/`remove_var` unsafety reflects a real-world safety issue: calling `setenv` concurrently with any other environment access (including `getenv`) is undefined behavior on POSIX platforms. This has caused real bugs in production Rust code, particularly in test harnesses that set environment variables in parallel test threads.

# Examples

**Example 1** (prelude ambiguity): A trait with a `poll` method becomes ambiguous when `Future` is in the prelude. Fix: `<_ as MyPoller>::poll(...)`.

**Example 2** (boxed slice migration): `cargo fix --edition` changes `my_boxed_slice.into_iter()` to `my_boxed_slice.iter()` to preserve by-reference iteration behavior.

**Example 3** (set_var): `cargo fix --edition` wraps `std::env::set_var("FOO", "123")` in `unsafe { ... }` with a TODO comment to audit single-threadedness.

# Relationships

## Builds Upon
- **prelude-2021** -- extends the 2021 prelude with Future and IntoFuture

## Related
- **rust-2024-edition** -- these are the standard library changes in the 2024 edition
- **disjoint-capture-closures** -- the 2021 edition's analogous stdlib changes

# Common Errors

- **Error**: After migration, keeping `unsafe { std::env::set_var(...) }` in code that runs in multi-threaded contexts (e.g., parallel test harnesses).
  **Correction**: `set_var` is genuinely unsafe in multi-threaded programs. Consider alternatives: thread-local storage, configuration structs, or ensuring single-threaded execution.

- **Error**: Expecting `for x in boxed_slice` to yield references, as it did with the old `.into_iter()` behavior.
  **Correction**: `for x in boxed_slice` (without `.into_iter()`) has always yielded owned values since Rust 1.80. Only the `.into_iter()` method call had the edition-dependent shim.

# Common Confusions

- **Confusion**: Thinking the prelude additions only matter for async code.
  **Clarification**: Any trait that has a method named `poll` (or any method shared with `Future`/`IntoFuture`) can be affected, even in synchronous code.

- **Confusion**: Thinking `Box<[T]>` needs special handling in `for` loops.
  **Clarification**: Only the `.into_iter()` method call is edition-dependent. Using `for x in boxed_slice` directly works consistently across all editions since 1.80.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Three sections under "Standard library": "Changes to the prelude" (adding `Future` and `IntoFuture`), "Add `IntoIterator` for `Box<[T]>`" (edition-dependent `.into_iter()` behavior), and "Unsafe functions" (`set_var`, `remove_var`, `before_exec`).

# Verification Notes

- Prelude additions: directly from "Changes to the prelude" Summary
- Box<[T]> IntoIterator: from "Add IntoIterator for Box<[T]>" section
- Unsafe functions: from "Unsafe functions" section
- set_var safety rationale: "It can be unsound to call std::env::set_var or std::env::remove_var in a multithreaded program"
- Confidence: HIGH -- all information directly from the edition guide
- Cross-references: slugs verified against this extraction set and previously extracted cards
