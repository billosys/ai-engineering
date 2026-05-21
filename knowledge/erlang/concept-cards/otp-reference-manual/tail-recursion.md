---
# === CORE IDENTIFICATION ===
concept: Tail Recursion
slug: tail-recursion

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-declarations
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Tail recursion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "tail-recursive call"
  - "tail call optimization"
  - "last call optimization"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
  - function-evaluation
extends: []
related:
  - function-clause
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is tail recursion in Erlang?"
  - "How do I write a tail-recursive function?"
  - "Why does tail recursion matter for Erlang processes?"
---

# Quick Definition

If the last expression of a function body is a function call, Erlang performs a tail-recursive call that consumes no additional call stack, allowing infinite loops without stack overflow.

# Core Definition

The Erlang Reference Manual states: "If the last expression of a function body is a function call, a _tail-recursive call_ is done. This is to ensure that no system resources, for example, call stack, are consumed. This means that an infinite loop using tail-recursive calls will not exhaust the call stack and can (in principle) run forever." (Erlang Reference Manual, "Functions", "Tail recursion").

# Prerequisites

- **function-declaration** -- Must understand function structure to position calls correctly
- **function-evaluation** -- Must understand how function bodies are evaluated to know what "last expression" means

# Key Properties

1. A tail-recursive call occurs when a function call is the last expression in a clause body
2. No additional call stack is consumed by a tail-recursive call
3. Infinite loops using tail-recursive calls will not exhaust the stack
4. A call is NOT tail-recursive if operations remain after the recursive call returns
5. The optimization is guaranteed by the runtime, not optional

# Construction / Recognition

## To Construct/Create:
1. Ensure the recursive (or other) function call is the very last expression in the clause body
2. Do not perform any operation on the return value of the recursive call
3. Use accumulator parameters to move computations before the recursive call

## To Identify/Recognize:
1. The last expression in the body is a function call (no wrapping operation)
2. Counter-example: `N * fact(N-1)` is NOT tail-recursive because multiplication happens after the call

# Context & Application

Tail recursion is essential in Erlang because processes are lightweight and have limited stack space. Server loops (`gen_server`, `gen_statem`) rely on tail recursion to run indefinitely. Any long-running or infinite loop must be tail-recursive to avoid stack overflow.

# Examples

**Example 1** (Tail recursion section): A tail-recursive infinite loop:
```erlang
loop(N) ->
    io:format("~w~n", [N]),
    loop(N+1).
```

**Example 2** (Tail recursion section): The factorial function as a counter-example: "It is not tail-recursive, since a multiplication is done on the result of the recursive call to `fact(N-1)`."
```erlang
fact(N) when N > 0 ->
    N * fact(N-1);   %% NOT tail-recursive: multiplication wraps the call
fact(0) ->
    1.
```

# Relationships

## Builds Upon
- **function-declaration** -- Tail recursion depends on clause body structure
- **function-evaluation** -- The last expression rule comes from evaluation order

## Enables
- Process server loops that run indefinitely without stack overflow

## Contrasts With
- Non-tail-recursive functions that consume stack per call

# Common Errors

- **Error**: Performing an operation on the result of a recursive call (e.g., `N * f(N-1)`)
  **Correction**: Use an accumulator parameter to move the computation before the recursive call

# Common Confusions

- **Confusion**: Thinking any recursive call in a function body is tail-recursive
  **Clarification**: Only the _last expression_ in the body qualifies; if the recursive call is wrapped in another operation or is not the final expression, it is not tail-recursive

# Source Reference

"Functions" chapter, section "Tail recursion", with the `loop/1` example and factorial counter-example.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: HIGH -- explicit definition with positive and negative examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
