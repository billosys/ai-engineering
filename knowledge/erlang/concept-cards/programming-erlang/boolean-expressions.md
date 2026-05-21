---
# === CORE IDENTIFICATION ===
concept: Boolean Expressions
slug: boolean-expressions

# === CLASSIFICATION ===
category: core-idioms
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Boolean Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "and"
  - "or"
  - "not"
  - "xor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
extends: []
related:
  - short-circuit-boolean
contrasts_with:
  - short-circuit-boolean

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What boolean expressions does Erlang provide?"
  - "Do Erlang's and/or operators evaluate both arguments?"
---

# Quick Definition

Erlang's four boolean expressions are `not B`, `B1 and B2`, `B1 or B2`, and `B1 xor B2`; their arguments must be boolean literals or expressions that evaluate to booleans.

# Core Definition

"There are four possible boolean expressions" ("The Rest of Sequential Erlang", *Boolean Expressions*): `not B1` (logical not), `B1 and B2` (logical and), `B1 or B2` (logical or), and `B1 xor B2` (logical xor). "In all of these, `B1` and `B2` must be boolean literals or expressions that evaluate to booleans." A crucial property, stated where short-circuit expressions are discussed: in `A or B` and `A and B`, "both the arguments are always evaluated, even if the truth value of the expression can be determined by evaluating only the first expression."

# Prerequisites

- **Boolean** — Boolean expressions operate on the boolean atoms `true` and `false`.

# Key Properties

1. There are exactly four boolean operators: `not`, `and`, `or`, `xor`.
2. `not` is unary; `and`, `or`, `xor` are binary.
3. Arguments must be booleans or expressions evaluating to booleans.
4. `and` and `or` always evaluate *both* arguments — they do not short-circuit.
5. They differ from the short-circuit operators `andalso` and `orelse`.

# Construction / Recognition

## To Construct/Create:
1. Combine boolean values: `true and false`, `not true`, `(2 > 1) or (3 > 4)`.

## To Identify/Recognize:
1. The keywords `and`, `or`, `not`, `xor` (without `also`/`else`) are the non-short-circuit operators.

# Context & Application

- **Typical contexts**: conditions and predicate logic where both operands are inexpensive and side-effect-free.
- **Common applications**: combining comparison results, e.g. `(2 > 1) or (3 > 4)` evaluates to `true`.
- **Historical/stylistic notes**: use `andalso`/`orelse` instead when the second operand is expensive or must not be evaluated.

# Examples

**Example 1** (*Boolean Expressions*): the operators in the shell:

```erlang
1> not true.
false
2> true and false.
false
3> true or false.
true
4> (2 > 1) or (3 > 4).
true
```

# Relationships

## Builds Upon
- **Boolean** — These operators consume and produce boolean values.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Short-circuit boolean** — `andalso`/`orelse` are the short-circuiting counterparts.

## Contrasts With
- **Short-circuit boolean** — `and`/`or` always evaluate both arguments; `andalso`/`orelse` evaluate the second only when needed.

# Common Errors

- **Error**: Using `and`/`or` expecting the second argument to be skipped.
  **Correction**: `and` and `or` always evaluate both arguments; use `andalso`/`orelse` for short-circuit behavior.

- **Error**: Passing non-boolean values to a boolean operator.
  **Correction**: Both operands must be boolean literals or expressions that evaluate to booleans.

# Common Confusions

- **Confusion**: Assuming `or` behaves like a short-circuit `||` from C-family languages.
  **Clarification**: Erlang's `or` evaluates both operands; the short-circuit operator is `orelse`.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", sections "Boolean Expressions" and "Short-Circuit Boolean Expressions".

# Verification Notes

- Definition source: Direct quotation from *Boolean Expressions* and the *Short-Circuit Boolean Expressions* note.
- Confidence rationale: HIGH — the source explicitly enumerates the four operators and states the both-arguments-evaluated rule.
- Uncertainties: None.
- Cross-reference status: Slug `boolean` extracted in this chapter; `short-circuit-boolean` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
