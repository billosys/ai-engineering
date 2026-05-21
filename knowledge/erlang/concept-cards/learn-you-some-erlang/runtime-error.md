---
concept: Runtime Error
slug: runtime-error
category: error-handling
subcategory: error-classes
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Exceptions"
chapter_number: 7
pdf_page: null
section: "Runtime Errors"
extraction_confidence: high
aliases:
  - "crash"
  - "function clause error"
  - "case clause error"
  - "bad match error"
  - "badarg"
prerequisites: []
extends: []
related:
  - compile-time-error
  - logical-error
  - error-exception
contrasts_with:
  - compile-time-error
  - logical-error
answers_questions:
  - "What distinguishes errors, exits, and throws?"
---

# Runtime Error

## Quick Definition

A runtime error is an error that crashes code while it executes. Erlang has many recognizable kinds, such as function clause, case clause, and bad match errors.

## Core Definition

Runtime errors are destructive in the sense that they crash your code. While Erlang has ways to deal with them, recognizing them is helpful. The chapter catalogs common runtime errors: *function clause* (all clause patterns/guards fail), *case clause* (no matching `case` branch), *if clause* (no `true` branch), *bad match* (pattern matching fails on `=`), *bad argument*/`badarg` (a function called with incorrect arguments, the error of choice for BIFs), *undefined function* (calling a non-existent or unexported function), *bad arithmetic*/`badarith` (impossible arithmetic such as division by zero), *bad function* (using a non-function value as a function), *bad arity* (a fun called with the wrong number of arguments), and *system limit* errors (Hébert, ch. 7, "Runtime Errors").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Crashes code while it executes.
2. Function clause error: all patterns/guards of a function fail.
3. Case clause / if clause error: no `case` branch matches / no `if` branch is `true`.
4. Bad match error: pattern matching on `=` fails (e.g., rebinding a variable).
5. Bad argument (`badarg`): wrong arguments; the typical error from BIFs.
6. Undefined function, bad arithmetic (`badarith`), bad function, bad arity.
7. System limit errors (too many processes, atoms too long, etc.) can crash the whole VM.

## Construction / Recognition

To recognize a runtime error: the program compiles but crashes during execution with an `** exception error:` message naming the error type.

## Context & Application

Recognizing runtime errors helps with debugging. They can be handled with `try ... catch`, but the Erlang philosophy is often to let processes crash and recover via the concurrent part of the language.

## Examples

**Example** (ch. 7): `lists:sort(fffffff).` raises `** exception error: no function clause matching lists:sort(fffffff)`.

**Example** (ch. 7): `[X,Y] = {4,5}.` raises `** exception error: no match of right hand side value {4,5}` (a bad match error).

## Relationships

### Related

- **Compile-time error** — Caught before running; runtime errors are not
- **Logical error** — Does not crash; runtime errors do
- **Error exception** — `erlang:error/1` deliberately raises a runtime error

### Contrasts With

- **Compile-time error** — Detected at compile time, not execution
- **Logical error** — Produces wrong results without crashing

## Common Errors

- **Error**: Calling a function not exported from its module
  **Correction**: Export it with the right arity and ensure the module is compiled and in the path

## Common Confusions

- **Confusion**: Treating `_Var` as identical to `_`
  **Clarification**: `_Var` is a normal variable (just no unused warning) and cannot be bound twice

## Source Reference

Chapter 7: "Errors and Exceptions," section "Runtime Errors" and its subsections.

## Verification Notes

- Definition: Adapted from the "Runtime Errors" section
- Confidence: HIGH — explicit section cataloguing each error
- Uncertainties: None
