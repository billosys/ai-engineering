---
concept: Anonymous Function
slug: anonymous-function
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Higher-Order Functions"
chapter_number: 6
pdf_page: null
section: "Anonymous Functions"
extraction_confidence: high
aliases:
  - "fun"
  - "lambda"
  - "inline function"
prerequisites:
  - higher-order-function
extends: []
related:
  - closure
  - function-scope
  - map-higher-order-function
contrasts_with: []
answers_questions:
  - "What is an anonymous function (fun)?"
---

# Anonymous Function

## Quick Definition

An anonymous function (a "fun") is a function declared inline without a name, usable wherever a function value is needed.

## Core Definition

Anonymous functions, or *funs*, address the problem of using functions as parameters by letting you declare a special kind of function inline, without naming it. Anonymous functions can do almost everything normal functions can — including multiple clauses with guards — except call themselves recursively (since they are anonymous). The syntax is `fun(Args1) -> Expr...; (Args2) -> Expr... end` (Hébert, ch. 6, "Anonymous Functions").

## Prerequisites

- **Higher-order function** — Funs exist mainly to be passed to higher-order functions

## Key Properties

1. Declared inline with `fun ... end`, with no name.
2. Can have multiple clauses with guards, like named functions.
3. Cannot call themselves recursively (they have no name).
4. Can be assigned to a variable and called via that variable: `Fn()`.
5. Avoid the chore of naming, exporting, and compiling a one-off function.

## Construction / Recognition

To write an anonymous function:

1. Write `fun(Args) -> Body end`.
2. Optionally add more clauses separated by `;`.
3. Assign it to a variable or pass it directly to a higher-order function.

## Context & Application

Anonymous functions make abstraction practical at a low level: instead of putting every function passed to `map/2` in a module, you declare it on the fly. Funs let you focus on what is done rather than how to loop.

## Examples

**Example** (ch. 6): `Fn = fun() -> a end.` then `Fn().` returns `a`.

**Example** (ch. 6): `hhfuns:map(fun(X) -> X + 1 end, L).` returns `[2,3,4,5,6]` for `L = [1,2,3,4,5]`.

## Relationships

### Prerequisites

- **Higher-order function** — Funs are passed to HOFs

### Related

- **Closure** — A fun that captures variables from its scope is a closure
- **Function scope** — A fun inherits the scope where it is declared
- **Map higher-order function** — Funs are commonly passed to `map`

## Common Errors

- **Error**: Trying to make an anonymous function call itself recursively
  **Correction**: Recursion needs a name; use a named function or a separate construct

## Common Confusions

- **Confusion**: Thinking funs are less capable than named functions
  **Clarification**: They support multiple clauses and guards; they only lack a name (and self-recursion)

## Source Reference

Chapter 6: "Higher-Order Functions," section "Anonymous Functions."

## Verification Notes

- Definition: Adapted from the "Anonymous Functions" section
- Confidence: HIGH — explicit section
- Uncertainties: None
