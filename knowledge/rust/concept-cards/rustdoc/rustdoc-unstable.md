---
# === CORE IDENTIFICATION ===
concept: Rustdoc Unstable Features
slug: rustdoc-unstable

# === CLASSIFICATION ===
category: documentation
subcategory: nightly-features
tier: advanced

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "Unstable features"
chapter_number: 8
pdf_page: null
section: "All sections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "nightly rustdoc features"
  - "doc_auto_cfg"
  - "doc_cfg"
  - "doc_notable_trait"
  - "doc_masked"
  - "rustdoc nightly"
  - "unstable rustdoc flags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
extends: []
related:
  - doc-comments
  - doc-tests
  - doc-reexports
  - rustdoc-cli
  - rustdoc-advanced-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What rustdoc features are only available on nightly?"
  - "How do I show platform/feature availability markers in docs?"
  - "What is doc(auto_cfg) and how does it work?"
  - "How do I add my trait to the Notable Traits dialog?"
  - "How do I hide certain dependencies from documentation?"
  - "What unstable command-line flags does rustdoc support?"
  - "How does doc test merging work with --merge?"
  - "How do I get JSON output from rustdoc?"
  - "How do I measure documentation coverage?"
  - "What is the doc(cfg) attribute for?"
---

# Quick Definition

Rustdoc has numerous unstable features available only on nightly Rust, covering three categories: nightly-gated functionality (no feature flag needed), `#[doc]` attribute extensions (require `#![feature(...)]`), and unstable command-line arguments (require `-Z unstable-options`). Key features include `doc(auto_cfg)` / `doc(cfg(...))` for platform/feature availability markers, `doc(notable_trait)` for highlighting important trait implementations, `--show-coverage` for documentation coverage metrics, `--output-format json` for machine-readable documentation, and `--merge` options for faster cross-crate documentation builds.

# Core Definition

Rustdoc's unstable features fall into three categories:

**Nightly-gated functionality** (no feature flag needed):
- Error numbers for `compile_fail` doctests (e.g., `` ```compile_fail,E0044 ``)
- `missing_doc_code_examples` lint

**`#[doc]` attribute extensions** (require `#![feature(...)]`):
- **`doc(notable_trait)`**: Adds a trait to the "Notable traits" dialog (tracking #45040). Applied to traits like `Iterator`, `Future`, `io::Read`, `io::Write` in std.
- **`doc(masked)`**: Hides types from dependency crates in trait implementation lists (tracking #44027). Internal use.
- **`doc(keyword = "...")`** and **`doc(attribute = "...")`**: For documenting language keywords and built-in attributes in the standard library. Internal use.
- **`doc(cfg(...))` and `doc(auto_cfg)`**: The most significant unstable feature -- displays visual markers showing under which conditions an item is available.

**`doc(cfg)` and `doc(auto_cfg)` system:**
- `#[doc(auto_cfg)]` (enabled by default at crate level): Automatically displays `cfg(...)` compatibility information derived from `#[cfg]` attributes.
- `#[doc(cfg(...))]`: Manually specifies availability information, overriding `auto_cfg`. Only affects documentation display, not compilation.
- `#[doc(auto_cfg(hide(...)))]`: Prevents specific cfgs from appearing in markers (e.g., hide `unix` from all docs).
- `#[doc(auto_cfg(show(...)))]`: Reverses a `hide(...)` for a specific item and its descendants.
- `#[doc(auto_cfg = false)]`: Disables automatic cfg display for an item and descendants.
- Cfg attributes are inherited from parent modules to children, and merged logically (e.g., "Available on (Windows or Unix) and non-Unix only").

**Unstable command-line arguments** (require `-Z unstable-options`):
- `--merge`, `--parts-out-dir`, `--include-parts-dir`: Control cross-crate documentation merging. Default `--merge=shared` is O(n^2); `--merge=none` + `--merge=finalize` is O(n).
- `--document-hidden-items`: Shows `#[doc(hidden)]` items with a ghost icon.
- `--show-coverage`: Reports percentage of documented public items.
- `--output-format json`: Emits machine-readable JSON documentation.
- `--output-format doctest`: Emits JSON metadata about doctests.
- `--show-type-layout`: Adds memory layout information to type docs.
- `--with-examples` / `--scrape-examples-*`: Shows usage examples from reverse dependencies (RFC 3123).
- `--generate-link-to-definition`: Adds clickable links in source code pages.
- `--persist-doctests`: Keeps compiled doctest binaries after testing.
- `--check`: Type-checks and lints without generating documentation.
- `--no-capture`: Shows doctest stdout/stderr directly in terminal.
- `--doctest-build-arg`: Passes additional arguments to rustc when compiling doctests.

# Prerequisites

- **doc-attribute** -- unstable features extend the `#[doc]` attribute system

# Key Properties

1. **Three activation mechanisms**: Some features are nightly-gated only, some need `#![feature(...)]`, some need `-Z unstable-options`
2. **`doc(auto_cfg)` is on by default**: When enabled, `#[cfg(feature = "foo")]` automatically generates "Available on feature = foo" markers
3. **`doc(cfg)` overrides `auto_cfg`**: Manual `doc(cfg(...))` takes precedence over automatic detection
4. **`auto_cfg(hide/show)` is inherited**: Applies to the item and all descendants, can be overridden by children
5. **Cfg inheritance merges logically**: Parent `cfg(any(windows, unix))` + child `cfg(not(unix))` = "Available on (Windows or Unix) and non-Unix only"
6. **Re-export cfg merging rules**: Cfgs only merge when `#[doc(inline)]` is present; non-inlined re-exports show only their own cfgs
7. **`--merge=finalize` for O(n) builds**: Defers shared-data merging to the last crate, avoiding O(n^2) work in multi-crate docs
8. **`--show-coverage` methodology**: Counts only public items (unless `--document-private-items`), excludes fields/variants/modules/impl blocks by default, supports JSON output
9. **`doc(notable_trait)` marker**: Applied to "fundamental" traits whose implementations are the primary interface for their types

# Construction / Recognition

## `doc(cfg)` for Manual Availability Markers:
```rust
#[cfg(feature = "futures-io")]
#[doc(cfg(feature = "futures-io"))]
pub mod futures {}
// Displays: "This is supported on feature="futures-io" only."
```

## `doc(auto_cfg)` with Hidden Cfgs:
```rust
#![doc(auto_cfg(hide(unix)))]  // Never show "unix" in cfg markers

#[cfg(any(unix, feature = "futures-io"))]
pub mod futures {}  // Only shows feature="futures-io"
```

## Notable Trait:
```rust
#![feature(doc_notable_trait)]

#[doc(notable_trait)]
pub trait MyIterator { /* ... */ }
// Functions returning impl MyIterator get a "Notable traits" button
```

## Documentation Coverage:
```bash
$ rustdoc src/lib.rs -Z unstable-options --show-coverage
+-------------------------------------+------------+------------+
| File                                | Documented | Percentage |
+-------------------------------------+------------+------------+
| lib.rs                              |          4 |     100.0% |
+-------------------------------------+------------+------------+
```

## O(n) Cross-Crate Documentation Build:
```bash
$ rustdoc +nightly crate1.rs --merge=none --parts-out-dir=crate1.d -Zunstable-options
$ rustdoc +nightly crate2.rs --merge=finalize --include-parts-dir=crate1.d -Zunstable-options
```

# Context & Application

These unstable features are primarily used by the Rust standard library team, large crate ecosystems with complex feature flags (like `tokio`, `serde`), and documentation tooling. The `doc(cfg)` / `doc(auto_cfg)` system is the most widely anticipated feature, as it lets users of feature-gated crates see at a glance which items require which features or platforms. The `--show-coverage` flag is useful for CI pipelines enforcing documentation standards. The `--output-format json` enables third-party documentation tools and analysis.

# Examples

**Example 1** (Ch 8): `doc(cfg)` for manual platform markers:
```rust
#[cfg(feature = "futures-io")]
#[doc(cfg(feature = "futures-io"))]
pub mod futures {}
```
> "It will display in the documentation for this module: This is supported on feature='futures-io' only."

**Example 2** (Ch 8): `auto_cfg(hide)` to suppress noisy cfgs:
```rust
#![doc(auto_cfg(hide(unix)))]
// #[cfg(unix)] -> nothing displayed
// #[cfg(any(unix, windows))] -> only "windows" displayed
// #[cfg(feature = "unix")] -> "feature = unix" still displayed (different from cfg)
```

**Example 3** (Ch 8): Cfg inheritance with logical merging:
```rust
#[doc(cfg(any(windows, unix)))]
pub mod desktop {
    #[doc(cfg(not(unix)))]
    pub mod non_unix { }
}
// Displays: "Available on (Windows or Unix) and non-Unix only."
```

**Example 4** (Ch 8): The `--merge` optimization for large documentation builds:
> "Default `--merge=shared` is O(crates^2) work. Using `--merge=none` on every crate except the last (`--merge=finalize`) reduces to O(crates) work."

# Relationships

## Builds Upon
- **doc-attribute** -- all `#[doc(...)]` extensions build on the stable attribute system

## Enables
- Nothing directly -- these are experimental features that may eventually stabilize

## Related
- **doc-comments** -- unstable features affect how doc comments are processed and displayed
- **doc-tests** -- error numbers for `compile_fail`, `--persist-doctests`, `--no-capture`, `--doctest-build-arg`
- **doc-reexports** -- cfg merging has special rules for inlined vs. non-inlined re-exports
- **rustdoc-cli** -- many unstable features are command-line flags
- **rustdoc-advanced-features** -- some unstable features relate to advanced output options

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Using `#[doc(cfg(...))]` and expecting it to affect compilation.
  **Correction**: `doc(cfg)` only affects documentation display. "This means `#[doc(cfg(not(windows)))]` will not cause your docs to be hidden on non-windows targets, even though `#[cfg(not(windows))]` does do that."

- **Error**: Using `doc(auto_cfg = false)` and `doc(auto_cfg(hide(...)))` on the same item.
  **Correction**: This is an error. `doc(auto_cfg = ...)` enables/disables the feature, while `doc(auto_cfg(...))` enables it unconditionally. They conflict when on the same item.

- **Error**: Expecting `--show-coverage` to count struct fields, enum variants, or trait impl items.
  **Correction**: These items are excluded from the coverage count by default. Only items with code examples are counted if they appear.

# Common Confusions

- **Confusion**: Thinking `doc(auto_cfg(hide(unix)))` also hides `feature = "unix"`.
  **Clarification**: `hide(unix)` only hides the `unix` cfg identifier. `cfg(feature = "unix")` is a feature flag, not the `unix` cfg, so it is still displayed.

- **Confusion**: Thinking all unstable features require `#![feature(...)]`.
  **Clarification**: There are three activation mechanisms: nightly-gated (just use nightly), feature-gated (`#![feature(...)]`), and command-line (`-Z unstable-options`). Each feature uses only one.

- **Confusion**: Thinking `doc(cfg)` on a re-export automatically merges with the re-exported item's cfg.
  **Clarification**: Cfg merging only happens when `#[doc(inline)]` is present. Without inline, re-exports show only their own cfg, and the re-exported item shows only its own.

# Source Reference

Chapter 8: Unstable features; all sections covering nightly-gated functionality, `#[doc]` attribute extensions, effects of other nightly features, and unstable command-line arguments. Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 8 -- comprehensive coverage of all unstable rustdoc features with tracking issues
- Confidence rationale: HIGH -- the source provides detailed specifications with examples, though features may change before stabilization
- Uncertainties: All features are unstable and subject to change. `doc(cfg)` / `doc(auto_cfg)` is the most mature. Some features (keyword, attribute, rust_logo) are compiler-internal only.
- Cross-reference status: doc-attribute, doc-tests, doc-reexports, doc-comments, rustdoc-cli, rustdoc-advanced-features are in this extraction set or referenced
