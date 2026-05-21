---
# === CORE IDENTIFICATION ===
concept: Singleton Types
slug: singleton-types

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
  - "literal types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
extends: []
related:
  - predefined-types
  - type-union
  - type-lattice
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
Singleton types are types containing exactly one value, allowed for integers and atoms. Examples include `42`, `-1`, `'foo'`, and `'bar'`.

# Core Definition
"For integers and atoms, it is allowed for singleton types; for example, the integers `-1` and `42`, or the atoms `'foo'` and `'bar'`" (Erlang Reference Manual, "Types and their Syntax"). Singleton types are subtypes of their corresponding base types (`atom()` or `integer()`) and are absorbed when unioned with the base type.

# Prerequisites
- **erlang-type-language** -- Singleton types are basic elements of the type language

# Key Properties
1. Only allowed for integers and atoms
2. A singleton integer type is a specific integer value, e.g., `42`
3. A singleton atom type is a specific atom, e.g., `'ok'`
4. Singleton types are subtypes of their parent types (`'foo'` is a subtype of `atom()`)
5. Integer ranges (`1..100`) are built from singleton integer types
6. Integer expressions using binary/unary operators can define singleton types

# Construction / Recognition
## To Construct:
1. For atoms: use the atom literal in quotes, e.g., `'ok'`, `'error'`
2. For integers: use the integer literal, e.g., `42`, `-1`
3. For integer expressions: use arithmetic, e.g., `1 + 2`

## To Identify/Recognize:
1. A literal atom or integer appearing in a type position
2. Used extensively in tagged-tuple patterns like `{'ok', Result} | {'error', Reason}`

# Context & Application
Singleton types are essential for expressing Erlang's ubiquitous tagged tuples. Without them, you could not type `{ok, Value} | {error, Reason}` -- the `ok` and `error` atoms are singleton types that distinguish the two tuple variants.

# Examples
**Example 1** (Types and their Syntax):
```text
atom() | 'bar' | integer() | 42
```
Here `'bar'` and `42` are singleton types. The union simplifies to `atom() | integer()` because singleton types are absorbed by their parent types.

# Relationships
## Builds Upon
- **erlang-type-language** -- Part of the type language primitives

## Enables
- **type-union** -- Singleton types are commonly combined in unions
- **function-specification** -- Tagged-tuple return types use singleton atoms

## Related
- **predefined-types** -- Singleton types are subtypes of predefined types
- **type-lattice** -- Singleton types sit near the bottom of the lattice

## Contrasts With
None within this source.

# Common Errors
- **Error**: Trying to create singleton types for floats or other non-atom, non-integer values
  **Correction**: Singleton types are only allowed for integers and atoms

# Common Confusions
- **Confusion**: Thinking `'ok'` in a type spec is different from the atom `ok`
  **Clarification**: `'ok'` in a type specification denotes the singleton type containing only the atom `ok`

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax."

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicitly defined with examples
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
