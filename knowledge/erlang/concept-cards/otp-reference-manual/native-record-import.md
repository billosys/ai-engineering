---
# === CORE IDENTIFICATION ===
concept: Native Record Import
slug: native-record-import

# === CLASSIFICATION ===
category: api-design
subcategory: native-records
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Importing Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-import_record"
  - "record import attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-export
extends: []
related:
  - native-record-construction
  - native-record-definition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use a native record from another module without qualifying it?"
  - "What is the -import_record attribute?"
  - "Can I use a native record without importing it?"
---

# Quick Definition
The `-import_record(Module, [Name1, ...])` attribute lets you use native records from another module without prefixing each use with the module name. Without importing, you must use the `#Module:Name{...}` syntax.

# Core Definition
The Erlang Reference Manual states: "To use a native record defined in another module without fully qualifying its name every time, use `-import_record`." The syntax is `-import_record(Module, [Name1, Name2, ..., NameN]).` where `Module` "specifies which module to import records from" and `Name1`, `Name2`, etc. "are record names (atoms) to be imported" (Native Records, "Importing Records" section).

# Prerequisites
- **native-record-export** -- The record must be exported from its defining module to be usable externally

# Key Properties
1. Syntax: `-import_record(Module, [Name1, Name2, ..., NameN]).`
2. Allows using `#Name{...}` instead of `#Module:Name{...}`
3. The referenced records must be exported from the source module
4. Importing is optional -- fully qualified syntax always works
5. Imported record operations count as "external" operations

# Construction / Recognition
## To Import:
1. Add `-import_record(Module, [RecordNames])` to your module
2. Use `#Name{...}` syntax as if the record were defined locally

## To Recognize:
1. Look for `-import_record(Module, [...])` attributes
2. Subsequent uses of `#Name{...}` without a module prefix on imported names

# Context & Application
Importing records reduces syntactic noise when a module frequently uses records from another module. It is analogous to `-import` for functions. Even with importing, the operations remain "external" -- they require the source module to be loaded and the record to be exported. This distinction matters for error handling and hot code update behavior.

# Examples
**Example 1** (Importing Records section):
```erlang
-module(example).
-import_record(vector_lib, [vector, position]).

%% Now #vector{...} works without the vector_lib: prefix
make_unit_x() ->
    #vector{x=1.0, y=0.0}.
```

**Example 2** (External Record Construction section): Without importing:
```erlang
-module(example).

make_unit_x() ->
    #vector_lib:vector{x=1.0, y=0.0}.
```

# Relationships
## Builds Upon
- **native-record-export** -- Records must be exported to be importable

## Enables
- **native-record-construction** -- Imported records can be constructed without module prefix
- **native-record-field-access** -- Field access on imported records uses unqualified syntax

## Related
- **native-record-definition** -- The original definition determines the fields

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Importing a record that is not exported from the source module
  **Correction**: Ensure the source module has `-export_record([name])` for the record you want to import.

- **Error**: Importing from a module that is not loaded at runtime
  **Correction**: External record operations require the module to be loaded. Ensure it is loaded or handle the potential runtime exception.

# Common Confusions
- **Confusion**: Thinking importing makes the record "local"
  **Clarification**: Imported records are still external. The module must be loaded, the record must be exported, and runtime errors differ from local construction errors (runtime exceptions vs. compile errors).

# Source Reference
Native Records chapter, "Importing Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit syntax and examples
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
