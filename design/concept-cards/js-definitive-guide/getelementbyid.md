---
concept: getElementById
slug: getelementbyid
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 457
section: "15.3.1 Other element selection methods"
extraction_confidence: high
aliases:
  - document.getElementById
prerequisites:
  - dom-tree
extends: []
related:
  - element-selection-queryselector
contrasts_with:
  - element-selection-queryselector
answers_questions:
  - "What distinguishes querySelector() from getElementById()?"
---

# Quick Definition

`document.getElementById()` is an older DOM method that returns the single Element with the specified `id` attribute value, or null if no such element exists.

# Core Definition

`getElementById()` takes an ID string (without the CSS `#` prefix) and returns the matching element. It is defined only on the Document object, not on Element. Along with `getElementsByName()`, `getElementsByTagName()`, and `getElementsByClassName()`, these are older selection methods that are now largely superseded by `querySelector()` and `querySelectorAll()` (Flanagan, Ch. 15, p. 457).

# Prerequisites

- **dom-tree** — Must understand the document structure.

# Key Properties

1. Takes a bare ID string, not a CSS selector (no `#` prefix).
2. Returns a single Element object, not a NodeList.
3. The `getElementsByTagName()` and `getElementsByClassName()` variants return live NodeLists that update when the document changes.
4. Only defined on the Document object.

# Construction / Recognition

```javascript
let sect1 = document.getElementById("sect1");
```

# Context & Application

Still commonly seen in existing codebases. For new code, `querySelector("#id")` is generally preferred for consistency with other CSS-selector-based queries.

# Examples

From the source (p. 457):
```javascript
let sect1 = document.getElementById("sect1");
let headings = document.getElementsByTagName("h1");
let tooltips = document.getElementsByClassName("tooltip");
```

# Relationships

## Builds Upon
- **dom-tree** — Queries the DOM tree

## Enables
- **dom-traversal** — Found elements can be traversed

## Related
- **element-selection-queryselector** — Modern replacement

## Contrasts With
- **element-selection-queryselector** — `querySelector()` accepts any CSS selector; `getElementById()` only accepts an ID string

# Common Errors

- **Error**: Passing `"#myid"` to `getElementById()`.
  **Correction**: Pass just `"myid"` without the hash prefix.

# Common Confusions

- **Confusion**: `getElementsByTagName()` returns a static NodeList like `querySelectorAll()`.
  **Clarification**: The older methods return live NodeLists that change when the document changes.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.1, pages 457-458.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clearly documented with comparisons
- Uncertainties: None
- Cross-reference status: Verified
