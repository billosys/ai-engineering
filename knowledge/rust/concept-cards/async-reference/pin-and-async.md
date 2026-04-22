---
concept: Pin and Async
slug: pin-and-async
category: async-programming
subcategory: null
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Pinning and async programming"
extraction_confidence: high
aliases:
  - "pinning and async/await"
  - "why async needs pinning"
  - "futures and pinning"
prerequisites:
  - pinning
  - pin-type
  - self-referential-type
  - move-semantics
extends:
  - pinning
  - self-referential-type
related:
  - future-poll-signature
  - manual-pinning
  - address-sensitivity
contrasts_with: []
answers_questions:
  - "How does pinning relate to async/await implementation?"
  - "Why do async functions need pinning?"
  - "Why does Future::poll require Pin<&mut Self>?"
---

# Quick Definition

Async functions are compiled into future structs where local variables become fields. When a variable references another variable across an await point, the future becomes self-referential, requiring pinning to ensure the internal references remain valid.

# Core Definition

"Async functions are implemented as futures. At each await point execution of the function may be paused and during that time the values of live variables must be saved. They essentially become fields of a struct (which is part of an enum). Such variables may refer to other variables which are saved in the future." (Ch. 2, "Pinning and async programming")

The source illustrates with a concrete example: given an async function where variable `b` references variable `a` across an await point, the generated future struct would look like:
```rust
struct Foo {
    a: A,
    b: &'self A,  // Invariant: self.b == &self.a
}
```

"if we know that once it is created, then an instance of `Foo` will never move, then everything Just Works. (The compiler has a concept similar to `'self` internally for such cases, as a programmer, we would have to use raw pointers and unsafe code). This concept of not moving is exactly what pinning describes." (Ch. 2, "Pinning and async programming")

"We see this requirement in the signature of `Future::poll`, where the type of `self` (the future) is `Pin<&mut Self>`. Mostly, when using async/await, the compiler takes care of pinning and unpinning, and as a programmer you don't need to worry about it." (Ch. 2, "Pinning and async programming")

# Prerequisites

- **Pinning** — The abstract concept that pin-and-async depends on
- **Pin type** — The concrete type that appears in `Future::poll`
- **Self-referential type** — Compiler-generated futures are self-referential; understanding why self-references are problematic is essential
- **Move semantics** — Moving a self-referential future would invalidate internal references

# Key Properties

1. Async functions compile into state-machine structs where local variables become fields
2. Variables alive across await points are stored as fields of the generated future struct
3. When a local variable references another local variable across an await point, the future becomes self-referential
4. Rust does not have a `'self` lifetime, so self-references cannot be expressed in the type system directly
5. If a self-referential future were moved, internal references would become dangling pointers
6. Pinning guarantees the future won't move once created, making self-references safe
7. The compiler uses an internal concept similar to `'self` and raw pointers for the implementation
8. `Future::poll` takes `Pin<&mut Self>` to ensure the future is pinned before polling
9. The async/await syntax handles pinning automatically in most cases

# Construction / Recognition

## To Understand When Async Needs Pinning

1. Identify variables that are live across await points in an async function
2. Check if any of these variables reference other variables that are also live across await points
3. If so, the generated future is self-referential and requires pinning
4. The compiler handles this automatically when using `async`/`await`

## To Recognize When Pinning Becomes Visible

1. Working with futures directly (not through `async`/`await`)
2. Polling a future manually (must pin it first)
3. Using `select!` with a reference to a future (must pin the reference)
4. Implementing a custom future (must work with `Pin<&mut Self>` in `poll`)

# Context & Application

Pinning exists in Rust primarily because of async/await. The source is clear: "Hopefully, you can do all you ever want to do with async Rust and never worry about pinning." For most programmers, `async`/`await` handles pinning transparently. Pinning becomes visible in edge cases: implementing custom futures, using combinators, or working with futures by reference.

The historical context is important: pinning was not designed as a general-purpose mechanism. It was added to Rust post-1.0 specifically to make async/await possible while maintaining backwards compatibility. The source notes in the alternatives section that "If you are designing a brand new language and want to support async/await, self-references, or immovable types there are certainly better ways to do so than Rust's pinning." (Ch. 2, "Alternatives and extensions")

# Examples

**Self-referential async function** (Ch. 2, "Pinning and async programming"):
```rust
async fn foo() {
    let a = ...;
    let b = &a;
    bar().await;
    // use b
}
```

**Generated future (simplified)** (Ch. 2, "Pinning and async programming"):
```rust
struct Foo {
    a: A,
    b: &'self A,  // Invariant `self.b == &self.a`
}
```

**Why moving breaks this** (Ch. 2, "Pinning and async programming"):
```rust
let f1 = Foo { ... }; // f1.b == &f1.a
let f2 = f1; // f2.b == &f1.a, but f1 no longer exists since it moved to f2
```

**The solution** (Ch. 2, "Pinning and async programming"):
> "if we know that once it is created, then an instance of `Foo` will never move, then everything Just Works. ... This concept of not moving is exactly what pinning describes."

# Relationships

## Builds Upon
- **Pinning** — Async is the primary motivation for pinning in Rust
- **Self-referential type** — Compiler-generated futures are the canonical example of self-referential types
- **Move semantics** — Moving self-referential futures is the problem pinning solves

## Enables
- **Future poll signature** — The requirement for `Pin<&mut Self>` in `Future::poll` follows directly from this
- **Manual pinning** — When the async/await abstraction leaks, manual pinning is needed

## Related
- **Address sensitivity** — Futures with self-references are address-sensitive
- **Cancellation safety** — Pinning interacts with async cancellation since dropping a pinned future ends the pinning contract

## Contrasts With
(none)

# Common Errors

- **Error**: Moving a future after it has been polled (when not using async/await).
  **Correction**: Once a future has been polled, it may contain self-references. It must be pinned before polling and must not be moved afterward.

- **Error**: Trying to use a future by reference in `select!` without pinning it.
  **Correction**: Pin the reference using `pin!` before passing it to `select!`.

# Common Confusions

- **Confusion**: Believing all async functions produce self-referential futures.
  **Clarification**: Only async functions where a variable references another variable across an await point produce self-referential futures. Many simple async functions do not.

- **Confusion**: Thinking pinning is a general-purpose mechanism for self-referential types.
  **Clarification**: Pinning was designed specifically for async/await implementation. Using it for other self-referential use cases "generally only works if it is wrapped in thick layers of abstraction, since it will require lots of fiddly and hard to reason about unsafe code." (Ch. 2, footnote 1)

# Source Reference

Chapter 2: Pinning, section "Pinning and async programming."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Pinning and async programming" section (lines 235-273 of source)
- Confidence rationale: HIGH — the source provides a thorough explanation with concrete code examples showing the generated future struct and why pinning is necessary
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (pinning, self-referential-type, move-semantics, address-sensitivity, cancellation-safety) and co-extracted concepts (pin-type, future-poll-signature, manual-pinning)
