---
# === CORE IDENTIFICATION ===
concept: Exit Reasons
slug: exit-reasons

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
section: "Exit Reasons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "exit reason"
  - "error reasons"
  - "crash reasons"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception-classes
  - runtime-errors
extends: []
related:
  - try-expression
  - catch-expression
  - stacktrace
  - process-termination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the common exit reasons in Erlang?"
  - "What does badarg mean in Erlang?"
  - "What does function_clause mean?"
  - "What does case_clause mean?"
  - "What is the structure of an exit reason for a runtime error?"
  - "What does undef mean in Erlang?"
---

# Quick Definition

When a runtime error (exception class `error`) occurs, the exit reason is a tuple `{Reason, Stack}` where `Reason` indicates the type of error (e.g., `badarg`, `badarith`, `function_clause`, `{case_clause, V}`) and `Stack` is the call-stack backtrace.

# Core Definition

When a runtime error occurs (exception of class `error`), the exit reason is a tuple `{Reason, Stack}`. `Reason` is a term indicating the type of error, and `Stack` is the stack of function calls being evaluated when the error occurred, given as a list of tuples `{Module, Name, Arity, ExtraInfo}` with the most recent function call first (Erlang Reference Manual, "Errors and Error Handling" chapter, "Exit Reasons" section).

# Prerequisites

- **exception-classes** — Exit reasons are part of the `error` class exception structure.
- **runtime-errors** — Exit reasons describe the type of runtime error.

# Key Properties

The following are the standard exit reasons defined by the runtime system:

1. **`badarg`** — Bad argument. The argument is of the wrong data type or is otherwise badly formed.
2. **`badarith`** — An argument for an arithmetic expression was not numeric, or the expression does not evaluate to a finite number.
3. **`{badmatch, V}`** — Evaluation of a match expression failed. The value `V` did not match.
4. **`function_clause`** — No matching function clause found when evaluating a function call.
5. **`{case_clause, V}`** — No matching branch found in a `case` expression. The value `V` did not match.
6. **`if_clause`** — No true branch found when evaluating an `if` expression.
7. **`{try_clause, V}`** — No matching branch found in the `of` section of a `try` expression. The value `V` did not match.
8. **`undef`** — The function cannot be found when evaluating a function call.
9. **`{badfun, F}`** — `F` was expected to be a fun, but is not.
10. **`{badarity, {Fun, Args}}`** — A fun is applied to the wrong number of arguments.
11. **`timeout_value`** — The timeout value in a `receive...after` is not an integer or `infinity`.
12. **`noproc`** — Trying to link or monitor a non-existing process or port.
13. **`noconnection`** — A link or monitor to a remote process was broken due to connection failure.
14. **`{nocatch, V}`** — Trying to evaluate a `throw` outside the scope of a `catch`/`try`. `V` is the thrown term.
15. **`system_limit`** — A system limit has been reached.

# Construction / Recognition

## To Recognize:
```erlang
%% In a catch expression:
{'EXIT', {badarg, Stack}} = catch hd([])

%% In a try expression:
try hd([])
catch error:badarg:Stack -> {badarg, Stack}
end
```

## Common Patterns:
```erlang
error:badarg          %% bad argument
error:badarith        %% bad arithmetic
error:{badmatch, V}   %% failed match, V is the value
error:function_clause  %% no matching function clause
error:{case_clause, V} %% no matching case clause
error:undef           %% undefined function
```

# Context & Application

Exit reasons are the primary diagnostic information for understanding why a process crashed. They appear in crash logs, supervisor reports, and error messages. Understanding common exit reasons helps in debugging and writing robust error handling. The structured format (`Reason` + `Stack`) provides both the category of error and the location where it occurred.

# Examples

**Example 1**: Common runtime errors and their exit reasons:

```erlang
1> catch 1 + a.
{'EXIT',{badarith,[...]}}

2> catch element(5, {a,b,c}).
{'EXIT',{badarg,[...]}}

3> catch lists:nonexistent(1).
{'EXIT',{undef,[...]}}

4> F = not_a_fun, catch F(1).
{'EXIT',{{badfun,not_a_fun},[...]}}
```

**Example 2**: Match failure exit reason:

```erlang
1> catch ({x,Y} = {a,b,c}).
{'EXIT',{{badmatch,{a,b,c}},[...]}}
```

**Example 3**: Case clause exit reason:

```erlang
1> catch (case foo of bar -> ok end).
{'EXIT',{{case_clause,foo},[...]}}
```

# Relationships

## Builds Upon
- **exception-classes** — Exit reasons are part of the `error` class.
- **runtime-errors** — Each runtime error produces an exit reason.

## Enables
- Error-specific handling in `try`/`catch` expressions.
- Crash diagnostics and logging.

## Related
- **try-expression** — `try` can match on specific exit reasons.
- **catch-expression** — `catch` returns exit reasons in `{'EXIT', {Reason, Stack}}` format.
- **stacktrace** — The `Stack` component of the exit reason.
- **process-termination** — Exit reasons are reported when processes terminate.

# Common Errors

- **Error**: Matching on `{badmatch, _}` as a bare atom instead of a tuple.
  **Correction**: Some exit reasons are tuples (e.g., `{badmatch, V}`, `{case_clause, V}`). Match accordingly.

- **Error**: Not including the stacktrace when logging error information.
  **Correction**: Always include the stacktrace for debugging. Use `error:Reason:Stack` in `try` to capture it.

# Common Confusions

- **Confusion**: Thinking `function_clause` and `undef` are the same.
  **Clarification**: `function_clause` means the function exists but no clause matched the arguments. `undef` means the function does not exist at all (not defined or not exported).

- **Confusion**: Thinking `badarg` is specific to function arguments.
  **Clarification**: `badarg` is a general "bad argument" error that can occur in BIF calls, operator applications, or any operation receiving an argument of the wrong type.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Exit Reasons" section.

# Verification Notes

- Definition source: Direct from source text — complete exit reason list reproduced
- Confidence rationale: High — comprehensive list with descriptions from source
- Uncertainties: None
- Cross-reference status: Exit reasons verified against expression error descriptions (if_clause, case_clause, etc.)
