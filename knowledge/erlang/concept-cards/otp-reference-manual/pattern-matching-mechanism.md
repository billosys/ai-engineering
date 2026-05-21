---
# === CORE IDENTIFICATION ===
concept: Pattern Matching Mechanism
slug: pattern-matching-mechanism

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
  - "match semantics"
  - "binding mechanism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends:
  - pattern-matching
related:
  - variables
  - match-operator
  - single-assignment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does pattern matching work step by step in Erlang?"
  - "What happens when a bound variable appears in a pattern?"
  - "In what contexts does pattern matching occur?"
---

# Quick Definition

The pattern matching mechanism evaluates patterns against terms by recursively comparing structure and values. Unbound variables are bound on success; already-bound variables must match their current value; structural mismatches raise exceptions.

# Core Definition

Pattern matching in Erlang follows a specific mechanism: patterns have "the same structure as a term but can contain unbound variables" (Erlang Reference Manual, "Pattern Matching"). When a pattern is matched against a term, the runtime recursively compares structure. Unbound variables bind to the corresponding part of the term. Bound variables act as equality assertions -- they must match their current value. The matching contexts are explicitly enumerated: `case` expressions, `receive` expressions, `try` expressions, and the match operator (`=`) (Erlang Reference Manual, "Pattern Matching").

# Prerequisites

- **pattern-matching** -- The general concept of pattern matching must be understood before the mechanism details

# Key Properties

1. Patterns mirror the structure of terms but may contain unbound variables
2. Matching is recursive: compound terms (tuples, lists, maps) are matched element by element
3. Unbound variables bind to the corresponding value on successful match
4. Bound variables must exactly match their current value
5. Literal values in patterns must match the corresponding value in the term
6. Matching failure raises a runtime exception
7. Matching occurs in four specific contexts: `case`, `receive`, `try`, and `=`

# Construction / Recognition

## To Construct/Create:
1. Structure a pattern to mirror the expected shape of the term
2. Place unbound variables where values need to be extracted
3. Place bound variables or literals where specific values are expected

## To Identify/Recognize:
1. A match succeeds silently when all positions match
2. A match failure produces a runtime exception with the unmatched value
3. After a successful match, previously unbound variables have values

# Context & Application

The matching mechanism is the engine behind Erlang's functional dispatch and data destructuring. The fact that bound variables act as assertions (not rebinding) is a direct consequence of single assignment and enables defensive programming patterns where re-matching a variable verifies an expected value.

# Examples

**Example 1** (Pattern Matching section): Step-by-step matching demonstration:
```erlang
2> X = 2.       %% X is unbound, binds to 2
2
4> {X, Y} = {1, 2}.  %% X is bound to 2, cannot match 1
** exception error: no match of right hand side value {1,2}
5> {X, Y} = {2, 3}.  %% X matches 2 (bound), Y binds to 3
{2,3}
```

# Relationships

## Builds Upon
- **pattern-matching** -- This describes the detailed mechanism of the general concept

## Enables
- **function-evaluation** -- Function clause selection uses the matching mechanism
- **case-expression** -- Case branches are selected by pattern matching
- **match-operator** -- The match operator triggers the matching mechanism

## Related
- **single-assignment** -- Single assignment means bound variables assert rather than rebind
- **variables** -- Variables are the primary elements affected by matching

# Common Errors

- **Error**: Expecting a bound variable to rebind to a new value in a pattern
  **Correction**: In Erlang, a bound variable in a pattern asserts that the matched value equals the variable's current value. Use a fresh variable name to capture a new value.

# Common Confusions

- **Confusion**: Assuming pattern matching only extracts values (like destructuring in other languages)
  **Clarification**: Pattern matching both extracts values (via unbound variables) and asserts values (via bound variables and literals). This dual nature is central to Erlang's design.

# Source Reference

"Pattern Matching" chapter, section "Pattern Matching". The examples demonstrate the mechanism for both unbound and bound variable matching.

# Verification Notes

- Definition source: Synthesized from explicit statements and examples in source
- Confidence rationale: HIGH -- mechanism is clearly demonstrated through examples in source
- Uncertainties: None
- Cross-reference status: Related slugs planned for extraction
