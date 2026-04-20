---
concept: Intl.NumberFormat
slug: intl-numberformat
category: standard-library
subcategory: internationalization
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 327
section: "11.7.1 Formatting Numbers"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - intl-datetimeformat
contrasts_with: []
answers_questions: []
---

# Quick Definition

An internationalization class that formats numbers as locale-appropriate strings, supporting decimal, percentage, and currency styles with control over digits, grouping, and script.

# Core Definition

"The Intl.NumberFormat class defines a format() method that takes all of these formatting possibilities into account" (p. 327). The constructor takes a locale string and an options object with properties like `style` ("decimal", "percent", "currency"), `currency`, `useGrouping`, and digit precision controls. The `format()` method is bound to the instance for convenient use.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Constructor: `Intl.NumberFormat(locale, options)`
2. Styles: "decimal" (default), "percent", "currency"
3. `currency` property required when style is "currency" (e.g., "USD", "EUR")
4. `format()` method is bound to the instance — can be passed directly to `map()`
5. Supports non-Latin digit scripts via locale extensions (e.g., `-u-nu-deva`)

# Construction / Recognition

```js
let euros = Intl.NumberFormat("es", {style: "currency", currency: "EUR"});
euros.format(10)  // => "10,00 €"
let pct = Intl.NumberFormat(undefined, {style: "percent", minimumFractionDigits: 1});
[0.05, .75, 1].map(pct.format)  // => ["5.0%", "75.0%", "100.0%"]
```

# Context & Application

Essential for displaying numbers in user-facing applications that support multiple locales. Handles decimal separators, thousands grouping, currency symbols, and digit scripts automatically.

# Examples

From the source text (p. 328-329): Spanish euros: `Intl.NumberFormat("es", {style: "currency", currency: "EUR"}).format(10)` returns `"10,00 €"`. Arabic digits: `Intl.NumberFormat("ar", {useGrouping: false}).format(1234567890)` returns Arabic numerals.

# Relationships

## Related
- **Intl.DateTimeFormat** — The date/time equivalent in the Intl API

# Common Errors

- **Error**: Forgetting the `currency` option when using `style: "currency"`.
  **Correction**: The `currency` property is required when style is "currency".

# Common Confusions

- **Confusion**: Creating a new Intl.NumberFormat for every format call.
  **Clarification**: Create the formatter once and reuse it. The `format()` method is bound and can be extracted: `const fmt = new Intl.NumberFormat(...).format`.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.7.1, pages 327-329.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
