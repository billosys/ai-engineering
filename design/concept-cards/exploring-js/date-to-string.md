---
concept: Date to String Conversion
slug: date-to-string
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.7 Converting Dates to strings"
extraction_confidence: high
aliases:
  - Date formatting
  - toISOString
prerequisites:
  - date-class
extends: []
related:
  - date-time-formats
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

Dates can be converted to strings via several methods: `.toISOString()` (UTC, machine-readable), `.toString()` (local time, human-readable), `.toUTCString()` (UTC, human-readable), and Intl API methods for locale-specific formatting.

# Core Definition

"Exploring JavaScript" Ch. 47 lists conversion methods: `.toTimeString()` (local), `.toDateString()` (local), `.toString()` (local), `.toUTCString()` (UTC), `.toISOString()` (UTC, ISO format). The Intl API methods `.toLocaleTimeString()`, `.toLocaleDateString()`, `.toLocaleString()` provide locale-aware formatting with time zone support.

# Prerequisites

- **Date class** -- these are Date instance methods

# Key Properties

1. `.toISOString()`: UTC, ISO 8601 format, e.g., `'1970-01-01T00:00:00.000Z'`
2. `.toString()`: local time zone, e.g., `'Thu Jan 01 1970 01:00:00 GMT+0100'`
3. `.toUTCString()`: UTC, e.g., `'Thu, 01 Jan 1970 00:00:00 GMT'`
4. `.toDateString()`: local, date only
5. `.toTimeString()`: local, time only
6. Intl API methods for locale-specific formatting (separate API)

# Construction / Recognition

```js
const d = new Date(0);
d.toISOString()    // '1970-01-01T00:00:00.000Z'
d.toString()       // 'Thu Jan 01 1970 01:00:00 GMT+0100 (CET)'
d.toUTCString()    // 'Thu, 01 Jan 1970 00:00:00 GMT'
```

(Ch. 47, Section 47.7, lines 466-531)

# Context & Application

`.toISOString()` for machine-readable serialization; `.toString()` for debugging; Intl API for user-facing display.

# Examples

See construction examples above. (Ch. 47, Section 47.7, lines 466-520)

# Relationships

## Builds Upon
- **Date class** -- instance methods for conversion

## Related
- **Date time formats** -- `.toISOString()` uses ISO format

# Common Errors

- **Error**: Using `.toString()` for serialization/storage
  **Correction**: Use `.toISOString()` for portable, parseable format

# Common Confusions

- **Confusion**: All toString methods use the same time zone
  **Clarification**: `.toISOString()` and `.toUTCString()` use UTC; others use local time zone

# Source Reference

Chapter 47: Dates (Date), Section 47.7, lines 466-531.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit listing of all methods
- Cross-reference status: verified
