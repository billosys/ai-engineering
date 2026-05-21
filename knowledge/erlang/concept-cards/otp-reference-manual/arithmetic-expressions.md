---
# === CORE IDENTIFICATION ===
concept: Arithmetic Expressions
slug: arithmetic-expressions

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
section: "Arithmetic Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "arithmetic operators"
  - "numeric operators"
  - "bitwise operators"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - term-comparisons
  - guard-expressions
  - operator-precedence
contrasts_with:
  - boolean-operators

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What arithmetic operators are available in Erlang?"
  - "What is the difference between / and div in Erlang?"
  - "What bitwise operators does Erlang provide?"
---

# Quick Definition

Arithmetic expressions perform numeric and bitwise operations on Erlang numbers. They include standard arithmetic (+, -, *, /), integer-specific operations (div, rem), and bitwise operations (band, bor, bxor, bnot, bsl, bsr).

# Core Definition

Arithmetic expressions use unary or binary operators on numeric arguments. The operators include: unary `+` and `-`, binary `+` (addition), `-` (subtraction), `*` (multiplication), `/` (floating-point division), `div` (integer division), `rem` (integer remainder), and the bitwise operators `bnot` (unary NOT), `band` (AND), `bor` (OR), `bxor` (XOR), `bsl` (shift left), `bsr` (arithmetic shift right). Operators requiring `Number` arguments accept both integers and floats; operators requiring `Integer` arguments accept only integers. An argument of the wrong type causes a `badarg` runtime error (Erlang Reference Manual, "Arithmetic Expressions" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The `/` operator always returns a float, even when both operands are integers (e.g., `4/2` returns `2.0`).
2. `div` performs integer division and requires integer arguments.
3. `rem` returns the integer remainder of `X/Y` and requires integer arguments.
4. Bitwise operators (`band`, `bor`, `bxor`, `bnot`, `bsl`, `bsr`) require integer arguments.
5. Erlang integers have arbitrary precision (no overflow), but `bsl` with very large shift amounts can cause a `system_limit` error.
6. Applying arithmetic operators to non-numeric arguments (e.g., `a + 10`) causes a `badarith` runtime error.
7. All arithmetic expressions are valid in guards.

# Construction / Recognition

## To Construct:
1. Use unary form: `op Expr` (for `+`, `-`, `bnot`).
2. Use binary form: `Expr1 op Expr2` (for all binary operators).
3. Ensure operands match the required type (Number or Integer).

## To Recognize:
1. Look for standard arithmetic symbols (`+`, `-`, `*`, `/`) or keyword operators (`div`, `rem`, `band`, `bor`, `bxor`, `bnot`, `bsl`, `bsr`).

# Context & Application

Arithmetic expressions are used throughout Erlang programs for numerical computation. They are valid in guard expressions, making them useful in function clause heads and conditional expressions. The distinction between `/` (always float) and `div` (integer-only) is particularly important for programs that need to maintain integer precision.

# Examples

**Example 1** (Arithmetic Expressions section): Basic arithmetic:

```erlang
1> +1.
1
2> -1.
-1
3> 1+1.
2
4> 4/2.
2.0
5> 5 div 2.
2
6> 5 rem 2.
1
```

**Example 2** (Arithmetic Expressions section): Bitwise operations:

```erlang
7> 2#10 band 2#01.
0
8> 2#10 bor 2#01.
3
```

**Example 3** (Arithmetic Expressions section): Type error:

```erlang
9> a + 10.
** exception error: an error occurred when evaluating an arithmetic expression
     in operator  +/2
        called as a + 10
```

**Example 4** (Arithmetic Expressions section): System limit with large shift:

```erlang
10> 1 bsl (1 bsl 64).
** exception error: a system limit has been reached
     in operator  bsl/2
        called as 1 bsl 18446744073709551616
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **guard-expressions** — Arithmetic expressions are valid guard expressions.

## Related
- **term-comparisons** — Often used together with comparison operators.
- **operator-precedence** — Multiplicative operators bind tighter than additive.

## Contrasts With
- **boolean-operators** — Boolean operators work on `true`/`false` values, not numbers.

# Common Errors

- **Error**: Using `/` when integer division is intended.
  **Correction**: Use `div` for integer division; `/` always produces a float.

- **Error**: Applying bitwise operators to floats.
  **Correction**: Bitwise operators require integer arguments. Convert with `trunc/1` or `round/1` if needed.

# Common Confusions

- **Confusion**: Expecting `/` to return an integer when both operands are integers.
  **Clarification**: The `/` operator always returns a float in Erlang (e.g., `4/2` returns `2.0`). Use `div` for integer division.

- **Confusion**: Confusing `rem` with modulo — they differ for negative numbers.
  **Clarification**: `rem` returns the remainder with the same sign as the dividend, which matches mathematical remainder but not all definitions of modulo.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Arithmetic Expressions" section.

# Verification Notes

- Definition source: Direct from source text (operator table and examples)
- Confidence rationale: High — explicit operator table with types and examples
- Uncertainties: None
- Cross-reference status: Related concepts verified against planned extractions
