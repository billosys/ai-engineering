---
concept: Accumulator
slug: accumulator
category: functions-pattern-matching
subcategory: recursion
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Hello Recursion!"
chapter_number: 5
pdf_page: null
section: "Length of a Tail Recursion"
extraction_confidence: high
aliases:
  - "acc"
  - "temporary variable"
prerequisites:
  - recursion
extends: []
related:
  - tail-recursion
  - fold
contrasts_with: []
answers_questions:
  - "How does tail recursion relate to accumulators?"
  - "How do I write a recursive function?"
---

# Accumulator

## Quick Definition

An accumulator is an extra parameter that stores the running results of a recursive computation, enabling tail recursion by limiting the growth of calls.

## Core Definition

An accumulator is a temporary variable held as a parameter in a function, acting as a place to store the results of computations as they happen, in order to limit the growth of recursive calls. It is the mechanism that turns a plain recursive function into a tail-recursive one: the work is reduced into the accumulator argument as the recursion happens, rather than being stacked up for after the recursion returns. An accumulator can be a single value or a list (Hébert, ch. 5, "Length of a Tail Recursion" and "Fold Everything").

## Prerequisites

- **Recursion** — Accumulators are added to recursive functions

## Key Properties

1. An extra parameter that carries the running result.
2. Enables tail recursion by reducing work as the recursion proceeds.
3. Can be a single value (e.g., a count, a product) or a list.
4. Often introduced via a wrapper function of lower arity that supplies the initial value.
5. When the accumulator is a list built by prepending, the result comes out reversed.

## Construction / Recognition

To add an accumulator:

1. Write a wrapper function that calls the worker with an initial accumulator value.
2. In the worker, fold the per-step computation into the accumulator argument.
3. Return the accumulator in the base case.

## Context & Application

Accumulators combined with last call optimization are what make tail recursion useful. When an accumulator list is built by prepending heads, the final result is reversed (as in `tail_reverse`), so a deliberate reversal may be needed (as in `tail_sublist`).

## Examples

**Example** (ch. 5): In `tail_fac(N,Acc) when N > 0 -> tail_fac(N-1,N*Acc).`, `Acc` accumulates the running product.

**Example** (ch. 5): `tail_reverse([H|T],Acc) -> tail_reverse(T, [H|Acc]).` uses a list accumulator that naturally reverses the list.

## Relationships

### Prerequisites

- **Recursion** — Accumulators are added to recursive functions

### Related

- **Tail recursion** — Accumulators are the means to achieve tail recursion
- **Fold** — A fold's running value is essentially an accumulator

## Common Errors

- **Error**: Forgetting that a prepend-built accumulator reverses the result
  **Correction**: Reverse the accumulator at the end if order matters (e.g., `lists:reverse/1`)

## Common Confusions

- **Confusion**: Thinking an accumulator must be a number
  **Clarification**: An accumulator can be any term, including a list used to build a result

## Source Reference

Chapter 5: "Hello Recursion!", sections "Length of a Tail Recursion," "A Reverse Function," and "A Sublist Function."

## Verification Notes

- Definition: Adapted from the accumulator discussion across chapter 5
- Confidence: HIGH — explicit, repeated treatment
- Uncertainties: None
