---
concept: Date Lacks Time Zone Support
slug: date-no-time-zone-support
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.2.2 Dates do not support time zones"
extraction_confidence: high
aliases:
  - Date time zone limitation
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

JavaScript's `Date` class does not support arbitrary time zones -- it only supports the local time zone, UTC, and time offsets. This leads to location-specific bugs and makes it impossible to work with multiple time zones.

# Core Definition

"Exploring JavaScript" Ch. 47: "Dates support the following time standards: The local time zone (which depends on the current location), UTC, Time offsets (relative to UTC). Depending on the operation, only some of those options are available." The downsides: "It makes it impossible to support multiple time zones. It can lead to location-specific bugs."

# Prerequisites

- **Date class** -- this is a limitation of the Date class

# Key Properties

1. Only local time zone and UTC are available
2. Cannot specify arbitrary time zones
3. Different locations produce different results for the same code
4. Internally stored as UTC; local time zone used for display
5. Safe practice: use UTC-based operations and append `Z` when parsing
6. Use a date library with time zone support for production code

# Construction / Recognition

```js
// Same code, different results depending on location:
> new Date(2077, 0, 27).toISOString()
'2077-01-26T23:00:00.000Z'  // in CET (UTC+1), day differs!
```

(Ch. 47, Section 47.2.2, lines 163-167)

# Context & Application

This is the primary reason the book recommends using date libraries instead of the built-in Date class.

# Examples

```js
// CEST (summer)
assert.equal(new Date('2122-06-29').getTimezoneOffset(), -120);
// CET (winter)
assert.equal(new Date('2122-12-29').getTimezoneOffset(), -60);
```

(Ch. 47, Section 47.2.2, lines 150-157)

# Relationships

## Builds Upon
- **Date class** -- this is a fundamental limitation

## Related
- **Date time formats** -- appending Z mitigates timezone issues

# Common Errors

- **Error**: Parsing date strings without considering time zone differences
  **Correction**: Always append `Z` for UTC, or explicitly handle local time zone

# Common Confusions

- **Confusion**: `.getTimezoneOffset()` returns the current time zone
  **Clarification**: It returns the offset from UTC in minutes for the specific date (can vary with daylight saving time)

# Source Reference

Chapter 47: Dates (Date), Section 47.2.2, lines 131-197.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section on the limitation
- Cross-reference status: verified
