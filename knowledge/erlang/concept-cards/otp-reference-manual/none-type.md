---
# === CORE IDENTIFICATION ===
concept: None Type
slug: none-type

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
  - "bottom type"
  - "no_return()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
extends: []
related:
  - type-lattice
  - no-return-type
  - built-in-type-aliases
contrasts_with:
  - any-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
`none()` is the bottom type in Erlang's type lattice, denoting the empty set of terms. Its alias `no_return()` is used in specs for functions that never return normally.

# Core Definition
`none()` is defined as "The bottom type, contains no terms" (Erlang Reference Manual, "Types and their Syntax"). It is the bottom-most element of the type lattice, meaning it is a subtype of every other type. The alias `no_return()` is provided as a built-in convenience for specifying functions that do not return.

# Prerequisites
- **erlang-type-language** -- `none()` is a fundamental element of the type language

# Key Properties
1. Denotes the empty set of terms -- no value has type `none()`
2. Bottom element of the type lattice
3. Subtype of every other type
4. `no_return()` is a built-in alias for `none()`
5. Used in return position of specs for functions that throw exceptions, loop forever, or call `exit/1`

# Construction / Recognition
## To Use:
1. Write `none()` or `no_return()` in the return type position of a spec
2. Typically only used for function return types, not argument types

## To Identify/Recognize:
1. Explicit `none()` or `no_return()` in type expressions
2. Functions whose specs end with `-> no_return()`

# Context & Application
`none()` is primarily useful through its alias `no_return()` for documenting functions that never return normally -- server loops, exception throwers, and process terminators. It signals to Dialyzer and readers that the function's return value will never be used.

# Examples
**Example 1** (Specifications for Functions):
```erlang
my_error(Err) -> throw({error, Err}).
```
Recommended spec:
```text
-spec my_error(term()) -> no_return().
```

# Relationships
## Builds Upon
- **erlang-type-language** -- Fundamental predefined type

## Enables
- **type-lattice** -- Bottom element of the lattice
- **no-return-type** -- `no_return()` is the practical application of `none()`

## Related
- **built-in-type-aliases** -- `no_return()` is an alias for `none()`

## Contrasts With
- **any-type** -- `any()` is the top (all terms), `none()` is the bottom (no terms)

# Common Errors
- **Error**: Using `none()` for a function that might return in some code paths
  **Correction**: `none()` / `no_return()` means the function NEVER returns; use it only for functions that always throw, exit, or loop forever

# Common Confusions
- **Confusion**: Thinking `none()` means "no type specified" or "unknown type"
  **Clarification**: `none()` means "empty set of terms." For unknown/unspecified types, use `any()` or `term()`

# Source Reference
"Types and Function Specifications" chapter, sections "Types and their Syntax" and "Specifications for Functions."

# Verification Notes
- Definition source: Direct from the type grammar
- Confidence rationale: High -- explicitly defined in grammar and usage example
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
