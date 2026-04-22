---
# === CORE IDENTIFICATION ===
concept: LateLintPass
slug: late-lint-pass

# === CLASSIFICATION ===
category: lint-development
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "LateLintPass"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc_lint::LateLintPass"
  - "late lint pass"
  - "HIR lint pass"
  - "late pass"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-pass
extends: []
related:
  - early-lint-pass
  - lint-registration
  - lint-emission
  - adding-a-lint
  - late-context
  - typeck-results
  - ty-type
contrasts_with:
  - early-lint-pass

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is LateLintPass and when should I use it?"
  - "What information is available in LateContext?"
  - "How does LateLintPass differ from EarlyLintPass?"
  - "Why is LateLintPass the recommended default for Clippy lints?"
  - "What check_* methods are most commonly used with LateLintPass?"
---

# Quick Definition

`LateLintPass` is a Clippy lint trait that operates on the High-Level Intermediate Representation (HIR) after type checking, providing access to type information, trait resolution, and symbol lookup via `LateContext`. It is the recommended default for most Clippy lints.

# Core Definition

The source states: "In contrast to `EarlyLintPass`, `LateLintPass` contains type information." Every method in the `LateLintPass` trait receives a `LateContext`, which provides type-checking capabilities not available in `EarlyContext`.

The `LateContext` documentation reveals methods that deal with type-checking, including:
- `maybe_typeck_results` -- optionally access type checking results
- `typeck_results` -- access type checking results (panics if unavailable)

The source explains why `LateLintPass` is the default: "When you browse through Clippy's lints, you will notice that almost every lint is implemented in a `LateLintPass`, specifically because we often need to check not only for syntactic issues but also type information."

The `LateLintPass` trait is generic over `'tcx` (the type-checking lifetime), reflecting its deep integration with the type system:

```rust
pub trait LateLintPass<'tcx>: LintPass {
    // Trait methods
}
```

The `check_expr` method is "by far the most common method used for Clippy lints" because "Rust is an expression language and, more often than not, the lint we want to work on must examine expressions." Other frequently used methods include `check_fn` and `check_item`.

# Prerequisites

- **lint-pass** -- Understanding the general lint pass concept (visitor pattern, registration, `check_*` methods) is required before specializing to LateLintPass.

# Key Properties

1. Operates on HIR (High-Level Intermediate Representation), not AST
2. Runs after type checking and HIR lowering
3. Uses `LateContext<'tcx>` which provides `typeck_results()` and `maybe_typeck_results()`
4. The recommended default for new Clippy lints
5. Generic over `'tcx` -- the type-checking lifetime
6. `check_expr` is the most commonly used method (Rust is expression-oriented)
7. `check_fn` and `check_item` are also frequently used
8. Nodes in HIR can be looked up by ID, unlike AST nodes in EarlyLintPass
9. Scaffolded with `cargo dev new_lint --pass=late` (the default)
10. Registered with `store.register_late_pass(|_| Box::new(...))`

# Construction / Recognition

## To Determine if a Lint Should Use LateLintPass:
1. Does the lint need to check the type of an expression? -> LateLintPass
2. Does the lint need to verify trait implementations? -> LateLintPass
3. Does the lint need to resolve which method is actually being called? -> LateLintPass
4. Does the lint need to inspect other nodes by ID? -> LateLintPass
5. Are you unsure whether you need type info? -> Default to LateLintPass

## To Implement a LateLintPass:
1. Generate boilerplate: `cargo dev new_lint --name=<name> --pass=late --category=<cat>` (or omit `--pass` since `late` is the default)
2. Implement `LateLintPass<'tcx>` on your lint struct
3. Override the appropriate `check_*` method (commonly `check_expr`)
4. Use `LateContext<'tcx>` to access type information when needed
5. Call diagnostic functions from `clippy_utils::diagnostics`

## To Recognize a LateLintPass Lint:
1. Look for `impl<'tcx> LateLintPass<'tcx> for <Struct>`
2. Look for `LateContext<'tcx>` as a parameter in `check_*` methods
3. Look for `register_late_pass` in the registration code
4. Look for `'tcx` lifetime annotations -- a hallmark of late-pass code

# Context & Application

The source contrasts the two passes using the same code example:
```rust
let x = OurUndefinedType;
x.non_existing_method();
```

While syntactically valid (the AST/parser accepts it), "going down a level and looking at the type information, the compiler will notice that both `OurUndefinedType` and `non_existing_method()` are undefined." This is the kind of analysis only `LateLintPass` can perform.

**Why most lints use LateLintPass**: "Almost every lint is implemented in a `LateLintPass`, specifically because we often need to check not only for syntactic issues but also type information." Even lints that primarily check syntax often need type info for edge cases (e.g., ensuring a method name refers to the specific method, not just any method with that name).

**MSRV checking in late passes** uses the `Msrv` struct:
```rust
pub struct ManualStrip {
    msrv: Msrv,
}
impl ManualStrip {
    pub fn new(conf: &'static Conf) -> Self {
        Self { msrv: conf.msrv }
    }
}
// In the lint logic:
if !self.msrv.meets(cx, msrvs::STR_STRIP_PREFIX) {
    return;
}
```

**Helper utilities**: Clippy provides `clippy_utils` with functions like `implements_trait`, `snippet`, and many others specifically designed for `LateLintPass` use.

# Examples

**Example 1**: LateLintPass implementation with `check_expr`:
```rust
impl<'tcx> LateLintPass<'tcx> for LintName {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx Expr<'_>) {
        if some_lint_expr_logic(expr) {
            span_lint_and_help(
                cx,
                LINT_NAME,
                expr.span,
                "message on why the lint is emitted",
                None,
                "message that provides a helpful suggestion",
            );
        }
    }
}
```

**Example 2**: LateLintPass with a suggestion (using `span_lint_and_sugg`):
```rust
impl<'tcx> LateLintPass<'tcx> for LintName {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, expr: &'tcx Expr<'_>) {
        if some_lint_expr_logic(expr) {
            span_lint_and_sugg(
                cx,
                LINT_NAME,
                span,
                "message on why the lint is emitted",
                "use",
                format!("foo + {} * bar", snippet(cx, expr.span, "<default>")),
                Applicability::MachineApplicable,
            );
        }
    }
}
```

**Example 3**: Registering a late lint pass:
```rust
store.register_late_pass(|_| Box::new(foo_functions::FooFunctions));
```

# Relationships

## Builds Upon
- **lint-pass** -- LateLintPass is the more capable of the two lint pass specializations

## Enables
- **lint-emission** -- LateLintPass `check_*` methods are where diagnostics are emitted, with type-aware logic

## Contrasts With
- **early-lint-pass** -- EarlyLintPass operates on AST without type info; LateLintPass operates on HIR with full type info

## Related
- **late-context** -- LateContext provides type information, snippet utilities, and diagnostic access
- **typeck-results** -- Type checking results accessible via `LateContext::typeck_results()`
- **ty-type** -- The `Ty` type and its `TyKind` variants are used in late-pass type analysis
- **lint-registration** -- Late passes are registered with `store.register_late_pass()`
- **clippy-utils** -- Helper functions like `implements_trait` and `snippet` are designed for late-pass use

# Common Errors

- **Error**: Forgetting to use the `'tcx` lifetime in the impl and method signatures.
  **Correction**: The impl must be `impl<'tcx> LateLintPass<'tcx> for YourStruct`, and methods receive `&LateContext<'tcx>` and `&'tcx Expr<'_>` (or similar HIR types).

- **Error**: Calling `typeck_results()` in a context where it is not available (e.g., in `check_item` for non-function items).
  **Correction**: Use `maybe_typeck_results()` which returns `Option` and does not panic.

- **Error**: Using `LateLintPass` for a pure syntax check, paying unnecessary compilation cost.
  **Correction**: If the lint genuinely needs no type information, use `EarlyLintPass` for simplicity -- though this is a minor optimization, not a critical error.

# Common Confusions

- **Confusion**: Thinking `LateLintPass` means the lint runs "later" in a temporal sequence after early lints.
  **Clarification**: "Late" refers to the compilation stage (after type checking), not execution order relative to early lints. The two passes operate on entirely different data structures (AST vs. HIR).

- **Confusion**: Assuming you always need to use `typeck_results()` in a `LateLintPass`.
  **Clarification**: Many late lints work primarily with HIR node patterns and only occasionally need type info. Having access to types does not mean every method must use them.

- **Confusion**: Believing `LateLintPass` can see macro-unexpanded code.
  **Clarification**: Like `EarlyLintPass`, the code has already been macro-expanded. The difference is that HIR has also been type-checked and lowered from AST. Use `from_expansion()` or `in_external_macro()` to detect macro-generated code.

# Source Reference

Chapter 3: Lint Basics, section "LateLintPass" under "Lint passes". Also covered in the "Emitting a lint" section which demonstrates the full `LateLintPass<'tcx>` pattern with `check_expr`. The "Cheat Sheet" section provides additional references for late-pass development.

# Verification Notes

- Definition: Directly quoted -- "In contrast to EarlyLintPass, LateLintPass contains type information"
- Prevalence: Source confirms "almost every lint is implemented in a LateLintPass"
- check_expr: Source states it is "by far the most common method" because "Rust is an expression language"
- LateContext methods: Source lists `maybe_typeck_results` and `typeck_results` as distinguishing features
- Default: Source confirms `cargo dev new_lint` defaults to `LateLintPass`
- Cheat sheet references: `Ty::TyKind`, `LateLintPass`, `implements_trait`, `snippet` all cited
- Confidence: HIGH -- the section provides detailed comparison with examples
- Cross-references: All slugs verified against planned extractions across agents (including Agent C: late-context, typeck-results, ty-type)
