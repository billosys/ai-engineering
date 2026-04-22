---
concept: Inlining for Performance
slug: perf-inlining
category: performance
subcategory: code-optimization
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Inlining"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "inline attribute"
  - "#[inline]"
  - "#[inline(always)]"
  - "#[inline(never)]"
  - "cross-crate inlining"
  - "outlining"
  - "#[cold]"
prerequisites:
  - perf-profiling
extends: []
related:
  - perf-build-configuration
  - perf-heap-allocations
contrasts_with: []
answers_questions:
  - "When should I use #[inline] in Rust?"
  - "What is the difference between #[inline], #[inline(always)], and #[inline(never)]?"
  - "How do I inline a function at one call site but not others?"
  - "What is outlining and when should I use #[cold]?"
  - "How can I tell if a function was inlined using Cachegrind?"
---

# Quick Definition

Inlining removes function call overhead and enables further compiler optimizations. Rust provides four inline attributes -- none, `#[inline]`, `#[inline(always)]`, and `#[inline(never)]` -- which are hints rather than guarantees. For functions with mixed hot/cold call sites, splitting into always-inlined and never-inlined variants is an effective technique.

# Core Definition

"Entry to and exit from hot, uninlined functions often accounts for a non-trivial fraction of execution time. Inlining these functions removes these entries and exits and can enable additional low-level optimizations by the compiler. In the best case the overall effect is small but easy speed wins." (Ch. 5, Inlining introduction)

Four inline attributes are available:
- **None**: The compiler decides based on optimization level, function size, whether it's generic, and whether it's cross-crate
- **`#[inline]`**: Suggests the function should be inlined
- **`#[inline(always)]`**: Strongly suggests inlining (effectively guarantees it in all but exceptional cases)
- **`#[inline(never)]`**: Strongly suggests the function should not be inlined

"Inline attributes do not guarantee that a function is inlined or not inlined, but in practice `#[inline(always)]` will cause inlining in all but the most exceptional cases." (Ch. 5)

# Prerequisites

- **perf-profiling** -- profiling (especially with Cachegrind) is needed to identify hot uninlined functions and verify the effects of inlining changes

# Key Properties

1. Inline attributes are hints, not guarantees, though `#[inline(always)]` is nearly always honored
2. The best candidates for inlining are (a) very small functions and (b) functions with a single call site
3. The compiler often inlines these automatically, but attributes are sometimes needed
4. Inlining is non-transitive: if `f` calls `g` and both should be inlined at a callsite to `f`, both must be marked with inline attributes
5. The effects of inlining can be unpredictable: adding `#[inline]` may cause a nearby previously-inlined function to no longer be inlined
6. Inlining can affect compile times, especially cross-crate inlining which duplicates internal representations
7. Cachegrind can verify inlining: an inlined function's first and last lines will not have event counts
8. The `#[cold]` attribute on rarely-executed functions improves code generation for the hot path (outlining)

# Construction / Recognition

## To Apply Inlining Optimizations:
1. Profile with Cachegrind to identify hot uninlined functions
2. For very small or single-call-site functions that the compiler missed, add `#[inline]` or `#[inline(always)]`
3. Measure again -- effects can be unpredictable
4. Verify inlining in Cachegrind output: inlined functions have no event counts on their first and last lines

## To Handle Mixed Hot/Cold Call Sites:
1. Split the function into two variants:
   ```rust
   #[inline(always)]
   fn inlined_my_function() {
       // original function body
   }

   #[inline(never)]
   fn uninlined_my_function() {
       inlined_my_function();
   }
   ```
2. Use the `#[inline(always)]` variant at the hot call site
3. Use the `#[inline(never)]` variant at cold call sites to avoid code bloat

## To Apply Outlining:
1. Identify rarely-executed code paths (error handling, panic paths)
2. Move them to separate functions marked with `#[cold]`
3. This tells the compiler the function is rarely called, improving code generation for the hot path

# Context & Application

Inlining is one of the most accessible code-level optimizations in Rust. The compiler generally does a good job of deciding what to inline, so manual intervention is a refinement step, not a first resort. The technique is most impactful for hot, small functions that the compiler failed to inline automatically.

The split-function technique for hot/cold call sites is particularly useful in large codebases where a utility function is called from many locations but only one or two are performance-critical. This avoids the code bloat of inlining everywhere while capturing the speed benefit where it matters.

Cross-crate inlining is a special concern: generic functions are always available for inlining across crates, but non-generic functions require `#[inline]` to be eligible for cross-crate inlining. This has compile-time implications because the compiler must duplicate internal representations.

# Examples

**Example 1** (Ch. 5, Cachegrind verification): How to tell if a function was inlined using Cachegrind output:
```text
      .  #[inline(always)]
      .  fn inlined(x: u32, y: u32) -> u32 {
700,000      eprintln!("inlined: {} + {}", x, y);
200,000      x + y
      .  }
      .
      .  #[inline(never)]
400,000  fn not_inlined(x: u32, y: u32) -> u32 {
700,000      eprintln!("not_inlined: {} + {}", x, y);
200,000      x + y
200,000  }
```
The inlined function's first and last lines show `.` (no counts), while the not-inlined function's entry line shows counts.

**Example 2** (Ch. 5, Harder Cases): Splitting a function for selective inlining:
```rust
#[inline(always)]
fn inlined_my_function() {
    one();
    two();
    three();
}

#[inline(never)]
fn uninlined_my_function() {
    inlined_my_function();
}
```

# Relationships

## Builds Upon
- **perf-profiling** -- Cachegrind is specifically recommended for identifying inlining opportunities

## Enables
- General code optimization -- inlining enables further low-level compiler optimizations

## Related
- **perf-build-configuration** -- LTO and codegen-units settings affect the compiler's inlining decisions, especially across crate boundaries

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Adding `#[inline(always)]` to large functions used at many call sites.
  **Correction**: This causes code bloat without proportional speed gains. Use the split-function technique to inline only at hot call sites.

- **Error**: Adding inline attributes without measuring the effect.
  **Correction**: "You should measure again after adding inline attributes, because the effects can be unpredictable. Sometimes it has no effect because a nearby function that was previously inlined no longer is. Sometimes it slows the code down."

- **Error**: Marking only the outer function with `#[inline]` when the inner function also needs inlining.
  **Correction**: "Inlining is non-transitive. If a function `f` calls a function `g` and you want both functions to be inlined together at a callsite to `f`, both functions should be marked with an inline attribute."

# Common Confusions

- **Confusion**: Thinking `#[inline]` guarantees a function will be inlined.
  **Clarification**: "Inline attributes do not guarantee that a function is inlined or not inlined." They are strong hints, not directives. Only `#[inline(always)]` is effectively guaranteed in practice.

- **Confusion**: Thinking the compiler always makes optimal inlining decisions.
  **Clarification**: The compiler makes good decisions in most cases, but it "cannot always make the best choices, so attributes are sometimes needed." This is especially true for cross-crate boundaries where non-generic functions are not inlined by default.

- **Confusion**: Confusing `#[cold]` with `#[inline(never)]`.
  **Clarification**: `#[cold]` tells the compiler a function is rarely called, which improves code generation for the *hot path* (e.g., branch prediction hints). `#[inline(never)]` prevents inlining but does not convey information about call frequency.

# Source Reference

Chapter 5: Inlining -- all sections: introduction (four inline attributes), Simple Cases (best candidates, Cachegrind verification), Harder Cases (split-function technique), Outlining (`#[cold]` attribute).

# Verification Notes

- Definition source: Direct quotations from Ch. 5 introduction and throughout
- Inline attribute semantics: Directly from the chapter's enumeration
- Cachegrind example: Directly reproduced from source
- Split-function technique: Directly from "Harder Cases" section with code examples
- Confidence rationale: HIGH -- the chapter is explicit, well-structured, and provides concrete examples with links to real-world PRs
- Uncertainties: None
