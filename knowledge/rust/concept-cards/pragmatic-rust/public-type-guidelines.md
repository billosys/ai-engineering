---
concept: Public Type and API Design Guidelines
slug: public-type-guidelines
category: api-design
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "01-universal"
chapter_number: 1
pdf_page: null
section: "M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY, M-REGULAR-FN, M-SMALLER-CRATES"
extraction_confidence: high
aliases:
  - "debug display requirements"
  - "public types debug"
  - "regular functions rust"
  - "crate splitting"
  - "smaller crates"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - naming-and-quality-guidelines
  - panic-vs-error-guidelines
contrasts_with: []
answers_questions:
  - "Should all public types implement Debug in Rust?"
  - "When should a public type implement Display?"
  - "When should I use associated functions vs regular functions?"
  - "When should I split a Rust crate into smaller crates?"
  - "How do I handle sensitive data in Debug implementations?"
  - "What is the difference between features and crates?"
---

# Quick Definition

Four universal guidelines govern public API design: M-PUBLIC-DEBUG (v1.0) requires all public types to implement `Debug` (with custom implementations for sensitive data); M-PUBLIC-DISPLAY (v1.0) requires `Display` for types meant to be read by consumers; M-REGULAR-FN (v1.0) mandates that functionality not tied to a receiver be regular functions rather than associated functions; and M-SMALLER-CRATES (v1.0) encourages splitting crates aggressively to improve compile times and modularity.

# Core Definition

**M-PUBLIC-DEBUG** (v1.0): "All public types exposed by a crate should implement Debug." Most types use `#[derive(Debug)]`. Types holding sensitive data must implement `Debug` manually with a custom implementation that redacts secrets, and this behavior must be verified with unit tests. (Ch. 1, Universal)

**M-PUBLIC-DISPLAY** (v1.0): "If your type is expected to be read by upstream consumers, be it developers or end users, it should implement Display." This particularly includes error types (mandated by `std::error::Error`) and wrappers around string-like data. Display implementations should follow Rust customs for newlines and escape sequences, and the sensitive-data handling from M-PUBLIC-DEBUG applies analogously. (Ch. 1, Universal)

**M-REGULAR-FN** (v1.0): "Associated functions should primarily be used for instance creation, not general purpose computation." Regular (free) functions are first-class citizens in Rust and need no module or class to host them. Functionality that does not clearly belong to a receiver should not reside in a type's `impl` block. Associated trait functions remain idiomatic. (Ch. 1, Universal)

**M-SMALLER-CRATES** (v1.0): "You should err on the side of having too many crates rather than too few, as this leads to dramatic compile time improvements and prevents cyclic component dependencies." If a submodule can be used independently, it should be a separate crate. Losing `pub(crate)` access is often a desirable side-effect that prompts better abstraction design. (Ch. 1, Universal)

# Prerequisites

- **pragmatic-rust-overview** -- understanding the universal guideline applicability and maturity framework

# Key Properties

1. **Debug for all public types**: Use `#[derive(Debug)]` by default; implement manually only for sensitive data types
2. **Sensitive data in Debug**: Custom `Debug` implementations must redact secrets; unit tests must verify that sensitive values do not appear in the rendered output
3. **Display for readable types**: Error types must implement `Display` (required by `std::error::Error`); string-like wrappers should implement `Display`
4. **Regular functions over associated functions**: If a function does not take `self`/`&self`/`&mut self` and does not create an instance, it should be a free function
5. **Associated trait functions are fine**: `Default::default()`, `FromStr::from_str()`, etc. are idiomatic as associated functions
6. **Aggressive crate splitting**: Prefer too many crates over too few; compile times improve dramatically
7. **Features vs. crates**: Crates are for items that can reasonably be used independently; features unlock extra functionality that cannot stand alone
8. **Re-exports for technical splits**: Proc macro crates split for technical reasons should always be re-exported; otherwise, re-exports should be used sparingly

# Construction / Recognition

## Implementing Debug and Display:
1. Add `#[derive(Debug)]` to all public types by default
2. For types containing sensitive data, implement `Debug` manually: `write!(f, "TypeName(...)")`
3. Add unit tests verifying that sensitive values do not appear in `format!("{:?}", instance)`
4. Implement `Display` for error types and types meant to be read by users
5. Follow Rust customs for newlines and escape sequences in `Display`

## Deciding Regular vs. Associated Function:
1. Does the function create an instance of the type? -> Associated function (e.g., `new()`)
2. Does the function take `&self` or `&mut self`? -> Method (associated function with receiver)
3. Does the function have no relationship to a specific type's instances? -> Regular (free) function

## Deciding When to Split Crates:
1. Can a submodule be used independently? -> Split it into its own crate
2. Would splitting force redesigning `pub(crate)` access? -> That is often a positive signal, not a reason to avoid splitting
3. Is the split purely technical (e.g., proc macros)? -> Split but re-export from the umbrella crate

# Context & Application

These four guidelines collectively shape how a crate presents itself to consumers. Debug and Display affect developer experience during debugging and error reporting. Regular functions affect API ergonomics and discoverability. Crate splitting affects compile times, dependency management, and architectural modularity.

**Typical contexts:**
- Library design: ensuring all public types are debuggable and that error types are displayable
- API review: checking that associated functions are justified (instance creation or trait implementation)
- Monorepo architecture: deciding where to draw crate boundaries for compile-time optimization
- Security review: verifying that sensitive data does not leak through Debug or Display

# Examples

**Example 1** (Ch. 1, M-PUBLIC-DEBUG): A `UserSecret(String)` type implements `Debug` manually: `write!(f, "UserSecret(...)")`. A test asserts that `format!("{:?}", secret)` contains "UserSecret" but does not contain the actual secret key.

**Example 2** (Ch. 1, M-REGULAR-FN): A `Database` type has `fn new() -> Self` (ok, creates instance), `fn query(&self)` (ok, takes receiver), but `fn check_parameters(p: &str)` does not belong in `impl Database` -- it should be a regular function `fn check_parameters(p: &str)`.

**Example 3** (Ch. 1, M-SMALLER-CRATES): A `web` crate with `web::server`, `web::client`, and `web::protocols` modules should be split into `web_server`, `web_client`, and `web_protocols` so users needing only the client do not pay for server compilation.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- these are universal guidelines from the Pragmatic Rust framework

## Enables
- library-ux-guidelines (covered by another extraction agent) -- public API quality builds on Debug/Display and function design
- library-interop-guidelines (covered by another extraction agent) -- crate splitting and clean APIs enable better interoperability

## Related
- **naming-and-quality-guidelines** -- M-CONCISE-NAMES and M-STATIC-VERIFICATION complement these API design guidelines
- **panic-vs-error-guidelines** -- error types must implement Display, connecting to M-PUBLIC-DISPLAY
- documentation-guidelines (covered by another extraction agent) -- well-documented public types build on Debug/Display implementations

## Contrasts With
- OOP-style designs where all functions are methods on classes
- Monolithic crates that bundle unrelated functionality for convenience

# Common Errors

- **Error**: Deriving `Debug` on types containing API keys, passwords, or tokens.
  **Correction**: Implement `Debug` manually with redaction. Add unit tests to verify secrets do not appear in the debug output.

- **Error**: Placing utility functions as associated functions on a type because "they're related."
  **Correction**: If the function does not create an instance or operate on a receiver, make it a regular (free) function. Associated functions add noise on the caller side (`Type::utility()` vs. `utility()`).

- **Error**: Keeping a large crate monolithic because splitting would require redesigning `pub(crate)` boundaries.
  **Correction**: Losing `pub(crate)` access is often a positive signal that prompts better abstractions. Split and design a proper public API for the extracted crate.

# Common Confusions

- **Confusion**: Thinking Debug output is only used by developers during debugging.
  **Clarification**: Debug output may appear in logs, error messages, and crash reports in production. Sensitive data in Debug implementations is a security concern, not just a convenience issue.

- **Confusion**: Thinking associated trait functions violate M-REGULAR-FN.
  **Clarification**: Associated trait functions (e.g., `Default::default()`, `FromStr::from_str()`) are explicitly noted as perfectly idiomatic. The guideline targets non-trait associated functions that have no receiver and do not create instances.

# Source Reference

Chapter 1: Universal Guidelines, sections M-PUBLIC-DEBUG (v1.0, "To simplify debugging and prevent leaking sensitive data"), M-PUBLIC-DISPLAY (v1.0, "To improve usability"), M-REGULAR-FN (v1.0, "To improve readability"), and M-SMALLER-CRATES (v1.0, "To improve compile times and modularity"). Each includes code examples and rationale.

# Verification Notes

- Definition: Direct quotations from each guideline section
- Key Properties: Synthesized from code examples and discussion in each section
- Confidence: HIGH -- all four guidelines are v1.0 with explicit code examples and clear rationale
- Uncertainties: None
- Cross-reference status: All slugs are within this extraction set or reference Agent B's planned cards
