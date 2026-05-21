---
# === CORE IDENTIFICATION ===
concept: Runtime Errors
slug: runtime-errors

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
  - "run-time errors"
  - "runtime exceptions"
  - "crashes"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - exception-classes
  - exit-reasons
  - try-expression
  - catch-expression
contrasts_with:
  - compile-time-errors
  - logical-errors
  - generated-errors

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a runtime error in Erlang?"
  - "What exception class do runtime errors belong to?"
  - "How can runtime errors be handled?"
  - "What happens when a runtime error is not caught?"
---

# Quick Definition

Runtime errors occur when a crash happens during program execution, such as applying an operator to arguments of the wrong type. They are exceptions of class `error` and can be caught with `try`/`catch` or `catch`.

# Core Definition

Runtime errors occur when a crash happens during execution, for example when an operator is applied to arguments of the wrong type. Erlang has built-in features for handling runtime errors. A runtime error can also be emulated by calling `error(Reason)`. Runtime errors are exceptions of class `error`. When a runtime error occurs and is not caught, the process that evaluated the erroneous expression terminates, emitting an exit signal with an exit reason that describes why the process terminated (Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section).

# Prerequisites

None.

# Key Properties

1. Occur during program execution.
2. Exception class: `error`.
3. Can be caught with `try`/`catch` or `catch` expressions.
4. Can be emulated with `error(Reason)` or `error(Reason, Args)` or `error(Reason, Args, Options)`.
5. Uncaught runtime errors cause process termination.
6. The exit reason is a tuple `{Reason, Stack}` where `Reason` indicates the error type.
7. Terminating processes emit exit signals to linked processes.

# Construction / Recognition

## To Trigger:
```erlang
1 + a.                    %% badarith
element(5, {a,b,c}).      %% badarg
hd([]).                   %% badarg
error(my_reason).         %% explicit error
```

## To Handle:
```erlang
try dangerous_operation()
catch
    error:Reason:Stacktrace -> {error, Reason, Stacktrace}
end
```

# Context & Application

Runtime errors are central to Erlang's error handling philosophy. The "let it crash" approach encourages letting processes fail on unexpected errors, relying on supervisors to restart them. Selective error handling via `try`/`catch` is used when recovery is possible and meaningful. Runtime errors carry a stacktrace for debugging.

# Examples

**Example 1** (Terminology section): Arithmetic error:

```erlang
1> 1 + a.
** exception error: an error occurred when evaluating an arithmetic expression
```

**Example 2**: Catching a runtime error:

```erlang
1> catch 1 + a.
{'EXIT',{badarith,[...]}}
```

**Example 3**: Emulating a runtime error:

```erlang
1> error(my_custom_error).
** exception error: my_custom_error
```

# Relationships

## Enables
- **exception-classes** — Runtime errors are the `error` class of exceptions.
- **exit-reasons** — Runtime errors produce specific exit reasons.
- **try-expression** — `try` can catch runtime errors with `error:Pattern`.
- **catch-expression** — `catch` returns `{'EXIT', {Reason, Stack}}` for runtime errors.

## Related
- **generated-errors** — Exceptions of class `exit` or `throw`, intentionally raised by code.

## Contrasts With
- **compile-time-errors** — Compile-time errors prevent execution; runtime errors occur during execution.
- **logical-errors** — Logical errors don't crash; runtime errors do.
- **generated-errors** — Runtime errors are class `error`; generated errors are class `exit` or `throw`.

# Common Errors

- **Error**: Catching all runtime errors with a broad `catch error:_ -> ok` and silently discarding them.
  **Correction**: Only catch errors you can meaningfully recover from. Let unexpected errors crash the process so supervisors can restart it cleanly.

# Common Confusions

- **Confusion**: Thinking all exceptions are runtime errors.
  **Clarification**: Exceptions come in three classes: `error` (runtime errors), `exit` (intentional exits), and `throw` (non-local returns). Only `error` class exceptions are runtime errors.

- **Confusion**: Thinking a runtime error always terminates the entire application.
  **Clarification**: A runtime error terminates only the process where it occurred. Other processes continue, and supervisors can restart the failed process.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Terminology" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — directly defined in source
- Uncertainties: None
- Cross-reference status: Part of four-category error taxonomy; linked to exception classes
