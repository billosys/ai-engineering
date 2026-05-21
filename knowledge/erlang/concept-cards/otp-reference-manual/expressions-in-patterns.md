---
# === CORE IDENTIFICATION ===
concept: Expressions in Patterns
slug: expressions-in-patterns

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: patterns
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Expressions in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "arithmetic expressions in patterns"
  - "constant expressions in patterns"
  - "compile-time constant patterns"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - patterns-in-expressions
  - compound-pattern-operator
  - match-operator
contrasts_with:
  - patterns-in-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I use an arithmetic expression inside a pattern?"
  - "What conditions must an expression meet to be allowed in a pattern?"
  - "Why does ?THRESHOLD+1 work as a pattern element?"
---

# Quick Definition

An arithmetic expression may appear inside a pattern only if it uses only numeric or bitwise operators and evaluates to a constant at compile time. This lets constants like `?THRESHOLD+1` be matched directly.

# Core Definition

An arithmetic expression can be used within a pattern if it meets *both* conditions (Reference Manual, "Expressions" > "Expressions in Patterns"):

1. It uses only numeric or bitwise operators.
2. Its value can be evaluated to a constant when compiled.

This is the narrow, well-defined sense in which "expressions" are permitted on the pattern side — they must be compile-time constants, so the compiler can fold them into a literal before matching.

# Prerequisites

- **pattern-matching** — you must understand how a pattern is matched against a term before understanding what may appear inside one

# Key Properties

1. Only numeric and bitwise operators are permitted (`+`, `-`, `*`, `bsl`, `band`, etc.).
2. The expression must be a *compile-time constant* — no variables whose values are only known at run time.
3. Macros that expand to constants (e.g. `?THRESHOLD`) are common operands.
4. The compiler evaluates the expression once, at compile time, and matches against the resulting literal.

# Construction / Recognition

## To Apply:
1. Ensure every operand is a literal or a constant macro.
2. Use only numeric/bitwise operators.
3. Place the expression where a literal pattern element would go.

## To Recognize:
1. An arithmetic operator appearing on the left-hand (pattern) side of a `case` clause, function head, or match.
2. A macro-plus-constant form such as `?THRESHOLD+1` inside a tuple/list pattern.

# Context & Application

- **Typical contexts**: matching against a threshold or offset derived from a constant macro without introducing a guard.
- **Common applications**: `case {Value, Result} of {?THRESHOLD+1, ok} -> ... end`.

# Examples

**Example 1** (Reference Manual, "Expressions in Patterns"):

```erlang
case {Value, Result} of
    {?THRESHOLD+1, ok} -> ...
end
```

The element `?THRESHOLD+1` is evaluated to a constant at compile time and matched as a literal.

# Relationships

## Builds Upon
- **pattern-matching** — the matching mechanism this refines

## Related
- **compound-pattern-operator** — another pattern-side construct
- **match-operator** — patterns appear on the left of `=`

## Contrasts With
- **patterns-in-expressions** — the inverse direction: patterns appearing where expressions are evaluated, rather than constant expressions appearing inside patterns

# Common Errors

- **Error**: Using a run-time variable in a pattern expression (e.g. `{N+1, ok}` where `N` is bound at run time).
  **Correction**: Only compile-time constants are allowed; move run-time comparisons into a guard.

- **Error**: Using a non-arithmetic operator (e.g. `++`) and expecting it to fold.
  **Correction**: Only numeric/bitwise operators qualify (string-prefix `++` is a separate, specifically-allowed sugar — see `string-prefix-in-patterns`).

# Common Confusions

- **Confusion**: Thinking arbitrary expressions can be used in patterns.
  **Clarification**: Only constant-folding numeric/bitwise expressions are allowed.

- **Confusion**: Conflating this with using a pattern within an expression.
  **Clarification**: That is the converse concept, `patterns-in-expressions`.

# Source Reference

Chapter "Expressions", section "Patterns" > subsection "Expressions in Patterns" (Erlang Reference Manual). See the `?THRESHOLD+1` example.

# Verification Notes

- Definition source: Direct adaptation of the two-condition rule and the example.
- Confidence rationale: HIGH — explicit, short, unambiguous rule with an example.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified (`pattern-matching`, `patterns-in-expressions`, `compound-pattern-operator`, `match-operator`).
- Re-extraction notes: New card filling a documented gap (was referenced by `patterns-in-expressions`).
