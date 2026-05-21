---
concept: Maps vs Records
slug: maps-vs-records
category: data-structures
subcategory: maps
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Maps"
chapter_number: null
pdf_page: null
section: "Maps or Records?"
extraction_confidence: high
aliases:
  - "records versus maps"
  - "maps versus records"
prerequisites: []
extends: []
related:
  - maps-as-alternative-to-records
  - small-map-implementation
contrasts_with: []
answers_questions:
  - "How do records compare to maps for performance?"
  - "What are the trade-offs between maps and records in Erlang?"
---

# Quick Definition

Records and small maps have similar performance when the advice in the Efficiency Guide is followed. The choice between them should be based on desired properties of the data structure, not on performance.

# Core Definition

The Efficiency Guide states: "If the advice in this chapter is followed, the performance of records compared to using small maps instead of records is expected to be similar. Therefore, the choice between records and maps should be based on the desired properties of the data structure and not performance" (Maps chapter, "Maps or Records?" section).

Records offer compile-time safety (misspelled field names cause compilation errors) and use slightly less memory with slightly better performance. Maps offer flexibility: adding a new field does not require recompilation of all code using the data structure.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Performance of records and small maps (at most 32 elements) is expected to be similar
2. Records catch misspelled field names at compile time; maps only fail at runtime
3. Records use slightly less memory than maps
4. Records have slightly better performance in most circumstances
5. Adding a new field to a record requires recompilation of all code using that record
6. Records are recommended only within a unit of code that can be easily recompiled (e.g., a single application or module)

# Construction / Recognition

## When to Choose Records

1. The data structure is used only within a single application or module
2. Compile-time safety for field names is desired
3. Memory usage must be minimized

## When to Choose Maps

1. The data structure crosses application or module boundaries
2. Fields may be added over time without recompiling all consumers
3. Runtime flexibility in key sets is needed

# Context & Application

This decision is one of the first a developer faces when designing data structures in Erlang. The Efficiency Guide positions it as a non-performance decision, redirecting developers to consider maintainability and safety properties instead.

**Typical guidance:** Use records for internal module state where all code can be recompiled together. Use maps for public APIs and data that crosses module boundaries.

# Examples

**Record advantage** (Maps chapter): If a record field name is misspelled, the compiler raises an error. If a map key is misspelled, there is no compiler warning and the program will fail at runtime.

**Record disadvantage** (Maps chapter): If a new field is added to a record, all code that uses that record must be recompiled. This makes records unsuitable for data structures shared across independently compiled units.

# Relationships

## Related

- **maps-as-alternative-to-records** -- Detailed advice for using maps in place of records
- **small-map-implementation** -- Understanding the small map representation explains why performance is similar to records

# Common Errors

- **Error**: Choosing maps over records purely for perceived modernity or flexibility without considering the loss of compile-time safety
  **Correction**: Evaluate the actual trade-offs; records provide valuable compile-time checks that maps cannot

- **Error**: Using records in public API boundaries shared across many applications
  **Correction**: Adding a field to such a record forces recompilation of all consumers; maps are more appropriate here

# Common Confusions

- **Confusion**: Believing maps are significantly slower than records
  **Clarification**: When the Efficiency Guide's advice is followed (small maps, map syntax, key sharing), performance is expected to be similar

- **Confusion**: Thinking records and maps are interchangeable in all contexts
  **Clarification**: Records provide compile-time guarantees that maps cannot; maps provide runtime flexibility that records cannot

# Source Reference

Maps chapter, "Maps or Records?" section. No chapter number or page number available (OTP documentation source).

# Verification Notes

- Definition: Direct extraction from the opening paragraph of the "Maps or Records?" section
- Key Properties: All items directly stated in the source text
- Confidence: HIGH -- the source provides explicit, unambiguous guidance on this comparison
- Cross-references: Slugs verified against planned extractions for this batch
