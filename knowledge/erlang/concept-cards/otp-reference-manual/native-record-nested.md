---
# === CORE IDENTIFICATION ===
concept: Nested Native Records
slug: native-record-nested

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
section: "Nested Native Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "chained native record access"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-definition
  - native-record-field-access
  - native-record-update
extends:
  - native-record-field-access
  - native-record-update
related:
  - nested-records
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I access fields in nested native records?"
  - "How do I update deeply nested native record fields?"
  - "Is the nesting syntax the same as for tuple-based records?"
---

# Quick Definition
Nested native record access and update use the same chained syntax as tuple-based records: `N2#nrec2.nrec1#nrec1.nrec0#nrec0.name`. Parentheses are not required; the expression associates left to right.

# Core Definition
The Erlang Reference Manual states that for native records, "Accessing or updating nested records can be written without parentheses." The chained expression `N2#nrec2.nrec1#nrec1.nrec0#nrec0.name` is equivalent to `((N2#nrec2.nrec1)#nrec1.nrec0)#nrec0.name` (Native Records, "Nested Native Records" section).

# Prerequisites
- **native-record-definition** -- All record types in the chain must be defined
- **native-record-field-access** -- Understanding single-level field access
- **native-record-update** -- Understanding single-level record update

# Key Properties
1. Chained access: `Expr#R1.f1#R2.f2` accesses nested fields left to right
2. Chained update: `Expr#R1.f1#R2{f2=NewVal}` updates nested fields
3. No parentheses required
4. Left-to-right associativity
5. Identical syntax to tuple-based nested records, but operates on native records
6. Note: fields that hold nested records do not use default record construction in the definition (no `nrec0=#nrec0{}` -- just `nrec0`)

# Construction / Recognition
## To Access Nested Fields:
1. Chain `#RecordName.field` segments from outer to inner
2. Each intermediate result must be a native record of the expected type

## To Recognize:
1. Multiple `#RecordName.field` segments in sequence on a single expression

# Context & Application
Nested native records follow the same ergonomic syntax as tuple-based nested records, making migration straightforward. Note that in the native record version, the nested record field definitions are simpler -- they just name the field without including a default record construction (e.g., `nrec0` rather than `nrec0=#nrec0{}`), reflecting that native records require explicit initialization.

# Examples
**Example 1** (Nested Native Records section): Definitions and access:
```erlang
-record #nrec0{name = "nested0"}.
-record #nrec1{name = "nested1", nrec0}.
-record #nrec2{name = "nested2", nrec1}.

N2 = #nrec2{nrec1 = #nrec1{nrec0 = #nrec0{}}},

"nested0" = N2#nrec2.nrec1#nrec1.nrec0#nrec0.name,
```

**Example 2** (Nested Native Records section): Nested update:
```erlang
N0n = N2#nrec2.nrec1#nrec1.nrec0#nrec0{name = "nested0a"},
```
Equivalent with parentheses:
```erlang
N0n = ((N2#nrec2.nrec1)#nrec1.nrec0)#nrec0{name = "nested0a"},
```

# Relationships
## Builds Upon
- **native-record-field-access** -- Each chain segment is a field access
- **native-record-update** -- The final segment can be an update

## Enables
No direct dependents within this extraction scope.

## Related
- **nested-records** -- Same syntax pattern for tuple-based records

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Forgetting to construct nested records explicitly when creating the outer record
  **Correction**: Unlike tuple-based records, native records do not have implicit defaults for nested record fields. You must explicitly provide `#nrec1{nrec0 = #nrec0{}}`.

# Common Confusions
- **Confusion**: Thinking nested native record updates propagate to the outer record
  **Clarification**: As with all Erlang values, the update creates a new inner record value but does not modify the outer record. Each nesting level must be explicitly updated.

# Source Reference
Native Records chapter, "Nested Native Records" section.

# Verification Notes
- Definition source: Direct examples from source text
- Confidence rationale: High -- explicit examples with equivalences
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
