---
concept: Date Time Formats (ISO)
slug: date-time-formats
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.3 Background: date time formats (ISO)"
extraction_confidence: high
aliases:
  - ISO 8601 date format
  - date string format
prerequisites:
  - date-class
extends: []
related:
  - date-time-values
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

JavaScript uses ISO 8601-based date time formats for parsing and serialization: `YYYY-MM-DDTHH:mm:ss.sssZ` (full format) with optional time zones via `Z` (UTC) or `+HH:mm`/`-HH:mm` offsets. Appending `Z` makes parsing deterministic.

# Core Definition

"Exploring JavaScript" Ch. 47 describes the format structures: date formats (`YYYY-MM-DD`, `YYYY-MM`, `YYYY`), time formats (`THH:mm:ss.sss` with optional `Z`), and combined formats. The tip: "If we add a Z to the end of a string, date parsing doesn't produce different results at different locations."

# Prerequisites

- **Date class** -- formats are used with Date parsing/serialization

# Key Properties

1. `YYYY-MM-DDTHH:mm:ss.sssZ` is the longest/full format
2. `Z` suffix means UTC; its absence means local time zone
3. Date-only strings (`YYYY-MM-DD`) are interpreted as UTC
4. Date-time strings without `Z` use local time zone
5. Time offsets: `+HH:mm` or `-HH:mm` relative to UTC
6. Returned by `.toISOString()`, accepted by `Date.parse()` and `new Date()`

# Construction / Recognition

```js
> new Date('2077-01-27T00:00Z').toISOString()
'2077-01-27T00:00:00.000Z'
> new Date('2077-01-27T00:00').toISOString() // CET (UTC+1)
'2077-01-26T23:00:00.000Z'  // different day!
```

(Ch. 47, Section 47.3.1, lines 263-275)

# Context & Application

ISO date formats are the standard for serializing dates in JSON, APIs, and configuration. Always append `Z` for deterministic parsing.

# Examples

From the source: "Tip: append a Z to make date parsing deterministic."

(Ch. 47, Section 47.3.1, lines 254-275)

# Relationships

## Builds Upon
- **Date class** -- formats are used with Date methods

## Related
- **Date time values** -- parsing converts strings to time values

# Common Errors

- **Error**: Parsing date strings without `Z` and expecting UTC
  **Correction**: Always append `Z` for UTC, or the local time zone is used

# Common Confusions

- **Confusion**: Date-only strings and date-time strings use the same default time zone
  **Clarification**: Date-only strings default to UTC; date-time strings without offset default to local time zone

# Source Reference

Chapter 47: Dates (Date), Section 47.3, lines 198-275.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit format specification with tip
- Cross-reference status: verified
