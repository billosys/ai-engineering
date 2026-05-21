---
# === CORE IDENTIFICATION ===
concept: If Expression
slug: if-expression

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
section: "If"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "if expression"
  - "if block"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - guard-sequences
  - guard-expressions
extends: []
related:
  - case-expression
  - receive-expression
  - variable-scope
contrasts_with:
  - case-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the if expression work in Erlang?"
  - "Why does my if expression fail with an if_clause error?"
  - "How do I create an else branch in an Erlang if expression?"
  - "What can appear in if branches in Erlang?"
---

# Quick Definition

The `if` expression evaluates guard sequences in order and executes the body of the first branch whose guard evaluates to true. Unlike `case`, it does not perform pattern matching; it relies solely on guard sequences.

# Core Definition

An `if` expression scans its branches sequentially until a guard sequence `GuardSeq` that evaluates to true is found, then evaluates the corresponding `Body` (a sequence of expressions separated by `,`). The return value of `Body` is the return value of the `if` expression. If no guard sequence evaluates to true, an `if_clause` run-time error occurs. The guard expression `true` can be used in the last branch to serve as an "else" branch (Erlang Reference Manual, "If" section).

# Prerequisites

- **guard-sequences** — The `if` expression branches are controlled entirely by guard sequences.
- **guard-expressions** — Only valid guard expressions can appear in `if` branches.

# Key Properties

1. Branches are scanned sequentially until a true guard is found.
2. No pattern matching is involved; only guard sequences control branching.
3. If no guard is true, an `if_clause` run-time error occurs.
4. The atom `true` can be used as a catch-all "else" guard.
5. The return value is the value of the selected body.
6. Variables bound in one branch must be bound in all branches to be safe outside the expression.

# Construction / Recognition

## To Construct:
```erlang
if
    GuardSeq1 ->
        Body1;
    ...;
    GuardSeqN ->
        BodyN
end
```

## To Recognize:
1. Look for `if ... end` block structure.
2. Each branch has a guard sequence (not a pattern) before the `->`.

# Context & Application

The `if` expression is used when decisions depend on conditions testable as guards (comparisons, type tests, arithmetic checks) rather than on the structure of a value. It is less common than `case` in Erlang code because `case` provides both pattern matching and guard support. The `if` expression is most useful when multiple independent boolean conditions need to be tested.

# Examples

**Example 1** (If section): Basic if with a true catch-all:

```erlang
is_greater_than(X, Y) ->
    if
        X > Y ->
            true;
        true -> % works as an 'else' branch
            false
    end
```

**Example 2**: Multi-branch if:

```erlang
classify(X) ->
    if
        X > 0 -> positive;
        X < 0 -> negative;
        true  -> zero
    end.
```

# Relationships

## Builds Upon
- **guard-sequences** — Each branch of an `if` is a guard sequence.
- **guard-expressions** — The conditions must be valid guard expressions.

## Enables
- **variable-scope** — Variables bound in `if` branches affect outer scope only if bound in all branches.

## Related
- **case-expression** — Both are multi-branch control flow expressions.
- **receive-expression** — Also uses guard sequences in clauses.

## Contrasts With
- **case-expression** — `case` matches patterns against a value; `if` only tests guard sequences.

# Common Errors

- **Error**: Omitting a catch-all `true` branch, causing `if_clause` errors at runtime.
  **Correction**: Add `true -> DefaultValue` as the last branch, or ensure the guard sequences are exhaustive.

- **Error**: Using non-guard expressions (function calls with side effects) in `if` branches.
  **Correction**: Only valid guard expressions are allowed. Use `case` with a match if arbitrary expressions are needed for branching.

# Common Confusions

- **Confusion**: Expecting `if` to work like `if` in imperative languages with an implicit else.
  **Clarification**: Erlang's `if` is an expression that must return a value. Every branch must be covered, or a runtime error occurs.

- **Confusion**: Thinking `if` can do pattern matching.
  **Clarification**: `if` only tests guard sequences. Use `case` for pattern matching.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "If" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear syntax, semantics, and example from source
- Uncertainties: None
- Cross-reference status: Contrasts with case-expression verified in source
