---
concept: Defer and Async Script Attributes
slug: defer-and-async-scripts
category: browser-apis
subcategory: document-loading
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 431
section: "15.1.1 When scripts run: async and deferred"
extraction_confidence: high
aliases:
  - defer attribute
  - async attribute
  - deferred scripts
prerequisites:
  - script-tag-loading
extends: []
related:
  - dom-tree
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The `defer` and `async` attributes on `<script>` tags control when scripts execute relative to HTML parsing: `defer` runs scripts after the document is fully parsed in document order, while `async` runs scripts as soon as they download, possibly out of order.

# Core Definition

Both `defer` and `async` tell the browser that the linked script does not use `document.write()`, allowing the browser to continue parsing the document while downloading the script. The `defer` attribute causes deferred execution until after the document is fully loaded and parsed. The `async` attribute causes the browser to run the script as soon as possible after download. If both attributes are present, `async` takes precedence (Flanagan, Ch. 15, p. 431).

# Prerequisites

- **script-tag-loading** — Must understand basic script inclusion before controlling load behavior.

# Key Properties

1. Both attributes are boolean (no value needed) and only meaningful with the `src` attribute.
2. Deferred scripts run in document order; async scripts run as they load (potentially out of order).
3. Scripts with `type="module"` are deferred by default.
4. Neither deferred nor async scripts should use `document.write()`.

# Construction / Recognition

```html
<script defer src="deferred.js"></script>
<script async src="async.js"></script>
```

# Context & Application

Use `defer` for scripts that need the full DOM but should not block parsing. Use `async` for independent scripts like analytics that do not depend on DOM order or other scripts.

# Examples

From the source (p. 431): "Note that deferred scripts run in the order in which they appear in the document. Async scripts run as they load, which means that they may execute out of order."

# Relationships

## Builds Upon
- **script-tag-loading** — Extends the basic script loading mechanism

## Enables
- **dom-tree** — Deferred scripts have access to the complete DOM

## Related
- **dom-tree** — Script timing affects DOM availability

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `defer` or `async` on inline scripts (without `src`).
  **Correction**: These attributes are only meaningful when used with the `src` attribute.

# Common Confusions

- **Confusion**: `async` scripts will run in document order.
  **Clarification**: Async scripts execute as soon as they download, regardless of order. Only `defer` preserves document order.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.1.1, pages 430-432.

# Verification Notes

- Definition source: Direct quote and paraphrase
- Confidence rationale: Clear, detailed source explanation
- Uncertainties: None
- Cross-reference status: Verified
