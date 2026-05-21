---
# === CORE IDENTIFICATION ===
concept: Boolean Operators
slug: boolean-operators

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
section: "Boolean Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "logical operators"
  - "strict boolean operators"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - guard-expressions
  - operator-precedence
contrasts_with:
  - short-circuit-operators

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do short-circuit operators (andalso/orelse) differ from strict boolean operators (and/or)?"
  - "What boolean operators does Erlang provide?"
---

# Quick Definition

Boolean operators (`not`, `and`, `or`, `xor`) perform strict logical operations on Boolean values (`true` and `false`). Unlike `andalso`/`orelse`, all operands are always evaluated.

# Core Definition

Boolean expressions use the operators `not` (unary logical NOT), `and` (logical AND), `or` (logical OR), and `xor` (logical XOR). Both arguments must evaluate to `true` or `false`; otherwise a `badarg` runtime error occurs. Both operands of binary boolean operators are always evaluated regardless of the first operand's value (Erlang Reference Manual, "Boolean Expressions" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Four operators: `not` (unary), `and`, `or`, `xor` (binary).
2. Both operands are always evaluated (strict evaluation, no short-circuiting).
3. Both arguments must be Boolean values (`true` or `false`); non-Boolean arguments cause a `badarg` error.
4. `and` has higher precedence than `or` (same level as `*`, `div`, `rem`, `band`).
5. `or` and `xor` have lower precedence than `and` (same level as `+`, `-`, `bor`, `bxor`).
6. All boolean operators are valid in guard expressions.

# Construction / Recognition

## To Construct:
1. Unary: `not Expr` where `Expr` evaluates to a Boolean.
2. Binary: `Expr1 and Expr2`, `Expr1 or Expr2`, `Expr1 xor Expr2`.

## To Recognize:
1. Look for the keywords `not`, `and`, `or`, `xor` used as operators.
2. Note that these are strict (not short-circuit) operators.

# Context & Application

Boolean operators are used when both operands must be evaluated (e.g., when both expressions have side effects that must occur). They are valid in guards. For most conditional logic, the short-circuit operators `andalso` and `orelse` are preferred because they avoid evaluating the second operand unnecessarily and do not raise errors on non-Boolean second operands.

# Examples

**Example 1** (Boolean Expressions section):

```erlang
1> not true.
false
2> true and false.
false
3> true xor false.
true
```

**Example 2** (Boolean Expressions section): Error on non-Boolean argument:

```erlang
4> true or garbage.
** exception error: bad argument
     in operator  or/2
        called as true or garbage
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **guard-expressions** — Boolean operators are valid in guards.

## Related
- **operator-precedence** — `and` binds tighter than `or`/`xor`.

## Contrasts With
- **short-circuit-operators** — `andalso`/`orelse` short-circuit evaluation and allow non-Boolean second operands; `and`/`or` evaluate both operands strictly.

# Common Errors

- **Error**: Passing non-Boolean arguments to `and`/`or` (e.g., `true or garbage`).
  **Correction**: Ensure both operands evaluate to `true` or `false`, or use `andalso`/`orelse` if the second operand might not be Boolean.

- **Error**: Relying on `or` to short-circuit and skip evaluation of the second operand.
  **Correction**: Use `orelse` for short-circuit behavior.

# Common Confusions

- **Confusion**: Thinking `and`/`or` and `andalso`/`orelse` are interchangeable.
  **Clarification**: `and`/`or` always evaluate both operands and require both to be Boolean. `andalso`/`orelse` short-circuit and allow non-Boolean second operands.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Boolean Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit operator table and examples in source
- Uncertainties: None
- Cross-reference status: Contrast with short-circuit-operators verified against planned extraction
