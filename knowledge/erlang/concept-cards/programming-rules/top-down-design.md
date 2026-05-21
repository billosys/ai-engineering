---
concept: Write Programs Top-Down
slug: top-down-design
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.7 Top-down"
extraction_confidence: high
aliases:
  - "top-down"
  - "top-down design"
prerequisites: []
extends: []
related:
  - abstract-common-patterns
  - dont-leak-private-data-structures
contrasts_with: []
answers_questions:
  - "Should I write Erlang programs top-down or bottom-up?"
---

# Quick Definition

Write programs top-down — starting from the high-level structure and successively approaching details — rather than bottom-up from primitives.

# Core Definition

"Write your program using the top-down fashion, not bottom-up (starting with details)" (Programming Rules, 3.7). Top-down development successively approaches implementation details, ending with the definition of primitive functions. Because the data representation is not yet known when the higher levels are designed, the higher-level code stays independent of representation.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Development proceeds from high-level structure down to primitive functions.
2. Details are approached successively, not started with.
3. Higher-level code is independent of data representation, since representation is decided later.

# Construction / Recognition

## To Apply

1. Design the high-level structure first.
2. Refine downward, defining primitive functions last.

## To Recognize a Violation

1. Development starts from low-level primitives before the overall structure exists.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: starting a new module or subsystem.
- **Common applications**: sketching top-level functions in terms of not-yet-written helpers.

# Examples

The source states the principle directly; no code example is given.

# Relationships

## Related

- **Abstract out common patterns of code or behavior** — top-down work surfaces shared patterns.
- **Don't allow private data structure to leak out of a module** — top-down design keeps higher levels representation-independent.

# Common Errors

- **Error**: Building low-level primitives before the structure that uses them.
  **Correction**: Design top-down; let primitive functions fall out last.

# Common Confusions

- **Confusion**: Thinking representation must be fixed early.
  **Clarification**: Top-down design deliberately defers representation, keeping high-level code independent of it.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.7 "Top-down".

# Verification Notes

- Definition source: Direct adaptation of section 3.7.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
