---
concept: Guard
slug: guard
category: functions-pattern-matching
subcategory: guards
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "Guards, Guards!"
extraction_confidence: high
aliases:
  - "guard expression"
  - "guard clause"
  - "when clause"
prerequisites:
  - pattern-matching
  - boolean-and-comparison-operators
extends:
  - pattern-matching
related:
  - function-clause
  - if-expression
  - type-test-bif
contrasts_with: []
answers_questions:
  - "What is a guard?"
---

# Guard

## Quick Definition

A guard is an extra clause, introduced by `when`, that goes in a function head to make pattern matching more expressive — for example, testing ranges of values.

## Core Definition

Guards are additional clauses that can go in a function's head to make pattern matching more expressive, since pattern matching alone cannot express things like a range of values or certain types of data. A guard is introduced by `when`. A basic rule is that a guard expression must return `true` to succeed; it fails if it returns `false` or raises an exception. In guards, the comma (`,`) acts like `andalso` and the semicolon (`;`) acts like `orelse` — but `,`/`;` catch exceptions while `andalso`/`orelse` do not. Guards may use comparisons, Boolean evaluation, math operations, and type-test BIFs, but not user-defined functions (because of side effects) (Hébert, ch. 3, "Guards, Guards!").

## Prerequisites

- **Pattern matching** — Guards augment pattern matching in function heads
- **Boolean and comparison operators** — Guard expressions are built from these

## Key Properties

1. Introduced by the `when` keyword in a function head.
2. Must return `true` to succeed; `false` or an exception means failure.
3. Comma `,` joins guards like `andalso`; semicolon `;` like `orelse`.
4. `,`/`;` catch exceptions in sub-expressions; `andalso`/`orelse` do not.
5. Only `andalso`/`orelse` (not `,`/`;`) can be nested inside guards.
6. Allowed: comparisons, Boolean ops, math ops, and type-test BIFs.
7. User-defined functions are not allowed in guards.

## Construction / Recognition

To add a guard to a function clause:

1. Write the clause head.
2. Append `when GuardExpression` before the `->`.
3. Combine multiple guard tests with `,` (all must pass) or `;` (any may pass).

## Context & Application

Guards solve the problem that patterns cannot count or check ranges — e.g., is a driver between 16 and 104 years old? They convert an impractical list of literal clauses into a concise check.

## Examples

**Example** (ch. 3): `old_enough(X) when X >= 16 -> true; old_enough(_) -> false.`

**Example** (ch. 3): `right_age(X) when X >= 16, X =< 104 -> true; right_age(_) -> false.` requires both tests to pass.

## Relationships

### Prerequisites

- **Pattern matching** — Guards extend matching
- **Boolean and comparison operators** — Building blocks of guard expressions

### Builds Upon

- **Pattern matching** — Guards add range/type expressiveness

### Related

- **Function clause** — Guards live in clause heads
- **If expression** — `if` clauses are guard patterns used outside a function head
- **Type-test BIF** — Type-test BIFs are among the few functions allowed in guards

## Common Errors

- **Error**: Calling a user-defined function inside a guard
  **Correction**: Only BIFs (comparisons, math, type tests) are permitted in guards

## Common Confusions

- **Confusion**: Treating `,`/`;` in guards as exactly equivalent to `andalso`/`orelse`
  **Clarification**: `,`/`;` catch exceptions; `andalso`/`orelse` do not, and only the latter nest

## Source Reference

Chapter 3: "Syntax in Functions," section "Guards, Guards!"

## Verification Notes

- Definition: Adapted from the "Guards, Guards!" section
- Confidence: HIGH — explicit section
- Uncertainties: None
