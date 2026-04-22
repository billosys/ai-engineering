---
concept: Diagnostic Items (Identifying Standard Library Types and Traits)
slug: diagnostic-item
category: lint-development
subcategory: type-identification
tier: advanced
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "04-advanced-linting"
chapter_number: 4
pdf_page: null
section: "Using Diagnostic Items"
extraction_confidence: high
aliases:
  - "diagnostic items"
  - "diagnostic item"
  - "get_diagnostic_item"
  - "is_diag_item"
  - "lang items"
  - "lang_items"
prerequisites:
  - late-context
  - ty-type-and-kind
extends: []
related:
  - trait-checking
  - clippy-utils
  - clippy
contrasts_with: []
answers_questions:
  - "How do I check if a type is Option, Vec, String, or another standard library type?"
  - "What are diagnostic items and how do they differ from lang items?"
  - "How do I get the DefId of a standard library trait?"
  - "When should I use diagnostic items vs lang items vs type paths?"
---

# Quick Definition

Diagnostic items are compiler-assigned `Symbol` identifiers for standard library types and traits (like `Iterator`, `Option`, `String`) that allow lints to reliably identify these types via `cx.tcx.get_diagnostic_item(sym::Name)` without relying on fragile path-based matching. Lang items serve a similar purpose for core language types.

# Core Definition

The Clippy documentation introduces diagnostic items through the trait checking use case: "As explained in the Rust Compiler Development Guide, diagnostic items are introduced for identifying types via Symbols." (Ch. 4, "Using Diagnostic Items")

Chapter 5 demonstrates the three-tier approach: diagnostic items (preferred), lang items, and type paths (fallback). For type checking: "There are three ways to check if an expression type is a specific type we want to check for." (Ch. 5, "Checking for a specific type")

For trait identification, the same hierarchy applies: "There are three ways to do this, depending on if the target trait has a diagnostic item, lang item or neither." (Ch. 5, "Checking if a type implements a specific trait")

The documentation explicitly recommends diagnostic items as the preferred approach and notes that the type path approach "should be avoided if possible, the best thing to do would be to make a PR to `rust-lang/rust` adding a diagnostic item." (Ch. 4, "Using Type Path")

# Prerequisites

- **LateContext** — diagnostic items are accessed through `cx.tcx.get_diagnostic_item(...)` and lang items through `cx.tcx.lang_items()`
- **Ty type and kind** — diagnostic item checks operate on `Ty` values; understanding the type system is necessary to use the results

# Key Properties

1. Diagnostic items use `Symbol`s (from `clippy_utils::sym` or `rustc_span::sym`) to identify types and traits
2. `cx.tcx.get_diagnostic_item(sym::Name)` returns `Option<DefId>` for the named type or trait
3. Lang items are accessed via `cx.tcx.lang_items()` and have specific methods like `drop_trait()`, `eq_trait()`
4. Lang items cover core language types (`Drop`, `Copy`, `Clone`, `Eq`, `PartialEq`, `RangeFull`, etc.)
5. Diagnostic items cover a broader range of standard library types (`Iterator`, `Option`, `String`, `Vec`, `HashMap`, etc.)
6. `clippy_utils::paths` provides a fallback for types that have neither diagnostic items nor lang items
7. For type checking: `ty.is_diag_item(cx, sym::Option)` and `ty.is_lang_item(cx, LangItem::RangeFull)`
8. For trait checking: get the `DefId` via diagnostic/lang items, then pass to `implements_trait`

# Construction / Recognition

## To Check if a Type Is a Specific Standard Library Type (Ch. 5)

1. **Diagnostic item** (preferred): `ty.is_diag_item(cx, sym::Option)`
2. **Lang item**: `ty.is_lang_item(cx, LangItem::RangeFull)`
3. **Type path** (fallback): `paths::RESULT.matches_ty(cx, ty)`

## To Get a Trait's DefId for Trait Checking

1. **Diagnostic item** (preferred): `cx.tcx.get_diagnostic_item(sym::Iterator)`
2. **Lang item**: `cx.tcx.lang_items().drop_trait()`
3. **Type path** (fallback): `paths::ITER_STEP.first(cx)`

## To Discover Available Symbols

1. Check `rustc_span::sym` for compiler-defined symbols
2. Check `clippy_utils::sym` for Clippy-specific symbols
3. Refer to the [symbol index](https://doc.rust-lang.org/beta/nightly-rustc/rustc_span/symbol/sym/index.html) for the full list

# Context & Application

Diagnostic items and lang items are the canonical way to identify specific standard library types and traits in Clippy lints. Rather than matching on string paths (which can break with internal reorganizations), diagnostic items provide stable, symbolic identifiers maintained by the compiler itself.

The three-tier hierarchy (diagnostic items > lang items > paths) reflects the Clippy project's preference for stability and maintainability. When a lint needs to identify `Option`, `Vec`, `Iterator`, or other well-known types, diagnostic items should always be the first choice.

# Examples

**Checking for a specific type using diagnostic items** (Ch. 5, "Checking for a specific type"):
```rust
use clippy_utils::{paths, sym};
use clippy_utils::res::MaybeDef;
use rustc_hir::LangItem;

impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);

        // 1. Using diagnostic items
        if ty.is_diag_item(cx, sym::Option) {
            // The type is an `Option`
        }

        // 2. Using lang items
        if ty.is_lang_item(cx, LangItem::RangeFull) {
            // The type is a full range like `.drain(..)`
        }

        // 3. Using the type path (avoid if possible)
        if paths::RESULT.matches_ty(cx, ty) {
            // The type is a `core::result::Result`
        }
    }
}
```

**Getting a trait DefId for Iterator via diagnostic item** (Ch. 4, "Using Diagnostic Items"):
```rust
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;

let implements_iterator = (cx.tcx.get_diagnostic_item(sym::Iterator))
    .is_some_and(|id| implements_trait(cx, cx.typeck_results().expr_ty(expr), id, &[]));
```

**Getting Drop trait via lang items** (Ch. 4, "Using Lang Items"):
```rust
let ty = cx.typeck_results().expr_ty(expr);
if cx.tcx.lang_items()
    .drop_trait()
    .map_or(false, |id| implements_trait(cx, ty, id, &[])) {
        println!("`expr` implements `Drop` trait!");
    }
```

# Relationships

## Builds Upon
- **LateContext** — diagnostic items and lang items are accessed through `cx.tcx`
- **Ty type and kind** — diagnostic item checks operate on resolved `Ty` values

## Enables
- **Trait checking** — trait `DefId`s obtained via diagnostic items are passed to `implements_trait`

## Related
- **Clippy utils** — `clippy_utils::sym` extends the available symbols; `clippy_utils::paths` provides fallback path-based matching
- **Clippy** — user-facing Clippy relies on diagnostic items internally to identify types for lints

# Common Errors

- **Error**: Using `paths::*` for types that have diagnostic items.
  **Correction**: "This approach should be avoided if possible, the best thing to do would be to make a PR to `rust-lang/rust` adding a diagnostic item." (Ch. 4) Always check for a diagnostic item or lang item first.

- **Error**: Forgetting to handle the `None` case from `get_diagnostic_item`.
  **Correction**: `get_diagnostic_item` returns `Option<DefId>`. Always handle `None` gracefully (e.g., with `is_some_and` or `map_or(false, ...)`). A diagnostic item might not exist in all compilation contexts.

# Common Confusions

- **Confusion**: Diagnostic items and lang items are the same thing.
  **Clarification**: Lang items are a smaller, more foundational set of items the compiler itself needs to function (e.g., `Drop`, `Copy`, `Eq`, `PartialEq`, range types). Diagnostic items are a broader set intended for diagnostics and tooling, covering more of the standard library (e.g., `Iterator`, `Option`, `String`, `Vec`). Both provide `DefId`s, but they are accessed through different APIs.

- **Confusion**: Thinking new symbols can be used without registration.
  **Clarification**: "New symbols such as `our_fancy_method` need to be added to the `clippy_utils::sym` module. This module extends the list of symbols already provided by the compiler crates in `rustc_span::sym`." (Ch. 4, "Method Checking")

# Source Reference

Chapter 4: "Trait Checking," sections "Using Diagnostic Items," "Using Lang Items," and "Using Type Path." Chapter 5: "Common tools for writing lints," sections "Checking for a specific type" and "Checking if a type implements a specific trait."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 and Ch. 5 of the Clippy documentation
- Confidence rationale: HIGH — both chapters provide clear explanations and code examples for all three identification approaches with explicit preference ordering
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (clippy) and within this card set (late-context, ty-type-and-kind, trait-checking, clippy-utils)
