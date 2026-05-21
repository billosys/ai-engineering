---
concept: Don't Write Deeply Nested Code
slug: dont-write-deeply-nested-code
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.1 Don't write deeply nested code"
extraction_confidence: high
aliases:
  - "deeply nested code"
  - "two levels of indentation"
prerequisites: []
extends: []
related:
  - dont-write-long-functions
  - common-erlang-programming-mistakes
contrasts_with: []
answers_questions:
  - "How deeply should Erlang code be nested?"
---

# Quick Definition

Don't write deeply nested code — limit most code to about two levels of indentation by breaking it into shorter functions.

# Core Definition

"Nested code is code containing case/if/receive statements within other case/if/receive statements" (Programming Rules, 7.1). Deeply nested code drifts across the page to the right and soon becomes unreadable. Limit most code to a maximum of two levels of indentation; this is achieved by dividing the code into shorter functions.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Nesting means `case`/`if`/`receive` statements inside other `case`/`if`/`receive` statements.
2. Most code should stay within about two levels of indentation.
3. Deep nesting drifts rightward and becomes unreadable.
4. The remedy is dividing the code into shorter functions.

# Construction / Recognition

## To Apply

1. When nesting deepens, extract the inner block into a separate function.

## To Recognize a Violation

1. `case`/`if`/`receive` statements are nested several levels deep in one function.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: functions making several layered decisions.
- **Common applications**: pulling an inner `case` out into its own function.

# Examples

The source states the principle directly; no code listing is given.

# Relationships

## Related

- **Don't write very long functions** — both are cured by extracting shorter functions.
- **The most common mistakes** — deeply nested code is listed among them.

# Common Errors

- **Error**: Nesting `case`/`if`/`receive` several levels deep.
  **Correction**: Extract inner blocks into separate functions.

# Common Confusions

- **Confusion**: Thinking deep nesting is unavoidable for complex logic.
  **Clarification**: Complex logic is better expressed as several short functions than one deeply nested one.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.1 "Don't write deeply nested code".

# Verification Notes

- Definition source: Direct adaptation of section 7.1.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
