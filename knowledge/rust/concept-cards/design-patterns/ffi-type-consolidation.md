---
concept: Type Consolidation into Wrappers for FFI
slug: ffi-type-consolidation
category: ffi-pattern
subcategory: null
tier: advanced
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Type Consolidation into Wrappers"
extraction_confidence: high
aliases:
  - "consolidated wrapper"
  - "FFI wrapper type"
  - "type consolidation"
prerequisites:
  - ffi-object-based-api
  - contain-unsafety
extends:
  - ffi-object-based-api
related:
  - ffi-object-based-api
  - contain-unsafety
  - raii-guards
contrasts_with: []
answers_questions:
  - "How do I expose Rust iterators through FFI safely?"
  - "How do I consolidate multiple Rust types into a single FFI-safe object?"
  - "Why is wrapping iterators for FFI so difficult in Rust?"
---

# Quick Definition

When exporting Rust types through FFI, consolidate multiple related types (such as a collection and its iterator) into a single wrapper struct that manages all state internally. This avoids exposing Rust's lifetime relationships across the FFI boundary, where foreign code cannot enforce them, minimizing the surface area for memory unsafety.

# Core Definition

"This pattern is designed to allow gracefully handling multiple related types, while minimizing the surface area for memory unsafety." The source explains that when Rust types are exported to other languages, "they are usually transformed into pointers. In Rust, a pointer means 'the user manages the lifetime of the pointee.'" The "consolidated wrapper" folds "all possible interactions with an object into a 'wrapper type', while keeping the Rust API clean." This is described as "the lowest risk API." (Ch. 2, "Type Consolidation into Wrappers")

# Prerequisites

- **ffi-object-based-api** -- type consolidation is a companion technique to the object-based API pattern; understanding encapsulated vs. transactional types is essential
- **contain-unsafety** -- the wrapper contains unsafe lifetime management within a safe Rust type

# Key Properties

1. Multiple related Rust types are combined into a single wrapper struct
2. The wrapper internalizes state that would otherwise require separate lifetime-bounded types (e.g., iterator position stored as an index rather than an iterator object)
3. The wrapper presents a simple API that avoids exposing Rust lifetime relationships
4. The wrapper itself contains no `unsafe` code; all unsafety is at the FFI boundary
5. If the collection supports efficient `nth()`, iteration state can be ephemeral (recreated each call)
6. The wrapper trades some API expressiveness for memory safety guarantees

# Construction / Recognition

## To Apply Type Consolidation:
1. Identify the primary Rust type that will be exposed through FFI (e.g., a collection)
2. Identify related types that have lifetime dependencies on the primary type (e.g., iterators)
3. Create a wrapper struct containing the primary type plus any state needed for the related types' functionality (e.g., an index counter instead of an iterator)
4. Implement methods on the wrapper that provide the combined functionality without exposing separate lifetime-bounded types
5. Export `extern "C"` functions that operate on the wrapper

## To Recognize This Pattern:
1. A wrapper struct containing a Rust collection plus iteration state as a simple integer index
2. Methods like `first_key`/`next_key` that manage iteration internally
3. No separate iterator type exposed to foreign callers

# Context & Application

The source illustrates the pattern with a `MySetWrapper` that wraps `MySet` and stores an `iter_next: usize` index. The `first_key()` method resets the index to 0, and `next_key()` uses `nth()` on the collection's iterator to advance. This avoids exposing a separate iterator type with a lifetime bound on the collection.

The source then extensively discusses why naively wrapping iterators fails. Storing a lifetime-erased iterator (`Option<NonNull<KeysIter<'static>>>` created via `transmute`) inside the wrapper leads to undefined behavior: if the collection is mutated during iteration (e.g., via a `myset_store` function), both the mutable reference to the collection and the shared reference from the iterator exist simultaneously, violating Rust's aliasing rules. The source explains: "According to Rust, the mutable reference in this block must have exclusive access to the object. If the iterator simply exists, it's not exclusive, so we have undefined behaviour!"

The solution is to avoid storing the iterator at all: use index-based access via `nth()`, reconstructing the iteration position each call. This is less efficient than a C version (which can simply use raw pointers without aliasing constraints), but it is sound.

# Examples

**Example 1** (Ch. 2, "Type Consolidation" -- Correct Wrapper): `struct MySetWrapper { myset: MySet, iter_next: usize }` with `first_key()` resetting `iter_next` to 0 and `next_key()` calling `self.myset.keys().nth(self.iter_next)` then incrementing. "The wrapper is simple and contains no unsafe code."

**Example 2** (Ch. 2, "Type Consolidation" -- Failing Approach): A wrapper storing `iterator: Option<NonNull<KeysIter<'static>>>` created via `transmute`. The source demonstrates that calling `myset_store` while the iterator exists creates undefined behavior because the mutable reference to the collection conflicts with the iterator's shared reference. "If the iterator simply exists, it's not exclusive, so we have undefined behaviour!"

# Relationships

## Builds Upon
- **ffi-object-based-api** -- type consolidation implements the object-based principle of consolidating lifetimes into the encapsulated type
- **contain-unsafety** -- the wrapper keeps unsafe lifetime management contained

## Enables
- Safe iteration over Rust collections from C/foreign code
- FFI APIs that avoid exposing Rust's lifetime system

## Related
- **raii-guards** -- both manage resource lifecycle, though RAII guards are for Rust-internal use while wrappers are for FFI export

## Contrasts With
- Exposing separate iterator types through FFI (unsafe, leads to aliasing violations)
- Using `transmute` to erase lifetimes on iterators (leads to undefined behavior)

# Common Errors

- **Error**: Storing a lifetime-erased iterator inside the wrapper using `transmute`.
  **Correction**: Store iteration state as a simple index. Use `nth()` to recreate the iterator position on each call. The source explicitly labels the `transmute` approach as leading to undefined behavior.

- **Error**: Allowing mutation of the underlying collection while iteration state exists as a separate object.
  **Correction**: Either invalidate iteration state on mutation, or use index-based access that does not hold a reference to the collection between calls.

# Common Confusions

- **Confusion**: Thinking the consolidated wrapper is always less efficient than exposing separate types.
  **Clarification**: The source acknowledges C can be more efficient because "it cheats -- Rust's aliasing rules are the problem, and C simply ignores them." However, the wrapper approach trades some efficiency for guaranteed soundness. If `nth()` is O(1), the overhead is minimal.

- **Confusion**: Thinking undefined behavior from aliasing only matters when the iterator is actively being read.
  **Clarification**: The source explains (in a footnote): "the iterator need not be read during this code to cause the UB. The exclusivity rule also enables compiler optimizations which may cause inconsistent observations by the iterator's shared reference (e.g. stack spills or reordering instructions for efficiency). These observations may happen any time after the mutable reference is created."

# Source Reference

Chapter 2: Design Patterns, "Type Consolidation into Wrappers" section (FFI Patterns). Includes the correct `MySetWrapper` implementation, extensive discussion of why iterator wrapping via `transmute` fails (with code examples showing the undefined behavior), and a footnote explaining Rust's aliasing rules in depth.

# Verification Notes

- Definition source: Direct quotations from "Description" subsection
- Key Properties: Derived from code examples and the extended "Trying to Wrap Iterators (and Failing)" discussion
- Confidence rationale: HIGH -- the source provides both correct and incorrect approaches with detailed explanation of the aliasing-rule violation
- Uncertainties: None
- Cross-reference status: `ffi-object-based-api` and `contain-unsafety` are in this extraction set; `raii-guards` from Agent 3
