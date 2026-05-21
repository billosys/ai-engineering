---
# === CORE IDENTIFICATION ===
concept: Exception
slug: exception

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
section: "Handling Errors in Sequential Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - raised exception
  - error condition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - throw-exit-error
  - try-catch
  - catch-expression
  - error-class
contrasts_with:
  - error-return-tuple

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an exception in Erlang?"
  - "How do I handle errors in sequential programs?"
  - "When does the system raise an exception automatically?"
---

# Quick Definition

An exception is what happens when a function cannot return a sensible value — "the technical term for crashing." Exceptions are raised automatically by the system on internal errors or explicitly with `throw`, `exit`, or `error`.

# Core Definition

"Every time we call a function in Erlang, one of two things will happen: either the function returns a value or something goes wrong" ("Error Handling in Sequential Programs", *Handling Errors in Sequential Code*). When there is no sensible value to return, "instead of returning a value, the system raises an exception — this is the technical term for 'crashing.'" Exceptions are raised by the system when internal errors are encountered, or explicitly in code by calling `throw(Exception)`, `exit(Exception)`, or `error(Exception)`. Typical internal errors that raise exceptions are pattern matching errors (no clause in a function matches), calling BIFs with incorrectly typed arguments, or calling a BIF with an invalid argument value (such as dividing by zero).

# Prerequisites

- **Pattern matching** — Many exceptions arise from pattern matching failures, and exceptions are handled by matching them.

# Key Properties

1. An exception occurs when a function has no sensible value to return.
2. It can be generated automatically by the runtime (internal errors).
3. It can be raised explicitly with `throw`, `exit`, or `error`.
4. Internal errors detected by the runtime always carry the tag `error`.
5. An uncaught exception crashes the current process.
6. It is up to the caller, not the failing function, to decide how to respond.

# Construction / Recognition

## To Construct/Create:
1. Cause one automatically — e.g. call a function with arguments no clause matches (`cost(socks)`).
2. Raise one explicitly with `throw(Why)`, `exit(Why)`, or `error(Why)`.

## To Identify/Recognize:
1. The shell or error log shows `** exception error: ...` with a reason and location.
2. Catch the exception with `try...catch` to inspect its class and value.

# Context & Application

- **Typical contexts**: invalid input, missing function clauses, type errors in BIF calls.
- **Common applications**: the basis for the "let it crash" approach to error handling.
- **Historical/stylistic notes**: Erlang treats defensive programming as built-in — describe behavior only for valid inputs; all other arguments raise automatically detected internal errors.

# Examples

**Example 1** (*Handling Errors in Sequential Code*): an automatic exception from a missing clause:

```erlang
cost(oranges) -> 5;
cost(newspaper) -> 8;
cost(apples) -> 2;
cost(pears) -> 9;
cost(milk) -> 7.
```

```erlang
2> shop:cost(socks).
** exception error: no function clause matching
shop:cost(socks) (shop.erl, line 5)
```

Calling `cost(socks)` crashes — there is no sensible value for the price of socks, so the system raises an exception.

# Relationships

## Builds Upon
- This is a foundational error-handling concept with no error-handling prerequisites within this source.

## Enables
- **try...catch** — Used to trap and dispatch on exceptions.
- **catch expression** — The other mechanism for trapping exceptions.

## Related
- **throw/exit/error** — The three BIFs that raise exceptions explicitly.
- **Error class** — Each exception carries one of the classes `throw`, `exit`, or `error`.

## Contrasts With
- **Error return tuple** — Returning `{error, Reason}` is the alternative to raising an exception when errors are common.

# Common Errors

- **Error**: Writing defensive argument checks that return a value for invalid input.
  **Correction**: Never return a value for invalid arguments — raise an exception ("let it crash").

- **Error**: Trying to "repair" an exception inside the failing function.
  **Correction**: The failing function cannot repair the error; the caller decides what to do.

# Common Confusions

- **Confusion**: Believing an exception always means a programmer mistake.
  **Clarification**: An exception simply means there is no sensible value to return; it can be a normal, expected outcome (e.g. invalid user input).

- **Confusion**: Thinking the failing function should handle the exception.
  **Clarification**: Responsibility for handling lies with the caller of the function that crashed.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", section "Handling Errors in Sequential Code".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Handling Errors in Sequential Code*.
- Confidence rationale: HIGH — the source explicitly defines exceptions and the conditions that raise them.
- Uncertainties: None.
- Cross-reference status: Slugs `throw-exit-error`, `try-catch`, `catch-expression`, `error-class` extracted in this chapter; `pattern-matching` assumed canonical; `error-return-tuple` exists.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
