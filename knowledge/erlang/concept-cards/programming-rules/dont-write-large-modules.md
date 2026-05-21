---
concept: Don't Write Very Large Modules
slug: dont-write-large-modules
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.2 Don't write very large modules"
extraction_confidence: high
aliases:
  - "large modules"
  - "400 lines per module"
prerequisites: []
extends: []
related:
  - dont-write-long-functions
  - reduce-intermodule-dependencies
contrasts_with: []
answers_questions:
  - "How large should an Erlang module be?"
---

# Quick Definition

Don't write very large modules — a module should not exceed about 400 lines of source code.

# Core Definition

"A module should not contain more than 400 lines of source code. It is better to have several small modules than one large one" (Programming Rules, 7.2).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A module should not exceed roughly 400 lines of source code.
2. Several small modules are preferred over one large module.

# Construction / Recognition

## To Apply

1. When a module approaches 400 lines, split it into smaller, cohesive modules.

## To Recognize a Violation

1. A module's source exceeds about 400 lines.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: modules that grew by accretion.
- **Common applications**: splitting an oversized module along functional lines.

# Examples

The source states the numeric limit directly; no code listing is given.

# Relationships

## Related

- **Don't write very long functions** — the function-level analogue of this size limit.
- **Try to reduce intermodule dependencies** — splitting modules should not create a tangle of dependencies.

# Common Errors

- **Error**: Letting a module grow well past 400 lines.
  **Correction**: Split it into several smaller modules.

# Common Confusions

- **Confusion**: Treating 400 lines as an exact hard limit.
  **Clarification**: It is a guideline figure; the intent is that small modules beat one large one.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.2 "Don't write very large modules".

# Verification Notes

- Definition source: Direct adaptation of section 7.2.
- Confidence rationale: HIGH — the rule is stated explicitly with a numeric limit.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
