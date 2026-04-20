---
# === CORE IDENTIFICATION ===
concept: HTML
slug: html

# === CLASSIFICATION ===
category: web-platform
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "JavaScript and the Browser"
chapter_number: 13
pdf_page: null
section: "HTML"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - HyperText Markup Language

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - document-object-model
  - css
  - javascript-in-browser
  - html-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the DOM relate to HTML?"
  - "What must I know before working with the DOM?"
---

# Quick Definition
HTML (HyperText Markup Language) is the document format used for web pages, containing text and tags that give structure to the content.

# Core Definition
"*HTML*, which stands for HyperText Markup Language, is the document format used for web pages. An HTML document contains text, as well as *tags* that give structure to the text, describing things such as links, paragraphs, and headings." (Eloquent JavaScript, Ch. 13, lines 197-200)

# Prerequisites
None -- this is a foundational web concept.

# Key Properties
1. Documents have a head (metadata) and body (content)
2. Tags are wrapped in angle brackets: `<p>`, `</p>`
3. Tags can have attributes: `<a href="...">`
4. HTML is parsed in an error-tolerant way by browsers
5. Self-closing tags don't need closing tags (e.g., `<meta>`)
6. Special characters are escaped with entities (`&lt;`, `&amp;`)

# Construction / Recognition
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My home page</title>
  </head>
  <body>
    <h1>My home page</h1>
    <p>Hello, I am Marijn and this is my home page.</p>
    <p>I also wrote a book! Read it
      <a href="http://eloquentjavascript.net">here</a>.</p>
  </body>
</html>
```
(lines 207-220)

# Context & Application
HTML is the foundational format of the web. Every web page is an HTML document that the browser parses, renders, and exposes through the DOM.

# Examples
From the source: "An element, such as the body, a paragraph, or a link, is started by an *opening tag* like `<p>` and ended by a *closing tag* like `</p>`. Some opening tags, such as the one for the link (`<a>`), contain extra information in the form of `name=\"value\"` pairs. These are called *attributes*." (lines 250-254)

"HTML is parsed in a remarkably error-tolerant way. When tags that should be there are missing, the browser automatically adds them." (lines 282-284)

# Relationships
## Builds Upon
- Basic text documents
## Enables
- Web pages, the DOM, browser rendering
## Related
- DOM (the programmatic representation of HTML)
- CSS (styling for HTML)
- JavaScript in the browser
## Contrasts With
- Plain text (no structure)
- XML (stricter parsing rules)

# Common Errors
- **Error**: Forgetting the doctype declaration
  **Correction**: "Browsers will often do ridiculous things when you forget them." (lines 321-322)

# Common Confusions
- **Confusion**: HTML and the DOM are the same thing
  **Clarification**: HTML is the text format; the DOM is the in-memory tree representation that the browser creates from the HTML

# Source Reference
Chapter 13: JavaScript and the Browser, Section "HTML", lines 194-324 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Extensively covered
- Cross-reference status: verified against Ch. 14
