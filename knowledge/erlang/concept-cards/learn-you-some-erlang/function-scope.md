---
concept: Function Scope
slug: function-scope
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
  - "scope"
  - "shadowing"
prerequisites:
  - variable
  - anonymous-function
extends: []
related:
  - closure
contrasts_with: []
answers_questions:
  - "What is a closure?"
---

# Function Scope

## Quick Definition

A function's scope is the place where its variables and their values are stored. Anonymous functions inherit the scope of the function in which they are declared.

## Core Definition

A function's scope can be imagined as the place where all the variables and their values are stored. Inside a function, you can refer to any variable in its scope — including from anonymous functions declared within it, which inherit the parent function's scope. Inheritance goes only one way: a parent cannot see variables defined only inside a nested function. Defining a new variable with the same name as one in the parent scope is called *shadowing*, which the compiler warns about; it is allowed only when the new variable is introduced in the nested function's head (Hébert, ch. 6, "Function Scope and Closures").

## Prerequisites

- **Variable** — Scope governs which variables are visible and bound
- **Anonymous function** — Scope inheritance is observed through nested funs

## Key Properties

1. Scope holds the variables and values available in a function.
2. An anonymous function inherits its parent function's scope.
3. Inheritance is one-way: the parent cannot see the child's locally defined variables.
4. The inherited scope follows the anonymous function even when passed elsewhere.
5. Shadowing is reusing a parent-scope name in a nested function; the compiler warns.
6. A variable can be re-introduced only in a nested function's head (e.g., `fun(A) -> ...`).

## Construction / Recognition

To recognize scope inheritance: variables bound in an enclosing function are usable inside a `fun` declared within it, but not vice versa.

## Context & Application

Scope inheritance is what makes closures possible — an anonymous function can carry parameters and content out of their original context. The shadowing warning helps prevent accidental name reuse bugs.

## Examples

**Example** (ch. 6): In `base(A) -> B = A + 1, F = fun() -> A * B end, F().`, `F` can use `A` and `B` from `base/1`'s scope.

**Example** (ch. 6): `base() -> A = 1, (fun(A) -> A = 2 end)(2).` compiles but warns "variable 'A' shadowed in 'fun'."

## Relationships

### Prerequisites

- **Variable** — Scope concerns variable visibility
- **Anonymous function** — Scope inheritance is seen through funs

### Related

- **Closure** — A closure is a fun plus the scope it carries

## Common Errors

- **Error**: Trying to use a variable defined only inside a nested fun from the parent
  **Correction**: Inheritance is one-way; return the value from the fun instead

## Common Confusions

- **Confusion**: Thinking you can rebind a parent-scope variable inside a fun body
  **Clarification**: Using `=` on it compares; rebinding is only possible by shadowing in the fun's head

## Source Reference

Chapter 6: "Higher-Order Functions," section "Function Scope and Closures."

## Verification Notes

- Definition: Adapted from the scope discussion
- Confidence: HIGH — explicit treatment with examples
- Uncertainties: None
