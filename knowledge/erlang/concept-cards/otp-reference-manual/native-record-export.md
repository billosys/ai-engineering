---
# === CORE IDENTIFICATION ===
concept: Native Record Export
slug: native-record-export

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
section: "Exporting Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-export_record"
  - "record export attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-definition
extends: []
related:
  - native-record-import
  - native-record-construction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a native record accessible to other modules?"
  - "What is the -export_record attribute?"
  - "What happens if I don't export a native record?"
---

# Quick Definition
The `-export_record([Name1, Name2, ...])` attribute makes native record fields accessible to other modules. Without this attribute, the record's fields are private to the defining module.

# Core Definition
The Erlang Reference Manual states: "By default, the fields of a native record are only accessible within the defining module. To make them accessible to other modules, the record needs to be exported." The syntax is `-export_record([Name1, Name2, ..., NameN]).` where the names are record names (atoms) defined in the current module (Native Records, "Exporting Records" section).

# Prerequisites
- **native-record-definition** -- The record must be defined in the module before it can be exported

# Key Properties
1. Syntax: `-export_record([Name1, Name2, ..., NameN]).`
2. By default, native record fields are private to the defining module
3. Exporting makes fields accessible to other modules
4. The export status is captured when a record is constructed
5. Subsequent operations on the record check the captured export status
6. Multiple record names can be exported in a single attribute

# Construction / Recognition
## To Export:
1. Define the native record in the module
2. Add an `-export_record([...])` attribute listing the record names

## To Recognize:
1. Look for `-export_record([...])` attributes in the module

# Context & Application
The export mechanism for native records embodies the principle of information hiding. A module defines and owns its records, exporting only those that form part of its public API. This contrasts with tuple-based records, which rely on shared header files and have no visibility control. The export status is captured at construction time, meaning even if a record is later unexported (by reloading a modified module), existing record values remain accessible.

# Examples
**Example 1** (Exporting Records section):
```erlang
-module(vector_lib).
-record #vector{x = 0.0, y = 0.0}.
-record #position{x = 0.0, y = 0.0}.
-export_record([vector, position]).
```

# Relationships
## Builds Upon
- **native-record-definition** -- Must be defined before exporting

## Enables
- **native-record-import** -- Exported records can be imported by other modules
- **native-record-construction** -- External construction requires the record to be exported

## Related
- **native-record-field-access** -- External field access requires the record to have been exported at construction time

## Contrasts With
No direct contrasts within this extraction scope. (Tuple-based records have no export mechanism -- they use header files instead.)

# Common Errors
- **Error**: Forgetting to export a record that other modules need to use
  **Correction**: Add `-export_record([record_name])` to make the record's fields accessible externally.

- **Error**: Exporting a record name that is not defined in the module
  **Correction**: Ensure the record is defined with `-record #Name{...}` before the export attribute.

# Common Confusions
- **Confusion**: Thinking `-export_record` works like `-export` for functions
  **Clarification**: `-export_record` controls field access visibility, not function visibility. It is specific to native records.

- **Confusion**: Thinking unexported records cannot be constructed externally at all
  **Clarification**: An unexported record can still be constructed externally using `#Module:Name{...}`, but field access, update, and pattern matching on specific fields will fail on the resulting value.

# Source Reference
Native Records chapter, "Exporting Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit syntax and semantics
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
