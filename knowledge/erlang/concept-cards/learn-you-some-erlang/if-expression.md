---
concept: If Expression
slug: if-expression
category: functions-pattern-matching
subcategory: control-flow
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "What the If ?!"
extraction_confidence: high
aliases:
  - "if clause"
  - "guard pattern"
prerequisites:
  - guard
extends: []
related:
  - case-expression
  - function-clause
contrasts_with:
  - case-expression
answers_questions:
  - "What is a guard?"
---

# If Expression

## Quick Definition

An Erlang `if` expression acts like a guard outside a function head: it picks the first branch whose guard evaluates to `true`. Its branches are called guard patterns.

## Core Definition

An `if` clause acts like a guard and shares the guard syntax, but outside a function clause's head; `if` clauses are called *guard patterns*. Unlike `if` in most languages, Erlang's `if` must return something, so if no guard succeeds it crashes with "no true branch found." A catchall branch is written with the atom `true` (Erlang's equivalent of `else`), though the book recommends covering all logical ends rather than relying on a `true` catchall (Hébert, ch. 3, "What the If ?!").

## Prerequisites

- **Guard** — `if` branches use guard syntax and semantics

## Key Properties

1. Uses guard syntax, but outside a function head.
2. Each branch is a guard pattern: `Guard -> Expression`.
3. Always returns a value; if no branch succeeds it raises an error.
4. `true` serves as the catchall ("else") branch.
5. The compiler warns when a branch's guard always evaluates to `false`.
6. Erlang has no null value, so every branch must produce a result.

## Construction / Recognition

To write an `if` expression:

1. Write `if Guard1 -> Expr1; Guard2 -> Expr2; ... end`.
2. Optionally add `true -> Expr` as a catchall.

## Context & Application

`if` was added as a short way to use guards without writing a full pattern-matching head. The book recommends covering all logical cases explicitly (e.g., `X > Y`, `X < Y`, `X == Y`) rather than relying on a `true` branch.

## Examples

**Example** (ch. 3): `oh_god(N) -> if N =:= 2 -> might_succeed; true -> always_does end.`

**Example** (ch. 3): An `if` with only `1 =:= 2, 1 =:= 1 -> fails` crashes with "no true branch found."

## Relationships

### Prerequisites

- **Guard** — `if` branches are guards

### Related

- **Case expression** — `case ... of` is the pattern-matching alternative
- **Function clause** — `if` is a compact alternative to guarded clauses

### Contrasts With

- **Case expression** — `case` matches patterns on a value; `if` only evaluates guards

## Common Errors

- **Error**: Writing an `if` with no branch that can succeed
  **Correction**: Cover all cases or add a `true` catchall; `if` must return a value

## Common Confusions

- **Confusion**: Expecting Erlang's `if` to behave like `if` in C-style languages
  **Clarification**: It is a set of guard patterns, not a true/false branch; it crashes if none match

## Source Reference

Chapter 3: "Syntax in Functions," section "What the If ?!"

## Verification Notes

- Definition: Adapted from the "What the If ?!" section
- Confidence: HIGH — explicit section
- Uncertainties: None
