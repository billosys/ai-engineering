---
concept: No Types In Include Files
slug: no-types-in-header-files
category: data-types
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "No types in include files"
extraction_confidence: high
aliases:
  - "no -type in hrl"
  - "types not in headers"
prerequisites: []
extends:
  - header-file-contents
related:
  - dont-share-records
  - no-nested-header-inclusion
  - export-types-for-exported-functions
contrasts_with: []
answers_questions:
  - "Why shouldn't -type definitions go in header files?"
  - "Where should types be defined so other modules can use them?"
---

# Quick Definition

Don't put `-type` definitions in `.hrl` header files; define types in their owning modules and export them.

# Core Definition

"No `-type` in hrl files" (Inaka, "No types in include files"). Types defined in public headers can clash across projects and modules; instead, define each type in the module it corresponds to, use `-export_type`, and reference it as `some_mod:some_type()`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. No `-type`/`-opaque` definitions appear in `.hrl` files.
2. Types are defined in their owning module and exported with `-export_type`.
3. Module namespacing (`mod:type()`) prevents the name clashes headers risk.
4. Module-defined types can be `-opaque`, which benefits Dialyzer.

# Construction / Recognition

## To Apply

1. Define each type in the module that owns its data.
2. `-export_type([id/0, type/0])` so other modules can reference `module:id()`.

## To Recognize a Violation

1. A `.hrl` file contains a `-type` declaration.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: shared `include/` directories, especially headers used via `-include_lib`.
- **Common applications**: `-type id() :: pos_integer()` defined and exported from a `types` module, referenced as `types:id()`.

# Examples

**Example 1** — bad: a `bad_types.hrl` included for its `-type` definitions.

**Example 2** — good: `-type id() :: pos_integer()` and `-opaque type() :: #type{}` defined in the module and `-export_type`d; callers write `types:id()` with no include.

# Relationships

## Builds Upon

- **Header files** — this is the type-specific case of the headers-content rule.

## Related

- **Don't share your records** — the parallel rule for records.
- **No nested header inclusion** — companion header-hygiene rule.
- **Types in exported functions** — module-defined exported types are how the API exposes types.

# Common Errors

- **Error**: Placing shared types in a `.hrl` for `-include_lib` reuse.
  **Correction**: Define them in their module and `-export_type`; reference `module:type()`.

# Common Confusions

- **Confusion**: Thinking header-defined types are a convenient way to share.
  **Clarification**: They invite name clashes and forfeit `-opaque`; module namespacing solves sharing cleanly.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "No types in include files".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
