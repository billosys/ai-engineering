---
# === CORE IDENTIFICATION ===
concept: Error Handling Within Processes
slug: error-handling-within-processes

# === CLASSIFICATION ===
category: error-handling
subcategory: process-error-handling
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "Handling of Run-time Errors in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "intra-process error handling"
  - "local error handling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception-classes
extends: []
related:
  - try-expression
  - catch-expression
  - error-handling-between-processes
contrasts_with:
  - error-handling-between-processes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle errors within a single Erlang process?"
  - "What mechanisms exist for catching exceptions in Erlang?"
  - "When should I use try/catch vs letting a process crash?"
---

# Quick Definition

Error handling within a single process uses `try` or `catch` expressions to prevent runtime errors and other exceptions from causing the process to terminate, allowing local recovery.

# Core Definition

It is possible to prevent runtime errors and other exceptions from causing the process to terminate by using `try` or `catch` expressions. The `try` expression provides structured exception handling with the ability to distinguish between exception classes (`error`, `exit`, `throw`). The `catch` expression is a simpler mechanism that catches all exceptions but cannot distinguish between classes (Erlang Reference Manual, "Errors and Error Handling" chapter, "Error Handling Within Processes" section).

# Prerequisites

- **exception-classes** — Must understand the three exception classes to handle them appropriately.

# Key Properties

1. Uses `try`/`catch` or `catch` expressions.
2. `try` can distinguish between `error`, `exit`, and `throw` classes.
3. `catch` catches all exceptions but wraps them differently per class.
4. Only catches exceptions within the same process.
5. Prevents process termination for caught exceptions.
6. The "let it crash" philosophy recommends selective use: catch only expected, recoverable errors.

# Construction / Recognition

## With try:
```erlang
try risky_operation()
catch
    error:badarg -> handle_badarg();
    throw:Value -> handle_throw(Value);
    exit:Reason -> handle_exit(Reason)
end
```

## With catch:
```erlang
Result = catch risky_operation()
```

# Context & Application

Error handling within processes is used when local recovery from an error is possible and meaningful. The Erlang philosophy generally favors letting processes crash and relying on supervisors, but within-process error handling is appropriate for expected exceptional conditions (e.g., file not found, invalid user input, network timeout). It is the complement to between-process error handling via links and monitors.

# Examples

**Example 1**: Handling a file operation error:

```erlang
read_config(Path) ->
    try
        {ok, Bin} = file:read_file(Path),
        {ok, parse_config(Bin)}
    catch
        error:{badmatch, {error, enoent}} ->
            {error, not_found};
        error:{badmatch, {error, Reason}} ->
            {error, Reason}
    end.
```

**Example 2**: Using catch for simple error suppression:

```erlang
safe_divide(A, B) ->
    case catch (A / B) of
        {'EXIT', {badarith, _}} -> {error, division_by_zero};
        Result -> {ok, Result}
    end.
```

# Relationships

## Builds Upon
- **exception-classes** — Understanding classes is needed for `try`/`catch` usage.

## Enables
- Local error recovery within a process.

## Related
- **try-expression** — The primary mechanism for within-process error handling.
- **catch-expression** — The simpler, older mechanism.

## Contrasts With
- **error-handling-between-processes** — Between-process handling uses links/monitors; within-process handling uses `try`/`catch`.

# Common Errors

- **Error**: Using a bare `catch` expression and forgetting it wraps errors in `{'EXIT', Reason}` tuples rather than raising.
  **Correction**: Prefer `try`/`catch` which separates exception classes cleanly; if using `catch`, always match the `{'EXIT', _}` wrapper.

# Common Confusions

- **Confusion**: Thinking `try`/`catch` should be used everywhere for defensive programming.
  **Clarification**: Erlang's philosophy favors "let it crash" for unexpected errors. Use `try`/`catch` selectively for expected, recoverable conditions.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Error Handling Within Processes" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — directly described in source
- Uncertainties: None
- Cross-reference status: Verified relationship with try-expression and catch-expression
