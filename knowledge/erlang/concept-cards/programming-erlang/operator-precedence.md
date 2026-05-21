---
# === CORE IDENTIFICATION ===
concept: Operator Precedence
slug: operator-precedence

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
section: "Operator Precedence"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - operator priority
  - associativity

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - arithmetic-expressions
  - list-operators
  - term-comparison
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does operator precedence determine evaluation order?"
  - "Which operators are left or right associative?"
---

# Quick Definition

Operator precedence and associativity determine the evaluation order of unparenthesized expressions: higher-priority operators are evaluated first, and equal-priority operators evaluate by their associativity.

# Core Definition

The book gives a table of all Erlang operators in order of descending priority with their associativity ("The Rest of Sequential Erlang", *Operator Precedence*). "Operator precedence and associativity are used to determine the evaluation order in unparenthesized expressions. Expressions with higher priority (higher up in the table) are evaluated first, and then expressions with lower priority are evaluated." From highest to lowest, the table runs: `:`; `#`; unary `+`/`-`/`bnot`/`not`; `/ * div rem band and` (left associative); `+ - bor bxor bsl bsr or xor` (left associative); `++ --` (right associative); the comparison operators `== /= =< < >= > =:= =/=`; `andalso`; `orelse`; `= !` (right associative); `catch`. "As with all programming languages, it is better to use parentheses to denote scope than to rely upon the precedence rules."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Higher-priority operators (higher in the table) are evaluated before lower-priority ones.
2. Multiplication-class operators (`* / div rem band and`) outrank addition-class (`+ - bor ... or xor`).
3. `* /`-class and `+ -`-class operators are left associative.
4. `++` and `--` are right associative.
5. `=` and `!` are right associative.
6. Comparison operators sit below the list operators and above `andalso`/`orelse`.
7. Parentheses override the default order.

# Construction / Recognition

## To Construct/Create:
1. Use parentheses to make evaluation order explicit rather than relying on precedence.

## To Identify/Recognize:
1. Read the precedence table top-down: the first-listed operator in an expression that appears highest binds tightest.

# Context & Application

- **Typical contexts**: parsing the meaning of any unparenthesized compound expression.
- **Common applications**: knowing `3+4*5+6` means `((3+(4*5))+6)`.
- **Historical/stylistic notes**: the book recommends parentheses over reliance on precedence rules.

# Examples

**Example 1** (*Operator Precedence*): evaluating `3+4*5+6` — `*` outranks `+`, so `4*5` is computed first, giving `3+20+6`; `+` is left associative, so this is `(3+20)+6 = 29`. In fully parenthesized form, `3+4*5+6` means `((3+(4*5))+6)`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Arithmetic expressions** — Arithmetic operators occupy several rows of the precedence table.
- **List operators** — `++` and `--` are the right-associative list-operator row.
- **Term comparison** — The comparison operators form one row of the table.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Assuming `+` and `*` evaluate strictly left to right regardless of operator.
  **Correction**: `*` has higher priority than `+`; multiplication is evaluated first regardless of position.

# Common Confusions

- **Confusion**: Believing all binary operators are left associative.
  **Clarification**: `++`, `--`, `=`, and `!` are right associative.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Operator Precedence" (Table 5).

# Verification Notes

- Definition source: Direct adaptation of the operator precedence table in *Operator Precedence*.
- Confidence rationale: HIGH — the source tabulates every operator with its priority and associativity.
- Uncertainties: None.
- Cross-reference status: Slugs `arithmetic-expressions`, `list-operators`, `term-comparison` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
