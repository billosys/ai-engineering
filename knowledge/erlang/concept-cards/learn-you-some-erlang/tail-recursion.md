---
concept: Tail Recursion
slug: tail-recursion
category: functions-pattern-matching
subcategory: recursion
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Hello Recursion!"
chapter_number: 5
pdf_page: null
section: "Length of a Tail Recursion"
extraction_confidence: high
aliases:
  - "tail call optimization"
  - "TCO"
  - "last call optimization"
  - "LCO"
prerequisites:
  - recursion
  - accumulator
extends:
  - recursion
related:
  - thinking-recursively
contrasts_with:
  - recursion
answers_questions:
  - "What is tail recursion?"
  - "How does tail recursion relate to accumulators?"
---

# Tail Recursion

## Quick Definition

Tail recursion is a form of recursion where the recursive call is the last expression evaluated, so the VM reuses the stack frame and memory stays constant.

## Core Definition

Tail recursion transforms a linear recursive process (which grows with the number of elements) into an iterative one with essentially no growth. To make a function call tail recursive, the recursive call must be "alone" — the last expression evaluated — which requires holding an extra temporary variable (an accumulator) as a parameter. When the VM sees a function calling itself in a tail position, it eliminates the current stack frame; this is *tail call optimization (TCO)*, a special case of the more general *last call optimization (LCO)*, which applies whenever the last expression in a function body is any function call. As a result, tail-recursive functions use constant space (Hébert, ch. 5, "Length of a Tail Recursion" and the "Last Call Optimization" sidebar).

## Prerequisites

- **Recursion** — Tail recursion is a refinement of recursion
- **Accumulator** — Tail recursion uses an accumulator to carry results

## Key Properties

1. The recursive call must be the last expression evaluated (the tail position).
2. The VM eliminates the current stack frame, so memory is constant.
3. TCO is a special case of last call optimization (LCO).
4. LCO applies to any tail-position function call, not just self-calls.
5. Requires an extra accumulator parameter to carry intermediate results.
6. Calculating `factorial(4)` uses the same space as `factorial(1000000)`.

## Construction / Recognition

To make a function tail recursive:

1. Add an accumulator parameter (often via a helper of higher arity).
2. Move the work (e.g., `+1`, list construction) into the accumulator argument.
3. Make the recursive call the final expression in the body.

## Context & Application

Tail recursion matters most for functions meant to loop infinitely (main loops) and for functions that would otherwise build very large stacks (e.g., a non-iterative Fibonacci). In practice, performance differences with plain recursion are often small; profile before optimizing.

## Examples

**Example** (ch. 5): `tail_fac(0,Acc) -> Acc; tail_fac(N,Acc) when N > 0 -> tail_fac(N-1,N*Acc).`

**Example** (ch. 5): `tail_len([], Acc) -> Acc; tail_len([_|T], Acc) -> tail_len(T,Acc+1).`

## Relationships

### Prerequisites

- **Recursion** — The base concept
- **Accumulator** — Carries the running result

### Builds Upon

- **Recursion** — Tail recursion is a space-efficient recursion

### Related

- **Thinking recursively** — Designing tail-recursive functions follows the recursive mindset

### Contrasts With

- **Recursion** — Plain recursion stacks pending operations; tail recursion eliminates the stack frame

## Common Errors

- **Error**: Leaving an operation (like `1 +`) outside the recursive call
  **Correction**: Move it into the accumulator so the recursive call is alone in tail position

## Common Confusions

- **Confusion**: Thinking tail recursion is always faster
  **Clarification**: On short lists plain recursion can be faster; tail recursion's gain is constant memory, especially for long-running loops

## Source Reference

Chapter 5: "Hello Recursion!", section "Length of a Tail Recursion" and the "Last Call Optimization" sidebar.

## Verification Notes

- Definition: Adapted from the tail-recursion section and LCO sidebar
- Confidence: HIGH — explicit treatment with worked expansions
- Uncertainties: None
