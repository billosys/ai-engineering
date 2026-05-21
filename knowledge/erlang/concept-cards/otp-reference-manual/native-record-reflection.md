---
# === CORE IDENTIFICATION ===
concept: Native Record Reflection
slug: native-record-reflection

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
section: "Reflection: The records Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "records module"
  - "native record introspection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
extends: []
related:
  - native-record-definition
  - record-internal-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I inspect native records at runtime?"
  - "What is the records module?"
  - "Can I dynamically construct or examine native records?"
---

# Quick Definition
The `records` module provides functions for constructing and inspecting native records at runtime. It is intended primarily for debugging, library functions (like printing), and tools (like the Debugger), not for general production code.

# Core Definition
The Erlang Reference Manual states: "The `records` module contains functions for constructing and inspecting native records. The main purpose of the functions in the `records` module is for debugging, implementing library functions (such as printing of native records), and implementing tools (such as the Debugger). Use with care in production code." (Native Records, "Reflection: The records Module" section).

# Prerequisites
- **native-record-construction** -- Understanding what native records are and how they are created

# Key Properties
1. The `records` module provides runtime introspection of native records
2. Intended for debugging, library functions, and tool implementation
3. Should be used with care in production code
4. Enables dynamic construction and inspection (not just compile-time access)

# Construction / Recognition
## To Use Reflection:
1. Call functions from the `records` module
2. Use for debugging, printing, or tool integration

## To Recognize:
1. Look for calls to the `records` module

# Context & Application
The `records` module fills a gap that arises from native records being a compile-time construct in normal code. For tools like debuggers, serializers, and pretty-printers, runtime access to record structure is essential. The "use with care" warning reflects the fact that reflection bypasses the normal compile-time guarantees and may have performance implications.

# Examples
**Example 1** (Reflection section, based on module description):
```erlang
%% Using the records module for debugging/inspection
%% (exact API is in the records module documentation)
records:fields(SomeRecord).
```

# Relationships
## Builds Upon
- **native-record-construction** -- Operates on constructed native records

## Enables
No direct dependents within this extraction scope.

## Related
- **native-record-definition** -- Reflection exposes the structure defined by the definition
- **record-internal-representation** -- Tuple-based records have `record_info/2` as their reflection mechanism

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Using the `records` module in hot paths in production code
  **Correction**: The source warns to "use with care in production code." Prefer compile-time record access for performance-critical code.

# Common Confusions
- **Confusion**: Thinking `record_info/2` works on native records
  **Clarification**: `record_info/2` is the reflection mechanism for tuple-based records. Native records use the `records` module instead.

# Source Reference
Native Records chapter, "Reflection: The records Module" section.

# Verification Notes
- Definition source: Direct quote from source text
- Confidence rationale: High -- explicit purpose statement; however, the section is brief and refers to the `records` module documentation for details
- Uncertainties: Specific API functions of the `records` module are not detailed in this source chapter
- Cross-reference status: All referenced slugs correspond to cards in this extraction
