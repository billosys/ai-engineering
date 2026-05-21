---
concept: More, Smaller Functions Over Case Expressions
slug: functions-over-case-expressions
category: functions-pattern-matching
subcategory: source-code-layout
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "More, smaller functions over case expressions"
extraction_confidence: high
aliases:
  - "function clauses over case"
  - "prefer pattern matching to case"
prerequisites:
  - keep-functions-small
extends: []
related:
  - avoid-deep-nesting
  - prefer-pattern-matching-over-equality
contrasts_with:
  - avoid-if-expressions
answers_questions:
  - "How do I replace a top-level case expression with function clauses?"
  - "When should a case be turned into separate function clauses?"
---

# Quick Definition

Prefer pattern-matching function clauses over `case` expressions, especially when the `case` is the top-level expression of a function or is large.

# Core Definition

"Use pattern-matching in clause functions rather than case's" (Inaka, "More, smaller functions over case expressions"), specially important when the `case` is the top-level expression of the function, or huge. A `case` in a function body usually represents a decision; promoting each branch to a named function clause gives that decision a meaningful name.

# Prerequisites

- **Keep functions small** — this rule produces more, smaller functions; the small-function discipline frames why that is desirable.

# Key Properties

1. A top-level `case` is the strongest candidate for conversion to function clauses.
2. A "huge" `case` is also a strong candidate regardless of position.
3. Each `case` branch becomes one function clause, named meaningfully.
4. An un-promoted `case` acts as an "anonymous function" that obscures meaning.

# Construction / Recognition

## To Apply

1. Identify a `case` whose scrutinee is a function argument or local binding.
2. Create a new function; turn each `case` clause into a function clause that pattern-matches the same value.
3. Replace the `case` with a call to the new, meaningfully named function.

## To Recognize a Violation

1. A function body is just a `case` over its own argument.
2. An internal `case` binds a result variable that is then used once.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: dispatch functions; functions that branch on a tag atom.
- **Common applications**: replacing `bad(Arg) -> case Arg of ... end` with `good(this_one) -> ...; good(and_this_one) -> ...`.
- **Exception**: a `case` used as the argument to a higher-order function is acceptable.

# Examples

**Example 1** — bad: `bad(Arg) -> case Arg of this_one -> ...; and_this_one -> ... end.`

**Example 2** — good: two clauses `good(this_one) -> ...` and `good(and_this_one) -> ...`.

**Example 3** — good: an internal `case` result is replaced by a call to a named helper `good(InitialArg)`.

# Relationships

## Builds Upon

- **Keep functions small** — motivates splitting decisions into named functions.

## Related

- **Avoid deep nesting** — promoting `case` branches to clauses flattens nesting.
- **Prefer pattern-matching over testing for equality** — same preference for matching over branching.

## Contrasts With

- **Avoid if expressions** — both reject in-body control constructs in favor of clauses.

# Common Errors

- **Error**: Leaving a giant `case` as the entire function body.
  **Correction**: Split each branch into a named function clause.

# Common Confusions

- **Confusion**: Believing all `case` expressions are bad.
  **Clarification**: A `case` is fine when small and not top-level, or when used within a higher-order function context.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "More, smaller functions over case expressions".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning paragraph.
- Confidence rationale: HIGH — explicit rule with three examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
