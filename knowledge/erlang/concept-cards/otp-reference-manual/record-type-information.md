---
# === CORE IDENTIFICATION ===
concept: Record Type Information
slug: record-type-information

# === CLASSIFICATION ===
category: data-types
subcategory: type-annotations
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Type Information in Record Declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "typed records"
  - "record field types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - predefined-types
  - type-declaration
extends: []
related:
  - function-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
  - "What must I know before writing type specifications?"
---

# Quick Definition
Record fields can be annotated with types in their declaration using `field :: Type` syntax. Unannotated fields default to `any()`, and initial values must be compatible with their declared types.

# Core Definition
"The types of record fields can be specified in the declaration of the record" with the syntax `-record(rec, {field1 :: Type1, field2, field3 :: Type3}).` Fields without annotations default to `any()`. "In the presence of initial values for fields, the type must be declared after the initialization": `-record(rec, {field1 = [] :: Type1, field2, field3 = 42 :: Type3}).` "The initial values for fields are to be compatible with (that is, a member of) the corresponding types. This is checked by the compiler" (Erlang Reference Manual, "Type Information in Record Declarations").

# Prerequisites
- **predefined-types** -- Field types are expressed using the type language
- **type-declaration** -- Understanding type expressions is needed

# Key Properties
1. Syntax: `-record(rec, {field :: Type}).`
2. For native records: `-record #rec{field :: Type}.`
3. Unannotated fields default to `any()`
4. Initial values must come before type annotations: `field = Value :: Type`
5. The compiler checks initial value compatibility with declared types
6. Since OTP 19, `'undefined'` is no longer automatically added to field types for fields without initial values
7. Records can be used as types with `#rec{}` syntax
8. Record types can be refined: `#rec{some_field :: Type}`

# Construction / Recognition
## To Construct:
1. Define the record with typed fields: `-record(rec, {name :: string(), age :: pos_integer()}).`
2. For fields with defaults: `-record(rec, {name = "" :: string()}).`
3. Leave fields without types to default to `any()`

## To Identify/Recognize:
1. `::` in record field definitions
2. Record definitions with type annotations after field names or default values

# Context & Application
Typed records are the primary way to annotate structured data in Erlang. Dialyzer uses record field types to verify that record access and updates use compatible types. When using records with ETS/Mnesia match patterns, record field types may need special handling (adding `'_'` to the field type).

# Examples
**Example 1** (Type Information in Record Declarations):
```erlang
-record(rec, {field1 :: Type1, field2, field3 :: Type3}).
```
Equivalent to:
```erlang
-record(rec, {field1 :: Type1, field2 :: any(), field3 :: Type3}).
```

**Example 2** (Type Information in Record Declarations):
With initial values:
```erlang
-record(rec, {field1 = [] :: Type1, field2, field3 = 42 :: Type3}).
```

**Example 3** (Type Information in Record Declarations):
Handling ETS match patterns:
```erlang
-record(person, {name :: string(), height :: height() | '_'}).
-type person() :: #person{height :: height()}.
```

# Relationships
## Builds Upon
- **predefined-types** -- Field types use the type language
- **type-declaration** -- Record types can be used in type declarations

## Enables
- **function-specification** -- Specs reference record types

## Related
- **function-specification** -- Specs often use record types in arguments/return types

## Contrasts With
None within this source.

# Common Errors
- **Error**: Placing type annotation before the initial value
  **Correction**: Initial value must come first: `field = Value :: Type`, not `field :: Type = Value`

- **Error**: Assuming `'undefined'` is automatically added to field types (pre-OTP 19 behavior)
  **Correction**: Since OTP 19, if you need `'undefined'` in your field type, you must add it explicitly

# Common Confusions
- **Confusion**: Thinking `#rec{}` and `rec()` are interchangeable type notations
  **Clarification**: `#rec{}` is the record-as-type syntax; `rec()` would be a separate user-defined type. The source recommends defining a `person()` type and preferring it over `#person{}`

# Source Reference
"Types and Function Specifications" chapter, section "Type Information in Record Declarations."

# Verification Notes
- Definition source: Direct from source text with multiple examples
- Confidence rationale: High -- explicit syntax, rules, and examples
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
