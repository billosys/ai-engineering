---
concept: Application and FFI Guidelines
slug: application-guidelines
category: guidelines
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "03-applications"
chapter_number: 3
pdf_page: null
section: "M-APP-ERROR, M-MIMALLOC-APPS, M-ISOLATE-DLL-STATE"
extraction_confidence: high
aliases:
  - "anyhow for apps"
  - "eyre for apps"
  - "mimalloc allocator"
  - "rust FFI DLL state"
  - "application error handling rust"
prerequisites:
  - pragmatic-rust-overview
  - panic-vs-error-guidelines
extends: []
related:
  - naming-and-quality-guidelines
  - public-type-guidelines
  - logging-and-observability
contrasts_with: []
answers_questions:
  - "Should Rust applications use anyhow or eyre for errors?"
  - "Why should Rust apps use mimalloc?"
  - "What is the difference between library and application error handling?"
  - "How do I safely share state between Rust DLLs?"
  - "What types are portable across FFI boundaries?"
  - "Why can't I share String or Vec between Rust DLLs?"
---

# Quick Definition

Three guidelines cover application-specific and FFI concerns: M-APP-ERROR (v0.1) permits applications to use anyhow, eyre, or similar crates for error handling instead of defining custom error types; M-MIMALLOC-APPS (v0.1) recommends setting mimalloc as the global allocator for applications to gain free performance improvements; and M-ISOLATE-DLL-STATE (v0.1) requires that only "portable" data be shared between Rust-based dynamic libraries to prevent data corruption and undefined behavior.

# Core Definition

**M-APP-ERROR** (v0.1): "Applications, and crates in your own repository exclusively used from your application, may use anyhow, eyre or similar application-level error crates instead of implementing their own types." This is a relaxation of M-ERRORS-CANONICAL-STRUCTS (a library guideline). Once an application error crate is selected, all application-level errors should use that type consistently. Libraries (crates used by more than one crate) must still follow M-ERRORS-CANONICAL-STRUCTS. (Ch. 3, Applications)

**M-MIMALLOC-APPS** (v0.1): "Applications should set mimalloc as their global allocator. This usually results in notable performance increases along allocating hot paths; we have seen up to 25% benchmark improvements." Implementation requires only adding the dependency and two lines in `main.rs`. (Ch. 3, Applications)

**M-ISOLATE-DLL-STATE** (v0.1): "When loading multiple Rust-based dynamic libraries (DLLs) within one application, you may only share 'portable' state between these libraries." Portable means `#[repr(C)]` (or similarly well-defined) with no interaction with any `static`/thread-local, no interaction with any `TypeId`, and no pointers or references to non-portable data. The Rust compiler treats each DLL as a separate compilation artifact with its own statics, type layouts for `#[repr(Rust)]` types, and unique type IDs. (Ch. 4, FFI)

# Prerequisites

- **pragmatic-rust-overview** -- understanding the guideline framework and applicability levels
- **panic-vs-error-guidelines** -- M-APP-ERROR builds on the panic/error distinction to define how applications handle recoverable errors

# Key Properties

1. **Application error simplification**: Applications may use anyhow/eyre instead of custom error types; libraries must not
2. **Error type consistency**: Once an application-level error crate is chosen, do not mix multiple application-level error types
3. **Library vs. application distinction**: Libraries (used by more than one crate) must define canonical error structs; application-only crates get the anyhow/eyre relaxation
4. **Mimalloc as global allocator**: Two lines of code (`#[global_allocator] static GLOBAL: MiMalloc = MiMalloc;`) yield up to 25% benchmark improvements on allocating hot paths
5. **DLL state isolation**: Each Rust DLL has its own statics, thread-locals, `#[repr(Rust)]` type layouts, and TypeIds
6. **Portable type requirements**: `#[repr(C)]`, no static/thread-local interaction, no TypeId interaction, no pointers to non-portable data
7. **Non-portable types across DLLs**: `String`, `Vec<u8>`, `Box<Foo>`, any `#[repr(Rust)]` struct, anything depending on statics (e.g., tokio, log), anything relying on consistent TypeId
8. **Invisible FFI hazards**: Even types and methods not directly at the FFI boundary can cause undefined behavior if they involve non-portable data internally

# Construction / Recognition

## Setting Up Application Error Handling:
1. Choose one application-level error crate (anyhow or eyre)
2. Re-export its `Result` type: `use eyre::Result;`
3. Use `?` operator throughout application code to propagate errors
4. Do not define custom error types in application crates unless there is a specific reason
5. Ensure library crates still follow M-ERRORS-CANONICAL-STRUCTS

## Setting Up Mimalloc:
1. Add to `Cargo.toml`: `mimalloc = { version = "0.1" }`
2. Add to `main.rs`: `use mimalloc::MiMalloc;` and `#[global_allocator] static GLOBAL: MiMalloc = MiMalloc;`

## Checking FFI Portability:
1. Is the type `#[repr(C)]` or similarly well-defined? If not, it is not portable
2. Does the type or its usage interact with any `static` or thread-local? If yes, not portable
3. Does the type or its usage interact with `TypeId`? If yes, not portable
4. Does the type contain pointers or references to non-portable data? If yes, not portable
5. Consider methods called on the type: code from DLL1 calling a method on data from DLL2 will use DLL1's statics, not DLL2's

# Context & Application

These three guidelines address the practical concerns of building and deploying Rust applications, as opposed to libraries. Application error handling differs fundamentally from library error handling because applications are the terminal consumer of errors -- they log, display, or retry rather than propagate structured errors to further callers. Mimalloc is a simple drop-in performance win. FFI state isolation is critical for plugin architectures and multi-DLL applications.

**Typical contexts:**
- Application `main.rs` setup: error handling and allocator configuration
- Plugin architectures loading multiple Rust DLLs in one process
- FFI boundary design between Rust components compiled separately
- Deciding whether a crate is "application-only" or a reusable library

# Examples

**Example 1** (Ch. 3, M-APP-ERROR): An application entry point using eyre:
```rust
use eyre::Result;
fn start_application() -> Result<()> {
    start_server()?;
    Ok(())
}
```
All third-party library errors are automatically handled via eyre's `Result`, especially those following M-ERRORS-CANONICAL-STRUCTS.

**Example 2** (Ch. 3, M-MIMALLOC-APPS): Setting the global allocator:
```rust
use mimalloc::MiMalloc;
#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;
```

**Example 3** (Ch. 4, M-ISOLATE-DLL-STATE): A method in DLL1 receives `&CommonService` from DLL2. Even though `CommonService` looks like a normal reference, calling `common.do_work()` executes DLL1's code with DLL2's data structure, using DLL1's statics -- leading to undefined behavior if the type layout differs or statics are involved.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- these are application and FFI guidelines within the Pragmatic Rust framework
- **panic-vs-error-guidelines** -- the panic/error boundary determines when to use Result (and thus anyhow/eyre) vs. panic
- library-ux-guidelines (covered by another extraction agent) -- M-ERRORS-CANONICAL-STRUCTS is the library counterpart to M-APP-ERROR

## Enables
- Clean application entry points with minimal error boilerplate
- Free performance improvements from allocator selection
- Safe multi-DLL plugin architectures

## Related
- **naming-and-quality-guidelines** -- M-STATIC-VERIFICATION helps catch FFI safety issues (miri)
- **public-type-guidelines** -- M-SMALLER-CRATES relates to the library/application boundary decisions
- **logging-and-observability** -- application error handling works alongside structured logging for observability
- safety-guidelines (covered by another extraction agent) -- M-UNSAFE and M-UNSAFE-IMPLIES-UB are especially relevant to FFI code
- performance-guidelines (covered by another extraction agent) -- M-MIMALLOC-APPS connects to throughput optimization

## Contrasts With
- Library error handling with canonical error structs (which remains required for libraries)
- Default system allocator (which mimalloc replaces for application performance)
- Naive FFI designs that pass `String`, `Vec`, or `Box` between DLLs

# Common Errors

- **Error**: Using anyhow/eyre in a library crate that is consumed by multiple applications.
  **Correction**: Libraries must follow M-ERRORS-CANONICAL-STRUCTS with proper error types. Only application crates and crates exclusively used by one application may use anyhow/eyre.

- **Error**: Mixing multiple application-level error types (e.g., using both anyhow and eyre in the same application).
  **Correction**: Choose one and use it consistently across all application crates.

- **Error**: Passing `String`, `Vec<u8>`, or `Box<T>` across FFI boundaries between Rust DLLs.
  **Correction**: These types are not portable. Each DLL has its own allocator, type layouts, and statics. Use `#[repr(C)]` types with no static/TypeId interactions.

# Common Confusions

- **Confusion**: Thinking M-APP-ERROR means applications should never define their own error types.
  **Clarification**: M-APP-ERROR is a relaxation -- applications may use anyhow/eyre. If a specific application benefits from custom error types, that remains an option.

- **Confusion**: Thinking the FFI DLL isolation issue only affects types visible at the FFI boundary.
  **Clarification**: The source explicitly warns about "types and methods that are invisible at the FFI boundary." A method from DLL1 called on data from DLL2 will use DLL1's code and statics, not DLL2's, even for deeply nested types.

# Source Reference

Chapter 3: Application Guidelines, sections M-APP-ERROR (v0.1, "To simplify application-level error handling") and M-MIMALLOC-APPS (v0.1, "To get significant performance for free"). Chapter 4: FFI Guidelines, section M-ISOLATE-DLL-STATE (v0.1, "To prevent data corruption and undefined behavior"). All include code examples and detailed rationale.

# Verification Notes

- Definition: Direct quotations from each guideline section
- Key Properties: Synthesized from the portability definition, affected type list, and code examples
- Confidence: HIGH -- all three guidelines are explicit with code examples, though all are v0.1 (newer/may evolve)
- Uncertainties: M-MIMALLOC-APPS performance claims are based on the authors' benchmarks; results may vary by workload
- Cross-reference status: All slugs are within this extraction set or reference Agent B's planned cards
