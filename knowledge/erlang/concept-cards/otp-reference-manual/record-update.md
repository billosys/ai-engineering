---
# === CORE IDENTIFICATION ===
concept: Record Update
slug: record-update

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
section: "Updating Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record modification"
  - "functional record update"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - record-creation
extends: []
related:
  - record-field-access
  - record-patterns
contrasts_with:
  - native-record-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I change a field value in a record?"
  - "Does record update modify the original record?"
  - "What happens to fields I don't mention in a record update?"
---

# Quick Definition
Record update creates a copy of an existing record with specified fields changed, using the syntax `Expr#Name{Field1=Expr1, ..., FieldK=ExprK}`. Unmentioned fields retain their old values.

# Core Definition
The Erlang Reference Manual states that `Expr#Name{Field1=Expr1, ..., FieldK=ExprK}` where "`Expr` is to evaluate to a `Name` record. A copy of this record is returned, with the value of each specified field `FieldI` changed to the value of evaluating the corresponding expression `ExprI`. All other fields retain their old values." (Records, "Updating Records" section).

# Prerequisites
- **record-definition** -- The record type must be defined
- **record-creation** -- A record instance must exist to be updated

# Key Properties
1. Syntax: `Expr#Name{Field1=Expr1, ..., FieldK=ExprK}`
2. Returns a copy with specified fields changed; the original is unmodified
3. Fields not mentioned retain their old values
4. The expression must evaluate to a record of the specified type
5. This is functional update -- records are immutable values

# Construction / Recognition
## To Update:
1. Start with an expression evaluating to a record
2. Append `#RecordName{FieldName=NewValue, ...}`
3. Only list the fields you want to change

## To Recognize:
1. Look for `Expr#Name{...}` where `Expr` is a variable or expression (not empty) and the braces contain field assignments

# Context & Application
Record update is the standard way to produce a modified version of a record in Erlang's immutable data model. It is heavily used in `gen_server` handle functions to evolve process state. Since records are immutable, the "update" always returns a new value rather than mutating the existing one.

# Examples
**Example 1**: Updating a single field (inferred from syntax description):
```erlang
-record(person, {name, phone, address}).

update_phone(Person, NewPhone) ->
    Person#person{phone=NewPhone}.
```

# Relationships
## Builds Upon
- **record-definition** -- Field names are resolved from the definition
- **record-creation** -- A record must exist before it can be updated

## Enables
- **nested-records** -- Nested update chains allow updating deeply nested fields

## Related
- **record-field-access** -- Similar syntax but reads rather than writes
- **record-patterns** -- Pattern matching can extract values for use in updates

## Contrasts With
- **native-record-update** -- Native record update uses the captured definition from construction time, not the current module definition

# Common Errors
- **Error**: Expecting the original record to be modified in place
  **Correction**: Record update returns a new copy. Bind the result to a variable to use the updated record.

- **Error**: Using update syntax on a value that is not the expected record type
  **Correction**: Ensure the expression evaluates to the correct record type or a runtime error will occur.

# Common Confusions
- **Confusion**: Confusing record creation (`#Name{...}`) with record update (`Expr#Name{...}`)
  **Clarification**: Creation starts with `#Name` (no preceding expression). Update is preceded by an expression that evaluates to an existing record.

# Source Reference
Records chapter, "Updating Records" section.

# Verification Notes
- Definition source: Direct quote from source text
- Confidence rationale: High -- explicit definition
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
