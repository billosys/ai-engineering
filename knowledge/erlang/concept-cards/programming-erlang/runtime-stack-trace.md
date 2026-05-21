---
# === CORE IDENTIFICATION ===
concept: Runtime Stack Trace
slug: runtime-stack-trace

# === CLASSIFICATION ===
category: error-handling
subcategory: diagnostics
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Runtime Diagnostics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "stack trace"
  - "runtime error message"
  - "runtime diagnostics"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - compiler-diagnostics
  - io-format-debugging
contrasts_with:
  - compiler-diagnostics

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang stack trace?"
  - "How do I read a runtime error message?"
  - "Why is a function missing from the stack trace?"
---

# Quick Definition

A runtime stack trace is the list of function names, modules, and line numbers printed when a process linked to the shell crashes. It shows where the error occurred and the chain of functions that call would have returned to.

# Core Definition

If an Erlang process crashes you may get an error message, but only if some other process monitors it — "if we just create a process with `spawn` and the process dies, we won't get any error message"; using `spawn_link` ensures errors are shown ("Runtime Diagnostics"). "Every time a process crashes that is linked to the shell, a stack trace will be printed." The trace starts with the name of the function where the error occurred, followed by the functions (with module names and line numbers) that the current function would return to on completion. Only the top entries are interesting. A function called as a tail call (last-call optimization) is *not* in the trace: the last-call optimization replaces such a call with a jump, so the calling function is replaced in the call stack by the called function and becomes invisible.

# Prerequisites

- **Process** — Stack traces are printed when a process crashes; visibility depends on linking (e.g. to the shell or via `spawn_link`).

# Key Properties

1. Printed when a process linked to the shell crashes.
2. Begins with the function where the error occurred.
3. Each entry has module name and line number; entries are return points.
4. Only the top entries are generally interesting.
5. A tail-called function is absent from the trace due to the last-call optimization.
6. The error message line (e.g. `** exception error: no match of right hand side value {error,badarg}`) precedes the trace.
7. A bare `spawn`ed process that dies prints nothing; `spawn_link` makes errors visible.

# Construction / Recognition

## To Read a Stack Trace:
1. Read the error message above the trace to learn the failure kind.
2. Look at the top entry — that is where the error occurred.
3. Follow lower entries as the return chain leading to the failure.
4. Remember a tail-called function will be missing — check the caller.

## To Recognize:
1. Output beginning `** exception error: ...` followed by `in function .../N (file.erl, line N)` lines.

# Context & Application

Stack traces are the primary built-in diagnostic for runtime crashes.

- **Typical contexts**: A process crashes during development or operation.
- **Common applications**: Locating the failing function and the call chain.
- **Historical/stylistic notes**: The absence of tail-called functions is a consequence of the same last-call optimization that makes infinite-loop receive loops possible.

# Examples

**Example 1** ("The Stack Trace"): A deliberate error in `lib_misc:deliberate_error/1`.

```erlang
1> lib_misc:deliberate_error("file.erl").
** exception error: no match of right hand side value {error,badarg}
  in function lib_misc:bad_function/2 (lib_misc.erl, line 804)
  in call from lib_misc:deliberate_error/1 (lib_misc.erl, line 800)
```

The badmatch comes from `{ok, Bin} = file:open({abc,123}, A)` — `file:open/2` returned `{error, badarg}`.

**Example 2** ("The Stack Trace"): With `deliberate_error1/1`, which tail-calls `bad_function/2`, `deliberate_error1` is missing from the trace because the tail call leaves no return frame.

# Relationships

## Builds Upon
- **Process** — A trace is produced by a crashing process.

## Enables
- (No card depends on this concept.)

## Related
- **Compiler diagnostics** — Both report errors with line numbers.
- **io:format debugging** — A complementary technique for understanding failures.

## Contrasts With
- **Compiler diagnostics** — Compiler diagnostics report errors at compile time; a stack trace reports a failure at run time.

# Common Errors

- **Error**: Expecting an error message from a process started with bare `spawn`.
  **Correction**: A `spawn`ed process that dies prints nothing; use `spawn_link` (or a monitor) to see the error.

- **Error**: Assuming the calling function is always in the trace.
  **Correction**: A tail-called function leaves no return frame, so its caller may be absent — check the caller of the caller.

# Common Confusions

- **Confusion**: Thinking the error message line number is always the true source of the bug.
  **Clarification**: The trace shows where the error occurred and return points; the underlying mistake (e.g. a bad argument) may be elsewhere on that line.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "Runtime Diagnostics" (subsection "The Stack Trace").

# Verification Notes

- Definition source: Direct quotes from "Runtime Diagnostics" and "The Stack Trace".
- Confidence rationale: HIGH — stack-trace structure, the spawn/spawn_link distinction, and the tail-call effect are explicitly explained with worked examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards; `process` is a canonical shared slug.
- Re-extraction notes: Fresh extraction — no pre-existing card.
