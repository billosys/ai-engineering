---
# === CORE IDENTIFICATION ===
concept: Rustdoc Advanced Features
slug: rustdoc-advanced-features

# === CLASSIFICATION ===
category: documentation
subcategory: advanced-configuration
tier: advanced

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "Advanced features, Scraped examples"
chapter_number: 7
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "doc(cfg)"
  - "doc(alias)"
  - "cfg(doc)"
  - "scraped examples"
  - "rustdoc platform-specific docs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustdoc
  - rustdoc-search
extends: []
related:
  - rustdoc-cli
  - rustdoc-lints
  - doc-attribute
  - rustdoc-unstable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I document platform-specific items across all platforms?"
  - "What is #[cfg(doc)] and when should I use it?"
  - "How do I add search aliases to an item with doc(alias)?"
  - "How do I set up a custom browser search engine for rustdoc?"
  - "What are scraped examples and how do I enable them?"
  - "When does rustdoc show #[repr(...)] in documentation?"
  - "How does rustdoc handle #[repr(transparent)]?"
  - "What limitations exist for cross-platform documentation?"
  - "How many scraped examples appear per item?"
---

# Quick Definition

Rustdoc's advanced features include `#[cfg(doc)]` for ensuring platform-specific items appear in documentation regardless of build target, `#[doc(alias)]` for adding search aliases to items, custom browser search engine integration, scraped examples from the `examples/` directory (unstable), and conditional display of `#[repr(...)]` annotations based on field visibility.

# Core Definition

Rustdoc provides several advanced features beyond basic documentation generation:

**`#[cfg(doc)]` for platform-specific documentation**: Rustdoc sets the `cfg(doc)` flag whenever it builds documentation. This allows items that would normally be filtered by platform-specific `cfg` attributes to appear in documentation. As the source states: "If you want to make sure an item is seen by Rustdoc regardless of what platform it's targeting, you can apply `#[cfg(doc)]` to it." (Ch. 7: Advanced features). The typical pattern combines it with other cfg attributes: `#[cfg(any(windows, doc))]`.

**`#[doc(alias)]` for search**: This attribute adds alternative search terms to an item. When users search for the alias, the item appears first in results. Aliases cannot contain quotes or most whitespace (ASCII spaces are allowed if not at the start or end). Multiple aliases can be specified individually or as a list.

**Scraped examples** (Ch. 6, unstable): Rustdoc can automatically scrape code from the `examples/` directory and include usage examples in the generated documentation. Enabled with `cargo doc -Zunstable-options -Zrustdoc-scrape-examples`. A maximum of 5 examples are included per item, with only one shown by default (rest behind a toggle), and examples are sorted by size (smaller first).

**`#[repr(...)]` display**: Rustdoc conditionally shows representation annotations. It displays `#[repr(...)]` only when none of the type's variants are `#[doc(hidden)]` and all fields are public and not `#[doc(hidden)]`. For `#[repr(transparent)]`, the attribute is shown if and only if the non-1-ZST field is public and not `#[doc(hidden)]`.

**Custom search engines**: Browser URL templates using `https://doc.rust-lang.org/stable/std/?search=%s` enable searching rustdoc directly from the browser address bar. Appending `&go_to_first=true` navigates directly to the top result.

# Prerequisites

- **rustdoc** -- Understanding the basic tool and documentation generation
- **rustdoc-search** -- Understanding how search works (for `doc(alias)` and custom search engines)

# Key Properties

1. **cfg(doc) flag**: Automatically set by rustdoc during documentation builds; not passed to doctests
2. **Platform combination pattern**: Use `#[cfg(any(platform, doc))]` to show platform-specific items in docs while preserving normal conditional compilation
3. **No cross-platform magic**: Rustdoc sees all code at once as if `--cfg doc` were passed, not by compiling once per platform
4. **Alias restrictions**: No quotes (`'`, `"`), no leading/trailing spaces, no most whitespace; ASCII space allowed mid-alias
5. **Multiple alias syntax**: Either multiple `#[doc(alias = "x")]` attributes or a single `#[doc(alias("x", "y"))]`
6. **Scraped example limits**: Maximum 5 examples per item; only 1 shown by default; sorted by size (smallest first)
7. **Scraped examples scope**: Only scrapes from files matching Cargo's `--examples` filter; `cargo check --examples` must include the file
8. **repr display heuristic**: Only shown when representation is likely part of the public ABI (public fields, no hidden variants)
9. **repr(transparent) specificity**: Displayed only when the non-1-ZST field is public and not hidden
10. **go_to_first parameter**: `?search=%s&go_to_first=true` can be appended to any rustdoc search URL

# Construction / Recognition

## Platform-Specific Documentation:
```rust
/// Token struct that can only be used on Windows.
#[cfg(any(windows, doc))]
pub struct WindowsToken;

/// Token struct that can only be used on Unix.
#[cfg(any(unix, doc))]
pub struct UnixToken;
```
Both tokens appear in documentation regardless of the build platform.

## Search Aliases:
```rust
#[doc(alias = "x")]
#[doc(alias = "big")]
pub struct BigX;

// Or equivalently:
#[doc(alias("x", "big"))]
pub struct BigX;
```
Searching for "x" or "big" in rustdoc will show `BigX` first in results.

## Enabling Scraped Examples:
```bash
cargo doc -Zunstable-options -Zrustdoc-scrape-examples
```

For docs.rs, add to `Cargo.toml`:
```toml
[package.metadata.docs.rs]
cargo-args = ["-Zunstable-options", "-Zrustdoc-scrape-examples"]
```

## Custom Browser Search Engine:
```text
https://doc.rust-lang.org/stable/std/?search=%s
https://doc.rust-lang.org/stable/std/?search=%s&go_to_first=true
```

# Context & Application

These advanced features address common real-world needs. `#[cfg(doc)]` solves the problem of documenting cross-platform libraries where important API items would be invisible on non-matching platforms. `#[doc(alias)]` improves discoverability for items with well-known alternative names (e.g., aliasing a struct by its protocol-level name). Scraped examples reduce the maintenance burden of documentation by automatically extracting real usage from the examples directory. Custom search engines improve developer workflow by allowing direct documentation lookup from the browser address bar. The `#[repr]` display logic ensures that representation details are documented when they are part of the public ABI contract.

# Examples

**Example 1** (Ch. 7): Platform-specific items visible in all documentation:
```rust
#[cfg(any(windows, doc))]
pub struct WindowsToken;
#[cfg(any(unix, doc))]
pub struct UnixToken;
```
> "Here, the respective tokens can only be used by dependent crates on their respective platforms, but they will both appear in documentation."

**Example 2** (Ch. 7): Limitation of cfg(doc) -- no per-platform compilation:
> "Rustdoc does not have a magic way to compile documentation 'as-if' you'd run it once for each platform... Instead, it sees *all* of your code at once, the same way the Rust compiler would if you passed it `--cfg doc`."

**Example 3** (Ch. 7): doc(alias) for search discoverability:
```rust
#[doc(alias = "x")]
#[doc(alias = "big")]
pub struct BigX;
```
> "Then, when looking for it through the `rustdoc` search, if you enter 'x' or 'big', search will show the `BigX` struct first."

**Example 4** (Ch. 6): Scraped examples from the examples/ directory:
```rust
// a_crate/src/lib.rs
pub fn a_func() {}
```
```rust
// a_crate/examples/ex.rs
fn main() {
    a_crate::a_func();
}
```
> "Then this code snippet will be included in the documentation for `a_func`. This documentation is inserted by Rustdoc and cannot be manually edited by the crate author."

**Example 5** (Ch. 6): Scraped examples display behavior:
> "For a given item, a maximum of 5 examples are included in the page. The remaining examples are just links to source code. Only one example is shown by default, and the remaining examples are hidden behind a toggle."

**Example 6** (Ch. 7): repr(transparent) display rules:
> "Rustdoc helpfully displays the attribute if and only if the non-1-ZST field is public and not `#[doc(hidden)]`."

# Relationships

## Builds Upon
- **rustdoc** -- these features extend basic documentation generation
- **rustdoc-search** -- `doc(alias)` and custom search engines integrate with the search feature

## Enables
- None directly -- these are advanced configuration options

## Related
- **rustdoc-cli** -- `--cfg` and `--target` flags interact with `#[cfg(doc)]`
- **rustdoc-lints** -- lints may interact with conditionally documented items
- **doc-attribute** -- `#[doc(alias)]` and `#[doc(cfg)]` are doc attributes
- **rustdoc-unstable** -- scraped examples are an unstable feature

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `#[cfg(doc)]` alone without the platform condition, making the item always invisible outside documentation.
  **Correction**: Use `#[cfg(any(platform_condition, doc))]` to preserve the item in both normal builds on the target platform and in documentation builds.

- **Error**: Expecting `#[cfg(doc)]` to be passed to doctests.
  **Correction**: "Please note that this `cfg` is not passed to doctests." Doctests run as normal Rust code and do not have the `doc` cfg set.

- **Error**: Expecting scraped examples to appear when the example file is not included by Cargo's `--examples` filter.
  **Correction**: "You should ensure that `cargo check --examples` includes your example file." Scraped examples only come from files Cargo recognizes as examples.

- **Error**: Using `#[cfg_attr(not(doc), repr(transparent))]` to hide representation from documentation.
  **Correction**: Due to current cross-crate limitations, this method "is not always guaranteed to work." Document the representation as private in prose instead.

# Common Confusions

- **Confusion**: Thinking `#[cfg(doc)]` provides per-platform documentation compilation.
  **Clarification**: Rustdoc sees all code at once "the same way the Rust compiler would if you passed it `--cfg doc`." It does not compile separately for each platform. Some invalid code may not produce errors because rustdoc does not run all compiler passes.

- **Confusion**: Thinking `#[doc(alias)]` changes the item's actual name or path.
  **Clarification**: Aliases only affect search results. The item's canonical name, path, and documentation remain unchanged. Aliases make items easier to find, not easier to reference in code.

- **Confusion**: Thinking scraped examples can be manually curated per-item.
  **Clarification**: "This documentation is inserted by Rustdoc and cannot be manually edited by the crate author." The selection is automatic based on size (smaller examples are preferred) and limited to 5 per item.

# Source Reference

Chapter 6: Scraped examples -- feature overview and configuration. Chapter 7: Advanced features -- `#[cfg(doc)]`, `#[doc(alias)]`, custom search engines, and `#[repr(...)]` display rules. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 7 -- "If you want to make sure an item is seen by Rustdoc regardless of what platform it's targeting, you can apply `#[cfg(doc)]` to it."
- Confidence rationale: HIGH -- each feature is documented with clear examples and explicit limitations
- Uncertainties: Scraped examples are an unstable feature and may change; repr display logic for edge cases with cfg_attr has known limitations
- Cross-reference status: rustdoc, rustdoc-search, rustdoc-cli, rustdoc-lints are in this extraction set; doc-attribute, rustdoc-unstable from Agent B
