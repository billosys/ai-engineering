---
# === CORE IDENTIFICATION ===
concept: Nested Records
slug: nested-records

# === CLASSIFICATION ===
category: data-types
subcategory: records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Nested Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "nested record access"
  - "chained record access"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - record-field-access
  - record-update
extends:
  - record-field-access
  - record-update
related:
  - native-record-nested
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I access fields in nested records?"
  - "How do I update a field inside a nested record?"
  - "Do I need parentheses for nested record access?"
---

# Quick Definition
Nested record access and update can be written without parentheses by chaining `#RecordName.field` and `#RecordName{field=Value}` expressions. The expression `N2#nrec2.nrec1#nrec1.nrec0#nrec0.name` chains from left to right.

# Core Definition
The Erlang Reference Manual explains that "Accessing or updating nested records can be written without parentheses." The chained expression `N2#nrec2.nrec1#nrec1.nrec0#nrec0.name` is equivalent to `((N2#nrec2.nrec1)#nrec1.nrec0)#nrec0.name`, showing left-to-right associativity. Before Erlang/OTP R14, parentheses were required (Records, "Nested Records" section).

# Prerequisites
- **record-definition** -- All record types in the chain must be defined
- **record-field-access** -- Understanding single-level field access
- **record-update** -- Understanding single-level record update

# Key Properties
1. Chained access: `Expr#R1.f1#R2.f2#R3.f3` accesses deeply nested fields
2. Chained update: `Expr#R1.f1#R2.f2#R3{f3=NewVal}` updates a deeply nested field
3. Left-to-right associativity: `A#R1.f1#R2.f2` equals `(A#R1.f1)#R2.f2`
4. Parentheses are optional since Erlang/OTP R14
5. Each intermediate access must yield the expected record type

# Construction / Recognition
## To Access Nested Fields:
1. Start with the outermost record expression
2. Chain `#RecordName.field` for each level of nesting

## To Update Nested Fields:
1. Access down to the level you want to update
2. Use `#RecordName{field=NewValue}` at the deepest level

## To Recognize:
1. Look for multiple `#RecordName.field` or `#RecordName{...}` segments in sequence

# Context & Application
Nested records are common when modeling hierarchical data structures such as protocol headers, configuration trees, or composite entities. The parenthesis-free syntax makes deeply nested access more readable. However, deeply nested updates can be verbose because each level requires specifying the record type.

# Examples
**Example 1** (Nested Records section): Nested record definitions and access:
```erlang
-record(nrec0, {name = "nested0"}).
-record(nrec1, {name = "nested1", nrec0=#nrec0{}}).
-record(nrec2, {name = "nested2", nrec1=#nrec1{}}).

N2 = #nrec2{},
"nested0" = N2#nrec2.nrec1#nrec1.nrec0#nrec0.name,
```

**Example 2** (Nested Records section): Nested record update:
```erlang
N0n = N2#nrec2.nrec1#nrec1.nrec0#nrec0{name = "nested0a"},
```
This is equivalent to:
```erlang
N0n = ((N2#nrec2.nrec1)#nrec1.nrec0)#nrec0{name = "nested0a"},
```

# Relationships
## Builds Upon
- **record-field-access** -- Each chain segment is a field access
- **record-update** -- The final segment can be an update

## Enables
No direct dependents within this extraction scope.

## Related
- **native-record-nested** -- Native records support the same chained syntax

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Forgetting to specify the correct record type at each level in the chain
  **Correction**: Each `#RecordName` in the chain must match the type of the value at that nesting level.

- **Error**: Trying to update a deeply nested field and expecting the outer record to be modified
  **Correction**: The chained update `A#R1.f1#R2{f2=V}` only creates a new inner record. To propagate the change outward, you must update each outer level as well.

# Common Confusions
- **Confusion**: Thinking nested record update propagates changes to the outer record automatically
  **Clarification**: Erlang values are immutable. A nested update expression like `N2#nrec2.nrec1#nrec1.nrec0#nrec0{name="new"}` returns a new `nrec0` value but does not change `N2`. You must explicitly update each outer record level.

# Source Reference
Records chapter, "Nested Records" section.

# Verification Notes
- Definition source: Direct examples from source text
- Confidence rationale: High -- explicit examples with equivalences
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
