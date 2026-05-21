---
concept: Abstract Out Common Patterns Of Code Or Behavior
slug: abstract-common-patterns
category: core-idioms
subcategory: sw-engineering-principles
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.6 Abstract out common patterns of code or behavior"
extraction_confidence: high
aliases:
  - "abstract common patterns"
  - "no copy-paste programming"
  - "DRY"
prerequisites: []
extends: []
related:
  - common-code-into-libraries
  - use-generic-server-functions
  - dont-write-long-functions
contrasts_with: []
answers_questions:
  - "What should I do when the same code pattern appears in several places?"
  - "Why is copy-and-paste programming discouraged?"
---

# Quick Definition

When the same pattern of code appears in two or more places, isolate it into a common function and call that instead — avoid copy-and-paste programming.

# Core Definition

"Whenever you have the same pattern of code in two or more places in the code try to isolate this in a common function and call this function instead" (Programming Rules, 3.6). Copied code is costly to maintain. When patterns are *almost* identical, it is worth changing the problem slightly so the cases become the same, then writing a small amount of extra code to describe the differences.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Repeated code patterns are factored into a shared function.
2. Copied code is expensive to maintain.
3. Near-identical patterns are worth reshaping so they become a single, parameterized case.
4. "Avoid 'copy' and 'paste' programming, use functions!"

# Construction / Recognition

## To Apply

1. Spot repeated or near-repeated code patterns.
2. Extract the common part into a function; parameterize the differences.

## To Recognize a Violation

1. The same (or almost the same) block of code appears in two or more places.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: code that grew by duplication.
- **Common applications**: replacing duplicated blocks with calls to one shared function.

# Examples

The source states the principle directly: "Avoid 'copy' and 'paste' programming, use functions!" — no code listing is given.

# Relationships

## Related

- **Put commonly used code into libraries** — abstracted patterns often belong in a library.
- **Use generic functions for servers and protocol handlers** — generic behaviors are large-scale pattern abstraction.
- **Don't write very long functions** — abstraction also shortens functions.

# Common Errors

- **Error**: Copy-pasting a block and tweaking it in place.
  **Correction**: Extract a shared function and parameterize the differences.

# Common Confusions

- **Confusion**: Thinking near-identical code can't be unified.
  **Clarification**: The source advises reshaping the problem slightly so the cases coincide, then describing the small differences.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.6 "Abstract out common patterns of code or behavior".

# Verification Notes

- Definition source: Direct adaptation of section 3.6.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
