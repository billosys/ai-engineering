---
concept: Record Names
slug: lowercase-record-names
category: data-types
subcategory: records
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Record names"
extraction_confidence: high
aliases:
  - "record naming"
  - "record field naming"
prerequisites: []
extends:
  - lowercase-atoms
related:
  - records-before-functions
  - type-record-fields
  - explicit-state-record-naming
contrasts_with: []
answers_questions:
  - "How should records and record fields be named in Erlang?"
---

# Quick Definition

Record names and record field names use only lowercase characters, with words separated by underscores.

# Core Definition

"Record names must use only lowercase characters. Words in record names must be separated with `_`. Same rule applies to record field names" (Inaka, "Record names"). Because record and field names are atoms, the atom-naming rule applies to them.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Record names are lowercase `snake_case`.
2. Record field names are lowercase `snake_case`.
3. Record/field names are atoms, so the atom rule governs them.
4. It is a PR-rejection rule under Records.

# Construction / Recognition

## To Apply

1. Define `-record(good_name, {good_field_name :: any()})`.

## To Recognize a Violation

1. A record or field name uses camelCase or uppercase (`#badName{}`, `badFieldName`, `#'UPPERCASE'{}`).

# Context & Application

A PR-blocking convention under Records.

- **Typical contexts**: every `-record` definition.
- **Common applications**: `#good_name{good_field_name = ...}`.

# Examples

**Example 1** — bad: `-record(badName, {})`, `-record(bad_field_name, {badFieldName :: any()})`, `-record('UPPERCASE', {'THIS_IS_BAD' :: any()})`.

**Example 2** — good: `-record(good_name, {good_field_name :: any()})`.

# Relationships

## Builds Upon

- **Lowercase atoms** — record/field names are atoms; this applies the atom rule.

## Related

- **Records go first** — companion record rule.
- **Types in records** — companion record rule.
- **Explicit state should be explicitly named** — the state record obeys this naming rule.

# Common Errors

- **Error**: Naming a record `#userAccount{}`.
  **Correction**: Use `#user_account{}`.

# Common Confusions

- **Confusion**: Treating record naming as independent of atom rules.
  **Clarification**: Record and field names are atoms; the atom rule is the source of this one.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Records", guideline "Record names".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
