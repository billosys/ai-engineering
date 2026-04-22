---
concept: Naming and Code Quality Guidelines
slug: naming-and-quality-guidelines
category: guidelines
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "01-universal"
chapter_number: 1
pdf_page: null
section: "M-CONCISE-NAMES, M-DOCUMENTED-MAGIC, M-LINT-OVERRIDE-EXPECT, M-STATIC-VERIFICATION, M-UPSTREAM-GUIDELINES"
extraction_confidence: high
aliases:
  - "rust naming guidelines"
  - "static verification rust"
  - "weasel words"
  - "magic values"
  - "lint expect"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - public-type-guidelines
  - logging-and-observability
contrasts_with: []
answers_questions:
  - "What naming conventions does Pragmatic Rust recommend?"
  - "What are weasel words in type names?"
  - "How should magic values be documented in Rust?"
  - "Should I use #[allow] or #[expect] for lint overrides?"
  - "What static verification tools should Rust projects use?"
  - "What upstream Rust guidelines should I follow?"
---

# Quick Definition

Five universal guidelines collectively address code quality, naming clarity, and verification: M-UPSTREAM-GUIDELINES (v1.0) requires following the Rust API Guidelines and related community resources; M-STATIC-VERIFICATION (v1.0) prescribes specific compiler lints, Clippy categories, rustfmt, cargo-audit, cargo-hack, cargo-udeps, and miri; M-LINT-OVERRIDE-EXPECT (v1.0) mandates `#[expect]` over `#[allow]` for lint overrides; M-CONCISE-NAMES (v1.0) prohibits weasel words like Service, Manager, and Factory in type names; and M-DOCUMENTED-MAGIC (v1.0) requires that all hardcoded magic values include comments explaining their rationale.

# Core Definition

**M-UPSTREAM-GUIDELINES** (v1.0): The Pragmatic Rust guidelines complement existing resources. Teams must also follow the Rust API Guidelines, Rust Style Guide, Rust Design Patterns, and the Rust Reference on Undefined Behavior. Special attention is called to frequently forgotten items: C-CONV (ad-hoc conversion naming), C-GETTER (getter naming), C-COMMON-TRAITS (eagerly implementing common traits), C-CTOR (constructors as static inherent methods), and C-FEATURE (feature names free of placeholder words). (Ch. 1, Universal)

**M-STATIC-VERIFICATION** (v1.0): Projects should use compiler lints, Clippy lints, rustfmt, cargo-audit, cargo-hack, cargo-udeps, and miri. The guideline specifies exact `[lints.rust]` and `[lints.clippy]` configurations, enabling all major Clippy categories (cargo, complexity, correctness, pedantic, perf, style, suspicious) plus specific restriction lints. (Ch. 1, Universal)

**M-LINT-OVERRIDE-EXPECT** (v1.0): When overriding project-global lints, use `#[expect]` instead of `#[allow]`. Expected lints emit a warning if the marked warning was not encountered, preventing stale lint suppressions from accumulating. Overrides should include a `reason`. (Ch. 1, Universal)

**M-CONCISE-NAMES** (v1.0): "Symbol names, especially types and traits names, should be free of weasel words that do not meaningfully add information. Common offenders include Service, Manager, and Factory." A `BookingService` type should be `Bookings` or `BookingDispatcher`; `Factory` should be `Builder`; accepting factories as parameters should use `impl Fn() -> Foo` instead. (Ch. 1, Universal)

**M-DOCUMENTED-MAGIC** (v1.0): "Hardcoded magic values in production code must be accompanied by a comment" explaining why the value was chosen, non-obvious side effects if changed, and external systems that interact with the constant. Named constants are preferred over inline values. (Ch. 1, Universal)

# Prerequisites

- **pragmatic-rust-overview** -- understanding the guideline framework and how these universal items apply across all project types

# Key Properties

1. **Upstream compliance**: Following Rust API Guidelines is not optional; Pragmatic Rust builds on top, not instead of, community standards
2. **Seven static verification tools**: compiler lints, Clippy, rustfmt, cargo-audit, cargo-hack, cargo-udeps, and miri -- configured for CI/CD gates
3. **Lint override hygiene**: `#[expect]` over `#[allow]` prevents dead lint suppressions; `#[allow]` remains valid for generated code and macros
4. **Weasel word avoidance**: Service, Manager, Factory are almost always meaningless in Rust type names; use descriptive names that convey what the type actually does
5. **Magic value documentation**: Comments must explain why (not just what), side effects, and external dependencies; named constants are preferred over inline literals
6. **Specific Clippy restriction lints**: The guideline enumerates 20+ restriction-group lints to enable, including `undocumented_unsafe_blocks`, `map_err_ignore`, `string_to_string`, and `clone_on_ref_ptr`

# Construction / Recognition

## Applying These Guidelines to a Project:
1. Add `[lints.rust]` and `[lints.clippy]` sections to `Cargo.toml` using the configurations from M-STATIC-VERIFICATION
2. Set up CI to run rustfmt, Clippy, cargo-audit, cargo-hack, and cargo-udeps
3. Search for `#[allow(...)]` in the codebase and convert to `#[expect(..., reason = "...")]`
4. Audit type names for Service/Manager/Factory and rename to convey actual purpose
5. Search for hardcoded numeric literals and string constants; add documentation or extract to named constants
6. Review the Rust API Guidelines checklist, paying special attention to C-CONV, C-GETTER, C-COMMON-TRAITS, C-CTOR, and C-FEATURE

## Recommended Compiler Lints (from M-STATIC-VERIFICATION):
- `ambiguous_negative_literals`, `missing_debug_implementations`, `redundant_imports`, `redundant_lifetimes`, `trivial_numeric_casts`, `unsafe_op_in_unsafe_fn`, `unused_lifetimes` -- all set to "warn"

# Context & Application

These five guidelines form the foundation of day-to-day code quality. They cover what happens before you write code (tool configuration), as you write code (naming, documenting magic values), and after you write code (lint verification). Together they ensure a codebase is consistent, readable, and maintained.

**Typical contexts:**
- Setting up a new Rust project's CI pipeline
- Code review: checking for meaningless type names, undocumented magic values, stale `#[allow]` attributes
- Onboarding: pointing new developers to the upstream guidelines they must also follow
- Refactoring: converting inline magic values to documented named constants

# Examples

**Example 1** (Ch. 1, M-CONCISE-NAMES): Instead of `BookingService`, use `Bookings` (if it manages bookings) or `BookingDispatcher` (if it dispatches them). Instead of `FooFactory`, use `FooBuilder` or accept `impl Fn() -> Foo`.

**Example 2** (Ch. 1, M-DOCUMENTED-MAGIC): Bad: `wait_timeout(60 * 60 * 24).await // Wait at most a day`. Better: include rationale about why a day is the right value. Best: extract to `const UPSTREAM_SERVER_TIMEOUT: Duration = Duration::from_secs(60 * 60 * 24);` with a doc comment explaining the choice, side effects, and related external systems.

**Example 3** (Ch. 1, M-LINT-OVERRIDE-EXPECT): Use `#[expect(clippy::unused_async, reason = "API fixed, will use I/O later")]` instead of `#[allow(clippy::unused_async)]`. The `#[expect]` version will warn when the lint override becomes stale.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- these are universal guidelines that apply to all project types
- Rust API Guidelines (M-UPSTREAM-GUIDELINES explicitly requires following them)

## Enables
- **public-type-guidelines** -- quality naming and linting support clear public API design
- **logging-and-observability** -- structured logging benefits from the same discipline of clarity and documentation

## Related
- documentation-guidelines (covered by another extraction agent) -- M-DOCUMENTED-MAGIC overlaps with documentation practices
- safety-guidelines (covered by another extraction agent) -- M-STATIC-VERIFICATION includes miri for unsafe code validation

## Contrasts With
- Minimal lint configurations that rely only on compiler defaults
- Ad hoc naming conventions without explicit weasel-word avoidance

# Common Errors

- **Error**: Using `#[allow]` for lint overrides in non-generated code.
  **Correction**: Use `#[expect(lint_name, reason = "justification")]` so that stale suppressions produce warnings when the underlying issue is resolved.

- **Error**: Naming a type `ConnectionManager` when it actually pools connections.
  **Correction**: Call it `ConnectionPool` -- the name should describe what the type does, not that it "manages" something.

- **Error**: Adding a magic value with a comment that only restates the value ("Wait 86400 seconds").
  **Correction**: Document why the value was chosen, what happens if it changes, and what external systems depend on it.

# Common Confusions

- **Confusion**: Thinking M-UPSTREAM-GUIDELINES means Pragmatic Rust replaces the Rust API Guidelines.
  **Clarification**: Pragmatic Rust explicitly complements, not replaces, the upstream guidelines. Both must be followed.

- **Confusion**: Assuming all Clippy restriction lints should be enabled.
  **Clarification**: M-STATIC-VERIFICATION selectively enables specific restriction lints, not the entire group. The full restriction group would be too noisy; the guideline curates a useful subset.

# Source Reference

Chapter 1: Universal Guidelines, sections M-UPSTREAM-GUIDELINES (v1.0), M-STATIC-VERIFICATION (v1.0, includes full Cargo.toml lint configurations), M-LINT-OVERRIDE-EXPECT (v1.0), M-CONCISE-NAMES (v1.0), and M-DOCUMENTED-MAGIC (v1.0). Each section includes rationale and code examples.

# Verification Notes

- Definition: Direct quotations from each guideline section
- Key Properties: Drawn from the specific tool lists, lint configurations, and naming examples in the source
- Confidence: HIGH -- all five guidelines are explicit with code examples and detailed rationale
- Uncertainties: The specific Clippy restriction lint list may evolve with new Clippy versions
- Cross-reference status: All slugs are within this extraction set or reference Agent B's planned cards
