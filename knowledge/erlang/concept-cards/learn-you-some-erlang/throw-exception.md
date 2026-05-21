---
concept: Throw Exception
slug: throw-exception
category: error-handling
subcategory: exception-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Throw Exceptions"
extraction_confidence: high
aliases:
  - "throw"
  - "nonlocal return"
prerequisites:
  - error-exception
extends: []
related:
  - exit-exception
  - try-catch-expression
  - catch-expression
contrasts_with:
  - error-exception
  - exit-exception
answers_questions:
  - "What distinguishes errors, exits, and throws?"
  - "How do I handle exceptions with try ... catch?"
---

# Throw Exception

## Quick Definition

A throw, raised by `throw/1`, is an exception for cases the programmer is expected to handle. It carries control-flow intent, not a crash intent.

## Core Definition

One of the three kinds of exceptions in Erlang. A throw is a class of exceptions used for cases that the programmer can be expected to handle. Unlike exits and errors, throws do not carry any "crash that process!" intent — they are about control flow. The syntax is `throw(Reason)`, where `Reason` can be any term. Throws can also be used for nonlocal returns in deep recursion: the `ssl` module uses `throw/1` to push `{error, Reason}` tuples back to a top-level function, and the `array` module throws a `default` value caught by a top-level function. As a rule of thumb, limit throws used for nonlocal returns to a single module (Hébert, ch. 7, "Throw Exceptions").

## Prerequisites

- **Error exception** — Throws are best understood as one of the three exception classes

## Key Properties

1. Raised with `throw(Reason)`; the reason is any term.
2. Carries control-flow intent, not a crash intent.
3. Used for cases the programmer is expected to handle.
4. Useful for nonlocal returns out of deep recursion.
5. If a module uses throws expecting handling, document them.
6. The default `TypeOfError` in a `try ... catch` is `throw`.

## Construction / Recognition

To raise a throw: call `throw(Reason)` with a meaningful term as the reason.

## Context & Application

Throws let an implementer write code only for the successful cases and have one top-level function deal with exceptional cases — avoiding threading a default value through every function. Keep throws used for nonlocal returns within a single module so they remain easy to debug and the module's interface stays stable.

## Examples

**Example** (ch. 7): `throw(permission_denied).` raises `** exception throw: permission_denied`.

**Example** (ch. 7): In the chapter's `has_value1` tree search, `throw(true)` is used so a match aborts the traversal and is caught by a top-level `has_value`.

## Relationships

### Prerequisites

- **Error exception** — One of the three exception classes

### Related

- **Exit exception** — Another exception class, with kill-the-process intent
- **Try-catch expression** — Throws are caught (by default) with `try ... catch`
- **Catch expression** — `catch` also captures throws

### Contrasts With

- **Error exception** — Errors mean the caller cannot handle it; throws expect handling
- **Exit exception** — Exits signal killing the process; throws are control flow

## Common Errors

- **Error**: Spreading throw-based nonlocal returns across many modules
  **Correction**: Limit such throws to a single module for debuggability and stable interfaces

## Common Confusions

- **Confusion**: Thinking a throw means something has gone seriously wrong
  **Clarification**: A throw carries no crash intent; it is a control-flow mechanism the programmer handles

## Source Reference

Chapter 7: "Errors and Exceptions," section "Throw Exceptions" and "Try a try in a Tree."

## Verification Notes

- Definition: Adapted from the "Throw Exceptions" section
- Confidence: HIGH — explicit section
- Uncertainties: None
