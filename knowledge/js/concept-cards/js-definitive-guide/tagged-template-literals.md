---
concept: Tagged Template Literals
slug: tagged-template-literals
category: metaprogramming
subcategory: template-tags
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Metaprogramming"
chapter_number: 14
pdf_page: 412
section: "14.5 Template Tags"
extraction_confidence: high
aliases:
  - "template tag functions"
  - "tagged templates"
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions: []
---

# Quick Definition

A metaprogramming feature where a function (tag) is invoked with a template literal, receiving an array of string parts and the interpolated values as separate arguments, enabling custom DSLs and HTML escaping.

# Core Definition

"When an expression whose value is a function is followed by a template literal, it turns into a function invocation, and we call it a 'tagged template literal'" (p. 412). The tag function receives the string parts as an array (first argument) and interpolated values as additional arguments. The array also has a `raw` property with unescaped strings.

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond template literal syntax.

# Key Properties

1. Tag function receives `(strings, ...values)` where strings.length === values.length + 1
2. The return value can be any type (not just strings)
3. `strings.raw` provides un-escaped versions (backslashes not interpreted)
4. Enables DSLs (GraphQL `gql\`\``, CSS-in-JS `css\`\``, etc.)
5. `String.raw` is a built-in tag function

# Construction / Recognition

```js
function html(strings, ...values) {
    let escaped = values.map(v => String(v)
        .replace("&", "&amp;").replace("<", "&lt;"));
    let result = strings[0];
    for(let i = 0; i < escaped.length; i++) {
        result += escaped[i] + strings[i+1];
    }
    return result;
}
html`<b>x ${operator} y</b>`  // => "<b>x &lt; y</b>"
```

# Context & Application

Used to create domain-specific languages embedded in JavaScript. Popular in GraphQL (`gql`), styled-components (`css`), and HTML sanitization.

# Examples

From the source text (p. 413-414): `html` tag that escapes HTML special characters in interpolated values. `glob` tag that creates Glob pattern objects from template literals.

# Relationships

This is a standalone metaprogramming technique.

# Common Errors

- **Error**: Expecting tagged template return value to always be a string.
  **Correction**: Tag functions can return any value — objects, parsed ASTs, etc.

# Common Confusions

- **Confusion**: Thinking tagged templates are just string formatting.
  **Clarification**: Tagged templates are function calls in disguise. The tag function has full control over the return value, which need not be a string at all.

# Source Reference

Chapter 14: Metaprogramming, Section 14.5, pages 412-414.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
