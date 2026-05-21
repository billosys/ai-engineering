---
# === CORE IDENTIFICATION ===
concept: Native Record Fields and Default Values
slug: native-record-fields-defaults

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
section: "Defining Native Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record default values"
  - "native record field initialization"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-definition
extends: []
related:
  - native-record-construction
  - record-definition
contrasts_with:
  - record-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What default values can native record fields have?"
  - "What happens if I omit a field without a default value when constructing a native record?"
  - "How do native record defaults differ from tuple-based record defaults?"
---

# Quick Definition
Native record fields can have optional default values that must be literals or simple compile-time evaluable expressions. Unlike tuple-based records, fields without defaults do **not** get `undefined` automatically -- they must be explicitly provided during construction, or a compile-time/runtime error occurs.

# Core Definition
The Erlang Reference Manual states: "A default value must be a literal or a simple expression evaluable at compile time. The expression must not contain variables, function calls, or record constructions." For construction: "It is an error if not all fields are given values either explicitly or through default values." For local construction, this is a compilation error. For external construction, it is a runtime exception (Native Records, "Defining Native Records" and "Constructing Native Records" sections).

# Prerequisites
- **native-record-definition** -- Understanding native record syntax and semantics

# Key Properties
1. Default values must be literals or simple compile-time expressions
2. No variables, function calls, or record constructions in defaults
3. Fields without defaults must be explicitly assigned during construction
4. No implicit `undefined` default (unlike tuple-based records)
5. Missing field values in local construction cause a compile error
6. Missing field values in external construction cause a runtime exception

# Construction / Recognition
## To Set Defaults:
1. Add `= Value` after the field name in the definition
2. Ensure the value is a literal or compile-time evaluable expression

## To Recognize Missing Defaults:
1. Fields listed without `= Value` have no default
2. These fields MUST be provided at every construction site

# Context & Application
The strict default value policy of native records prevents accidental construction of records with uninitialized fields. This is a deliberate design choice that improves safety over tuple-based records, where omitting a field silently produces `undefined`. The compile-time restriction on default value expressions ensures that defaults are deterministic and reproducible.

# Examples
**Example 1** (Constructing Native Records section): Compile error for missing fields:
```erlang
-record #pair{a, b}.

make_empty_pair() ->
    #pair{}.  %% Compilation error: field a and b are not initialized
```

Compiler output:
```
example.erl:7:5: field a is not initialized in native record pair
example.erl:7:5: field b is not initialized in native record pair
```

**Example 2** (Defining Native Records section): Record with defaults:
```erlang
-record #vector{x = 0.0, y = 0.0}.

%% This is valid -- both fields have defaults:
make_origin() ->
    #vector{}.
```

# Relationships
## Builds Upon
- **native-record-definition** -- Default values are part of the definition

## Enables
- **native-record-construction** -- Defaults determine which fields can be omitted at construction

## Related
- **record-definition** -- Tuple-based records use `undefined` for omitted defaults

## Contrasts With
- **record-definition** -- Tuple-based records implicitly default to `undefined`; native records require explicit defaults or explicit field assignment

# Common Errors
- **Error**: Assuming uninitialized native record fields default to `undefined`
  **Correction**: Native records have no implicit default. Provide explicit defaults in the definition or explicit values at every construction site.

- **Error**: Using function calls in default value expressions
  **Correction**: Only literals and simple compile-time expressions are allowed (e.g., `0`, `[]`, `<<"hello">>`, `{a, b}`).

# Common Confusions
- **Confusion**: Expecting the same defaulting behavior as tuple-based records
  **Clarification**: Tuple-based records default to `undefined`. Native records require all fields to be explicitly initialized, either via defaults in the definition or values at construction.

# Source Reference
Native Records chapter, "Defining Native Records" and "Constructing Native Records" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit error examples shown
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
