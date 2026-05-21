---
# === CORE IDENTIFICATION ===
concept: Native Records in Guards
slug: native-record-in-guards

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: native-records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Native Records in Guards"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record guard expressions"
  - "is_record/1 guard"
  - "is_record/3 guard"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
  - native-record-field-access
extends: []
related:
  - native-record-patterns
contrasts_with:
  - record-in-guards

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I use native records in guard expressions?"
  - "What is is_record/1?"
  - "What is the difference between is_record/1, is_record/2, and is_record/3?"
  - "Can I create native records in guards?"
---

# Quick Definition
Only field access (`Expr#Name.Field`) is allowed for native records in guards -- not construction or update. The BIFs `is_record/1`, `is_record/2`, and `is_record/3` provide type testing for native records in guard expressions.

# Core Definition
The Erlang Reference Manual states: "Field access is the only native-record operation allowed in guards." Three guard BIFs are available: `is_record(Term)` "tests whether `Term` is a native record" (returns `false` for tuple-based records); `is_record(Term, Name)` "tests whether `Term` is either a native or a tuple-based record with the name `Name`, defined in the current module or (in the case of a native record) imported from another module"; and `is_record(Term, Module, Name)` "tests whether `Term` is a native record with the name `Name` constructed from a definition in module `Module`" (Native Records, "Native Records in Guards", "The Guard BIF is_record/1", "The Guard BIF is_record/2", and "The Guard BIF is_record/3" sections).

# Prerequisites
- **native-record-construction** -- Records must be constructed to be tested
- **native-record-field-access** -- Field access is the only allowed operation in guards

# Key Properties
1. Only field access is allowed in guards for native records (not construction or update)
2. `is_record/1` -- tests if `Term` is any native record (returns `false` for tuple-based)
3. `is_record/2` -- tests if `Term` is a native **or** tuple-based record with name `Name`
4. `is_record/3` -- tests if `Term` is a native record with name `Name` from module `Module`
5. Pattern matching on the record name is often more convenient than `is_record/2` or `is_record/3`
6. Pattern matching `#Name{}` succeeds regardless of export status

# Construction / Recognition
## To Use in Guards:
1. Field access: `when Expr#Name.Field =:= Value`
2. Type test: `when is_record(Term)`, `when is_record(Term, Name)`, or `when is_record(Term, Module, Name)`

## To Recognize:
1. Look for `is_record/1,2,3` or `Expr#Name.Field` after `when`

# Context & Application
The three-arity `is_record` BIF is particularly useful for disambiguating same-named records from different modules -- a situation unique to native records. The source notes that matching is "often more convenient" than `is_record` because it provides the same type check plus field extraction in one step.

# Examples
**Example 1** (Native Records in Guards section): Field access in guard:
```erlang
handle(Msg, State) when State#state.running =:= true ->
    ...
```

**Example 2** (The Guard BIF is_record/2 section): Using is_record/2:
```erlang
-record #vec{x, y}.

increment(Vec) when is_record(Vec, vec) ->
    ... .
```

**Example 3** (The Guard BIF is_record/2 section): Equivalent with pattern matching:
```erlang
-record #vec{x, y}.

increment(#vec{}=Vec) ->
    ... .
```

**Example 4** (The Guard BIF is_record/3 section): Disambiguating by module:
```erlang
increment(Vec) when is_record(Vec, geom_2d, vec) ->
    ... ;
increment(Vec) when is_record(Vec, geom_3d, vec) ->
    ... .
```

**Example 5** (The Guard BIF is_record/3 section): Equivalent with pattern matching:
```erlang
increment(#geom_2d:vec{}=Vec) ->
    ... ;
increment(#geom_3d:vec{}=Vec) ->
    ... .
```

# Relationships
## Builds Upon
- **native-record-construction** -- Records must exist to be tested
- **native-record-field-access** -- The only native-record operation allowed in guards

## Enables
No direct dependents within this extraction scope.

## Related
- **native-record-patterns** -- Pattern matching is an alternative to guard-based type testing

## Contrasts With
- **record-in-guards** -- Tuple-based records allow both creation and field access in guards; native records only allow field access. Also, `is_record/1` returns `false` for tuple-based records.

# Common Errors
- **Error**: Attempting to construct a native record in a guard expression
  **Correction**: Only field access is allowed for native records in guards. Use pattern matching in the function head instead.

- **Error**: Using `is_record/1` expecting it to return `true` for tuple-based records
  **Correction**: `is_record/1` only returns `true` for native records. Use `is_record/2` to test for both types.

# Common Confusions
- **Confusion**: Conflating `is_record/1`, `is_record/2`, and `is_record/3`
  **Clarification**: `/1` tests for any native record; `/2` tests for native or tuple-based by name; `/3` tests for native records by module and name.

# Source Reference
Native Records chapter, "Native Records in Guards", "The Guard BIF is_record/1", "The Guard BIF is_record/2", and "The Guard BIF is_record/3" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit BIF descriptions and examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
