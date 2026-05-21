---
# === CORE IDENTIFICATION ===
concept: Dynamic Type
slug: dynamic-type

# === CLASSIFICATION ===
category: data-types
subcategory: type-primitives
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Types and their Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gradual type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
  - any-type
extends: []
related:
  - type-lattice
contrasts_with:
  - any-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
  - "How does the type specification system relate to Dialyzer?"
---

# Quick Definition
`dynamic()` is a special type for gradual typing that represents a statically unknown type. Dialyzer treats it the same as `any()` for success typing purposes.

# Core Definition
"To facilitate gradual typing of Erlang, the type `dynamic()` is provided. The type `dynamic()` represents a statically unknown type. It is similar to Any in Python, any in TypeScript and dynamic in Hack." Furthermore, "`any()` and `dynamic()` interact with success typing the same way, so Dialyzer doesn't distinguish between them" (Erlang Reference Manual, "Types and their Syntax"). Unlike all other types, `dynamic()` is excluded from the type lattice.

# Prerequisites
- **erlang-type-language** -- `dynamic()` is part of the type language
- **any-type** -- Understanding `any()` is needed to understand the distinction

# Key Properties
1. Represents a statically unknown type
2. Designed for gradual typing support
3. Excluded from the type lattice (does not participate in the subtype hierarchy)
4. Dialyzer does not distinguish between `dynamic()` and `any()` for success typing
5. Analogous to Python's `Any`, TypeScript's `any`, and Hack's `dynamic`

# Construction / Recognition
## To Use:
1. Write `dynamic()` in a type position where the type is statically unknown

## To Identify/Recognize:
1. Explicit `dynamic()` in type expressions
2. Used in contexts where gradual typing is being adopted

# Context & Application
`dynamic()` exists to support incremental adoption of type annotations in Erlang codebases. It communicates that a type is intentionally unspecified, as opposed to `any()` which represents "can be any term." In practice, current Dialyzer treats them identically.

# Examples
**Example 1** (Types and their Syntax):
`dynamic()` is listed in the type grammar alongside `any()` and `none()`:
```text
Type :: any()       %% The top type, the set of all Erlang terms
      | none()      %% The bottom type, contains no terms
      | dynamic()
      ...
```

# Relationships
## Builds Upon
- **erlang-type-language** -- Part of the predefined types

## Enables
Gradual typing adoption in Erlang codebases.

## Related
- **type-lattice** -- `dynamic()` is the one type excluded from the lattice

## Contrasts With
- **any-type** -- Semantically different (unknown vs. all terms) but treated identically by Dialyzer

# Common Errors
- **Error**: Expecting Dialyzer to produce different results for `dynamic()` vs `any()`
  **Correction**: Dialyzer currently treats them identically for success typing

# Common Confusions
- **Confusion**: Thinking `dynamic()` disables type checking
  **Clarification**: `dynamic()` marks a type as unknown for gradual typing purposes; Dialyzer still performs analysis

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax."

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit definition and explanation
- Uncertainties: Future tooling may distinguish `dynamic()` from `any()`
- Cross-reference status: All slugs verified against planned cards
