---
# === CORE IDENTIFICATION ===
concept: Exception Class
slug: error-class

# === CLASSIFICATION ===
category: error-handling
subcategory: exceptions
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Error Handling in Sequential Programs"
chapter_number: 6
pdf_page: null
section: "Trapping an Exception with try...catch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - exception type
  - "ExceptionType"
  - error type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
extends:
  - exception
related:
  - throw-exit-error
  - try-catch
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the exception classes in Erlang?"
  - "What is the difference between throw, exit, and error exceptions?"
  - "Which class do runtime errors carry?"
---

# Quick Definition

Every exception has a class — one of the atoms `throw`, `exit`, or `error` — that records how it was generated and is used in `try...catch` to dispatch on the kind of failure.

# Core Definition

In a `try...catch` expression, the catch clauses are tagged `ExceptionType:ExPattern`. "`ExceptionType` is an atom (one of `throw`, `exit`, or `error`) that tells us how the exception was generated. If `ExceptionType` is omitted, then the value defaults to `throw`" ("Error Handling in Sequential Programs", *Trapping an Exception with try...catch*). The book adds the important note: "Internal errors that are detected by the Erlang runtime system always have the tag `error`." The class corresponds to the BIF that raised the exception — `throw(Why)` produces class `throw`, `exit(Why)` produces class `exit`, and `error(Why)` (and all runtime-detected errors) produce class `error`.

# Prerequisites

- **Exception** — A class is an attribute of an exception, so the exception concept must be understood first.

# Key Properties

1. There are exactly three exception classes: `throw`, `exit`, and `error`.
2. `throw` exceptions are raised by `throw/1`.
3. `exit` exceptions are raised by `exit/1`.
4. `error` exceptions are raised by `error/1` and by all internal runtime errors.
5. In a `catch` clause, an omitted class tag defaults to `throw`.
6. The class is matched in `try...catch` with the `Class:Pattern` form.

# Construction / Recognition

## To Construct/Create:
1. The class is fixed by which BIF raised the exception; you do not set it independently.

## To Identify/Recognize:
1. In a caught exception, read the class atom before the colon in `Class:Value`.
2. A runtime-detected internal error always has class `error`.

# Context & Application

- **Typical contexts**: writing `catch` clauses that respond differently depending on whether an exception was thrown, an exit, or a crashing error.
- **Common applications**: the `catcher/1` function matches `throw:X`, `exit:X`, and `error:X` separately.
- **Historical/stylistic notes**: knowing that runtime errors always carry `error` lets a catch-all of `error:_` trap all system-generated faults.

# Examples

**Example 1** (*Programming Idioms with try...catch*): dispatching on each class:

```erlang
catch
    throw:X -> {N, caught, thrown, X};
    exit:X  -> {N, caught, exited, X};
    error:X -> {N, caught, error, X}
end.
```

The `demo1()` results show class `thrown` for `throw(a)`, `exited` for `exit(a)`, and `error` for `error(a)`.

# Relationships

## Builds Upon
- **Exception** — A class is a property of every exception.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **throw/exit/error** — Each BIF produces its corresponding class.
- **try...catch** — The catch patterns are tagged with a class.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Writing a catch clause `_ -> ...` expecting it to match `error`-class exceptions.
  **Correction**: An untagged clause defaults to class `throw`; specify `error:_` or use `_:_`.

# Common Confusions

- **Confusion**: Believing runtime errors can have class `throw` or `exit`.
  **Clarification**: All internal errors detected by the runtime system carry the class `error`.

- **Confusion**: Thinking the class and the exception reason are the same thing.
  **Clarification**: The class is the atom `throw`/`exit`/`error`; the reason is the separate arbitrary term passed to the raising BIF.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", section "Trapping an Exception with try...catch" (and the `catcher/1` example in "Programming Idioms with try...catch").

# Verification Notes

- Definition source: Direct quotation from *Trapping an Exception with try...catch*.
- Confidence rationale: HIGH — the source explicitly enumerates the three classes and states the runtime-error rule.
- Uncertainties: None.
- Cross-reference status: Slugs `exception`, `throw-exit-error`, `try-catch` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card content merged.
