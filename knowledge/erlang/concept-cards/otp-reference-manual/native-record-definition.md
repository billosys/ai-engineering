---
# === CORE IDENTIFICATION ===
concept: Native Record Definition
slug: native-record-definition

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
  - "-record # attribute"
  - "native record declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
  - record-definition
extends: []
related:
  - native-record-export
  - native-record-import
  - native-record-construction
contrasts_with:
  - record-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a native record in Erlang?"
  - "What is the syntax difference between native record and tuple-based record definitions?"
  - "Can native record names look like variable names?"
  - "Should native records be defined in header files?"
---

# Quick Definition
A native record is defined using `-record #Name{Field1 [= Expr1], ..., FieldN [= ExprN]}.` -- note the `#` before the name. Unlike tuple-based records, native records are a distinct runtime type introduced in Erlang/OTP 29 (experimental).

# Core Definition
The Erlang Reference Manual states: "A native record is a data structure for storing a fixed number of elements in named fields. Unlike traditional tuple-based records described in the previous section, a native record is a distinct type." A definition consists of "the `#` character followed by the record name and a set of named fields. Field names must be atoms." The `#Name` syntax "denotes a native record definition" and "As opposed to tuple-based records, it is not necessary to quote atoms that look like variable names or keywords" (Native Records, "Defining Native Records" section).

# Prerequisites
- **atom** -- Record names and field names are atoms
- **record-definition** -- Understanding tuple-based records helps contrast with native records

# Key Properties
1. Syntax: `-record #Name{Field1 [= Expr1], ..., FieldN [= ExprN]}.`
2. Native records are a distinct type, not tuples
3. Record names need not be quoted even when they look like variable names or keywords (e.g., `#State`, `#div`)
4. Default values must be literals or simple compile-time evaluable expressions (no variables, function calls, or record constructions)
5. The definition must appear before any usage in the module
6. Fields are private to the defining module by default -- must be exported for external access
7. Native records should **never** be defined in header files
8. Introduced as experimental in Erlang/OTP 29

# Construction / Recognition
## To Define:
1. Use `-record #Name{...}` (note the `#` before the name -- this distinguishes it from tuple-based records)
2. List field names, optionally with default values
3. Place the definition before any usage in the module

## To Recognize:
1. Look for `-record #Name{...}` with the `#` prefix on the name
2. Contrast with tuple-based syntax: `-record(Name, {...})` (parentheses, no `#`)

# Context & Application
Native records provide a proper type-safe record mechanism in Erlang. Unlike tuple-based records, they cannot be confused with ordinary tuples, making code more robust. The recommendation to never define them in header files reflects the module-scoped ownership model: a native record belongs to exactly one module, which controls its visibility through export/import.

# Examples
**Example 1** (Defining Native Records section): Various definitions:
```erlang
-record #div{class}.
-record #State{}.
-record #'42'{}.
```

**Example 2** (Defining Native Records section): Record with defaults:
```erlang
-record #vector{x = 0.0, y = 0.0}.
```

# Relationships
## Builds Upon
- **atom** -- Names and fields are atoms
- **record-definition** -- Contrasts with the traditional approach

## Enables
- **native-record-export** -- Defined records can be exported
- **native-record-construction** -- Records must be defined before construction
- **native-record-field-access** -- Field access requires a definition

## Related
- **native-record-import** -- Other modules import the record to use it

## Contrasts With
- **record-definition** -- Tuple-based records use `-record(Name, {...})` syntax, compile to tuples, can be in header files, and field names must be quoted if they look like variables

# Common Errors
- **Error**: Defining a native record in a header file
  **Correction**: Native records should be defined in exactly one module and exported with `-export_record`. Do not use `.hrl` files.

- **Error**: Using variables or function calls in default values
  **Correction**: Default values must be literals or simple compile-time expressions.

# Common Confusions
- **Confusion**: Thinking native records and tuple-based records are interchangeable
  **Clarification**: They are completely different types. `is_record/1` returns `false` for tuple-based records. They have different syntaxes, different runtime representations, and different visibility rules.

- **Confusion**: Thinking the `#Name` syntax is the same as tuple-based record syntax
  **Clarification**: Tuple-based: `-record(Name, {fields}).` Native: `-record #Name{fields}.` The `#` prefix and lack of parentheses distinguish them.

# Source Reference
Native Records chapter, "Defining Native Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit definition, syntax, and examples
- Uncertainties: Experimental status in OTP 29 means API may change in OTP 30
- Cross-reference status: All referenced slugs correspond to cards in this extraction
