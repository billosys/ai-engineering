---
concept: Macro Handling (Dealing with Macros and Expansions in Lints)
slug: macro-handling
category: lint-development
subcategory: macro-awareness
tier: intermediate
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "04-advanced-linting"
chapter_number: 4
pdf_page: null
section: "Dealing with macros and expansions"
extraction_confidence: high
aliases:
  - "macro handling"
  - "macro expansion"
  - "from_expansion"
  - "in_external_macro"
  - "is_from_proc_macro"
  - "span context"
prerequisites:
  - lint-pass
  - lint-emission
extends: []
related:
  - late-context
  - early-lint-pass
  - late-lint-pass
  - clippy-utils
contrasts_with: []
answers_questions:
  - "How do I handle macro-expanded code in a Clippy lint?"
  - "How do I avoid false positives from macro expansions?"
  - "What is the difference between from_expansion, in_external_macro, and is_from_proc_macro?"
  - "How do I detect proc macro-generated code?"
  - "How do I test a lint with macros?"
---

# Quick Definition

Macro handling in Clippy lints involves detecting and typically ignoring macro-expanded code to avoid false positives, using a layered defense of `span.from_expansion()` (any expansion), `span.in_external_macro(source_map)` (foreign crate macros), `span.ctxt()` (syntax context comparison), and `is_from_proc_macro(cx, node)` (proc macros that manipulate spans).

# Core Definition

The Clippy documentation establishes the guiding principle: "The general rule of thumb is that we should ignore code with macro expansions when working with Clippy because the code can be dynamic in ways that are difficult or impossible for us to foresee." (Ch. 4, "Dealing with macros and expansions")

The reason is clear: "If we wrote a new lint, there is a possibility that the lint is triggered in macro-generated code. Since this expanded macro code is not written by the macro's user but really by the macro's author, the user cannot and should not be responsible for fixing the issue that triggers the lint." (Ch. 4, "False Positives")

Chapter 5 reinforces: "Keep in mind that macros are already expanded and desugaring is already applied to the code representation that you are working with in Clippy. This unfortunately causes a lot of false positives because macro expansions are 'invisible' unless you actively check for them." (Ch. 5, "Dealing with macros and expansions")

# Prerequisites

- **Lint passes** — macro handling applies to both `EarlyLintPass` and `LateLintPass`; understanding the lint pass lifecycle is needed to know where to insert macro checks
- **Lint emission** — macro checks are typically placed before lint emission to prevent false positives

# Key Properties

1. `span.from_expansion()` — returns `true` if the span is from any macro expansion or desugaring; the most common first check in a lint
2. `span.ctxt()` — returns `SyntaxContext`; comparing contexts of two spans reveals whether they come from the same or different expansions
3. `span.in_external_macro(cx.sess().source_map())` — returns `true` if the span is from a macro defined in a foreign crate
4. `is_from_proc_macro(cx, node)` — Clippy-specific approximation for detecting proc macro-generated code, even when the proc macro sets spans to input token spans
5. Code not from expansion is in the "root" context, so `from_expansion() == false` implies same context for all such spans
6. `Span` information (lines, columns) should not be relied upon in macro contexts since macro authors can manipulate spans
7. Macros are expanded before lint passes run — the AST/HIR lints see is already fully expanded

# Construction / Recognition

## Defense-in-Depth Pattern

1. **First line**: `span.from_expansion()` — catches all declarative macro expansions and most proc macro expansions
2. **Second line**: `span.in_external_macro(cx.sess().source_map())` — if the lint should work with some macros, filter out external crate macros
3. **Context comparison**: `left.span.ctxt() != right.span.ctxt()` — when comparing two expressions, check if they come from the same expansion context
4. **Last resort**: `is_from_proc_macro(cx, node)` — catches proc macros that set output spans to input spans; more expensive than other checks

## Recommended Ordering (Ch. 4, "is_from_proc_macro")

Place cheaper checks first in condition chains:
```
if let ... = ...
    && ...
    && !e.span.from_expansion()   // cheap, early
    && ...
    && !is_from_proc_macro(cx, e) // expensive, late
```

# Context & Application

Macro handling is a cross-cutting concern for virtually every Clippy lint. The expanded code that lints analyze may originate from user code, from `macro_rules!` definitions, or from proc macros. Since macro-generated code is outside the user's direct control, linting it produces false positives that frustrate users.

The documentation describes a layered approach where each function catches a different category of macro code. Most lints only need `span.from_expansion()` as a first check, but lints that intentionally work with some macro code need the finer-grained tools.

# Examples

**Basic expansion check** (Ch. 4/5, "The Span::from_expansion method"):
```rust
if expr.span.from_expansion() {
    // We most likely want to ignore it.
    return;
}
```

**Context comparison for binary expressions** (Ch. 4/5, "Span::ctxt method"):
```rust
// For code like `1 + mac!()` which expands to `1 + 0`:
if left.span.ctxt() != right.span.ctxt() {
    // The code author most likely cannot modify this expression
    return;
}
```

**External macro check** (Ch. 4, "The in_external_macro function"):
```rust
if foo_span.in_external_macro(cx.sess().source_map()) {
    // We should ignore macro from a foreign crate.
    return;
}
```

**Proc macro detection with is_from_proc_macro** (Ch. 4, "The is_from_proc_macro function"):
```rust
impl<'tcx> LateLintPass<'tcx> for BorrowDerefRef {
    fn check_expr(&mut self, cx: &LateContext<'tcx>, e: &rustc_hir::Expr<'tcx>) {
        if let ... = ...
            && ...
            && !e.span.from_expansion()
            && ...
            && ...
            && !is_from_proc_macro(cx, e)
            && ...
        {
            ...
        }
    }
}
```

**Testing macro handling** (Ch. 4, "Testing lints with macro expansions"):
```rust
//@aux-build:proc_macros.rs
extern crate proc_macros;

fn main() {
    // Echos tokens with macro span (caught by from_expansion/in_external_macro)
    proc_macros::external!{ code_that_should_trigger_your_lint }
    // Echos tokens with input span (requires is_from_proc_macro)
    proc_macros::with_span!{ span code_that_should_trigger_your_lint }
}
```

# Relationships

## Builds Upon
- **Lint passes** — macro checks are performed within lint pass callbacks
- **Lint emission** — macro handling prevents incorrect lint emission

## Enables
- Correct, false-positive-free lint behavior across all code, including macro-generated code

## Related
- **LateContext** — `cx.sess().source_map()` is accessed through `LateContext` for `in_external_macro`
- **Clippy utils** — `is_from_proc_macro` is provided by `clippy_utils`
- **EarlyLintPass** — macros are expanded at the early pass level; the AST is already expanded
- **LateLintPass** — macro detection is equally important in late passes

# Common Errors

- **Error**: Forgetting to check `from_expansion()` and emitting lints on macro-generated code.
  **Correction**: "This is also why most lints check if they are inside a macro or not before emitting suggestions to the end user to avoid false positives." (Ch. 4, "False Positives"). Add `from_expansion()` as one of the first checks in every lint.

- **Error**: Relying solely on `from_expansion()` to catch all proc macro code.
  **Correction**: Proc macros can set output spans to input token spans (via `quote_spanned!`), making `from_expansion()` return `false`. Use `is_from_proc_macro` as an additional defense for such cases. (Ch. 4, "The is_from_proc_macro function")

- **Error**: Relying on line/column information from spans in macro contexts.
  **Correction**: "A Span in a macro can be changed by the macro author. Therefore, any lint check related to lines or columns should be avoided since they might be changed at any time and become unreliable or incorrect information." (Ch. 4, "False Positives")

# Common Confusions

- **Confusion**: Thinking `in_external_macro` and `is_from_proc_macro` do the same thing.
  **Clarification**: `in_external_macro` detects macros defined in foreign crates (works well for declarative macros). `is_from_proc_macro` specifically detects proc macro-generated code where the proc macro has set spans to input token spans, making other detection methods fail. They complement each other and serve different purposes. (Ch. 4, "The is_from_proc_macro function")

- **Confusion**: Thinking `from_expansion()` only catches `macro_rules!` macros.
  **Clarification**: `from_expansion()` detects expansion from all macro types including `macro_rules!`, macros 2.0, proc macros (when they use `Span::call_site()` or similar), and desugaring. The exception is proc macros that explicitly set spans to input spans.

- **Confusion**: Assuming `x_is_some_span.ctxt() == x_unwrap_span.ctxt()` in the `m!(x, x.unwrap())` example.
  **Clarification**: They have different contexts. `x.is_some()` is generated from inside the macro body (`$a.is_some()`), while `x.unwrap()` corresponds to the macro argument `$b`. "x.is_some() is from inside the macro / x.unwrap() is from outside the macro" — they have different syntax contexts. (Ch. 4, "Span::ctxt method")

# Source Reference

Chapter 4: "Dealing with macros and expansions," all sections including "False Positives," "The Span::from_expansion method," "Span::ctxt method," "The in_external_macro function," "The is_from_proc_macro function," and "Testing lints with macro expansions." Supplemented by Chapter 5: "Common tools for writing lints," section "Dealing with macros and expansions."

# Verification Notes

- Definition source: Direct quotations from Ch. 4 and Ch. 5 of the Clippy documentation
- Confidence rationale: HIGH — the source provides extensive coverage of macro handling with multiple examples, a clear defense-in-depth approach, and testing guidance
- Uncertainties: None
- Cross-reference status: Slugs verified against Agent B concepts (lint-pass, early-lint-pass, late-lint-pass, lint-emission) and within this card set (late-context, clippy-utils)
