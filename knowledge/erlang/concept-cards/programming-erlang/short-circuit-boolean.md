---
# === CORE IDENTIFICATION ===
concept: Short-Circuit Boolean Expressions
slug: short-circuit-boolean

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
section: "Short-Circuit Boolean Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "andalso"
  - "orelse"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
extends: []
related:
  - boolean-expressions
contrasts_with:
  - boolean-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are short-circuit boolean expressions?"
  - "What is the difference between and and andalso?"
---

# Quick Definition

Short-circuit boolean expressions — `andalso` and `orelse` — evaluate their second argument only when its value is actually needed to determine the result.

# Core Definition

"Short-circuit boolean expressions are boolean expressions whose arguments are evaluated only when necessary" ("The Rest of Sequential Erlang", *Short-Circuit Boolean Expressions*). There are two: `Expr1 orelse Expr2` first evaluates `Expr1`; if it is `true`, `Expr2` is not evaluated; if it is `false`, `Expr2` is evaluated. `Expr1 andalso Expr2` first evaluates `Expr1`; if it is `true`, `Expr2` is evaluated; if it is `false`, `Expr2` is not evaluated. This contrasts with the ordinary boolean operators `and` and `or`, where "both the arguments are always evaluated, even if the truth value of the expression can be determined by evaluating only the first expression."

# Prerequisites

- **Boolean** — Short-circuit expressions operate on boolean values.

# Key Properties

1. There are two short-circuit operators: `andalso` and `orelse`.
2. `orelse` skips the second argument when the first is `true`.
3. `andalso` skips the second argument when the first is `false`.
4. The non-short-circuit `and`/`or` always evaluate both arguments.
5. Short-circuiting avoids evaluating expensive or potentially failing second operands.

# Construction / Recognition

## To Construct/Create:
1. Use `Expr1 andalso Expr2` when `Expr2` should run only if `Expr1` is `true`.
2. Use `Expr1 orelse Expr2` when `Expr2` should run only if `Expr1` is `false`.

## To Identify/Recognize:
1. The keywords `andalso` and `orelse` indicate short-circuit evaluation.

# Context & Application

- **Typical contexts**: guarding a potentially failing or costly second operand behind a first test.
- **Common applications**: conditions where the second operand depends on the first being a particular value.
- **Historical/stylistic notes**: equivalent in intent to `&&` / `||` in C-family languages.

# Examples

**Example 1** (*Short-Circuit Boolean Expressions*): `Expr1 orelse Expr2` evaluates `Expr2` only when `Expr1` is `false`; `Expr1 andalso Expr2` evaluates `Expr2` only when `Expr1` is `true`. By contrast `A or B` and `A and B` always evaluate both `A` and `B`.

# Relationships

## Builds Upon
- **Boolean** — Short-circuit operators consume and produce boolean values.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Boolean expressions** — `andalso`/`orelse` are the short-circuiting counterparts of `and`/`or`.

## Contrasts With
- **Boolean expressions** — `and`/`or` always evaluate both operands; `andalso`/`orelse` evaluate the second only when needed.

# Common Errors

- **Error**: Using `and`/`or` to guard a second operand that must not be evaluated.
  **Correction**: Use `andalso`/`orelse`, which skip the second operand when the result is already determined.

# Common Confusions

- **Confusion**: Believing `and` and `andalso` are interchangeable.
  **Clarification**: `and` always evaluates both arguments; `andalso` short-circuits.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Short-Circuit Boolean Expressions".

# Verification Notes

- Definition source: Direct quotation from *Short-Circuit Boolean Expressions*.
- Confidence rationale: HIGH — the source explicitly defines both operators and contrasts them with `and`/`or`.
- Uncertainties: None.
- Cross-reference status: Slug `boolean` extracted in this chapter; `boolean-expressions` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
