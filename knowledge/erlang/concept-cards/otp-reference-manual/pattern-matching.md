---
# === CORE IDENTIFICATION ===
concept: Pattern Matching
slug: pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Pattern Matching"
chapter_number: null
pdf_page: null
section: "Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "matching"
  - "destructuring"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - match-operator
  - case-expression
  - variables
  - function-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is pattern matching in Erlang?"
  - "How are variables bound to values in Erlang?"
  - "What happens when pattern matching fails?"
---

# Quick Definition

Pattern matching is the mechanism by which variables are bound to values in Erlang. A left-hand side pattern is matched against a right-hand side term; if the match succeeds, unbound variables in the pattern become bound; if it fails, an exception is raised.

# Core Definition

The Erlang Reference Manual states: "Variables are bound to values through the _pattern matching_ mechanism. Pattern matching occurs when evaluating the `case`, `receive`, `try`, and the match operator (`=`) expressions." Furthermore: "In pattern matching, a left-hand side pattern is matched against a right-hand side term. If the matching succeeds, any unbound variables in the pattern become bound. If the matching fails, an exception is raised." (Erlang Reference Manual, "Pattern Matching").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Pattern matching is the only way to bind variables to values in Erlang
2. Matching occurs in `case`, `receive`, `try`, and match operator (`=`) expressions
3. A pattern has the same structure as a term but can contain unbound variables
4. If matching succeeds, unbound variables in the pattern become bound
5. If matching fails, a runtime exception is raised
6. Already-bound variables in a pattern must match their current value (due to single assignment)

# Construction / Recognition

## To Construct/Create:
1. Write a pattern on the left-hand side of a match operator or in a clause head
2. Include unbound variables where values should be extracted
3. Use literal values where specific values are expected

## To Identify/Recognize:
1. The `=` operator with a pattern on the left
2. Clause heads in `case`, `receive`, `try`, or function declarations
3. Variables becoming bound after evaluation

# Context & Application

Pattern matching is the most fundamental operation in Erlang. It replaces assignment statements found in other languages, and is integral to function dispatch (selecting which clause to execute), data destructuring (extracting parts of complex terms), and control flow (case/receive expressions). Understanding pattern matching is essential for writing any Erlang code.

# Examples

**Example 1** (Pattern Matching section): Demonstrating variable binding and rebinding failure:
```erlang
1> X.
** 1:1: variable 'X' is unbound **
2> X = 2.
2
3> X + 1.
3
4> {X, Y} = {1, 2}.
** exception error: no match of right hand side value {1,2}
5> {X, Y} = {2, 3}.
{2,3}
6> Y.
3
```

In line 4, `X` is already bound to `2`, so matching against `{1, 2}` fails because `X` cannot match `1`. In line 5, `X` matches `2` (its bound value) and `Y` becomes bound to `3`.

# Relationships

## Enables
- **match-operator** -- The match operator (`=`) is one of the primary contexts where pattern matching occurs
- **case-expression** -- Case expressions use pattern matching to select branches
- **function-declaration** -- Function clause heads use pattern matching for dispatch
- **variables** -- Variables are bound through pattern matching

## Related
- **compound-pattern-operator** -- Extends basic patterns with simultaneous matching
- **patterns-in-expressions** -- Patterns appear in multiple expression contexts

# Common Errors

- **Error**: Attempting to re-bind an already bound variable to a different value
  **Correction**: Erlang uses single assignment; once a variable is bound, it can only match its current value. Use a new variable name or restructure the code.

# Common Confusions

- **Confusion**: Treating `=` as an assignment operator (as in imperative languages)
  **Clarification**: `=` is a match operator in Erlang. If the left side contains only an unbound variable, it behaves like assignment, but it can also assert equality when variables are already bound.

- **Confusion**: Expecting pattern matching failure to return a value like `false`
  **Clarification**: Pattern matching failure raises a runtime exception (such as `badmatch`), not a boolean result

# Source Reference

"Pattern Matching" chapter, section "Pattern Matching", with shell examples.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition and detailed examples in source
- Uncertainties: None
- Cross-reference status: Related slugs planned for extraction
