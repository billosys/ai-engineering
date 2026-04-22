---
concept: Type Size Optimization
slug: perf-type-sizes
category: performance
subcategory: memory
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Type Sizes"
chapter_number: 8
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "type layout optimization"
  - "enum size optimization"
  - "boxed slice"
  - "ThinVec"
  - "-Zprint-type-sizes"
  - "static_assertions"
  - "smaller types"
prerequisites:
  - perf-profiling
  - perf-heap-allocations
extends: []
related:
  - perf-build-configuration
  - perf-stdlib-types
contrasts_with: []
answers_questions:
  - "How do I measure the size and layout of Rust types?"
  - "How do I shrink an enum with one large variant?"
  - "What is a boxed slice and when should I use it?"
  - "What is ThinVec and how does it differ from Vec?"
  - "How do I prevent type size regressions?"
  - "Why does Rust use memcpy for types larger than 128 bytes?"
---

# Quick Definition

Shrinking frequently-instantiated types reduces memory usage, cache pressure, and `memcpy` overhead. Techniques include boxing outsized enum variants, using smaller integer types, converting Vec to boxed slices, using ThinVec, and measuring layouts with `-Zprint-type-sizes`. Types larger than 128 bytes trigger `memcpy` instead of inline code.

# Core Definition

"Shrinking oft-instantiated types can help performance." The chapter identifies two performance mechanisms: reducing peak memory usage and cache pressure for frequently allocated types, and avoiding `memcpy` overhead for types exceeding 128 bytes. "Rust types that are larger than 128 bytes are copied with `memcpy` rather than inline code. If `memcpy` shows up in non-trivial amounts in profiles, DHAT's 'copy profiling' mode will tell you exactly where the hot `memcpy` calls are and the types involved." (Ch. 8, introduction)

The Rust compiler automatically sorts struct and enum fields to minimize size (unless `#[repr(C)]` is used), so manual field ordering is unnecessary. Instead, the chapter focuses on structural techniques: boxing large enum variants, using smaller integer types, boxed slices, and ThinVec. (Ch. 8, Field Ordering and subsequent sections)

# Prerequisites

- **perf-profiling** -- DHAT profiling identifies hot allocation points, type sizes, and hot `memcpy` calls
- **perf-heap-allocations** -- understanding heap allocation costs motivates type size optimization

# Key Properties

1. The `-Zprint-type-sizes` flag (nightly only) prints size, layout, alignment, field ordering, and padding for all types in use
2. The compiler automatically reorders struct/enum fields to minimize size (unless `#[repr(C)]` is specified)
3. Types larger than 128 bytes use `memcpy` instead of inline copy code, which can be a performance bottleneck
4. Boxing outsized enum variants reduces overall enum size at the cost of one heap allocation per use of that variant
5. Using smaller integers (u32, u16, u8 instead of usize for indices) can significantly shrink types
6. Boxed slices (`Box<[T]>`) use two words (length + pointer) vs. Vec's three words (length + capacity + pointer)
7. Boxed slices can be created from `Vec::into_boxed_slice()` (drops excess capacity) or directly from `Iterator::collect()`
8. `ThinVec` stores length and capacity in the same allocation as elements, so `size_of::<ThinVec<T>>` is only one word
9. `ThinVec` is especially useful for vectors that are often empty and for shrinking large enum variants containing Vec
10. Static assertions (via `static_assertions` crate) can guard against accidental type size regressions

# Construction / Recognition

## To Measure Type Sizes:
1. Use nightly Rust with the `-Zprint-type-sizes` flag:
   ```bash
   RUSTFLAGS=-Zprint-type-sizes cargo +nightly build --release
   ```
2. Review the output for size, alignment, discriminant, variant sizes, field ordering, and padding
3. Use the `top-type-sizes` crate for a more compact display

## To Shrink Enums with Outsized Variants:
1. Identify the largest variant using `-Zprint-type-sizes`
2. Box the large variant's fields:
   ```rust
   // Before: enum is sized to largest variant
   enum A { X, Y(i32), Z(i32, LargeType) }
   // After: Z variant is just a pointer
   enum A { X, Y(i32), Z(Box<(i32, LargeType)>) }
   ```
3. This is most beneficial when the large variant is relatively rare

## To Use Boxed Slices:
1. Convert a finalized Vec: `let bs: Box<[u32]> = v.into_boxed_slice();`
2. Or collect directly: `let bs: Box<[u32]> = (1..3).collect();`
3. Convert back if needed: `slice::into_vec` (no cloning or reallocation)

## To Prevent Size Regressions:
1. Add a static assertion for hot types:
   ```rust
   #[cfg(target_arch = "x86_64")]
   static_assertions::assert_eq_size!(HotType, [u8; 64]);
   ```
2. Use `cfg(target_arch)` because type sizes vary across platforms

# Context & Application

Type size optimization is a second-order optimization that becomes important for types that are instantiated millions of times or copied frequently. The 128-byte `memcpy` threshold is a concrete, measurable boundary: if hot types can be shrunk below it, inline copy code replaces `memcpy` calls.

The enum variant boxing technique is extensively used in the Rust compiler itself, with six linked PRs demonstrating its application. The key trade-off is that boxing adds a heap allocation for the boxed variant and makes pattern matching slightly less ergonomic.

`ThinVec` is particularly clever: by storing metadata in the same allocation as elements, it reduces the in-struct size to a single word. This is especially valuable when a Vec is a field of a frequently-instantiated struct or the largest variant of an enum, and the Vec is often empty (in which case no allocation occurs at all).

The `static_assertions` approach is a pragmatic way to prevent regressions: since type sizes can vary across platforms, restricting the assertion to x86_64 "is likely to be good enough to prevent regressions in practice."

# Examples

**Example 1** (Ch. 8, Measuring Type Sizes): Output of `-Zprint-type-sizes` for an enum:
```text
print-type-size type: `E`: 32 bytes, alignment: 8 bytes
print-type-size     discriminant: 1 bytes
print-type-size     variant `D`: 31 bytes
print-type-size         padding: 7 bytes
print-type-size         field `.0`: 24 bytes, alignment: 8 bytes
print-type-size     variant `C`: 23 bytes
print-type-size         field `.1`: 1 bytes
print-type-size         field `.3`: 1 bytes
print-type-size         padding: 5 bytes
print-type-size         field `.0`: 8 bytes, alignment: 8 bytes
print-type-size         field `.2`: 8 bytes
```
Note the compiler has reordered variant C's fields to minimize padding.

**Example 2** (Ch. 8, Boxed Slices): Vec uses three words, boxed slice uses two:
```rust
let v: Vec<u32> = vec![1, 2, 3];
assert_eq!(size_of_val(&v), 3 * size_of::<usize>());

let bs: Box<[u32]> = v.into_boxed_slice();
assert_eq!(size_of_val(&bs), 2 * size_of::<usize>());
```

**Example 3** (Ch. 8, Static Assertions): Preventing type size regressions:
```rust
#[cfg(target_arch = "x86_64")]
static_assertions::assert_eq_size!(HotType, [u8; 64]);
```

# Relationships

## Builds Upon
- **perf-profiling** -- DHAT's copy profiling mode identifies hot `memcpy` calls from oversized types
- **perf-heap-allocations** -- boxing enum variants involves a heap allocation trade-off

## Enables
- Reduced memory usage, cache pressure, and `memcpy` overhead for hot types

## Related
- **perf-stdlib-types** -- Vec and other standard library types are common candidates for size optimization
- **perf-build-configuration** -- type size interacts with optimization levels and codegen

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Manually ordering struct fields to minimize size.
  **Correction**: "The Rust compiler automatically sorts the fields in struct and enums to minimize their sizes (unless the `#[repr(C)]` attribute is specified)." Manual field ordering is unnecessary.

- **Error**: Boxing an enum variant that is frequently used.
  **Correction**: "This is more likely to be a net performance win if the `A::Z` variant is relatively rare." If the boxed variant is common, the extra heap allocation per use may outweigh the size savings.

- **Error**: Using `Vec::into_boxed_slice()` on a Vec that will need to grow later.
  **Correction**: Boxed slices cannot grow. Only convert Vecs that are finalized and unlikely to change. Use `slice::into_vec` to convert back if needed.

# Common Confusions

- **Confusion**: Thinking all types benefit equally from size optimization.
  **Clarification**: Only "oft-instantiated" types matter. If a type is created once or rarely, its size has negligible impact on performance. Profile with DHAT to identify which types are worth optimizing.

- **Confusion**: Thinking ThinVec is always better than Vec.
  **Clarification**: ThinVec has a one-word in-struct size but stores metadata alongside elements. This is beneficial for types with many empty Vecs or when shrinking enum variants, but for general Vec usage the overhead of accessing metadata from the heap may not be worthwhile.

- **Confusion**: Thinking the 128-byte threshold is about allocation size.
  **Clarification**: The 128-byte threshold determines whether Rust uses inline code or `memcpy` for *copying* the type. This affects moves, function calls, and other copy operations -- not heap allocation.

# Source Reference

Chapter 8: Type Sizes -- all sections: introduction (128-byte memcpy threshold), Measuring Type Sizes (`-Zprint-type-sizes`, `top-type-sizes`), Field Ordering (automatic reordering), Smaller Enums (boxing variants), Smaller Integers, Boxed Slices, ThinVec, Avoiding Regressions (`static_assertions`).

# Verification Notes

- Definition source: Direct quotations from Ch. 8 introduction
- `-Zprint-type-sizes` output: Directly reproduced from the chapter's example
- Boxing technique: Directly from Smaller Enums section with before/after code
- Boxed slice: Directly from Boxed Slices section with size assertions
- Confidence rationale: HIGH -- the chapter provides concrete tools, code examples, and six linked rustc PRs demonstrating the techniques
- Uncertainties: None
