---
concept: Map (Higher-Order Function)
slug: map-higher-order-function
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Higher-Order Functions"
chapter_number: 6
pdf_page: null
section: "Let's Get Functional"
extraction_confidence: high
aliases:
  - "map/2"
  - "lists:map"
prerequisites:
  - higher-order-function
  - recursion
extends: []
related:
  - filter-higher-order-function
  - fold
  - list-comprehension
contrasts_with:
  - filter-higher-order-function
answers_questions:
  - "How does fold relate to map and filter?"
---

# Map (Higher-Order Function)

## Quick Definition

`map/2` is a higher-order function that applies a given function to every element of a list, returning a list of the results.

## Core Definition

`map/2` abstracts the common recursive pattern of cycling through a list, applying a function to each element, and recursing. Its definition is `map(_, []) -> []; map(F, [H|T]) -> [F(H)|map(F,T)].`. Once `map/2` exists, applying a function to each element of a list only requires calling `map/2` with that function as a parameter, rather than writing a new recursive function each time. The standard library provides `lists:map/2` (Hébert, ch. 6, "Let's Get Functional" and "More Abstractions").

## Prerequisites

- **Higher-order function** — `map` takes a function as an argument
- **Recursion** — `map` abstracts a recursive list pattern

## Key Properties

1. Applies a function `F` to every element of a list.
2. Returns a new list of the same length with transformed elements.
3. Definition: `map(_, []) -> []; map(F, [H|T]) -> [F(H)|map(F,T)].`.
4. `lists:map/2` is the standard library version.
5. Can itself be implemented in terms of `fold`.

## Construction / Recognition

To use `map`:

1. Define or pass a function that transforms one element.
2. Call `map(Function, List)`.
3. Receive the list of transformed results.

## Context & Application

`map` removes the boilerplate of writing a fresh recursive function (`increment`, `decrement`, etc.) every time you want to transform a list. The book also shows `map` can be built from `fold`.

## Examples

**Example** (ch. 6): `hhfuns:map(fun(X) -> X + 1 end, L).` returns `[2,3,4,5,6]` for `L = [1,2,3,4,5]`.

**Example** (ch. 6): `map2(F,L) -> reverse(fold(fun(X,Acc) -> [F(X)|Acc] end, [], L)).` re-implements `map` via `fold`.

## Relationships

### Prerequisites

- **Higher-order function** — `map` accepts a function
- **Recursion** — `map` abstracts recursion over a list

### Related

- **Filter higher-order function** — Selects elements rather than transforming them
- **Fold** — More general; `map` can be expressed as a `fold`
- **List comprehension** — Comprehensions also transform every element

### Contrasts With

- **Filter higher-order function** — `map` transforms each element; `filter` keeps or drops them

## Common Errors

- **Error**: Expecting `map` to change the list length
  **Correction**: `map` returns a list of the same length; use `filter` to drop elements

## Common Confusions

- **Confusion**: Thinking `map` reduces a list
  **Clarification**: `map` transforms element-by-element; `fold` reduces to a single value

## Source Reference

Chapter 6: "Higher-Order Functions," sections "Let's Get Functional" and "More Abstractions."

## Verification Notes

- Definition: Adapted from the `map/2` discussion
- Confidence: HIGH — explicit definition and examples
- Uncertainties: None
