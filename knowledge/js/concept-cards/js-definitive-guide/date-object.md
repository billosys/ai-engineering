---
concept: Date Object
slug: date-object
category: standard-library
subcategory: dates-and-times
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 317
section: "11.4 Dates and Times"
extraction_confidence: high
aliases:
  - "Date class"
prerequisites: []
extends: []
related:
  - intl-datetimeformat
contrasts_with: []
answers_questions: []
---

# Quick Definition

JavaScript's built-in class for representing and manipulating dates and times, internally stored as millisecond timestamps since January 1, 1970 UTC.

# Core Definition

The Date class represents dates and times as millisecond timestamps since the Unix epoch. Dates can be created with no arguments (current time), a timestamp number, individual components (year, month, day, hour, minute, second, ms), or a date string. "One quirk of the Date API is that the first month of a year is number 0, but the first day of a month is number 1" (p. 317).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Internal representation: milliseconds since January 1, 1970 UTC
2. Month is 0-indexed (0=January, 11=December)
3. Day-of-month is 1-indexed
4. `Date.now()` returns current timestamp
5. Get/set methods for each component (local and UTC variants)
6. `getTime()` returns the timestamp; dates can be compared with `<`, `>`, subtracted

# Construction / Recognition

```js
let now = new Date();
let epoch = new Date(0);
let century = new Date(2100, 0, 1, 2, 3, 4, 5);  // Jan 1 2100
let iso = new Date("2100-01-01T00:00:00Z");
```

# Context & Application

Used for all date/time operations. For locale-aware formatting, use `Intl.DateTimeFormat`. For high-precision timing, use `performance.now()`.

# Examples

From the source text (p. 317-321): `Date.now()` for timestamps. `Date.UTC(2100, 0, 1)` for UTC dates. Date arithmetic: `d.setTime(d.getTime() + 30000)` adds 30 seconds. Formatting: `d.toISOString()` returns `"2020-01-02T01:10:30.000Z"`.

# Relationships

## Enables
- **Intl.DateTimeFormat** — Locale-aware date formatting

# Common Errors

- **Error**: Using month 1 for January.
  **Correction**: Months are 0-indexed. January is 0, December is 11.

# Common Confusions

- **Confusion**: Using `getDay()` to get the day of the month.
  **Clarification**: `getDay()` returns the day of the week (0-6). Use `getDate()` for the day of the month.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.4, pages 317-321.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
