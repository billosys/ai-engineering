---
concept: Don't Import
slug: dont-use-import
category: core-idioms
subcategory: misc
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Don't import"
extraction_confidence: high
aliases:
  - "no -import"
  - "import directive"
prerequisites: []
extends: []
related:
  - dont-use-export-all
  - explicit-mixer-functions
contrasts_with: []
answers_questions:
  - "Why shouldn't I use the -import directive in Erlang?"
---

# Quick Definition

Do not use the `-import` directive.

# Core Definition

"Do not use the `-import` directive" (Inaka, "Don't import"). Functions from other modules are always called with their module prefix (`lists:map(...)`), never imported into the local namespace.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The `-import` directive is not used.
2. External functions are always called fully qualified (`module:function(...)`).
3. The module prefix is part of the function's meaning.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Call external functions as `module:function(Args)`.

## To Recognize a Violation

1. The module contains an `-import(...)` directive.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: any module calling functions from other modules.
- **Common applications**: `lists:map(fun(X) -> X * 2 end, L)` rather than an imported `map/2`.

# Examples

**Example 1** — bad: `-import(lists, [map/2])` then `map(fun(X) -> X * 2 end, L)`.

**Example 2** — good: `lists:map(fun(X) -> X * 2 end, L)`.

# Relationships

## Related

- **Don't export_all** — companion rule on explicit, visible module boundaries.
- **No implicit functions with mixer** — same preference for explicit, visible function origins.

# Common Errors

- **Error**: Importing a few helpers to shorten call sites.
  **Correction**: Keep the module prefix; it disambiguates local from external functions.

# Common Confusions

- **Confusion**: Thinking `-import` improves readability.
  **Clarification**: It removes the visual cue that distinguishes local calls from external ones, making code harder to read and debug.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Don't import".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
