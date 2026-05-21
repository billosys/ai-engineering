---
# === CORE IDENTIFICATION ===
concept: Record Field Access
slug: record-field-access

# === CLASSIFICATION ===
category: data-types
subcategory: records
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Accessing Record Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record dot notation"
  - "record field retrieval"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - record-creation
extends: []
related:
  - record-update
  - record-field-position
  - record-in-guards
contrasts_with:
  - native-record-field-access

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I get the value of a specific field from a record?"
  - "What does the Expr#Name.Field syntax mean?"
---

# Quick Definition
Record field access uses the syntax `Expr#Name.Field` to return the value of a specific field from a record. The expression `Expr` must evaluate to a record of type `Name`.

# Core Definition
The Erlang Reference Manual specifies that `Expr#Name.Field` "returns the value of the specified field. `Expr` is to evaluate to a `Name` record." This is the primary mechanism for reading individual fields from a tuple-based record (Records, "Accessing Record Fields" section).

# Prerequisites
- **record-definition** -- The record type must be defined to access its fields
- **record-creation** -- A record instance must exist to access its fields

# Key Properties
1. Syntax: `Expr#Name.Field`
2. `Expr` must evaluate to a record of type `Name`
3. Returns the value stored in the specified `Field`
4. This is a compile-time transformation to `element/2` on the underlying tuple

# Construction / Recognition
## To Access a Field:
1. Start with an expression that evaluates to a record
2. Append `#RecordName.FieldName`

## To Recognize:
1. Look for the `Expr#Name.Field` pattern -- an expression followed by `#`, a record name, a dot, and a field name

# Context & Application
Field access is the most common record operation. Since records compile to tuples, field access compiles to an `element/2` call with the position computed at compile time. This makes field access efficient and type-safe at compile time, though no runtime type checking occurs.

# Examples
**Example 1** (Accessing Record Fields section):
```erlang
-record(person, {name, phone, address}).

get_person_name(Person) ->
    Person#person.name.
```

# Relationships
## Builds Upon
- **record-definition** -- Field names are resolved from the definition
- **record-creation** -- A record must be created before its fields can be accessed

## Enables
- **record-in-guards** -- Field access is allowed in guard expressions
- **nested-records** -- Nested field access chains multiple accesses

## Related
- **record-field-position** -- Related syntax `#Name.Field` returns the field's tuple position
- **record-update** -- Similar syntax but modifies rather than reads

## Contrasts With
- **native-record-field-access** -- Native records use the same dot syntax but operate on a distinct type, not tuples

# Common Errors
- **Error**: Accessing a field on a value that is not the expected record type
  **Correction**: Ensure the expression evaluates to the correct record type. A runtime `badrecord` error will occur if the tuple tag does not match.

# Common Confusions
- **Confusion**: Confusing `Expr#Name.Field` (value access) with `#Name.Field` (position access)
  **Clarification**: With an expression prefix, you get the field value. Without, you get the integer position of the field in the underlying tuple.

# Source Reference
Records chapter, "Accessing Record Fields" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit syntax and semantics
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
