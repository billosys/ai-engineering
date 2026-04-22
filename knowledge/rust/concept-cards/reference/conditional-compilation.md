---
concept: Conditional Compilation
slug: conditional-compilation
category: language-semantics
subcategory: compilation-model
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Conditional Compilation"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "cfg attribute"
  - "cfg_attr attribute"
  - "cfg macro"
  - "configuration predicate"
  - "cfg_select macro"
  - "platform-conditional code"
prerequisites: []
extends: []
related:
  - rust-attributes
  - rust-items
contrasts_with: []
answers_questions:
  - "How does Rust conditionally compile source code?"
  - "What are the available configuration predicates in cfg?"
  - "What is the difference between the cfg attribute, cfg_attr, and the cfg! macro?"
  - "What target configuration options are available for conditional compilation?"
  - "How does cfg_select differ from nested cfg attributes?"
---

# Quick Definition

Conditional compilation in Rust allows source code to be included or excluded based on configuration predicates evaluated at compile time. The system provides three main mechanisms: the `#[cfg]` attribute (which removes annotated items entirely), the `#[cfg_attr]` attribute (which conditionally applies other attributes), and the `cfg!()` macro (which evaluates to a boolean at compile time without removing code). A fourth mechanism, `cfg_select!`, selects among multiple branches based on configuration predicates.

# Core Definition

"Conditionally compiled source code is source code that is compiled only under certain conditions" (Ch. 5). The system is built on _configuration predicates_ that evaluate to true or false. Configuration options are "either names or key-value pairs, and are either set or unset" -- names are single identifiers like `unix`, while key-value pairs use the form `target_arch = "x86_64"`. Keys do not need to be unique; for example, both `feature = "std"` and `feature = "serde"` can be set simultaneously.

Predicates compose with three logical operators: `all()` (true if all sub-predicates are true or the list is empty), `any()` (true if at least one sub-predicate is true; false if empty), and `not()` (negation). The literal values `true` and `false` are also valid predicates.

Configuration options are "determined statically during the compilation of the crate" -- some are compiler-set based on the target, while others are arbitrarily-set via compiler flags. "It is not possible to set a configuration option from within the source code of the crate being compiled."

# Prerequisites

General familiarity with Rust attributes and item structure is helpful but not required. This is a standalone compilation concept.

# Key Properties

1. **Configuration options** are either names (e.g., `unix`) or key-value pairs (e.g., `target_os = "linux"`), set statically at compile time
2. **Three predicate combinators**: `all()` (conjunction), `any()` (disjunction), `not()` (negation), plus `true`/`false` literals
3. **`#[cfg]` attribute** removes the annotated form entirely when the predicate is false; when true, the attribute itself is stripped and the form remains
4. **`#[cfg_attr]` attribute** conditionally expands to zero or more other attributes; it can nest (a `cfg_attr` can expand to another `cfg_attr`)
5. **`cfg!()` macro** evaluates to a `true` or `false` literal at compile time without removing any code -- useful in runtime expressions like `if cfg!(unix)`
6. **`cfg_select!` macro** selects code from the first matching arm (like a compile-time match); a `_` wildcard arm always matches; it is a compile error if no arm matches
7. **`crate_type` and `crate_name`** cannot be used with `cfg_attr`
8. **Crate-level `cfg`**: when false, the crate still exists but attributes preceding the `cfg` are kept while following content is removed (enables patterns like `#![no_std]` before `#![cfg(false)]`)

# Construction / Recognition

## To Use Conditional Compilation:

1. For item-level inclusion/exclusion: `#[cfg(predicate)]` on the item
2. For conditional attribute application: `#[cfg_attr(predicate, attr1, attr2)]`
3. For runtime boolean checks: `if cfg!(predicate) { ... }`
4. For multi-branch selection: `cfg_select! { pred1 => { ... }, pred2 => { ... }, _ => { ... } }`

## To Identify Target Configuration:

Use `rustc --print cfg --target $TARGET` to display all configuration options set for a given target. Feature flags are set via `--cfg feature="name"` or through Cargo's `[features]` mechanism.

# Context & Application

- **Platform-specific code**: Use `#[cfg(target_os = "linux")]` or `#[cfg(unix)]` to provide OS-specific implementations
- **Feature flags**: `#[cfg(feature = "serde")]` for optional dependencies, following the Cargo convention
- **Test code**: `#[cfg(test)]` to compile test modules only in test mode
- **Architecture-specific optimizations**: `#[cfg(target_arch = "x86_64")]` combined with `target_feature` checks
- **Debug-only code**: `#[cfg(debug_assertions)]` for code that runs only in debug builds

# Examples

**Example 1** (Ch. 5, "The cfg attribute"): Platform-specific functions using logical combinators:
```rust
#[cfg(target_os = "macos")]
fn macos_only() { /* ... */ }

#[cfg(all(unix, target_pointer_width = "32"))]
fn on_32bit_unix() { /* ... */ }

#[cfg(not(foo))]
fn needs_not_foo() { /* ... */ }
```

**Example 2** (Ch. 5, "The cfg_attr attribute"): Conditional module path selection:
```rust,ignore
#[cfg_attr(target_os = "linux", path = "linux.rs")]
#[cfg_attr(windows, path = "windows.rs")]
mod os;
```

**Example 3** (Ch. 5, "The cfg_select macro"): Compile-time branch selection:
```rust
cfg_select! {
    unix => {
        fn foo() { /* unix specific functionality */ }
    }
    target_pointer_width = "32" => {
        fn foo() { /* non-unix, 32-bit functionality */ }
    }
    _ => {
        fn foo() { /* fallback implementation */ }
    }
}
```

**Example 4** (Ch. 5, "The cfg macro"): Runtime boolean check:
```rust
let machine_kind = if cfg!(unix) {
  "unix"
} else if cfg!(windows) {
  "windows"
} else {
  "unknown"
};
```

# Relationships

## Builds Upon
(none -- conditional compilation is a foundational compilation mechanism)

## Enables
- **rust-attributes** -- `cfg` and `cfg_attr` are among the most commonly used built-in attributes
- **rust-items** -- items are the primary targets of conditional compilation

## Related
- **rust-attributes** -- `cfg` and `cfg_attr` are classified as active attributes (they remove themselves during processing)

## Contrasts With
(none within scope)

# Common Errors

- **Error**: Using `cfg_attr` with `crate_type` or `crate_name`.
  **Correction**: These two attributes "cannot be used with cfg_attr" (Ch. 5). They must be applied unconditionally.

- **Error**: Expecting `cfg_select!` to compile when no arm matches.
  **Correction**: "It is a compile error if none of the predicates evaluate to true." Always include a `_` wildcard arm as a fallback when exhaustiveness is not guaranteed.

- **Error**: Attempting to set configuration options from within source code.
  **Correction**: Configuration options are determined externally. Use `--cfg` flags for `rustc` or `[features]` in `Cargo.toml` for Cargo-managed projects.

# Common Confusions

- **Confusion**: `#[cfg(...)]` and `cfg!(...)` are interchangeable.
  **Clarification**: `#[cfg(...)]` is an attribute that removes the entire annotated form when false. `cfg!(...)` is a macro that evaluates to a boolean literal at compile time -- the surrounding code is always compiled, only the branch taken changes at runtime. Use `#[cfg]` for item-level exclusion and `cfg!()` for runtime branching.

- **Confusion**: `any()` with no predicates evaluates to true (like `all()`).
  **Clarification**: `all()` with an empty list is true, but `any()` with an empty list is false. This follows standard logical convention (conjunction identity is true, disjunction identity is false).

- **Confusion**: `target_feature` and `target_arch` serve the same purpose.
  **Clarification**: `target_arch` identifies the CPU architecture (e.g., "x86_64", "aarch64"), while `target_feature` identifies specific hardware features available for the target (e.g., "avx2", "sse4.1"). A single architecture may have many optional features.

# Source Reference

Chapter 5: Conditional Compilation (511 lines). Covers configuration predicate grammar, all compiler-set options (`target_arch`, `target_os`, `target_family`, `target_env`, `target_abi`, `target_endian`, `target_pointer_width`, `target_vendor`, `target_has_atomic`, `test`, `debug_assertions`, `proc_macro`, `panic`), and all four forms of conditional compilation (`cfg` attribute, `cfg_attr` attribute, `cfg!` macro, `cfg_select!` macro).

# Verification Notes

- Definition source: Direct from Chapter 5, with key phrases quoted verbatim
- Key Properties: All 8 items directly supported by source text
- Confidence rationale: HIGH -- the source is the authoritative language reference with complete, explicit specification
- Uncertainties: The `cfg_select!` macro is relatively new; its stabilization status may evolve
- Cross-reference status: Related slugs reference cards in the reference extraction set
