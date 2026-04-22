---
concept: TypeckResults (Type Checking Results)
slug: typeck-results
category: lint-development
subcategory: type-checking
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
  - "TypeckResults"
  - "typeck_results"
  - "type checking results"
prerequisites:
  - late-context
  - late-lint-pass
extends:
  - late-context
related:
  - ty-type-and-kind
  - trait-checking
  - clippy-utils
contrasts_with: []
answers_questions:
  - "How do I get the type of an expression in a Clippy lint?"
  - "What is TypeckResults and what information does it contain?"
  - "How do I get the type of a pattern in a lint?"
  - "What is the difference between expr_ty and pat_ty?"
---

# Quick Definition

`TypeckResults` is the struct returned by `LateContext::typeck_results()` that contains the results of type checking for the current function body, including methods like `expr_ty()` to retrieve the `Ty` of an expression and `pat_ty()` to retrieve the `Ty` of a pattern.

# Core Definition

The Clippy documentation describes `TypeckResults` as one of the two most useful structures in `LateLintPass`: "`LateContext.typeck_results`'s return value is `TypeckResults` and is created in the type checking step, it includes useful information such as types of expressions, ways to resolve methods and so on." (Ch. 4, "LateContext and TypeckResults")

"`TypeckResults` contains useful methods such as `expr_ty`, which gives us access to the underlying structure `Ty` of a given expression." (Ch. 4, "LateContext and TypeckResults")

Chapter 5 reaffirms: "`typeck_results`'s return value is `TypeckResults` and is created by type checking step, it includes useful information such as types of expressions, ways to resolve methods and so on." (Ch. 5, "Retrieving the type of expression")

# Prerequisites

- **LateContext** — `TypeckResults` is accessed through `cx.typeck_results()`, which requires a `LateContext`
- **LateLintPass** — `LateContext` is only available in late lint passes

# Key Properties

1. Accessed via `cx.typeck_results()` where `cx` is a `LateContext`
2. `expr_ty(&self, expr: &Expr<'_>) -> Ty<'tcx>` returns the type of a given expression
3. `pat_ty(&self, pat: &Pat<'_>) -> Ty<'tcx>` returns the type of a given pattern
4. `node_type()` can be used to get a `ty::Ty` from a `hir::Ty` inside function bodies (as an alternative to `lower_ty`, which must not be used inside bodies)
5. Results are scoped to the current function body, not the entire crate
6. Created during the type checking compilation step, so it reflects fully resolved types

# Construction / Recognition

## To Recognize TypeckResults Usage

1. Look for `cx.typeck_results()` calls in lint implementations
2. Look for chained calls like `cx.typeck_results().expr_ty(expr)` or `cx.typeck_results().pat_ty(pat)`
3. The result is typically used to obtain a `Ty` value for further inspection

## Common Access Patterns

1. Get expression type: `let ty = cx.typeck_results().expr_ty(expr);`
2. Get pattern type: `let ty = cx.typeck_results().pat_ty(pat);`
3. Get node type (from HIR node): `cx.typeck_results().node_type(hir_id)`
4. Chain with kind inspection: `cx.typeck_results().expr_ty(expr).kind()`

# Context & Application

`TypeckResults` is the primary bridge between HIR nodes (expressions, patterns) and their resolved types. In virtually every Clippy lint that needs to inspect types, the first step is calling `cx.typeck_results().expr_ty(expr)` to get the `Ty` of the expression under examination. This `Ty` can then be inspected for its kind, checked against specific types via diagnostic items, or tested for trait implementations.

The struct is produced during the compiler's type checking phase and contains not just types but also method resolution information. This makes it the authoritative source for "what type does this expression have?" within a lint.

# Examples

**Retrieving expression type** (Ch. 4, "is_* Usage" / Ch. 5, "Retrieving the type of expression"):
```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        // Get type of `expr`
        let ty = cx.typeck_results().expr_ty(expr);
        // Match its kind to enter its type
        match ty.kind() {
            ty::Adt(adt_def, _) if adt_def.is_struct() => println!("Our `expr` is a struct!"),
            _ => ()
        }
    }
}
```

**Using expr_ty for trait checking** (Ch. 4, "Using Diagnostic Items"):
```rust
let implements_iterator = (cx.tcx.get_diagnostic_item(sym::Iterator))
    .is_some_and(|id| implements_trait(cx, cx.typeck_results().expr_ty(expr), id, &[]));
```

**The expr_ty signature** (Ch. 4, "LateContext and TypeckResults"):
```rust
pub fn expr_ty(&self, expr: &Expr<'_>) -> Ty<'tcx>
```

# Relationships

## Builds Upon
- **LateContext** — `TypeckResults` is obtained via `cx.typeck_results()`

## Enables
- **Ty type and kind** — `expr_ty` and `pat_ty` return `Ty` values that can be further inspected
- **Trait checking** — the `Ty` retrieved from `TypeckResults` is passed to `implements_trait`
- **Diagnostic items** — type-based diagnostic item checks start with a `Ty` from `TypeckResults`

## Related
- **Clippy utils** — many utility functions internally use `TypeckResults` to retrieve types

# Common Errors

- **Error**: Using `lower_ty` inside a function body to convert `hir::Ty` to `ty::Ty`.
  **Correction**: Use `cx.typeck_results().node_type()` inside bodies. "Don't use `lower_ty` inside of bodies, because this can cause ICEs." (Ch. 4, "hir::Ty and ty::Ty")

- **Error**: Assuming `TypeckResults` provides types for all nodes in the crate.
  **Correction**: `TypeckResults` is per-body. It only contains type information for the function body currently being checked.

# Common Confusions

- **Confusion**: Thinking `expr_ty` and `pat_ty` return the same kind of information.
  **Clarification**: Both return `Ty`, but `expr_ty` works on expressions (`Expr`) while `pat_ty` works on patterns (`Pat`). They are separate methods because expressions and patterns are distinct HIR node types, though both resolve to `Ty`.

- **Confusion**: Conflating `hir::Ty` (what the user wrote) with the `ty::Ty` returned by `TypeckResults`.
  **Clarification**: "`hir::Ty` would represent *what* the user wrote, while `ty::Ty` is how the compiler sees the type and has more information." (Ch. 4, "hir::Ty and ty::Ty"). `TypeckResults` returns `ty::Ty`, which has full compiler understanding of the type including resolved lifetimes and type equivalence.

# Source Reference

Chapter 4: "Type Checking," sections "LateContext and TypeckResults" and "hir::Ty and ty::Ty." Supplemented by Chapter 5: "Common tools for writing lints," section "Retrieving the type of expression."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 and Ch. 5 of the Clippy documentation
- Confidence rationale: HIGH — both chapters explicitly describe `TypeckResults` and its key methods with code examples
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent B concepts (late-lint-pass) and within this card set (late-context, ty-type-and-kind, trait-checking, clippy-utils, diagnostic-item)
