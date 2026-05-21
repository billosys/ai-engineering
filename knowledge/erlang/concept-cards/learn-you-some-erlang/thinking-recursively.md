---
concept: Thinking Recursively
slug: thinking-recursively
category: core-idioms
subcategory: recursion
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Hello Recursion!"
chapter_number: 5
pdf_page: null
section: "Thinking Recursively"
extraction_confidence: high
aliases:
  - "recursive mindset"
  - "declarative recursion"
prerequisites:
  - recursion
extends: []
related:
  - tail-recursion
  - pattern-matching
contrasts_with: []
answers_questions:
  - "How do I write a recursive function?"
---

# Thinking Recursively

## Quick Definition

Thinking recursively means designing solutions declaratively — "if you get this input, do that; otherwise do this" — rather than as a step-by-step imperative sequence.

## Core Definition

A different aspect of recursive definitions compared to their imperative counterparts (usually `while` or `for` loops) is that, instead of a step-by-step approach ("do this, then that, then you're finished"), the approach is declarative ("if you get this input, do that; otherwise, do this"). This property is made more obvious by pattern matching in function heads. Recursion coupled with pattern matching is often an optimal solution for writing concise, easy-to-understand algorithms: by subdividing a problem into separate functions until they can no longer be simplified, the algorithm becomes the assembly of correct answers from short routines. The regular pattern is: find the base cases and write them down, then make all other cases converge toward them (Hébert, ch. 5, "Thinking Recursively").

## Prerequisites

- **Recursion** — Thinking recursively is the mindset for designing recursive functions

## Key Properties

1. Declarative ("if input X, do Y") rather than imperative step-by-step.
2. Made clearer by pattern matching in function heads.
3. The regular pattern: write the base cases first, then make other cases converge to them.
4. Problems are subdivided into short routines whose answers are assembled.
5. Erlang's standard library has already abstracted many recursive patterns into reusable functions.

## Construction / Recognition

To think recursively about a problem:

1. Identify the base case(s) — the simplest input(s) with a direct answer.
2. Define each other case so it moves toward a base case.
3. Trust the recursive call to handle the smaller subproblem.

## Context & Application

The recursive mindset transfers to every functional language. The book notes that because many common recursive patterns (accumulators, reversing, mapping, folding) recur so often, they have been abstracted into library functions and higher-order functions — so you rarely need to write recursion by hand.

## Examples

**Example** (ch. 5): The quicksort implementation is built by subdividing the problem into a `partition` routine and a recursive `quicksort` glue function, each simple on its own.

## Relationships

### Prerequisites

- **Recursion** — The mechanism this mindset applies to

### Related

- **Tail recursion** — A space-efficient form arrived at by the same mindset
- **Pattern matching** — Makes recursive case analysis explicit in function heads

## Common Errors

- **Error**: Trying to trace every step of a recursion mentally like a loop
  **Correction**: Trust the base case and the converging recursive case; reason declaratively

## Common Confusions

- **Confusion**: Believing recursion is only for educational, non-tail-recursive examples
  **Clarification**: The mindset underlies real code; abstractions like folds and HOFs are built on it

## Source Reference

Chapter 5: "Hello Recursion!", section "Thinking Recursively" and "The Author vs. Himself" sidebar.

## Verification Notes

- Definition: Adapted from the "Thinking Recursively" section
- Confidence: HIGH — explicit section
- Uncertainties: None
