---
# === CORE IDENTIFICATION ===
concept: Try Stacktrace
slug: try-stacktrace

# === CLASSIFICATION ===
category: error-handling
subcategory: exception-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Try"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "stacktrace binding"
  - "exception stacktrace"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - try-expression
extends:
  - try-expression
related:
  - stacktrace
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I capture the stacktrace in a try-catch expression?"
  - "How do I bind the stacktrace when catching an exception?"
---

# Quick Definition

In a `try` expression, the stacktrace can be bound to a variable using the `Class:Pattern:Stacktrace` syntax in catch clauses, providing the call-stack backtrace at the point of the exception.

# Core Definition

Within a `try` expression's `catch` clause, the syntax `Class:ExceptionPattern:Stacktrace` allows binding the stack trace to a variable when the corresponding `ExceptionPattern` matches. `Stacktrace` must be the name of a variable (not a pattern). The stack trace is bound to this variable when the match succeeds. This works for any exception class (`error`, `exit`, `throw`). When a runtime error is caught by the standalone `catch` expression, the stacktrace is part of the exit reason: `{'EXIT', {Reason, Stacktrace}}` (Erlang Reference Manual, "Try" section and "Exceptions" section in Errors chapter).

# Prerequisites

- **try-expression** — Stacktrace binding is a feature of the `try` expression's `catch` clause.

# Key Properties

1. Syntax: `Class:Pattern:StacktraceVar` in a `try...catch` clause.
2. `StacktraceVar` must be a plain variable name, not a pattern.
3. Available for all exception classes (`error`, `exit`, `throw`).
4. The stacktrace is optional — it can be omitted: `Class:Pattern`.
5. In standalone `catch`, the stacktrace for `error` class is embedded in `{'EXIT', {Reason, Stack}}`.

# Construction / Recognition

## To Capture a Stacktrace:
1. Use `try ... catch Class:Pattern:Stk -> ... end`.
2. `Stk` is now bound to the stacktrace.

## To Recognize:
1. Look for three colon-separated components in a `catch` clause pattern.

# Context & Application

Stacktrace binding is essential for error logging and debugging. It provides the call chain that led to the exception, enabling detailed error reports. The stacktrace should primarily be used for debugging, not for control flow, as the VM may optimize away entries through tail call optimization.

# Examples

**Example 1** (Exceptions section): Binding stacktrace in try:

```erlang
> try throw(test) catch Class:Reason:Stacktrace -> Stacktrace end.
[{shell,apply_fun,3,[]},
 {erl_eval,do_apply,6,[]},
 ...]
```

**Example 2** (Try section): Using stacktrace in catch clauses:

```erlang
try Expr
catch
    throw:Term -> Term;
    exit:Reason -> {'EXIT',Reason};
    error:Reason:Stk -> {'EXIT',{Reason,Stk}}
end
```

# Relationships

## Builds Upon
- **try-expression** — Stacktrace binding is a feature of `try`'s `catch` clause.

## Enables
- No directly dependent concepts.

## Related
- **stacktrace** — The stacktrace structure and its contents.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Trying to use a pattern (not a plain variable) for the stacktrace binding.
  **Correction**: The stacktrace position must be a single variable name.

# Common Confusions

- **Confusion**: Expecting the stacktrace to always contain complete call information.
  **Clarification**: The VM performs tail call optimization and limits stacktrace depth. Entries may be removed or added by compiler optimizations.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Try" section; "Errors and Error Handling" chapter, "Exceptions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax and examples provided
- Uncertainties: None
- Cross-reference status: Prerequisites verified
