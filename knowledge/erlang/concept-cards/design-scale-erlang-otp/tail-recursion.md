---
# === CORE IDENTIFICATION ===
concept: Tail Recursion
slug: tail-recursion

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: recursion
tier: intermediate

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
  - last-call optimization
  - tail-recursive function
  - last-call optimisation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - recursion
extends:
  - recursion
related:
  - processes-and-message-passing
  - process-skeleton
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What makes a function tail recursive?"
  - "Why does tail recursion run in constant memory?"
  - "How do Erlang processes loop without overflowing the stack?"
---

# Quick Definition

A function is tail recursive when its recursive call is the last expression executed in the clause. Such calls behave as a jump, so the function runs in constant stack space.

# Core Definition

"A function is said to be tail recursive if the only recursive calls to the function occur as the last expression to be executed in the function clause. We can think of this final call as a 'jump' back to the start of the function, now called with a different parameter. Tail-recursive functions allow last-call optimization, ensuring stack frames are not added in each iteration. This allows functions to execute in constant memory space and removes the risk of a stack overflow, which in Erlang manifests itself through the virtual machine running out of memory" (Cesarini & Vinoski, p. 22).

# Prerequisites

- **Recursion** — Tail recursion is a specific discipline of writing recursive functions; you must understand recursion first.

# Key Properties

1. The recursive call must be the *last* expression evaluated in the clause.
2. The runtime applies last-call optimization, reusing the current stack frame.
3. Execution proceeds in constant memory space regardless of iteration count.
4. It removes the risk of stack overflow (which appears as the VM running out of memory).
5. It is the standard way to give looping behavior to long-lived processes.

# Construction / Recognition

## To Construct:
1. Carry any accumulated result in a function argument (an accumulator), not in a pending operation.
2. Ensure the body's final expression is the self-call.

## To Recognize:
1. Inspect the last expression of each recursive clause.
2. If it is the self-call (nothing pending after it), the function is tail recursive; if the call is an operand of another operation (e.g., `N * factorial(N-1)`), it is body recursion.

# Context & Application

- **Typical contexts**: Process receive-loops; iterative computations over large data.
- **Common applications**: The `loop/0`/`loop/1` functions of servers, which must "execute in constant memory space" while alive.
- **Historical/stylistic notes**: A `case`-expression form can make tail recursion easier to see for those from imperative backgrounds, "but uglier" (p. 22).

# Examples

**Example 1** (p. 22): `print_all/1` is tail recursive — the final expression of the nonempty clause is `print_all(Xs)`:

```erlang
print_all([]) ->
    io:format("~n");
print_all([X|Xs]) ->
    io:format("~p\t",[X]),
    print_all(Xs).
```

**Example 2** (p. 22): The same logic written with a `case` expression to highlight the tail call:

```erlang
all_print(Ys) ->
    case Ys of
        [] ->
            io:format("~n");
        [X|Xs] ->
            io:format("~p\t",[X]),
            all_print(Xs)
    end.
```

**Counter-example** (p. 21): `factorial/1` is *not* tail recursive — `N * factorial(N-1)` leaves a multiplication pending.

# Relationships

## Builds Upon
- **Recursion** — Tail recursion is a disciplined form of recursion.

## Enables
- **Processes and message passing** — Server loops stay alive indefinitely thanks to constant-space tail recursion.
- **Process skeleton** — The standard `loop/1` pattern relies on it.

## Related
- *(none additional)*

## Contrasts With
- *(none — body recursion is described as a counter-example, not a separately carded concept)*

# Common Errors

- **Error**: Leaving an operation pending after the recursive call (e.g., `1 + loop(...)`), defeating last-call optimization.
  **Correction**: Use an accumulator argument so the self-call is truly last.

# Common Confusions

- **Confusion**: Believing any recursive function automatically runs in constant space.
  **Clarification**: Only tail-recursive calls get last-call optimization; body recursion grows the stack.

# Source Reference

Chapter 1: Introducing Erlang, Section "Recursion and Pattern Matching," page 22.

# Verification Notes

- Definition source: Direct quote from p. 22.
- Confidence rationale: HIGH — explicit definition and contrasting examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
