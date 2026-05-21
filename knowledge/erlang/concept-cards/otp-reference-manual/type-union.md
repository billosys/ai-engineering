---
# === CORE IDENTIFICATION ===
concept: Type Union
slug: type-union

# === CLASSIFICATION ===
category: data-types
subcategory: type-composition
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
  - "union type"
  - "type alternatives"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
extends: []
related:
  - predefined-types
  - singleton-types
  - type-lattice
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
  - "How do I write a type specification for a function?"
---

# Quick Definition
A type union combines two or more types with the `|` operator, describing the set of terms belonging to any of the constituent types. Subtypes are absorbed by their supertypes in a union.

# Core Definition
Types in Erlang are "built using unions of either predefined types or singleton types." The syntax is `Type1 | Type2`. A key property is subtype absorption: "In a type union between a type and one of its subtypes, the subtype is absorbed by the supertype. Thus, the union is then treated as if the subtype was not a constituent of the union" (Erlang Reference Manual, "Types and their Syntax").

# Prerequisites
- **erlang-type-language** -- Type unions are the primary composition mechanism in the type language

# Key Properties
1. Syntax: `Type1 | Type2`
2. Subtypes are absorbed by supertypes in a union
3. Unions can combine predefined types, singleton types, and user-defined types
4. The union `atom() | 'bar' | integer() | 42` is equivalent to `atom() | integer()` due to absorption

# Construction / Recognition
## To Construct:
1. Write the first type
2. Add `|` as separator
3. Write the second type
4. Repeat for additional types

## To Identify/Recognize:
1. Look for the `|` operator between type expressions
2. Appears in `-type`, `-spec`, and record field type annotations

# Context & Application
Type unions are fundamental to Erlang's type system. Nearly every non-trivial type specification uses unions to express alternatives. For example, a function that returns either an ok-tuple or an error-tuple uses a union: `{ok, Result} | {error, Reason}`.

# Examples
**Example 1** (Types and their Syntax):
```text
atom() | 'bar' | integer() | 42
```
This describes the same set of terms as:
```text
atom() | integer()
```
Because `'bar'` is absorbed by `atom()` and `42` is absorbed by `integer()`.

# Relationships
## Builds Upon
- **erlang-type-language** -- Unions are a core construct of the type language

## Enables
- **function-specification** -- Specs use unions to express alternative argument/return types
- **type-declaration** -- User-defined types are often defined as unions

## Related
- **singleton-types** -- Singleton types are often union constituents
- **type-lattice** -- Union semantics are governed by the subtype lattice

## Contrasts With
None within this source.

# Common Errors
- **Error**: Including a subtype alongside its supertype and expecting distinct treatment
  **Correction**: Subtypes are absorbed by supertypes in unions; `atom() | 'foo'` is just `atom()`

# Common Confusions
- **Confusion**: Thinking union order matters for type semantics
  **Clarification**: The order of types in a union does not affect the set of terms it describes (though map association order matters for overlap resolution)

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax."

# Verification Notes
- Definition source: Direct from source text on union syntax and subtype absorption
- Confidence rationale: High -- explicit definition with examples
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
