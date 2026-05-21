---
# === CORE IDENTIFICATION ===
concept: Reference
slug: reference

# === CLASSIFICATION ===
category: data-types
subcategory: atomic-data
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "References"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erlang:make_ref()"
  - unique reference
  - ref

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - term-comparison
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reference in Erlang?"
  - "How do I create a unique reference?"
  - "What are references used for?"
---

# Quick Definition

A reference is a globally unique Erlang term created with `erlang:make_ref()`, useful as a unique tag that can later be compared for equality.

# Core Definition

"*References* are globally unique Erlang terms. They are created with the BIF `erlang:make_ref()`. References are useful for creating unique tags that can be included in data and then at a later stage compared for equality" ("The Rest of Sequential Erlang", *References*). The book gives the example of a bug-tracking system that adds a reference to each new bug report to give it a unique identity.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A reference is a globally unique Erlang term.
2. Created with the BIF `erlang:make_ref()`.
3. Useful as a unique tag embedded in data structures.
4. Two references can be compared for equality at a later stage.
5. References occupy a fixed position in the term total order (between atom and fun).

# Construction / Recognition

## To Construct/Create:
1. Call `erlang:make_ref()` to obtain a fresh unique reference.

## To Identify/Recognize:
1. A reference is a distinct term type; equality comparison distinguishes one reference from another.

# Context & Application

- **Typical contexts**: generating unique identities for items in data.
- **Common applications**: a bug-tracking system tagging each bug report with a reference for unique identity.
- **Historical/stylistic notes**: in the term ordering, `reference` ranks between `atom` and `fun`.

# Examples

**Example 1** (*References*): a bug-tracking system can add a reference (from `erlang:make_ref()`) to each new bug report so the report has a unique identity that can later be compared for equality.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Term comparison** — References occupy a fixed slot in the total ordering of terms.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Reusing a single reference where unique identities are needed.
  **Correction**: Call `erlang:make_ref()` each time a new unique tag is required.

# Common Confusions

- **Confusion**: Thinking a reference is a pointer to a value.
  **Clarification**: A reference is simply a globally unique term used as a tag; it does not point to or alias other data.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "References".

# Verification Notes

- Definition source: Direct quotation from *References*.
- Confidence rationale: HIGH — the source explicitly defines references and their creation BIF.
- Uncertainties: None.
- Cross-reference status: Slug `term-comparison` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
