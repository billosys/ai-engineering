---
concept: Get Your Types Together
slug: types-at-top-of-module
category: data-types
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Get your types together"
extraction_confidence: high
aliases:
  - "get your types together"
  - "types at the beginning of the file"
prerequisites: []
extends: []
related:
  - records-before-functions
  - group-functions-logically
  - write-function-specs
contrasts_with: []
answers_questions:
  - "Where should -type definitions go in an Erlang module?"
  - "How does \"get your types together\" relate to \"records go first\"?"
---

# Quick Definition

Place all `-type` definitions together at the beginning of the module file.

# Core Definition

"Place all types at the beginning of the file" (Inaka, "Get your types together"). Type declarations are collected as a block near the top of the module rather than scattered next to the functions that happen to use them.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. All `-type`/`-opaque` declarations are grouped at the top of the file.
2. Types are not interleaved with the functions that use them.
3. It mirrors how `edoc` renders documentation — types first.
4. It is a PR-rejection rule under Source Code Layout.

# Construction / Recognition

## To Apply

1. Move every `-type` declaration above the first function body.
2. Keep the type block together, optionally before or after record definitions.

## To Recognize a Violation

1. A `-type` declaration appears between two functions, tied visually to just one of them.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: modules that define several shared types.
- **Common applications**: a type block placed just below the `-export` directives.

# Examples

**Example 1** — good: `good_type()` is declared before `good/0`, in the module's type block.

**Example 2** — bad: `bad_type()` is declared immediately above `bad/0`, tying it to a single function.

# Relationships

## Related

- **Records go first** — the companion rule for record definitions.
- **Group functions logically** — same top-down module-organization principle.
- **Write function specs** — specs reference these centrally defined types.

# Common Errors

- **Error**: Declaring a type right before the one function that currently uses it.
  **Correction**: Move it into the module's type block; types are usually shared by multiple functions.

# Common Confusions

- **Confusion**: Thinking a type "belongs to" the first function that uses it.
  **Clarification**: Types define data structures used across the module; their placement is module-level, not function-level.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Get your types together".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
