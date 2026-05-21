---
# === CORE IDENTIFICATION ===
concept: Case Expression
slug: case-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Case"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "case expression"
  - "case block"
  - "case-of"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - guard-sequences
extends: []
related:
  - if-expression
  - receive-expression
  - try-expression
  - variable-scope
contrasts_with:
  - if-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the case expression work in Erlang?"
  - "How do I match patterns with guards in a case expression?"
  - "What happens when no pattern matches in a case expression?"
  - "What is a case_clause error?"
---

# Quick Definition

The `case` expression evaluates an expression and matches the result against a series of patterns with optional guard sequences, executing the body of the first matching clause. It is the primary branching construct in Erlang.

# Core Definition

In a `case` expression, the expression `Expr` is evaluated and the patterns `Pattern` are sequentially matched against the result. If a match succeeds and the optional guard sequence `GuardSeq` is true, the corresponding `Body` is evaluated. The return value of `Body` is the return value of the `case` expression. If there is no matching pattern with a true guard sequence, a `case_clause` run-time error occurs (Erlang Reference Manual, "Case" section).

# Prerequisites

- **pattern-matching** — The `case` expression fundamentally relies on pattern matching.
- **guard-sequences** — Optional guards refine pattern matching in each clause.

# Key Properties

1. Evaluates `Expr` first, then matches sequentially against patterns.
2. The first pattern that matches with a true guard wins.
3. If no clause matches, a `case_clause` run-time error occurs.
4. Each clause can have an optional guard sequence (introduced by `when`).
5. The return value is the value of the matched clause's body.
6. Variables bound in one branch must be bound in all branches to be safe outside the expression.

# Construction / Recognition

## To Construct:
```erlang
case Expr of
    Pattern1 [when GuardSeq1] ->
        Body1;
    ...;
    PatternN [when GuardSeqN] ->
        BodyN
end
```

## To Recognize:
1. Look for the `case ... of ... end` block structure.
2. Each clause has a pattern (optionally with guard) before the `->`.

# Context & Application

The `case` expression is the most common branching construct in Erlang, combining pattern matching with optional guard conditions. It is used when the control flow depends on the structure or value of a term. Unlike `if`, which only tests guards, `case` can destructure terms and bind variables in patterns.

# Examples

**Example 1** (Case section): Validating a signal tuple:

```erlang
is_valid_signal(Signal) ->
    case Signal of
        {signal, _What, _From, _To} ->
            true;
        {signal, _What, _To} ->
            true;
        _Else ->
            false
    end.
```

**Example 2**: Using a guard in a case clause:

```erlang
classify(X) ->
    case X of
        N when N > 0 -> positive;
        0 -> zero;
        N when N < 0 -> negative
    end.
```

# Relationships

## Builds Upon
- **pattern-matching** — Core mechanism for selecting a branch.
- **guard-sequences** — Provides additional clause filtering.

## Enables
- **variable-scope** — Variables bound in `case` branches affect scope.

## Related
- **if-expression** — Both are multi-branch control flow expressions.
- **receive-expression** — Uses similar clause syntax with patterns and guards.
- **try-expression** — The `of` section of `try` works like `case` (but raises `try_clause`).

## Contrasts With
- **if-expression** — `if` tests only guard sequences; `case` matches patterns against a value.

# Common Errors

- **Error**: Omitting a catch-all pattern, causing `case_clause` errors at runtime.
  **Correction**: Add a catch-all clause like `_ -> DefaultValue` as the last branch.

- **Error**: Shadowing variables by reusing a bound variable name in a pattern (expecting re-binding).
  **Correction**: Erlang's single-assignment means a bound variable in a pattern is a match test, not a rebinding. Use a fresh variable name or a guard test.

# Common Confusions

- **Confusion**: Thinking `case_clause` errors come from incorrect expressions rather than unmatched patterns.
  **Clarification**: A `case_clause` error means no pattern matched the evaluated expression, with `{case_clause, V}` reporting the unmatched value `V`.

- **Confusion**: Expecting clauses to be evaluated in parallel or non-deterministically.
  **Clarification**: Clauses are always matched sequentially from top to bottom.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Case" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear syntax, semantics, and example from source
- Uncertainties: None
- Cross-reference status: Contrasts with if-expression verified in source
