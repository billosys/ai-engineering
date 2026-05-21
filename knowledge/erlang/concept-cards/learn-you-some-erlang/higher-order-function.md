---
concept: Higher-Order Function
slug: higher-order-function
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
  - "HOF"
  - "fun reference"
prerequisites:
  - function-clause
  - recursion
extends: []
related:
  - anonymous-function
  - map-higher-order-function
  - filter-higher-order-function
  - fold
contrasts_with: []
answers_questions:
  - "How do I write a recursive function?"
---

# Higher-Order Function

## Quick Definition

A higher-order function is a function that accepts other functions as parameters. It is a powerful means of abstraction in Erlang.

## Core Definition

A higher-order function is a function that can accept other functions as parameters. Passing a function as a parameter binds it to a variable, which can then be used like any other variable within the function. The concept is rooted in lambda calculus. To pass a function defined outside a module, Erlang uses the notation `fun Module:Function/Arity`, which tells the VM to use that specific function and bind it to a variable. Function names written without a parameter list are interpreted as atoms, and atoms cannot be called as functions (Hébert, ch. 6, "Let's Get Functional").

## Prerequisites

- **Function clause** — Higher-order functions are ordinary functions defined with clauses
- **Recursion** — HOFs like `map`/`filter`/`fold` abstract recursive list patterns

## Key Properties

1. Accepts one or more functions as arguments.
2. A function passed in is bound to a variable and called like any value.
3. `fun Module:Function/Arity` references an exported function.
4. A bare function name is an atom, not a callable function.
5. HOFs are a powerful means of abstraction — among the best tools in Erlang.

## Construction / Recognition

To pass a named function to a higher-order function:

1. Write `fun Module:Function/Arity` to reference it.
2. Pass that reference as an argument.

## Context & Application

Higher-order functions let you abstract away the repetitive parts of recursive list code — such as cycling through a list and applying a function — so only the varying part (the function) is supplied. `map`, `filter`, and `fold` are the canonical examples.

## Examples

**Example** (ch. 6): `hhfuns:add(fun hhfuns:one/0, fun hhfuns:two/0).` returns `3`; passing the bare atoms `one, two` fails with "bad function."

**Example** (ch. 6): `hhfuns:map(fun hhfuns:incr/1, L)` applies `incr/1` to each element of `L`.

## Relationships

### Prerequisites

- **Function clause** — HOFs are regular functions
- **Recursion** — HOFs abstract recursive patterns

### Related

- **Anonymous function** — Funs are commonly passed to HOFs
- **Map higher-order function** — A HOF that transforms each element
- **Filter higher-order function** — A HOF that keeps elements passing a predicate
- **Fold** — A HOF that reduces a list to a single value

## Common Errors

- **Error**: Passing a bare function name like `one` instead of `fun hhfuns:one/0`
  **Correction**: A bare name is an atom; use the `fun Module:Function/Arity` form

## Common Confusions

- **Confusion**: Thinking only anonymous functions can be passed around
  **Clarification**: Named exported functions can be passed via `fun Module:Function/Arity`

## Source Reference

Chapter 6: "Higher-Order Functions," section "Let's Get Functional."

## Verification Notes

- Definition: Adapted from the "Let's Get Functional" section
- Confidence: HIGH — explicit section
- Uncertainties: None
