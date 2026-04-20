---
concept: Date Getters and Setters
slug: date-getters-setters
category: standard-library
subcategory: dates
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Dates (Date)"
chapter_number: 47
pdf_page: null
section: "47.6 Getters and setters"
extraction_confidence: high
aliases:
  - Date time unit accessors
prerequisites:
  - date-class
extends: []
related:
  - date-to-string
contrasts_with: []
answers_questions:
  - "How do I work with dates in JavaScript?"
---

# Quick Definition

Date objects provide getter/setter pairs for each time unit (FullYear, Month, Date, Day, Hours, Minutes, Seconds, Milliseconds) in both local time zone (`get/set«Unit»()`) and UTC (`get/setUTC«Unit»()`) variants.

# Core Definition

"Exploring JavaScript" Ch. 47 lists the pattern: `Date.prototype.get«Unit»()` and `Date.prototype.set«Unit»(num)` for local time zone; `Date.prototype.getUTC«Unit»()` and `Date.prototype.setUTC«Unit»(num)` for UTC. Supported units: FullYear, Month (0-11), Date (1-31), Day (getter only, 0-6, 0=Sunday), Hours, Minutes, Seconds, Milliseconds.

# Prerequisites

- **Date class** -- getters/setters are Date instance methods

# Key Properties

1. Local time zone: `getFullYear()`, `setFullYear(num)`, etc.
2. UTC: `getUTCFullYear()`, `setUTCFullYear(num)`, etc.
3. Month: 0-11 (0=January) -- pitfall!
4. Day: 0-6 (0=Sunday) -- getter only, no setter
5. `getTimezoneOffset()`: minutes difference from UTC

# Construction / Recognition

```js
const d = new Date('2122-06-29');
d.getFullYear()       // year in local time
d.getUTCFullYear()    // year in UTC
d.getMonth()          // 0-11 (local)
d.getTimezoneOffset() // minutes from UTC
```

(Ch. 47, Section 47.6.1, lines 420-464)

# Context & Application

Used to extract or modify individual time components. Be mindful of which time zone version to use.

# Examples

```js
> new Date('2122-06-29').getTimezoneOffset()
-120  // CEST = UTC+2
> new Date('2122-12-29').getTimezoneOffset()
-60   // CET = UTC+1
```

(Ch. 47, Section 47.6.1, lines 460-463)

# Relationships

## Builds Upon
- **Date class** -- instance methods

## Related
- **Date to string conversion** -- string methods also have timezone variants

# Common Errors

- **Error**: Expecting `getMonth()` to return 1 for January
  **Correction**: `getMonth()` returns 0 for January, 11 for December

# Common Confusions

- **Confusion**: `getDay()` returns the day of the month
  **Clarification**: `getDay()` returns the day of the WEEK (0-6); `getDate()` returns day of month

# Source Reference

Chapter 47: Dates (Date), Section 47.6, lines 418-464.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit pattern with all units listed
- Cross-reference status: verified
