---
# === CORE IDENTIFICATION ===
concept: HTML and URL Filters
slug: html-url-filters

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
section: "stdlib::filters::html / stdlib::filters::url"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "HTML filters"
  - "URL filters"
  - "escape filters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
  - output-tags
extends:
  - liquid-template-language
related:
  - string-filters
  - date-filter
  - utility-filters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
  - "How does the Liquid Rust crate relate to Ruby Liquid?"
---

# Quick Definition
HTML and URL filters are Liquid template filters provided by the `liquid-lib` standard library for escaping HTML entities, stripping HTML tags, converting newlines to `<br>` tags, and encoding/decoding URLs.

# Core Definition
The Liquid Rust crate's standard library (`liquid-lib`) provides a set of HTML-related and URL-related filters that process string values in Liquid templates. The HTML filters include `escape` (converts special characters to HTML entities), `escape_once` (escapes without double-escaping already-escaped entities), `strip_html` (removes all HTML tags), and `newline_to_br` (converts newline characters to HTML `<br>` tags). The URL filters include `url_encode` (percent-encodes a string for use in URLs) and `url_decode` (decodes a percent-encoded string). These filters are part of the Rust implementation and are functionally equivalent to their Ruby Liquid counterparts (source: liquid-lib rustdoc, `stdlib::filters::html` and `stdlib::filters::url` modules).

# Prerequisites
- Understanding of Liquid template language and filter syntax (see `liquid-template-language`)
- Understanding of output tags for applying filters (see `output-tags`)

# Key Properties
## HTML Filters
1. **`escape`** (struct `Escape`): Converts special HTML characters (`&`, `<`, `>`, `"`, `'`) to their HTML entity equivalents (`&amp;`, `&lt;`, `&gt;`, `&quot;`, `&#39;`).
2. **`escape_once`** (struct `EscapeOnce`): Same as `escape`, but does not re-escape characters that are already escaped. For example, `&amp;` remains `&amp;` instead of becoming `&amp;amp;`.
3. **`strip_html`** (struct `StripHtml`): Removes all HTML tags from a string, leaving only the text content.
4. **`newline_to_br`** (struct `NewlineToBr`): Replaces each newline character (`\n`) with an HTML `<br />` tag.

## URL Filters
5. **`url_encode`** (struct `UrlEncode`): Percent-encodes a string so it can be safely used in a URL. Spaces become `%20`, special characters are encoded.
6. **`url_decode`** (struct `UrlDecode`): Decodes a percent-encoded string back to its original form.

# Construction / Recognition
## To Use:
Apply filters using the pipe (`|`) syntax in Liquid output tags:

```liquid
{{ "<p>Hello & world</p>" | escape }}
<!-- Output: &lt;p&gt;Hello &amp; world&lt;/p&gt; -->

{{ "&lt;p&gt;" | escape_once }}
<!-- Output: &lt;p&gt; (not double-escaped) -->

{{ "<p>Hello</p>" | strip_html }}
<!-- Output: Hello -->

{{ "Hello\nWorld" | newline_to_br }}
<!-- Output: Hello<br />World -->

{{ "hello world" | url_encode }}
<!-- Output: hello%20world -->

{{ "hello%20world" | url_decode }}
<!-- Output: hello world -->
```

# Context & Application
- **Typical contexts**: Displaying user-generated content safely (escape), preparing text for RSS/Atom feeds (strip_html), building URLs with dynamic parameters (url_encode).
- **When to use escape**: When outputting content that may contain HTML special characters to prevent XSS or rendering issues.
- **When to use strip_html**: When you need plain text from HTML content (e.g., for excerpts, meta descriptions).
- **When to use url_encode/url_decode**: When constructing or parsing URLs with dynamic values.

# Examples
**Example 1** (source: liquid-lib rustdoc): Escaping HTML content

```liquid
{{ page.content | escape }}
```

**Example 2** (source: liquid-lib rustdoc): Creating a URL-safe query string

```liquid
<a href="/search?q={{ query | url_encode }}">Search</a>
```

# Relationships
## Builds Upon
- `liquid-template-language`: These are standard Liquid filters.
- `output-tags`: Filters are applied within output tags (`{{ }}`).

## Enables
- Safe HTML output and XSS prevention.
- URL construction with dynamic parameters.

## Related
- `string-filters`: Other string manipulation filters (append, prepend, replace, etc.).
- `date-filter`: Another standard filter for date formatting.
- `utility-filters`: The `default` and `size` filters.

## Contrasts With
- `escape` vs. `escape_once`: `escape` always escapes; `escape_once` avoids double-escaping.

# Common Errors
1. **Double-escaping**: Using `escape` on already-escaped content produces double-escaped entities. Use `escape_once` to avoid this.
2. **Forgetting to escape in non-layout contexts**: Content output directly without `escape` may contain unescaped HTML.

# Common Confusions
1. **`escape` vs. `strip_html`**: `escape` preserves HTML structure as visible text (entities); `strip_html` removes tags entirely.
2. **Rust implementation vs. Ruby Liquid**: These filters are functionally equivalent to Ruby Liquid filters but are implemented as Rust structs in the `liquid-lib` crate. The API is compatible at the template level.

# Source Reference
- liquid-lib rustdoc: `stdlib::filters::html::Escape`, `EscapeOnce`, `StripHtml`, `NewlineToBr`.
- liquid-lib rustdoc: `stdlib::filters::url::UrlEncode`, `UrlDecode`.

# Verification Notes
- Filter names confirmed from the HTML source files in `sources-html/liquid_lib/stdlib/filters/html/` and `sources-html/liquid_lib/stdlib/filters/url/`.
