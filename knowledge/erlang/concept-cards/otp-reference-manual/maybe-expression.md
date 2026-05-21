---
# === CORE IDENTIFICATION ===
concept: Maybe Expression
slug: maybe-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Maybe"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "maybe block"
  - "maybe...else"
  - "conditional match operator"
  - "?= operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - match-operator
extends: []
related:
  - case-expression
  - try-expression
  - variable-scope
contrasts_with:
  - case-expression
  - match-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the maybe expression in Erlang?"
  - "How does the ?= conditional match operator work?"
  - "How do I avoid deeply nested case expressions in Erlang?"
  - "What happens when a ?= match fails in a maybe block?"
  - "What is the else clause in a maybe expression?"
---

# Quick Definition

The `maybe` expression (OTP 25+, default from OTP 27) provides a way to chain conditional match operations using the `?=` operator. If any conditional match fails, execution short-circuits and the non-matching value is returned (or matched against `else` clauses).

# Core Definition

In a `maybe` block, expressions are evaluated sequentially. The conditional match operator `?=` matches a pattern against an expression; on success, unbound variables become bound and evaluation continues. If the match fails, the remaining expressions are skipped and the value of the failed expression becomes the return value of the block. If the `maybe` block includes `else` clauses, a failed conditional match value is matched against those clauses instead. If no `else` clause matches, an `else_clause` run-time error occurs. Variables bound in the `maybe` block must not be used after the block or in the `else` clauses. The `?=` operator is only allowed at the top-level of a `maybe` block (Erlang Reference Manual, "Maybe" section).

# Prerequisites

- **pattern-matching** — The `?=` operator performs pattern matching.
- **match-operator** — Understanding `=` vs `?=` is essential; `=` raises on failure while `?=` short-circuits.

# Key Properties

1. Introduced in OTP 25 as a feature; enabled by default from OTP 27.
2. The `?=` conditional match operator is only allowed at the top-level of a `maybe` block.
3. On `?=` match failure, execution short-circuits and returns the non-matching value.
4. The regular match operator `=` inside a `maybe` block still raises `badmatch` on failure.
5. An optional `else` section catches failed `?=` values with pattern-matching clauses.
6. If `else` is present and no clause matches, `else_clause` run-time error occurs.
7. Variables bound in the `maybe` block are unsafe outside the block and in `else` clauses.
8. `?=` is non-associative and has the lowest precedence in the operator table.

# Construction / Recognition

## To Construct:
```erlang
maybe
    {ok, A} ?= expr1(),
    {ok, B} ?= expr2(),
    A + B
end
```

With `else` clauses:
```erlang
maybe
    {ok, A} ?= expr1(),
    {ok, B} ?= expr2(),
    A + B
else
    error -> handle_error;
    {error, Reason} -> {failed, Reason}
end
```

## To Recognize:
1. Look for `maybe ... end` block structure.
2. Uses `?=` operator for conditional matches.

# Context & Application

The `maybe` expression addresses the common Erlang pattern of deeply nested `case` expressions when chaining operations that may fail. It is particularly useful for sequences of operations that return `{ok, Value}` or error tuples, eliminating "staircase" nesting. It replaces patterns that would otherwise require nested case expressions or monadic-style error handling.

# Examples

**Example 1** (Maybe section): Chaining fallible operations:

```erlang
maybe
    {ok, A} ?= a(),
    true = A >= 0,
    {ok, B} ?= b(),
    A + B
end
```

If `a()` returns `{ok,42}` and `b()` returns `{ok,58}`, the result is `100`. If `a()` returns `error`, the result is `error`. If `b()` returns `wrong`, the result is `wrong`.

**Example 2** (Maybe section): Equivalent nested case expressions:

```erlang
case a() of
    {ok, A} ->
        true = A >= 0,
        case b() of
            {ok, B} ->
                A + B;
            Other1 ->
                Other1
        end;
    Other2 ->
        Other2
end
```

**Example 3** (Maybe section): Using `else` clauses:

```erlang
maybe
    {ok, A} ?= a(),
    true = A >= 0,
    {ok, B} ?= b(),
    A + B
else
    error -> error;
    wrong -> error
end
```

# Relationships

## Builds Upon
- **pattern-matching** — `?=` performs pattern matching.
- **match-operator** — `=` is still usable within `maybe` blocks with its normal semantics.

## Enables
- Flattened error-handling pipelines without nested `case` expressions.

## Related
- **case-expression** — `maybe` can replace nested case expressions.
- **try-expression** — Both handle exceptional control flow.
- **variable-scope** — Variables bound in `maybe` are unsafe outside the block.

## Contrasts With
- **case-expression** — `case` nests; `maybe` linearizes chained conditional matches.
- **match-operator** — `=` raises `badmatch` on failure; `?=` short-circuits.

# Common Errors

- **Error**: Using `?=` outside of a `maybe` block.
  **Correction**: The `?=` operator is only valid at the top-level of a `maybe` block.

- **Error**: Using variables bound inside the `maybe` block after the block ends.
  **Correction**: Variables bound in a `maybe` block are unsafe outside it. Capture the result of the entire `maybe` block in a variable instead.

- **Error**: Forgetting that `=` inside `maybe` still raises `badmatch` on failure.
  **Correction**: Use `?=` for conditional matching (short-circuit on failure) and `=` only when failure should be an error.

# Common Confusions

- **Confusion**: Thinking `else` catches all failures including `=` match failures.
  **Clarification**: The `else` section only catches values from failed `?=` matches. A failed `=` match raises a `badmatch` error as usual.

- **Confusion**: Expecting variables from `maybe` to be accessible in `else` clauses.
  **Clarification**: Variables bound in the `maybe` block are not available in `else` clauses.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Maybe" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — comprehensive syntax, semantics, examples, and scoping rules from source
- Uncertainties: None
- Cross-reference status: Relationship to case-expression and match-operator verified in source
