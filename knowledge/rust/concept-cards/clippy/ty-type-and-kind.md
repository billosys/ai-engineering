---
concept: "Ty and TyKind (Type Representation and Classification)"
slug: ty-type-and-kind
category: type-system
subcategory: type-representation
tier: advanced
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "04-advanced-linting"
chapter_number: 4
pdf_page: null
section: "Ty"
extraction_confidence: high
aliases:
  - "Ty"
  - "TyKind"
  - "ty::Ty"
  - "rustc_middle::ty::Ty"
  - "Ty.kind()"
  - "type kind"
prerequisites:
  - typeck-results
  - late-context
extends:
  - typeck-results
related:
  - diagnostic-item
  - trait-checking
  - clippy-utils
contrasts_with: []
answers_questions:
  - "What is the Ty struct in rustc?"
  - "How do I inspect the kind of a type in a Clippy lint?"
  - "What is TyKind and what variants does it have?"
  - "How do I check if a type is a struct, a primitive, or a reference?"
  - "What is the difference between hir::Ty and ty::Ty?"
  - "How do I create types programmatically for trait checking?"
---

# Quick Definition

`Ty` is the compiler's interned type representation (`rustc_middle::ty::Ty`), obtained from `TypeckResults::expr_ty()`. Its `kind()` method returns `TyKind`, an enum of 25+ variants (`Bool`, `Int`, `Ref`, `Adt`, etc.) used for pattern matching on type structure in lints.

# Core Definition

The Clippy documentation introduces `Ty` as the core type representation: "`Ty` struct contains the type information of an expression." Its internal structure is `pub struct Ty<'tcx>(Interned<'tcx, WithStableHash<TyS<'tcx>>>)` — "At a first glance, this struct looks quite esoteric. But at a closer look, we will see that this struct contains many useful methods for type checking." (Ch. 4, "Ty")

For `TyKind`, the documentation explains: "`TyKind` defines the kinds of types in Rust's type system. Peeking into `TyKind` documentation, we will see that it is an enum of over 25 variants, including items such as `Bool`, `Int`, `Ref`, etc." (Ch. 4, "TyKind")

The connection between the two is through the `kind()` method: "Indeed, we just discovered `Ty`'s `kind()` method, which provides us with `TyKind` of a `Ty`." (Ch. 4, "is_* Usage")

The documentation also distinguishes `ty::Ty` from `hir::Ty`: "`hir::Ty` would represent *what* the user wrote, while `ty::Ty` is how the compiler sees the type and has more information." (Ch. 4, "hir::Ty and ty::Ty")

# Prerequisites

- **TypeckResults** — `Ty` is obtained from `TypeckResults` methods like `expr_ty()` and `pat_ty()`
- **LateContext** — `TypeckResults` is accessed through `LateContext`, making it the entry point for all type retrieval

# Key Properties

1. `Ty` is an interned type — it uses pointer equality for fast comparison and is cheap to copy
2. `Ty.kind()` returns `TyKind`, the primary way to inspect what kind of type a `Ty` represents
3. `Ty` provides convenience `is_*` methods (`is_char()`, `is_bool()`, `is_str()`, etc.) that internally match on `TyKind`
4. `TyKind` has 25+ variants including `Bool`, `Char`, `Int`, `Uint`, `Float`, `Str`, `Ref`, `Adt`, `Tuple`, `Slice`, `Array`, `FnDef`, `FnPtr`, `Never`, and more
5. The `Adt` variant (algebraic data type) covers structs, enums, and unions, with an `AdtDef` for further inspection
6. `Ty::new_*` methods allow creating types programmatically (e.g., `Ty::new_slice(cx.tcx, Ty::new_u8())` creates `[u8]`)
7. `hir::Ty` represents what the user wrote; `ty::Ty` represents the compiler's resolved understanding with full lifetime and type information

# Construction / Recognition

## To Retrieve a Ty

1. From an expression: `cx.typeck_results().expr_ty(expr)`
2. From a pattern: `cx.typeck_results().pat_ty(pat)`
3. From a HIR node (inside bodies): `cx.typeck_results().node_type(hir_id)`
4. From a HIR type (outside bodies): `lower_ty(hir_ty)` (never inside bodies — causes ICEs)

## To Inspect a Ty

1. Use convenience methods: `ty.is_char()`, `ty.is_bool()`, `ty.is_str()`, etc.
2. Use `ty.kind()` and pattern match on `TyKind` variants for complex checks
3. For structs/enums/unions: match `ty::Adt(adt_def, substs)` and inspect `adt_def`

## To Create a Ty Programmatically

1. Use `Ty::new_*` methods: `Ty::new_u8()`, `Ty::new_char()`, `Ty::new_bool()`, etc.
2. Compose complex types: `Ty::new_slice(cx.tcx, Ty::new_u8())` creates `[u8]`
3. Convert to `GenericArg` with `.into()` for trait checking with generic parameters

# Context & Application

`Ty` and `TyKind` are the fundamental building blocks for any type-aware lint logic. When a lint needs to determine what kind of value an expression produces, it retrieves the `Ty` and either uses a convenience `is_*` method for simple checks or pattern matches on `TyKind` for complex structural analysis.

Chapter 5 shows the combined pattern as the standard approach: get the type, match its kind. Chapter 4 provides the deeper explanation of why `is_*` methods work (they internally call `kind()` and match on `TyKind`), and how to build types programmatically when checking generic trait implementations.

# Examples

**Simple type check with is_* method** (Ch. 4, "is_* Usage"):
```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);
        if ty.is_char() {
            println!("Our expression is a char!");
        }
    }
}
```

**How is_char works internally** (Ch. 4, "is_* Usage"):
```rust
#[inline]
pub fn is_char(self) -> bool {
    matches!(self.kind(), Char)
}
```

**Pattern matching on TyKind for struct detection** (Ch. 4, "kind Usage"):
```rust
impl LateLintPass<'_> for MyStructLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);
        match ty.kind() {
            ty::Adt(adt_def, _) if adt_def.is_struct() => println!("Our `expr` is a struct!"),
            _ => ()
        }
    }
}
```

**Creating types programmatically** (Ch. 4, "Creating Types programmatically"):
```rust
use rustc_middle::ty::Ty;
let ty = Ty::new_slice(cx.tcx, Ty::new_u8());
```

# Relationships

## Builds Upon
- **TypeckResults** — `Ty` values are obtained from `TypeckResults` methods

## Enables
- **Trait checking** — `Ty` is passed to `implements_trait` to check trait implementations; types can be created programmatically for generic trait parameters
- **Diagnostic items** — `Ty`-level checks like `ty.is_diag_item(cx, sym::Option)` operate on `Ty` values

## Related
- **Clippy utils** — many utilities accept `Ty` or return `Ty` values

# Common Errors

- **Error**: Matching on `ty.kind()` and forgetting the catch-all `_ => ()` arm.
  **Correction**: `TyKind` has 25+ variants. Always include a wildcard arm unless you have exhaustively handled all relevant cases.

- **Error**: Checking `ty::Adt` and assuming it is a struct without checking `adt_def.is_struct()`.
  **Correction**: The `Adt` variant covers structs, enums, and unions. Always inspect `AdtDef` to determine which kind of algebraic data type it is.

- **Error**: Using `lower_ty` inside a function body to convert `hir::Ty` to `ty::Ty`.
  **Correction**: Use `cx.typeck_results().node_type()` inside bodies. `lower_ty` inside bodies can cause internal compiler errors (ICEs).

# Common Confusions

- **Confusion**: Thinking `hir::Ty` and `ty::Ty` are interchangeable.
  **Clarification**: "`hir::Ty` would represent *what* the user wrote, while `ty::Ty` is how the compiler sees the type and has more information." For example, in `fn foo(x: u32) -> u32`, `hir::Ty` sees the parameter type and return type as potentially different types, but `ty::Ty` understands they are the same type with full lifetime resolution. (Ch. 4, "hir::Ty and ty::Ty")

- **Confusion**: Thinking `Ty` is expensive to copy or compare.
  **Clarification**: `Ty` is interned (`Ty<'tcx>(Interned<'tcx, ...>)`), meaning it is essentially a pointer. Copying and comparing `Ty` values is cheap.

- **Confusion**: Thinking `is_*` methods and `kind()` matching are different approaches.
  **Clarification**: The `is_*` methods are convenience wrappers that internally call `kind()` and match on a specific `TyKind` variant. They are equivalent — `is_*` is terser for single checks, `kind()` matching is better when checking multiple variants at once.

# Source Reference

Chapter 4: "Type Checking," sections "Ty," "is_* Usage," "TyKind," "kind Usage," "hir::Ty and ty::Ty," and "Creating Types programmatically." Supplemented by Chapter 5: "Common tools for writing lints," section "Retrieving the type of expression."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 of the Clippy documentation
- Confidence rationale: HIGH — the source provides detailed explanation of both `Ty` and `TyKind` with multiple code examples and internal implementation details
- Uncertainties: None
- Cross-reference status: Slugs verified against within this card set (typeck-results, late-context, diagnostic-item, trait-checking, clippy-utils)
