---
# === CORE IDENTIFICATION ===
concept: When Constraint
slug: when-constraint

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
  - "subtype constraint"
  - "bounded quantification"
  - "type guard"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-specification
  - type-variables-in-specs
extends:
  - type-variables-in-specs
related:
  - spec-overloading
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
---

# Quick Definition
The `when` clause in a spec provides subtype constraints on type variables, using the syntax `when X :: Type` to bound a type variable to a specific type (read as "X is a subtype of Type").

# Core Definition
Type variables in specs "can be constrained by guard-like subtype constraints and provide bounded quantification." The syntax is `-spec id(X) -> X when X :: tuple().` where "`::` constraint (read as 'is a subtype of') is the only guard constraint that can be used in the `when` part of a `-spec` attribute." The scope of a constraint "is the `(...) -> RetType` specification after which it appears" (Erlang Reference Manual, "Specifications for Functions").

# Prerequisites
- **function-specification** -- `when` constraints appear in specs
- **type-variables-in-specs** -- Constraints bound type variables

# Key Properties
1. Syntax: `when Var :: Type`
2. `::` is read as "is a subtype of"
3. `::` is currently the only guard constraint available in `when`
4. The constraint's scope is the spec clause after which it appears
5. In overloaded specs, each clause has its own `when` scope

# Construction / Recognition
## To Construct:
1. Write a spec with type variables
2. Add `when` after the return type
3. List constraints as `Var :: Type`
4. Example: `-spec id(X) -> X when X :: tuple().`

## To Identify/Recognize:
1. `when` keyword after the return type in a spec
2. Followed by `Variable :: Type` constraints

# Context & Application
`when` constraints enable bounded polymorphism in function specs. Without them, a type variable like `X` accepts any type. With `when X :: tuple()`, the function is constrained to accept and return only tuples. This provides more precise type information for Dialyzer analysis.

# Examples
**Example 1** (Specifications for Functions):
```erlang
-spec id(X) -> X when X :: tuple().
```
This constrains the identity function to work only with tuples.

**Example 2** (Specifications for Functions):
With overloaded specs, use different variables per clause:
```erlang
-spec foo({X, integer()}) -> X when X :: atom();
         ([Y]) -> Y when Y :: number().
```

# Relationships
## Builds Upon
- **type-variables-in-specs** -- Constraints bound the type variables
- **function-specification** -- Constraints appear in spec syntax

## Enables
Bounded polymorphism in function specifications.

## Related
- **spec-overloading** -- Each overloaded clause has its own constraint scope

## Contrasts With
None within this source.

# Common Errors
- **Error**: Reusing the same variable name in different overloaded clause constraints
  **Correction**: The source suggests using "different variables in different constituents of an overloaded contract" to avoid confusion

# Common Confusions
- **Confusion**: Thinking `when X :: tuple()` means X IS a tuple (equality)
  **Clarification**: `::` means "is a subtype of" -- X can be any subtype of `tuple()`, including specific tuple types like `{atom(), integer()}`

# Source Reference
"Types and Function Specifications" chapter, section "Specifications for Functions."

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit syntax and semantics
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
