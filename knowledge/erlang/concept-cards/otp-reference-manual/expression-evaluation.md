---
# === CORE IDENTIFICATION ===
concept: Expression Evaluation
slug: expression-evaluation

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Expression Evaluation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "evaluation order"
  - "subexpression evaluation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - terms
  - variables
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are expressions evaluated in Erlang?"
  - "In what order are subexpressions evaluated?"
  - "What happens when an operator receives a wrong argument type?"
---

# Quick Definition

In Erlang, all subexpressions are evaluated before the expression itself is evaluated, unless explicitly stated otherwise. Operators applied to arguments of incorrect type cause a `badarg` runtime error.

# Core Definition

The Erlang Reference Manual states: "All subexpressions are evaluated before an expression itself is evaluated, unless explicitly stated otherwise. For example, consider the expression `Expr1 + Expr2`. `Expr1` and `Expr2`, which are also expressions, are evaluated first -- in any order -- before the addition is performed." Additionally: "Many of the operators can only be applied to arguments of a certain type. For example, arithmetic operators can only be applied to numbers. An argument of the wrong type causes a `badarg` runtime error." (Erlang Reference Manual, "Expressions", "Expression Evaluation").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Subexpressions are evaluated before the containing expression
2. The order of subexpression evaluation is generally undefined (any order)
3. Type-incorrect arguments to operators cause `badarg` runtime errors
4. Some expressions explicitly specify evaluation order (e.g., short-circuit operators)
5. Macro and record expressions are expanded at compile time and are not true expressions

# Construction / Recognition

## To Identify/Recognize:
1. Any compound expression evaluates its parts before combining them
2. `badarg` errors indicate a type mismatch in operator arguments
3. The phrase "unless explicitly stated otherwise" signals exceptions to the default evaluation rule

# Context & Application

The unspecified evaluation order of subexpressions means Erlang code should not depend on side effects of one subexpression being visible to another subexpression at the same level. This is particularly relevant for expressions involving function calls with side effects.

# Examples

**Example 1** (Expression Evaluation section): Evaluation of `Expr1 + Expr2`: "`Expr1` and `Expr2`, which are also expressions, are evaluated first -- in any order -- before the addition is performed."

# Relationships

## Enables
- **terms** -- Terms are the simplest form of expression
- **variables** -- Variables are expressions whose evaluation returns their bound value
- **operator-precedence** -- Precedence determines the structure of compound expressions before evaluation

## Related
- **function-calls** -- Function call arguments are subexpressions evaluated before the call

# Common Errors

- **Error**: Depending on left-to-right evaluation order of subexpressions
  **Correction**: Subexpression evaluation order is not guaranteed; use explicit sequencing (comma-separated expressions) if order matters

# Common Confusions

- **Confusion**: Assuming macros and records are expressions
  **Clarification**: Macro and record expressions are expanded during compilation and "are in that sense not true Erlang expressions"

# Source Reference

"Expressions" chapter, section "Expression Evaluation."

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit statement in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
