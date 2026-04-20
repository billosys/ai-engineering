---
concept: Temporal API
slug: temporal-api
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.1 Best practice: avoid the built-in Date"
extraction_confidence: medium
aliases:
  - TC39 Temporal proposal
prerequisites:
  - date-class
extends: []
related:
  - date-no-time-zone-support
contrasts_with:
  - date-class
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

Temporal is an upcoming ECMAScript date-time API designed to replace the problematic built-in `Date`, offering proper time zone support, immutable objects, and a more intuitive interface. It can already be used via polyfills.

# Core Definition

"Exploring JavaScript" Ch. 47: "Temporal is an upcoming ECMAScript data time API that can already be used via polyfills." It is listed as the first recommendation for date/time functionality, ahead of libraries.

# Prerequisites

- **Date class** -- Temporal is designed to replace it

# Key Properties

1. Upcoming ECMAScript standard (TC39 proposal)
2. Available via polyfills before standardization
3. Designed to address Date's shortcomings (time zones, mutability, confusing API)
4. Will be built into JavaScript platforms

# Construction / Recognition

Not yet standardized. Use via polyfills. See the TC39 proposal at github.com/tc39/proposal-temporal.

# Context & Application

For new projects that need serious date/time handling, consider using Temporal (via polyfill) as the future-proof solution.

# Examples

Referenced in the source but no code examples provided. The source links to the TC39 proposal.

(Ch. 47, Section 47.1, lines 61-62)

# Relationships

## Builds Upon
- **Date class** -- designed as its replacement

## Contrasts With
- **Date class** -- addresses Date's limitations

## Related
- **Date lacks time zone support** -- a problem Temporal solves

# Common Errors

- **Error**: Waiting for standardization before considering Temporal
  **Correction**: Polyfills are available now for projects that need proper date handling

# Common Confusions

- **Confusion**: Temporal is already standardized
  **Clarification**: It is still a TC39 proposal; use polyfills for now

# Source Reference

Chapter 47: Dates (Date), Section 47.1, lines 61-62.

# Verification Notes

- Definition source: brief mention in source text
- Confidence rationale: medium -- briefly referenced, not detailed in source
- Cross-reference status: unverified (external reference)
