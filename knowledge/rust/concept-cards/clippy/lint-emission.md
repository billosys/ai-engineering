---
# === CORE IDENTIFICATION ===
concept: Lint Emission
slug: lint-emission

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
section: "Emitting a lint"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "span_lint"
  - "span_lint_and_help"
  - "span_lint_and_sugg"
  - "span_lint_and_note"
  - "span_lint_and_then"
  - "emitting diagnostics"
  - "lint diagnostics"
  - "clippy diagnostics"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-pass
  - lint-declaration
extends: []
related:
  - adding-a-lint
  - lint-testing
  - clippy-utils
  - diagnostic-item
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I emit a lint in Clippy?"
  - "What diagnostic functions are available for emitting lints?"
  - "What is the difference between span_lint, span_lint_and_help, and span_lint_and_sugg?"
  - "How do suggestions and automatic fixes work in Clippy?"
  - "What is Applicability and when should I use each variant?"
  - "How should lint messages be formatted?"
---

# Quick Definition

Lint emission is the act of producing a diagnostic message from within a `check_*` method, using functions from `clippy_utils::diagnostics` such as `span_lint`, `span_lint_and_help`, `span_lint_and_sugg`, and `span_lint_and_then`. Each function provides a different level of diagnostic detail, from bare warnings to machine-applicable code fix suggestions.

# Core Definition

The source introduces lint emission as the step where, with "UI tests and the lint declaration in place, we can start working on the implementation of the lint logic." Emission happens inside `check_*` methods of the lint pass.

Clippy provides five primary diagnostic functions in `clippy_utils/src/diagnostics.rs`:

1. **`span_lint`**: Emits a lint without any additional information
2. **`span_lint_and_note`**: Emits a lint and adds a note (explanatory context)
3. **`span_lint_and_help`**: Emits a lint and provides a helpful message
4. **`span_lint_and_sugg`**: Emits a lint and provides a concrete code suggestion that tools like `rustfix` can automatically apply
5. **`span_lint_and_then`**: Like `span_lint`, but allows extensive output customization via a closure

All functions take at minimum: `cx` (the lint context), the lint name constant (ALL_CAPS), a `Span`, and a message string.

**Message style**: "The text should be matter of fact and avoid capitalization and periods, unless multiple sentences are needed. When code or an identifier must appear in a message or label, it should be surrounded with single grave accents."

**Suggestions and Applicability**: When a lint can suggest a fix, `span_lint_and_sugg` is used with an `Applicability` level:
- `Applicability::MachineApplicable` -- the suggestion is always correct
- `Applicability::MaybeIncorrect` -- the suggestion may not be correct in all cases
- Other levels exist for varying confidence

Suggestions use `snippet()` functions from `clippy_utils::source` to extract code fragments and `format!` to interpolate them into the replacement.

# Prerequisites

- **lint-pass** -- Emission happens inside `check_*` methods of a lint pass implementation.
- **lint-declaration** -- The lint constant (e.g., `FOO_FUNCTIONS`) must be declared before it can be emitted.

# Key Properties

1. All diagnostic functions live in `clippy_utils/src/diagnostics.rs`
2. `span_lint` is the simplest -- just a warning message with no additional context
3. `span_lint_and_note` adds a note attached to an optional span for explanatory context
4. `span_lint_and_help` adds a help message (advice on what to do) attached to an optional span
5. `span_lint_and_sugg` provides a concrete replacement suggestion that `rustfix` can apply automatically
6. `span_lint_and_then` provides maximum customization via a closure that receives the diagnostic builder
7. `Applicability::MachineApplicable` means the suggestion is always correct and safe to auto-apply
8. `Applicability::MaybeIncorrect` means the suggestion might not be correct in every case
9. Messages should be lowercase, without periods, matter-of-fact; code identifiers in backticks
10. Snippets from `clippy_utils::source` extract source code text for use in suggestions

# Construction / Recognition

## To Choose a Diagnostic Function:
1. Just want to flag code with no extra info? -> `span_lint`
2. Want to explain why something is flagged with a reference to another location? -> `span_lint_and_note`
3. Want to give advice but cannot provide a concrete code fix? -> `span_lint_and_help`
4. Can provide a concrete code replacement? -> `span_lint_and_sugg`
5. Need complex multi-part diagnostics? -> `span_lint_and_then`

## To Write a Suggestion:
1. Choose `span_lint_and_sugg` as the diagnostic function
2. Extract source code snippets with `snippet(cx, expr.span, "<default>")`
3. Build the replacement string with `format!(..., snippet(...))`
4. Choose an `Applicability` level based on confidence in the suggestion
5. The suggestion message (e.g., `"use"`, `"try"`) is the short label before the replacement
6. If not all suggestions produce valid code, add `//@no-rustfix` to the test file header

## To Write a Lint Message:
1. Start with a lowercase letter (no capitalization)
2. Do not end with a period (unless multiple sentences)
3. Be matter-of-fact in tone
4. Surround code identifiers with backticks: `\`foo\``
5. If the message is complex, split into an error + help/note/suggestion

# Context & Application

The source frames the three types of additional information as serving different purposes:

**Notes** provide factual context. They explain what happened, often attached to a relevant span. Example: "argument has type `&SomeStruct`" -- a fact about the code.

**Help messages** provide advice. They tell the user what to do but cannot provide a concrete suggestion. Example: "consider using `f64::NAN` if you would like a constant representing NaN".

**Suggestions** provide concrete code replacements. They are the most helpful because tools like `rustfix` can automatically apply them. Example: `` help: try: `.any(|x| x > 2)` ``.

The choice between these affects the user experience directly. Suggestions with `MachineApplicable` applicability can be auto-fixed with `cargo clippy --fix`, making them the highest-value diagnostic type.

**Rustfix integration**: When `span_lint_and_sugg` is used, the test framework automatically generates `.fixed` files via `rustfix`. If a suggestion does not always produce valid code, add `//@no-rustfix` to the test file to suppress this.

# Examples

**Example 1**: Emitting with `span_lint_and_help` (the `foo_functions` example):
```rust
impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        span_lint_and_help(
            cx,
            FOO_FUNCTIONS,
            span,
            "function named `foo`",
            None,
            "consider using a more meaningful name"
        );
    }
}
```

**Example 2**: Emitting with `span_lint_and_sugg` (suggestion with `MachineApplicable`):
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

**Example 3**: Output of a suggestion in compiler output:
```text
error: an inclusive range would be more readable
  --> tests/ui/range_plus_minus_one.rs:37:14
   |
LL |     for _ in 1..1 + 1 {}
   |              ^^^^^^^^ help: use: `1..=1`
```

# Relationships

## Builds Upon
- **lint-pass** -- Emission happens inside lint pass `check_*` methods
- **lint-declaration** -- The lint constant is passed to every diagnostic function

## Enables
- **lint-testing** -- Emitted diagnostics are captured in `.stderr` files for UI test comparison

## Related
- **adding-a-lint** -- Emission is a step in the end-to-end lint creation process
- **clippy-utils** -- `clippy_utils::diagnostics` contains the emission functions; `clippy_utils::source` provides snippet utilities
- **diagnostic-item** -- Diagnostic items help identify standard library types in lint logic

# Common Errors

- **Error**: Using capitalization or periods in lint messages.
  **Correction**: Messages should be lowercase, matter-of-fact, without trailing periods. Use backticks for code: `"function named \`foo\`"`.

- **Error**: Using `span_lint_and_sugg` with `MachineApplicable` when the suggestion may not always produce valid code.
  **Correction**: Use `Applicability::MaybeIncorrect` when the suggestion is not always correct. This prevents `cargo clippy --fix` from automatically applying a potentially broken fix.

- **Error**: Using `span_lint_and_help` when a concrete code fix is available.
  **Correction**: Prefer `span_lint_and_sugg` when you can provide a specific replacement. Suggestions are more actionable and can be auto-applied.

# Common Confusions

- **Confusion**: Thinking notes and help messages are the same thing.
  **Clarification**: Notes explain facts ("argument has type X"). Help messages give advice ("consider using Y"). Notes are attached to spans to highlight relevant code; help messages tell the user what to do.

- **Confusion**: Believing all suggestions are automatically applied by `cargo clippy --fix`.
  **Clarification**: Only `MachineApplicable` suggestions are auto-applied. `MaybeIncorrect` and other levels are presented but not automatically applied.

- **Confusion**: Wondering where the `.fixed` file comes from in tests.
  **Clarification**: When `span_lint_and_sugg` is used, `cargo bless` automatically generates `.fixed` files by having `rustfix` apply the suggestions. If suggestions produce invalid code, use `//@no-rustfix` in the test file.

# Source Reference

Chapter 3: Lint Basics, sections "Emitting a lint" (in both the "Adding a new lint" walkthrough and the dedicated "Emitting a lint" chapter). Diagnostic function list and Applicability from the dedicated chapter. Message style guidelines reference the rustc-dev-guide. Suggestion examples include the `range_plus_one` lint.

# Verification Notes

- Function list: All five functions (`span_lint`, `span_lint_and_note`, `span_lint_and_help`, `span_lint_and_sugg`, `span_lint_and_then`) directly listed in the source
- Message guidelines: Quoted from source -- "matter of fact and avoid capitalization and periods"
- Applicability: Source explains `MachineApplicable` and `MaybeIncorrect` explicitly
- Snippet usage: Source shows `snippet(cx, expr.span, "<default>")` in the suggestion example
- No-rustfix: Source documents `//@no-rustfix` comment for suppressing rustfix in tests
- Output examples: The `range_plus_one` and `fold`/`any` examples are directly from the source
- Confidence: HIGH -- the chapter dedicates extensive coverage to diagnostic functions with examples
- Cross-references: All slugs verified against planned extractions across agents
