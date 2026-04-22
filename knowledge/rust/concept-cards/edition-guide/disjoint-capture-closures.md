---
concept: Disjoint Capture in Closures
slug: disjoint-capture-closures
category: edition-2021
subcategory: null
tier: intermediate
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "Disjoint capture in closures"
extraction_confidence: high
aliases:
  - "precise closure captures"
  - "RFC 2229"
  - "closure field capture"
  - "disjoint field capture"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - edition-migration
contrasts_with: []
answers_questions:
  - "How do closures capture variables differently in Rust 2021?"
  - "What is disjoint capture in closures?"
  - "Why might closures behave differently in Rust 2021 vs 2018?"
  - "How can disjoint capture affect drop order?"
  - "How can disjoint capture affect Send/Sync/Clone?"
  - "What is the rust_2021_incompatible_closure_captures lint?"
---

# Quick Definition

In Rust 2021, closures capture individual fields of variables rather than entire variables. For example, `|| a.x + 1` captures only `a.x` instead of all of `a`. This enables code patterns that were previously rejected (like using other fields of a partially-moved struct) but can change drop order and affect which traits (`Send`, `Sync`, `Clone`) a closure implements.

# Core Definition

"In Rust 2018 and before, closures capture entire variables, even if the closure only uses one field. For example, `|| a.x + 1` captures a reference to `a` and not just `a.x`. Capturing `a` in its entirety prevents mutation or moves from other fields of `a`. [...] Starting in Rust 2021, closures captures are more precise. Typically they will only capture the fields they use." (Edition Guide, Ch. 4: Rust 2021, "Disjoint capture in closures")

This change was proposed as RFC 2229. The migration lint `rust_2021_incompatible_closure_captures` detects cases where the behavioral change could affect program correctness, and `cargo fix --edition` inserts "dummy let" statements (e.g., `let _ = &a`) to force whole-variable capture where needed.

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- disjoint capture is one of the largest behavioral changes in the 2021 edition

# Key Properties

1. Closures capture individual fields instead of entire variables
2. `|| a.x + 1` captures only `a.x` in Rust 2021 (captured all of `a` in Rust 2018)
3. Code that was rejected due to partial borrows/moves may now compile
4. Drop order can change: fields not captured by the closure are dropped when the variable goes out of scope, not when the closure is dropped
5. Trait implementations (`Clone`, `Send`, `Sync`, `UnwindSafe`) can change because different values are captured
6. Wildcard patterns (`let _ = x`) are no-ops that do not capture `x`
7. The "dummy let" `let _ = &x` is not a no-op -- `&x` is an expression that must be evaluated
8. `cargo fix --edition` inserts `let _ = &variable` to force whole-variable capture where needed
9. The migration analysis is conservative: many inserted dummy lets can be safely removed

# Construction / Recognition

## To Understand What a Closure Captures in Rust 2021:
1. Identify all field paths used inside the closure body (e.g., `a.x`, `a.y.z`)
2. Each distinct field path is captured individually
3. Wildcard bindings (`let _ = x`) do not count as capturing `x`
4. The capture mode (by reference, by mutable reference, by move) is determined per-field

## To Manually Migrate Closures:
1. Run `cargo fix --edition` to auto-insert dummy lets
2. Review each dummy let (`let _ = &variable`) in closures
3. Test whether removing the dummy let changes behavior
4. Keep the dummy let if removal changes drop order for types with side-effectful destructors
5. Keep the dummy let if removal changes trait implementations the closure needs (e.g., `Send`)

## To Force Whole-Variable Capture:
1. Insert `let _ = &variable;` at the start of the closure body
2. For `move` closures: `let _ = &variable;` still forces the entire variable to be moved into the closure

# Context & Application

Disjoint capture is one of the biggest changes in Rust 2021. In Rust 2018, closures captured entire variables, which was a frequent source of frustration. For example, you could not move one field of a struct and then create a closure that uses another field, because the closure would try to capture the entire (partially moved) struct.

The change has two categories of observable effects:

**Drop order changes**: When a closure takes ownership of part of a variable, in Rust 2018 the entire variable's lifetime is tied to the closure. In Rust 2021, only the captured fields are tied to the closure, so uncaptured fields may be dropped earlier (when the variable goes out of scope, not when the closure is dropped). This matters for types with side-effectful destructors.

**Trait implementation changes**: Closures automatically implement `Clone`, `Send`, `Sync`, and `UnwindSafe` based on captured values. If a struct is `Send` (e.g., a wrapper around a raw pointer with `unsafe impl Send`), but the individual field being captured is not `Send` (e.g., the raw pointer itself), the closure may lose its `Send` implementation in Rust 2021.

# Examples

**Example 1** (Code that now compiles, "Details" section):

```rust
struct SomeStruct { x: Vec<i32>, y: String }

let a = SomeStruct { x: vec![1], y: String::from("hello") };
drop(a.x);                     // Move out of one field
println!("{}", a.y);            // Still use another field -- OK
let c = || println!("{}", a.y); // Rust 2021: captures only a.y -- OK
                                // Rust 2018: tries to capture all of a -- Error
c();
```

**Example 2** (Drop order change, "Drop Order" subsection):

```rust
fn move_value<T>(_: T) {}

{
    let t = (vec![0], vec![0]);
    {
        let c = || {
            // Rust 2018: captures all of t
            // Rust 2021: captures only t.0
            move_value(t.0);
        };
    } // c dropped here. In 2018: all of t dropped. In 2021: only t.0 dropped.
} // In 2018: t already moved. In 2021: t.1 is dropped here.
```

**Example 3** (Trait implementation change, "Trait implementations" subsection):

```rust
use std::thread;

struct Ptr(*mut i32);
unsafe impl Send for Ptr {}

let mut x = 5;
let px = Ptr(&mut x as *mut i32);

let c = thread::spawn(move || {
    unsafe { *(px.0) += 10; }
});
// Rust 2018: captures all of px (which is Send) -- compiles
// Rust 2021: captures only px.0 (a *mut i32, which is NOT Send) -- may fail
```

**Example 4** (Dummy let insertion, "Migration" section):

```rust
let x = (vec![22], vec![23]);
let c = move || {
    // "Dummy let" forces x to be captured in its entirety
    let _ = &x;

    // Without the dummy let, only x.0 would be captured
    println!("{:?}", x.0);
};
```

**Example 5** (Wild card patterns, "Wild Card Patterns" subsection):

```rust
let x = 10;
let c = || {
    let _ = x; // This is a no-op; x is NOT captured
};

let c = || match x {
    _ => println!("Hello World!") // x is NOT captured
};
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- disjoint capture is one of the major 2021 edition changes

## Enables
- No downstream concepts directly

## Related
- **edition-migration** -- `cargo fix --edition` handles the conservative automated migration

## Contrasts With
- None explicitly stated (implicitly contrasts with Rust 2018 whole-variable capture)

# Common Errors

- **Error**: Removing all "dummy let" statements inserted by `cargo fix` without checking for side-effectful destructors.
  **Correction**: The migration analysis is conservative, so many dummy lets can be removed, but review each one. If the variable's type has a `Drop` impl with side effects (e.g., flushing, sending signals), changing when it runs could change program behavior.

- **Error**: Wrapping raw pointers in a `Send`/`Sync` struct and assuming the closure inherits those traits.
  **Correction**: In Rust 2021, the closure captures the individual field (the raw pointer), not the wrapper. If the raw pointer is not `Send`/`Sync`, the closure will not be `Send`/`Sync` either. Insert `let _ = &wrapper;` in the closure to force full capture.

# Common Confusions

- **Confusion**: Thinking `let _ = x` captures `x` in a closure.
  **Clarification**: `let _ = x` is a no-op that does not capture `x`, because `_` completely ignores the right-hand side when the RHS is a reference to a place in memory. However, `let _ = &x` is NOT a no-op -- `&x` is an expression that must be evaluated, forcing `x` to be captured.

- **Confusion**: Thinking disjoint capture only matters for `move` closures.
  **Clarification**: Disjoint capture affects all closures, including those that borrow. A non-`move` closure that references `a.x` will borrow only `a.x`, not all of `a`, which means you can mutably borrow `a.y` separately while the closure is alive.

- **Confusion**: Thinking drop order changes are always problematic.
  **Clarification**: In most cases, changing when values are dropped only affects when memory is freed and is not important. It only matters when `Drop` implementations have side effects. The migration lint specifically checks for this.

# Source Reference

Chapter 4: Rust 2021, "Disjoint capture in closures" section. RFC 2229 contains the detailed motivation and design. The section covers the behavioral change, drop order effects, trait implementation effects, wild card patterns, and the migration lint `rust_2021_incompatible_closure_captures`.

# Verification Notes

- Definition source: Direct quotation from "Disjoint capture in closures" section, "Details" subsection
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides comprehensive documentation including multiple examples for each category of impact (drop order, trait implementations, wild card patterns)
- Uncertainties: The source notes "in some cases, they might capture more than just what they use, see the Rust reference for full details" -- the exact capture rules are more nuanced than presented
- Cross-reference status: All slugs reference cards in this extraction set or Agent A's set
