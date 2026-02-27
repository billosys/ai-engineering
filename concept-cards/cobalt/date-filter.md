---
# === CORE IDENTIFICATION ===
concept: Date Filter
slug: date-filter

# === CLASSIFICATION ===
category: liquid-filters
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid API Reference"
chapter_number: null
pdf_page: null
section: "stdlib::filters::date"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "date formatting filter"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
  - output-tags
extends:
  - liquid-template-language
related:
  - string-filters
  - html-url-filters
  - utility-filters
  - page-variable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
---

# Quick Definition
The `date` filter formats a date value into a string representation using a strftime-compatible format string, implemented as the `Date` struct in the `liquid-lib` standard library.

# Core Definition
The `date` filter in Liquid Rust formats date values using strftime-style format strings. It takes a date value (from post metadata like `published_date`, or from the special string `"now"` / `"today"`) and a format string parameter. The filter is implemented as the `Date` struct in the `liquid-lib` crate's `stdlib::filters::date` module. This is functionally equivalent to the Ruby Liquid `date` filter, using the same strftime format directives (source: liquid-lib rustdoc, `stdlib::filters::date::Date`).

# Prerequisites
- Understanding of Liquid template language and filter syntax (see `liquid-template-language`)
- Understanding of output tags (see `output-tags`)
- Familiarity with strftime format strings

# Key Properties
1. **Format string parameter**: The filter takes a strftime-compatible format string as its argument.
2. **Common format directives**:
   - `%Y`: 4-digit year (e.g., 2024)
   - `%m`: 2-digit month (01-12)
   - `%d`: 2-digit day (01-31)
   - `%H`: 24-hour hour (00-23)
   - `%M`: Minute (00-59)
   - `%S`: Second (00-59)
   - `%B`: Full month name (e.g., January)
   - `%b`: Abbreviated month name (e.g., Jan)
   - `%A`: Full weekday name (e.g., Monday)
   - `%a`: Abbreviated weekday name (e.g., Mon)
3. **Special input values**: The strings `"now"` and `"today"` can be used as input to get the current date/time.
4. **Rust implementation**: Implemented as `struct Date` in `liquid_lib::stdlib::filters::date`.

# Construction / Recognition
## To Use:
```liquid
{{ page.published_date | date: "%Y-%m-%d" }}
<!-- Output: 2024-01-15 -->

{{ page.published_date | date: "%B %d, %Y" }}
<!-- Output: January 15, 2024 -->

{{ "now" | date: "%Y-%m-%d %H:%M" }}
<!-- Output: current date and time -->
```

# Context & Application
- **Typical contexts**: Displaying post publication dates, formatting dates in archives, generating date-based metadata in RSS feeds.
- **When to use**: Any time you need to display or format a date value in a template.
- **Scope**: Works on any value that can be interpreted as a date.

# Examples
**Example 1** (source: liquid-lib rustdoc): Formatting a post date

```liquid
<time datetime="{{ page.published_date | date: '%Y-%m-%d' }}">
  {{ page.published_date | date: "%B %d, %Y" }}
</time>
```

**Example 2** (source: liquid-lib rustdoc): Using "now" for current date

```liquid
<p>Page generated on {{ "now" | date: "%Y-%m-%d" }}</p>
```

# Relationships
## Builds Upon
- `liquid-template-language`: The date filter is part of the standard Liquid filter set.
- `output-tags`: Used within output tag expressions.

## Enables
- Formatted date display in templates.
- Localized or custom date formats for different parts of the site.

## Related
- `page-variable`: Post/page variables like `published_date` are common inputs to the date filter.
- `string-filters`: Other string transformation filters.
- `html-url-filters`: Other standard filters.

## Contrasts With
- Unlike string filters that manipulate arbitrary text, the date filter specifically processes date/time values.

# Common Errors
1. **Invalid format directives**: Using format codes not supported by strftime will produce unexpected output.
2. **Non-date input**: Passing a non-date value to the date filter may cause an error or produce meaningless output.

# Common Confusions
1. **Rust vs. Ruby strftime**: The Rust date filter uses chrono's strftime implementation, which is very similar but may have minor differences from Ruby's strftime in edge cases.
2. **"now" string**: The special string `"now"` refers to the build time, not the viewer's current time.

# Source Reference
- liquid-lib rustdoc: `stdlib::filters::date::Date`.

# Verification Notes
- Filter existence confirmed from `sources-html/liquid_lib/stdlib/filters/date/struct.Date.html`. Strftime behavior is standard for the Rust Liquid implementation.
