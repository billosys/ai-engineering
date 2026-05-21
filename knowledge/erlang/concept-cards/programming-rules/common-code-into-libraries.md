---
concept: Put Commonly Used Code Into Libraries
slug: common-code-into-libraries
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.3 Put commonly used code into libraries"
extraction_confidence: high
aliases:
  - "libraries of related functions"
  - "cohesive libraries"
prerequisites: []
extends: []
related:
  - reduce-intermodule-dependencies
  - abstract-common-patterns
  - eliminate-side-effects
contrasts_with: []
answers_questions:
  - "How should commonly used code be organized into libraries?"
  - "Why should library functions avoid side effects?"
---

# Quick Definition

Collect commonly used code into libraries, each library a cohesive collection of functions of the same type; the best library functions have no side effects.

# Core Definition

"Commonly used code should be placed into libraries. The libraries should be collections of related functions" (Programming Rules, 3.3). A library such as `lists` (only list functions) is a good choice; a `lists_and_maths` library mixing unrelated functions is a bad one. The best library functions have no side effects — side effects limit re-usability.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Common code is collected into libraries.
2. Each library is cohesive — its functions are all of the same type.
3. Mixing unrelated function families in one library is a bad choice.
4. Side-effect-free library functions are the most re-usable.

# Construction / Recognition

## To Apply

1. Group commonly used functions by type into focused libraries.
2. Prefer pure (side-effect-free) functions in libraries.

## To Recognize a Violation

1. A library mixes unrelated function families (e.g. list manipulation plus mathematics).

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: building shared utility modules.
- **Common applications**: a `lists`-style library of only list functions.

# Examples

**Example** (from source): `lists` (only list-manipulating functions) is a good library; `lists_and_maths` (lists plus maths) is "a very bad choice".

# Relationships

## Related

- **Try to reduce intermodule dependencies** — well-organized libraries reduce ad-hoc coupling.
- **Abstract out common patterns of code or behavior** — abstracted patterns belong in libraries.
- **Try to eliminate side effects** — side-effect-free library functions are most re-usable.

# Common Errors

- **Error**: Creating a grab-bag "utils" library of unrelated functions.
  **Correction**: Split it into cohesive, single-type libraries.

# Common Confusions

- **Confusion**: Thinking any reused code belongs in one shared library.
  **Clarification**: Reuse is best served by *cohesive* libraries; mixing types harms discoverability and reuse.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.3 "Put commonly used code into libraries".

# Verification Notes

- Definition source: Direct adaptation of section 3.3.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
