---
# === CORE IDENTIFICATION ===
concept: Record Definition
slug: record-definition

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
section: "Defining Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record attribute"
  - "-record declaration"
  - "tuple-based record definition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - atom
  - tuple
extends: []
related:
  - record-creation
  - record-field-access
  - record-internal-representation
contrasts_with:
  - native-record-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a record in Erlang?"
  - "What is the -record attribute syntax?"
  - "Can record fields have default values?"
  - "Where should a record definition be placed in a module?"
---

# Quick Definition
A record definition declares a named data structure with fixed fields using the `-record(Name, {Field1, ..., FieldN})` attribute. Each field can have an optional default value; if omitted, `undefined` is used.

# Core Definition
The Erlang Reference Manual states: "A record is a data structure for storing a fixed number of elements. It has named fields and is similar to a struct in C. Record expressions are translated to tuple expressions during compilation." A record definition consists of the name of the record followed by its field names, where "Record and field names must be atoms." Each field can have "an optional default value" which is "an arbitrary expression, except that it must not use any variables." If no default value is supplied, `undefined` is used (Records, "Defining Records" section).

# Prerequisites
- **atom** -- Record names and field names must be atoms
- **tuple** -- Records are internally represented as tagged tuples

# Key Properties
1. Syntax: `-record(Name, {Field1 [= Expr1], ..., FieldN [= ExprN]}).`
2. Record and field names must be atoms
3. Default values can be arbitrary expressions but must not contain variables
4. If no default value is supplied, `undefined` is used
5. The definition must appear before any usage of the record in the module
6. Definitions can be placed anywhere among attributes and function declarations
7. If used in multiple modules, the definition should be placed in an include file
8. Since Erlang/OTP 26, records can also be defined in the shell

# Construction / Recognition
## To Define:
1. Use the `-record` attribute
2. Provide the record name (an atom) and field list in curly braces
3. Optionally assign default values with `=`

## To Recognize:
1. Look for the `-record(Name, {Fields})` attribute syntax
2. The name and all field names are atoms
3. Default values follow `=` after field names

# Context & Application
Record definitions provide named access to tuple elements at compile time. They are the traditional way of defining structured data types in Erlang. Records are widely used in OTP for process state, protocol messages, and ETS table entries. When a record is shared across modules, the definition should be placed in a `.hrl` header file.

# Examples
**Example 1** (Defining Records section): Basic record definition with no default values:
```erlang
-record(person, {name, phone, address}).
```

**Example 2** (Defining Records section): General syntax with optional defaults:
```erlang
-record(Name, {Field1 [= Expr1],
               ...
               FieldN [= ExprN]}).
```

# Relationships
## Builds Upon
- **atom** -- Record and field names are atoms
- **tuple** -- Records are compiled to tagged tuples

## Enables
- **record-creation** -- A record must be defined before it can be created
- **record-field-access** -- Field access requires a prior definition
- **record-update** -- Updating records requires knowledge of their definition
- **record-patterns** -- Pattern matching on records uses the definition

## Related
- **record-internal-representation** -- Records are tuples underneath

## Contrasts With
- **native-record-definition** -- Native records use `-record #Name{...}` syntax and are a distinct type, not a tuple

# Common Errors
- **Error**: Using variables in default value expressions
  **Correction**: Default values must be constant expressions. Use only literals, other constants, or expressions that do not reference variables.

- **Error**: Using a record before its definition in the module
  **Correction**: Place the `-record` attribute before any code that references it.

# Common Confusions
- **Confusion**: Thinking records are a distinct runtime type
  **Clarification**: Tuple-based records are purely a compile-time abstraction. At runtime, they are ordinary tagged tuples.

- **Confusion**: Confusing tuple-based records (`-record(name, {...})`) with native records (`-record #name{...}`)
  **Clarification**: Tuple-based records existed first and compile to tuples. Native records (OTP 29+) are a separate, distinct data type.

# Source Reference
Records chapter, "Defining Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit definition and syntax given
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
