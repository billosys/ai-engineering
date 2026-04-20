---
concept: Date Creation
slug: date-creation
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.5 Creating Dates"
extraction_confidence: high
aliases:
  - creating Date objects
  - Date constructor
prerequisites:
  - date-class
extends: []
related:
  - date-time-values
  - date-time-formats
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

Dates can be created four ways: from numbers (`new Date(year, month, ...)` in local time zone), from strings (`new Date(dateTimeStr)` with time zone depending on format), from time values (`new Date(milliseconds)` in UTC), and for the current time (`new Date()` in UTC).

# Core Definition

"Exploring JavaScript" Ch. 47 describes four creation methods. From numbers: `new Date(year, month, date?, hours?, minutes?, seconds?, milliseconds?)` uses local time zone with 0-indexed months. From strings: `new Date(dateTimeStr)` where time zone depends on whether `Z` is appended. From time values: `new Date(timeValue)` is UTC. Current time: `new Date()` is `new Date(Date.now())`.

# Prerequisites

- **Date class** -- these are Date construction methods

# Key Properties

1. Numbers: local time zone, months are 0-indexed (0=January)
2. Strings: time zone depends on format (Z=UTC, no Z=local, date-only=UTC)
3. Time values: UTC, milliseconds since epoch
4. No arguments: current time
5. Pitfall: years 0-99 have 1900 added

# Construction / Recognition

```js
new Date(2077, 0, 27)              // Jan 27, 2077 (local)
new Date('2077-01-27T00:00Z')      // Jan 27, 2077 (UTC)
new Date('2077-01-27')             // Jan 27, 2077 (UTC, date-only)
new Date(0)                        // 1970-01-01T00:00:00.000Z
new Date()                         // current time
```

(Ch. 47, Section 47.5, lines 342-416)

# Context & Application

Understanding the different time zone behaviors of each creation method is critical for avoiding bugs.

# Examples

From the source:
```js
> new Date(2077, 0, 27, 21, 49).toISOString() // CET (UTC+1)
'2077-01-27T20:49:00.000Z'  // note: hours differ
```

(Ch. 47, Section 47.5.1, lines 366-369)

# Relationships

## Builds Upon
- **Date class** -- creation methods for Date

## Related
- **Date time values** -- creation from milliseconds
- **Date time formats** -- creation from strings

# Common Errors

- **Error**: Using month 1 for January in the number constructor
  **Correction**: Months are 0-indexed: `new Date(2077, 0, 27)` for January 27

# Common Confusions

- **Confusion**: All constructors use the same time zone
  **Clarification**: Number constructor uses local time zone; string constructor depends on format; time value constructor uses UTC

# Source Reference

Chapter 47: Dates (Date), Section 47.5, lines 342-416.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with all four methods
- Cross-reference status: verified
