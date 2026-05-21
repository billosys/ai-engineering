---
concept: Group Functions Logically
slug: group-functions-logically
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Group functions logically"
extraction_confidence: high
aliases:
  - "exported functions first"
  - "separate public and private functions"
prerequisites: []
extends: []
related:
  - types-at-top-of-module
  - records-before-functions
  - no-god-modules
contrasts_with: []
answers_questions:
  - "How do I lay out exported vs. unexported functions within a module?"
  - "Should public or private functions come first in a module?"
---

# Quick Definition

Separate exported and unexported functions into groups, with exported functions first — unless local proximity helps readability and code discovery.

# Core Definition

"Try to always separate **unexported** and **exported** functions in groups, with the exported ones first, unless it helps readability and code discovery" (Inaka, "Group functions logically"). The default layout is public API at the top, private helpers below; the escape hatch is when keeping a small private helper next to its single caller aids comprehension.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Exported and unexported functions form distinct groups.
2. Exported functions appear first by default.
3. A private helper used by exactly one public function may sit next to that caller.
4. A comment banner is often used to mark the start of the private section.

# Construction / Recognition

## To Apply

1. Place all exported (API) functions at the top of the module.
2. Place private helpers below, optionally under a `%%% PRIVATE FUNCTIONS %%%` banner.
3. As an exception, keep a one-caller helper immediately after its caller when that improves discovery.

## To Recognize a Violation

1. Public and private functions are interleaved with no organizing principle.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: every non-trivial module.
- **Common applications**: the `good.erl` example uses a `PRIVATE FUNCTIONS` comment banner.

# Examples

**Example 1** — bad (`bad.erl`): public and private functions are mixed in arbitrary order.

**Example 2** — "better" (`better.erl`): a private helper related only to the function above it is kept adjacent.

**Example 3** — good (`good.erl`): exported functions first, then a banner, then all private functions.

# Relationships

## Related

- **Get your types together** — same "organize the module top-down" principle applied to types.
- **Records go first** — same principle applied to records.
- **No God modules** — both concern keeping a module navigable.

# Common Errors

- **Error**: Scattering private helpers throughout the public API with no grouping.
  **Correction**: Collect them into a clearly delimited private section.

# Common Confusions

- **Confusion**: Treating "exported first" as absolute.
  **Clarification**: The source explicitly allows a private helper near its sole caller when it aids readability.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Group functions logically".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with three example files.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
