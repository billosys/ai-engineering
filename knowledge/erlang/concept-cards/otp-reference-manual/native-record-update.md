---
# === CORE IDENTIFICATION ===
concept: Native Record Update
slug: native-record-update

# === CLASSIFICATION ===
category: data-types
subcategory: native-records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Updating Native Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record modification"
  - "anonymous record update"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
extends: []
related:
  - native-record-field-access
  - native-record-patterns
contrasts_with:
  - record-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I update a native record?"
  - "What is anonymous record update?"
  - "Does update use the current definition or the captured definition?"
---

# Quick Definition
Native record update creates a copy with specified fields changed, using `Expr#Name{Field1=Expr1, ...}`, `Expr#Module:Name{...}`, or the anonymous form `Expr#_{Field1=Expr1, ...}`. Updates use the captured definition from construction time, not the current module definition.

# Core Definition
The Erlang Reference Manual states: "Updating is *not* construction, so the captured definition will be used." The syntax `Expr#Name{Field1=Expr1, ..., FieldK=ExprK}` returns "A copy of this record... with the value of each specified field `FieldI` changed to the value of evaluating the corresponding expression `ExprI`. All other fields retain their old values." For external updates, "the record value must have the name `Name` and be defined in the module `Module`." The anonymous form `Expr#_{Field1=Expr1, ..., FieldK=ExprK}` updates without specifying the record name. Operations "will fail with an exception if any of the named fields do not exist in the record definition captured when the record was constructed" (Native Records, "Updating Native Records" and "Anonymous Update" sections).

# Prerequisites
- **native-record-construction** -- A record must be constructed before it can be updated

# Key Properties
1. Local syntax: `Expr#Name{Field1=Expr1, ..., FieldK=ExprK}`
2. External syntax: `Expr#Module:Name{Field1=Expr1, ..., FieldK=ExprK}`
3. Anonymous syntax: `Expr#_{Field1=Expr1, ..., FieldK=ExprK}`
4. Returns a copy with specified fields changed; original is immutable
5. Uses the **captured** definition, not the current module definition
6. Fails if any named fields do not exist in the captured definition
7. External update fails if the record was not exported at construction time
8. Anonymous update requires export if the record is from another module

# Construction / Recognition
## To Update:
1. Local: `Record#Name{field=NewValue}`
2. External: `Record#Module:Name{field=NewValue}`
3. Anonymous: `Record#_{field=NewValue}`

## To Recognize:
1. Look for `Expr#Name{...}`, `Expr#Module:Name{...}`, or `Expr#_{...}` where `Expr` evaluates to an existing record

# Context & Application
The key insight for native record update is that it uses the captured definition. This means updates work correctly even when the module has been reloaded with a modified record definition. It also means you can update records on remote nodes where the defining module has never been loaded. The anonymous form enables polymorphic update functions.

# Examples
**Example 1**: Local update:
```erlang
-record #vec{x = 0.0, y = 0.0}.

scale_x(Vec, Factor) ->
    Vec#vec{x = Vec#vec.x * Factor}.
```

**Example 2**: Anonymous update:
```erlang
set_name(Rec, Name) ->
    Rec#_{name = Name}.
```

# Relationships
## Builds Upon
- **native-record-construction** -- The captured definition governs which fields can be updated

## Enables
- **native-record-hot-code-update** -- Understanding captured definitions is essential for hot code update strategies

## Related
- **native-record-field-access** -- Often used together to read and modify fields

## Contrasts With
- **record-update** -- Tuple-based record update uses the compile-time definition from the current module, not a captured definition

# Common Errors
- **Error**: Trying to update a field that was not present in the captured definition (e.g., after adding a field and reloading)
  **Correction**: Use the `update/1` pattern from the hot code update section to convert old records to new definitions.

- **Error**: Updating an unexported record from another module
  **Correction**: Ensure the record was exported at construction time.

# Common Confusions
- **Confusion**: Assuming update uses the current module definition
  **Clarification**: Update uses the captured definition from construction time. If the module has been reloaded with new fields, those fields are not available for update on old record values.

# Source Reference
Native Records chapter, "Updating Native Records" and "Anonymous Update" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit syntax and semantics
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
