---
concept: Recursion
slug: recursion
category: functions-pattern-matching
subcategory: recursion
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Hello Recursion!"
chapter_number: 5
pdf_page: null
section: "How Recursion Works"
extraction_confidence: high
aliases:
  - "base case"
  - "recursive function"
prerequisites:
  - function-clause
  - pattern-matching
extends: []
related:
  - tail-recursion
  - accumulator
  - thinking-recursively
  - cons-and-list-operations
contrasts_with:
  - tail-recursion
answers_questions:
  - "How do I write a recursive function?"
---

# Recursion

## Quick Definition

Recursion is a function that calls itself. It is the looping construct of functional languages, since Erlang has no `for` or `while`.

## Core Definition

Functional programming languages usually do not offer looping constructs like `for` and `while`; instead, functional programmers rely on recursion. "A function that calls itself" is one way to define recursion. However, a function calling itself is not enough: it also needs a stopping condition called a *base case* — a function clause that returns a value rather than calling the function again. Without a base case, the function would continue forever (Hébert, ch. 5, "How Recursion Works").

## Prerequisites

- **Function clause** — Recursive functions use multiple clauses, one for the base case
- **Pattern matching** — Clauses are selected by matching, typically `[]` vs. `[H|T]`

## Key Properties

1. A recursive function calls itself.
2. It must have a base case — a clause that returns without recursing.
3. Non-base clauses must converge toward the base case.
4. Recursion is the primary looping construct in Erlang (plus list comprehensions).
5. The factorial and list-length functions are canonical recursion examples.

## Construction / Recognition

To write a recursive function:

1. Identify and write the base case first (the simplest input).
2. Write the recursive case so it moves toward the base case.
3. Combine the cases as separate function clauses.

## Context & Application

Recursion replaces loops everywhere in Erlang. It is also useful in every other functional language. The base-case-first approach makes recursive functions easier to write.

## Examples

**Example** (ch. 5): `fac(0) -> 1; fac(N) when N > 0 -> N*fac(N-1).` is the recursive factorial.

**Example** (ch. 5): `len([]) -> 0; len([_|T]) -> 1 + len(T).` recursively counts list elements.

## Relationships

### Prerequisites

- **Function clause** — The base and recursive cases are separate clauses
- **Pattern matching** — Clause selection drives the recursion

### Related

- **Tail recursion** — A space-efficient form of recursion
- **Accumulator** — A parameter used to make recursion tail recursive
- **Thinking recursively** — The declarative mindset for designing recursive functions
- **Cons and list operations** — `[H|T]` decomposition powers list recursion

### Contrasts With

- **Tail recursion** — Plain recursion stacks operations; tail recursion does not

## Common Errors

- **Error**: Writing a recursive function with no base case
  **Correction**: Always include a clause that returns without recursing

## Common Confusions

- **Confusion**: Believing Erlang must have hidden loop constructs
  **Clarification**: There is no `for`/`while`; recursion (and comprehensions) is the looping mechanism

## Source Reference

Chapter 5: "Hello Recursion!", section "How Recursion Works."

## Verification Notes

- Definition: Adapted from the "How Recursion Works" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
