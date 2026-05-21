---
concept: Case Expression
slug: case-expression
category: functions-pattern-matching
subcategory: control-flow
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "In case ... of"
extraction_confidence: high
aliases:
  - "case ... of"
prerequisites:
  - pattern-matching
  - guard
extends: []
related:
  - if-expression
  - function-clause
contrasts_with:
  - if-expression
answers_questions:
  - "What is pattern matching?"
---

# Case Expression

## Quick Definition

A `case ... of` expression evaluates an expression and selects a branch by pattern matching, with optional guards — like a function head used inline.

## Core Definition

If the `if` expression is like a guard, a `case ... of` expression is like a whole function head: it offers the complex pattern matching available for each argument of a function, plus guards. A case expression matches the value of an expression against patterns (with optional guards) and runs the first matching branch's body. Functionally, `case ... of` is essentially equivalent to a set of function heads with guards; the two are represented the same way at a lower level and have the same performance cost (Hébert, ch. 3, "In case ... of" and "Which Should We Use?").

## Prerequisites

- **Pattern matching** — Case branches select by matching
- **Guard** — Case branches may include guards

## Key Properties

1. Syntax: `case Expression of Pattern [Guard] -> Body; ... end`.
2. Branches use full pattern matching plus optional guards.
3. The first matching branch's body runs.
4. Equivalent in power and performance to guarded function clauses.
5. To match multiple values, build a tuple: `case {A,B} of ... end`.
6. Failing all branches raises a case clause error.

## Construction / Recognition

To write a case expression:

1. Write `case Expr of`.
2. List `Pattern [when Guard] -> Body` branches separated by `;`.
3. End with `end`.

## Context & Application

`case ... of` is preferred when branching on a single value with rich patterns/guards (e.g., `insert/2` checking `lists:member`). For branching on multiple arguments, a multi-clause function is often cleaner than wrapping arguments in a tuple.

## Examples

**Example** (ch. 3): `case lists:member(X,Set) of true -> Set; false -> [X|Set] end` decides whether to add an element.

**Example** (ch. 3): `beach(Temperature)` uses a case with guarded branches for Celsius, Kelvin, and Fahrenheit ranges.

## Relationships

### Prerequisites

- **Pattern matching** — Case branches match patterns
- **Guard** — Case branches may carry guards

### Related

- **If expression** — A guard-only alternative
- **Function clause** — `case` branches mirror guarded function clauses

### Contrasts With

- **If expression** — `if` only evaluates guards; `case` matches patterns on a value

## Common Errors

- **Error**: Forgetting a possible value, causing a case clause error
  **Correction**: Cover all cases or add a `_` catchall branch

## Common Confusions

- **Confusion**: Believing `case` is faster or slower than function calls
  **Clarification**: `case` and function clauses are represented the same way with the same cost

## Source Reference

Chapter 3: "Syntax in Functions," sections "In case ... of" and "Which Should We Use?"

## Verification Notes

- Definition: Adapted from the "In case ... of" section
- Confidence: HIGH — explicit section
- Uncertainties: None
