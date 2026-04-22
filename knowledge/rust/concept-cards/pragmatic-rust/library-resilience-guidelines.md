---
concept: Library Resilience Guidelines
slug: library-resilience-guidelines
category: guidelines
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "02-libraries"
chapter_number: 2
pdf_page: null
section: "Resilience"
extraction_confidence: high
aliases:
  - "resilience guidelines"
  - "library robustness"
  - "mockable syscalls"
  - "test utilities"
  - "strong types"
prerequisites:
  - library-ux-guidelines
extends: []
related:
  - library-interop-guidelines
  - library-building-guidelines
  - safety-guidelines
  - logging-and-observability
contrasts_with: []
answers_questions:
  - "How should Rust libraries handle I/O and system calls for testability?"
  - "How do I make a Rust library mockable for testing?"
  - "Why should I avoid static variables in Rust libraries?"
  - "How should test utilities be gated in a Rust crate?"
  - "Why is glob re-exporting dangerous in Rust?"
  - "When should I use PathBuf vs String in Rust APIs?"
---

# Quick Definition

Resilience guidelines for Rust libraries covering five areas: making I/O and system calls mockable via enum dispatch (M-MOCKABLE-SYSCALLS), feature-gating test utilities (M-TEST-UTIL), using the strongest available std type (M-STRONG-TYPES), avoiding glob re-exports (M-NO-GLOB-REEXPORTS), and avoiding static variables where correctness depends on a consistent view (M-AVOID-STATICS).

# Core Definition

The resilience guidelines ensure libraries are robust, testable, and resistant to subtle correctness issues. M-MOCKABLE-SYSCALLS requires that any user-facing type performing I/O or system calls be mockable to those effects, using an internal enum that dispatches between native and mock implementations. M-TEST-UTIL requires all testing functionality (mocking, sensitive data inspection, safety overrides) to be gated behind a `test-util` feature flag. M-STRONG-TYPES mandates using the strongest available `std` type (e.g., `PathBuf` instead of `String` for OS paths). M-NO-GLOB-REEXPORTS prohibits `pub use foo::*` from other modules to prevent accidentally leaking unintended types. M-AVOID-STATICS warns against static variables where secret duplication across crate versions could cause correctness issues. (Ch. 2, "Libraries / Resilience Guidelines")

# Prerequisites

- **library-ux-guidelines** -- the resilience patterns (especially mocking and DI) build on the UX guidelines' DI hierarchy and service Clone patterns

# Key Properties

1. **M-MOCKABLE-SYSCALLS**: Any operation that is non-deterministic, reliant on external state, hardware-dependent, or not universally reproducible must be mockable
2. Libraries should not perform ad-hoc I/O, create their own I/O core, or offer `Default` constructors for types that do I/O
3. Mocking is implemented via a `pub(crate)` enum dispatching between `Native` and `Mocked(MockCtrl)` variants
4. `new_mocked()` should return `(Self, MockCtrl)` as a tuple, not accept a mock controller, to prevent state ambiguity
5. **M-TEST-UTIL**: A single `test-util` feature flag should gate all testing functionality including mocking, sensitive data inspection, and safety overrides
6. **M-STRONG-TYPES**: Use `PathBuf`/`Path` instead of `String`/`&str` for anything dealing with the OS; use the strongest available type as early as possible in the API flow
7. **M-NO-GLOB-REEXPORTS**: Re-export items individually (`pub use foo::{A, B, C}`) instead of `pub use foo::*`; glob exports are only acceptable for platform-specific HAL modules
8. **M-AVOID-STATICS**: Statics are dangerous because Cargo may link multiple versions of the same crate, each with independently instantiated statics; statics used only for performance optimization (not correctness) are acceptable
9. The secret duplication problem is especially acute during a crate's `0.x` timeline, where each minor version is a separate major version for resolution purposes

# Construction / Recognition

## To Apply M-MOCKABLE-SYSCALLS:
1. Identify all I/O and system call sites in user-facing types
2. Create an internal enum (e.g., `LibraryCore`) with `Native` and `Mocked(MockCtrl)` variants
3. Implement dispatch methods on the enum that forward to OS calls or mock controller
4. Expose `fn new() -> Self` for production and `fn new_mocked() -> (Self, MockCtrl)` for testing
5. Gate mock variants behind `#[cfg(feature = "test-util")]`

## To Apply Other Guidelines:
1. Gate all test utilities behind a single `test-util` feature
2. Replace `String` with `PathBuf` for filesystem paths at API boundaries
3. Replace `pub use foo::*` with explicit `pub use foo::{A, B, C}`
4. Audit statics for correctness dependencies; replace with instance state passed through constructors

# Context & Application

These guidelines address common pitfalls in library design that manifest as subtle, hard-to-diagnose issues. The mockable syscalls pattern is essential for testing edge cases that are difficult to reproduce (network failures, clock skew, entropy exhaustion). The static variable warning addresses a Rust-specific issue where Cargo's version resolution can silently duplicate crate instances, causing "impossible" state inconsistencies. The glob re-export prohibition addresses a real code review problem: `pub use foo::*` makes it impossible to tell from a diff whether new public items are intentionally exported.

# Examples

**Example 1** (Ch. 2, M-MOCKABLE-SYSCALLS -- Enum dispatch): A `LibraryCore` enum with `Native` and `Mocked(mock::MockCtrl)` variants. The `random_u32()` method matches on self: `Native` calls `unsafe { os_random_u32() }`, `Mocked(m)` calls `m.random_u32()`. The `MockCtrl` follows the `Arc<Inner>` pattern with methods like `set_next_u32()`.

**Example 2** (Ch. 2, M-AVOID-STATICS -- Secret duplication): A `GLOBAL_COUNTER` static is used by `library_a` (which depends on `core` v0.4) and `library_b` (which depends on `core` v0.5). After incrementing 2 times via library_a and 3 times via library_b, the counter value could be 0, 2, 3, or 5 depending on version resolution, because Cargo may link separate instances of the static.

**Example 3** (Ch. 2, M-NO-GLOB-REEXPORTS -- Platform exception): Glob re-exports are acceptable for platform-specific HAL: `#[cfg(target_os = "windows")] pub use windows::*;` paired with `#[cfg(target_os = "linux")] pub use linux::*;` where exactly one module is active.

**Example 4** (Ch. 2, M-TEST-UTIL -- Feature gating): `HttpClient` has a public `get()` method always available, and a `bypass_certificate_checks()` method gated behind `#[cfg(feature = "test-util")]`.

# Relationships

## Builds Upon
- **library-ux-guidelines** -- the mocking pattern uses the DI hierarchy and services-Clone patterns from UX guidelines

## Enables
- Comprehensive unit testing of I/O-dependent library code
- Safe, auditable public API surfaces through explicit re-exports
- Correctness across Cargo's version resolution through avoiding statics

## Related
- **library-interop-guidelines** -- interop guidelines address related API surface concerns
- **library-building-guidelines** -- building guidelines complement resilience with compilation and platform concerns
- **safety-guidelines** -- mock controllers interact with unsafe code in native system call paths
- **logging-and-observability** -- observable behavior complements testable/mockable design

## Contrasts With
- Test-only crate designs that don't support mocking (requiring integration tests for all I/O)
- Libraries that rely on global state through statics for configuration or counters

# Common Errors

- **Error**: Creating `Library::new_mocked(ctrl: &mut MockCtrl)` that accepts a shared mock controller, leading to ambiguous state when multiple instances share one controller.
  **Correction**: Return `(Self, MockCtrl)` from `new_mocked()` so each instance has a dedicated controller.

- **Error**: Using `pub use internal_module::*` for convenience, accidentally exporting implementation details.
  **Correction**: Use explicit re-exports: `pub use internal_module::{TypeA, TypeB, TypeC}`.

- **Error**: Using a static `AtomicUsize` counter for tracking state that affects correctness, then experiencing phantom resets when a dependency upgrades to a new minor version.
  **Correction**: Pass state through instance constructors rather than relying on statics.

# Common Confusions

- **Confusion**: Thinking allocations should also be mockable since they are system calls.
  **Clarification**: The source explicitly exempts allocations: "Unless you write kernel code or similar, you can consider allocations to be deterministic, hardware independent and practically infallible." However, memory-hungry code should still provide bounded operations.

- **Confusion**: Believing that `static` is always wrong in Rust libraries.
  **Clarification**: Statics used purely for performance optimization (caching, lazy initialization) are fine. The guideline targets statics where secret duplication would cause correctness issues.

# Source Reference

Chapter 2: Library Guidelines, "Resilience" section. Contains five guidelines: M-MOCKABLE-SYSCALLS (v0.2), M-TEST-UTIL (v0.2), M-STRONG-TYPES (v1.0), M-NO-GLOB-REEXPORTS (v1.0), M-AVOID-STATICS (v1.0). Each includes `<why>` rationale, version tags, and code examples. M-MOCKABLE-SYSCALLS is the longest with a complete enum-dispatch mock pattern. M-AVOID-STATICS includes a detailed version-resolution scenario.

# Verification Notes

- Definition source: Direct from section headings and `<why>` tags for each guideline
- Key Properties: Derived from code examples, checklists, and explanatory scenarios
- Confidence rationale: HIGH -- all five guidelines have clear definitions, rationale, and code examples
- Uncertainties: M-MOCKABLE-SYSCALLS references M-RUNTIME-ABSTRACTED which is not in the extracted chapters
- Cross-reference status: library-ux-guidelines, library-interop-guidelines, safety-guidelines are from sibling extraction sets
