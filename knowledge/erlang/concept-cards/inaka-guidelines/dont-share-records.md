---
concept: Don't Share Your Records
slug: dont-share-records
category: data-types
subcategory: records
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Don't share your records"
extraction_confidence: high
aliases:
  - "record sharing"
  - "opaque types for records"
  - "record encapsulation"
prerequisites:
  - lowercase-record-names
extends: []
related:
  - header-file-contents
  - avoid-records-in-specs
  - no-types-in-header-files
  - export-types-for-exported-functions
contrasts_with: []
answers_questions:
  - "Why shouldn't records be shared across modules?"
  - "How do I provide an accessor-based API instead of sharing a record?"
---

# Quick Definition

Don't share records across modules; expose shared objects as opaque exported types with accessor functions instead.

# Core Definition

"Records should not be shared among multiple modules. If you need to share objects that are represented as records, use opaque exported types and provide adequate accessor functions in your module" (Inaka, "Don't share your records"). The record stays internal to its owning module; other modules see an opaque type and call accessors.

# Prerequisites

- **Record names** — sharing-avoidance still presupposes correctly named records.

# Key Properties

1. A record definition stays internal to one module.
2. Shared objects are exposed via an `-opaque` type with `-export_type`.
3. The owning module provides accessor/constructor functions for the type.
4. Sharing a record through a `.hrl` increases coupling and breaks encapsulation.

# Construction / Recognition

## To Apply

1. Define the record in exactly one module.
2. Declare `-opaque good() :: #good{}` and `-export_type([good/0])`.
3. Provide accessor and update functions (`good_field/1`, `good_field/2`).

## To Recognize a Violation

1. A record is defined in a `.hrl` and `-include`d by several modules.
2. A module references a record type (`#bad{}`) it does not define.

# Context & Application

A PR-blocking convention under Records.

- **Typical contexts**: domain objects passed between modules.
- **Common applications**: an opaque `good()` type with `good/0`, `good_field/1`, `good_field/2` accessors.

# Examples

**Example 1** — good: `-record(good, {...})` plus `-opaque good() :: #good{}`, `-export_type([good/0])`, and accessor functions.

**Example 2** — bad: `-spec bad() -> #bad{}` references a record `#bad{}` defined elsewhere (shared via header).

# Relationships

## Builds Upon

- **Record names** — well-named records are the input to this encapsulation rule.

## Related

- **Header files** — records must not be shared through headers.
- **Avoid records in specs** — the opaque type replaces raw records in specs.
- **No types in include files** — corollary about not sharing types via headers.
- **Types in exported functions** — the exported opaque type is what the API exposes.

# Common Errors

- **Error**: Putting a record in a `.hrl` so multiple modules can pattern-match it.
  **Correction**: Keep the record private; export an opaque type and accessors.

# Common Confusions

- **Confusion**: Believing shared records are a convenience.
  **Clarification**: They couple modules to internal structure; a structural change then forces edits everywhere the header reached.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Records", guideline "Don't share your records".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
