---
# === CORE IDENTIFICATION ===
concept: Documentation Re-exports
slug: doc-reexports

# === CLASSIFICATION ===
category: documentation
subcategory: re-exports
tier: intermediate

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "Re-exports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "re-export documentation"
  - "doc(inline) re-exports"
  - "doc(no_inline) re-exports"
  - "inlining rules"
  - "pub use documentation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
  - doc-attribute
extends: []
related:
  - intra-doc-links
  - rustdoc-unstable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do re-exports appear in rustdoc-generated documentation?"
  - "When does rustdoc inline a re-exported item versus showing a Re-exports section?"
  - "What does #[doc(inline)] do on a pub use statement?"
  - "What does #[doc(no_inline)] do on a pub use statement?"
  - "How does #[doc(hidden)] interact with re-exports?"
  - "How are attributes handled when an item is inlined via re-export?"
  - "What are the automatic inlining rules for re-exports?"
  - "How do cfg attributes behave with re-export inlining?"
---

# Quick Definition

When an item is re-exported with `pub use`, rustdoc applies inlining rules to determine whether the item appears directly in the re-exporting module's docs (inlined) or as a link in a "Re-exports" section. Items from private modules are automatically inlined. `#[doc(inline)]` forces inlining, and `#[doc(no_inline)]` prevents it. In Rust 2018+, `pub use` of external dependencies is not eagerly inlined unless `#[doc(inline)]` is specified. When inlined, doc comments and most attributes (except `alias`, `inline`, `no_inline`, `hidden`) are merged from all re-export steps.

# Core Definition

Re-exports (`pub use`) allow items to appear at a different location in a crate's public API without moving the source code. Rustdoc must decide how to present these re-exports in the generated documentation, and it follows specific inlining rules:

**Automatic inlining occurs when:**
- The re-exported item comes from a private module (there is no page to link to)
- The item's parent module has `#[doc(hidden)]`

**Automatic non-inlining (Re-exports section) when:**
- The re-exported item comes from a public module (it has its own page)
- In Rust 2018+, when `pub use`-ing an external dependency

**Manual control:**
- `#[doc(inline)]` forces the item to appear as if defined at the re-export site
- `#[doc(no_inline)]` forces the item to appear only in the "Re-exports" section

When an item is inlined, its doc comments and most attributes are merged from all intermediate re-export steps. The attributes `#[doc(alias)]`, `#[doc(inline)]`, `#[doc(no_inline)]`, and `#[doc(hidden)]` are *not* inherited through inlining. Intra-doc links in merged documentation are resolved relative to where the doc comment was originally defined.

# Prerequisites

- **doc-comments** -- understanding documentation comments that are merged during inlining
- **doc-attribute** -- `#[doc(inline)]`, `#[doc(no_inline)]`, and `#[doc(hidden)]` control re-export behavior

# Key Properties

1. **Private module items are inlined**: If a `pub use` re-exports from a `mod` (not `pub mod`), the item is inlined because there is no page to link to.
2. **`#[doc(hidden)]` parent causes inlining**: If a module is `#[doc(hidden)]`, its public items are inlined when re-exported.
3. **`#[doc(hidden)]` on the item itself**: The re-export (and its hidden item) will not appear in docs, unless `#[doc(inline)]` is explicitly added.
4. **`#[doc(inline)]` forces inlining**: The re-exported item appears as if defined at the re-export site, even if the source module is public.
5. **`#[doc(no_inline)]` prevents inlining**: Only a "Re-exports" line appears, with no link if the source is private.
6. **Rust 2018+ external deps**: `pub use` of dependencies is not eagerly inlined unless `#[doc(inline)]` is added.
7. **Attribute merging on inline**: Doc comments and `cfg` attributes from all re-export steps are merged. `alias`, `inline`, `no_inline`, and `hidden` are *not* inherited.
8. **Glob re-exports merge attributes**: `pub use module::*` inherits attributes from both the glob and the original items.
9. **Non-glob re-exports do not merge cfg**: Without `#[doc(inline)]`, `cfg` attributes on the `pub use` line are *not* displayed.

# Construction / Recognition

## Automatic Inlining (Private Module):
```rust
mod private_mod {
    pub struct Public;
}
// Public appears in Structs section (inlined from private module)
pub use self::private_mod::Public;
```

## Forcing Inline:
```rust
pub mod public_mod {
    pub struct Public;
}
#[doc(inline)]
pub use self::public_mod::Public;
// Public appears in both crate root AND public_mod
```

## Preventing Inline:
```rust
mod private_mod {
    pub struct Public;
}
#[doc(no_inline)]
pub use self::private_mod::Public;
// Only a Re-exports line appears, no link
```

## Hidden Item with Inline Override:
```rust
#[doc(hidden)]
pub struct Hidden;

#[doc(inline)]
pub use self::Hidden as InlinedHidden;
// Re-export is visible but links to nothing
```

## Attribute Merging Example:
```rust
mod private_mod {
    /// First
    #[cfg(a)]
    pub struct InPrivate;
    /// Second
    #[cfg(b)]
    pub use self::InPrivate as Second;
}
/// Third
#[doc(inline)]
#[cfg(c)]
pub use self::private_mod::Second as Visible;
// Visible has docs "First Second Third" and cfg: #[cfg(a, b, c)]
```

# Context & Application

Re-export documentation is critical for crates that organize code in internal modules but present a flat public API (the "facade" pattern). Without understanding inlining rules, crate authors may find items missing from their docs or duplicated unexpectedly. The `#[doc(inline)]` attribute is commonly used to bring important items from sub-modules to the crate root's documentation, while `#[doc(no_inline)]` is used to keep the crate root clean when re-exporting many items.

# Examples

**Example 1** (Ch 4): Default behavior -- public module items appear as Re-exports:
```rust
pub use bar::Bar;
pub mod bar {
    pub struct Bar;
}
// Documentation shows "Re-exports: pub use bar::Bar;" with Bar linked to its page
```

**Example 2** (Ch 4): Inlining from a private module:
```rust
pub use bar::Bar;
mod bar {
    pub struct Bar;
}
// Bar appears in Structs section as if defined at crate root
```

**Example 3** (Ch 4): `#[doc(hidden)]` chaining:
```rust
mod private_mod {
    /// First
    pub struct InPrivate;
}
/// Second
#[doc(hidden)]
pub use self::private_mod::InPrivate as Hidden;
/// Third
pub use self::Hidden as Visible;
// Visible has docs "First Third" (Second is skipped because its re-export is hidden)
```

**Example 4** (Ch 4): Rust 2018 external dependency behavior:
> "In Rust 2018 and later, if you `pub use` one of your dependencies, `rustdoc` will not eagerly inline it as a module unless you add `#[doc(inline)]`."

# Relationships

## Builds Upon
- **doc-comments** -- doc comments on re-exports are merged with the original item's docs
- **doc-attribute** -- `#[doc(inline)]`, `#[doc(no_inline)]`, `#[doc(hidden)]` control re-export presentation

## Enables
- Nothing directly -- re-export documentation is a presentation concern

## Related
- **intra-doc-links** -- links in re-exported documentation resolve in the original module's scope
- **rustdoc-unstable** -- `#[doc(cfg)]` has special merge rules for re-exports with/without `#[doc(inline)]`

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Expecting `pub use dep::Item` to inline the dependency's documentation in Rust 2018+.
  **Correction**: External dependencies are not eagerly inlined since Rust 2018. Add `#[doc(inline)]` explicitly if you want inlining.

- **Error**: Adding `#[doc(no_inline)]` on a re-export from a private module, then expecting a working link.
  **Correction**: `no_inline` shows a "Re-exports" line, but if the source module is private, there is no page to link to. The item name will appear without a hyperlink.

- **Error**: Expecting `cfg` attributes on a non-inlined `pub use` to be displayed.
  **Correction**: Without `#[doc(inline)]`, `cfg` attributes on the `pub use` line are not displayed. Only inlined re-exports merge `cfg` attributes.

# Common Confusions

- **Confusion**: Thinking `#[doc(inline)]` changes the item's actual module path.
  **Clarification**: `#[doc(inline)]` only affects documentation presentation. The item's real module path is unchanged. Users can still import from the original location.

- **Confusion**: Thinking `#[doc(hidden)]` on a re-export hides the original item from all documentation.
  **Clarification**: `#[doc(hidden)]` on a re-export only hides *that specific re-export*. Other re-exports of the same item remain visible, and the original item's documentation is unaffected.

- **Confusion**: Thinking attribute merging replaces attributes.
  **Clarification**: Attributes from all re-export steps are *accumulated*, not replaced. If item has `#[cfg(a)]` and re-export has `#[cfg(c)]`, the inlined result has both `cfg(a)` and `cfg(c)`.

# Source Reference

Chapter 4: How to Write Documentation; section "Re-exports" covering inlining rules, `#[doc(inline)]`, `#[doc(no_inline)]`, `#[doc(hidden)]` interaction, and attribute merging. Also from "The #[doc] attribute" section on `inline` and `no_inline`. Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- "If a public item comes from a private module, it will be inlined" and the detailed rules for attribute inheritance
- Confidence rationale: HIGH -- the source provides comprehensive inlining rules with multiple examples covering edge cases
- Uncertainties: None significant -- the inlining rules are clearly specified
- Cross-reference status: doc-comments, doc-attribute, intra-doc-links, rustdoc-unstable are in this extraction set
