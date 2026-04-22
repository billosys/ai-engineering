---
# === CORE IDENTIFICATION ===
concept: EarlyLintPass
slug: early-lint-pass

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
section: "EarlyLintPass"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc_lint::EarlyLintPass"
  - "early lint pass"
  - "AST lint pass"
  - "early pass"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-pass
extends: []
related:
  - late-lint-pass
  - lint-registration
  - lint-emission
  - adding-a-lint
contrasts_with:
  - late-lint-pass

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is EarlyLintPass and when should I use it?"
  - "What information is available in EarlyContext?"
  - "What are the limitations of EarlyLintPass compared to LateLintPass?"
  - "How do I scaffold a lint that uses EarlyLintPass?"
  - "What kinds of lints are good candidates for EarlyLintPass?"
---

# Quick Definition

`EarlyLintPass` is a Clippy lint trait that operates on the Abstract Syntax Tree (AST) before type checking and HIR lowering. It is faster than `LateLintPass` but has no access to type information, making it suitable only for syntax-level checks.

# Core Definition

The source describes `EarlyLintPass` as follows: "EarlyLintPass runs before type checking and HIR lowering." The trait's methods receive an `EarlyContext`, whose documentation states: "Context for lint checking of the AST, after expansion, before lowering to HIR."

This means `EarlyLintPass` works at the AST level -- after macro expansion but before the compiler has performed type inference, trait resolution, or any semantic analysis. The lint can see the syntactic structure of the code (function names, literal values, patterns, attribute annotations) but cannot determine what types expressions have, whether a method exists, or what trait a type implements.

The source uses the example of the `foo_functions` lint to illustrate: "Writing a lint that only checks for the name of a function means that we only have to deal with the AST and don't have to deal with the type system at all." The lint only needs to match `FnKind::Fn` and check `ident.name.as_str() == "foo"` -- purely syntactic operations.

Key imports for an `EarlyLintPass` lint:
```rust
use rustc_lint::{EarlyLintPass, EarlyContext};
use rustc_session::declare_lint_pass;
use rustc_ast::ast::*;
```

For MSRV checking in early passes, the source notes: "Early lint passes should instead use `MsrvStack` coupled with `extract_msrv_attr!()`" (rather than the `Msrv` struct used in late passes).

# Prerequisites

- **lint-pass** -- Understanding the general lint pass concept (visitor pattern, `check_*` methods, registration) is required before specializing to EarlyLintPass.

# Key Properties

1. Operates on the AST (Abstract Syntax Tree), not HIR
2. Runs before type checking and HIR lowering
3. Uses `EarlyContext` which has no type-checking methods
4. Faster than `LateLintPass` (though speed is rarely a practical concern)
5. Nodes are identified only by position in the AST -- cannot look up nodes by ID
6. Cannot determine types of expressions, resolve method calls, or check trait implementations
7. Scaffolded with `cargo dev new_lint --pass=early`
8. Registered with `store.register_early_pass(|| Box::new(...))`
9. MSRV checking uses `MsrvStack` and `extract_msrv_attr!()` instead of `Msrv::meets()`
10. Less commonly used than `LateLintPass` -- most lints need type information

# Construction / Recognition

## To Determine if a Lint Should Use EarlyLintPass:
1. Does the lint only check names, syntax patterns, or literal values? -> EarlyLintPass is appropriate
2. Does the lint check whether a type implements a trait? -> Must use LateLintPass
3. Does the lint need to resolve method calls to their definitions? -> Must use LateLintPass
4. Does the lint need to inspect nodes other than the currently visited one by ID? -> Prefer LateLintPass
5. Is the check purely "grammatical" -- does the AST alone contain enough information? -> EarlyLintPass works

## To Implement an EarlyLintPass:
1. Generate boilerplate: `cargo dev new_lint --name=<name> --pass=early --category=<cat>`
2. The generated file will import `rustc_lint::{EarlyLintPass, EarlyContext}` and `rustc_ast::ast::*`
3. Implement `EarlyLintPass` on your lint struct
4. Override the appropriate `check_*` method (e.g., `check_fn`, `check_expr`, `check_item`)
5. Use `EarlyContext` for diagnostics -- call `span_lint_*` functions from `clippy_utils::diagnostics`

## To Recognize an EarlyLintPass Lint:
1. Look for `impl EarlyLintPass for <Struct>`
2. Look for `EarlyContext<'_>` as a parameter in `check_*` methods
3. Look for `register_early_pass` in the registration code
4. Look for imports from `rustc_ast::ast`

# Context & Application

The source gives the following AST-level reasoning: consider `let x = OurUndefinedType; x.non_existing_method();`. From the AST perspective, both lines are "grammatically correct." The assignment uses `let` and ends with a semicolon. The method invocation looks syntactically fine. The AST/parser is satisfied. Only when you go deeper into type information do you discover that `OurUndefinedType` and `non_existing_method()` are undefined. This is what the source means by "`EarlyLintPass` deals with only syntax on the AST level."

**Good candidates for EarlyLintPass**:
- Naming convention checks (like `foo_functions`)
- Syntactic pattern detection (redundant braces, unnecessary parentheses)
- Attribute validation
- Code style lints that depend only on source structure

**Poor candidates for EarlyLintPass**:
- Anything involving type resolution
- Checking if an expression is a specific library type
- Verifying trait implementations
- Analyzing method call chains where method identity matters

# Examples

**Example 1**: Complete `EarlyLintPass` lint checking for functions named `foo`:
```rust
use rustc_lint::{EarlyLintPass, EarlyContext};
use rustc_session::declare_lint_pass;
use rustc_ast::ast::*;

declare_clippy_lint! {
    /// ### What it does
    /// Checks for functions named `foo`.
    #[clippy::version = "1.29.0"]
    pub FOO_FUNCTIONS,
    pedantic,
    "function named `foo`, which is not a descriptive name"
}

declare_lint_pass!(FooFunctions => [FOO_FUNCTIONS]);

impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        if is_foo_fn(fn_kind) {
            span_lint_and_help(
                cx, FOO_FUNCTIONS, span,
                "function named `foo`",
                None,
                "consider using a more meaningful name"
            );
        }
    }
}

fn is_foo_fn(fn_kind: FnKind<'_>) -> bool {
    match fn_kind {
        FnKind::Fn(_, _, Fn { ident, .. }) => ident.name.as_str() == "foo",
        FnKind::Closure(..) => false
    }
}
```

**Example 2**: Registering an early lint pass:
```rust
store.register_early_pass(|| Box::new(foo_functions::FooFunctions));
```

**Example 3**: AST-level analysis -- the parser sees valid syntax here:
```rust
let x = OurUndefinedType;       // AST: valid assignment
x.non_existing_method();        // AST: valid method call syntax
// EarlyLintPass would see both as syntactically correct
// Only LateLintPass could detect the undefined type/method
```

# Relationships

## Builds Upon
- **lint-pass** -- EarlyLintPass is one specialization of the general lint pass concept

## Enables
- **lint-emission** -- EarlyLintPass `check_*` methods are where diagnostics are emitted for AST-level lints

## Contrasts With
- **late-lint-pass** -- LateLintPass operates on HIR with type information; EarlyLintPass operates on AST without it

## Related
- **lint-registration** -- Early passes are registered with `store.register_early_pass()`
- **adding-a-lint** -- `--pass=early` selects EarlyLintPass during scaffolding

# Common Errors

- **Error**: Trying to access type information from `EarlyContext`.
  **Correction**: `EarlyContext` has no type-checking methods. If you need types, switch to `LateLintPass`.

- **Error**: Using `Msrv::meets()` in an `EarlyLintPass`.
  **Correction**: Early lint passes should use `MsrvStack` coupled with `extract_msrv_attr!()` instead of the `Msrv` struct.

- **Error**: Attempting to look up a node by its ID in an `EarlyLintPass`.
  **Correction**: In the AST, nodes are identified only by position. Use `LateLintPass` if you need to look up nodes by ID.

# Common Confusions

- **Confusion**: Thinking "early" means the lint runs first and then the "late" lint runs on the same pass.
  **Clarification**: Early and late are completely separate passes over different representations (AST vs. HIR). A lint implements one or the other, never both.

- **Confusion**: Believing `EarlyLintPass` is inferior and should be avoided.
  **Clarification**: It is the right choice when only syntax matters. It is faster and simpler. The source explicitly says "it should be your choice if you know for sure a lint does not need type information."

- **Confusion**: Assuming `EarlyLintPass` runs on unexpanded macros.
  **Clarification**: `EarlyContext` documentation states it operates "after expansion." Macros have already been expanded when the early pass runs.

# Source Reference

Chapter 3: Lint Basics, section "EarlyLintPass" under "Lint passes". Also referenced in the "Adding a new lint" walkthrough where the `foo_functions` example uses `--pass=early`. The `MsrvStack` note is from the "Specifying the lint's minimum supported Rust version" section.

# Verification Notes

- Definition: Directly quoted -- "EarlyLintPass runs before type checking and HIR lowering"
- EarlyContext quote: Source quotes the EarlyContext docs -- "Context for lint checking of the AST, after expansion, before lowering to HIR"
- AST example: Source provides the `OurUndefinedType` example to illustrate AST-level analysis
- Speed note: Source states "the EarlyLintPass is faster, and it should be your choice if you know for sure a lint does not need type information"
- MsrvStack: Source explicitly states "Early lint passes should instead use MsrvStack"
- Confidence: HIGH -- the section is dedicated entirely to explaining EarlyLintPass with examples
- Cross-references: All slugs verified against planned extractions across agents
