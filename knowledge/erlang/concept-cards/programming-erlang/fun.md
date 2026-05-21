---
# === CORE IDENTIFICATION ===
concept: Fun
slug: fun

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: anonymous-functions
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
  - anonymous function
  - lambda abstraction
  - lambda

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - pattern-matching
extends: []
related:
  - higher-order-function
  - function-clause
  - list-comprehension
contrasts_with:
  - function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fun (anonymous function)?"
  - "How do I create my own control abstractions?"
---

# Quick Definition

A fun is an anonymous function — the Erlang data type that represents a function. Funs can be bound to variables, passed as arguments, and returned from other functions.

# Core Definition

"The data type that represents a function in Erlang is called a *fun*" (Chapter 4, "Funs: The Basic Unit of Abstraction"). "`funs` are 'anonymous' functions. They are called this because they have no name. You might see them referred to as *lambda abstractions* in other programming languages." A fun is written `fun(Args) -> Body end` and "there's only one thing we can do with a fun, and that is to apply it to an argument." Funs may take any number of arguments and "can have several different clauses." Because Erlang is a functional language, "functions can be used as arguments to functions and that functions can return functions." Funs are used to perform an operation on every element of a list (via `lists:map/2`, `lists:filter/2`), to create custom control abstractions, and to implement things like lazy evaluators and parser combinators.

# Prerequisites

- **Function** — A fun is the anonymous counterpart of a named function; the same head/body/clause structure applies.
- **Pattern matching** — A fun's argument patterns are matched like any function head.

# Key Properties

1. A fun is the Erlang data type that represents a function.
2. It is anonymous — it has no name.
3. Written `fun(Args) -> Body end`.
4. The only operation on a fun is applying it to arguments.
5. It can take any number of arguments and can have several clauses.
6. It can be bound to a variable, passed as an argument, and returned from a function.
7. Applying a fun with the wrong number of arguments raises an exception.

# Construction / Recognition

## To Create and Use a Fun:
1. Write `fun(Args) -> Body end` and optionally bind it to a variable.
2. Apply it by calling the variable with arguments, e.g. `Double(2)`.
3. For multiple clauses, separate them with `;` inside the `fun ... end`.

## To Recognize It:
1. The keywords `fun ... end`.
2. The shell prints a fun as `#Fun<...>`.

# Context & Application

- **Typical contexts**: Arguments to `lists:map/2` and `lists:filter/2`; building custom control abstractions; functions that return functions.
- **Common applications**: `Double = fun(X) -> 2*X end`; a `for` loop built from a fun; `MakeTest` returning a membership-testing fun.
- **Historical/stylistic notes**: Armstrong calls funs "the basic unit of abstraction" — they let you build control structures Erlang does not provide, such as a `for` loop.

# Examples

**Example 1** (Chapter 4, "Funs: The Basic Unit of Abstraction"): `Double = fun(X) -> 2*X end.` then `Double(2)` returns `4`.

**Example 2** (Chapter 4, "Funs: The Basic Unit of Abstraction"): `TempConvert = fun({c,C}) -> {f, 32 + C*9/5}; ({f,F}) -> {c, (F-32)*5/9} end.` — a fun with two clauses; `TempConvert({c,100})` returns `{f,212.0}`.

# Relationships

## Builds Upon
- **Function** — A fun has the same head/body/clause structure as a named function.

## Enables
- **Higher-order function** — Functions that take or return funs.
- **List comprehension** — Conceptually related; comprehensions express map/filter logic without explicit funs.

## Related
- **Higher-order function** — Funs are passed to and returned from higher-order functions.
- **Function clause** — A fun can have multiple clauses.

## Contrasts With
- **Function** — A named function is referenced by `module:name/arity`; a fun is anonymous, written `fun ... end`, and is itself a value that can be stored and passed around.

# Common Errors

- **Error**: Applying a fun with the wrong number of arguments.
  **Correction**: Supply exactly as many arguments as the fun's arity; otherwise an `interpreted function with arity N called with ...` exception is raised.

- **Error**: Expecting to call a fun by a name.
  **Correction**: A fun has no name; bind it to a variable and apply that variable.

# Common Confusions

- **Confusion**: Thinking a fun is a different kind of thing from data.
  **Clarification**: A fun *is* a data type — a value that can be bound, passed, and returned like any other.

- **Confusion**: Believing funs are exotic or rarely needed.
  **Clarification**: They are "the basic unit of abstraction" — passing funs to `map`/`filter` is "extremely common."

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "Funs: The Basic Unit of Abstraction" (subsections "Functions That Have Funs As Their Arguments," "Functions That Return Funs," "Defining Your Own Control Abstractions"). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Funs: The Basic Unit of Abstraction."
- Confidence rationale: HIGH — funs are explicitly defined as the data type representing a function.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
