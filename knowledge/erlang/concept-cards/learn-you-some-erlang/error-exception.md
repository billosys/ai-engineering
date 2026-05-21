---
concept: Error Exception
slug: error-exception
category: error-handling
subcategory: exception-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Error Exceptions"
extraction_confidence: high
aliases:
  - "erlang:error"
  - "error"
prerequisites:
  - runtime-error
extends: []
related:
  - exit-exception
  - throw-exception
  - try-catch-expression
contrasts_with:
  - exit-exception
  - throw-exception
answers_questions:
  - "What distinguishes errors, exits, and throws?"
  - "How do I handle exceptions with try ... catch?"
---

# Error Exception

## Quick Definition

An error exception, raised by `erlang:error(Reason)`, ends the current process's execution and includes a stack trace. It is used when the calling code cannot reasonably handle what happened.

## Core Definition

One of the three kinds of exceptions in Erlang. Calling `erlang:error(Reason)` ends the execution in the current process and includes a stack trace of the last functions called with their arguments. These are the kind of exceptions that provoke runtime errors. Errors are the means for a function to stop its execution when you cannot expect the calling code to handle what just happened. Errors are not limited to those Erlang provides — you can define your own error reasons (Hébert, ch. 7, "Error Exceptions").

## Prerequisites

- **Runtime error** — Error exceptions are the mechanism behind runtime errors

## Key Properties

1. Raised with `erlang:error(Reason)`.
2. Ends execution of the current process.
3. Includes a stack trace of the last calls and their arguments.
4. Used when the calling code cannot be expected to handle the situation.
5. Custom error reasons are allowed (e.g., `erlang:error(custom_error)`).
6. Caught in `try ... catch` with the type `error`.

## Construction / Recognition

To raise an error exception: call `erlang:error(Reason)` with any term as the reason.

## Context & Application

Errors are appropriate when there is nothing the caller can do — e.g., an if clause error means the code itself is wrong and must be changed. They are *not* appropriate when the caller can reasonably handle the outcome (e.g., a missing key in a tree lookup, where returning `{ok, Value}` or `undefined` is better).

## Examples

**Example** (ch. 7): `erlang:error(badarith).` raises `** exception error: bad argument in an arithmetic expression`.

**Example** (ch. 7): `erlang:error(custom_error).` raises `** exception error: custom_error` with a user-defined reason.

## Relationships

### Prerequisites

- **Runtime error** — Error exceptions cause runtime errors

### Related

- **Exit exception** — Another exception class, with "kill the process" intent
- **Throw exception** — Another exception class, for control flow
- **Try-catch expression** — Errors are caught with the `error` type in `try ... catch`

### Contrasts With

- **Exit exception** — `exit/1` carries no stack trace; intent is to kill the process
- **Throw exception** — Throws carry no "crash" intent; they are for control flow

## Common Errors

- **Error**: Using `erlang:error` where the caller could handle the result
  **Correction**: Return a `{ok, Value}` tuple or an atom like `undefined` instead

## Common Confusions

- **Confusion**: Thinking errors and exits are interchangeable
  **Clarification**: The real difference is intent and that `erlang:error/1` returns a stack trace while `exit/1` does not

## Source Reference

Chapter 7: "Errors and Exceptions," section "Error Exceptions."

## Verification Notes

- Definition: Adapted from the "Error Exceptions" section
- Confidence: HIGH — explicit section
- Uncertainties: None
