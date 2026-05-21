---
# === CORE IDENTIFICATION ===
concept: Term Comparisons
slug: term-comparisons

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
section: "Term Comparisons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "comparison operators"
  - "relational operators"
  - "term equivalence"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - arithmetic-expressions
  - guard-expressions
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compare terms in Erlang?"
  - "What is the difference between == and =:= in Erlang?"
  - "What is the term ordering in Erlang?"
---

# Quick Definition

Term comparison operators compare two Erlang terms and return `true` or `false`. Erlang defines a total ordering over all data types, allowing comparison of values of different types.

# Core Definition

The expression `Expr1 op Expr2` compares two terms using one of eight comparison operators: `==` (equal to), `/=` (not equal to), `=<` (less than or equal to), `<` (less than), `>=` (greater than or equal to), `>` (greater than), `=:=` (term equivalence), and `=/=` (term non-equivalence). Arguments can be of different data types, with the following ordering defined: `number < atom < reference < fun < port < pid < tuple < map < nil < list < bit string`. Term comparison operators return the Boolean value `true` or `false` (Erlang Reference Manual, "Term Comparisons" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Eight comparison operators are available: `==`, `/=`, `=<`, `<`, `>=`, `>`, `=:=`, `=/=`.
2. A total ordering exists across all types: `number < atom < reference < fun < port < pid < tuple < map < nil < list < bit string`.
3. `nil` (empty list `[]`) is a separate type from `list`, ordered before it.
4. Lists are compared element by element; tuples are ordered by size first, then element by element.
5. Maps are ordered by size first, then by keys in ascending order, then by values in key order.
6. Atoms are compared by their string value, codepoint by codepoint.
7. `=:=` and `=/=` (term equivalence) distinguish between integer and float representations of the same number (e.g., `1 =:= 1.0` is `false`).
8. `==` and `/=` consider the same numbers equal regardless of type (e.g., `1 == 1.0` is `true`).
9. Since OTP 27, `0.0` and `-0.0` are distinct under `=:=` (they were previously considered the same).
10. Bit strings are compared bit by bit; a prefix is considered smaller than the full bit string.

# Construction / Recognition

## To Compare Terms:
1. Choose the appropriate operator based on whether type-aware equality is needed (`=:=`/`=/=`) or numeric equality suffices (`==`/`/=`).
2. Write `Expr1 op Expr2`.
3. The result is `true` or `false`.

## To Recognize:
1. Look for any of the eight comparison operators between two expressions.
2. Comparison operators are non-associative (cannot be chained like `1 < X < 10`).

# Context & Application

Term comparisons are used throughout Erlang programs in guards, conditionals, and general logic. The term equivalence operators (`=:=` and `=/=`) are particularly important in associative containers and memoization where mixing integer and float keys could produce incorrect results. The total ordering across types enables sorting of heterogeneous data structures.

# Examples

**Example 1** (Term Comparisons section): Numeric equality vs. term equivalence:

```erlang
1> 1 == 1.0.
true
2> 1 =:= 1.0.
false
```

**Example 2** (Term Comparisons section): Signed zero distinction (OTP 27+):

```erlang
3> 0 =:= 0.0.
false
4> 0.0 =:= -0.0.
false
5> 0.0 =:= +0.0.
true
```

**Example 3** (Term Comparisons section): Cross-type comparison:

```erlang
6> 1 > a.
false
```

**Example 4** (Term Comparisons section): Map comparison:

```erlang
7> #{c => 3} > #{a => 1, b => 2}.
false
8> #{a => 1, b => 2} == #{a => 1.0, b => 2.0}.
true
```

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **guard-expressions** — Term comparisons are valid guard expressions.

## Related
- **arithmetic-expressions** — Arithmetic and comparison operators are often used together.
- **operator-precedence** — Comparison operators have specific precedence (non-associative, between arithmetic and `andalso`).

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Writing `=<` as `<=` (the latter is not a valid Erlang operator; `<=` is the bit string generator).
  **Correction**: Use `=<` for "less than or equal to" in Erlang.

- **Error**: Chaining comparisons like `1 < X < 10`.
  **Correction**: Comparison operators are non-associative. Use `X > 1 andalso X < 10`.

# Common Confusions

- **Confusion**: Thinking `==` and `=:=` behave the same way.
  **Clarification**: `==` performs numeric equality (1 == 1.0 is true), while `=:=` performs term equivalence (1 =:= 1.0 is false). Use `=:=` when the type distinction matters.

- **Confusion**: Expecting `0.0` and `-0.0` to be equal under `=:=`.
  **Clarification**: Since OTP 27, these are distinct terms under `=:=`. Use `+0.0` in patterns to silence compiler warnings about matching `0.0`.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Term Comparisons" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit operator table, ordering definition, and examples provided
- Uncertainties: None
- Cross-reference status: Related concepts verified against planned extractions
