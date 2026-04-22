---
concept: Drop Check and PhantomData
slug: drop-check-and-phantom-data
category: unsafe-rust
subcategory: ownership-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Ownership and Lifetimes"
chapter_number: 3
pdf_page: null
section: "Drop Check / PhantomData"
extraction_confidence: high
aliases:
  - "dropck"
  - "drop checker"
  - "sound generic drop"
  - "PhantomData"
  - "phantom data"
  - "may_dangle"
  - "dropck eyepatch"
  - "#[may_dangle]"
prerequisites:
  - ownership-and-lifetimes
  - subtyping-and-variance
extends:
  - ownership-and-lifetimes
  - subtyping-and-variance
related:
  - exotic-types
  - nomicon-overview
contrasts_with: []
answers_questions:
  - "What is the drop checker and why does it exist?"
  - "What is the big rule of sound generic drop?"
  - "What is PhantomData and when is it needed?"
  - "How does PhantomData affect variance?"
  - "What is #[may_dangle] and when is it used?"
  - "Why does adding a Drop impl change what the borrow checker accepts?"
  - "When is PhantomData<T> superfluous in a struct with Drop?"
---

# Quick Definition

The drop checker enforces that generic type arguments must strictly outlive a value for it to soundly implement `Drop`, because destructors can observe borrowed data. `PhantomData<T>` is a zero-sized marker type that simulates a field of type `T` for the purposes of variance, auto-traits, and drop checking, without consuming any space.

# Core Definition

**Drop Check** addresses a subtle soundness issue: when a type has a destructor, the destructor might access borrowed data during its execution. Without special rules, this could allow observing dangling references. The Big Rule: "For a generic type to soundly implement drop, its generics arguments must strictly outlive it." (Ch. 3, "Drop Check")

Adding a `Drop` impl changes borrow-checker behavior. Without `Drop`, the `Inspector<'a>` example compiles because `days` doesn't need to strictly outlive `inspector` -- as long as `inspector` is alive, `days` is too. But adding `impl<'a> Drop for Inspector<'a>` causes the program to fail because the destructor could access `self.0` (the `&'a u8`), requiring `'a` to strictly outlive the `Inspector`. Only generic types need this check; non-generic types can only harbor `'static` lifetimes.

Variables are dropped in reverse declaration order; struct/tuple fields in declaration order. The drop order is defined but the borrow checker doesn't track field-level drop ordering -- it cannot know what outlives what for vector elements dropped by library code.

**`#[may_dangle]`** (unstable, RFC 1327) is an escape hatch: it asserts that a generic type's destructor won't access expired data for a specific parameter. For example, `unsafe impl<#[may_dangle] 'a> Drop for Inspector<'a>` promises not to use `'a` data when dropping. This requires the `Drop` impl to be marked `unsafe`.

**`PhantomData`** is a special marker type that "consumes no space, but simulates a field of the given type for the purpose of static analysis." (Ch. 3, "PhantomData"). It serves three purposes: (1) controlling variance, (2) providing auto-trait information (`Send`/`Sync`), and (3) informing drop checking about ownership.

For a struct like `Iter<'a, T>` with only raw pointers, `'a` would be unbounded without `PhantomData<&'a T>`. This tells the compiler the struct logically contains `&'a T` references, making it covariant over both `'a` and `T`.

Since RFC 1238, an `impl<T> Drop for Vec<T>` alone makes Rust consider that `Vec<T>` owns values of type `T`. **Adding `PhantomData<T>` is superfluous for drop checking when a `Drop` impl already exists** -- it only affects variance and auto-traits in that case. However, the standard library still uses `PhantomData<T>` in `Vec` because of `#[may_dangle]`: the `unsafe impl<#[may_dangle] T> Drop for Vec<T>` opts out of the default drop-check conservatism, and `PhantomData<T>` re-adds the ownership assertion to handle the case where `T` has drop glue.

# Prerequisites

- **ownership-and-lifetimes** -- drop checking extends the lifetime system's guarantees to destructors
- **subtyping-and-variance** -- PhantomData's primary use is controlling variance

# Key Properties

1. The Big Rule: generic arguments must strictly outlive a type for sound generic drop
2. Adding `Drop` to a generic type changes what the borrow checker accepts -- it requires borrowed data to strictly outlive the value
3. Only generic types need drop checking; non-generic types only harbor `'static` lifetimes
4. Variables drop in reverse declaration order; struct/tuple fields drop in declaration order
5. The borrow checker doesn't track field-level drop ordering in the general case
6. `PhantomData<T>` is zero-sized but simulates a field of type `T` for static analysis
7. `PhantomData` affects three things: variance, auto-traits (`Send`/`Sync`), and drop checking
8. `PhantomData<T>` is superfluous for drop checking when `Drop` is already implemented (since RFC 1238)
9. `#[may_dangle]` (unstable) allows asserting a destructor won't access expired data for specific parameters
10. `#[may_dangle]` requires the `Drop` impl to be `unsafe` and the `dropck_eyepatch` feature
11. When using `#[may_dangle] T`, the `PhantomData<T>` field re-asserts ownership to handle transitive drop glue

# Construction / Recognition

## PhantomData Patterns Table

| Phantom type              | Variance `'a` | Variance `T`   | Send/Sync        | Dangling in drop |
|---------------------------|---------------|----------------|-------------------|------------------|
| `PhantomData<T>`          | -             | covariant      | inherited         | disallowed       |
| `PhantomData<&'a T>`      | covariant     | covariant      | requires `T: Sync`| allowed          |
| `PhantomData<&'a mut T>`  | covariant     | invariant      | inherited         | allowed          |
| `PhantomData<*const T>`   | -             | covariant      | `!Send + !Sync`   | allowed          |
| `PhantomData<*mut T>`     | -             | invariant      | `!Send + !Sync`   | allowed          |
| `PhantomData<fn(T)>`      | -             | contravariant  | `Send + Sync`     | allowed          |
| `PhantomData<fn() -> T>`  | -             | covariant      | `Send + Sync`     | allowed          |
| `PhantomData<fn(T) -> T>` | -             | invariant      | `Send + Sync`     | allowed          |
| `PhantomData<Cell<&'a ()>>`| invariant    | -              | `Send + !Sync`    | allowed          |

## To Choose the Right PhantomData

1. Need covariance + ownership: `PhantomData<T>`
2. Need covariance + borrowed reference semantics: `PhantomData<&'a T>`
3. Need invariance: `PhantomData<&'a mut T>`, `PhantomData<*mut T>`, or `PhantomData<fn(T) -> T>`
4. Need contravariance: `PhantomData<fn(T)>`
5. Need to opt out of Send/Sync: `PhantomData<*const T>` or `PhantomData<*mut T>`

# Context & Application

Drop checking and PhantomData are where Rust's ownership system meets unsafe code head-on. When building low-level data structures with raw pointers, the type system doesn't know about logical ownership. `PhantomData` bridges this gap by telling the compiler "this type logically owns/borrows these types" without actually storing them.

The standard library's `Vec<T>` is the canonical example: it stores data behind `*const T` (for covariance) but adds `PhantomData<T>` for ownership semantics. Combined with `#[may_dangle]`, this allows `Vec<&'s str>` to be dropped even when `'s` has expired (because `Vec`'s destructor only deallocates memory, not accessing the `&str` values -- unless they have drop glue, which `PhantomData<T>` handles).

The `Unique<T>` internal utility in the standard library combines `*const T` (variance), `PhantomData<T>` (ownership + auto-traits), `NonZero` (null pointer optimization), and auto-derives `Send`/`Sync` as if `T` were contained. This pattern is pervasive for types that own allocations.

# Examples

**Example 1** (Ch. 3, "Drop Check"): Adding `Drop` changes borrow-checker behavior:
```rust
struct Inspector<'a>(&'a u8);
impl<'a> Drop for Inspector<'a> {
    fn drop(&mut self) { println!("I was only {} days from retirement!", self.0); }
}
struct World<'a> { inspector: Option<Inspector<'a>>, days: Box<u8> }
fn main() {
    let mut world = World { inspector: None, days: Box::new(1) };
    world.inspector = Some(Inspector(&world.days));
    // ERROR: world.days does not live long enough (destructor might access it)
}
```
Without the `Drop` impl, this compiles fine.

**Example 2** (Ch. 3, "PhantomData"): Using PhantomData for an iterator:
```rust
use std::marker;
struct Iter<'a, T: 'a> {
    ptr: *const T,
    end: *const T,
    _marker: marker::PhantomData<&'a T>,  // bounds 'a, gives covariance over 'a and T
}
```

**Example 3** (Ch. 3, "Drop Check"): The `#[may_dangle]` escape hatch:
```rust
#![feature(dropck_eyepatch)]
unsafe impl<#[may_dangle] 'a> Drop for Inspector<'a> {
    fn drop(&mut self) {
        println!("Inspector knows when *not* to inspect.");
        // Must NOT access self.0 -- the 'a data may be expired
    }
}
```

# Relationships

## Builds Upon
- **ownership-and-lifetimes** -- drop checking extends lifetime analysis to destructors
- **subtyping-and-variance** -- PhantomData's primary role is controlling variance

## Enables
(none directly -- this is the most advanced topic in the ownership chapter)

## Related
- **exotic-types** -- ZSTs (PhantomData is a ZST); empty types interact with drop semantics
- **nomicon-overview** -- unsafe traits and soundness are the backdrop for drop check

## Contrasts With
(none)

# Common Errors

- **Error**: Adding `PhantomData<T>` to a struct that already has `impl<T> Drop` (without `#[may_dangle]`), thinking it's needed for drop checking.
  **Correction**: Since RFC 1238, the `Drop` impl itself makes the compiler consider that the type owns `T`. `PhantomData<T>` is only needed for drop-checking purposes when using `#[may_dangle]` to opt out of the default conservatism.

- **Error**: Using `#[may_dangle]` on a type parameter and then accessing that parameter's data in the destructor (via trait methods, callbacks, or printing).
  **Correction**: `#[may_dangle]` asserts the destructor won't access the parameter's data. Doing so (even indirectly through `Display`, `Debug`, or callback invocation) is UB.

# Common Confusions

- **Confusion**: Thinking drop order within a struct is undefined.
  **Clarification**: Drop order is defined (fields in declaration order, variables in reverse declaration order, per RFC 1857). However, relying on it is fragile -- use `ManuallyDrop` when order matters.

- **Confusion**: Believing `PhantomData<T>` and `PhantomData<&'a T>` are interchangeable.
  **Clarification**: They have different effects. `PhantomData<T>` asserts ownership (disallows dangling in drop), while `PhantomData<&'a T>` asserts borrowed access (allows dangling in drop but adds `Send` requirement: `T: Sync`). The variance effects may also differ.

- **Confusion**: Thinking all generic types need `PhantomData` for soundness.
  **Clarification**: `PhantomData` is needed when a type or lifetime is logically associated with a struct but not present in any field (e.g., a lifetime only used through raw pointers). If the type parameter appears in real fields, its variance and drop-check effects are already established.

# Source Reference

Chapter 3: Ownership and Lifetimes -- Drop Check (the Big Rule, Inspector/World examples, `#[may_dangle]` escape hatch, drop order notes), PhantomData (purpose, Iter example, Vec example, RFC 1238, `#[may_dangle]` interaction, complete PhantomData patterns table, Unique<T> utility).

# Verification Notes

- Definition source: Direct synthesis from Ch. 3 "Drop Check" and "PhantomData" sections (lines 1287-1896 of source)
- Key Properties: The Big Rule is a direct quotation; PhantomData patterns table is reproduced from source; RFC 1238 behavior explicitly discussed
- Confidence rationale: HIGH -- extensive source coverage with complete patterns table, multiple examples, and explicit discussion of the RFC 1238 change
- Uncertainties: `#[may_dangle]` is unstable; the source notes "the finer details of how the drop checker validates types is totally up in the air"
- Cross-reference status: All slugs reference cards in the nomicon extraction set
