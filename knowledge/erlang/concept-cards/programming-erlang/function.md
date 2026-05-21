---
# === CORE IDENTIFICATION ===
concept: Function
slug: function

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Modules Are Where We Store Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - named function
  - arity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - pattern-matching
extends: []
related:
  - function-clause
  - export-attribute
  - guard
  - fun
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function in Erlang?"
  - "How do I write, compile, and run a module?"
---

# Quick Definition

A function is a named unit of code defined inside a module, made up of one or more clauses. It has no explicit return statement — its value is the value of the last expression evaluated.

# Core Definition

Functions are "the basic units from which sequential and parallel programs are built. Modules contain functions, and the functions can be run sequentially or in parallel" (Chapter 4 opening). A function is made of one or more *clauses* tried in order; each clause "has a *head* and a *body* separated by an arrow (`->`)." "The head consists of a function name followed by zero or more patterns, and the body consists of a sequence of *expressions* ... which are evaluated if the pattern in the head is successfully matched against the calling arguments" (Chapter 4, "Modules Are Where We Store Code"). A function has no return statement: "the return value of the function is simply the value of the last expression in the body of the clause." A function is identified by name and *arity* — the number of arguments — written `Name/Arity` (e.g., `area/1`). Functions are called qualified by module: `geometry:area({rectangle, 10, 5})`.

# Prerequisites

- **Module** — Functions are defined inside modules.
- **Pattern matching** — A function's clause heads contain patterns matched against the call arguments.

# Key Properties

1. A function is defined inside a module and named.
2. It is identified by name *and* arity (number of arguments) — `Name/Arity`.
3. It consists of one or more clauses, tried in the order written.
4. Each clause has a head (name plus patterns) and a body (expression sequence) joined by `->`.
5. There is no return statement; the value is that of the last expression in the matching clause.
6. Calling a function from another module uses the qualified form `module:function(...)`.
7. If no clause matches the arguments, a runtime error is raised.

# Construction / Recognition

## To Define a Function:
1. Write the function name followed by an argument pattern, `->`, and a body.
2. Separate additional clauses with `;` and end the last with `.`.
3. List the function in `-export` if callers outside the module need it.

## To Call a Function:
1. From the same module, write `name(Args)`.
2. From another module, write `module:name(Args)`.

## To Recognize It:
1. A `name(Patterns) -> Expressions` definition inside a module.

# Context & Application

- **Typical contexts**: Every Erlang program; functions implement all behavior.
- **Common applications**: `area/1` computing geometric areas; `total/1` summing a shopping list.
- **Historical/stylistic notes**: Exported functions are like public methods; non-exported functions like private methods.

# Examples

**Example 1** (Chapter 4, "Modules Are Where We Store Code"): `area({rectangle, Width, Height}) -> Width * Height; area({square, Side}) -> Side * Side.` — a two-clause function; `geometry:area({rectangle, 10, 5})` returns `50`.

**Example 2** (Chapter 4, "Back to Shopping"): `cost/1` is a five-clause function; `shop:cost(apples)` returns `2`.

# Relationships

## Builds Upon
- **Module** — Functions live inside modules.
- **Pattern matching** — Clause heads pattern-match the arguments.

## Enables
- **Function clause** — A function is composed of clauses.
- **Guard** — Guards refine which clause of a function applies.

## Related
- **Function clause** — The pieces a multi-clause function is built from.
- **Export attribute** — Declares which functions are public.
- **Fun** — The anonymous-function counterpart of a named function.

## Contrasts With
- No directly contrasting concept; `fun` is the related anonymous form.

# Common Errors

- **Error**: Adding an explicit return statement.
  **Correction**: Erlang functions have no return statement; the value is the last expression evaluated.

- **Error**: Calling a function with arguments that match no clause.
  **Correction**: Provide a clause for every expected case, or accept a `no function clause matching` runtime error.

# Common Confusions

- **Confusion**: Thinking `area/1` and `area/2` are the same function.
  **Clarification**: A function is identified by name *and* arity; different arities are different functions.

- **Confusion**: Believing the first clause always runs.
  **Clarification**: Clauses are tried in order; the *first whose pattern (and guard) matches* runs.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, sections opening and "Modules Are Where We Store Code." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Modules Are Where We Store Code."
- Confidence rationale: HIGH — function structure (head, body, clauses, no return) is explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
