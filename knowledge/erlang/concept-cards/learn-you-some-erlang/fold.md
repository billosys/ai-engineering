---
concept: Fold
slug: fold
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Higher-Order Functions"
chapter_number: 6
pdf_page: null
section: "Fold Everything"
extraction_confidence: high
aliases:
  - "fold/3"
  - "lists:foldl"
  - "lists:foldr"
  - "reduce"
prerequisites:
  - higher-order-function
  - accumulator
extends: []
related:
  - map-higher-order-function
  - filter-higher-order-function
contrasts_with: []
answers_questions:
  - "How does fold relate to map and filter?"
---

# Fold

## Quick Definition

A fold is a higher-order function that applies an operation across a list to reduce it to a single value, starting from an initial value.

## Core Definition

A fold applies an operation to each element of a list successively to reduce the elements to a single value. Its definition is `fold(_, Start, []) -> Start; fold(F, Start, [H|T]) -> fold(F, F(H,Start), T).`. Every fold needs an initial value to start with (e.g., `0` for sums, `1` for products, or the first list element for min/max); since a suitable start cannot always be decided automatically, it is left to the programmer. Folding is universal: because an accumulator can be a single value or a list, almost any recursive function over lists — including `map` and `filter` — can be implemented as a fold. The standard library provides `lists:foldl/3` and `lists:foldr/3` (Hébert, ch. 6, "Fold Everything").

## Prerequisites

- **Higher-order function** — A fold takes a combining function as an argument
- **Accumulator** — A fold's running value is an accumulator

## Key Properties

1. Reduces a list to a single value via a combining function.
2. Definition: `fold(_, Start, []) -> Start; fold(F, Start, [H|T]) -> fold(F, F(H,Start), T).`.
3. Requires an explicit initial value supplied by the programmer.
4. The accumulator may be a single value or a list.
5. Universal: `map`, `filter`, and `reverse` can all be expressed as folds.
6. `lists:foldl/3` and `lists:foldr/3` are the standard library versions.

## Construction / Recognition

To use a fold:

1. Choose an initial value appropriate to the operation.
2. Supply a combining function `F(Element, Acc)`.
3. Call `fold(F, Start, List)`; the result is the final accumulator.

## Context & Application

Fold subsumes `max`, `min`, and `sum`, all of which reduce a list to one value. It is the most general list abstraction in the chapter — `map` and `filter` are special cases. Pretty much any recursive function reducing a list can be expressed as a fold.

## Examples

**Example** (ch. 6): `hhfuns:fold(fun(A,B) -> A + B end, 0, lists:seq(1,6)).` returns `21`.

**Example** (ch. 6): `reverse(L) -> fold(fun(X,Acc) -> [X|Acc] end, [], L).` reverses a list using a fold.

## Relationships

### Prerequisites

- **Higher-order function** — Fold takes a combining function
- **Accumulator** — The fold's running value is an accumulator

### Related

- **Map higher-order function** — A special case of fold (build a transformed list)
- **Filter higher-order function** — A special case of fold (build a filtered list)

## Common Errors

- **Error**: Using `0` as the starting value for a min/max over negative numbers
  **Correction**: Use the first list element as the start when no neutral value exists

## Common Confusions

- **Confusion**: Thinking fold can only produce scalars
  **Clarification**: The accumulator can be a list, so fold can build lists — even implement `map`/`filter`

## Source Reference

Chapter 6: "Higher-Order Functions," section "Fold Everything."

## Verification Notes

- Definition: Adapted from the "Fold Everything" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
