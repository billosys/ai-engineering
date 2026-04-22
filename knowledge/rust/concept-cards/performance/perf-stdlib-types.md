---
concept: Standard Library Type Performance
slug: perf-stdlib-types
category: performance
subcategory: data-structures
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Standard Library Types"
chapter_number: 9
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "stdlib performance"
  - "Vec performance tips"
  - "swap_remove"
  - "ok_or_else"
  - "parking_lot"
  - "Rc::make_mut"
  - "Arc::make_mut"
prerequisites:
  - perf-heap-allocations
extends: []
related:
  - perf-hashing
  - perf-type-sizes
  - perf-overview
contrasts_with: []
answers_questions:
  - "What are the fastest ways to use Vec in Rust?"
  - "When should I use swap_remove instead of remove?"
  - "Why should I use ok_or_else instead of ok_or?"
  - "What is parking_lot and should I use it?"
  - "What does Rc::make_mut do?"
  - "How do I create a zero-filled Vec efficiently?"
---

# Quick Definition

The Rust standard library types (`Vec`, `Option`, `Result`, `Rc`/`Arc`, `Mutex`, etc.) have performance-relevant methods and alternatives that are easy to overlook. Key tips include using `swap_remove` for O(1) removal, lazy evaluation variants (`ok_or_else`, `map_or_else`), `Rc::make_mut`/`Arc::make_mut` for clone-on-write, and the `parking_lot` crate as a potential replacement for synchronization primitives.

# Core Definition

"It is worth reading through the documentation for common standard library types -- such as `Vec`, `Option`, `Result`, and `Rc`/`Arc` -- to find interesting functions that can sometimes be used to improve performance." The chapter also notes the value of knowing "high-performance alternatives to standard library types, such as `Mutex`, `RwLock`, `Condvar`, and `Once`." (Ch. 9, Standard Library Types introduction)

The chapter provides targeted performance tips for each major type family, focusing on method choices that affect algorithmic complexity and lazy vs. eager evaluation. (Ch. 9, all sections)

# Prerequisites

- **perf-heap-allocations** -- understanding allocation costs motivates many of these optimizations (e.g., `vec![0; n]`, `swap_remove`, lazy evaluation)

# Key Properties

1. **Vec zero-fill**: `vec![0; n]` is the best way to create a zero-filled Vec -- it can use OS assistance and is as fast or faster than alternatives like `resize`, `extend`, or unsafe code
2. **Vec::swap_remove**: O(1) alternative to `Vec::remove` (which is O(n)) -- replaces the element with the last element, not preserving order
3. **Vec::retain**: Efficiently removes multiple items from a Vec; equivalent methods exist on `String`, `HashSet`, and `HashMap`
4. **Lazy evaluation**: `Option::ok_or_else`, `Option::map_or_else`, `Option::unwrap_or_else`, `Result::or_else`, `Result::map_or_else`, and `Result::unwrap_or_else` use closures to defer expensive computation until needed
5. **Rc::make_mut / Arc::make_mut**: Clone-on-write semantics -- if refcount is 1, modifies in place; if >1, clones the inner value to ensure unique ownership
6. **parking_lot**: Alternative implementations of `Mutex`, `RwLock`, `Condvar`, and `Once` with similar but not identical APIs; previously reliably better, but "the standard library versions have greatly improved on some platforms" -- measure before switching
7. Use Clippy's `disallowed_types` to enforce universal use of parking_lot types and prevent accidental use of standard library equivalents

# Construction / Recognition

## To Optimize Vec Operations:
1. Create zero-filled Vecs with `vec![0; n]` (not resize/extend/unsafe)
2. When element order doesn't matter, use `swap_remove` instead of `remove` for O(1) instead of O(n)
3. Use `retain` to remove multiple elements efficiently instead of multiple `remove` calls

## To Optimize Option/Result Chains:
1. Replace `ok_or(expensive())` with `ok_or_else(|| expensive())`
2. Apply the same pattern to `map_or`, `unwrap_or`, `Result::or`, `Result::map_or`, and `Result::unwrap_or` -- use the `_else` variant when the fallback computation is expensive
3. Recognize the pattern: if the argument to `ok_or`/`unwrap_or`/`map_or` involves a function call, allocation, or non-trivial computation, switch to the lazy variant

## To Use Clone-on-Write with Rc/Arc:
1. Use `Rc::make_mut(&mut rc)` or `Arc::make_mut(&mut arc)` to get a mutable reference
2. If the refcount is 1, the value is modified in place (no allocation)
3. If the refcount is >1, the inner value is cloned to ensure unique ownership

## To Evaluate parking_lot:
1. Benchmark your program with both standard library and parking_lot synchronization types
2. If parking_lot is faster, use Clippy's `disallowed_types` to prevent accidental use of standard library equivalents

# Context & Application

This chapter serves as a "tips and tricks" reference for standard library types, complementing the deeper treatment of allocation behavior in the Heap Allocations chapter. The guidance is practical and immediately applicable.

The `swap_remove` vs. `remove` distinction is a classic algorithmic optimization: `remove` must shift all subsequent elements (O(n)), while `swap_remove` simply moves the last element into the gap (O(1)). The trade-off is that element ordering is not preserved.

The eager-vs-lazy evaluation guidance (`ok_or` vs `ok_or_else`) is a pattern that appears throughout the standard library. The eager variants evaluate their arguments unconditionally, even when the value is not needed (e.g., when the Option is `Some`). This is wasteful if the fallback involves computation or allocation.

`Rc::make_mut`/`Arc::make_mut` are described as "not needed often, but extremely useful on occasion." They enable an efficient copy-on-write pattern where shared data is only cloned when it actually needs to be mutated and is shared.

The parking_lot recommendation has evolved: while it "used to be reliably smaller, faster, and more flexible," the standard library has improved. This is a good example of the book's practical, evidence-based approach: always measure.

# Examples

**Example 1** (Ch. 9, Vec): `Vec::swap_remove` replaces an element at index i with the final element:
- `Vec::remove(i)` is O(n) -- shifts all subsequent elements left
- `Vec::swap_remove(i)` is O(1) -- swaps with last element, does not preserve ordering

**Example 2** (Ch. 9, Option and Result): Lazy vs. eager evaluation:
```rust
// Eager: always evaluates expensive(), even when o is Some
let r = o.ok_or(expensive());

// Lazy: only evaluates expensive() when o is None
let r = o.ok_or_else(|| expensive());
```

**Example 3** (Ch. 9, Rc/Arc): `Rc::make_mut`/`Arc::make_mut` provide clone-on-write semantics, cloning the inner value only when the reference count is greater than one.

# Relationships

## Builds Upon
- **perf-heap-allocations** -- allocation awareness motivates many of these type-level optimizations

## Enables
- More efficient use of standard library types throughout a Rust program

## Related
- **perf-hashing** -- hash table performance is closely related to hash map usage patterns
- **perf-type-sizes** -- type sizes affect Vec and other container performance
- **perf-overview** -- Clippy's `disallowed_types` enforces consistent use of alternative types

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `Vec::remove` in a hot loop where element order doesn't matter.
  **Correction**: Use `Vec::swap_remove` for O(1) removal. Only use `remove` when element ordering must be preserved.

- **Error**: Using `ok_or(format!("error: {}", x))` which allocates even when the Option is Some.
  **Correction**: Use `ok_or_else(|| format!("error: {}", x))` to defer the allocation until it's actually needed.

- **Error**: Cloning an entire Rc/Arc value when only a mutable reference is needed and the refcount might be 1.
  **Correction**: Use `Rc::make_mut` or `Arc::make_mut`, which modifies in place when the refcount is 1 and only clones when necessary.

# Common Confusions

- **Confusion**: Thinking parking_lot is always faster than standard library synchronization types.
  **Clarification**: "The standard library versions have greatly improved on some platforms. So you should measure before switching to `parking_lot`." The blanket recommendation to use parking_lot is outdated.

- **Confusion**: Thinking `vec![0; n]` is naive or slow because it looks simple.
  **Clarification**: It is "as fast or faster" than alternatives including resize, extend, or unsafe code because "it can use OS assistance" for zero-filling large allocations.

- **Confusion**: Thinking the `_else` variants are always necessary.
  **Clarification**: The eager variants (`ok_or`, `unwrap_or`, `map_or`) are fine when the fallback value is cheap to compute (e.g., a literal, a Copy type). The lazy `_else` variants are only needed when the fallback is expensive (function calls, allocations, I/O).

# Source Reference

Chapter 9: Standard Library Types -- all sections: Vec (`vec![0; n]`, `swap_remove`, `retain`), Option and Result (lazy evaluation variants), Rc/Arc (`make_mut`), Mutex/RwLock/Condvar/Once (parking_lot alternatives).

# Verification Notes

- Definition source: Direct quotation from Ch. 9 introduction
- Vec tips: Directly from the Vec section
- Option/Result lazy evaluation: Directly from the Option and Result section with code examples
- Rc/Arc make_mut: Directly from the Rc/Arc section
- parking_lot: Directly from the Mutex/RwLock/Condvar/Once section, including the nuanced recommendation
- Confidence rationale: HIGH -- the chapter provides explicit, actionable guidance with clear method names and trade-offs
- Uncertainties: None
