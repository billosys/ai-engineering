---
concept: Prefer Pattern-Matching Over Testing For Equality
slug: prefer-pattern-matching-over-equality
category: functions-pattern-matching
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Prefer pattern-matching over testing for equality"
extraction_confidence: high
aliases:
  - "pattern matching over equality"
  - "match instead of =:="
prerequisites: []
extends: []
related:
  - avoid-if-expressions
  - functions-over-case-expressions
  - avoid-boolean-parameters
contrasts_with: []
answers_questions:
  - "Should I use =:= or pattern matching to compare values?"
---

# Quick Definition

When writing a conditional based on comparing two values, prefer pattern matching over an equality test followed by a boolean switch.

# Core Definition

"When you want to write a conditional statement based on a comparison of two values, don't use equality and then switch according to the boolean result value. Use pattern matching instead" (Inaka, "Prefer pattern-matching over testing for equality"). Matching one value against another directly is more declarative than computing `A =:= B` and branching on `true`/`false`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A `case A =:= B of true -> ...; false -> ... end` is replaced by matching `A` against `B`.
2. Equality-then-switch introduces static boolean logic that reduces flexibility.
3. Matching can also bind the result of a function call for further use.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Replace `case X =:= Y of true -> ...; false -> ... end` with `case X of Y -> ...; Other -> ... end`.
2. Where a function produces the value, match on its result and bind the non-matching case.

## To Recognize a Candidate

1. A `case` scrutinee is a `=:=` (or `==`) comparison.

# Context & Application

A "Suggestion & Great Idea" — code that should be considered but does not, by itself, cause PR rejection.

- **Typical contexts**: conditionals comparing two computed values.
- **Common applications**: matching `{change(A), change(B)}` as `{C, C}` vs `{D, _}` instead of `change(A) =:= change(B)`.

# Examples

**Example 1** — bad: `bad(A, B, 0) -> case A =:= B of true -> proceed(); false -> fail(A) end`.

**Example 2** — good: `good(A, B, 0) -> case A of B -> proceed(); A -> fail(A) end`.

# Relationships

## Related

- **Avoid if expressions** — both reject static boolean logic in favor of matching.
- **More, smaller functions over case expressions** — same family of pattern-matching preferences.
- **Avoid boolean parameters** — both avoid boolean-driven control flow.

# Common Errors

- **Error**: Writing `case A =:= B of true -> ...` out of habit.
  **Correction**: Match `A` against `B` directly.

# Common Confusions

- **Confusion**: Thinking equality tests and matching are equivalent.
  **Clarification**: Matching is more declarative and, when a function is involved, lets you capture and use its result.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Prefer pattern-matching over testing for equality".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
