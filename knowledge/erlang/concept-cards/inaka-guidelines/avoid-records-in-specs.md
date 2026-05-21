---
concept: Avoid Records In Specs
slug: avoid-records-in-specs
category: data-types
subcategory: records
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Avoid records in specs"
extraction_confidence: high
aliases:
  - "records in specs"
  - "use types not records in specs"
prerequisites: []
extends: []
related:
  - dont-share-records
  - write-function-specs
  - explicit-state-record-naming
  - export-types-for-exported-functions
contrasts_with: []
answers_questions:
  - "Should I use #record{} or a type in my -spec declarations?"
---

# Quick Definition

Avoid using raw records in `-spec` declarations; use a defined type instead.

# Core Definition

"Avoid using records in your specs, use types" (Inaka, "Avoid records in specs"). Rather than writing `-spec f(#state{}) -> ...`, define `-opaque state() :: #state{}` and write `-spec f(state()) -> ...`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A `-spec` references a named type, not a bare `#record{}`.
2. The type (often `-opaque`) is defined for the record and can be exported.
3. Using a type aids documentation and, with `-opaque`, encapsulation and abstraction.
4. It is a PR-rejection rule under Records.

# Construction / Recognition

## To Apply

1. Define `-opaque state() :: #state{}` (and `-export_type` it if part of the API).
2. Write specs in terms of `state()`.

## To Recognize a Violation

1. A `-spec` mentions `#record{}` directly.

# Context & Application

A PR-blocking convention under Records.

- **Typical contexts**: specs of functions that take or return a record.
- **Common applications**: `-spec good(state()) -> {any(), state()}` instead of `-spec bad(#state{}) -> {any(), #state{}}`.

# Examples

**Example 1** — bad: `-spec bad(#state{}) -> {any(), #state{}}`.

**Example 2** — good: `-spec good(state()) -> {any(), state()}` with `-opaque state() :: #state{}` defined and exported.

# Relationships

## Related

- **Don't share your records** — the opaque type both rules rely on.
- **Write function specs** — this rule shapes *how* specs are written.
- **Explicit state should be explicitly named** — the `state()` type is the canonical example.
- **Types in exported functions** — exported types are what specs should reference.

# Common Errors

- **Error**: Writing `-spec f(#state{}) -> ...` with a bare record.
  **Correction**: Define and use a `state()` type.

# Common Confusions

- **Confusion**: Thinking records and types are interchangeable in specs.
  **Clarification**: Only types can be exported and made opaque — records in specs forfeit both benefits.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Records", guideline "Avoid records in specs".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
