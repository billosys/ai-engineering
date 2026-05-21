---
concept: List Comprehension
slug: list-comprehension
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "List Comprehensions"
extraction_confidence: high
aliases:
  - "generator expression"
prerequisites:
  - list
  - pattern-matching
  - boolean-and-comparison-operators
extends: []
related:
  - binary-comprehension
  - map-higher-order-function
  - filter-higher-order-function
contrasts_with:
  - binary-comprehension
answers_questions:
  - "What is a list comprehension?"
  - "How does a list comprehension relate to a binary comprehension?"
---

# List Comprehension

## Quick Definition

A list comprehension is a concise way to build or modify lists, based on mathematical set notation. It maps an expression over generators while filtering with conditions.

## Core Definition

List comprehensions are ways to build or modify lists, based on the mathematical idea of set notation. The recipe is `NewList = [Expression || Pattern <- List, Condition1, ..., ConditionN]`, where `Pattern <- List` is a *generator expression*. The arrow `<-` acts like the `=` operator except that it does not throw exceptions, so generator patterns can also act as filters: non-matching elements are simply ignored. A comprehension may have more than one generator, in which case it iterates over every combination (Hébert, ch. 1, "List Comprehensions").

## Prerequisites

- **List** — Comprehensions consume and produce lists
- **Pattern matching** — Generator patterns pattern-match each element
- **Boolean and comparison operators** — Conditions are Boolean-valued expressions

## Key Properties

1. Syntax: `[Expression || GeneratorExp1, ..., Condition1, ...]`.
2. `Pattern <- List` is a generator expression; `<-` is like `=` but does not raise exceptions.
3. Conditions are Boolean expressions that filter elements.
4. Multiple generators iterate over all combinations of their elements.
5. A non-matching generator pattern silently drops that element (acting as a filter).

## Construction / Recognition

To build a list comprehension:

1. Write the result expression on the left of `||`.
2. Add one or more generator expressions `Pattern <- List`.
3. Optionally add Boolean conditions to filter elements.

## Context & Application

List comprehensions make programs short and easy to understand compared to manual list manipulation. They are used to apply a function to each element of a list while enforcing constraints — e.g., menu prices between $3 and $10 with tax added.

## Examples

**Example** (ch. 1): `[2*N || N <- [1,2,3,4]].` returns `[2,4,6,8]`.

**Example** (ch. 1): `[X || X <- [1,2,3,4,5,6,7,8,9,10], X rem 2 =:= 0].` returns `[2,4,6,8,10]`.

**Example** (ch. 1): `[X || {X, fog} <- Weather].` extracts cities whose weather tuple matches `{X, fog}`, ignoring the rest.

## Relationships

### Prerequisites

- **List** — Input and output structure
- **Pattern matching** — Generator patterns match elements
- **Boolean and comparison operators** — Conditions filter elements

### Related

- **Binary comprehension** — The same idea applied to binaries
- **Map higher-order function** — Comprehensions and `map` both transform every element
- **Filter higher-order function** — Comprehension conditions parallel `filter`

### Contrasts With

- **Binary comprehension** — Uses `<=` and binaries instead of `<-` and lists

## Common Errors

- **Error**: Expecting a non-matching generator pattern to raise an exception
  **Correction**: It silently drops the element; `<-` does not throw

## Common Confusions

- **Confusion**: Thinking conditions come before generators
  **Clarification**: Generators come first, then conditions

## Source Reference

Chapter 1: "Starting Out," section "List Comprehensions."

## Verification Notes

- Definition: Adapted from the section with set-notation analogy
- Confidence: HIGH — explicit section with multiple examples
- Uncertainties: None
