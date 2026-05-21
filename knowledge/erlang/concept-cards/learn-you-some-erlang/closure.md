---
concept: Closure
slug: closure
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Higher-Order Functions"
chapter_number: 6
pdf_page: null
section: "Function Scope and Closures"
extraction_confidence: high
aliases:
  - "lexical closure"
prerequisites:
  - anonymous-function
  - function-scope
extends:
  - anonymous-function
related:
  - higher-order-function
contrasts_with: []
answers_questions:
  - "What is a closure?"
  - "What is an anonymous function (fun)?"
---

# Closure

## Quick Definition

A closure is an anonymous function that carries some of its surrounding environment (variables from its scope) along with it, even when executed elsewhere.

## Core Definition

A closure is the idea of having a function that references some environment along with it (the values that are part of its scope). In other words, a closure is what happens when anonymous functions meet the concept of scope and carrying variables around. Because the inherited scope follows an anonymous function wherever it goes — including when passed to another function — the fun can still access the captured variables when executed in a different context (Hébert, ch. 6, "Function Scope and Closures").

## Prerequisites

- **Anonymous function** — A closure is an anonymous function plus captured environment
- **Function scope** — Closures rely on scope inheritance

## Key Properties

1. A closure is an anonymous function bundled with its referenced environment.
2. The captured scope follows the fun even when passed to another function.
3. Lets you carry parameters and content out of their original context.
4. Useful for fixing one argument of a multi-argument function while varying others.

## Construction / Recognition

To create a useful closure:

1. Declare an anonymous function inside a function that has a variable you want to capture.
2. The fun captures that variable from the enclosing scope.
3. Return or pass the fun; it retains the captured value.

## Context & Application

Closures are commonly used to carry state when you have a function taking many arguments but one stays constant — e.g., wrapping `math:pow/2` in a fun with `Base` captured so each `map` call varies only the exponent. The book's "PrepareAlarm" example also returns a closure capturing the `Room` variable.

## Examples

**Example** (ch. 6): `a() -> Secret = "pony", fun() -> Secret end.` returns a closure capturing `Secret`; calling it later in `b/1` still yields `"pony"`.

**Example** (ch. 6): `PowerOfTwo = fun(X) -> math:pow(Base,X) end` captures `Base` so `map(PowerOfTwo, [1,2,3,4])` works.

## Relationships

### Prerequisites

- **Anonymous function** — A closure is a fun with captured environment
- **Function scope** — Provides the variables a closure captures

### Builds Upon

- **Anonymous function** — A closure is a fun that references its scope

### Related

- **Higher-order function** — Closures are commonly passed to HOFs

## Common Errors

- **Error**: Expecting a closure to see variables bound *after* it was declared
  **Correction**: A closure captures the scope as it was at declaration time

## Common Confusions

- **Confusion**: Thinking every anonymous function is a closure
  **Clarification**: A fun is a closure specifically when it references variables from its enclosing scope

## Source Reference

Chapter 6: "Higher-Order Functions," section "Function Scope and Closures."

## Verification Notes

- Definition: Adapted from the closure discussion
- Confidence: HIGH — explicit treatment with examples
- Uncertainties: None
