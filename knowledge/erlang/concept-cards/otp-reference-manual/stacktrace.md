---
# === CORE IDENTIFICATION ===
concept: Stacktrace
slug: stacktrace

# === CLASSIFICATION ===
category: error-handling
subcategory: exception-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "The call-stack backtrace (stacktrace)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "call-stack backtrace"
  - "stack backtrace"
  - "stack trace"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception-classes
  - exit-reasons
extends: []
related:
  - try-expression
  - try-stacktrace
  - catch-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a stacktrace in Erlang?"
  - "What information does a stacktrace contain?"
  - "How do I access the stacktrace of an exception?"
  - "What is the format of stacktrace entries?"
  - "Can I rely on the stacktrace for program logic?"
---

# Quick Definition

A stacktrace is a list of tuples providing the call-stack backtrace at the point where an exception occurred. Each entry contains `{Module, Function, Arity, ExtraInfo}` or `{Fun, Arity, ExtraInfo}`, with the most recent call first.

# Core Definition

The stack backtrace (stacktrace) is a list that contains `{Module, Function, Arity, ExtraInfo}` and/or `{Fun, Arity, ExtraInfo}` tuples. The field `Arity` can be the argument list of the function call instead of an arity integer, depending on the exception. `ExtraInfo` is a (possibly empty) list of two-element tuples providing additional information: `error_info` (a map with additional error details, created via `error/3`), `file` (source filename), and `line` (line number). The stacktrace can be bound to a variable from within a `try` expression for any exception class, or extracted from the exit reason when caught by `catch` (Erlang Reference Manual, "Errors and Error Handling" chapter, "The call-stack backtrace" section).

# Prerequisites

- **exception-classes** — Stacktraces are part of every exception.
- **exit-reasons** — For `error` class exceptions, the stacktrace is part of the exit reason tuple.

# Key Properties

1. A list of `{Module, Function, Arity, ExtraInfo}` or `{Fun, Arity, ExtraInfo}` tuples.
2. Most recent function call is first in the list.
3. `Arity` may be the actual argument list instead of an integer.
4. `ExtraInfo` may include `error_info`, `file`, and `line` entries.
5. Tail call optimization removes entries from the stacktrace.
6. Stacktraces are limited to a certain depth by the VM.
7. **Warning**: Should only be relied upon for debugging, not program logic.
8. Exception: `error:undef` is guaranteed to have the `{Module, Function, Arity}` of the attempted call as the first entry.
9. Compiler options, optimizations, and future changes may add or remove entries.

# Construction / Recognition

## To Access via try:
```erlang
try dangerous()
catch
    Class:Reason:Stacktrace ->
        {Class, Reason, Stacktrace}
end
```

## To Access via catch:
```erlang
{'EXIT', {Reason, Stacktrace}} = catch error(test)
```

## Entry Format:
```erlang
{Module, Function, Arity, [{file, "filename.erl"}, {line, 42}]}
```

# Context & Application

Stacktraces are essential for debugging errors. They show the chain of function calls that led to an exception, including file and line information when available. However, because tail call optimization eliminates stack frames and the VM limits stacktrace depth, the trace may not show the complete call history. Programs should not depend on stacktrace structure for logic, only for diagnostic purposes.

# Examples

**Example 1** (Exceptions section): Getting a stacktrace via catch:

```erlang
> {'EXIT',{test,Stacktrace}} = (catch error(test)), Stacktrace.
[{shell,apply_fun,3,[]},
 {erl_eval,do_apply,6,[]},
 ...]
```

**Example 2** (Exceptions section): Getting a stacktrace via try:

```erlang
> try throw(test) catch Class:Reason:Stacktrace -> Stacktrace end.
[{shell,apply_fun,3,[]},
 {erl_eval,do_apply,6,[]},
 ...]
```

**Example 3**: Stacktrace entry with file and line information:

```erlang
{my_module, my_function, 2, [{file, "my_module.erl"}, {line, 15}]}
```

# Relationships

## Builds Upon
- **exception-classes** — Every exception carries a stacktrace.
- **exit-reasons** — The stacktrace is part of the `error` class exit reason.

## Related
- **try-expression** — `try` can bind the stacktrace to a variable.
- **try-stacktrace** — Detailed coverage of stacktrace binding in `try`.
- **catch-expression** — `catch` includes the stacktrace in the `{'EXIT', ...}` tuple.

# Common Errors

- **Error**: Using stacktrace entries for program logic (branching based on specific modules or functions in the trace).
  **Correction**: Stacktraces should only be used for debugging. Tail call optimization, depth limits, and VM changes can alter the trace.

- **Error**: Expecting a complete call chain in the stacktrace.
  **Correction**: Tail call optimization removes intermediate frames. The stacktrace may be truncated by the VM's depth limit.

# Common Confusions

- **Confusion**: Thinking the stacktrace always contains argument lists.
  **Clarification**: The `Arity` field may be an integer (arity) or the actual argument list, depending on the exception and context.

- **Confusion**: Expecting stacktraces to be identical across OTP versions.
  **Clarification**: Compiler options, optimizations, and OTP version changes may add or remove stacktrace entries.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "The call-stack backtrace (stacktrace)" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — comprehensive format description and warnings from source
- Uncertainties: None
- Cross-reference status: Verified against try-stacktrace and catch-expression cards
