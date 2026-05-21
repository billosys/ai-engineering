---
# === CORE IDENTIFICATION ===
concept: Generated Errors
slug: generated-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-types
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "Terminology"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "intentional errors"
  - "explicit exceptions"
  - "exit and throw exceptions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception-classes
extends: []
related:
  - runtime-errors
  - try-expression
  - catch-expression
contrasts_with:
  - runtime-errors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a generated error in Erlang?"
  - "How do generated errors differ from runtime errors?"
  - "When should I use exit/1 vs throw/1?"
---

# Quick Definition

Generated errors are exceptions intentionally raised by code calling `exit/1` (class `exit`) or `throw/1` (class `throw`), as opposed to runtime errors that arise from operational failures.

# Core Definition

Generated errors occur when code itself calls `exit/1` or `throw/1`. They are exceptions of class `exit` or `throw`, respectively. This distinguishes them from runtime errors (class `error`) which arise from operational failures like type mismatches or undefined functions. `exit/1` is used for intentional process termination or signaling abnormal conditions through process links. `throw/1` is used for non-local returns and must be evaluated within a `catch` or `try`/`catch`; otherwise a `nocatch` runtime error occurs (Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section).

# Prerequisites

- **exception-classes** — Generated errors are the `exit` and `throw` classes.

# Key Properties

1. `exit/1` raises an exception of class `exit`.
2. `throw/1` raises an exception of class `throw`.
3. Both can be caught by `try`/`catch` or `catch`.
4. `exit/1` is typically used for intentional process termination.
5. `throw/1` is used for non-local returns; must be within a catcher or `nocatch` error occurs.
6. Generated errors are intentional — the programmer explicitly raises them.
7. Distinct from runtime errors which arise from unintended operational failures.

# Construction / Recognition

## To Generate:
```erlang
exit(normal)            %% normal process termination
exit({shutdown, Reason}) %% shutdown with reason
throw(not_found)        %% non-local return
```

## To Handle:
```erlang
try search(List)
catch
    throw:not_found -> default_value;
    exit:Reason -> {exited, Reason}
end
```

# Context & Application

Generated errors serve different purposes from runtime errors. `exit/1` is used in OTP patterns for process lifecycle management — a process calls `exit(normal)` for clean shutdown or `exit({shutdown, Reason})` for supervised shutdown. `throw/1` is used for control flow (e.g., aborting a deep recursion with a result) rather than signaling a bug. Understanding the distinction helps in choosing the right exception class and writing appropriate error handlers.

# Examples

**Example 1**: Using exit for process termination:

```erlang
loop(State) ->
    receive
        stop -> exit(normal);
        {error, Reason} -> exit({error, Reason})
    end.
```

**Example 2**: Using throw for non-local return:

```erlang
find(Key, [{Key, Value} | _]) -> throw({found, Value});
find(Key, [_ | T]) -> find(Key, T);
find(_, []) -> not_found.

search(Key, List) ->
    try find(Key, List)
    catch
        throw:{found, Value} -> {ok, Value}
    end.
```

# Relationships

## Builds Upon
- **exception-classes** — Generated errors are the `exit` and `throw` exception classes.

## Related
- **runtime-errors** — The other type of exception (class `error`).
- **try-expression** — Can distinguish generated errors from runtime errors.
- **catch-expression** — Catches all exception classes.

## Contrasts With
- **runtime-errors** — Runtime errors are unintentional operational failures (class `error`); generated errors are intentional (classes `exit` and `throw`).

# Common Errors

- **Error**: Using `throw/1` outside any `catch` or `try`/`catch` scope.
  **Correction**: Ensure `throw/1` is always within a catching context. Uncaught throws become `{nocatch, V}` runtime errors.

- **Error**: Using `exit/1` to signal a recoverable condition.
  **Correction**: Use `throw/1` for recoverable non-local returns. Reserve `exit/1` for process termination conditions.

# Common Confusions

- **Confusion**: Thinking `exit/1` always terminates the process immediately.
  **Clarification**: `exit/1` raises an exception that can be caught by `try`/`catch`. The process only terminates if the exception is uncaught.

- **Confusion**: Not distinguishing between `exit/1` (raises an exception in the calling process) and `exit/2` (sends an exit signal to another process).
  **Clarification**: `exit/1` is for the calling process's own exception. `exit/2` sends a signal to a different process.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — directly defined in source
- Uncertainties: None
- Cross-reference status: Part of four-category error taxonomy; linked to exception classes
