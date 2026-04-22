---
concept: "clippy_utils (Helper Utilities for Lint Operations)"
slug: clippy-utils
category: lint-development
subcategory: utility-crate
tier: intermediate
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "05-common-tools"
chapter_number: 5
pdf_page: null
section: "Common tools for writing lints"
extraction_confidence: high
aliases:
  - "clippy_utils"
  - "clippy utils"
  - "Clippy utilities"
  - "clippy_utils::ty"
  - "clippy_utils::sym"
  - "clippy_utils::paths"
prerequisites:
  - late-lint-pass
  - late-context
extends: []
related:
  - ty-type-and-kind
  - trait-checking
  - diagnostic-item
  - macro-handling
  - adding-a-lint
contrasts_with: []
answers_questions:
  - "What utilities does clippy_utils provide for lint development?"
  - "How do I check if an expression calls a specific method?"
  - "How do I check if an impl block defines a method?"
  - "Where do I find path definitions for type matching in Clippy?"
  - "How do I add new symbols for method name matching?"
---

# Quick Definition

`clippy_utils` is Clippy's utility crate providing helper functions and modules for common lint operations, including `clippy_utils::ty` (type utilities like `implements_trait`), `clippy_utils::sym` (symbol definitions), `clippy_utils::paths` (type path definitions), and `clippy_utils::res` (resolution helpers like `MaybeDef`, `MaybeTypeckRes`).

# Core Definition

Chapter 5 of the Clippy documentation is organized entirely around the common tools and patterns provided by `clippy_utils` and related compiler APIs. These utilities cover the recurring operations lint authors need: retrieving expression types, checking method calls, identifying specific types, verifying trait implementations, checking method definitions, and handling macros.

The key modules and utilities documented across Chapters 4 and 5 include:

- `clippy_utils::ty::implements_trait` — checks if a type implements a specific trait
- `clippy_utils::sym` — extends `rustc_span::sym` with Clippy-specific symbols for method and type names
- `clippy_utils::paths` — provides path definitions for types lacking diagnostic items (e.g., `paths::RESULT`, `paths::ITER_STEP`)
- `clippy_utils::res::MaybeDef` and `MaybeTypeckRes` — resolution helpers for checking method ownership
- `clippy_utils::return_ty` — retrieves the return type of an `ImplItem`
- `clippy_utils::is_from_proc_macro` — detects proc macro-generated code

# Prerequisites

- **LateLintPass** — most `clippy_utils` functions operate in the context of a late lint pass
- **LateContext** — many utility functions accept `cx: &LateContext` as their first parameter

# Key Properties

1. `clippy_utils::ty::implements_trait(cx, ty, trait_def_id, generic_args)` is the standard way to check trait implementations
2. `clippy_utils::sym` defines symbols for method names, type names, and other identifiers used in pattern matching; it extends `rustc_span::sym`
3. "New symbols such as `our_fancy_method` need to be added to the `clippy_utils::sym` module" (Ch. 4, "Method Checking")
4. `clippy_utils::paths` provides fallback type path matching for types without diagnostic items; "This approach should be avoided if possible" (Ch. 4, "Using Type Path")
5. `clippy_utils::res::MaybeDef` enables checking which trait a method belongs to: `cx.ty_based_def(expr).opt_parent(cx).is_diag_item(cx, sym::OurFancyTrait)` (Ch. 4, "Method Checking")
6. `clippy_utils::return_ty(cx, impl_item.hir_id)` retrieves the return type of an impl method
7. `clippy_utils::is_from_proc_macro(cx, node)` approximates whether code comes from a proc macro

# Construction / Recognition

## Method Call Checking (Ch. 4 & 5)

1. Pattern match `expr.kind` against `hir::ExprKind::MethodCall(path, _, _, _)`
2. Check method name: `path.ident.name == sym::method_name`
3. Optionally verify the owning trait: `cx.ty_based_def(expr).opt_parent(cx).is_diag_item(cx, sym::TraitName)`

## Method Definition Checking (Ch. 4 & 5)

1. Implement `check_impl_item` in `LateLintPass`
2. Match `impl_item.kind` against `ImplItemKind::Fn(ref signature, _)`
3. Check method name: `impl_item.ident.name.as_str() == "method_name"` or `impl_item.ident.name == sym::method_name`
4. Optionally check self parameter: `signature.decl.implicit_self.has_implicit_self()`
5. Optionally check return type: `return_ty(cx, impl_item.hir_id).is_diag_item(cx, sym::String)`

# Context & Application

`clippy_utils` is the practical toolkit that makes lint development manageable. Without it, every lint would need to reimplement common patterns like trait checking, type identification, and method resolution. The crate encapsulates best practices and provides type-safe, idiomatic utilities.

Chapter 5 serves as a practical quick-reference for these utilities, while Chapter 4 provides deeper explanations. Together they form the essential reference for Clippy lint authors.

# Examples

**Checking if an expression calls a specific method** (Ch. 4, "Checking if an expr is calling a specific method"):
```rust
use rustc_hir as hir;
use clippy_utils::res::{MaybeDef, MaybeTypeckRes};
use clippy_utils::sym;

impl<'tcx> LateLintPass<'tcx> for OurFancyMethodLint {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx hir::Expr<'_>) {
        if let hir::ExprKind::MethodCall(path, _, _, _) = &expr.kind
            && path.ident.name == sym::our_fancy_method
            // Check if the method belongs to the expected trait
            && cx.ty_based_def(expr).opt_parent(cx).is_diag_item(cx, sym::OurFancyTrait)
        {
            println!("`expr` is a method call for `our_fancy_method`");
        }
    }
}
```

**Checking if an impl block defines a method** (Ch. 4, "Checking if a impl block implements a method"):
```rust
use clippy_utils::{return_ty, sym};
use clippy_utils::res::MaybeDef;
use rustc_hir::{ImplItem, ImplItemKind};

impl<'tcx> LateLintPass<'tcx> for MyTypeImpl {
    fn check_impl_item(&mut self, cx: &LateContext<'tcx>, impl_item: &'tcx ImplItem<'_>) {
        if let ImplItemKind::Fn(ref signature, _) = impl_item.kind
            && impl_item.ident.name.as_str() == "our_fancy_method"
            && signature.decl.implicit_self.has_implicit_self()
            && return_ty(cx, impl_item.hir_id).is_diag_item(cx, sym::String)
        {
            println!("`our_fancy_method` is implemented!");
        }
    }
}
```

**Type path fallback** (Ch. 4, "Using Type Path"):
```rust
use clippy_utils::paths;
use clippy_utils::ty::implements_trait;

if let Some(trait_def_id) = paths::ITER_STEP.first(cx)
    && implements_trait(cx, ty, trait_def_id, &[])
{
    println!("`expr` implements the `core::iter::Step` trait!");
}
```

# Relationships

## Builds Upon
- **LateContext** — most utility functions take `cx: &LateContext` as a parameter
- **LateLintPass** — utilities are designed for use within late lint callbacks

## Enables
- **Trait checking** — `implements_trait` is the primary trait checking function
- **Diagnostic items** — `clippy_utils::sym` provides symbols for diagnostic item lookup
- **Macro handling** — `is_from_proc_macro` is a Clippy-specific macro detection utility

## Related
- **Ty type and kind** — many utilities operate on or return `Ty` values
- **Adding a lint** — the lint scaffolding process involves importing from `clippy_utils`

# Common Errors

- **Error**: Omitting the trait ownership check when matching method calls, matching only on method name.
  **Correction**: "If a trait defines only one method [...] one might be tempted to omit the method name check. This would work, but is not always advisable because: if a new method [...] were to be added to the trait, there would be a risk of matching the wrong method." (Ch. 4, "Method Checking"). The same applies in reverse — always verify the method belongs to the expected trait.

- **Error**: Forgetting to add new symbols to `clippy_utils::sym`.
  **Correction**: "New symbols such as `our_fancy_method` need to be added to the `clippy_utils::sym` module." (Ch. 4, "Method Checking"). Custom method or type names used in symbol comparisons must be registered.

# Common Confusions

- **Confusion**: Thinking `clippy_utils::paths` is the preferred way to identify types.
  **Clarification**: Paths are the fallback. Diagnostic items (via `sym`) and lang items are preferred. "This approach should be avoided if possible, the best thing to do would be to make a PR to `rust-lang/rust` adding a diagnostic item." (Ch. 4, "Using Type Path")

- **Confusion**: Thinking method name matching alone is sufficient to identify a specific method.
  **Clarification**: Multiple traits can define methods with the same name (e.g., `map` exists on both `Iterator` and user-defined traits). Always verify the owning trait using `cx.ty_based_def(expr).opt_parent(cx).is_diag_item(...)` or equivalent. "Comparing symbols is very cheap and might prevent a more expensive lookup." (Ch. 4, "Method Checking")

# Source Reference

Chapter 5: "Common tools for writing lints," all sections. Supplemented by Chapter 4: "Method Checking" and "Trait Checking" sections.

# Verification Notes

- Definition source: Synthesized from Ch. 4 and Ch. 5 of the Clippy documentation; individual functions documented with direct quotations
- Confidence rationale: HIGH — both chapters provide explicit code examples for every major utility function
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent B concepts (late-lint-pass, adding-a-lint) and within this card set (late-context, ty-type-and-kind, trait-checking, diagnostic-item, macro-handling)
