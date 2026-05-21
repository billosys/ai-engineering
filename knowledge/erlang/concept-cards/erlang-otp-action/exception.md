---
# === CORE IDENTIFICATION ===
concept: Exception
slug: exception

# === CLASSIFICATION ===
category: error-handling
subcategory: exceptions
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.8 Exceptions, try, and catch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - error exception
  - exit exception
  - throw exception

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-function
extends: []
related:
  - process-termination
  - let-it-crash
  - exit-signal
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an exception in Erlang?"
  - "What are the three classes of exceptions?"
  - "What is the difference between error, exit, and throw?"
---

# Quick Definition

An exception is an alternative way of returning from a function: it keeps propagating up to the caller, and the caller's caller, until it is caught or the process dies. Erlang has three classes: error, exit, and throw.

# Core Definition

"What, then, is an exception? You could say that it's an alternative way of returning from a function, with the difference that it keeps going back to the caller, and to the caller's caller, and so on, until either someone catches it or it reaches the initial call of the process (in which case the process dies)" (Chapter 2, section 2.8). There are three classes of exceptions: **`error`** — runtime errors such as division by zero, failing matches, or no matching function clause; if these kill a process they are reported to the Erlang error logger. **`exit`** — used to signal "this process is giving up"; generally not caught, expected to terminate the process and let others know why; `exit(normal)` signals normal completion and is not reported. **`throw`** — for user-defined purposes, such as signaling something unexpected or performing a nonlocal return; an uncaught `throw` becomes an `error` exception with reason `nocatch`. Each class has a corresponding BIF to raise it: `erlang:error(Reason)`, `exit(Reason)`, and `throw(SomeTerm)` (`exit` and `throw` are auto-imported).

# Prerequisites

- **Erlang function** — exceptions are an alternative way of returning from a function.

# Key Properties

1. An exception is an alternative return that propagates up the call chain.
2. It keeps propagating until caught or until it reaches the process's initial call (killing the process).
3. There are three classes: `error`, `exit`, and `throw`.
4. `error` exceptions come from runtime errors and are logged when they kill a process.
5. `exit` signals a process giving up; `exit(normal)` is normal termination and is not logged.
6. `throw` is for user-defined purposes; an uncaught `throw` becomes an `error` with reason `nocatch`.
7. Raised via `erlang:error/1`, `exit/1`, and `throw/1`.

# Construction / Recognition

## To Identify/Recognize:
1. A runtime fault (bad match, no clause, divide by zero) raises an `error` exception.
2. `exit(Reason)` raises an `exit`; `throw(Term)` raises a `throw`.
3. Uncaught, the exception propagates until the process dies.

# Context & Application

- **Typical contexts**: Error signaling and the "let it crash" philosophy.
- **Common applications**: `error` for library argument errors (`badarg`); `exit` for deliberate process termination; `throw` for nonlocal returns out of deep recursion.
- **Historical/stylistic notes**: In normal code you rarely raise `error` exceptions yourself, though it is good practice when writing a library.

# Examples

**Example 1** (section 2.8): A failing match such as `17 = 42` raises an `error` exception with reason code `badmatch`; calling a function with arguments matching no clause raises a `function_clause` error.

**Example 2** (section 2.8.1): If a process calls `exit(normal)` and it is not caught, the process terminates as if it had finished its job — other linked processes do not regard it as abnormal termination.

# Relationships

## Builds Upon
- **Erlang function** — an exception is an alternative function return.

## Enables
- **Let it crash** — uncaught exceptions cleanly terminate a process.

## Related
- **Process termination** — an uncaught exception kills the process.
- **Exit signal** — an `exit` exception relates to the signals linked processes receive.
- **Pattern matching** — failed matches raise `error` exceptions.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Catching `exit` exceptions routinely.
  **Correction**: `exit` is generally expected not to be caught — it should terminate the process and inform others why.

# Common Confusions

- **Confusion**: Believing an uncaught `throw` simply vanishes.
  **Clarification**: An uncaught `throw` mutates into an `error` exception with reason `nocatch`, terminating and logging the process.

# Source Reference

Chapter 2: Erlang language essentials, section 2.8 "Exceptions, try, and catch," including 2.8.1 "Throwing (raising) exceptions."

# Verification Notes

- Definition source: Direct adaptation from section 2.8.
- Confidence rationale: HIGH — the three exception classes are explicitly defined.
- Uncertainties: Full `try ... catch` handling syntax is treated in section 2.8.2; this card covers the exception concept itself. Detailed error-handling treatment may also appear in a later chapter owned by another agent.
- Cross-reference status: Verified against planned/existing card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
