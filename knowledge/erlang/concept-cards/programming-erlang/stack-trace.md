---
# === CORE IDENTIFICATION ===
concept: Stack Trace
slug: stack-trace

# === CLASSIFICATION ===
category: error-handling
subcategory: diagnostics
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Error Handling in Sequential Programs"
chapter_number: 6
pdf_page: null
section: "Stack Traces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erlang:get_stacktrace()"
  - stacktrace
  - call stack trace

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
extends: []
related:
  - try-catch
  - catch-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a stack trace?"
  - "How do I obtain the stack trace of a caught exception?"
  - "Why might a stack trace not show where a function was called from?"
---

# Quick Definition

A stack trace is a list of `{Mod,Func,Arity,Info}` tuples showing where a crashed function would have returned to; it is obtained after catching an exception with `erlang:get_stacktrace()`.

# Core Definition

"When an exception is caught, we can find the latest stack trace by calling `erlang:get_stacktrace()`" ("Error Handling in Sequential Programs", *Stack Traces*). The stack trace "contains information about where the current function (which crashed) would have returned to had it succeeded." The individual tuples are of the form `{Mod,Func,Arity,Info}`, where `Mod`, `Func`, and `Arity` denote a function and `Info` contains the filename and line number of the item in the trace. Because Erlang applies a last-call optimization, if a function was the last call in a sequence of expressions, the trace records only where it will *return to*, not where it was called from.

# Prerequisites

- **Exception** — A stack trace is obtained in the context of a caught exception.

# Key Properties

1. Retrieved with `erlang:get_stacktrace()` after catching an exception.
2. A list of `{Mod,Func,Arity,Info}` tuples.
3. `Info` carries the filename and line number for each entry.
4. Describes return points — where each function would have returned to.
5. Last-call optimization means call sites of tail calls are not retained.
6. The top two entries usually pinpoint where the error occurred.

# Construction / Recognition

## To Construct/Create:
1. Inside a `catch` clause, call `erlang:get_stacktrace()` and pair it with the caught value.

## To Identify/Recognize:
1. Read the trace top-down: the first tuple is the crashing function, the next is its caller's return point, and so on.

# Context & Application

- **Typical contexts**: diagnosing where a sequential program crashed.
- **Common applications**: `demo3` catches an `error` exception and returns `{X, erlang:get_stacktrace()}`.
- **Historical/stylistic notes**: examining the trace gives a good indication of where execution was at the time of the error.

# Examples

**Example 1** (*Stack Traces*): capturing the trace of a caught error:

```erlang
demo3() ->
    try generate_exception(5)
    catch
        error:X ->
            {X, erlang:get_stacktrace()}
    end.
```

`try_test:demo3()` returns a trace beginning `{try_test,generate_exception,1,[{file,"try_test.erl"},{line,9}]}` — showing the crash occurred in `generate_exception/1` at line 9 — followed by `{try_test,demo3,0,...}` and further frames.

# Relationships

## Builds Upon
- This builds directly on the exception concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **try...catch** — The trace is fetched inside a catch clause.
- **catch expression** — The bare `catch` primitive embeds a stack trace in its `{'EXIT', ...}` tuple.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Expecting the trace to show the exact call site of every function.
  **Correction**: Tail calls are last-call optimized, so the trace records return points, not call sites, for those calls.

- **Error**: Calling `erlang:get_stacktrace()` long after the exception.
  **Correction**: It returns the *latest* stack trace; capture it promptly inside the catch clause.

# Common Confusions

- **Confusion**: Believing a stack trace shows where functions were called from.
  **Clarification**: It shows where each function would have *returned to*; with last-call optimization the call site of a tail call is not retained.

- **Confusion**: Thinking every trace entry is equally informative.
  **Clarification**: Normally the top two entries are enough to locate the error.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", section "Stack Traces".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Stack Traces*.
- Confidence rationale: HIGH — the source explicitly defines the trace structure, the retrieval BIF, and the last-call caveat.
- Uncertainties: The source uses the OTP-pre-21 `erlang:get_stacktrace/0`; later OTP versions bind the trace in the catch pattern instead. The card reflects the book's text.
- Cross-reference status: Slugs `exception`, `try-catch`, `catch-expression` extracted in this chapter.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
