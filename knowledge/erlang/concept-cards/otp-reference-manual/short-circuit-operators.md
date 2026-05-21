---
# === CORE IDENTIFICATION ===
concept: Short-Circuit Operators
slug: short-circuit-operators

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Short-Circuit Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "andalso"
  - "orelse"
  - "short-circuit boolean operators"
  - "short-circuit expressions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-operators
extends:
  - boolean-operators
related:
  - guard-expressions
  - operator-precedence
contrasts_with:
  - boolean-operators

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do short-circuit operators (andalso/orelse) differ from strict boolean operators (and/or)?"
  - "What is short-circuit evaluation in Erlang?"
---

# Quick Definition

The `andalso` and `orelse` operators are short-circuit Boolean operators that only evaluate the second operand when necessary. Unlike `and`/`or`, the second operand need not be a Boolean value and these operators are tail-recursive.

# Core Definition

`Expr1 orelse Expr2` evaluates `Expr2` only if `Expr1` evaluates to `false`. `Expr1 andalso Expr2` evaluates `Expr2` only if `Expr1` evaluates to `true`. The expression returns either the value of `Expr1` (that is, `true` or `false`) or the value of `Expr2` (if evaluated). `Expr2` is not required to evaluate to a Boolean value, which makes `andalso` and `orelse` tail-recursive (Erlang Reference Manual, "Short-Circuit Expressions" section).

# Prerequisites

- **boolean-operators** — Understanding strict boolean operators provides the basis for understanding what short-circuit operators add.

# Key Properties

1. `andalso` evaluates `Expr2` only if `Expr1` is `true`.
2. `orelse` evaluates `Expr2` only if `Expr1` is `false`.
3. `Expr2` is not required to evaluate to a Boolean value.
4. Because `Expr2` can be any value, `andalso` and `orelse` are tail-recursive.
5. `andalso` has higher precedence than `orelse`.
6. Both are left-associative.
7. Both are valid in guard expressions.
8. Before Erlang/OTP R13A, `Expr2` was required to be Boolean and these operators were not tail-recursive.

# Construction / Recognition

## To Construct:
1. Use `Expr1 andalso Expr2` for short-circuit AND.
2. Use `Expr1 orelse Expr2` for short-circuit OR.
3. `Expr1` must evaluate to a Boolean; `Expr2` can be any term.

## To Recognize:
1. Look for the keywords `andalso` or `orelse` between expressions.

# Context & Application

Short-circuit operators are the preferred choice for conditional Boolean logic in Erlang because they avoid unnecessary evaluation and potential errors in the second operand. They are commonly used in guards and to protect expressions that would fail if evaluated with invalid input (e.g., checking a value is non-negative before taking its square root). Their tail-recursiveness enables use in recursive function definitions.

# Examples

**Example 1** (Short-Circuit Expressions section): Protecting against invalid arguments:

```erlang
case A >= -1.0 andalso math:sqrt(A+1) > B of
```

This works even if `A` is less than `-1.0`, since `math:sqrt/1` is never evaluated.

**Example 2** (Short-Circuit Expressions section): Compound condition:

```erlang
OnlyOne = is_atom(L) orelse
         (is_list(L) andalso length(L) == 1),
```

**Example 3** (Short-Circuit Expressions section): Tail-recursive function using `andalso`:

```erlang
all(Pred, [Hd|Tail]) ->
    Pred(Hd) andalso all(Pred, Tail);
all(_, []) ->
    true.
```

# Relationships

## Builds Upon
- **boolean-operators** — Short-circuit operators extend the concept of logical AND/OR with lazy evaluation.

## Enables
- **guard-expressions** — Short-circuit operators are valid in guards.

## Related
- **operator-precedence** — `andalso` binds tighter than `orelse`; both bind looser than comparison operators.

## Contrasts With
- **boolean-operators** — `and`/`or` evaluate both operands and require both to be Boolean; `andalso`/`orelse` short-circuit and allow non-Boolean second operands.

# Common Errors

- **Error**: Assuming `Expr1` can be a non-Boolean value.
  **Correction**: Only `Expr2` can be non-Boolean; `Expr1` must evaluate to `true` or `false`.

# Common Confusions

- **Confusion**: Thinking `andalso`/`orelse` always return Boolean values.
  **Clarification**: They return the value of `Expr2` if it is evaluated, which may not be Boolean. For example, `true andalso 42` returns `42`.

- **Confusion**: Believing `andalso`/`orelse` behave identically to `and`/`or`.
  **Clarification**: `and`/`or` are strict (both operands always evaluated, both must be Boolean). `andalso`/`orelse` are lazy (second operand evaluated only when needed, and it can be any term).

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Short-Circuit Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax, semantics, and tail-recursion properties described
- Uncertainties: None
- Cross-reference status: Contrast with boolean-operators verified
