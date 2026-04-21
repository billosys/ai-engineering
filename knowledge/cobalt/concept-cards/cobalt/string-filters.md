---
# === CORE IDENTIFICATION ===
concept: String Filters
slug: string-filters

# === CLASSIFICATION ===
category: liquid-filters
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "String Filters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "text filters"
  - "string manipulation filters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - output-tags
  - liquid-template-language
extends: []
related:
  - array-filters
  - math-filters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid filter?"
  - "How do I use Liquid template variables in my pages?"
---

# Quick Definition

String filters are Liquid filters that transform text values. They are applied within output tags using the pipe syntax (`{{ value | filter }}`) and include operations for changing case, modifying content, splitting strings, and controlling whitespace.

# Core Definition

String filters are part of the Liquid standard library implemented in the `liquid_lib` crate (source: `stdlib/filters/string/` and `stdlib/filters/html/`). They operate on string values and are applied using the pipe character in output tags. Cobalt's Rust-based Liquid implementation provides a comprehensive set of string manipulation filters that cover case conversion, content modification, whitespace control, HTML processing, and URL encoding. Multiple filters can be chained together: `{{ value | downcase | truncate: 20 }}`. (Source: liquid_lib stdlib filters)

# Prerequisites

- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Understanding the filter pipe syntax.

# Key Properties

The following string filters are available in the liquid_lib standard library:

**Case Conversion:**
1. **`capitalize`**: Capitalizes the first character of the string. `{{ "hello" | capitalize }}` produces `Hello`.
2. **`downcase`**: Converts the entire string to lowercase. `{{ "HELLO" | downcase }}` produces `hello`.
3. **`upcase`**: Converts the entire string to uppercase. `{{ "hello" | upcase }}` produces `HELLO`.

**Content Modification:**
4. **`append`**: Appends a string to the end. `{{ "hello" | append: " world" }}` produces `hello world`.
5. **`prepend`**: Prepends a string to the beginning. `{{ "world" | prepend: "hello " }}` produces `hello world`.
6. **`remove`**: Removes all occurrences of a substring. `{{ "hello world" | remove: "world" }}` produces `hello `.
7. **`remove_first`**: Removes the first occurrence of a substring.
8. **`replace`**: Replaces all occurrences of a substring. `{{ "hello" | replace: "l", "r" }}` produces `herro`.
9. **`replace_first`**: Replaces the first occurrence of a substring.

**Splitting and Truncation:**
10. **`split`**: Splits a string into an array on a delimiter. `{{ "a,b,c" | split: "," }}` produces an array.
11. **`truncate`**: Shortens a string to a specified number of characters, appending an ellipsis by default. `{{ "long text" | truncate: 5 }}` produces `lo...`.
12. **`truncatewords`**: Shortens a string to a specified number of words.

**Whitespace Control:**
13. **`strip`**: Removes whitespace from both sides of a string.
14. **`lstrip`**: Removes whitespace from the left (beginning) of a string.
15. **`rstrip`**: Removes whitespace from the right (end) of a string.
16. **`strip_newlines`**: Removes all newline characters from a string.

**HTML Filters:**
17. **`escape`**: Escapes HTML special characters (`<`, `>`, `&`, `"`).
18. **`escape_once`**: Escapes HTML but does not double-escape already-escaped entities.
19. **`newline_to_br`**: Converts newline characters to HTML `<br>` tags.
20. **`strip_html`**: Removes all HTML tags from a string.

**URL Filters:**
21. **`url_encode`**: Encodes a string for use in a URL.
22. **`url_decode`**: Decodes a URL-encoded string.

**Other:**
23. **`date`**: Formats a date/time value.
24. **`size`**: Returns the length of a string (or array).
25. **`default`**: Returns a default value if the input is nil, false, or empty.

# Construction / Recognition

## To Construct/Create:
1. Place a filter after a value using the pipe: `{{ value | filter_name }}`.
2. For filters with parameters, use colon syntax: `{{ value | filter_name: parameter }}`.
3. Chain multiple filters: `{{ value | filter1 | filter2 }}`.

## To Identify/Recognize:
1. Look for pipe characters (`|`) followed by filter names in output tags.
2. String filters typically operate on text values.

# Context & Application

- **Typical contexts**: Formatting text for display, preparing strings for URLs, cleaning HTML output, controlling whitespace.
- **Common applications**: Lowercasing slugs, truncating excerpts, escaping user content, formatting dates, building URLs.

# Examples

**Example 1** (source: Liquid Standard Library): Chaining filters:
```liquid
{{ page.title | downcase | replace: " ", "-" }}
```
Converts "My Blog Post" to `my-blog-post`.

**Example 2** (source: Liquid Standard Library): Truncating with custom ending:
```liquid
{{ page.description | truncate: 100, "..." }}
```

# Relationships

## Builds Upon
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Filter pipe syntax.

## Enables
- Text formatting and manipulation in templates.

## Related
- **[Array Filters](/concept-cards/cobalt/array-filters.md)** -- Filters for array operations.
- **[Math Filters](/concept-cards/cobalt/math-filters.md)** -- Filters for numeric operations.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using a filter that expects a string on a non-string value.
  **Correction**: Ensure the input value is a string, or use type-appropriate filters.

# Common Confusions

- **Confusion**: Not knowing the difference between `escape` and `escape_once`.
  **Clarification**: `escape` always escapes HTML characters. `escape_once` checks if characters are already escaped and avoids double-escaping (e.g., `&amp;` won't become `&amp;amp;`).

# Source Reference

Liquid Standard Library, string/html/url filter modules. Source: liquid_lib rustdoc (stdlib/filters/).

# Verification Notes

- Definition source: liquid_lib stdlib filter structs
- Confidence rationale: All filters verified in the liquid_lib stdlib struct list.
- Uncertainties: None for filter names; specific parameter details may vary.
- Cross-reference status: Verified against liquid_lib stdlib index listing all structs.
