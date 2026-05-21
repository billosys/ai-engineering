---
# === CORE IDENTIFICATION ===
concept: Single-Assignment Variables
slug: single-assignment-variables

# === CLASSIFICATION ===
category: core-idioms
subcategory: variables
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
  - immutable variables
  - single assignment
  - variable binding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does single assignment mean in Erlang?"
  - "Why can't an Erlang variable be changed once bound?"
---

# Quick Definition

Erlang variables are single assignment: once a value is bound to a variable, that variable cannot be changed. Re-matching the variable checks equality against its current value rather than rebinding it.

# Core Definition

"Erlang variables are single assignment, so once you've bound a value to a variable, you can no longer change that variable" (Cesarini & Vinoski, p. 23). In a recursive function, "variables of the same name, including function arguments, are considered fresh in every function iteration" (p. 23) — immutability holds within a scope, but each recursive call introduces a new scope. Function arguments therefore play the role of mutable variables whose values change between calls, even though no single binding is ever overwritten.

# Prerequisites

- **Pattern matching** — A second use of a bound variable is a match (equality check), not an assignment; understanding this requires pattern matching.

# Key Properties

1. A variable can be bound exactly once within its scope.
2. Re-using a bound variable with `=` performs a pattern match against its existing value.
3. Matching a bound variable to an equal value succeeds; matching to a different value fails with a runtime error.
4. In recursion, same-named variables are fresh per iteration — a new scope, not a mutation.
5. Variable names start with an uppercase letter (e.g., `X`, `Xs`, `N`).

# Construction / Recognition

## To Construct:
1. Bind a variable with `=` or via a function-head pattern.
2. To represent "changing" state, pass a new value as an argument in a recursive call rather than reassigning.

## To Recognize:
1. An uppercase identifier appearing on the left of `=` for the first time is being bound.
2. The same identifier used again is being matched, not reassigned.

# Context & Application

- **Typical contexts**: All Erlang code; especially relevant in recursive loops carrying state.
- **Common applications**: Recursive functions thread changing state through fresh argument bindings each iteration.
- **Historical/stylistic notes**: Single assignment is a functional-programming principle; it eliminates a whole class of mutation bugs and makes processes' state explicit.

# Examples

**Example 1** (p. 24): A shell session demonstrating the behavior:

```erlang
1> A = 3.
3
2> A = 2+1.
3
3> A = 3+1.
** exception error: no match of right hand side value 4
```

Command 1 binds `A`; command 2 matches `A` against an equal value and succeeds; command 3 fails because `4` differs from `A`'s current value.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Recursion** — State that "changes" is modeled as fresh bindings each iteration.

## Related
- **Pattern matching** — Re-matching a bound variable is an equality constraint.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Reusing a variable name expecting it to be overwritten with a new value.
  **Correction**: Choose a fresh variable name (e.g., `NewState` rather than `State`).

# Common Confusions

- **Confusion**: Thinking single assignment makes loop state impossible.
  **Clarification**: State is threaded through function arguments; each recursive call gets fresh bindings, so the *value* changes while no binding is mutated.

# Source Reference

Chapter 1: Introducing Erlang, Section "Recursion and Pattern Matching," pages 23-24.

# Verification Notes

- Definition source: Direct quotes from p. 23.
- Confidence rationale: HIGH — explicitly defined with a shell example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
