---
# === CORE IDENTIFICATION ===
concept: Arithmetic Expressions
slug: arithmetic-expressions

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
section: "Arithmetic Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - arithmetic operators
  - "div"
  - "rem"
  - bitwise operators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - numbers
extends: []
related:
  - operator-precedence
contrasts_with:
  - boolean-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What arithmetic operators does Erlang provide?"
  - "What is the difference between / and div?"
  - "How is operator priority used in arithmetic?"
---

# Quick Definition

Erlang's arithmetic expressions cover unary and binary operators on numbers and integers — including `+`, `-`, `*`, `/`, `div`, `rem`, and the bitwise operators — each with an evaluation priority.

# Core Definition

The book tabulates all legal arithmetic expressions ("The Rest of Sequential Erlang", *Arithmetic Expressions*). Operators take one or two arguments of type Integer or Number (a Number may be an integer or a float). They are: unary `+ X` and `- X` (priority 1); `X * Y`, `X / Y` (floating-point division), `bnot X`, `X div Y` (integer division), `X rem Y` (integer remainder), `X band Y` (priority 2); `X + Y`, `X - Y`, `X bor Y`, `X bxor Y`, `X bsl N` (arithmetic shift left), `X bsr N` (arithmetic shift right) (priority 3). "The order of evaluation of a complex arithmetic expression depends upon the priority of the operator: all operations with priority 1 operators are evaluated first, then all operators with priority 2, and so on." Parentheses override the default order; equal-priority operators are left associative.

# Prerequisites

- **Numbers** — Arithmetic operators act on integers and floats, so the number syntax must be understood.

# Key Properties

1. Operators are grouped into three priorities; lower-numbered priorities evaluate first.
2. `/` is always floating-point division; `div` is integer division.
3. `rem` gives the integer remainder.
4. The bitwise operators (`bnot`, `band`, `bor`, `bxor`, `bsl`, `bsr`) require integer arguments.
5. A "Number" argument may be an integer or a float; an "Integer" argument must be an integer.
6. Operators of equal priority are left associative and evaluate left to right.
7. Parentheses override the default priority order.

# Construction / Recognition

## To Construct/Create:
1. Combine operands with operators: `3 + 4 * 5 + 6`.
2. Use `div` and `rem` for integer arithmetic; `/` for floating-point.

## To Identify/Recognize:
1. The priority column of the arithmetic table determines which subexpression evaluates first.

# Context & Application

- **Typical contexts**: numeric computation throughout sequential Erlang.
- **Common applications**: integer-exact arithmetic with `div`/`rem`; bit manipulation with `band`/`bor`/`bsl`/`bsr`.
- **Historical/stylistic notes**: as with all languages, the book advises using parentheses rather than relying on precedence.

# Examples

**Example 1** (*Arithmetic Expressions* / *Operator Precedence*): evaluating `3+4*5+6` — the priority-2 `4*5` is computed first, giving `3+20+6`; left associativity then yields `(3+20)+6 = 29`.

**Example 2** (*Arithmetic Expressions*): `bnot X` is the bitwise not of integer `X`; `X bsl N` shifts `X` left by `N` bits.

# Relationships

## Builds Upon
- **Numbers** — Arithmetic operates on Erlang's integer and float types.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Operator precedence** — Arithmetic priorities are part of the full operator precedence table.

## Contrasts With
- **Boolean expressions** — Boolean operators act on `true`/`false` atoms, not numbers.

# Common Errors

- **Error**: Using `/` expecting integer division.
  **Correction**: `/` always yields a float; use `div` for integer division.

- **Error**: Applying a bitwise operator like `band` to a float.
  **Correction**: Bitwise operators require integer arguments.

# Common Confusions

- **Confusion**: Thinking `rem` always returns a non-negative result.
  **Clarification**: `rem` is the integer remainder of `X div Y`; the source defines it as such without further sign claims — rely on the documented behavior, not assumptions.

- **Confusion**: Believing all arithmetic operators share one priority.
  **Clarification**: They span three priority levels; multiplication-class operators bind tighter than addition-class operators.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Arithmetic Expressions" (Table 3) and "Operator Precedence".

# Verification Notes

- Definition source: Direct adaptation of the arithmetic-expressions table in *Arithmetic Expressions*.
- Confidence rationale: HIGH — the source tabulates every operator with its argument type and priority.
- Uncertainties: None.
- Cross-reference status: Slugs `numbers`, `operator-precedence`, `boolean-expressions` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
