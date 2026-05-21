---
concept: Append Operator Efficiency
slug: append-operator-efficiency
category: performance
subcategory: list-operations
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "Operator ++"
extraction_confidence: high
aliases:
  - "++ operator"
  - "list append"
  - "list concatenation"
prerequisites:
  - erlang-data-type-memory-sizes
extends: []
related:
  - length-function-cost
  - accidental-copying-in-closures
contrasts_with: []
answers_questions:
  - "How does the ++ operator relate to list copying?"
  - "Why does using ++ in a naive reverse produce quadratic complexity?"
  - "When is it safe to use ++ in a loop?"
---

# Quick Definition

The `++` operator copies its entire left-hand side operand; using it carelessly in a loop (with the growing result on the left) leads to quadratic time complexity. Placing the accumulator on the right avoids repeated copying.

# Core Definition

The `++` operator appends two lists by copying the left-hand side operand and attaching the right-hand side to the end of the copy. The right-hand side is never copied. This asymmetry is critical for performance: if a growing accumulator is placed on the left side inside a recursive loop, the accumulator is re-copied on every iteration, resulting in O(n^2) time complexity (Ericsson/OTP Team, "Common Caveats," section "Operator ++").

The compiler can optimize `[H] ++ Acc` into the equivalent `[H|Acc]`, so using `++` with a single-element list on the left is effectively free.

# Prerequisites

- **erlang-data-type-memory-sizes** -- Understanding list memory layout (1 word per element + element size) is needed to grasp why copying the left operand is expensive.

# Key Properties

1. `++` copies all cons cells of the left-hand side operand
2. The right-hand side operand is shared, not copied
3. Placing a growing result on the left side produces O(n^2) behavior
4. Placing a growing result on the right side produces O(n) behavior
5. The compiler rewrites `[H] ++ Acc` to `[H|Acc]`, eliminating the intermediate list construction

# Construction / Recognition

## Recognizing the Anti-Pattern

1. Look for `++` inside a recursive function
2. Check whether the left operand grows across iterations (typically a recursive call result)
3. If the left operand grows, the code has quadratic complexity

## Fixing the Anti-Pattern

1. Restructure so the accumulator is always the right operand of `++`
2. Or replace `[X] ++ Acc` with `[X|Acc]` (cons operator) for single-element prepends
3. Use `lists:reverse/1` at the end if element order needs to be restored

# Context & Application

This caveat applies whenever lists are built incrementally in a loop. The classic example is naive list reversal, but it also appears in any accumulator-based list construction where `++` is used incorrectly.

**Typical contexts:**
- Implementing list reversal
- Building result lists in recursive functions
- Flattening nested structures

The issue is fundamental to how Erlang's singly-linked lists work: appending to the end requires traversing (and copying) the entire prefix.

# Examples

**DO NOT** -- Naive reverse with quadratic complexity (source: "Common Caveats," section "Operator ++"):

```erlang
naive_reverse([H|T]) ->
    naive_reverse(T) ++ [H];
naive_reverse([]) ->
    [].
```

The growing result of `naive_reverse(T)` is on the left side and is copied on every recursive call.

**OK** -- Accumulator on the right side (source: same section):

```erlang
naive_but_ok_reverse([H|T], Acc) ->
    naive_but_ok_reverse(T, [H] ++ Acc);
naive_but_ok_reverse([], Acc) ->
    Acc.
```

Each list element is copied only once. The compiler rewrites `[H] ++ Acc` to `[H|Acc]`.

**DO** -- Idiomatic cons-based accumulation (source: same section):

```erlang
vanilla_reverse([H|T], Acc) ->
    vanilla_reverse(T, [H|Acc]);
vanilla_reverse([], Acc) ->
    Acc.
```

# Relationships

## Related

- **length-function-cost** -- Another O(n) list operation that can be surprisingly expensive
- **accidental-copying-in-closures** -- Another form of unintended data copying

# Common Errors

- **Error**: Placing the recursive call result (growing list) on the left side of `++`
  **Correction**: Restructure so the accumulator is the right operand, or use cons `[H|Acc]`

- **Error**: Assuming `++` is always O(n) in the total list size
  **Correction**: `++` is O(length of left operand) per call; in a loop this compounds

# Common Confusions

- **Confusion**: Believing `++` copies both operands
  **Clarification**: Only the left-hand side is copied; the right-hand side is shared

- **Confusion**: Thinking `[H] ++ Acc` is less efficient than `[H|Acc]`
  **Clarification**: The compiler optimizes `[H] ++ Acc` into `[H|Acc]`, so they are equivalent in practice

# Source Reference

"Common Caveats," section "Operator ++." The source provides an explicit Erlang implementation of `++` showing the copy behavior, plus three examples (DO NOT, OK, DO) demonstrating correct and incorrect usage.

# Verification Notes

- Definition: Directly from source -- "The ++ operator copies its left-hand side operand"
- Key Properties: All items derived from explicit source statements
- Examples: All three examples taken verbatim from source
- Compiler optimization note (`[H] ++ Acc` -> `[H|Acc]`) explicitly stated in source
- Confidence: HIGH -- explicit documentation with code examples from official OTP guide
