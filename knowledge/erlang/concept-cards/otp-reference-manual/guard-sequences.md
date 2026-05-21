---
# === CORE IDENTIFICATION ===
concept: Guard Sequence
slug: guard-sequences

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: guards
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Guard Sequences"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "guard sequence"
  - "guard"
  - "when clause"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - guard-expressions
extends: []
related:
  - function-clause
  - case-expression
  - if-expression
  - receive-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a guard sequence in Erlang?"
  - "What is the difference between a guard and a guard sequence?"
  - "How do semicolons and commas work in guards?"
  - "When is a guard sequence considered true?"
---

# Quick Definition

A guard sequence is a sequence of guards separated by semicolons (`;`), where each guard is a sequence of guard expressions separated by commas (`,`). The guard sequence is true if at least one of its guards is true; a guard is true if all of its guard expressions evaluate to `true`.

# Core Definition

A guard sequence has the form `Guard1; ...; GuardK` where each guard has the form `GuardExpr1, ..., GuardExprN`. The guard sequence is true if at least one of the guards is true (the remaining guards, if any, are not evaluated). A guard is true if all guard expressions evaluate to `true`. In other words, semicolons act as logical OR between guards, and commas act as logical AND between guard expressions within a single guard (Erlang Reference Manual, "Guard Sequences" section).

# Prerequisites

- **guard-expressions** — Guard sequences are composed of guard expressions.

# Key Properties

1. A guard sequence is a series of guards separated by `;` (logical OR).
2. A guard is a series of guard expressions separated by `,` (logical AND).
3. The guard sequence is true if at least one guard is true.
4. A guard is true if all its guard expressions are true.
5. Evaluation stops at the first true guard (short-circuit on `;`).
6. If a guard expression fails (exception or non-boolean), the entire guard fails, and the next guard in the sequence is tried.
7. Guard sequences appear after the `when` keyword in function heads, `case` clauses, `receive` clauses, `if` branches, and `try` clauses.

# Construction / Recognition

## To Construct:
```erlang
f(X) when is_integer(X), X > 0 ->    %% single guard: X is integer AND X > 0
    positive;
f(X) when is_integer(X); is_float(X) -> %% guard sequence: X is integer OR float
    number.
```

## To Recognize:
1. Look for `when` followed by expressions before `->`.
2. Commas separate conjuncts (AND); semicolons separate disjuncts (OR).

# Context & Application

Guard sequences are used in function clause heads, `case`, `receive`, `if`, and `try` expressions to add conditions beyond pattern matching. They provide a way to test properties of values that cannot be expressed by pattern matching alone, such as numeric ranges, type tests, and arithmetic conditions. The key constraint is that only valid guard expressions (side-effect-free) can appear in guards.

# Examples

**Example 1**: Guard with comma (AND):

```erlang
f(X) when is_integer(X), X > 0, X < 100 ->
    in_range.
```

All three conditions must be true: X must be an integer, greater than 0, and less than 100.

**Example 2**: Guard sequence with semicolon (OR):

```erlang
g(X) when X =:= hello; X =:= goodbye ->
    greeting.
```

The guard succeeds if X is `hello` OR `goodbye`.

**Example 3**: Combined AND and OR:

```erlang
h(X) when is_integer(X), X > 0; is_atom(X) ->
    ok.
```

Succeeds if (X is an integer AND X > 0) OR (X is an atom).

# Relationships

## Builds Upon
- **guard-expressions** — Guard sequences are composed of valid guard expressions.

## Enables
- **function-clause** — Guards refine function clause selection.
- **case-expression** — Guards add conditions to case clauses.
- **if-expression** — If branches are entirely guard sequences.
- **receive-expression** — Guards add conditions to receive clauses.

## Related
- All clause-based expressions use guard sequences.

# Common Errors

- **Error**: Using `,` when `;` is needed, or vice versa, changing AND/OR semantics.
  **Correction**: Use `,` for AND (all must be true) and `;` for OR (any can be true).

- **Error**: Using a non-guard expression in a guard (e.g., a user-defined function call).
  **Correction**: Only guard BIFs and valid guard expressions can appear in guards. Use a `case` expression body for arbitrary tests.

# Common Confusions

- **Confusion**: Thinking a failing guard expression causes a runtime error.
  **Clarification**: If a guard expression fails (raises an exception), the entire guard fails silently and the next guard in the sequence is tried. No runtime error propagates from guard evaluation.

- **Confusion**: Confusing guard `,` with the `andalso` operator and guard `;` with `orelse`.
  **Clarification**: While similar in meaning, `,` and `;` in guards have special behavior: a failing sub-expression causes the guard to fail (rather than propagating an exception), whereas `andalso`/`orelse` can also be used in guards but with standard short-circuit semantics.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Guard Sequences" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear definitions of guard and guard sequence from source
- Uncertainties: None
- Cross-reference status: Verified usage in function-clause, case, if, receive, and try contexts
