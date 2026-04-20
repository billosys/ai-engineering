---
concept: URL Class
slug: url-class
category: standard-library
subcategory: web-apis
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 337
section: "11.9 URL APIs"
extraction_confidence: high
aliases:
  - "URL API"
  - "URLSearchParams"
prerequisites: []
extends: []
related:
  - import-meta-url
contrasts_with: []
answers_questions: []
---

# Quick Definition

A class for parsing, constructing, and manipulating URLs with proper escaping, providing read/write access to protocol, host, port, pathname, search, and hash components, plus `URLSearchParams` for query parameter management.

# Core Definition

"The URL class parses URLs and also allows modification of existing URLs. It also properly handles the complicated topic of escaping and unescaping the various components of a URL" (p. 337). Properties include `href`, `origin`, `protocol`, `host`, `hostname`, `port`, `pathname`, `search`, `hash`, `username`, `password`. The `searchParams` property provides a `URLSearchParams` object for managing query parameters.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Constructor: `new URL(urlString)` or `new URL(relative, base)`
2. Read/write properties for each URL component
3. `origin` is read-only (combination of protocol and host)
4. Automatic escaping of special characters when setting components
5. `searchParams` — a URLSearchParams for query parameter management
6. `href` property and `toString()` return the full URL string

# Construction / Recognition

```js
let url = new URL("https://example.com:8000/path/name?q=term#fragment");
url.pathname = "api/search";
url.searchParams.append("q", "test");
url.toString()  // => "https://example.com:8000/api/search?q=test"
```

# Context & Application

The correct way to parse and construct URLs in JavaScript. Replaces legacy `encodeURI()`/`encodeURIComponent()` functions for proper URL handling.

# Examples

From the source text (p. 337-340): Parsing: `url.protocol` returns `"https:"`, `url.hostname` returns `"example.com"`. Auto-escaping: setting `url.pathname = "path with spaces"` produces `/path%20with%20spaces`. URLSearchParams: `url.searchParams.append("q", "term")` properly encodes parameters.

# Relationships

## Related
- **import.meta.url** — Commonly used with URL constructor for relative path resolution

# Common Errors

- **Error**: Using `encodeURIComponent()` for all URL escaping.
  **Correction**: Use the URL class instead — it handles escaping correctly for each component automatically.

# Common Confusions

- **Confusion**: Expecting `searchParams` to be a plain string.
  **Clarification**: `searchParams` is a `URLSearchParams` object with methods like `get()`, `set()`, `append()`, `delete()`, and `sort()`. Use `search` for the raw query string.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.9, pages 337-340.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
