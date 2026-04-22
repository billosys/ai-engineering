---
# === CORE IDENTIFICATION ===
concept: Compiler Diagnostics Infrastructure
slug: compiler-diagnostics

# === CLASSIFICATION ===
category: compiler-internals
subcategory: diagnostics
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Errors and Lints"
chapter_number: 17
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc diagnostics"
  - "compiler error messages"
  - "rustc lints"
  - "Span"
  - "DiagCtxt"
  - "Diag"
  - "Diagnostic derive"
  - "Subdiagnostic"
  - "rustc_on_unimplemented"
  - "Applicability"
  - "LintStore"
  - "ErrorGuaranteed"
  - "diagnostic structs"
  - "Fluent translation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-types-and-generics
  - compiler-type-checking
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of a rustc diagnostic error message?"
  - "How are error codes and extended explanations managed in rustc?"
  - "What is the difference between lints and fixed diagnostics?"
  - "What are the diagnostic levels (error, warning, help, note) and when is each used?"
  - "How do suggestions work and what are the Applicability levels?"
  - "What is a Span and how is it used in diagnostics?"
  - "How do you define a new lint using declare_lint! and EarlyLintPass/LateLintPass?"
  - "What are diagnostic structs (#[derive(Diagnostic)]) and subdiagnostic structs?"
  - "How does rustc's translation infrastructure work with Fluent?"
  - "What is the LintStore and how are lints registered?"
  - "What is ErrorGuaranteed and why does it matter for soundness?"
  - "How does #[rustc_on_unimplemented] customize trait error messages?"
---

# Quick Definition

Rustc's diagnostic infrastructure is a comprehensive system for emitting compiler errors, warnings, suggestions, and lints. Diagnostics are structured with levels (error, warning, help, note), optional error codes (like `E0308`), source spans pointing to relevant code, and machine-applicable suggestions. Lints are user-controllable diagnostics managed through the `LintStore`, while fixed diagnostics cannot be silenced. The system supports translatable messages via Fluent, type-safe diagnostic structs via `#[derive(Diagnostic)]`, and a zero-sized `ErrorGuaranteed` type that statically proves an error has been emitted. The `#[rustc_on_unimplemented]` attribute enables trait-specific error customization.

# Core Definition

Diagnostic output in rustc follows a structured format: a **level** (error, warning, etc.), an optional **error code** (e.g. `E0308`), a **message**, a **diagnostic window** showing source code with primary and secondary span labels, and optional **sub-diagnostics** (notes, help, suggestions).

The main infrastructure lives in the `rustc_errors` crate. `DiagCtxt` is the central type for creating and emitting diagnostics. Methods like `span_err` emit directly, while `struct_span_err` returns a `Diag` builder that allows adding notes, suggestions, and labels before calling `emit()`. "Failing to either emit or cancel a `Diag` will result in an ICE."

**Lints** are diagnostics where the user can control the level via `#[allow]`, `#[warn]`, `#[deny]`, or `#[forbid]`. They are defined using the `declare_lint!` macro and implemented via `EarlyLintPass` (on AST nodes after macro expansion) or `LateLintPass` (on HIR nodes with full type information). The `LintStore` manages all lint registrations and is frozen into an `Arc` after initialization.

**Suggestions** use the `span_suggestion` method with an `Applicability` confidence level: `MachineApplicable` (can be applied automatically), `HasPlaceholders` (contains placeholder text), `MaybeIncorrect` (may not be right), or `Unspecified`.

**Diagnostic structs** (`#[derive(Diagnostic)]`) provide a declarative way to define diagnostics as Rust types, separating diagnostic structure from emission logic. Fields annotated with `#[primary_span]`, `#[label]`, `#[note]`, `#[help]`, and `#[suggestion]` generate the corresponding subdiagnostics.

**ErrorGuaranteed** is "a zero-sized type that is unconstructable outside of the `rustc_errors` crate. It is generated whenever an error is reported to the user, so that if your compiler code ever encounters a value of type `ErrorGuaranteed`, the compilation is statically guaranteed to fail." This is critical for soundness -- it prevents the compiler from silently suppressing errors.

**Translation** uses Fluent resources. "Fluent is built around the idea of 'asymmetric localization', which aims to decouple the expressiveness of translations from the grammar of the source language." Diagnostic messages are defined in `.ftl` files as Fluent messages with attributes for subdiagnostics.

# Prerequisites

- General understanding of the rustc compilation pipeline (AST, HIR, MIR phases)

# Key Properties

1. **Diagnostic levels**: `error` (program cannot compile), `warning` (something odd), `help` (how to fix), `note` (additional context)
2. **Error codes**: Unique identifiers like `E0308` linking to extended explanations viewable via `rustc --explain E0308`
3. **Span**: Primary data structure representing a location in source code; attached to most HIR/MIR constructs; looked up in `SourceMap` for snippets
4. **Lints vs fixed diagnostics**: Lints have user-controllable levels; fixed diagnostics (like borrow checker errors) cannot be silenced
5. **Lint passes**: Pre-expansion (before macro expansion), early (after expansion, on AST), late (on HIR with full type info), and MIR passes
6. **LintStore**: Central registry holding all lint declarations and passes; frozen into `Arc` after initialization; three sources: internal, builtin, driver-registered
7. **Suggestion Applicability**: Four levels from `MachineApplicable` (safe for automated fix tools like `rustfix`) to `Unspecified`
8. **Diagnostic derive**: `#[derive(Diagnostic)]` generates `Diagnostic` trait implementations from struct definitions with annotated fields
9. **Subdiagnostic derive**: `#[derive(Subdiagnostic)]` represents partial diagnostics (labels, notes, suggestions) that can be conditionally added
10. **Fluent translation**: Diagnostics are translatable via Fluent resources; identifiers use `_` separation; arguments interpolated with `{$name}` syntax
11. **`#[rustc_on_unimplemented]`**: Attribute on traits allowing custom error messages with filtering via `on(Self = "...", ...)` and format parameters
12. **ErrorGuaranteed**: Zero-sized proof that an error was emitted; used to prevent unsoundness from missing error reports
13. **Buffered lints**: Lints emitted before the linting system is ready are buffered and processed later; parser lints use a separate buffer

# Construction / Recognition

## Emitting a structured diagnostic:
```rust,ignore
let mut err = sess.dcx.struct_span_err(sp, fluent::example::error_msg);
if let Ok(snippet) = sess.source_map().span_to_snippet(sp) {
    err.span_suggestion(
        suggestion_sp,
        fluent::example::suggestion,
        format!("qux {}", snippet),
        Applicability::MachineApplicable,
    );
}
err.emit();
```

## Declaring and implementing a lint:
```rust,ignore
declare_lint! { WHILE_TRUE, Warn, "suggest using `loop { }` instead of `while true { }`" }
declare_lint_pass!(WhileTrue => [WHILE_TRUE]);

impl EarlyLintPass for WhileTrue {
    fn check_expr(&mut self, cx: &EarlyContext<'_>, e: &ast::Expr) {
        // Check for while true patterns, emit lint via cx.struct_span_lint
    }
}
```

## Using diagnostic structs:
```rust,ignore
#[derive(Diagnostic)]
#[diag("field `{$field_name}` is already declared", code = E0124)]
pub struct FieldAlreadyDeclared {
    pub field_name: Ident,
    #[primary_span]
    #[label("field already declared")]
    pub span: Span,
    #[label("`{$field_name}` first declared here")]
    pub prev_span: Span,
}

// Usage:
tcx.dcx().emit_err(FieldAlreadyDeclared { field_name: f.ident, span: f.span, prev_span });
```

# Context & Application

- Rustc's diagnostic quality is a major Rust selling point; "a lot of effort has been put into making `rustc` have great error messages"
- The diagnostic style guide mandates: plain English, lowercase messages without periods, `invalid` instead of `illegal`, minimal spans, and using the Oxford comma
- Lint naming follows RFC 0344: names should read naturally as "allow lint-name items" (e.g. `deprecated`, `unused_variables`)
- Future-incompatible lints signal code that will break in future Rust versions; they can be edition-based or soundness-based
- Combined lint passes (e.g. `BuiltinCombinedModuleLateLintPass`) are used for performance, bundling many individual passes into one to benefit from static dispatch
- Diagnostic items (`#[rustc_diagnostic_item = "..."]`) provide stable `Symbol`-based identification of types/traits for use in lints, avoiding brittle path-based checks

# Examples

**Example 1**: A diagnostic output with suggestion:
```console
error[E0999]: oh no! this is an error!
 --> mycode.rs:3:5
  |
3 |     sad()
  |     ^ help: try using a qux here: `qux sad()`
```

**Example 2**: `#[rustc_on_unimplemented]` with filtering:
```rust,ignore
#[rustc_on_unimplemented(
    on(Self = "&str", note = "call `.chars()` or `.as_bytes()` on `{Self}`"),
    message = "`{Self}` is not an iterator",
    label = "`{Self}` is not an iterator",
    note = "maybe try calling `.iter()` or a similar method"
)]
pub trait Iterator {}
```
This produces different messages for `&str` vs other types that don't implement `Iterator`.

**Example 3**: Finding error sources using `-Z treat-err-as-bug=1` to get a stack trace at the point of emission, or `-Z track-diagnostics` to print creation locations alongside errors.

# Relationships

## Builds Upon
- The rustc compilation pipeline (AST, HIR, MIR representations provide the nodes and spans that diagnostics attach to)

## Enables
- **compiler-type-checking** -- type errors are reported through this diagnostic infrastructure
- **compiler-borrow-checker** -- borrow check errors use fixed diagnostics through this system
- **compiler-trait-solving** -- trait solver errors, including `#[rustc_on_unimplemented]`, use this infrastructure

## Related
- **compiler-types-and-generics** -- type error diagnostics need to render types, handle `TyKind::Error` propagation
- **compiler-type-checking** -- HIR type checking is a primary source of diagnostic emissions

## Contrasts With
- None within this source

# Common Errors

- **Error**: Producing a `TyKind::Error` without first having emitted an error to the user.
  **Correction**: Always use `Ty::new_error` (which requires an `ErrorGuaranteed`) or `Ty::new_error_with_message` (which calls `span_delayed_bug`). "The compiler should never produce `Error` unless we know that an error has already been reported to the user."

- **Error**: Emitting multiple error messages for the same underlying problem.
  **Correction**: Detect duplicates and avoid redundant emissions. Use `ErrorGuaranteed` propagation to suppress cascading errors.

- **Error**: Forgetting to emit or cancel a `Diag` builder.
  **Correction**: Always call `.emit()` or `.cancel()` on `Diag` values; failure to do so causes an ICE.

- **Error**: Using hard-coded warnings (`span_warn`) for normal code instead of lints.
  **Correction**: Prefer lints which give users control over the level. Hard-coded warnings are reserved for special cases like CLI flag warnings.

# Common Confusions

- **Confusion**: Lints and lint passes are the same thing.
  **Clarification**: "There are two parts to the linting mechanism: lints and lint passes. A lint might not have any lint pass that emits it, it could have many, or just one -- the compiler doesn't track whether a pass is in any way associated with a particular lint."

- **Confusion**: `ErrorGuaranteed` indicates the kind of error or that a future error will occur.
  **Clarification**: "It does not convey information about the kind of error" and "should not be used to indicate that a compilation will emit an error in the future. It should be used to indicate that an error has already been emitted."

- **Confusion**: The JSON diagnostic output format is valid JSON.
  **Clarification**: "The output is a series of lines, each of which is a JSON object, but the series of lines taken together is, unfortunately, not valid JSON." Each line is a separate JSON object (JSON Lines format).

- **Confusion**: `help` and `note` sub-diagnostics are interchangeable.
  **Clarification**: "`help` should be used to show changes the user can possibly make to fix the problem. `note` should be used for everything else, such as other context, information and facts, online resources to read, etc."

# Source Reference

Chapter 17: Errors and Lints (2002 lines). Seven sections covering: diagnostic structure and style guide (levels, error codes, suggestions, Applicability); Span and error message APIs (DiagCtxt, Diag, span methods); suggestions (structured API, style guide, rustfix integration); lints (LintStore, lint passes, declaration, edition/feature/future-incompatible lints, lint groups, buffered lints); diagnostic and subdiagnostic structs (#[derive(Diagnostic/Subdiagnostic)]); translation via Fluent; LintStore internals (registration, combined passes); error codes (allocation, explanations); diagnostic items (#[rustc_diagnostic_item]); and ErrorGuaranteed.

# Verification Notes

- Definition source: All key concepts drawn directly from source text descriptions
- Key Properties: All 13 items supported by explicit source content
- Confidence rationale: HIGH -- this is comprehensive internal documentation written by compiler team members
- Uncertainties: Translation infrastructure noted as "pending a redesign" as of October 2024
- Cross-reference status: Related slugs reference other cards in this extraction set
