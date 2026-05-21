---
# === CORE IDENTIFICATION ===
concept: Records in Guards
slug: record-in-guards

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: records
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Records in Guards"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record guard expressions"
  - "is_record in guards"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - record-field-access
extends: []
related:
  - record-patterns
  - record-creation
contrasts_with:
  - native-record-in-guards

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I use records in guard expressions?"
  - "How does is_record/2 work?"
  - "Can I access record fields in guard tests?"
  - "Can I create records inside guard expressions?"
---

# Quick Definition
Record expressions are allowed in guards because they compile to tuple expressions. Both record creation and field access can appear in guards, provided all subexpressions are valid guard expressions. The BIF `is_record(Term, RecordTag)` tests whether a term is a record of a given type.

# Core Definition
The Erlang Reference Manual states: "Since record expressions are expanded to tuple expressions, creating records and accessing record fields are allowed in guards. However, all subexpressions (for initializing fields) must be valid guard expressions as well." There is also the type test BIF `is_record(Term, RecordTag)` for testing whether a term is a specific record type (Records, "Records in Guards" section).

# Prerequisites
- **record-definition** -- The record type must be defined
- **record-field-access** -- Understanding of `Expr#Name.Field` syntax

# Key Properties
1. Record creation is allowed in guards (compiles to tuple creation)
2. Record field access is allowed in guards (compiles to `element/2`)
3. All subexpressions in record guard expressions must themselves be valid guard expressions
4. `is_record(Term, RecordTag)` is a guard BIF that tests if `Term` is a record with tag `RecordTag`
5. `is_record/2` checks both the tuple tag and the tuple size

# Construction / Recognition
## To Use Records in Guards:
1. Use record field access: `when Expr#Name.Field =:= Value`
2. Use record creation for comparison: `when Msg =:= #msg{to=void, no=3}`
3. Use `is_record/2` for type testing: `when is_record(Term, RecordTag)`

## To Recognize:
1. Look for `#Name.Field` or `#Name{...}` expressions after `when`
2. Look for `is_record/2` calls in guard position

# Context & Application
Using records in guards enables concise conditional logic based on record types and field values. The `is_record/2` BIF is particularly useful for type-dispatching in function clauses when you want to check the record type without destructuring it. Since record expressions expand to tuple operations, they are efficient in guards.

# Examples
**Example 1** (Records in Guards section): Record creation in a guard:
```erlang
handle(Msg, State) when Msg =:= #msg{to=void, no=3} ->
    ...
```

**Example 2** (Records in Guards section): Field access in a guard:
```erlang
handle(Msg, State) when State#state.running =:= true ->
    ...
```

**Example 3** (Records in Guards section): Using is_record/2:
```erlang
is_person(P) when is_record(P, person) ->
    true;
is_person(_P) ->
    false.
```

# Relationships
## Builds Upon
- **record-definition** -- Guard expressions reference defined records
- **record-field-access** -- Field access syntax used in guards

## Enables
No direct dependents within this extraction scope.

## Related
- **record-patterns** -- Pattern matching and guards often work together in function clauses
- **record-creation** -- Record creation can appear in guard comparisons

## Contrasts With
- **native-record-in-guards** -- Native records only allow field access in guards, not record creation

# Common Errors
- **Error**: Using non-guard-safe expressions as field initializers in a guard record expression
  **Correction**: All subexpressions in guard record expressions must be valid guard expressions (no function calls, side effects, etc.).

# Common Confusions
- **Confusion**: Thinking `is_record/2` works on native records the same way
  **Clarification**: For tuple-based records, `is_record/2` checks the tuple tag and size. For native records, `is_record/2` tests both native and tuple-based records with the given name.

# Source Reference
Records chapter, "Records in Guards" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit examples provided
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
