---
concept: Uninitialized Memory
slug: uninitialized-memory
category: unsafe-rust
subcategory: memory
tier: advanced
source: "The Rustonomicon"
source_slug: nomicon
authors: "The Rust Project"
chapter: "Working With Uninitialized Memory"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "MaybeUninit"
  - "uninitialized memory"
  - "drop flags"
  - "checked uninitialized memory"
  - "unchecked uninitialized memory"
  - "ptr::write"
  - "mem::uninitialized"
prerequisites: []
extends: []
related:
  - ownership-based-resource-management
  - unwinding-and-exception-safety
  - unsafe-concurrency
contrasts_with: []
answers_questions:
  - "How does Rust prevent reading uninitialized memory in safe code?"
  - "What is MaybeUninit and how do I use it?"
  - "What are drop flags and how do they work?"
  - "How do I initialize an array element by element in unsafe Rust?"
  - "What is the difference between checked and unchecked uninitialized memory?"
  - "Why was mem::uninitialized deprecated in favor of MaybeUninit?"
  - "How do ptr::write, ptr::copy, and ptr::copy_nonoverlapping differ?"
  - "When does Rust track drop state at runtime vs compile time?"
---

# Quick Definition

All runtime-allocated memory in Rust begins as uninitialized. Safe Rust statically prevents reading uninitialized memory through branch analysis. Unsafe Rust provides `MaybeUninit` to work with memory that has not been fully initialized, while drop flags track at runtime whether conditionally initialized values should be dropped.

# Core Definition

"All runtime-allocated memory in a Rust program begins its life as *uninitialized*. In this state the value of the memory is an indeterminate pile of bits that may or may not even reflect a valid state for the type that is supposed to inhabit that location of memory. Attempting to interpret this memory as a value of *any* type will cause Undefined Behavior." (Ch. 5, Introduction)

Rust provides two layers for managing uninitialized memory. The checked (safe) layer uses static analysis: "Like C, all stack variables in Rust are uninitialized until a value is explicitly assigned to them. Unlike C, Rust statically prevents you from ever reading them until you do." This analysis ensures "every branch must assign a value to `x` before it is first used." (Ch. 5, Checked Uninitialized Memory)

For runtime tracking, "Rust actually tracks whether a type should be dropped or not *at runtime*. As a variable becomes initialized and uninitialized, a *drop flag* for that variable is toggled." When the initialization state is statically known, the compiler generates more efficient code with *static drop semantics*; otherwise the flag is checked at runtime. (Ch. 5, Drop Flags)

The unchecked (unsafe) layer centers on `MaybeUninit`: "Unsafe Rust gives us a powerful tool to handle this problem: `MaybeUninit`. This type can be used to handle memory that has not been fully initialized yet." In memory, `MaybeUninit<T>` looks the same as `T`, allowing transmutation after initialization. (Ch. 5, Unchecked Uninitialized Memory)

# Prerequisites

This is an advanced concept with no formal prerequisites within this source. Understanding ownership, moves, and the Drop trait is assumed.

# Key Properties

1. **Static branch analysis**: The compiler tracks initialization across all branches; every branch must assign a value before first use, but the analysis does not consider constant values
2. **Delayed initialization**: A variable need not be mutable for delayed initialization if every branch assigns exactly once
3. **Move creates uninit**: Moving out of a non-Copy variable makes it logically uninitialized; reassigning afterward requires `mut`
4. **Drop flags on the stack**: Runtime flags track whether conditionally initialized values need dropping; in old Rust versions these were hidden fields in Drop types
5. **Static drop semantics**: When initialization state is statically known, the compiler eliminates runtime flag checks (straight-line code, uniform branching)
6. **MaybeUninit<T>**: Safe wrapper for uninitialized memory; dropping a `MaybeUninit` does nothing, which prevents double-free of uninitialized data
7. **Transmute after init**: `MaybeUninit<T>` has the same layout as `T` for arrays, enabling `mem::transmute` after full initialization; but `Container<MaybeUninit<T>>` does NOT always match `Container<T>` (e.g., `Option<bool>` vs `Option<MaybeUninit<bool>>`)
8. **ptr module functions**: `ptr::write`, `ptr::copy`, and `ptr::copy_nonoverlapping` assign to memory without dropping the old value
9. **Raw pointer requirement**: Constructing a *reference* to uninitialized data is illegal; use raw reference syntax (`&raw mut`) to get a pointer to struct fields without creating an intermediate reference
10. **mem::uninitialized is deprecated**: "Always use `MaybeUninit` instead in new code, and port old code over when you get the opportunity"
11. **Panic interaction**: Every control path through a variable's scope must initialize the value before it ends if it has a destructor, including code that panics

# Construction / Recognition

## To Initialize an Array Element by Element:
1. Create an array of `MaybeUninit<T>` using `[const { MaybeUninit::uninit() }; SIZE]`
2. Initialize each element using `MaybeUninit::new(value)` via indexed assignment
3. After all elements are initialized, transmute: `mem::transmute::<_, [T; SIZE]>(array)`
4. Dropping `MaybeUninit` does nothing, so the assignment operator on `x[i]` is safe even though the compiler considers the slot already initialized

## To Write to Uninitialized Memory Without Dropping:
1. Obtain a raw pointer (not a reference) to the target location
2. Use `ptr::write(ptr, val)` to move a value into the location without dropping the old value
3. Or use `ptr::copy(src, dest, count)` (like C's `memmove`) or `ptr::copy_nonoverlapping(src, dest, count)` (like C's `memcpy`)

## To Initialize Struct Fields Individually:
1. Create `MaybeUninit::<Struct>::uninit()`
2. Use `&raw mut (*uninit.as_mut_ptr()).field` to get a raw pointer to the field without creating a reference
3. Use `f1_ptr.write(value)` to initialize the field
4. After all fields are initialized, call `uninit.assume_init()`

# Context & Application

Uninitialized memory handling is one of the foundational concerns of unsafe Rust. The chapter establishes that safe Rust's branch analysis provides strong guarantees against reading uninitialized memory, but unsafe code must manually manage initialization state.

The drop flag mechanism reveals an important implementation detail: Rust does not purely rely on static analysis for drop decisions. Conditional initialization paths force runtime tracking, though the compiler optimizes this away when possible (static drop semantics).

`MaybeUninit` replaced the older `mem::uninitialized` function, which "turned out to be impossible to properly integrate with the rest of the language." The key insight is that `MaybeUninit<T>` is a union type whose drop does nothing, making it safe to assign over uninitialized slots without triggering drops of garbage data.

The subtle distinction between `Container<MaybeUninit<T>>` and `Container<T>` is important: while arrays allow the transmute, types like `Option` exploit validity constraints of their inner type for niche optimization, which `MaybeUninit` breaks.

# Examples

**Example 1** (Ch. 5, Checked): Static analysis prevents reading possibly uninitialized variables, even with sophisticated control flow understanding:
```rust
let x: i32;
if true {
    x = 1;
} else {
    x = 2;
}
println!("{}", x); // OK: both branches assign
```

**Example 2** (Ch. 5, Drop Flags): Runtime flags resolve conditional initialization:
```rust
let x;
if condition {
    x = Box::new(0);    // x was uninit; just overwrite
    println!("{}", x);
}
// x goes out of scope; x might be uninit; check the flag!
```

**Example 3** (Ch. 5, MaybeUninit Array): Element-by-element array initialization:
```rust
use std::mem::{self, MaybeUninit};
const SIZE: usize = 10;
let x = {
    let mut x = [const { MaybeUninit::uninit() }; SIZE];
    for i in 0..SIZE {
        x[i] = MaybeUninit::new(Box::new(i as u32));
    }
    unsafe { mem::transmute::<_, [Box<u32>; SIZE]>(x) }
};
```

**Example 4** (Ch. 5, Raw Reference): Initializing struct fields without creating references to uninitialized data:
```rust
use std::{ptr, mem::MaybeUninit};
struct Demo { field: bool }
let mut uninit = MaybeUninit::<Demo>::uninit();
let f1_ptr = unsafe { &raw mut (*uninit.as_mut_ptr()).field };
unsafe { f1_ptr.write(true); }
let init = unsafe { uninit.assume_init() };
```

# Relationships

## Builds Upon
- Ownership and move semantics (moves create logically uninitialized state)
- The Drop trait (drop flags exist to manage destructors)

## Enables
- **ownership-based-resource-management** -- safe OBRM depends on correct initialization and destruction
- Safe element-by-element array initialization in unsafe code

## Related
- **unwinding-and-exception-safety** -- panicking through uninitialized memory causes double-frees or leaks
- **unsafe-concurrency** -- concurrent initialization requires additional synchronization

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `*x[i].as_mut_ptr() = value` to write to MaybeUninit elements.
  **Correction**: This overwrites a `Box<T>` through the raw pointer, triggering a drop of uninitialized data. Use `x[i] = MaybeUninit::new(value)` instead, or use `ptr::write`.

- **Error**: Creating a reference (`&mut`) to uninitialized struct fields.
  **Correction**: "It is illegal to construct a *reference* to uninitialized data." Use raw reference syntax: `&raw mut (*uninit.as_mut_ptr()).field`.

- **Error**: Using `mem::uninitialized()` in new code.
  **Correction**: This function is deprecated. "Always use `MaybeUninit` instead in new code."

- **Error**: Assuming `Container<MaybeUninit<T>>` has the same layout as `Container<T>`.
  **Correction**: This is only true for arrays. For types like `Option<bool>`, niche optimization means `Option<MaybeUninit<bool>>` has a different layout than `Option<bool>`.

# Common Confusions

- **Confusion**: Thinking drop flags add overhead to all types.
  **Clarification**: Drop flags are only needed when initialization state cannot be determined statically. Straight-line code and uniformly branching code use static drop semantics with no runtime cost.

- **Confusion**: Believing `MaybeUninit<T>` prevents all initialization bugs.
  **Clarification**: `MaybeUninit` prevents double-free of uninitialized data by making drop a no-op. But in case of a panic, "instead of a double-free of the not yet initialized parts, you end up with a memory leak of the already initialized parts." It does not eliminate the problem, only changes its character.

- **Confusion**: Thinking types without `Drop` need the same care around uninitialized memory.
  **Clarification**: "You don't need to worry about `ptr::write`-style shenanigans with types which don't implement `Drop` or contain `Drop` types, because Rust knows not to try to drop them."

# Source Reference

Chapter 5: Working With Uninitialized Memory -- all sections: Checked Uninitialized Memory (static branch analysis, move semantics), Drop Flags (runtime tracking, static drop semantics, stack-stored flags), Unchecked Uninitialized Memory (MaybeUninit, array initialization, ptr::write/copy/copy_nonoverlapping, raw references, mem::uninitialized deprecation).

# Verification Notes

- Definition source: Direct quotations from Ch. 5 introduction, Checked, Drop Flags, and Unchecked sections
- MaybeUninit details: Directly from Unchecked section with code examples
- Drop flag mechanics: Directly from Drop Flags section including static vs runtime semantics
- Container<MaybeUninit<T>> caveat: Directly from Unchecked section (Option<bool> example)
- Confidence rationale: HIGH -- the chapter is explicit and self-contained with clear code examples
- Uncertainties: None
