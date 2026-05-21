---
# === CORE IDENTIFICATION ===
concept: Single Assignment
slug: single-assignment

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "single assignment variables"
  - "immutable binding"
  - "once-only binding"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variables
  - pattern-matching
extends: []
related:
  - pattern-matching-mechanism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I reassign a variable in Erlang?"
  - "What is single assignment?"
  - "Why does pattern matching fail when a bound variable does not match?"
---

# Quick Definition

Erlang uses single assignment: a variable can only be bound once. After binding, the variable's value is immutable; attempting to match it against a different value causes a runtime exception.

# Core Definition

The Erlang Reference Manual states: "Erlang uses _single assignment_, that is, a variable can only be bound once." This is demonstrated through the pattern matching mechanism: when a bound variable appears in a pattern, it acts as an equality assertion rather than a rebinding. If the value does not match, a runtime exception is raised (Erlang Reference Manual, "Expressions", "Variables").

# Prerequisites

- **variables** -- Must understand what variables are in Erlang
- **pattern-matching** -- Single assignment is enforced through pattern matching

# Key Properties

1. A variable can only be bound once within its scope
2. After binding, the variable's value cannot change
3. When a bound variable appears in a pattern, it asserts equality with the matched value
4. A failed assertion raises a runtime exception (e.g., `badmatch`)
5. To use a new value, a new variable name must be used

# Construction / Recognition

## To Identify/Recognize:
1. A `badmatch` error when re-matching a bound variable with a different value
2. Variables that hold the same value throughout their scope
3. Multiple variable names in sequence (e.g., `X1`, `X2`) where other languages would reuse `X`

# Context & Application

Single assignment is fundamental to Erlang's design philosophy. It eliminates mutable state within a process, simplifying reasoning about concurrent programs. Since variables cannot be reassigned, there are no race conditions on variable access. This also enables the runtime to safely share data between processes by reference.

# Examples

**Example 1** (Pattern Matching chapter): Demonstrating single assignment:
```erlang
2> X = 2.
2
4> {X, Y} = {1, 2}.
** exception error: no match of right hand side value {1,2}
```
`X` is bound to `2`; matching `{X, Y}` against `{1, 2}` fails because `X` (value `2`) cannot match `1`.

# Relationships

## Builds Upon
- **variables** -- Single assignment is the binding model for variables
- **pattern-matching** -- Enforces single assignment by asserting bound variable values

## Enables
- Safe concurrent programming without variable-level race conditions

## Related
- **pattern-matching-mechanism** -- The mechanism that enforces single assignment

# Common Errors

- **Error**: Attempting to rebind a variable: `X = 1, X = 2`
  **Correction**: Use a new variable name: `X = 1, Y = 2`, or if transforming: `X1 = f(X)`

# Common Confusions

- **Confusion**: Thinking `X = X + 1` increments `X` as in imperative languages
  **Clarification**: This always fails in Erlang because `X` is already bound and `X + 1` produces a different value. Use a new name: `Y = X + 1`

# Source Reference

"Expressions" chapter, section "Variables", statement on single assignment. Also demonstrated in the "Pattern Matching" chapter examples.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: HIGH -- explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
