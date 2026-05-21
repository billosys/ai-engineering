---
concept: Types In Records
slug: type-record-fields
category: data-types
subcategory: records
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Types in records"
extraction_confidence: high
aliases:
  - "typed record fields"
  - "record field types"
prerequisites: []
extends: []
related:
  - records-before-functions
  - lowercase-record-names
  - write-function-specs
contrasts_with: []
answers_questions:
  - "Should record fields have type definitions?"
---

# Quick Definition

Always add type definitions to your record fields.

# Core Definition

"Always add type definitions to your record fields" (Inaka, "Types in records"). Every field in a `-record` declaration carries a `:: Type` annotation.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every record field has an explicit `:: Type` annotation.
2. Untyped fields (`{no_type}`) are disallowed.
3. The field type is a core part of the data-structure definition.
4. It is a PR-rejection rule under Records.

# Construction / Recognition

## To Apply

1. Annotate each field: `-record(good, {with_type :: string()})`.

## To Recognize a Violation

1. A record field has no `::` annotation (`-record(bad, {no_type})`).

# Context & Application

A PR-blocking convention under Records.

- **Typical contexts**: every `-record` definition.
- **Common applications**: `#good{with_type :: string()}` — typed for Dialyzer.

# Examples

**Example 1** — bad: `-record(bad, {no_type})`.

**Example 2** — good: `-record(good, {with_type :: string()})`.

# Relationships

## Related

- **Records go first** — companion record-definition rule.
- **Record names** — companion record rule.
- **Write function specs** — both feed Dialyzer with type information.

# Common Errors

- **Error**: Declaring a record field with just a name and no type.
  **Correction**: Add a `:: Type` annotation to every field.

# Common Confusions

- **Confusion**: Believing field types are optional polish.
  **Clarification**: The source frames the field type as "one of the most important parts" of the record definition.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Records", guideline "Types in records".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
