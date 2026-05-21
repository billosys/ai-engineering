---
concept: Header File Contents
slug: header-file-contents
category: data-types
subcategory: source-code-layout
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Header files"
extraction_confidence: high
aliases:
  - "header files"
  - "hrl contents"
  - "what belongs in a .hrl"
prerequisites: []
extends: []
related:
  - no-types-in-header-files
  - dont-share-records
  - avoid-macros
  - no-nested-header-inclusion
contrasts_with: []
answers_questions:
  - "What is allowed in an Erlang header (.hrl) file?"
  - "Why shouldn't records and types go in header files?"
---

# Quick Definition

Header files should not contain type, record, or function definitions; they may contain macro definitions, though macros themselves should be avoided.

# Core Definition

Per Inaka's "Header files" guideline, `.hrl` files SHOULD NOT include type definitions, record definitions, or function definitions, and MAY include macro definitions — although macros should be avoided. Types belong in the modules that own the data; records should be defined in their owning module behind an opaque type with accessor functions; function definitions in headers cause code duplication.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. No `-type`/`-opaque` definitions in headers.
2. No `-record` definitions in headers.
3. No function definitions in headers.
4. Macro definitions are permitted but discouraged.

# Construction / Recognition

## To Apply

1. Move type definitions into their owning modules (use module-prefixed types in specs).
2. Move record definitions into their owning module behind an opaque exported type with accessors.
3. Never place function bodies in a `.hrl`.

## To Recognize a Violation

1. A `.hrl` defines a record, a `-type`, or a function.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: shared `include/` directories.
- **Common applications**: a header containing only a small, justified macro such as `-define(COOKIE, <<"Cookie: ">>).`

# Examples

**Example 1** — bad: a header defining `#nasty_non_encapsulated_record{}`, a `who_knows_what_this_is()` type, and a `cool_function_everyone_uses/1` function.

**Example 2** — OK: a header containing only `-define(COOKIE, <<"Cookie: ">>).`

# Relationships

## Related

- **No types in include files** — the type-specific corollary of this rule.
- **Don't share your records** — records belong in their owning module, not a shared header.
- **Avoid macros** — even the permitted macro use is discouraged.
- **No nested header inclusion** — companion rule for the headers you do keep.

# Common Errors

- **Error**: Putting a shared `#state{}` record in a `.hrl` so several modules can use it.
  **Correction**: Define the record in one module behind an opaque type with accessor functions.

# Common Confusions

- **Confusion**: Believing headers exist to share records and types.
  **Clarification**: Module-prefixed types and opaque types make header sharing unnecessary and harmful to encapsulation.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Header files".

# Verification Notes

- Definition source: Adapted from the guideline's MUST NOT / MAY list and reasoning.
- Confidence rationale: HIGH — explicit rule with bad/OK examples and detailed reasoning.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
