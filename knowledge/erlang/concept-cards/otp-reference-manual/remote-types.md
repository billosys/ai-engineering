---
# === CORE IDENTIFICATION ===
concept: Remote Types
slug: remote-types

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
  - "cross-module types"
  - "qualified types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - export-type
extends: []
related:
  - parameterized-types
  - opaque-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
---

# Quick Definition
A remote type is a type defined in and exported by one module that is referenced from another module using the syntax `Module:TypeName(Args)`.

# Core Definition
Remote types are "type defined in, and exported by, other modules" (Erlang Reference Manual, "Type Declarations of User-Defined Types"). The syntax for referencing a remote type is `Module:TypeName()` or `Module:TypeName(Arg1, ..., ArgN)` for parameterized types. The referenced type must be exported from the defining module via `-export_type`.

# Prerequisites
- **type-declaration** -- Remote types are declared with `-type`, `-opaque`, or `-nominal`
- **export-type** -- The type must be exported to be used remotely

# Key Properties
1. Syntax: `Module:TypeName()` or `Module:TypeName(Arg1, ..., ArgN)`
2. The referenced type must be exported from the defining module
3. It is not allowed to refer to types that are not declared as exported
4. Remote types enable cross-module type sharing and API contracts

# Construction / Recognition
## To Construct:
1. Define and export a type in the source module
2. Reference it from another module as `Module:TypeName()`

## To Identify/Recognize:
1. Type expressions containing a module prefix and colon, e.g., `mod:my_type()`
2. Appears in `-spec`, `-type`, or record declarations

# Context & Application
Remote types are critical for building APIs across module boundaries. They allow a library to define and export types that consumers reference in their own specs. This is especially important for opaque types, which must be exported and accessed remotely.

# Examples
**Example 1** (Type Declarations of User-Defined Types):
Assuming types are exported from module `mod`:
```erlang
-export_type([my_struct_type/0, orddict/2]).
```
They can be used from other modules:
```erlang
mod:my_struct_type()
mod:orddict(atom(), term())
```

# Relationships
## Builds Upon
- **export-type** -- Only exported types can be used remotely
- **type-declaration** -- Remote types reference declared types

## Enables
Cross-module type contracts and API design.

## Related
- **parameterized-types** -- Remote types can be parameterized
- **opaque-type** -- Opaque types are always accessed as remote types

## Contrasts With
None within this source.

# Common Errors
- **Error**: Referencing a type that is not exported from the other module
  **Correction**: Ensure the type is listed in `-export_type` in the defining module

# Common Confusions
- **Confusion**: Thinking remote types carry runtime overhead
  **Clarification**: Remote type references are purely compile-time/analysis-time constructs with no runtime cost

# Source Reference
"Types and Function Specifications" chapter, section "Type Declarations of User-Defined Types."

# Verification Notes
- Definition source: Direct from source text with examples
- Confidence rationale: High -- explicit definition and syntax
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
