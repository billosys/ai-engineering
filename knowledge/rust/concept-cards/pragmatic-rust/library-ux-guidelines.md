---
concept: Library UX Guidelines
slug: library-ux-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "02-libraries"
chapter_number: 2
pdf_page: null
section: "UX"
extraction_confidence: high
aliases:
  - "library UX"
  - "API ergonomics"
  - "API usability guidelines"
  - "Rust API UX"
prerequisites:
  - public-type-guidelines
  - naming-and-quality-guidelines
extends: []
related:
  - library-interop-guidelines
  - library-resilience-guidelines
  - library-building-guidelines
  - panic-vs-error-guidelines
contrasts_with: []
answers_questions:
  - "How should I design ergonomic Rust library APIs?"
  - "When should I use builders vs direct constructors in Rust?"
  - "Should I expose Arc, Box, and other smart pointers in my public API?"
  - "How should I structure error types in Rust libraries?"
  - "When should I prefer concrete types over generics over dyn Trait?"
  - "How should services implement Clone in Rust?"
  - "When should I use impl AsRef vs concrete types in function signatures?"
---

# Quick Definition

UX guidelines for Rust libraries covering eleven areas: avoiding smart pointer exposure (M-AVOID-WRAPPERS), preferring concrete types over generics over dyn Trait (M-DI-HIERARCHY), structuring errors as canonical structs (M-ERRORS-CANONICAL-STRUCTS), builder patterns for complex construction (M-INIT-BUILDER), cascaded initialization for many parameters (M-INIT-CASCADED), shared-ownership Clone for services (M-SERVICES-CLONE), limiting visible type nesting (M-SIMPLE-ABSTRACTIONS), accepting `impl AsRef` (M-IMPL-ASREF), accepting `impl RangeBounds` (M-IMPL-RANGEBOUNDS), sans-IO via `impl Read/Write` (M-IMPL-IO), and keeping essential functions inherent (M-ESSENTIAL-FN-INHERENT).

# Core Definition

The UX guidelines define how library APIs should present themselves to users for maximum ergonomics. The overarching principle is reducing cognitive load: abstractions should not visibly nest (M-SIMPLE-ABSTRACTIONS), smart pointers should stay hidden (M-AVOID-WRAPPERS), and essential functionality should be inherent rather than requiring trait imports (M-ESSENTIAL-FN-INHERENT). For dependency injection, a design escalation ladder prefers concrete types, then generics, then dyn Trait (M-DI-HIERARCHY). Error types should be situation-specific structs with Backtrace and helper methods, not global enum catchalls (M-ERRORS-CANONICAL-STRUCTS). Construction complexity is managed via builders for 3+ optional parameters (M-INIT-BUILDER) and cascaded helper types for 4+ required parameters (M-INIT-CASCADED). Services should implement cheap Clone via Arc<Inner> (M-SERVICES-CLONE). Function signatures should accept `impl AsRef<T>`, `impl RangeBounds<T>`, and `impl Read/Write` for flexibility (M-IMPL-ASREF, M-IMPL-RANGEBOUNDS, M-IMPL-IO). (Ch. 2, "Libraries / UX Guidelines")

# Prerequisites

- **public-type-guidelines** -- understanding public API surface design is essential before applying UX constraints
- **naming-and-quality-guidelines** -- naming conventions feed into the discoverability aspects of these UX guidelines

# Key Properties

1. **M-SIMPLE-ABSTRACTIONS**: Service-like types should not nest type parameters on their own volition; if they do, only 1 level deep (e.g., `Service<Backend>` is acceptable, `Service<Backend<Store>>` is bad)
2. **M-AVOID-WRAPPERS**: `Rc<T>`, `Arc<T>`, `Box<T>`, `RefCell<T>` should not appear in public APIs; hide them behind clean interfaces using `&T`, `&mut T`, or `T`
3. **M-DI-HIERARCHY**: Design escalation ladder: (1) concrete types, (2) enum with mock variant for testing, (3) narrow traits with generic parameters, (4) dyn Trait only when generics cause excessive nesting
4. **M-ERRORS-CANONICAL-STRUCTS**: Errors should be situation-specific structs containing a `Backtrace`, upstream cause, and `is_xxx()` helper methods; inner `ErrorKind` enums should be `pub(crate)` not public
5. **M-INIT-BUILDER**: Types with 3+ optional initialization parameters should provide builders; the builder must be named `FooBuilder`, use chainable methods, and terminate with `.build()`; required parameters go in `Foo::builder(deps)`, not setter methods
6. **M-INIT-CASCADED**: Types requiring 4+ parameters should cascade initialization through semantically grouped helper types (e.g., `Account` and `Currency` instead of four loose parameters)
7. **M-SERVICES-CLONE**: Heavyweight service types should implement shared-ownership Clone via the `Arc<Inner>` pattern, making cloning cheap handle duplication rather than deep copies
8. **M-IMPL-ASREF**: Function signatures should accept `impl AsRef<str>`, `impl AsRef<Path>`, `impl AsRef<[u8]>` instead of concrete `&str`/`String`, `&Path`/`PathBuf`, `&[u8]`/`Vec<u8>`; however, structs should not be generic over `AsRef` bounds
9. **M-IMPL-IO**: Functions performing one-shot I/O should be written "sans-io", accepting `impl std::io::Read` or `impl std::io::Write` rather than concrete `File` types
10. **M-IMPL-RANGEBOUNDS**: Functions accepting ranges should use `impl RangeBounds<T>` rather than hand-rolled `(low, high)` tuples
11. **M-ESSENTIAL-FN-INHERENT**: Core functionality should be implemented as inherent methods; trait impls should forward to inherent methods, not replace them

# Construction / Recognition

## To Apply These Guidelines:
1. Audit public API for exposed smart pointers and nested generics -- hide or flatten them
2. For dependency injection, start with concrete types; escalate to enums, then generics, then dyn Trait only as needed
3. Design error types as structs with `Backtrace::capture()` in constructors and `is_xxx()` helper methods
4. Use builders for types with 3+ optional construction parameters; group required params into deps structs
5. Implement `Clone` for services using the `Arc<Inner>` pattern
6. Replace concrete types in function signatures with `impl AsRef<T>`, `impl RangeBounds<T>`, or `impl Read/Write` where appropriate
7. Ensure essential type methods are inherent, with trait impls forwarding to them

## To Recognize Violations:
1. Public APIs requiring `Arc<Mutex<T>>` or `Rc<RefCell<T>>` in signatures
2. Global error enums used across unrelated operations
3. Constructor functions with 4+ loose parameters
4. Essential methods only accessible after importing an external trait

# Context & Application

These guidelines emerge from practical experience building large-scale Rust services. The DI hierarchy guideline explicitly addresses the common anti-pattern of translating C# interface-heavy designs directly to Rust, which produces non-idiomatic, object-safety-constrained code. The error struct guideline addresses the tension between convenience (one error type per crate) and precision (one per failure domain). The builder and cascaded initialization guidelines provide concrete thresholds (3+ optional params for builders, 4+ total params for cascading) rather than vague advice. The services-Clone pattern reflects the reality that heavyweight services are shared across threads and handlers, and deep cloning would be prohibitively expensive.

# Examples

**Example 1** (Ch. 2, M-AVOID-WRAPPERS -- Good vs Bad API): Good: `pub fn process_data(data: &Data) -> State` and `pub fn store_config(config: Config) -> Result<(), Error>`. Bad: `pub fn process_shared(data: Arc<Mutex<Shared>>) -> Box<Processed>` and `pub fn initialize(config: Rc<RefCell<Config>>) -> Arc<Server>`.

**Example 2** (Ch. 2, M-DI-HIERARCHY -- Escalation): The source shows the escalation from a naive `trait Database` with `dyn` dispatch to: (1) an enum `DataAccess { MyDatabase(...), Mock(...), Dynamic(...) }` combining real, mock, and dynamic variants; (2) narrow traits like `StoreObject` and `LoadObject` used as generic bounds; (3) a `DynamicDataAccess(Arc<dyn DataAccess>)` wrapper only when generics cause nesting problems.

**Example 3** (Ch. 2, M-ERRORS-CANONICAL-STRUCTS -- Error struct): An `HttpError` struct containing a `pub(crate) ErrorKind` enum and a `Backtrace`, with public `is_io()` and `is_protocol()` helper methods. The inner enum variants are hidden from callers, preventing coupling to internal failure modes.

**Example 4** (Ch. 2, M-SERVICES-CLONE -- Arc<Inner> pattern): `ServiceCommon` wraps `Arc<ServiceCommonInner>`, derives `Clone`, and forwards method calls to `self.inner.foo()`. Users can pass `&ServiceCommon` to multiple handlers; each clones only the Arc handle.

# Relationships

## Builds Upon
- **public-type-guidelines** -- these UX guidelines refine how public types are designed and presented
- **naming-and-quality-guidelines** -- naming conventions support discoverability of builders, error types, and inherent methods

## Enables
- Ergonomic, low-cognitive-load library APIs
- Testable designs through the DI hierarchy and mockable patterns
- Future-proof APIs through builders and cascaded construction

## Related
- **library-interop-guidelines** -- interop guidelines complement UX guidelines for complete API design
- **library-resilience-guidelines** -- resilience guidelines (mockability, test utilities) connect to the DI hierarchy
- **panic-vs-error-guidelines** -- error handling strategy complements the error struct design in M-ERRORS-CANONICAL-STRUCTS

## Contrasts With
- Interface-heavy dependency injection patterns from C#/Java (explicitly contrasted in M-DI-HIERARCHY)
- Global error enums covering all failure modes (contrasted in M-ERRORS-CANONICAL-STRUCTS)

# Common Errors

- **Error**: Creating a single `Error` enum with variants for every possible failure across the entire crate.
  **Correction**: Use situation-specific error structs (e.g., `DownloadError`, `VmError`) with private `ErrorKind` enums and public `is_xxx()` helpers.

- **Error**: Translating a C# `IDatabase` interface directly into a Rust `trait Database` used via `Rc<dyn Database>`.
  **Correction**: Follow the DI escalation ladder: start with a concrete type or enum, use narrow generic traits if needed, and only resort to dyn Trait when generics cause excessive nesting.

- **Error**: Placing core methods only in trait implementations, requiring users to figure out which trait to `use`.
  **Correction**: Implement essential functionality as inherent methods; have trait impls forward to them via `Self::method(self, args)`.

# Common Confusions

- **Confusion**: Thinking `impl AsRef<str>` should be used everywhere, including struct field bounds.
  **Clarification**: The source explicitly states that `impl AsRef<T>` is for function signatures only; structs should store concrete types like `String`, not be generic over `T: AsRef<str>`.

- **Confusion**: Assuming builders are always needed for any type with optional configuration.
  **Clarification**: Types with up to 2 optional parameters can use inherent methods (`new()`, `with_a()`, `with_b()`, `with_a_b()`). Builders are recommended starting at 3+ optional parameters (4+ permutations).

- **Confusion**: Thinking `Clone` on a service type means deep copying all internal state.
  **Clarification**: Service Clone should follow the `Arc<Inner>` pattern, where cloning duplicates only the Arc handle, not the inner data. This is explicitly a shared-ownership pattern.

# Source Reference

Chapter 2: Library Guidelines, "UX" section. Contains eleven guidelines: M-SIMPLE-ABSTRACTIONS (v0.1), M-AVOID-WRAPPERS (v1.0), M-DI-HIERARCHY (v0.1), M-ERRORS-CANONICAL-STRUCTS (v1.0), M-INIT-BUILDER (v0.3), M-INIT-CASCADED (v1.0), M-SERVICES-CLONE (v1.0), M-IMPL-ASREF (v1.0), M-IMPL-RANGEBOUNDS (v1.0), M-IMPL-IO (v0.1), M-ESSENTIAL-FN-INHERENT (v1.0). Each includes `<why>` rationale, version tags, and code examples showing good vs bad patterns.

# Verification Notes

- Definition source: Direct from section headings, `<why>` tags, and explanatory text for each guideline
- Key Properties: Derived from code examples, checklists, and threshold values stated in the guidelines
- Confidence rationale: HIGH -- all eleven guidelines have clear definitions, code examples, and concrete thresholds
- Uncertainties: The DI hierarchy references M-MOCKABLE-SYSCALLS and M-RUNTIME-ABSTRACTED from the resilience section
- Cross-reference status: library-interop-guidelines, library-resilience-guidelines, panic-vs-error-guidelines are from sibling extraction sets
