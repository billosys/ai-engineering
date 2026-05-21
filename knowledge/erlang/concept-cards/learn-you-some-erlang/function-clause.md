---
concept: Function Clause
slug: function-clause
category: functions-pattern-matching
subcategory: functions
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Syntax in Functions"
chapter_number: 3
pdf_page: null
section: "Pattern Matching"
extraction_confidence: high
aliases:
  - "function declaration"
  - "function head"
prerequisites:
  - pattern-matching
  - module
extends: []
related:
  - guard
  - case-expression
contrasts_with: []
answers_questions:
  - "What is pattern matching?"
---

# Function Clause

## Quick Definition

A function clause is one pattern-matching branch of a function. Clauses are separated by semicolons and together form a function declaration ended with a period.

## Core Definition

Each pattern-matching branch of a function definition is called a *function clause*. Function clauses must be separated by semicolons (`;`) and together form a *function declaration*. A function declaration counts as one larger statement, which is why the final clause ends with a period. When a pattern fails in one clause, Erlang looks for the next clause with a matching pattern and runs that one. The syntax of each clause is `Name(Args) -> Body.`, where `Name` is an atom and `Body` is one or more expressions separated by commas (Hébert, ch. 3, "Pattern Matching" and ch. 2, "Creating Modules").

## Prerequisites

- **Pattern matching** — Each clause has a pattern that Erlang matches against
- **Module** — Functions (and their clauses) are defined in modules

## Key Properties

1. A clause is one pattern branch of a function.
2. Clauses are separated by semicolons (`;`).
3. The final clause of a function ends with a period (`.`).
4. All clauses of a function must have the same name and arity.
5. Erlang tries clauses top to bottom, running the first whose pattern matches.
6. The body is one or more comma-separated expressions; the last is returned.

## Construction / Recognition

To write a multi-clause function:

1. Write each clause as `name(Pattern) -> Body`.
2. Separate clauses with `;`.
3. End the last clause with `.`.

## Context & Application

Function clauses are the declarative replacement for imperative conditional cascades. Failing all clauses raises a function clause error.

## Examples

**Example** (ch. 3): `head([H|_]) -> H.` is a single-clause function; `same(X,X) -> true; same(_,_) -> false.` is a two-clause function.

## Relationships

### Prerequisites

- **Pattern matching** — Clauses are selected by matching
- **Module** — Clauses define functions inside modules

### Related

- **Guard** — A clause head may include guards for extra expressiveness
- **Case expression** — A `case ... of` branch is like a function clause

## Common Errors

- **Error**: Separating clauses with periods instead of semicolons
  **Correction**: Use `;` between clauses; only the last clause ends with `.`

## Common Confusions

- **Confusion**: Thinking interleaving clauses of two functions is allowed
  **Clarification**: All clauses of a function must be contiguous and share name and arity

## Source Reference

Chapter 3: "Syntax in Functions," section "Pattern Matching."

## Verification Notes

- Definition: Adapted from the function-clause discussion in chapter 3
- Confidence: HIGH — explicit definition
- Uncertainties: None
