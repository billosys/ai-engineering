---
concept: Catch Expression
slug: catch-expression
category: error-handling
subcategory: exception-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Wait, There's More!"
extraction_confidence: high
aliases:
  - "catch keyword"
prerequisites:
  - error-exception
  - exit-exception
  - throw-exception
extends: []
related:
  - try-catch-expression
contrasts_with:
  - try-catch-expression
answers_questions:
  - "How do I handle exceptions with try ... catch?"
  - "What distinguishes errors, exits, and throws?"
---

# Catch Expression

## Quick Definition

The `catch` keyword is an older error-handling construct that captures all exception classes plus normal results, but with limitations that led to `try ... catch`.

## Core Definition

`catch` is an error-handling construct, defined by the keyword `catch`, that captures all types of exceptions on top of good results. It displays a different representation of exceptions: throws remain as-is, while exits and errors are both represented as `{'EXIT', Reason}` (for backward compatibility, since errors were bolted on after exits). For errors, the `Reason` includes a stack trace, whose top tuple is the last function called. `catch` has several warts: it conflicts with the `=` operator (requiring parentheses, as in `X = (catch 4+2)`), you cannot tell an underlying exception representation from a real exception value, and you cannot tell a thrown value from an actual return value. These problems prompted the addition of `try ... catch` in Erlang/OTP R10B (Hébert, ch. 7, "Wait, There's More!").

## Prerequisites

- **Error exception**, **Exit exception**, **Throw exception** — `catch` captures all three classes

## Key Properties

1. Captures all exception classes plus normal return values.
2. Throws appear unchanged; exits and errors both appear as `{'EXIT', Reason}`.
3. Error reasons include a stack trace; the top tuple is the last call.
4. Conflicts with `=`; must be wrapped in parentheses when assigned.
5. Cannot distinguish an exception's representation from a real value of that shape.
6. Cannot distinguish a thrown value from an actual return value.
7. Often written as `case catch Expr of ... end`.

## Construction / Recognition

To use `catch`: write `catch Expression`; wrap it in parentheses if used with `=`, e.g., `X = (catch 4+2)`.

## Context & Application

`catch` is a compact way to capture exceptions but its ambiguities make it inferior to `try ... catch` for most code. It survives mainly for backward compatibility and concise cases where the ambiguity does not matter. `erlang:get_stacktrace/0` can also fetch a stack trace from a crashed process.

## Examples

**Example** (ch. 7): `catch throw(whoa).` evaluates to `whoa`; `catch exit(die).` evaluates to `{'EXIT',die}`.

**Example** (ch. 7): `catcher(X,Y) -> case catch X/Y of {'EXIT', {badarith,_}} -> "uh oh"; N -> N end.` returns `"uh oh"` for division by zero.

## Relationships

### Prerequisites

- **Error exception**, **Exit exception**, **Throw exception** — The classes `catch` captures

### Related

- **Try-catch expression** — The modern replacement for `catch`

### Contrasts With

- **Try-catch expression** — `try ... catch` distinguishes exception classes and a thrown value from a return value; `catch` cannot

## Common Errors

- **Error**: Writing `X = catch 4+2` without parentheses
  **Correction**: `catch` conflicts with `=`; write `X = (catch 4+2)`

## Common Confusions

- **Confusion**: Assuming a `{'EXIT', Reason}` result always means an exception occurred
  **Clarification**: A function could legitimately return such a tuple; `catch` cannot tell them apart

## Source Reference

Chapter 7: "Errors and Exceptions," section "Wait, There's More!"

## Verification Notes

- Definition: Adapted from the "Wait, There's More!" section
- Confidence: HIGH — explicit section
- Uncertainties: None
