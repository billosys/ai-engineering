---
# === CORE IDENTIFICATION ===
concept: Type Declaration
slug: type-declaration

# === CLASSIFICATION ===
category: data-types
subcategory: user-defined-types
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Type Declarations of User-Defined Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-type attribute"
  - "user-defined type"
  - "type alias"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
  - predefined-types
extends: []
related:
  - parameterized-types
  - export-type
  - remote-types
  - opaque-type
  - nominal-type
contrasts_with:
  - opaque-type
  - nominal-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
  - "How do I write a type specification for a function?"
---

# Quick Definition
A type declaration uses the `-type` attribute to define a named type as an alias for a type expression. The declared type uses structural equivalence -- two `-type` declarations with the same structure are considered the same type.

# Core Definition
"New types are declared using `-type`, `-opaque`, and `-nominal` attributes" (Erlang Reference Manual, "Type Declarations of User-Defined Types"). The syntax is `-type my_struct_type() :: Type.` where the type name is an atom followed by parentheses, and `Type` is any valid type expression. Types declared with `-type` use structural typing: "the Erlang compiler will ignore their type names" and "two types are seen as equivalent if their structures are the same" (Nominals chapter). A restriction is that `Type` can only contain predefined types or user-defined types that are either module-local (with a definition present in the module) or remote (defined in and exported by other modules).

# Prerequisites
- **erlang-type-language** -- Type declarations are part of the type language
- **predefined-types** -- Declared types are built from predefined types

# Key Properties
1. Syntax: `-type Name() :: Type.`
2. Uses structural typing -- two types with the same structure are equivalent regardless of name
3. Can only reference predefined types, module-local user types, or remote types
4. The compiler enforces that referenced module-local types exist (compilation error otherwise)
5. Type declarations can be parameterized with type variables

# Construction / Recognition
## To Construct:
1. Write `-type` followed by the type name with parentheses
2. Add `::` followed by the type expression
3. Terminate with a period
4. Example: `-type my_type() :: atom() | integer().`

## To Identify/Recognize:
1. Lines beginning with `-type` in module source
2. The name is an atom followed by `()`
3. The right-hand side is a type expression after `::`

# Context & Application
Type declarations are the primary mechanism for creating named, reusable type aliases in Erlang modules. They improve code readability, provide documentation, and enable Dialyzer to reason about program correctness. Since they use structural typing, they provide no nominal guarantees -- use `-opaque` or `-nominal` when name-based distinction is needed.

# Examples
**Example 1** (Type Declarations of User-Defined Types):
```erlang
-type my_struct_type() :: Type.
-opaque my_opaq_type() :: Type.
-nominal my_nominal_type() :: Type.
```

**Example 2** (Type Declarations of User-Defined Types):
```erlang
-type orddict(Key, Val) :: [{Key, Val}].
```
A parameterized type declaration.

# Relationships
## Builds Upon
- **predefined-types** -- User types are built from predefined types
- **erlang-type-language** -- Type declarations are core syntax

## Enables
- **parameterized-types** -- Type declarations can be parameterized
- **export-type** -- Declared types can be exported
- **function-specification** -- Specs reference user-defined types

## Related
- **remote-types** -- Types from other modules

## Contrasts With
- **opaque-type** -- `-opaque` hides internal structure from external modules
- **nominal-type** -- `-nominal` uses name-based equivalence instead of structural

# Common Errors
- **Error**: Referencing a type that is not defined in the current module or imported as a remote type
  **Correction**: The compiler enforces that referenced module-local types exist; define or import the type first

# Common Confusions
- **Confusion**: Thinking `-type` declarations create distinct types
  **Clarification**: `-type` creates structural aliases. `-type meter() :: integer()` and `-type foot() :: integer()` are equivalent types. Use `-nominal` for distinct types with the same structure

# Source Reference
"Types and Function Specifications" chapter, section "Type Declarations of User-Defined Types." Also see "Nominals" chapter for structural vs. nominal distinction.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit syntax and semantics
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
