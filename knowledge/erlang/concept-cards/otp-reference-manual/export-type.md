---
# === CORE IDENTIFICATION ===
concept: Export Type
slug: export-type

# === CLASSIFICATION ===
category: data-types
subcategory: user-defined-types
tier: intermediate

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
  - "-export_type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
extends: []
related:
  - remote-types
  - export-attribute
  - opaque-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a module's export attribute relate to its API design?"
---

# Quick Definition
The `-export_type` attribute declares which user-defined types in a module are visible to other modules, enabling them to be used as remote types.

# Core Definition
"A module can export some types to declare that other modules are allowed to refer to them as remote types. This declaration has the following form: `-export_type([T1/A1, ..., Tk/Ak]).`" where "the `Ti`s are atoms (the name of the type) and the `Ai`s are their arities" (Erlang Reference Manual, "Type Declarations of User-Defined Types"). It is not allowed to refer to types that are not declared as exported.

# Prerequisites
- **type-declaration** -- Only declared types can be exported

# Key Properties
1. Syntax: `-export_type([Name1/Arity1, ..., NameN/ArityN]).`
2. Exported types can be referenced as remote types from other modules
3. Non-exported types cannot be referenced from other modules
4. Opaque types should always be exported (they do not make sense as module-local)

# Construction / Recognition
## To Construct:
1. Declare a type with `-type`, `-opaque`, or `-nominal`
2. Add `-export_type([TypeName/Arity]).` to the module
3. Example: `-export_type([my_struct_type/0, orddict/2]).`

## To Identify/Recognize:
1. Lines beginning with `-export_type` in module source
2. Contains a list of `Name/Arity` pairs

# Context & Application
Exporting types is essential for API design in Erlang modules. It makes types part of the module's public interface, allowing other modules and Dialyzer to reference them. Opaque types must be exported since their purpose is to define an interface for external consumers while hiding internal structure.

# Examples
**Example 1** (Type Declarations of User-Defined Types):
```erlang
-export_type([my_struct_type/0, orddict/2]).
```

# Relationships
## Builds Upon
- **type-declaration** -- Exports declared types

## Enables
- **remote-types** -- Exported types can be used as remote types

## Related
- **export-attribute** -- Analogous to function exports (`-export`)
- **opaque-type** -- Opaque types should always be exported

## Contrasts With
None within this source.

# Common Errors
- **Error**: Defining an opaque type without exporting it
  **Correction**: Opaque types "do not make much sense as module local" and "are always to be exported"

- **Error**: Trying to reference a type from another module that is not exported
  **Correction**: The referenced type must appear in the defining module's `-export_type` list

# Common Confusions
- **Confusion**: Conflating `-export` (functions) with `-export_type` (types)
  **Clarification**: They serve parallel purposes but for different namespaces. Functions are exported with `-export`, types with `-export_type`

# Source Reference
"Types and Function Specifications" chapter, section "Type Declarations of User-Defined Types."

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit syntax and rules
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
