---
# === CORE IDENTIFICATION ===
concept: Operator Precedence
slug: operator-precedence

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
section: "Operator Precedence"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "precedence table"
  - "operator associativity"
  - "evaluation order"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-expressions
  - boolean-operators
  - term-comparisons
extends: []
related:
  - parenthesized-expression
  - match-operator
  - send-operator
  - short-circuit-operators
  - list-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the operator precedence in Erlang?"
  - "Which operators have the highest precedence in Erlang?"
  - "What does operator associativity mean in Erlang?"
  - "Why can't I chain comparison operators in Erlang?"
  - "What is the precedence of the catch operator?"
---

# Quick Definition

Erlang operators have a defined precedence (highest to lowest) and associativity (left, right, or non-associative) that determines evaluation order when operators are combined without explicit parentheses.

# Core Definition

Operator precedence in Erlang defines the evaluation order when multiple operators appear in an expression without explicit parentheses. Operators with higher precedence are evaluated first. Operators with the same precedence are evaluated according to their associativity: left-associative operators group left to right, right-associative operators group right to left, and non-associative operators cannot be combined with operators of the same precedence. The `catch` operator's precedence was raised in OTP 24 (previously it had the lowest precedence). The `?=` conditional match operator (used only in `maybe` blocks) has the lowest precedence (Erlang Reference Manual, "Operator Precedence" section).

# Prerequisites

- **arithmetic-expressions** — Arithmetic operators are part of the precedence table.
- **boolean-operators** — Boolean operators are part of the precedence table.
- **term-comparisons** — Comparison operators are part of the precedence table.

# Key Properties

1. Precedence descending order (highest first):
   - `#` (record)
   - Unary `+`, `-`, `bnot`, `not`
   - `/`, `*`, `div`, `rem`, `band`, `and` (left-associative)
   - `+`, `-`, `bor`, `bxor`, `bsl`, `bsr`, `or`, `xor` (left-associative)
   - `++`, `--` (right-associative)
   - `==`, `/=`, `=<`, `<`, `>=`, `>`, `=:=`, `=/=` (non-associative)
   - `andalso` (left-associative)
   - `orelse` (left-associative)
   - `catch`
   - `=`, `!` (right-associative)
   - `?=` (non-associative)
2. Non-associative operators cannot be chained (e.g., `1 < X < 10` is a syntax error).
3. `=` and `!` share the same precedence level and are right-associative.
4. `catch` precedence was raised in OTP 24; previously required parentheses with `=`.
5. `?=` is restricted to top-level of `maybe` blocks.

# Construction / Recognition

The precedence table is a reference; it is recognized by its effect on evaluation order.

**Left-associative example:**
```
6 + 5 * 4 - 3 / 2
= 6 + 20 - 1.5
= 26 - 1.5
= 24.5
```

**Non-associative restriction:**
```erlang
1> 1 < X < 10.
* 1:7: syntax error before: '<'
```

# Context & Application

Understanding operator precedence is necessary for writing correct expressions without excessive parenthesization and for reading complex expressions. The non-associativity of comparison operators is a notable difference from some other languages. The right-associativity of `=` and `!` enables chained match expressions and message sends.

# Examples

**Example 1** (Operator Precedence section): Arithmetic precedence:

```
6 + 5 * 4 - 3 / 2 evaluates to
6 + 20 - 1.5 evaluates to
26 - 1.5 evaluates to
24.5
```

**Example 2** (Operator Precedence section): Non-associative comparison (syntax error):

```erlang
1> 1 < X < 10.
* 1:7: syntax error before: '<'
```

**Example 3** (Parenthesized Expressions section): Using parentheses to override:

```erlang
1> 1 + 2 * 3.
7
2> (1 + 2) * 3.
9
```

**Example 4**: Catch precedence change (OTP 24+):

```erlang
%% OTP 24+: no parentheses needed
A = catch 42.

%% Before OTP 24: parentheses were required
A = (catch 42).
```

# Relationships

## Builds Upon
- **arithmetic-expressions** — Arithmetic operators in the table.
- **boolean-operators** — Boolean operators in the table.
- **term-comparisons** — Comparison operators in the table.

## Enables
- Correct parsing and evaluation of complex expressions.

## Related
- **parenthesized-expression** — Used to override precedence.
- **match-operator** — `=` is right-associative, shared precedence with `!`.
- **send-operator** — `!` is right-associative, shared precedence with `=`.
- **short-circuit-operators** — `andalso`/`orelse` have specific positions in the table.
- **list-operations** — `++`/`--` are right-associative.

# Common Errors

- **Error**: Chaining comparison operators like `1 < X < 10`.
  **Correction**: Comparison operators are non-associative. Write `X > 1 andalso X < 10` instead.

- **Error**: Assuming `catch` has the lowest precedence (pre-OTP 24 behavior).
  **Correction**: Since OTP 24, `catch` has higher precedence than `=` and `!`. `A = catch 42` works without parentheses.

# Common Confusions

- **Confusion**: Thinking `and` and `andalso` have the same precedence.
  **Clarification**: `and` has higher precedence (in the multiplication group); `andalso` has lower precedence (below comparisons).

- **Confusion**: Expecting `++` and `--` to be left-associative like arithmetic operators.
  **Clarification**: `++` and `--` are right-associative. This means `A ++ B ++ C` is `A ++ (B ++ C)`, which is more efficient for list concatenation.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Operator Precedence" section.

# Verification Notes

- Definition source: Direct from source text — precedence table reproduced from source
- Confidence rationale: High — complete table and examples from source
- Uncertainties: None
- Cross-reference status: OTP 24 catch precedence change verified in source
