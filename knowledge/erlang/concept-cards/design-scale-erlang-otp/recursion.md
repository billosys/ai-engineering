---
# === CORE IDENTIFICATION ===
concept: Recursion
slug: recursion

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: recursion
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Recursion and Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - recursive function
  - base case

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - single-assignment-variables
  - list-comprehensions
contrasts_with:
  - tail-recursion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang programmers get iterative behavior?"
  - "What is a base case in a recursive function?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

Recursion is the mechanism by which Erlang programs achieve iterative or repetitive behavior, since there are no loop constructs. A recursive function calls itself until it reaches a base case where recursion stops.

# Core Definition

"Recursion is the way Erlang programmers get iterative or repetitive behavior in their programs. It is also what keeps processes alive in between bursts of activity" (Cesarini & Vinoski, p. 21). A recursive function is typically written in multiple clauses: one or more recursive clauses that reduce the problem, and a base case clause "where recursing stops" (p. 21). Iteration continues until the call pattern-matches the base-case clause.

# Prerequisites

- **Pattern matching** — Recursive clauses are selected by matching the argument against each clause head; the base case is itself a pattern (e.g., `0` or `[]`).

# Key Properties

1. There are no `for`/`while` loops in Erlang — repetition is expressed as self-calls.
2. A recursive function needs at least one base-case clause to terminate.
3. Clauses are tried top to bottom; the first matching clause is used.
4. If no clause matches (e.g., `factorial(-3)`), the call fails with a `function_clause` error.
5. Recursion drives both value computation and process loops.

# Construction / Recognition

## To Construct:
1. Write a base-case clause for the smallest/terminating input, returning a direct value.
2. Write a recursive clause that handles the general input and calls the function with a reduced argument.
3. Add guards where the input domain must be restricted (e.g., `when N > 0`).

## To Recognize:
1. A function whose body contains a call to itself.
2. At least one clause that returns without calling itself (the base case).

# Context & Application

- **Typical contexts**: Computing values over numbers and lists, and keeping server processes alive via receive-loops.
- **Common applications**: Factorial, list traversal, server `loop/1` functions.
- **Historical/stylistic notes**: Recursion replaces imperative iteration; it is the "pattern behind all patterns" once a process loops awaiting messages.

# Examples

**Example 1** (p. 21): The factorial function, with `0` as the base case:

```erlang
-module(ex1).
-export([factorial/1]).
factorial(0) ->
    1;
factorial(N) when N > 0 ->
    N * factorial(N-1).
```

`factorial(0)` matches the base case returning `1`; any positive `N` returns `N * factorial(N-1)`.

**Example 2** (p. 22): Recursive list printing — recursion used for imperative-style side effects:

```erlang
print_all([]) ->
    io:format("~n");
print_all([X|Xs]) ->
    io:format("~p\t",[X]),
    print_all(Xs).
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **List comprehensions** — An alternative, often clearer way to express list recursion.
- **Process and message passing** — Server loops stay alive through recursive `loop/1` calls.

## Related
- **Single-assignment variables** — Each recursive call introduces fresh bindings.

## Contrasts With
- **Tail recursion** — A specific recursion form that runs in constant stack space.

# Common Errors

- **Error**: Omitting the base case, causing infinite recursion.
  **Correction**: Always provide a terminating clause.
- **Error**: Expecting graceful handling of out-of-domain input (e.g., negative numbers).
  **Correction**: Either guard the recursive clause or let the call fail — Erlang favors "let it fail."

# Common Confusions

- **Confusion**: Believing recursion always grows the stack and risks overflow.
  **Clarification**: Body recursion does grow the stack, but tail recursion runs in constant space via last-call optimization.

# Source Reference

Chapter 1: Introducing Erlang, Section "Recursion and Pattern Matching," pages 21-23.

# Verification Notes

- Definition source: Direct quote from p. 21.
- Confidence rationale: HIGH — explicit definition and worked factorial example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
