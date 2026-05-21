---
concept: Try-Catch Expression
slug: try-catch-expression
category: error-handling
subcategory: exception-handling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Dealing with Exceptions"
extraction_confidence: high
aliases:
  - "try ... catch"
  - "try ... of ... catch"
prerequisites:
  - error-exception
  - exit-exception
  - throw-exception
  - case-expression
extends: []
related:
  - after-clause
  - catch-expression
contrasts_with:
  - catch-expression
answers_questions:
  - "How do I handle exceptions with try ... catch?"
  - "What distinguishes errors, exits, and throws?"
---

# Try-Catch Expression

## Quick Definition

A `try ... catch` expression evaluates a protected expression while letting you handle both its successful result and any exception it raises.

## Core Definition

A `try ... catch` is a way to evaluate an expression while letting you handle the successful case as well as the errors encountered. The general syntax is `try Expression of SuccessfulPattern [Guards] -> Expr; ... catch TypeOfError:ExceptionPattern -> Expr; ... end`. The expression between `try` and `of` is *protected*: any exception within it is caught. The patterns between `try ... of` and `catch` behave exactly like a `case ... of` — they are not protected and allow matching, binding, and guards. In the `catch` part, `TypeOfError` is `error`, `throw`, or `exit`; if no type is given, `throw` is assumed. The pattern `_:_` catches any exception of any type. More than one expression may appear between `try` and `of`, and the `of` part may be omitted entirely (Hébert, ch. 7, "Dealing with Exceptions").

## Prerequisites

- **Error exception** — `try ... catch` handles error exceptions
- **Exit exception** — It handles exit exceptions
- **Throw exception** — It handles throw exceptions
- **Case expression** — The `of` part behaves like a `case ... of`

## Key Properties

1. The expression between `try` and `of` is protected: exceptions there are caught.
2. The `of` patterns work like `case ... of` and are not protected.
3. `catch` clauses match `TypeOfError:ExceptionPattern`; type is `error`, `throw`, or `exit`.
4. If no type is given in a catch clause, `throw` is assumed.
5. `_:_` catches any exception of any class.
6. Multiple expressions may appear between `try` and `of`; the `of` part is optional.
7. A `try ... catch` without `of` has only a protected part, which is not tail-recursive-safe.

## Construction / Recognition

To handle exceptions:

1. Write `try Expr` and the protected expression(s).
2. Optionally add `of Pattern -> ...` to match successful results.
3. Add `catch Type:Pattern -> ...` clauses for the exception classes.
4. End with `end`.

## Context & Application

`try ... catch` was added in Erlang/OTP R10B to fix the ambiguities of the older `catch`. Use catchall `_:_` clauses sparingly — protect only what you can handle. Put recursive calls between `of` and `catch` so they benefit from last call optimization, since the protected part cannot be tail recursive.

## Examples

**Example** (ch. 7): The `black_knight/1` function uses `throw:slice`, `error:cut_arm`, `exit:cut_leg`, and `_:_` clauses to handle every exception class.

**Example** (ch. 7): `im_impressed/0` drops the `of` part and catches `Exception:Reason` for several expressions.

## Relationships

### Prerequisites

- **Error exception**, **Exit exception**, **Throw exception** — The three classes it handles
- **Case expression** — The `of` part mirrors `case ... of`

### Related

- **After clause** — An optional `after` block can be added to a `try`
- **Catch expression** — The older, simpler exception-capturing construct

### Contrasts With

- **Catch expression** — `catch` cannot distinguish exception classes or a thrown value from a real return; `try ... catch` can

## Common Errors

- **Error**: Putting a recursive call in the protected part of a `try ... catch` without `of`
  **Correction**: Place recursive calls between `of` and `catch` to keep last call optimization

## Common Confusions

- **Confusion**: Forgetting that an omitted catch type means `throw`
  **Clarification**: A catch clause with no `Type:` prefix catches only throws

## Source Reference

Chapter 7: "Errors and Exceptions," section "Dealing with Exceptions" and its subsections.

## Verification Notes

- Definition: Adapted from the "Dealing with Exceptions" section
- Confidence: HIGH — explicit section with syntax and examples
- Uncertainties: None
