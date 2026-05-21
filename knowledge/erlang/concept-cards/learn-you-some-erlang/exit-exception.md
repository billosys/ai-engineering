---
concept: Exit Exception
slug: exit-exception
category: error-handling
subcategory: exception-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Exit Exceptions"
extraction_confidence: high
aliases:
  - "exit"
  - "internal exit"
  - "external exit"
  - "exit signal"
prerequisites:
  - error-exception
extends: []
related:
  - throw-exception
  - try-catch-expression
contrasts_with:
  - error-exception
  - throw-exception
answers_questions:
  - "What distinguishes errors, exits, and throws?"
---

# Exit Exception

## Quick Definition

An exit exception, raised by `exit/1`, stops the current process. It signals a condition serious enough to kill the process and carries no stack trace.

## Core Definition

One of the three kinds of exceptions in Erlang. Two kinds of exits exist: *internal exits*, triggered by `exit/1`, which make the current process stop its execution; and *external exits*, called with `exit/2`, which concern multiple processes in the concurrent part of Erlang. Internal exits are similar to errors — historically they were the same — but the difference is intent: an error is simply an error, while an exit signals a condition worthy of killing the current process. A key practical difference is that `erlang:error/1` returns a stack trace whereas `exit/1` does not, which matters when copying exit messages to listening processes (Hébert, ch. 7, "Exit Exceptions").

## Prerequisites

- **Error exception** — Exits are closely related to errors and best understood by contrast

## Key Properties

1. Internal exit: `exit/1` stops the current process.
2. External exit: `exit/2` is used between processes (concurrent Erlang).
3. Similar to errors; the difference is intent.
4. `exit/1` carries no stack trace, unlike `erlang:error/1`.
5. Exits are communicated between processes as a special exit-signal message.
6. Caught in `try ... catch` with the type `exit`.

## Construction / Recognition

To raise an internal exit: call `exit(Reason)` with any term as the reason.

## Context & Application

Use `exit/1` when the condition is serious enough to warrant killing the process rather than merely signalling an error. Because `exit/1` omits the stack trace, copying its message to many listening processes is cheaper than copying a large error trace. External exits and exit signals underpin Erlang's process supervision.

## Examples

**Example** (ch. 7): `exceptions:exits(fun() -> exit(goodbye) end).` returns `{exit,caught,goodbye}` when caught with an `exit:` clause.

**Example** (ch. 7): `catch exit(die).` evaluates to `{'EXIT',die}`.

## Relationships

### Prerequisites

- **Error exception** — Exits are best understood relative to errors

### Related

- **Throw exception** — The third exception class, for control flow
- **Try-catch expression** — Exits are caught with the `exit` type

### Contrasts With

- **Error exception** — Errors carry a stack trace and signal "the caller can't handle this"; exits do not carry a trace and signal "kill the process"
- **Throw exception** — Throws carry no "crash" intent at all

## Common Errors

- **Error**: Using `exit/1` for a recoverable condition
  **Correction**: Use it only when the process genuinely should die; otherwise return a value or use a throw

## Common Confusions

- **Confusion**: Thinking exits and errors are completely different mechanisms
  **Clarification**: They were historically the same; the difference is intent and the presence of a stack trace

## Source Reference

Chapter 7: "Errors and Exceptions," section "Exit Exceptions."

## Verification Notes

- Definition: Adapted from the "Exit Exceptions" section
- Confidence: HIGH — explicit section
- Uncertainties: None
