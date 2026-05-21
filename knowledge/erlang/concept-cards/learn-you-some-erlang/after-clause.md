---
concept: After Clause
slug: after-clause
category: error-handling
subcategory: exception-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "After the Catch"
extraction_confidence: high
aliases:
  - "after"
  - "finally"
prerequisites:
  - try-catch-expression
extends:
  - try-catch-expression
related: []
contrasts_with: []
answers_questions:
  - "How do I handle exceptions with try ... catch?"
---

# After Clause

## Quick Definition

An `after` clause is an optional block of a `try ... catch` that always runs, whether or not an exception occurred — Erlang's equivalent of `finally`.

## Core Definition

You can add an `after` clause to a `try ... catch` that will always be executed: `try Expression of Pattern -> Expr1 catch Type:Exception -> Expr2 after Expr3 end`. This is equivalent to the `finally` block in many other languages: whether or not there are errors, the expressions inside the `after` part are guaranteed to run. However, you cannot get any return value out of the `after` construct, so `after` is mostly used to run code with side effects (Hébert, ch. 7, "After the Catch").

## Prerequisites

- **Try-catch expression** — `after` is an optional part of a `try ... catch`

## Key Properties

1. An optional `after Expr` block at the end of a `try ... catch`.
2. Always runs, whether or not an exception was raised.
3. Equivalent to `finally` in other languages.
4. Produces no return value; used for side effects.
5. Using `after` cancels last call optimization, since the block must run after everything else.

## Construction / Recognition

To add an `after` clause:

1. Write the `try ... catch` as usual.
2. Add `after Expr` before the final `end`.

## Context & Application

The canonical use of `after` is ensuring cleanup with side effects — for example, making sure a file you were reading gets closed whether or not an exception was raised. Because `after` must run after all other code, it disables last call optimization for the `try`.

## Examples

**Example** (ch. 7): The book describes the canonical use: closing a file in an `after` block regardless of whether reading it raised an exception.

## Relationships

### Prerequisites

- **Try-catch expression** — `after` is part of `try ... catch`

### Builds Upon

- **Try-catch expression** — `after` extends the `try` construct

## Common Errors

- **Error**: Expecting to use the value of the `after` block
  **Correction**: `after` yields no return value; use it only for side effects

## Common Confusions

- **Confusion**: Thinking `after` runs only on success or only on failure
  **Clarification**: `after` always runs, in both cases

## Source Reference

Chapter 7: "Errors and Exceptions," section "After the Catch."

## Verification Notes

- Definition: Adapted from the "After the Catch" section
- Confidence: HIGH — explicit section
- Uncertainties: None
