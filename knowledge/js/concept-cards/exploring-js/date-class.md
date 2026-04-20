---
concept: Date Class
slug: date-class
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
extraction_confidence: high
aliases:
  - JavaScript Date
  - Date object
prerequisites: []
extends: []
related:
  - date-time-values
  - date-creation
  - date-time-formats
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

The `Date` class is JavaScript's built-in API for working with dates and times, but it is "cumbersome to use" and best avoided in favor of libraries like Luxon, Day.js, or the upcoming Temporal API.

# Core Definition

"Exploring JavaScript" Ch. 47: "The JavaScript Date API is cumbersome to use. Hence, it's best to rely on a library for anything related to dates." The chapter recommends the upcoming Temporal API, the Intl API for formatting, and libraries like Luxon, Day.js, js-joda, and date-fns. Important considerations include tree-shaking support and time zone support.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Built-in JavaScript class for date/time operations
2. Author explicitly recommends avoiding it in favor of libraries
3. Internally stores dates as UTC milliseconds since Unix epoch
4. Does not support time zones (only local time zone and UTC)
5. Temporal API is the upcoming replacement
6. Month numbers are 0-indexed (0 = January) -- a common pitfall

# Construction / Recognition

```js
const d = new Date();              // current date
const d = new Date(2077, 0, 27);   // Jan 27, 2077 (local time)
const d = new Date('2077-01-27');  // Jan 27, 2077 (UTC)
const d = new Date(0);             // Unix epoch
```

(Ch. 47, Section 47.5, lines 342-416)

# Context & Application

Despite recommendations to use libraries, understanding the built-in Date is necessary for legacy code and when libraries are unavailable. The Intl API provides useful date formatting.

# Examples

```js
> new Date(2077, 0, 27).toISOString()  // CET (UTC+1)
'2077-01-26T23:00:00.000Z'  // note: day differs due to timezone
```

(Ch. 47, Section 47.5.1, lines 366-369)

# Relationships

## Enables
- **Date time values** -- internal representation of dates
- **Date creation** -- various ways to create dates
- **Date time formats** -- ISO format for dates

# Common Errors

- **Error**: Using month 1 for January
  **Correction**: Months are 0-indexed: 0 = January, 11 = December

- **Error**: Mixing time zones when parsing and formatting
  **Correction**: Be explicit about UTC vs local time; append 'Z' for UTC

# Common Confusions

- **Confusion**: `new Date()` with a string and `new Date()` with numbers use the same time zone
  **Clarification**: Date-only strings are parsed as UTC; numbers use the local time zone

# Source Reference

Chapter 47: Dates (Date), Section 47.1, lines 55-97.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit recommendation with alternatives
- Cross-reference status: verified
