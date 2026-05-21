---
# === CORE IDENTIFICATION ===
concept: Higher-Order Function
slug: higher-order-function

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: abstraction
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Funs: The Basic Unit of Abstraction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - HOF
  - list-at-a-time operation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fun
  - function
extends: []
related:
  - list-comprehension
  - list
  - recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function?"
  - "How do map and filter work?"
---

# Quick Definition

A higher-order function is a function that takes other functions as arguments or returns functions as results. `lists:map/2` and `lists:filter/2` are the canonical examples.

# Core Definition

"Functions that manipulate functions are called *higher-order functions*, and the data type that represents a function in Erlang is called a *fun*" (Chapter 4, "Funs: The Basic Unit of Abstraction"). "Higher-order functions are the very essence of functional programming languages — not only can functional programs manipulate regular data structures, they can also manipulate the functions that transform the data." The standard library `lists` module "exports several functions whose arguments are funs"; the most useful is `lists:map(F, L)`, which "returns a list made by applying the fun `F` to every element in the list `L`," and `lists:filter(P, L)`, which "returns a new list of all the elements `E` in `L` such that `P(E)` is `true`." Functions can also *return* funs — `Mult = fun(Times) -> (fun(X) -> X * Times end) end` returns a function. Operations like `map` and `filter` that act on a whole list in one call are called *list-at-a-time* operations.

# Prerequisites

- **Fun** — Higher-order functions take or return funs; the fun is the value being manipulated.
- **Function** — A higher-order function is itself a function.

# Key Properties

1. A higher-order function takes functions as arguments and/or returns functions.
2. Funs are the data type passed to and returned from higher-order functions.
3. `lists:map(F, L)` applies `F` to every element of `L`, returning a new list.
4. `lists:filter(P, L)` keeps the elements `E` of `L` for which `P(E)` is `true`.
5. Functions can return funs (e.g., `Mult(3)` returns `fun(X) -> X * 3 end`).
6. Operations acting on a whole list in one call are "list-at-a-time" operations.
7. They are described as "the very essence of functional programming languages."

# Construction / Recognition

## To Use a Higher-Order Function:
1. Write or choose a fun expressing the per-element operation or predicate.
2. Pass it to `lists:map/2`, `lists:filter/2`, or a custom higher-order function.

## To Write One That Returns a Fun:
1. Make the function body a `fun ... end` expression.
2. The outer arguments are captured (closed over) by the returned fun.

## To Recognize It:
1. A function whose argument or return value is itself a function/fun.

# Context & Application

- **Typical contexts**: List processing; building custom control abstractions.
- **Common applications**: `lists:map`, `lists:filter`; a custom `for` loop; `MakeTest` returning a membership predicate.
- **Historical/stylistic notes**: List-at-a-time operations "make our programs small and easy to understand" — each operation on the whole list is "a single conceptual step."

# Examples

**Example 1** (Chapter 4, "Functions That Have Funs As Their Arguments"): `lists:map(fun(X) -> 2*X end, [1,2,3,4])` returns `[2,4,6,8]`; `lists:filter(Even, [1,2,3,4,5,6,8])` returns `[2,4,6,8]`.

**Example 2** (Chapter 4, "Functions That Return Funs"): `Mult = fun(Times) -> (fun(X) -> X * Times end) end`; `Triple = Mult(3)` returns a fun, and `Triple(5)` is `15`.

# Relationships

## Builds Upon
- **Fun** — The function values that higher-order functions consume and produce.
- **Function** — A higher-order function is a function.

## Enables
- Custom control abstractions (e.g., a hand-built `for` loop) and list-at-a-time processing.

## Related
- **List comprehension** — A more concise alternative for many map/filter uses.
- **List** — The structure most higher-order functions operate on.
- **Recursion** — The underlying mechanism implementing `map`, `filter`, etc.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Passing a fun of the wrong arity to `map`/`filter`.
  **Correction**: `map`/`filter` apply the fun to one element; the fun must take exactly one argument.

- **Error**: Expecting a function that returns a fun to return a final value.
  **Correction**: It returns a *function*; you must then apply that function to get a value (`Mult(3)` then `Triple(5)`).

# Common Confusions

- **Confusion**: Thinking higher-order functions are an advanced or rare feature.
  **Clarification**: They are "the very essence of functional programming"; passing funs to `map`/`filter` is everyday Erlang.

- **Confusion**: Believing `map` and `filter` mutate the input list.
  **Clarification**: They return *new* lists; Erlang data is immutable.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "Funs: The Basic Unit of Abstraction" (subsections "Functions That Have Funs As Their Arguments" and "Functions That Return Funs"). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Funs: The Basic Unit of Abstraction."
- Confidence rationale: HIGH — higher-order functions are explicitly defined and demonstrated with `map`/`filter`.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
