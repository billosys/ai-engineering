---
concept: Trait Checking (Verifying Trait Implementations in Lints)
slug: trait-checking
category: type-system
subcategory: trait-verification
tier: advanced
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "04-advanced-linting"
chapter_number: 4
pdf_page: null
section: "Trait Checking"
extraction_confidence: high
aliases:
  - "trait checking"
  - "implements_trait"
  - "trait implementation check"
  - "checking trait implementations"
prerequisites:
  - late-context
  - typeck-results
  - ty-type-and-kind
  - diagnostic-item
extends:
  - ty-type-and-kind
related:
  - clippy-utils
  - clippy
contrasts_with: []
answers_questions:
  - "How do I check if a type implements a specific trait in a Clippy lint?"
  - "How do I use implements_trait?"
  - "How do I check for a generic trait implementation like Borrow<[u8]>?"
  - "How do I create types programmatically for generic trait parameters?"
---

# Quick Definition

Trait checking in Clippy lints uses `clippy_utils::ty::implements_trait(cx, ty, trait_def_id, &[generic_args])` to determine whether a given `Ty` implements a specific trait, where the trait's `DefId` is obtained via diagnostic items, lang items, or path-based lookup.

# Core Definition

Chapter 4 introduces trait checking as a complement to type checking: "Besides type checking, we might want to examine if a specific type `Ty` implements certain trait when implementing a lint. There are three approaches to achieve this, depending on if the target trait that we want to examine has a diagnostic item, lang item, or neither." (Ch. 4, "Trait Checking")

The core function is `implements_trait` from `clippy_utils::ty`. Chapter 5 shows the concise pattern: "Check for the trait implementation via the `implements_trait` util." (Ch. 5, "Checking if a type implements a specific trait")

For generic traits, Chapter 4 explains: "Traits are often generic over a type parameter, e.g. `Borrow<T>` is generic over `T`. Rust allows us to implement a trait for a specific type. [...] To do so, we can use the same `implements_trait` function as above, and supply a type parameter that represents `[u8]`." (Ch. 4, "Creating Types Programmatically")

# Prerequisites

- **LateContext** — needed to access `TyCtxt` for trait `DefId` lookup
- **TypeckResults** — needed to retrieve the `Ty` of the expression to check
- **Ty type and kind** — understanding `Ty` is essential since `implements_trait` takes a `Ty` parameter
- **Diagnostic items** — the preferred way to obtain a trait's `DefId` for use with `implements_trait`

# Key Properties

1. `implements_trait(cx, ty, trait_def_id, generic_args)` is the core function from `clippy_utils::ty`
2. `trait_def_id` is a `DefId` obtained via diagnostic items, lang items, or `clippy_utils::paths`
3. `generic_args` is `&[GenericArg]` — empty `&[]` for non-generic traits, populated for generic traits like `Borrow<T>`
4. To supply generic type arguments, create `Ty` values programmatically with `Ty::new_*` and convert with `.into()`
5. The preferred hierarchy for obtaining trait `DefId`s: diagnostic items > lang items > paths
6. Generic args are created by constructing `Ty` values and calling `.into()` to wrap them as `GenericArg`

# Construction / Recognition

## Standard Pattern for Non-Generic Traits

1. Get the `Ty` of the expression: `let ty = cx.typeck_results().expr_ty(expr);`
2. Get the trait's `DefId`: `cx.tcx.get_diagnostic_item(sym::TraitName)` or `cx.tcx.lang_items().trait_method()`
3. Check: `implements_trait(cx, ty, trait_def_id, &[])`

## Pattern for Generic Traits (e.g., Borrow<[u8]>)

1. Get the `Ty` of the expression
2. Get the trait's `DefId`
3. Create the generic argument type: `let slice_of_bytes = Ty::new_slice(cx.tcx, cx.tcx.types.u8);`
4. Convert to `GenericArg`: `let generic_param = slice_of_bytes.into();`
5. Check: `implements_trait(cx, ty, trait_def_id, &[generic_param])`

# Context & Application

Trait checking is one of the most common operations in Clippy lints. Many lints need to determine whether a type can be iterated (`Iterator`), compared (`Eq`, `PartialEq`), cloned (`Clone`), or dropped (`Drop`). The `implements_trait` utility centralizes this logic, insulating lint authors from the details of the compiler's trait resolution system.

The pattern is especially powerful for lints that suggest code transformations — before suggesting that code use `.iter()`, a lint should verify the type implements `IntoIterator`; before suggesting `==` comparison, it should verify `PartialEq` is implemented.

# Examples

**Checking Iterator via diagnostic item** (Ch. 4, "Using Diagnostic Items"):
```rust
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;

impl LateLintPass<'_> for CheckIteratorTraitLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let implements_iterator = (cx.tcx.get_diagnostic_item(sym::Iterator))
            .is_some_and(|id| implements_trait(cx, cx.typeck_results().expr_ty(expr), id, &[]));
        if implements_iterator {
            // [...]
        }
    }
}
```

**Checking Drop via lang items** (Ch. 4, "Using Lang Items"):
```rust
use clippy_utils::ty::implements_trait;

impl LateLintPass<'_> for CheckDropTraitLint {
    fn check_expr(&mut self, cx: &LateContext<'_>, expr: &Expr<'_>) {
        let ty = cx.typeck_results().expr_ty(expr);
        if cx.tcx.lang_items()
            .drop_trait()
            .map_or(false, |id| implements_trait(cx, ty, id, &[])) {
                println!("`expr` implements `Drop` trait!");
            }
    }
}
```

**Checking generic Borrow<[u8]> with programmatic types** (Ch. 4, "Creating Types Programmatically"):
```rust
use rustc_middle::ty::Ty;
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;

let ty = todo!("Get the `Foo` type to check for a trait implementation");
let borrow_id = cx.tcx.get_diagnostic_item(sym::Borrow).unwrap();
let slice_of_bytes_t = Ty::new_slice(cx.tcx, cx.tcx.types.u8);
let generic_param = slice_of_bytes_t.into();
if implements_trait(cx, ty, borrow_id, &[generic_param]) {
    todo!("Rest of lint implementation")
}
```

**Concise pattern from Ch. 5** (Ch. 5, "Checking if a type implements a specific trait"):
```rust
use clippy_utils::sym;
use clippy_utils::ty::implements_trait;

// Get trait DefId (via lang items or diagnostic items)
let trait_id = cx.tcx.get_diagnostic_item(sym::Eq);
let ty = cx.typeck_results().expr_ty(expr);
if trait_id.is_some_and(|id| implements_trait(cx, ty, id, &[])) {
    // `ty` implements the trait.
}

// For traits with generic parameters
let trait_id = cx.tcx.lang_items().eq_trait();
if trait_id.is_some_and(|id| implements_trait(cx, ty, id, &[ty])) {
    // `ty` implements `PartialEq<Self>`
}
```

# Relationships

## Builds Upon
- **Ty type and kind** — trait checking operates on `Ty` values; programmatic type creation uses `Ty::new_*`
- **Diagnostic items** — the preferred way to obtain trait `DefId`s
- **TypeckResults** — provides the `Ty` to check
- **LateContext** — provides access to `TyCtxt` for `DefId` lookup

## Enables
- Higher-level lint logic that gates suggestions on trait availability

## Related
- **Clippy utils** — `implements_trait` lives in `clippy_utils::ty`
- **Clippy** — trait checking enables the type-aware lints users interact with

# Common Errors

- **Error**: Passing an empty generic args slice `&[]` when the trait has required generic parameters.
  **Correction**: For generic traits like `Borrow<T>` or `PartialEq<Rhs>`, you must supply the appropriate generic arguments. Create the types programmatically with `Ty::new_*` and convert with `.into()`.

- **Error**: Using `unwrap()` on `get_diagnostic_item` results.
  **Correction**: Always use `is_some_and`, `map_or(false, ...)`, or similar patterns. The documentation's own example includes a note: "avoid unwrap in real code." (Ch. 4, "Creating Types Programmatically")

# Common Confusions

- **Confusion**: Thinking `implements_trait` checks if a type *can* implement a trait (i.e., satisfies the bounds).
  **Clarification**: `implements_trait` checks if a concrete `impl` exists for the given type and trait. It queries the compiler's trait resolution system for an actual implementation, not whether one could theoretically be written.

- **Confusion**: Not understanding the role of `GenericArg` in `implements_trait`.
  **Clarification**: "In rustc, a generic is an entity that the compiler understands and has three kinds, type, const and lifetime. By calling `.into()` on a constructed `Ty`, we wrap the type into a generic which can then be used by the query system to decide whether the specialized trait is implemented." (Ch. 4, "Creating Types Programmatically")

# Source Reference

Chapter 4: "Trait Checking," all sections including "Using Diagnostic Items," "Using Lang Items," "Using Type Path," and "Creating Types Programmatically." Supplemented by Chapter 5: "Common tools for writing lints," section "Checking if a type implements a specific trait."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 and Ch. 5 of the Clippy documentation
- Confidence rationale: HIGH — the source provides thorough coverage with three distinct approaches and programmatic type creation, all with code examples
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent A concepts (clippy) and within this card set (late-context, typeck-results, ty-type-and-kind, diagnostic-item, clippy-utils)
