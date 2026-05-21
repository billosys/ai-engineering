---
concept: No Nested Header Inclusion
slug: no-nested-header-inclusion
category: core-idioms
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "No nested header inclusion"
extraction_confidence: high
aliases:
  - "nested header inclusion"
  - "include guards"
  - "ifndef header guard"
prerequisites: []
extends: []
related:
  - header-file-contents
  - no-types-in-header-files
contrasts_with: []
answers_questions:
  - "How do I avoid nested header-inclusion conflicts?"
  - "How do I make a header includable in any order?"
---

# Quick Definition

When headers include other headers, guard each with `-ifndef(HEADER_FILE_HRL) ... -endif` so they can be included in any order without conflicts.

# Core Definition

"When having many nested 'include files', use `-ifndef(HEADER_FILE_HRL) .... -endif` so they can be included in any order without conflicts" (Inaka, "No nested header inclusion"). An include guard makes a header idempotent under repeated or out-of-order inclusion.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each header is wrapped in an `-ifndef/-define/-endif` include guard.
2. The guard makes inclusion order and repetition harmless.
3. Unguarded nested `-include` directives can duplicate inclusions and cause conflicts.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. At the top of a header, write `-ifndef(HEADER_FILE_HRL).` and `-define(HEADER_FILE_HRL, true).`
2. Close the file with `-endif.`

## To Recognize a Violation

1. A header that `-include`s other headers has no `-ifndef` guard.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: projects with headers that include other headers.
- **Common applications**: include guards on every `.hrl` in a nested-include graph.

# Examples

The source links an example header (`include/nested.hrl`) rather than inlining code; it demonstrates the `-ifndef/-define/-endif` guard pattern.

# Relationships

## Related

- **Header files** — governs what headers may contain; this rule governs how they include each other.
- **No types in include files** — companion header-hygiene rule.

# Common Errors

- **Error**: Letting headers `-include` each other with no guards.
  **Correction**: Add an `-ifndef` include guard to every header.

# Common Confusions

- **Confusion**: Thinking inclusion order can simply be managed by hand.
  **Clarification**: The guard removes the ordering problem entirely and hides nothing from the developer.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "No nested header inclusion".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule; the source's example is a linked file rather than inline code (noted above).
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
