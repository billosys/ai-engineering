---
concept: Avoid If Expressions
slug: avoid-if-expressions
category: functions-pattern-matching
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Avoid if expressions"
extraction_confidence: high
aliases:
  - "no if"
  - "avoid if"
prerequisites: []
extends: []
related:
  - functions-over-case-expressions
  - prefer-pattern-matching-over-equality
contrasts_with:
  - functions-over-case-expressions
answers_questions:
  - "Why should I avoid the if expression in Erlang?"
  - "What distinguishes an if expression from a case expression in idiomatic Erlang?"
---

# Quick Definition

Don't use `if` expressions; prefer `case` or pattern-matching function clauses.

# Core Definition

"Don't use `if`" (Inaka, "Avoid if expressions"). In many situations `if` introduces static boolean logic that reduces flexibility; a `case` or a function call with pattern-matching clauses is more declarative. `if` is also error-prone for newcomers who learned it in other languages.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `if` is avoided entirely.
2. `if` tends to encode static boolean logic, reducing flexibility.
3. A `case` on a tuple of values, or pattern-matching function clauses, is the idiomatic replacement.
4. It is a PR-rejection rule under Syntax.

# Construction / Recognition

## To Apply

1. Replace an `if` whose guards test several variables with a `case` over a tuple of those variables.
2. Better still, lift the decision into a function with pattern-matching clauses.

## To Recognize a Violation

1. The `if ... end` construct appears in the code.

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: branching on the result of guard tests.
- **Common applications**: converting `if Transport =/= cowboy_spdy, Version =:= 'HTTP/1.1' -> ...` into a `connection_headers/3` function with matching clauses.

# Examples

**Example 1** — bad: an `if` with a `Transport =/= cowboy_spdy, Version =:= 'HTTP/1.1'` guard and a `true ->` catch-all.

**Example 2** — "better": a `case {Transport, Version} of ... end`.

**Example 3** — good: a `connection_headers/3` function with pattern-matching clauses.

# Relationships

## Related

- **More, smaller functions over case expressions** — the "good" form pushes the decision into function clauses.
- **Prefer pattern-matching over testing for equality** — same preference for matching over boolean logic.

## Contrasts With

- **More, smaller functions over case expressions** — `case` is the *acceptable* middle ground here, yet that rule pushes further toward function clauses; the two together rank `if` < `case` < clauses.

# Common Errors

- **Error**: Reaching for `if` out of habit from other languages.
  **Correction**: Use `case` or, better, pattern-matching function clauses.

# Common Confusions

- **Confusion**: Thinking `if` is just a stylistic dislike.
  **Clarification**: The source's rationale is concrete — `if` injects static boolean logic and is easily abused or misunderstood.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Avoid if expressions". The source links Robert Virding's "The problem with 'if'" and related discussions.

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with three examples and external debate links.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
