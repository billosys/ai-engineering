---
concept: Library Interoperability Guidelines
slug: library-interop-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "02-libraries"
chapter_number: 2
pdf_page: null
section: "Interoperability"
extraction_confidence: high
aliases:
  - "interop guidelines"
  - "library interop"
  - "type leaking"
  - "escape hatches"
  - "Send types"
prerequisites:
  - public-type-guidelines
extends: []
related:
  - library-ux-guidelines
  - library-resilience-guidelines
  - library-building-guidelines
  - safety-guidelines
contrasts_with: []
answers_questions:
  - "How should Rust library APIs handle types from external crates?"
  - "When should types be leaked from third-party dependencies in public APIs?"
  - "How do I provide escape hatches for FFI native handles?"
  - "Why should public types be Send in Rust?"
  - "How do I assert that a future or type is Send?"
---

# Quick Definition

Interoperability guidelines for Rust libraries covering three core concerns: avoiding leakage of external crate types in public APIs (M-DONT-LEAK-TYPES), providing unsafe escape hatches for native handle wrappers (M-ESCAPE-HATCHES), and ensuring public types are Send for async runtime compatibility (M-TYPES-SEND).

# Core Definition

The Pragmatic Rust interoperability guidelines address how library APIs interact with the broader Rust ecosystem. M-DONT-LEAK-TYPES states that public APIs should prefer `std` types over external crate types because any type in a public API becomes part of the API contract, and only `std` types carry a permanent stability guarantee. M-ESCAPE-HATCHES requires that types wrapping native handles provide `unsafe` conversion methods (`from_native`, `into_native`, `to_native`) so users can interoperate with FFI or handles obtained elsewhere. M-TYPES-SEND requires that public types, especially futures, be `Send` to ensure compatibility with work-stealing async runtimes like Tokio. (Ch. 2, "Libraries / Interoperability Guidelines")

# Prerequisites

- **public-type-guidelines** -- understanding how public types form API contracts is essential before applying interoperability constraints on those types

# Key Properties

1. **M-DONT-LEAK-TYPES**: Public APIs should prefer `std` types; leaking third-party types makes them part of the API contract and creates interoperability risk
2. If part of an umbrella crate, types from sibling crates may be freely leaked since users interact through the umbrella
3. Third-party types may be leaked behind a feature flag (e.g., `serde`) or without a feature only if they provide substantial ecosystem benefit
4. **M-ESCAPE-HATCHES**: Types wrapping native handles must provide `unsafe fn from_native()` for construction from external handles, plus `into_native()` and `to_native()` for extraction
5. The `from_native` method must document all safety requirements that callers must fulfill
6. **M-TYPES-SEND**: All futures produced by the library (explicitly or implicitly) must be `Send`; most other types should also be `Send`
7. Non-Send types held across `.await` points infect the entire future, making it `!Send` and incompatible with Tokio
8. Types whose default use is instantaneous (not held across `.await` boundaries) may be `!Send`
9. The cost of Send (atomics, uncontended locks) is negligible for occasional operations but measurable in tight loops over large atomic collections

# Construction / Recognition

## To Apply M-DONT-LEAK-TYPES:
1. Audit all public API signatures for types originating from external crates
2. Replace external types with `std` equivalents where feasible
3. For unavoidable external types, place them behind feature flags
4. For umbrella crates, document which sibling crate types may be freely exposed

## To Apply M-ESCAPE-HATCHES:
1. Identify types that wrap native handles (e.g., OS handles, FFI pointers)
2. Provide `unsafe fn from_native(native: HNATIVE) -> Self` with documented safety requirements
3. Provide `fn into_native(self) -> HNATIVE` (consuming) and `fn to_native(&self) -> HNATIVE` (borrowing)

## To Apply M-TYPES-SEND:
1. Use compile-time assertions: `const fn assert_send<T: Send>() {}` and `const _: () = assert_send::<YourType>();`
2. For async methods, assert returned futures are Send at main entry points
3. Avoid `Rc`, `RefCell`, and other `!Send` types in structs that may be held across await points

# Context & Application

These guidelines originate from Microsoft's internal Rust practices and target library authors building crates consumed by a broad ecosystem. The type leaking guideline is particularly important for crates in the `0.x` version range, where each minor version constitutes a separate major version in Cargo's resolution, potentially causing diamond dependency conflicts. The escape hatch guideline is critical for systems programming crates that wrap platform-specific handles. The Send guideline reflects the practical reality that Tokio's multi-threaded runtime is the dominant async executor, making `!Send` types a significant adoption barrier.

# Examples

**Example 1** (Ch. 2, M-DONT-LEAK-TYPES -- Heuristic checklist): The guideline provides a decision checklist: (1) if you can avoid leaking third-party types, do not leak them; (2) umbrella crate siblings may freely leak each other's types; (3) behind a feature flag, types may be leaked; (4) without a feature, only if they give substantial benefit for ecosystem interoperability.

**Example 2** (Ch. 2, M-ESCAPE-HATCHES -- Code): A `Handle` struct wrapping `HNATIVE` provides `fn new() -> Self` for safe creation, `unsafe fn from_native(native: HNATIVE) -> Self` for construction from external handles, `fn into_native(self) -> HNATIVE` for consuming extraction, and `fn to_native(&self) -> HNATIVE` for borrowing extraction.

**Example 3** (Ch. 2, M-TYPES-SEND -- Compile-time assertion): The source shows how to assert a future is Send with `const fn assert_send<T: Send>() {}` followed by `const _: () = assert_send::<Foo>();` for explicit Future impls, and `fn assert_send<T: Send>(_: T) {}` with `_ = assert_send(foo());` for implicit async functions.

**Example 4** (Ch. 2, M-TYPES-SEND -- Rc infection): Demonstrates how holding an `Rc::new(123)` across a `read_file("foo.txt").await` point prevents the entire future from being `Send`, because `Rc` is `!Send`.

# Relationships

## Builds Upon
- **public-type-guidelines** -- interop rules constrain which types appear at API boundaries

## Enables
- Broad ecosystem compatibility through `Send` types and minimal type leaking
- FFI interoperability through escape hatches on native handle wrappers

## Related
- **library-ux-guidelines** -- UX guidelines complement interop guidelines in forming the complete library API surface
- **library-resilience-guidelines** -- resilience guidelines cover robustness aspects of library design
- **library-building-guidelines** -- building guidelines cover compilation and platform concerns
- **safety-guidelines** -- escape hatches use `unsafe`, connecting to the safety guidelines

## Contrasts With
- Libraries that freely expose dependency types in public APIs (common in languages without Cargo's version resolution model)

# Common Errors

- **Error**: Exposing a type from a popular crate (e.g., `bytes::Bytes`) in a public API without a feature gate, then being forced into lockstep version updates with that dependency.
  **Correction**: Use `std` equivalents in the public API, or gate the external type behind a feature flag like `feature = "bytes"`.

- **Error**: Omitting `Send` assertions and discovering `!Send` futures only when users try to use the library with Tokio.
  **Correction**: Add compile-time `Send` assertions for all major public types and future-producing entry points.

- **Error**: Making native handle wrappers opaque with no way to extract or inject the underlying handle.
  **Correction**: Provide `unsafe fn from_native()`, `fn into_native()`, and `fn to_native()` methods with documented safety contracts.

# Common Confusions

- **Confusion**: Thinking `Send` is free and has no performance cost.
  **Clarification**: Send itself has no direct cost, but achieving it often requires using `Arc` instead of `Rc` and `Mutex` instead of `RefCell`. The source notes that uncontended atomics are negligible unless accessed more frequently than every ~64 words in a hot loop.

- **Confusion**: Believing all types must be `Send` with no exceptions.
  **Clarification**: Types whose default use is instantaneous and never held across `.await` boundaries may be `!Send`. The source gives a telemetry example: `telemetry().ping(0)` used ad-hoc between await points.

# Source Reference

Chapter 2: Library Guidelines, "Interoperability" section. Contains three guidelines: M-DONT-LEAK-TYPES (v0.1), M-ESCAPE-HATCHES (v0.1), and M-TYPES-SEND (v1.0). Each includes rationale tags, code examples, and practical heuristics. M-TYPES-SEND includes a performance diagram showing the cost of atomics relative to cache lines.

# Verification Notes

- Definition source: Direct from section headings and `<why>` tags for each guideline
- Key Properties: Derived from the checklist items, code examples, and explanatory text in each guideline
- Confidence rationale: HIGH -- all three guidelines have clear definitions, code examples, and actionable checklists
- Uncertainties: None
- Cross-reference status: public-type-guidelines, library-ux-guidelines, safety-guidelines are from sibling extraction sets
