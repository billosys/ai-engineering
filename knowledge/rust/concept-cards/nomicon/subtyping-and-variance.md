---
concept: Subtyping and Variance
slug: subtyping-and-variance
category: unsafe-rust
subcategory: ownership-system
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Ownership and Lifetimes"
chapter_number: 3
pdf_page: null
section: "Subtyping and Variance"
extraction_confidence: high
aliases:
  - "variance"
  - "covariance"
  - "contravariance"
  - "invariance"
  - "lifetime subtyping"
  - "covariant"
  - "contravariant"
  - "invariant"
prerequisites:
  - ownership-and-lifetimes
  - lifetime-elision-and-bounds
extends:
  - ownership-and-lifetimes
related:
  - drop-check-and-phantom-data
  - type-conversions
contrasts_with: []
answers_questions:
  - "What is subtyping in Rust and how does it relate to lifetimes?"
  - "What are covariance, contravariance, and invariance?"
  - "Why is &mut T invariant over T?"
  - "Why is fn(T) contravariant over T?"
  - "How does a struct inherit variance from its fields?"
  - "What is the variance of Box, Vec, Cell, UnsafeCell?"
---

# Quick Definition

Rust uses subtyping and variance to allow flexible use of lifetimes while preventing misuse. Subtyping relates lifetimes (`'long <: 'short` when `'long` contains `'short`), and variance determines how subtyping of a type parameter affects subtyping of the containing type -- covariant (preserves), contravariant (inverts), or invariant (no relationship).

# Core Definition

**Subtyping** in Rust applies primarily to lifetimes: `Sub <: Super` means `Sub` satisfies all requirements of `Super` (and possibly more). For lifetimes: `'long <: 'short` if and only if `'long` defines a region of code that completely contains `'short`. So `'static <: 'a` for any `'a`, because `'static` covers all regions.

**Variance** determines how subtyping of generic parameters propagates through type constructors. Given `Sub <: Super` (Ch. 3, "Variance"):

- **Covariant**: `F<Sub> <: F<Super>` -- the subtype relationship passes through
- **Contravariant**: `F<Super> <: F<Sub>` -- the subtype relationship is inverted
- **Invariant**: no subtype relationship exists between `F<Sub>` and `F<Super>`

The variance table for standard types:

| Type              | `'a`      | `T`             | `U`       |
|-------------------|-----------|-----------------|-----------|
| `&'a T`           | covariant | covariant       |           |
| `&'a mut T`       | covariant | **invariant**   |           |
| `Box<T>`          |           | covariant       |           |
| `Vec<T>`          |           | covariant       |           |
| `UnsafeCell<T>`   |           | invariant       |           |
| `Cell<T>`         |           | invariant       |           |
| `fn(T) -> U`      |           | **contra**variant | covariant |
| `*const T`        |           | covariant       |           |
| `*mut T`          |           | invariant       |           |

A struct inherits variance from its fields: if `A` is used in multiple fields, all covariant yields covariant, all contravariant yields contravariant, and any mix (or invariant) yields invariant. **Invariance wins all conflicts.**

# Prerequisites

- **ownership-and-lifetimes** -- understanding lifetimes as regions and the two reference rules is essential
- **lifetime-elision-and-bounds** -- HRTBs interact with variance through function pointers

# Key Properties

1. Subtyping in Rust is primarily about lifetimes: `'long <: 'short` when `'long` completely contains `'short`
2. `'static <: 'a` for any lifetime `'a` (static lives at least as long as anything)
3. `&'a T` is covariant over both `'a` and `T` -- a longer-lived reference can substitute for a shorter-lived one
4. `&'a mut T` is covariant over `'a` but **invariant** over `T` -- preventing the `assign(&mut hello, &world)` use-after-free
5. `Box<T>` and `Vec<T>` are covariant over `T` because by-value ownership prevents aliasing-based attacks
6. `UnsafeCell<T>`, `Cell<T>` are invariant over `T` because interior mutability gives `&T` the properties of `&mut T`
7. `fn(T) -> U` is contravariant over `T` (arguments) and covariant over `U` (return) -- the only source of contravariance in the language
8. `*const T` follows `&T` (covariant); `*mut T` follows `&mut T` (invariant)
9. Structs inherit variance from their fields; invariance in any field over a parameter makes the struct invariant over that parameter
10. Covariance of `Box` is safe because moving an owned value destroys the old variable -- "we destroyed the only thing in the universe that remembered it lived for longer"

# Construction / Recognition

## To Determine a Type's Variance Over a Parameter

1. If the parameter appears only in covariant positions (e.g., `&'a T`, `Box<T>`, bare `T`), the type is covariant
2. If only in contravariant positions (e.g., `fn(T)`), the type is contravariant
3. If in invariant positions (e.g., `&mut T`, `Cell<T>`, `UnsafeCell<T>`, `*mut T`), the type is invariant
4. If in mixed positions, invariance wins all conflicts
5. For function pointers: arguments are contravariant, return types are covariant

## To Recognize Variance-Related Errors

1. If `&mut T` is involved and the compiler rejects a lifetime substitution, check for invariance over `T`
2. If `Cell<T>` or `UnsafeCell<T>` is involved, the parameter is invariant
3. If assigning through `&mut` would allow a shorter-lived value to replace a longer-lived one, invariance prevents it

# Context & Application

Variance is what makes Rust's lifetime system practical rather than overly restrictive. Without covariance, `&'static str` could never be used where `&'a str` is expected, which would be absurdly limiting. But without invariance on `&mut T`, the `assign(&mut hello, &world)` example shows how a use-after-free could be constructed by smuggling a short-lived reference into a long-lived mutable slot.

The source provides a key insight about why `Box<T>` can be covariant: "if you're allowed to mutate or move a value, you are guaranteed to be the only one with access to it." When you move `Box<&'static str>` into `Box<&'b str>`, the old variable is consumed -- there's no remaining alias that remembers the longer lifetime. This is fundamentally different from `&mut &'static str`, where the mutable reference creates an alias.

Contravariance is rare in practice because it only arises from function pointer arguments. A `fn(&'static str)` cannot substitute for `fn(&'a str)` because the more restrictive function would reject inputs the less restrictive one accepts. But `fn(&'a str)` can substitute for `fn(&'static str)` because a function that accepts any lifetime certainly accepts `'static`.

# Examples

**Example 1** (Ch. 3, "Subtyping"): Covariance allows `&'static str` to substitute for `&'world str`:
```rust
fn debug<'a>(a: &'a str, b: &'a str) {
    println!("a = {a:?} b = {b:?}");
}
fn main() {
    let hello: &'static str = "hello";
    {
        let world = String::from("world");
        let world = &world;
        debug(hello, world); // hello downgrades from &'static str to &'world str
    }
}
```

**Example 2** (Ch. 3, "Variance"): Invariance of `&mut T` prevents use-after-free:
```rust
fn assign<T>(input: &mut T, val: T) { *input = val; }
fn main() {
    let mut hello: &'static str = "hello";
    {
        let world = String::from("world");
        assign(&mut hello, &world); // ERROR: world does not live long enough
    }
    println!("{hello}"); // would be use-after-free without invariance
}
```

**Example 3** (Ch. 3, "Variance"): Contravariance of function arguments. A `fn(&'static str)` stored via `fn(&'a str)` pointer could be called with a short-lived string, pushing an invalid reference into a `Vec<&'static str>`. Contravariance prevents this substitution.

**Example 4** (Ch. 3, "Variance"): Struct variance inherits from fields:
```rust
struct MyType<'a, 'b, A: 'a, B: 'b, C, D, E, F, G, H, In, Out, Mixed> {
    a: &'a A,     // covariant over 'a and A
    b: &'b mut B, // covariant over 'b, invariant over B
    c: *const C,  // covariant over C
    d: *mut D,    // invariant over D
    e: E,         // covariant over E
    f: Vec<F>,    // covariant over F
    g: Cell<G>,   // invariant over G
    h1: H,        // would be covariant, but...
    h2: Cell<H>,  // invariant over H (invariance wins)
    i: fn(In) -> Out, // contravariant over In, covariant over Out
    k1: fn(Mixed) -> usize, // would be contravariant, but...
    k2: Mixed,    // invariant over Mixed (invariance wins)
}
```

# Relationships

## Builds Upon
- **ownership-and-lifetimes** -- variance extends the lifetime system to handle generic type parameters

## Enables
- **drop-check-and-phantom-data** -- PhantomData is used to control variance when raw pointers don't express the intended relationship

## Related
- **type-conversions** -- coercions interact with variance (e.g., unsizing coercions)
- **lifetime-elision-and-bounds** -- HRTBs and contravariance both involve function arguments with lifetime parameters

## Contrasts With
(none)

# Common Errors

- **Error**: Assuming `&mut &'static str` can be treated as `&mut &'a str` (applying covariance through `&mut`).
  **Correction**: `&mut T` is invariant over `T`. The compiler will not allow subtyping through a mutable reference, because doing so could allow writing a shorter-lived reference into a longer-lived slot.

- **Error**: Using `Cell<T>` or `UnsafeCell<T>` and expecting covariant behavior over `T`.
  **Correction**: Interior mutability types are invariant over their parameter because a shared reference can mutate the inner value, making it as dangerous as a mutable reference.

# Common Confusions

- **Confusion**: Thinking Rust has OOP-style subtyping (struct inheritance).
  **Clarification**: Rust's subtyping is almost exclusively about lifetimes. `'static <: 'a` is the primary subtype relationship. There is no struct-level type hierarchy.

- **Confusion**: Believing contravariance is common or important in everyday Rust.
  **Clarification**: "The only source of contravariance in the language is the arguments to a function, which is why it really doesn't come up much in practice." It only matters with function pointers that take references with specific lifetimes.

- **Confusion**: Thinking that `*const T` being covariant means raw pointers are safe to use covariantly.
  **Clarification**: `*const T` has the same variance as `&T` for type-checking purposes, but using raw pointers is already unsafe. The variance just determines whether the compiler accepts lifetime substitutions involving the pointer type.

# Source Reference

Chapter 3: Ownership and Lifetimes, section "Subtyping and Variance" -- subtyping definition, variance definitions (covariant/contravariant/invariant), complete variance table, struct variance inheritance, detailed examples with assign/debug functions, Box covariance argument, function pointer contravariance.

# Verification Notes

- Definition source: Direct synthesis from Ch. 3 "Subtyping and Variance" section (lines 908-1283 of source)
- Key Properties: Variance table reproduced directly from source; definitions are verbatim; inheritance rules explicit
- Confidence rationale: HIGH -- the source provides a complete formal treatment with the variance table, multiple worked examples, and explicit rules for struct variance inheritance
- Uncertainties: None -- this is one of the most thoroughly covered topics in the Nomicon
- Cross-reference status: All slugs reference cards in the nomicon extraction set
