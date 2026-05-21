---
# === CORE IDENTIFICATION ===
concept: Native Record Field Access
slug: native-record-field-access

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
section: "Record Field Access"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record dot syntax"
  - "anonymous field access"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
extends: []
related:
  - native-record-update
  - native-record-patterns
contrasts_with:
  - record-field-access

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I access a field of a native record?"
  - "What is anonymous field access with #_.Field?"
  - "What conditions must be met for native record field access to succeed?"
---

# Quick Definition
Native record field access uses `Expr#Name.Field`, `Expr#Module:Name.Field`, or the anonymous form `Expr#_.Field`. Access uses the captured definition from construction time and checks export status for external access.

# Core Definition
The Erlang Reference Manual describes three forms of field access. The standard forms `Expr#Name.Field` and `Expr#Module:Name.Field` require `Expr` to evaluate to a record value with the matching name and module. The anonymous form `Expr#_.Field` accesses a field without specifying the record name. For local access, "the record value must have the name `Name` and its module must be the same as the name of the currently executing module." For external access, "the record value must be named `Name` and be defined in module `Module`. Furthermore, at the time the record was constructed, the record must have been exported." In all cases, "the `Field` must have existed at the time the record was constructed." For anonymous access, "the operation will fail if the field does not exist in the captured record definition" (Native Records, "Record Field Access" and "Anonymous Record Field Access" sections).

# Prerequisites
- **native-record-construction** -- A record must be constructed (with captured definition) before field access

# Key Properties
1. Local access: `Expr#Name.Field` -- record must match name and current module
2. External access: `Expr#Module:Name.Field` -- record must match name and module, and must have been exported at construction time
3. Anonymous access: `Expr#_.Field` -- accesses field by name only, checks export status if from another module
4. All forms use the captured definition, not the current module definition
5. In guards, access failure causes the guard to fail (not an exception)
6. In function bodies, access failure raises an exception

# Construction / Recognition
## To Access a Field:
1. Local: `Record#Name.Field` (record must be from current module)
2. External: `Record#Module:Name.Field` (record must be exported from `Module`)
3. Anonymous: `Record#_.Field` (works on any native record with that field)

## To Recognize:
1. Look for `Expr#Name.Field`, `Expr#Module:Name.Field`, or `Expr#_.Field` patterns

# Context & Application
The anonymous access form `#_.Field` is useful for polymorphic code that operates on records from multiple modules that share field names. The export status check ensures that module authors can control which records are part of their public API. The captured definition mechanism means field access works even if the defining module has been reloaded with a different definition.

# Examples
**Example 1** (Record Field Access section):
```erlang
-record #person{name, phone, address}.

get_person_name(Person) ->
    Person#person.name.

get_vec_x(Vec) ->
    Vec#geom_2d:vec.x.
```

**Example 2** (Anonymous Record Field Access section): Anonymous access:
```erlang
get_name(Rec) ->
    Rec#_.name.
```

# Relationships
## Builds Upon
- **native-record-construction** -- The captured definition determines accessible fields

## Enables
- **native-record-in-guards** -- Field access is the only native-record operation allowed in guards

## Related
- **native-record-update** -- Similar syntax but modifies the record
- **native-record-patterns** -- Pattern matching is an alternative to explicit field access

## Contrasts With
- **record-field-access** -- Tuple-based record field access has no export checks, no anonymous form, and no module-qualified form

# Common Errors
- **Error**: Accessing a field on a non-exported record from another module
  **Correction**: Ensure the record was exported at construction time, or use the anonymous form (which still requires export for cross-module access).

- **Error**: Accessing a field name that was not present when the record was constructed
  **Correction**: The field must have existed in the definition at construction time, regardless of the current definition.

# Common Confusions
- **Confusion**: Thinking `#_.Field` bypasses export checks entirely
  **Clarification**: Anonymous access still requires the record to have been exported if the record's module differs from the currently executing module.

# Source Reference
Native Records chapter, "Record Field Access" and "Anonymous Record Field Access" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit syntax, semantics, and examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
