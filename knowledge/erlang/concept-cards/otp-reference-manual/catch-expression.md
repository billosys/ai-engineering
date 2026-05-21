---
# === CORE IDENTIFICATION ===
concept: Catch Expression
slug: catch-expression

# === CLASSIFICATION ===
category: error-handling
subcategory: exception-handling
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Catch and Throw"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "catch operator"
  - "catch and throw"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - try-expression
  - exception-classes
  - operator-precedence
contrasts_with:
  - try-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I catch exceptions in Erlang?"
  - "What does the catch expression return for different exception classes?"
  - "What is the difference between catch and try?"
---

# Quick Definition

The `catch` expression evaluates an expression and returns its value normally, or catches any exception and returns a transformed value. It cannot distinguish between exception classes.

# Core Definition

The expression `catch Expr` returns the value of `Expr` unless an exception is raised during evaluation. If an exception occurs, the return value depends on the class: for `error` (runtime error or `error(Term)`), it returns `{'EXIT', {Reason, Stack}}`; for `exit` (`exit(Term)`), it returns `{'EXIT', Term}`; for `throw` (`throw(Term)`), it returns `Term` directly. The BIF `throw(Any)` can be used for non-local return from a function — it must be evaluated within a `catch`, which returns `Any`. If `throw/1` is not evaluated within a catch, a `nocatch` runtime error occurs (Erlang Reference Manual, "Catch and Throw" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Syntax: `catch Expr`.
2. Returns `Expr` value on success.
3. On `error` exception: returns `{'EXIT', {Reason, Stack}}`.
4. On `exit` exception: returns `{'EXIT', Term}`.
5. On `throw` exception: returns `Term` (the thrown value directly).
6. Cannot distinguish between `exit` and `error` exception classes (both wrapped in `{'EXIT', ...}`).
7. Since Erlang/OTP 24, `catch` has higher precedence than `=` and `!`, so `A = catch 42` works without parentheses.
8. Before OTP 24, parentheses were required: `A = (catch 42)`.

# Construction / Recognition

## To Use Catch:
1. Write `catch Expr` where `Expr` is the expression to protect.
2. Check the return value for the `{'EXIT', ...}` tuple to detect exceptions.

## To Recognize:
1. Look for the `catch` keyword followed by a single expression (not inside a `try` block).

# Context & Application

`catch` is the simpler and older exception-handling mechanism in Erlang. It is useful for quick-and-dirty error handling but has the limitation of not being able to distinguish between `error` and `exit` exceptions. For production code, `try` is generally preferred because it provides explicit exception class matching. `catch` combined with `throw` provides a non-local return mechanism.

# Examples

**Example 1** (Catch and Throw section): Normal evaluation:

```erlang
1> catch 1+2.
3
```

**Example 2** (Catch and Throw section): Catching a runtime error:

```erlang
2> catch 1+a.
{'EXIT',{badarith,[...]}}
```

**Example 3** (Catch and Throw section): Catching a throw:

```erlang
3> catch throw(hello).
hello
```

**Example 4** (Catch and Throw section): Assignment with catch (OTP 24+):

```erlang
1> A = catch 42.
42
2> A.
42
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- No directly dependent concepts.

## Related
- **try-expression** — The `try` expression is the enhanced successor to `catch`.
- **exception-classes** — Understanding exception classes clarifies `catch` return values.
- **operator-precedence** — `catch` has specific precedence in the operator table.

## Contrasts With
- **try-expression** — `try` can distinguish between exception classes; `catch` cannot.

# Common Errors

- **Error**: Using `catch` to distinguish between `error` and `exit` exceptions.
  **Correction**: Use `try...catch` instead, which provides explicit `Class:Reason` matching.

- **Error**: Calling `throw/1` outside any `catch` or `try`.
  **Correction**: Ensure `throw/1` is always within the scope of a `catch` or `try`; otherwise a `nocatch` error occurs.

# Common Confusions

- **Confusion**: Thinking the `catch` keyword in `try...catch...end` is the same as the standalone `catch` expression.
  **Clarification**: They are distinct constructs. The standalone `catch Expr` is a simpler, older form. The `catch` in `try...catch...end` is part of the `try` expression syntax.

- **Confusion**: Expecting `catch` to return error and exit exceptions differently.
  **Clarification**: Both `error` and `exit` exceptions are wrapped in `{'EXIT', ...}` tuples, making them indistinguishable through `catch`.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Catch and Throw" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit return values for each exception class documented
- Uncertainties: None
- Cross-reference status: Contrasts with try-expression verified
