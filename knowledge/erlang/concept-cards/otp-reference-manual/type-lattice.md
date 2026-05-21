---
# === CORE IDENTIFICATION ===
concept: Type Lattice
slug: type-lattice

# === CLASSIFICATION ===
category: data-types
subcategory: type-theory
tier: advanced

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
  - "subtype lattice"
  - "type hierarchy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - predefined-types
  - type-union
  - any-type
  - none-type
extends: []
related:
  - dynamic-type
  - singleton-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
  - "How does the type specification system relate to Dialyzer?"
---

# Quick Definition
All Erlang types except `dynamic()` form a lattice, with `any()` as the top element (set of all terms) and `none()` as the bottom element (empty set), connected by subtype relationships.

# Core Definition
"Because of subtype relations that exist between types, all types, except `dynamic()`, form a lattice where the top-most element, `any()`, denotes the set of all Erlang terms and the bottom-most element, `none()`, denotes the empty set of terms" (Erlang Reference Manual, "Types and their Syntax"). This lattice structure means that for any two types, there exists a least upper bound (their union) and a greatest lower bound (their intersection), which governs how Dialyzer reasons about type compatibility and subtype absorption in unions.

# Prerequisites
- **predefined-types** -- The lattice is composed of predefined types
- **type-union** -- Unions correspond to joins in the lattice
- **any-type** -- Top element of the lattice
- **none-type** -- Bottom element of the lattice

# Key Properties
1. `any()` is the top element -- the set of all Erlang terms
2. `none()` is the bottom element -- the empty set of terms
3. `dynamic()` is excluded from the lattice (exists outside the subtype hierarchy)
4. Subtype absorption in unions follows from lattice structure
5. Every type is a subtype of `any()` and a supertype of `none()`
6. Singleton types (e.g., `'foo'`, `42`) are subtypes of their corresponding base types (`atom()`, `integer()`)

# Construction / Recognition
## To Identify/Recognize:
1. The lattice is implicit -- it is the theoretical structure that governs type relationships
2. When Dialyzer reports type errors, it is reasoning about positions in this lattice
3. Subtype absorption in unions (e.g., `atom() | 'foo'` simplifying to `atom()`) is a lattice operation

# Context & Application
The lattice structure is the theoretical foundation for Dialyzer's type inference and checking. Understanding it explains why certain type unions simplify, why `any()` accepts everything, and why `none()` represents impossible values. It also explains how success typing works -- Dialyzer computes the least restrictive type (closest to `any()`) that is consistent with all observed uses.

# Examples
**Example 1** (Types and their Syntax):
```text
atom() | 'bar' | integer() | 42
```
Simplifies to `atom() | integer()` because `'bar'` is below `atom()` in the lattice and `42` is below `integer()`.

# Relationships
## Builds Upon
- **any-type** -- Top of the lattice
- **none-type** -- Bottom of the lattice
- **predefined-types** -- Nodes in the lattice

## Enables
- **function-specification** -- Dialyzer uses the lattice for spec checking

## Related
- **dynamic-type** -- Exists outside the lattice
- **singleton-types** -- Lowest non-bottom nodes in the lattice

## Contrasts With
None within this source.

# Common Errors
- **Error**: Assuming `dynamic()` participates in the subtype lattice like other types
  **Correction**: `dynamic()` is explicitly excluded from the lattice; it exists for gradual typing

# Common Confusions
- **Confusion**: Thinking the lattice imposes runtime type checks
  **Clarification**: The lattice is a theoretical structure used by static analysis tools like Dialyzer, not enforced at runtime

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax."

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition of lattice structure
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
