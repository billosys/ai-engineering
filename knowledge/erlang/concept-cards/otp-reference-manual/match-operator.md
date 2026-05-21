---
# === CORE IDENTIFICATION ===
concept: Match Operator
slug: match-operator

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
section: "The Match Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "= operator"
  - "match expression"
  - "pattern match operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - single-assignment
extends: []
related:
  - compound-pattern-operator
  - variables
  - case-expression
contrasts_with:
  - compound-pattern-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the = match operator work in Erlang expressions?"
  - "What is the difference between the match operator and the compound pattern operator?"
  - "What happens when a match fails in Erlang?"
  - "How are chained match operators evaluated?"
---

# Quick Definition

The match operator `=` matches a pattern on the left against the value of an expression on the right. On success, unbound variables in the pattern become bound and the expression value is returned. On failure, a `badmatch` run-time error occurs.

# Core Definition

The match operator `Pattern = Expr` evaluates `Expr` and matches the result against `Pattern`. If matching succeeds, any unbound variable in the pattern becomes bound and the value of `Expr` is returned. If matching fails, a `badmatch` run-time error occurs. When multiple match operators are applied in sequence (`Pattern1 = Pattern2 = ... = Expr`), they are evaluated from right to left: the expression is evaluated once, then each pattern is matched against it in right-to-left order (Erlang Reference Manual, "The Match Operator" section).

# Prerequisites

- **pattern-matching** — The match operator performs pattern matching.
- **single-assignment** — Variables can only be bound once; the match operator either binds or tests equality.

# Key Properties

1. `Pattern = Expr` matches the value of `Expr` against `Pattern`.
2. On success, returns the value of `Expr` and binds any unbound variables.
3. On failure, raises a `{badmatch, V}` run-time error where `V` is the value of `Expr`.
4. Chained matches are evaluated right to left.
5. The match operator is allowed everywhere an expression is allowed.
6. Right-associative with the same precedence as `!` (send).
7. Contextually distinct from the compound pattern operator, which uses the same `=` character.

# Construction / Recognition

## To Construct:
```erlang
{A, B} = {answer, 42}
```

Chained matches:
```erlang
{A, B} = T = {answer, 42}
```

## To Recognize:
1. Look for `Pattern = Expr` where `=` appears in an expression context (not in a pattern-only context).
2. The right side is evaluated as an expression; the left side is a pattern.

# Context & Application

The match operator is fundamental to Erlang programming. It is used for variable binding, destructuring, assertion (matching a bound variable against a value), and extracting components from data structures. Since Erlang uses single assignment, the match operator serves both as variable initialization and as a runtime assertion mechanism.

# Examples

**Example 1** (The Match Operator section): Binding and destructuring:

```erlang
1> {A, B} = T = {answer, 42}.
{answer,42}
2> A.
answer
3> B.
42
4> T.
{answer,42}
```

**Example 2** (The Match Operator section): Match failure:

```erlang
5> {C, D} = [1, 2].
** exception error: no match of right-hand side value [1,2]
```

**Example 3** (The Match Operator section): Right-to-left evaluation of chained matches:

```erlang
Pattern1 = Pattern2 = ... = PatternN = Expression
```

is equivalent to:

```erlang
Temporary = Expression,
PatternN = Temporary,
...
Pattern2 = Temporary,
Pattern1 = Temporary
```

# Relationships

## Builds Upon
- **pattern-matching** — The match operator applies pattern matching.
- **single-assignment** — Variables bound via match cannot be rebound.

## Enables
- **case-expression** — Pattern matching in `case` uses the same mechanism.
- **variables** — The match operator is the primary way to bind variables.

## Related
- **compound-pattern-operator** — Uses the same `=` character but in pattern context.

## Contrasts With
- **compound-pattern-operator** — The compound pattern operator joins two patterns matched simultaneously; the match operator evaluates an expression and matches a pattern against it. Context determines which is meant.

# Common Errors

- **Error**: Expecting `=` to rebind an already-bound variable to a new value.
  **Correction**: In Erlang, `=` on a bound variable is a match test, not a reassignment. If the value differs, `badmatch` occurs.

- **Error**: Confusing match operator failure with a compile error.
  **Correction**: `badmatch` is a run-time error, not a compile-time error. The pattern may be structurally valid but fail at runtime.

# Common Confusions

- **Confusion**: Not distinguishing the match operator from the compound pattern operator.
  **Clarification**: When `=` appears between two patterns (e.g., inside a function head or `case` clause pattern), it is the compound pattern operator. When it appears with an expression on the right, it is the match operator. Context determines which is used.

- **Confusion**: Thinking chained matches evaluate left to right.
  **Clarification**: Chained match operators evaluate right to left. The expression is evaluated once, then each pattern is matched against it from right to left.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "The Match Operator" and "The Match Operator and the Compound Pattern Operator" sections.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax, evaluation order, and examples from source
- Uncertainties: None
- Cross-reference status: Distinction from compound-pattern-operator verified in source
