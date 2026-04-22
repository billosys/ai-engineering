---
concept: LateContext (Lint Context for Type Information)
slug: late-context
category: lint-development
subcategory: lint-context
tier: advanced
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "04-advanced-linting"
chapter_number: 4
pdf_page: null
section: "LateContext and TypeckResults"
extraction_confidence: high
aliases:
  - "LateContext"
  - "late context"
  - "lint context"
  - "cx"
prerequisites:
  - late-lint-pass
extends:
  - late-lint-pass
related:
  - typeck-results
  - ty-type-and-kind
  - lint-emission
  - clippy-utils
contrasts_with:
  - early-lint-pass
answers_questions:
  - "What is LateContext and what does it provide?"
  - "How do I access type information in a LateLintPass?"
  - "What is the cx parameter in Clippy lint methods?"
  - "How do I access the type context (TyCtxt) from a lint?"
---

# Quick Definition

`LateContext` is the lint context struct passed to all `LateLintPass` callback methods, providing access to type checking results, the type context (`TyCtxt`), and other compiler internals needed for type-aware linting.

# Core Definition

The Clippy documentation introduces `LateContext` as one of the two most useful data structures available in `LateLintPass`: "The lint context `LateContext` and `TypeckResults` (returned by `LateContext::typeck_results`) are the two most useful data structures in `LateLintPass`. They allow us to jump to type definitions and other compilation stages such as HIR." (Ch. 4, "LateContext and TypeckResults")

Chapter 5 reaffirms: "`cx` is the lint context `LateContext`. The two most useful data structures in this context are `tcx` and the `TypeckResults` returned by `LateContext::typeck_results`, allowing us to jump to type definitions and other compilation stages such as HIR." (Ch. 5, "Retrieving the type of expression")

# Prerequisites

- **LateLintPass** — `LateContext` is the parameter passed to all `LateLintPass` callback methods; understanding the late lint pass is essential to knowing when and how `LateContext` is available

# Key Properties

1. `LateContext` is conventionally named `cx` in lint method signatures
2. It provides `typeck_results()` to access the `TypeckResults` for the current function body, which contains expression and pattern types
3. It provides `tcx` (the `TyCtxt`), which gives access to lang items, diagnostic items, and the full compiler query system
4. It is only available in `LateLintPass`, not `EarlyLintPass`, because type checking has not yet occurred during early linting
5. Through `cx.tcx`, lints can look up diagnostic items (`cx.tcx.get_diagnostic_item(...)`) and lang items (`cx.tcx.lang_items()`)
6. Through `cx.sess()`, lints can access the session and source map for macro detection

# Construction / Recognition

## To Recognize LateContext Usage

1. Look for `cx: &LateContext<'_>` or `cx: &LateContext<'tcx>` as the second parameter in `LateLintPass` method implementations
2. Any call to `cx.typeck_results()`, `cx.tcx`, or `cx.sess()` indicates `LateContext` usage
3. The variable is almost always named `cx` by convention

## Typical Access Patterns

1. Type retrieval: `cx.typeck_results().expr_ty(expr)` to get the type of an expression
2. Diagnostic item lookup: `cx.tcx.get_diagnostic_item(sym::Iterator)` to get a trait's `DefId`
3. Lang item lookup: `cx.tcx.lang_items().drop_trait()` to get a language item's `DefId`
4. Macro detection: `expr.span.in_external_macro(cx.sess().source_map())` to check for external macros

# Context & Application

`LateContext` is the central hub for all type-aware lint logic in Clippy. Every `LateLintPass` lint receives it as a parameter in callbacks like `check_expr`, `check_impl_item`, `check_fn`, and others. It bridges the lint code to the compiler's type system, enabling lints to answer questions like "is this expression a struct?", "does this type implement Drop?", or "is this a call to a specific method?".

Without `LateContext`, a lint can only inspect syntax (as in `EarlyLintPass`). With it, lints gain full access to resolved types, trait implementations, and the compiler's query system.

# Examples

**Basic type retrieval** (Ch. 4, "is_* Usage"):
```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        // Get type of `expr`
        let ty = cx.typeck_results().expr_ty(expr);
        // Check if the `Ty` of this expression is of character type
        if ty.is_char() {
            println!("Our expression is a char!");
        }
    }
}
```

**Diagnostic item lookup via TyCtxt** (Ch. 4, "Using Diagnostic Items"):
```rust
let implements_iterator = (cx.tcx.get_diagnostic_item(sym::Iterator))
    .is_some_and(|id| implements_trait(cx, cx.typeck_results().expr_ty(expr), id, &[]));
```

**External macro detection** (Ch. 4, "The in_external_macro function"):
```rust
if foo_span.in_external_macro(cx.sess().source_map()) {
    // We should ignore macro from a foreign crate.
    return;
}
```

# Relationships

## Builds Upon
- **LateLintPass** — `LateContext` is provided as a parameter to `LateLintPass` callbacks

## Enables
- **TypeckResults** — accessed via `cx.typeck_results()`
- **Ty type and kind** — type retrieval flows through `LateContext`
- **Trait checking** — trait lookups use `cx.tcx` for diagnostic/lang items and `cx` for `implements_trait`
- **Diagnostic items** — looked up through `cx.tcx.get_diagnostic_item(...)`

## Related
- **Clippy utils** — many utility functions take `cx: &LateContext` as their first parameter
- **Lint emission** — diagnostics are emitted through `LateContext`

## Contrasts With
- **EarlyLintPass** — early lints receive `EarlyContext`, which lacks type information

# Common Errors

- **Error**: Attempting to access `typeck_results()` in an `EarlyLintPass`.
  **Correction**: Type information is only available in `LateLintPass`. If your lint needs type information, implement `LateLintPass` instead of `EarlyLintPass`.

- **Error**: Calling `lower_ty` (to convert `hir::Ty` to `ty::Ty`) inside a function body.
  **Correction**: Inside bodies, use `cx.typeck_results().node_type()` instead. "Don't use `lower_ty` inside of bodies, because this can cause ICEs." (Ch. 4, "hir::Ty and ty::Ty")

# Common Confusions

- **Confusion**: Thinking `LateContext` and `EarlyContext` provide similar capabilities.
  **Clarification**: `EarlyContext` only has access to the AST before type checking. `LateContext` operates on the HIR after type checking and resolution, giving access to resolved types, trait implementations, and the full query system. They serve fundamentally different lint categories.

- **Confusion**: Thinking `cx.typeck_results()` returns results for the entire crate.
  **Clarification**: `TypeckResults` are scoped to the current function body being checked. Each body has its own `TypeckResults`.

# Source Reference

Chapter 4: "Type Checking," section "LateContext and TypeckResults." Supplemented by Chapter 5: "Common tools for writing lints," section "Retrieving the type of expression."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 and Ch. 5 of the Clippy documentation
- Confidence rationale: HIGH — the source clearly defines `LateContext` and its role with explicit examples
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent B concepts (late-lint-pass, early-lint-pass, lint-emission) and within this card set (typeck-results, ty-type-and-kind, trait-checking, diagnostic-item, clippy-utils)
