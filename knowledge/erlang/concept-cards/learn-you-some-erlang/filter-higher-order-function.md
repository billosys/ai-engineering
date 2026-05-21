---
concept: Filter (Higher-Order Function)
slug: filter-higher-order-function
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Higher-Order Functions"
chapter_number: 6
pdf_page: null
section: "Filters"
extraction_confidence: high
aliases:
  - "filter/2"
  - "lists:filter"
  - "predicate"
prerequisites:
  - higher-order-function
  - recursion
extends: []
related:
  - map-higher-order-function
  - fold
  - list-comprehension
contrasts_with:
  - map-higher-order-function
answers_questions:
  - "How does fold relate to map and filter?"
---

# Filter (Higher-Order Function)

## Quick Definition

`filter/2` is a higher-order function that keeps only the elements of a list that satisfy a predicate, dropping the rest.

## Core Definition

`filter/2` abstracts the common pattern of operating on a list, keeping elements that succeed some test (a *predicate*) and dropping the others. Its definition uses an accumulator and a `case` on the predicate result: `filter(Pred, [H|T], Acc) -> case Pred(H) of true -> filter(Pred, T, [H|Acc]); false -> filter(Pred, T, Acc) end.`, with the result reversed at the end. Using `filter/2`, the programmer needs only to supply the predicate and the list; the act of cycling through the list to discard unwanted items is abstracted away (Hébert, ch. 6, "Filters").

## Prerequisites

- **Higher-order function** — `filter` takes a predicate function
- **Recursion** — `filter` abstracts a recursive list pattern

## Key Properties

1. Takes a predicate and a list.
2. A predicate is a function returning a Boolean for each element.
3. Keeps elements for which the predicate returns `true`.
4. Returns a list that may be shorter than the input.
5. `lists:filter/2` is the standard library version.
6. Can itself be implemented in terms of `fold`.

## Construction / Recognition

To use `filter`:

1. Define a predicate function returning `true`/`false` for one element.
2. Call `filter(Predicate, List)`.
3. Receive the list of elements that passed.

## Context & Application

`filter` replaces hand-written functions like `even/1` or `old_men/1` that each cycle a list keeping matching elements. The general rule: get rid of what is always the same and let the programmer supply only the part that changes.

## Examples

**Example** (ch. 6): `hhfuns:filter(fun(X) -> X rem 2 == 0 end, Numbers).` returns `[2,4,6,8,10]`.

**Example** (ch. 6): `hhfuns:filter(fun({Gender,Age}) -> Gender == male andalso Age > 60 end, People).` keeps males over 60.

## Relationships

### Prerequisites

- **Higher-order function** — `filter` accepts a predicate
- **Recursion** — `filter` abstracts recursion over a list

### Related

- **Map higher-order function** — Transforms elements rather than selecting them
- **Fold** — More general; `filter` can be expressed as a `fold`
- **List comprehension** — Comprehension conditions do the same selection

### Contrasts With

- **Map higher-order function** — `filter` keeps/drops elements; `map` transforms all of them

## Common Errors

- **Error**: Passing a predicate that does not return a Boolean
  **Correction**: A predicate must return `true` or `false`; `filter` branches on that

## Common Confusions

- **Confusion**: Expecting `filter` to transform elements
  **Clarification**: `filter` only selects; use `map` to transform

## Source Reference

Chapter 6: "Higher-Order Functions," section "Filters."

## Verification Notes

- Definition: Adapted from the "Filters" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
