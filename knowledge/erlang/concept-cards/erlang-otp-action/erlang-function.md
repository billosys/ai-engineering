---
# === CORE IDENTIFICATION ===
concept: Erlang Function
slug: erlang-function

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.3.4 Creating modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - function definition
  - function head
  - function body

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - function-arity
  - function-clause-selection
  - guard
  - fun
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang function definition?"
  - "What separates a function head from its body?"
  - "Does an Erlang function need a return statement?"
---

# Quick Definition

An Erlang function is a named definition inside a module: a head (name and arguments) and a body (the expression to evaluate), separated by `->`. A function always returns the value of its body.

# Core Definition

A function definition such as `pie() -> 3.14.` "creates a function `pie` that takes no arguments and returns the floating-point number 3.14" (Chapter 2, section 2.3.4). "The arrow `->` is there to separate the function *head* (the name and arguments) from its *body* (what the function does)." There is no `return` keyword — "a function always returns the value of the expression in the body." A function definition must end with a period. A function lives inside a module and may consist of multiple clauses; it is identified by its name together with its arity.

# Prerequisites

- **Erlang module** — functions are defined inside modules.

# Key Properties

1. A function definition has a head (name + arguments) and a body.
2. The head and body are separated by the arrow `->`.
3. A function always returns the value of its body expression; there is no `return` keyword.
4. A function definition ends with a period.
5. A function is identified by its name plus its arity.
6. A function may consist of multiple clauses.

# Construction / Recognition

## To Construct/Create:
1. Write the head: function name followed by parenthesized arguments.
2. Write `->`.
3. Write the body — the expression(s) to evaluate.
4. End the definition with a period.
5. Export the function if it must be callable from outside the module.

# Context & Application

- **Typical contexts**: All Erlang program code.
- **Common applications**: Defining behavior; functions are the building blocks of modules and the units of recursion.
- **Historical/stylistic notes**: Functions can have side effects (e.g. `io:format/2` prints text), though in Erlang side effects can generally be seen as messages.

# Examples

**Example 1** (Listing 2.1): `pie() -> 3.14.` defines a zero-argument function returning the float 3.14.

**Example 2** (section 2.5.1): `print(Term) -> io:format("The value of Term is: ~p.~n", [Term]).` defines a one-argument function whose body calls `io:format/2`.

# Relationships

## Builds Upon
- **Erlang module** — functions live inside modules.

## Enables
- **Function clause selection** — a function may have multiple clauses.
- **Fun** — a function can be referenced as a value (a fun).

## Related
- **Function arity** — a function's identity includes its arity.
- **Guard** — clauses may carry guards.
- **Built-in function** — BIFs are functions implemented in C.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Writing `return` to return a value from a function.
  **Correction**: Erlang has no `return`; a function returns the value of its body expression.

- **Error**: Omitting the terminating period of a function definition.
  **Correction**: A function definition must end with a period, like a shell expression.

# Common Confusions

- **Confusion**: Believing the function name alone identifies a function.
  **Clarification**: A function is identified by name *and* arity; `foo/1` and `foo/2` are distinct functions.

# Source Reference

Chapter 2: Erlang language essentials, section 2.3.4 "Creating modules" and section 2.5.1 "A function with side effects: printing text." See Listing 2.1.

# Verification Notes

- Definition source: Direct adaptation from section 2.3.4.
- Confidence rationale: HIGH — function definitions, heads, and bodies are explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
