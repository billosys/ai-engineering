---
concept: Write Function Specs
slug: write-function-specs
category: api-design
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Write function specs"
extraction_confidence: high
aliases:
  - "function specs"
  - "-spec declarations"
  - "type specifications"
prerequisites: []
extends: []
related:
  - types-at-top-of-module
  - avoid-records-in-specs
  - type-record-fields
  - export-types-for-exported-functions
contrasts_with: []
answers_questions:
  - "How do I write -specs for exported functions?"
  - "How do function specs relate to Dialyzer?"
---

# Quick Definition

Write `-spec`s for all exported functions, and for unexported ones when it adds real documentation value; define as many types as needed.

# Core Definition

"Write the **-spec**'s for your exported fun's, and for unexported fun's when it adds real value for documentation purposes. Define as many types as needed" (Inaka, "Write function specs"). Specs give Dialyzer and human readers semantically meaningful type information.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every exported function has a `-spec`.
2. Unexported functions get a `-spec` when it documents non-obvious behavior.
3. As many `-type` definitions as needed are introduced to name argument/return types.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Add a `-spec` line directly above each exported function.
2. Introduce named types (e.g., `-type command() :: inc | dec`) for non-trivial arguments.

## To Recognize a Violation

1. An exported function has no `-spec`.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: module public APIs.
- **Common applications**: `-spec good(pos_integer(), [command()]) -> pos_integer()` with `command()` defined.

# Examples

**Example 1** — bad: `bad/2` is exported with no `-spec`.

**Example 2** — good: `-type command() :: inc | dec` plus `-spec good(pos_integer(), [command()]) -> pos_integer()`.

# Relationships

## Related

- **Get your types together** — the named types specs use live in the module's type block.
- **Avoid records in specs** — shapes what specs reference.
- **Types in records** — both supply Dialyzer with type information.
- **Types in exported functions** — exported functions' custom types must be declared and exported.

# Common Errors

- **Error**: Exporting a function with no spec.
  **Correction**: Add a `-spec`; introduce named types for non-obvious arguments.

# Common Confusions

- **Confusion**: Thinking specs are only for tooling.
  **Clarification**: They also document intent — semantically loaded type names make a function's purpose clearer to readers.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Write function specs".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
