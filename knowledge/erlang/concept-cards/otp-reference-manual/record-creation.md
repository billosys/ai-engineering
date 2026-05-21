---
# === CORE IDENTIFICATION ===
concept: Record Creation
slug: record-creation

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
section: "Creating Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record construction"
  - "record instantiation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
extends: []
related:
  - record-update
  - record-patterns
  - record-field-access
contrasts_with:
  - native-record-construction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a new record instance in Erlang?"
  - "Can I omit fields when creating a record?"
  - "What does the _ = ExprL syntax do in record creation?"
---

# Quick Definition
A new record is created using the syntax `#Name{Field1=Expr1, ..., FieldK=ExprK}`. Fields can appear in any order and can be omitted, in which case they receive their default values.

# Core Definition
The Erlang Reference Manual states that the expression `#Name{Field1=Expr1, ..., FieldK=ExprK}` "creates a new `Name` record where the value of each field `FieldI` is the value of evaluating the corresponding expression `ExprI`." The fields can be given "in any order, not necessarily the same order as in the record definition, and fields can be omitted. Omitted fields get their respective default value instead." A special wildcard default syntax `#Name{Field1=Expr1, ..., FieldK=ExprK, _=ExprL}` assigns the value of `ExprL` to all omitted fields instead of their defined defaults (Records, "Creating Records" section).

# Prerequisites
- **record-definition** -- The record must be defined before it can be created

# Key Properties
1. Syntax: `#Name{Field1=Expr1, ..., FieldK=ExprK}`
2. Fields can appear in any order
3. Omitted fields receive their default values from the record definition
4. The wildcard default `_=ExprL` overrides default values for all unspecified fields
5. The wildcard default is primarily intended for ETS and Mnesia match functions

# Construction / Recognition
## To Create a Record:
1. Write `#` followed by the record name
2. Open curly braces `{`
3. List field assignments as `Field=Value`, separated by commas
4. Optionally use `_=Value` to set a default for all unspecified fields
5. Close with `}`

## To Recognize:
1. Look for `#RecordName{...}` syntax in expression context (not after another expression)

# Context & Application
Record creation is used whenever a new structured value is needed. The wildcard default (`_=ExprL`) is especially useful for creating match patterns for ETS and Mnesia queries, where unmatched fields should be set to `'_'` (the Mnesia/ETS wildcard). Fields can be set in any order, making code more readable when only a few fields need non-default values.

# Examples
**Example 1** (Creating Records section): Using wildcard default for ETS matching:
```erlang
-record(person, {name, phone, address}).

lookup(Name, Tab) ->
    ets:match_object(Tab, #person{name=Name, _='_'}).
```

**Example 2**: Creating a record with explicit field values:
```erlang
-record(person, {name, phone, address}).

new_person() ->
    #person{name="Joe", phone="555-1234", address="Stockholm"}.
```

# Relationships
## Builds Upon
- **record-definition** -- Must be defined before creation

## Enables
- **record-field-access** -- Once created, fields can be accessed
- **record-update** -- Created records can be updated

## Related
- **record-patterns** -- Pattern matching uses the same syntax as creation
- **record-internal-representation** -- The created value is a tagged tuple

## Contrasts With
- **native-record-construction** -- Native records require all fields without defaults to be given values; the `_=ExprL` wildcard syntax is not available

# Common Errors
- **Error**: Misspelling a field name in the creation expression
  **Correction**: The compiler will report an error. Verify field names match the record definition.

- **Error**: Forgetting that omitted fields get `undefined` by default (when no default was specified in the definition)
  **Correction**: Either provide explicit values or set appropriate defaults in the record definition.

# Common Confusions
- **Confusion**: Thinking the field order in creation must match the definition order
  **Clarification**: Fields can be given in any order during record creation.

# Source Reference
Records chapter, "Creating Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit syntax and semantics with examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
