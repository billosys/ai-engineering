---
concept: Pattern Matching
slug: pattern-matching
category: functions-pattern-matching
subcategory: pattern-matching
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "Pattern Matching"
extraction_confidence: high
aliases:
  - "match"
prerequisites:
  - variable
  - tuple
  - list
extends: []
related:
  - function-clause
  - bound-variable-in-pattern
  - guard
  - case-expression
contrasts_with: []
answers_questions:
  - "What is pattern matching?"
  - "How do I write a recursive function?"
---

# Pattern Matching

## Quick Definition

Pattern matching lets you select which part of a function runs and bind values at the same time, by comparing data against patterns rather than testing values with explicit conditionals.

## Core Definition

Pattern matching, which underlies the `=` operator's behavior, lets Erlang compare and assign variables in structures such as lists and tuples. When defining functions, Erlang uses pattern matching to decide which parts of a function should be used and to bind the needed values at the same time — there is no need to first bind values and then compare them. This produces a declarative style. Pattern matching can specify precise values (a known number or atom) or abstract shapes (a list head/tail, an N-element tuple, `_` or unbound variables), but it cannot express ranges of values or type tests — that requires guards (Hébert, ch. 3, "Pattern Matching").

## Prerequisites

- **Variable** — Matching binds unbound variables
- **Tuple** — Tuple patterns are a common matching target
- **List** — List patterns (head/tail) are a common matching target

## Key Properties

1. Combines value binding and value comparison in one step.
2. Replaces chains of imperative `if`/`else` with declarative function clauses.
3. Can match precise values (atoms, numbers) or abstract shapes.
4. The `_` wildcard matches anything and discards the value.
5. Cannot express ranges or type tests — guards are needed for those.
6. The `=` operator can match a value to both a structure and its parts in one head, e.g., `Date = {Y,M,D}`.

## Construction / Recognition

To use pattern matching in a function:

1. Write multiple function clauses with patterns in their heads.
2. Erlang tries each clause in order, running the first whose pattern matches.

## Context & Application

Pattern matching saves boilerplate: a `greet` function dispatching on gender becomes three clauses instead of a conditional cascade. It is the basis of recursive functions, `case ... of`, and binary/list decomposition.

## Examples

**Example** (ch. 3): `greet(male, Name) -> ...; greet(female, Name) -> ...; greet(_, Name) -> ...` dispatches by matching the first argument.

**Example** (ch. 3): `valid_time({Date = {Y,M,D}, Time = {H,Min,S}}) -> ...` matches a nested tuple while also binding the whole inner tuples.

## Relationships

### Prerequisites

- **Variable** — Patterns bind unbound variables
- **Tuple** — Tuple patterns
- **List** — List head/tail patterns

### Related

- **Function clause** — Each clause has a pattern in its head
- **Bound variable in pattern** — A pattern may reuse an already-bound variable
- **Guard** — Guards add the range/type expressiveness patterns lack
- **Case expression** — `case ... of` is pattern matching outside a function head

## Common Errors

- **Error**: Trying to match a value range with a plain pattern
  **Correction**: Use guards for ranges and type tests; patterns only match shapes and exact values

## Common Confusions

- **Confusion**: Thinking pattern matching is just assignment
  **Clarification**: It both binds variables and verifies structure/values, dispatching control flow

## Source Reference

Chapter 3: "Syntax in Functions," section "Pattern Matching."

## Verification Notes

- Definition: Adapted from the "Pattern Matching" section
- Confidence: HIGH — explicit, central treatment
- Uncertainties: None
