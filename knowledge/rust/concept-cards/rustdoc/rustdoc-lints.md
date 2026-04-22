---
# === CORE IDENTIFICATION ===
concept: Rustdoc Lints
slug: rustdoc-lints

# === CLASSIFICATION ===
category: documentation
subcategory: quality-enforcement
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "Lints"
chapter_number: 5
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustdoc lint warnings"
  - "documentation lints"
  - "rustdoc::broken_intra_doc_links"
  - "missing_docs lint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustdoc
extends: []
related:
  - rustdoc-cli
  - intra-doc-links
  - doc-tests
  - doc-comments
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What lints does rustdoc provide for documentation quality?"
  - "How do I enable or disable specific rustdoc lints?"
  - "What is the broken_intra_doc_links lint?"
  - "How do I require documentation on all public items?"
  - "What lint catches typos in code block attributes like should_panic?"
  - "Which rustdoc lints are on by default?"
  - "Which rustdoc lints are off (allow) by default?"
  - "Can I use rustdoc lints from rustc, or only from rustdoc?"
  - "What lint detects bare URLs in documentation?"
  - "What lint catches invalid HTML tags in documentation?"
---

# Quick Definition

Rustdoc provides a set of documentation-specific lints that detect broken links, missing documentation, invalid code blocks, HTML issues, bare URLs, unescaped backticks, and redundant explicit links. These lints use the standard `allow`/`warn`/`deny` mechanism and are prefixed with `rustdoc::`, except for `missing_docs` which is available from both `rustc` and `rustdoc`.

# Core Definition

Rustdoc lints are static analysis checks focused on documentation quality. As stated in the source: "`rustdoc` provides lints to help you writing and testing your documentation. You can use them like any other lints." (Ch. 5: Lints). The lints use the standard Rust lint level attributes:

```rust
#![allow(rustdoc::broken_intra_doc_links)]  // suppress
#![warn(rustdoc::broken_intra_doc_links)]   // warn
#![deny(rustdoc::broken_intra_doc_links)]   // error
```

A key distinction: "except for `missing_docs`, these lints are only available when running `rustdoc`, not `rustc`." This means most documentation lints only fire during `cargo doc` or `rustdoc` invocations, not during `cargo build` or `cargo check`.

The lints fall into two groups by default level:

**Warn by default**: `broken_intra_doc_links`, `private_intra_doc_links`, `invalid_codeblock_attributes`, `invalid_html_tags`, `invalid_rust_codeblocks`, `bare_urls`, `redundant_explicit_links`.

**Allow by default**: `missing_docs`, `missing_crate_level_docs`, `missing_doc_code_examples` (nightly-only), `private_doc_tests`, `unescaped_backticks`.

# Prerequisites

- **rustdoc** -- Understanding what rustdoc is and when it runs

# Key Properties

1. **Standard lint mechanism**: All lints support `allow`, `warn`, `deny` via attributes or command-line flags
2. **Rustdoc-only execution**: All lints except `missing_docs` only run during `rustdoc`, not `rustc`
3. **Namespace prefix**: Lints are namespaced as `rustdoc::lint_name` (except `missing_docs`)
4. **Link validation**: `broken_intra_doc_links` detects unresolvable intra-doc links and ambiguities; `private_intra_doc_links` warns when public docs link to private items
5. **Code block validation**: `invalid_codeblock_attributes` catches typos like `should-panic` (should be `should_panic`); `invalid_rust_codeblocks` detects empty or unparseable Rust code blocks
6. **HTML validation**: `invalid_html_tags` detects unclosed or invalid HTML tags in documentation
7. **URL validation**: `bare_urls` detects URLs not wrapped in angle brackets or link syntax
8. **Backtick validation**: `unescaped_backticks` (allow by default) detects broken inline code caused by unmatched backticks
9. **Completeness enforcement**: `missing_docs` enforces documentation on all public items; `missing_crate_level_docs` checks for crate root documentation; `missing_doc_code_examples` (nightly) enforces code examples
10. **Ambiguity resolution**: `broken_intra_doc_links` suggests disambiguation syntax like `enum@Foo` or `Foo()` when a name is ambiguous

# Construction / Recognition

## Enabling Lints Crate-Wide:
```rust
#![warn(missing_docs)]                          // require docs on public items
#![warn(rustdoc::missing_crate_level_docs)]     // require crate-level docs
#![deny(rustdoc::broken_intra_doc_links)]       // error on broken links
#![warn(rustdoc::unescaped_backticks)]           // catch broken inline code
```

## Common Lint Triggers:

**broken_intra_doc_links** -- linking to nonexistent items:
```rust
/// I want to link to [`Nonexistent`] but it doesn't exist!
pub fn foo() {}
```

**invalid_codeblock_attributes** -- typos in code block annotations:
```rust
/// ```should-panic
/// assert_eq!(1, 2);
/// ```
pub fn foo() {}
// Warning: unknown attribute `should-panic`. Did you mean `should_panic`?
```

**bare_urls** -- unlinked URLs:
```rust
/// http://example.org
pub fn foo() {}
// Warning: help: use an automatic link instead: `<http://example.org>`
```

**redundant_explicit_links** -- unnecessary explicit link targets:
```rust
/// Takes 2 [`usize`](usize) values
pub fn add(left: usize, right: usize) -> usize { left + right }
// Warning: redundant explicit rustdoc link
```

# Context & Application

Rustdoc lints are essential for maintaining documentation quality in Rust projects. Enabling `#![warn(missing_docs)]` is a common practice for libraries published to crates.io, ensuring all public API items have documentation. The `broken_intra_doc_links` lint (warn by default) catches documentation rot where refactoring changes item names but forgets to update documentation links. CI pipelines can use `#![deny(rustdoc::broken_intra_doc_links)]` to fail builds on broken documentation. The `private_intra_doc_links` lint is important because it catches links that work during development with `--document-private-items` but would break in published documentation.

# Examples

**Example 1** (Ch. 5): Ambiguous intra-doc link with disambiguation suggestion:
```rust
/// [`Foo`]
pub fn function() {}
pub enum Foo {}
pub fn Foo() {}
```
```text
warning: `Foo` is both an enum and a function
help: to link to the enum, prefix with the item type
  /// [`enum@Foo`]
help: to link to the function, add parentheses
  /// [`Foo()`]
```

**Example 2** (Ch. 5): Private intra-doc link with `--document-private-items` interaction:
```rust
/// [private]
pub fn public() {}
fn private() {}
```
Without `--document-private-items`: warns that the link will be broken.
With `--document-private-items`: warns but still generates the link, noting "this link resolves only because you passed `--document-private-items`, but will break without."

**Example 3** (Ch. 5): Unescaped backtick detection:
```rust
#![warn(rustdoc::unescaped_backticks)]
/// `add(a, b) is the same as `add(b, a)`.
pub fn add(a: i32, b: i32) -> i32 { a + b }
```
The lint detects the unmatched backtick and suggests either closing the inline code with `` `add(a, b)` `` or escaping the literal backtick with `\``.

**Example 4** (Ch. 5): Invalid HTML tag detection:
```rust
/// <h1>
/// </script>
pub fn foo() {}
```
Produces two warnings: "unopened HTML tag `script`" and "unclosed HTML tag `h1`."

**Example 5** (Ch. 5): Items exempt from `missing_doc_code_examples`:
> This lint is not emitted for impl blocks, enum variants, struct/union fields, type aliases (including associated types), statics/constants, modules, or foreign reexported items.

# Relationships

## Builds Upon
- **rustdoc** -- lints run during rustdoc execution

## Enables
- None directly -- lints enforce quality but do not enable other features

## Related
- **rustdoc-cli** -- `--document-private-items` affects `private_intra_doc_links` behavior
- **intra-doc-links** -- `broken_intra_doc_links` and `private_intra_doc_links` validate these links
- **doc-tests** -- `private_doc_tests` detects tests on private items; `missing_doc_code_examples` enforces their presence
- **doc-comments** -- all lints analyze content within doc comments

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting rustdoc lints to fire during `cargo build` or `cargo check`.
  **Correction**: "Except for `missing_docs`, these lints are only available when running `rustdoc`, not `rustc`." Run `cargo doc` to trigger documentation lints.

- **Error**: Using `should-panic` instead of `should_panic` in code block attributes.
  **Correction**: The `invalid_codeblock_attributes` lint catches this: "unknown attribute `should-panic`. Did you mean `should_panic`?" Code block attributes use underscores, not hyphens.

- **Error**: Writing `#![warn(broken_intra_doc_links)]` without the `rustdoc::` prefix.
  **Correction**: All rustdoc-specific lints must be prefixed with `rustdoc::`, e.g., `#![warn(rustdoc::broken_intra_doc_links)]`. The only exception is `missing_docs`, which has no prefix.

# Common Confusions

- **Confusion**: Thinking `missing_docs` is a rustdoc-only lint like the others.
  **Clarification**: "`missing_docs` is also available from `rustc` directly." It fires during `cargo build` and `cargo check`, unlike all other rustdoc lints. It also does not use the `rustdoc::` namespace prefix.

- **Confusion**: Thinking `private_intra_doc_links` prevents the link from being generated.
  **Clarification**: When `--document-private-items` is passed, the link is still generated despite the warning. The lint warns that the link "will break without" that flag -- it is about the published documentation, not the current build.

- **Confusion**: Thinking `missing_doc_code_examples` applies to all items.
  **Clarification**: This nightly-only lint is explicitly not emitted for impl blocks, enum variants, struct/union fields, type aliases, statics/constants, modules, and foreign reexported items.

# Source Reference

Chapter 5: Lints -- all 12 lints documented with default levels, examples, and diagnostic output. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 5 -- "`rustdoc` provides lints to help you writing and testing your documentation."
- Confidence rationale: HIGH -- each lint is documented with its default level, example code, and exact diagnostic output
- Uncertainties: `missing_doc_code_examples` is nightly-only and may change
- Cross-reference status: rustdoc, rustdoc-cli are in this extraction set; intra-doc-links, doc-tests, doc-comments from Agent B
