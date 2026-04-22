---
concept: Rust Attributes
slug: rust-attributes
category: language-semantics
subcategory: metaprogramming
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Attributes"
chapter_number: 7
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "built-in attributes"
  - "attribute syntax"
  - "inner attributes"
  - "outer attributes"
  - "derive attribute"
  - "lint attributes"
  - "diagnostic attributes"
prerequisites: []
extends: []
related:
  - rust-items
  - conditional-compilation
contrasts_with: []
answers_questions:
  - "What is the syntax for inner and outer attributes in Rust?"
  - "What are the categories of built-in attributes?"
  - "Which attributes are considered unsafe?"
  - "What is the difference between active and inert attributes?"
  - "What are the built-in derive macros available in Rust?"
  - "How do lint check attributes (allow, warn, deny, forbid, expect) interact?"
  - "What does the non_exhaustive attribute do?"
  - "What are tool attributes?"
---

# Quick Definition

An attribute is "a general, free-form metadatum that is interpreted according to name, convention, language, and compiler version" (Ch. 7). Attributes come in two positional forms -- inner attributes (`#![...]`, applying to the enclosing item) and outer attributes (`#[...]`, applying to the following item) -- and four classification kinds: built-in attributes, proc macro attributes, derive macro helper attributes, and tool attributes. Rust provides a comprehensive set of built-in attributes organized into 12 categories covering conditional compilation, testing, derives, diagnostics, ABI/linking, code generation, documentation, preludes, modules, limits, runtime, and the type system.

# Core Definition

Attributes are "modeled on Attributes in ECMA-335, with the syntax coming from ECMA-334 (C#)" (Ch. 7). The attribute syntax consists of a path followed by an optional delimited token tree or `= Expression`.

**Inner vs. Outer**: Inner attributes (`#![attr]`, with a bang) "apply to the form that the attribute is declared within" -- such as a module, crate, or function body. Outer attributes (`#[attr]`, without the bang) "apply to the form that follows the attribute."

**Active vs. Inert**: "Active attributes remove themselves from the form they are on while inert attributes stay on." Only `cfg`, `cfg_attr`, and attribute macros are active; all other attributes are inert.

**Unsafe attributes**: Some attributes are unsafe to apply because they carry obligations the compiler cannot check. These must be wrapped in `unsafe(...)`: `export_name`, `link_section`, `naked`, and `no_mangle`.

**Meta item syntax**: Most built-in attributes use the MetaItem grammar with five common forms: MetaWord (`no_std`), MetaNameValueStr (`doc = "example"`), MetaListPaths (`allow(unused, clippy::inline_always)`), MetaListIdents (`macro_use(foo, bar)`), and MetaListNameValueStr (`link(name = "CoreFoundation", kind = "framework")`).

**Attribute positions**: Items accept outer attributes; external blocks, functions, implementations, and modules also accept inner attributes. Attributes can additionally appear on statements, block expressions, enum variants, struct/union fields, match arms, generic parameters, function/closure parameters, and inline assembly operands.

# Prerequisites

Basic familiarity with Rust items and syntax is assumed. Understanding of conditional compilation (`cfg`) helps for the conditional compilation attributes category.

# Key Properties

1. **12 categories of built-in attributes**: conditional compilation, testing, derive, macros, diagnostics, ABI/linking/symbols/FFI, code generation, documentation, preludes, modules, limits, runtime, type system, and debugger
2. **Lint check hierarchy**: `allow` suppresses, `expect` suppresses but warns if lint does not fire, `warn` warns, `deny` errors, `forbid` errors and prevents further overrides (except `deny` inside `forbid` is allowed but ignored)
3. **Derive**: applies only to structs, enums, and unions; built-in derives are `Clone`, `Copy`, `Debug`, `Default`, `Eq`, `Hash`, `Ord`, `PartialEq`, `PartialOrd`
4. **`deprecated`** accepts `since` and `note` fields; can apply to any item, trait item, enum variant, struct field, external block item, or macro definition
5. **`must_use`** triggers `unused_must_use` lint on types (struct/enum/union), function return values, and trait return types; exception for `Result<(), E>` when `E` is uninhabited
6. **`inline`** has three modes: `#[inline]` (suggest), `#[inline(always)]` (suggest always), `#[inline(never)]` (suggest never) -- all are hints the compiler may ignore
7. **`non_exhaustive`** on structs/enums/variants prevents construction and exhaustive matching from outside the defining crate; has no effect within the defining crate
8. **`test`** marks a function as a test; the function must be monomorphic, take no arguments, and return a type implementing `Termination`
9. **`should_panic`** on test functions causes the test to pass only if it panics; an `expected` string can filter panic messages
10. **Tool attributes** use namespaced paths (e.g., `rustfmt::skip`, `clippy::cyclomatic_complexity`); currently recognized tools are clippy, rustfmt, diagnostic, miri, and rust_analyzer

# Construction / Recognition

## To Apply Attributes:

1. Place outer attributes before the item: `#[derive(Debug)] struct Foo;`
2. Place inner attributes at the beginning of the enclosing scope: `#![allow(unused)]`
3. For unsafe attributes, wrap in `unsafe()`: `#[unsafe(no_mangle)]`
4. For lint control, choose the appropriate level: `allow` < `expect` < `warn` < `deny` < `forbid`

## To Identify Attribute Behavior:

1. Check if the attribute is active (`cfg`, `cfg_attr`, proc macro attributes) or inert (all others)
2. Active attributes remove themselves during processing; inert attributes remain on the form
3. Attribute macros are expanded in a specific order: attribute macros left-to-right, then derive macros, then expression macros within attributes

# Context & Application

- **Conditional compilation**: `#[cfg]` and `#[cfg_attr]` control which code is included based on target platform, features, or custom flags
- **Testing**: `#[test]`, `#[ignore]`, `#[should_panic]` define and control test functions
- **Deriving traits**: `#[derive(Clone, Debug, PartialEq)]` auto-generates trait implementations
- **Lint management**: `#[allow(unused)]`, `#[deny(missing_docs)]`, `#[expect(dead_code)]` control compiler warnings and errors
- **FFI and linking**: `#[link]`, `#[link_name]`, `#[repr(C)]`, `#[no_mangle]` control ABI and symbol management
- **API evolution**: `#[non_exhaustive]` enables adding fields/variants without breaking downstream code; `#[deprecated]` signals migration paths
- **Performance hints**: `#[inline]`, `#[cold]`, `#[target_feature]` guide code generation

# Examples

**Example 1** (Ch. 7, "Attributes"): Inner vs. outer attribute syntax:
```rust
#![crate_type = "lib"]  // Inner: applies to enclosing crate

#[test]                  // Outer: applies to following function
fn test_foo() { /* ... */ }

#[cfg(target_os = "linux")]  // Outer: conditionally includes module
mod bar { /* ... */ }
```

**Example 2** (Ch. 7, "Derive"): Using derive with built-in macros and the generated implementation:
```rust
#[derive(PartialEq, Clone)]
struct Foo<T> {
    a: i32,
    b: T,
}
// Generates:
// impl<T: PartialEq> PartialEq for Foo<T> { ... }
// impl<T: Clone> Clone for Foo<T> { ... }
```

**Example 3** (Ch. 7, "Lint check attributes"): Lint level hierarchy and overriding:
```rust
#[warn(missing_docs)]
pub mod m2 {
    #[allow(missing_docs)]
    pub mod nested {
        pub fn undocumented_one() -> i32 { 1 }  // No warning

        #[warn(missing_docs)]
        pub fn undocumented_two() -> i32 { 2 }  // Warning despite allow above
    }
    pub fn undocumented_too() -> i32 { 3 }  // Warning
}
```

**Example 4** (Ch. 7, "The non_exhaustive attribute"): Preventing external construction:
```rust
#[non_exhaustive]
pub struct Config {
    pub window_width: u16,
    pub window_height: u16,
}

#[non_exhaustive]
pub enum Error {
    Message(String),
    Other,
}
// Within the defining crate: construction and exhaustive matching work normally.
// Outside: must use `..` in struct patterns, `_` in enum matches.
```

# Relationships

## Builds Upon
(none -- attributes are a foundational language mechanism)

## Enables
- **conditional-compilation** -- `cfg` and `cfg_attr` are attributes that control conditional compilation
- **rust-items** -- attributes modify item behavior (derive, visibility, representation, etc.)

## Related
- **rust-items** -- items are the primary forms to which attributes are attached
- **conditional-compilation** -- the `cfg` system is the most prominent active attribute system

## Contrasts With
(none within scope)

# Common Errors

- **Error**: Using `#[forbid(lint)]` and then trying to `#[allow(lint)]` in a child scope.
  **Correction**: "forbid is the same as deny, but also forbids changing the lint level afterwards." The `allow` will be rejected. Only `deny` is permitted within a `forbid` context (but is ignored).

- **Error**: Applying `#[derive]` to a function or trait.
  **Correction**: "The derive attribute may only be applied to structs, enums, and unions" (Ch. 7).

- **Error**: Expecting `#[non_exhaustive]` to have an effect within the defining crate.
  **Correction**: "Within the defining crate, non_exhaustive has no effect" (Ch. 7). The restrictions only apply to downstream crates.

- **Error**: Forgetting `unsafe(...)` wrapper on attributes like `#[no_mangle]`.
  **Correction**: `export_name`, `link_section`, `naked`, and `no_mangle` are unsafe attributes that must be written as `#[unsafe(no_mangle)]` to assert the programmer has verified safety obligations.

# Common Confusions

- **Confusion**: `#[inline]` guarantees inlining.
  **Clarification**: "In every form the attribute is a hint. The compiler may ignore it." Even `#[inline(always)]` is technically a suggestion. The attribute is also ignored if the function is externally exported with `no_mangle` or `export_name`.

- **Confusion**: `#[allow]` and `#[expect]` are identical.
  **Clarification**: `#[expect(C)]` "indicates that lint C is expected to be emitted. The attribute will suppress the emission of C or issue a warning, if the expectation is unfulfilled." Unlike `allow`, `expect` warns you when the suppressed lint no longer fires, helping catch stale suppressions.

- **Confusion**: `#[must_use]` on a function prevents the function from being called without using its return value.
  **Clarification**: `must_use` only triggers a lint (`unused_must_use`), not a hard error (unless the lint level is set to `deny` or `forbid`). The code still compiles with default settings.

# Source Reference

Chapter 7: Attributes (2873 lines). Covers attribute syntax (inner/outer, meta item grammar, active/inert classification, tool attributes, unsafe attributes), built-in attributes index (12 categories), testing attributes (`test`, `ignore`, `should_panic`), derive (built-in derives, `automatically_derived`), diagnostic attributes (lint checks with `allow`/`expect`/`warn`/`deny`/`forbid`, lint reasons, `#[expect]`, lint groups, tool lint attributes, `deprecated`, `must_use`, `diagnostic::on_unimplemented`, `diagnostic::do_not_recommend`), code generation attributes (`inline`, `cold`, `naked`, `no_builtins`, `target_feature`, `track_caller`, `instruction_set`), limits (`recursion_limit`, `type_length_limit`), type system attributes (`non_exhaustive`), and debugger attributes (`debugger_visualizer`, `collapse_debuginfo`).

# Verification Notes

- Definition source: Direct synthesis from Ch. 7, with key phrases quoted verbatim from the reference
- Key Properties: All 10 items directly supported by explicit source text
- Confidence rationale: HIGH -- the source is the authoritative language reference with comprehensive, explicit specification
- Uncertainties: The `diagnostic` tool attribute namespace contains hint-level attributes whose behavior may evolve; `type_length_limit` enforcement requires a nightly flag
- Cross-reference status: Related slugs reference cards in the reference extraction set
