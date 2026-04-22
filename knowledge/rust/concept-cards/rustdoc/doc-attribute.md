---
# === CORE IDENTIFICATION ===
concept: The #[doc] Attribute
slug: doc-attribute

# === CLASSIFICATION ===
category: documentation
subcategory: attributes
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "The #[doc] attribute"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "doc attribute"
  - "#[doc] attribute"
  - "doc(hidden)"
  - "doc(alias)"
  - "doc(html_playground_url)"
  - "doc(html_logo_url)"
  - "doc(html_favicon_url)"
  - "doc(inline)"
  - "doc(no_inline)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - doc-reexports
  - doc-tests
  - rustdoc-unstable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the relationship between /// and #[doc]?"
  - "How do I include an external file as documentation?"
  - "How do I hide an item from documentation?"
  - "How do I add a search alias to an item?"
  - "How do I set the crate logo and favicon in docs?"
  - "How do I add a playground URL to doc examples?"
  - "What crate-level #[doc] options are available?"
  - "What item-level #[doc] options are available?"
  - "How do I control attributes applied to doc tests?"
---

# Quick Definition

The `#[doc]` attribute is the underlying mechanism for all Rust documentation. Doc comments (`///` and `//!`) are syntactic sugar for `#[doc = "..."]`. Beyond raw text, `#[doc]` provides crate-level options (favicon, logo, playground URL, source visibility) and item-level options (`hidden`, `inline`, `no_inline`, `alias`, `test(attr(...))`). It also supports including external files as documentation via `#[doc = include_str!("...")]`.

# Core Definition

The `#[doc]` attribute controls how rustdoc generates documentation. At its most basic, `/// This is a doc comment.` is equivalent to `#[doc = r" This is a doc comment."]`, and `//!` is equivalent to `#![doc]`.

The attribute has two primary use cases beyond raw documentation text:

**Crate-level attributes** (`#![doc(...)]`):
- `html_favicon_url`: Sets the docs favicon
- `html_logo_url`: Sets the logo in the upper left
- `html_playground_url`: Enables "Run" buttons linked to a playground
- `html_root_url`: Base URL for linking to external crate docs
- `html_no_source`: Disables source code inclusion
- `issue_tracker_base_url`: Links to tracking issues for unstable features
- `test(no_crate_inject)`: Prevents automatic `extern crate` injection in doc tests
- `test(attr(...))`: Adds attributes to all doc tests in scope

**Item-level attributes** (`#[doc(...)]`):
- `hidden`: Removes the item from generated documentation
- `inline`: Forces a re-exported item to be inlined into the current module's docs
- `no_inline`: Prevents inlining of a re-exported item
- `alias`: Adds a search alias for the item

The `#[doc]` attribute also supports macro-generated documentation through multiple attributes that are merged by the `collapse-docs` pass, and external file inclusion via `include_str!`.

# Prerequisites

- **doc-comments** -- understanding that `///` and `//!` are sugar for `#[doc]`

# Key Properties

1. **Sugar equivalence**: `/// text` equals `#[doc = r" text"]`; `//!` equals `#![doc]`
2. **Multiple `#[doc]` merge**: Multiple `#[doc = "..."]` attributes are collapsed into one, useful in macro-generated code
3. **External file inclusion**: `#[doc = include_str!("../../README.md")]` includes a file as documentation text
4. **`hidden` is documentation-only**: `#[doc(hidden)]` hides from docs but does not change visibility or accessibility
5. **`alias` adds search entries**: `#[doc(alias = "TheAlias")]` makes the item findable by alternative names, especially useful for FFI bindings
6. **`test(attr(...))` is inherited**: Test attributes are appended to parent module's attributes, not replaced. Child modules accumulate all parent test attributes.
7. **Playground URL enables Run buttons**: `#![doc(html_playground_url = "...")]` adds interactive code execution to examples

# Construction / Recognition

## External File as Documentation:
```rust
#[doc = include_str!("../../README.md")]
pub struct MyStruct;
```

## Macro-Generated Documentation:
```rust
#[doc = "This is"]
#[doc = " a "]
#[doc = "doc comment"]
fn f() {}
```

## Crate-Level Configuration:
```rust
#![doc(html_favicon_url = "https://example.com/favicon.ico")]
#![doc(html_logo_url = "https://example.com/logo.jpg")]
#![doc(html_playground_url = "https://playground.example.com/")]
#![doc(html_root_url = "https://docs.rs/serde/1.0")]
#![doc(html_no_source)]
#![doc(test(no_crate_inject))]
```

## Item-Level Attributes:
```rust
#[doc(hidden)]
pub fn internal_helper() {}

#[doc(alias = "lib_name_do_something")]
pub fn do_something(&mut self) -> i32 { /* ... */ }

#[doc(inline)]
pub use bar::Bar;

#[doc(no_inline)]
pub use bar::Baz;
```

## Test Attributes:
```rust
#![doc(test(attr(deny(dead_code))))]

mod my_mod {
    #![doc(test(attr(allow(dead_code))))]
    // Both deny(dead_code) and allow(dead_code) apply to doctests here
}
```

# Context & Application

The `#[doc]` attribute is essential for crate authors who need fine-grained control over generated documentation. FFI crate authors benefit heavily from `#[doc(alias = "...")]` to make Rust wrappers discoverable by their C function names. Library authors use `#[doc(hidden)]` to keep implementation details out of the public documentation while maintaining public access for dependent crates. The `test(attr(...))` feature lets crate authors enforce lint levels across all doc tests.

# Examples

**Example 1** (Ch 4): The sugar equivalence:
```rust
/// This is a doc comment.
#[doc = r" This is a doc comment."]
```

**Example 2** (Ch 4): FFI alias for discoverability:
```rust
// C function: int lib_name_do_something(Obj *obj);
impl Obj {
    #[doc(alias = "lib_name_do_something")]
    pub fn do_something(&mut self) -> i32 {
        unsafe { ffi::lib_name_do_something(self.inner) }
    }
}
```
> "Users can now look for `lib_name_do_something` in our crate directly and find `Obj::do_something`."

**Example 3** (Ch 4): Test attribute inheritance:
```rust
#![doc(test(attr(deny(dead_code))))]

mod my_mod {
    #![doc(test(attr(allow(dead_code))))]
    // For every doctest in `my_mod`, both attributes are present:
    // #![deny(dead_code)]  -- from crate root
    // #![allow(dead_code)] -- from my_mod
}
```

**Example 4** (Ch 4): Playground URL enabling Run buttons:
```rust
#![doc(html_playground_url = "https://playground.example.com/")]
```
> "When you press 'run', the button will make a request to this domain."

# Relationships

## Builds Upon
- **doc-comments** -- `#[doc]` is the underlying mechanism for doc comments

## Enables
- **doc-reexports** -- `#[doc(inline)]` and `#[doc(no_inline)]` control re-export inlining
- **doc-tests** -- `#[doc(test(...))]` configures doc test behavior

## Related
- **rustdoc-unstable** -- nightly features add `#[doc(cfg(...))]`, `#[doc(auto_cfg)]`, `#[doc(notable_trait)]`, `#[doc(masked)]`
- **rustdoc-cli** -- some `#[doc]` options have command-line equivalents

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Using `#[doc(hidden)]` thinking it makes an item inaccessible.
  **Correction**: `#[doc(hidden)]` only hides from documentation. The item remains public and usable in code. Use `pub(crate)` for actual access restriction.

- **Error**: Expecting `test(attr(...))` on a child module to replace the parent's test attributes.
  **Correction**: `test(attr(..))` attributes are *appended* to the parent's, not replaced. The child module gets both the parent's and its own test attributes.

- **Error**: Setting `html_playground_url` but the playground doesn't have the crate available.
  **Correction**: "Please be aware that the official Rust Playground at play.rust-lang.org does not have every crate available, so if your examples require your crate, make sure the playground you provide has your crate available."

# Common Confusions

- **Confusion**: Thinking `#[doc = include_str!("README.md")]` on a function includes the README as part of that function's docs.
  **Clarification**: The `include_str!` content replaces the entire doc content for that item. It is typically used on a dummy struct with `#[cfg(doctest)]` to test README examples, not on actual API items.

- **Confusion**: Thinking `#[doc(alias)]` changes the item's name or creates a type alias.
  **Clarification**: `#[doc(alias = "...")]` only affects the search index in generated documentation. It has no effect on the compiler or the item's actual name.

- **Confusion**: Thinking `#[doc(inline)]` and `#[doc(no_inline)]` affect code behavior.
  **Clarification**: These attributes only affect how rustdoc presents re-exports in documentation -- whether the re-exported item appears in the re-exporting module's page or as a "Re-exports" link.

# Source Reference

Chapter 4: How to Write Documentation; section "The #[doc] attribute" covering crate-level and item-level sub-attributes. Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- "That is, `///` is syntax sugar for `#[doc]` (as is `//!` for `#![doc]`)" and the complete enumeration of sub-attributes
- Confidence rationale: HIGH -- the source provides a comprehensive reference of all stable `#[doc]` variants with examples
- Uncertainties: Some `#[doc]` variants are nightly-only (cfg, auto_cfg, notable_trait, masked) -- covered in rustdoc-unstable
- Cross-reference status: doc-comments, doc-reexports, doc-tests, rustdoc-unstable are in this extraction set
