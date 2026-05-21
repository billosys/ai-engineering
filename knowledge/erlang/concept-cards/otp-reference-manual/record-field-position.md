---
# === CORE IDENTIFICATION ===
concept: Record Field Position
slug: record-field-position

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
  - "record field index"
  - "record field offset"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - record-internal-representation
extends: []
related:
  - record-field-access
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I get the position of a field in a record's tuple representation?"
  - "What does #Name.Field return without an expression prefix?"
  - "How do I use records with lists:keyfind/3?"
---

# Quick Definition
The expression `#Name.Field` (without a preceding expression) returns the integer position of the specified field in the record's underlying tuple representation. This is useful with functions like `lists:keyfind/3` that require a tuple element position.

# Core Definition
The Erlang Reference Manual states that `#Name.Field` "returns the position of the specified field in the tuple representation of the record." This is distinct from `Expr#Name.Field`, which returns the field's value. The position is a 1-based integer index into the tuple, where position 1 is the record tag atom (Records, "Accessing Record Fields" section).

# Prerequisites
- **record-definition** -- The record must be defined to determine field positions
- **record-internal-representation** -- Understanding that records are tuples is essential to interpreting the position

# Key Properties
1. Syntax: `#Name.Field` (no preceding expression)
2. Returns an integer -- the 1-based position of the field in the tuple
3. Position 1 is always the record tag (the record name atom)
4. The first user-defined field is at position 2
5. This is a compile-time constant -- the compiler resolves it

# Construction / Recognition
## To Get a Field Position:
1. Write `#RecordName.FieldName` without any expression before the `#`

## To Recognize:
1. Look for `#Name.Field` at the start of an expression or as an argument -- no variable or expression preceding the `#`

# Context & Application
Field position access is primarily used with tuple-oriented functions such as `lists:keyfind/3`, `lists:keysort/2`, and `ets:new/2` (with `{keypos, Pos}` option). It provides a way to reference tuple positions symbolically rather than with magic numbers, keeping code maintainable even when fields are added or reordered.

# Examples
**Example 1** (Accessing Record Fields section): Using field position with lists:keyfind/3:
```erlang
-record(person, {name, phone, address}).

lookup(Name, List) ->
    lists:keyfind(Name, #person.name, List).
```

In this example, `#person.name` evaluates to `2` (the position of `name` in the underlying tuple `{person, Name, Phone, Address}`).

# Relationships
## Builds Upon
- **record-definition** -- Positions are derived from the field order in the definition
- **record-internal-representation** -- Positions refer to the underlying tuple structure

## Enables
No direct dependents within this extraction scope.

## Related
- **record-field-access** -- `Expr#Name.Field` returns the value; `#Name.Field` returns the position

## Contrasts With
No direct contrasts -- native records do not have an equivalent concept since they are not tuples.

# Common Errors
- **Error**: Using `#Name.Field` expecting a field value instead of a position
  **Correction**: To get a field value, use `Expr#Name.Field` with a record expression. Without an expression prefix, you get the integer position.

# Common Confusions
- **Confusion**: Confusing `#Name.Field` (position) with `Expr#Name.Field` (value)
  **Clarification**: The presence or absence of a preceding expression determines whether you get a position integer or a field value.

- **Confusion**: Expecting position 1 to be the first field
  **Clarification**: Position 1 is the record tag atom. The first field is at position 2.

# Source Reference
Records chapter, "Accessing Record Fields" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit example and explanation
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
