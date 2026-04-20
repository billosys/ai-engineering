---
concept: innerHTML vs textContent
slug: innerhtml-vs-textcontent
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 464
section: "15.3.4 Element Content"
extraction_confidence: high
aliases:
  - innerHTML property
  - textContent property
prerequisites:
  - dom-tree
extends: []
related:
  - creating-inserting-deleting-nodes
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

`innerHTML` reads or sets an element's content as an HTML markup string (parsing tags), while `textContent` reads or sets it as plain text (no parsing, safe from XSS).

# Core Definition

The `innerHTML` property of an Element returns the content as a string of markup and, when set, invokes the browser's HTML parser to replace the element's current content. The `textContent` property returns all text in all descendants as plain text and, when set, replaces content with a Text node without parsing HTML. Using `innerHTML` with untrusted input creates cross-site scripting (XSS) vulnerabilities (Flanagan, Ch. 15, pp. 464-465).

# Prerequisites

- **dom-tree** — Must understand element content in the tree.

# Key Properties

1. `innerHTML` triggers HTML parsing; `textContent` does not.
2. Appending to `innerHTML` with `+=` is inefficient (serializes then re-parses).
3. `outerHTML` includes the element's own tags in addition to its content.
4. `insertAdjacentHTML()` inserts HTML at positions relative to an element.
5. `textContent` is defined on the Node class; works on Text nodes too.

# Construction / Recognition

```javascript
let para = document.querySelector("p");
let text = para.textContent;
para.textContent = "Hello World!";
document.body.innerHTML = "<h1>Oops</h1>";
```

# Context & Application

Use `textContent` when working with plain text or when security is a concern. Use `innerHTML` when you need to insert HTML markup from a trusted source.

# Examples

From the source (p. 464-465): Setting `innerHTML` replaces the entire element content with parsed HTML. Setting `textContent` safely inserts plain text without parsing.

# Relationships

## Builds Upon
- **dom-tree** — Reads and writes DOM content

## Enables
- **creating-inserting-deleting-nodes** — Alternative content manipulation approach

## Related
- **creating-inserting-deleting-nodes** — Programmatic node creation as an alternative

## Contrasts With
- (None - this card describes the contrast between the two properties)

# Common Errors

- **Error**: Using `innerHTML` to insert user-provided content.
  **Correction**: Use `textContent` for untrusted input to prevent XSS attacks.

# Common Confusions

- **Confusion**: `innerText` and `textContent` are identical.
  **Clarification**: `innerText` has complex behaviors (attempting to preserve layout) and is not consistently implemented. `textContent` is preferred.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.4, pages 464-465.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Key security-relevant distinction clearly documented
- Uncertainties: None
- Cross-reference status: Verified
