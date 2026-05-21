---
# === CORE IDENTIFICATION ===
concept: catch Expression
slug: catch-expression

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
section: "Trapping an Exception with catch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - catch primitive
  - bare catch

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
extends: []
related:
  - stack-trace
  - throw-exit-error
contrasts_with:
  - try-catch

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I trap an exception with catch?"
  - "How does the catch primitive differ from try...catch?"
  - "What does catch return when an exception occurs?"
---

# Quick Definition

The `catch` primitive evaluates an expression and, if an exception occurs within it, converts the exception into an `{'EXIT', ...}` tuple instead of crashing.

# Core Definition

`catch` is a primitive for trapping an exception. "The `catch` primitive is not the same as the `catch` block in the `try...catch` statement (this is because the `catch` statement was part of the language long before `try...catch` was introduced)" ("Error Handling in Sequential Programs", *Trapping an Exception with catch*). When an exception occurs within a `catch` expression, "it is converted into an `{'EXIT', ...}` tuple that describes the error." If the expression evaluates normally, `catch` simply yields the expression's value. Compared with `try...catch`, the bare `catch` provides a more detailed stack trace but does not let you dispatch on the exception class.

# Prerequisites

- **Exception** — `catch` exists to trap exceptions.

# Key Properties

1. `catch` is a separate, older primitive — distinct from the `catch` block of `try...catch`.
2. On normal evaluation, `catch Expr` returns the value of `Expr`.
3. On an exception, `catch` returns an `{'EXIT', ...}` tuple describing the error.
4. The `{'EXIT', ...}` tuple includes a detailed stack trace.
5. `catch` cannot pattern-match on the exception class the way `try...catch` can.

# Construction / Recognition

## To Construct/Create:
1. Wrap an expression: `catch generate_exception(I)`.
2. Often combined with a comprehension to collect results and trapped errors together.

## To Identify/Recognize:
1. A result of the form `{'EXIT', Reason}` indicates `catch` trapped an exception.

# Context & Application

- **Typical contexts**: quick trapping of any error when a detailed stack trace is wanted and class dispatch is not needed.
- **Common applications**: the `demo2` function calls `generate_exception` inside `catch` within a list comprehension.
- **Historical/stylistic notes**: `catch` predates `try...catch`; the newer construct is generally preferred for new code because of its richer dispatch.

# Examples

**Example 1** (*Trapping an Exception with catch*): trapping exceptions in a comprehension:

```erlang
demo2() ->
    [{I, (catch generate_exception(I))} || I <- [1,2,3,4,5]].
```

Running `try_test:demo2()` yields entries like `{1,a}`, `{2,a}`, `{3,{'EXIT',a}}`, `{4,{'EXIT',a}}`, and a `{5,{'EXIT',{a,[...stack trace...]}}}`. The `throw` and `error`/`exit` cases produce differing amounts of detail; `catch` provides a detailed stack trace.

# Relationships

## Builds Upon
- This builds directly on the exception concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Stack trace** — A `catch` of a crashing error yields an `{'EXIT', ...}` tuple containing a full stack trace.
- **throw/exit/error** — The exceptions `catch` traps.

## Contrasts With
- **try...catch** — `try...catch` summarizes exception information and supports class dispatch and an `after` block; bare `catch` returns an `{'EXIT', ...}` tuple with a detailed trace but no class dispatch.

# Common Errors

- **Error**: Confusing the `catch` primitive with the `catch` keyword inside `try...catch`.
  **Correction**: They are different constructs; the bare `catch` is a standalone primitive.

- **Error**: Treating a normal `{'EXIT', Reason}` return value as proof an exception occurred.
  **Correction**: A function may legitimately return such a tuple; only `catch` converting an actual exception produces it from a crash.

# Common Confusions

- **Confusion**: Thinking `catch` lets you handle `throw`, `exit`, and `error` separately.
  **Clarification**: Bare `catch` collapses all exceptions into an `{'EXIT', ...}` tuple; use `try...catch` to dispatch on class.

- **Confusion**: Believing `catch` and `try...catch` give the same debug detail.
  **Clarification**: `catch` provides a more detailed stack trace; `try...catch` (in the book's example) gives summarized information.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", section "Trapping an Exception with catch".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Trapping an Exception with catch*.
- Confidence rationale: HIGH — the source explicitly explains the primitive, its `{'EXIT', ...}` conversion, and its contrast with `try...catch`.
- Uncertainties: None.
- Cross-reference status: Slugs `exception`, `try-catch`, `stack-trace`, `throw-exit-error` extracted in this chapter.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
