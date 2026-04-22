---
concept: Rustfmt Style Edition 2024
slug: rustfmt-style-edition
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "style edition"
  - "rustfmt 2024"
  - "style_edition"
  - "rustfmt formatting changes 2024"
  - "version sorting rustfmt"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "What is a style edition in rustfmt?"
  - "How do I control the formatting style edition?"
  - "What formatting changes did rustfmt make in 2024?"
  - "What is version sorting in rustfmt?"
  - "How does raw identifier sorting work in rustfmt 2024?"
---

# Quick Definition

Rust 2024 introduces the "style edition" concept (RFC 3338), allowing `rustfmt` to evolve formatting rules across editions without breaking stability guarantees. The 2024 style edition includes formatting fixes (comment alignment, indentation, wrapping), corrected raw identifier sorting, and version-sort-based ordering that handles numeric suffixes more intuitively.

# Core Definition

**Style edition concept (RFC 3338):** Previously, Rustfmt's formatting stability guarantee (newer versions cannot change already-formatted output) prevented both the Style Guide and Rustfmt from evolving. RFC 3338 resolved this by aligning the Rust Style Guide to the edition model. Users can now specify a style edition independently from the parsing edition, allowing formatting to evolve without breaking existing CI pipelines.

By default, `rustfmt` uses the same style edition as the Rust edition. The style edition can be overridden:
- Via `Cargo.toml`: `edition = "2024"` implies style edition 2024
- Via `rustfmt.toml`: `style_edition = "2024"`
- Via CLI: `rustfmt --style-edition 2024`
- Via CLI (both parsing and style): `rustfmt --edition 2024`

**Formatting fixes in 2024:** The 2024 style edition corrects multiple long-standing formatting issues:
- Unrelated trailing comments after items are no longer indented to align with the previous item's trailing comment
- Strings in comments are no longer incorrectly formatted
- Long strings no longer prevent expressions from being formatted
- Generics in `impl` blocks use correct indentation (no more double-indent)
- Complex `fn` signatures get correct indentation
- Nested tuple indexing no longer has an extra space (`((1,),).0.0` not `((1,),).0 .0`)
- `return`/`break`/`continue` in match arm blocks properly end with semicolons
- Long array and slice patterns are properly wrapped
- Macro metavariable expressions are preserved without adding extra spaces
- `let-else` statements and `async` closures format correctly
- `where` clause formatting improvements

**Raw identifier sorting:** The `r#` prefix is now stripped before sorting, so `r#async` sorts under "a" not "r".

**Version sorting:** The sorting algorithm changes from ASCIIbetical to a version-sort-like algorithm. This means `NonZeroU8` sorts before `NonZeroU16` (numeric comparison), and lowercase sorts after uppercase within each group (`self` sorts after `Read`).

# Prerequisites

- **Rust editions** -- understanding the edition mechanism that enables style evolution

# Key Properties

1. The style edition concept allows formatting rules to evolve across editions
2. Style edition defaults to the Rust edition but can be overridden
3. The 2024 style edition includes ~15 formatting fixes accumulated over years
4. Raw identifiers now sort by their underlying identifier, not the `r#` prefix
5. Version sorting uses numeric comparison for digit sequences (NonZeroU8 < NonZeroU16)
6. Version sorting uses Unicode lexicographic comparison for non-digit characters
7. Running `cargo fmt` with edition 2024 automatically applies all formatting changes
8. Projects should add `style_edition` to `rustfmt.toml` for editor format-on-save consistency
9. The stability guarantee now applies per style edition, not globally

# Construction / Recognition

## Configuring Style Edition:

In `rustfmt.toml`:

```toml
style_edition = "2024"
```

CLI options:

```sh
cargo fmt                             # uses edition from Cargo.toml
rustfmt lib.rs --edition 2024        # both parsing and style
rustfmt lib.rs --style-edition 2024  # style only
```

## Version Sorting Example:

```rust
// 2021 (ASCIIbetical -- uppercase before lowercase, digits by character):
use std::io::{self, stdout, Read, Write};
use std::num::{NonZeroU16, NonZeroU32, NonZeroU64, NonZeroU8};

// 2024 (version sort -- numeric comparison, more intuitive):
use std::io::{self, Read, Write, stdout};
use std::num::{NonZeroU8, NonZeroU16, NonZeroU32, NonZeroU64};
```

## Raw Identifier Sorting Example:

```rust
// 2021 (r# prefix affects sort -- sorts under "r"):
use websocket::client::ClientBuilder;
use websocket::r#async::futures::Stream;
use websocket::result::WebSocketError;

// 2024 (r# stripped for sorting -- sorts under "a"):
use websocket::r#async::futures::Stream;
use websocket::client::ClientBuilder;
use websocket::result::WebSocketError;
```

## Formatting Fix Example (comment alignment):

```rust
// 2021: following comments aligned to trailing comment
pub const IFF_MULTICAST: ::c_int = 0x0000000800; // Supports multicast
                                                 // Multicast using broadcst. add.
// 2024: following comments at normal indentation
pub const IFF_MULTICAST: ::c_int = 0x0000000800; // Supports multicast
// Multicast using broadcst. add.
```

# Context & Application

The style edition concept is a significant infrastructure improvement. Before RFC 3338, Rustfmt was trapped: it could not fix known formatting bugs without breaking its stability guarantee. The style edition mechanism releases this pressure by scoping the guarantee to each style edition.

For teams, the key migration consideration is editor consistency. Many editors run `rustfmt` directly (defaulting to 2015 style) while `cargo fmt` uses the project's edition. Adding a `rustfmt.toml` with `style_edition = "2024"` ensures both paths produce identical output. Without this, developers may see formatting flip-flop between editor saves and CI runs.

The version sorting change is the most visibly impactful: it reorders imports project-wide. While semantically meaningless, it creates large diffs on the first format pass. Plan for a dedicated formatting commit when adopting the 2024 style edition.

# Examples

**Example 1** (nested tuple access fix): `((1,),).0 .0` becomes `((1,),).0.0` -- the extra space is removed.

**Example 2** (impl generics indentation): Generic parameters in `impl` blocks drop from double-indentation to single-indentation, matching other contexts.

**Example 3** (version sorting): `use std::num::{NonZeroU16, NonZeroU32, NonZeroU64, NonZeroU8}` becomes `use std::num::{NonZeroU8, NonZeroU16, NonZeroU32, NonZeroU64}` -- sorted numerically.

# Relationships

## Related
- **rust-2024-edition** -- the style edition is a new concept introduced in the 2024 edition

# Common Errors

- **Error**: Not adding `style_edition = "2024"` to `rustfmt.toml`, causing editor format-on-save to use the default 2015 style while `cargo fmt` uses 2024.
  **Correction**: Add `style_edition = "2024"` to your project's `rustfmt.toml` to ensure consistent formatting across all invocation methods.

- **Error**: Applying the 2024 style edition formatting mixed into a feature branch, making the diff hard to review.
  **Correction**: Apply formatting changes in a dedicated commit separate from functional changes.

# Common Confusions

- **Confusion**: Thinking the style edition must match the Rust edition.
  **Clarification**: The style edition can be set independently. You can use `edition = "2021"` for parsing with `style_edition = "2024"` for formatting, or vice versa.

- **Confusion**: Thinking Rustfmt's stability guarantee is gone.
  **Clarification**: The stability guarantee still holds within each style edition. Upgrading Rustfmt will not change output as long as you stay on the same style edition. The guarantee only "resets" when you change the style edition.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Four sections under "Rustfmt": "Rustfmt: Style edition" (RFC 3338, the concept and configuration), "Rustfmt: Formatting fixes" (~650 lines of detailed formatting change examples), "Rustfmt: Raw identifier sorting," and "Rustfmt: Version sorting." The formatting fixes section documents approximately 15 individual fixes with before/after examples.

# Verification Notes

- Style edition concept: from "Rustfmt: Style edition" section, RFC 3338
- Configuration methods: all four methods from the source text
- Formatting fixes: surveyed from ~15 subsections in "Formatting fixes"
- Version sorting algorithm: from "Version sorting" section
- Raw identifier sorting: from "Raw identifier sorting" section
- Editor consistency recommendation: directly from the "Migration" subsection
- Confidence: HIGH -- all information directly from the edition guide
- Cross-references: slugs verified against this extraction set
