---
concept: Intl.DateTimeFormat
slug: intl-datetimeformat
category: standard-library
subcategory: internationalization
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 329
section: "11.7.2 Formatting Dates and Times"
extraction_confidence: high
aliases: []
prerequisites:
  - date-object
extends: []
related:
  - intl-numberformat
contrasts_with: []
answers_questions: []
---

# Quick Definition

An internationalization class for locale-aware date and time formatting with fine-grained control over which fields are displayed and how they are presented.

# Core Definition

"The Intl.DateTimeFormat class is a lot like the Intl.NumberFormat class" (p. 329). It provides a `format()` method that converts Date objects to locale-appropriate strings. The options object controls which fields appear (year, month, day, weekday, hour, minute, second) and how (numeric, 2-digit, long, short, narrow). Supports non-Gregorian calendars via locale extensions.

# Prerequisites

- **date-object** — DateTimeFormat formats Date objects

# Key Properties

1. Constructor: `Intl.DateTimeFormat(locale, options)`
2. Options for each field: year, month, day, weekday, hour, minute, second
3. Month options: "numeric", "2-digit", "long", "short", "narrow"
4. timeZone option supports IANA time zone names
5. Non-Gregorian calendars via locale extension `-u-ca-` (buddhist, hebrew, islamic, etc.)

# Construction / Recognition

```js
let opts = { weekday: "long", month: "long", year: "numeric", day: "numeric" };
Intl.DateTimeFormat("en-US", opts).format(d)  // "Thursday, January 2, 2020"
Intl.DateTimeFormat("es-ES", opts).format(d)  // "jueves, 2 de enero de 2020"
```

# Context & Application

The recommended way to format dates for user display, replacing the limited built-in `toLocaleDateString()` and `toLocaleTimeString()` methods.

# Examples

From the source text (p. 330-332): Basic: `Intl.DateTimeFormat("en-US").format(d)` returns `"1/2/2020"`. With time zone: `Intl.DateTimeFormat("fr-CA", {hour: "numeric", minute: "2-digit", timeZone: "America/New_York"}).format(d)` returns `"8 h 14"`. Non-Gregorian: `Intl.DateTimeFormat("en-u-ca-hebrew", {year:"numeric", era:"short"}).format(d)` returns `"5780 AM"`.

# Relationships

## Builds Upon
- **Date Object** — Formats Date objects

## Related
- **Intl.NumberFormat** — The number equivalent in the Intl API

# Common Errors

- **Error**: Specifying hours and seconds but omitting minutes and expecting them to be hidden.
  **Correction**: The formatter finds the closest available format — it will typically include minutes even if not explicitly requested.

# Common Confusions

- **Confusion**: Expecting the formatter to always produce exactly the requested fields.
  **Clarification**: The options specify desired fields, but the formatter chooses the closest locale-appropriate format, which may include additional fields.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.7.2, pages 329-332.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
