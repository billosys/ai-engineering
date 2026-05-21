---
# === CORE IDENTIFICATION ===
concept: Any Type
slug: any-type

# === CLASSIFICATION ===
category: data-types
subcategory: type-primitives
tier: foundational

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
  - "term()"
  - "top type"
  - "_"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
extends: []
related:
  - type-lattice
  - built-in-type-aliases
  - dynamic-type
contrasts_with:
  - none-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
`any()` is the top type in Erlang's type lattice, denoting the set of all Erlang terms. Its alias `term()` is commonly used, and the anonymous type variable `_` is equivalent.

# Core Definition
`any()` is defined as "The top type, the set of all Erlang terms" (Erlang Reference Manual, "Types and their Syntax"). It sits at the top of the type lattice, meaning every other type is a subtype of `any()`. The alias `term()` is a built-in convenience name for `any()`. The anonymous type variable `_` is also equivalent to `term()` or `any()` and can be used as a shorthand in specs.

# Prerequisites
- **erlang-type-language** -- `any()` is a fundamental element of the type language

# Key Properties
1. Denotes the set of all Erlang terms
2. Top element of the type lattice
3. `term()` is an alias for `any()`
4. `_` (anonymous type variable) is equivalent to `any()` in specs
5. Record fields without type annotations default to `any()`
6. `any()` and `dynamic()` interact with success typing the same way

# Construction / Recognition
## To Use:
1. Write `any()`, `term()`, or `_` in a type position
2. Omit the type annotation on a record field (defaults to `any()`)

## To Identify/Recognize:
1. Explicit `any()` or `term()` in type expressions
2. `_` used as a type in `-spec` attributes
3. Record fields without type annotations

# Context & Application
`any()` is used when a function accepts or returns any Erlang term without restriction. It is the default type for unannotated record fields and the implicit type when no spec is provided. Using `term()` is often preferred for readability.

# Examples
**Example 1** (Types and their Syntax):
```text
-spec Function(string(), _) -> string().
```
is equivalent to:
```text
-spec Function(string(), any()) -> string().
```

# Relationships
## Builds Upon
- **erlang-type-language** -- Fundamental predefined type

## Enables
- **type-lattice** -- Top element of the lattice
- **built-in-type-aliases** -- `term()` is an alias for `any()`

## Related
- **dynamic-type** -- Similar in practice but exists outside the lattice

## Contrasts With
- **none-type** -- `none()` is the bottom (empty set), `any()` is the top (all terms)

# Common Errors
- **Error**: Using `[]` or `[_]` interchangeably for "list of anything"
  **Correction**: `[_]` means `list(any())` (proper list of any elements); `[]` means only the empty list

# Common Confusions
- **Confusion**: Thinking `any()` and `dynamic()` are different in practice for Dialyzer
  **Clarification**: The source states that `any()` and `dynamic()` "interact with success typing the same way, so Dialyzer doesn't distinguish between them"

# Source Reference
"Types and Function Specifications" chapter, sections "Types and their Syntax" and "Specifications for Functions."

# Verification Notes
- Definition source: Direct from the type grammar and explanatory text
- Confidence rationale: High -- explicitly defined in grammar and discussed
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
