---
# === CORE IDENTIFICATION ===
concept: Spec Overloading
slug: spec-overloading

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: type-annotations
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Specifications for Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "overloaded spec"
  - "multi-clause spec"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-specification
extends:
  - function-specification
related:
  - type-variables-in-specs
  - when-constraint
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
---

# Quick Definition
A function specification can be overloaded by providing multiple type clauses separated by semicolons, each describing a different combination of argument and return types.

# Core Definition
"A function specification can be overloaded. That is, it can have several types, separated by a semicolon (`;`)." However, "a current restriction, which currently results in a warning by Dialyzer, is that the domains of the argument types cannot overlap" (Erlang Reference Manual, "Specifications for Functions").

# Prerequisites
- **function-specification** -- Overloading extends basic spec syntax

# Key Properties
1. Multiple clauses are separated by `;`
2. Each clause has its own argument types and return type
3. Argument type domains should not overlap (Dialyzer warns if they do)
4. Different type variables should be used in different clauses to avoid confusion

# Construction / Recognition
## To Construct:
1. Write the first spec clause
2. End it with `;` instead of `.`
3. Write the next clause indented, starting with `(`
4. End the last clause with `.`

## To Identify/Recognize:
1. A `-spec` with `;` separating multiple clauses
2. Multiple `(...) -> Type` patterns in one spec

# Context & Application
Overloaded specs model Erlang functions that behave differently depending on argument types -- a common pattern given Erlang's pattern-matching-based dispatch. They allow Dialyzer to infer more precise return types based on the specific argument types at each call site.

# Examples
**Example 1** (Specifications for Functions):
```erlang
-spec foo(T1, T2) -> T3;
         (T4, T5) -> T6.
```

**Example 2** (Specifications for Functions):
This produces a Dialyzer warning because domains overlap:
```erlang
-spec foo(pos_integer()) -> pos_integer();
         (integer()) -> integer().
```

**Example 3** (Specifications for Functions):
Using different type variables per clause:
```erlang
-spec foo({X, integer()}) -> X when X :: atom();
         ([Y]) -> Y when Y :: number().
```

# Relationships
## Builds Upon
- **function-specification** -- Extends basic spec with multiple clauses

## Enables
More precise type analysis for multi-clause functions.

## Related
- **type-variables-in-specs** -- Each clause can use its own type variables
- **when-constraint** -- Constraints are scoped to individual clauses

## Contrasts With
None within this source.

# Common Errors
- **Error**: Overlapping argument type domains between clauses
  **Correction**: Ensure each clause handles a distinct set of argument types; Dialyzer warns about overlaps

- **Error**: Reusing the same type variable names across clauses
  **Correction**: Use different variable names per clause to avoid confusion, e.g., `X` in one, `Y` in another

# Common Confusions
- **Confusion**: Thinking overloaded specs are matched in order like function clauses
  **Clarification**: Overloaded spec clauses should have non-overlapping domains; they are not tried in sequence

# Source Reference
"Types and Function Specifications" chapter, section "Specifications for Functions."

# Verification Notes
- Definition source: Direct from source text with examples
- Confidence rationale: High -- explicit definition and restriction documented
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
