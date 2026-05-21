---
concept: Types In Exported Functions
slug: export-types-for-exported-functions
category: api-design
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Types in exported functions"
extraction_confidence: high
aliases:
  - "exported function types"
  - "export_type for API types"
prerequisites: []
extends: []
related:
  - write-function-specs
  - avoid-records-in-specs
  - dont-share-records
  - no-types-in-header-files
contrasts_with: []
answers_questions:
  - "Should custom data types used in exported functions be declared and exported?"
---

# Quick Definition

Custom data types used in exported functions should be defined with Erlang type declarations and exported from the module.

# Core Definition

"Custom data types used in exported functions should be defined with Erlang type declarations and exported from the module" (Inaka, "Types in exported functions"). Rather than spelling out an ad-hoc type inline in a spec, declare a named `-type` (or `-opaque`) and `-export_type` it.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Custom types in exported functions' specs are declared as named `-type`/`-opaque`.
2. Those types are made available with `-export_type`.
3. Using `-opaque` for them adds encapsulation.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Declare `-type your_type() :: ...` (or `-opaque my_type() :: ...`).
2. `-export_type([your_type/0, my_type/0])`.
3. Reference the named types in the exported functions' specs.

## To Recognize a Candidate

1. An exported function's spec inlines a structural type (`{integer(), string()}`) instead of a named one.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: module public APIs that pass around custom data structures.
- **Common applications**: `-spec good(your_type()) -> {ok, my_type()}` with both types declared and exported.

# Examples

**Example 1** — bad: `-spec bad({integer(), string()}) -> {ok, {binary(), binary()}}` — the structural types are inlined.

**Example 2** — good: `-type your_type() :: {integer(), string()}` and `-opaque my_type() :: {binary(), binary()}`, both `-export_type`d, used in `-spec good(your_type()) -> {ok, my_type()}`.

# Relationships

## Related

- **Write function specs** — this rule shapes the types those specs reference.
- **Avoid records in specs** — same preference for named, exportable types over raw structures.
- **Don't share your records** — exported opaque types are the sharing mechanism that replaces shared records.
- **No types in include files** — exported module types are how types are shared without headers.

# Common Errors

- **Error**: Inlining a tuple type in an exported function's spec.
  **Correction**: Declare a named type and `-export_type` it.

# Common Confusions

- **Confusion**: Thinking inline structural types in specs are equivalent.
  **Clarification**: Named, exported types document the API and, when `-opaque`, enforce encapsulation.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Types in exported functions".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
