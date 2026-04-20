---
concept: Time Values
slug: date-time-values
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.4 Time values"
extraction_confidence: high
aliases:
  - Unix timestamp milliseconds
  - epoch milliseconds
prerequisites:
  - date-class
extends: []
related:
  - date-creation
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

A time value is the number of milliseconds since 1 January 1970 00:00:00 UTC (Unix epoch), which is how Dates are internally stored and can be used for creation, comparison, and arithmetic.

# Core Definition

"Exploring JavaScript" Ch. 47: "A time value represents a date via the number of milliseconds since 1 January 1970 00:00:00 UTC." Time values can create Dates (`new Date(timeValue)`), and coercing a Date to a number returns its time value. Methods include `Date.now()`, `Date.parse()`, and `Date.UTC()`.

# Prerequisites

- **Date class** -- time values are the internal representation

# Key Properties

1. Milliseconds since Unix epoch (1970-01-01T00:00:00Z)
2. `Date.now()` returns current time value
3. `Number(date)` returns the time value of a Date
4. Dates can be compared with ordering operators (coerced to numbers)
5. `Date.UTC()` creates time values from components in UTC

# Construction / Recognition

```js
const timeValue = 0;
assert.equal(new Date(timeValue).toISOString(), '1970-01-01T00:00:00.000Z');
assert.equal(Number(new Date(123)), 123);
assert.equal(new Date('1972-05-03') < new Date('2001-12-23'), true);
```

(Ch. 47, Section 47.4, lines 277-312)

# Context & Application

Time values are useful for date arithmetic, comparison, and interop with APIs that use Unix timestamps.

# Examples

From the source:
```js
> Number(new Date(123))
123
```

(Ch. 47, Section 47.4, lines 298-299)

# Relationships

## Builds Upon
- **Date class** -- internal representation of Date objects

## Related
- **Date creation** -- time values are one way to create Dates

# Common Errors

- **Error**: Confusing seconds and milliseconds
  **Correction**: JavaScript uses milliseconds; Unix timestamps in seconds must be multiplied by 1000

# Common Confusions

- **Confusion**: Time values include time zone information
  **Clarification**: Time values are always in UTC; time zone is only relevant for display

# Source Reference

Chapter 47: Dates (Date), Section 47.4, lines 277-331.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition
- Cross-reference status: verified
